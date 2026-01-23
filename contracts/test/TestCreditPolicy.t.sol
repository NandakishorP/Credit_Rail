// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import {CreditPolicy} from "../src/CreditPolicy.sol";
import {Test} from "forge-std/Test.sol";

contract TestCreditPolicy is Test {
    address deployer = makeAddr("deployer");
    address seniorUser1 = makeAddr("seniorUser1");
    CreditPolicy creditPolicy;

    function setUp() public {
        vm.prank(deployer);
        creditPolicy = new CreditPolicy();
    }

    function testCreatePolicyRevertIfOwnerIsNotAdmin() public {
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.createPolicy(1);
    }

    // Test creating duplicate policy versions
    function testCreatePolicyRevertsIfVersionExists() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature(
                "CreditPolicy__PolicyVersionExists(uint256)",
                1
            )
        );
        creditPolicy.createPolicy(1); // Should revert
    }

    function testCreatePolicy() public {
        vm.prank(deployer);
        vm.expectEmit(true, true, false, true);
        emit CreditPolicy.PolicyCreated(1, block.timestamp);
        creditPolicy.createPolicy(1);
        assertEq(creditPolicy.policyCreated(1), true);
        assertEq(creditPolicy.policyActive(1), true);
        assertEq(creditPolicy.activePolicyVersion(), 1);
        assertEq(creditPolicy.policyFrozen(1), false);
        assertEq(creditPolicy.lastUpdated(1), block.timestamp);
    }

    function testFreezePolicyRevertIfOwnerIsNotAdmin() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.freezePolicy(1);
    }

    function testFreezePolicyRevertsIfPolicyDontExist() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.freezePolicy(1);
    }

    function testFreezePolicy() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.PolicyFrozen(1, block.timestamp);
        creditPolicy.freezePolicy(1);
        assertEq(creditPolicy.policyFrozen(1), true);
    }

    function testUpdateEligibility() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        CreditPolicy.EligibilityCriteria memory criteria = CreditPolicy
            .EligibilityCriteria({
                minAnnualRevenue: 1_00_00_000,
                minEBITDA: 10_00_000,
                minTangibleNetWorth: 5_00_00_000,
                minBusinessAgeDays: 180,
                maxDefaultsLast36Months: 0,
                bankruptcyExcluded: true
            });
        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.PolicyEligibilityUpdated(1, block.timestamp);
        creditPolicy.updateEligibility(1, criteria);
    }

    // Verify eligibility data is stored correctly
    function testUpdateEligibilityStoresDataCorrectly() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);

        CreditPolicy.EligibilityCriteria memory criteria = CreditPolicy
            .EligibilityCriteria({
                minAnnualRevenue: 1_00_00_000,
                minEBITDA: 10_00_000,
                minTangibleNetWorth: 5_00_00_000,
                minBusinessAgeDays: 180,
                maxDefaultsLast36Months: 0,
                bankruptcyExcluded: true
            });

        vm.prank(deployer);
        creditPolicy.updateEligibility(1, criteria);

        // Verify stored data
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

    // Test managing multiple policy versions
    function testMultiplePolicyVersions() public {
        vm.startPrank(deployer);

        creditPolicy.createPolicy(1);
        creditPolicy.createPolicy(2);
        creditPolicy.createPolicy(3);

        assertEq(creditPolicy.activePolicyVersion(), 3); // Last created is active
        assertEq(creditPolicy.policyCreated(1), true);
        assertEq(creditPolicy.policyCreated(2), true);
        assertEq(creditPolicy.policyCreated(3), true);

        vm.stopPrank();
    }

    function testUpdateEligibilityRevertsIfPolicyIsFrozen() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        vm.prank(deployer);
        creditPolicy.freezePolicy(1);
        CreditPolicy.EligibilityCriteria memory criteria = CreditPolicy
            .EligibilityCriteria({
                minAnnualRevenue: 1_00_00_000,
                minEBITDA: 10_00_000,
                minTangibleNetWorth: 5_00_00_000,
                minBusinessAgeDays: 180,
                maxDefaultsLast36Months: 0,
                bankruptcyExcluded: true
            });
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature("CreditPolicy__PolicyFrozen(uint256)", 1)
        );
        creditPolicy.updateEligibility(1, criteria);
    }

    function testUpdateEligibilityRevertsIfPolicyDontExist() public {
        CreditPolicy.EligibilityCriteria memory criteria = CreditPolicy
            .EligibilityCriteria({
                minAnnualRevenue: 1_00_00_000,
                minEBITDA: 10_00_000,
                minTangibleNetWorth: 5_00_00_000,
                minBusinessAgeDays: 180,
                maxDefaultsLast36Months: 0,
                bankruptcyExcluded: true
            });
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);

        creditPolicy.updateEligibility(1, criteria);
    }

    // testing unauthorized access
    function testUnAuthorizedUpdateEligibility() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        CreditPolicy.EligibilityCriteria memory criteria = CreditPolicy
            .EligibilityCriteria({
                minAnnualRevenue: 1_00_00_000,
                minEBITDA: 10_00_000,
                minTangibleNetWorth: 5_00_00_000,
                minBusinessAgeDays: 180,
                maxDefaultsLast36Months: 0,
                bankruptcyExcluded: true
            });
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.updateEligibility(1, criteria);
    }

    function testUnAuthorizedUpdateFinancialRatios() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        CreditPolicy.FinancialRatios memory ratios = CreditPolicy
            .FinancialRatios({
                maxTotalDebtToEBITDA: 4e18,
                minInterestCoverageRatio: 2e18,
                minCurrentRatio: 1e18,
                minEBITDAMarginBps: 1500
            });
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.updateRatios(1, ratios);
    }

    function testUpdateFinancialRatiosRevertsIfPolicyIsFrozen() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        vm.prank(deployer);
        creditPolicy.freezePolicy(1);
        CreditPolicy.FinancialRatios memory ratios = CreditPolicy
            .FinancialRatios({
                maxTotalDebtToEBITDA: 4e18,
                minInterestCoverageRatio: 2e18,
                minCurrentRatio: 1e18,
                minEBITDAMarginBps: 1500
            });
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature("CreditPolicy__PolicyFrozen(uint256)", 1)
        );
        creditPolicy.updateRatios(1, ratios);
    }

    function testUpdateFinancialRatiosRevertIfPolicyDontExist() public {
        CreditPolicy.FinancialRatios memory ratios = CreditPolicy
            .FinancialRatios({
                maxTotalDebtToEBITDA: 4e18,
                minInterestCoverageRatio: 2e18,
                minCurrentRatio: 1e18,
                minEBITDAMarginBps: 1500
            });
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.updateRatios(1, ratios);
    }

    function testUpdateFinancialRatios() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        CreditPolicy.FinancialRatios memory ratios = CreditPolicy
            .FinancialRatios({
                maxTotalDebtToEBITDA: 4e18,
                minInterestCoverageRatio: 2e18,
                minCurrentRatio: 1e18,
                minEBITDAMarginBps: 1500
            });
        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.PolicyRatiosUpdated(1, block.timestamp);
        creditPolicy.updateRatios(1, ratios);
    }

    function testUpdateRatiosStoresDataCorrectly() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);

        CreditPolicy.FinancialRatios memory ratios = CreditPolicy
            .FinancialRatios({
                maxTotalDebtToEBITDA: 4e18,
                minInterestCoverageRatio: 2e18,
                minCurrentRatio: 1e18,
                minEBITDAMarginBps: 1500
            });

        vm.prank(deployer);
        creditPolicy.updateRatios(1, ratios);

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

    function testLastUpdatedTimestamp() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);

        uint256 creationTime = creditPolicy.lastUpdated(1);

        // Advance time
        vm.warp(block.timestamp + 1000);

        CreditPolicy.EligibilityCriteria memory criteria = CreditPolicy
            .EligibilityCriteria({
                minAnnualRevenue: 1_00_00_000,
                minEBITDA: 10_00_000,
                minTangibleNetWorth: 5_00_00_000,
                minBusinessAgeDays: 180,
                maxDefaultsLast36Months: 0,
                bankruptcyExcluded: true
            });

        vm.prank(deployer);
        creditPolicy.updateEligibility(1, criteria);

        uint256 updateTime = creditPolicy.lastUpdated(1);
        assertGt(updateTime, creationTime);
        assertEq(updateTime, block.timestamp);
    }

    function testUpdateConcentrationStoresDataCorrectly() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);

        CreditPolicy.ConcentrationLimits memory limits = CreditPolicy
            .ConcentrationLimits({
                maxSingleBorrowerBps: 1000,
                maxIndustryConcentrationBps: 3000
            });

        vm.prank(deployer);
        creditPolicy.updateConcentration(1, limits);

        (uint256 maxBorrower, uint256 maxIndustry) = creditPolicy.concentration(
            1
        );
        assertEq(maxBorrower, 1000);
        assertEq(maxIndustry, 3000);
    }

    function testUpdateConcentrationLimitsRevertsIfPolicyIsFrozen() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        vm.prank(deployer);
        creditPolicy.freezePolicy(1);
        CreditPolicy.ConcentrationLimits memory limits = CreditPolicy
            .ConcentrationLimits({
                maxSingleBorrowerBps: 1000,
                maxIndustryConcentrationBps: 3000
            });
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature("CreditPolicy__PolicyFrozen(uint256)", 1)
        );
        creditPolicy.updateConcentration(1, limits);
    }

    function testUpdateConcentrationLimitsRevertIfPolicyDontExist() public {
        CreditPolicy.ConcentrationLimits memory limits = CreditPolicy
            .ConcentrationLimits({
                maxSingleBorrowerBps: 1000,
                maxIndustryConcentrationBps: 3000
            });
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.updateConcentration(1, limits);
    }

    function testUnAuthorizedUpdateConcentrationLimits() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        CreditPolicy.ConcentrationLimits memory limits = CreditPolicy
            .ConcentrationLimits({
                maxSingleBorrowerBps: 1000,
                maxIndustryConcentrationBps: 3000
            });
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.updateConcentration(1, limits);
    }

    function testUpdateConcentrationLimits() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        CreditPolicy.ConcentrationLimits memory limits = CreditPolicy
            .ConcentrationLimits({
                maxSingleBorrowerBps: 1000,
                maxIndustryConcentrationBps: 3000
            });
        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.PolicyConcentrationUpdated(1, block.timestamp);
        creditPolicy.updateConcentration(1, limits);
    }

    function testUpdateAttestationRequirmentsRevertsIfPolicyIsFrozen() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        vm.prank(deployer);
        creditPolicy.freezePolicy(1);
        CreditPolicy.AttestationRequirements memory requirements = CreditPolicy
            .AttestationRequirements({
                maxAttestationAgeDays: 90,
                reAttestationFrequencyDays: 180,
                requiresCPAAttestation: true
            });
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature("CreditPolicy__PolicyFrozen(uint256)", 1)
        );
        creditPolicy.updateAttestation(1, requirements);
    }

    function testUpdateAttestationRequirmentsRevertIfPolicyDontExist() public {
        CreditPolicy.AttestationRequirements memory requirements = CreditPolicy
            .AttestationRequirements({
                maxAttestationAgeDays: 90,
                reAttestationFrequencyDays: 180,
                requiresCPAAttestation: true
            });
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.updateAttestation(1, requirements);
    }

    function testUnAuthorizedUpdateAttestationRequirements() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        CreditPolicy.AttestationRequirements memory requirements = CreditPolicy
            .AttestationRequirements({
                maxAttestationAgeDays: 90,
                reAttestationFrequencyDays: 180,
                requiresCPAAttestation: true
            });
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.updateAttestation(1, requirements);
    }

    function testUpdateAttestationRequirments() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        CreditPolicy.AttestationRequirements memory requirements = CreditPolicy
            .AttestationRequirements({
                maxAttestationAgeDays: 90,
                reAttestationFrequencyDays: 180,
                requiresCPAAttestation: true
            });
        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.PolicyAttestationUpdated(1, block.timestamp);
        creditPolicy.updateAttestation(1, requirements);
    }

    function testUpdateCovenantsRevertsIfPolicyIsFrozen() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        vm.prank(deployer);
        creditPolicy.freezePolicy(1);
        CreditPolicy.MaintenanceCovenants memory covenants = CreditPolicy
            .MaintenanceCovenants({
                maxLeverageRatio: 4e18,
                minCoverageRatio: 2e18,
                minLiquidityAmount: 1_00_00_000,
                allowsDividends: false,
                reportingFrequencyDays: 90
            });
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature("CreditPolicy__PolicyFrozen(uint256)", 1)
        );
        creditPolicy.updateCovenants(1, covenants);
    }

    function testUpdateCovenantsRevertIfPolicyDontExist() public {
        CreditPolicy.MaintenanceCovenants memory covenants = CreditPolicy
            .MaintenanceCovenants({
                maxLeverageRatio: 4e18,
                minCoverageRatio: 2e18,
                minLiquidityAmount: 1_00_00_000,
                allowsDividends: false,
                reportingFrequencyDays: 90
            });
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.updateCovenants(1, covenants);
    }

    function testUnAuthorizedUpdateCovenants() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        CreditPolicy.MaintenanceCovenants memory covenants = CreditPolicy
            .MaintenanceCovenants({
                maxLeverageRatio: 4e18,
                minCoverageRatio: 2e18,
                minLiquidityAmount: 1_00_00_000,
                allowsDividends: false,
                reportingFrequencyDays: 90
            });
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.updateCovenants(1, covenants);
    }

    function testUpdateCovenants() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        CreditPolicy.MaintenanceCovenants memory covenants = CreditPolicy
            .MaintenanceCovenants({
                maxLeverageRatio: 4e18,
                minCoverageRatio: 2e18,
                minLiquidityAmount: 1_00_00_000,
                allowsDividends: false,
                reportingFrequencyDays: 90
            });
        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.PolicyCovenantsUpdated(1, block.timestamp);
        creditPolicy.updateCovenants(1, covenants);
    }

    function testSetLoanTierRevertsIfNotAdmin() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        CreditPolicy.LoanTier memory tier = CreditPolicy.LoanTier({
            name: "Tier 1",
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

        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.setLoanTier(1, 1, tier);
    }

    function testSetLoanTierRevertsIfPolicyDontExist() public {
        CreditPolicy.LoanTier memory tier = CreditPolicy.LoanTier({
            name: "Tier 1",
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

        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.setLoanTier(1, 1, tier);
    }

    function testSetLoanTierRevertsIfPolicyIsFrozen() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        vm.prank(deployer);
        creditPolicy.freezePolicy(1);
        CreditPolicy.LoanTier memory tier = CreditPolicy.LoanTier({
            name: "Tier 1",
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

        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature("CreditPolicy__PolicyFrozen(uint256)", 1)
        );
        creditPolicy.setLoanTier(1, 1, tier);
    }

    function testSetLoanTier() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        CreditPolicy.LoanTier memory tier = CreditPolicy.LoanTier({
            name: "Tier 1",
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

        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.LoanTierUpdated(1, 1, block.timestamp);
        creditPolicy.setLoanTier(1, 1, tier);
    }

    function testExcludeIndustryRevertsIfNotAdmin() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.excludeIndustry(1, bytes32("IndustryA"));
    }

    function testMultipleTierManagement() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);

        vm.startPrank(deployer);

        for (uint8 i = 0; i < 5; i++) {
            CreditPolicy.LoanTier memory tier = createMockTier(
                string(abi.encodePacked("Tier ", i))
            );
            creditPolicy.setLoanTier(1, i, tier);
        }

        assertEq(creditPolicy.totalTiers(1), 5);

        CreditPolicy.LoanTier memory tier6 = createMockTier("Tier 6");
        creditPolicy.setLoanTier(1, 6, tier6);

        assertEq(creditPolicy.totalTiers(1), 7);

        vm.stopPrank();
    }

    function testExcludeIndustryRevertsIfPolicyDontExist() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.excludeIndustry(1, bytes32("IndustryA"));
    }

    function testExcludeIndustryRevertsIfPolicyIsFrozen() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        vm.prank(deployer);
        creditPolicy.freezePolicy(1);
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature("CreditPolicy__PolicyFrozen(uint256)", 1)
        );
        creditPolicy.excludeIndustry(1, bytes32("IndustryA"));
    }

    function testExcludeIndustryUnitTest() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.IndustryExcluded(
            1,
            bytes32("IndustryA"),
            block.timestamp
        );
        creditPolicy.excludeIndustry(1, bytes32("IndustryA"));
    }

    // Verify industry exclusion state
    function testIndustryExclusionState() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);

        bytes32 industry = keccak256("Manufacturing");

        assertEq(creditPolicy.excludedIndustries(1, industry), false);

        vm.prank(deployer);
        creditPolicy.excludeIndustry(1, industry);
        assertEq(creditPolicy.excludedIndustries(1, industry), true);

        vm.prank(deployer);
        creditPolicy.includeIndustry(1, industry);
        assertEq(creditPolicy.excludedIndustries(1, industry), false);
    }

    function testIncludeIndustryRevertsIfNotAdmin() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.includeIndustry(1, bytes32("IndustryA"));
    }

    function testIncludeIndustryRevertsIfPolicyDontExist() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.includeIndustry(1, bytes32("IndustryA"));
    }

    function testMultipleIndustryExclusions() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);

        bytes32[] memory industries = new bytes32[](3);
        industries[0] = keccak256("Gambling");
        industries[1] = keccak256("Tobacco");
        industries[2] = keccak256("Cannabis");

        vm.startPrank(deployer);
        for (uint i = 0; i < industries.length; i++) {
            creditPolicy.excludeIndustry(1, industries[i]);
        }
        vm.stopPrank();

        // Verify all are excluded
        for (uint i = 0; i < industries.length; i++) {
            assertTrue(creditPolicy.excludedIndustries(1, industries[i]));
        }
    }

    function testIncludeIndustryRevertsIfPolicyIsFrozen() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        vm.prank(deployer);
        creditPolicy.freezePolicy(1);
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature("CreditPolicy__PolicyFrozen(uint256)", 1)
        );
        creditPolicy.includeIndustry(1, bytes32("IndustryA"));
    }

    // Test totalTiers increments correctly
    function testSetLoanTierIncrementsTotalTiers() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);

        CreditPolicy.LoanTier memory tier1 = createMockTier("Tier 1");
        CreditPolicy.LoanTier memory tier2 = createMockTier("Tier 2");

        vm.startPrank(deployer);
        creditPolicy.setLoanTier(1, 0, tier1);
        assertEq(creditPolicy.totalTiers(1), 1);

        creditPolicy.setLoanTier(1, 1, tier2);
        assertEq(creditPolicy.totalTiers(1), 2);

        // Update existing tier - totalTiers shouldn't change
        creditPolicy.setLoanTier(1, 0, tier1);
        assertEq(creditPolicy.totalTiers(1), 2);

        vm.stopPrank();
    }

    function testIncludeIndustryUnitTest() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        vm.prank(deployer);
        creditPolicy.excludeIndustry(1, bytes32("IndustryA"));
        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.IndustryIncluded(
            1,
            bytes32("IndustryA"),
            block.timestamp
        );
        creditPolicy.includeIndustry(1, bytes32("IndustryA"));
    }

    function testSetPolicyDocumentRevertsIfNotAdmin() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        vm.prank(seniorUser1);
        vm.expectRevert(CreditPolicy.CreditPolicy__Unauthorized.selector);
        creditPolicy.setPolicyDocument(
            1,
            bytes32("document"),
            "ipfs://policyDocHash"
        );
    }

    function testSetPolicyDocumentRevertsIfPolicyDontExist() public {
        vm.prank(deployer);
        vm.expectRevert(CreditPolicy.CreditPolicy__InvalidVersion.selector);
        creditPolicy.setPolicyDocument(
            1,
            bytes32("document"),
            "ipfs://policyDocHash"
        );
    }

    function testSetPolicyDocumentRevertsIfPolicyIsFrozen() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        vm.prank(deployer);
        creditPolicy.freezePolicy(1);
        vm.prank(deployer);
        vm.expectRevert(
            abi.encodeWithSignature("CreditPolicy__PolicyFrozen(uint256)", 1)
        );
        creditPolicy.setPolicyDocument(
            1,
            bytes32("document"),
            "ipfs://policyDocHash"
        );
    }

    function testPolicyVersionIsolation() public {
        vm.startPrank(deployer);
        creditPolicy.createPolicy(1);
        creditPolicy.createPolicy(2);

        // Exclude industry in version 1
        bytes32 industry = keccak256("Gambling");
        creditPolicy.excludeIndustry(1, industry);

        // Should only affect version 1, not version 2
        assertTrue(creditPolicy.excludedIndustries(1, industry));
        assertFalse(creditPolicy.excludedIndustries(2, industry));

        vm.stopPrank();
    }

    function testSetLoanTierStoresDataCorrectly() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);

        CreditPolicy.LoanTier memory tier = createMockTier("Premium Tier");
        tier.interestRateBps = 950; // Custom value

        vm.prank(deployer);
        creditPolicy.setLoanTier(1, 0, tier);

        (string memory name, , , , , , uint256 intRate, , , ) = creditPolicy
            .loanTiers(1, 0);

        assertEq(name, "Premium Tier");
        assertEq(intRate, 950);
    }

    function testUpdateAttestationStoresDataCorrectly() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);

        CreditPolicy.AttestationRequirements memory req = CreditPolicy
            .AttestationRequirements({
                maxAttestationAgeDays: 90,
                reAttestationFrequencyDays: 180,
                requiresCPAAttestation: true
            });

        vm.prank(deployer);
        creditPolicy.updateAttestation(1, req);

        (uint256 maxAge, uint256 freq, bool requiresCPA) = creditPolicy
            .attestation(1);
        assertEq(maxAge, 90);
        assertEq(freq, 180);
        assertTrue(requiresCPA);
    }

    function testUpdateCovenantsStoresDataCorrectly() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);

        CreditPolicy.MaintenanceCovenants memory cov = CreditPolicy
            .MaintenanceCovenants({
                maxLeverageRatio: 4e18,
                minCoverageRatio: 2e18,
                minLiquidityAmount: 1_00_00_000,
                allowsDividends: false,
                reportingFrequencyDays: 90
            });

        vm.prank(deployer);
        creditPolicy.updateCovenants(1, cov);

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

    function testEligibilityWithZeroValues() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);

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

    function testSetPolicyDocumentUnitTest() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);
        vm.prank(deployer);
        vm.expectEmit(true, false, false, true);
        emit CreditPolicy.PolicyDocumentSet(
            1,
            bytes32("document"),
            "ipfs://policyDocHash",
            block.timestamp
        );
        creditPolicy.setPolicyDocument(
            1,
            bytes32("document"),
            "ipfs://policyDocHash"
        );
    }

    // Verify document storage
    function testSetPolicyDocumentStoresCorrectly() public {
        vm.prank(deployer);
        creditPolicy.createPolicy(1);

        bytes32 docHash = keccak256("policyDocument");
        string memory uri = "ipfs://QmX...";

        vm.prank(deployer);
        creditPolicy.setPolicyDocument(1, docHash, uri);

        assertEq(creditPolicy.policyDocumentHash(1), docHash);
        assertEq(creditPolicy.policyDocumentURI(1), uri);
        assertEq(creditPolicy.lastUpdated(1), block.timestamp);
    }

    // Helper to create mock LoanTier
    function createMockTier(
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
}
