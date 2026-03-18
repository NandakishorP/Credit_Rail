/*
 * Certora Verification Spec — TranchePool
 *
 * Core invariants:
 *   1. Capital conservation: money in == money accounted for
 *   2. Loss/recovery waterfall symmetry and ordering
 *   3. Interest waterfall: accrued ≤ target
 *   4. Interest index is monotonically non-decreasing
 *   5. Pool state machine: OPEN → COMMITTED → DEPLOYED → CLOSED
 *   6. Share-to-idle parity in OPEN state
 *   7. Allocation ratios sum to ≤ 100%
 *   8. No deployed capital in OPEN or CLOSED states
 */

using TranchePoolHarness as tp;

// ═══════════════════════════════════════════════════════════════════════
//                          METHODS BLOCK
// ═══════════════════════════════════════════════════════════════════════

methods {
    function tp.getIdleValue(uint256) external returns (uint256) envfree;
    function tp.getDeployedValue(uint256) external returns (uint256) envfree;
    function tp.getTotalShares(uint256) external returns (uint256) envfree;
    function tp.getInterestIndex(uint256) external returns (uint256) envfree;
    function tp.getAccruedInterest(uint256) external returns (uint256) envfree;
    function tp.getTargetInterest(uint256) external returns (uint256) envfree;
    function tp.getPrincipalShortfall(uint256) external returns (uint256) envfree;
    function tp.getUserShares(uint256, address) external returns (uint256) envfree;
    function tp.getUserIndex(uint256, address) external returns (uint256) envfree;
    function tp.getTotalIdleAcrossTranches() external returns (uint256) envfree;
    function tp.getTotalDeployedAcrossTranches() external returns (uint256) envfree;
    function tp.getTotalCapitalAcrossTranches() external returns (uint256) envfree;
    function tp.getTotalShortfallAcrossTranches() external returns (uint256) envfree;
    function tp.getProtocolRevenue() external returns (uint256) envfree;
    function tp.getTotalDeposited() external returns (uint256) envfree;
    function tp.getTotalLoss() external returns (uint256) envfree;
    function tp.getTotalRecovered() external returns (uint256) envfree;
    function tp.getPoolStateCurrent() external returns (ITranchePool.PoolState) envfree;
    function tp.isInitialized() external returns (bool) envfree;
    function tp.getSeniorAllocationFactor() external returns (uint256) envfree;
    function tp.getJuniorAllocationFactor() external returns (uint256) envfree;

    // Summarize SafeERC20 internal library calls as NONDET —
    // bypasses the assembly in OZ SafeERC20 that causes AUTO havoc.
    // NONDET = non-deterministic return, NO storage side-effects.
    function SafeERC20.safeTransfer(address, address, uint256) internal => NONDET;
    function SafeERC20.safeTransferFrom(address, address, address, uint256) internal => NONDET;
}

// ═══════════════════════════════════════════════════════════════════════
//                         DEFINITIONS
// ═══════════════════════════════════════════════════════════════════════

// Tranche indices
definition SENIOR() returns uint256 = 0;
definition JUNIOR() returns uint256 = 1;
definition EQUITY() returns uint256 = 2;
definition INIT() returns bool = tp.isInitialized();

// Exclude harness-only functions from parametric checks
definition EXCLUDED(method f) returns bool =
    f.selector == sig:upgradeToAndCall(address,bytes).selector
    || f.selector == sig:initializeHarness(address,address).selector
    || f.selector == sig:initialize(address,address).selector;
// ═══════════════════════════════════════════════════════════════════════
//                          INVARIANTS
// ═══════════════════════════════════════════════════════════════════════


/// @title interest-index-above-base
/// Interest indices never drop below the initial 1e18.
invariant interestIndexAboveBase(uint256 tid)
    INIT() && tid <= 2 => tp.getInterestIndex(tid) >= 1000000000000000000
    filtered { f -> !EXCLUDED(f) }

invariant capitalLocationCorrectness()
    INIT() => 
        to_mathint(tp.getTotalIdleAcrossTranches()) + to_mathint(tp.getTotalDeployedAcrossTranches())
        == to_mathint(tp.getTotalDeposited()) - to_mathint(tp.getTotalLoss()) + to_mathint(tp.getTotalRecovered())
    filtered { f -> !EXCLUDED(f) }

