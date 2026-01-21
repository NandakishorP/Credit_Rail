// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/**
 * @title CreditPolicy
 * @notice Immutable-by-version credit constitution for private credit funds
 */
contract CreditPolicy {
    /*//////////////////////////////////////////////////////////////
                                ERRORS
    //////////////////////////////////////////////////////////////*/
    error CreditPolicy__Unauthorized();
    error CreditPolicy__PolicyFrozen(uint256 version);
    error CreditPolicy__InvalidVersion();
    error CreditPolicy__PolicyInactive();
    error CreditPolicy__PolicyVersionExists(uint256 version);

    /*//////////////////////////////////////////////////////////////
                                MODIFIERS
    //////////////////////////////////////////////////////////////*/
    modifier onlyAdmin() {
        if (msg.sender != policyAdmin) revert CreditPolicy__Unauthorized();
        _;
    }

    modifier policyEditable(uint256 version) {
        if (policyFrozen[version]) revert CreditPolicy__PolicyFrozen(version);
        _;
    }

    modifier policyExists(uint256 version) {
        if (!policyCreated[version]) revert CreditPolicy__InvalidVersion();
        _;
    }

    /*//////////////////////////////////////////////////////////////
                                CORE ROLES
    //////////////////////////////////////////////////////////////*/
    address public policyAdmin;

    /*//////////////////////////////////////////////////////////////
                            POLICY LIFECYCLE
    //////////////////////////////////////////////////////////////*/
    uint256 public activePolicyVersion;
    mapping(uint256 => bool) public policyCreated;
    mapping(uint256 => bool) public policyFrozen;
    mapping(uint256 => bool) public policyActive;

    mapping(uint256 => uint256) public lastUpdated;

    /*//////////////////////////////////////////////////////////////
                        ELIGIBILITY (PRE-LOAN)
    //////////////////////////////////////////////////////////////*/
    struct EligibilityCriteria {
        uint256 minAnnualRevenue;
        uint256 minEBITDA;
        uint256 minTangibleNetWorth;
        uint256 minBusinessAgeDays;
        uint256 maxDefaultsLast36Months;
        bool bankruptcyExcluded;
    }

    mapping(uint256 => EligibilityCriteria) public eligibility;

    /*//////////////////////////////////////////////////////////////
                        FINANCIAL RATIOS (UNDERWRITING)
    //////////////////////////////////////////////////////////////*/
    struct FinancialRatios {
        uint256 maxTotalDebtToEBITDA;
        uint256 minInterestCoverageRatio;
        uint256 minCurrentRatio;
        uint256 minEBITDAMarginBps;
    }

    mapping(uint256 => FinancialRatios) public ratios;

    /*//////////////////////////////////////////////////////////////
                        LOAN TIERS (PRICING REFERENCE)
    //////////////////////////////////////////////////////////////*/
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

    mapping(uint256 => mapping(uint8 => LoanTier)) public loanTiers;
    mapping(uint256 => uint8) public totalTiers;

    /*//////////////////////////////////////////////////////////////
                        CONCENTRATION LIMITS
    //////////////////////////////////////////////////////////////*/
    struct ConcentrationLimits {
        uint256 maxSingleBorrowerBps;
        uint256 maxIndustryConcentrationBps;
    }

    mapping(uint256 => ConcentrationLimits) public concentration;

    /*//////////////////////////////////////////////////////////////
                        INDUSTRY EXCLUSIONS
    //////////////////////////////////////////////////////////////*/
    mapping(uint256 => mapping(bytes32 => bool)) public excludedIndustries;

    /*//////////////////////////////////////////////////////////////
                        ATTESTATION REQUIREMENTS
    //////////////////////////////////////////////////////////////*/
    struct AttestationRequirements {
        uint256 maxAttestationAgeDays;
        uint256 reAttestationFrequencyDays;
        bool requiresCPAAttestation;
    }

    mapping(uint256 => AttestationRequirements) public attestation;

    /*//////////////////////////////////////////////////////////////
                        MAINTENANCE COVENANTS
    //////////////////////////////////////////////////////////////*/
    struct MaintenanceCovenants {
        uint256 maxLeverageRatio;
        uint256 minCoverageRatio;
        uint256 minLiquidityAmount;
        bool allowsDividends;
        uint256 reportingFrequencyDays;
    }

    mapping(uint256 => MaintenanceCovenants) public covenants;

    /*//////////////////////////////////////////////////////////////
                        DOCUMENT ANCHORING
    //////////////////////////////////////////////////////////////*/
    mapping(uint256 => bytes32) public policyDocumentHash;
    mapping(uint256 => string) public policyDocumentURI;

    /*//////////////////////////////////////////////////////////////
                                EVENTS
    //////////////////////////////////////////////////////////////*/
    event PolicyCreated(uint256 version, uint256 timestamp);
    event PolicyFrozen(uint256 version, uint256 timestamp);
    event PolicyUpdated(uint256 version);
    event LoanTierUpdated(uint256 version, uint8 tierId);
    event IndustryExcluded(uint256 version, bytes32 industry);
    event IndustryIncluded(uint256 version, bytes32 industry);

    /*//////////////////////////////////////////////////////////////
                                CONSTRUCTOR
    //////////////////////////////////////////////////////////////*/
    constructor() {
        policyAdmin = msg.sender;
    }

    /*//////////////////////////////////////////////////////////////
                        POLICY CREATION
    //////////////////////////////////////////////////////////////*/
    function createPolicy(uint256 version) external onlyAdmin {
        if (policyCreated[version]) {
            revert CreditPolicy__PolicyVersionExists(version);
        }

        policyCreated[version] = true;
        policyActive[version] = true;
        activePolicyVersion = version;
        lastUpdated[version] = block.timestamp;

        emit PolicyCreated(version, block.timestamp);
    }

    function freezePolicy(
        uint256 version
    ) external onlyAdmin policyExists(version) {
        policyFrozen[version] = true;

        emit PolicyFrozen(version, block.timestamp);
    }

    /*//////////////////////////////////////////////////////////////
                        ELIGIBILITY UPDATE
    //////////////////////////////////////////////////////////////*/
    function updateEligibility(
        uint256 version,
        EligibilityCriteria calldata data
    ) external onlyAdmin policyEditable(version) policyExists(version) {
        eligibility[version] = data;
        lastUpdated[version] = block.timestamp;
        emit PolicyUpdated(version);
    }

    /*//////////////////////////////////////////////////////////////
                        RATIOS UPDATE
    //////////////////////////////////////////////////////////////*/
    function updateRatios(
        uint256 version,
        FinancialRatios calldata data
    ) external onlyAdmin policyEditable(version) policyExists(version) {
        ratios[version] = data;
        lastUpdated[version] = block.timestamp;
        emit PolicyUpdated(version);
    }

    /*//////////////////////////////////////////////////////////////
                        CONCENTRATION UPDATE
    //////////////////////////////////////////////////////////////*/
    function updateConcentration(
        uint256 version,
        ConcentrationLimits calldata data
    ) external onlyAdmin policyEditable(version) policyExists(version) {
        concentration[version] = data;
        lastUpdated[version] = block.timestamp;
        emit PolicyUpdated(version);
    }

    /*//////////////////////////////////////////////////////////////
                        ATTESTATION UPDATE
    //////////////////////////////////////////////////////////////*/
    function updateAttestation(
        uint256 version,
        AttestationRequirements calldata data
    ) external onlyAdmin policyEditable(version) policyExists(version) {
        attestation[version] = data;
        lastUpdated[version] = block.timestamp;
        emit PolicyUpdated(version);
    }

    /*//////////////////////////////////////////////////////////////
                        COVENANT UPDATE
    //////////////////////////////////////////////////////////////*/
    function updateCovenants(
        uint256 version,
        MaintenanceCovenants calldata data
    ) external onlyAdmin policyEditable(version) policyExists(version) {
        covenants[version] = data;
        lastUpdated[version] = block.timestamp;
        emit PolicyUpdated(version);
    }

    /*//////////////////////////////////////////////////////////////
                        LOAN TIERS
    //////////////////////////////////////////////////////////////*/
    function setLoanTier(
        uint256 version,
        uint8 tierId,
        LoanTier calldata tier
    ) external onlyAdmin policyEditable(version) policyExists(version) {
        loanTiers[version][tierId] = tier;
        if (tierId >= totalTiers[version]) {
            totalTiers[version] = tierId + 1;
        }
        emit LoanTierUpdated(version, tierId);
    }

    /*//////////////////////////////////////////////////////////////
                        INDUSTRY CONTROLS
    //////////////////////////////////////////////////////////////*/
    function excludeIndustry(
        uint256 version,
        bytes32 industry
    ) external onlyAdmin policyEditable(version) policyExists(version) {
        excludedIndustries[version][industry] = true;
        emit IndustryExcluded(version, industry);
    }

    function includeIndustry(
        uint256 version,
        bytes32 industry
    ) external onlyAdmin policyEditable(version) policyExists(version) {
        excludedIndustries[version][industry] = false;
        emit IndustryIncluded(version, industry);
    }

    /*//////////////////////////////////////////////////////////////
                        DOCUMENT UPDATE
    //////////////////////////////////////////////////////////////*/
    function setPolicyDocument(
        uint256 version,
        bytes32 hash,
        string calldata uri
    ) external onlyAdmin policyEditable(version) policyExists(version) {
        policyDocumentHash[version] = hash;
        policyDocumentURI[version] = uri;
        lastUpdated[version] = block.timestamp;
    }
}
