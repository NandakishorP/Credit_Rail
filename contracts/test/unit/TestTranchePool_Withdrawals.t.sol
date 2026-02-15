// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {TestTranchePoolBase} from "./TestTranchePoolBase.t.sol";
import {TranchePool} from "../../src/TranchePool.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {VmSafe} from "forge-std/Vm.sol";

contract TestTranchePool_Withdrawals is TestTranchePoolBase {
    function test_WithdrawSeniorTranche_ByShares_Success() public {
        // Deposit first
        uint256 depositAmount = 5_00_00_000 * USDT;
        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), depositAmount);
        tranchePool.depositSeniorTranche(depositAmount);

        uint256 balanceBefore = usdt.balanceOf(seniorUser1);
        uint256 sharesToWithdraw = 2_00_00_000 * USDT;

        tranchePool.withdrawSeniorTranche(sharesToWithdraw);
        vm.stopPrank();

        assertEq(usdt.balanceOf(seniorUser1), balanceBefore + sharesToWithdraw);
        assertEq(
            tranchePool.getSeniorTrancheShares(seniorUser1),
            depositAmount - sharesToWithdraw
        );
    }

    function test_WithdrawSeniorTranche_All_Success() public {
        uint256 depositAmount = 5_00_00_000 * USDT;
        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), depositAmount);
        tranchePool.depositSeniorTranche(depositAmount);

        uint256 balanceBefore = usdt.balanceOf(seniorUser1);

        // Withdraw all (pass 0)
        tranchePool.withdrawSeniorTranche(0);
        vm.stopPrank();

        assertEq(usdt.balanceOf(seniorUser1), balanceBefore + depositAmount);
        assertEq(tranchePool.getSeniorTrancheShares(seniorUser1), 0);
    }

    function test_WithdrawSeniorTranche_RevertIf_NotOpenOrClosed() public {
        uint256 depositAmount = 5_00_00_000 * USDT;
        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), depositAmount);
        tranchePool.depositSeniorTranche(depositAmount);
        vm.stopPrank();

        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        vm.prank(seniorUser1);
        vm.expectRevert(
            abi.encodeWithSelector(
                TranchePool.TranchePool__WithdrawNotAllowed.selector,
                TranchePool.PoolState.COMMITED
            )
        );
        tranchePool.withdrawSeniorTranche(1_00_000 * USDT);
    }

    function test_WithdrawSeniorTranche_RevertIf_InsufficientShares() public {
        vm.prank(seniorUser1);
        vm.expectRevert(TranchePool.TranchePool__InsufficientShares.selector);
        tranchePool.withdrawSeniorTranche(1_00_000 * USDT);
    }

    function test_WithdrawSeniorTranche_RevertIf_WithdrawMoreThanOwned()
        public
    {
        uint256 depositAmount = 5_00_00_000 * USDT;
        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), depositAmount);
        tranchePool.depositSeniorTranche(depositAmount);

        vm.expectRevert(TranchePool.TranchePool__InsufficientShares.selector);
        tranchePool.withdrawSeniorTranche(depositAmount + 1);
        vm.stopPrank();
    }

    function test_WithdrawSeniorTrancheByAmount_Success() public {
        uint256 depositAmount = 5_00_00_000 * USDT;
        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), depositAmount);
        tranchePool.depositSeniorTranche(depositAmount);

        uint256 withdrawAmount = 2_00_00_000 * USDT;
        uint256 balanceBefore = usdt.balanceOf(seniorUser1);

        tranchePool.withdrawSeniorTrancheByAmount(withdrawAmount);
        vm.stopPrank();

        assertEq(usdt.balanceOf(seniorUser1), balanceBefore + withdrawAmount);
    }

    function test_WithdrawSeniorTrancheByAmount_RevertIf_ZeroAmount() public {
        uint256 depositAmount = 5_00_00_000 * USDT;
        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), depositAmount);
        tranchePool.depositSeniorTranche(depositAmount);

        vm.expectRevert(TranchePool.TranchePool__ZeroWithdrawal.selector);
        tranchePool.withdrawSeniorTrancheByAmount(0);
        vm.stopPrank();
    }

    /*//////////////////////////////////////////////////////////////
                        WITHDRAWAL TESTS - JUNIOR
    //////////////////////////////////////////////////////////////*/

    function test_WithdrawJuniorTranche_ByShares_Success() public {
        uint256 depositAmount = 2_00_00_000 * USDT;
        vm.startPrank(juniorUser1);
        usdt.approve(address(tranchePool), depositAmount);
        tranchePool.depositJuniorTranche(depositAmount);

        uint256 balanceBefore = usdt.balanceOf(juniorUser1);
        uint256 sharesToWithdraw = 1_00_00_000 * USDT;

        tranchePool.withdrawJuniorTranche(sharesToWithdraw);
        vm.stopPrank();

        assertEq(usdt.balanceOf(juniorUser1), balanceBefore + sharesToWithdraw);
        assertEq(
            tranchePool.getJuniorTrancheShares(juniorUser1),
            depositAmount - sharesToWithdraw
        );
    }

    function test_WithdrawJuniorTranche_All_Success() public {
        uint256 depositAmount = 2_00_00_000 * USDT;
        vm.startPrank(juniorUser1);
        usdt.approve(address(tranchePool), depositAmount);
        tranchePool.depositJuniorTranche(depositAmount);

        uint256 balanceBefore = usdt.balanceOf(juniorUser1);

        tranchePool.withdrawJuniorTranche(0);
        vm.stopPrank();

        assertEq(usdt.balanceOf(juniorUser1), balanceBefore + depositAmount);
        assertEq(tranchePool.getJuniorTrancheShares(juniorUser1), 0);
    }

    function test_WithdrawJuniorTrancheByAmount_Success() public {
        uint256 depositAmount = 2_00_00_000 * USDT;
        vm.startPrank(juniorUser1);
        usdt.approve(address(tranchePool), depositAmount);
        tranchePool.depositJuniorTranche(depositAmount);

        uint256 withdrawAmount = 1_00_00_000 * USDT;
        uint256 balanceBefore = usdt.balanceOf(juniorUser1);

        tranchePool.withdrawJuniorTrancheByAmount(withdrawAmount);
        vm.stopPrank();

        assertEq(usdt.balanceOf(juniorUser1), balanceBefore + withdrawAmount);
    }

    /*//////////////////////////////////////////////////////////////
                        WITHDRAWAL TESTS - EQUITY
    //////////////////////////////////////////////////////////////*/

    function test_WithdrawEquityTranche_ByShares_Success() public {
        uint256 depositAmount = 1_00_00_000 * USDT;
        vm.startPrank(equityUser1);
        usdt.approve(address(tranchePool), depositAmount);
        tranchePool.depositEquityTranche(depositAmount);

        uint256 balanceBefore = usdt.balanceOf(equityUser1);
        uint256 sharesToWithdraw = 50_00_000 * USDT;

        tranchePool.withdrawEquityTranche(sharesToWithdraw);
        vm.stopPrank();

        assertEq(usdt.balanceOf(equityUser1), balanceBefore + sharesToWithdraw);
        assertEq(
            tranchePool.getEquityTrancheShares(equityUser1),
            depositAmount - sharesToWithdraw
        );
    }

    function test_WithdrawEquityTranche_All_Success() public {
        uint256 depositAmount = 1_00_00_000 * USDT;
        vm.startPrank(equityUser1);
        usdt.approve(address(tranchePool), depositAmount);
        tranchePool.depositEquityTranche(depositAmount);

        uint256 balanceBefore = usdt.balanceOf(equityUser1);

        tranchePool.withdrawEquityTranche(0);
        vm.stopPrank();

        assertEq(usdt.balanceOf(equityUser1), balanceBefore + depositAmount);
        assertEq(tranchePool.getEquityTrancheShares(equityUser1), 0);
    }

    function test_WithdrawEquityTrancheByAmount_Success() public {
        uint256 depositAmount = 1_00_00_000 * USDT;
        vm.startPrank(equityUser1);
        usdt.approve(address(tranchePool), depositAmount);
        tranchePool.depositEquityTranche(depositAmount);

        uint256 withdrawAmount = 50_00_000 * USDT;
        uint256 balanceBefore = usdt.balanceOf(equityUser1);

        tranchePool.withdrawEquityTrancheByAmount(withdrawAmount);
        vm.stopPrank();

        assertEq(usdt.balanceOf(equityUser1), balanceBefore + withdrawAmount);
    }

}
