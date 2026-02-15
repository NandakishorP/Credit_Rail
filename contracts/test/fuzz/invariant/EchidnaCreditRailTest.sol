// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {CreditRailStateFullFuzzTest} from "./CreditRailStateFullFuzzTest.t.sol";

// Echidna explicitly looks for public functions to fuzz.
// This contract inherits the entire setup from CreditRailStateFullFuzzTest
// and adds the necessary public wrapper functions for Echidna.
contract EchidnaCreditRailTest is CreditRailStateFullFuzzTest {
    
    constructor() CreditRailStateFullFuzzTest() {
        // Since we changed the parent to use setUp(), we must call it here explicitly
        setUp();
    }

    // -----------------------------------------------------------------------
    // INTERNAL INVARIANT CHECKER (called after every action to mimic Foundry)
    // -----------------------------------------------------------------------
    function _checkCriticalInvariants() internal view {
        invariant__lossRecoveryWaterfallSymmetry();
        // Add more invariants here if you want comprehensive checking.
        // Note: Checking all invariants after every call is expensive but thorough.
    }

    // -----------------------------------------------------------------------
    // MEDUSA/ECHIDNA TEST PROBE
    // -----------------------------------------------------------------------
    function property_alive() public pure returns (bool) {
        return true;
    }

    // -----------------------------------------------------------------------
    // ECHIDNA INVARIANT CHECKER (called randomly by Echidna)
    // -----------------------------------------------------------------------
    function echidna_invariant_checks() public view {
        invariant__totalIdleAndDeployedValueMatchesAccounting();
        invariant__OutStandingPrincipalMatchesDeployed();
        invariant__totalUnclaimedInterestAndIdleValueMatchesTotalTokenBalance();
        invariant__totalDeployedValueMatchesSumOfIndividualTranches();
        invariant__systemLevel_PrincipalIntegrity();
        invariant__lossRecoveryWaterfallSymmetry();
        invariant__totalIdleValueIntegrity();
        invariant__seniorShareToIdleOpen();
        invariant__loanStateConsistency();
        invariant__interestIndexMonotonicity();
        invariant__poolStateValidityDeployedCapital();
        invariant__loanInterestAccounting();
    }

    // -----------------------------------------------------------------------
    // ECHIDNA WRAPPERS (with post-action invariant checks)
    // -----------------------------------------------------------------------

    function depositSeniorTranche(uint256 userIndex, uint256 amount) public {
        handler.depositSeniorTranche(userIndex, amount);
        _checkCriticalInvariants();
    }

    function depositJuniorTranche(uint256 userIndex, uint256 amount) public {
        handler.depositJuniorTranche(userIndex, amount);
        _checkCriticalInvariants();
    }

    function depositEquityTranche(uint256 userIndex, uint256 amount) public {
        handler.depositEquityTranche(userIndex, amount);
        _checkCriticalInvariants();
    }

    function maybeCommitPool() public {
        handler.maybeCommitPool();
        _checkCriticalInvariants();
    }

    function createLoan(
        uint256 principalIssued,
        uint256 originationFeeBps,
        uint256 termDays,
        uint256 userIndex
    ) public {
        handler.createLoan(principalIssued, originationFeeBps, termDays, userIndex);
        _checkCriticalInvariants();
    }

    function activateLoan(uint256 loanId) public {
        handler.activateLoan(loanId);
        _checkCriticalInvariants();
    }

    function repayLoan(
        uint256 loanId,
        uint256 principalAmount,
        uint256 interestAmount
    ) public {
        handler.repayLoan(loanId, principalAmount, interestAmount);
        _checkCriticalInvariants();
    }

    function maybeDeclareDefault(uint256 loanId, bytes32 reasonHash) public {
        handler.maybeDeclareDefault(loanId, reasonHash);
        _checkCriticalInvariants();
    }

    function maybeWriteOffLoan(uint256 loanId) public {
        handler.maybeWriteOffLoan(loanId);
        _checkCriticalInvariants();
    }

    function maybeRecoverLoan(
        uint256 loanId,
        uint256 amount,
        uint256 agentIndex
    ) public {
        handler.maybeRecoverLoan(loanId, amount, agentIndex);
        _checkCriticalInvariants();
    }

    function warpTime(uint256 daysToWarp) public {
        handler.warpTime(daysToWarp);
        _checkCriticalInvariants();
    }

    function mayClosePool() public {
        handler.mayClosePool();
        _checkCriticalInvariants();
    }

    function claimSeniorTrancheInterest(uint256 userIndex) public {
        handler.claimSeniorTrancheInterest(userIndex);
        _checkCriticalInvariants();
    }

    function claimJuniorTrancheInterest(uint256 userIndex) public {
        handler.claimJuniorTrancheInterest(userIndex);
        _checkCriticalInvariants();
    }

    function claimEquityTrancheInterest(uint256 userIndex) public {
        handler.claimEquityTrancheInterest(userIndex);
        _checkCriticalInvariants();
    }

    function withdrawSeniorTranche(uint256 userIndex, uint256 amount) public {
        handler.withdrawSeniorTranche(userIndex, amount);
        _checkCriticalInvariants();
    }

    function withdrawJuniorTranche(uint256 userIndex, uint256 amount) public {
        handler.withdrawJuniorTranche(userIndex, amount);
        _checkCriticalInvariants();
    }

    function withdrawEquityTranche(uint256 userIndex, uint256 amount) public {
        handler.withdrawEquityTranche(userIndex, amount);
        _checkCriticalInvariants();
    }
}
