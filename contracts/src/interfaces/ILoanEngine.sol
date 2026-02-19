// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/**
 * @title ILoanEngine
 * @notice Interface for the LoanEngine contract managing privacy-preserving institutional credit
 */
interface ILoanEngine {
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
    error LoanEngine__InvalidFeeManagerEntity(address manager);
    error LoanEngine__InvalidRecoveryAgent(address agent);
    error LoanEngine__InvalidRepaymentAgent(address agent);
    error LoanEngine__InsufficientPoolLiquidity();
    error LoanEngine__ProofAlreadyUsed();
    error LoanEngine__InvalidPublicInputs();
    error LoanEngine__InvalidUnderwriterKey();
    error LoanEngine__ProofExpired(
        uint256 proofTimestamp,
        uint256 currentTimestamp
    );
    error LoanEngine__ProofFromFuture(
        uint256 proofTimestamp,
        uint256 currentTimestamp
    );
    error LoanEngine__IndustryExcluded(uint256 policyVersion, bytes32 industry);
    error LoanEngine__InvalidPublicInputsLength();
    error LoanEngine__ZeroAddress();

    /*//////////////////////////////////////////////////////////////
                                EVENTS
    //////////////////////////////////////////////////////////////*/

    event LoanCreated(
        uint256 indexed loanId,
        bytes32 indexed borrowerCommitment,
        uint256 principalIssued,
        uint8 indexed tierId,
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
        bytes32 indexed reasonHash,
        uint256 timestamp
    );

    event LoanWrittenOff(uint256 indexed loanId, uint256 timestamp);

    event LoanRecovered(
        uint256 indexed loanId,
        uint256 amount,
        uint256 timestamp
    );

    event UnderwriterAuthorizationUpdated(
        bytes32 indexed keyHash,
        bytes32 keyX,
        bytes32 keyY,
        bool isAuthorized,
        uint256 timestamp
    );

    event MaxOriginationFeeBpsUpdated(uint256 newMaxFeeBps);
    event WhitelistedOffRampingEntityUpdated(address indexed entity, bool isWhitelisted);
    event WhitelistedRecoveryAgentUpdated(address indexed agent, bool isWhitelisted);
    event WhitelistedRepaymentAgentUpdated(address indexed agent, bool isWhitelisted);
    event WhitelistedFeeManagerUpdated(address indexed manager, bool isWhitelisted);

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
        // allocation_ratio
        uint256 seniorPrincipalAllocated;
        uint256 juniorPrincipalAllocated;
    }

    struct CreateLoanParams {
        bytes32 borrowerCommitment;
        bytes32 nullifierHash;
        uint256 policyVersion;
        uint8 tierId;
        uint256 principalIssued;
        uint256 aprBps;
        uint256 originationFeeBps;
        uint256 termDays;
        bytes32 industry;
        bytes32 underwriterKeyX;
        bytes32 underwriterKeyY;
        uint256 proofTimestamp;
    }

    /*//////////////////////////////////////////////////////////////
                            EXTERNAL FUNCTIONS
    //////////////////////////////////////////////////////////////*/

    function createLoan(
        CreateLoanParams calldata params,
        bytes calldata proofData,
        bytes32[] calldata publicInputs
    ) external;

    function activateLoan(
        uint256 loanId,
        address receivingEntity,
        address feeManager
    ) external;

    function repayLoan(
        uint256 loanId,
        uint256 principalAmount,
        uint256 interestAmount,
        address repaymentAgent,
        uint256 timestamp
    ) external;

    function declareDefault(
        uint256 loanId,
        bytes32 reasonHash,
        uint256 timestamp
    ) external;

    function writeOffLoan(uint256 loanId) external;

    function recoverLoan(
        uint256 loanId,
        uint256 amount,
        address recoveryAgent
    ) external;

    function setWhitelistedOffRampingEntity(
        address entity,
        bool status
    ) external;

    function setWhitelistedRecoveryAgent(address agent, bool status) external;

    function setWhitelistedRepaymentAgent(address agent, bool status) external;

    function setWhitelistedFeeManager(address manager, bool status) external;

    function setMaxOriginationFeeBps(uint256 _maxOriginationFeeBps) external;

    function setUnderwriterAuthorization(
        bytes32 keyX,
        bytes32 keyY,
        bool isAuthorized
    ) external;

    function pause() external;

    function unpause() external;

    /*//////////////////////////////////////////////////////////////
                            VIEW FUNCTIONS
    //////////////////////////////////////////////////////////////*/

    function getNextLoanId() external view returns (uint256);
}
