// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {TestTranchePoolBase} from "./TestTranchePoolBase.t.sol";
import {TranchePool} from "../../src/TranchePool.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {VmSafe} from "forge-std/Vm.sol";

contract TestTranchePool_Allocation is TestTranchePoolBase {
    function test_AllocateCapital_Success() public {
        // Deposit to tranches
        _depositToAllTranches();

        // Move to COMMITED state
        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        uint256 totalDisbursement = 1_00_00_000 * USDT;
        uint256 fees = 10_000 * USDT;
        address borrower_ = makeAddr("borrower");
        address feeManager_ = makeAddr("feeManager");

        vm.prank(loanEngine);
        tranchePool.allocateCapital(
            totalDisbursement,
            fees,
            borrower_,
            feeManager_
        );

        // Check deployed values
        uint256 totalAmount = totalDisbursement + fees;
        uint256 expectedSenior = (totalAmount * 80) / 100;
        uint256 expectedJunior = (totalAmount * 15) / 100;
        uint256 expectedEquity = totalAmount - expectedSenior - expectedJunior;

        assertEq(tranchePool.getSeniorTrancheDeployedValue(), expectedSenior);
        assertEq(tranchePool.getJuniorTrancheDeployedValue(), expectedJunior);
        assertEq(tranchePool.getEquityTrancheDeployedValue(), expectedEquity);

        // Check transfers
        assertEq(usdt.balanceOf(borrower_), totalDisbursement);
        assertEq(usdt.balanceOf(feeManager_), fees);

        // Check pool state changed to DEPLOYED
        assertEq(
            uint256(tranchePool.getPoolState()),
            uint256(TranchePool.PoolState.DEPLOYED)
        );
    }

    function test_AllocateCapital_NoFees_Success() public {
        _depositToAllTranches();

        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        uint256 totalDisbursement = 1_00_00_000 * USDT;
        address borrower_ = makeAddr("borrower");
        address feeManager_ = makeAddr("feeManager");

        vm.prank(loanEngine);
        tranchePool.allocateCapital(
            totalDisbursement,
            0,
            borrower_,
            feeManager_
        );

        assertEq(usdt.balanceOf(borrower_), totalDisbursement);
        assertEq(usdt.balanceOf(feeManager_), 0);
    }

    function test_AllocateCapital_RevertIf_NotCommited() public {
        _depositToAllTranches();

        vm.prank(loanEngine);
        vm.expectRevert(TranchePool.TranchePool__PoolIsNotCommited.selector);
        tranchePool.allocateCapital(
            1_00_00_000 * USDT,
            0,
            makeAddr("borrower"),
            makeAddr("feeManager")
        );
    }

    function test_AllocateCapital_RevertIf_Pool_Is_Commited_Or_Deployed()
        public
    {
        _depositToAllTranches();

        vm.prank(loanEngine);
        vm.expectRevert(TranchePool.TranchePool__PoolIsNotCommited.selector);
        tranchePool.allocateCapital(
            1_00_00_000 * USDT,
            0,
            makeAddr("borrower"),
            makeAddr("feeManager")
        );
    }

    function test_AllocateCapital_RevertIf_InsufficientLiquidity() public {
        _depositToAllTranches();

        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        uint256 excessiveAmount = 100_00_00_000 * USDT;

        vm.prank(loanEngine);
        vm.expectRevert(
            TranchePool.TranchePool__InsufficientLiquidity.selector
        );
        tranchePool.allocateCapital(
            excessiveAmount,
            0,
            makeAddr("borrower"),
            makeAddr("feeManager")
        );
    }

    function test_AllocateCapital_RevertIf_NotLoanEngine() public {
        _depositToAllTranches();

        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        vm.prank(seniorUser1);
        vm.expectRevert(
            abi.encodeWithSelector(
                TranchePool.TranchePool__InvalidCaller.selector,
                seniorUser1
            )
        );
        tranchePool.allocateCapital(
            1_00_00_000 * USDT,
            0,
            makeAddr("borrower"),
            makeAddr("feeManager")
        );
    }

    function test_AllocateCapital_WhenAlreadyDeployed_Success() public {
        // Setup: Deposit to all tranches
        _depositToAllTranches();

        // Move to COMMITTED and then allocate (which moves to DEPLOYED)
        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        uint256 firstDisbursement = 50_00_000 * USDT;
        uint256 firstFees = 5_000 * USDT;

        vm.prank(loanEngine);
        tranchePool.allocateCapital(
            firstDisbursement,
            firstFees,
            borrower,
            feeManager
        );

        // Verify we're in DEPLOYED state
        assertEq(
            uint256(tranchePool.getPoolState()),
            uint256(TranchePool.PoolState.DEPLOYED)
        );

        // Record state before second allocation
        uint256 seniorDeployedBefore = tranchePool
            .getSeniorTrancheDeployedValue();
        uint256 juniorDeployedBefore = tranchePool
            .getJuniorTrancheDeployedValue();
        uint256 equityDeployedBefore = tranchePool
            .getEquityTrancheDeployedValue();

        uint256 seniorIdleBefore = tranchePool.getSeniorTrancheIdleValue();
        uint256 juniorIdleBefore = tranchePool.getJuniorTrancheIdleValue();
        uint256 equityIdleBefore = tranchePool.getEquityTrancheIdleValue();

        // Second allocation while already in DEPLOYED state
        uint256 secondDisbursement = 30_00_000 * USDT;
        uint256 secondFees = 3_000 * USDT;

        // Listen for events - should NOT emit PoolStateUpdated
        vm.recordLogs();

        vm.prank(loanEngine);
        tranchePool.allocateCapital(
            secondDisbursement,
            secondFees,
            borrower,
            feeManager
        );

        // Verify state remains DEPLOYED
        assertEq(
            uint256(tranchePool.getPoolState()),
            uint256(TranchePool.PoolState.DEPLOYED),
            "Pool state should remain DEPLOYED"
        );

        // Calculate expected allocations for second disbursement
        uint256 totalAmount = secondDisbursement + secondFees;
        uint256 expectedSenior = (totalAmount * 80) / 100;
        uint256 expectedJunior = (totalAmount * 15) / 100;
        uint256 expectedEquity = totalAmount - expectedSenior - expectedJunior;

        // Verify deployed values increased correctly
        assertEq(
            tranchePool.getSeniorTrancheDeployedValue(),
            seniorDeployedBefore + expectedSenior,
            "Senior deployed should increase by expected amount"
        );
        assertEq(
            tranchePool.getJuniorTrancheDeployedValue(),
            juniorDeployedBefore + expectedJunior,
            "Junior deployed should increase by expected amount"
        );
        assertEq(
            tranchePool.getEquityTrancheDeployedValue(),
            equityDeployedBefore + expectedEquity,
            "Equity deployed should increase by expected amount"
        );

        // Verify idle values decreased correctly
        assertEq(
            tranchePool.getSeniorTrancheIdleValue(),
            seniorIdleBefore - expectedSenior,
            "Senior idle should decrease by expected amount"
        );
        assertEq(
            tranchePool.getJuniorTrancheIdleValue(),
            juniorIdleBefore - expectedJunior,
            "Junior idle should decrease by expected amount"
        );
        assertEq(
            tranchePool.getEquityTrancheIdleValue(),
            equityIdleBefore - expectedEquity,
            "Equity idle should decrease by expected amount"
        );

        // Verify NO extra PoolStateUpdated event was emitted
        VmSafe.Log[] memory logs = vm.getRecordedLogs();
        uint256 poolStateUpdateCount = 0;

        for (uint256 i = 0; i < logs.length; i++) {
            // PoolStateUpdated event signature
            if (logs[i].topics[0] == keccak256("PoolStateUpdated(uint8)")) {
                poolStateUpdateCount++;
            }
        }

        assertEq(
            poolStateUpdateCount,
            0,
            "Should not emit PoolStateUpdated when already DEPLOYED"
        );
    }

    function test_AllocateCapital_WhenClosed_Reverts() public {
        // Setup: Deposit to all tranches
        _depositToAllTranches();

        // Move to CLOSED state
        vm.startPrank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);
        tranchePool.setPoolState(TranchePool.PoolState.DEPLOYED);
        tranchePool.setPoolState(TranchePool.PoolState.CLOSED);
        vm.stopPrank();

        // Try to allocate when CLOSED - should revert
        uint256 disbursement = 50_00_000 * USDT;
        uint256 fees = 5_000 * USDT;

        vm.prank(loanEngine);
        vm.expectRevert(TranchePool.TranchePool__PoolIsNotCommited.selector);
        tranchePool.allocateCapital(disbursement, fees, borrower, feeManager);
    }

    function test_AllocateCapital_WhenOpen_Reverts() public {
        // Setup: Deposit to all tranches but stay in OPEN state
        _depositToAllTranches();

        // Pool is still in OPEN state
        assertEq(
            uint256(tranchePool.getPoolState()),
            uint256(TranchePool.PoolState.OPEN)
        );

        // Try to allocate when OPEN - should revert
        uint256 disbursement = 50_00_000 * USDT;
        uint256 fees = 5_000 * USDT;

        vm.prank(loanEngine);
        vm.expectRevert(TranchePool.TranchePool__PoolIsNotCommited.selector);
        tranchePool.allocateCapital(disbursement, fees, borrower, feeManager);
    }

    function test_AllocateCapital_ExactLiquidityMatch_WithRedistribution()
        public
    {
        // ------------------------------------------------------------
        // Arrange
        // ------------------------------------------------------------

        uint256 seniorDeposit = 80_00_000 * USDT;
        uint256 juniorDeposit = 15_00_000 * USDT;
        uint256 equityDeposit = 50_00_000 * USDT;

        // Senior deposit
        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), seniorDeposit);
        tranchePool.depositSeniorTranche(seniorDeposit);
        vm.stopPrank();

        // Junior deposit
        vm.startPrank(juniorUser1);
        usdt.approve(address(tranchePool), juniorDeposit);
        tranchePool.depositJuniorTranche(juniorDeposit);
        vm.stopPrank();

        // Equity deposit
        vm.startPrank(equityUser1);
        usdt.approve(address(tranchePool), equityDeposit);
        tranchePool.depositEquityTranche(equityDeposit);
        vm.stopPrank();

        uint256 totalAvailable = seniorDeposit + juniorDeposit + equityDeposit;

        // Move pool to COMMITED
        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        uint256 disbursement = 144_00_000 * USDT;
        uint256 fees = 1_00_000 * USDT;
        uint256 totalAmount = disbursement + fees;

        assertEq(totalAmount, totalAvailable);

        // ------------------------------------------------------------
        // Act
        // ------------------------------------------------------------

        vm.prank(loanEngine);
        tranchePool.allocateCapital(disbursement, fees, borrower, feeManager);

        // ------------------------------------------------------------
        // Assert — GLOBAL INVARIANTS
        // ------------------------------------------------------------

        // 1️⃣ All capital must be deployed
        assertEq(
            tranchePool.getTotalDeployedValue(),
            totalAmount,
            "Total deployed must equal total liquidity"
        );

        // 2️⃣ Idle + deployed conservation
        assertEq(
            tranchePool.getSeniorTrancheIdleValue() +
                tranchePool.getSeniorTrancheDeployedValue(),
            seniorDeposit,
            "Senior capital conserved"
        );

        assertEq(
            tranchePool.getJuniorTrancheIdleValue() +
                tranchePool.getJuniorTrancheDeployedValue(),
            juniorDeposit,
            "Junior capital conserved"
        );

        assertEq(
            tranchePool.getEquityTrancheIdleValue() +
                tranchePool.getEquityTrancheDeployedValue(),
            equityDeposit,
            "Equity capital conserved"
        );

        // ------------------------------------------------------------
        // Assert — PER-TRANCHE DEPLOYMENT
        // ------------------------------------------------------------

        assertEq(
            tranchePool.getSeniorTrancheDeployedValue(),
            seniorDeposit,
            "Senior capped by liquidity"
        );

        assertEq(
            tranchePool.getJuniorTrancheDeployedValue(),
            juniorDeposit,
            "Junior capped by liquidity"
        );

        assertEq(
            tranchePool.getTotalDeployedValue(),
            totalAmount,
            "All capital deployed"
        );

        assertLe(
            tranchePool.getSeniorTrancheDeployedValue(),
            seniorDeposit,
            "Senior never exceeds liquidity"
        );

        assertLe(
            tranchePool.getJuniorTrancheDeployedValue(),
            juniorDeposit,
            "Junior never exceeds liquidity"
        );

        assertEq(
            tranchePool.getEquityTrancheDeployedValue(),
            equityDeposit,
            "Equity absorbs remaining allocation"
        );

        // ------------------------------------------------------------
        // Assert — IDLE VALUES (ONLY BECAUSE THIS CASE IS PROPORTIONAL)
        // ------------------------------------------------------------

        assertEq(
            tranchePool.getSeniorTrancheIdleValue(),
            0,
            "Senior idle should be zero"
        );

        assertEq(
            tranchePool.getJuniorTrancheIdleValue(),
            0,
            "Junior idle should be zero"
        );

        assertEq(
            tranchePool.getEquityTrancheIdleValue(),
            0,
            "Equity idle should be zero"
        );

        // ------------------------------------------------------------
        // Assert — TRANSFERS
        // ------------------------------------------------------------

        assertEq(
            usdt.balanceOf(borrower),
            disbursement,
            "Borrower received disbursement"
        );

        assertEq(usdt.balanceOf(feeManager), fees, "Fee manager received fees");
    }

    // testing the protocol reverts if the total disbursment + fees is more than the total idle value
    function test_AllocateCapital_Reverts_If_Total_Disbursed_Plus_Fees_Exceeds_Idle_Value()
        public
    {
        // ------------------------------------------------------------
        // Arrange
        // ------------------------------------------------------------

        uint256 seniorDeposit = 80_00_000 * USDT;
        uint256 juniorDeposit = 15_00_000 * USDT;
        uint256 equityDeposit = 50_00_000 * USDT;

        // Senior deposit
        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), seniorDeposit);
        tranchePool.depositSeniorTranche(seniorDeposit);
        vm.stopPrank();

        // Junior deposit
        vm.startPrank(juniorUser1);
        usdt.approve(address(tranchePool), juniorDeposit);
        tranchePool.depositJuniorTranche(juniorDeposit);
        vm.stopPrank();

        // Equity deposit
        vm.startPrank(equityUser1);
        usdt.approve(address(tranchePool), equityDeposit);
        tranchePool.depositEquityTranche(equityDeposit);
        vm.stopPrank();

        uint256 totalAvailable = seniorDeposit + juniorDeposit + equityDeposit;

        // Move pool to COMMITED
        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        uint256 disbursement = 151_00_000 * USDT;
        uint256 fees = 1_00_000 * USDT;
        uint256 totalAmount = disbursement + fees;

        assertGt(totalAmount, totalAvailable);

        // ------------------------------------------------------------
        // Act & Assert
        // ------------------------------------------------------------

        vm.prank(loanEngine);
        vm.expectRevert(
            TranchePool.TranchePool__InsufficientLiquidity.selector
        );
        tranchePool.allocateCapital(disbursement, fees, borrower, feeManager);
    }

    function test_AllocateCapital_ExactLiquidityMatch_WithRounding_Success()
        public
    {
        // Deposit amounts that might cause rounding issues
        uint256 seniorDeposit = 77_77_777 * USDT;
        uint256 juniorDeposit = 24_58_333 * USDT;
        uint256 equityDeposit = 50_86_111 * USDT;

        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), seniorDeposit);
        tranchePool.depositSeniorTranche(seniorDeposit);
        vm.stopPrank();

        vm.startPrank(juniorUser1);
        usdt.approve(address(tranchePool), juniorDeposit);
        tranchePool.depositJuniorTranche(juniorDeposit);
        vm.stopPrank();

        vm.startPrank(equityUser1);
        usdt.approve(address(tranchePool), equityDeposit);
        tranchePool.depositEquityTranche(equityDeposit);
        vm.stopPrank();

        uint256 totalAvailable = tranchePool.getSeniorTrancheIdleValue() +
            tranchePool.getJuniorTrancheIdleValue() +
            tranchePool.getEquityTrancheIdleValue();

        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        // Allocate exactly total available
        uint256 disbursement = totalAvailable - 1_000 * USDT;
        uint256 fees = 1_000 * USDT;

        vm.prank(loanEngine);
        tranchePool.allocateCapital(disbursement, fees, borrower, feeManager);

        // Should succeed without integer overflow/underflow issues
        assertEq(
            tranchePool.getSeniorTrancheIdleValue(),
            0,
            "Senior idle should be zero"
        );
    }

    function test_AllocateCapital_SeniorExactExhaustion_Success() public {
        // Deposit specific amounts
        uint256 seniorDeposit = 80_00_000 * USDT;
        uint256 juniorDeposit = 50_00_000 * USDT;
        uint256 equityDeposit = 50_00_000 * USDT;

        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), seniorDeposit);
        tranchePool.depositSeniorTranche(seniorDeposit);
        vm.stopPrank();

        vm.startPrank(juniorUser1);
        usdt.approve(address(tranchePool), juniorDeposit);
        tranchePool.depositJuniorTranche(juniorDeposit);
        vm.stopPrank();

        vm.startPrank(equityUser1);
        usdt.approve(address(tranchePool), equityDeposit);
        tranchePool.depositEquityTranche(equityDeposit);
        vm.stopPrank();

        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        // Calculate allocation that will exhaust senior exactly
        // seniorAmount = totalAmount * 0.8 = seniorDeposit
        // totalAmount = seniorDeposit / 0.8 = 100M
        uint256 totalAmount = (seniorDeposit * 100) / 80;
        uint256 disbursement = totalAmount - 1_00_000 * USDT;
        uint256 fees = 1_00_000 * USDT;

        uint256 juniorIdleBefore = tranchePool.getJuniorTrancheIdleValue();
        uint256 equityIdleBefore = tranchePool.getEquityTrancheIdleValue();

        vm.prank(loanEngine);
        tranchePool.allocateCapital(disbursement, fees, borrower, feeManager);

        // Senior should be exactly exhausted
        assertEq(
            tranchePool.getSeniorTrancheIdleValue(),
            0,
            "Senior idle should be exactly zero"
        );
        assertEq(
            tranchePool.getSeniorTrancheDeployedValue(),
            seniorDeposit,
            "Senior deployed should equal original deposit"
        );

        // Calculate expected junior and equity allocations
        uint256 expectedJunior = (totalAmount * 15) / 100;
        uint256 expectedEquity = totalAmount - seniorDeposit - expectedJunior;

        // Junior and equity should be reduced but not exhausted
        assertEq(
            tranchePool.getJuniorTrancheIdleValue(),
            juniorIdleBefore - expectedJunior,
            "Junior idle reduced by expected amount"
        );
        assertGt(
            tranchePool.getJuniorTrancheIdleValue(),
            0,
            "Junior should have idle funds remaining"
        );

        assertEq(
            tranchePool.getEquityTrancheIdleValue(),
            equityIdleBefore - expectedEquity,
            "Equity idle reduced by expected amount"
        );
        assertGt(
            tranchePool.getEquityTrancheIdleValue(),
            0,
            "Equity should have idle funds remaining"
        );
    }

    // pending allocation tests, this one should be tested aggresively because it has most blast radius
    /*
        1. all allocations should succeed untill the cap is hit if the pool is in state of in deployed or commited state

        2. allocations should revert if the pool is in open or closed state

        3. tranche level allocations should not exceed the deployed value

        Partial absorption boundary tests
	•	Equity absorbs exactly remaining amount (not over)
	•	Junior absorbs exactly remaining amount
	•	Senior absorbs exactly remaining amount
	•	_minimum() logic never causes under- or over-allocation

These catch off-by-one / rounding edge cases.

⸻

    */

    // testing equitty tranche not having enough liquidity to cover its allocation
    // 1. equity_idle < equity_allocation -> junior_absorbs
    function test_AllocateCapital_EquityInsufficientLiquidity_JuniorAbsorbs()
        public
    {
        // Scenario: equity_idle < equity_allocation -> junior absorbs the shortfall

        // Deposits: Senior has plenty, Junior has plenty, Equity is SHORT
        uint256 seniorDeposit = 10_00_00_000 * USDT; // Plenty
        uint256 juniorDeposit = 5_00_00_000 * USDT; // Plenty
        uint256 equityDeposit = 50_00_000 * USDT; // SHORT - only 2M

        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), seniorDeposit);
        tranchePool.depositSeniorTranche(seniorDeposit);
        vm.stopPrank();

        vm.startPrank(juniorUser1);
        usdt.approve(address(tranchePool), juniorDeposit);
        tranchePool.depositJuniorTranche(juniorDeposit);
        vm.stopPrank();

        vm.startPrank(equityUser1);
        usdt.approve(address(tranchePool), equityDeposit);
        tranchePool.depositEquityTranche(equityDeposit);
        vm.stopPrank();

        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        // Allocate 100M total
        // Target: 80M senior, 15M junior, 5M equity
        // Reality: 80M senior (ok), 15M junior (ok), 5M equity (SHORT - only 2M available)
        // Expected: equity gets 2M, junior absorbs remaining 3M -> junior gets 15M + 3M = 18M
        uint256 totalAmount = 12_00_00_000 * USDT;
        uint256 disbursement = 11_90_00_000 * USDT;
        uint256 fees = 10_00_000 * USDT;

        vm.prank(loanEngine);
        tranchePool.allocateCapital(disbursement, fees, borrower, feeManager);

        // Verify equity is fully deployed (exhausted)
        assertEq(
            tranchePool.getEquityTrancheDeployedValue(),
            equityDeposit,
            "Equity should be fully deployed"
        );
        assertEq(
            tranchePool.getEquityTrancheIdleValue(),
            0,
            "Equity idle should be zero"
        );

        // Verify junior absorbed the equity shortfall
        uint256 targetEquity = (totalAmount * 5) / 100; // 5M
        uint256 equityShortfall = targetEquity - equityDeposit; // 3M
        uint256 targetJunior = (totalAmount * 15) / 100; // 15M
        uint256 expectedJuniorDeployed = targetJunior + equityShortfall; // 18M

        assertEq(
            tranchePool.getJuniorTrancheDeployedValue(),
            expectedJuniorDeployed,
            "Junior should absorb equity shortfall"
        );

        // Verify senior is unaffected (still at target)
        uint256 expectedSenior = (totalAmount * 80) / 100; // 80M
        assertEq(
            tranchePool.getSeniorTrancheDeployedValue(),
            expectedSenior,
            "Senior should be at target allocation"
        );

        // Verify total deployed equals total requested
        assertEq(
            tranchePool.getTotalDeployedValue(),
            totalAmount,
            "Total deployed must equal total allocation"
        );
    }

    // 2. equity_idle + junior_idle < equity_allocation -> senior_absorbs
    function test_AllocateCapital_EquityAndJuniorInsufficient_SeniorAbsorbs()
        public
    {
        // Scenario: equity_idle + junior_idle < (equity_allocation + junior_allocation overflow)
        // -> senior absorbs the combined shortfall

        // Deposits: Senior has plenty, Junior is SHORT, Equity is SHORT
        uint256 seniorDeposit = 2_00_00_000 * USDT; // Plenty
        uint256 juniorDeposit = 10_00_000 * USDT;
        uint256 equityDeposit = 50_00_000 * USDT;

        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), seniorDeposit);
        tranchePool.depositSeniorTranche(seniorDeposit);
        vm.stopPrank();

        vm.startPrank(juniorUser1);
        usdt.approve(address(tranchePool), juniorDeposit);
        tranchePool.depositJuniorTranche(juniorDeposit);
        vm.stopPrank();

        vm.startPrank(equityUser1);
        usdt.approve(address(tranchePool), equityDeposit);
        tranchePool.depositEquityTranche(equityDeposit);
        vm.stopPrank();

        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        // Allocate 100M total
        // Target: 80M senior, 15M junior, 5M equity
        // Reality:
        //   - Equity gets 2M (short by 3M)
        //   - Junior gets 10M initially (short by 5M from its target)
        //   - Junior tries to absorb equity's 3M shortfall -> needs 15M + 3M = 18M total
        //   - But junior only has 10M -> junior is short by 8M
        //   - Senior absorbs the remaining 8M -> senior gets 80M + 8M = 88M
        uint256 totalAmount = 2_60_00_000 * USDT;
        uint256 disbursement = 2_50_00_000 * USDT;
        uint256 fees = 10_00_000 * USDT;

        vm.prank(loanEngine);
        tranchePool.allocateCapital(disbursement, fees, borrower, feeManager);

        // Verify equity is fully deployed
        assertEq(
            tranchePool.getEquityTrancheDeployedValue(),
            equityDeposit,
            "Equity should be fully deployed"
        );
        assertEq(
            tranchePool.getEquityTrancheIdleValue(),
            0,
            "Equity idle should be zero"
        );

        // Verify junior is fully deployed
        assertEq(
            tranchePool.getJuniorTrancheDeployedValue(),
            juniorDeposit,
            "Junior should be fully deployed"
        );
        assertEq(
            tranchePool.getJuniorTrancheIdleValue(),
            0,
            "Junior idle should be zero"
        );

        // Verify senior absorbed all remaining allocation
        uint256 expectedSeniorDeployed = totalAmount -
            equityDeposit -
            juniorDeposit; // 88M
        assertEq(
            tranchePool.getSeniorTrancheDeployedValue(),
            expectedSeniorDeployed,
            "Senior should absorb combined shortfall"
        );

        // Verify total deployed equals total requested
        assertEq(
            tranchePool.getTotalDeployedValue(),
            totalAmount,
            "Total deployed must equal total allocation"
        );
    }

    // 3. equity_idle = 0 -> junior and senior absorbs
    function test_AllocateCapital_EquityZero_JuniorAndSeniorAbsorb() public {
        // Scenario: equity_idle = 0 -> junior and senior absorb

        // Deposits: Senior has plenty, Junior has some, Equity is ZERO
        uint256 seniorDeposit = 2_00_00_000 * USDT; // Plenty
        uint256 juniorDeposit = 30_00_000 * USDT; // Some

        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), seniorDeposit);
        tranchePool.depositSeniorTranche(seniorDeposit);
        vm.stopPrank();

        vm.startPrank(juniorUser1);
        usdt.approve(address(tranchePool), juniorDeposit);
        tranchePool.depositJuniorTranche(juniorDeposit);
        vm.stopPrank();

        // No equity deposit

        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        // Allocate 100M total
        // Target: 80M senior, 15M junior, 5M equity
        // Reality:
        //   - Equity gets 0M (short by 5M)
        //   - Junior should absorb equity's 5M -> junior needs 15M + 5M = 20M
        //   - Junior has 30M available -> junior gets 20M, has 10M left idle
        //   - Senior gets 80M as planned
        uint256 totalAmount = 100_00_000 * USDT;
        uint256 disbursement = 99_00_000 * USDT;
        uint256 fees = 1_00_000 * USDT;

        vm.prank(loanEngine);
        tranchePool.allocateCapital(disbursement, fees, borrower, feeManager);

        // Verify equity is zero (no deployment)
        assertEq(
            tranchePool.getEquityTrancheDeployedValue(),
            0,
            "Equity deployed should be zero"
        );
        assertEq(
            tranchePool.getEquityTrancheIdleValue(),
            0,
            "Equity idle should be zero"
        );

        // Verify junior absorbed equity's allocation
        uint256 targetJunior = (totalAmount * 15) / 100; // 15M
        uint256 targetEquity = (totalAmount * 5) / 100; // 5M
        uint256 expectedJuniorDeployed = targetJunior + targetEquity; // 20M

        assertEq(
            tranchePool.getJuniorTrancheDeployedValue(),
            expectedJuniorDeployed,
            "Junior should absorb full equity allocation"
        );

        // Verify senior is at target
        uint256 expectedSenior = (totalAmount * 80) / 100; // 80M
        assertEq(
            tranchePool.getSeniorTrancheDeployedValue(),
            expectedSenior,
            "Senior should be at target allocation"
        );

        // Verify total deployed equals total requested
        assertEq(
            tranchePool.getTotalDeployedValue(),
            totalAmount,
            "Total deployed must equal total allocation"
        );
    }

    // testing junior tranche not having enough liquidity to cover its allocation
    // 1. junior_idle < junior_allocation -> equity_absorbs -> senior_absorbs
    function test_AllocateCapital_JuniorInsufficient_EquityThenSeniorAbsorb()
        public
    {
        // ------------------------------------------------------------
        // Arrange
        // ------------------------------------------------------------

        uint256 seniorDeposit = 12_50_00_000 * USDT; // 125M
        uint256 juniorDeposit = 10_00_000 * USDT; // 1M
        uint256 equityDeposit = 50_00_000 * USDT; // 5M

        // Senior deposit
        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), seniorDeposit);
        tranchePool.depositSeniorTranche(seniorDeposit);
        vm.stopPrank();

        // Junior deposit (insufficient)
        vm.startPrank(juniorUser1);
        usdt.approve(address(tranchePool), juniorDeposit);
        tranchePool.depositJuniorTranche(juniorDeposit);
        vm.stopPrank();

        // Equity deposit (partial buffer)
        vm.startPrank(equityUser1);
        usdt.approve(address(tranchePool), equityDeposit);
        tranchePool.depositEquityTranche(equityDeposit);
        vm.stopPrank();

        // Move pool to COMMITED
        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        // Allocation request
        uint256 totalAmount = 12_00_00_000 * USDT; // 120M
        uint256 disbursement = totalAmount - 10_00_000 * USDT;
        uint256 fees = 10_00_000 * USDT;

        // ------------------------------------------------------------
        // Act
        // ------------------------------------------------------------

        vm.prank(loanEngine);
        tranchePool.allocateCapital(disbursement, fees, borrower, feeManager);

        // ------------------------------------------------------------
        // Assert
        // ------------------------------------------------------------

        // Junior is capped immediately
        assertEq(
            tranchePool.getJuniorTrancheDeployedValue(),
            juniorDeposit,
            "Junior should be fully deployed"
        );

        // Equity is capped immediately
        assertEq(
            tranchePool.getEquityTrancheDeployedValue(),
            equityDeposit,
            "Equity should be fully deployed"
        );

        // Senior absorbs *all remaining*
        uint256 expectedSeniorDeployed = totalAmount -
            juniorDeposit -
            equityDeposit;

        assertEq(
            tranchePool.getSeniorTrancheDeployedValue(),
            expectedSeniorDeployed,
            "Senior absorbs all remaining allocation"
        );

        // Global invariant
        assertEq(
            tranchePool.getTotalDeployedValue(),
            totalAmount,
            "Total deployed must equal total allocation"
        );
    }

    // 2. junior_idle = 0 -> equity_aborbs -> senior absorbs
    function test_AllocateCapital_JuniorZero_EquityThenSeniorAbsorb() public {
        // ------------------------------------------------------------
        // Arrange
        // ------------------------------------------------------------

        uint256 seniorDeposit = 12_00_00_000 * USDT; // 120M
        uint256 equityDeposit = 50_00_000 * USDT; // 5M
        // juniorDeposit = 0

        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), seniorDeposit);
        tranchePool.depositSeniorTranche(seniorDeposit);
        vm.stopPrank();

        vm.startPrank(equityUser1);
        usdt.approve(address(tranchePool), equityDeposit);
        tranchePool.depositEquityTranche(equityDeposit);
        vm.stopPrank();

        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        uint256 totalAmount = 10_00_00_000 * USDT; // 100M
        uint256 disbursement = totalAmount - 10_00_000 * USDT;
        uint256 fees = 10_00_000 * USDT;

        // ------------------------------------------------------------
        // Act
        // ------------------------------------------------------------

        vm.prank(loanEngine);
        tranchePool.allocateCapital(disbursement, fees, borrower, feeManager);

        // ------------------------------------------------------------
        // Assert
        // ------------------------------------------------------------

        // Junior skipped entirely
        assertEq(
            tranchePool.getJuniorTrancheDeployedValue(),
            0,
            "Junior deployed should be zero"
        );

        // Equity capped at idle
        assertEq(
            tranchePool.getEquityTrancheDeployedValue(),
            equityDeposit,
            "Equity fully deployed"
        );

        // Senior absorbs remaining
        uint256 expectedSenior = totalAmount - equityDeposit;

        assertEq(
            tranchePool.getSeniorTrancheDeployedValue(),
            expectedSenior,
            "Senior absorbs all remaining"
        );

        assertEq(
            tranchePool.getTotalDeployedValue(),
            totalAmount,
            "Total deployed invariant"
        );
    }

    // 3. junior_idle + equity_idle < junior_allocation -> senior_absorbs

    function test_AllocateCapital_JuniorAndEquityInsufficient_SeniorAbsorbs()
        public
    {
        // ------------------------------------------------------------
        // Arrange
        // ------------------------------------------------------------

        uint256 seniorDeposit = 13_00_00_000 * USDT; // 130M
        uint256 juniorDeposit = 10_00_000 * USDT; // 1M
        uint256 equityDeposit = 50_00_000 * USDT; // 5M

        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), seniorDeposit);
        tranchePool.depositSeniorTranche(seniorDeposit);
        vm.stopPrank();

        vm.startPrank(juniorUser1);
        usdt.approve(address(tranchePool), juniorDeposit);
        tranchePool.depositJuniorTranche(juniorDeposit);
        vm.stopPrank();

        vm.startPrank(equityUser1);
        usdt.approve(address(tranchePool), equityDeposit);
        tranchePool.depositEquityTranche(equityDeposit);
        vm.stopPrank();

        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        uint256 totalAmount = 10_00_00_000 * USDT; // 100M
        uint256 disbursement = totalAmount - 10_00_000 * USDT;
        uint256 fees = 10_00_000 * USDT;

        // ------------------------------------------------------------
        // Act
        // ------------------------------------------------------------

        vm.prank(loanEngine);
        tranchePool.allocateCapital(disbursement, fees, borrower, feeManager);

        // ------------------------------------------------------------
        // Assert
        // ------------------------------------------------------------

        // Junior fully exhausted
        assertEq(
            tranchePool.getJuniorTrancheDeployedValue(),
            juniorDeposit,
            "Junior fully exhausted"
        );

        // Equity fully exhausted
        assertEq(
            tranchePool.getEquityTrancheDeployedValue(),
            equityDeposit,
            "Equity fully exhausted"
        );

        // Senior absorbs everything else
        uint256 expectedSenior = totalAmount - juniorDeposit - equityDeposit;

        assertEq(
            tranchePool.getSeniorTrancheDeployedValue(),
            expectedSenior,
            "Senior absorbs combined shortfall"
        );

        assertEq(
            tranchePool.getTotalDeployedValue(),
            totalAmount,
            "Total deployed invariant"
        );
    }

    // proper testing of the order is demanded
    // junior should not absorb before equity tranche
    // senior should not absorb before junior and equity tranche => senior iff junior + equity is insufficient

    // test with different allocation factor
    // 1. senior: 100%, junior: 0%, equity: 0%
    function test_AllocateCapital_Senior100Percent() public {
        _depositToAllTranches();

        vm.startPrank(deployer);
        tranchePool.setTrancheCapitalAllocationFactorJunior(0);
        tranchePool.setTrancheCapitalAllocationFactorSenior(100);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);
        vm.stopPrank();

        uint256 totalAmount = 1_00_00_000 * USDT;

        vm.prank(loanEngine);
        tranchePool.allocateCapital(
            totalAmount - 10_000 * USDT,
            10_000 * USDT,
            borrower,
            feeManager
        );

        assertEq(
            tranchePool.getSeniorTrancheDeployedValue(),
            totalAmount,
            "Senior gets 100%"
        );
        assertEq(tranchePool.getJuniorTrancheDeployedValue(), 0);
        assertEq(tranchePool.getEquityTrancheDeployedValue(), 0);
    }

    // 2. senior: 0%, junior: 100%, equity: 0%
    function test_AllocateCapital_Junior100Percent() public {
        _depositToAllTranches();

        vm.startPrank(deployer);
        tranchePool.setTrancheCapitalAllocationFactorSenior(0);
        tranchePool.setTrancheCapitalAllocationFactorJunior(100);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);
        vm.stopPrank();

        uint256 totalAmount = 1_00_00_000 * USDT;

        vm.prank(loanEngine);
        tranchePool.allocateCapital(
            totalAmount - 10_000 * USDT,
            10_000 * USDT,
            borrower,
            feeManager
        );

        assertEq(tranchePool.getSeniorTrancheDeployedValue(), 0);
        assertEq(
            tranchePool.getJuniorTrancheDeployedValue(),
            totalAmount,
            "Junior gets 100%"
        );
        assertEq(tranchePool.getEquityTrancheDeployedValue(), 0);
    }

    // 3. senior: 0%, junior: 0%, equity: 100%
    function test_AllocateCapital_Equity100Percent() public {
        _depositToAllTranches();

        vm.startPrank(deployer);
        tranchePool.setTrancheCapitalAllocationFactorSenior(0);
        tranchePool.setTrancheCapitalAllocationFactorJunior(0);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);
        vm.stopPrank();

        uint256 totalAmount = 1_00_00_000 * USDT;

        vm.prank(loanEngine);
        tranchePool.allocateCapital(
            totalAmount - 10_000 * USDT,
            10_000 * USDT,
            borrower,
            feeManager
        );

        assertEq(tranchePool.getSeniorTrancheDeployedValue(), 0);
        assertEq(tranchePool.getJuniorTrancheDeployedValue(), 0);
        assertEq(
            tranchePool.getEquityTrancheDeployedValue(),
            totalAmount,
            "Equity gets 100%"
        );
    }

    // 4. senior: 70%, junior: 20%, equity: rest
    function test_AllocateCapital_70_20_10() public {
        _depositToAllTranches();

        vm.startPrank(deployer);
        tranchePool.setTrancheCapitalAllocationFactorJunior(20);
        tranchePool.setTrancheCapitalAllocationFactorSenior(70);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);
        vm.stopPrank();

        uint256 totalAmount = 1_00_00_000 * USDT;

        vm.prank(loanEngine);
        tranchePool.allocateCapital(
            totalAmount - 10_000 * USDT,
            10_000 * USDT,
            borrower,
            feeManager
        );

        assertEq(
            tranchePool.getSeniorTrancheDeployedValue(),
            (totalAmount * 70) / 100
        );
        assertEq(
            tranchePool.getJuniorTrancheDeployedValue(),
            (totalAmount * 20) / 100
        );
        assertEq(
            tranchePool.getEquityTrancheDeployedValue(),
            totalAmount - (totalAmount * 70) / 100 - (totalAmount * 20) / 100
        );
    }

    // 5. senior + junior = 100%, equity: 0%
    function test_AllocateCapital_80_20_0() public {
        _depositToAllTranches();

        vm.startPrank(deployer);
        tranchePool.setTrancheCapitalAllocationFactorSenior(80);
        tranchePool.setTrancheCapitalAllocationFactorJunior(20);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);
        vm.stopPrank();

        uint256 totalAmount = 1_00_00_000 * USDT;

        vm.prank(loanEngine);
        tranchePool.allocateCapital(
            totalAmount - 10_000 * USDT,
            10_000 * USDT,
            borrower,
            feeManager
        );

        assertEq(
            tranchePool.getSeniorTrancheDeployedValue(),
            (totalAmount * 80) / 100
        );
        assertEq(
            tranchePool.getJuniorTrancheDeployedValue(),
            (totalAmount * 20) / 100
        );
        assertEq(tranchePool.getEquityTrancheDeployedValue(), 0);
    }

    // mid lifecycle changing of allocation factor, should not affect deployed capital
    function test_AllocationFactorChange_DoesNotAffectDeployedCapital() public {
        _depositToAllTranches();

        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        uint256 totalAmount = 1_00_00_000 * USDT;

        vm.prank(loanEngine);
        tranchePool.allocateCapital(
            totalAmount - 10_000 * USDT,
            10_000 * USDT,
            borrower,
            feeManager
        );

        uint256 seniorBefore = tranchePool.getSeniorTrancheDeployedValue();
        uint256 juniorBefore = tranchePool.getJuniorTrancheDeployedValue();
        uint256 equityBefore = tranchePool.getEquityTrancheDeployedValue();

        // Change factors mid lifecycle
        vm.startPrank(deployer);
        tranchePool.setTrancheCapitalAllocationFactorSenior(70);
        tranchePool.setTrancheCapitalAllocationFactorJunior(20);
        vm.stopPrank();

        // Deployed values must NOT change
        assertEq(tranchePool.getSeniorTrancheDeployedValue(), seniorBefore);
        assertEq(tranchePool.getJuniorTrancheDeployedValue(), juniorBefore);
        assertEq(tranchePool.getEquityTrancheDeployedValue(), equityBefore);
    }

    // what if allocation factor change mid lifecycle
    // what if the allocation factor is initially 80-15-5 and then change to 70-20-10
    function test_AllocationFactorChange_AffectsFutureAllocations() public {
        _depositToAllTranches();

        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        // First allocation (80/15/5)
        vm.prank(loanEngine);
        tranchePool.allocateCapital(
            50_00_000 * USDT,
            5_000 * USDT,
            borrower,
            feeManager
        );

        // Change factors
        vm.startPrank(deployer);
        tranchePool.setTrancheCapitalAllocationFactorSenior(70);
        tranchePool.setTrancheCapitalAllocationFactorJunior(20);
        vm.stopPrank();

        uint256 seniorBefore = tranchePool.getSeniorTrancheDeployedValue();
        uint256 juniorBefore = tranchePool.getJuniorTrancheDeployedValue();
        uint256 equityBefore = tranchePool.getEquityTrancheDeployedValue();

        // Second allocation (70/20/10)
        vm.prank(loanEngine);
        tranchePool.allocateCapital(
            50_00_000 * USDT,
            5_000 * USDT,
            borrower,
            feeManager
        );

        uint256 secondTotal = 50_05_000 * USDT;

        assertEq(
            tranchePool.getSeniorTrancheDeployedValue(),
            seniorBefore + (secondTotal * 70) / 100
        );
        assertEq(
            tranchePool.getJuniorTrancheDeployedValue(),
            juniorBefore + (secondTotal * 20) / 100
        );
        assertEq(
            tranchePool.getEquityTrancheDeployedValue(),
            equityBefore +
                secondTotal -
                (secondTotal * 70) /
                100 -
                (secondTotal * 20) /
                100
        );
    }

    // changing the repayment and loss allocation models to take account of the allocation factor based on the info stored locally not the global allocation factors.
    // TODO: need exhaustive testing there

}
