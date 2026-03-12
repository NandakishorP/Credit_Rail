// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Test} from "forge-std/Test.sol";
import {LoanEngine} from "../../src/LoanEngine.sol";
import {ILoanEngine} from "../../src/interfaces/ILoanEngine.sol";
import {TranchePool} from "../../src/TranchePool.sol";
import {ITranchePool} from "../../src/interfaces/ITranchePool.sol";
import {CreditPolicy} from "../../src/CreditPolicy.sol";
import {ICreditPolicy} from "../../src/interfaces/ICreditPolicy.sol";
import {MockLoanProofVerifier} from "../mocks/MockLoanProofVerifier.sol";
import {MockPoseidon2} from "../mocks/MockPoseidon2.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {ERC1967Proxy} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";

/**
 * @title TestLoanEngineAccessControl
 * @notice Tests that every role-gated function on LoanEngine correctly reverts
 *         when called by an unauthorized address, and that zero-address checks
 *         fire on role grant/revoke functions.
 */
contract TestLoanEngineAccessControl is Test {
    LoanEngine loanEngine;
    address deployer = makeAddr("deployer");
    address outsider = makeAddr("outsider");

    function setUp() public {
        ERC20Mock usdt = new ERC20Mock();
        vm.startPrank(deployer);

        MockLoanProofVerifier verifier = new MockLoanProofVerifier();

        TranchePool tpImpl = new TranchePool();
        ERC1967Proxy tpProxy = new ERC1967Proxy(
            address(tpImpl),
            abi.encodeCall(TranchePool.initialize, (address(usdt), deployer))
        );

        MockPoseidon2 poseidon = new MockPoseidon2();

        CreditPolicy cpImpl = new CreditPolicy();
        ERC1967Proxy cpProxy = new ERC1967Proxy(
            address(cpImpl),
            abi.encodeCall(CreditPolicy.initialize, (deployer, address(poseidon)))
        );

        LoanEngine leImpl = new LoanEngine();
        ERC1967Proxy leProxy = new ERC1967Proxy(
            address(leImpl),
            abi.encodeCall(
                LoanEngine.initialize,
                (
                    address(cpProxy),
                    address(verifier),
                    500,
                    address(tpProxy),
                    address(usdt),
                    address(poseidon),
                    deployer
                )
            )
        );
        loanEngine = LoanEngine(address(leProxy));
        vm.stopPrank();
    }

    // =========================================================================
    //               ROLE-GATED FUNCTIONS: outsider reverts
    // =========================================================================

    function test_SetWhitelistedOffRampingEntity_RevertsForNonConfigAdmin()
        public
    {
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.setWhitelistedOffRampingEntity(makeAddr("entity"), true);
    }

    function test_SetWhitelistedRecoveryAgent_RevertsForNonConfigAdmin()
        public
    {
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.setWhitelistedRecoveryAgent(makeAddr("agent"), true);
    }

    function test_SetWhitelistedRepaymentAgent_RevertsForNonConfigAdmin()
        public
    {
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.setWhitelistedRepaymentAgent(makeAddr("agent"), true);
    }

    function test_SetWhitelistedFeeManager_RevertsForNonConfigAdmin() public {
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.setWhitelistedFeeManager(makeAddr("mgr"), true);
    }

    function test_SetMaxOriginationFeeBps_RevertsForNonConfigAdmin() public {
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.setMaxOriginationFeeBps(200);
    }

    function test_SetUnderwriterAuthorization_RevertsForNonConfigAdmin()
        public
    {
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.setUnderwriterAuthorization(
            bytes32(uint256(1)),
            bytes32(uint256(2)),
            true
        );
    }

    function test_Pause_RevertsForNonEmergencyAdmin() public {
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.pause();
    }

    function test_Unpause_RevertsForNonEmergencyAdmin() public {
        vm.prank(deployer);
        loanEngine.pause();
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.unpause();
    }

    function test_ChangeDefaultAdmin_RevertsForNonAdmin() public {
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.changeDefaultAdmin(outsider);
    }

    function test_GrantFundManagerRole_RevertsForNonAdmin() public {
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.grantFundManagerRole(outsider);
    }

    function test_RevokeFundManagerRole_RevertsForNonAdmin() public {
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.revokeFundManagerRole(deployer);
    }

    function test_GrantServicerRole_RevertsForNonAdmin() public {
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.grantServicerRole(outsider);
    }

    function test_RevokeServicerRole_RevertsForNonAdmin() public {
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.revokeServicerRole(deployer);
    }

    function test_GrantRiskAdminRole_RevertsForNonAdmin() public {
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.grantRiskAdminRole(outsider);
    }

    function test_RevokeRiskAdminRole_RevertsForNonAdmin() public {
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.revokeRiskAdminRole(deployer);
    }

    function test_GrantConfigAdminRole_RevertsForNonAdmin() public {
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.grantConfigAdminRole(outsider);
    }

    function test_RevokeConfigAdminRole_RevertsForNonAdmin() public {
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.revokeConfigAdminRole(deployer);
    }

    function test_GrantEmergencyAdminRole_RevertsForNonAdmin() public {
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.grantEmergencyAdminRole(outsider);
    }

    function test_RevokeEmergencyAdminRole_RevertsForNonAdmin() public {
        vm.prank(outsider);
        vm.expectRevert();
        loanEngine.revokeEmergencyAdminRole(deployer);
    }

    // =========================================================================
    //               ZERO-ADDRESS CHECKS ON ROLE MANAGEMENT
    // =========================================================================

    function test_GrantFundManagerRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        loanEngine.grantFundManagerRole(address(0));
    }

    function test_RevokeFundManagerRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        loanEngine.revokeFundManagerRole(address(0));
    }

    function test_GrantServicerRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        loanEngine.grantServicerRole(address(0));
    }

    function test_RevokeServicerRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        loanEngine.revokeServicerRole(address(0));
    }

    function test_GrantRiskAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        loanEngine.grantRiskAdminRole(address(0));
    }

    function test_RevokeRiskAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        loanEngine.revokeRiskAdminRole(address(0));
    }

    function test_GrantConfigAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        loanEngine.grantConfigAdminRole(address(0));
    }

    function test_RevokeConfigAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        loanEngine.revokeConfigAdminRole(address(0));
    }

    function test_GrantEmergencyAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        loanEngine.grantEmergencyAdminRole(address(0));
    }

    function test_RevokeEmergencyAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        loanEngine.revokeEmergencyAdminRole(address(0));
    }

    // =========================================================================
    //               ZERO-ADDRESS CHECKS ON WHITELIST SETTERS
    // =========================================================================

    function test_SetWhitelistedOffRampingEntity_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        loanEngine.setWhitelistedOffRampingEntity(address(0), true);
    }

    function test_SetWhitelistedRecoveryAgent_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        loanEngine.setWhitelistedRecoveryAgent(address(0), true);
    }

    function test_SetWhitelistedRepaymentAgent_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        loanEngine.setWhitelistedRepaymentAgent(address(0), true);
    }

    function test_SetWhitelistedFeeManager_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(ILoanEngine.LoanEngine__ZeroAddress.selector);
        loanEngine.setWhitelistedFeeManager(address(0), true);
    }
}
