// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Test} from "forge-std/Test.sol";
import {CreditPolicy} from "../../src/CreditPolicy.sol";
import {ICreditPolicy} from "../../src/interfaces/ICreditPolicy.sol";
import {ERC1967Proxy} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";

/**
 * @title TestCreditPolicySecurity
 * @notice Security-focused tests for CreditPolicy: initializer re-entry,
 *         UUPS upgrade auth, access control on role management, scope hash,
 *         and freeze-gate enforcement.
 */
contract TestCreditPolicySecurity is Test {
    CreditPolicy creditPolicy;

    address deployer = makeAddr("deployer");
    address attacker = makeAddr("attacker");

    function setUp() public {
        vm.startPrank(deployer);
        CreditPolicy impl = new CreditPolicy();
        ERC1967Proxy proxy = new ERC1967Proxy(
            address(impl),
            abi.encodeCall(CreditPolicy.initialize, (deployer))
        );
        creditPolicy = CreditPolicy(address(proxy));
        vm.stopPrank();
    }

    // =========================================================================
    //                    INITIALIZER SECURITY
    // =========================================================================

    function test_Initialize_CannotReinitializeProxy() public {
        vm.expectRevert();
        creditPolicy.initialize(deployer);
    }

    function test_Initialize_RolesGrantedCorrectly() public view {
        assertTrue(
            creditPolicy.hasRole(creditPolicy.DEFAULT_ADMIN_ROLE(), deployer)
        );
        assertTrue(
            creditPolicy.hasRole(creditPolicy.POLICY_ADMIN_ROLE(), deployer)
        );
        assertTrue(
            creditPolicy.hasRole(creditPolicy.INDUSTRY_ADMIN_ROLE(), deployer)
        );
    }

    // =========================================================================
    //                    UUPS UPGRADE AUTHORIZATION
    // =========================================================================

    function test_Upgrade_OnlyDefaultAdmin() public {
        CreditPolicy newImpl = new CreditPolicy();
        vm.prank(deployer);
        creditPolicy.upgradeToAndCall(address(newImpl), "");
    }

    function test_Upgrade_RevertsForNonAdmin() public {
        CreditPolicy newImpl = new CreditPolicy();
        vm.prank(attacker);
        vm.expectRevert();
        creditPolicy.upgradeToAndCall(address(newImpl), "");
    }

    // =========================================================================
    //                    POLICY CREATION SECURITY
    // =========================================================================

    function test_CreatePolicy_RevertsOnVersionZero() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.createPolicy(0);
    }

    function test_CreatePolicy_RevertsOnDuplicateVersion() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(1);
        vm.expectRevert(
            abi.encodeWithSelector(
                CreditPolicy.CreditPolicy__PolicyVersionExists.selector,
                1
            )
        );
        creditPolicy.createPolicy(1);
        vm.stopPrank();
    }

    function test_CreatePolicy_RevertsForNonPolicyAdmin() public {
        vm.prank(attacker);
        vm.expectRevert();
        creditPolicy.createPolicy(1);
    }

    // =========================================================================
    //                    FREEZE SECURITY
    // =========================================================================

    function test_FreezePolicy_RevertsIfIncomplete() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(1);
        // Only set document — missing scope hash
        creditPolicy.setPolicyDocument(1, keccak256("doc"), "ipfs://doc");

        vm.expectRevert(
            abi.encodeWithSelector(
                CreditPolicy.CreditPolicy__IncompletePolicy.selector,
                1
            )
        );
        creditPolicy.freezePolicy(1);
        vm.stopPrank();
    }

    function test_FreezePolicy_RevertsIfAlreadyFrozen() public {
        _createAndFreezePolicy(1);

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSelector(
                CreditPolicy.CreditPolicy__PolicyFrozen.selector,
                1
            )
        );
        creditPolicy.freezePolicy(1);
    }

    function test_FreezePolicy_RevertsIfDeactivated() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(2);
        creditPolicy.setPolicyScopeHash(2, 0, keccak256("hash"));
        creditPolicy.setPolicyDocument(2, keccak256("doc"), "ipfs://doc");
        creditPolicy.deActivatePolicy(2);

        vm.expectRevert(
            abi.encodeWithSelector(
                CreditPolicy.CreditPolicy__PolicyNotActive.selector,
                2
            )
        );
        creditPolicy.freezePolicy(2);
        vm.stopPrank();
    }

    function test_FreezePolicy_RevertsWithoutDocumentHash() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(3);
        creditPolicy.setPolicyScopeHash(3, 0, keccak256("hash"));
        // No document hash set

        vm.expectRevert(
            abi.encodeWithSelector(
                CreditPolicy.CreditPolicy__IncompletePolicy.selector,
                3
            )
        );
        creditPolicy.freezePolicy(3);
        vm.stopPrank();
    }

    function test_FreezePolicy_RevertsWithoutScopeHash() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(4);
        creditPolicy.setPolicyDocument(4, keccak256("doc"), "ipfs://doc");
        // No scope hash set

        vm.expectRevert(
            abi.encodeWithSelector(
                CreditPolicy.CreditPolicy__IncompletePolicy.selector,
                4
            )
        );
        creditPolicy.freezePolicy(4);
        vm.stopPrank();
    }

    // =========================================================================
    //                    EDITABLE GATE (frozen policy cannot be edited)
    // =========================================================================

    function test_SetPolicyScopeHash_RevertsOnFrozenPolicy() public {
        _createAndFreezePolicy(10);

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSelector(
                CreditPolicy.CreditPolicy__PolicyNotEditable.selector,
                10
            )
        );
        creditPolicy.setPolicyScopeHash(10, 0, keccak256("newHash"));
    }

    function test_SetPolicyScopeHash_RevertsOnZeroHash() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(11);
        vm.expectRevert(
            CreditPolicy.CreditPolicy__InvalidScopeHash.selector
        );
        creditPolicy.setPolicyScopeHash(11, 0, bytes32(0));
        vm.stopPrank();
    }

    function test_SetPolicyScopeHash_RegistersTier() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(12);
        assertFalse(creditPolicy.tierExistsInPolicy(12, 0));

        creditPolicy.setPolicyScopeHash(12, 0, keccak256("hash"));
        assertTrue(creditPolicy.tierExistsInPolicy(12, 0));
        vm.stopPrank();
    }

    // =========================================================================
    //                    INDUSTRY CONTROLS
    // =========================================================================

    function test_ExcludeIndustry_RevertsOnZeroHash() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(30);
        vm.expectRevert(
            CreditPolicy.CreditPolicy__InvalidIndustryHash.selector
        );
        creditPolicy.excludeIndustry(30, bytes32(0));
        vm.stopPrank();
    }

    function test_IncludeIndustry_RevertsOnZeroHash() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(31);
        vm.expectRevert(
            CreditPolicy.CreditPolicy__InvalidIndustryHash.selector
        );
        creditPolicy.includeIndustry(31, bytes32(0));
        vm.stopPrank();
    }

    function test_ExcludeIndustry_RevertsForNonIndustryAdmin() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(32);

        vm.prank(attacker);
        vm.expectRevert();
        creditPolicy.excludeIndustry(32, keccak256("GAMBLING"));
    }

    // =========================================================================
    //                    ROLE MANAGEMENT ACCESS CONTROL
    // =========================================================================

    function test_ChangeDefaultAdmin_RevertsForNonAdmin() public {
        vm.prank(attacker);
        vm.expectRevert();
        creditPolicy.changeDefaultAdmin(attacker);
    }

    function test_ChangeDefaultAdmin_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__ZeroAddress.selector);
        creditPolicy.changeDefaultAdmin(address(0));
    }

    function test_ChangeDefaultAdmin_TransfersRole() public {
        address newAdmin = makeAddr("newAdmin");
        vm.prank(deployer);
        creditPolicy.changeDefaultAdmin(newAdmin);

        assertTrue(
            creditPolicy.hasRole(creditPolicy.DEFAULT_ADMIN_ROLE(), newAdmin)
        );
        assertFalse(
            creditPolicy.hasRole(creditPolicy.DEFAULT_ADMIN_ROLE(), deployer)
        );
    }

    function test_GrantPolicyAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__ZeroAddress.selector);
        creditPolicy.grantPolicyAdminRole(address(0));
    }

    function test_RevokePolicyAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__ZeroAddress.selector);
        creditPolicy.revokePolicyAdminRole(address(0));
    }

    function test_GrantIndustryAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__ZeroAddress.selector);
        creditPolicy.grantIndustryAdminRole(address(0));
    }

    function test_RevokeIndustryAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__ZeroAddress.selector);
        creditPolicy.revokeIndustryAdminRole(address(0));
    }

    function test_GrantPolicyAdminRole_RevertsForNonAdmin() public {
        vm.prank(attacker);
        vm.expectRevert();
        creditPolicy.grantPolicyAdminRole(attacker);
    }

    // =========================================================================
    //                    EVENTS
    // =========================================================================

    function test_Event_PolicyCreated() public {
        vm.expectEmit(false, false, false, true);
        emit CreditPolicy.PolicyCreated(60, block.timestamp);

        vm.prank(deployer);
        creditPolicy.createPolicy(60);
    }

    function test_Event_PolicyFrozen() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(61);
        creditPolicy.setPolicyScopeHash(61, 0, keccak256("hash"));
        creditPolicy.setPolicyDocument(61, keccak256("doc"), "ipfs://doc");

        vm.expectEmit(false, false, false, true);
        emit CreditPolicy.PolicyFrozen(61, block.timestamp);
        creditPolicy.freezePolicy(61);
        vm.stopPrank();
    }

    function test_Event_PolicyScopeHashSet() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(62);
        bytes32 hash = keccak256("hash");

        vm.expectEmit(false, false, false, true);
        emit CreditPolicy.PolicyScopeHashSet(62, 0, hash, block.timestamp);
        creditPolicy.setPolicyScopeHash(62, 0, hash);
        vm.stopPrank();
    }

    function test_Event_DefaultAdminChanged() public {
        address newAdmin = makeAddr("newAdmin");

        vm.expectEmit(true, true, false, false);
        emit CreditPolicy.DefaultAdminChanged(deployer, newAdmin);

        vm.prank(deployer);
        creditPolicy.changeDefaultAdmin(newAdmin);
    }

    function test_Event_PolicyDeactivated() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(63);

        vm.expectEmit(false, false, false, true);
        emit CreditPolicy.PolicyDeactivated(63, block.timestamp);
        creditPolicy.deActivatePolicy(63);
        vm.stopPrank();
    }

    // =========================================================================
    //                    HELPERS
    // =========================================================================

    function _createAndFreezePolicy(uint256 version) internal {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(version);
        creditPolicy.setPolicyScopeHash(version, 0, keccak256("scopeHash"));
        creditPolicy.setPolicyDocument(version, keccak256("doc"), "ipfs://doc");
        creditPolicy.freezePolicy(version);
        vm.stopPrank();
    }
}
