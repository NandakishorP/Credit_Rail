// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/**
 * @title CreditPolicy
 * @notice Standalone (non-upgradeable) credit policy for Echidna testing.
 *         Mirrors the production CreditPolicy but without UUPS/AccessControl
 *         since Echidna cannot use proxies or OZ role machinery.
 */
contract CreditPolicy {
    /*//////////////////////////////////////////////////////////////
                                ERRORS
    //////////////////////////////////////////////////////////////*/
    error CreditPolicy__Unauthorized();
    error CreditPolicy__PolicyFrozen(uint256 version);
    error CreditPolicy__InvalidVersion();
    error CreditPolicy__PolicyVersionExists(uint256 version);
    error CreditPolicy__PolicyNotEditable(uint256 version);
    error CreditPolicy__IncompletePolicy(uint256 version);
    error CreditPolicy__InvalidIndustryHash();
    error CreditPolicy__PolicyNotActive(uint256 version);
    error CreditPolicy__InvalidScopeHash();
    error CreditPolicy__InvalidAdmin();

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

    /*//////////////////////////////////////////////////////////////
                            POLICY LIFECYCLE
    //////////////////////////////////////////////////////////////*/
    mapping(uint256 => bool) public policyCreated;
    mapping(uint256 => bool) public policyFrozen;
    mapping(uint256 => bool) public policyActive;
    mapping(uint256 => uint256) public lastUpdated;

    /*//////////////////////////////////////////////////////////////
                        POLICY SCOPE HASHES
    //////////////////////////////////////////////////////////////*/
    mapping(uint256 => mapping(uint8 => bytes32)) internal _policyScopeHashes;
    mapping(uint256 => mapping(uint8 => bool)) public tierExists;
    mapping(uint256 => bool) public hasScopeHash;

    /*//////////////////////////////////////////////////////////////
                        INDUSTRY EXCLUSIONS
    //////////////////////////////////////////////////////////////*/
    mapping(uint256 => mapping(bytes32 => bool)) public excludedIndustries;

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
    event PolicyScopeHashSet(uint256 version, uint8 tierId, bytes32 hash, uint256 timestamp);
    event IndustryExcluded(uint256 version, bytes32 industry, uint256 timestamp);
    event IndustryIncluded(uint256 version, bytes32 industry, uint256 timestamp);
    event PolicyAdminChanged(address newAdmin);
    event PolicyDocumentSet(uint256 version, bytes32 hash, string uri, uint256 timestamp);
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

    function deActivatePolicy(
        uint256 version
    ) external onlyAdmin policyExists(version) {
        policyActive[version] = false;
        lastUpdated[version] = block.timestamp;
        emit PolicyDeactivated(version, block.timestamp);
    }

    /*//////////////////////////////////////////////////////////////
                        SCOPE HASH MANAGEMENT
    //////////////////////////////////////////////////////////////*/

    function setPolicyScopeHash(
        uint256 version,
        uint8 tierId,
        bytes32 hash
    ) external onlyAdmin policyExists(version) policyEditable(version) {
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

    // View functions for interface compliance

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

    function policyScopeHash(
        uint256 version,
        uint8 tierId
    ) external view returns (bytes32) {
        return _policyScopeHashes[version][tierId];
    }

    function isIndustryExcluded(
        uint256 version,
        bytes32 industry
    ) external view returns (bool) {
        return excludedIndustries[version][industry];
    }
}
