This protocol implements a tranche-based lending system where capital moves across multiple contracts (TranchePool, LoanEngine) and multiple lifecycle states (deposit, deployment, repayment, default, write-off, recovery).

Unit tests validate individual functions, but they cannot guarantee global correctness under arbitrary sequencing.

Invariant testing is used to define and enforce the fundamental conservation laws of the system and to verify that they hold under adversarial, stateful fuzzing.

## 🧠 System Model & Handler Design

Invariant tests are driven by a system-level handler that interacts with the real production contracts, not mocks.

The handler models:
- Liquidity providers depositing into senior, junior, and equity tranches
- Administrative lifecycle transitions (commit, activation)
- Borrower flows through LoanEngine:
    - loan creation
    - activation (capital deployment)
    - repayment
    - default
    - write-off
    - recovery

The handler enforces only minimal preconditions required by the protocol (e.g., valid pool state, sufficient liquidity) and otherwise allows arbitrary sequencing of actions.

This design ensures that invariants are tested against realistic and adversarial execution paths, rather than curated happy flows.
    
## Invariant 1 — Outstanding Principal Matches Deployed Capital (Ghost State)

The total outstanding principal recorded by the LoanEngine must always match the total deployed value tracked by the TranchePool.

**Ensures:**
- Loan creation and activation correctly move capital from idle to deployed.
- Repayments reduce both the loan's outstanding principal and the pool's deployed value simultaneously.
- Write-offs (losses) reduce both values in sync.
- Recoveries only affect idle capital and do not resurrect deployed value.

### State transition reasoning

At any point in time, all principal capital must exist in exactly one of two states:
1. Idle capital held by the TranchePool
2. Deployed capital backing active loans

When a loan is activated, principal is transferred from idle capital to deployed capital, and the LoanEngine records the same amount as outstanding principal.

When a borrower repays principal, the outstanding principal is reduced and the same amount is returned to idle capital, reducing deployed value.

When a loss is realized, both the loan’s outstanding principal and the pool’s deployed value are reduced by the same amount.

Recoveries do not increase deployed capital or outstanding principal; they only increase idle capital.

Therefore, outstanding principal in the LoanEngine must always equal the deployed value tracked by the TranchePool.

