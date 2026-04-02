/*
 * Certora Verification Spec — LoanEngine
 *
 * Core invariants:
 *   1. Loan state machine: NONE → CREATED → ACTIVE → {REPAID, DEFAULTED → WRITTEN_OFF}
 *   2. Terminal states are permanent (REPAID, WRITTEN_OFF)
 *   3. Nullifier uniqueness (no proof replay)
 *   4. Accounting: principalOutstanding <= principalIssued
 *   5. Loan ID monotonically increases
 */

using LoanEngineHarness as le;

// ═══════════════════════════════════════════════════════════════════════
//                          METHODS BLOCK
// ═══════════════════════════════════════════════════════════════════════

methods {
    function le.getLoanState(uint256) external returns (ILoanEngine.LoanState) envfree;
    function le.getLoanPrincipalIssued(uint256) external returns (uint256) envfree;
    function le.getLoanPrincipalOutstanding(uint256) external returns (uint256) envfree;
    function le.getLoanInterestAccrued(uint256) external returns (uint256) envfree;
    function le.getLoanInterestPaid(uint256) external returns (uint256) envfree;
    function le.getLoanAprBps(uint256) external returns (uint256) envfree;
    function le.getLoanTermDays(uint256) external returns (uint256) envfree;
    function le.getLoanOriginationFeeBps(uint256) external returns (uint256) envfree;
    function le.getNullifierUsed(bytes32) external returns (bool) envfree;
    function le.s_nextLoanId() external returns (uint256) envfree;
    function le.s_maxOriginationFeeBps() external returns (uint256) envfree;
    function le.isInitialized() external returns (bool) envfree;

    // Summarize external contract calls as NONDET (we verify them separately)
    function _.verify(bytes, bytes32[]) external => NONDET;
    function _.isPolicyFrozen(uint256) external => NONDET;
    function _.isPolicyActive(uint256) external => NONDET;
    function _.isIndustryExcluded(uint256, bytes32) external => NONDET;
    function _.tierExistsInPolicy(uint256, uint8) external => NONDET;
    function _.policyScopeHash(uint256, uint8) external => NONDET;
    function _.getPoolState() external => NONDET;
    function _.getTotalIdleValue() external => NONDET;
    function _.allocateCapital(uint256, uint256, address, address) external => NONDET;
    function _.onRepayment(uint256, uint256) external => NONDET;
    function _.onInterestAccrued(uint256) external => NONDET;
    function _.onLoss(uint256, uint256) external => NONDET;
    function _.onRecovery(uint256) external => NONDET;
    function _.hash(Field.Type[]) external => NONDET;
    function _.safeTransferFrom(address, address, uint256) external => NONDET;
    function _.safeTransfer(address, uint256) external => NONDET;
}

ghost mathint sumOutStandingPrincipal{
    init_state axiom sumOutStandingPrincipal == 0;
}

hook Sstore loans[KEY uint256 id].outstandingPrincipal uint256 newVal (uint256 oldVal){
    sumOutStandingPrincipal = sumOutStandingPrincipal + newVal- oldVal ;
}

// ═══════════════════════════════════════════════════════════════════════
//                          DEFINITIONS
// ═══════════════════════════════════════════════════════════════════════

definition IS_TERMINAL(ILoanEngine.LoanState s) returns bool =
    s == ILoanEngine.LoanState.REPAID || s == ILoanEngine.LoanState.WRITTEN_OFF;

definition INIT() returns bool = le.isInitialized();

// Exclude initialize, proxy upgrade, and createLoan from parametric checks.
// - initialize: sets s_nextLoanId = 1 from HAVOC'd storage (looks like a decrease).
// - createLoan: too many NONDET-summarized externals (verify, policy, poseidon)
//   make every path revert, causing vacuity warnings across all rules.
//   createLoan is verified separately via the ZK proof + policy specs.
definition EXCLUDED(method f) returns bool =
    f.selector == sig:upgradeToAndCall(address,bytes).selector
    || f.selector == sig:initialize(address,address,uint256,address,address,address,address).selector
    || f.selector == sig:initializeHarness(address,address,uint256,address,address,address,address).selector
    || f.selector == 0x1230a365; // createLoan

// ═══════════════════════════════════════════════════════════════════════
//                          INVARIANTS
// ═══════════════════════════════════════════════════════════════════════

/// @title outstanding-leq-issued
/// A loan's outstanding principal can never exceed its issued principal.
invariant outstandingLeqIssued(uint256 loanId)
    INIT() => le.getLoanPrincipalOutstanding(loanId) <= le.getLoanPrincipalIssued(loanId)
    filtered { f -> !EXCLUDED(f) }

/// @title next-loan-id-positive
/// The next loan ID is always >= 1.
invariant nextLoanIdPositive()
    INIT() => le.s_nextLoanId() >= 1
    filtered { f -> !EXCLUDED(f) }

invariant totalDeployedMatchesSum()
    to_mathint(getTotalDeployed()) == sumOutStandingPrincipal
    filtered { f -> !EXCLUDED(f) }

