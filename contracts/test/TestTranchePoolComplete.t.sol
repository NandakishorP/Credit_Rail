// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Test} from "forge-std/Test.sol";
import {TranchePool} from "../src/TranchePool.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";

contract TestTranchePoolComplete is Test {
    TranchePool tranchePool;
    ERC20Mock usdt;

    address deployer = makeAddr("deployer");
    address loanEngine = makeAddr("loanEngine");

    address seniorUser1 = makeAddr("seniorUser1");
    address seniorUser2 = makeAddr("seniorUser2");
    address seniorUser3 = makeAddr("seniorUser3");

    address juniorUser1 = makeAddr("juniorUser1");
    address juniorUser2 = makeAddr("juniorUser2");
    address juniorUser3 = makeAddr("juniorUser3");

    address equityUser1 = makeAddr("equityUser1");
    address equityUser2 = makeAddr("equityUser2");

    address falseUser = makeAddr("falseUser");

    uint256 public USDT = 1e18;

    function setUp() public {
        usdt = new ERC20Mock();
        vm.startPrank(deployer);
        tranchePool = new TranchePool(address(usdt));

        // Set minimum deposits
        tranchePool.setMinimumDepositAmountSeniorTranche(5_00_000 * USDT);
        tranchePool.setMinimumDepositAmountJuniorTranche(10_00_000 * USDT);
        tranchePool.setMinimumDepositAmountEquityTranche(50_00_000 * USDT);

        // Set max caps
        tranchePool.setMaxAllocationCapSeniorTranche(13_00_00_000 * USDT);
        tranchePool.setMaxAllocationCapJuniorTranche(5_00_00_000 * USDT);
        tranchePool.setMaxAllocationCapEquityTranche(3_00_00_000 * USDT);

        // Set allocation factors
        tranchePool.setTrancheCapitalAllocationFactorSenior(80);
        tranchePool.setTrancheCapitalAllocationFactorJunior(15);

        // Whitelist users
        tranchePool.updateWhitelist(seniorUser1, true);
        tranchePool.updateWhitelist(seniorUser2, true);
        tranchePool.updateWhitelist(seniorUser3, true);
        tranchePool.updateWhitelist(juniorUser1, true);
        tranchePool.updateWhitelist(juniorUser2, true);
        tranchePool.updateWhitelist(juniorUser3, true);
        tranchePool.updateEqutyTrancheWhiteList(equityUser1, true);
        tranchePool.updateEqutyTrancheWhiteList(equityUser2, true);

        // Set loan engine
        tranchePool.setLoanEngine(loanEngine);

        vm.stopPrank();

        // Mint tokens
        usdt.mint(seniorUser1, 10_00_00_000 * USDT);
        usdt.mint(seniorUser2, 10_00_00_000 * USDT);
        usdt.mint(seniorUser3, 10_00_00_000 * USDT);
        usdt.mint(juniorUser1, 2_50_00_000 * USDT);
        usdt.mint(juniorUser2, 2_50_00_000 * USDT);
        usdt.mint(juniorUser3, 2_00_00_000 * USDT);
        usdt.mint(equityUser1, 5_00_00_000 * USDT);
        usdt.mint(equityUser2, 5_00_00_000 * USDT);
        usdt.mint(falseUser, 5_00_00_000 * USDT);
    }

    function testDepositSeniorTrancheRevertsIfPoolIsNotOpen() public {
        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);
        vm.startPrank(seniorUser1);
        ERC20Mock(usdt).approve(address(tranchePool), 10_00_000 * USDT);
        vm.expectRevert(TranchePool.TranchePool__PoolIsNotOpen.selector);
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
        emit TranchePool.FundsDepositedToSeniorTranche(
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
        emit TranchePool.FundsDepositedToSeniorTranche(
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
        emit TranchePool.FundsDepositedToSeniorTranche(
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
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);
        vm.startPrank(juniorUser1);
        ERC20Mock(usdt).approve(address(tranchePool), 10_00_000 * USDT);
        vm.expectRevert(TranchePool.TranchePool__PoolIsNotOpen.selector);
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
        emit TranchePool.FundsDepositedToJuniorTranche(
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
        emit TranchePool.FundsDepositedToJuniorTranche(
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
        emit TranchePool.FundsDepositedToJuniorTranche(
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
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);
        vm.startPrank(equityUser1);
        ERC20Mock(usdt).approve(address(tranchePool), 10_00_000 * USDT);
        vm.expectRevert(TranchePool.TranchePool__PoolIsNotOpen.selector);
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
        emit TranchePool.FundsDepositedToEquityTranche(
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
        emit TranchePool.FundsDepositedToEquityTranche(
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

    /*//////////////////////////////////////////////////////////////
                        WITHDRAWAL TESTS - SENIOR
    //////////////////////////////////////////////////////////////*/

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

    /*//////////////////////////////////////////////////////////////
                        CAPITAL ALLOCATION TESTS
    //////////////////////////////////////////////////////////////*/

    function test_AllocateCapital_Success() public {
        // Deposit to tranches
        _depositToAllTranches();

        // Move to COMMITED state
        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        uint256 totalDisbursement = 1_00_00_000 * USDT;
        uint256 fees = 10_000 * USDT;
        address borrower = makeAddr("borrower");
        address feeManager = makeAddr("feeManager");

        vm.prank(loanEngine);
        tranchePool.allocateCapital(
            totalDisbursement,
            fees,
            borrower,
            feeManager
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
        assertEq(usdt.balanceOf(borrower), totalDisbursement);
        assertEq(usdt.balanceOf(feeManager), fees);

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
        address borrower = makeAddr("borrower");
        address feeManager = makeAddr("feeManager");

        vm.prank(loanEngine);
        tranchePool.allocateCapital(totalDisbursement, 0, borrower, feeManager);

        assertEq(usdt.balanceOf(borrower), totalDisbursement);
        assertEq(usdt.balanceOf(feeManager), 0);
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

    function test_AllocateCapital_RevertIf_NotDeployed() public {
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

    /*//////////////////////////////////////////////////////////////
                        REPAYMENT TESTS
    //////////////////////////////////////////////////////////////*/

    function test_OnRepayment_PrincipalOnly_Success() public {
        _depositToAllTranches();
        _allocateCapital();

        uint256 principalRepaid = 50_00_000 * USDT;

        uint256 seniorDeployedBefore = tranchePool
            .getSeniorTrancheDeployedValue();
        uint256 juniorDeployedBefore = tranchePool
            .getJuniorTrancheDeployedValue();
        uint256 equityDeployedBefore = tranchePool
            .getEquityTrancheDeployedValue();

        vm.prank(loanEngine);
        tranchePool.onRepayment(principalRepaid, 0);

        uint256 expectedSenior = (principalRepaid * 80) / 100;
        uint256 expectedJunior = (principalRepaid * 15) / 100;
        uint256 expectedEquity = principalRepaid -
            expectedSenior -
            expectedJunior;

        assertEq(
            tranchePool.getSeniorTrancheDeployedValue(),
            seniorDeployedBefore - expectedSenior
        );
        assertEq(
            tranchePool.getJuniorTrancheDeployedValue(),
            juniorDeployedBefore - expectedJunior
        );
        assertEq(
            tranchePool.getEquityTrancheDeployedValue(),
            equityDeployedBefore - expectedEquity
        );
    }

    function test_OnRepayment_InterestOnly_Success() public {
        _depositToAllTranches();
        _allocateCapital();

        uint256 interestRepaid = 10_00_000 * USDT;

        // No accrued interest initially, so all goes to equity
        vm.prank(loanEngine);
        tranchePool.onRepayment(0, interestRepaid);

        uint256 expectedEquityIndex = 1e18 +
            (interestRepaid * 1e18) /
            tranchePool.getTotalEquityShares();
        assertEq(tranchePool.equityInterestIndex(), expectedEquityIndex);
    }

    function test_OnRepayment_BothPrincipalAndInterest_Success() public {
        _depositToAllTranches();
        _allocateCapital();

        uint256 principalRepaid = 50_00_000 * USDT;
        uint256 interestRepaid = 5_00_000 * USDT;

        vm.prank(loanEngine);
        tranchePool.onRepayment(principalRepaid, interestRepaid);

        // Verify principal returned
        assertGt(tranchePool.getSeniorTrancheIdleValue(), 0);
    }

    function test_OnRepayment_RevertIf_ZeroAmount() public {
        vm.prank(loanEngine);
        vm.expectRevert(
            abi.encodeWithSelector(
                TranchePool.TranchePool__InvalidTransferAmount.selector,
                0
            )
        );
        tranchePool.onRepayment(0, 0);
    }

    function test_OnRepayment_RevertIf_PrincipalExceedsDeployed() public {
        _depositToAllTranches();
        _allocateCapital();

        uint256 excessivePrincipal = 100_00_00_000 * USDT;

        vm.prank(loanEngine);
        vm.expectRevert(
            TranchePool.TranchePool__PrincipalRepaymentExceeded.selector
        );
        tranchePool.onRepayment(excessivePrincipal, 0);
    }

    /*//////////////////////////////////////////////////////////////
                        LOSS ALLOCATION TESTS
    //////////////////////////////////////////////////////////////*/

    function test_OnLoss_EquityAbsorbsAll_Success() public {
        _depositToAllTranches();
        _allocateCapital();

        uint256 equityDeployedBefore = tranchePool
            .getEquityTrancheDeployedValue();
        uint256 loss = equityDeployedBefore / 2;

        vm.prank(loanEngine);
        tranchePool.onLoss(loss);

        assertEq(
            tranchePool.getEquityTrancheDeployedValue(),
            equityDeployedBefore - loss
        );
        // Junior and Senior unchanged
        assertGt(tranchePool.getJuniorTrancheDeployedValue(), 0);
        assertGt(tranchePool.getSeniorTrancheDeployedValue(), 0);
    }

    function test_OnLoss_JuniorAbsorbs_Success() public {
        _depositToAllTranches();
        _allocateCapital();

        uint256 equityDeployed = tranchePool.getEquityTrancheDeployedValue();
        uint256 juniorDeployedBefore = tranchePool
            .getJuniorTrancheDeployedValue();

        // Loss exceeds equity
        uint256 loss = equityDeployed + (juniorDeployedBefore / 2);

        vm.prank(loanEngine);
        tranchePool.onLoss(loss);

        assertEq(tranchePool.getEquityTrancheDeployedValue(), 0);
        assertEq(
            tranchePool.getJuniorTrancheDeployedValue(),
            juniorDeployedBefore - (loss - equityDeployed)
        );
        // Senior unchanged
        assertGt(tranchePool.getSeniorTrancheDeployedValue(), 0);
    }

    function test_OnLoss_SeniorAbsorbs_Success() public {
        _depositToAllTranches();
        _allocateCapital();

        uint256 equityDeployed = tranchePool.getEquityTrancheDeployedValue();
        uint256 juniorDeployed = tranchePool.getJuniorTrancheDeployedValue();
        uint256 seniorDeployedBefore = tranchePool
            .getSeniorTrancheDeployedValue();

        // Loss exceeds equity + junior
        uint256 loss = equityDeployed +
            juniorDeployed +
            (seniorDeployedBefore / 2);

        vm.prank(loanEngine);
        tranchePool.onLoss(loss);

        assertEq(tranchePool.getEquityTrancheDeployedValue(), 0);
        assertEq(tranchePool.getJuniorTrancheDeployedValue(), 0);
        assertEq(
            tranchePool.getSeniorTrancheDeployedValue(),
            seniorDeployedBefore - (loss - equityDeployed - juniorDeployed)
        );
    }

    function test_OnLoss_RevertIf_ExceedsCapital() public {
        _depositToAllTranches();
        _allocateCapital();

        uint256 totalDeployed = tranchePool.getSeniorTrancheDeployedValue() +
            tranchePool.getJuniorTrancheDeployedValue() +
            tranchePool.getEquityTrancheDeployedValue();

        uint256 excessiveLoss = totalDeployed + 1;

        vm.prank(loanEngine);
        vm.expectRevert(
            abi.encodeWithSelector(
                TranchePool.TranchePool__LossExceededCapital.selector,
                1
            )
        );
        tranchePool.onLoss(excessiveLoss);
    }

    /*//////////////////////////////////////////////////////////////
                        RECOVERY TESTS
    //////////////////////////////////////////////////////////////*/

    function test_OnRecovery_Success() public {
        _depositToAllTranches();

        uint256 recoveryAmount = 10_00_000 * USDT;

        uint256 seniorIdleBefore = tranchePool.getSeniorTrancheIdleValue();
        uint256 juniorIdleBefore = tranchePool.getJuniorTrancheIdleValue();
        uint256 equityIdleBefore = tranchePool.getEquityTrancheIdleValue();

        vm.prank(loanEngine);
        tranchePool.onRecovery(recoveryAmount);

        uint256 expectedSenior = (recoveryAmount * 80) / 100;
        uint256 expectedJunior = (recoveryAmount * 15) / 100;
        uint256 expectedEquity = recoveryAmount -
            expectedSenior -
            expectedJunior;

        assertEq(
            tranchePool.getSeniorTrancheIdleValue(),
            seniorIdleBefore + expectedSenior
        );
        assertEq(
            tranchePool.getJuniorTrancheIdleValue(),
            juniorIdleBefore + expectedJunior
        );
        assertEq(
            tranchePool.getEquityTrancheIdleValue(),
            equityIdleBefore + expectedEquity
        );
    }

    /*//////////////////////////////////////////////////////////////
                        INTEREST CLAIM TESTS
    //////////////////////////////////////////////////////////////*/

    function test_ClaimSeniorInterest_RevertIf_NoShares() public {
        vm.prank(seniorUser1);
        vm.expectRevert(TranchePool.TranchePool__InsufficientShares.selector);
        tranchePool.claimSeniorInterest();
    }

    function test_ClaimSeniorInterest_RevertIf_ZeroClaim() public {
        uint256 depositAmount = 5_00_00_000 * USDT;
        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), depositAmount);
        tranchePool.depositSeniorTranche(depositAmount);

        // Try to claim with no index change
        vm.expectRevert(TranchePool.TranchePool__ZeroWithdrawal.selector);
        tranchePool.claimSeniorInterest();
        vm.stopPrank();
    }

    function test_ClaimJuniorInterest_RevertIf_NoShares() public {
        vm.prank(juniorUser1);
        vm.expectRevert(TranchePool.TranchePool__InsufficientShares.selector);
        tranchePool.claimJuniorInterest();
    }

    function test_ClaimEquityInterest_RevertIf_NoShares() public {
        vm.prank(equityUser1);
        vm.expectRevert(TranchePool.TranchePool__InsufficientShares.selector);
        tranchePool.claimEquityInterest();
    }

    /*//////////////////////////////////////////////////////////////
                        POOL STATE TESTS
    //////////////////////////////////////////////////////////////*/

    function test_SetPoolState_ToCommited_Success() public {
        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        assertEq(
            uint256(tranchePool.getPoolState()),
            uint256(TranchePool.PoolState.COMMITED)
        );
    }

    function test_SetPoolState_ToDeployed_Success() public {
        vm.startPrank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);
        tranchePool.setPoolState(TranchePool.PoolState.DEPLOYED);
        vm.stopPrank();

        assertEq(
            uint256(tranchePool.getPoolState()),
            uint256(TranchePool.PoolState.DEPLOYED)
        );
    }

    function test_SetPoolState_ToClosed_Success() public {
        _depositToAllTranches();
        _allocateCapital();

        uint256 seniorDeployed = tranchePool.getSeniorTrancheDeployedValue();
        uint256 juniorDeployed = tranchePool.getJuniorTrancheDeployedValue();
        uint256 equityDeployed = tranchePool.getEquityTrancheDeployedValue();

        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.CLOSED);

        // Deployed values should be moved to idle
        assertEq(tranchePool.getSeniorTrancheDeployedValue(), 0);
        assertEq(tranchePool.getJuniorTrancheDeployedValue(), 0);
        assertEq(tranchePool.getEquityTrancheDeployedValue(), 0);

        assertGt(tranchePool.getSeniorTrancheIdleValue(), seniorDeployed);
        assertGt(tranchePool.getJuniorTrancheIdleValue(), juniorDeployed);
        assertGt(tranchePool.getEquityTrancheIdleValue(), equityDeployed);
    }

    function test_SetPoolState_RevertIf_Backwards() public {
        vm.startPrank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        vm.expectRevert(
            abi.encodeWithSelector(
                TranchePool.TranchePool__InvalidStateTransition.selector,
                TranchePool.PoolState.OPEN
            )
        );
        tranchePool.setPoolState(TranchePool.PoolState.OPEN);
        vm.stopPrank();
    }

    /*//////////////////////////////////////////////////////////////
                        ADMIN SETTER TESTS
    //////////////////////////////////////////////////////////////*/

    function test_SetAllocationFactor_Senior_Success() public {
        vm.prank(deployer);
        tranchePool.setTrancheCapitalAllocationFactorSenior(70);

        assertEq(tranchePool.s_capital_allocation_factor_senior(), 70);
    }

    function test_SetAllocationFactor_Junior_Success() public {
        vm.prank(deployer);
        tranchePool.setTrancheCapitalAllocationFactorJunior(20);

        assertEq(tranchePool.s_capital_allocation_factor_junior(), 20);
    }

    function test_SetAllocationFactor_RevertIf_ExceedsMax() public {
        vm.prank(deployer);
        vm.expectRevert(
            TranchePool.TranchePool__InvalidAllocationRatio.selector
        );
        tranchePool.setTrancheCapitalAllocationFactorSenior(90);
    }

    function test_SetSeniorAPR_Success() public {
        vm.prank(deployer);
        tranchePool.setSeniorAPR(500);

        assertEq(tranchePool.s_senior_apr(), 500);
    }

    function test_SetSeniorAPR_RevertIf_Zero() public {
        vm.prank(deployer);
        vm.expectRevert(TranchePool.TranchePool__ZeroAPRError.selector);
        tranchePool.setSeniorAPR(0);
    }

    function test_SetTargetJuniorAPR_Success() public {
        vm.prank(deployer);
        tranchePool.setTargetJuniorAPR(1000);

        assertEq(tranchePool.s_target_junior_apr(), 1000);
    }

    function test_SetTargetJuniorAPR_RevertIf_Zero() public {
        vm.prank(deployer);
        vm.expectRevert(TranchePool.TranchePool__ZeroAPRError.selector);
        tranchePool.setTargetJuniorAPR(0);
    }

    function test_SetMaxCap_RevertIf_Zero() public {
        vm.prank(deployer);
        vm.expectRevert(TranchePool.TranchePool__ZeroValueError.selector);
        tranchePool.setMaxAllocationCapSeniorTranche(0);
    }

    function test_SetLoanEngine_Success() public {
        address newLoanEngine = makeAddr("newLoanEngine");

        vm.prank(deployer);
        tranchePool.setLoanEngine(newLoanEngine);

        assertEq(tranchePool.loanEngine(), newLoanEngine);
    }

    function test_UpdateWhitelist_Success() public {
        address newUser = makeAddr("newUser");

        vm.prank(deployer);
        tranchePool.updateWhitelist(newUser, true);

        assertTrue(tranchePool.whiteListedLps(newUser));
    }

    function test_UpdateEquityTrancheWhitelist_Success() public {
        address newUser = makeAddr("newUser");

        vm.prank(deployer);
        tranchePool.updateEqutyTrancheWhiteList(newUser, true);

        assertTrue(tranchePool.whiteListedForEquityTranche(newUser));
    }

    /*//////////////////////////////////////////////////////////////
                        GETTER TESTS
    //////////////////////////////////////////////////////////////*/

    function test_GetSeniorTrancheBalance_Success() public {
        uint256 depositAmount = 5_00_00_000 * USDT;
        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), depositAmount);
        tranchePool.depositSeniorTranche(depositAmount);
        vm.stopPrank();

        assertEq(
            tranchePool.getSeniorTrancheBalance(seniorUser1),
            depositAmount
        );
    }

    function test_GetJuniorTrancheBalance_Success() public {
        uint256 depositAmount = 2_00_00_000 * USDT;
        vm.startPrank(juniorUser1);
        usdt.approve(address(tranchePool), depositAmount);
        tranchePool.depositJuniorTranche(depositAmount);
        vm.stopPrank();

        assertEq(
            tranchePool.getJuniorTrancheBalance(juniorUser1),
            depositAmount
        );
    }

    function test_GetEquityTrancheBalance_Success() public {
        uint256 depositAmount = 1_00_00_000 * USDT;
        vm.startPrank(equityUser1);
        usdt.approve(address(tranchePool), depositAmount);
        tranchePool.depositEquityTranche(depositAmount);
        vm.stopPrank();

        assertEq(
            tranchePool.getEquityTrancheBalance(equityUser1),
            depositAmount
        );
    }

    function test_GetBalances_ReturnsZero_WhenNoShares() public view {
        assertEq(tranchePool.getSeniorTrancheBalance(seniorUser1), 0);
        assertEq(tranchePool.getJuniorTrancheBalance(juniorUser1), 0);
        assertEq(tranchePool.getEquityTrancheBalance(equityUser1), 0);
    }

    /*//////////////////////////////////////////////////////////////
                        HELPER FUNCTIONS
    //////////////////////////////////////////////////////////////*/

    function _depositToAllTranches() internal {
        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), 5_00_00_000 * USDT);
        tranchePool.depositSeniorTranche(5_00_00_000 * USDT);
        vm.stopPrank();

        vm.startPrank(juniorUser1);
        usdt.approve(address(tranchePool), 2_00_00_000 * USDT);
        tranchePool.depositJuniorTranche(2_00_00_000 * USDT);
        vm.stopPrank();

        vm.startPrank(equityUser1);
        usdt.approve(address(tranchePool), 1_00_00_000 * USDT);
        tranchePool.depositEquityTranche(1_00_00_000 * USDT);
        vm.stopPrank();
    }

    function _allocateCapital() internal {
        vm.prank(deployer);
        tranchePool.setPoolState(TranchePool.PoolState.COMMITED);

        uint256 totalDisbursement = 1_00_00_000 * USDT;
        uint256 fees = 10_000 * USDT;

        vm.prank(loanEngine);
        tranchePool.allocateCapital(
            totalDisbursement,
            fees,
            makeAddr("borrower"),
            makeAddr("feeManager")
        );
    }
}
