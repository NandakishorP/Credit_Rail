// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

interface ICreditPolicy {
    /*//////////////////////////////////////////////////////////////
                            FUNCTION SIGNATURES
    //////////////////////////////////////////////////////////////*/
    function createPolicy(uint256 version) external;

    function freezePolicy(uint256 version) external;

    function deActivatePolicy(uint256 version) external;

    function setPolicyScopeHash(
        uint256 version,
        uint8 tierId,
        bytes32 hash
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

    function changeDefaultAdmin(address newAdmin) external;

    function grantPolicyAdminRole(address account) external;

    function revokePolicyAdminRole(address account) external;

    function grantIndustryAdminRole(address account) external;

    function revokeIndustryAdminRole(address account) external;

    function isPolicyActive(uint256 version) external view returns (bool);

    function isPolicyFrozen(uint256 version) external view returns (bool);

    function isIndustryExcluded(
        uint256 version,
        bytes32 industry
    ) external view returns (bool);

    function policyScopeHash(uint256 version, uint8 tierId) external view returns (bytes32);
}
