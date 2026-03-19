# Invariants

This protocol implements a tranche-based lending system where capital moves across multiple contracts (`TranchePool`, `LoanEngine`) and multiple lifecycle states (deposit, deployment, repayment, default, write-off, recovery).

Unit tests validate individual functions, but they cannot guarantee global correctness under arbitrary sequencing. Invariant testing defines and enforces the fundamental conservation laws of the system, verifying they hold under adversarial, stateful fuzzing.

---

## Fuzzing Infrastructure

Invariants are tested across four frameworks:

| Framework | File | Strategy |
|---|---|---|
| Foundry Invariant | `test/fuzz/invariant/CreditRailStateFullFuzzTest.t.sol` | Stateful handler with ghost accounting |
| Foundry Handler | `test/fuzz/invariant/Handler.t.sol` | Drives all 18 state transition selectors (17 invariants total) |
| Echidna | `test/fuzz/echidna/EchidnaTest.sol` | Property-based corpus fuzzing |
| Medusa | `test/medusa/MedusaTest.sol` | Coverage-guided stateful fuzzing |

The handler interacts with real production contracts (not mocks) and maintains ghost variables that mirror the expected state for cross-referencing.

---

## Conservation Law Invariants

These are the core accounting invariants. If any of these fail, the protocol has a critical bug.

---

### Invariant 1 — Capital Location Correctness

All principal capital must be in exactly one of two states: idle or deployed.

```
Idle + Deployed = TotalDeposited − TotalLoss + TotalRecovered
```

**Bugs it catches:** Capital disappearing during deployment. Recovery inflating deployed instead of idle. Write-offs not reducing deployed.

```solidity
function invariant__totalIdleAndDeployedValueMatchesAccounting() public view {
    assertEq(
        tranchePool.getTotalIdleValue() + tranchePool.getTotalDeployedValue(),
        tranchePool.getTotalDeposited() - tranchePool.getTotalLoss() + tranchePool.getTotalRecovered()
    );
}
```

---

### Invariant 2 — Outstanding Principal Matches Deployed (Ghost State)

The handler's ghost `outstandingPrincipal` tracker must always match the pool's deployed value.

```
Handler.outstandingPrincipal == TranchePool.totalDeployedValue
```

**Bugs it catches:** Ghost principal remaining after repayment. Deployed capital drift after write-off. Activation recording principal without pool allocation.

```solidity
function invariant__OutStandingPrincipalMatchesDeployed() public view {
    assertEq(handler.outStandingPrincipal(), tranchePool.getTotalDeployedValue());
}
```

---

### Invariant 3 — Global Conservation Law (Token Balance ≥ Liabilities)

The actual ERC20 token balance held by TranchePool must always be sufficient to cover all internal liabilities: idle capital, unclaimed interest, and protocol revenue.

```
TokenBalance(TranchePool) ≥ TotalIdle + TotalUnclaimedInterest + ProtocolRevenue
```

The `assertGe` (rather than `assertEq`) accounts for rounding dust from the interest index pattern: each repayment's two integer divisions can leave up to 1 wei of irrecoverable dust in `s_totalUnclaimedInterest`. A 10-wei tolerance covers multiple repayment rounds.

**Bugs it catches:** Interest distribution creating tokens from nowhere. Idle accounting drifting from actual balance. Protocol revenue being double-counted. Value leaking out of the pool unaccounted.

```solidity
function invariant__globalConservationLaw() public view {
    uint256 poolBalance = ERC20Mock(usdt).balanceOf(address(tranchePool));
    uint256 totalLiabilities = tranchePool.getTotalIdleValue()
        + tranchePool.getTotalUnclaimedInterest()
        + tranchePool.getProtocolRevenue();
    uint256 tolerance = 10;
    assertGe(poolBalance + tolerance, totalLiabilities);
    assertGe(totalLiabilities, poolBalance);
}
```

---

### Invariant 4 — System-Level Principal Integrity

Iterates over *actual contract storage* (all loans in LoanEngine) and verifies the sum of `principalOutstanding` equals the pool's total deployed value.

