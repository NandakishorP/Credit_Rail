// SPDX-License-Identifier: MIT
pragma solidity 0.8.30;

import {CreditPolicy} from "../../src/CreditPolicy.sol";

/// @title CreditPolicyHarness
/// @notice Exposes internal state for Certora verification.
contract CreditPolicyHarness is CreditPolicy {

    bool private _harnessInitialized;

    function initializeHarness(
        address initialAdmin
    ) external {
        require(!_harnessInitialized, "already initialized");
        this.initialize(initialAdmin);
        _harnessInitialized = true;
    }

    function isInitialized() external view returns (bool) {
        return _harnessInitialized;
    }

    function getPolicyFrozen(uint256 version) external view returns (bool) {
        return policyFrozen[version];
    }

    function getPolicyActive(uint256 version) external view returns (bool) {
        return policyActive[version];
    }

    function getHasScopeHash(uint256 version) external view returns (bool) {
        return hasScopeHash[version];
    }

    function getExcludedIndustry(uint256 version, bytes32 industry) external view returns (bool) {
        return excludedIndustries[version][industry];
    }

    function getPolicyScopeHash(uint256 version, uint8 tierId) external view returns (bytes32) {
        return _policyScopeHashes[version][tierId];
    }

}
