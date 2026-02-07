// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {LoanEngine} from "../../src/LoanEngine.sol";
import {TranchePool} from "../../src/TranchePool.sol";
import {CreditPolicy} from "../../src/CreditPolicy.sol";
import {MockLoanProofVerifier} from "../mocks/MockLoanProofVerifier.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";

// Simple contract that Medusa will fuzz directly
contract MedusaTest {
    LoanEngine public loanEngine;
    TranchePool public tranchePool;
    ERC20Mock public usdt;
    CreditPolicy public creditPolicy;
    
    uint256 public USDT = 1e18;
    address public deployer = address(0x999);
    address public recevingEntity = address(0x888);
    address public feeManager = address(0x777);
    
    // Users
    address[] public seniorUsers;
    address[] public juniorUsers;
    address[] public equityUsers;
    address[] public loanBorrowers;
    
    // Ghost variables for tracking
    uint256 public totalIdleValue;
    uint256 public totalDeployedValue;
    uint256 public totalLoss;
    uint256 public totalRecovered;
    uint256 public outStandingPrincipal;
    
    constructor() {
        // Setup contracts
        usdt = new ERC20Mock();
        tranchePool = new TranchePool(address(usdt));
        
        // Configure tranches
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
        
        // Setup credit policy
        creditPolicy = new CreditPolicy();
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
        
        // Setup loan engine
        MockLoanProofVerifier mockVerifier = new MockLoanProofVerifier();
        loanEngine = new LoanEngine(
            address(creditPolicy),
            address(mockVerifier),
            500,
            address(tranchePool),
            address(usdt)
        );
        loanEngine.setMaxOriginationFeeBps(500);
        tranchePool.setLoanEngine(address(loanEngine));
        
        // Whitelist entities
        loanEngine.setWhitelistedFeeManager(feeManager, true);
        loanEngine.setWhitelistedOffRampingEntity(recevingEntity, true);
        loanEngine.setWhitelistedRepaymentAgent(recevingEntity, true);
        loanEngine.setWhitelistedRecoveryAgent(recevingEntity, true);
        
        // Create and fund users
        for (uint160 i = 1; i <= 20; i++) {
            address user = address(i);
            seniorUsers.push(user);
            usdt.mint(user, 1_00_00_00000 * USDT);
            tranchePool.updateWhitelist(user, true);
        }
        
        for (uint160 i = 21; i <= 30; i++) {
            address user = address(i);
            juniorUsers.push(user);
            usdt.mint(user, 50_00_00_000 * USDT);
            tranchePool.updateWhitelist(user, true);
        }
        
        for (uint160 i = 31; i <= 35; i++) {
            address user = address(i);
            equityUsers.push(user);
            usdt.mint(user, 50_00_00_000 * USDT);
            tranchePool.updateEquityTrancheWhiteList(user, true);
        }
        
        for (uint160 i = 100; i < 120; i++) {
            loanBorrowers.push(address(i));
        }
        
        usdt.mint(recevingEntity, 50_00_00_000 * USDT);
    }
    
    // FUZZ FUNCTIONS - Medusa will call these
    
    function depositSenior(uint256 userSeed, uint256 amount) external {
        if (tranchePool.getPoolState() != TranchePool.PoolState.OPEN) return;
        
        address user = seniorUsers[userSeed % seniorUsers.length];
        amount = _bound(amount, 10_00_000 * USDT, 5_00_00_000 * USDT);
        
        if (amount > usdt.balanceOf(user)) return;
        
        // Deposit
        _impersonate(user);
        usdt.approve(address(tranchePool), amount);
        tranchePool.depositSeniorTranche(amount);
        _stopImpersonate();
        
        totalIdleValue += amount;
    }
    
    function depositJunior(uint256 userSeed, uint256 amount) external {
        if (tranchePool.getPoolState() != TranchePool.PoolState.OPEN) return;
        
        address user = juniorUsers[userSeed % juniorUsers.length];
        amount = _bound(amount, 50_00_000 * USDT, 3_00_00_000 * USDT);
        
        if (amount > usdt.balanceOf(user)) return;
        
        _impersonate(user);
        usdt.approve(address(tranchePool), amount);
        tranchePool.depositJuniorTranche(amount);
        _stopImpersonate();
        
        totalIdleValue += amount;
    }
    
    function depositEquity(uint256 userSeed, uint256 amount) external {
        if (tranchePool.getPoolState() != TranchePool.PoolState.OPEN) return;
        
        address user = equityUsers[userSeed % equityUsers.length];
        amount = _bound(amount, 1_00_00_000 * USDT, 2_00_00_000 * USDT);
        
        if (amount > usdt.balanceOf(user)) return;
        
        _impersonate(user);
        usdt.approve(address(tranchePool), amount);
        tranchePool.depositEquityTranche(amount);
        _stopImpersonate();
        
        totalIdleValue += amount;
    }
    
    function commitPool() external {
        if (tranchePool.getPoolState() == TranchePool.PoolState.OPEN && 
            tranchePool.getTotalIdleValue() > 0) {
            tranchePool.setPoolState(TranchePool.PoolState.COMMITED);
        }
    }
    
    function createAndActivateLoan(uint256 principalSeed, uint256 borrowerSeed) external {
        if (tranchePool.getPoolState() != TranchePool.PoolState.COMMITED &&
            tranchePool.getPoolState() != TranchePool.PoolState.DEPLOYED) return;
        
        if (tranchePool.getTotalIdleValue() < 10_00_000 * USDT) return;
        
        uint256 principal = _bound(principalSeed, 10_00_000 * USDT, 
            _min(2_00_00_000 * USDT, tranchePool.getTotalIdleValue()));
        
        address borrower = loanBorrowers[borrowerSeed % loanBorrowers.length];
        bytes32 commitment = keccak256(abi.encodePacked(borrower, borrowerSeed));
        
        uint256 loanId = loanEngine.getNextLoanId();
        bytes32 nullifier = keccak256(abi.encode(loanId, borrowerSeed, commitment, block.timestamp));
        bytes memory proof = abi.encodePacked(loanId, borrowerSeed, principal);
        
        // Create loan
        loanEngine.createLoan(
            commitment,
            nullifier,
            1, // policyVersion
            1, // tierIndex
            principal,
            500, // interestRateBps
            100, // originationFeeBps
            365, // termDays
            bytes32(0), // industry
            proof,
            new bytes32[](0)
        );
        
        // Activate immediately
        loanEngine.activateLoan(loanId, recevingEntity, feeManager);
        
        totalDeployedValue += principal;
        totalIdleValue -= principal;
        outStandingPrincipal += principal;
    }
    
    function repayLoan(uint256 loanSeed, uint256 percentToRepay) external {
        if (loanEngine.getNextLoanId() == 1) return;
        
        uint256 loanId = _bound(loanSeed, 1, loanEngine.getNextLoanId() - 1);
        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);
        
        if (loan.state != LoanEngine.LoanState.ACTIVE) return;
        if (loan.principalOutstanding == 0) return;
        
        percentToRepay = _bound(percentToRepay, 10, 100); // 10% to 100%
        uint256 principalAmount = (loan.principalOutstanding * percentToRepay) / 100;
        uint256 interestAmount = loan.interestAccrued;
        
        uint256 totalAmount = principalAmount + interestAmount;
        
        _impersonate(recevingEntity);
        usdt.approve(address(loanEngine), totalAmount);
        _stopImpersonate();
        
        loanEngine.repayLoan(loanId, principalAmount, interestAmount, recevingEntity);
        
        totalDeployedValue -= principalAmount;
        totalIdleValue += principalAmount;
        outStandingPrincipal -= principalAmount;
    }
    
    function writeOffLoan(uint256 loanSeed) external {
        if (loanEngine.getNextLoanId() == 1) return;
        
        uint256 loanId = _bound(loanSeed, 1, loanEngine.getNextLoanId() - 1);
        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);
        
        if (loan.state != LoanEngine.LoanState.ACTIVE) return;
        
        // Declare default first
        loanEngine.declareDefault(loanId, keccak256("default"));
        
        // Then write off
        uint256 principal = loanEngine.getLoanDetails(loanId).principalOutstanding;
        loanEngine.writeOffLoan(loanId);
        
        totalDeployedValue -= principal;
        outStandingPrincipal -= principal;
        totalLoss += principal;
    }
    
    // INVARIANTS - Medusa will check these
    
    function invariant_totalValueBalance() external view returns (bool) {
        return (tranchePool.getTotalIdleValue() + tranchePool.getTotalDeployedValue()) ==
               (tranchePool.getTotalDeposited() - tranchePool.getTotalLoss() + tranchePool.getTotalRecovered());
    }
    
    function invariant_deployedMatchesOutstanding() external view returns (bool) {
        return outStandingPrincipal == tranchePool.getTotalDeployedValue();
    }
    
    function invariant_principalIntegrity() external view returns (bool) {
        uint256 totalPrincipal = 0;
        uint256 nextId = loanEngine.getNextLoanId();
        
        for (uint256 i = 1; i < nextId; i++) {
            LoanEngine.Loan memory loan = loanEngine.getLoanDetails(i);
            totalPrincipal += loan.principalOutstanding;
        }
        
        return totalPrincipal == tranchePool.getTotalDeployedValue();
    }
    
    // HELPER FUNCTIONS
    
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
    
    function _bound(uint256 x, uint256 min, uint256 max) internal pure returns (uint256) {
        if (x < min) return min;
        if (x > max) return max;
        return x;
    }
    
    function _min(uint256 a, uint256 b) internal pure returns (uint256) {
        return a < b ? a : b;
    }
    
    // Mock vm.prank functionality
    address private currentCaller;
    
    function _impersonate(address who) internal {
        currentCaller = who;
        // In real Medusa, you'd use assembly or actual prank
    }
    
    function _stopImpersonate() internal {
        currentCaller = address(0);
    }
}