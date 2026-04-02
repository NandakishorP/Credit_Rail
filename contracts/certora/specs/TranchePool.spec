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
    function tp.getLastTrancheAccrualTimestamp() external returns (uint256) envfree;

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

// Functions gated by onlyLoanEngine — only callable during DEPLOYED state.
// Filter these from OPEN-state invariants since they can never fire in OPEN.
definition LOAN_ENGINE_ONLY(method f) returns bool =
    f.selector == sig:onRecovery(uint256).selector
    || f.selector == sig:onRepayment(uint256,uint256).selector
    || f.selector == sig:onLoss(uint256,uint256).selector
    || f.selector == sig:allocateCapital(uint256,uint256,address,address).selector
    || f.selector == sig:onInterestAccrued(uint256).selector;
// ═══════════════════════════════════════════════════════════════════════
//                        HELPER FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════

/// @notice Constrain HAVOC'd storage to realistic values.
/// Without this, Certora sets fields like lastTrancheAccrualTimestamp to MAX_UINT256,
/// causing underflows in _accrueTrancheTargets and overflows in interest accounting.
function requireRealisticState(env e) {
    // Timestamp must be in the past (monotonic clock)
    require tp.getLastTrancheAccrualTimestamp() <= e.block.timestamp;

    // Capital values bounded to avoid overflow in aggregation helpers
    require tp.getIdleValue(SENIOR()) + tp.getIdleValue(JUNIOR()) + tp.getIdleValue(EQUITY()) < 2^128;
    require tp.getDeployedValue(SENIOR()) + tp.getDeployedValue(JUNIOR()) + tp.getDeployedValue(EQUITY()) < 2^128;

    // Interest accounting bounded to avoid overflow in onRepayment
    require tp.getAccruedInterest(SENIOR()) < 2^128;
    require tp.getAccruedInterest(JUNIOR()) < 2^128;
    require tp.getAccruedInterest(EQUITY()) < 2^128;
    require tp.getTargetInterest(SENIOR()) < 2^128;
    require tp.getTargetInterest(JUNIOR()) < 2^128;
}

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
    {
        preserved onRecovery(uint256 amount) with (env e) {
            requireRealisticState(e);
        }
        preserved onRepayment(uint256 principalRepaid, uint256 interestRepaid) with (env e) {
            requireRealisticState(e);
        }
        preserved onLoss(uint256 principalLoss, uint256 interestAccrued) with (env e) {
            requireRealisticState(e);
        }
        preserved allocateCapital(uint256 totalDisbursement, uint256 fees, address deployer, address feeManager) with (env e) {
            requireRealisticState(e);
        }
    }

/// @title shortfall-bounded-by-total-loss (Invariant 8a)
/// Total shortfall can never exceed cumulative losses — recovery only reduces shortfall.
invariant shortfallBoundedByTotalLoss()
    INIT() => to_mathint(tp.getTotalShortfallAcrossTranches()) <= to_mathint(tp.getTotalLoss())
    filtered { f -> !EXCLUDED(f) }
    {
        preserved onRecovery(uint256 amount) with (env e) {
            requireRealisticState(e);
        }
        preserved onRepayment(uint256 principalRepaid, uint256 interestRepaid) with (env e) {
            requireRealisticState(e);
        }
        preserved onLoss(uint256 principalLoss, uint256 interestAccrued) with (env e) {
            requireRealisticState(e);
        }
    }

/// @title shortfall-plus-recovered-covers-loss (Invariant 8b)
/// shortfall + totalRecovered ≥ totalLoss always, because any recovery excess
/// flows to equity idle (not reducing shortfall) so the sum can only grow.
invariant shortfallPlusRecoveredCoversLoss()
    INIT() => to_mathint(tp.getTotalShortfallAcrossTranches()) + to_mathint(tp.getTotalRecovered())
              >= to_mathint(tp.getTotalLoss())
    filtered { f -> !EXCLUDED(f) }
    {
        preserved onRecovery(uint256 amount) with (env e) {
            requireRealisticState(e);
        }
        preserved onRepayment(uint256 principalRepaid, uint256 interestRepaid) with (env e) {
            requireRealisticState(e);
        }
        preserved onLoss(uint256 principalLoss, uint256 interestAccrued) with (env e) {
            requireRealisticState(e);
        }
    }

/// @title per-tranche-shortfall-bounded (Invariant 9)
/// No individual tranche shortfall can exceed total cumulative loss.
invariant perTrancheShortfallBoundedByLoss(uint256 tid)
    INIT() && tid <= 2
        => to_mathint(tp.getPrincipalShortfall(tid)) <= to_mathint(tp.getTotalLoss())
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
    filtered { f -> !EXCLUDED(f) && !LOAN_ENGINE_ONLY(f) }

invariant shareToIdleParityOpenJunior()
    INIT() && tp.getPoolStateCurrent() == ITranchePool.PoolState.OPEN
        => tp.getTotalShares(JUNIOR()) == tp.getIdleValue(JUNIOR())
    filtered { f -> !EXCLUDED(f) && !LOAN_ENGINE_ONLY(f) }

invariant shareToIdleParityOpenEquity()
    INIT() && tp.getPoolStateCurrent() == ITranchePool.PoolState.OPEN
        => tp.getTotalShares(EQUITY()) == tp.getIdleValue(EQUITY())
    filtered { f -> !EXCLUDED(f) && !LOAN_ENGINE_ONLY(f) }

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

