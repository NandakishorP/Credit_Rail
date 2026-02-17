// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {LoanEngine} from "../../../src/LoanEngine.sol";
import {TranchePool} from "../../../src/TranchePool.sol";
import {CreditPolicy} from "../../../src/CreditPolicy.sol";
import {ICreditPolicy} from "../../../src/interfaces/ICreditPolicy.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {MockLoanProofVerifier} from "../../mocks/MockLoanProofVerifier.sol";
import {MockPoseidon2} from "../../mocks/MockPoseidon2.sol";

/**
 * @title EchidnaHandler
 * @notice Echidna-compatible handler matching Foundry Handler.t.sol EXACTLY
 * @dev No Foundry cheatcodes - this contract is its own deployer/owner
 */
contract EchidnaHandler {
    // =========================================================================
    // STATE - Matching Foundry Handler
    // =========================================================================

    LoanEngine public loanEngine;
    TranchePool public tranchePool;
    ERC20Mock public usdt;
    CreditPolicy public creditPolicy;
    MockLoanProofVerifier public verifier;

    // Constants (matching Handler.t.sol EXACTLY)
    uint256 public constant USDT = 1e18;
    uint256 public constant minimumLoanPrincipal = 10_00_000 * USDT; // 1M USDT
    uint256 public constant maximumLoanPrincipal = 2_00_00_000 * USDT; // 20M USDT
    uint256 public constant minimumOriginationFeeBps = 50; // 0.5%
    uint256 public constant minimumTermDays = 180;
    uint256 public constant maximumTermDays = 480;
    uint256 public constant MAX_ORIGINATION_FEE_BPS = 500; // 5%
    bool public constant allowFullDeployment = true;

    // Initial funding (large enough to meet minimums)
    uint256 public constant INITIAL_SENIOR_DEPOSIT = 80_00_00_000 * USDT;
    uint256 public constant INITIAL_JUNIOR_DEPOSIT = 50_00_00_000 * USDT;
    uint256 public constant INITIAL_EQUITY_DEPOSIT = 100_00_00_000 * USDT;

    // Ghost variables for invariants (matching Foundry)
    uint256 public outstandingPrincipal;
    uint256 public totalIdleValue;
    uint256 public totalDeployedValue;
    uint256 public totalDeposited;
    uint256 public totalLoss;
    uint256 public totalRecovered;
    uint256 public totalUnclaimedInterest;

    uint256 public activePolicyVersion = 1;
    uint256 public defaultCounter;
    uint256 public writeOffCounter;
    uint256 public recoveryCounter;

    // =========================================================================
    // CONSTRUCTOR
    // =========================================================================

    constructor() {
        // Deploy mock token
        usdt = new ERC20Mock();

        // Deploy TranchePool
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

        // Deploy MockLoanProofVerifier
        verifier = new MockLoanProofVerifier();

        // Deploy CreditPolicy and set it up
        creditPolicy = new CreditPolicy();
        _setupCreditPolicy();

        // Deploy LoanEngine with MockPoseidon2
        MockPoseidon2 mockPoseidon = new MockPoseidon2();
        loanEngine = new LoanEngine(
            address(creditPolicy),
            address(verifier),
            MAX_ORIGINATION_FEE_BPS,
            address(tranchePool),
            address(usdt),
            address(mockPoseidon)
        );
        loanEngine.setMaxOriginationFeeBps(500);
        tranchePool.setLoanEngine(address(loanEngine));

        // Whitelist this contract for all operations
        loanEngine.setWhitelistedFeeManager(address(this), true);
        loanEngine.setWhitelistedOffRampingEntity(address(this), true);
        loanEngine.setWhitelistedRepaymentAgent(address(this), true);
        loanEngine.setWhitelistedRecoveryAgent(address(this), true);
        tranchePool.updateWhitelist(address(this), true);
        tranchePool.updateEquityTrancheWhiteList(address(this), true);

        // Mint USDT for operations
        usdt.mint(address(this), 500_00_00_000 * USDT); // 5B USDT

        // Initial deposits to ensure pool has liquidity
        _initialDeposits();
    }

    function _setupCreditPolicy() internal {
        creditPolicy.createPolicy(1);
        creditPolicy.setMaxTiers(3);

        creditPolicy.updateEligibility(
            1,
            ICreditPolicy.EligibilityCriteria({
                minAnnualRevenue: 1_00_00_000,
                minEBITDA: 10_00_000,
                minTangibleNetWorth: 5_00_00_000,
                minBusinessAgeDays: 180,
                maxDefaultsLast36Months: 0,
                bankruptcyExcluded: true
            })
        );

        creditPolicy.updateRatios(
            1,
            ICreditPolicy.FinancialRatios({
                maxTotalDebtToEBITDA: 4e18,
                minInterestCoverageRatio: 2e18,
                minCurrentRatio: 1e18,
                minEBITDAMarginBps: 1500
            })
        );

        creditPolicy.updateConcentration(
            1,
            ICreditPolicy.ConcentrationLimits({
                maxSingleBorrowerBps: 1000,
                maxIndustryConcentrationBps: 3000
            })
        );

        creditPolicy.updateAttestation(
            1,
            ICreditPolicy.AttestationRequirements({
                maxAttestationAgeDays: 90,
                reAttestationFrequencyDays: 180,
                requiresCPAAttestation: true
            })
        );

        creditPolicy.updateCovenants(
            1,
            ICreditPolicy.MaintenanceCovenants({
                maxLeverageRatio: 4e18,
                minCoverageRatio: 2e18,
                minLiquidityAmount: 1_00_00_000,
                allowsDividends: false,
                reportingFrequencyDays: 90
            })
        );

        creditPolicy.setLoanTier(
            1,
            1,
            ICreditPolicy.LoanTier({
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

        creditPolicy.setPolicyDocument(
            1,
            keccak256("document"),
            "ipfs://policyDocHash"
        );
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
        totalIdleValue += seniorDeposit;

        // Junior tranche deposit
        uint256 juniorMin = tranchePool.getJuniorTrancheMinimumDepositAmount();
        uint256 juniorMax = tranchePool.getJuniorTrancheMaxDepositCap();
        uint256 juniorDeposit = _min(INITIAL_JUNIOR_DEPOSIT, juniorMax);
        juniorDeposit = _max(juniorDeposit, juniorMin);

        usdt.approve(address(tranchePool), juniorDeposit);
        tranchePool.depositJuniorTranche(juniorDeposit);
        totalIdleValue += juniorDeposit;

        // Equity tranche deposit
        uint256 equityMin = tranchePool.getEquityTrancheMinimumDepositAmount();
        uint256 equityMax = tranchePool.getEquityTrancheMaxDepositCap();
        uint256 equityDeposit = _min(INITIAL_EQUITY_DEPOSIT, equityMax);
        equityDeposit = _max(equityDeposit, equityMin);

        usdt.approve(address(tranchePool), equityDeposit);
        tranchePool.depositEquityTranche(equityDeposit);
        totalIdleValue += equityDeposit;
    }

    // =========================================================================
    // DEPOSIT FUNCTIONS - Matching Foundry Handler
    // =========================================================================

    function depositSeniorTranche(uint256 amount) public {
        if (tranchePool.getPoolState() != ITranchePool.PoolState.OPEN) return;

        uint256 minDeposit = tranchePool.getSeniorTrancheMinimumDepositAmount();
        uint256 maxDeposit = tranchePool.getSeniorTrancheMaxDepositCap();
        uint256 currentValue = tranchePool.getSeniorTrancheIdleValue() +
            tranchePool.getSeniorTrancheDeployedValue();

        if (currentValue >= maxDeposit) return;

        uint256 remaining = maxDeposit - currentValue;
        amount = _bound(amount, minDeposit, _min(remaining, maxDeposit));

        if (amount < minDeposit) return;

        usdt.approve(address(tranchePool), amount);
        try tranchePool.depositSeniorTranche(amount) {
            totalIdleValue += amount;
        } catch {}
    }

    function depositJuniorTranche(uint256 amount) public {
        if (tranchePool.getPoolState() != ITranchePool.PoolState.OPEN) return;

        uint256 minDeposit = tranchePool.getJuniorTrancheMinimumDepositAmount();
        uint256 maxDeposit = tranchePool.getJuniorTrancheMaxDepositCap();
        uint256 currentValue = tranchePool.getJuniorTrancheIdleValue() +
            tranchePool.getJuniorTrancheDeployedValue();

        if (currentValue >= maxDeposit) return;

        uint256 remaining = maxDeposit - currentValue;
        amount = _bound(amount, minDeposit, _min(remaining, maxDeposit));

        if (amount < minDeposit) return;

        usdt.approve(address(tranchePool), amount);
        try tranchePool.depositJuniorTranche(amount) {
            totalIdleValue += amount;
        } catch {}
    }

    function depositEquityTranche(uint256 amount) public {
        if (tranchePool.getPoolState() != ITranchePool.PoolState.OPEN) return;

        uint256 minDeposit = tranchePool.getEquityTrancheMinimumDepositAmount();
        uint256 maxDeposit = tranchePool.getEquityTrancheMaxDepositCap();
        uint256 currentValue = tranchePool.getEquityTrancheIdleValue() +
            tranchePool.getEquityTrancheDeployedValue();

        if (currentValue >= maxDeposit) return;

        uint256 remaining = maxDeposit - currentValue;
        amount = _bound(amount, minDeposit, _min(remaining, maxDeposit));

        if (amount < minDeposit) return;

        usdt.approve(address(tranchePool), amount);
        try tranchePool.depositEquityTranche(amount) {
            totalIdleValue += amount;
        } catch {}
    }

    // =========================================================================
    // POOL STATE TRANSITIONS - Matching Foundry Handler
    // =========================================================================

    function commitPool() public {
        if (tranchePool.getPoolState() != ITranchePool.PoolState.OPEN) return;
        if (tranchePool.getTotalIdleValue() == 0) return;

        try tranchePool.setPoolState(ITranchePool.PoolState.COMMITED) {
            totalDeposited = tranchePool.getTotalIdleValue();
        } catch {}
    }

    function closePool() public {
        if (tranchePool.getTotalDeployedValue() > 0) return;
        if (tranchePool.getPoolState() != ITranchePool.PoolState.DEPLOYED)
            return;

        try tranchePool.setPoolState(ITranchePool.PoolState.CLOSED) {} catch {}
    }

    // =========================================================================
    // LOAN LIFECYCLE - Matching Foundry Handler EXACTLY
    // =========================================================================

    function createLoan(
        uint256 principalIssued,
        uint256 originationFeeBps,
        uint256 termDays
    ) public {
        ITranchePool.PoolState state = tranchePool.getPoolState();
        if (
            state != ITranchePool.PoolState.COMMITED &&
            state != ITranchePool.PoolState.DEPLOYED
        ) return;

        // Matching Foundry handler logic EXACTLY
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
            MAX_ORIGINATION_FEE_BPS
        );
        termDays = _bound(termDays, minimumTermDays, maximumTermDays);

        if (!creditPolicy.isPolicyFrozen(activePolicyVersion)) return;

        bytes32 borrowerCommitment = keccak256(
            abi.encodePacked(block.timestamp, principalIssued)
        );
        uint256 nextLoanId = loanEngine.getNextLoanId();
        bytes32 nullifierHash = keccak256(
            abi.encode(nextLoanId, borrowerCommitment, block.timestamp)
        );
        bytes memory proofData = abi.encodePacked(
            nextLoanId,
            principalIssued,
            originationFeeBps,
            termDays
        );

        LoanEngine.CreateLoanParams memory params = LoanEngine
            .CreateLoanParams({
                borrowerCommitment: borrowerCommitment,
                nullifierHash: nullifierHash,
                policyVersion: activePolicyVersion,
                tierId: 1,
                principalIssued: principalIssued,
                aprBps: 500,
                originationFeeBps: originationFeeBps,
                termDays: termDays,
                industry: bytes32(0),
                underwriterKeyX: bytes32(0),
                underwriterKeyY: bytes32(0),
                proofTimestamp: block.timestamp
            });

        try
            loanEngine.createLoan(params, proofData, new bytes32[](3))
        {} catch {}
    }

    function activateLoan(uint256 loanId) public {
        if (loanEngine.getNextLoanId() <= 1) return;
        loanId = _bound(loanId, 1, loanEngine.getNextLoanId() - 1);

        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);
        if (loan.state != LoanEngine.LoanState.CREATED) return;

        ITranchePool.PoolState poolState = tranchePool.getPoolState();
        if (
            poolState != ITranchePool.PoolState.COMMITED &&
            poolState != ITranchePool.PoolState.DEPLOYED
        ) return;

        if (loan.principalIssued > tranchePool.getTotalIdleValue()) return;

        try loanEngine.activateLoan(loanId, address(this), address(this)) {
            totalDeployedValue += loan.principalIssued;
            totalIdleValue -= loan.principalIssued;
            outstandingPrincipal += loan.principalIssued;
        } catch {}
    }

    function repayLoan(
        uint256 loanId,
        uint256 principalAmount,
        uint256 interestAmount
    ) public {
        if (loanEngine.getNextLoanId() <= 1) return;
        loanId = _bound(loanId, 1, loanEngine.getNextLoanId() - 1);

        LoanEngine.Loan memory loanBefore = loanEngine.getLoanDetails(loanId);
        if (loanBefore.state != LoanEngine.LoanState.ACTIVE) return;

        // DUST PAYMENT FIX: Minimum $10K payment
        uint256 MIN_PAYMENT = 10_000 * USDT;

        principalAmount = _bound(
            principalAmount,
            0,
            loanBefore.principalOutstanding
        );

        uint256 pendingInterest = _accrueInterest(loanId);
        uint256 totalInterestDue = loanBefore.interestAccrued + pendingInterest;

        interestAmount = _bound(interestAmount, 0, totalInterestDue);

        uint256 total = principalAmount + interestAmount;
        if (total == 0) return;

        // Block dust payments UNLESS it's a full repayment
        uint256 fullAmount = loanBefore.principalOutstanding +
            loanBefore.interestAccrued +
            pendingInterest;
        if (total < MIN_PAYMENT && total != fullAmount) {
            return; // NO DUST PAYMENTS!
        }

        // Interest before principal rule
        if (principalAmount > 0 && interestAmount == 0 && totalInterestDue > 0)
            return;

        // Calculate ACTUAL amounts (matching Foundry handler)
        uint256 interestAccrued = loanBefore.interestAccrued +
            _accrueInterest(loanId);
        uint256 actualInterestPaid = _min(total, interestAccrued);
        uint256 actualPrincipalPaid = _min(
            total - actualInterestPaid,
            loanBefore.principalOutstanding
        );

        usdt.approve(address(loanEngine), total);
        try
            loanEngine.repayLoan(
                loanId,
                principalAmount,
                interestAmount,
                address(this),
                block.timestamp
            )
        {
            totalDeployedValue -= actualPrincipalPaid;
            totalIdleValue += actualPrincipalPaid;
            outstandingPrincipal -= actualPrincipalPaid;
            totalUnclaimedInterest += actualInterestPaid;
        } catch {}
    }

    function declareDefault(uint256 loanId) public {
        if (loanEngine.getNextLoanId() <= 1) return;

        defaultCounter++;
        if (defaultCounter % 10 != 0) return; // Only occasionally default

        loanId = _bound(loanId, 1, loanEngine.getNextLoanId() - 1);

        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);
        if (loan.state != LoanEngine.LoanState.ACTIVE) return;

        try
            loanEngine.declareDefault(loanId, bytes32(0), block.timestamp)
        {} catch {}
    }

    function writeOffLoan(uint256 loanId) public {
        if (loanEngine.getNextLoanId() <= 1) return;

        writeOffCounter++;

        loanId = _bound(loanId, 1, loanEngine.getNextLoanId() - 1);

        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);
        if (loan.state != LoanEngine.LoanState.DEFAULTED) return;

        uint256 principal = loan.principalOutstanding;

        try loanEngine.writeOffLoan(loanId) {
            totalDeployedValue -= principal;
            outstandingPrincipal -= principal;
            totalLoss += principal;
        } catch {}
    }

    function recoverLoan(uint256 loanId, uint256 amount) public {
        if (loanEngine.getNextLoanId() <= 1) return;

        recoveryCounter++;

        loanId = _bound(loanId, 1, loanEngine.getNextLoanId() - 1);

        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);
        if (loan.state != LoanEngine.LoanState.WRITTEN_OFF) return;

        // Recovery bounded to principal issued (no over-recovery)
        uint256 maxRecovery = loan.principalIssued - loan.totalRecovered;
        if (maxRecovery == 0) return;

        // Minimum recovery: 1% of principal or 10K USDT
        uint256 minRecovery = _max(loan.principalIssued / 100, 10_000 * USDT);
        amount = _bound(amount, minRecovery, maxRecovery);

        if (amount > maxRecovery) amount = maxRecovery;
        if (amount == 0) return;

        usdt.approve(address(loanEngine), amount);
        try loanEngine.recoverLoan(loanId, amount, address(this)) {
            totalIdleValue += amount;
            totalRecovered += amount;
        } catch {}
    }

    // =========================================================================
    // HELPER FUNCTIONS - Matching Foundry Handler
    // =========================================================================

    function _accrueInterest(uint256 loanId) internal view returns (uint256) {
        LoanEngine.Loan memory loan = loanEngine.getLoanDetails(loanId);

        uint256 timeElapsed = block.timestamp - loan.lastAccrualTimestamp;
        if (loan.principalOutstanding == 0) return 0;

        uint256 interest = (loan.principalOutstanding *
            loan.aprBps *
            timeElapsed) / (365 days * 10_000);
        return interest;
    }

    function _bound(
        uint256 x,
        uint256 min,
        uint256 max
    ) internal pure returns (uint256) {
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
}
