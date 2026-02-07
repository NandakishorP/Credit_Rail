// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {LoanEngine} from "../../../src/LoanEngine.sol";
import {TranchePool} from "../../../src/TranchePool.sol";
import {CreditPolicy} from "../../../src/CreditPolicy.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {MockLoanProofVerifier} from "../../mocks/MockLoanProofVerifier.sol";

/**
 * @title EchidnaHandler
 * @notice Echidna-compatible handler with proper bounds for permissioned DeFi
 * @dev No Foundry cheatcodes - this contract is its own deployer/owner
 * 
 * Key bounds (matching Handler.t.sol):
 * - minimumLoanPrincipal: 1,000,000 USDT (1M)
 * - maximumLoanPrincipal: 20,000,000 USDT (20M)
 * - minimumOriginationFeeBps: 50 (0.5%)
 * - minimumTermDays: 180
 * - maximumTermDays: 480
 * - Deposits: use contract's min/max values
 */
contract EchidnaHandler {
    // =========================================================================
    // STATE
    // =========================================================================
    
    LoanEngine public loanEngine;
    TranchePool public tranchePool;
    ERC20Mock public usdt;
    CreditPolicy public creditPolicy;
    MockLoanProofVerifier public verifier;
    
    // Constants (matching Handler.t.sol)
    uint256 public constant USDT = 1e18;
    uint256 public constant MINIMUM_LOAN_PRINCIPAL = 10_00_000 * USDT;  // 1M USDT
    uint256 public constant MAXIMUM_LOAN_PRINCIPAL = 2_00_00_000 * USDT; // 20M USDT
    uint256 public constant MINIMUM_ORIGINATION_FEE_BPS = 50;  // 0.5%
    uint256 public constant MINIMUM_TERM_DAYS = 180;
    uint256 public constant MAXIMUM_TERM_DAYS = 480;
    uint256 public constant MAX_ORIGINATION_FEE_BPS = 500;  // 5%
    
    // Initial funding to ensure minimums can be met
    uint256 public constant INITIAL_SENIOR_DEPOSIT = 80_00_00_000 * USDT;  // 800M USDT
    uint256 public constant INITIAL_JUNIOR_DEPOSIT = 50_00_00_000 * USDT;  // 500M USDT
    uint256 public constant INITIAL_EQUITY_DEPOSIT = 100_00_00_000 * USDT; // 1B USDT
    
    // Ghost variables for invariants
    uint256 public outstandingPrincipal;
    
    // =========================================================================
    // CONSTRUCTOR
    // =========================================================================
    
    constructor() {
        // Deploy mock token
        usdt = new ERC20Mock();
        
        // Deploy TranchePool
        tranchePool = new TranchePool(address(usdt));
        
        // Deploy MockLoanProofVerifier
        verifier = new MockLoanProofVerifier();
        
        // Deploy CreditPolicy and set it up
        creditPolicy = new CreditPolicy();
        _setupCreditPolicy();
        
        // Deploy LoanEngine with correct constructor signature
        // constructor(creditPolicy, verifier, maxOriginationFee, tranchePool, stablecoin)
        loanEngine = new LoanEngine(
            address(creditPolicy),
            address(verifier),
            MAX_ORIGINATION_FEE_BPS,
            address(tranchePool),
            address(usdt)
        );
        
        // Setup: This contract IS the owner, no vm.prank needed
        tranchePool.setLoanEngine(address(loanEngine));
        
        // Whitelist this contract for all operations
        loanEngine.setWhitelistedFeeManager(address(this), true);
        loanEngine.setWhitelistedOffRampingEntity(address(this), true);
        loanEngine.setWhitelistedRepaymentAgent(address(this), true);
        loanEngine.setWhitelistedRecoveryAgent(address(this), true);
        tranchePool.updateWhitelist(address(this), true);
        tranchePool.updateEquityTrancheWhiteList(address(this), true);
        
        // Configure tranche caps (required before deposits)
        tranchePool.setMaxAllocationCapSeniorTranche(INITIAL_SENIOR_DEPOSIT);
        tranchePool.setMaxAllocationCapJuniorTranche(INITIAL_JUNIOR_DEPOSIT);
        tranchePool.setMaxAllocationCapEquityTranche(INITIAL_EQUITY_DEPOSIT);
        
        // Mint USDT for operations (large amount for institutional scale)
        usdt.mint(address(this), 500_00_00_000 * USDT);  // 5B USDT
        
        // Initial deposits to ensure pool has liquidity
        _initialDeposits();
    }
    
    function _setupCreditPolicy() internal {
        // Create policy version 1
        creditPolicy.createPolicy(1);
        
        // Set max tiers first
        creditPolicy.setMaxTiers(10);
        
        // Update eligibility
        creditPolicy.updateEligibility(
            1,
            CreditPolicy.EligibilityCriteria({
                minAnnualRevenue: 1_00_00_000,
                minEBITDA: 10_00_000,
                minTangibleNetWorth: 5_00_00_000,
                minBusinessAgeDays: 180,
                maxDefaultsLast36Months: 0,
                bankruptcyExcluded: true
            })
        );
        
        // Update financial ratios
        creditPolicy.updateRatios(
            1,
            CreditPolicy.FinancialRatios({
                maxTotalDebtToEBITDA: 4e18,
                minInterestCoverageRatio: 2e18,
                minCurrentRatio: 1e18,
                minEBITDAMarginBps: 1500
            })
        );
        
        // Update concentration limits
        creditPolicy.updateConcentration(
            1,
            CreditPolicy.ConcentrationLimits({
                maxSingleBorrowerBps: 1000,
                maxIndustryConcentrationBps: 3000
            })
        );
        
        // Update attestation requirements
        creditPolicy.updateAttestation(
            1,
            CreditPolicy.AttestationRequirements({
                maxAttestationAgeDays: 90,
                reAttestationFrequencyDays: 180,
                requiresCPAAttestation: true
            })
        );
        
        // Update maintenance covenants
        creditPolicy.updateCovenants(
            1,
            CreditPolicy.MaintenanceCovenants({
                maxLeverageRatio: 4e18,
                minCoverageRatio: 2e18,
                minLiquidityAmount: 1_00_00_000,
                allowsDividends: false,
                reportingFrequencyDays: 90
            })
        );
        
        // Set loan tier
        creditPolicy.setLoanTier(
            1,
            1,  // tierId
            CreditPolicy.LoanTier({
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
            })
        );
        
        // Set policy document
        creditPolicy.setPolicyDocument(
            1,
            keccak256("document"),
            "ipfs://policyDocHash"
        );
        
        // Freeze policy
        creditPolicy.freezePolicy(1);
    }
    
    function _initialDeposits() internal {
        // Senior tranche deposit
        uint256 seniorMin = tranchePool.getSeniorTrancheMinimumDepositAmount();
        uint256 seniorMax = tranchePool.getSeniorTrancheMaxDepositCap();
        uint256 seniorDeposit = _min(INITIAL_SENIOR_DEPOSIT, seniorMax);
        seniorDeposit = _max(seniorDeposit, seniorMin);
        
        usdt.approve(address(tranchePool), seniorDeposit);
        tranchePool.depositSeniorTranche(seniorDeposit);
        
        // Junior tranche deposit
        uint256 juniorMin = tranchePool.getJuniorTrancheMinimumDepositAmount();
        uint256 juniorMax = tranchePool.getJuniorTrancheMaxDepositCap();
        uint256 juniorDeposit = _min(INITIAL_JUNIOR_DEPOSIT, juniorMax);
        juniorDeposit = _max(juniorDeposit, juniorMin);
        
        usdt.approve(address(tranchePool), juniorDeposit);
        tranchePool.depositJuniorTranche(juniorDeposit);
        
        // Equity tranche deposit
        uint256 equityMin = tranchePool.getEquityTrancheMinimumDepositAmount();
        uint256 equityMax = tranchePool.getEquityTrancheMaxDepositCap();
        uint256 equityDeposit = _min(INITIAL_EQUITY_DEPOSIT, equityMax);
        equityDeposit = _max(equityDeposit, equityMin);
        
        usdt.approve(address(tranchePool), equityDeposit);
        tranchePool.depositEquityTranche(equityDeposit);
    }
    
    // =========================================================================
    // BOUND HELPER (Echidna-compatible)
    // =========================================================================
    
    function _bound(uint256 x, uint256 min, uint256 max) internal pure returns (uint256) {
        if (min > max) return min;
        if (x < min) return min;
        if (x > max) return max;
        return min + (x % (max - min + 1));
    }
    
    function _min(uint256 a, uint256 b) internal pure returns (uint256) {
        return a < b ? a : b;
    }
    
    function _max(uint256 a, uint256 b) internal pure returns (uint256) {
        return a > b ? a : b;
    }
    
    // =========================================================================
    // DEPOSIT FUNCTIONS (with proper bounds)
    // =========================================================================
    
    function depositSeniorTranche(uint256 amount) public {
        if (tranchePool.getPoolState() != TranchePool.PoolState.OPEN) return;
        
        uint256 minDeposit = tranchePool.getSeniorTrancheMinimumDepositAmount();
        uint256 maxDeposit = tranchePool.getSeniorTrancheMaxDepositCap();
        uint256 currentValue = tranchePool.getSeniorTrancheIdleValue() + 
                               tranchePool.getSeniorTrancheDeployedValue();
        
        if (currentValue >= maxDeposit) return;
        
        uint256 remaining = maxDeposit - currentValue;
        amount = _bound(amount, minDeposit, _min(remaining, maxDeposit));
        
        if (amount < minDeposit) return;
        
        usdt.approve(address(tranchePool), amount);
        try tranchePool.depositSeniorTranche(amount) {} catch {}
    }
    
    function depositJuniorTranche(uint256 amount) public {
        if (tranchePool.getPoolState() != TranchePool.PoolState.OPEN) return;
        
        uint256 minDeposit = tranchePool.getJuniorTrancheMinimumDepositAmount();
        uint256 maxDeposit = tranchePool.getJuniorTrancheMaxDepositCap();
        uint256 currentValue = tranchePool.getJuniorTrancheIdleValue() + 
                               tranchePool.getJuniorTrancheDeployedValue();
        
        if (currentValue >= maxDeposit) return;
        
        uint256 remaining = maxDeposit - currentValue;
        amount = _bound(amount, minDeposit, _min(remaining, maxDeposit));
        
        if (amount < minDeposit) return;
        
        usdt.approve(address(tranchePool), amount);
        try tranchePool.depositJuniorTranche(amount) {} catch {}
    }
    
    function depositEquityTranche(uint256 amount) public {
        if (tranchePool.getPoolState() != TranchePool.PoolState.OPEN) return;
        
        uint256 minDeposit = tranchePool.getEquityTrancheMinimumDepositAmount();
        uint256 maxDeposit = tranchePool.getEquityTrancheMaxDepositCap();
        uint256 currentValue = tranchePool.getEquityTrancheIdleValue() + 
                               tranchePool.getEquityTrancheDeployedValue();
        
        if (currentValue >= maxDeposit) return;
        
        uint256 remaining = maxDeposit - currentValue;
        amount = _bound(amount, minDeposit, _min(remaining, maxDeposit));
        
        if (amount < minDeposit) return;
        
        usdt.approve(address(tranchePool), amount);
        try tranchePool.depositEquityTranche(amount) {} catch {}
    }
    
    // =========================================================================
    // POOL STATE TRANSITIONS
    // =========================================================================
    
    function commitPool() public {
        if (tranchePool.getPoolState() != TranchePool.PoolState.OPEN) return;
        if (tranchePool.getTotalIdleValue() == 0) return;
        
        try tranchePool.setPoolState(TranchePool.PoolState.COMMITED) {} catch {}
    }
    
    function closePool() public {
        if (tranchePool.getTotalDeployedValue() > 0) return;
        if (tranchePool.getPoolState() != TranchePool.PoolState.DEPLOYED) return;
        
        try tranchePool.setPoolState(TranchePool.PoolState.CLOSED) {} catch {}
    }
    
    // =========================================================================
    // LOAN LIFECYCLE (with proper bounds)
    // =========================================================================
    
    function createLoan(uint256 principalIssued, uint256 originationFeeBps, uint256 termDays) public {
        TranchePool.PoolState state = tranchePool.getPoolState();
        if (state != TranchePool.PoolState.COMMITED && state != TranchePool.PoolState.DEPLOYED) return;
        
        uint256 idleValue = tranchePool.getTotalIdleValue();
        if (idleValue < MINIMUM_LOAN_PRINCIPAL) return;
        
        // Bound principal: 1M - min(20M, idle/10)
        // Reserve 90% of pool - only deploy up to 10% per loan
        uint256 maxForThisLoan = _min(MAXIMUM_LOAN_PRINCIPAL, idleValue / 10);
        if (maxForThisLoan < MINIMUM_LOAN_PRINCIPAL) {
            maxForThisLoan = _min(MINIMUM_LOAN_PRINCIPAL, idleValue);
        }
        
        principalIssued = _bound(principalIssued, MINIMUM_LOAN_PRINCIPAL, maxForThisLoan);
        
        if (principalIssued > idleValue) return;
        
        // Bound origination fee
        originationFeeBps = _bound(
            originationFeeBps,
            MINIMUM_ORIGINATION_FEE_BPS,
            MAX_ORIGINATION_FEE_BPS
        );
        
        // Bound term days
        termDays = _bound(termDays, MINIMUM_TERM_DAYS, MAXIMUM_TERM_DAYS);
        
        // Check policy is frozen
        if (!creditPolicy.isPolicyFrozen(1)) return;
        
        bytes32 borrowerCommitment = keccak256(abi.encodePacked(block.timestamp, principalIssued));
        bytes32 nullifierHash = keccak256(abi.encodePacked(borrowerCommitment, termDays));
        
        try loanEngine.createLoan(
            borrowerCommitment,
            nullifierHash,
            1,  // policyVersion
            1,  // tierId
            principalIssued,
            800,  // aprBps (8%)
            originationFeeBps,
            termDays,
            bytes32(0),  // industry
            "",  // proofData
            new bytes32[](0)  // publicInputs
        ) {} catch {}
    }
    
    function activateLoan(uint256 loanId) public {
        if (loanEngine.getNextLoanId() <= 1) return;
        loanId = _bound(loanId, 1, loanEngine.getNextLoanId() - 1);
        
        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);
        if (loan.state != LoanEngine.LoanState.CREATED) return;
        
        TranchePool.PoolState poolState = tranchePool.getPoolState();
        if (poolState != TranchePool.PoolState.COMMITED && poolState != TranchePool.PoolState.DEPLOYED) return;
        
        if (loan.principalIssued > tranchePool.getTotalIdleValue()) return;
        
        try loanEngine.activateLoan(loanId, address(this), address(this)) {
            outstandingPrincipal += loan.principalIssued;
        } catch {}
    }
    
    function repayLoan(uint256 loanId, uint256 principalAmount, uint256 interestAmount) public {
        if (loanEngine.getNextLoanId() <= 1) return;
        loanId = _bound(loanId, 1, loanEngine.getNextLoanId() - 1);
        
        LoanEngine.Loan memory loanBefore = loanEngine.getLoanDetails(loanId);
        if (loanBefore.state != LoanEngine.LoanState.ACTIVE) return;
        
        // Bound to realistic amounts
        principalAmount = _bound(principalAmount, 0, loanBefore.principalOutstanding);
        interestAmount = _bound(interestAmount, 0, loanBefore.interestAccrued);
        
        uint256 total = principalAmount + interestAmount;
        if (total == 0) return;
        
        // Interest before principal rule
        if (principalAmount > 0 && interestAmount == 0 && loanBefore.interestAccrued > 0) return;
        
        usdt.approve(address(loanEngine), total);
        try loanEngine.repayLoan(loanId, principalAmount, interestAmount, address(this)) {
            // Track ACTUAL principal change (LoanEngine may swap interest/principal)
            LoanEngine.Loan memory loanAfter = loanEngine.getLoanDetails(loanId);
            uint256 actualPrincipalRepaid = loanBefore.principalOutstanding - loanAfter.principalOutstanding;
            if (actualPrincipalRepaid > 0) outstandingPrincipal -= actualPrincipalRepaid;
        } catch {}
    }
    
    function declareDefault(uint256 loanId) public {
        if (loanEngine.getNextLoanId() <= 1) return;
        loanId = _bound(loanId, 1, loanEngine.getNextLoanId() - 1);
        
        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);
        if (loan.state != LoanEngine.LoanState.ACTIVE) return;
        
        try loanEngine.declareDefault(loanId, bytes32(0)) {} catch {}
    }
    
    function writeOffLoan(uint256 loanId) public {
        if (loanEngine.getNextLoanId() <= 1) return;
        loanId = _bound(loanId, 1, loanEngine.getNextLoanId() - 1);
        
        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);
        if (loan.state != LoanEngine.LoanState.DEFAULTED) return;
        
        uint256 principal = loan.principalOutstanding;
        
        try loanEngine.writeOffLoan(loanId) {
            outstandingPrincipal -= principal;
        } catch {}
    }
    
    function recoverLoan(uint256 loanId, uint256 amount) public {
        if (loanEngine.getNextLoanId() <= 1) return;
        loanId = _bound(loanId, 1, loanEngine.getNextLoanId() - 1);
        
        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);
        if (loan.state != LoanEngine.LoanState.WRITTEN_OFF) return;
        
        // Recovery bounded to principal issued (realistic - no over-recovery)
        uint256 maxRecovery = loan.principalIssued - loan.totalRecovered;
        if (maxRecovery == 0) return;
        
        // Minimum recovery: 1% of principal or 10K USDT, whichever is larger
        uint256 minRecovery = _max(loan.principalIssued / 100, 10_000 * USDT);
        amount = _bound(amount, minRecovery, maxRecovery);
        
        if (amount > maxRecovery) amount = maxRecovery;
        if (amount == 0) return;
        
        usdt.approve(address(loanEngine), amount);
        try loanEngine.recoverLoan(loanId, amount, address(this)) {} catch {}
    }
    
    
}
