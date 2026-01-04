// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Test} from "forge-std/Test.sol";
import {TranchePool} from "../src/TranchePool.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";

contract TestTranchePool is Test {
    TranchePool tranchePool;
    // scaled to 1e18 as standard point => 1$ = 1e18
    ERC20Mock usdt;
    address deployer = makeAddr("deployer");
    address alice = makeAddr("alice");

    function setUp() public {
        usdt = new ERC20Mock();
        vm.prank(deployer);
        tranchePool = new TranchePool(address(usdt));

        ERC20Mock(usdt).mint(alice, 10_00_000 * 1e18);
    }

    function testDepositSeniorTranche() public {
        vm.startPrank(deployer);
        // the minimum deposit is stated to 1m$
        tranchePool.setMinimumDepositAmountSeniorTranche(10_00_000);
        tranchePool.updateWhitelist(alice, true);
        vm.stopPrank();
        vm.startPrank(alice);
        ERC20Mock(usdt).approve(address(tranchePool), 10_00_000);
        tranchePool.depositSeniorTranche(10_00_000);

        vm.stopPrank();

        assertEq(10_00_000, tranchePool.getSeniorTrancheBalance(alice));
    }

    function testDepositJuniorTranche() public {
        vm.startPrank(deployer);
        // the minimum deposit is stated to 500k$
        tranchePool.setMinimumDepositAmountJuniorTranche(5_00_000);
        tranchePool.updateWhitelist(alice, true);
        vm.stopPrank();
        vm.startPrank(alice);
        ERC20Mock(usdt).approve(address(tranchePool), 10_00_000);
        tranchePool.depositJuniorTranche(10_00_000);

        vm.stopPrank();

        assertEq(10_00_000, tranchePool.getJuniorTrancheBalance(alice));
    }

    function testDepositEquityTranche() public {
        vm.startPrank(deployer);
        // the minimum deposit is stated to 100k$
        tranchePool.setMinimumDepositAmountSeniorTranche(1_00_000);
        tranchePool.updateEqutyTrancheWhiteList(alice, true);
        vm.stopPrank();
        vm.startPrank(alice);
        ERC20Mock(usdt).approve(address(tranchePool), 1_00_000);
        tranchePool.depositEquityTranche(1_00_000);

        vm.stopPrank();

        assertEq(1_00_000, tranchePool.getEquityTrancheBalance(alice));
    }
}
