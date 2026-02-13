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
    error LoanEngine__InvalidFeeManagerEntity(address manager);
    error LoanEngine__InvalidRecoveryAgent(address agent);
    error LoanEngine__InvalidRepaymentAgent(address agent);
    error LoanEngine__InsufficientPoolLiquidity();
    error LoanEngine__ProofAlreadyUsed();
    error LoanEngine__InvalidPublicInputs();
    error LoanEngine__InvalidUnderwriterKey();
    error LoanEngine__ProofExpired(uint256 proofTimestamp, uint256 currentTimestamp);
    error LoanEngine__ProofFromFuture(uint256 proofTimestamp, uint256 currentTimestamp);
    error LoanEngine__IndustryExcluded(uint256 policyVersion, bytes32 industry);
    error LoanEngine__InvalidPublicInputsLength();

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
            revert LoanEngine__InvalidRecoveryAgent(agent);
        }
    }

    modifier isWhiteListedRepaymentAgent(address agent) {
        _isWhiteListedRepaymentAgent(agent);
        _;
    }

    function _isWhiteListedRepaymentAgent(address agent) internal view {
        if (!whitelistedRepaymentAgents[agent]) {
            revert LoanEngine__InvalidRepaymentAgent(agent);
        }
    }

    modifier isWhiteListedFeeManager(address manager) {
        _isWhiteListedFeeManager(manager);
        _;
    }

    function _isWhiteListedFeeManager(address manager) internal view {
        if (!whitelistedFeeManagers[manager]) {
            revert LoanEngine__InvalidFeeManagerEntity(manager);
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

    mapping(address whiteListedFeeManager => bool)
        public whitelistedFeeManagers;
    mapping(bytes32 nullifierHash => bool) public s_nullifierHashes;
    uint256 public s_nextLoanId = 1;
    uint256 public s_maxOriginationFeeBps;
    address public s_stableCoinAddress;
    mapping(bytes32 => bool) public authorizedUnderwriters;
    uint256 public constant STANDARD_BPS = 100;
    uint256 public constant PROOF_MAX_AGE = 1 hours;

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

    uint256 public constant POLICY_VERSION_HASH_INDEX = 0;
    uint256 public constant BORROWER_COMMITMENT_INDEX = 1;
    uint256 public constant UNDERWRITER_KEY_X_INDEX = 2;
    uint256 public constant UNDERWRITER_KEY_Y_INDEX = 3;
    uint256 public constant TIER_ID_INDEX = 4;
    uint256 public constant PRINCIPAL_ISSUED_INDEX = 5;
    uint256 public constant APR_BPS_INDEX = 6;
    uint256 public constant ORIGINATION_FEE_BPS_INDEX = 7;
    uint256 public constant TERM_DAYS_INDEX = 8;
    uint256 public constant INDUSTRY_INDEX = 9;
    uint256 public constant GENERATION_TIMESTAMP_INDEX = 10;
    uint256 public constant LOAN_ID_INDEX = 11;
    uint256 public constant NULLIFIER_HASH_INDEX = 12;
    uint256 public constant TOTAL_PUBLIC_INPUTS = 13;

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

    event UnderwriterAuthorizationUpdated(
        bytes32 indexed keyHash,
        bytes32 keyX,
        bytes32 keyY,
        bool isAuthorized,
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
    // preconditions
    // borrowerCommitment should match the publicinput commitment
    // all the parameteres should match the public inputs
    function createLoan(
        bytes32 borrowerCommitment,
        bytes32 nullifierHash,
        uint256 policyVersion,
        uint8 tierId,
        uint256 principalIssued,
        uint256 aprBps,
        uint256 originationFeeBps,
        uint256 termDays,
        bytes32 industry,
        bytes calldata proofData,
        bytes32[] calldata publicInputs
    ) external onlyOwner {
        if(publicinput.length != TOTAL_PUBLIC_INPUTS){
            revert LoanEngine__InvalidPublicInputsLength();
        }
        if (
            tranchePool.getPoolState() != TranchePool.PoolState.DEPLOYED &&
            tranchePool.getPoolState() != TranchePool.PoolState.COMMITED
        ) {
            revert LoanEngine__PoolNotDeployed();
        }
        if (s_loans[s_nextLoanId].state != LoanState.NONE) {
            revert LoanEngine__LoanExists(s_nextLoanId);
        }
        // Implementation goes here
        if (!creditPolicyContract.isPolicyFrozen(policyVersion)) {
            revert LoanEngine__PolicyNotFrozen(policyVersion);
        }

        if (creditPolicyContract.isIndustryExcluded(policyVersion, industry)) {
            revert LoanEngine__IndustryExcluded(policyVersion, industry);
        }

        if (!creditPolicyContract.tierExistsInPolicy(policyVersion, tierId)) {
            revert LoanEngine__LoanTierIsNotInPolicy(policyVersion, tierId);
        }

        if (s_nullifierHashes[nullifierHash]) {
            revert LoanEngine__ProofAlreadyUsed();
        }

        // Verify that the proof was generated using the correct policy version hash
        // publicInputs[0] must correspond to the policy_version_hash from the circuit
        if (publicInputs[POLICY_VERSION_HASH_INDEX] != creditPolicyContract.policyScopeHash(policyVersion)) {
             revert LoanEngine__InvalidPublicInputs();
        }

        if(publicInputs[BORROWER_COMMITMENT_INDEX] != borrowerCommitment){
            revert LoanEngine__InvalidPublicInputs();
        }

        bytes32 underwriterKeyHash = keccak256(abi.encodePacked(publicInputs[UNDERWRITER_KEY_X_INDEX], publicInputs[UNDERWRITER_KEY_Y_INDEX]));
        if (!authorizedUnderwriters[underwriterKeyHash]) {
            revert LoanEngine__InvalidUnderwriterKey();
        }

        if(uint8(uint256(publicInputs[TIER_ID_INDEX])) != tierId){
            revert LoanEngine__InvalidPublicInputs();
        }

        if(uint256(publicInputs[PRINCIPAL_ISSUED_INDEX]) != principalIssued){
            revert LoanEngine__InvalidPublicInputs();
        }

        if(uint256(publicInputs[APR_BPS_INDEX]) != aprBps){
            revert LoanEngine__InvalidPublicInputs();
        }

        if(uint256(publicInputs[ORIGINATION_FEE_BPS_INDEX]) != originationFeeBps){
            revert LoanEngine__InvalidPublicInputs();
        }

        if(uint256(publicInputs[TERM_DAYS_INDEX]) != termDays){
            revert LoanEngine__InvalidPublicInputs();
        }

        if(publicInputs[INDUSTRY_INDEX] != industry){
            revert LoanEngine__InvalidPublicInputs();
        }

        if(publicInputs[LOAN_ID_INDEX] != s_nextLoanId){
            revert LoanEngine__InvalidPublicInputs();
        }

        if(publicInputs[NULLIFIER_HASH_INDEX] != nullifierHash){
            revert LoanEngine__InvalidPublicInputs();
        }

        uint256 proofTimestamp = uint256(publicInputs[GENERATION_TIMESTAMP_INDEX]);
        if (proofTimestamp > block.timestamp) {
            revert LoanEngine__ProofFromFuture(proofTimestamp, block.timestamp);
        }
        // ALLOW A DRIFT OF PROOF_MAX_AGE
        if (block.timestamp - proofTimestamp > PROOF_MAX_AGE) {
            revert LoanEngine__ProofExpired(proofTimestamp, block.timestamp);
        }

        if (principalIssued == 0 || aprBps == 0 || termDays == 0) {
            revert LoanEngine__InvalidLoanParameters(
                s_nextLoanId,
                principalIssued,
                aprBps,
                termDays
            );
        }

        if (originationFeeBps > s_maxOriginationFeeBps) {
            revert LoanEngine__MaxOriginationFeeExceeded(
                s_nextLoanId,
                originationFeeBps,
                s_maxOriginationFeeBps
            );
        }

        if (principalIssued > tranchePool.getTotalIdleValue()) {
            revert LoanEngine__InsufficientPoolLiquidity();
        }

        if (loanProofVerifier.verify(proofData, publicInputs) == false) {
            revert LoanEngine__InvalidProof();
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
            totalRecovered: 0,
            seniorPrincipalAllocated: 0,
            juniorPrincipalAllocated: 0
        });

        s_loans[s_nextLoanId++] = newLoan;
        s_nullifierHashes[nullifierHash] = true;

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
        isWhiteListedFeeManager(feeManager)
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

        if (loan.principalIssued > tranchePool.getTotalIdleValue()) {
            revert LoanEngine__InsufficientPoolLiquidity();
        }

        uint256 totalDisbursement = loan.principalIssued - originationFee;
        (uint256 seniorAmount, uint256 juniorAmount, ) = tranchePool
            .allocateCapital(
                totalDisbursement,
                originationFee,
                receivingEntity,
                feeManager
            );
        loan.seniorPrincipalAllocated = seniorAmount;

        loan.juniorPrincipalAllocated = juniorAmount;

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
        Loan storage loan = s_loans[loanId];
        if (loan.state != LoanState.ACTIVE) {
            revert LoanEngine__LoanIsNotActive(loanId);
        }

        uint256 totalPayment = principalAmount + interestAmount;
        if (totalPayment == 0) {
            revert LoanEngine__InvalidRepayment();
        }

        _accrueInterest(loanId);

        // 1️⃣ Transfer funds to pool (settlement layer)
        IERC20(s_stableCoinAddress).safeTransferFrom(
            repaymentAgent,
            address(tranchePool),
            totalPayment
        );

        // 2️⃣ Interest first
        uint256 interestDue = loan.interestAccrued;
        uint256 interestPaid = totalPayment > interestDue
            ? interestDue
            : totalPayment;

        // 3️⃣ Principal second
        uint256 remainingForPrincipal = totalPayment - interestPaid;
        uint256 principalDue = loan.principalOutstanding;

        uint256 principalPaid = remainingForPrincipal > principalDue
            ? principalDue
            : remainingForPrincipal;

        // 4️⃣ Update loan accounting
        loan.interestAccrued -= interestPaid;
        loan.interestPaid += interestPaid;
        loan.principalOutstanding -= principalPaid;

        bool fullyRepaid = loan.principalOutstanding == 0 &&
            loan.interestAccrued == 0;

        if (fullyRepaid) {
            loan.state = LoanState.REPAID;
        }

        tranchePool.onRepayment(principalPaid, interestPaid);

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
        uint256 interestAccrued = loan.interestAccrued;
        if (loss == 0) {
            revert LoanEngine__ZeroLossOnWriteOff(loanId);
        }

        loan.principalOutstanding = 0;
        loan.interestAccrued = 0;
        loan.state = LoanState.WRITTEN_OFF;
        tranchePool.onLoss(loss, interestAccrued);
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
        loan.lastAccrualTimestamp = block.timestamp;
        if (interest > 0) {
            loan.interestAccrued += interest;
            tranchePool.onInterestAccrued(interest);
        }
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

    function setWhitelistedFeeManager(
        address manager,
        bool isWhitelisted
    ) external onlyOwner {
        whitelistedFeeManagers[manager] = isWhitelisted;
    }

    function getMaxOriginationFeeBps() external view returns (uint256) {
        return s_maxOriginationFeeBps;
    }

    

    function setUnderwriterAuthorization(
        bytes32 keyX,
        bytes32 keyY,
        bool isAuthorized
    ) external onlyOwner {
        bytes32 keyHash = keccak256(abi.encodePacked(keyX, keyY));
        authorizedUnderwriters[keyHash] = isAuthorized;
        emit UnderwriterAuthorizationUpdated(keyHash, keyX, keyY, isAuthorized, block.timestamp);
    }

    function getNextLoanId() external view returns (uint256) {
        return s_nextLoanId;
    }

    function getLoanDetails(
        uint256 loanId
    ) external view returns (Loan memory) {
        return s_loans[loanId];
    }
}
