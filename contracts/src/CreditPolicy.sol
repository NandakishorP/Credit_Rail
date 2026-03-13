// SPDX-License-Identifier: MIT
pragma solidity 0.8.30;
import {ICreditPolicy} from "./interfaces/ICreditPolicy.sol";
import {AccessControlUpgradeable} from "@openzeppelin/contracts-upgradeable/access/AccessControlUpgradeable.sol";
import {UUPSUpgradeable} from "@openzeppelin/contracts-upgradeable/proxy/utils/UUPSUpgradeable.sol";
import {Initializable} from "@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol";
import {IPoseidon2} from "./interfaces/IPoseidon2.sol";
import {Field} from "@poseidon2-evm/Field.sol";

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
 *      Access is controlled via OpenZeppelin's AccessControl with granular
 *      roles (POLICY_ADMIN, POLICY_EDITOR, INDUSTRY_ADMIN). In production,
 *      DEFAULT_ADMIN_ROLE should be held by a ProtocolController (timelock + multisig).
 */
contract CreditPolicy is
    ICreditPolicy,
    Initializable,
    AccessControlUpgradeable,
    UUPSUpgradeable
{
    /*//////////////////////////////////////////////////////////////
                                ERRORS
    //////////////////////////////////////////////////////////////*/
    error CreditPolicy__PolicyFrozen(uint256 version);
    error CreditPolicy__InvalidVersion();
    error CreditPolicy__PolicyVersionExists(uint256 version);
    error CreditPolicy__PolicyNotEditable(uint256 version);
    error CreditPolicy__IncompletePolicy(uint256 version);
    error CreditPolicy__InvalidIndustryHash();
    error CreditPolicy__PolicyNotActive(uint256 version);
    error CreditPolicy__InvalidTierCount(uint256 count);
    error CreditPolicy__ValueExceedsU64(string field, uint256 value);
    error CreditPolicy__ZeroAddress();

    /*//////////////////////////////////////////////////////////////
                         ACCESS CONTROL ROLES
    //////////////////////////////////////////////////////////////*/

    bytes32 public constant POLICY_ADMIN_ROLE = keccak256("POLICY_ADMIN_ROLE");
    bytes32 public constant POLICY_EDITOR_ROLE =
        keccak256("POLICY_EDITOR_ROLE");
    bytes32 public constant INDUSTRY_ADMIN_ROLE =
        keccak256("INDUSTRY_ADMIN_ROLE");

    /*//////////////////////////////////////////////////////////////
                                MODIFIERS
    //////////////////////////////////////////////////////////////*/

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

    /// @dev Reverts if `value` exceeds the u64 range expected by the Noir ZK circuit.
    ///      All numeric policy parameters that feed into `compute_policy_hash()` in the
    ///      circuit are typed as `u64`. Storing a value > type(uint64).max on-chain would
    ///      make proof generation impossible, bricking the policy version.
    function _requireU64(string memory field, uint256 value) internal pure {
        if (value > type(uint64).max) {
            revert CreditPolicy__ValueExceedsU64(field, value);
        }
    }

    /*//////////////////////////////////////////////////////////////
                                CORE STATE
    //////////////////////////////////////////////////////////////*/
    uint8 internal maxTiers;
    IPoseidon2 public i_poseidon2;

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
    // Stored per (version, tierId) since each (policy, tier) combination
    // produces a unique Poseidon2 hash in the Noir circuit.
    mapping(uint256 => mapping(uint8 => bytes32)) internal _policyScopeHashes;

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

    event DefaultAdminChanged(
        address indexed previousAdmin,
        address indexed newAdmin
    );
    event OperationalRolesGranted(address indexed account);
    event OperationalRolesRevoked(address indexed account);

    event PolicyDocumentSet(
        uint256 version,
        bytes32 hash,
        string uri,
        uint256 timestamp
    );
    event PolicyScopeHashSet(uint256 version, bytes32 hash, uint256 timestamp);
    event PolicyDeactivated(uint256 version, uint256 timestamp);

    /*//////////////////////////////////////////////////////////////
                            INITIALIZER
    //////////////////////////////////////////////////////////////*/

    /// @custom:oz-upgrades-unsafe-allow constructor
    constructor() {
        _disableInitializers();
    }

    /// @notice Initialize the CreditPolicy proxy, granting all roles to `initialAdmin`.
    /// @dev Can only be called once (via proxy). In production, `initialAdmin`
    ///      should be the ProtocolController (timelock + multisig).
    /// @param initialAdmin The address to receive all admin roles.
    function initialize(address initialAdmin, address poseidon2_) external initializer {
        if (poseidon2_ == address(0)) revert CreditPolicy__ZeroAddress();
        __AccessControl_init();
        i_poseidon2 = IPoseidon2(poseidon2_);
        _grantRole(DEFAULT_ADMIN_ROLE, initialAdmin);
        _grantRole(POLICY_ADMIN_ROLE, initialAdmin);
        _grantRole(POLICY_EDITOR_ROLE, initialAdmin);
        _grantRole(INDUSTRY_ADMIN_ROLE, initialAdmin);
    }

    /// @dev Only DEFAULT_ADMIN_ROLE can authorize upgrades.
    function _authorizeUpgrade(
        address newImplementation
    ) internal override onlyRole(DEFAULT_ADMIN_ROLE) {}

    /*//////////////////////////////////////////////////////////////
                        POLICY CREATION
    //////////////////////////////////////////////////////////////*/

    /// @notice Create a new policy version.
    /// @dev The version is created in an active, editable (unfrozen) state.
    ///      All required sections must be populated before the policy can be frozen.
    /// @param version The version number to create (must be > 0 and not already exist).
    function createPolicy(
        uint256 version
    ) external onlyRole(POLICY_ADMIN_ROLE) {
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
    ///      attestation, covenants, at least one tier, and document hash.
    ///      Internally computes the Poseidon2 policyScopeHash for each tier,
    ///      matching the Noir circuit's `compute_policy_hash()` exactly.
    ///      Once frozen, the policy can never be edited again.
    /// @param version The version number to freeze.
    function freezePolicy(
        uint256 version
    ) external onlyRole(POLICY_ADMIN_ROLE) policyExists(version) {
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

        // Compute Poseidon2 scope hash for each tier (matches Noir circuit's compute_policy_hash)
        EligibilityCriteria storage e = eligibility[version];
        FinancialRatios storage r = ratios[version];
        AttestationRequirements storage a = attestation[version];

        uint8 numTiers = totalTiers[version];
        for (uint8 t = 0; t < numTiers; t++) {
            if (!tierExists[version][t]) continue;
            LoanTier storage tier = loanTiers[version][t];

            // 21 elements — exactly matching Noir's compute_policy_hash order
            Field.Type[] memory inputs = new Field.Type[](21);
            inputs[0]  = Field.toField(e.minAnnualRevenue);
            inputs[1]  = Field.toField(e.minEBITDA);
            inputs[2]  = Field.toField(e.minTangibleNetWorth);
            inputs[3]  = Field.toField(e.minBusinessAgeDays);
            inputs[4]  = Field.toField(e.maxDefaultsLast36Months);
            inputs[5]  = Field.toField(e.bankruptcyExcluded ? 1 : 0);
            inputs[6]  = Field.toField(r.maxTotalDebtToEBITDA);
            inputs[7]  = Field.toField(r.minInterestCoverageRatio);
            inputs[8]  = Field.toField(r.minCurrentRatio);
            inputs[9]  = Field.toField(r.minEBITDAMarginBps);
            inputs[10] = Field.toField(a.maxAttestationAgeDays);
            // Tier constraints
            inputs[11] = Field.toField(uint256(t));
            inputs[12] = Field.toField(tier.minRevenue);
            inputs[13] = Field.toField(tier.maxRevenue);
            inputs[14] = Field.toField(tier.minEBITDA);
            inputs[15] = Field.toField(tier.maxDebtToEBITDA);
            inputs[16] = Field.toField(tier.maxLoanToEBITDA);
            inputs[17] = Field.toField(tier.interestRateBps);
            inputs[18] = Field.toField(tier.originationFeeBps);
            inputs[19] = Field.toField(tier.termDays);
            inputs[20] = Field.toField(tier.active ? 1 : 0);

            bytes32 hash = bytes32(Field.toUint256(i_poseidon2.hash(inputs)));
            _policyScopeHashes[version][t] = hash;
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
    ) external onlyRole(POLICY_ADMIN_ROLE) policyExists(version) {
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
    )
        external
        onlyRole(POLICY_EDITOR_ROLE)
        policyExists(version)
        policyEditable(version)
    {
        _requireU64("minAnnualRevenue", data.minAnnualRevenue);
        _requireU64("minEBITDA", data.minEBITDA);
        _requireU64("minTangibleNetWorth", data.minTangibleNetWorth);
        _requireU64("minBusinessAgeDays", data.minBusinessAgeDays);
        _requireU64("maxDefaultsLast36Months", data.maxDefaultsLast36Months);

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
    )
        external
        onlyRole(POLICY_EDITOR_ROLE)
        policyExists(version)
        policyEditable(version)
    {
        _requireU64("maxTotalDebtToEBITDA", data.maxTotalDebtToEBITDA);
        _requireU64("minInterestCoverageRatio", data.minInterestCoverageRatio);
        _requireU64("minCurrentRatio", data.minCurrentRatio);
        _requireU64("minEBITDAMarginBps", data.minEBITDAMarginBps);

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
    )
        external
        onlyRole(POLICY_EDITOR_ROLE)
        policyExists(version)
        policyEditable(version)
    {
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
    )
        external
        onlyRole(POLICY_EDITOR_ROLE)
        policyExists(version)
        policyEditable(version)
    {
        _requireU64("maxAttestationAgeDays", data.maxAttestationAgeDays);

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
    )
        external
        onlyRole(POLICY_EDITOR_ROLE)
        policyExists(version)
        policyEditable(version)
    {
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
    )
        external
        onlyRole(POLICY_EDITOR_ROLE)
        policyExists(version)
        policyEditable(version)
    {
        if (tierId >= maxTiers) {
            revert CreditPolicy__InvalidTierCount(tierId);
        }

        _requireU64("tier.minRevenue", tier.minRevenue);
        _requireU64("tier.maxRevenue", tier.maxRevenue);
        _requireU64("tier.minEBITDA", tier.minEBITDA);
        _requireU64("tier.maxDebtToEBITDA", tier.maxDebtToEBITDA);
        _requireU64("tier.maxLoanToEBITDA", tier.maxLoanToEBITDA);
        _requireU64("tier.interestRateBps", tier.interestRateBps);
        _requireU64("tier.originationFeeBps", tier.originationFeeBps);
        _requireU64("tier.termDays", tier.termDays);

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
    )
        external
        onlyRole(INDUSTRY_ADMIN_ROLE)
        policyExists(version)
        policyEditable(version)
    {
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
    )
        external
        onlyRole(INDUSTRY_ADMIN_ROLE)
        policyExists(version)
        policyEditable(version)
    {
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
    )
        external
        onlyRole(POLICY_EDITOR_ROLE)
        policyExists(version)
        policyEditable(version)
    {
        policyDocumentHash[version] = hash;
        policyDocumentURI[version] = uri;
        lastUpdated[version] = block.timestamp;

        emit PolicyDocumentSet(version, hash, uri, block.timestamp);
    }

    /// @notice Returns the Poseidon2 scope hash for a specific (version, tierId) pair.
    /// @dev Computed automatically during `freezePolicy()`. Matches the Noir
    ///      circuit's `compute_policy_hash()` output.
    /// @param version The policy version.
    /// @param tierId  The tier index.
    /// @return The Poseidon2 hash binding all policy + tier parameters.
    function policyScopeHash(
        uint256 version,
        uint8 tierId
    ) external view returns (bytes32) {
        return _policyScopeHashes[version][tierId];
    }

    /// @notice Transfer the DEFAULT_ADMIN_ROLE to a new address.
    /// @dev Grants DEFAULT_ADMIN_ROLE to `newAdmin` and revokes it from the caller.
    ///      This is the most sensitive operation — it controls who can authorize
    ///      contract upgrades and manage all other roles. Use with extreme caution.
    /// @param newAdmin The address to become the new default admin (must not be zero).
    function changeDefaultAdmin(
        address newAdmin
    ) external onlyRole(DEFAULT_ADMIN_ROLE) {
        if (newAdmin == address(0)) revert CreditPolicy__ZeroAddress();

        address previousAdmin = msg.sender;
        grantRole(DEFAULT_ADMIN_ROLE, newAdmin);
        revokeRole(DEFAULT_ADMIN_ROLE, previousAdmin);

        emit DefaultAdminChanged(previousAdmin, newAdmin);
    }

    /// @notice Grant POLICY_ADMIN_ROLE to an address (can create/freeze policies).
    /// @param account The address to receive the role (must not be zero).
    function grantPolicyAdminRole(
        address account
    ) external onlyRole(DEFAULT_ADMIN_ROLE) {
        if (account == address(0)) revert CreditPolicy__ZeroAddress();
        grantRole(POLICY_ADMIN_ROLE, account);
    }

    /// @notice Revoke POLICY_ADMIN_ROLE from an address.
    /// @param account The address to lose the role (must not be zero).
    function revokePolicyAdminRole(
        address account
    ) external onlyRole(DEFAULT_ADMIN_ROLE) {
        if (account == address(0)) revert CreditPolicy__ZeroAddress();
        revokeRole(POLICY_ADMIN_ROLE, account);
    }

    /// @notice Grant POLICY_EDITOR_ROLE to an address (can edit policy sections).
    /// @param account The address to receive the role (must not be zero).
    function grantPolicyEditorRole(
        address account
    ) external onlyRole(DEFAULT_ADMIN_ROLE) {
        if (account == address(0)) revert CreditPolicy__ZeroAddress();
        grantRole(POLICY_EDITOR_ROLE, account);
    }

    /// @notice Revoke POLICY_EDITOR_ROLE from an address.
    /// @param account The address to lose the role (must not be zero).
    function revokePolicyEditorRole(
        address account
    ) external onlyRole(DEFAULT_ADMIN_ROLE) {
        if (account == address(0)) revert CreditPolicy__ZeroAddress();
        revokeRole(POLICY_EDITOR_ROLE, account);
    }

    /// @notice Grant INDUSTRY_ADMIN_ROLE to an address (can manage industry exclusions).
    /// @param account The address to receive the role (must not be zero).
    function grantIndustryAdminRole(
        address account
    ) external onlyRole(DEFAULT_ADMIN_ROLE) {
        if (account == address(0)) revert CreditPolicy__ZeroAddress();
        grantRole(INDUSTRY_ADMIN_ROLE, account);
    }

    /// @notice Revoke INDUSTRY_ADMIN_ROLE from an address.
    /// @param account The address to lose the role (must not be zero).
    function revokeIndustryAdminRole(
        address account
    ) external onlyRole(DEFAULT_ADMIN_ROLE) {
        if (account == address(0)) revert CreditPolicy__ZeroAddress();
        revokeRole(INDUSTRY_ADMIN_ROLE, account);
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
    function setMaxTiers(uint8 _maxTiers) external onlyRole(POLICY_ADMIN_ROLE) {
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

    /*//////////////////////////////////////////////////////////////
                        STORAGE GAP
    //////////////////////////////////////////////////////////////*/

    /// @dev Reserved storage for future upgrades.
    uint256[50] private __gap;
}