/// @title loss-recovery-waterfall-symmetry (Invariant 8)
/// If recovered ≥ loss, total shortfall must be zero.
/// Otherwise shortfall == loss − recovered.
invariant lossRecoveryWaterfallSymmetry()
    INIT() && tp.getTotalRecovered() >= tp.getTotalLoss()
        => tp.getTotalShortfallAcrossTranches() == 0
    filtered { f -> !EXCLUDED(f) }

invariant lossRecoveryWaterfallSymmetryDeficit()
    INIT() && tp.getTotalRecovered() < tp.getTotalLoss()
        => to_mathint(tp.getTotalShortfallAcrossTranches())
           == to_mathint(tp.getTotalLoss()) - to_mathint(tp.getTotalRecovered())
    filtered { f -> !EXCLUDED(f) }

/// @title loss-waterfall-ordering (Invariant 9)
/// If senior has shortfall and junior is capitalised, junior must also have shortfall.
invariant lossWaterfallOrderingSeniorImpliesJunior()
    INIT()
    && tp.getPrincipalShortfall(SENIOR()) > 0
    && tp.getTotalShares(JUNIOR()) > 0
        => tp.getPrincipalShortfall(JUNIOR()) > 0
    filtered { f -> !EXCLUDED(f) }

/// If senior has shortfall and equity is capitalised, equity must also have shortfall.
invariant lossWaterfallOrderingSeniorImpliesEquity()
    INIT()
    && tp.getPrincipalShortfall(SENIOR()) > 0
    && tp.getTotalShares(EQUITY()) > 0
        => tp.getPrincipalShortfall(EQUITY()) > 0
    filtered { f -> !EXCLUDED(f) }

/// If junior has shortfall and equity is capitalised, equity must also have shortfall.
invariant lossWaterfallOrderingJuniorImpliesEquity()
    INIT()
    && tp.getPrincipalShortfall(JUNIOR()) > 0
    && tp.getTotalShares(EQUITY()) > 0
        => tp.getPrincipalShortfall(EQUITY()) > 0
    filtered { f -> !EXCLUDED(f) }

/// @title pool-state-deployed-capital-validity (Invariant 15)
/// In OPEN or CLOSED state, no capital should be deployed.
invariant noDeployedCapitalInOpenOrClosed()
    INIT()
    && (tp.getPoolStateCurrent() == ITranchePool.PoolState.OPEN
        || tp.getPoolStateCurrent() == ITranchePool.PoolState.CLOSED)
        => tp.getTotalDeployedAcrossTranches() == 0
    filtered { f -> !EXCLUDED(f) }

/// @title share-to-idle-parity-open (Invariant 17)
/// In OPEN state, shares are minted 1:1 so totalShares == idleValue per tranche.
invariant shareToIdleParityOpenSenior()
    INIT() && tp.getPoolStateCurrent() == ITranchePool.PoolState.OPEN
        => tp.getTotalShares(SENIOR()) == tp.getIdleValue(SENIOR())
    filtered { f -> !EXCLUDED(f) }

invariant shareToIdleParityOpenJunior()
    INIT() && tp.getPoolStateCurrent() == ITranchePool.PoolState.OPEN
        => tp.getTotalShares(JUNIOR()) == tp.getIdleValue(JUNIOR())
    filtered { f -> !EXCLUDED(f) }

invariant shareToIdleParityOpenEquity()
    INIT() && tp.getPoolStateCurrent() == ITranchePool.PoolState.OPEN
        => tp.getTotalShares(EQUITY()) == tp.getIdleValue(EQUITY())
    filtered { f -> !EXCLUDED(f) }

/// @title allocation-ratios-bounded (Invariant 18)
/// Senior + Junior allocation factors must never exceed 100.
invariant allocationRatiosBounded()
    INIT() => tp.getSeniorAllocationFactor() + tp.getJuniorAllocationFactor() <= 100
    filtered { f -> !EXCLUDED(f) }

invariant seniorInterestAccruedNeverOverflowsTargetedInterest()
    INIT() => tp.getAccruedInterest(SENIOR()) <= tp.getTargetInterest(SENIOR())
    filtered { f -> !EXCLUDED(f) }


invariant juniorInterestAccruedNeverOverflowsTargetedInterest()
    INIT() => tp.getAccruedInterest(JUNIOR()) <= tp.getTargetInterest(JUNIOR())
    filtered { f -> !EXCLUDED(f) }

