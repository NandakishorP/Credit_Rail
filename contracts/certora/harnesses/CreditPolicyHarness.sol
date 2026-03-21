// SPDX-License-Identifier: MIT
pragma solidity 0.8.30;

import {CreditPolicy} from "../../src/CreditPolicy.sol";

/// @title CreditPolicyHarness
/// @notice Exposes internal state for Certora verification.
contract CreditPolicyHarness is CreditPolicy {

    bool private _harnessInitialized;

    function initializeHarness(
        address initialAdmin,
        address poseidon2_
    ) external {
        require(!_harnessInitialized, "already initialized");
        this.initialize(initialAdmin, poseidon2_);
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

    function getEligibilitySet(uint256 version) external view returns (bool) {
        return eligibilitySet[version];
    }

    function getRatiosSet(uint256 version) external view returns (bool) {
        return ratiosSet[version];
    }

    function getConcentrationSet(uint256 version) external view returns (bool) {
        return concentrationSet[version];
    }

    function getAttestationSet(uint256 version) external view returns (bool) {
        return attestationSet[version];
    }

    function getCovenantsSet(uint256 version) external view returns (bool) {
        return covenantsSet[version];
    }

    function getHasAtLeastOneTier(uint256 version) external view returns (bool) {
        return hasAtLeastOneTier[version];
    }

    function harnessMaxTiers() external view returns (uint8) {
        return maxTiers;
    }

    function getExcludedIndustry(uint256 version, bytes32 industry) external view returns (bool) {
        return excludedIndustries[version][industry];
    }

    function getPolicyScopeHash(uint256 version, uint8 tierId) external view returns (bytes32) {
        return _policyScopeHashes[version][tierId];
    }

}