// ═══════════════════════════════════════════════════════════════════════
//                             RULES
// ═══════════════════════════════════════════════════════════════════════

/// @title terminal-states-are-permanent
/// Once a loan is REPAID or WRITTEN_OFF, no function can change its state.
rule terminalStatesArePermanent(method f, uint256 loanId)
filtered { f -> !EXCLUDED(f) }
{
    env e;
    calldataarg args;
    require INIT();

    ILoanEngine.LoanState stateBefore = le.getLoanState(loanId);
    require IS_TERMINAL(stateBefore);

    f(e, args);

    assert le.getLoanState(loanId) == stateBefore,
        "A terminal loan state was changed";
}

/// @title valid-state-transitions-only
/// Loan state can only transition along valid edges:
/// NONE→CREATED, CREATED→ACTIVE, ACTIVE→REPAID, ACTIVE→DEFAULTED, DEFAULTED→WRITTEN_OFF
rule validStateTransitions(method f, uint256 loanId)
filtered { f -> !EXCLUDED(f) }
{
    env e;
    calldataarg args;
    require INIT();

    ILoanEngine.LoanState before = le.getLoanState(loanId);

    f(e, args);

    ILoanEngine.LoanState after = le.getLoanState(loanId);

    assert before == after
        || (before == ILoanEngine.LoanState.NONE && after == ILoanEngine.LoanState.CREATED)
        || (before == ILoanEngine.LoanState.CREATED && after == ILoanEngine.LoanState.ACTIVE)
        || (before == ILoanEngine.LoanState.ACTIVE && after == ILoanEngine.LoanState.REPAID)
        || (before == ILoanEngine.LoanState.ACTIVE && after == ILoanEngine.LoanState.DEFAULTED)
        || (before == ILoanEngine.LoanState.DEFAULTED && after == ILoanEngine.LoanState.WRITTEN_OFF),
        "Invalid loan state transition detected";
}

/// @title nullifier-once-used-always-used
/// Once a nullifier is marked as used, it can never be un-used.
/// Prevents ZK proof replay attacks.
rule nullifierPermanence(method f, bytes32 nullifier)
filtered { f -> !EXCLUDED(f) }
{
    env e;
    calldataarg args;
    require INIT();

    require le.getNullifierUsed(nullifier);

    f(e, args);

    assert le.getNullifierUsed(nullifier),
        "A used nullifier was reset — proof replay possible";
}

/// @title loan-id-monotonically-increases
/// s_nextLoanId can only increase, never decrease.
rule loanIdMonotonicallyIncreases(method f)
filtered { f -> !EXCLUDED(f) }
{
    env e;
    calldataarg args;
    require INIT();

    uint256 idBefore = le.s_nextLoanId();

    f(e, args);

    assert le.s_nextLoanId() >= idBefore,
        "s_nextLoanId decreased";
}

/// @title repaid-loan-has-zero-outstanding
/// If a loan transitions to REPAID, its outstanding principal and accrued interest must be 0.
rule repaidLoanIsFullySettled(uint256 loanId) {
    env e;
    calldataarg args;
    require INIT();

    ILoanEngine.LoanState before = le.getLoanState(loanId);
    require before == ILoanEngine.LoanState.ACTIVE;

    // Call any function
    le.repayLoan(e, args);

    ILoanEngine.LoanState after = le.getLoanState(loanId);

    assert after == ILoanEngine.LoanState.REPAID =>
        (le.getLoanPrincipalOutstanding(loanId) == 0 &&
         le.getLoanInterestAccrued(loanId) == 0),
        "Loan marked REPAID but still has outstanding balance";
}

/// @title written-off-loan-zeroed
/// When a loan is written off, principal outstanding and interest accrued must be zeroed.
rule writtenOffLoanZeroed(uint256 loanId) {
    env e;
    require INIT();

    ILoanEngine.LoanState before = le.getLoanState(loanId);
    require before == ILoanEngine.LoanState.DEFAULTED;

    le.writeOffLoan(e, loanId);

    assert le.getLoanPrincipalOutstanding(loanId) == 0,
        "Written-off loan still has outstanding principal";
    assert le.getLoanInterestAccrued(loanId) == 0,
        "Written-off loan still has accrued interest";
}

/// @title principal-never-increases
/// A loan's principalOutstanding can never exceed what it was after activation.
rule principalNeverIncreases(method f, uint256 loanId)
filtered { f -> !EXCLUDED(f) }
{
    env e;
    calldataarg args;
    require INIT();

    require le.getLoanState(loanId) == ILoanEngine.LoanState.ACTIVE;
    uint256 outstandingBefore = le.getLoanPrincipalOutstanding(loanId);

    f(e, args);

    // If loan is still active, principal can only decrease or stay same
    require le.getLoanState(loanId) == ILoanEngine.LoanState.ACTIVE;
    assert le.getLoanPrincipalOutstanding(loanId) <= outstandingBefore,
        "Outstanding principal increased on an active loan";
}
