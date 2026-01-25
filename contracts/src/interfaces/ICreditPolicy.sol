// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import {CreditPolicy} from "../CreditPolicy.sol";

interface ICreditPolicy {
    function createPolicy(uint256 version) external;

    function freezePolicy(uint256 version) external;

    function deActivatePolicy(uint256 version) external;

    function updateEligibility(
        uint256 version,
        CreditPolicy.EligibilityCriteria calldata data
    ) external;

    function updateRatios(
        uint256 version,
        CreditPolicy.FinancialRatios calldata data
    ) external;

    function updateConcentration(
        uint256 version,
        CreditPolicy.ConcentrationLimits calldata data
    ) external;

    function updateAttestation(
        uint256 version,
        CreditPolicy.AttestationRequirements calldata data
    ) external;

    function updateCovenants(
        uint256 version,
        CreditPolicy.MaintenanceCovenants calldata data
    ) external;

    function setLoanTier(
        uint256 version,
        uint8 tierId,
        CreditPolicy.LoanTier calldata tier
    ) external;

    function excludeIndustry(uint256 version, bytes32 industry) external;

    function includeIndustry(uint256 version, bytes32 industry) external;

    function setPolicyDocument(
        uint256 version,
        bytes32 hash,
        string calldata uri
    ) external;

    function tierExistsInPolicy(
        uint256 version,
        uint8 tierId
    ) external view returns (bool);

    function changePolicyAdmin(address newAdmin) external;

    function isPolicyActive(uint256 version) external view returns (bool);

    function isPolicyFrozen(uint256 version) external view returns (bool);
}
