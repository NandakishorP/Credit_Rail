// SPDX-License-Identifier: MIT
pragma solidity 0.8.30;
import {ICreditPolicy} from "./interfaces/ICreditPolicy.sol";
import {AccessControlUpgradeable} from "@openzeppelin/contracts-upgradeable/access/AccessControlUpgradeable.sol";
import {UUPSUpgradeable} from "@openzeppelin/contracts-upgradeable/proxy/utils/UUPSUpgradeable.sol";
import {Initializable} from "@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol";

/**
 * @title CreditPolicy
 * @notice On-chain policy registry for privacy-preserving private credit funds.
 * @dev Each policy version goes through a lifecycle: Created → Editable → Frozen.
 *      Once frozen, a policy version can never be modified, ensuring that ZK proofs
 *      generated against a specific version remain valid forever.
 *
 *      Policy parameters (eligibility criteria, financial ratios, loan tiers, etc.)
 *      are stored OFF-CHAIN to protect the fund manager's underwriting IP. Only the
 *      Poseidon2 scope hash (computed off-chain) is committed on-chain per (version, tierId)
 *      pair. LPs can verify the hash matches what they were shown under NDA.
 *
 *      A policy version contains on-chain:
 *        - Policy scope hashes per tier (binding ZK proofs to policy parameters)
 *        - Industry exclusion list (dynamic, checked on-chain by LoanEngine)
 *        - Document hash and URI for legal anchoring
 *
 *      Access is controlled via OpenZeppelin's AccessControl with granular
 *      roles (POLICY_ADMIN, INDUSTRY_ADMIN). In production,
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
    error CreditPolicy__ZeroAddress();
    error CreditPolicy__InvalidScopeHash();

    /*//////////////////////////////////////////////////////////////
                         ACCESS CONTROL ROLES
    //////////////////////////////////////////////////////////////*/

    bytes32 public constant POLICY_ADMIN_ROLE = keccak256("POLICY_ADMIN_ROLE");
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

    /*//////////////////////////////////////////////////////////////
                            POLICY LIFECYCLE
    //////////////////////////////////////////////////////////////*/
    mapping(uint256 => bool) public policyCreated;
    mapping(uint256 => bool) internal policyFrozen;
    mapping(uint256 => bool) internal policyActive;
    mapping(uint256 => uint256) public lastUpdated;

    /*//////////////////////////////////////////////////////////////
                        POLICY SCOPE HASHES
    //////////////////////////////////////////////////////////////*/
    // Poseidon2 hash of all policy + tier parameters, computed OFF-CHAIN.
    // Stored per (version, tierId) since each (policy, tier) combination
    // produces a unique hash in the Noir circuit.
    mapping(uint256 => mapping(uint8 => bytes32)) internal _policyScopeHashes;

    // Track which tiers have been registered (derived from scope hash setting)
    mapping(uint256 => mapping(uint8 => bool)) internal tierExists;

    // At least one scope hash must be set before freezing
    mapping(uint256 => bool) public hasScopeHash;

    /*//////////////////////////////////////////////////////////////
                        INDUSTRY EXCLUSIONS
    //////////////////////////////////////////////////////////////*/
    mapping(uint256 => mapping(bytes32 => bool)) internal excludedIndustries;

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
    event PolicyScopeHashSet(
        uint256 version,
        uint8 tierId,
        bytes32 hash,
        uint256 timestamp
    );
    event IndustryExcluded(
        uint256 version,
        bytes32 industry,
        uint256 timestamp
    );
    event IndustryIncluded(
        uint256 version,
        bytes32 industry,
        uint256 timestamp
    );

    event DefaultAdminChanged(
        address indexed previousAdmin,
        address indexed newAdmin
    );

    event PolicyDocumentSet(
        uint256 version,
        bytes32 hash,
        string uri,
        uint256 timestamp
    );
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
    function initialize(address initialAdmin) external initializer {
        __AccessControl_init();
        _grantRole(DEFAULT_ADMIN_ROLE, initialAdmin);
        _grantRole(POLICY_ADMIN_ROLE, initialAdmin);
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
    ///      Scope hashes and document must be set before the policy can be frozen.
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
    /// @dev Requires at least one scope hash and a document hash to be set.
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
        if (!hasScopeHash[version]) {
            revert CreditPolicy__IncompletePolicy(version);
        }
        if (policyDocumentHash[version] == bytes32(0)) {
            revert CreditPolicy__IncompletePolicy(version);
        }

        policyFrozen[version] = true;
        lastUpdated[version] = block.timestamp;
        emit PolicyFrozen(version, block.timestamp);
    }

    /// @notice Deactivate a policy version (prevents new loans, but existing loans are unaffected).
    /// @dev A deactivated policy cannot be used for new loan creation.
    ///      Unlike freezing, deactivation does not require completeness.
    /// @param version The version number to deactivate.
    function deActivatePolicy(
        uint256 version
    ) external onlyRole(POLICY_ADMIN_ROLE) policyExists(version) {
        policyActive[version] = false;
        lastUpdated[version] = block.timestamp;
        emit PolicyDeactivated(version, block.timestamp);
    }

    /*//////////////////////////////////////////////////////////////
                        SCOPE HASH MANAGEMENT
    //////////////////////////////////////////////////////////////*/

    /// @notice Set the Poseidon2 scope hash for a specific (version, tierId) pair.
    /// @dev The hash is computed OFF-CHAIN from all policy + tier parameters and
    ///      must match the Noir circuit's `compute_policy_hash()` output exactly.
    ///      Setting a scope hash also registers the tier as existing for this version.
    /// @param version The policy version.
    /// @param tierId  The tier index.
    /// @param hash    The Poseidon2 hash binding all policy + tier parameters.
    function setPolicyScopeHash(
        uint256 version,
        uint8 tierId,
        bytes32 hash
    )
        external
        onlyRole(POLICY_ADMIN_ROLE)
        policyExists(version)
        policyEditable(version)
    {
        if (hash == bytes32(0)) {
            revert CreditPolicy__InvalidScopeHash();
        }
        _policyScopeHashes[version][tierId] = hash;
        tierExists[version][tierId] = true;
        hasScopeHash[version] = true;
        lastUpdated[version] = block.timestamp;
        emit PolicyScopeHashSet(version, tierId, hash, block.timestamp);
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
        onlyRole(POLICY_ADMIN_ROLE)
        policyExists(version)
        policyEditable(version)
    {
        policyDocumentHash[version] = hash;
        policyDocumentURI[version] = uri;
        lastUpdated[version] = block.timestamp;

        emit PolicyDocumentSet(version, hash, uri, block.timestamp);
    }

    /*//////////////////////////////////////////////////////////////
                            ROLE MANAGEMENT
    //////////////////////////////////////////////////////////////*/

    /// @notice Returns the Poseidon2 scope hash for a specific (version, tierId) pair.
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

    /// @notice Grant POLICY_ADMIN_ROLE to an address.
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
    /// @return True if the policy is active.
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
    /// @dev A tier exists if a scope hash has been set for it.
    /// @param version The policy version to query.
    /// @param tierId  The tier index to check.
    /// @return True if the tier has a scope hash set for this policy version.
    function tierExistsInPolicy(
        uint256 version,
        uint8 tierId
    ) external view returns (bool) {
        return tierExists[version][tierId];
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
