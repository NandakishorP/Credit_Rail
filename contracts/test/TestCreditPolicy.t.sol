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

    function testCreatePolicy() public {
        vm.prank(deployer);
        vm.expectEmit(true, true, false, true);
        emit CreditPolicy.PolicyCreated(1, block.timestamp);
        creditPolicy.createPolicy(1);
        assertEq(creditPolicy.policyCreated(1), true);
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
}
