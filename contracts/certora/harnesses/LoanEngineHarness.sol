// SPDX-License-Identifier: MIT
pragma solidity 0.8.30;

import {LoanEngine} from "../patched/LoanEngine.sol";
import {ILoanEngine} from "../patched/interfaces/ILoanEngine.sol";

/// @title LoanEngineHarness
/// @notice Exposes internal state and helpers for Certora verification.
contract LoanEngineHarness is LoanEngine {

    bool private _harnessInitialized;

    function initializeHarness(
        address _creditPolicyContract,
        address _loanProofVerifier,
        uint256 _maxOriginationFeeBps,
        address _tranchePool,
        address _stableCoinAddress,
        address _poseidon2,
        address _initialAdmin
    ) external {
        require(!_harnessInitialized, "already initialized");
        this.initialize(
            _creditPolicyContract,
            _loanProofVerifier,
            _maxOriginationFeeBps,
            _tranchePool,
            _stableCoinAddress,
            _poseidon2,
            _initialAdmin
        );
        _harnessInitialized = true;
    }

    function isInitialized() external view returns (bool) {
        return _harnessInitialized;
    }

    function getLoanState(uint256 loanId) external view returns (ILoanEngine.LoanState) {
        return s_loans[loanId].state;
    }

    function getLoanPrincipalIssued(uint256 loanId) external view returns (uint256) {
        return s_loans[loanId].principalIssued;
    }

    function getLoanPrincipalOutstanding(uint256 loanId) external view returns (uint256) {
        return s_loans[loanId].principalOutstanding;
    }

    function getLoanInterestAccrued(uint256 loanId) external view returns (uint256) {
        return s_loans[loanId].interestAccrued;
    }

    function getLoanInterestPaid(uint256 loanId) external view returns (uint256) {
        return s_loans[loanId].interestPaid;
    }

    function getLoanAprBps(uint256 loanId) external view returns (uint256) {
        return s_loans[loanId].aprBps;
    }

    function getLoanTermDays(uint256 loanId) external view returns (uint256) {
        return s_loans[loanId].termDays;
    }

    function getLoanStartTimestamp(uint256 loanId) external view returns (uint256) {
        return s_loans[loanId].startTimestamp;
    }

    function getLoanMaturityTimestamp(uint256 loanId) external view returns (uint256) {
        return s_loans[loanId].maturityTimestamp;
    }

    function getLoanOriginationFeeBps(uint256 loanId) external view returns (uint256) {
        return s_loans[loanId].originationFeeBps;
    }

    function getLoanLastAccrualTimestamp(uint256 loanId) external view returns (uint256) {
        return s_loans[loanId].lastAccrualTimestamp;
    }

    function getNullifierUsed(bytes32 nullifier) external view returns (bool) {
        return s_nullifierHashes[nullifier];
    }
}
