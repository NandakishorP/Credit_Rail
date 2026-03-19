// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Test} from "forge-std/Test.sol";
import {SymTest} from "halmos-cheatcodes/SymTest.sol";
import {CreditPolicy} from "../../src/CreditPolicy.sol";
import {ICreditPolicy} from "../../src/interfaces/ICreditPolicy.sol";
import {ERC1967Proxy} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import {MockPoseidon2} from "../mocks/MockPoseidon2.sol";

/// @title HalmosCreditPolicy
/// @notice Symbolic tests for CreditPolicy using Halmos.
///         Naming convention: check_ prefix (Halmos default) instead of test_.
contract HalmosCreditPolicy is Test, SymTest {
    CreditPolicy creditPolicy;
    address admin;
    MockPoseidon2 mockPoseidon;

    function setUp() public {
        admin = address(0xA);
        vm.startPrank(admin);

        mockPoseidon = new MockPoseidon2();
        CreditPolicy impl = new CreditPolicy();
        ERC1967Proxy proxy = new ERC1967Proxy(
            address(impl),
            abi.encodeCall(CreditPolicy.initialize, (admin, address(mockPoseidon)))
        );
        creditPolicy = CreditPolicy(address(proxy));
        creditPolicy.setMaxTiers(10);

        vm.stopPrank();
    }

    // ---------------------------------------------------------------
    // Property 1: createPolicy version 0 always reverts
    // ---------------------------------------------------------------
    function check_createPolicy_reverts_on_version_zero() public {
        vm.prank(admin);
        try creditPolicy.createPolicy(0) {
            assert(false); // should never reach here
        } catch {
            assert(true);
        }
    }

    // ---------------------------------------------------------------
    // Property 2: After createPolicy, the policy must be active and not frozen
    // ---------------------------------------------------------------
    function check_createPolicy_sets_active_state() public {
        uint256 version = svm.createUint256("version");
        vm.assume(version > 0 && version < 1000);

        vm.prank(admin);
        creditPolicy.createPolicy(version);

        assert(creditPolicy.policyCreated(version));
        assert(creditPolicy.isPolicyActive(version));
        assert(!creditPolicy.isPolicyFrozen(version));
    }

    // ---------------------------------------------------------------
    // Property 3: Cannot create the same version twice
    // ---------------------------------------------------------------
    function check_createPolicy_no_duplicate_version() public {
        uint256 version = svm.createUint256("version");
        vm.assume(version > 0 && version < 1000);

        vm.prank(admin);
        creditPolicy.createPolicy(version);

        vm.prank(admin);
        try creditPolicy.createPolicy(version) {
            assert(false); // should revert
        } catch {
            assert(true);
        }
    }
}
