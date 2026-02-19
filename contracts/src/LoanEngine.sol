// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {AccessControl} from "@openzeppelin/contracts/access/AccessControl.sol";
import {Pausable} from "@openzeppelin/contracts/utils/Pausable.sol";
import {ICreditPolicy} from "./interfaces/ICreditPolicy.sol";
import {IVerifier} from "./interfaces/IVerifier.sol";
import {ITranchePool} from "./interfaces/ITranchePool.sol";
import {ILoanEngine} from "./interfaces/ILoanEngine.sol";
import {ReentrancyGuard} from "@openzeppelin/contracts/utils/ReentrancyGuard.sol";
import {SafeERC20, IERC20} from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import {TranchePool} from "./TranchePool.sol";
import {IPoseidon2} from "./interfaces/IPoseidon2.sol";
import {Field} from "@poseidon2-evm/Field.sol";

contract LoanEngine is AccessControl, ReentrancyGuard, Pausable, ILoanEngine {
    using SafeERC20 for IERC20;

    /*//////////////////////////////////////////////////////////////
                            ACCESS CONTROL ROLES
    //////////////////////////////////////////////////////////////*/

    bytes32 public constant UNDERWRITER_ROLE = keccak256("UNDERWRITER_ROLE");
    bytes32 public constant SERVICER_ROLE = keccak256("SERVICER_ROLE");
    bytes32 public constant RISK_ADMIN_ROLE = keccak256("RISK_ADMIN_ROLE");
    bytes32 public constant CONFIG_ADMIN_ROLE = keccak256("CONFIG_ADMIN_ROLE");
    bytes32 public constant EMERGENCY_ADMIN_ROLE =
        keccak256("EMERGENCY_ADMIN_ROLE");

    /*//////////////////////////////////////////////////////////////
                                MODIFIERS
    //////////////////////////////////////////////////////////////*/

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

    ICreditPolicy public immutable i_creditPolicy;
    IVerifier public immutable i_loanProofVerifier;
    ITranchePool public immutable i_tranchePool;

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
    address public immutable i_stableCoin;
    mapping(bytes32 => bool) public authorizedUnderwriters;
    uint256 public constant PROOF_MAX_AGE = 1 hours;
    IPoseidon2 public immutable i_poseidon2;

    uint256 public constant POLICY_VERSION_HASH_INDEX = 0;
    uint256 public constant LOAN_HASH_INDEX = 1;
    uint256 public constant NULLIFIER_HASH_INDEX = 2;
    uint256 public constant TOTAL_PUBLIC_INPUTS = 3;

    /*//////////////////////////////////////////////////////////////
                            CONSTRUCTOR
    //////////////////////////////////////////////////////////////*/

    constructor(
        address _creditPolicyContract,
        address _loanProofVerifier,
        uint256 _maxOriginationFeeBps,
        address _tranchePool,
        address _stableCoinAddress,
        address _poseidon2
    ) {
        if (_creditPolicyContract == address(0))
            revert LoanEngine__ZeroAddress();
        if (_loanProofVerifier == address(0)) revert LoanEngine__ZeroAddress();
        if (_tranchePool == address(0)) revert LoanEngine__ZeroAddress();
        if (_stableCoinAddress == address(0)) revert LoanEngine__ZeroAddress();
        if (_poseidon2 == address(0)) revert LoanEngine__ZeroAddress();
        if (_maxOriginationFeeBps > 10_000)
            revert LoanEngine__InvalidLoanParameters(
                0,
                0,
                _maxOriginationFeeBps,
                0
            );

        i_creditPolicy = ICreditPolicy(_creditPolicyContract);
        i_loanProofVerifier = IVerifier(_loanProofVerifier);
        s_maxOriginationFeeBps = _maxOriginationFeeBps;
        i_tranchePool = ITranchePool(_tranchePool);
        i_stableCoin = _stableCoinAddress;
        i_poseidon2 = IPoseidon2(_poseidon2);

        // Grant all roles to deployer initially
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(UNDERWRITER_ROLE, msg.sender);
        _grantRole(SERVICER_ROLE, msg.sender);
        _grantRole(RISK_ADMIN_ROLE, msg.sender);
        _grantRole(CONFIG_ADMIN_ROLE, msg.sender);
        _grantRole(EMERGENCY_ADMIN_ROLE, msg.sender);
    }

    /*//////////////////////////////////////////////////////////////
                            CORE LOAN FUNCTIONS
    //////////////////////////////////////////////////////////////*/

    /// @notice Create a zero-knowledge loan commitment on-chain
    /// @dev Requires UNDERWRITER_ROLE
    function createLoan(
        CreateLoanParams calldata params,
        bytes calldata proofData,
        bytes32[] calldata publicInputs
    ) external onlyRole(UNDERWRITER_ROLE) whenNotPaused {
        if (publicInputs.length != TOTAL_PUBLIC_INPUTS) {
            revert LoanEngine__InvalidPublicInputsLength();
        }
        ITranchePool.PoolState poolState = i_tranchePool.getPoolState();
        if (
            poolState != ITranchePool.PoolState.DEPLOYED &&
            poolState != ITranchePool.PoolState.COMMITED
        ) {
            revert LoanEngine__PoolNotDeployed();
        }

        if (!i_creditPolicy.isPolicyFrozen(params.policyVersion)) {
            revert LoanEngine__PolicyNotFrozen(params.policyVersion);
        }

        if (
            i_creditPolicy.isIndustryExcluded(
                params.policyVersion,
                params.industry
            )
        ) {
            revert LoanEngine__IndustryExcluded(
                params.policyVersion,
                params.industry
            );
        }

        if (
            !i_creditPolicy.tierExistsInPolicy(
                params.policyVersion,
                params.tierId
            )
        ) {
            revert LoanEngine__LoanTierIsNotInPolicy(
                params.policyVersion,
                params.tierId
            );
        }

        if (s_nullifierHashes[params.nullifierHash]) {
            revert LoanEngine__ProofAlreadyUsed();
        }

        // Verify that the proof was generated using the correct policy version hash
        // publicInputs[0] must correspond to the policy_version_hash from the circuit
        if (
            publicInputs[POLICY_VERSION_HASH_INDEX] !=
            i_creditPolicy.policyScopeHash(params.policyVersion)
        ) {
            revert LoanEngine__InvalidPublicInputs();
        }

        if (publicInputs[NULLIFIER_HASH_INDEX] != params.nullifierHash) {
            revert LoanEngine__InvalidPublicInputs();
        }

        bytes32 underwriterKeyHash = keccak256(
            abi.encodePacked(params.underwriterKeyX, params.underwriterKeyY)
        );
        if (!authorizedUnderwriters[underwriterKeyHash]) {
            revert LoanEngine__InvalidUnderwriterKey();
        }

        // Reconstruct Loan Hash
        Field.Type[] memory inputs = new Field.Type[](11);
        inputs[0] = Field.toField(uint256(params.borrowerCommitment));
        inputs[1] = Field.toField(uint256(params.underwriterKeyX));
        inputs[2] = Field.toField(uint256(params.underwriterKeyY));
        inputs[3] = Field.toField(uint256(params.tierId));
        inputs[4] = Field.toField(params.principalIssued);
        inputs[5] = Field.toField(params.aprBps);
        inputs[6] = Field.toField(params.originationFeeBps);
        inputs[7] = Field.toField(params.termDays);
        inputs[8] = Field.toField(uint256(params.industry));
        inputs[9] = Field.toField(params.proofTimestamp);
        inputs[10] = Field.toField(s_nextLoanId);

        if (
            Field.toUint256(i_poseidon2.hash(inputs)) !=
            uint256(publicInputs[LOAN_HASH_INDEX])
        ) {
            revert LoanEngine__InvalidPublicInputs();
        }

        if (params.proofTimestamp > block.timestamp) {
            revert LoanEngine__ProofFromFuture(
                params.proofTimestamp,
                block.timestamp
            );
        }
        // ALLOW A DRIFT OF PROOF_MAX_AGE
        if (block.timestamp - params.proofTimestamp > PROOF_MAX_AGE) {
            revert LoanEngine__ProofExpired(
                params.proofTimestamp,
                block.timestamp
            );
        }

        if (
            params.principalIssued == 0 ||
            params.aprBps == 0 ||
            params.termDays == 0
        ) {
            revert LoanEngine__InvalidLoanParameters(
                s_nextLoanId,
                params.principalIssued,
                params.aprBps,
                params.termDays
            );
        }

        if (params.originationFeeBps > s_maxOriginationFeeBps) {
            revert LoanEngine__MaxOriginationFeeExceeded(
                s_nextLoanId,
                params.originationFeeBps,
                s_maxOriginationFeeBps
            );
        }

        if (params.principalIssued > i_tranchePool.getTotalIdleValue()) {
            revert LoanEngine__InsufficientPoolLiquidity();
        }

        if (i_loanProofVerifier.verify(proofData, publicInputs) == false) {
            revert LoanEngine__InvalidProof();
        }

        Loan memory newLoan = Loan({
            loanId: s_nextLoanId,
            borrowerCommitment: params.borrowerCommitment,
            policyVersion: params.policyVersion,
            tierId: params.tierId,
            principalIssued: params.principalIssued,
            principalOutstanding: 0,
            aprBps: params.aprBps,
            originationFeeBps: params.originationFeeBps,
            interestAccrued: 0,
            interestPaid: 0,
            lastAccrualTimestamp: 0,
            startTimestamp: 0,
            maturityTimestamp: 0,
            termDays: params.termDays,
            state: LoanState.CREATED,
            totalRecovered: 0,
            seniorPrincipalAllocated: 0,
            juniorPrincipalAllocated: 0
        });

        s_loans[s_nextLoanId++] = newLoan;
        s_nullifierHashes[params.nullifierHash] = true;

        emit LoanCreated(
            newLoan.loanId,
            params.borrowerCommitment,
            params.principalIssued,
            params.tierId,
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
        onlyRole(SERVICER_ROLE)
        isWhiteListedOffRampingEntity(receivingEntity)
        isWhiteListedFeeManager(feeManager)
        nonReentrant
        whenNotPaused
    {
        Loan storage loan = s_loans[loanId];

        if (loan.state != LoanState.CREATED) {
            revert LoanEngine__LoanIsNotInCreatedState(loanId);
        }

        // Cache storage reads
        uint256 principal = loan.principalIssued; // SLOAD once instead of 4x
        uint256 ts = block.timestamp;

        loan.principalOutstanding = principal;
        loan.lastAccrualTimestamp = ts;
        loan.startTimestamp = ts;
        uint256 maturity = ts + (loan.termDays * 1 days);
        loan.maturityTimestamp = maturity;
        loan.state = LoanState.ACTIVE;

        uint256 originationFee = (principal * loan.originationFeeBps) / 10000;

        s_originationFees[loanId] = originationFee;

        if (principal > i_tranchePool.getTotalIdleValue()) {
            revert LoanEngine__InsufficientPoolLiquidity();
        }

        uint256 totalDisbursement = principal - originationFee;
        (uint256 seniorAmount, uint256 juniorAmount, ) = i_tranchePool
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
            principal,
            ts,
            ts,
            maturity
        );
    }

    function repayLoan(
        uint256 loanId,
        uint256 principalAmount,
        uint256 interestAmount,
        address repaymentAgent,
        uint256 timestamp
    )
        external
        onlyRole(SERVICER_ROLE)
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

        _accrueInterest(loanId, timestamp);

        // 1. Transfer funds to pool (settlement layer)
        IERC20(i_stableCoin).safeTransferFrom(
            repaymentAgent,
            address(i_tranchePool),
            totalPayment
        );

        // Cache storage reads — avoid re-reading after writes
        uint256 interestDue = loan.interestAccrued;       // SLOAD once
        uint256 principalDue = loan.principalOutstanding;  // SLOAD once

        // 2. Interest first
        uint256 interestPaid = totalPayment > interestDue
            ? interestDue
            : totalPayment;

        // 3. Principal second
        uint256 remainingForPrincipal = totalPayment - interestPaid;
        uint256 principalPaid = remainingForPrincipal > principalDue
            ? principalDue
            : remainingForPrincipal;

        // 4. Update loan accounting — compute locally, write once
        uint256 newAccrued = interestDue - interestPaid;
        uint256 newOutstanding = principalDue - principalPaid;

        loan.interestAccrued = newAccrued;
        loan.interestPaid += interestPaid;
        loan.principalOutstanding = newOutstanding;

        bool fullyRepaid = newOutstanding == 0 && newAccrued == 0;

        if (fullyRepaid) {
            loan.state = LoanState.REPAID;
        }

        i_tranchePool.onRepayment(principalPaid, interestPaid);

        emit LoanRepaid(loan.loanId, principalPaid, interestPaid, timestamp);

        if (fullyRepaid) {
            emit LoanClosed(loanId, timestamp);
        }
    }

    function declareDefault(
        uint256 loanId,
        bytes32 reasonHash,
        uint256 timestamp
    ) external onlyRole(RISK_ADMIN_ROLE) whenNotPaused {
        // Implementation goes here
        Loan storage loan = s_loans[loanId];
        if (loan.state != LoanState.ACTIVE) {
            revert LoanEngine__LoanIsNotActive(loanId);
        }
        _accrueInterest(loanId, timestamp);
        loan.state = LoanState.DEFAULTED;
        emit LoanDefaulted(loanId, reasonHash, timestamp);
    }

    function writeOffLoan(
        uint256 loanId
    ) external onlyRole(RISK_ADMIN_ROLE) whenNotPaused {
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
        i_tranchePool.onLoss(loss, interestAccrued);
        emit LoanWrittenOff(loanId, block.timestamp);
    }

    function recoverLoan(
        uint256 loanId,
        uint256 amount,
        address recoveryAgent
    )
        external
        onlyRole(SERVICER_ROLE)
        isWhiteListedRecoveryAgent(recoveryAgent)
    {
        Loan storage loan = s_loans[loanId];
        if (loan.state != LoanState.WRITTEN_OFF) {
            revert LoanEngine__LoanNotRecoverable(loanId);
        }
        if (amount == 0) {
            revert LoanEngine__ZeroRecovery();
        }
        loan.totalRecovered += amount;
        IERC20(i_stableCoin).safeTransferFrom(
            recoveryAgent,
            address(i_tranchePool),
            amount
        );
        i_tranchePool.onRecovery(amount);
        emit LoanRecovered(loanId, amount, block.timestamp);
    }

    function _accrueInterest(uint256 loanId, uint256 timestamp) internal {
        Loan storage loan = s_loans[loanId];
        if (loan.state != LoanState.ACTIVE) {
            revert LoanEngine__LoanIsNotActive(loanId);
        }

        uint256 timeElapsed = timestamp - loan.lastAccrualTimestamp;
        uint256 outstanding = loan.principalOutstanding; // SLOAD once instead of 2x

        if (outstanding == 0) {
            loan.lastAccrualTimestamp = block.timestamp;
            return;
        }

        uint256 interest = (outstanding * loan.aprBps * timeElapsed) /
            (365 days * 10_000);
        loan.lastAccrualTimestamp = block.timestamp;
        if (interest > 0) {
            loan.interestAccrued += interest;
            i_tranchePool.onInterestAccrued(interest);
        }
    }

    // setters for contract management

    function setMaxOriginationFeeBps(
        uint256 _maxOriginationFeeBps
    ) external onlyRole(CONFIG_ADMIN_ROLE) {
        s_maxOriginationFeeBps = _maxOriginationFeeBps;
    }

    function pause() external onlyRole(EMERGENCY_ADMIN_ROLE) {
        _pause();
    }

    function unpause() external onlyRole(EMERGENCY_ADMIN_ROLE) {
        _unpause();
    }

    function setWhitelistedOffRampingEntity(
        address entity,
        bool isWhitelisted
    ) external onlyRole(CONFIG_ADMIN_ROLE) {
        if (entity == address(0)) revert LoanEngine__ZeroAddress();
        whitelistedOffRampingEntities[entity] = isWhitelisted;
    }

    function setWhitelistedRecoveryAgent(
        address agent,
        bool isWhitelisted
    ) external onlyRole(CONFIG_ADMIN_ROLE) {
        if (agent == address(0)) revert LoanEngine__ZeroAddress();
        whitelistedRecoveryAgents[agent] = isWhitelisted;
    }

    function setWhitelistedRepaymentAgent(
        address agent,
        bool isWhitelisted
    ) external onlyRole(CONFIG_ADMIN_ROLE) {
        if (agent == address(0)) revert LoanEngine__ZeroAddress();
        whitelistedRepaymentAgents[agent] = isWhitelisted;
    }

    function setWhitelistedFeeManager(
        address manager,
        bool isWhitelisted
    ) external onlyRole(CONFIG_ADMIN_ROLE) {
        if (manager == address(0)) revert LoanEngine__ZeroAddress();
        whitelistedFeeManagers[manager] = isWhitelisted;
    }

    function getMaxOriginationFeeBps() external view returns (uint256) {
        return s_maxOriginationFeeBps;
    }

    function setUnderwriterAuthorization(
        bytes32 keyX,
        bytes32 keyY,
        bool isAuthorized
    ) external onlyRole(CONFIG_ADMIN_ROLE) {
        bytes32 keyHash = keccak256(abi.encodePacked(keyX, keyY));
        authorizedUnderwriters[keyHash] = isAuthorized;
        emit UnderwriterAuthorizationUpdated(
            keyHash,
            keyX,
            keyY,
            isAuthorized,
            block.timestamp
        );
    }

    function getNextLoanId() external view returns (uint256) {
        return s_nextLoanId;
    }

    function getLoanDetails(
        uint256 loanId
    ) external view returns (Loan memory) {
        return s_loans[loanId];
    }

    function poseidon2() external view returns (IPoseidon2) {
        return i_poseidon2;
    }

    function creditPolicy() external view returns (ICreditPolicy) {
        return i_creditPolicy;
    }

    function tranchePool() external view returns (ITranchePool) {
        return i_tranchePool;
    }

    function loanProofVerifier() external view returns (IVerifier) {
        return i_loanProofVerifier;
    }

    function stableCoin() external view returns (address) {
        return i_stableCoin;
    }
}
