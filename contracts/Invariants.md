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

## Invariant 1 — Global Value Conservation

The ERC20 token balance held by the pool must match the protocol’s internal accounting for all protocol-mediated state transitions.


**Ensures:**
- No value is created or destroyed
- Fees, recoveries, and repayments are properly accounted for
- There are no silent mint or burn paths

**Bugs ruled out:**
- Missing balance updates
- Double-counted fees
- Partial state updates during capital movement
- Reentrancy-related accounting mismatches

```solidity
function invariant__poolAccountingMatchesTokenBalance() public view {
        uint256 poolBalance = usdt.balanceOf(address(tranchePool));

        uint256 internalAccounting = tranchePool.getTotalIdleValue() +
            tranchePool.getTotalDeployedValue() +
            tranchePool.getProtocolRevenue();

        assertEq(poolBalance, internalAccounting);
    }
```

## Invariant 2 — Capital Location Correctness

All capital must always be either idle or deployed.

This invariant enforces:
idle + deployed = deposited − loss + recovered
**It guarantees that:**
	•	Capital transitions (idle ↔ deployed) occur exactly once
	•	Losses and recoveries are reflected in the correct location
	•	The system remains consistent even under full capital deployment

**Bugs ruled out:**
	•	Capital disappearing during deployment
	•	Deployed value not reduced on write-off
	•	Recovery inflating deployed balances
```solidity
function invariant__totalIdleAndDeployedValueMatchesAccounting()
        public
        view
    {
        assertEq(
            tranchePool.getTotalIdleValue() +
                tranchePool.getTotalDeployedValue(),
            tranchePool.getTotalDeposited() +
                tranchePool.getTotalLoss() -
                tranchePool.getTotalRecovered(),
            "Total idle and deployed value does not match handler accounting"
        );
    }
```

## Invariant 3 — Loan Ledger and Pool Ledger Consistency

The sum of outstanding principal across all active loans must equal the pool’s total deployed capital.

This invariant cross-checks:
	•	LoanEngine’s internal loan ledger
	•	TranchePool’s deployed capital accounting

**It ensures that:**
	•	Loan activation deploys capital exactly once
	•	Repayments reduce both outstanding principal and deployed capital
	•	Defaults and write-offs do not leave phantom deployed value

**Bugs ruled out:**
	•	Double deployment on activation
	•	Partial repayment mismatches
	•	Deployed capital drifting from loan state

```solidity

function invariant__OutStandingPrincipalMatchesDeployed() public view {
        assertEq(
            handler.outStandingPrincipal(),
            tranchePool.getTotalDeployedValue(),
            "Outstanding principal does not match deployed minus recovered and loss"
        );
    }

```
## Invariant 4 — Exhaustion Safety

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

