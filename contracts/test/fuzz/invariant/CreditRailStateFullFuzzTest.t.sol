// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {LoanEngine} from "../../../src/LoanEngine.sol";
import {ILoanEngine} from "../../../src/interfaces/ILoanEngine.sol";
import {TranchePool} from "../../../src/TranchePool.sol";
import {ITranchePool} from "../../../src/interfaces/ITranchePool.sol";
import {CreditPolicy} from "../../../src/CreditPolicy.sol";
import {ICreditPolicy} from "../../../src/interfaces/ICreditPolicy.sol";
import {MockLoanProofVerifier} from "../../mocks/MockLoanProofVerifier.sol";
import {MockPoseidon2} from "../../mocks/MockPoseidon2.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {ERC1967Proxy} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";

import {Handler} from "./Handler.t.sol";
import {Test} from "forge-std/Test.sol";
import {StdInvariant} from "forge-std/StdInvariant.sol";

// we assume protocol revenue is zero as we have equity tranche
contract CreditRailStateFullFuzzTest is StdInvariant, Test {
    Handler public handler;
    ERC20Mock public usdt;
    uint256 public maxOriginationFeeBps = 500; // 5%
    TranchePool public tranchePool;
    LoanEngine public loanEngine;
    CreditPolicy public creditPolicy;
    uint256 public USDT = 1e6;
    address public deployer = makeAddr("deployer");

    function setUp() public {
        // Change from constructor to setUp
        vm.deal(deployer, 100 ether);
        vm.startPrank(deployer);
        usdt = new ERC20Mock();

        // Deploy TranchePool via proxy
        TranchePool tpImpl = new TranchePool();
        ERC1967Proxy tpProxy = new ERC1967Proxy(
            address(tpImpl),
            abi.encodeCall(TranchePool.initialize, (address(usdt), deployer))
        );
        tranchePool = TranchePool(address(tpProxy));

        tranchePool.setMaxDepositCapSeniorTranche(5_00_00_000 * USDT);
        tranchePool.setMaxDepositCapJuniorTranche(3_00_00_000 * USDT);
        tranchePool.setMaxDepositCapEquityTranche(2_00_00_000 * USDT);
        tranchePool.setMinimumDepositAmountSeniorTranche(10_00_000 * USDT);
        tranchePool.setMinimumDepositAmountJuniorTranche(50_00_000 * USDT);
        tranchePool.setMinimumDepositAmountEquityTranche(1_00_00_000 * USDT);
        tranchePool.setTrancheCapitalAllocationFactorJunior(15);
        tranchePool.setTrancheCapitalAllocationFactorSenior(80);
        tranchePool.setSeniorAPR(800);
        tranchePool.setTargetJuniorAPR(1500);

        // Deploy CreditPolicy via proxy
        CreditPolicy cpImpl = new CreditPolicy();
        ERC1967Proxy cpProxy = new ERC1967Proxy(
            address(cpImpl),
            abi.encodeCall(CreditPolicy.initialize, (deployer))
        );
        creditPolicy = CreditPolicy(address(cpProxy));

        creditPolicy.setMaxTiers(3);
        creditPolicy.createPolicy(1);

        creditPolicy.updateEligibility(1, _createEligibilityCriteria());
        creditPolicy.updateRatios(1, _createFinancialRatios());
        creditPolicy.updateConcentration(1, _createConcentrationLimits());
        creditPolicy.updateAttestation(1, _createAttestationRequirements());
        creditPolicy.updateCovenants(1, _createMaintenanceCovenants());
        creditPolicy.setLoanTier(1, 1, _createMockTier("Tier 1"));
        creditPolicy.setPolicyDocument(
            1,
            _hashString("document"),
            "ipfs://policyDocHash"
        );
        creditPolicy.setPolicyScopeHash(1, _hashString("scope"));
        creditPolicy.freezePolicy(1);

        // Deploy LoanEngine via proxy
        MockLoanProofVerifier mockLoanProofVerifier = new MockLoanProofVerifier();
        MockPoseidon2 mockPoseidon = new MockPoseidon2();
        LoanEngine leImpl = new LoanEngine();
        ERC1967Proxy leProxy = new ERC1967Proxy(
            address(leImpl),
            abi.encodeCall(
                LoanEngine.initialize,
                (
                    address(creditPolicy),
                    address(mockLoanProofVerifier),
                    maxOriginationFeeBps,
                    address(tranchePool),
                    address(usdt),
                    address(mockPoseidon),
                    deployer
                )
            )
        );
        loanEngine = LoanEngine(address(leProxy));

        loanEngine.setMaxOriginationFeeBps(500);
        tranchePool.setLoanEngine(address(loanEngine));

        vm.stopPrank();
        handler = new Handler(loanEngine, tranchePool, creditPolicy, usdt);

        bytes4[] memory selectors = new bytes4[](18);
        selectors[0] = handler.depositSeniorTranche.selector;
        selectors[1] = handler.depositJuniorTranche.selector;
        selectors[2] = handler.depositEquityTranche.selector;
        selectors[3] = handler.maybeCommitPool.selector;
        selectors[4] = handler.createLoan.selector;
        selectors[5] = handler.activateLoan.selector;
        selectors[6] = handler.repayLoan.selector;
        selectors[7] = handler.maybeDeclareDefault.selector;
        selectors[8] = handler.maybeWriteOffLoan.selector;
        selectors[9] = handler.maybeRecoverLoan.selector;
        selectors[10] = handler.warpTime.selector;
        selectors[11] = handler.mayClosePool.selector;
        selectors[12] = handler.claimSeniorTrancheInterest.selector;
        selectors[13] = handler.claimJuniorTrancheInterest.selector;
        selectors[14] = handler.claimEquityTrancheInterest.selector;
        selectors[15] = handler.withdrawSeniorTranche.selector;
        selectors[16] = handler.withdrawJuniorTranche.selector;
        selectors[17] = handler.withdrawEquityTranche.selector;

        targetSelector(
            FuzzSelector({addr: address(handler), selectors: selectors})
        );
        targetContract(address(handler));
    }

    function _createEligibilityCriteria()
        internal
        pure
        returns (ICreditPolicy.EligibilityCriteria memory)
    {
        return
            ICreditPolicy.EligibilityCriteria({
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

    function _createConcentrationLimits()
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

    function _createAttestationRequirements()
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

    function _createMaintenanceCovenants()
        internal
        pure
        returns (ICreditPolicy.MaintenanceCovenants memory)
    {
        return
            ICreditPolicy.MaintenanceCovenants({
                maxLeverageRatio: 4e18,
                minCoverageRatio: 2e18,
                minLiquidityAmount: 1_00_00_000,
                allowsDividends: false,
                reportingFrequencyDays: 90
            });
    }

    function _createMockTier(
        string memory name
    ) internal pure returns (ICreditPolicy.LoanTier memory) {
        return
            ICreditPolicy.LoanTier({
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

    function invariant__totalIdleAndDeployedValueMatchesAccounting()
        public
        view
    {
        assertEq(
            tranchePool.getTotalIdleValue() +
                tranchePool.getTotalDeployedValue(),
            tranchePool.getTotalDeposited() -
                tranchePool.getTotalLoss() +
                tranchePool.getTotalRecovered(),
            "Total idle and deployed value does not match handler accounting"
        );
    }

    function invariant__OutStandingPrincipalMatchesDeployed() public view {
        assertEq(
            handler.outStandingPrincipal(),
            tranchePool.getTotalDeployedValue(),
            "Outstanding principal does not match deployed minus recovered and loss"
        );
    }

    function invariant__totalUnclaimedInterestAndIdleValueMatchesTotalTokenBalance()
        public
        view
    {
        assertEq(
            tranchePool.getTotalUnclaimedInterest() +
                tranchePool.getTotalIdleValue(),
            ERC20Mock(usdt).balanceOf(address(tranchePool)),
            "Total unclaimed interest does not match deployed minus recovered and loss"
        );
    }

    function invariant__totalDeployedValueMatchesSumOfIndividualTranches()
        public
        view
    {
        assertEq(
            tranchePool.getTotalDeployedValue(),
            tranchePool.getSeniorTrancheDeployedValue() +
                tranchePool.getJuniorTrancheDeployedValue() +
                tranchePool.getEquityTrancheDeployedValue(),
            "Total deployed value does not match sum of individual tranches"
        );
    }

    /*
        @notice System Level Invariant: Loan Principal Integrity
        Iterates over all loans in the LoanEngine and sums up the outstanding principal.
        This sum must strictly equal the Total Deployed Value in the TranchePool.
        This ensures that:
        1. Every deployed dollar is accounted for by a loan.
        2. No "Ghost" capital exists in the deployed state.
        3. Loan principal updates (repayment/write-off) always sync with the Pool.
    */
    function invariant__systemLevel_PrincipalIntegrity() public view {
        uint256 totalOutstandingPrincipal = 0;
        // nextLoanId is 1-indexed, loop from 1 to nextLoanId - 1
        uint256 nextId = loanEngine.getNextLoanId();
        for (uint256 i = 1; i < nextId; i++) {
            ILoanEngine.Loan memory loan = loanEngine.getLoanDetails(i);
            // Only count active principal. Theoretically, REPAID/DEFAULTED could have 0,
            // but we sum whatever is in the principalOutstanding field to be safe.
            totalOutstandingPrincipal += loan.principalOutstanding;
        }

        assertEq(
            totalOutstandingPrincipal,
            tranchePool.getTotalDeployedValue(),
            "System Level Invariant Failed: Sum of Loan Principals != Pool Deployed Value"
        );
    }

    function invariant__lossRecoveryWaterfallSymmetry() public view {
        uint256 totalShortfall = tranchePool.getSeniorPrincipalShortfall() +
            tranchePool.getJuniorPrincipalShortfall() +
            tranchePool.getEquityPrincipalShortfall();

        if (tranchePool.getTotalRecovered() >= tranchePool.getTotalLoss()) {
            // If we recovered more than lost, the hole should be completely filled.
            assertEq(
                totalShortfall,
                0,
                "Shortfall must be 0 if fully recovered"
            );
        } else {
            // If we haven't recovered everything, shortfall should exactly match the remaining hole.
            assertEq(
                totalShortfall,
                tranchePool.getTotalLoss() - tranchePool.getTotalRecovered(),
                "Shortfall mismatch"
            );
        }
    }

    function invariant__totalIdleValueIntegrity() public view {
        assertEq(
            tranchePool.getSeniorTrancheIdleValue() +
                tranchePool.getJuniorTrancheIdleValue() +
                tranchePool.getEquityTrancheIdleValue(),
            tranchePool.getTotalIdleValue(),
            "Sum of tranche idle values != total idle value"
        );
    }

    function invariant__seniorShareToIdleOpen() public view {
        if (tranchePool.getPoolState() == ITranchePool.PoolState.OPEN) {
            assertEq(
                tranchePool.getTotalSeniorShares(),
                tranchePool.getSeniorTrancheIdleValue(),
                "Senior: Shares != Idle in OPEN state"
            );
        }
    }

    function invariant__loanStateConsistency() public view {
        uint256 nextId = loanEngine.getNextLoanId();
        for (uint256 i = 1; i < nextId; i++) {
            ILoanEngine.Loan memory loan = loanEngine.getLoanDetails(i);

            // NONE and CREATED should have 0 principal outstanding
            if (
                loan.state == ILoanEngine.LoanState.NONE ||
                loan.state == ILoanEngine.LoanState.CREATED
            ) {
                assertEq(
                    loan.principalOutstanding,
                    0,
                    "NONE/CREATED loan has outstanding principal"
                );
            }

            // REPAID and WRITTEN_OFF must have 0 outstanding
            if (
                loan.state == ILoanEngine.LoanState.REPAID ||
                loan.state == ILoanEngine.LoanState.WRITTEN_OFF
            ) {
                assertEq(
                    loan.principalOutstanding,
                    0,
                    "Terminal loan has outstanding principal"
                );
            }

            // ACTIVE loans must have principalOutstanding <= principalIssued
            if (loan.state == ILoanEngine.LoanState.ACTIVE) {
                assertLe(
                    loan.principalOutstanding,
                    loan.principalIssued,
                    "Active loan: outstanding > issued"
                );
            }
        }
    }

    function invariant__interestIndexMonotonicity() public view {
        // Indices initialize at 1e18 and can only increase
        assertGe(
            tranchePool.getSeniorInterestIndex(),
            1e18,
            "Senior interest index below initial"
        );
        assertGe(
            tranchePool.getJuniorInterestIndex(),
            1e18,
            "Junior interest index below initial"
        );
        assertGe(
            tranchePool.getEquityInterestIndex(),
            1e18,
            "Equity interest index below initial"
        );
    }

    function invariant__poolStateValidityDeployedCapital() public view {
        ITranchePool.PoolState state = tranchePool.getPoolState();
        if (
            state == ITranchePool.PoolState.OPEN ||
            state == ITranchePool.PoolState.CLOSED
        ) {
            assertEq(
                tranchePool.getTotalDeployedValue(),
                0,
                "OPEN/CLOSED pool has deployed capital"
            );
        }

        // Cannot close with active loans (deployed > 0)
        if (state == ITranchePool.PoolState.CLOSED) {
            assertEq(
                tranchePool.getTotalDeployedValue(),
                0,
                "CLOSED pool still has deployed capital"
            );
        }
    }

    function invariant__loanInterestAccounting() public view {
        uint256 nextId = loanEngine.getNextLoanId();

        for (uint256 i = 1; i < nextId; i++) {
            ILoanEngine.Loan memory loan = loanEngine.getLoanDetails(i);
            if (loan.state == ILoanEngine.LoanState.REPAID) {
                assertEq(
                    loan.interestAccrued,
                    0,
                    "REPAID loan has remaining accrued interest"
                );
            }
            if (loan.state == ILoanEngine.LoanState.WRITTEN_OFF) {
                assertEq(
                    loan.interestAccrued,
                    0,
                    "WRITTEN_OFF loan has accrued interest"
                );
            }
        }
    }

    function invariant__lossWaterfallOrdering() public view {
        // Losses absorb equity → junior → senior via deployedValue.
        //
        // The waterfall can only absorb from a tranche that HAS deployedValue
        // at the time of loss. If equity/junior had zero deployment when a loss
        // occurred (e.g. no deposits in that tranche), the loss skips them and
        // hits senior directly.  Likewise, recovery restores senior-first,
        // which can clear a senior shortfall while junior's remains.
        //
        // Therefore the ordering invariant only holds among tranches that
        // have ever received deposits (totalShares > 0). A tranche with
        // zero shares was never capitalised, so having zero shortfall is
        // correct even when a more-senior tranche has a shortfall.

        uint256 seniorShortfall = tranchePool.getSeniorPrincipalShortfall();
        uint256 juniorShortfall = tranchePool.getJuniorPrincipalShortfall();
        uint256 equityShortfall = tranchePool.getEquityPrincipalShortfall();

        bool juniorCapitalised = tranchePool.getTotalJuniorShares() > 0;
        bool equityCapitalised = tranchePool.getTotalEquityShares() > 0;

        // If senior has a shortfall, subordinate tranches that were
        // capitalised must also show a shortfall (they absorb first).
        if (seniorShortfall > 0) {
            if (juniorCapitalised) {
                assertTrue(
                    juniorShortfall > 0,
                    "Senior has shortfall but capitalised junior has none"
                );
            }
            if (equityCapitalised) {
                assertTrue(
                    equityShortfall > 0,
                    "Senior has shortfall but capitalised equity has none"
                );
            }
        }
        // If junior has a shortfall, equity (if capitalised) must also.
        if (juniorShortfall > 0 && equityCapitalised) {
            assertTrue(
                equityShortfall > 0,
                "Junior has shortfall but capitalised equity has none"
            );
        }
    }

    function invariant__interestWaterfallSeniorPriority() public view {
        uint256 seniorAccrued = tranchePool.seniorAccruedInterest();
        uint256 seniorTarget = tranchePool.seniorTargetInterest();
        uint256 juniorAccrued = tranchePool.juniorAccruedInterest();
        uint256 juniorTarget = tranchePool.juniorTargetInterest();

        assertLe(
            seniorAccrued,
            seniorTarget,
            "Senior accrued interest exceeds target"
        );
        assertLe(
            juniorAccrued,
            juniorTarget,
            "Junior accrued interest exceeds target"
        );
    }

    function invariant__juniorShareToIdleOpen() public view {
        if (tranchePool.getPoolState() == ITranchePool.PoolState.OPEN) {
            assertEq(
                tranchePool.getTotalJuniorShares(),
                tranchePool.getJuniorTrancheIdleValue(),
                "Junior: Shares != Idle in OPEN state"
            );
            assertEq(
                tranchePool.getTotalEquityShares(),
                tranchePool.getEquityTrancheIdleValue(),
                "Equity: Shares != Idle in OPEN state"
            );
        }
    }

    function invariant__allocationRatiosSumTo100OrLess() public view {
        assertLe(
            tranchePool.getSeniorAllocationRatio() +
                tranchePool.getJuniorAllocationRatio(),
            100,
            "Allocation factors exceed 100%"
        );
    }

    function invariant__originationFeeBounded() public view {
        uint256 nextId = loanEngine.getNextLoanId();
        uint256 maxFee = loanEngine.getMaxOriginationFeeBps();
        for (uint256 i = 1; i < nextId; i++) {
            ILoanEngine.Loan memory loan = loanEngine.getLoanDetails(i);
            assertLe(
                loan.originationFeeBps,
                maxFee,
                "Loan origination fee exceeds max"
            );
        }
    }

    function invariant__aprSanityBound() public view {
        uint256 nextId = loanEngine.getNextLoanId();
        for (uint256 i = 1; i < nextId; i++) {
            ILoanEngine.Loan memory loan = loanEngine.getLoanDetails(i);
            if (loan.state != ILoanEngine.LoanState.NONE) {
                assertGt(loan.aprBps, 0, "Loan APR is zero");
                assertLt(loan.aprBps, 10000, "Loan APR >= 100%");
            }
        }
    }

    function invariant__globalConservationLaw() public view {
        uint256 poolBalance = ERC20Mock(usdt).balanceOf(address(tranchePool));
        uint256 totalLiabilities = tranchePool.getTotalIdleValue() +
            tranchePool.getTotalUnclaimedInterest() +
            tranchePool.getProtocolRevenue();

        // The interest index pattern uses two integer divisions:
        //   indexDelta  = (paidAmount * 1e18) / totalShares   (truncates)
        //   claimable   = (userShares * delta) / 1e18         (truncates)
        // Each repayment can leave up to 1 wei of irrecoverable dust in
        // s_totalUnclaimedInterest. This dust is a liability that can never
        // be claimed, so totalLiabilities may exceed poolBalance by a small
        // amount proportional to the number of repayments processed.
        //
        // Allow up to 10 wei tolerance (covers multiple repayment rounds).
        uint256 tolerance = 10;

        assertGe(
            poolBalance + tolerance,
            totalLiabilities,
            "Token balance far below liabilities (value leak detected)"
        );
        assertGe(
            totalLiabilities,
            poolBalance,
            "Token balance exceeds liabilities (phantom tokens detected)"
        );
    }

    function invariant__poolSolvency() public view {
        uint256 poolBalance = ERC20Mock(usdt).balanceOf(address(tranchePool));
        uint256 totalClaims = tranchePool.getTotalIdleValue() +
            tranchePool.getTotalUnclaimedInterest();
        // The pool token balance must always cover all obligations
        assertGe(
            poolBalance,
            totalClaims,
            "Pool is insolvent: balance < obligations"
        );
    }
}
