// SPDX-License-Identifier: MIT
pragma solidity ^0.8.30;

import {LoanEngine} from "../src/LoanEngine.sol";
import {Test} from "forge-std/Test.sol";
import {TranchePool} from "../src/TranchePool.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {CreditPolicy} from "../src/CreditPolicy.sol";
import {MockLoanProofVerifier} from "./mocks/MockLoanProofVerifier.sol";

contract TestLoanEngine is Test {
    TranchePool tranchePool;
    ERC20Mock usdt;
    LoanEngine loanEngine;
    address deployer = makeAddr("deployer");
    address seniorUser1 = makeAddr("seniorUser1");
    CreditPolicy creditPolicy;
    uint256 public USDT = 1e18;

    function setUp() public {
        usdt = new ERC20Mock();
        vm.startPrank(deployer);
        MockLoanProofVerifier verifier = new MockLoanProofVerifier();
        tranchePool = new TranchePool(address(usdt));
        tranchePool.setMaxAllocationCapSeniorTranche(13_00_00_000 * USDT);
        tranchePool.setMinimumDepositAmountSeniorTranche(5_00_000 * USDT);
        tranchePool.updateWhitelist(seniorUser1, true);
        creditPolicy = new CreditPolicy();

        _createPolicy(1);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        creditPolicy.updateRatios(1, _createFinancialRatios());
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
        creditPolicy.setLoanTier(1, 1, _createMockTier("Tier 1"));
        _freezePolicy(1);
        loanEngine = new LoanEngine(
            address(creditPolicy),
            address(verifier),
            500,
            address(tranchePool),
            address(usdt)
        );
        vm.stopPrank();

        ERC20Mock(usdt).mint(seniorUser1, 10_00_00_000 * 1e18);
    }

    function _createPolicy(uint256 version) internal {
        creditPolicy.createPolicy(version);
    }

    function _freezePolicy(uint256 version) internal {
        creditPolicy.freezePolicy(version);
    }

    function _createAndFreezePolicy(uint256 version) internal {
        _createPolicy(version);
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
}
