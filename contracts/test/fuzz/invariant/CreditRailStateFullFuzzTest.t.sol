// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {LoanEngine} from "../../../src/LoanEngine.sol";
import {TranchePool} from "../../../src/TranchePool.sol";
import {CreditPolicy} from "../../../src/CreditPolicy.sol";
import {ICreditPolicy} from "../../../src/interfaces/ICreditPolicy.sol";
import {MockLoanProofVerifier} from "../../mocks/MockLoanProofVerifier.sol";
import {MockPoseidon2} from "../../mocks/MockPoseidon2.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";

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
    uint256 public USDT = 1e18;
    address public deployer = makeAddr("deployer");

    function setUp() public {
        // Change from constructor to setUp
        vm.deal(deployer, 100 ether);
        vm.startPrank(deployer);
        usdt = new ERC20Mock();
        tranchePool = new TranchePool(address(usdt));
        tranchePool.setMaxAllocationCapSeniorTranche(5_00_00_000 * USDT);
        tranchePool.setMaxAllocationCapJuniorTranche(3_00_00_000 * USDT);
        tranchePool.setMaxAllocationCapEquityTranche(2_00_00_000 * USDT);
        tranchePool.setMinimumDepositAmountSeniorTranche(10_00_000 * USDT);
        tranchePool.setMinimumDepositAmountJuniorTranche(50_00_000 * USDT);
        tranchePool.setMinimumDepositAmountEquityTranche(1_00_00_000 * USDT);
        tranchePool.setTrancheCapitalAllocationFactorJunior(15);
        tranchePool.setTrancheCapitalAllocationFactorSenior(80);
        tranchePool.setSeniorAPR(800);
        tranchePool.setTargetJuniorAPR(1500);

        creditPolicy = new CreditPolicy();
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

        MockLoanProofVerifier mockLoanProofVerifier = new MockLoanProofVerifier();
        MockPoseidon2 mockPoseidon = new MockPoseidon2();
        loanEngine = new LoanEngine(
            address(creditPolicy),
            address(mockLoanProofVerifier),
            maxOriginationFeeBps,
            address(tranchePool),
            address(usdt),
            address(mockPoseidon)
        );
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
            LoanEngine.Loan memory loan = loanEngine.getLoanDetails(i);
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
            LoanEngine.Loan memory loan = loanEngine.getLoanDetails(i);

            // NONE and CREATED should have 0 principal outstanding
            if (
                loan.state == LoanEngine.LoanState.NONE ||
                loan.state == LoanEngine.LoanState.CREATED
            ) {
                assertEq(
                    loan.principalOutstanding,
                    0,
                    "NONE/CREATED loan has outstanding principal"
                );
            }

            // REPAID and WRITTEN_OFF must have 0 outstanding
            if (
                loan.state == LoanEngine.LoanState.REPAID ||
                loan.state == LoanEngine.LoanState.WRITTEN_OFF
            ) {
                assertEq(
                    loan.principalOutstanding,
                    0,
                    "Terminal loan has outstanding principal"
                );
            }

            // ACTIVE loans must have principalOutstanding <= principalIssued
            if (loan.state == LoanEngine.LoanState.ACTIVE) {
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
            LoanEngine.Loan memory loan = loanEngine.getLoanDetails(i);
            if (loan.state == LoanEngine.LoanState.REPAID) {
                assertEq(
                    loan.interestAccrued,
                    0,
                    "REPAID loan has remaining accrued interest"
                );
            }
            if (loan.state == LoanEngine.LoanState.WRITTEN_OFF) {
                assertEq(
                    loan.interestAccrued,
                    0,
                    "WRITTEN_OFF loan has accrued interest"
                );
            }
        }
    }
}
