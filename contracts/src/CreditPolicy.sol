// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import {ICreditPolicy} from "./interfaces/ICreditPolicy.sol";
import {console} from "forge-std/console.sol";

/**
 * @title CreditPolicy
 * @notice Immutable-by-version credit constitution for private credit funds
 */
contract CreditPolicy is ICreditPolicy {
    /*//////////////////////////////////////////////////////////////
                                ERRORS
    //////////////////////////////////////////////////////////////*/
    error CreditPolicy__Unauthorized();
    error CreditPolicy__PolicyFrozen(uint256 version);
    error CreditPolicy__InvalidVersion();
    error CreditPolicy__PolicyVersionExists(uint256 version);
    error CreditPolicy__InvalidAdmin();
    error CreditPolicy__PolicyNotEditable(uint256 version);
    error CreditPolicy__IncompletePolicy(uint256 version);
    error CreditPolicy__InvalidIndustryHash();
    error CreditPolicy__PolicyNotActive(uint256 version);
    error CreditPolicy__InvalidTierCount(uint256 count);
    /*//////////////////////////////////////////////////////////////
                                MODIFIERS
    //////////////////////////////////////////////////////////////*/
    modifier onlyAdmin() {
        _onlyAdmin();
        _;
    }

    function _onlyAdmin() internal view {
        if (msg.sender != policyAdmin) revert CreditPolicy__Unauthorized();
    }

    modifier policyEditable(uint256 version) {
        _policyEditable(version);
        _;
    }

    function _policyEditable(uint256 version) internal view {
        if (policyFrozen[version] || !policyActive[version])
            revert CreditPolicy__PolicyNotEditable(version);
    }

    modifier policyExists(uint256 version) {
        _policyExists(version);
        _;
    }

    function _policyExists(uint256 version) internal view {
        if (!policyCreated[version]) revert CreditPolicy__InvalidVersion();
    }

    /*//////////////////////////////////////////////////////////////
                                CORE ROLES
    //////////////////////////////////////////////////////////////*/
    address public policyAdmin;
    uint8 internal maxTiers;

    /*//////////////////////////////////////////////////////////////
                            POLICY LIFECYCLE
    //////////////////////////////////////////////////////////////*/
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
    mapping(uint256 => mapping(uint8 => bool)) public tierExists;

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

    mapping(uint256 => bool) public eligibilitySet;
    mapping(uint256 => bool) public ratiosSet;
    mapping(uint256 => bool) public concentrationSet;
    mapping(uint256 => bool) public attestationSet;
    mapping(uint256 => bool) public covenantsSet;
    mapping(uint256 => bool) public hasAtLeastOneTier;

    /*//////////////////////////////////////////////////////////////
                                EVENTS
    //////////////////////////////////////////////////////////////*/
    event PolicyCreated(uint256 version, uint256 timestamp);
    event PolicyFrozen(uint256 version, uint256 timestamp);
    event PolicyEligibilityUpdated(uint256 version, uint256 timestamp);
    event PolicyRatiosUpdated(uint256 version, uint256 timestamp);
    event PolicyConcentrationUpdated(uint256 version, uint256 timestamp);
    event PolicyAttestationUpdated(uint256 version, uint256 timestamp);
    event PolicyCovenantsUpdated(uint256 version, uint256 timestamp);
    event LoanTierUpdated(uint256 version, uint8 tierId, uint256 timestamp);
    event IndustryExcluded(
        uint256 version,
        bytes32 industry,
        uint256 timestamp
    );
    event MaxTiersChanged(uint8 maxTiers);
    event IndustryIncluded(
        uint256 version,
        bytes32 industry,
        uint256 timestamp
    );

    event PolicyAdminChanged(address newAdmin);

    event PolicyDocumentSet(
        uint256 version,
        bytes32 hash,
        string uri,
        uint256 timestamp
    );
    event PolicyDeactivated(uint256 version, uint256 timestamp);

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
        if (version == 0) {
            revert CreditPolicy__InvalidVersion();
        }
        if (policyCreated[version]) {
            revert CreditPolicy__PolicyVersionExists(version);
        }

        policyCreated[version] = true;
        policyActive[version] = true;
        lastUpdated[version] = block.timestamp;
        emit PolicyCreated(version, block.timestamp);
    }

    function freezePolicy(
        uint256 version
    ) external onlyAdmin policyExists(version) {
        if (policyFrozen[version]) {
            revert CreditPolicy__PolicyFrozen(version);
        }
        if (policyActive[version] == false) {
            revert CreditPolicy__PolicyNotActive(version);
        }
        if (
            !eligibilitySet[version] ||
            !ratiosSet[version] ||
            !concentrationSet[version] ||
            !attestationSet[version] ||
            !covenantsSet[version] ||
            !hasAtLeastOneTier[version]
        ) {
            revert CreditPolicy__IncompletePolicy(version);
        }
        if (policyDocumentHash[version] == bytes32(0)) {
            revert CreditPolicy__IncompletePolicy(version);
        }

        policyFrozen[version] = true;
        lastUpdated[version] = block.timestamp;
        emit PolicyFrozen(version, block.timestamp);
    }

    function deActivatePolicy(
        uint256 version
    ) external onlyAdmin policyExists(version) {
        policyActive[version] = false;
        lastUpdated[version] = block.timestamp;
        emit PolicyDeactivated(version, block.timestamp);
    }

    /*//////////////////////////////////////////////////////////////
                        ELIGIBILITY UPDATE
    //////////////////////////////////////////////////////////////*/
    function updateEligibility(
        uint256 version,
        EligibilityCriteria calldata data
    ) external onlyAdmin policyExists(version) policyEditable(version) {
        eligibility[version] = data;
        lastUpdated[version] = block.timestamp;
        eligibilitySet[version] = true;
        emit PolicyEligibilityUpdated(version, block.timestamp);
    }

    /*//////////////////////////////////////////////////////////////
                        RATIOS UPDATE
    //////////////////////////////////////////////////////////////*/
    function updateRatios(
        uint256 version,
        FinancialRatios calldata data
    ) external onlyAdmin policyExists(version) policyEditable(version) {
        ratios[version] = data;
        lastUpdated[version] = block.timestamp;
        ratiosSet[version] = true;
        emit PolicyRatiosUpdated(version, block.timestamp);
    }

    /*//////////////////////////////////////////////////////////////
                        CONCENTRATION UPDATE
    //////////////////////////////////////////////////////////////*/
    function updateConcentration(
        uint256 version,
        ConcentrationLimits calldata data
    ) external onlyAdmin policyExists(version) policyEditable(version) {
        concentration[version] = data;
        lastUpdated[version] = block.timestamp;
        concentrationSet[version] = true;
        emit PolicyConcentrationUpdated(version, block.timestamp);
    }

    /*//////////////////////////////////////////////////////////////
                        ATTESTATION UPDATE
    //////////////////////////////////////////////////////////////*/
    function updateAttestation(
        uint256 version,
        AttestationRequirements calldata data
    ) external onlyAdmin policyExists(version) policyEditable(version) {
        attestation[version] = data;
        lastUpdated[version] = block.timestamp;
        attestationSet[version] = true;
        emit PolicyAttestationUpdated(version, block.timestamp);
    }

    /*//////////////////////////////////////////////////////////////
                        COVENANT UPDATE
    //////////////////////////////////////////////////////////////*/
    function updateCovenants(
        uint256 version,
        MaintenanceCovenants calldata data
    ) external onlyAdmin policyExists(version) policyEditable(version) {
        covenants[version] = data;
        lastUpdated[version] = block.timestamp;
        covenantsSet[version] = true;
        emit PolicyCovenantsUpdated(version, block.timestamp);
    }

    /*//////////////////////////////////////////////////////////////
                        LOAN TIERS
    //////////////////////////////////////////////////////////////*/
    function setLoanTier(
        uint256 version,
        uint8 tierId,
        LoanTier calldata tier
    ) external onlyAdmin policyExists(version) policyEditable(version) {
        if (tierId >= maxTiers) {
            revert CreditPolicy__InvalidTierCount(tierId);
        }
        console.log("here");
        loanTiers[version][tierId] = tier;
        tierExists[version][tierId] = true;
        if (tierId >= totalTiers[version]) {
            totalTiers[version] = tierId + 1;
        }
        hasAtLeastOneTier[version] = true;
        lastUpdated[version] = block.timestamp;
        emit LoanTierUpdated(version, tierId, block.timestamp);
    }

    /*//////////////////////////////////////////////////////////////
                        INDUSTRY CONTROLS
    //////////////////////////////////////////////////////////////*/
    function excludeIndustry(
        uint256 version,
        bytes32 industry
    ) external onlyAdmin policyExists(version) policyEditable(version) {
        if (industry == bytes32(0)) {
            revert CreditPolicy__InvalidIndustryHash();
        }
        excludedIndustries[version][industry] = true;
        lastUpdated[version] = block.timestamp;
        emit IndustryExcluded(version, industry, block.timestamp);
    }

    function includeIndustry(
        uint256 version,
        bytes32 industry
    ) external onlyAdmin policyExists(version) policyEditable(version) {
        if (industry == bytes32(0)) {
            revert CreditPolicy__InvalidIndustryHash();
        }
        excludedIndustries[version][industry] = false;
        lastUpdated[version] = block.timestamp;
        emit IndustryIncluded(version, industry, block.timestamp);
    }

    /*//////////////////////////////////////////////////////////////
                        DOCUMENT UPDATE
    //////////////////////////////////////////////////////////////*/
    function setPolicyDocument(
        uint256 version,
        bytes32 hash,
        string calldata uri
    ) external onlyAdmin policyExists(version) policyEditable(version) {
        policyDocumentHash[version] = hash;
        policyDocumentURI[version] = uri;
        lastUpdated[version] = block.timestamp;

        emit PolicyDocumentSet(version, hash, uri, block.timestamp);
    }

    function changePolicyAdmin(address newAdmin) external onlyAdmin {
        if (newAdmin == address(0)) {
            revert CreditPolicy__InvalidAdmin();
        }
        policyAdmin = newAdmin;

        emit PolicyAdminChanged(newAdmin);
    }

    // getters for interface compliance

    function isPolicyActive(uint256 version) external view returns (bool) {
        return policyActive[version];
    }

    function isPolicyFrozen(uint256 version) external view returns (bool) {
        return policyFrozen[version];
    }

    function tierExistsInPolicy(
        uint256 version,
        uint8 tierId
    ) external view returns (bool) {
        return tierExists[version][tierId];
    }

    function setMaxTiers(uint8 _maxTiers) external onlyAdmin {
        if (_maxTiers == 255) {
            revert CreditPolicy__InvalidTierCount(_maxTiers);
        }
        maxTiers = _maxTiers;
        emit MaxTiersChanged(_maxTiers);
    }

    function getMaxTiers() external view returns (uint8) {
        return maxTiers;
    }
}
