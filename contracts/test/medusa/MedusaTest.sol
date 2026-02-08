// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {LoanEngine} from "../../src/LoanEngine.sol";
import {TranchePool} from "../../src/TranchePool.sol";
import {CreditPolicy} from "../../src/CreditPolicy.sol";
import {MockLoanProofVerifier} from "../mocks/MockLoanProofVerifier.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";

contract MedusaTest {
    LoanEngine public loanEngine;
    TranchePool public tranchePool;
    ERC20Mock public usdt;
    CreditPolicy public creditPolicy;
    
    uint256 public constant USDT = 1e18;
    address public deployer = address(0x999);
    address public recevingEntity = address(0x888);
    address public feeManager = address(0x777);
    
    // Configuration constants (matching Foundry handler)
    bool public allowFullDeployment = true;
    uint256 public minimumLoanPrincipal = 10_00_000 * USDT;
    uint256 public maximumLoanPrincipal = 2_00_00_000 * USDT;
    uint256 public minimumOriginationFeeBps = 50;
    uint256 public minimumTermDays = 180;
    uint256 public maximumTermDays = 480;
    uint256 public activePolicyVersion = 1;
    
    // Counters
    uint256 public defaultCounter;
    uint256 public writeOffCounter;
    uint256 public recoveryCounter;
    
    // Users
    address[] public seniorUsers;
    address[] public juniorUsers;
    address[] public equityUsers;
    address[] public loanBorrowers;
    
    // Ghost variables for tracking (matching Foundry handler)
    uint256 public totalIdleValue;
    uint256 public totalDeployedValue;
    uint256 public totalDeposited;
    uint256 public totalLoss;
    uint256 public totalRecovered;
    uint256 public totalUnclaimedInterest;
    uint256 public outStandingPrincipal;
    
    // VM cheatcodes interface
    Hevm internal constant vm = Hevm(0x7109709ECfa91a80626fF3989D68f67F5b1DD12D);
    
    constructor() {
        // Deploy contracts
        usdt = new ERC20Mock();
        tranchePool = new TranchePool(address(usdt));
        
        // Configure tranches (matching Foundry)
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
        
        // Create and fund users (matching Foundry - lots of users)
        for (uint160 i = 1; i < 100; i++) {
            seniorUsers.push(address(i));
            if (i % 2 == 0) {
                usdt.mint(address(i), 1_00_00_00000 * USDT);
                tranchePool.updateWhitelist(address(i), true);
            } else if (i % 3 == 0) {
                usdt.mint(address(i), 50_0000_0000 * USDT);
                tranchePool.updateWhitelist(address(i), true);
            } else {
                usdt.mint(address(i), 10_000_0000000 * USDT);
                tranchePool.updateWhitelist(address(i), true);
            }
        }
        
        for (uint160 i = 1; i < 10; i++) {
            juniorUsers.push(address(i));
            if (i % 2 == 0) {
                usdt.mint(address(i), 500000_00_000 * USDT);
                tranchePool.updateWhitelist(address(i), true);
            } else {
                usdt.mint(address(i), 10_000000_000 * USDT);
                tranchePool.updateWhitelist(address(i), true);
            }
        }
        
        for (uint160 i = 1; i < 5; i++) {
            equityUsers.push(address(i));
            usdt.mint(address(i), 50_0000_0000 * USDT);
            tranchePool.updateEquityTrancheWhiteList(address(i), true);
        }
        
        for (uint160 i = 200; i < 220; i++) {
            loanBorrowers.push(address(i));
        }
        
        usdt.mint(recevingEntity, 50_0000_0000 * USDT);
    }
    
    // =========================================================================
    // FUZZ FUNCTIONS - Matching Foundry Handler Logic
    // =========================================================================
    
    function depositSenior(uint256 userSeed, uint256 amount) external {
        if (tranchePool.getPoolState() != TranchePool.PoolState.OPEN) return;
        
        address user = seniorUsers[userSeed % seniorUsers.length];
        amount = _bound(
            amount,
            tranchePool.getSeniorTrancheMinimumDepositAmount(),
            tranchePool.getSeniorTrancheMaxDepositCap()
        );
        
        uint256 currentValue = tranchePool.getSeniorTrancheIdleValue() + 
                               tranchePool.getSeniorTrancheDeployedValue();
        
        if (currentValue >= tranchePool.getSeniorTrancheMaxDepositCap()) return;
        
        uint256 remaining = tranchePool.getSeniorTrancheMaxDepositCap() - currentValue;
        amount = _min(amount, remaining);
        
        if (amount < tranchePool.getSeniorTrancheMinimumDepositAmount()) return;
        if (amount == 0) return;
        
        _impersonate(user);
        usdt.approve(address(tranchePool), amount);
        tranchePool.depositSeniorTranche(amount);
        _stopImpersonate();
        
        totalIdleValue += amount;
    }
    
    function depositJunior(uint256 userSeed, uint256 amount) external {
        if (tranchePool.getPoolState() != TranchePool.PoolState.OPEN) return;
        
        address user = juniorUsers[userSeed % juniorUsers.length];
        amount = _bound(
            amount,
            tranchePool.getJuniorTrancheMinimumDepositAmount(),
            tranchePool.getJuniorTrancheMaxDepositCap()
        );
        
        uint256 currentValue = tranchePool.getJuniorTrancheIdleValue() + 
                               tranchePool.getJuniorTrancheDeployedValue();
        
        if (currentValue >= tranchePool.getJuniorTrancheMaxDepositCap()) return;
        
        uint256 remaining = tranchePool.getJuniorTrancheMaxDepositCap() - currentValue;
        amount = _min(amount, remaining);
        
        if (amount < tranchePool.getJuniorTrancheMinimumDepositAmount()) return;
        if (amount == 0) return;
        
        _impersonate(user);
        usdt.approve(address(tranchePool), amount);
        tranchePool.depositJuniorTranche(amount);
        _stopImpersonate();
        
        totalIdleValue += amount;
    }
    
    function depositEquity(uint256 userSeed, uint256 amount) external {
        if (tranchePool.getPoolState() != TranchePool.PoolState.OPEN) return;
        
        address user = equityUsers[userSeed % equityUsers.length];
        amount = _bound(
            amount,
            tranchePool.getEquityTrancheMinimumDepositAmount(),
            tranchePool.getEquityTrancheMaxDepositCap()
        );
        
        uint256 currentValue = tranchePool.getEquityTrancheIdleValue() + 
                               tranchePool.getEquityTrancheDeployedValue();
        
        if (currentValue >= tranchePool.getEquityTrancheMaxDepositCap()) return;
        
        uint256 remaining = tranchePool.getEquityTrancheMaxDepositCap() - currentValue;
        amount = _min(amount, remaining);
        
        if (amount < tranchePool.getEquityTrancheMinimumDepositAmount()) return;
        if (amount == 0) return;
        
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
            totalDeposited = tranchePool.getTotalIdleValue();
        }
    }
    
    function createLoan(
        uint256 principalIssued,
        uint256 originationFeeBps,
        uint256 termDays,
        uint256 userIndex
    ) external {
        if (tranchePool.getPoolState() != TranchePool.PoolState.COMMITED &&
            tranchePool.getPoolState() != TranchePool.PoolState.DEPLOYED) return;
        
        // Matching Foundry handler logic
        uint256 minPrincipal = minimumLoanPrincipal;
        
        if (allowFullDeployment) {
            if (tranchePool.getTotalIdleValue() < minPrincipal) {
                minPrincipal = tranchePool.getTotalIdleValue();
            }
        } else {
            if (tranchePool.getTotalIdleValue() < minPrincipal * 10) {
                return;
            }
        }
        
        if (tranchePool.getTotalIdleValue() < minimumLoanPrincipal) return;
        
        principalIssued = _bound(
            principalIssued,
            minimumLoanPrincipal,
            _min(maximumLoanPrincipal, tranchePool.getTotalIdleValue())
        );
        
        if (principalIssued > tranchePool.getTotalIdleValue() / 10) {
            principalIssued = tranchePool.getTotalIdleValue() / 10;
        }
        
        originationFeeBps = _bound(
            originationFeeBps,
            minimumOriginationFeeBps,
            loanEngine.getMaxOriginationFeeBps()
        );
        
        termDays = _bound(termDays, minimumTermDays, maximumTermDays);
        
        if (!creditPolicy.isPolicyFrozen(activePolicyVersion)) return;
        
        bytes32 borrowerCommitment = keccak256(
            abi.encodePacked(
                loanBorrowers[userIndex % loanBorrowers.length],
                userIndex
            )
        );
        
        uint256 nextLoanId = loanEngine.getNextLoanId();
        bytes memory proofData = abi.encodePacked(
            nextLoanId,
            userIndex,
            principalIssued,
            originationFeeBps,
            termDays
        );
        
        loanEngine.createLoan(
            borrowerCommitment,
            keccak256(abi.encode(nextLoanId, userIndex, borrowerCommitment, block.timestamp)),
            activePolicyVersion,
            1,
            principalIssued,
            500,
            originationFeeBps,
            termDays,
            bytes32(0),
            proofData,
            new bytes32[](0)
        );
    }
    
    function activateLoan(uint256 loanId) external {
        if (loanEngine.getNextLoanId() == 1) return;
        
        loanId = _bound(loanId, 1, loanEngine.getNextLoanId() - 1);
        
        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);
        if (loan.state != LoanEngine.LoanState.CREATED) return;
        
        if (tranchePool.getPoolState() != TranchePool.PoolState.COMMITED &&
            tranchePool.getPoolState() != TranchePool.PoolState.DEPLOYED) return;
        
        if (loan.principalIssued > tranchePool.getTotalIdleValue()) return;
        
        loanEngine.activateLoan(loanId, recevingEntity, feeManager);
        
        totalDeployedValue += loan.principalIssued;
        totalIdleValue -= loan.principalIssued;
        outStandingPrincipal += loan.principalIssued;
    }
    
    function repayLoan(uint256 loanId, uint256 principalAmount, uint256 interestAmount) external {
        if (loanEngine.getNextLoanId() == 1) return;
        
        loanId = _bound(loanId, 1, loanEngine.getNextLoanId() - 1);
        
        LoanEngine.Loan memory loanDetails = loanEngine.getLoanDetails(loanId);
        if (loanDetails.state != LoanEngine.LoanState.ACTIVE) return;
        
        principalAmount = _bound(principalAmount, 0, loanDetails.principalOutstanding);
        
        uint256 pendingInterest = _accrueInterest(loanId);
        uint256 totalInterestDue = loanDetails.interestAccrued + pendingInterest;
        
        interestAmount = _bound(interestAmount, 0, totalInterestDue);
        
        if (principalAmount == 0 && interestAmount == 0) return;
        
        // Interest before principal rule
        if (principalAmount > 0 && interestAmount == 0 && totalInterestDue > 0) return;
        
        uint256 totalRepayAmount = principalAmount + interestAmount;
        
        // Calculate ACTUAL amounts that will be paid (matching Foundry)
        uint256 interestAccrued = loanDetails.interestAccrued + _accrueInterest(loanId);
        uint256 actualInterestPaid = _min(totalRepayAmount, interestAccrued);
        uint256 actualPrincipalPaid = _min(
            totalRepayAmount - actualInterestPaid,
            loanDetails.principalOutstanding
        );
        
        _impersonate(recevingEntity);
        usdt.approve(address(loanEngine), totalRepayAmount);
        _stopImpersonate();
        
        totalUnclaimedInterest += actualInterestPaid;
        
        loanEngine.repayLoan(loanId, principalAmount, interestAmount, recevingEntity);
        
        // Use ACTUAL principal paid (THIS IS THE FIX!)
        totalDeployedValue -= actualPrincipalPaid;
        totalIdleValue += actualPrincipalPaid;
        outStandingPrincipal -= actualPrincipalPaid;
    }
    
    function warpTime(uint256 daysToWarp) external {
        daysToWarp = _bound(daysToWarp, 1, 365);
        vm.warp(block.timestamp + (daysToWarp * 1 days));
    }
    
    function maybeDeclareDefault(uint256 loanId, bytes32 reasonHash) external {
        if (loanEngine.getNextLoanId() == 1) return;
        
        defaultCounter++;
        if (defaultCounter % 10 != 0) return;
        
        loanId = _bound(loanId, 1, loanEngine.getNextLoanId() - 1);
        
        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);
        if (loan.state != LoanEngine.LoanState.ACTIVE) return;
        
        loanEngine.declareDefault(loanId, reasonHash);
    }
    
    function maybeWriteOffLoan(uint256 loanId) external {
        if (loanEngine.getNextLoanId() == 1) return;
        
        writeOffCounter++;
        
        loanId = _bound(loanId, 1, loanEngine.getNextLoanId() - 1);
        
        if (loanEngine.getLoanDetails(loanId).state != LoanEngine.LoanState.DEFAULTED) return;
        
        // Read principal before writeoff
        uint256 principalOutstanding = loanEngine.getLoanDetails(loanId).principalOutstanding;
        
        loanEngine.writeOffLoan(loanId);
        
        totalDeployedValue -= principalOutstanding;
        outStandingPrincipal -= principalOutstanding;
        totalLoss += principalOutstanding;
    }
    
    function maybeRecoverLoan(uint256 loanId, uint256 amount, uint256 agentIndex) external {
        if (loanEngine.getNextLoanId() == 1) return;
        
        recoveryCounter++;
        
        loanId = _bound(loanId, 1, loanEngine.getNextLoanId() - 1);
        
        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);
        if (loan.state != LoanEngine.LoanState.WRITTEN_OFF) return;
        
        amount = _bound(amount, 1, loan.principalIssued);
        
        _impersonate(recevingEntity);
        usdt.approve(address(loanEngine), amount);
        _stopImpersonate();
        
        loanEngine.recoverLoan(loanId, amount, recevingEntity);
        
        totalIdleValue += amount;
        totalRecovered += amount;
    }
    
    function mayClosePool() external {
        if (tranchePool.getTotalDeployedValue() > 0 || 
            tranchePool.getPoolState() != TranchePool.PoolState.DEPLOYED) return;
        
        tranchePool.setPoolState(TranchePool.PoolState.CLOSED);
    }
    
    // =========================================================================
    // INVARIANTS - Matching Foundry Invariants
    // =========================================================================
    
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

    function invariant_tokenBalance() external view returns (bool) {
        return (tranchePool.getTotalUnclaimedInterest() + 
                tranchePool.getTotalIdleValue() + 
                tranchePool.getProtocolRevenue()) == 
                usdt.balanceOf(address(tranchePool));
    }

    function invariant_trancheSum() external view returns (bool) {
        return tranchePool.getTotalDeployedValue() == 
               (tranchePool.getSeniorTrancheDeployedValue() + 
                tranchePool.getJuniorTrancheDeployedValue() + 
                tranchePool.getEquityTrancheDeployedValue());
    }

    function invariant_waterfallSymmetry() external view returns (bool) {
        uint256 totalShortfall = tranchePool.getSeniorPrincipalShortfall() +
            tranchePool.getJuniorPrincipalShortfall() +
            tranchePool.getEquityPrincipalShortfall();

        if (tranchePool.getTotalRecovered() >= tranchePool.getTotalLoss()) {
            return totalShortfall == 0;
        } else {
            return totalShortfall == (tranchePool.getTotalLoss() - tranchePool.getTotalRecovered());
        }
    }

    function invariant_idleIntegrity() external view returns (bool) {
        return (tranchePool.getSeniorTrancheIdleValue() +
                tranchePool.getJuniorTrancheIdleValue() +
                tranchePool.getEquityTrancheIdleValue()) == 
                tranchePool.getTotalIdleValue();
    }

    function invariant_seniorShareOpen() external view returns (bool) {
        if (tranchePool.getPoolState() == TranchePool.PoolState.OPEN) {
            return tranchePool.getTotalSeniorShares() == tranchePool.getSeniorTrancheIdleValue();
        }
        return true;
    }

    function invariant_loanState() external view returns (bool) {
        uint256 nextId = loanEngine.getNextLoanId();
        for (uint256 i = 1; i < nextId; i++) {
            LoanEngine.Loan memory loan = loanEngine.getLoanDetails(i);
            
            if (loan.state == LoanEngine.LoanState.NONE || 
                loan.state == LoanEngine.LoanState.CREATED) {
                if (loan.principalOutstanding != 0) return false;
            }
            
            if (loan.state == LoanEngine.LoanState.REPAID ||
                loan.state == LoanEngine.LoanState.WRITTEN_OFF) {
                if (loan.principalOutstanding != 0) return false;
            }
            
            if (loan.state == LoanEngine.LoanState.ACTIVE) {
                if (loan.principalOutstanding > loan.principalIssued) return false;
            }
        }
        return true;
    }

    function invariant_interestMonotonicity() external view returns (bool) {
        return tranchePool.getSeniorInterestIndex() >= 1e18 &&
               tranchePool.getJuniorInterestIndex() >= 1e18 &&
               tranchePool.getEquityInterestIndex() >= 1e18;
    }

    function invariant_poolState() external view returns (bool) {
        TranchePool.PoolState state = tranchePool.getPoolState();
        if (state == TranchePool.PoolState.OPEN || 
            state == TranchePool.PoolState.CLOSED) {
            if (tranchePool.getTotalDeployedValue() != 0) return false;
        }
        return true;
    }

    function invariant_interestAccounting() external view returns (bool) {
        uint256 nextId = loanEngine.getNextLoanId();
        for (uint256 i = 1; i < nextId; i++) {
            LoanEngine.Loan memory loan = loanEngine.getLoanDetails(i);
            if (loan.state == LoanEngine.LoanState.REPAID) {
                if (loan.interestAccrued != 0) return false;
            }
            if (loan.state == LoanEngine.LoanState.WRITTEN_OFF) {
                if (loan.interestAccrued != 0) return false;
            }
        }
        return true;
    }
    
    // =========================================================================
    // HELPER FUNCTIONS
    // =========================================================================
    
    function _accrueInterest(uint256 loanId) internal view returns (uint256) {
        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);
        
        uint256 timeElapsed = block.timestamp - loan.lastAccrualTimestamp;
        if (loan.principalOutstanding == 0) return 0;
        
        uint256 interest = (loan.principalOutstanding * loan.aprBps * timeElapsed) / (365 days * 10_000);
        return interest;
    }
    
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
        if (min > max) return min;
        if (x < min) return min;
        if (x > max) return max;
        return min + (x % (max - min + 1));
    }
    
    function _min(uint256 a, uint256 b) internal pure returns (uint256) {
        return a < b ? a : b;
    }
    
    // Medusa impersonate pattern
    function _impersonate(address who) internal {
        vm.startPrank(who);
    }
    
    function _stopImpersonate() internal {
        vm.stopPrank();
    }
}

// Hevm interface for cheatcodes
interface Hevm {
    function startPrank(address) external;
    function stopPrank() external;
    function warp(uint256) external;
}