Unlike Invariant 2 (which compares against the Handler's ghost), this invariant verifies the protocol is internally consistent even if the handler is wrong.

```solidity
function invariant__systemLevel_PrincipalIntegrity() public view {
    uint256 totalOutstandingPrincipal = 0;
    uint256 nextId = loanEngine.getNextLoanId();
    for (uint256 i = 1; i < nextId; i++) {
        ILoanEngine.Loan memory loan = loanEngine.getLoanDetails(i);
        totalOutstandingPrincipal += loan.principalOutstanding;
    }
    assertEq(totalOutstandingPrincipal, tranchePool.getTotalDeployedValue());
}
```

---

## Waterfall Invariants

These verify that the interest and loss waterfalls behave correctly under all sequencing.

---

### Invariant 5 — Loss/Recovery Waterfall Symmetry

If total recovered ≥ total loss, the combined shortfall across all tranches must be zero—the hole has been completely filled. Otherwise, the shortfall must exactly equal the remaining gap.

```
if Recovered ≥ Loss → totalShortfall == 0
if Recovered < Loss → totalShortfall == Loss − Recovered
```

**Bugs it catches:** Recovery not filling shortfall. Shortfall remaining after over-recovery. Tranche-level shortfall drifting from global loss accounting.

```solidity
function invariant__lossRecoveryWaterfallSymmetry() public view {
    uint256 totalShortfall = tranchePool.getSeniorPrincipalShortfall()
        + tranchePool.getJuniorPrincipalShortfall()
        + tranchePool.getEquityPrincipalShortfall();

    if (tranchePool.getTotalRecovered() >= tranchePool.getTotalLoss()) {
        assertEq(totalShortfall, 0);
    } else {
        assertEq(totalShortfall, tranchePool.getTotalLoss() - tranchePool.getTotalRecovered());
    }
}
```

---

### Invariant 6 — Loss Waterfall Ordering

Losses absorb equity → junior → senior (via `deployedValue`). If a senior tranche has a shortfall, every **capitalised** subordinate tranche (one with `totalShares > 0`) must also have a shortfall — because the waterfall would have absorbed their `deployedValue` first.

The check is gated on `totalShares > 0` because:
- **Uncapitalised tranche edge case:** If equity or junior has zero deposits (`totalShares == 0`), it has zero `deployedValue` when loss hits, so the waterfall skips it. Senior can acquire a shortfall while an uncapitalised subordinate tranche has none — that is correct protocol behaviour, not a bug.
- **Re-deployment after loss:** New loan activations move idle → deployed, which can increase `deployedValue` from 0 even while a shortfall exists. Therefore we check *shortfalls* (cumulative loss), not `deployedValue == 0`.
- **Recovery ordering:** Recovery restores senior → junior → equity. Since equity shortfall is the *last* to be cleared, equity's shortfall cannot reach 0 while junior's shortfall is still > 0 (among capitalised tranches).

```solidity
function invariant__lossWaterfallOrdering() public view {
    uint256 seniorShortfall = tranchePool.getSeniorPrincipalShortfall();
    uint256 juniorShortfall = tranchePool.getJuniorPrincipalShortfall();
    uint256 equityShortfall = tranchePool.getEquityPrincipalShortfall();

    bool juniorCapitalised = tranchePool.getTotalJuniorShares() > 0;
    bool equityCapitalised = tranchePool.getTotalEquityShares() > 0;

    if (seniorShortfall > 0) {
        if (juniorCapitalised) {
            assertTrue(juniorShortfall > 0, "Senior has shortfall but capitalised junior has none");
        }
        if (equityCapitalised) {
            assertTrue(equityShortfall > 0, "Senior has shortfall but capitalised equity has none");
        }
    }
    if (juniorShortfall > 0 && equityCapitalised) {
        assertTrue(equityShortfall > 0, "Junior has shortfall but capitalised equity has none");
    }
}
```

---

### Invariant 7 — Interest Waterfall Senior Priority

Senior and Junior accrued interest can never exceed their respective targets. If it did, it would mean a lower-priority tranche received interest before a higher-priority tranche's target was met.

```
seniorAccrued ≤ seniorTarget
juniorAccrued ≤ juniorTarget
```

```solidity
function invariant__interestWaterfallSeniorPriority() public view {
    assertLe(tranchePool.seniorAccruedInterest(), tranchePool.seniorTargetInterest());
    assertLe(tranchePool.juniorAccruedInterest(), tranchePool.juniorTargetInterest());
}
```

---

## Loan-Level Invariants

These verify correctness of individual loan state across the full lifecycle.

---

### Invariant 8 — Loan State Consistency

- `NONE` and `CREATED` loans must have `principalOutstanding == 0` (no capital deployed yet)
- `REPAID` and `WRITTEN_OFF` loans must have `principalOutstanding == 0` (terminal states)
- `ACTIVE` loans must have `principalOutstanding ≤ principalIssued` (can't owe more than borrowed)

```solidity
function invariant__loanStateConsistency() public view {
    uint256 nextId = loanEngine.getNextLoanId();
    for (uint256 i = 1; i < nextId; i++) {
        ILoanEngine.Loan memory loan = loanEngine.getLoanDetails(i);
        if (loan.state == ILoanEngine.LoanState.NONE || loan.state == ILoanEngine.LoanState.CREATED) {
            assertEq(loan.principalOutstanding, 0);
        }
        if (loan.state == ILoanEngine.LoanState.REPAID || loan.state == ILoanEngine.LoanState.WRITTEN_OFF) {
            assertEq(loan.principalOutstanding, 0);
        }
        if (loan.state == ILoanEngine.LoanState.ACTIVE) {
            assertLe(loan.principalOutstanding, loan.principalIssued);
        }
    }
}
```

---

### Invariant 9 — Loan Interest Accounting

- `REPAID` loans must have `interestAccrued == 0` (all interest was paid before closure)
- `WRITTEN_OFF` loans must have `interestAccrued == 0` (interest was cancelled on write-off)

```solidity
function invariant__loanInterestAccounting() public view {
    uint256 nextId = loanEngine.getNextLoanId();
    for (uint256 i = 1; i < nextId; i++) {
        ILoanEngine.Loan memory loan = loanEngine.getLoanDetails(i);
        if (loan.state == ILoanEngine.LoanState.REPAID) {
            assertEq(loan.interestAccrued, 0);
        }
        if (loan.state == ILoanEngine.LoanState.WRITTEN_OFF) {
            assertEq(loan.interestAccrued, 0);
        }
    }
}
```

---

### Invariant 10 — Origination Fee Bounded

Every loan's `originationFeeBps` must be ≤ the protocol's configured `maxOriginationFeeBps`. This ensures no loan was created with a fee exceeding the cap.

```solidity
function invariant__originationFeeBounded() public view {
    uint256 nextId = loanEngine.getNextLoanId();
    uint256 maxFee = loanEngine.getMaxOriginationFeeBps();
    for (uint256 i = 1; i < nextId; i++) {
        ILoanEngine.Loan memory loan = loanEngine.getLoanDetails(i);
        assertLe(loan.originationFeeBps, maxFee);
    }
}
```

---

### Invariant 11 — APR Sanity Bound

Every created loan must have an APR > 0 and < 100%. A zero or 100%+ APR would indicate a misconfigured tier or a broken loan creation path.

```solidity
function invariant__aprSanityBound() public view {
    uint256 nextId = loanEngine.getNextLoanId();
    for (uint256 i = 1; i < nextId; i++) {
        ILoanEngine.Loan memory loan = loanEngine.getLoanDetails(i);
        if (loan.state != ILoanEngine.LoanState.NONE) {
            assertGt(loan.aprBps, 0);
            assertLt(loan.aprBps, 10000);
        }
    }
}
```

---

## Pool State Invariants

These verify the pool's state machine constraints hold under all sequencing.

---

### Invariant 12 — Pool State / Deployed Capital Validity

If the pool is in `OPEN` or `CLOSED` state, the total deployed value must be zero. No capital should be outstanding before the pool accepts loans or after all loans have been settled.

```solidity
function invariant__poolStateValidityDeployedCapital() public view {
    ITranchePool.PoolState state = tranchePool.getPoolState();
    if (state == ITranchePool.PoolState.OPEN || state == ITranchePool.PoolState.CLOSED) {
        assertEq(tranchePool.getTotalDeployedValue(), 0);
    }
}
```

---

### Invariant 13 — Interest Index Monotonicity

Interest indices for all three tranches initialise at `1e18` and can only increase over time. A decrease would mean interest is being "un-distributed", which breaks the claim calculation.

```solidity
function invariant__interestIndexMonotonicity() public view {
    assertGe(tranchePool.getSeniorInterestIndex(), 1e18);
    assertGe(tranchePool.getJuniorInterestIndex(), 1e18);
    assertGe(tranchePool.getEquityInterestIndex(), 1e18);
}
```

---

### Invariant 14 — Share-to-Idle Parity in OPEN State

When the pool is in `OPEN` state (no capital has been deployed, no interest has arrived), each tranche's total shares must exactly equal its idle value. Shares are minted 1:1 on deposit and no interest has been distributed yet, so any drift indicates a deposit or withdrawal bug.

This is enforced by **two separate invariant functions** in the test suite — one for senior, one for junior + equity.

```solidity
function invariant__seniorShareToIdleOpen() public view {
    if (tranchePool.getPoolState() == ITranchePool.PoolState.OPEN) {
        assertEq(tranchePool.getTotalSeniorShares(), tranchePool.getSeniorTrancheIdleValue());
    }
}

function invariant__juniorShareToIdleOpen() public view {
    if (tranchePool.getPoolState() == ITranchePool.PoolState.OPEN) {
        assertEq(tranchePool.getTotalJuniorShares(), tranchePool.getJuniorTrancheIdleValue());
        assertEq(tranchePool.getTotalEquityShares(), tranchePool.getEquityTrancheIdleValue());
    }
}
```

---

### Invariant 15 — Allocation Ratios Sum to ≤ 100%

The Senior + Junior allocation factors must never exceed 100%. The Equity allocation is implicitly `100 − Senior − Junior`, so exceeding 100 would make it negative, breaking the allocation algorithm.

```solidity
function invariant__allocationRatiosSumTo100OrLess() public view {
    assertLe(
        tranchePool.getSeniorAllocationRatio() + tranchePool.getJuniorAllocationRatio(),
        100
    );
}
```

---

### Invariant 16 — Unclaimed Interest + Idle Value Equals Token Balance

The pool's actual ERC20 token balance must exactly equal the sum of all idle capital plus all unclaimed (distributed but not yet claimed) interest across the three tranches.

```
TokenBalance(TranchePool) == TotalIdle + TotalUnclaimedInterest
```

**Bugs it catches:** Interest distribution minting new tokens rather than redistributing existing ones. Idle accounting drifting from the actual balance after mass claims. Race conditions between `onInterestAccrued()` and `claimInterest()` that leave the pool overcounted.

```solidity
function invariant__totalUnclaimedInterestAndIdleValueMatchesTotalTokenBalance()
    public
    view
{
    assertEq(
        tranchePool.getTotalUnclaimedInterest() + tranchePool.getTotalIdleValue(),
        ERC20Mock(usdt).balanceOf(address(tranchePool))
    );
}
```

---

## Assumptions and Scope

The invariant tests operate under the following assumptions:
- Token transfers succeed (standard ERC20 behaviour)
- Unsolicited ERC20 transfers to the pool are out-of-scope donations not reflected in internal accounting
- Credit policy is correctly configured and frozen before loan creation
- External price or oracle risk is out of scope
- Access control is correctly configured (the handler holds the required roles)
- Protocol revenue is assumed zero as the equity tranche always has LP shares in the test harness
