// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import {ICreditPolicy} from "./interfaces/ICreditPolicy.sol";

/**
 * @title CreditPolicy
 * @notice Immutable-by-version credit constitution for private credit funds.
 * @dev Each policy version goes through a lifecycle: Created → Editable → Frozen.
 *      Once frozen, a policy version can never be modified, ensuring that ZK proofs
 *      generated against a specific version remain valid forever.
 *
 *      A policy version contains:
 *        - Eligibility criteria (minimum revenue, EBITDA, net worth, etc.)
 *        - Financial ratio requirements (debt/EBITDA, coverage, etc.)
 *        - Loan tiers with pricing parameters (APR, fees, term)
 *        - Concentration limits (single borrower, industry caps)
 *        - Attestation requirements (CPA attestation age, frequency)
 *        - Maintenance covenants (leverage, coverage, reporting)
 *        - Industry exclusion list
 *        - Document hash and URI for legal anchoring
 *        - Policy scope hash (binds all parameters for ZK circuit verification)
 *
 *      Access is controlled by a single `policyAdmin` address which should
 *      be set to a ProtocolController (timelock + multisig) in production.
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
    mapping(uint256 => bool) internal policyFrozen;
    mapping(uint256 => bool) internal policyActive;
    mapping(uint256 => uint256) public lastUpdated;

    /*//////////////////////////////////////////////////////////////
                        ELIGIBILITY (PRE-LOAN)
    //////////////////////////////////////////////////////////////*/
    // Struct defined in ICreditPolicy interface

    mapping(uint256 => EligibilityCriteria) public eligibility;

    /*//////////////////////////////////////////////////////////////
                        FINANCIAL RATIOS (UNDERWRITING)
    //////////////////////////////////////////////////////////////*/
    // Struct defined in ICreditPolicy interface

    mapping(uint256 => FinancialRatios) public ratios;

    /*//////////////////////////////////////////////////////////////
                        LOAN TIERS (PRICING REFERENCE)
    //////////////////////////////////////////////////////////////*/
    // Struct defined in ICreditPolicy interface

    mapping(uint256 => mapping(uint8 => LoanTier)) public loanTiers;
    mapping(uint256 => uint8) public totalTiers;
    mapping(uint256 => mapping(uint8 => bool)) internal tierExists;

    /*//////////////////////////////////////////////////////////////
                        CONCENTRATION LIMITS
    //////////////////////////////////////////////////////////////*/
    // Struct defined in ICreditPolicy interface

    mapping(uint256 => ConcentrationLimits) public concentration;

    /*//////////////////////////////////////////////////////////////
                        INDUSTRY EXCLUSIONS
    //////////////////////////////////////////////////////////////*/
    mapping(uint256 => mapping(bytes32 => bool)) internal excludedIndustries;

    /*//////////////////////////////////////////////////////////////
                        ATTESTATION REQUIREMENTS
    //////////////////////////////////////////////////////////////*/
    // Struct defined in ICreditPolicy interface

    mapping(uint256 => AttestationRequirements) public attestation;

    /*//////////////////////////////////////////////////////////////
                        MAINTENANCE COVENANTS
    //////////////////////////////////////////////////////////////*/
    // Struct defined in ICreditPolicy interface

    mapping(uint256 => MaintenanceCovenants) public covenants;

    /*//////////////////////////////////////////////////////////////
                        DOCUMENT ANCHORING
    //////////////////////////////////////////////////////////////*/
    mapping(uint256 => bytes32) public policyDocumentHash;
    mapping(uint256 => string) public policyDocumentURI;

    // Computational hash of policy parameters (must match circuit)
    mapping(uint256 => bytes32) public policyScopeHash;

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
    event PolicyScopeHashSet(uint256 version, bytes32 hash, uint256 timestamp);
    event PolicyDeactivated(uint256 version, uint256 timestamp);

    /*//////////////////////////////////////////////////////////////
                                CONSTRUCTOR
    //////////////////////////////////////////////////////////////*/

    /// @notice Deploy a new CreditPolicy, setting `msg.sender` as the initial admin.
    constructor() {
        policyAdmin = msg.sender;
    }

    /*//////////////////////////////////////////////////////////////
                        POLICY CREATION
    //////////////////////////////////////////////////////////////*/

    /// @notice Create a new policy version.
    /// @dev The version is created in an active, editable (unfrozen) state.
    ///      All required sections must be populated before the policy can be frozen.
    /// @param version The version number to create (must be > 0 and not already exist).
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

    /// @notice Freeze a policy version, making it permanently immutable.
    /// @dev Requires all sections to be set: eligibility, ratios, concentration,
    ///      attestation, covenants, at least one tier, document hash, and scope hash.
    ///      Once frozen, the policy can never be edited again. This is the state
    ///      required for `LoanEngine.createLoan()` to accept proofs against it.
    /// @param version The version number to freeze.
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
        if (policyScopeHash[version] == bytes32(0)) {
            revert CreditPolicy__IncompletePolicy(version);
        }

        policyFrozen[version] = true;
        lastUpdated[version] = block.timestamp;
        emit PolicyFrozen(version, block.timestamp);
    }

    /// @notice Deactivate a policy version (prevents new loans, but existing loans are unaffected).
    /// @dev A deactivated policy cannot be used for new loan creation.
    ///      Unlike freezing, deactivation does not require all sections to be set.
    /// @param version The version number to deactivate.
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

    /// @notice Set or update the borrower eligibility criteria for a policy version.
    /// @dev Can only be called while the policy is active and not frozen.
    /// @param version The policy version to update.
    /// @param data    The eligibility criteria struct (min revenue, EBITDA, net worth, etc.).
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

    /// @notice Set or update the financial ratio requirements for a policy version.
    /// @param version The policy version to update.
    /// @param data    The financial ratios struct (max debt/EBITDA, min coverage, etc.).
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

    /// @notice Set or update the concentration limits for a policy version.
    /// @param version The policy version to update.
    /// @param data    The concentration limits struct (max single borrower, max industry %).
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

    /// @notice Set or update the attestation requirements for a policy version.
    /// @param version The policy version to update.
    /// @param data    The attestation requirements struct (max age, frequency, CPA required).
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

    /// @notice Set or update the maintenance covenants for a policy version.
    /// @param version The policy version to update.
    /// @param data    The covenants struct (leverage, coverage, liquidity, dividends, reporting).
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

    /// @notice Set or update a loan tier within a policy version.
    /// @dev Tiers define pricing bands (APR, fees, term) based on borrower metrics.
    ///      The tier ID must be less than `maxTiers`. Setting the first tier
    ///      automatically marks the policy as having at least one tier.
    /// @param version The policy version to update.
    /// @param tierId  The tier index (0-based, must be < maxTiers).
    /// @param tier    The LoanTier struct with pricing and eligibility bounds.
    function setLoanTier(
        uint256 version,
        uint8 tierId,
        LoanTier calldata tier
    ) external onlyAdmin policyExists(version) policyEditable(version) {
        if (tierId >= maxTiers) {
            revert CreditPolicy__InvalidTierCount(tierId);
        }
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

    /// @notice Exclude an industry from a policy version (loans in this industry will be rejected).
    /// @param version  The policy version to update.
    /// @param industry Keccak256 hash of the industry code (must be non-zero).
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

    /// @notice Re-include a previously excluded industry.
    /// @param version  The policy version to update.
    /// @param industry Keccak256 hash of the industry code to re-include.
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

    /// @notice Anchor a legal document to a policy version.
    /// @dev Both the hash and URI are stored. The hash ensures document integrity;
    ///      the URI provides retrieval (e.g. IPFS). Required before freezing.
    /// @param version The policy version to update.
    /// @param hash    Keccak256 hash of the policy document content.
    /// @param uri     URI where the document can be retrieved (e.g. "ipfs://...").
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

    /// @notice Set the policy scope hash — a Poseidon2 hash of all policy parameters.
    /// @dev This hash is what the Noir ZK circuit uses to verify that the proof
    ///      was generated against the correct frozen policy. It must be computed
    ///      off-chain (matching the circuit's `compute_policy_hash()`) and set
    ///      before the policy can be frozen.
    /// @param version The policy version to update.
    /// @param hash    The Poseidon2 hash of all policy parameters (computed off-chain).
    function setPolicyScopeHash(
        uint256 version,
        bytes32 hash
    ) external onlyAdmin policyExists(version) policyEditable(version) {
        policyScopeHash[version] = hash;
        lastUpdated[version] = block.timestamp;

        emit PolicyScopeHashSet(version, hash, block.timestamp);
    }

    /// @notice Transfer policy admin rights to a new address.
    /// @dev In production, this should be a ProtocolController address.
    /// @param newAdmin The address to become the new policy admin (must be non-zero).
    function changePolicyAdmin(address newAdmin) external onlyAdmin {
        if (newAdmin == address(0)) {
            revert CreditPolicy__InvalidAdmin();
        }
        policyAdmin = newAdmin;

        emit PolicyAdminChanged(newAdmin);
    }

    /*//////////////////////////////////////////////////////////////
                            VIEW FUNCTIONS
    //////////////////////////////////////////////////////////////*/

    /// @notice Check if a policy version is currently active.
    /// @param version The policy version to query.
    /// @return True if the policy is active (can be used or edited).
    function isPolicyActive(uint256 version) external view returns (bool) {
        return policyActive[version];
    }

    /// @notice Check if a policy version has been permanently frozen.
    /// @param version The policy version to query.
    /// @return True if the policy is frozen (immutable, usable for loan creation).
    function isPolicyFrozen(uint256 version) external view returns (bool) {
        return policyFrozen[version];
    }

    /// @notice Check if a specific tier exists within a policy version.
    /// @param version The policy version to query.
    /// @param tierId  The tier index to check.
    /// @return True if the tier has been set for this policy version.
    function tierExistsInPolicy(
        uint256 version,
        uint8 tierId
    ) external view returns (bool) {
        return tierExists[version][tierId];
    }

    /// @notice Set the global maximum number of tiers allowed per policy.
    /// @param _maxTiers The new max tier count (must be < 255).
    function setMaxTiers(uint8 _maxTiers) external onlyAdmin {
        if (_maxTiers == 255) {
            revert CreditPolicy__InvalidTierCount(_maxTiers);
        }
        maxTiers = _maxTiers;
        emit MaxTiersChanged(_maxTiers);
    }

    /// @notice Returns the current maximum tier count.
    function getMaxTiers() external view returns (uint8) {
        return maxTiers;
    }

    /// @notice Check if an industry is excluded from a policy version.
    /// @param version  The policy version to query.
    /// @param industry Keccak256 hash of the industry code.
    /// @return True if the industry is excluded (loans in this industry are rejected).
    function isIndustryExcluded(
        uint256 version,
        bytes32 industry
    ) external view returns (bool) {
        return excludedIndustries[version][industry];
    }
}
