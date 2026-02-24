# Invariants

This protocol implements a tranche-based lending system where capital moves across multiple contracts (`TranchePool`, `LoanEngine`) and multiple lifecycle states (deposit, deployment, repayment, default, write-off, recovery).

Unit tests validate individual functions, but they cannot guarantee global correctness under arbitrary sequencing. Invariant testing defines and enforces the fundamental conservation laws of the system, verifying they hold under adversarial, stateful fuzzing.

---

## Fuzzing Infrastructure

Invariants are tested across four frameworks:

| Framework | File | Strategy |
|---|---|---|
| Foundry Invariant | `test/fuzz/invariant/CreditRailStateFullFuzzTest.t.sol` | Stateful handler with ghost accounting |
| Foundry Handler | `test/fuzz/invariant/Handler.t.sol` | Drives all state transitions |
| Echidna | `test/fuzz/echidna/EchidnaTest.sol` | Property-based corpus fuzzing |
| Medusa | `test/medusa/MedusaTest.sol` | Coverage-guided stateful fuzzing |

The handler interacts with real production contracts (not mocks) and maintains ghost variables that mirror the expected state for cross-referencing.

---

## Invariant 1 — Outstanding Principal Matches Deployed Capital

The total outstanding principal in `LoanEngine` must always equal the total deployed capital in `TranchePool`.

**Conservation rule:**
```
LoanEngine.sumOf(principalOutstanding) == TranchePool.totalDeployedValue
```

**Reasoning:** At every state transition, both sides must update simultaneously. Activation moves principal from pool idle → deployed and sets loan outstanding. Repayment reduces both. Write-off reduces both. Recovery does neither (it restores idle, not deployed).

**Bugs it catches:** Ghost principal after repayment. Deployed capital drift after write-off. Activation recording principal without pool allocation.

```solidity
function invariant__OutStandingPrincipalMatchesDeployed() public view {
    assertEq(
        handler.outStandingPrincipal(),
        tranchePool.getTotalDeployedValue()
    );
}
```

---

## Invariant 2 — Capital Location Correctness

All principal capital must be in exactly one of two states: idle or deployed.

**Conservation rule:**
```
Idle + Deployed = TotalDeposited - TotalLoss + TotalRecovered
```

**Reasoning:** Deposits increase both `TotalDeposited` and `Idle`. Activation moves `Idle → Deployed`. Repayment moves `Deployed → Idle`. Write-offs reduce `Deployed` and increase `TotalLoss`. Recoveries increase `TotalRecovered` and `Idle`.

**Bugs it catches:** Capital disappearing during deployment transitions. Recovery inflating deployed balances. Write-offs not reducing deployed.

```solidity
function invariant__totalIdleAndDeployedValueMatchesAccounting() public view {
    assertEq(
        tranchePool.getTotalIdleValue() + tranchePool.getTotalDeployedValue(),
        tranchePool.getTotalDeposited()
            - tranchePool.getTotalLoss()
            + tranchePool.getTotalRecovered()
    );
}
```

---

## Invariant 3 — Protocol Solvency

The actual ERC20 token balance held by `TranchePool` must equal the sum of all internal obligations.

**Conservation rule:**
```
TokenBalance(TranchePool) == TotalIdle + TotalUnclaimedInterest + ProtocolRevenue
```

This is the hard solvency check. If `TokenBalance < Obligations`, the protocol cannot meet its obligations.

**Bugs it catches:** Interest distribution creating tokens from nothing. Idle accounting drifting from actual token balance. Protocol revenue being double-counted.

```solidity
function invariant__totalUnclaimedInterestAndIdleValueMatchesTotalTokenBalance() public view {
    assertEq(
        tranchePool.getTotalUnclaimedInterest()
            + tranchePool.getTotalIdleValue()
            + tranchePool.getProtocolRevenue(),
        ERC20Mock(usdt).balanceOf(address(tranchePool))
    );
}
```

---

## Invariant 4 — Tranche Decomposition Integrity

The global deployed value counter must always equal the sum of deployed values across individual tranches.

**Conservation rule:**
```
TotalDeployed == SeniorDeployed + JuniorDeployed + EquityDeployed
```

**Reasoning:** Waterfall functions update both the global counter and the per-tranche counters. If any update path only modifies one and not the other, the global counter drifts from the tranche sum.

**Bugs it catches:** Loss absorption updating the global total but not a specific tranche. Allocation updating tranches but not the global total.

```solidity
function invariant__totalDeployedValueMatchesSumOfIndividualTranches() public view {
    assertEq(
        tranchePool.getTotalDeployedValue(),
        tranchePool.getSeniorTrancheDeployedValue()
            + tranchePool.getJuniorTrancheDeployedValue()
            + tranchePool.getEquityTrancheDeployedValue()
    );
}
```

---

## Invariant 5 — Loan Principal Integrity (System-Level)

A system-level variant of Invariant 1 that iterates over actual contract storage rather than handler ghost state.

**Conservation rule:**
```
TranchePool.totalDeployedValue == Σ loan.principalOutstanding for all loans
```

**Distinction from Invariant 1:** Invariant 1 uses the handler's ghost accounting. Invariant 5 reads directly from `LoanEngine` storage. This verifies the protocol is internally consistent independent of the handler's tracking.

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
        tranchePool.getTotalDeployedValue()
    );
}
```

---

## Invariant 6 — Exhaustion Safety

All invariants must hold even when idle liquidity reaches zero.

The handler explicitly allows full capital deployment and then exercises repayments, defaults, write-offs, and recoveries against a fully depleted idle pool.

**Bugs it catches:** Underflows when idle reaches zero. Incorrect recovery handling after full deployment. Last-loan edge cases.

```solidity
bool allowFullDeployment = true;
```

---

## Assumptions and Scope

The invariant tests operate under the following assumptions:
- Token transfers succeed (standard ERC20 behaviour)
- Unsolicited ERC20 transfers to the pool are out-of-scope donations not reflected in internal accounting
- Credit policy is correctly configured and frozen before loan creation
- External price or oracle risk is out of scope
- Access control is correctly configured (the handler holds the required roles)
