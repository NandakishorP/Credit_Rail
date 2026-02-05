// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {LoanEngine} from "../../../src/LoanEngine.sol";
import {TranchePool} from "../../../src/TranchePool.sol";
import {CreditPolicy} from "../../../src/CreditPolicy.sol";
import {MockLoanProofVerifier} from "../../mocks/MockLoanProofVerifier.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {Handler} from "./Handler.t.sol";

/// @notice Medusa-specific invariant test contract
contract MedusaInvariantTest {
    Handler public handler;
    TranchePool public tranchePool;
    LoanEngine public loanEngine;
    
    constructor() {
        // Deploy infrastructure (your existing code)
        address deployer = address(0x41414141);
        ERC20Mock usdt = new ERC20Mock();
        uint256 USDT = 1e18;
        
        tranchePool = new TranchePool(address(usdt));
        tranchePool.setMaxAllocationCapSeniorTranche(5_00_00_000 * USDT);
        tranchePool.setMaxAllocationCapJuniorTranche(3_00_00_000 * USDT);
        tranchePool.setMaxAllocationCapEquityTranche(2_00_00_000 * USDT);
        tranchePool.setMinimumDepositAmountSeniorTranche(10_00_000 * USDT);
        tranchePool.setMinimumDepositAmountJuniorTranche(50_00_000 * USDT);
        tranchePool.setMinimumDepositAmountEquityTranche(1_00_00_000 * USDT);
        tranchePool.setTrancheCapitalAllocationFactorJunior(15);
        tranchePool.setTrancheCapitalAllocationFactorSenior(80);
        tranchePool.setSeniorAPR(8);
        tranchePool.setTargetJuniorAPR(15);

        CreditPolicy creditPolicy = new CreditPolicy();
        creditPolicy.setMaxTiers(3);
        creditPolicy.createPolicy(1);
        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        creditPolicy.updateRatios(1, _createFinancialRatios());
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
        creditPolicy.setLoanTier(1, 1, _createMockTier("Tier 1"));
        creditPolicy.setPolicyDocument(1, keccak256(bytes("document")), "ipfs://policyDocHash");
        creditPolicy.freezePolicy(1);

        MockLoanProofVerifier mockLoanProofVerifier = new MockLoanProofVerifier();
        loanEngine = new LoanEngine(
            address(creditPolicy),
            address(mockLoanProofVerifier),
            500,
            address(tranchePool),
            address(usdt)
        );
        loanEngine.setMaxOriginationFeeBps(500);
        tranchePool.setLoanEngine(address(loanEngine));

        handler = new Handler(loanEngine, tranchePool, creditPolicy, usdt);
    }

    // =====================================================================
    // MEDUSA ENTRY POINTS - Public functions that Medusa will call
    // =====================================================================
    
    function depositSeniorTranche(uint256 userIndex, uint256 amount) public {
        handler.depositSeniorTranche(userIndex, amount);
    }

    function depositJuniorTranche(uint256 userIndex, uint256 amount) public {
        handler.depositJuniorTranche(userIndex, amount);
    }

    function depositEquityTranche(uint256 userIndex, uint256 amount) public {
        handler.depositEquityTranche(userIndex, amount);
    }

    function maybeCommitPool() public {
        handler.maybeCommitPool();
    }

    function createLoan(
        uint256 principalIssued,
        uint256 originationFeeBps,
        uint256 termDays,
        uint256 userIndex
    ) public {
        handler.createLoan(principalIssued, originationFeeBps, termDays, userIndex);
    }

    function activateLoan(uint256 loanId) public {
        handler.activateLoan(loanId);
    }

    function repayLoan(
        uint256 loanId,
        uint256 principalAmount,
        uint256 interestAmount
    ) public {
        handler.repayLoan(loanId, principalAmount, interestAmount);
    }

    function maybeDeclareDefault(uint256 loanId, bytes32 reasonHash) public {
        handler.maybeDeclareDefault(loanId, reasonHash);
    }

    function maybeWriteOffLoan(uint256 loanId) public {
        handler.maybeWriteOffLoan(loanId);
    }

    function maybeRecoverLoan(
        uint256 loanId,
        uint256 amount,
        uint256 agentIndex
    ) public {
        handler.maybeRecoverLoan(loanId, amount, agentIndex);
    }

    function warpTime(uint256 daysToWarp) public {
        handler.warpTime(daysToWarp);
    }

    // =====================================================================
    // INVARIANTS - Medusa checks these after each call sequence
    // =====================================================================
    
    function invariant_outstandingPrincipalMatchesDeployed() public view {
        assert(handler.outStandingPrincipal() == tranchePool.getTotalDeployedValue());
    }

    function invariant_totalValueConservation() public view {
        uint256 idleAndDeployed = tranchePool.getTotalIdleValue() + tranchePool.getTotalDeployedValue();
        uint256 expected = tranchePool.getTotalDeposited() - tranchePool.getTotalLoss() + tranchePool.getTotalRecovered();
        assert(idleAndDeployed == expected);
    }

    // Helper functions (your existing code)
    function _createEligibilityCriteria() internal pure returns (CreditPolicy.EligibilityCriteria memory) {
        return CreditPolicy.EligibilityCriteria({
            minAnnualRevenue: 1_00_00_000,
            minEBITDA: 10_00_000,
            minTangibleNetWorth: 5_00_00_000,
            minBusinessAgeDays: 180,
            maxDefaultsLast36Months: 0,
            bankruptcyExcluded: true
        });
    }

    function _createFinancialRatios() internal pure returns (CreditPolicy.FinancialRatios memory) {
        return CreditPolicy.FinancialRatios({
            maxTotalDebtToEBITDA: 4e18,
            minInterestCoverageRatio: 2e18,
            minCurrentRatio: 1e18,
            minEBITDAMarginBps: 1500
        });
    }

    function _createConcentrationLimits() internal pure returns (CreditPolicy.ConcentrationLimits memory) {
        return CreditPolicy.ConcentrationLimits({
            maxSingleBorrowerBps: 1000,
            maxIndustryConcentrationBps: 3000
        });
    }

    function _createAttestationRequirements() internal pure returns (CreditPolicy.AttestationRequirements memory) {
        return CreditPolicy.AttestationRequirements({
            maxAttestationAgeDays: 90,
            reAttestationFrequencyDays: 180,
            requiresCPAAttestation: true
        });
    }

    function _createMaintenanceCovenants() internal pure returns (CreditPolicy.MaintenanceCovenants memory) {
        return CreditPolicy.MaintenanceCovenants({
            maxLeverageRatio: 4e18,
            minCoverageRatio: 2e18,
            minLiquidityAmount: 1_00_00_000,
            allowsDividends: false,
            reportingFrequencyDays: 90
        });
    }

    function _createMockTier(string memory name) internal pure returns (CreditPolicy.LoanTier memory) {
        return CreditPolicy.LoanTier({
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