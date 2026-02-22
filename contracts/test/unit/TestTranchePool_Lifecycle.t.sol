// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {TestTranchePoolBase} from "./TestTranchePoolBase.t.sol";
import {TranchePool, ITranchePool} from "../../src/TranchePool.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {VmSafe} from "forge-std/Vm.sol";

contract TestTranchePool_Lifecycle is TestTranchePoolBase {
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

        // Waterfall: Senior first
        // Since principalRepaid (5M) < Senior Deployed (~8M), Senior gets everything
        uint256 expectedSenior = principalRepaid;
        uint256 expectedJunior = 0;
        uint256 expectedEquity = 0;

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
                ITranchePool.TranchePool__InvalidTransferAmount.selector,
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
            ITranchePool.TranchePool__PrincipalRepaymentExceeded.selector
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
        tranchePool.onLoss(loss, 0);

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
        tranchePool.onLoss(loss, 0);

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
        tranchePool.onLoss(loss, 0);

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
                ITranchePool.TranchePool__LossExceededCapital.selector,
                1
            )
        );
        tranchePool.onLoss(excessiveLoss, 0);
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

        // Waterfall: Senior Shortfall -> Junior Shortfall -> Equity Shortfall -> Equity Upside
        // No shortfall initiated in this test, so all goes to Equity Upside
        uint256 expectedSenior = 0;
        uint256 expectedJunior = 0;
        uint256 expectedEquity = recoveryAmount;

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
        vm.expectRevert(ITranchePool.TranchePool__InsufficientShares.selector);
        tranchePool.claimSeniorInterest();
    }

    function test_ClaimSeniorInterest_RevertIf_ZeroClaim() public {
        uint256 depositAmount = 5_00_00_000 * USDT;
        vm.startPrank(seniorUser1);
        usdt.approve(address(tranchePool), depositAmount);
        tranchePool.depositSeniorTranche(depositAmount);

        // Try to claim with no index change
        vm.expectRevert(ITranchePool.TranchePool__ZeroWithdrawal.selector);
        tranchePool.claimSeniorInterest();
        vm.stopPrank();
    }

    function test_ClaimJuniorInterest_RevertIf_NoShares() public {
        vm.prank(juniorUser1);
        vm.expectRevert(ITranchePool.TranchePool__InsufficientShares.selector);
        tranchePool.claimJuniorInterest();
    }

    function test_ClaimEquityInterest_RevertIf_NoShares() public {
        vm.prank(equityUser1);
        vm.expectRevert(ITranchePool.TranchePool__InsufficientShares.selector);
        tranchePool.claimEquityInterest();
    }

    /*//////////////////////////////////////////////////////////////
                        POOL STATE TESTS
    //////////////////////////////////////////////////////////////*/

    function test_SetPoolState_ToCommited_Success() public {
        vm.prank(deployer);
        tranchePool.setPoolState(ITranchePool.PoolState.COMMITED);

        assertEq(
            uint256(tranchePool.getPoolState()),
            uint256(ITranchePool.PoolState.COMMITED)
        );
    }

    function test_SetPoolState_ToDeployed_Success() public {
        vm.startPrank(deployer);
        tranchePool.setPoolState(ITranchePool.PoolState.COMMITED);
        tranchePool.setPoolState(ITranchePool.PoolState.DEPLOYED);
        vm.stopPrank();

        assertEq(
            uint256(tranchePool.getPoolState()),
            uint256(ITranchePool.PoolState.DEPLOYED)
        );
    }

    function test_SetPoolState_ToClosed_Success() public {
        _depositToAllTranches();
        // Do NOT allocate capital. Closing is only allowed if deployed == 0.

        vm.prank(deployer);
        tranchePool.setPoolState(ITranchePool.PoolState.CLOSED);

        assertEq(
            uint256(tranchePool.getPoolState()),
            uint256(ITranchePool.PoolState.CLOSED)
        );
    }

    function test_SetPoolState_ToClosed_RevertIf_Deployed() public {
        _depositToAllTranches();
        _allocateCapital();

        vm.prank(deployer);
        vm.expectRevert(
            ITranchePool.TranchePool__DeployedCapitalExists.selector
        );
        tranchePool.setPoolState(ITranchePool.PoolState.CLOSED);
    }

    function test_SetPoolState_RevertIf_Backwards() public {
        vm.startPrank(deployer);
        tranchePool.setPoolState(ITranchePool.PoolState.COMMITED);

        vm.expectRevert(
            abi.encodeWithSelector(
                ITranchePool.TranchePool__InvalidStateTransition.selector,
                ITranchePool.PoolState.OPEN
            )
        );
        tranchePool.setPoolState(ITranchePool.PoolState.OPEN);
        vm.stopPrank();
    }

    /*//////////////////////////////////////////////////////////////
                        ADMIN SETTER TESTS
    //////////////////////////////////////////////////////////////*/

    function test_SetAllocationFactor_Senior_Success() public {
        vm.prank(deployer);
        tranchePool.setTrancheCapitalAllocationFactorSenior(70);

        assertEq(tranchePool.getSeniorAllocationRatio(), 70);
    }

    function test_SetAllocationFactor_Junior_Success() public {
        vm.prank(deployer);
        tranchePool.setTrancheCapitalAllocationFactorJunior(20);

        assertEq(tranchePool.getJuniorAllocationRatio(), 20);
    }

    function test_SetAllocationFactor_RevertIf_ExceedsMax() public {
        vm.prank(deployer);
        vm.expectRevert(
            ITranchePool.TranchePool__InvalidAllocationRatio.selector
        );
        tranchePool.setTrancheCapitalAllocationFactorSenior(90);
    }

    function test_SetSeniorAPR_Success() public {
        vm.prank(deployer);
        tranchePool.setSeniorAPR(500);

        assertEq(tranchePool.s_senior_apr_bps(), 500);
    }

    function test_SetSeniorAPR_RevertIf_Zero() public {
        vm.prank(deployer);
        vm.expectRevert(ITranchePool.TranchePool__ZeroAPRError.selector);
        tranchePool.setSeniorAPR(0);
    }

    function test_SetTargetJuniorAPR_Success() public {
        vm.prank(deployer);
        tranchePool.setTargetJuniorAPR(1000);

        assertEq(tranchePool.s_target_junior_apr_bps(), 1000);
    }

    function test_SetTargetJuniorAPR_RevertIf_Zero() public {
        vm.prank(deployer);
        vm.expectRevert(ITranchePool.TranchePool__ZeroAPRError.selector);
        tranchePool.setTargetJuniorAPR(0);
    }

    function test_SetMaxCap_RevertIf_Zero() public {
        vm.prank(deployer);
        vm.expectRevert(ITranchePool.TranchePool__ZeroValueError.selector);
        tranchePool.setMaxAllocationCapSeniorTranche(0);
    }

    function test_SetLoanEngine_Success() public {
        address newLoanEngine = makeAddr("newLoanEngine");

        vm.prank(deployer);
        tranchePool.setLoanEngine(newLoanEngine);

        assertEq(tranchePool.getLoanEngine(), newLoanEngine);
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
        tranchePool.updateEquityTrancheWhiteList(newUser, true);

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

    function test_OnInterestAccrued_DistributesCorrectly() public {
        _depositToAllTranches();
        _allocateCapital();

        // Simulate 1 year passing
        uint256 timeElapsed = 365 days;
        vm.warp(block.timestamp + timeElapsed);

        uint256 seniorDeployed = tranchePool.getSeniorTrancheDeployedValue();
        uint256 juniorDeployed = tranchePool.getJuniorTrancheDeployedValue();

        // Calculate expected interest
        // Senior: 5% of deployed
        uint256 expectedSeniorInterest = (seniorDeployed * 500) / 10000;
        // Junior: 10% of deployed
        uint256 expectedJuniorInterest = (juniorDeployed * 1000) / 10000;

        // Total interest to distribute (make it sufficient to cover both + some equity)
        uint256 totalInterest = expectedSeniorInterest +
            expectedJuniorInterest +
            10_000 *
            USDT;

        uint256 seniorInterestBefore = tranchePool.seniorAccruedInterest();
        uint256 juniorInterestBefore = tranchePool.juniorAccruedInterest();
        uint256 equityInterestBefore = tranchePool.equityAccruedInterest();

        vm.prank(loanEngine);
        tranchePool.onInterestAccrued(totalInterest);

        assertEq(
            tranchePool.seniorAccruedInterest(),
            seniorInterestBefore + expectedSeniorInterest,
            "Senior interest incorrect"
        );
        assertEq(
            tranchePool.juniorAccruedInterest(),
            juniorInterestBefore + expectedJuniorInterest,
            "Junior interest incorrect"
        );
        assertEq(
            tranchePool.equityAccruedInterest(),
            equityInterestBefore + 10_000 * USDT,
            "Equity interest incorrect"
        );
    }
}