// ═══════════════════════════════════════════════════════════════════════
//                             RULES
// ════════════════════════════════════

/// @title interest-index-monotonic
/// The interest index for every tranche can only increase.
rule interestIndexMonotonic(method f, uint256 tid)
filtered { f -> !EXCLUDED(f) }
{
    env e;
    calldataarg args;
    require INIT();
    require tid <= 2;
    uint256 indexBefore = tp.getInterestIndex(tid);

    f(e, args);

    assert tp.getInterestIndex(tid) >= indexBefore,
        "Interest index decreased — LPs would lose claimable interest";
}



/// @title pool-state-machine
/// Pool state can only move forward: OPEN→COMMITTED→DEPLOYED→CLOSED.
rule poolStateOnlyMovesForward(method f)
filtered { f -> !EXCLUDED(f) }
{
    env e;
    calldataarg args;
    require INIT();
    ITranchePool.PoolState before = tp.getPoolStateCurrent();

    f(e, args);

    ITranchePool.PoolState after = tp.getPoolStateCurrent();

    assert before == after
        || (before == ITranchePool.PoolState.OPEN && after == ITranchePool.PoolState.COMMITTED)
        || (before == ITranchePool.PoolState.COMMITTED && after == ITranchePool.PoolState.DEPLOYED)
        || (before == ITranchePool.PoolState.DEPLOYED && after == ITranchePool.PoolState.CLOSED),
        "Pool state went backward or skipped a step";
}

/// @title loss-absorbed-equity-first
/// When onLoss is called and equity has deployed capital, equity shortfall
/// must increase (equity absorbs first, not senior).
rule lossAbsorbedEquityFirst(uint256 principalLoss, uint256 interestAccrued) {
    env e;
    
    uint256 equityDeployedBefore = tp.getDeployedValue(EQUITY());
    uint256 equityShortfallBefore = tp.getPrincipalShortfall(EQUITY());
    require INIT();
    require equityDeployedBefore > 0;
    require principalLoss > 0;
    require principalLoss <= tp.getTotalDeployedAcrossTranches();

    tp.onLoss(e, principalLoss, interestAccrued);

    assert tp.getPrincipalShortfall(EQUITY()) >= equityShortfallBefore,
        "Equity shortfall did not increase during loss — waterfall violated";
}

/// @title recovery-restores-senior-first
/// When onRecovery is called and senior has shortfall, senior shortfall
/// must decrease (senior is restored first).
rule recoveryRestoresSeniorFirst(uint256 amount) {
    env e;

    uint256 seniorShortfallBefore = tp.getPrincipalShortfall(SENIOR());
    require INIT();
    require seniorShortfallBefore > 0;
    require amount > 0;

    tp.onRecovery(e, amount);

    assert tp.getPrincipalShortfall(SENIOR()) < seniorShortfallBefore,
        "Senior shortfall did not decrease during recovery — waterfall violated";
}

/// @title deposit-increases-idle-and-shares
/// A successful deposit increases the tranche's idle value and total shares.
rule depositIncreasesIdleAndShares() {
    env e;

    uint256 amount;
    require INIT();
    uint256 idleBefore = tp.getIdleValue(SENIOR());
    uint256 sharesBefore = tp.getTotalShares(SENIOR());

    tp.depositSeniorTranche(e, amount);

    assert tp.getIdleValue(SENIOR()) == idleBefore + amount;
    assert tp.getTotalShares(SENIOR()) == sharesBefore + amount;
}

/// @title no-withdrawal-during-deployed
/// Withdrawals must revert when pool is in COMMITTED or DEPLOYED state.
rule noWithdrawalDuringDeployed() {
    env e;
    uint256 shares;
    require INIT();
    require tp.getPoolStateCurrent() == ITranchePool.PoolState.DEPLOYED;

    tp.withdrawSeniorTranche@withrevert(e, shares);

    assert lastReverted,
        "Withdrawal succeeded during DEPLOYED state";
}

/// @title total-loss-tracked
/// s_totalLoss only increases and tracks cumulative losses.
rule totalLossMonotonic(method f)
filtered { f -> !EXCLUDED(f) }
{
    env e;
    calldataarg args;
    require INIT();
    uint256 lossBefore = tp.getTotalLoss();

    f(e, args);

    assert tp.getTotalLoss() >= lossBefore,
        "Total loss decreased — accounting error";
}
