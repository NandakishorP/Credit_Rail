// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Test} from "forge-std/Test.sol";
import {TranchePool} from "../../src/TranchePool.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";

contract TestTranchePool is Test {
    TranchePool tranchePool;
    // scaled to 1e18 as standard point => 1$ = 1e18
    ERC20Mock usdt;
    address deployer = makeAddr("deployer");
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

    // the pool is taking a funding for 200M $ so senior raises 130M$, junior raises 50M$
    // and equity 30M$
    // the minimum deposit for senior is 500k$, junior is 1m$ and equity is 5M$
    function setUp() public {
        usdt = new ERC20Mock();
        vm.startPrank(deployer);
        tranchePool = new TranchePool(address(usdt));
        // set max to 130m usdt
        tranchePool.setMaxAllocationCapSeniorTranche(13_00_00_000 * USDT);
        // set to 500k usdt == 1,00,000
        tranchePool.setMinimumDepositAmountSeniorTranche(5_00_000 * USDT);

        tranchePool.setMaxAllocationCapJuniorTranche(5_00_00_000 * USDT);
        tranchePool.setMinimumDepositAmountJuniorTranche(10_00_000 * USDT);
        tranchePool.setMaxAllocationCapEquityTranche(3_00_00_000 * USDT);

        tranchePool.setMinimumDepositAmountEquityTranche(50_00_000 * USDT);
        tranchePool.updateWhitelist(seniorUser1, true);
        tranchePool.updateWhitelist(seniorUser2, true);
        tranchePool.updateWhitelist(seniorUser3, true);
        tranchePool.updateWhitelist(juniorUser1, true);
        tranchePool.updateWhitelist(juniorUser2, true);
        tranchePool.updateWhitelist(juniorUser3, true);
        tranchePool.updateEquityTrancheWhiteList(equityUser1, true);
        tranchePool.updateEquityTrancheWhiteList(equityUser2, true);

        vm.stopPrank();

        ERC20Mock(usdt).mint(seniorUser1, 10_00_00_000 * 1e18);
        ERC20Mock(usdt).mint(seniorUser2, 10_00_00_000 * 1e18);
        ERC20Mock(usdt).mint(seniorUser3, 10_00_00_000 * 1e18);

        ERC20Mock(usdt).mint(juniorUser1, 2_00_00_000 * 1e18);
        ERC20Mock(usdt).mint(juniorUser2, 2_00_00_000 * 1e18);
        ERC20Mock(usdt).mint(juniorUser3, 2_00_00_000 * 1e18);

        ERC20Mock(usdt).mint(equityUser1, 5_00_00_000 * 1e18);
        ERC20Mock(usdt).mint(equityUser2, 5_00_00_000 * 1e18);

        ERC20Mock(usdt).mint(falseUser, 5_00_00_000 * 1e18);
    }

    function testDepositSeniorTrancheRevertIfNotOpen() public {
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

    function testDepostiEquuityTracheRevertsIfMaxPoolCapExceeeded() public {
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
}
