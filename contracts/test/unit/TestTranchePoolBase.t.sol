// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Test, console} from "forge-std/Test.sol";
import {TranchePool} from "../../src/TranchePool.sol";
import {ITranchePool} from "../../src/interfaces/ITranchePool.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {VmSafe} from "forge-std/Vm.sol";
import {LoanEngine} from "../../src/LoanEngine.sol";

contract TestTranchePoolBase is Test {
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

    function setUp() public virtual {
        usdt = new ERC20Mock();
        vm.startPrank(deployer);
        tranchePool = new TranchePool(address(usdt));

        // Set max caps
        tranchePool.setMaxAllocationCapSeniorTranche(13_00_00_000 * USDT);
        tranchePool.setMaxAllocationCapJuniorTranche(5_00_00_000 * USDT);
        tranchePool.setMaxAllocationCapEquityTranche(3_00_00_000 * USDT);

        // Set minimum deposits
        tranchePool.setMinimumDepositAmountSeniorTranche(5_00_000 * USDT);
        tranchePool.setMinimumDepositAmountJuniorTranche(10_00_000 * USDT);
        tranchePool.setMinimumDepositAmountEquityTranche(50_00_000 * USDT);

        // Set allocation factors
        tranchePool.setTrancheCapitalAllocationFactorSenior(80);
        tranchePool.setTrancheCapitalAllocationFactorJunior(15);
        
        tranchePool.setSeniorAPR(500);
        tranchePool.setTargetJuniorAPR(1000);

        // Whitelist users
        tranchePool.updateWhitelist(seniorUser1, true);
        tranchePool.updateWhitelist(seniorUser2, true);
        tranchePool.updateWhitelist(seniorUser3, true);
        tranchePool.updateWhitelist(juniorUser1, true);
        tranchePool.updateWhitelist(juniorUser2, true);
        tranchePool.updateWhitelist(juniorUser3, true);
        tranchePool.updateEquityTrancheWhiteList(equityUser1, true);
        tranchePool.updateEquityTrancheWhiteList(equityUser2, true);

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
        tranchePool.setPoolState(ITranchePool.PoolState.COMMITED);

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
