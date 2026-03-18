// SPDX-License-Identifier: MIT
pragma solidity 0.8.30;

import {TranchePool} from "../../src/TranchePool.sol";

/// @title TranchePoolHarness
/// @notice Exposes internal tranche state for Certora verification.
contract TranchePoolHarness is TranchePool {
    // ── Tranche getters (tid: 0=senior, 1=junior, 2=equity) ──

    bool private _initialized;

    function initializeHarness(
        address stableCoin_,
        address initialAdmin
    ) external {
        require(!_initialized, "already initialized");
        this.initialize(stableCoin_, initialAdmin);
        _initialized = true;
    }

    function isInitialized() external view returns (bool) {
        return _initialized;
    }

    function getIdleValue(uint256 tid) external view returns (uint256) {
        return tranches[tid].idleValue;
    }

    function getDeployedValue(uint256 tid) external view returns (uint256) {
        return tranches[tid].deployedValue;
    }

    function getTotalShares(uint256 tid) external view returns (uint256) {
        return tranches[tid].totalShares;
    }

    function getInterestIndex(uint256 tid) external view returns (uint256) {
        return tranches[tid].interestIndex;
    }

    function getAccruedInterest(uint256 tid) external view returns (uint256) {
        return tranches[tid].accruedInterest;
    }

    function getTargetInterest(uint256 tid) external view returns (uint256) {
        return tranches[tid].targetInterest;
    }

    function getPrincipalShortfall(
        uint256 tid
    ) external view returns (uint256) {
        return tranches[tid].principalShortfall;
    }

    function getUserShares(
        uint256 tid,
        address user
    ) external view returns (uint256) {
        return tranches[tid].shares[user];
    }

    function getUserIndex(
        uint256 tid,
        address user
    ) external view returns (uint256) {
        return tranches[tid].userIndex[user];
    }

    // ── Aggregate helpers ──

    function getTotalIdleAcrossTranches() external view returns (uint256) {
        return
            tranches[0].idleValue +
            tranches[1].idleValue +
            tranches[2].idleValue;
    }

    function getTotalDeployedAcrossTranches() external view returns (uint256) {
        return
            tranches[0].deployedValue +
            tranches[1].deployedValue +
            tranches[2].deployedValue;
    }

    function getTotalCapitalAcrossTranches() external view returns (uint256) {
        return
            tranches[0].idleValue +
            tranches[0].deployedValue +
            tranches[1].idleValue +
            tranches[1].deployedValue +
            tranches[2].idleValue +
            tranches[2].deployedValue;
    }

    function getTotalShortfallAcrossTranches() external view returns (uint256) {
        return
            tranches[0].principalShortfall +
            tranches[1].principalShortfall +
            tranches[2].principalShortfall;
    }

    // ── Global state (only expose fields NOT already public on TranchePool) ──

    function getSeniorAllocationFactor() external view returns (uint256) {
        return s_capital_allocation_factor_senior;
    }

    function getJuniorAllocationFactor() external view returns (uint256) {
        return s_capital_allocation_factor_junior;
    }

    function getPoolStateCurrent() external view returns (PoolState) {
        return poolState;
    }

    /// @dev Block upgrades in the harness so Certora doesn't try to verify across implementation swaps.
    function upgradeToAndCall(address, bytes memory) public payable override {
        revert("harness: upgrades disabled for verification");
    }
}
