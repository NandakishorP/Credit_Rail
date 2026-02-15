// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

interface ICreditPolicy {
    /*//////////////////////////////////////////////////////////////
                            STRUCT DEFINITIONS
    //////////////////////////////////////////////////////////////*/
    struct EligibilityCriteria {
        uint256 minAnnualRevenue;
        uint256 minEBITDA;
        uint256 minTangibleNetWorth;
        uint256 minBusinessAgeDays;
        uint256 maxDefaultsLast36Months;
        bool bankruptcyExcluded;
    }

    struct FinancialRatios {
        uint256 maxTotalDebtToEBITDA;
        uint256 minInterestCoverageRatio;
        uint256 minCurrentRatio;
        uint256 minEBITDAMarginBps;
    }

    struct LoanTier {
        string name;
        uint256 minRevenue;
        uint256 maxRevenue;
        uint256 minEBITDA;
        uint256 maxDebtToEBITDA;
        uint256 maxLoanToEBITDA;
        uint256 interestRateBps;
        uint256 originationFeeBps;
        uint256 termDays;
        bool active;
    }

    struct ConcentrationLimits {
        uint256 maxSingleBorrowerBps;
        uint256 maxIndustryConcentrationBps;
    }

    struct AttestationRequirements {
        uint256 maxAttestationAgeDays;
        uint256 reAttestationFrequencyDays;
        bool requiresCPAAttestation;
    }

    struct MaintenanceCovenants {
        uint256 maxLeverageRatio;
        uint256 minCoverageRatio;
        uint256 minLiquidityAmount;
        bool allowsDividends;
        uint256 reportingFrequencyDays;
    }

    /*//////////////////////////////////////////////////////////////
                            FUNCTION SIGNATURES
    //////////////////////////////////////////////////////////////*/
    function createPolicy(uint256 version) external;

    function freezePolicy(uint256 version) external;

    function deActivatePolicy(uint256 version) external;

    function updateEligibility(
        uint256 version,
        EligibilityCriteria calldata data
    ) external;

    function updateRatios(
        uint256 version,
        FinancialRatios calldata data
    ) external;

    function updateConcentration(
        uint256 version,
        ConcentrationLimits calldata data
    ) external;

    function updateAttestation(
        uint256 version,
        AttestationRequirements calldata data
    ) external;

    function updateCovenants(
        uint256 version,
        MaintenanceCovenants calldata data
    ) external;

    function setLoanTier(
        uint256 version,
        uint8 tierId,
        LoanTier calldata tier
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

    function isIndustryExcluded(
        uint256 version,
        bytes32 industry
    ) external view returns (bool);

    function policyScopeHash(uint256 version) external view returns (bytes32);

    function setPolicyScopeHash(uint256 version, bytes32 hash) external;
}
