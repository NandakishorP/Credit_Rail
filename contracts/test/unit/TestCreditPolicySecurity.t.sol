// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Test} from "forge-std/Test.sol";
import {CreditPolicy} from "../../src/CreditPolicy.sol";
import {ICreditPolicy} from "../../src/interfaces/ICreditPolicy.sol";
import {ERC1967Proxy} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import {MockPoseidon2} from "../mocks/MockPoseidon2.sol";

/**
 * @title TestCreditPolicySecurity
 * @notice Security-focused tests for CreditPolicy: initializer re-entry,
 *         UUPS upgrade auth, access control on role management, _requireU64
 *         boundary, setPolicyScopeHash, and freeze-gate enforcement.
 */
contract TestCreditPolicySecurity is Test {
    CreditPolicy creditPolicy;

    address deployer = makeAddr("deployer");
    address attacker = makeAddr("attacker");

    MockPoseidon2 mockPoseidon;

    function setUp() public {
        vm.startPrank(deployer);
        mockPoseidon = new MockPoseidon2();
        CreditPolicy impl = new CreditPolicy();
        ERC1967Proxy proxy = new ERC1967Proxy(
            address(impl),
            abi.encodeCall(CreditPolicy.initialize, (deployer, address(mockPoseidon)))
        );
        creditPolicy = CreditPolicy(address(proxy));
        creditPolicy.setMaxTiers(5);
        vm.stopPrank();
    }

    // =========================================================================
    //                    INITIALIZER SECURITY
    // =========================================================================

    function test_Initialize_CannotReinitializeProxy() public {
        vm.expectRevert();
        creditPolicy.initialize(deployer, address(mockPoseidon));
    }

    function test_Initialize_RolesGrantedCorrectly() public view {
        assertTrue(
            creditPolicy.hasRole(creditPolicy.DEFAULT_ADMIN_ROLE(), deployer)
        );
        assertTrue(
            creditPolicy.hasRole(creditPolicy.POLICY_ADMIN_ROLE(), deployer)
        );
        assertTrue(
            creditPolicy.hasRole(creditPolicy.POLICY_EDITOR_ROLE(), deployer)
        );
        assertTrue(
            creditPolicy.hasRole(creditPolicy.INDUSTRY_ADMIN_ROLE(), deployer)
        );
    }

    // =========================================================================
    //                    UUPS UPGRADE AUTHORIZATION
    // =========================================================================

    function test_Upgrade_OnlyDefaultAdmin() public {
        CreditPolicy newImpl = new CreditPolicy();
        vm.prank(deployer);
        creditPolicy.upgradeToAndCall(address(newImpl), "");
    }

    function test_Upgrade_RevertsForNonAdmin() public {
        CreditPolicy newImpl = new CreditPolicy();
        vm.prank(attacker);
        vm.expectRevert();
        creditPolicy.upgradeToAndCall(address(newImpl), "");
    }

    // =========================================================================
    //                    POLICY CREATION SECURITY
    // =========================================================================

    function test_CreatePolicy_RevertsOnVersionZero() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.createPolicy(0);
    }

    function test_CreatePolicy_RevertsOnDuplicateVersion() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(1);
        vm.expectRevert(
            abi.encodeWithSelector(
                CreditPolicy.CreditPolicy__PolicyVersionExists.selector,
                1
            )
        );
        creditPolicy.createPolicy(1);
        vm.stopPrank();
    }

    function test_CreatePolicy_RevertsForNonPolicyAdmin() public {
        vm.prank(attacker);
        vm.expectRevert();
        creditPolicy.createPolicy(1);
    }

    // =========================================================================
    //                    FREEZE SECURITY
    // =========================================================================

    function test_FreezePolicy_RevertsIfIncomplete() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(1);
        // Only set eligibility - missing everything else
        creditPolicy.updateEligibility(1, _createEligibility());

        vm.expectRevert(
            abi.encodeWithSelector(
                CreditPolicy.CreditPolicy__IncompletePolicy.selector,
                1
            )
        );
        creditPolicy.freezePolicy(1);
        vm.stopPrank();
    }

    function test_FreezePolicy_RevertsIfAlreadyFrozen() public {
        _createAndFreezePolicy(1);

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSelector(
                CreditPolicy.CreditPolicy__PolicyFrozen.selector,
                1
            )
        );
        creditPolicy.freezePolicy(1);
    }

    function test_FreezePolicy_RevertsIfDeactivated() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(2);
        _populateAllSections(2);
        creditPolicy.deActivatePolicy(2);

        vm.expectRevert(
            abi.encodeWithSelector(
                CreditPolicy.CreditPolicy__PolicyNotActive.selector,
                2
            )
        );
        creditPolicy.freezePolicy(2);
        vm.stopPrank();
    }

    function test_FreezePolicy_RevertsWithoutDocumentHash() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(3);
        creditPolicy.updateEligibility(3, _createEligibility());
        creditPolicy.updateRatios(3, _createRatios());
        creditPolicy.updateConcentration(3, _createConcentration());
        creditPolicy.updateAttestation(3, _createAttestation());
        creditPolicy.updateCovenants(3, _createCovenants());
        creditPolicy.setLoanTier(3, 0, _createTier());
        // No document hash or scope hash set

        vm.expectRevert(
            abi.encodeWithSelector(
                CreditPolicy.CreditPolicy__IncompletePolicy.selector,
                3
            )
        );
        creditPolicy.freezePolicy(3);
        vm.stopPrank();
    }

    // =========================================================================
    //                    EDITABLE GATE (frozen policy cannot be edited)
    // =========================================================================

    function test_UpdateEligibility_RevertsOnFrozenPolicy() public {
        _createAndFreezePolicy(10);

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSelector(
                CreditPolicy.CreditPolicy__PolicyNotEditable.selector,
                10
            )
        );
        creditPolicy.updateEligibility(10, _createEligibility());
    }

    function test_UpdateRatios_RevertsOnFrozenPolicy() public {
        _createAndFreezePolicy(11);

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSelector(
                CreditPolicy.CreditPolicy__PolicyNotEditable.selector,
                11
            )
        );
        creditPolicy.updateRatios(11, _createRatios());
    }

    function test_SetLoanTier_RevertsOnFrozenPolicy() public {
        _createAndFreezePolicy(12);

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSelector(
                CreditPolicy.CreditPolicy__PolicyNotEditable.selector,
                12
            )
        );
        creditPolicy.setLoanTier(12, 0, _createTier());
    }

    // setPolicyScopeHash is no longer a manual operation — it's computed
    // internally by freezePolicy(). This test is removed.

    // =========================================================================
    //                    _requireU64 BOUNDARY TEST
    // =========================================================================

    function test_RequireU64_AcceptsMaxU64() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(20);
        // u64 max = 18446744073709551615
        ICreditPolicy.EligibilityCriteria memory e = ICreditPolicy
            .EligibilityCriteria({
                minAnnualRevenue: type(uint64).max,
                minEBITDA: 0,
                minTangibleNetWorth: 0,
                minBusinessAgeDays: 0,
                maxDefaultsLast36Months: 0,
                bankruptcyExcluded: false
            });
        creditPolicy.updateEligibility(20, e);
        vm.stopPrank();
    }

    function test_RequireU64_RevertsOnU64PlusOne() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(21);
        ICreditPolicy.EligibilityCriteria memory e = ICreditPolicy
            .EligibilityCriteria({
                minAnnualRevenue: uint256(type(uint64).max) + 1,
                minEBITDA: 0,
                minTangibleNetWorth: 0,
                minBusinessAgeDays: 0,
                maxDefaultsLast36Months: 0,
                bankruptcyExcluded: false
            });
        vm.expectRevert(
            abi.encodeWithSelector(
                CreditPolicy.CreditPolicy__ValueExceedsU64.selector,
                "minAnnualRevenue",
                uint256(type(uint64).max) + 1
            )
        );
        creditPolicy.updateEligibility(21, e);
        vm.stopPrank();
    }

    // =========================================================================
    //                    INDUSTRY CONTROLS
    // =========================================================================

    function test_ExcludeIndustry_RevertsOnZeroHash() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(30);
        vm.expectRevert(
            CreditPolicy.CreditPolicy__InvalidIndustryHash.selector
        );
        creditPolicy.excludeIndustry(30, bytes32(0));
        vm.stopPrank();
    }

    function test_IncludeIndustry_RevertsOnZeroHash() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(31);
        vm.expectRevert(
            CreditPolicy.CreditPolicy__InvalidIndustryHash.selector
        );
        creditPolicy.includeIndustry(31, bytes32(0));
        vm.stopPrank();
    }

    function test_ExcludeIndustry_RevertsForNonIndustryAdmin() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(32);

        vm.prank(attacker);
        vm.expectRevert();
        creditPolicy.excludeIndustry(32, keccak256("GAMBLING"));
    }

    // setPolicyScopeHash tests removed — hash is now computed internally by freezePolicy()

    // =========================================================================
    //                    ROLE MANAGEMENT ACCESS CONTROL
    // =========================================================================

    function test_ChangeDefaultAdmin_RevertsForNonAdmin() public {
        vm.prank(attacker);
        vm.expectRevert();
        creditPolicy.changeDefaultAdmin(attacker);
    }

    function test_ChangeDefaultAdmin_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__ZeroAddress.selector);
        creditPolicy.changeDefaultAdmin(address(0));
    }

    function test_ChangeDefaultAdmin_TransfersRole() public {
        address newAdmin = makeAddr("newAdmin");
        vm.prank(deployer);
        creditPolicy.changeDefaultAdmin(newAdmin);

        assertTrue(
            creditPolicy.hasRole(creditPolicy.DEFAULT_ADMIN_ROLE(), newAdmin)
        );
        assertFalse(
            creditPolicy.hasRole(creditPolicy.DEFAULT_ADMIN_ROLE(), deployer)
        );
    }

    function test_GrantPolicyAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__ZeroAddress.selector);
        creditPolicy.grantPolicyAdminRole(address(0));
    }

    function test_RevokePolicyAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__ZeroAddress.selector);
        creditPolicy.revokePolicyAdminRole(address(0));
    }

    function test_GrantPolicyEditorRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__ZeroAddress.selector);
        creditPolicy.grantPolicyEditorRole(address(0));
    }

    function test_RevokePolicyEditorRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__ZeroAddress.selector);
        creditPolicy.revokePolicyEditorRole(address(0));
    }

    function test_GrantIndustryAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__ZeroAddress.selector);
        creditPolicy.grantIndustryAdminRole(address(0));
    }

    function test_RevokeIndustryAdminRole_RevertsOnZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__ZeroAddress.selector);
        creditPolicy.revokeIndustryAdminRole(address(0));
    }

    function test_GrantPolicyAdminRole_RevertsForNonAdmin() public {
        vm.prank(attacker);
        vm.expectRevert();
        creditPolicy.grantPolicyAdminRole(attacker);
    }

    // =========================================================================
    //                    TIER VALIDATION
    // =========================================================================

    function test_SetLoanTier_RevertsOnTierIdExceedingMaxTiers() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(50);
        vm.expectRevert(
            abi.encodeWithSelector(
                CreditPolicy.CreditPolicy__InvalidTierCount.selector,
                5 // tierId >= maxTiers (5)
            )
        );
        creditPolicy.setLoanTier(50, 5, _createTier());
        vm.stopPrank();
    }

    function test_SetMaxTiers_RevertsOn255() public {
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSelector(
                CreditPolicy.CreditPolicy__InvalidTierCount.selector,
                255
            )
        );
        creditPolicy.setMaxTiers(255);
    }

    // =========================================================================
    //                    EVENTS
    // =========================================================================

    function test_Event_PolicyCreated() public {
        vm.expectEmit(false, false, false, true);
        emit CreditPolicy.PolicyCreated(60, block.timestamp);

        vm.prank(deployer);
        creditPolicy.createPolicy(60);
    }

    function test_Event_PolicyFrozen() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(61);
        _populateAllSections(61);

        vm.expectEmit(false, false, false, true);
        emit CreditPolicy.PolicyFrozen(61, block.timestamp);
        creditPolicy.freezePolicy(61);
        vm.stopPrank();
    }

    // PolicyScopeHashSet event test removed — hash is now computed internally

    function test_Event_DefaultAdminChanged() public {
        address newAdmin = makeAddr("newAdmin");

        vm.expectEmit(true, true, false, false);
        emit CreditPolicy.DefaultAdminChanged(deployer, newAdmin);

        vm.prank(deployer);
        creditPolicy.changeDefaultAdmin(newAdmin);
    }

    function test_Event_PolicyDeactivated() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(63);

        vm.expectEmit(false, false, false, true);
        emit CreditPolicy.PolicyDeactivated(63, block.timestamp);
        creditPolicy.deActivatePolicy(63);
        vm.stopPrank();
    }

    // =========================================================================
    //                    HELPERS
    // =========================================================================

    function _createAndFreezePolicy(uint256 version) internal {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(version);
        _populateAllSections(version);
        creditPolicy.freezePolicy(version);
        vm.stopPrank();
    }

    function _populateAllSections(uint256 version) internal {
        creditPolicy.updateEligibility(version, _createEligibility());
        creditPolicy.updateRatios(version, _createRatios());
        creditPolicy.updateConcentration(version, _createConcentration());
        creditPolicy.updateAttestation(version, _createAttestation());
        creditPolicy.updateCovenants(version, _createCovenants());
        creditPolicy.setLoanTier(version, 0, _createTier());
        creditPolicy.setPolicyDocument(version, keccak256("doc"), "ipfs://doc");
    }

    function _createEligibility()
        internal
        pure
        returns (ICreditPolicy.EligibilityCriteria memory)
    {
        return
            ICreditPolicy.EligibilityCriteria({
                minAnnualRevenue: 1_000_000,
                minEBITDA: 100_000,
                minTangibleNetWorth: 5_000_000,
                minBusinessAgeDays: 180,
                maxDefaultsLast36Months: 0,
                bankruptcyExcluded: true
            });
    }

    function _createRatios()
        internal
        pure
        returns (ICreditPolicy.FinancialRatios memory)
    {
        return
            ICreditPolicy.FinancialRatios({
                maxTotalDebtToEBITDA: 4e18,
                minInterestCoverageRatio: 2e18,
                minCurrentRatio: 1e18,
                minEBITDAMarginBps: 1500
            });
    }

    function _createConcentration()
        internal
        pure
        returns (ICreditPolicy.ConcentrationLimits memory)
    {
        return
            ICreditPolicy.ConcentrationLimits({
                maxSingleBorrowerBps: 1000,
                maxIndustryConcentrationBps: 3000
            });
    }

    function _createAttestation()
        internal
        pure
        returns (ICreditPolicy.AttestationRequirements memory)
    {
        return
            ICreditPolicy.AttestationRequirements({
                maxAttestationAgeDays: 90,
                reAttestationFrequencyDays: 180,
                requiresCPAAttestation: true
            });
    }

    function _createCovenants()
        internal
        pure
        returns (ICreditPolicy.MaintenanceCovenants memory)
    {
        return
            ICreditPolicy.MaintenanceCovenants({
                maxLeverageRatio: 4e18,
                minCoverageRatio: 2e18,
                minLiquidityAmount: 1_000_000,
                allowsDividends: false,
                reportingFrequencyDays: 90
            });
    }

    function _createTier()
        internal
        pure
        returns (ICreditPolicy.LoanTier memory)
    {
        return
            ICreditPolicy.LoanTier({
                name: "Tier 1",
                minRevenue: 1_000_000,
                maxRevenue: 5_000_000,
                minEBITDA: 100_000,
                maxDebtToEBITDA: 3e18,
                maxLoanToEBITDA: 2e18,
                interestRateBps: 800,
                originationFeeBps: 100,
                termDays: 365,
                active: true
            });
    }
}
