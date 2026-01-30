// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Test, console} from "forge-std/Test.sol";
import {TranchePool} from "../src/TranchePool.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {VmSafe} from "forge-std/Vm.sol";
import {LoanEngine} from "../src/LoanEngine.sol";

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

    address borrower = makeAddr("borrower");
    address feeManager = makeAddr("feeManager");

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
        usdt.mint(seniorUser1, 100_00_00_000 * USDT);
        usdt.mint(seniorUser2, 100_00_00_000 * USDT);
        usdt.mint(seniorUser3, 100_00_00_000 * USDT);
        usdt.mint(juniorUser1, 20_50_00_000 * USDT);
        usdt.mint(juniorUser2, 20_50_00_000 * USDT);
        usdt.mint(juniorUser3, 20_00_00_000 * USDT);
        usdt.mint(equityUser1, 50_00_00_000 * USDT);
        usdt.mint(equityUser2, 50_00_00_000 * USDT);
        usdt.mint(falseUser, 50_00_00_000 * USDT);
    }

    function _min(uint256 a, uint256 b) internal pure returns (uint256) {
        return a < b ? a : b;
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
        tranchePool.onRepayment(principalRepaid, 0, 80, 15);

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
        tranchePool.onRepayment(0, interestRepaid, 80, 15);

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
        tranchePool.onRepayment(principalRepaid, interestRepaid, 80, 15);

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
        tranchePool.onRepayment(0, 0, 80, 15);
    }

    function test_OnRepayment_RevertIf_PrincipalExceedsDeployed() public {
        _depositToAllTranches();
        _allocateCapital();

        uint256 excessivePrincipal = 100_00_00_000 * USDT;

        vm.prank(loanEngine);
        vm.expectRevert(
            TranchePool.TranchePool__PrincipalRepaymentExceeded.selector
        );
        tranchePool.onRepayment(excessivePrincipal, 0, 80, 15);
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
        tranchePool.onRecovery(recoveryAmount, 80, 15);

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

    // extra pending tests
}
