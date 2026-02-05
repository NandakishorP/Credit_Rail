// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {CreditRailStateFullFuzzTest} from "./CreditRailStateFullFuzzTest.t.sol";

// Echidna explicitly looks for public functions to fuzz.
// This contract inherits the entire setup from CreditRailStateFullFuzzTest
// and adds the necessary public wrapper functions for Echidna.
contract EchidnaCreditRailTest is CreditRailStateFullFuzzTest {
    
    constructor() CreditRailStateFullFuzzTest() {
        // The parent constructor runs automatically, setting up:
        // handler, loanEngine, tranchePool, etc.
    }

    // -----------------------------------------------------------------------
    // MEDUSA/ECHIDNA TEST PROBE
    // -----------------------------------------------------------------------
    function property_alive() public pure returns (bool) {
        return true;
    }

    // -----------------------------------------------------------------------
    // ECHIDNA WRAPPERS
    // -----------------------------------------------------------------------

    function depositSeniorTranche(uint256 userIndex, uint256 amount) public {
        handler.depositSeniorTranche(userIndex, amount);
    }

    function depositJuniorTranche(uint256 userIndex, uint256 amount) public {
        handler.depositJuniorTranche(userIndex, amount);
    }

    function depositEquityTranche(uint256 userIndex, uint256 amount) public {
        handler.depositEquityTranche(userIndex, amount);
    }

    function maybeCommitPool() public {
        handler.maybeCommitPool();
    }

    function createLoan(
        uint256 principalIssued,
        uint256 originationFeeBps,
        uint256 termDays,
        uint256 userIndex
    ) public {
        handler.createLoan(principalIssued, originationFeeBps, termDays, userIndex);
    }

    function activateLoan(uint256 loanId) public {
        handler.activateLoan(loanId);
    }

    function repayLoan(
        uint256 loanId,
        uint256 principalAmount,
        uint256 interestAmount
    ) public {
        handler.repayLoan(loanId, principalAmount, interestAmount);
    }

    function maybeDeclareDefault(uint256 loanId, bytes32 reasonHash) public {
        handler.maybeDeclareDefault(loanId, reasonHash);
    }

    function maybeWriteOffLoan(uint256 loanId) public {
        handler.maybeWriteOffLoan(loanId);
    }

    function maybeRecoverLoan(
        uint256 loanId,
        uint256 amount,
        uint256 agentIndex
    ) public {
        handler.maybeRecoverLoan(loanId, amount, agentIndex);
    }

    function warpTime(uint256 daysToWarp) public {
        handler.warpTime(daysToWarp);
    }
}
