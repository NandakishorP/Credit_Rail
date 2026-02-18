// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {EchidnaHandler} from "./EchidnaHandler.sol";
import {LoanEngine} from "../../../src/LoanEngine.sol";
import {ILoanEngine} from "../../../src/interfaces/ILoanEngine.sol";
import {TranchePool} from "../../../src/TranchePool.sol";
import {ITranchePool} from "../../../src/interfaces/ITranchePool.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";

/**
 * @title EchidnaTest
 * @notice Main Echidna test contract with ALL invariants from Foundry tests
 * @dev Uses EchidnaHandler for state transitions and checks invariants after each action
 */
contract EchidnaTest {
    EchidnaHandler public handler;

    constructor() {
        handler = new EchidnaHandler();
    }

    // =========================================================================
    // ECHIDNA ACTIONS (wrappers that check invariants after each action)
    // =========================================================================

    function depositSeniorTranche(uint256 amount) public {
        handler.depositSeniorTranche(amount);
        _checkAllInvariants();
    }

    function depositJuniorTranche(uint256 amount) public {
        handler.depositJuniorTranche(amount);
        _checkAllInvariants();
    }

    function depositEquityTranche(uint256 amount) public {
        handler.depositEquityTranche(amount);
        _checkAllInvariants();
    }

    function commitPool() public {
        handler.commitPool();
        _checkAllInvariants();
    }

    function createLoan(
        uint256 principalIssued,
        uint256 originationFeeBps,
        uint256 termDays
    ) public {
        handler.createLoan(principalIssued, originationFeeBps, termDays);
        _checkAllInvariants();
    }

    function activateLoan(uint256 loanId) public {
        handler.activateLoan(loanId);
        _checkAllInvariants();
    }

    function repayLoan(
        uint256 loanId,
        uint256 principalAmount,
        uint256 interestAmount
    ) public {
        handler.repayLoan(loanId, principalAmount, interestAmount);
        _checkAllInvariants();
    }

    function declareDefault(uint256 loanId) public {
        handler.declareDefault(loanId);
        _checkAllInvariants();
    }

    function writeOffLoan(uint256 loanId) public {
        handler.writeOffLoan(loanId);
        _checkAllInvariants();
    }

    function recoverLoan(uint256 loanId, uint256 amount) public {
        handler.recoverLoan(loanId, amount);
        _checkAllInvariants();
    }

    function closePool() public {
        handler.closePool();
        _checkAllInvariants();
    }

    // =========================================================================
    // MASTER INVARIANT CHECKER - calls all 12 invariants
    // =========================================================================

    function _checkAllInvariants() internal view {
        _invariant_totalIdleAndDeployedValueMatchesAccounting();
        _invariant_OutStandingPrincipalMatchesDeployed();
        _invariant_totalUnclaimedInterestAndIdleValueMatchesTotalTokenBalance();
        _invariant_totalDeployedValueMatchesSumOfIndividualTranches();
        _invariant_systemLevel_PrincipalIntegrity();
        _invariant_lossRecoveryWaterfallSymmetry();
        _invariant_totalIdleValueIntegrity();
        _invariant_seniorShareToIdleOpen();
        _invariant_loanStateConsistency();
        _invariant_interestIndexMonotonicity();
        _invariant_poolStateValidityDeployedCapital();
        _invariant_loanInterestAccounting();
    }

    // =========================================================================
    // INVARIANT 1: Total Idle And Deployed Value Matches Accounting
    // =========================================================================
    function _invariant_totalIdleAndDeployedValueMatchesAccounting()
        internal
        view
    {
        TranchePool tp = handler.tranchePool();
        uint256 left = tp.getTotalIdleValue() + tp.getTotalDeployedValue();
        uint256 right = tp.getTotalDeposited() -
            tp.getTotalLoss() +
            tp.getTotalRecovered();
        assert(left == right);
    }

    // =========================================================================
    // INVARIANT 2: Outstanding Principal Matches Deployed
    // =========================================================================
    function _invariant_OutStandingPrincipalMatchesDeployed() internal view {
        assert(
            handler.outstandingPrincipal() ==
                handler.tranchePool().getTotalDeployedValue()
        );
    }

    // =========================================================================
    // INVARIANT 3: Total Unclaimed Interest + Idle Value = Token Balance
    // =========================================================================
    function _invariant_totalUnclaimedInterestAndIdleValueMatchesTotalTokenBalance()
        internal
        view
    {
        TranchePool tp = handler.tranchePool();
        uint256 left = tp.getTotalUnclaimedInterest() +
            tp.getTotalIdleValue() +
            tp.getProtocolRevenue();
        uint256 tokenBalance = ERC20Mock(address(handler.usdt())).balanceOf(
            address(tp)
        );
        assert(left == tokenBalance);
    }

    // =========================================================================
    // INVARIANT 4: Total Deployed Value = Sum of Individual Tranches
    // =========================================================================
    function _invariant_totalDeployedValueMatchesSumOfIndividualTranches()
        internal
        view
    {
        TranchePool tp = handler.tranchePool();
        uint256 total = tp.getTotalDeployedValue();
        uint256 sum = tp.getSeniorTrancheDeployedValue() +
            tp.getJuniorTrancheDeployedValue() +
            tp.getEquityTrancheDeployedValue();
        assert(total == sum);
    }

    // =========================================================================
    // INVARIANT 5: System Level Principal Integrity
    // =========================================================================
    function _invariant_systemLevel_PrincipalIntegrity() internal view {
        LoanEngine le = handler.loanEngine();
        TranchePool tp = handler.tranchePool();

        uint256 totalOutstandingPrincipal = 0;
        uint256 nextId = le.getNextLoanId();

        for (uint256 i = 1; i < nextId; i++) {
            ILoanEngine.Loan memory loan = le.getLoanDetails(i);
            totalOutstandingPrincipal += loan.principalOutstanding;
        }

        assert(totalOutstandingPrincipal == tp.getTotalDeployedValue());
    }

    // =========================================================================
    // INVARIANT 6: Loss Recovery Waterfall Symmetry (FIXED VERSION)
    // =========================================================================
    function _invariant_lossRecoveryWaterfallSymmetry() internal view {
        TranchePool tp = handler.tranchePool();

        uint256 totalShortfall = tp.getSeniorPrincipalShortfall() +
            tp.getJuniorPrincipalShortfall() +
            tp.getEquityPrincipalShortfall();

        if (tp.getTotalRecovered() >= tp.getTotalLoss()) {
            // If we recovered more than lost, shortfall should be 0
            assert(totalShortfall == 0);
        } else {
            // Otherwise shortfall = loss - recovered
            uint256 expectedShortfall = tp.getTotalLoss() -
                tp.getTotalRecovered();
            assert(totalShortfall == expectedShortfall);
        }
    }

    // =========================================================================
    // INVARIANT 7: Total Idle Value Integrity
    // =========================================================================
    function _invariant_totalIdleValueIntegrity() internal view {
        TranchePool tp = handler.tranchePool();

        uint256 sum = tp.getSeniorTrancheIdleValue() +
            tp.getJuniorTrancheIdleValue() +
            tp.getEquityTrancheIdleValue();

        assert(sum == tp.getTotalIdleValue());
    }

    // =========================================================================
    // INVARIANT 8: Senior Share To Idle (OPEN state)
    // =========================================================================
    function _invariant_seniorShareToIdleOpen() internal view {
        TranchePool tp = handler.tranchePool();

        if (tp.getPoolState() == ITranchePool.PoolState.OPEN) {
            assert(tp.getTotalSeniorShares() == tp.getSeniorTrancheIdleValue());
        }
    }

    // =========================================================================
    // INVARIANT 9: Loan State Consistency
    // =========================================================================
    function _invariant_loanStateConsistency() internal view {
        LoanEngine le = handler.loanEngine();
        uint256 nextId = le.getNextLoanId();

        for (uint256 i = 1; i < nextId; i++) {
            ILoanEngine.Loan memory loan = le.getLoanDetails(i);

            // NONE and CREATED should have 0 principal outstanding
            if (
                loan.state == ILoanEngine.LoanState.NONE ||
                loan.state == ILoanEngine.LoanState.CREATED
            ) {
                assert(loan.principalOutstanding == 0);
            }

            // REPAID and WRITTEN_OFF must have 0 outstanding
            if (
                loan.state == ILoanEngine.LoanState.REPAID ||
                loan.state == ILoanEngine.LoanState.WRITTEN_OFF
            ) {
                assert(loan.principalOutstanding == 0);
            }

            // ACTIVE loans must have principalOutstanding <= principalIssued
            if (loan.state == ILoanEngine.LoanState.ACTIVE) {
                assert(loan.principalOutstanding <= loan.principalIssued);
            }
        }
    }

    // =========================================================================
    // INVARIANT 10: Interest Index Monotonicity
    // =========================================================================
    function _invariant_interestIndexMonotonicity() internal view {
        TranchePool tp = handler.tranchePool();

        // Indices initialize at 1e18 and can only increase
        assert(tp.getSeniorInterestIndex() >= 1e18);
        assert(tp.getJuniorInterestIndex() >= 1e18);
        assert(tp.getEquityInterestIndex() >= 1e18);
    }

    // =========================================================================
    // INVARIANT 11: Pool State Validity (Deployed Capital)
    // =========================================================================
    function _invariant_poolStateValidityDeployedCapital() internal view {
        TranchePool tp = handler.tranchePool();
        ITranchePool.PoolState state = tp.getPoolState();

        if (
            state == ITranchePool.PoolState.OPEN ||
            state == ITranchePool.PoolState.CLOSED
        ) {
            assert(tp.getTotalDeployedValue() == 0);
        }
    }

    // =========================================================================
    // INVARIANT 12: Loan Interest Accounting
    // =========================================================================
    function _invariant_loanInterestAccounting() internal view {
        LoanEngine le = handler.loanEngine();
        uint256 nextId = le.getNextLoanId();

        for (uint256 i = 1; i < nextId; i++) {
            ILoanEngine.Loan memory loan = le.getLoanDetails(i);

            if (loan.state == ILoanEngine.LoanState.REPAID) {
                assert(loan.interestAccrued == 0);
            }
            if (loan.state == ILoanEngine.LoanState.WRITTEN_OFF) {
                assert(loan.interestAccrued == 0);
            }
        }
    }

    // =========================================================================
    // ECHIDNA PROPERTIES
    // =========================================================================

    function echidna_property_alive() public pure returns (bool) {
        return true;
    }

    function echidna_check_all_invariants() public view returns (bool) {
        _checkAllInvariants();
        return true;
    }
}
