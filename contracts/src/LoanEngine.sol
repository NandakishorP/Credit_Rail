// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import {ICreditPolicy} from "./interfaces/ICreditPolicy.sol";
import {IVerifier} from "./interfaces/IVerifier.sol";
import {ITranchePool} from "./interfaces/ITranchePool.sol";
import {ReentrancyGuard} from "@openzeppelin/contracts/utils/ReentrancyGuard.sol";
import {SafeERC20, IERC20} from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import {TranchePool} from "./TranchePool.sol";

contract LoanEngine is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;
    /*//////////////////////////////////////////////////////////////
                        ERRORS
    //////////////////////////////////////////////////////////////*/

    error LoanEngine__PolicyNotFrozen(uint256 policyVersion);
    error LoanEngine__InvalidProof();
    error LoanEngine__LoanTierIsNotInPolicy(
        uint256 policyVersion,
        uint8 tierId
    );
    error LoanEngine__InvalidLoanParameters(
        uint256 loanId,
        uint256 principalIssued,
        uint256 aprBps,
        uint256 termDays
    );
    error LoanEngine__MaxOriginationFeeExceeded(
        uint256 loanId,
        uint256 originationFeeBps,
        uint256 maxOriginationFeeBps
    );
    error LoanEngine__PoolNotDeployed();
    error LoanEngine__InvalidOffRampingEntity(address entity);
    error LoanEngine__LoanExists(uint256 loanId);
    error LoanEngine__LoanIsNotInCreatedState(uint256 loanId);
    error LoanEngine__LoanIsNotActive(uint256 loanId);
    error LoanEngine__LoanIsNotDefaulted(uint256 loanId);
    error LoanEngine__InvalidRepayment();
    error LoanEngine__ZeroRecovery();
    error LoanEngine__LoanNotRecoverable(uint256 loanId);
    error LoanEngine__ZeroLossOnWriteOff(uint256 loanId);
    modifier isWhiteListedOffRampingEntity(address entity) {
        _isWhiteListedOffRampingEntity(entity);
        _;
    }

    function _isWhiteListedOffRampingEntity(address entity) internal view {
        if (!whitelistedOffRampingEntities[entity]) {
            revert LoanEngine__InvalidOffRampingEntity(entity);
        }
    }

    modifier isWhiteListedRecoveryAgent(address agent) {
        _isWhiteListedRecoveryAgent(agent);
        _;
    }

    function _isWhiteListedRecoveryAgent(address agent) internal view {
        if (!whitelistedRecoveryAgents[agent]) {
            revert LoanEngine__InvalidOffRampingEntity(agent);
        }
    }

    modifier isWhiteListedRepaymentAgent(address agent) {
        _isWhiteListedRepaymentAgent(agent);
        _;
    }

    function _isWhiteListedRepaymentAgent(address agent) internal view {
        if (!whitelistedRepaymentAgents[agent]) {
            revert LoanEngine__InvalidOffRampingEntity(agent);
        }
    }

    ICreditPolicy public creditPolicyContract;
    IVerifier loanProofVerifier;
    ITranchePool tranchePool;

    mapping(uint256 loanId => Loan) public s_loans;
    mapping(uint256 loanId => uint256) public s_originationFees;
    mapping(address whitelistedOffRampingEntity => bool)
        public whitelistedOffRampingEntities;
    mapping(address whiteListedRecoveryAgent => bool)
        public whitelistedRecoveryAgents;

    mapping(address whiteListedRepaymentAgent => bool)
        public whitelistedRepaymentAgents;
    uint256 public s_nextLoanId = 1;
    uint256 public s_maxOriginationFeeBps;
    address public s_stableCoinAddress;

    enum LoanState {
        NONE,
        CREATED,
        ACTIVE,
        REPAID,
        DEFAULTED,
        WRITTEN_OFF
    }

    struct Loan {
        // Identity
        uint256 loanId;
        bytes32 borrowerCommitment;
        uint256 policyVersion;
        uint8 tierId;
        // Economics
        uint256 principalIssued;
        uint256 principalOutstanding;
        uint256 aprBps;
        uint256 originationFeeBps;
        // Interest accounting
        uint256 interestAccrued;
        uint256 interestPaid;
        uint256 lastAccrualTimestamp;
        // Timing
        uint256 startTimestamp;
        uint256 maturityTimestamp;
        uint256 termDays;
        // State
        LoanState state;
        uint256 totalRecovered;
    }

    /*//////////////////////////////////////////////////////////////
                        EVENTS
    //////////////////////////////////////////////////////////////*/

    event LoanCreated(
        uint256 indexed loanId,
        bytes32 borrowerCommitment,
        uint256 principalIssued,
        uint8 tierId,
        uint256 timestamp
    );

    event LoanActivated(
        uint256 indexed loanId,
        uint256 principalIssued,
        uint256 timestamp,
        uint256 startTimestamp,
        uint256 maturityTimestamp
    );

    event LoanRepaid(
        uint256 indexed loanId,
        uint256 principalRepaid,
        uint256 interestRepaid,
        uint256 timestamp
    );

    event LoanClosed(uint256 indexed loanId, uint256 timestamp);

    event LoanDefaulted(
        uint256 indexed loanId,
        bytes32 reasonHash,
        uint256 timestamp
    );

    event LoanWrittenOff(uint256 indexed loanId, uint256 timestamp);

    event LoanRecovered(
        uint256 indexed loanId,
        uint256 amount,
        uint256 timestamp
    );

    constructor(
        address _creditPolicyContract,
        address _loanProofVerifier,
        uint256 _maxOriginationFeeBps,
        address _tranchePool,
        address _stableCoinAddress
    ) Ownable(msg.sender) {
        creditPolicyContract = ICreditPolicy(_creditPolicyContract);
        loanProofVerifier = IVerifier(_loanProofVerifier);
        s_maxOriginationFeeBps = _maxOriginationFeeBps;
        tranchePool = ITranchePool(_tranchePool);
        s_stableCoinAddress = _stableCoinAddress;
    }

    // A notarization step that records a policy-compliant loan intent on-chain
    // TODO: public inputs needed to be verified against the contract state
    // will be implemented after the public inputs structure is finalized
    function createLoan(
        bytes32 borrowerCommitment,
        uint256 policyVersion,
        uint8 tierId,
        uint256 principalIssued,
        uint256 aprBps,
        uint256 originationFeeBps,
        uint256 termDays,
        bytes calldata proofData,
        bytes32[] calldata publicInputs
    ) external onlyOwner {
        if (s_loans[s_nextLoanId].state != LoanState.NONE) {
            revert LoanEngine__LoanExists(s_nextLoanId);
        }
        // Implementation goes here
        if (!creditPolicyContract.isPolicyFrozen(policyVersion)) {
            revert LoanEngine__PolicyNotFrozen(policyVersion);
        }

        if (!creditPolicyContract.tierExistsInPolicy(policyVersion, tierId)) {
            revert LoanEngine__LoanTierIsNotInPolicy(policyVersion, tierId);
        }

        if (loanProofVerifier.verify(proofData, publicInputs) == false) {
            revert LoanEngine__InvalidProof();
        }

        if (
            tranchePool.getPoolState() != TranchePool.PoolState.DEPLOYED &&
            tranchePool.getPoolState() != TranchePool.PoolState.COMMITED
        ) {
            revert LoanEngine__PoolNotDeployed();
        }

        if (originationFeeBps > s_maxOriginationFeeBps) {
            revert LoanEngine__MaxOriginationFeeExceeded(
                s_nextLoanId,
                originationFeeBps,
                s_maxOriginationFeeBps
            );
        }

        if (principalIssued == 0 || aprBps == 0 || termDays == 0) {
            revert LoanEngine__InvalidLoanParameters(
                s_nextLoanId,
                principalIssued,
                aprBps,
                termDays
            );
        }

        Loan memory newLoan = Loan({
            loanId: s_nextLoanId,
            borrowerCommitment: borrowerCommitment,
            policyVersion: policyVersion,
            tierId: tierId,
            principalIssued: principalIssued,
            principalOutstanding: 0,
            aprBps: aprBps,
            originationFeeBps: originationFeeBps,
            interestAccrued: 0,
            interestPaid: 0,
            lastAccrualTimestamp: 0,
            startTimestamp: 0,
            maturityTimestamp: 0,
            termDays: termDays,
            state: LoanState.CREATED,
            totalRecovered: 0
        });

        s_loans[s_nextLoanId++] = newLoan;

        emit LoanCreated(
            newLoan.loanId,
            borrowerCommitment,
            principalIssued,
            tierId,
            block.timestamp
        );
    }

    /*
        preconditions
        - onlyOwner
        - loan must already exist
        - loan.state == CREATED
    */
    function activateLoan(
        uint256 loanId,
        address receivingEntity,
        address feeManager
    )
        external
        onlyOwner
        isWhiteListedOffRampingEntity(receivingEntity)
        nonReentrant
    {
        // Implementation goes here
        Loan storage loan = s_loans[loanId];

        if (loan.state != LoanState.CREATED) {
            revert LoanEngine__LoanIsNotInCreatedState(loanId);
        }
        loan.principalOutstanding = loan.principalIssued;
        loan.lastAccrualTimestamp = block.timestamp;
        loan.startTimestamp = block.timestamp;
        loan.maturityTimestamp = block.timestamp + (loan.termDays * 1 days);
        loan.state = LoanState.ACTIVE;

        uint256 originationFee = (loan.principalIssued *
            loan.originationFeeBps) / 10000;

        s_originationFees[loanId] = originationFee;

        uint256 totalDisbursement = loan.principalIssued - originationFee;
        tranchePool.allocateCapital(
            totalDisbursement,
            originationFee,
            receivingEntity,
            feeManager
        );
        emit LoanActivated(
            loan.loanId,
            loan.principalIssued,
            block.timestamp,
            loan.startTimestamp,
            loan.maturityTimestamp
        );
    }

    function repayLoan(
        uint256 loanId,
        uint256 principalAmount,
        uint256 interestAmount,
        address repaymentAgent
    )
        external
        onlyOwner
        isWhiteListedRepaymentAgent(repaymentAgent)
        nonReentrant
    {
        // Implementation goes here
        Loan storage loan = s_loans[loanId];
        if (loan.state != LoanState.ACTIVE) {
            revert LoanEngine__LoanIsNotActive(loanId);
        }

        if (principalAmount == 0 && interestAmount == 0) {
            revert LoanEngine__InvalidRepayment();
        }

        _accrueInterest(loanId);
        uint256 interestDue = loan.interestAccrued;
        // any excess payment is simply ignored so it should be handled off-chain
        uint256 interestPaid = interestAmount > interestDue
            ? interestDue
            : interestAmount;
        loan.interestAccrued -= interestPaid;
        loan.interestPaid += interestPaid;
        uint256 principalDue = loan.principalOutstanding;
        uint256 principalPaid = principalAmount > principalDue
            ? principalDue
            : principalAmount;
        loan.principalOutstanding -= principalPaid;
        bool fullyRepaid = loan.principalOutstanding == 0 &&
            loan.interestAccrued == 0;

        if (fullyRepaid) {
            loan.state = LoanState.REPAID;
        }
        tranchePool.onRepayment(principalPaid, interestPaid);
        IERC20(s_stableCoinAddress).safeTransferFrom(
            repaymentAgent,
            address(tranchePool),
            principalPaid + interestPaid
        );

        emit LoanRepaid(
            loan.loanId,
            principalPaid,
            interestPaid,
            block.timestamp
        );
        if (fullyRepaid) {
            emit LoanClosed(loanId, block.timestamp);
        }
    }

    function declareDefault(
        uint256 loanId,
        bytes32 reasonHash
    ) external onlyOwner {
        // Implementation goes here
        Loan storage loan = s_loans[loanId];
        if (loan.state != LoanState.ACTIVE) {
            revert LoanEngine__LoanIsNotActive(loanId);
        }
        _accrueInterest(loanId);
        loan.state = LoanState.DEFAULTED;
        emit LoanDefaulted(loanId, reasonHash, block.timestamp);
    }

    function writeOffLoan(uint256 loanId) external onlyOwner {
        // Implementation goes here
        Loan storage loan = s_loans[loanId];
        if (loan.state != LoanState.DEFAULTED) {
            revert LoanEngine__LoanIsNotDefaulted(loanId);
        }
        uint256 loss = loan.principalOutstanding;
        if (loss == 0) {
            revert LoanEngine__ZeroLossOnWriteOff(loanId);
        }

        loan.principalOutstanding = 0;
        loan.interestAccrued = 0;
        loan.state = LoanState.WRITTEN_OFF;
        tranchePool.onLoss(loss);
        emit LoanWrittenOff(loanId, block.timestamp);
    }

    function recoverLoan(
        uint256 loanId,
        uint256 amount,
        address recoveryAgent
    ) external onlyOwner isWhiteListedRecoveryAgent(recoveryAgent) {
        Loan storage loan = s_loans[loanId];
        if (loan.state != LoanState.WRITTEN_OFF) {
            revert LoanEngine__LoanNotRecoverable(loanId);
        }
        if (amount == 0) {
            revert LoanEngine__ZeroRecovery();
        }
        loan.totalRecovered += amount;
        IERC20(s_stableCoinAddress).safeTransferFrom(
            recoveryAgent,
            address(tranchePool),
            amount
        );
        tranchePool.onRecovery(amount);
        emit LoanRecovered(loanId, amount, block.timestamp);
    }

    function _accrueInterest(uint256 loanId) internal {
        // Implementation goes here
        Loan storage loan = s_loans[loanId];
        if (loan.state != LoanState.ACTIVE) {
            revert LoanEngine__LoanIsNotActive(loanId);
        }
        uint256 timeElapsed = block.timestamp - loan.lastAccrualTimestamp;
        if (loan.principalOutstanding == 0) {
            loan.lastAccrualTimestamp = block.timestamp;
            return;
        }

        uint256 interest = (loan.principalOutstanding *
            loan.aprBps *
            timeElapsed) / (365 days * 10_000);

        if (interest > 0) {
            loan.interestAccrued += interest;
        }
        loan.lastAccrualTimestamp = block.timestamp;
    }

    // setters for contract management

    function setMaxOriginationFeeBps(
        uint256 _maxOriginationFeeBps
    ) external onlyOwner {
        s_maxOriginationFeeBps = _maxOriginationFeeBps;
    }

    function setWhitelistedOffRampingEntity(
        address entity,
        bool isWhitelisted
    ) external onlyOwner {
        whitelistedOffRampingEntities[entity] = isWhitelisted;
    }

    function setWhitelistedRecoveryAgent(
        address agent,
        bool isWhitelisted
    ) external onlyOwner {
        whitelistedRecoveryAgents[agent] = isWhitelisted;
    }

    function setWhitelistedRepaymentAgent(
        address agent,
        bool isWhitelisted
    ) external onlyOwner {
        whitelistedRepaymentAgents[agent] = isWhitelisted;
    }
}
