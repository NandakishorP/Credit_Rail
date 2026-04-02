// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import {CreditPolicy} from "../../src/CreditPolicy.sol";
import {ICreditPolicy} from "../../src/interfaces/ICreditPolicy.sol";
import {IAccessControl} from "@openzeppelin/contracts/access/IAccessControl.sol";
import {Test} from "forge-std/Test.sol";
import {ERC1967Proxy} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";

contract TestCreditPolicy is Test {
    address deployer = makeAddr("deployer");
    address seniorUser1 = makeAddr("seniorUser1");
    address seniorUser2 = makeAddr("seniorUser2");
    CreditPolicy creditPolicy;

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

    /*//////////////////////////////////////////////////////////////
                            HELPER FUNCTIONS
    //////////////////////////////////////////////////////////////*/

    function _createPolicy(uint256 version) internal {
        vm.prank(deployer);
        creditPolicy.createPolicy(version);
    }

    function _freezePolicy(uint256 version) internal {
        vm.prank(deployer);
        creditPolicy.freezePolicy(version);
    }

    function _createAndFreezePolicy(uint256 version) internal {
        _createPolicy(version);
        vm.startPrank(deployer);
        creditPolicy.setPolicyScopeHash(version, 0, keccak256("scopeHash"));
        creditPolicy.setPolicyDocument(
            version,
            _hashString("document"),
            "ipfs://policyDocHash"
        );
        vm.stopPrank();
        _freezePolicy(version);
    }

    function _hashString(string memory str) internal pure returns (bytes32) {
        return keccak256(bytes(str));
    }

    /*//////////////////////////////////////////////////////////////
                        POLICY CREATION TESTS
    //////////////////////////////////////////////////////////////*/

    function testCreatePolicyRevertIfOwnerIsNotAdmin() public {
        vm.prank(seniorUser1);
        vm.expectRevert();
        creditPolicy.createPolicy(1);
    }

    function testCreatePolicyRevertsIfVersionIsZero() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.createPolicy(0);
    }

    function testCreatePolicyRevertsIfVersionExists() public {
        _createPolicy(1);
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__PolicyVersionExists(uint256)",
                1
            )
        );
        creditPolicy.createPolicy(1);
    }

    function testCreatePolicy() public {
        vm.prank(deployer);
        vm.expectEmit(true, true, false, true);
        emit CreditPolicy.PolicyCreated(1, block.timestamp);
        creditPolicy.createPolicy(1);

        assertEq(creditPolicy.policyCreated(1), true);
        assertEq(creditPolicy.isPolicyActive(1), true);
        assertEq(creditPolicy.isPolicyFrozen(1), false);
        assertEq(creditPolicy.lastUpdated(1), block.timestamp);
    }

    function testMultiplePolicyVersions() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(1);
        creditPolicy.createPolicy(2);
        creditPolicy.createPolicy(3);
        vm.stopPrank();

        assertEq(creditPolicy.policyCreated(1), true);
        assertEq(creditPolicy.policyCreated(2), true);
        assertEq(creditPolicy.policyCreated(3), true);
    }

    function testPolicyVersionIsolation() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(1);
        creditPolicy.createPolicy(2);

        bytes32 industry = _hashString("Gambling");
        creditPolicy.excludeIndustry(1, industry);

        assertTrue(creditPolicy.isIndustryExcluded(1, industry));
        assertFalse(creditPolicy.isIndustryExcluded(2, industry));
        vm.stopPrank();
    }

    /*//////////////////////////////////////////////////////////////
                        DEACTIVATE POLICY TESTS
    //////////////////////////////////////////////////////////////*/

    function testDeactivatePolicy() public {
        _createPolicy(1);
        assertEq(creditPolicy.isPolicyActive(1), true);

        vm.prank(deployer);
        creditPolicy.deActivatePolicy(1);

        assertEq(creditPolicy.isPolicyActive(1), false);
    }

    function testDeactivatePolicyRevertIfOwnerIsNotAdmin() public {
        _createPolicy(1);
        vm.prank(seniorUser1);
        vm.expectRevert();
        creditPolicy.deActivatePolicy(1);
    }

    function testDeactivatePolicyRevertsIfPolicyDontExist() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.deActivatePolicy(1);
    }

    function testDeactivateUpdatesLastUpdated() public {
        _createPolicy(1);
        uint256 t1 = creditPolicy.lastUpdated(1);

        vm.warp(block.timestamp + 100);
        vm.prank(deployer);
        creditPolicy.deActivatePolicy(1);

        assertEq(creditPolicy.lastUpdated(1), block.timestamp);
        assertGt(creditPolicy.lastUpdated(1), t1);
    }

    function testDeactivatePolicyIsIdempotent() public {
        _createPolicy(1);

        vm.prank(deployer);
        creditPolicy.deActivatePolicy(1);

        uint256 t1 = creditPolicy.lastUpdated(1);

        vm.warp(block.timestamp + 10);
        vm.prank(deployer);
        creditPolicy.deActivatePolicy(1);

        assertFalse(creditPolicy.isPolicyActive(1));
        assertEq(creditPolicy.lastUpdated(1), block.timestamp);
        assertGt(creditPolicy.lastUpdated(1), t1);
    }

    function testUpdateRevertsIfPolicyInactive() public {
        _createPolicy(1);
        vm.prank(deployer);
        creditPolicy.deActivatePolicy(1);

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__PolicyNotEditable(uint256)",
                1
            )
        );
        creditPolicy.setPolicyScopeHash(1, 0, keccak256("hash"));
    }

    /*//////////////////////////////////////////////////////////////
                        SCOPE HASH TESTS
    //////////////////////////////////////////////////////////////*/

    function testSetPolicyScopeHash() public {
        _createPolicy(1);
        bytes32 hash = keccak256("scopeHash");

        vm.prank(deployer);
        creditPolicy.setPolicyScopeHash(1, 0, hash);

        assertEq(creditPolicy.policyScopeHash(1, 0), hash);
        assertTrue(creditPolicy.tierExistsInPolicy(1, 0));
        assertTrue(creditPolicy.hasScopeHash(1));
    }

    function testSetPolicyScopeHashRevertsOnZeroHash() public {
        _createPolicy(1);

        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidScopeHash.selector);
        creditPolicy.setPolicyScopeHash(1, 0, bytes32(0));
    }

    function testSetPolicyScopeHashMultipleTiers() public {
        _createPolicy(1);
        bytes32 hash0 = keccak256("tier0");
        bytes32 hash1 = keccak256("tier1");

        vm.startPrank(deployer);
        creditPolicy.setPolicyScopeHash(1, 0, hash0);
        creditPolicy.setPolicyScopeHash(1, 1, hash1);
        vm.stopPrank();

        assertEq(creditPolicy.policyScopeHash(1, 0), hash0);
        assertEq(creditPolicy.policyScopeHash(1, 1), hash1);
        assertTrue(creditPolicy.tierExistsInPolicy(1, 0));
        assertTrue(creditPolicy.tierExistsInPolicy(1, 1));
    }

    function testSetPolicyScopeHashRevertsOnFrozenPolicy() public {
        _createAndFreezePolicy(1);

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__PolicyNotEditable(uint256)",
                1
            )
        );
        creditPolicy.setPolicyScopeHash(1, 0, keccak256("newHash"));
    }

    /*//////////////////////////////////////////////////////////////
                        FREEZE POLICY TESTS
    //////////////////////////////////////////////////////////////*/

    function testFreezePolicyUnitTest() public {
        _createPolicy(1);
        vm.startPrank(deployer);
        creditPolicy.setPolicyScopeHash(1, 0, keccak256("scopeHash"));
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.PolicyFrozen(1, block.timestamp);
        creditPolicy.freezePolicy(1);
    }

    function testFreezePolicyRevertIfOwnerIsNotAdmin() public {
        _createPolicy(1);
        vm.prank(seniorUser1);
        vm.expectRevert();
        creditPolicy.freezePolicy(1);
    }

    function testFreezePolicyRevertsIfPolicyDontExist() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.freezePolicy(1);
    }

    function testFreezePolicyReverstIfPolicyIsNotActive() public {
        _createPolicy(1);
        vm.prank(deployer);
        creditPolicy.deActivatePolicy(1);

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature("CreditPolicy__PolicyNotActive(uint256)", 1)
        );
        creditPolicy.freezePolicy(1);
    }

    function testFreezePolicyRevertsIfAlreadyFrozen() public {
        _createAndFreezePolicy(1);

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature("CreditPolicy__PolicyFrozen(uint256)", 1)
        );
        creditPolicy.freezePolicy(1); // Try to freeze again
    }

    function testFreezePolicyMarksPolicyAsFrozen() public {
        _createPolicy(1);
        assertEq(creditPolicy.isPolicyActive(1), true);
        vm.startPrank(deployer);
        creditPolicy.setPolicyScopeHash(1, 0, keccak256("scopeHash"));
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );
        vm.stopPrank();
        _freezePolicy(1);
        assertEq(creditPolicy.isPolicyFrozen(1), true);
    }

    function testFreezeUpdatesLastUpdated() public {
        _createPolicy(1);

        vm.startPrank(deployer);
        creditPolicy.setPolicyScopeHash(1, 0, keccak256("scopeHash"));
        creditPolicy.setPolicyDocument(1, _hashString("doc"), "uri");
        vm.stopPrank();

        uint256 t1 = creditPolicy.lastUpdated(1);

        vm.warp(block.timestamp + 10);
        vm.prank(deployer);
        creditPolicy.freezePolicy(1);

        assertEq(creditPolicy.lastUpdated(1), block.timestamp);
        assertGt(creditPolicy.lastUpdated(1), t1);
    }

    function testFreezeDoesNotDeactivatePolicy() public {
        _createAndFreezePolicy(1);
        assertTrue(creditPolicy.isPolicyActive(1));
        assertTrue(creditPolicy.isPolicyFrozen(1));
    }

    function testFrozenPolicyIsFullyImmutable() public {
        _createAndFreezePolicy(1);

        vm.startPrank(deployer);

        vm.expectRevert();
        creditPolicy.setPolicyScopeHash(1, 0, keccak256("newHash"));
        vm.expectRevert();
        creditPolicy.excludeIndustry(1, _hashString("X"));
        vm.expectRevert();
        creditPolicy.setPolicyDocument(1, _hashString("x"), "uri");

        vm.stopPrank();
    }

    function testFreezePolicyRevertsIfNoScopeHashSet() public {
        _createPolicy(1);
        vm.startPrank(deployer);
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );

        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__IncompletePolicy(uint256)",
                1
            )
        );
        creditPolicy.freezePolicy(1);
        vm.stopPrank();
    }

    function testFreezePolicyRevertsIfNoDocumentHash() public {
        _createPolicy(1);
        vm.startPrank(deployer);
        creditPolicy.setPolicyScopeHash(1, 0, keccak256("scopeHash"));

        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__IncompletePolicy(uint256)",
                1
            )
        );
        creditPolicy.freezePolicy(1);
        vm.stopPrank();
    }
}
