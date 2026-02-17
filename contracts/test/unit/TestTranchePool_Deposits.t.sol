// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {TestTranchePoolBase} from "./TestTranchePoolBase.t.sol";
import {TranchePool, ITranchePool} from "../../src/TranchePool.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {VmSafe} from "forge-std/Vm.sol";

contract TestTranchePool_Deposits is TestTranchePoolBase {
    function testDepositSeniorTrancheRevertsIfPoolIsNotOpen() public {
        vm.prank(deployer);
        tranchePool.setPoolState(ITranchePool.PoolState.COMMITED);
        vm.startPrank(seniorUser1);
        ERC20Mock(usdt).approve(address(tranchePool), 10_00_000 * USDT);
        vm.expectRevert(ITranchePool.TranchePool__PoolIsNotOpen.selector);
        tranchePool.depositSeniorTranche(10_00_000 * USDT);
        vm.stopPrank();
    }

    function testDepositSeniorTrancheRevertIfLessThanMinimumDeposit() public {
        vm.startPrank(seniorUser1);
        ERC20Mock(usdt).approve(address(tranchePool), 1_00_000 * USDT);
        vm.expectRevert(
            abi.encodeWithSignature(
                "TranchePool__LessThanDepositThreshold(uint256)",
                1_00_000 * USDT
            )
        );
        tranchePool.depositSeniorTranche(1_00_000 * USDT);
        vm.stopPrank();
    }

    function testDepositRevertIfUserIsNotWhiteListedSeniorTranche() public {
        vm.startPrank(falseUser);
        uint256 falseUser1DepositAmount = 5_00_00_000 * USDT;
        ERC20Mock(usdt).approve(address(tranchePool), falseUser1DepositAmount);
        vm.expectRevert(
            abi.encodeWithSignature(
                "TranchePool__NotWhiteListed(address)",
                falseUser
            )
        );
        tranchePool.depositSeniorTranche(falseUser1DepositAmount);
        vm.stopPrank();
    }

    function testDepostiSeniorTracheRevertsIfMaxPoolCapExceeeded() public {
        uint256 seniorUser1DepositAmount = 5_00_00_000 * USDT;
        uint256 seniorUser2DepositAmount = 5_00_00_000 * USDT;
        uint256 seniorUser3DepositAmount = 5_00_00_000 * USDT;
        vm.startPrank(seniorUser1);
        ERC20Mock(usdt).approve(address(tranchePool), seniorUser1DepositAmount);
        tranchePool.depositSeniorTranche(seniorUser1DepositAmount);
        vm.stopPrank();
        vm.startPrank(seniorUser2);
        ERC20Mock(usdt).approve(address(tranchePool), seniorUser2DepositAmount);
        tranchePool.depositSeniorTranche(seniorUser2DepositAmount);
        vm.stopPrank();
        vm.startPrank(seniorUser3);
        ERC20Mock(usdt).approve(address(tranchePool), seniorUser3DepositAmount);
        vm.expectRevert(
            abi.encodeWithSignature(
                "TranchePool__MaxDepositCapExceeded(uint256,uint256)",
                tranchePool.getSeniorTrancheMaxDepositCap(),
                seniorUser3DepositAmount
            )
        );
        tranchePool.depositSeniorTranche(seniorUser1DepositAmount);
        vm.stopPrank();
    }

    // Invariant: During OPEN, senior shares represent principal 1:1.
    // totalSeniorShares == seniorTrancheIdleValue always holds.
    function testFullDepositSeniorTranche() public {
        uint256 seniorTrancheDeposit1 = 5_00_00_000 * USDT;
        uint256 seniorTrancheDeposit2 = 5_00_00_000 * USDT;
        uint256 seniorTrancheDeposit3 = 3_00_00_000 * USDT;
        assertEq(tranchePool.getSeniorUserIndex(seniorUser1), 0);
        assertEq(tranchePool.getSeniorUserIndex(seniorUser2), 0);
        assertEq(tranchePool.getSeniorUserIndex(seniorUser3), 0);
        assertEq(tranchePool.getTotalSeniorShares(), 0);
        assertEq(tranchePool.getSeniorTrancheIdleValue(), 0);
        vm.startPrank(seniorUser1);
        ERC20Mock(usdt).approve(address(tranchePool), seniorTrancheDeposit1);
        vm.expectEmit(true, false, false, true);
        emit ITranchePool.FundsDepositedToSeniorTranche(
            seniorUser1,
            seniorTrancheDeposit1,
            seniorTrancheDeposit1,
            block.timestamp
        );
        tranchePool.depositSeniorTranche(seniorTrancheDeposit1);
        vm.stopPrank();
        assertEq(tranchePool.getTotalSeniorShares(), seniorTrancheDeposit1);
        assertEq(
            tranchePool.getSeniorTrancheIdleValue(),
            seniorTrancheDeposit1
        );

        vm.startPrank(seniorUser2);
        ERC20Mock(usdt).approve(address(tranchePool), seniorTrancheDeposit2);
        vm.expectEmit(true, false, false, true);
        emit ITranchePool.FundsDepositedToSeniorTranche(
            seniorUser2,
            seniorTrancheDeposit2,
            seniorTrancheDeposit2,
            block.timestamp
        );
        tranchePool.depositSeniorTranche(seniorTrancheDeposit2);
        vm.stopPrank();
        assertEq(
            tranchePool.getSeniorTrancheIdleValue(),
            seniorTrancheDeposit1 + seniorTrancheDeposit2
        );

        assertEq(
            tranchePool.getTotalSeniorShares(),
            seniorTrancheDeposit1 + seniorTrancheDeposit2
        );

        vm.startPrank(seniorUser3);
        ERC20Mock(usdt).approve(address(tranchePool), seniorTrancheDeposit3);
        vm.expectEmit(true, false, false, true);
        emit ITranchePool.FundsDepositedToSeniorTranche(
            seniorUser3,
            seniorTrancheDeposit3,
            seniorTrancheDeposit3,
            block.timestamp
        );
        tranchePool.depositSeniorTranche(seniorTrancheDeposit3);
        vm.stopPrank();

        assertEq(
            tranchePool.getSeniorTrancheIdleValue(),
            seniorTrancheDeposit1 +
                seniorTrancheDeposit2 +
                seniorTrancheDeposit3
        );
        assertEq(tranchePool.getSeniorTrancheDeployedValue(), 0);

        assertEq(
            tranchePool.getTotalSeniorShares(),
            seniorTrancheDeposit1 +
                seniorTrancheDeposit2 +
                seniorTrancheDeposit3
        );

        assertEq(
            seniorTrancheDeposit1,
            tranchePool.getSeniorTrancheBalance(seniorUser1)
        );

        assertEq(tranchePool.getSeniorUserIndex(seniorUser1), 1e18);

        assertEq(
            seniorTrancheDeposit1,
            tranchePool.getSeniorTrancheShares(seniorUser1)
        );

        assertEq(
            seniorTrancheDeposit2,
            tranchePool.getSeniorTrancheBalance(seniorUser2)
        );
        assertEq(tranchePool.getSeniorUserIndex(seniorUser2), 1e18);

        assertEq(
            seniorTrancheDeposit2,
            tranchePool.getSeniorTrancheShares(seniorUser2)
        );
        assertEq(
            seniorTrancheDeposit3,
            tranchePool.getSeniorTrancheBalance(seniorUser3)
        );
        assertEq(tranchePool.getSeniorUserIndex(seniorUser3), 1e18);

        assertEq(
            seniorTrancheDeposit3,
            tranchePool.getSeniorTrancheShares(seniorUser3)
        );

        assertEq(
            tranchePool.getTotalSeniorShares(),
            tranchePool.getSeniorTrancheIdleValue()
        );
    }

    function testDepositSeniorTrancheExactlyAtMaxCap() public {
        uint256 seniorUser1DepositAmount = 6_50_00_000 * USDT;
        uint256 seniorUser2DepositAmount = 6_50_00_000 * USDT;
        vm.startPrank(seniorUser1);
        ERC20Mock(usdt).approve(address(tranchePool), seniorUser1DepositAmount);
        tranchePool.depositSeniorTranche(seniorUser1DepositAmount);
        vm.stopPrank();
        vm.startPrank(seniorUser2);
        ERC20Mock(usdt).approve(address(tranchePool), seniorUser2DepositAmount);
        tranchePool.depositSeniorTranche(seniorUser2DepositAmount);
        vm.stopPrank();
        assertEq(
            tranchePool.getSeniorTrancheIdleValue(),
            tranchePool.getSeniorTrancheMaxDepositCap()
        );
    }

    function testDepositSeniorTrancheMultipleTimesBySameUser() public {
        uint256 seniorUser1FirstDeposit = 3_00_00_000 * USDT;
        uint256 seniorUser1SecondDeposit = 2_00_00_000 * USDT;
        vm.startPrank(seniorUser1);
        ERC20Mock(usdt).approve(
            address(tranchePool),
            seniorUser1FirstDeposit + seniorUser1SecondDeposit
        );
        tranchePool.depositSeniorTranche(seniorUser1FirstDeposit);
        tranchePool.depositSeniorTranche(seniorUser1SecondDeposit);
        vm.stopPrank();
        assertEq(
            tranchePool.getSeniorTrancheBalance(seniorUser1),
            seniorUser1FirstDeposit + seniorUser1SecondDeposit
        );

        assertEq(
            tranchePool.getSeniorTrancheShares(seniorUser1),
            seniorUser1FirstDeposit + seniorUser1SecondDeposit
        );
    }

    function testDepositSeniorTrancheAccountingIsCorrectWhenDepositAndWithdrawAtSameTime()
        public
    {
        uint256 seniorUser1Deposit = 5_00_00_000 * USDT;
        uint256 seniorUser1Withdraw = 2_00_00_000 * USDT;
        vm.startPrank(seniorUser1);
        ERC20Mock(usdt).approve(address(tranchePool), seniorUser1Deposit);
        tranchePool.depositSeniorTranche(seniorUser1Deposit);
        tranchePool.withdrawSeniorTranche(seniorUser1Withdraw);
        vm.stopPrank();
        assertEq(
            tranchePool.getSeniorTrancheBalance(seniorUser1),
            seniorUser1Deposit - seniorUser1Withdraw
        );

        assertEq(
            tranchePool.getSeniorTrancheShares(seniorUser1),
            seniorUser1Deposit - seniorUser1Withdraw
        );

        vm.startPrank(seniorUser1);
        ERC20Mock(usdt).approve(address(tranchePool), seniorUser1Withdraw);
        tranchePool.depositSeniorTranche(seniorUser1Withdraw);

        vm.stopPrank();

        assertEq(
            tranchePool.getSeniorTrancheBalance(seniorUser1),
            seniorUser1Deposit
        );

        assertEq(
            tranchePool.getSeniorTrancheShares(seniorUser1),
            seniorUser1Deposit
        );
    }

    // junior tranche deposit tests

    function testDepositJuniorTrancheRevertIfNotOpen() public {
        vm.prank(deployer);
        tranchePool.setPoolState(ITranchePool.PoolState.COMMITED);
        vm.startPrank(juniorUser1);
        ERC20Mock(usdt).approve(address(tranchePool), 10_00_000 * USDT);
        vm.expectRevert(ITranchePool.TranchePool__PoolIsNotOpen.selector);
        tranchePool.depositJuniorTranche(10_00_000 * USDT);
        vm.stopPrank();
    }

    function testDepositJuniorTrancheRevertIfLessThanMinimumDeposit() public {
        vm.startPrank(juniorUser1);
        ERC20Mock(usdt).approve(address(tranchePool), 1_00_000 * USDT);
        vm.expectRevert(
            abi.encodeWithSignature(
                "TranchePool__LessThanDepositThreshold(uint256)",
                1_00_000 * USDT
            )
        );
        tranchePool.depositJuniorTranche(1_00_000 * USDT);
        vm.stopPrank();
    }

    function testDepositRevertIfUserIsNotWhiteListedJuniorTranche() public {
        vm.startPrank(falseUser);
        uint256 falseUser1DepositAmount = 5_00_00_000 * USDT;
        ERC20Mock(usdt).approve(address(tranchePool), falseUser1DepositAmount);
        vm.expectRevert(
            abi.encodeWithSignature(
                "TranchePool__NotWhiteListed(address)",
                falseUser
            )
        );
        tranchePool.depositJuniorTranche(falseUser1DepositAmount);
        vm.stopPrank();
    }

    function testDepostiJuniorTracheRevertsIfMaxPoolCapExceeeded() public {
        uint256 juniorUser1DepositAmount = 2_00_00_000 * USDT;
        uint256 juniorUser2DepositAmount = 2_00_00_000 * USDT;
        uint256 juniorUser3DepositAmount = 2_00_00_000 * USDT;
        vm.startPrank(juniorUser1);
        ERC20Mock(usdt).approve(address(tranchePool), juniorUser1DepositAmount);
        tranchePool.depositJuniorTranche(juniorUser1DepositAmount);
        vm.stopPrank();
        vm.startPrank(juniorUser2);
        ERC20Mock(usdt).approve(address(tranchePool), juniorUser2DepositAmount);
        tranchePool.depositJuniorTranche(juniorUser2DepositAmount);
        vm.stopPrank();
        vm.startPrank(juniorUser3);
        ERC20Mock(usdt).approve(address(tranchePool), juniorUser3DepositAmount);
        vm.expectRevert(
            abi.encodeWithSignature(
                "TranchePool__MaxDepositCapExceeded(uint256,uint256)",
                tranchePool.getJuniorTrancheMaxDepositCap(),
                juniorUser3DepositAmount
            )
        );
        tranchePool.depositJuniorTranche(juniorUser1DepositAmount);
        vm.stopPrank();
    }

    // Invariant: During OPEN, junior shares represent principal 1:1.
    // totalJuniorShares == juniorTrancheIdleValue always holds.
    function testFullDepositJuniorTranche() public {
        uint256 juniorTrancheDeposit1 = 2_00_00_000 * USDT;
        uint256 juniorTrancheDeposit2 = 2_00_00_000 * USDT;
        uint256 juniorTrancheDeposit3 = 1_00_00_000 * USDT;
        assertEq(tranchePool.getJuniorUserIndex(juniorUser1), 0);
        assertEq(tranchePool.getJuniorUserIndex(juniorUser2), 0);
        assertEq(tranchePool.getJuniorUserIndex(juniorUser3), 0);
        assertEq(tranchePool.getTotalJuniorShares(), 0);
        assertEq(tranchePool.getJuniorTrancheIdleValue(), 0);
        vm.startPrank(juniorUser1);
        ERC20Mock(usdt).approve(address(tranchePool), juniorTrancheDeposit1);
        vm.expectEmit(true, false, false, true);
        emit ITranchePool.FundsDepositedToJuniorTranche(
            juniorUser1,
            juniorTrancheDeposit1,
            juniorTrancheDeposit1,
            block.timestamp
        );
        tranchePool.depositJuniorTranche(juniorTrancheDeposit1);
        vm.stopPrank();
        assertEq(tranchePool.getTotalJuniorShares(), juniorTrancheDeposit1);
        assertEq(
            tranchePool.getJuniorTrancheIdleValue(),
            juniorTrancheDeposit1
        );

        vm.startPrank(juniorUser2);
        ERC20Mock(usdt).approve(address(tranchePool), juniorTrancheDeposit2);
        vm.expectEmit(true, false, false, true);
        emit ITranchePool.FundsDepositedToJuniorTranche(
            juniorUser2,
            juniorTrancheDeposit2,
            juniorTrancheDeposit2,
            block.timestamp
        );
        tranchePool.depositJuniorTranche(juniorTrancheDeposit2);
        vm.stopPrank();
        assertEq(
            tranchePool.getJuniorTrancheIdleValue(),
            juniorTrancheDeposit1 + juniorTrancheDeposit2
        );

        assertEq(
            tranchePool.getTotalJuniorShares(),
            juniorTrancheDeposit1 + juniorTrancheDeposit2
        );

        vm.startPrank(juniorUser3);
        ERC20Mock(usdt).approve(address(tranchePool), juniorTrancheDeposit3);
        vm.expectEmit(true, false, false, true);
        emit ITranchePool.FundsDepositedToJuniorTranche(
            juniorUser3,
            juniorTrancheDeposit3,
            juniorTrancheDeposit3,
            block.timestamp
        );
        tranchePool.depositJuniorTranche(juniorTrancheDeposit3);
        vm.stopPrank();

        assertEq(
            tranchePool.getJuniorTrancheIdleValue(),
            juniorTrancheDeposit1 +
                juniorTrancheDeposit2 +
                juniorTrancheDeposit3
        );
        assertEq(tranchePool.getJuniorTrancheDeployedValue(), 0);

        assertEq(
            tranchePool.getTotalJuniorShares(),
            juniorTrancheDeposit1 +
                juniorTrancheDeposit2 +
                juniorTrancheDeposit3
        );

        assertEq(
            juniorTrancheDeposit1,
            tranchePool.getJuniorTrancheBalance(juniorUser1)
        );

        assertEq(tranchePool.getJuniorUserIndex(juniorUser1), 1e18);

        assertEq(
            juniorTrancheDeposit1,
            tranchePool.getJuniorTrancheShares(juniorUser1)
        );

        assertEq(
            juniorTrancheDeposit2,
            tranchePool.getJuniorTrancheBalance(juniorUser2)
        );
        assertEq(tranchePool.getJuniorUserIndex(juniorUser2), 1e18);

        assertEq(
            juniorTrancheDeposit2,
            tranchePool.getJuniorTrancheShares(juniorUser2)
        );
        assertEq(
            juniorTrancheDeposit3,
            tranchePool.getJuniorTrancheBalance(juniorUser3)
        );
        assertEq(tranchePool.getJuniorUserIndex(juniorUser3), 1e18);

        assertEq(
            juniorTrancheDeposit3,
            tranchePool.getJuniorTrancheShares(juniorUser3)
        );

        assertEq(
            tranchePool.getTotalJuniorShares(),
            tranchePool.getJuniorTrancheIdleValue()
        );
    }

    function testDepositJuniorTrancheExactlyAtMaxCap() public {
        uint256 juniorUser1DepositAmount = 2_50_00_000 * USDT;
        uint256 juniorUser2DepositAmount = 2_50_00_000 * USDT;
        vm.startPrank(juniorUser1);
        ERC20Mock(usdt).approve(address(tranchePool), juniorUser1DepositAmount);
        tranchePool.depositJuniorTranche(juniorUser1DepositAmount);
        vm.stopPrank();
        vm.startPrank(juniorUser2);
        ERC20Mock(usdt).approve(address(tranchePool), juniorUser2DepositAmount);
        tranchePool.depositJuniorTranche(juniorUser2DepositAmount);
        vm.stopPrank();
        assertEq(
            tranchePool.getJuniorTrancheIdleValue(),
            tranchePool.getJuniorTrancheMaxDepositCap()
        );
    }

    function testDepositJuniorTrancheMulitpleTImesBySameUser() public {
        uint256 juniorUser1FirstDeposit = 1_50_00_000 * USDT;
        uint256 juniorUser1SecondDeposit = 1_00_00_000 * USDT;
        vm.startPrank(juniorUser1);
        ERC20Mock(usdt).approve(
            address(tranchePool),
            juniorUser1FirstDeposit + juniorUser1SecondDeposit
        );
        tranchePool.depositJuniorTranche(juniorUser1FirstDeposit);
        tranchePool.depositJuniorTranche(juniorUser1SecondDeposit);
        vm.stopPrank();
        assertEq(
            tranchePool.getJuniorTrancheBalance(juniorUser1),
            juniorUser1FirstDeposit + juniorUser1SecondDeposit
        );

        assertEq(
            tranchePool.getJuniorTrancheShares(juniorUser1),
            juniorUser1FirstDeposit + juniorUser1SecondDeposit
        );
    }

    function testDepositJuniorTrancheAccountingIsCorrectWhenDepositAndWithdrawAtSameTime()
        public
    {
        uint256 juniorUser1Deposit = 2_00_00_000 * USDT;
        uint256 juniorUser1Withdraw = 80_00_000 * USDT;
        vm.startPrank(juniorUser1);
        ERC20Mock(usdt).approve(address(tranchePool), juniorUser1Deposit);
        tranchePool.depositJuniorTranche(juniorUser1Deposit);
        tranchePool.withdrawJuniorTranche(juniorUser1Withdraw);
        vm.stopPrank();
        assertEq(
            tranchePool.getJuniorTrancheBalance(juniorUser1),
            juniorUser1Deposit - juniorUser1Withdraw
        );

        assertEq(
            tranchePool.getJuniorTrancheShares(juniorUser1),
            juniorUser1Deposit - juniorUser1Withdraw
        );

        vm.startPrank(juniorUser1);
        ERC20Mock(usdt).approve(address(tranchePool), juniorUser1Withdraw);
        tranchePool.depositJuniorTranche(juniorUser1Withdraw);

        vm.stopPrank();

        assertEq(
            tranchePool.getJuniorTrancheBalance(juniorUser1),
            juniorUser1Deposit
        );

        assertEq(
            tranchePool.getJuniorTrancheShares(juniorUser1),
            juniorUser1Deposit
        );
    }

    // equity tranche deposit tests
    function testDepositEquityTrancheRevertIfNotOpen() public {
        vm.prank(deployer);
        tranchePool.setPoolState(ITranchePool.PoolState.COMMITED);
        vm.startPrank(equityUser1);
        ERC20Mock(usdt).approve(address(tranchePool), 10_00_000 * USDT);
        vm.expectRevert(ITranchePool.TranchePool__PoolIsNotOpen.selector);
        tranchePool.depositEquityTranche(10_00_000 * USDT);
        vm.stopPrank();
    }

    function testDepositEquityTrancheRevertIfLessThanMinimumDeposit() public {
        vm.startPrank(equityUser1);
        ERC20Mock(usdt).approve(address(tranchePool), 1_00_000 * USDT);
        vm.expectRevert(
            abi.encodeWithSignature(
                "TranchePool__LessThanDepositThreshold(uint256)",
                1_00_000 * USDT
            )
        );
        tranchePool.depositEquityTranche(1_00_000 * USDT);
        vm.stopPrank();
    }

    function testDepositRevertIfUserIsNotWhiteListedEquityTranche() public {
        vm.startPrank(falseUser);
        uint256 falseUser1DepositAmount = 5_00_00_000 * USDT;
        ERC20Mock(usdt).approve(address(tranchePool), falseUser1DepositAmount);
        vm.expectRevert(
            abi.encodeWithSignature(
                "TranchePool__NotWhiteListedForEquityTranche(address)",
                falseUser
            )
        );
        tranchePool.depositEquityTranche(falseUser1DepositAmount);
        vm.stopPrank();
    }

    function testDepositEquityTrancheRevertsIfMaxPoolCapExceeded() public {
        uint256 equityUser1DepositAmount = 2_00_00_000 * USDT;
        uint256 equityUser2DepositAmount = 5_00_00_000 * USDT;
        vm.startPrank(equityUser1);
        ERC20Mock(usdt).approve(address(tranchePool), equityUser1DepositAmount);
        tranchePool.depositEquityTranche(equityUser1DepositAmount);
        vm.stopPrank();

        vm.startPrank(equityUser2);
        ERC20Mock(usdt).approve(address(tranchePool), equityUser2DepositAmount);
        vm.expectRevert(
            abi.encodeWithSignature(
                "TranchePool__MaxDepositCapExceeded(uint256,uint256)",
                tranchePool.getEquityTrancheMaxDepositCap(),
                equityUser2DepositAmount
            )
        );
        tranchePool.depositEquityTranche(equityUser2DepositAmount);
        vm.stopPrank();
    }

    function testFullDepositEquityTranche() public {
        uint256 equityTrancheDeposit1 = 5_0_00_000 * USDT;
        uint256 equityTrancheDeposit2 = 5_0_00_000 * USDT;
        assertEq(tranchePool.getEquityUserIndex(equityUser1), 0);
        assertEq(tranchePool.getEquityUserIndex(equityUser2), 0);
        assertEq(tranchePool.getTotalEquityShares(), 0);
        assertEq(tranchePool.getEquityTrancheIdleValue(), 0);
        vm.startPrank(equityUser1);
        ERC20Mock(usdt).approve(address(tranchePool), equityTrancheDeposit1);
        vm.expectEmit(true, false, false, true);
        emit ITranchePool.FundsDepositedToEquityTranche(
            equityUser1,
            equityTrancheDeposit1,
            equityTrancheDeposit1,
            block.timestamp
        );
        tranchePool.depositEquityTranche(equityTrancheDeposit1);
        vm.stopPrank();
        assertEq(tranchePool.getTotalEquityShares(), equityTrancheDeposit1);
        assertEq(
            tranchePool.getEquityTrancheIdleValue(),
            equityTrancheDeposit1
        );

        vm.startPrank(equityUser2);
        ERC20Mock(usdt).approve(address(tranchePool), equityTrancheDeposit2);
        vm.expectEmit(true, false, false, true);
        emit ITranchePool.FundsDepositedToEquityTranche(
            equityUser2,
            equityTrancheDeposit2,
            equityTrancheDeposit2,
            block.timestamp
        );
        tranchePool.depositEquityTranche(equityTrancheDeposit2);
        vm.stopPrank();
        assertEq(
            tranchePool.getEquityTrancheIdleValue(),
            equityTrancheDeposit1 + equityTrancheDeposit2
        );

        assertEq(
            tranchePool.getTotalEquityShares(),
            equityTrancheDeposit1 + equityTrancheDeposit2
        );

        assertEq(
            tranchePool.getEquityTrancheIdleValue(),
            equityTrancheDeposit1 + equityTrancheDeposit2
        );
        assertEq(tranchePool.getEquityTrancheDeployedValue(), 0);

        assertEq(
            tranchePool.getTotalEquityShares(),
            equityTrancheDeposit1 + equityTrancheDeposit2
        );

        assertEq(
            equityTrancheDeposit1,
            tranchePool.getEquityTrancheBalance(equityUser1)
        );

        assertEq(tranchePool.getEquityUserIndex(equityUser1), 1e18);

        assertEq(
            equityTrancheDeposit1,
            tranchePool.getEquityTrancheShares(equityUser1)
        );

        assertEq(
            equityTrancheDeposit2,
            tranchePool.getEquityTrancheBalance(equityUser2)
        );
        assertEq(tranchePool.getEquityUserIndex(equityUser2), 1e18);

        assertEq(
            equityTrancheDeposit2,
            tranchePool.getEquityTrancheShares(equityUser2)
        );

        assertEq(
            tranchePool.getTotalEquityShares(),
            tranchePool.getEquityTrancheIdleValue()
        );
    }

    function testDepositEquityTrancheExactlyAtMaxCap() public {
        uint256 equityUser1DepositAmount = 1_50_00_000 * USDT;
        uint256 equityUser2DepositAmount = 1_50_00_000 * USDT;
        vm.startPrank(equityUser1);
        ERC20Mock(usdt).approve(address(tranchePool), equityUser1DepositAmount);
        tranchePool.depositEquityTranche(equityUser1DepositAmount);
        vm.stopPrank();
        vm.startPrank(equityUser2);
        ERC20Mock(usdt).approve(address(tranchePool), equityUser2DepositAmount);
        tranchePool.depositEquityTranche(equityUser2DepositAmount);
        vm.stopPrank();
        assertEq(
            tranchePool.getEquityTrancheIdleValue(),
            tranchePool.getEquityTrancheMaxDepositCap()
        );
    }

    function testDepositEquityTrancheMulitpleTImesBySameUser() public {
        uint256 equityUser1FirstDeposit = 1_00_00_000 * USDT;
        uint256 equityUser1SecondDeposit = 50_00_000 * USDT;
        vm.startPrank(equityUser1);
        ERC20Mock(usdt).approve(
            address(tranchePool),
            equityUser1FirstDeposit + equityUser1SecondDeposit
        );
        tranchePool.depositEquityTranche(equityUser1FirstDeposit);
        tranchePool.depositEquityTranche(equityUser1SecondDeposit);
        vm.stopPrank();
        assertEq(
            tranchePool.getEquityTrancheBalance(equityUser1),
            equityUser1FirstDeposit + equityUser1SecondDeposit
        );

        assertEq(
            tranchePool.getEquityTrancheShares(equityUser1),
            equityUser1FirstDeposit + equityUser1SecondDeposit
        );
    }

    function testDepositEquityTrancheAccountingIsCorrectWhenDepositAndWithdrawAtSameTime()
        public
    {
        uint256 equityUser1Deposit = 2_00_00_000 * USDT;
        uint256 equityUser1Withdraw = 70_00_000 * USDT;
        vm.startPrank(equityUser1);
        ERC20Mock(usdt).approve(address(tranchePool), equityUser1Deposit);
        tranchePool.depositEquityTranche(equityUser1Deposit);
        tranchePool.withdrawEquityTranche(equityUser1Withdraw);
        vm.stopPrank();
        assertEq(
            tranchePool.getEquityTrancheBalance(equityUser1),
            equityUser1Deposit - equityUser1Withdraw
        );

        assertEq(
            tranchePool.getEquityTrancheShares(equityUser1),
            equityUser1Deposit - equityUser1Withdraw
        );

        vm.startPrank(equityUser1);
        ERC20Mock(usdt).approve(address(tranchePool), equityUser1Withdraw);
        tranchePool.depositEquityTranche(equityUser1Withdraw);

        vm.stopPrank();

        assertEq(
            tranchePool.getEquityTrancheBalance(equityUser1),
            equityUser1Deposit
        );

        assertEq(
            tranchePool.getEquityTrancheShares(equityUser1),
            equityUser1Deposit
        );
    }
}
