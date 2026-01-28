// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import {CreditPolicy} from "../src/CreditPolicy.sol";
import {Test} from "forge-std/Test.sol";

contract TestCreditPolicy is Test {
    address deployer = makeAddr("deployer");
    address seniorUser1 = makeAddr("seniorUser1");
    address seniorUser2 = makeAddr("seniorUser2");
    CreditPolicy creditPolicy;

    function setUp() public {
        vm.startPrank(deployer);
        creditPolicy = new CreditPolicy();
        creditPolicy.setMaxTiers(50);
        vm.stopPrank();
    }

    /*//////////////////////////////////////////////////////////////
                            HELPER FUNCTIONS
    //////////////////////////////////////////////////////////////*/

    function _createPolicy(uint256 version) internal {
        vm.prank(deployer);
        creditPolicy.createPolicy(version);
    }

    function _freezePolicy(uint256 version) internal {
        vm.prank(deployer);
        creditPolicy.freezePolicy(version);
    }

    function _createAndFreezePolicy(uint256 version) internal {
        _createPolicy(version);
        vm.startPrank(deployer);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        creditPolicy.updateRatios(1, _createFinancialRatios());
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
        creditPolicy.setLoanTier(1, 0, _createMockTier("Tier 1"));
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );
        vm.stopPrank();
        _freezePolicy(version);
    }

    function _createEligibilityCriteria()
        internal
        pure
        returns (CreditPolicy.EligibilityCriteria memory)
    {
        return
            CreditPolicy.EligibilityCriteria({
                minAnnualRevenue: 1_00_00_000,
                minEBITDA: 10_00_000,
                minTangibleNetWorth: 5_00_00_000,
                minBusinessAgeDays: 180,
                maxDefaultsLast36Months: 0,
                bankruptcyExcluded: true
            });
    }

    function _createFinancialRatios()
        internal
        pure
        returns (CreditPolicy.FinancialRatios memory)
    {
        return
            CreditPolicy.FinancialRatios({
                maxTotalDebtToEBITDA: 4e18,
                minInterestCoverageRatio: 2e18,
                minCurrentRatio: 1e18,
                minEBITDAMarginBps: 1500
            });
    }

    function _createConcentrationLimits()
        internal
        pure
        returns (CreditPolicy.ConcentrationLimits memory)
    {
        return
            CreditPolicy.ConcentrationLimits({
                maxSingleBorrowerBps: 1000,
                maxIndustryConcentrationBps: 3000
            });
    }

    function _createAttestationRequirements()
        internal
        pure
        returns (CreditPolicy.AttestationRequirements memory)
    {
        return
            CreditPolicy.AttestationRequirements({
                maxAttestationAgeDays: 90,
                reAttestationFrequencyDays: 180,
                requiresCPAAttestation: true
            });
    }

    function _createMaintenanceCovenants()
        internal
        pure
        returns (CreditPolicy.MaintenanceCovenants memory)
    {
        return
            CreditPolicy.MaintenanceCovenants({
                maxLeverageRatio: 4e18,
                minCoverageRatio: 2e18,
                minLiquidityAmount: 1_00_00_000,
                allowsDividends: false,
                reportingFrequencyDays: 90
            });
    }

    function _createMockTier(
        string memory name
    ) internal pure returns (CreditPolicy.LoanTier memory) {
        return
            CreditPolicy.LoanTier({
                name: name,
                minRevenue: 1_00_00_000,
                maxRevenue: 5_00_00_000,
                minEBITDA: 10_00_000,
                maxDebtToEBITDA: 3e18,
                maxLoanToEBITDA: 2e18,
                interestRateBps: 800,
                originationFeeBps: 100,
                termDays: 365,
                active: true
            });
    }

    function _hashString(string memory str) internal pure returns (bytes32) {
        return keccak256(bytes(str));
    }

    /*//////////////////////////////////////////////////////////////
                        POLICY CREATION TESTS
    //////////////////////////////////////////////////////////////*/

    function testCreatePolicyRevertIfOwnerIsNotAdmin() public {
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.createPolicy(1);
    }

    function testCreatePolicyRevertsIfVersionIsZero() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.createPolicy(0);
    }

    function testCreatePolicyRevertsIfVersionExists() public {
        _createPolicy(1);
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__PolicyVersionExists(uint256)",
                1
            )
        );
        creditPolicy.createPolicy(1);
    }

    function testCreatePolicy() public {
        vm.prank(deployer);
        vm.expectEmit(true, true, false, true);
        emit CreditPolicy.PolicyCreated(1, block.timestamp);
        creditPolicy.createPolicy(1);

        assertEq(creditPolicy.policyCreated(1), true);
        assertEq(creditPolicy.policyActive(1), true);
        assertEq(creditPolicy.policyFrozen(1), false);
        assertEq(creditPolicy.lastUpdated(1), block.timestamp);
    }

    function testMultiplePolicyVersions() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(1);
        creditPolicy.createPolicy(2);
        creditPolicy.createPolicy(3);
        vm.stopPrank();

        assertEq(creditPolicy.policyCreated(1), true);
        assertEq(creditPolicy.policyCreated(2), true);
        assertEq(creditPolicy.policyCreated(3), true);
    }

    function testPolicyVersionIsolation() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(1);
        creditPolicy.createPolicy(2);

        bytes32 industry = _hashString("Gambling");
        creditPolicy.excludeIndustry(1, industry);

        assertTrue(creditPolicy.excludedIndustries(1, industry));
        assertFalse(creditPolicy.excludedIndustries(2, industry));
        vm.stopPrank();
    }

    /*//////////////////////////////////////////////////////////////
                        DEACTIVATE POLICY TESTS
    //////////////////////////////////////////////////////////////*/

    function testDeactivatePolicy() public {
        _createPolicy(1);
        assertEq(creditPolicy.policyActive(1), true);

        vm.prank(deployer);
        creditPolicy.deActivatePolicy(1);

        assertEq(creditPolicy.policyActive(1), false);
    }

    function testDeactivatePolicyRevertIfOwnerIsNotAdmin() public {
        _createPolicy(1);
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.deActivatePolicy(1);
    }

    function testDeactivatePolicyRevertsIfPolicyDontExist() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.deActivatePolicy(1);
    }

    function testDeactivateUpdatesLastUpdated() public {
        _createPolicy(1);
        uint256 t1 = creditPolicy.lastUpdated(1);

        vm.warp(block.timestamp + 100);
        vm.prank(deployer);
        creditPolicy.deActivatePolicy(1);

        assertEq(creditPolicy.lastUpdated(1), block.timestamp);
        assertGt(creditPolicy.lastUpdated(1), t1);
    }

    function testDeactivatePolicyIsIdempotent() public {
        _createPolicy(1);

        vm.prank(deployer);
        creditPolicy.deActivatePolicy(1);

        uint256 t1 = creditPolicy.lastUpdated(1);

        vm.warp(block.timestamp + 10);
        vm.prank(deployer);
        creditPolicy.deActivatePolicy(1);

        assertFalse(creditPolicy.policyActive(1));
        assertEq(creditPolicy.lastUpdated(1), block.timestamp);
        assertGt(creditPolicy.lastUpdated(1), t1);
    }

    function testUpdateRevertsIfPolicyInactive() public {
        _createPolicy(1);
        vm.prank(deployer);
        creditPolicy.deActivatePolicy(1);

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__PolicyNotEditable(uint256)",
                1
            )
        );
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
    }

    /*//////////////////////////////////////////////////////////////
                        FREEZE POLICY TESTS
    //////////////////////////////////////////////////////////////*/

    function testFreezePolicyUnitTest() public {
        _createPolicy(1);
        vm.startPrank(deployer);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        creditPolicy.updateRatios(1, _createFinancialRatios());
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
        creditPolicy.setLoanTier(1, 0, _createMockTier("Tier 1"));
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.PolicyFrozen(1, block.timestamp);
        creditPolicy.freezePolicy(1);
        vm.stopPrank();
        assertEq(creditPolicy.policyFrozen(1), true);
    }

    function testFreezePolicyRevertIfOwnerIsNotAdmin() public {
        _createPolicy(1);
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.freezePolicy(1);
    }

    function testFreezePolicyRevertsIfPolicyDontExist() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.freezePolicy(1);
    }

    function testFreezePolicyReverstIfPolicyIsNotActive() public {
        _createPolicy(1);
        vm.prank(deployer);
        creditPolicy.deActivatePolicy(1);

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature("CreditPolicy__PolicyNotActive(uint256)", 1)
        );
        creditPolicy.freezePolicy(1);
    }

    function testFreezePolicyRevertsIfAlreadyFrozen() public {
        _createAndFreezePolicy(1);

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature("CreditPolicy__PolicyFrozen(uint256)", 1)
        );
        creditPolicy.freezePolicy(1); // Try to freeze again
    }

    function testFreezePolicyMarksPolicyAsFrozen() public {
        _createPolicy(1);
        assertEq(creditPolicy.policyActive(1), true);
        vm.startPrank(deployer);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        creditPolicy.updateRatios(1, _createFinancialRatios());
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
        creditPolicy.setLoanTier(1, 0, _createMockTier("Tier 1"));
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );
        vm.stopPrank();
        _freezePolicy(1);
        assertEq(creditPolicy.policyFrozen(1), true);
    }

    function testFreezeUpdatesLastUpdated() public {
        _createPolicy(1);

        vm.startPrank(deployer);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        creditPolicy.updateRatios(1, _createFinancialRatios());
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
        creditPolicy.setLoanTier(1, 0, _createMockTier("Tier"));
        creditPolicy.setPolicyDocument(1, _hashString("doc"), "uri");
        vm.stopPrank();

        uint256 t1 = creditPolicy.lastUpdated(1);

        vm.warp(block.timestamp + 10);
        vm.prank(deployer);
        creditPolicy.freezePolicy(1);

        assertEq(creditPolicy.lastUpdated(1), block.timestamp);
        assertGt(creditPolicy.lastUpdated(1), t1);
    }

    function testFreezeDoesNotDeactivatePolicy() public {
        _createAndFreezePolicy(1);
        assertTrue(creditPolicy.policyActive(1));
        assertTrue(creditPolicy.policyFrozen(1));
    }

    function testFrozenPolicyIsFullyImmutable() public {
        _createAndFreezePolicy(1);

        vm.startPrank(deployer);

        vm.expectRevert();
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        vm.expectRevert();
        creditPolicy.updateRatios(1, _createFinancialRatios());
        vm.expectRevert();
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
        vm.expectRevert();
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
        vm.expectRevert();
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
        vm.expectRevert();
        creditPolicy.setLoanTier(1, 1, _createMockTier("T2"));
        vm.expectRevert();
        creditPolicy.excludeIndustry(1, _hashString("X"));
        vm.expectRevert();
        creditPolicy.setPolicyDocument(1, _hashString("x"), "uri");

        vm.stopPrank();
    }

    function testFreezePolicyRevertsIfNoEligibilitySet() public {
        _createPolicy(1);
        vm.startPrank(deployer);
        creditPolicy.updateRatios(1, _createFinancialRatios());
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
        creditPolicy.setLoanTier(1, 0, _createMockTier("Tier 1"));
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );

        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__IncompletePolicy(uint256)",
                1
            )
        );
        creditPolicy.freezePolicy(1);
        vm.stopPrank();
    }

    function testFreezePolicyRevertsIfNoRatiosSet() public {
        _createPolicy(1);
        vm.startPrank(deployer);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
        creditPolicy.setLoanTier(1, 0, _createMockTier("Tier 1"));
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );

        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__IncompletePolicy(uint256)",
                1
            )
        );
        creditPolicy.freezePolicy(1);
        vm.stopPrank();
    }

    function testFreezePolicyRevertsIfNoConcentrationSet() public {
        _createPolicy(1);
        vm.startPrank(deployer);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        creditPolicy.updateRatios(1, _createFinancialRatios());
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
        creditPolicy.setLoanTier(1, 0, _createMockTier("Tier 1"));
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );

        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__IncompletePolicy(uint256)",
                1
            )
        );
        creditPolicy.freezePolicy(1);
        vm.stopPrank();
    }

    function testFreezePolicyRevertsIfNoAttestationSet() public {
        _createPolicy(1);
        vm.startPrank(deployer);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        creditPolicy.updateRatios(1, _createFinancialRatios());
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
        creditPolicy.setLoanTier(1, 0, _createMockTier("Tier 1"));
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );

        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__IncompletePolicy(uint256)",
                1
            )
        );
        creditPolicy.freezePolicy(1);
        vm.stopPrank();
    }

    function testFreezePolicyRevertsIfNoCovenantsSet() public {
        _createPolicy(1);
        vm.startPrank(deployer);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        creditPolicy.updateRatios(1, _createFinancialRatios());
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
        creditPolicy.setLoanTier(1, 0, _createMockTier("Tier 1"));
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );

        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__IncompletePolicy(uint256)",
                1
            )
        );
        creditPolicy.freezePolicy(1);
        vm.stopPrank();
    }

    function testFreezePolicyRevertsIfNoLoanTiersSet() public {
        _createPolicy(1);
        vm.startPrank(deployer);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        creditPolicy.updateRatios(1, _createFinancialRatios());
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );

        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__IncompletePolicy(uint256)",
                1
            )
        );
        creditPolicy.freezePolicy(1);
        vm.stopPrank();
    }

    function testFreezePolicyRevertsIfNoDocumentHashSet() public {
        _createPolicy(1);
        vm.startPrank(deployer);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        creditPolicy.updateRatios(1, _createFinancialRatios());
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
        creditPolicy.setLoanTier(1, 0, _createMockTier("Tier 1"));
        // Note: NOT setting document hash

        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__IncompletePolicy(uint256)",
                1
            )
        );
        creditPolicy.freezePolicy(1);
        vm.stopPrank();
    }

    /*//////////////////////////////////////////////////////////////
                        ADMIN TESTS
    //////////////////////////////////////////////////////////////*/

    function testChangePolicyAdmin() public {
        vm.prank(deployer);
        creditPolicy.changePolicyAdmin(seniorUser1);
        assertEq(creditPolicy.policyAdmin(), seniorUser1);
    }

    function testChaingePolicyAdminRevertsIfNotAdmin() public {
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.changePolicyAdmin(seniorUser2);
    }

    function testAdminRevertIfNewAdminIsZeroAddress() public {
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature("CreditPolicy__InvalidAdmin()")
        );
        creditPolicy.changePolicyAdmin(address(0));
    }

    function testChangePolicyAdminEmitsEvent() public {
        vm.prank(deployer);
        vm.expectEmit(true, true, false, false);
        emit CreditPolicy.PolicyAdminChanged(seniorUser1); // You need to add this event to the contract!
        creditPolicy.changePolicyAdmin(seniorUser1);
    }

    function testOldAdminLosesAccessAfterAdminChange() public {
        vm.prank(deployer);
        creditPolicy.changePolicyAdmin(seniorUser1);

        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.createPolicy(99);
    }

    function testNewAdminCanCreatePolicy() public {
        vm.prank(deployer);
        creditPolicy.changePolicyAdmin(seniorUser1);

        vm.prank(seniorUser1);
        creditPolicy.createPolicy(99);

        assertEq(creditPolicy.policyCreated(99), true);
        assertEq(creditPolicy.policyAdmin(), seniorUser1);
    }

    function testNewAdminCanManageExistingPolicy() public {
        _createPolicy(1);

        vm.prank(deployer);
        creditPolicy.changePolicyAdmin(seniorUser1);

        vm.prank(seniorUser1);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
    }

    /*//////////////////////////////////////////////////////////////
                        ELIGIBILITY TESTS
    //////////////////////////////////////////////////////////////*/

    function testUpdateEligibility() public {
        _createPolicy(1);
        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.PolicyEligibilityUpdated(1, block.timestamp);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
    }

    function testMultipleEligibilityUpdates() public {
        _createPolicy(1);
        vm.startPrank(deployer);

        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        uint256 t1 = creditPolicy.lastUpdated(1);

        vm.warp(block.timestamp + 100);

        CreditPolicy.EligibilityCriteria memory newCriteria = CreditPolicy
            .EligibilityCriteria({
                minAnnualRevenue: 2_00_00_000,
                minEBITDA: 20_00_000,
                minTangibleNetWorth: 10_00_00_000,
                minBusinessAgeDays: 365,
                maxDefaultsLast36Months: 1,
                bankruptcyExcluded: false
            });

        creditPolicy.updateEligibility(1, newCriteria);
        assertGt(creditPolicy.lastUpdated(1), t1);

        (uint256 minRev, , , , , ) = creditPolicy.eligibility(1);
        assertEq(minRev, 2_00_00_000); // Verify it was overwritten
        vm.stopPrank();
    }

    function testUpdateEligibilityStoresDataCorrectly() public {
        _createPolicy(1);
        vm.prank(deployer);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());

        (
            uint256 minRev,
            uint256 minEbitda,
            uint256 minNet,
            uint256 minAge,
            uint256 maxDef,
            bool bankEx
        ) = creditPolicy.eligibility(1);

        assertEq(minRev, 1_00_00_000);
        assertEq(minEbitda, 10_00_000);
        assertEq(minNet, 5_00_00_000);
        assertEq(minAge, 180);
        assertEq(maxDef, 0);
        assertEq(bankEx, true);
    }

    function testUpdateEligibilityRevertsIfPolicyIsFrozen() public {
        _createAndFreezePolicy(1);
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__PolicyNotEditable(uint256)",
                1
            )
        );
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
    }

    function testUpdateEligibilityRevertsIfPolicyDontExist() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
    }

    function testUnAuthorizedUpdateEligibility() public {
        _createPolicy(1);
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
    }

    function testEligibilityWithZeroValues() public {
        _createPolicy(1);
        CreditPolicy.EligibilityCriteria memory criteria = CreditPolicy
            .EligibilityCriteria({
                minAnnualRevenue: 0,
                minEBITDA: 0,
                minTangibleNetWorth: 0,
                minBusinessAgeDays: 0,
                maxDefaultsLast36Months: 0,
                bankruptcyExcluded: false
            });

        vm.prank(deployer);
        creditPolicy.updateEligibility(1, criteria);

        (uint256 minRev, , , , uint256 maxDef, bool bankEx) = creditPolicy
            .eligibility(1);
        assertEq(minRev, 0);
        assertEq(maxDef, 0);
        assertFalse(bankEx);
    }

    /*//////////////////////////////////////////////////////////////
                        FINANCIAL RATIOS TESTS
    //////////////////////////////////////////////////////////////*/

    function testUpdateFinancialRatios() public {
        _createPolicy(1);
        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.PolicyRatiosUpdated(1, block.timestamp);
        creditPolicy.updateRatios(1, _createFinancialRatios());
    }

    function testUpdateRatiosStoresDataCorrectly() public {
        _createPolicy(1);
        vm.prank(deployer);
        creditPolicy.updateRatios(1, _createFinancialRatios());

        (
            uint256 maxDebt,
            uint256 minInt,
            uint256 minCurr,
            uint256 minMargin
        ) = creditPolicy.ratios(1);
        assertEq(maxDebt, 4e18);
        assertEq(minInt, 2e18);
        assertEq(minCurr, 1e18);
        assertEq(minMargin, 1500);
    }

    function testUpdateFinancialRatiosRevertsIfPolicyIsFrozen() public {
        _createAndFreezePolicy(1);
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__PolicyNotEditable(uint256)",
                1
            )
        );
        creditPolicy.updateRatios(1, _createFinancialRatios());
    }

    function testUpdateFinancialRatiosRevertIfPolicyDontExist() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.updateRatios(1, _createFinancialRatios());
    }

    function testUnAuthorizedUpdateFinancialRatios() public {
        _createPolicy(1);
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.updateRatios(1, _createFinancialRatios());
    }

    /*//////////////////////////////////////////////////////////////
                        CONCENTRATION TESTS
    //////////////////////////////////////////////////////////////*/

    function testUpdateConcentrationLimits() public {
        _createPolicy(1);
        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.PolicyConcentrationUpdated(1, block.timestamp);
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
    }

    function testUpdateConcentrationStoresDataCorrectly() public {
        _createPolicy(1);
        vm.prank(deployer);
        creditPolicy.updateConcentration(1, _createConcentrationLimits());

        (uint256 maxBorrower, uint256 maxIndustry) = creditPolicy.concentration(
            1
        );
        assertEq(maxBorrower, 1000);
        assertEq(maxIndustry, 3000);
    }

    function testUpdateConcentrationLimitsRevertsIfPolicyIsFrozen() public {
        _createAndFreezePolicy(1);
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__PolicyNotEditable(uint256)",
                1
            )
        );
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
    }

    function testUpdateConcentrationLimitsRevertIfPolicyDontExist() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
    }

    function testUnAuthorizedUpdateConcentrationLimits() public {
        _createPolicy(1);
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
    }

    /*//////////////////////////////////////////////////////////////
                        ATTESTATION TESTS
    //////////////////////////////////////////////////////////////*/

    function testUpdateAttestationRequirments() public {
        _createPolicy(1);
        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.PolicyAttestationUpdated(1, block.timestamp);
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
    }

    function testUpdateAttestationStoresDataCorrectly() public {
        _createPolicy(1);
        vm.prank(deployer);
        creditPolicy.updateAttestation(1, _createAttestationRequirements());

        (uint256 maxAge, uint256 freq, bool requiresCPA) = creditPolicy
            .attestation(1);
        assertEq(maxAge, 90);
        assertEq(freq, 180);
        assertTrue(requiresCPA);
    }

    function testUpdateAttestationRequirmentsRevertsIfPolicyIsFrozen() public {
        _createAndFreezePolicy(1);
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__PolicyNotEditable(uint256)",
                1
            )
        );
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
    }

    function testUpdateAttestationRequirmentsRevertIfPolicyDontExist() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
    }

    function testUnAuthorizedUpdateAttestationRequirements() public {
        _createPolicy(1);
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
    }

    /*//////////////////////////////////////////////////////////////
                        COVENANTS TESTS
    //////////////////////////////////////////////////////////////*/

    function testUpdateCovenants() public {
        _createPolicy(1);
        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.PolicyCovenantsUpdated(1, block.timestamp);
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
    }

    function testUpdateCovenantsStoresDataCorrectly() public {
        _createPolicy(1);
        vm.prank(deployer);
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());

        (
            uint256 maxLev,
            uint256 minCov,
            uint256 minLiq,
            bool allowDiv,
            uint256 reportFreq
        ) = creditPolicy.covenants(1);

        assertEq(maxLev, 4e18);
        assertEq(minCov, 2e18);
        assertEq(minLiq, 1_00_00_000);
        assertFalse(allowDiv);
        assertEq(reportFreq, 90);
    }

    function testUpdateCovenantsRevertsIfPolicyIsFrozen() public {
        _createAndFreezePolicy(1);
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__PolicyNotEditable(uint256)",
                1
            )
        );
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
    }

    function testUpdateCovenantsRevertIfPolicyDontExist() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
    }

    function testUnAuthorizedUpdateCovenants() public {
        _createPolicy(1);
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
    }

    /*//////////////////////////////////////////////////////////////
                        LOAN TIER TESTS
    //////////////////////////////////////////////////////////////*/

    function testSetLoanTier() public {
        _createPolicy(1);
        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.LoanTierUpdated(1, 1, block.timestamp);
        creditPolicy.setLoanTier(1, 1, _createMockTier("Tier 1"));
    }

    function testSetLoanTierWithMaxUint8RevertBecauseOfMaxTierLimit() public {
        _createPolicy(1);
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__InvalidTierCount(uint256)",
                255
            )
        );
        creditPolicy.setLoanTier(1, 255, _createMockTier("Max Tier"));
    }

    function testSetLoanTierStoresDataCorrectly() public {
        _createPolicy(1);
        CreditPolicy.LoanTier memory tier = _createMockTier("Premium Tier");
        tier.interestRateBps = 950;

        vm.prank(deployer);
        creditPolicy.setLoanTier(1, 0, tier);

        (string memory name, , , , , , uint256 intRate, , , ) = creditPolicy
            .loanTiers(1, 0);
        assertEq(name, "Premium Tier");
        assertEq(intRate, 950);
    }

    function testSetLoanTierRevertsIfNotAdmin() public {
        _createPolicy(1);
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.setLoanTier(1, 1, _createMockTier("Tier 1"));
    }

    function testSetLoanTierRevertsIfPolicyDontExist() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.setLoanTier(1, 1, _createMockTier("Tier 1"));
    }

    function testSetLoanTierRevertsIfPolicyIsFrozen() public {
        _createAndFreezePolicy(1);
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__PolicyNotEditable(uint256)",
                1
            )
        );
        creditPolicy.setLoanTier(1, 1, _createMockTier("Tier 1"));
    }

    function testSetLoanTierIncrementsTotalTiers() public {
        _createPolicy(1);
        vm.startPrank(deployer);

        creditPolicy.setLoanTier(1, 0, _createMockTier("Tier 1"));
        assertEq(creditPolicy.totalTiers(1), 1);

        creditPolicy.setLoanTier(1, 1, _createMockTier("Tier 2"));
        assertEq(creditPolicy.totalTiers(1), 2);

        creditPolicy.setLoanTier(1, 0, _createMockTier("Tier 1")); // Update existing
        assertEq(creditPolicy.totalTiers(1), 2);

        vm.stopPrank();
    }

    function testMultipleTierManagement() public {
        _createPolicy(1);
        vm.startPrank(deployer);

        for (uint8 i = 0; i < 5; i++) {
            creditPolicy.setLoanTier(
                1,
                i,
                _createMockTier(string(abi.encodePacked("Tier ", i)))
            );
        }
        assertEq(creditPolicy.totalTiers(1), 5);

        creditPolicy.setLoanTier(1, 6, _createMockTier("Tier 6")); // Gap at tier 5
        assertEq(creditPolicy.totalTiers(1), 7);

        vm.stopPrank();
    }

    function testTotalTiersDoesNotDecrease() public {
        _createPolicy(1);
        vm.startPrank(deployer);

        creditPolicy.setLoanTier(1, 5, _createMockTier("T5"));
        assertEq(creditPolicy.totalTiers(1), 6);

        creditPolicy.setLoanTier(1, 2, _createMockTier("T2"));
        assertEq(creditPolicy.totalTiers(1), 6);
    }

    function testTierExistsGetter() public {
        _createPolicy(1);
        vm.prank(deployer);
        creditPolicy.setLoanTier(1, 0, _createMockTier("Tier"));

        assertTrue(creditPolicy.tierExistsInPolicy(1, 0));
        assertFalse(creditPolicy.tierExistsInPolicy(1, 1));
    }

    function testOverwriteExistingTier() public {
        _createPolicy(1);
        vm.startPrank(deployer);

        CreditPolicy.LoanTier memory tier1 = _createMockTier("Original");
        tier1.interestRateBps = 800;
        creditPolicy.setLoanTier(1, 0, tier1);

        CreditPolicy.LoanTier memory tier2 = _createMockTier("Updated");
        tier2.interestRateBps = 900;
        creditPolicy.setLoanTier(1, 0, tier2);

        (string memory name, , , , , , uint256 rate, , , ) = creditPolicy
            .loanTiers(1, 0);
        assertEq(name, "Updated");
        assertEq(rate, 900);
        vm.stopPrank();
    }

    /*//////////////////////////////////////////////////////////////
                        INDUSTRY EXCLUSION TESTS
    //////////////////////////////////////////////////////////////*/

    function testExcludeIndustryUnitTest() public {
        _createPolicy(1);
        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.IndustryExcluded(
            1,
            _hashString("IndustryA"),
            block.timestamp
        );
        creditPolicy.excludeIndustry(1, _hashString("IndustryA"));
    }

    function testExcludeIndustryRevertsIfNotAdmin() public {
        _createPolicy(1);
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.excludeIndustry(1, _hashString("IndustryA"));
    }

    function testExcludeIndustryIsIdempotent() public {
        _createPolicy(1);
        bytes32 industry = _hashString("Gambling");

        vm.startPrank(deployer);
        creditPolicy.excludeIndustry(1, industry);
        assertTrue(creditPolicy.excludedIndustries(1, industry));

        creditPolicy.excludeIndustry(1, industry);
        assertTrue(creditPolicy.excludedIndustries(1, industry));
        vm.stopPrank();
    }

    function testExcludeIndustryRevertsIfDataIsZeroHash() public {
        _createPolicy(1);
        vm.prank(deployer);
        vm.expectRevert(
            CreditPolicy.CreditPolicy__InvalidIndustryHash.selector
        );
        creditPolicy.excludeIndustry(1, bytes32(0));
    }

    function testExcludeIndustryRevertsIfPolicyDontExist() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.excludeIndustry(1, _hashString("IndustryA"));
    }

    function testExcludeIndustryRevertsIfPolicyIsFrozen() public {
        _createAndFreezePolicy(1);
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__PolicyNotEditable(uint256)",
                1
            )
        );
        creditPolicy.excludeIndustry(1, _hashString("IndustryA"));
    }

    function testIncludeIndustryUnitTest() public {
        _createPolicy(1);
        vm.startPrank(deployer);
        creditPolicy.excludeIndustry(1, _hashString("IndustryA"));

        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.IndustryIncluded(
            1,
            _hashString("IndustryA"),
            block.timestamp
        );
        creditPolicy.includeIndustry(1, _hashString("IndustryA"));
        vm.stopPrank();
    }

    function testIncludeNeverExcludedIndustry() public {
        _createPolicy(1);
        bytes32 industry = _hashString("Tech");

        vm.prank(deployer);
        creditPolicy.includeIndustry(1, industry); // Should work, sets to false

        assertFalse(creditPolicy.excludedIndustries(1, industry));
    }

    function testIncludeIndustryRevertsIfDataIsZeroHash() public {
        _createPolicy(1);
        vm.prank(deployer);
        vm.expectRevert(
            CreditPolicy.CreditPolicy__InvalidIndustryHash.selector
        );
        creditPolicy.includeIndustry(1, bytes32(0));
    }

    function testIncludeIndustryRevertsIfNotAdmin() public {
        _createPolicy(1);
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.includeIndustry(1, _hashString("IndustryA"));
    }

    function testIncludeIndustryRevertsIfPolicyDontExist() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.includeIndustry(1, _hashString("IndustryA"));
    }

    function testIncludeIndustryRevertsIfPolicyIsFrozen() public {
        _createAndFreezePolicy(1);
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__PolicyNotEditable(uint256)",
                1
            )
        );
        creditPolicy.includeIndustry(1, _hashString("IndustryA"));
    }

    function testIndustryExclusionState() public {
        _createPolicy(1);
        bytes32 industry = _hashString("Manufacturing");

        assertEq(creditPolicy.excludedIndustries(1, industry), false);

        vm.prank(deployer);
        creditPolicy.excludeIndustry(1, industry);
        assertEq(creditPolicy.excludedIndustries(1, industry), true);

        vm.prank(deployer);
        creditPolicy.includeIndustry(1, industry);
        assertEq(creditPolicy.excludedIndustries(1, industry), false);
    }

    function testMultipleIndustryExclusions() public {
        _createPolicy(1);
        bytes32[] memory industries = new bytes32[](3);
        industries[0] = _hashString("Gambling");
        industries[1] = _hashString("Tobacco");
        industries[2] = _hashString("Cannabis");

        vm.startPrank(deployer);
        for (uint i = 0; i < industries.length; i++) {
            creditPolicy.excludeIndustry(1, industries[i]);
        }
        vm.stopPrank();

        for (uint i = 0; i < industries.length; i++) {
            assertTrue(creditPolicy.excludedIndustries(1, industries[i]));
        }
    }

    /*//////////////////////////////////////////////////////////////
                        DOCUMENT TESTS
    //////////////////////////////////////////////////////////////*/

    function testSetPolicyDocumentUnitTest() public {
        _createPolicy(1);
        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.PolicyDocumentSet(
            1,
            _hashString("document"),
            "ipfs://policyDocHash",
            block.timestamp
        );
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );
    }

    function testSetPolicyDocumentStoresCorrectly() public {
        _createPolicy(1);
        bytes32 docHash = _hashString("policyDocument");
        string memory uri = "ipfs://QmX...";

        vm.prank(deployer);
        creditPolicy.setPolicyDocument(1, docHash, uri);

        assertEq(creditPolicy.policyDocumentHash(1), docHash);
        assertEq(creditPolicy.policyDocumentURI(1), uri);
        assertEq(creditPolicy.lastUpdated(1), block.timestamp);
    }

    function testUpdatePolicyDocumentMultipleTimes() public {
        _createPolicy(1);
        vm.startPrank(deployer);

        creditPolicy.setPolicyDocument(1, _hashString("doc1"), "uri1");
        assertEq(creditPolicy.policyDocumentHash(1), _hashString("doc1"));

        creditPolicy.setPolicyDocument(1, _hashString("doc2"), "uri2");
        assertEq(creditPolicy.policyDocumentHash(1), _hashString("doc2"));
        assertEq(creditPolicy.policyDocumentURI(1), "uri2");
        vm.stopPrank();
    }

    function testSetPolicyDocumentRevertsIfNotAdmin() public {
        _createPolicy(1);
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );
    }

    function testSetPolicyDocumentRevertsIfPolicyDontExist() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );
    }

    function testSetPolicyDocumentRevertsIfPolicyIsFrozen() public {
        _createAndFreezePolicy(1);
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__PolicyNotEditable(uint256)",
                1
            )
        );
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );
    }

    /*//////////////////////////////////////////////////////////////
                        MISC TESTS
    //////////////////////////////////////////////////////////////*/

    function testLastUpdatedTimestamp() public {
        _createPolicy(1);
        uint256 creationTime = creditPolicy.lastUpdated(1);

        vm.warp(block.timestamp + 1000);

        vm.prank(deployer);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());

        uint256 updateTime = creditPolicy.lastUpdated(1);
        assertGt(updateTime, creationTime);
        assertEq(updateTime, block.timestamp);
    }

    function testLastUpdatedAlwaysMovesForward() public {
        _createPolicy(1);
        uint256 t1 = creditPolicy.lastUpdated(1);

        vm.warp(block.timestamp + 10);
        vm.prank(deployer);
        creditPolicy.updateRatios(1, _createFinancialRatios());
        assertGt(creditPolicy.lastUpdated(1), t1);
    }

    // Test complete lifecycle
    function testCompletePolicyLifecycle() public {
        _createPolicy(1);
        assertTrue(creditPolicy.policyActive(1));
        assertFalse(creditPolicy.policyFrozen(1));

        // Build policy
        vm.startPrank(deployer);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        creditPolicy.updateRatios(1, _createFinancialRatios());
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
        creditPolicy.setLoanTier(1, 0, _createMockTier("T1"));
        creditPolicy.setPolicyDocument(1, _hashString("doc"), "uri");
        vm.stopPrank();

        // Freeze
        _freezePolicy(1);
        assertTrue(creditPolicy.policyFrozen(1));
        assertTrue(creditPolicy.policyActive(1));

        // Cannot deactivate frozen policy? - TEST THIS
        vm.prank(deployer);
        creditPolicy.deActivatePolicy(1);
        assertFalse(creditPolicy.policyActive(1));
        assertTrue(creditPolicy.policyFrozen(1)); // Still frozen
    }

    // Test interaction between deactivate and freeze
    function testCannotFreezeDeactivatedPolicy() public {
        _createPolicy(1);
        vm.startPrank(deployer);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        creditPolicy.updateRatios(1, _createFinancialRatios());
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
        creditPolicy.setLoanTier(1, 0, _createMockTier("T1"));
        creditPolicy.setPolicyDocument(1, _hashString("doc"), "uri");

        creditPolicy.deActivatePolicy(1);

        vm.expectRevert(
            abi.encodeWithSignature("CreditPolicy__PolicyNotActive(uint256)", 1)
        );
        creditPolicy.freezePolicy(1);
        vm.stopPrank();
    }

    function testIsPolicyActiveGetter() public {
        _createPolicy(1);
        assertTrue(creditPolicy.isPolicyActive(1));

        vm.prank(deployer);
        creditPolicy.deActivatePolicy(1);
        assertFalse(creditPolicy.isPolicyActive(1));
    }

    function testIsPolicyFrozenGetter() public {
        _createAndFreezePolicy(1);
        assertTrue(creditPolicy.isPolicyFrozen(1));

        _createPolicy(2);
        assertFalse(creditPolicy.isPolicyFrozen(2));
    }

    // Test with extremely large version numbers
    function testPolicyWithLargeVersionNumber() public {
        uint256 largeVersion = type(uint256).max - 1;
        vm.prank(deployer);
        creditPolicy.createPolicy(largeVersion);
        assertTrue(creditPolicy.policyCreated(largeVersion));
    }

    // Test setting empty string for tier name
    function testLoanTierWithEmptyName() public {
        _createPolicy(1);
        CreditPolicy.LoanTier memory tier = _createMockTier("");

        vm.prank(deployer);
        creditPolicy.setLoanTier(1, 0, tier);

        (string memory name, , , , , , , , , ) = creditPolicy.loanTiers(1, 0);
        assertEq(name, "");
    }

    function testSetMaxTiersRevertsIfNotAdmin() public {
        _createPolicy(1);
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.setMaxTiers(30);
    }

    function testSetMaxTiersRevertIfItsMoreThan255() public {
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__InvalidTierCount(uint256)",
                255
            )
        );
        creditPolicy.setMaxTiers(255);
    }

    function testSetMaxTiersUnitTest() public {
        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.MaxTiersChanged(20);
        creditPolicy.setMaxTiers(20);

        assertEq(creditPolicy.getMaxTiers(), 20);
    }

    // Test setting empty URI
    function testSetPolicyDocumentWithEmptyURI() public {
        _createPolicy(1);
        vm.prank(deployer);
        creditPolicy.setPolicyDocument(1, _hashString("hash"), "");

        assertEq(creditPolicy.policyDocumentURI(1), "");
    }
}