**Bugs ruled out:**
- "Ghost" principal remaining after repayment.
- Deployed capital drift (pool thinking money is deployed when it's actually repaid).
- Loss accounting mismatches where a writedown clears the loan but leaves the pool believing capital is still deployed.

```solidity
function invariant__OutStandingPrincipalMatchesDeployed() public view {
    assertEq(
        handler.outStandingPrincipal(),
        tranchePool.getTotalDeployedValue(),
        "Outstanding principal does not match deployed minus recovered and loss"
    );
}
```

## Invariant 2 — Capital Location Correctness (Ghost vs Accounting)

All principal capital must always be either idle or deployed.

This invariant enforces the conservation of principal assets:
`Idle + Deployed = Deposited - Loss + Recovered`

**Ensures:**
- Capital transitions (idle ↔ deployed) occur exactly once.
- Losses decrease the total capital in the system.
- Recoveries restore capital to the idle state.
- The system remains consistent even under full capital deployment.

### State transition reasoning

The total capital in the system is defined as the net deposits (`Deposited` - `Loss` + `Recovered`). This capital must physically exist in one of two states:
1. **Idle**: Held as liquid ERC20 tokens in the TranchePool.
2. **Deployed**: Outstanding as principal in active loans.

When capital is deposited, it increases `Deposited` and `Idle` equally.
When a loan is activated, `Idle` decreases and `Deployed` increases by the same amount.
When a loan is repaid, `Deployed` decreases and `Idle` increases.
When a loss occurs (write-off), both `Deployed` and total capital (`Loss` increases) decrease.
When recovery happens, `Recovered` increases (boosting total capital) and `Idle` increases.

Thus, the sum of `Idle` + `Deployed` must always equal `Deposited` - `Loss` + `Recovered`.

**Bugs ruled out:**
- Capital disappearing during deployment (leaky bucket).
- Deployed value not reduced on write-off.
- Recovery inflating deployed balances instead of idle.

```solidity
function invariant__totalIdleAndDeployedValueMatchesAccounting()
    public
    view
{
    assertEq(
        tranchePool.getTotalIdleValue() +
            tranchePool.getTotalDeployedValue(),
        tranchePool.getTotalDeposited() -
            tranchePool.getTotalLoss() +
            tranchePool.getTotalRecovered(),
        "Total idle and deployed value does not match handler accounting"
    );
}
```

## Invariant 3 — Protocol Solvency (System Level)

**Backing Assets Match Obligations**

Tokens actually held by the contract must strictly equal the sum of:
1. Idle Capital (waiting to be deployed)
2. Unclaimed Interest (owed to LPs)
3. Protocol Revenue (owed to protocol)

This is a **Hard Solvency Check**. If `TokenBalance < Obligations`, the protocol is insolvent.

```solidity
function invariant__totalUnclaimedInterestAndIdleValueMatchesTotalTokenBalance() public view {
    assertEq(
        tranchePool.getTotalUnclaimedInterest() + tranchePool.getTotalIdleValue() + tranchePool.getProtocolRevenue(),
        ERC20Mock(usdt).balanceOf(address(tranchePool)),
        "Total unclaimed interest does not match deployed minus recovered and loss"
    );
}
```

## Invariant 4 — Tranche Integrity (System Level)

**The Whole Equals the Sum of Parts**

The Total Deployed Value tracked by the pool must equal the sum of deployed capital allocated to Senior, Junior, and Equity tranches.

`TotalDeployed == SeniorDeployed + JuniorDeployed + EquityDeployed`

**Ensures:**
- No capital is "lost" between the global counter and the individual tranche counters.
- Waterfalls correctly update both global and tranche-specific state.

```solidity
function invariant__totalDeployedValueMatchesSumOfIndividualTranches() public view {
    assertEq(
        tranchePool.getTotalDeployedValue(),
        tranchePool.getSeniorTrancheDeployedValue() +
            tranchePool.getJuniorTrancheDeployedValue() +
            tranchePool.getEquityTrancheDeployedValue(),
        "Total deployed value does not match sum of individual tranches"
    );
}
```

## Invariant 5 — Loan Principal Integrity (System Level)

**Loan Engine State Matches Pool State**

The Total Deployed Value in the Tranche Pool must strictly equal the sum of `principalOutstanding` across all active loans in the Loan Engine.

*Difference from Invariant 1*: This iterates over **actual contract storage** (all loans), whereas Invariant 1 compares against the Handler's "Ghost" tracking. This verifies that the Protocol itself is internally consistent, even if the Handler is wrong.

```solidity
function invariant__systemLevel_PrincipalIntegrity() public view {
    uint256 totalOutstandingPrincipal = 0;
    uint256 nextId = loanEngine.getNextLoanId();
    for (uint256 i = 1; i < nextId; i++) {
        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(i);
        totalOutstandingPrincipal += loan.principalOutstanding;
    }

    assertEq(
        totalOutstandingPrincipal,
        tranchePool.getTotalDeployedValue(),
        "System Level Invariant Failed: Sum of Loan Principals != Pool Deployed Value"
    );
}
```

## Invariant 6 — Exhaustion Safety

All invariants must hold even when idle liquidity reaches zero.

The test harness explicitly allows full capital deployment and then exercises:
	•	repayments
	•	defaults
	•	write-offs
	•	recoveries

This ensures that edge cases involving zero liquidity do not break accounting or state transitions.

**Bugs ruled out:**
	•	Underflows at zero idle
	•	Incorrect recovery handling after full deployment
	•	Last-loan edge case failures

    ```solidity
    bool allowFullDeployment = true;
    ```

    All invariants hold regardless of deployment levels—even when liquidity is fully deployed, the system maintains correctness across all state transitions.

Assumptions & Scope

The invariant tests make the following assumptions:
	•	Token transfers succeed (standard ERC20 behavior)
	•	Unsolicited ERC20 transfers to the pool contract are considered out-of-scope donations and are not reflected in 
        internal accounting.
	•	Credit policy configuration is correct and frozen before loan creation
	•	External price or oracle risk is out of scope

