// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import {Pausable} from "@openzeppelin/contracts/utils/Pausable.sol";
import {ReentrancyGuard} from "@openzeppelin/contracts/utils/ReentrancyGuard.sol";
import {SafeERC20, IERC20} from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import {Math} from "@openzeppelin/contracts/utils/math/Math.sol";
import {ITranchePool} from "./interfaces/ITranchePool.sol";
import {InterestMath} from "./libraries/InterestMath.sol";

/**
 * @title TranchePool
 * @notice Three-tranche capital pool with waterfall interest distribution.
 * @dev Uses a `TrancheState` struct to eliminate the 3x code duplication
 *      that previously existed for senior / junior / equity logic.
 *
 *      Tranche indices:  SENIOR = 0,  JUNIOR = 1,  EQUITY = 2
 */
contract TranchePool is ITranchePool, Ownable, Pausable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // =========================================================================
    //                           TRANCHE STATE
    // =========================================================================

    /// @dev Per-tranche accounting packed into a single struct.
    struct TrancheState {
        uint256 idleValue;
        uint256 deployedValue;
        uint256 totalShares;
        uint256 interestIndex; // 1e18 precision
        uint256 accruedInterest;
        uint256 targetInterest;
        uint256 principalShortfall;
        uint256 maxCap;
        uint256 minDeposit;
        uint256 aprBps; // only used for senior (idx 0) and junior (idx 1)
        mapping(address => uint256) shares;
        mapping(address => uint256) userIndex;
    }

    uint256 internal constant SENIOR = 0;
    uint256 internal constant JUNIOR = 1;
    uint256 internal constant EQUITY = 2;

    /// @dev The three tranches.  Access via `tranches[SENIOR]`, etc.
    TrancheState[3] internal tranches;

    // =========================================================================
    //                          GLOBAL STATE
    // =========================================================================

    mapping(address => bool) public whiteListedLps;
    mapping(address => bool) public whiteListedForEquityTranche;

    address public immutable i_stableCoin;
    address public loanEngine;

    uint256 public s_capital_allocation_factor_senior;
    uint256 public s_capital_allocation_factor_junior;

    uint256 public lastTrancheAccrualTimestamp;

    uint256 public s_protocolRevenue;
    uint256 public s_totalDeposited;
    uint256 public s_totalLoss;
    uint256 public s_totalRecovered;
    uint256 public s_totalUnclaimedInterest;

    PoolState public poolState = PoolState.OPEN;

    // =========================================================================
    //                            MODIFIERS
    // =========================================================================

    modifier isWhiteListed(address user) {
        if (!whiteListedLps[user]) revert TranchePool__NotWhiteListed(user);
        _;
    }

    modifier onlyLoanEngine(address user) {
        if (user != loanEngine) revert TranchePool__InvalidCaller(user);
        _;
    }

    modifier isWhiteListedForEquityTranche(address user) {
        if (!whiteListedForEquityTranche[user])
            revert TranchePool__NotWhiteListedForEquityTranche(user);
        _;
    }

    // =========================================================================
    //                           CONSTRUCTOR
    // =========================================================================

    constructor(address stableCoin_) Ownable(msg.sender) {
        if (stableCoin_ == address(0)) revert TranchePool__ZeroAddressError();
        i_stableCoin = stableCoin_;

        tranches[SENIOR].interestIndex = 1e18;
        tranches[JUNIOR].interestIndex = 1e18;
        tranches[EQUITY].interestIndex = 1e18;
        lastTrancheAccrualTimestamp = block.timestamp;
    }

    // =========================================================================
    //                   DEPOSIT  (external thin wrappers)
    // =========================================================================

    function depositSeniorTranche(
        uint256 amount
    ) external isWhiteListed(msg.sender) whenNotPaused nonReentrant {
        _deposit(SENIOR, amount);
        emit FundsDepositedToSeniorTranche(
            msg.sender,
            amount,
            amount,
            block.timestamp
        );
    }

    function depositJuniorTranche(
        uint256 amount
    ) external isWhiteListed(msg.sender) whenNotPaused nonReentrant {
        _deposit(JUNIOR, amount);
        emit FundsDepositedToJuniorTranche(
            msg.sender,
            amount,
            amount,
            block.timestamp
        );
    }

    function depositEquityTranche(
        uint256 amount
    )
        external
        isWhiteListedForEquityTranche(msg.sender)
        whenNotPaused
        nonReentrant
    {
        _deposit(EQUITY, amount);
        emit FundsDepositedToEquityTranche(
            msg.sender,
            amount,
            amount,
            block.timestamp
        );
    }

    // =========================================================================
    //                  WITHDRAW BY SHARES  (external thin wrappers)
    // =========================================================================

    function withdrawSeniorTranche(
        uint256 shares
    ) external isWhiteListed(msg.sender) nonReentrant {
        (uint256 amount, uint256 burned) = _withdraw(SENIOR, shares);
        emit WithdrawnFromSeniorTranche(
            msg.sender,
            amount,
            burned,
            block.timestamp
        );
    }

    function withdrawJuniorTranche(
        uint256 shares
    ) external isWhiteListed(msg.sender) nonReentrant {
        (uint256 amount, uint256 burned) = _withdraw(JUNIOR, shares);
        emit WithdrawnFromJuniorTranche(
            msg.sender,
            amount,
            burned,
            block.timestamp
        );
    }

    function withdrawEquityTranche(
        uint256 shares
    ) external isWhiteListedForEquityTranche(msg.sender) nonReentrant {
        (uint256 amount, uint256 burned) = _withdraw(EQUITY, shares);
        emit WithdrawnFromEquityTranche(
            msg.sender,
            amount,
            burned,
            block.timestamp
        );
    }

    // =========================================================================
    //                WITHDRAW BY AMOUNT  (external thin wrappers)
    // =========================================================================

    function withdrawSeniorTrancheByAmount(
        uint256 amount
    ) external isWhiteListed(msg.sender) nonReentrant {
        (uint256 withdrawn, uint256 burned) = _withdrawByAmount(SENIOR, amount);
        emit WithdrawnFromSeniorTranche(
            msg.sender,
            withdrawn,
            burned,
            block.timestamp
        );
    }

    function withdrawJuniorTrancheByAmount(
        uint256 amount
    ) external isWhiteListed(msg.sender) nonReentrant {
        (uint256 withdrawn, uint256 burned) = _withdrawByAmount(JUNIOR, amount);
        emit WithdrawnFromJuniorTranche(
            msg.sender,
            withdrawn,
            burned,
            block.timestamp
        );
    }

    function withdrawEquityTrancheByAmount(
        uint256 amount
    ) external isWhiteListedForEquityTranche(msg.sender) nonReentrant {
        (uint256 withdrawn, uint256 burned) = _withdrawByAmount(EQUITY, amount);
        emit WithdrawnFromEquityTranche(
            msg.sender,
            withdrawn,
            burned,
            block.timestamp
        );
    }

    // =========================================================================
    //                  CLAIM INTEREST  (external thin wrappers)
    // =========================================================================

    function claimSeniorInterest() external nonReentrant {
        _claimInterest(SENIOR);
    }

    function claimJuniorInterest() external nonReentrant {
        _claimInterest(JUNIOR);
    }

    function claimEquityInterest()
        external
        isWhiteListedForEquityTranche(msg.sender)
        nonReentrant
    {
        _claimInterest(EQUITY);
    }

    // =========================================================================
    //            CAPITAL ALLOCATION  (called by LoanEngine)
    // =========================================================================

    function allocateCapital(
        uint256 totalDisbursement,
        uint256 fees,
        address deployer,
        address feeManager
    ) external onlyLoanEngine(msg.sender) returns (uint256, uint256, uint256) {
        if (poolState != PoolState.COMMITED && poolState != PoolState.DEPLOYED)
            revert TranchePool__PoolIsNotCommited();

        uint256 totalAmount = totalDisbursement + fees;

        uint256 totalIdle = tranches[SENIOR].idleValue +
            tranches[JUNIOR].idleValue +
            tranches[EQUITY].idleValue;

        if (totalAmount > totalIdle)
            revert TranchePool__InsufficientLiquidity();

        uint256 targetSenior = (totalAmount *
            s_capital_allocation_factor_senior) / 100;
        uint256 targetJunior = (totalAmount *
            s_capital_allocation_factor_junior) / 100;
        uint256 targetEquity = totalAmount - targetSenior - targetJunior;

        uint256 seniorAmount = Math.min(
            targetSenior,
            tranches[SENIOR].idleValue
        );
        uint256 juniorAmount = Math.min(
            targetJunior,
            tranches[JUNIOR].idleValue
        );
        uint256 equityAmount = Math.min(
            targetEquity,
            tranches[EQUITY].idleValue
        );

        uint256 remaining = totalAmount -
            (seniorAmount + juniorAmount + equityAmount);

        // Overflow absorption: equity -> junior -> senior
        if (remaining > 0 && tranches[EQUITY].idleValue > equityAmount) {
            uint256 extra = Math.min(
                remaining,
                tranches[EQUITY].idleValue - equityAmount
            );
            equityAmount += extra;
            remaining -= extra;
        }
        if (remaining > 0 && tranches[JUNIOR].idleValue > juniorAmount) {
            uint256 extra = Math.min(
                remaining,
                tranches[JUNIOR].idleValue - juniorAmount
            );
            juniorAmount += extra;
            remaining -= extra;
        }
        if (remaining > 0 && tranches[SENIOR].idleValue > seniorAmount) {
            uint256 extra = Math.min(
                remaining,
                tranches[SENIOR].idleValue - seniorAmount
            );
            seniorAmount += extra;
            remaining -= extra;
        }
        if (remaining > 0) revert TranchePool__InsufficientLiquidity();

        if (poolState == PoolState.COMMITED) {
            poolState = PoolState.DEPLOYED;
            emit PoolStateUpdated(PoolState.DEPLOYED);
        }

        _accrueTrancheTargets();

        // Move idle -> deployed
        tranches[SENIOR].idleValue -= seniorAmount;
        tranches[JUNIOR].idleValue -= juniorAmount;
        tranches[EQUITY].idleValue -= equityAmount;
        tranches[SENIOR].deployedValue += seniorAmount;
        tranches[JUNIOR].deployedValue += juniorAmount;
        tranches[EQUITY].deployedValue += equityAmount;

        IERC20(i_stableCoin).safeTransfer(deployer, totalDisbursement);
        if (fees > 0) IERC20(i_stableCoin).safeTransfer(feeManager, fees);

        emit CapitalAllocated(
            seniorAmount,
            juniorAmount,
            equityAmount,
            block.timestamp
        );
        return (seniorAmount, juniorAmount, equityAmount);
    }

    // =========================================================================
    //                  INTEREST ACCRUAL  (called by LoanEngine)
    // =========================================================================

    function onInterestAccrued(
        uint256 interestAmount
    ) external onlyLoanEngine(msg.sender) {
        if (interestAmount == 0) return;

        _accrueTrancheTargets();

        uint256 remaining = interestAmount;

        // Senior gets up to what is owed
        uint256 seniorOwed = 0;
        if (
            tranches[SENIOR].targetInterest > tranches[SENIOR].accruedInterest
        ) {
            seniorOwed =
                tranches[SENIOR].targetInterest -
                tranches[SENIOR].accruedInterest;
        }
        uint256 seniorPaid = remaining < seniorOwed ? remaining : seniorOwed;
        if (seniorPaid > 0) {
            tranches[SENIOR].accruedInterest += seniorPaid;
            remaining -= seniorPaid;
        }

        // Junior next
        uint256 juniorOwed = 0;
        if (
            tranches[JUNIOR].targetInterest > tranches[JUNIOR].accruedInterest
        ) {
            juniorOwed =
                tranches[JUNIOR].targetInterest -
                tranches[JUNIOR].accruedInterest;
        }
        uint256 juniorPaid = remaining < juniorOwed ? remaining : juniorOwed;
        if (juniorPaid > 0) {
            tranches[JUNIOR].accruedInterest += juniorPaid;
            remaining -= juniorPaid;
        }

        // Residual -> equity
        if (remaining > 0) {
            tranches[EQUITY].accruedInterest += remaining;
        }
    }

    // =========================================================================
    //                    REPAYMENT  (called by LoanEngine)
    // =========================================================================

    function onRepayment(
        uint256 principalRepaid,
        uint256 interestRepaid
    ) external onlyLoanEngine(msg.sender) {
        if (principalRepaid == 0 && interestRepaid == 0)
            revert TranchePool__InvalidTransferAmount(0);

        _accrueTrancheTargets();

        // -- Interest waterfall (indexed) --
        uint256 remainingInterest = interestRepaid;
        s_totalUnclaimedInterest += interestRepaid;

        // 1. Senior interest
        if (
            remainingInterest > 0 &&
            tranches[SENIOR].accruedInterest > 0 &&
            tranches[SENIOR].totalShares > 0
        ) {
            uint256 seniorPaid = Math.min(
                remainingInterest,
                tranches[SENIOR].accruedInterest
            );
            tranches[SENIOR].accruedInterest -= seniorPaid;
            tranches[SENIOR].targetInterest -= Math.min(
                tranches[SENIOR].targetInterest,
                seniorPaid
            );
            tranches[SENIOR].interestIndex += InterestMath.computeIndexDelta(
                seniorPaid,
                tranches[SENIOR].totalShares
            );
            remainingInterest -= seniorPaid;
        }

        // 2. Junior interest
        if (
            remainingInterest > 0 &&
            tranches[JUNIOR].accruedInterest > 0 &&
            tranches[JUNIOR].totalShares > 0
        ) {
            uint256 juniorPaid = Math.min(
                remainingInterest,
                tranches[JUNIOR].accruedInterest
            );
            tranches[JUNIOR].accruedInterest -= juniorPaid;
            tranches[JUNIOR].targetInterest -= Math.min(
                tranches[JUNIOR].targetInterest,
                juniorPaid
            );
            tranches[JUNIOR].interestIndex += InterestMath.computeIndexDelta(
                juniorPaid,
                tranches[JUNIOR].totalShares
            );
            remainingInterest -= juniorPaid;
        }

        // 3. Equity / overflow
        if (remainingInterest > 0) {
            if (tranches[EQUITY].totalShares > 0) {
                tranches[EQUITY].interestIndex += InterestMath
                    .computeIndexDelta(
                        remainingInterest,
                        tranches[EQUITY].totalShares
                    );
                tranches[EQUITY].accruedInterest -= Math.min(
                    tranches[EQUITY].accruedInterest,
                    remainingInterest
                );
            } else if (tranches[JUNIOR].totalShares > 0) {
                tranches[JUNIOR].interestIndex += InterestMath
                    .computeIndexDelta(
                        remainingInterest,
                        tranches[JUNIOR].totalShares
                    );
            } else {
                s_protocolRevenue += remainingInterest;
            }
        }

        // -- Principal redemption (senior -> junior -> equity) --
        if (principalRepaid > 0) {
            uint256 rem = principalRepaid;
            for (uint256 i = SENIOR; i <= EQUITY; i++) {
                if (rem == 0) break;
                if (tranches[i].deployedValue > 0) {
                    uint256 pay = Math.min(rem, tranches[i].deployedValue);
                    tranches[i].deployedValue -= pay;
                    tranches[i].idleValue += pay;
                    rem -= pay;
                }
            }
            if (rem > 0) revert TranchePool__PrincipalRepaymentExceeded();
        }
    }

    // =========================================================================
    //                       LOSS  (called by LoanEngine)
    // =========================================================================

    function onLoss(
        uint256 principalLoss,
        uint256 interestAccrued
    ) external onlyLoanEngine(msg.sender) {
        if (principalLoss == 0 && interestAccrued == 0)
            revert TranchePool__ZeroValueError();

        _accrueTrancheTargets();

        // -- Cancel ghost interest (senior -> junior) --
        uint256 remainingInterest = interestAccrued;

        if (remainingInterest > 0 && tranches[SENIOR].accruedInterest > 0) {
            uint256 cancel = Math.min(
                remainingInterest,
                tranches[SENIOR].accruedInterest
            );
            tranches[SENIOR].accruedInterest -= cancel;
            remainingInterest -= cancel;
            tranches[SENIOR].targetInterest -= Math.min(
                tranches[SENIOR].targetInterest,
                cancel
            );
        }
        if (remainingInterest > 0 && tranches[JUNIOR].accruedInterest > 0) {
            uint256 cancel = Math.min(
                remainingInterest,
                tranches[JUNIOR].accruedInterest
            );
            tranches[JUNIOR].accruedInterest -= cancel;
            remainingInterest -= cancel;
            tranches[JUNIOR].targetInterest -= Math.min(
                tranches[JUNIOR].targetInterest,
                cancel
            );
        }

        // -- Principal loss waterfall (equity -> junior -> senior) --
        s_totalLoss += principalLoss;
        uint256 remaining = principalLoss;

        uint256[3] memory losses;
        // Reverse order: equity first, senior last
        for (uint256 i = EQUITY + 1; i > 0; ) {
            unchecked {
                i--;
            }
            if (remaining == 0) break;
            if (tranches[i].deployedValue > 0) {
                losses[i] = Math.min(remaining, tranches[i].deployedValue);
                tranches[i].deployedValue -= losses[i];
                tranches[i].principalShortfall += losses[i];
                remaining -= losses[i];
            }
        }

        if (remaining > 0) revert TranchePool__LossExceededCapital(remaining);

        emit LossAllocated(losses[SENIOR], losses[JUNIOR], losses[EQUITY]);
    }

    // =========================================================================
    //                    RECOVERY  (called by LoanEngine)
    // =========================================================================

    function onRecovery(uint256 amount) external onlyLoanEngine(msg.sender) {
        if (amount == 0) revert TranchePool__ZeroValueError();

        _accrueTrancheTargets();

        s_totalRecovered += amount;
        uint256 remaining = amount;

        // Restore shortfall: senior -> junior -> equity
        for (uint256 i = SENIOR; i <= EQUITY; i++) {
            if (remaining == 0) break;
            if (tranches[i].principalShortfall > 0) {
                uint256 pay = Math.min(
                    remaining,
                    tranches[i].principalShortfall
                );
                tranches[i].principalShortfall -= pay;
                tranches[i].idleValue += pay;
                remaining -= pay;
            }
        }

        // Excess -> equity
        if (remaining > 0) {
            tranches[EQUITY].idleValue += remaining;
        }

        emit RecoverAmountTransferredToTranchePool(amount, block.timestamp);
    }

    // =========================================================================
    //               INTERNAL:  PARAMETERISED DEPOSIT / WITHDRAW
    // =========================================================================

    /**
     * @dev Unified deposit logic for any tranche.
     *      Shares are minted 1:1 with amount (pool is OPEN, so idle == shares).
     */
    function _deposit(uint256 tid, uint256 amount) internal {
        if (poolState != PoolState.OPEN) revert TranchePool__PoolIsNotOpen();
        if (amount == 0) revert TranchePool__ZeroValueError();

        TrancheState storage t = tranches[tid];

        if (amount < t.minDeposit)
            revert TranchePool__LessThanDepositThreshold(amount);
        if (amount + t.idleValue > t.maxCap)
            revert TranchePool__MaxDepositCapExceeded(t.maxCap, amount);

        uint256 shares = amount;

        IERC20(i_stableCoin).safeTransferFrom(
            msg.sender,
            address(this),
            amount
        );

        t.shares[msg.sender] += shares;
        t.totalShares += shares;
        t.idleValue += amount;
        t.userIndex[msg.sender] = t.interestIndex;
        s_totalDeposited += amount;
    }

    /**
     * @dev Unified withdraw-by-shares logic.
     * @return amountToWithdraw The stablecoin amount returned to the user.
     * @return sharesToBurn     The shares that were burned.
     */
    function _withdraw(
        uint256 tid,
        uint256 shares
    ) internal returns (uint256 amountToWithdraw, uint256 sharesToBurn) {
        if (poolState != PoolState.OPEN && poolState != PoolState.CLOSED)
            revert TranchePool__WithdrawNotAllowed(poolState);

        TrancheState storage t = tranches[tid];

        uint256 userShares = t.shares[msg.sender];
        if (userShares == 0) revert TranchePool__InsufficientShares();

        if (t.userIndex[msg.sender] != t.interestIndex)
            revert TranchePool__InterestNotClaimed();

        sharesToBurn = shares == 0 ? userShares : shares;
        if (sharesToBurn > userShares) revert TranchePool__InsufficientShares();

        amountToWithdraw = (sharesToBurn * t.idleValue) / t.totalShares;
        if (amountToWithdraw == 0) revert TranchePool__ZeroWithdrawal();
        if (amountToWithdraw > t.idleValue)
            revert TranchePool__InsufficientLiquidity();

        t.shares[msg.sender] -= sharesToBurn;
        t.totalShares -= sharesToBurn;
        t.idleValue -= amountToWithdraw;
        s_totalDeposited -= amountToWithdraw;

        IERC20(i_stableCoin).safeTransfer(msg.sender, amountToWithdraw);
    }

    /**
     * @dev Unified withdraw-by-amount logic.
     */
    function _withdrawByAmount(
        uint256 tid,
        uint256 amount
    ) internal returns (uint256, uint256 sharesToBurn) {
        if (poolState != PoolState.OPEN && poolState != PoolState.CLOSED)
            revert TranchePool__WithdrawNotAllowed(poolState);
        if (amount == 0) revert TranchePool__ZeroWithdrawal();

        TrancheState storage t = tranches[tid];

        if (t.userIndex[msg.sender] != t.interestIndex)
            revert TranchePool__InterestNotClaimed();

        uint256 userBalance = _getBalance(tid, msg.sender);
        if (amount > userBalance) revert TranchePool__InsufficientShares();
        if (amount > t.idleValue) revert TranchePool__InsufficientLiquidity();

        sharesToBurn = (amount * t.totalShares) / t.idleValue;
        if (sharesToBurn > t.shares[msg.sender])
            sharesToBurn = t.shares[msg.sender];

        t.shares[msg.sender] -= sharesToBurn;
        t.totalShares -= sharesToBurn;
        t.idleValue -= amount;
        s_totalDeposited -= amount;

        IERC20(i_stableCoin).safeTransfer(msg.sender, amount);
        return (amount, sharesToBurn);
    }

    /**
     * @dev Unified claim-interest logic using the global index pattern.
     */
    function _claimInterest(uint256 tid) internal {
        TrancheState storage t = tranches[tid];

        uint256 userShares = t.shares[msg.sender];
        if (userShares == 0) revert TranchePool__InsufficientShares();

        uint256 claimable = InterestMath.calculateClaimable(
            userShares,
            t.interestIndex,
            t.userIndex[msg.sender]
        );
        if (claimable == 0) revert TranchePool__ZeroWithdrawal();

        t.userIndex[msg.sender] = t.interestIndex;
        s_totalUnclaimedInterest -= claimable;

        emit InterestClaimed(tid, msg.sender, claimable);
        IERC20(i_stableCoin).safeTransfer(msg.sender, claimable);
    }

    /// @dev User's pro-rata share of idle value.
    function _getBalance(
        uint256 tid,
        address user
    ) internal view returns (uint256) {
        TrancheState storage t = tranches[tid];
        if (t.totalShares == 0) return 0;
        return (t.shares[user] * t.idleValue) / t.totalShares;
    }

    // =========================================================================
    //                     INTERNAL:  INTEREST ACCRUAL
    // =========================================================================

    function _accrueTrancheTargets() internal {
        uint256 currentTimestamp = block.timestamp;
        uint256 timeElapsed = currentTimestamp - lastTrancheAccrualTimestamp;
        if (timeElapsed == 0) return;

        tranches[SENIOR].targetInterest += InterestMath.accrueTargetInterest(
            tranches[SENIOR].deployedValue,
            tranches[SENIOR].aprBps,
            timeElapsed
        );

        tranches[JUNIOR].targetInterest += InterestMath.accrueTargetInterest(
            tranches[JUNIOR].deployedValue,
            tranches[JUNIOR].aprBps,
            timeElapsed
        );

        lastTrancheAccrualTimestamp = currentTimestamp;
    }

    // =========================================================================
    //                          ADMIN  FUNCTIONS
    // =========================================================================

    function setMinimumDepositAmountSeniorTranche(
        uint256 amount
    ) external onlyOwner {
        if (amount > tranches[SENIOR].maxCap)
            revert TranchePool__InvalidMinDepositAmount();
        tranches[SENIOR].minDeposit = amount;
        emit MinimumDepositAmountUpdated(SENIOR, amount);
    }

    function setMinimumDepositAmountJuniorTranche(
        uint256 amount
    ) external onlyOwner {
        if (amount > tranches[JUNIOR].maxCap)
            revert TranchePool__InvalidMinDepositAmount();
        tranches[JUNIOR].minDeposit = amount;
        emit MinimumDepositAmountUpdated(JUNIOR, amount);
    }

    function setMinimumDepositAmountEquityTranche(
        uint256 amount
    ) external onlyOwner {
        if (amount > tranches[EQUITY].maxCap)
            revert TranchePool__InvalidMinDepositAmount();
        tranches[EQUITY].minDeposit = amount;
        emit MinimumDepositAmountUpdated(EQUITY, amount);
    }

    function setTrancheCapitalAllocationFactorSenior(
        uint256 factor
    ) external onlyOwner {
        if (factor + s_capital_allocation_factor_junior > 100)
            revert TranchePool__InvalidAllocationRatio();
        s_capital_allocation_factor_senior = factor;
        emit CapitalAllocationFactorUpdatedSenior(factor);
    }

    function setTrancheCapitalAllocationFactorJunior(
        uint256 factor
    ) external onlyOwner {
        if (factor + s_capital_allocation_factor_senior > 100)
            revert TranchePool__InvalidAllocationRatio();
        s_capital_allocation_factor_junior = factor;
        emit CapitalAllocationFactorUpdatedJunior(factor);
    }

    function setSeniorAPR(uint256 aprbps) external onlyOwner {
        if (aprbps == 0) revert TranchePool__ZeroAPRError();
        _accrueTrancheTargets();
        tranches[SENIOR].aprBps = aprbps;
        emit TrancheAPRUpdated(SENIOR, aprbps);
    }

    function setTargetJuniorAPR(uint256 aprbps) external onlyOwner {
        if (aprbps == 0) revert TranchePool__ZeroAPRError();
        _accrueTrancheTargets();
        tranches[JUNIOR].aprBps = aprbps;
        emit TrancheAPRUpdated(JUNIOR, aprbps);
    }

    function setPoolState(PoolState newState) external onlyOwner {
        if (uint256(newState) < uint256(poolState))
            revert TranchePool__InvalidStateTransition(newState);

        if (newState == PoolState.CLOSED) {
            if (getTotalDeployedValue() > 0)
                revert TranchePool__DeployedCapitalExists();
        }

        poolState = newState;
        emit PoolStateUpdated(newState);
    }

    function setLoanEngine(address _loanEngine) external onlyOwner {
        if (_loanEngine == address(0)) revert TranchePool__ZeroAddressError();
        loanEngine = _loanEngine;
        emit LoanEngineUpdated(_loanEngine);
    }

    function setMaxAllocationCapSeniorTranche(
        uint256 amount
    ) external onlyOwner {
        if (amount == 0) revert TranchePool__ZeroValueError();
        if (amount < tranches[SENIOR].minDeposit)
            revert TranchePool__InvalidMaxCapAmount();
        tranches[SENIOR].maxCap = amount;
        emit MaxAllocationCapUpdated(SENIOR, amount);
    }

    function setMaxAllocationCapJuniorTranche(
        uint256 amount
    ) external onlyOwner {
        if (amount == 0) revert TranchePool__ZeroValueError();
        if (amount < tranches[JUNIOR].minDeposit)
            revert TranchePool__InvalidMaxCapAmount();
        tranches[JUNIOR].maxCap = amount;
        emit MaxAllocationCapUpdated(JUNIOR, amount);
    }

    function setMaxAllocationCapEquityTranche(
        uint256 amount
    ) external onlyOwner {
        if (amount == 0) revert TranchePool__ZeroValueError();
        if (amount < tranches[EQUITY].minDeposit)
            revert TranchePool__InvalidMaxCapAmount();
        tranches[EQUITY].maxCap = amount;
        emit MaxAllocationCapUpdated(EQUITY, amount);
    }

    function updateWhitelist(address user, bool status) external onlyOwner {
        whiteListedLps[user] = status;
        emit WhitelistUpdated(user, status);
    }

    function updateEquityTrancheWhiteList(
        address user,
        bool status
    ) external onlyOwner {
        whiteListedForEquityTranche[user] = status;
        emit EquityWhitelistUpdated(user, status);
    }

    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }

    // =========================================================================
    //                  VIEW / GETTER  FUNCTIONS
    //  (backward-compatible with existing tests and external callers)
    // =========================================================================

    // -- Balances --
    function getSeniorTrancheBalance(
        address user
    ) public view returns (uint256) {
        return _getBalance(SENIOR, user);
    }

    function getJuniorTrancheBalance(
        address user
    ) public view returns (uint256) {
        return _getBalance(JUNIOR, user);
    }

    function getEquityTrancheBalance(
        address user
    ) public view returns (uint256) {
        return _getBalance(EQUITY, user);
    }

    // -- Shares --
    function getSeniorTrancheShares(
        address user
    ) external view returns (uint256) {
        return tranches[SENIOR].shares[user];
    }

    function getJuniorTrancheShares(
        address user
    ) external view returns (uint256) {
        return tranches[JUNIOR].shares[user];
    }

    function getEquityTrancheShares(
        address user
    ) external view returns (uint256) {
        return tranches[EQUITY].shares[user];
    }

    function getTotalSeniorShares() external view returns (uint256) {
        return tranches[SENIOR].totalShares;
    }

    function getTotalJuniorShares() external view returns (uint256) {
        return tranches[JUNIOR].totalShares;
    }

    function getTotalEquityShares() external view returns (uint256) {
        return tranches[EQUITY].totalShares;
    }

    // -- Idle / Deployed --
    function getSeniorTrancheIdleValue() external view returns (uint256) {
        return tranches[SENIOR].idleValue;
    }

    function getJuniorTrancheIdleValue() external view returns (uint256) {
        return tranches[JUNIOR].idleValue;
    }

    function getEquityTrancheIdleValue() external view returns (uint256) {
        return tranches[EQUITY].idleValue;
    }

    function getSeniorTrancheDeployedValue() external view returns (uint256) {
        return tranches[SENIOR].deployedValue;
    }

    function getJuniorTrancheDeployedValue() external view returns (uint256) {
        return tranches[JUNIOR].deployedValue;
    }

    function getEquityTrancheDeployedValue() external view returns (uint256) {
        return tranches[EQUITY].deployedValue;
    }

    // -- Interest indices --
    function getSeniorInterestIndex() external view returns (uint256) {
        return tranches[SENIOR].interestIndex;
    }

    function getJuniorInterestIndex() external view returns (uint256) {
        return tranches[JUNIOR].interestIndex;
    }

    function getEquityInterestIndex() external view returns (uint256) {
        return tranches[EQUITY].interestIndex;
    }

    function getSeniorUserIndex(address user) external view returns (uint256) {
        return tranches[SENIOR].userIndex[user];
    }

    function getJuniorUserIndex(address user) external view returns (uint256) {
        return tranches[JUNIOR].userIndex[user];
    }

    function getEquityUserIndex(address user) external view returns (uint256) {
        return tranches[EQUITY].userIndex[user];
    }

    // -- Caps / Minimums --
    function getSeniorTrancheMaxDepositCap() external view returns (uint256) {
        return tranches[SENIOR].maxCap;
    }

    function getJuniorTrancheMaxDepositCap() external view returns (uint256) {
        return tranches[JUNIOR].maxCap;
    }

    function getEquityTrancheMaxDepositCap() external view returns (uint256) {
        return tranches[EQUITY].maxCap;
    }

    function getSeniorTrancheMinimumDepositAmount()
        external
        view
        returns (uint256)
    {
        return tranches[SENIOR].minDeposit;
    }

    function getJuniorTrancheMinimumDepositAmount()
        external
        view
        returns (uint256)
    {
        return tranches[JUNIOR].minDeposit;
    }

    function getEquityTrancheMinimumDepositAmount()
        external
        view
        returns (uint256)
    {
        return tranches[EQUITY].minDeposit;
    }

    // -- Shortfalls --
    function getSeniorPrincipalShortfall() external view returns (uint256) {
        return tranches[SENIOR].principalShortfall;
    }

    function getJuniorPrincipalShortfall() external view returns (uint256) {
        return tranches[JUNIOR].principalShortfall;
    }

    function getEquityPrincipalShortfall() external view returns (uint256) {
        return tranches[EQUITY].principalShortfall;
    }

    // -- Aggregates --
    function getTotalDeployedValue() public view returns (uint256) {
        return
            tranches[SENIOR].deployedValue +
            tranches[JUNIOR].deployedValue +
            tranches[EQUITY].deployedValue;
    }

    function getTotalIdleValue() external view returns (uint256) {
        return
            tranches[SENIOR].idleValue +
            tranches[JUNIOR].idleValue +
            tranches[EQUITY].idleValue;
    }

    function getPoolState() external view returns (PoolState) {
        return poolState;
    }

    function getSeniorAllocationRatio() external view returns (uint256) {
        return s_capital_allocation_factor_senior;
    }

    function getJuniorAllocationRatio() external view returns (uint256) {
        return s_capital_allocation_factor_junior;
    }

    function getTotalDeposited() external view returns (uint256) {
        return s_totalDeposited;
    }

    function getTotalLoss() external view returns (uint256) {
        return s_totalLoss;
    }

    function getTotalRecovered() external view returns (uint256) {
        return s_totalRecovered;
    }

    function getProtocolRevenue() external view returns (uint256) {
        return s_protocolRevenue;
    }

    function getTotalUnclaimedInterest() external view returns (uint256) {
        return s_totalUnclaimedInterest;
    }

    // -- Legacy public-variable getters --
    // Tests access these as tranchePool.seniorAccruedInterest() etc.
    function seniorAccruedInterest() external view returns (uint256) {
        return tranches[SENIOR].accruedInterest;
    }

    function juniorAccruedInterest() external view returns (uint256) {
        return tranches[JUNIOR].accruedInterest;
    }

    function equityAccruedInterest() external view returns (uint256) {
        return tranches[EQUITY].accruedInterest;
    }

    function seniorInterestIndex() external view returns (uint256) {
        return tranches[SENIOR].interestIndex;
    }

    function juniorInterestIndex() external view returns (uint256) {
        return tranches[JUNIOR].interestIndex;
    }

    function equityInterestIndex() external view returns (uint256) {
        return tranches[EQUITY].interestIndex;
    }

    function seniorTargetInterest() external view returns (uint256) {
        return tranches[SENIOR].targetInterest;
    }

    function juniorTargetInterest() external view returns (uint256) {
        return tranches[JUNIOR].targetInterest;
    }

    function s_senior_apr_bps() external view returns (uint256) {
        return tranches[SENIOR].aprBps;
    }

    function s_target_junior_apr_bps() external view returns (uint256) {
        return tranches[JUNIOR].aprBps;
    }

    function seniorPrincipalShortfall() external view returns (uint256) {
        return tranches[SENIOR].principalShortfall;
    }

    function juniorPrincipalShortfall() external view returns (uint256) {
        return tranches[JUNIOR].principalShortfall;
    }

    function equityPrincipalShortfall() external view returns (uint256) {
        return tranches[EQUITY].principalShortfall;
    }

    // share mappings (tests call tranchePool.s_seniorTrancheShares(addr))
    function s_seniorTrancheShares(address u) external view returns (uint256) {
        return tranches[SENIOR].shares[u];
    }

    function s_juniorTrancheShares(address u) external view returns (uint256) {
        return tranches[JUNIOR].shares[u];
    }

    function s_equityTrancheShares(address u) external view returns (uint256) {
        return tranches[EQUITY].shares[u];
    }

    function s_totalSeniorShares() external view returns (uint256) {
        return tranches[SENIOR].totalShares;
    }

    function s_totalJuniorShares() external view returns (uint256) {
        return tranches[JUNIOR].totalShares;
    }

    function s_totalEquityShares() external view returns (uint256) {
        return tranches[EQUITY].totalShares;
    }

    function s_seniorTrancheIdleValue() external view returns (uint256) {
        return tranches[SENIOR].idleValue;
    }

    function s_juniorTrancheIdleValue() external view returns (uint256) {
        return tranches[JUNIOR].idleValue;
    }

    function s_equityTrancheIdleValue() external view returns (uint256) {
        return tranches[EQUITY].idleValue;
    }

    function s_seniorTrancheDeployedValue() external view returns (uint256) {
        return tranches[SENIOR].deployedValue;
    }

    function s_juniorTrancheDeployedValue() external view returns (uint256) {
        return tranches[JUNIOR].deployedValue;
    }

    function s_equityTrancheDeployedValue() external view returns (uint256) {
        return tranches[EQUITY].deployedValue;
    }

    function s_seniorTrancheMaxCap() external view returns (uint256) {
        return tranches[SENIOR].maxCap;
    }

    function s_juniorTrancheMaxCap() external view returns (uint256) {
        return tranches[JUNIOR].maxCap;
    }

    function s_equityTrancheMaxCap() external view returns (uint256) {
        return tranches[EQUITY].maxCap;
    }

    function s_minimumDepositAmountSeniorTranche()
        external
        view
        returns (uint256)
    {
        return tranches[SENIOR].minDeposit;
    }

    function s_minimumDepositAmountJuniorTranche()
        external
        view
        returns (uint256)
    {
        return tranches[JUNIOR].minDeposit;
    }

    function s_minimumDepositAmountEquityTranche()
        external
        view
        returns (uint256)
    {
        return tranches[EQUITY].minDeposit;
    }

    function seniorUserIndex(address u) external view returns (uint256) {
        return tranches[SENIOR].userIndex[u];
    }

    function juniorUserIndex(address u) external view returns (uint256) {
        return tranches[JUNIOR].userIndex[u];
    }

    function equityUserIndex(address u) external view returns (uint256) {
        return tranches[EQUITY].userIndex[u];
    }
}
