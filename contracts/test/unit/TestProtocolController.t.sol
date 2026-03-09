// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Test} from "forge-std/Test.sol";
import {ProtocolController} from "../../src/ProtocolController.sol";
import {TimelockController} from "@openzeppelin/contracts/governance/TimelockController.sol";

/**
 * @title TestProtocolController
 * @notice Unit tests for the ProtocolController (TimelockController wrapper).
 * @dev Covers constructor validation, role assignments, timelock flow
 *      (schedule → wait → execute), guardian cancellation, and access control.
 */
contract TestProtocolController is Test {
    ProtocolController controller;

    address multisig = makeAddr("multisig");
    address guardian = makeAddr("guardian");
    address outsider = makeAddr("outsider");
    address targetAddr = makeAddr("target");

    uint256 constant MIN_DELAY = 2 days; // 48 hours

    function setUp() public {
        controller = new ProtocolController(MIN_DELAY, multisig, guardian);
    }

    // =========================================================================
    //                    CONSTRUCTOR & ROLE VALIDATION
    // =========================================================================

    function test_Constructor_MinDelay() public view {
        assertEq(
            controller.getMinDelay(),
            MIN_DELAY,
            "Min delay should be set correctly"
        );
    }

    function test_Constructor_MultisigHasProposerRole() public view {
        bytes32 proposerRole = controller.PROPOSER_ROLE();
        assertTrue(
            controller.hasRole(proposerRole, multisig),
            "Multisig should have PROPOSER_ROLE"
        );
    }

    function test_Constructor_MultisigHasExecutorRole() public view {
        bytes32 executorRole = controller.EXECUTOR_ROLE();
        assertTrue(
            controller.hasRole(executorRole, multisig),
            "Multisig should have EXECUTOR_ROLE"
        );
    }

    function test_Constructor_GuardianHasCancellerRole() public view {
        bytes32 cancellerRole = controller.CANCELLER_ROLE();
        assertTrue(
            controller.hasRole(cancellerRole, guardian),
            "Guardian should have CANCELLER_ROLE"
        );
    }

    function test_Constructor_OutsiderHasNoRoles() public view {
        assertFalse(controller.hasRole(controller.PROPOSER_ROLE(), outsider));
        assertFalse(controller.hasRole(controller.EXECUTOR_ROLE(), outsider));
        assertFalse(controller.hasRole(controller.CANCELLER_ROLE(), outsider));
    }

    function test_Constructor_WithZeroGuardian() public {
        // Guardian = address(0) means admin role to zero address (open admin)
        ProtocolController noGuardian = new ProtocolController(
            MIN_DELAY,
            multisig,
            address(0)
        );
        assertEq(noGuardian.getMinDelay(), MIN_DELAY);
        assertTrue(noGuardian.hasRole(noGuardian.PROPOSER_ROLE(), multisig));
    }

    function test_Constructor_ZeroDelay() public {
        ProtocolController zeroDelay = new ProtocolController(
            0,
            multisig,
            guardian
        );
        assertEq(zeroDelay.getMinDelay(), 0, "Should allow 0 delay");
    }

    // =========================================================================
    //                    TIMELOCK FLOW: SCHEDULE → WAIT → EXECUTE
    // =========================================================================

    function test_TimelockFlow_ScheduleAndExecute() public {
        // Create a call that just sends 0 ETH to target (no-op for testing)
        bytes32 salt = keccak256("test-salt");
        bytes memory data = "";
        bytes32 predecessor = bytes32(0);

        bytes32 opId = controller.hashOperation(
            targetAddr,
            0,
            data,
            predecessor,
            salt
        );

        // Not yet scheduled
        assertFalse(controller.isOperationPending(opId));

        // Schedule from multisig
        vm.prank(multisig);
        controller.schedule(
            targetAddr,
            0,
            data,
            predecessor,
            salt,
            MIN_DELAY
        );

        assertTrue(
            controller.isOperationPending(opId),
            "Operation should be pending"
        );
        assertFalse(
            controller.isOperationReady(opId),
            "Operation should not be ready yet"
        );

        // Warp past the delay
        vm.warp(block.timestamp + MIN_DELAY);

        assertTrue(
            controller.isOperationReady(opId),
            "Operation should be ready after delay"
        );

        // Execute from multisig
        vm.prank(multisig);
        controller.execute(targetAddr, 0, data, predecessor, salt);

        assertTrue(
            controller.isOperationDone(opId),
            "Operation should be done"
        );
    }

    function test_TimelockFlow_CannotExecuteBeforeDelay() public {
        bytes32 salt = keccak256("early-exec");
        bytes memory data = "";
        bytes32 predecessor = bytes32(0);

        vm.prank(multisig);
        controller.schedule(
            targetAddr,
            0,
            data,
            predecessor,
            salt,
            MIN_DELAY
        );

        // Warp only half the delay
        vm.warp(block.timestamp + MIN_DELAY / 2);

        vm.prank(multisig);
        vm.expectRevert();
        controller.execute(targetAddr, 0, data, predecessor, salt);
    }

    function test_TimelockFlow_CannotExecuteWithoutSchedule() public {
        bytes32 salt = keccak256("never-scheduled");
        bytes memory data = "";
        bytes32 predecessor = bytes32(0);

        vm.prank(multisig);
        vm.expectRevert();
        controller.execute(targetAddr, 0, data, predecessor, salt);
    }

    // =========================================================================
    //                    GUARDIAN CANCELLATION
    // =========================================================================

    function test_Guardian_CanCancelPendingOperation() public {
        bytes32 salt = keccak256("cancel-test");
        bytes memory data = "";
        bytes32 predecessor = bytes32(0);

        bytes32 opId = controller.hashOperation(
            targetAddr,
            0,
            data,
            predecessor,
            salt
        );

        // Schedule
        vm.prank(multisig);
        controller.schedule(
            targetAddr,
            0,
            data,
            predecessor,
            salt,
            MIN_DELAY
        );
        assertTrue(controller.isOperationPending(opId));

        // Guardian cancels
        vm.prank(guardian);
        controller.cancel(opId);

        assertFalse(
            controller.isOperationPending(opId),
            "Cancelled operation should not be pending"
        );
    }

    function test_Guardian_CannotExecute() public {
        bytes32 salt = keccak256("guardian-exec-test");
        bytes memory data = "";
        bytes32 predecessor = bytes32(0);

        vm.prank(multisig);
        controller.schedule(
            targetAddr,
            0,
            data,
            predecessor,
            salt,
            MIN_DELAY
        );

        vm.warp(block.timestamp + MIN_DELAY);

        // Guardian cannot execute (no EXECUTOR_ROLE)
        vm.prank(guardian);
        vm.expectRevert();
        controller.execute(targetAddr, 0, data, predecessor, salt);
    }

    // =========================================================================
    //                    ACCESS CONTROL
    // =========================================================================

    function test_OutsiderCannotSchedule() public {
        bytes32 salt = keccak256("outsider-schedule");
        bytes memory data = "";
        bytes32 predecessor = bytes32(0);

        vm.prank(outsider);
        vm.expectRevert();
        controller.schedule(
            targetAddr,
            0,
            data,
            predecessor,
            salt,
            MIN_DELAY
        );
    }

    function test_OutsiderCannotCancel() public {
        bytes32 salt = keccak256("outsider-cancel");
        bytes memory data = "";
        bytes32 predecessor = bytes32(0);

        bytes32 opId = controller.hashOperation(
            targetAddr,
            0,
            data,
            predecessor,
            salt
        );

        vm.prank(multisig);
        controller.schedule(
            targetAddr,
            0,
            data,
            predecessor,
            salt,
            MIN_DELAY
        );

        vm.prank(outsider);
        vm.expectRevert();
        controller.cancel(opId);
    }

    function test_OutsiderCannotExecute() public {
        bytes32 salt = keccak256("outsider-exec");
        bytes memory data = "";
        bytes32 predecessor = bytes32(0);

        vm.prank(multisig);
        controller.schedule(
            targetAddr,
            0,
            data,
            predecessor,
            salt,
            MIN_DELAY
        );

        vm.warp(block.timestamp + MIN_DELAY);

        vm.prank(outsider);
        vm.expectRevert();
        controller.execute(targetAddr, 0, data, predecessor, salt);
    }

    // =========================================================================
    //                    BATCH OPERATIONS
    // =========================================================================

    function test_BatchScheduleAndExecute() public {
        address[] memory targets = new address[](2);
        targets[0] = targetAddr;
        targets[1] = targetAddr;

        uint256[] memory values = new uint256[](2);
        values[0] = 0;
        values[1] = 0;

        bytes[] memory payloads = new bytes[](2);
        payloads[0] = "";
        payloads[1] = "";

        bytes32 predecessor = bytes32(0);
        bytes32 salt = keccak256("batch-test");

        bytes32 opId = controller.hashOperationBatch(
            targets,
            values,
            payloads,
            predecessor,
            salt
        );

        vm.prank(multisig);
        controller.scheduleBatch(
            targets,
            values,
            payloads,
            predecessor,
            salt,
            MIN_DELAY
        );

        assertTrue(controller.isOperationPending(opId));

        vm.warp(block.timestamp + MIN_DELAY);

        vm.prank(multisig);
        controller.executeBatch(targets, values, payloads, predecessor, salt);

        assertTrue(controller.isOperationDone(opId));
    }
}
