// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Test} from "forge-std/Test.sol";
import {TranchePool} from "../../src/TranchePool.sol";
import {ITranchePool} from "../../src/interfaces/ITranchePool.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {ERC1967Proxy} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";

/**
 * @title TestTranchePoolSecurity
 * @notice Security-focused tests for TranchePool: initializer re-entry,
 *         UUPS upgrade authorization, pause/unpause, access control on
 *         admin setters, sweep, claimInterest, and state transitions.
 */
contract TestTranchePoolSecurity is Test {
    TranchePool tranchePool;
    ERC20Mock usdt;

    address deployer = makeAddr("deployer");
    address attacker = makeAddr("attacker");
    address loanEngineAddr = makeAddr("loanEngine");
    address seniorUser = makeAddr("seniorUser");
    address juniorUser = makeAddr("juniorUser");
    address equityUser = makeAddr("equityUser");

    uint256 public USDT = 1e18;

    function setUp() public {
        usdt = new ERC20Mock();
        vm.startPrank(deployer);

        TranchePool impl = new TranchePool();
        ERC1967Proxy proxy = new ERC1967Proxy(
            address(impl),
            abi.encodeCall(TranchePool.initialize, (address(usdt), deployer))
        );
        tranchePool = TranchePool(address(proxy));

        tranchePool.setMaxDepositCapSeniorTranche(10_000_000 * USDT);
        tranchePool.setMaxDepositCapJuniorTranche(5_000_000 * USDT);
        tranchePool.setMaxDepositCapEquityTranche(3_000_000 * USDT);
        tranchePool.setMinimumDepositAmountSeniorTranche(10_000 * USDT);
        tranchePool.setMinimumDepositAmountJuniorTranche(10_000 * USDT);
        tranchePool.setMinimumDepositAmountEquityTranche(10_000 * USDT);
        tranchePool.setTrancheCapitalAllocationFactorSenior(80);
        tranchePool.setTrancheCapitalAllocationFactorJunior(15);
        tranchePool.setSeniorAPR(500);
        tranchePool.setTargetJuniorAPR(1000);
        tranchePool.updateWhitelist(seniorUser, true);
        tranchePool.updateWhitelist(juniorUser, true);
        tranchePool.updateEquityTrancheWhiteList(equityUser, true);
        tranchePool.setLoanEngine(loanEngineAddr);

        vm.stopPrank();

        // Fund users
        usdt.mint(seniorUser, 100_000_000 * USDT);
        usdt.mint(juniorUser, 50_000_000 * USDT);
        usdt.mint(equityUser, 50_000_000 * USDT);
    }

    // =========================================================================
    //                    INITIALIZER SECURITY
    // =========================================================================

    function test_Initialize_CannotReinitializeProxy() public {
        vm.expectRevert();
        tranchePool.initialize(address(usdt), deployer);
    }

    function test_Initialize_RevertsOnZeroStablecoin() public {
        TranchePool impl = new TranchePool();
        vm.expectRevert(ITranchePool.TranchePool__ZeroAddressError.selector);
        new ERC1967Proxy(
            address(impl),
            abi.encodeCall(TranchePool.initialize, (address(0), deployer))
        );
    }

    function test_Initialize_RevertsOnZeroAdmin() public {
        TranchePool impl = new TranchePool();
        vm.expectRevert(ITranchePool.TranchePool__ZeroAddressError.selector);
        new ERC1967Proxy(
            address(impl),
            abi.encodeCall(TranchePool.initialize, (address(usdt), address(0)))
        );
    }

    // =========================================================================
    //                    UUPS UPGRADE AUTHORIZATION
    // =========================================================================

    function test_Upgrade_OnlyDefaultAdmin() public {
        TranchePool newImpl = new TranchePool();
        vm.prank(deployer);
        tranchePool.upgradeToAndCall(address(newImpl), "");
    }

    function test_Upgrade_RevertsForNonAdmin() public {
        TranchePool newImpl = new TranchePool();
        vm.prank(attacker);
        vm.expectRevert();
        tranchePool.upgradeToAndCall(address(newImpl), "");
    }

    // =========================================================================
    //                    PAUSE / UNPAUSE
    // =========================================================================

    function test_Pause_OnlyEmergencyAdmin() public {
        vm.prank(deployer);
        tranchePool.pause();
        assertTrue(tranchePool.paused());
    }

    function test_Unpause_OnlyEmergencyAdmin() public {
        vm.prank(deployer);
        tranchePool.pause();
        vm.prank(deployer);
        tranchePool.unpause();
        assertFalse(tranchePool.paused());
    }

    function test_Pause_RevertsForNonEmergencyAdmin() public {
        vm.prank(attacker);
        vm.expectRevert();
        tranchePool.pause();
    }

    function test_Unpause_RevertsForNonEmergencyAdmin() public {
        vm.prank(deployer);
        tranchePool.pause();
        vm.prank(attacker);
        vm.expectRevert();
        tranchePool.unpause();
    }

    function test_Deposit_RevertsWhenPaused() public {
        vm.prank(deployer);
        tranchePool.pause();

        vm.startPrank(seniorUser);
        usdt.approve(address(tranchePool), 100_000 * USDT);
        vm.expectRevert();
        tranchePool.depositSeniorTranche(100_000 * USDT);
        vm.stopPrank();
    }

    // =========================================================================
    //                    ACCESS CONTROL ON ADMIN SETTERS
    // =========================================================================

    function test_SetLoanEngine_RevertsForNonAdmin() public {
        vm.prank(attacker);
        vm.expectRevert();
        tranchePool.setLoanEngine(makeAddr("newEngine"));
    }

    function test_SetLoanEngine_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ITranchePool.TranchePool__ZeroAddressError.selector);
        tranchePool.setLoanEngine(address(0));
    }

    function test_SetPoolState_RevertsForNonPoolAdmin() public {
        vm.prank(attacker);
        vm.expectRevert();
        tranchePool.setPoolState(ITranchePool.PoolState.COMMITTED);
    }

    function test_SetSeniorAPR_RevertsForNonConfigAdmin() public {
        vm.prank(attacker);
        vm.expectRevert();
        tranchePool.setSeniorAPR(600);
    }

    function test_SetSeniorAPR_RevertsOnZero() public {
        vm.prank(deployer);
        vm.expectRevert(ITranchePool.TranchePool__ZeroAPRError.selector);
        tranchePool.setSeniorAPR(0);
    }

    function test_SetTargetJuniorAPR_RevertsForNonConfigAdmin() public {
        vm.prank(attacker);
        vm.expectRevert();
        tranchePool.setTargetJuniorAPR(1200);
    }

    function test_SetTargetJuniorAPR_RevertsOnZero() public {
        vm.prank(deployer);
        vm.expectRevert(ITranchePool.TranchePool__ZeroAPRError.selector);
        tranchePool.setTargetJuniorAPR(0);
    }

    function test_SetMaxDepositCap_RevertsOnZero() public {
        vm.startPrank(deployer);
        vm.expectRevert(ITranchePool.TranchePool__ZeroValueError.selector);
        tranchePool.setMaxDepositCapSeniorTranche(0);
        vm.expectRevert(ITranchePool.TranchePool__ZeroValueError.selector);
        tranchePool.setMaxDepositCapJuniorTranche(0);
        vm.expectRevert(ITranchePool.TranchePool__ZeroValueError.selector);
        tranchePool.setMaxDepositCapEquityTranche(0);
        vm.stopPrank();
    }

    function test_SetMinDeposit_RevertsIfExceedsMaxCap() public {
        vm.startPrank(deployer);
        vm.expectRevert(
            ITranchePool.TranchePool__InvalidMinDepositAmount.selector
        );
        tranchePool.setMinimumDepositAmountSeniorTranche(999_999_999 * USDT);
        vm.stopPrank();
    }

    function test_UpdateWhitelist_RevertsForNonWhitelistAdmin() public {
        vm.prank(attacker);
        vm.expectRevert();
        tranchePool.updateWhitelist(makeAddr("user"), true);
    }

    function test_UpdateEquityWhitelist_RevertsForNonWhitelistAdmin() public {
        vm.prank(attacker);
        vm.expectRevert();
        tranchePool.updateEquityTrancheWhiteList(makeAddr("user"), true);
    }

    function test_SetAllocationFactor_RevertsOnInvalidRatio() public {
        // Senior + Junior > 100
        vm.startPrank(deployer);
        vm.expectRevert(
            ITranchePool.TranchePool__InvalidAllocationRatio.selector
        );
        tranchePool.setTrancheCapitalAllocationFactorSenior(90); // 90 + 15 = 105 > 100
        vm.stopPrank();
    }

    // =========================================================================
    //                    STATE TRANSITION SECURITY
    // =========================================================================

    function test_SetPoolState_CannotMoveBackward() public {
        vm.startPrank(deployer);
        tranchePool.setPoolState(ITranchePool.PoolState.COMMITTED);

        vm.expectRevert(
            abi.encodeWithSelector(
                ITranchePool.TranchePool__InvalidStateTransition.selector,
                ITranchePool.PoolState.OPEN
            )
        );
        tranchePool.setPoolState(ITranchePool.PoolState.OPEN);
        vm.stopPrank();
    }

    function test_SetPoolState_CannotCloseWithDeployedCapital() public {
        // Deposit and deploy capital
        _depositAll();

        vm.startPrank(deployer);
        tranchePool.setPoolState(ITranchePool.PoolState.COMMITTED);
        vm.stopPrank();

        // Allocate capital to simulate deployment
        vm.prank(loanEngineAddr);
        tranchePool.allocateCapital(
            100_000 * USDT,
            1_000 * USDT,
            makeAddr("borrower"),
            makeAddr("feeMgr")
        );

        vm.prank(deployer);
        vm.expectRevert(
            ITranchePool.TranchePool__DeployedCapitalExists.selector
        );
        tranchePool.setPoolState(ITranchePool.PoolState.CLOSED);
    }

    // =========================================================================
    //                    DEPOSIT SECURITY
    // =========================================================================

    function test_Deposit_RevertsForNonWhitelisted() public {
        vm.startPrank(attacker);
        usdt.approve(address(tranchePool), 100_000 * USDT);
        vm.expectRevert(
            abi.encodeWithSelector(
                ITranchePool.TranchePool__NotWhiteListed.selector,
                attacker
            )
        );
        tranchePool.depositSeniorTranche(100_000 * USDT);
        vm.stopPrank();
    }

    function test_DepositEquity_RevertsForNonEquityWhitelisted() public {
        // seniorUser is whitelisted for LP, but not for equity
        vm.startPrank(seniorUser);
        usdt.approve(address(tranchePool), 100_000 * USDT);
        vm.expectRevert(
            abi.encodeWithSelector(
                ITranchePool
                    .TranchePool__NotWhiteListedForEquityTranche
                    .selector,
                seniorUser
            )
        );
        tranchePool.depositEquityTranche(100_000 * USDT);
        vm.stopPrank();
    }

    function test_Deposit_RevertsOnZeroAmount() public {
        vm.startPrank(seniorUser);
        usdt.approve(address(tranchePool), 100_000 * USDT);
        vm.expectRevert(ITranchePool.TranchePool__ZeroValueError.selector);
        tranchePool.depositSeniorTranche(0);
        vm.stopPrank();
    }

    function test_Deposit_RevertsBelowMinimum() public {
        vm.startPrank(seniorUser);
        usdt.approve(address(tranchePool), 100 * USDT);
        vm.expectRevert(
            abi.encodeWithSelector(
                ITranchePool.TranchePool__LessThanDepositThreshold.selector,
                100 * USDT
            )
        );
        tranchePool.depositSeniorTranche(100 * USDT); // below 10,000 min
        vm.stopPrank();
    }

    function test_Deposit_RevertsAboveMaxCap() public {
        vm.startPrank(seniorUser);
        usdt.approve(address(tranchePool), 99_000_000 * USDT);
        vm.expectRevert(); // exceeds max cap
        tranchePool.depositSeniorTranche(99_000_000 * USDT);
        vm.stopPrank();
    }

    function test_Deposit_RevertsWhenNotOpen() public {
        vm.prank(deployer);
        tranchePool.setPoolState(ITranchePool.PoolState.COMMITTED);

        vm.startPrank(seniorUser);
        usdt.approve(address(tranchePool), 100_000 * USDT);
        vm.expectRevert(ITranchePool.TranchePool__PoolIsNotOpen.selector);
        tranchePool.depositSeniorTranche(100_000 * USDT);
        vm.stopPrank();
    }

    // =========================================================================
    //                    SWEEP SECURITY
    // =========================================================================

    function test_SweepProtocolRevenue_RevertsForNonTreasury() public {
        vm.prank(attacker);
        vm.expectRevert();
        tranchePool.sweepProtocolRevenue(attacker, 1);
    }

    function test_SweepProtocolRevenue_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ITranchePool.TranchePool__ZeroAddressError.selector);
        tranchePool.sweepProtocolRevenue(address(0), 1);
    }

    function test_SweepProtocolRevenue_RevertsOnZeroOrExcessiveAmount() public {
        vm.prank(deployer);
        vm.expectRevert(); // amount 0 or > s_protocolRevenue (which is 0)
        tranchePool.sweepProtocolRevenue(deployer, 0);
    }

    // =========================================================================
    //                    ROLE MANAGEMENT ZERO-ADDRESS CHECKS
    // =========================================================================

    function test_ChangeDefaultAdmin_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ITranchePool.TranchePool__ZeroAddressError.selector);
        tranchePool.changeDefaultAdmin(address(0));
    }

    function test_GrantPoolAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ITranchePool.TranchePool__ZeroAddressError.selector);
        tranchePool.grantPoolAdminRole(address(0));
    }

    function test_RevokePoolAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ITranchePool.TranchePool__ZeroAddressError.selector);
        tranchePool.revokePoolAdminRole(address(0));
    }

    function test_GrantConfigAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ITranchePool.TranchePool__ZeroAddressError.selector);
        tranchePool.grantConfigAdminRole(address(0));
    }

    function test_GrantWhitelistAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ITranchePool.TranchePool__ZeroAddressError.selector);
        tranchePool.grantWhitelistAdminRole(address(0));
    }

    function test_GrantEmergencyAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ITranchePool.TranchePool__ZeroAddressError.selector);
        tranchePool.grantEmergencyAdminRole(address(0));
    }

    function test_GrantTreasuryRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ITranchePool.TranchePool__ZeroAddressError.selector);
        tranchePool.grantTreasuryRole(address(0));
    }

    // =========================================================================
    //                    onLoanEngine-GATED CALLBACKS
    // =========================================================================

    function test_AllocateCapital_RevertsForNonLoanEngine() public {
        vm.prank(attacker);
        vm.expectRevert(
            abi.encodeWithSelector(
                ITranchePool.TranchePool__InvalidCaller.selector,
                attacker
            )
        );
        tranchePool.allocateCapital(100, 10, makeAddr("b"), makeAddr("f"));
    }

    function test_OnRepayment_RevertsForNonLoanEngine() public {
        vm.prank(attacker);
        vm.expectRevert(
            abi.encodeWithSelector(
                ITranchePool.TranchePool__InvalidCaller.selector,
                attacker
            )
        );
        tranchePool.onRepayment(100, 10);
    }

    function test_OnRecovery_RevertsForNonLoanEngine() public {
        vm.prank(attacker);
        vm.expectRevert(
            abi.encodeWithSelector(
                ITranchePool.TranchePool__InvalidCaller.selector,
                attacker
            )
        );
        tranchePool.onRecovery(100);
    }

    function test_OnLoss_RevertsForNonLoanEngine() public {
        vm.prank(attacker);
        vm.expectRevert(
            abi.encodeWithSelector(
                ITranchePool.TranchePool__InvalidCaller.selector,
                attacker
            )
        );
        tranchePool.onLoss(100, 10);
    }

    function test_OnInterestAccrued_RevertsForNonLoanEngine() public {
        vm.prank(attacker);
        vm.expectRevert(
            abi.encodeWithSelector(
                ITranchePool.TranchePool__InvalidCaller.selector,
                attacker
            )
        );
        tranchePool.onInterestAccrued(100);
    }

    // =========================================================================
    //                    EVENTS
    // =========================================================================

    function test_Event_PoolStateUpdated() public {
        vm.expectEmit(false, false, false, true);
        emit ITranchePool.PoolStateUpdated(ITranchePool.PoolState.COMMITTED);

        vm.prank(deployer);
        tranchePool.setPoolState(ITranchePool.PoolState.COMMITTED);
    }

    function test_Event_WhitelistUpdated() public {
        address newUser = makeAddr("newLP");
        vm.expectEmit(true, false, false, true);
        emit ITranchePool.WhitelistUpdated(newUser, true);

        vm.prank(deployer);
        tranchePool.updateWhitelist(newUser, true);
    }

    function test_Event_EquityWhitelistUpdated() public {
        address newUser = makeAddr("newEquity");
        vm.expectEmit(true, false, false, true);
        emit ITranchePool.EquityWhitelistUpdated(newUser, true);

        vm.prank(deployer);
        tranchePool.updateEquityTrancheWhiteList(newUser, true);
    }

    function test_Event_LoanEngineUpdated() public {
        address newEngine = makeAddr("newEngine");
        vm.expectEmit(true, false, false, false);
        emit ITranchePool.LoanEngineUpdated(newEngine);

        vm.prank(deployer);
        tranchePool.setLoanEngine(newEngine);
    }

    function test_Event_FundsDeposited() public {
        vm.startPrank(seniorUser);
        usdt.approve(address(tranchePool), 100_000 * USDT);

        vm.expectEmit(true, false, false, true);
        emit ITranchePool.FundsDepositedToSeniorTranche(
            seniorUser,
            100_000 * USDT,
            100_000 * USDT,
            block.timestamp
        );
        tranchePool.depositSeniorTranche(100_000 * USDT);
        vm.stopPrank();
    }

    // =========================================================================
    //                    HELPERS
    // =========================================================================

    function _depositAll() internal {
        vm.startPrank(seniorUser);
        usdt.approve(address(tranchePool), 500_000 * USDT);
        tranchePool.depositSeniorTranche(500_000 * USDT);
        vm.stopPrank();

        vm.startPrank(juniorUser);
        usdt.approve(address(tranchePool), 200_000 * USDT);
        tranchePool.depositJuniorTranche(200_000 * USDT);
        vm.stopPrank();

        vm.startPrank(equityUser);
        usdt.approve(address(tranchePool), 100_000 * USDT);
        tranchePool.depositEquityTranche(100_000 * USDT);
        vm.stopPrank();
    }
}
