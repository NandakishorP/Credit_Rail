// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import {Pausable} from "@openzeppelin/contracts/utils/Pausable.sol";
import {ReentrancyGuard} from "@openzeppelin/contracts/utils/ReentrancyGuard.sol";
import {SafeERC20, IERC20} from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import {Math} from "@openzeppelin/contracts/utils/math/Math.sol";
import {ITranchePool} from "./interfaces/ITranchePool.sol";
import {InterestMath} from "./libraries/InterestMath.sol";

contract TranchePool is ITranchePool, Ownable, Pausable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Errors

    // Whitelist
    mapping(address => bool) public whiteListedLps;
    mapping(address => bool) public whiteListedForEquityTranche;

    // Shares tracking (instead of amounts)
    mapping(address => uint256) public s_seniorTrancheShares;
    mapping(address => uint256) public s_juniorTrancheShares;
    mapping(address => uint256) public s_equityTrancheShares;

    uint256 public s_totalSeniorShares;
    uint256 public s_totalJuniorShares;
    uint256 public s_totalEquityShares;

    // Total value in each tranche (this decreases when capital is allocated)
    // why some part of the capital should stay idle.
    // 1. Liquidity and operational buffer.
    //
    uint256 public s_seniorTrancheIdleValue;
    uint256 public s_juniorTrancheIdleValue;
    uint256 public s_equityTrancheIdleValue;

    uint256 public s_seniorTrancheDeployedValue;
    uint256 public s_juniorTrancheDeployedValue;
    uint256 public s_equityTrancheDeployedValue;

    // Minimum deposits
    uint256 public s_minimumDepositAmountSeniorTranche;
    uint256 public s_minimumDepositAmountJuniorTranche;
    uint256 public s_minimumDepositAmountEquityTranche;

    // CHANGED: global interest index (scaled)
    uint256 public seniorInterestIndex; // 1e18 precision
    uint256 public juniorInterestIndex; // 1e18 precision
    uint256 public equityInterestIndex; // 1e18 precision

    // CHANGED: per-user last claimed index
    mapping(address => uint256) public seniorUserIndex;
    mapping(address => uint256) public juniorUserIndex;
    mapping(address => uint256) public equityUserIndex;

    // Stable coin
    address public immutable i_stableCoin;
    address public loanEngine;

    // Capital allocation factor (e.g., 80 for 80% senior, 15% junior, 5% equity)
    uint256 public s_capital_allocation_factor_senior;
    uint256 public s_capital_allocation_factor_junior;

    uint256 public s_senior_apr_bps;
    uint256 public s_target_junior_apr_bps;
    uint256 public lastTrancheAccrualTimestamp;

    uint256 public seniorAccruedInterest;
    uint256 public juniorAccruedInterest;
    uint256 public equityAccruedInterest;

    uint256 public s_seniorTrancheMaxCap;
    uint256 public s_juniorTrancheMaxCap;
    uint256 public s_equityTrancheMaxCap;

    uint256 public s_protocolRevenue;
    uint256 public s_totalDeposited;
    uint256 public s_totalLoss;
    uint256 public s_totalRecovered;

    PoolState public poolState = PoolState.OPEN;

    uint256 public seniorPrincipalShortfall;
    uint256 public juniorPrincipalShortfall;
    uint256 public equityPrincipalShortfall;

    uint256 public s_totalUnclaimedInterest;

    uint256 public seniorTargetInterest;
    uint256 public juniorTargetInterest;

    modifier isWhiteListed(address user) {
        _isWhiteListed(user);
        _;
    }

    function _isWhiteListed(address user) internal view {
        if (!whiteListedLps[user]) {
            revert TranchePool__NotWhiteListed(user);
        }
    }

    modifier onlyLoanEngine(address user) {
        _onlyLoanEngine(user);
        _;
    }

    function _onlyLoanEngine(address user) internal view {
        if (user != loanEngine) {
            revert TranchePool__InvalidCaller(user);
        }
    }

    modifier isWhiteListedForEquityTranche(address user) {
        _isWhiteListedForEquityTranche(user);
        _;
    }

    function _isWhiteListedForEquityTranche(address user) internal view {
        if (!whiteListedForEquityTranche[user]) {
            revert TranchePool__NotWhiteListedForEquityTranche(user);
        }
    }

    constructor(address stableCoin_) Ownable(msg.sender) {
        if (stableCoin_ == address(0)) revert TranchePool__ZeroAddressError();
        i_stableCoin = stableCoin_;
        seniorInterestIndex = 1e18;
        juniorInterestIndex = 1e18;
        equityInterestIndex = 1e18;
        lastTrancheAccrualTimestamp = block.timestamp;
    }

    function depositSeniorTranche(
        uint256 amount
    ) external isWhiteListed(msg.sender) whenNotPaused nonReentrant {
        // q: wy we need a minimum deposit for a tranche?
        // a: in book.
        if (poolState != PoolState.OPEN) {
            revert TranchePool__PoolIsNotOpen();
        }
        if (amount == 0) {
            revert TranchePool__ZeroValueError();
        }
        if (amount < s_minimumDepositAmountSeniorTranche) {
            revert TranchePool__LessThanDepositThreshold(amount);
        }
        // why there is a max cap exists?
        //
        //  1. to prevent the liquidity from sitting idle
        //
        if (amount + s_seniorTrancheIdleValue > s_seniorTrancheMaxCap) {
            revert TranchePool__MaxDepositCapExceeded(
                s_seniorTrancheMaxCap,
                amount
            );
        }

        // Calculate shares to mint
        // invariant: the total shares == idle value because the deposit is allowed only when
        // the pool is open and once the pool is moved to a new state new deposits are not allowed
        // so what shares == amount holding 1:1 is valid and is not affecting or opening any attack vectors.
        uint256 shares = amount;

        IERC20(i_stableCoin).safeTransferFrom(
            msg.sender,
            address(this),
            amount
        );

        s_seniorTrancheShares[msg.sender] += shares;
        s_totalSeniorShares += shares;
        s_seniorTrancheIdleValue += amount;
        seniorUserIndex[msg.sender] = seniorInterestIndex;
        s_totalDeposited += amount;
        emit FundsDepositedToSeniorTranche(
            msg.sender,
            amount,
            shares,
            block.timestamp
        );
    }

    function depositJuniorTranche(
        uint256 amount
    ) external isWhiteListed(msg.sender) whenNotPaused nonReentrant {
        if (poolState != PoolState.OPEN) {
            revert TranchePool__PoolIsNotOpen();
        }
        if (amount < s_minimumDepositAmountJuniorTranche) {
            revert TranchePool__LessThanDepositThreshold(amount);
        }

        if (amount + s_juniorTrancheIdleValue > s_juniorTrancheMaxCap) {
            revert TranchePool__MaxDepositCapExceeded(
                s_juniorTrancheMaxCap,
                amount
            );
        }

        uint256 shares = amount;

        IERC20(i_stableCoin).safeTransferFrom(
            msg.sender,
            address(this),
            amount
        );

        s_juniorTrancheShares[msg.sender] += shares;
        s_totalJuniorShares += shares;
        s_juniorTrancheIdleValue += amount;
        juniorUserIndex[msg.sender] = juniorInterestIndex;
        s_totalDeposited += amount;

        emit FundsDepositedToJuniorTranche(
            msg.sender,
            amount,
            shares,
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
        if (poolState != PoolState.OPEN) {
            revert TranchePool__PoolIsNotOpen();
        }
        if (amount < s_minimumDepositAmountEquityTranche) {
            revert TranchePool__LessThanDepositThreshold(amount);
        }

        if (amount + s_equityTrancheIdleValue > s_equityTrancheMaxCap) {
            revert TranchePool__MaxDepositCapExceeded(
                s_equityTrancheMaxCap,
                amount
            );
        }

        uint256 shares = amount;

        IERC20(i_stableCoin).safeTransferFrom(
            msg.sender,
            address(this),
            amount
        );
        s_equityTrancheShares[msg.sender] += shares;
        s_totalEquityShares += shares;
        s_equityTrancheIdleValue += amount;
        equityUserIndex[msg.sender] = equityInterestIndex;
        s_totalDeposited += amount;

        emit FundsDepositedToEquityTranche(
            msg.sender,
            amount,
            shares,
            block.timestamp
        );
    }

    /**
     * @notice Allocate capital according to the 80/20 split
     * @param totalDisbursement Total amount to allocate from the pool
     * @param fees Total fees to be collected
     */
    function allocateCapital(
        uint256 totalDisbursement,
        uint256 fees,
        address deployer,
        address feeManager
    ) external onlyLoanEngine(msg.sender) returns (uint256, uint256, uint256) {
        if (
            poolState != PoolState.COMMITED && poolState != PoolState.DEPLOYED
        ) {
            revert TranchePool__PoolIsNotCommited();
        }

        uint256 totalAmount = totalDisbursement + fees;

        // Global liquidity check
        uint256 totalIdle = s_seniorTrancheIdleValue +
            s_juniorTrancheIdleValue +
            s_equityTrancheIdleValue;

        if (totalAmount > totalIdle) {
            revert TranchePool__InsufficientLiquidity();
        }

        uint256 targetSenior = (totalAmount *
            s_capital_allocation_factor_senior) / 100;

        uint256 targetJunior = (totalAmount *
            s_capital_allocation_factor_junior) / 100;

        uint256 targetEquity = totalAmount - targetSenior - targetJunior;

        uint256 seniorAmount = Math.min(targetSenior, s_seniorTrancheIdleValue);

        uint256 juniorAmount = Math.min(targetJunior, s_juniorTrancheIdleValue);

        uint256 equityAmount = Math.min(targetEquity, s_equityTrancheIdleValue);

        uint256 allocated = seniorAmount + juniorAmount + equityAmount;

        uint256 remaining = totalAmount - allocated;

        // Equity absorbs first
        if (remaining > 0 && s_equityTrancheIdleValue > equityAmount) {
            uint256 extra = Math.min(
                remaining,
                s_equityTrancheIdleValue - equityAmount
            );
            equityAmount += extra;
            remaining -= extra;
        }

        // Junior absorbs next
        if (remaining > 0 && s_juniorTrancheIdleValue > juniorAmount) {
            uint256 extra = Math.min(
                remaining,
                s_juniorTrancheIdleValue - juniorAmount
            );
            juniorAmount += extra;
            remaining -= extra;
        }

        // Senior absorbs last
        if (remaining > 0 && s_seniorTrancheIdleValue > seniorAmount) {
            uint256 extra = Math.min(
                remaining,
                s_seniorTrancheIdleValue - seniorAmount
            );
            seniorAmount += extra;
            remaining -= extra;
        }

        // Final safety check
        if (remaining > 0) {
            revert TranchePool__InsufficientLiquidity();
        }

        if (poolState == PoolState.COMMITED) {
            poolState = PoolState.DEPLOYED;
            emit PoolStateUpdated(PoolState.DEPLOYED);
        }

        _accrueTrancheTargets();

        s_seniorTrancheIdleValue -= seniorAmount;
        s_juniorTrancheIdleValue -= juniorAmount;
        s_equityTrancheIdleValue -= equityAmount;

        s_seniorTrancheDeployedValue += seniorAmount;
        s_juniorTrancheDeployedValue += juniorAmount;
        s_equityTrancheDeployedValue += equityAmount;

        IERC20(i_stableCoin).safeTransfer(deployer, totalDisbursement);

        if (fees > 0) {
            IERC20(i_stableCoin).safeTransfer(feeManager, fees);
        }

        emit CapitalAllocated(
            seniorAmount,
            juniorAmount,
            equityAmount,
            block.timestamp
        );
        return (seniorAmount, juniorAmount, equityAmount);
    }

    function onInterestAccrued(
        uint256 interestAmount
    ) external onlyLoanEngine(msg.sender) {
        if (interestAmount == 0) return;

        _accrueTrancheTargets();

        uint256 remaining = interestAmount;

        // Senior gets up to what is owed
        uint256 seniorOwed = 0;
        if (seniorTargetInterest > seniorAccruedInterest) {
            seniorOwed = seniorTargetInterest - seniorAccruedInterest;
        }

        uint256 seniorPaid = remaining < seniorOwed ? remaining : seniorOwed;

        if (seniorPaid > 0) {
            seniorAccruedInterest += seniorPaid;
            remaining -= seniorPaid;
        }

        // Junior next
        uint256 juniorOwed = 0;
        if (juniorTargetInterest > juniorAccruedInterest) {
            juniorOwed = juniorTargetInterest - juniorAccruedInterest;
        }

        uint256 juniorPaid = remaining < juniorOwed ? remaining : juniorOwed;

        if (juniorPaid > 0) {
            juniorAccruedInterest += juniorPaid;
            remaining -= juniorPaid;
        }

        // Residual
        if (remaining > 0) {
            equityAccruedInterest += remaining;
        }
    }

    function onRepayment(
        uint256 principalRepaid,
        uint256 interestRepaid
    ) external onlyLoanEngine(msg.sender) {
        if (principalRepaid == 0 && interestRepaid == 0) {
            revert TranchePool__InvalidTransferAmount(0);
        }

        _accrueTrancheTargets();

        /*//////////////////////////////////////////////////////////////
                        INTEREST WATERFALL (INDEXED)
    //////////////////////////////////////////////////////////////*/

        uint256 remainingInterest = interestRepaid;
        s_totalUnclaimedInterest += interestRepaid;

        // 1️⃣ Senior interest
        if (
            remainingInterest > 0 &&
            seniorAccruedInterest > 0 &&
            s_totalSeniorShares > 0
        ) {
            uint256 seniorPaid = Math.min(
                remainingInterest,
                seniorAccruedInterest
            );
            seniorAccruedInterest -= seniorPaid;
            seniorTargetInterest -= Math.min(seniorTargetInterest, seniorPaid);
            seniorInterestIndex += InterestMath.computeIndexDelta(seniorPaid, s_totalSeniorShares);
            remainingInterest -= seniorPaid;
        }

        // 2️⃣ Junior interest
        if (
            remainingInterest > 0 &&
            juniorAccruedInterest > 0 &&
            s_totalJuniorShares > 0
        ) {
            uint256 juniorPaid = Math.min(
                remainingInterest,
                juniorAccruedInterest
            );
            juniorAccruedInterest -= juniorPaid;
            juniorTargetInterest -= Math.min(juniorTargetInterest, juniorPaid);
            juniorInterestIndex += InterestMath.computeIndexDelta(juniorPaid, s_totalJuniorShares);
            remainingInterest -= juniorPaid;
        }

        // 3️⃣ Equity / overflow interest
        if (remainingInterest > 0) {
            if (s_totalEquityShares > 0) {
                equityInterestIndex += InterestMath.computeIndexDelta(
                    remainingInterest,
                    s_totalEquityShares
                );
                equityAccruedInterest -= Math.min(
                    equityAccruedInterest,
                    remainingInterest
                );
            } else if (s_totalJuniorShares > 0) {
                // no equity → junior gets excess
                juniorInterestIndex += InterestMath.computeIndexDelta(
                    remainingInterest,
                    s_totalJuniorShares
                );
            } else {
                // no LPs left → protocol revenue
                s_protocolRevenue += remainingInterest;
            }
        }

        /*//////////////////////////////////////////////////////////////
                        PRINCIPAL REDEMPTION
            (REVERSE OF LOSS WATERFALL — NO RATIOS)
    //////////////////////////////////////////////////////////////*/

        if (principalRepaid > 0) {
            uint256 remaining = principalRepaid;

            // Senior first (restore safest capital)
            if (remaining > 0 && s_seniorTrancheDeployedValue > 0) {
                uint256 seniorPay = Math.min(
                    remaining,
                    s_seniorTrancheDeployedValue
                );
                s_seniorTrancheDeployedValue -= seniorPay;
                s_seniorTrancheIdleValue += seniorPay;
                remaining -= seniorPay;
            }

            // Junior next
            if (remaining > 0 && s_juniorTrancheDeployedValue > 0) {
                uint256 juniorPay = Math.min(
                    remaining,
                    s_juniorTrancheDeployedValue
                );
                s_juniorTrancheDeployedValue -= juniorPay;
                s_juniorTrancheIdleValue += juniorPay;
                remaining -= juniorPay;
            }

            // Equity last
            if (remaining > 0 && s_equityTrancheDeployedValue > 0) {
                uint256 equityPay = Math.min(
                    remaining,
                    s_equityTrancheDeployedValue
                );
                s_equityTrancheDeployedValue -= equityPay;
                s_equityTrancheIdleValue += equityPay;
                remaining -= equityPay;
            }

            // Safety: should never happen unless LoanEngine lies
            if (remaining > 0) {
                revert TranchePool__PrincipalRepaymentExceeded();
            }
        }
    }

    // lp profit withdrawal is pending but it can only be implemented
    // after the loan enginge implementation which determines how the
    // interest will be accured and the distribution is dependent on the
    // share capacity

    function onLoss(
        uint256 principalLoss,
        uint256 interestAccrued
    ) external onlyLoanEngine(msg.sender) {
        if (principalLoss == 0 && interestAccrued == 0) {
            revert TranchePool__ZeroValueError();
        }

        _accrueTrancheTargets();

        /*//////////////////////////////////////////////////////////////
                    1️⃣ CANCEL GHOST INTEREST
        (SAME PRIORITY AS INTEREST PAYOUT)
    //////////////////////////////////////////////////////////////*/

        uint256 remainingInterest = interestAccrued;

        // Cancel senior accrued interest first
        if (remainingInterest > 0 && seniorAccruedInterest > 0) {
            uint256 seniorCancel = Math.min(
                remainingInterest,
                seniorAccruedInterest
            );
            seniorAccruedInterest -= seniorCancel;
            remainingInterest -= seniorCancel;
            seniorTargetInterest -= Math.min(
                seniorTargetInterest,
                seniorCancel
            );
        }

        // Then junior
        if (remainingInterest > 0 && juniorAccruedInterest > 0) {
            uint256 juniorCancel = Math.min(
                remainingInterest,
                juniorAccruedInterest
            );
            juniorAccruedInterest -= juniorCancel;
            remainingInterest -= juniorCancel;
            juniorTargetInterest -= Math.min(
                juniorTargetInterest,
                juniorCancel
            );
        }

        // Any remaining interest is ignored (equity / protocol had no promise)

        /*//////////////////////////////////////////////////////////////
                    2️⃣ PRINCIPAL LOSS WATERFALL
                Equity → Junior → Senior
    //////////////////////////////////////////////////////////////*/

        s_totalLoss += principalLoss;
        uint256 remaining = principalLoss;

        uint256 equityLoss;
        uint256 juniorLoss;
        uint256 seniorLoss;

        // Equity absorbs first
        if (remaining > 0 && s_equityTrancheDeployedValue > 0) {
            equityLoss = Math.min(remaining, s_equityTrancheDeployedValue);
            s_equityTrancheDeployedValue -= equityLoss;
            equityPrincipalShortfall += equityLoss;
            remaining -= equityLoss;
        }

        // Junior next
        if (remaining > 0 && s_juniorTrancheDeployedValue > 0) {
            juniorLoss = Math.min(remaining, s_juniorTrancheDeployedValue);
            s_juniorTrancheDeployedValue -= juniorLoss;
            juniorPrincipalShortfall += juniorLoss;
            remaining -= juniorLoss;
        }

        // Senior last
        if (remaining > 0 && s_seniorTrancheDeployedValue > 0) {
            seniorLoss = Math.min(remaining, s_seniorTrancheDeployedValue);
            s_seniorTrancheDeployedValue -= seniorLoss;
            seniorPrincipalShortfall += seniorLoss;
            remaining -= seniorLoss;
        }

        if (remaining > 0) {
            revert TranchePool__LossExceededCapital(remaining);
        }

        emit LossAllocated(seniorLoss, juniorLoss, equityLoss);
    }

    // on recovery what happens is the protocol may recover more than he lost and it can cause appreciation of the share value when withdrawing, keeping the design simple because adding it to interest accured make no difference at the end of withdrawing.

    function onRecovery(uint256 amount) external onlyLoanEngine(msg.sender) {
        if (amount == 0) {
            revert TranchePool__ZeroValueError();
        }

        _accrueTrancheTargets();

        s_totalRecovered += amount;
        uint256 remaining = amount;

        // Senior first
        if (remaining > 0 && seniorPrincipalShortfall > 0) {
            uint256 seniorPay = Math.min(remaining, seniorPrincipalShortfall);
            seniorPrincipalShortfall -= seniorPay;
            s_seniorTrancheIdleValue += seniorPay;
            remaining -= seniorPay;
        }

        // Junior next
        if (remaining > 0 && juniorPrincipalShortfall > 0) {
            uint256 juniorPay = Math.min(remaining, juniorPrincipalShortfall);
            juniorPrincipalShortfall -= juniorPay;
            s_juniorTrancheIdleValue += juniorPay;
            remaining -= juniorPay;
        }

        // Equity last
        if (remaining > 0 && equityPrincipalShortfall > 0) {
            uint256 equityPay = Math.min(remaining, equityPrincipalShortfall);
            equityPrincipalShortfall -= equityPay;
            s_equityTrancheIdleValue += equityPay;
            remaining -= equityPay;
        }

        // Any excess is true upside → equity
        if (remaining > 0) {
            s_equityTrancheIdleValue += remaining;
        }

        emit RecoverAmountTransferredToTranchePool(amount, block.timestamp);
    }

    // when the pool closes if the user withdraw the shares before claiming interest on those he will lose the interest for the withdrawn shares
    function claimSeniorInterest() external nonReentrant {
        uint256 userShares = s_seniorTrancheShares[msg.sender];
        if (userShares == 0) revert TranchePool__InsufficientShares();

        uint256 claimable = InterestMath.calculateClaimable(
            userShares,
            seniorInterestIndex,
            seniorUserIndex[msg.sender]
        );
        if (claimable == 0) revert TranchePool__ZeroWithdrawal();

        // Update user index BEFORE transfer
        seniorUserIndex[msg.sender] = seniorInterestIndex;
        s_totalUnclaimedInterest -= claimable;

        IERC20(i_stableCoin).safeTransfer(msg.sender, claimable);
    }

    function claimJuniorInterest() external nonReentrant {
        uint256 userShares = s_juniorTrancheShares[msg.sender];
        if (userShares == 0) revert TranchePool__InsufficientShares();

        uint256 claimable = InterestMath.calculateClaimable(
            userShares,
            juniorInterestIndex,
            juniorUserIndex[msg.sender]
        );
        if (claimable == 0) revert TranchePool__ZeroWithdrawal();

        // Update user index BEFORE transfer
        juniorUserIndex[msg.sender] = juniorInterestIndex;
        s_totalUnclaimedInterest -= claimable;

        IERC20(i_stableCoin).safeTransfer(msg.sender, claimable);
    }

    function claimEquityInterest()
        external
        isWhiteListedForEquityTranche(msg.sender)
        nonReentrant
    {
        uint256 userShares = s_equityTrancheShares[msg.sender];
        if (userShares == 0) revert TranchePool__InsufficientShares();

        uint256 claimable = InterestMath.calculateClaimable(
            userShares,
            equityInterestIndex,
            equityUserIndex[msg.sender]
        );
        if (claimable == 0) revert TranchePool__ZeroWithdrawal();

        s_totalUnclaimedInterest -= claimable;

        // Update user index BEFORE transfer
        equityUserIndex[msg.sender] = equityInterestIndex;

        IERC20(i_stableCoin).safeTransfer(msg.sender, claimable);
    }

    /**
     *
     *
     * @notice Withdraw from senior tranche by burning shares
     * @param shares Number of shares to burn (0 = withdraw all)
     * passing zero amount will cause the burn of all shares
     */
    function withdrawSeniorTranche(
        uint256 shares
    ) external isWhiteListed(msg.sender) nonReentrant {
        if (poolState != PoolState.OPEN && poolState != PoolState.CLOSED) {
            revert TranchePool__WithdrawNotAllowed(poolState);
        }
        uint256 userShares = s_seniorTrancheShares[msg.sender];

        if (userShares == 0) {
            revert TranchePool__InsufficientShares();
        }

        // If shares is 0, withdraw everything
        uint256 sharesToBurn = shares == 0 ? userShares : shares;

        if (sharesToBurn > userShares) {
            revert TranchePool__InsufficientShares();
        }

        // Calculate amount to withdraw based on current pool value
        uint256 amountToWithdraw = (sharesToBurn * s_seniorTrancheIdleValue) /
            s_totalSeniorShares;

        if (seniorUserIndex[msg.sender] != seniorInterestIndex) {
            revert TranchePool__InterestNotClaimed();
        }

        if (amountToWithdraw == 0) {
            revert TranchePool__ZeroWithdrawal();
        }

        if (amountToWithdraw > s_seniorTrancheIdleValue) {
            revert TranchePool__InsufficientLiquidity();
        }

        // Update state before transfer (CEI pattern)
        s_seniorTrancheShares[msg.sender] -= sharesToBurn;
        s_totalSeniorShares -= sharesToBurn;
        s_seniorTrancheIdleValue -= amountToWithdraw;
        s_totalDeposited -= amountToWithdraw;
        // Transfer tokens
        IERC20(i_stableCoin).safeTransfer(msg.sender, amountToWithdraw);

        emit WithdrawnFromSeniorTranche(
            msg.sender,
            amountToWithdraw,
            sharesToBurn,
            block.timestamp
        );
    }

    /**
     * @notice Withdraw from junior tranche by burning shares
     * @param shares Number of shares to burn (0 = withdraw all)
     */
    function withdrawJuniorTranche(
        uint256 shares
    ) external isWhiteListed(msg.sender) nonReentrant {
        if (poolState != PoolState.OPEN && poolState != PoolState.CLOSED) {
            revert TranchePool__WithdrawNotAllowed(poolState);
        }
        uint256 userShares = s_juniorTrancheShares[msg.sender];

        if (userShares == 0) {
            revert TranchePool__InsufficientShares();
        }

        if (juniorUserIndex[msg.sender] != juniorInterestIndex) {
            revert TranchePool__InterestNotClaimed();
        }

        uint256 sharesToBurn = shares == 0 ? userShares : shares;

        if (sharesToBurn > userShares) {
            revert TranchePool__InsufficientShares();
        }

        uint256 amountToWithdraw = (sharesToBurn * s_juniorTrancheIdleValue) /
            s_totalJuniorShares;

        if (amountToWithdraw == 0) {
            revert TranchePool__ZeroWithdrawal();
        }
        if (amountToWithdraw > s_juniorTrancheIdleValue) {
            revert TranchePool__InsufficientLiquidity();
        }

        s_juniorTrancheShares[msg.sender] -= sharesToBurn;
        s_totalJuniorShares -= sharesToBurn;
        s_juniorTrancheIdleValue -= amountToWithdraw;
        s_totalDeposited -= amountToWithdraw;

        IERC20(i_stableCoin).safeTransfer(msg.sender, amountToWithdraw);

        emit WithdrawnFromJuniorTranche(
            msg.sender,
            amountToWithdraw,
            sharesToBurn,
            block.timestamp
        );
    }

    function withdrawEquityTranche(
        uint256 shares
    ) external isWhiteListedForEquityTranche(msg.sender) nonReentrant {
        if (poolState != PoolState.OPEN && poolState != PoolState.CLOSED) {
            revert TranchePool__WithdrawNotAllowed(poolState);
        }
        uint256 userShares = s_equityTrancheShares[msg.sender];

        if (userShares == 0) {
            revert TranchePool__InsufficientShares();
        }
        if (equityUserIndex[msg.sender] != equityInterestIndex) {
            revert TranchePool__InterestNotClaimed();
        }
        uint256 sharesToBurn = shares == 0 ? userShares : shares;
        if (sharesToBurn > userShares) {
            revert TranchePool__InsufficientShares();
        }

        uint256 amountToWithdraw = (sharesToBurn * s_equityTrancheIdleValue) /
            s_totalEquityShares;

        if (amountToWithdraw == 0) {
            revert TranchePool__ZeroWithdrawal();
        }
        if (amountToWithdraw > s_equityTrancheIdleValue) {
            revert TranchePool__InsufficientLiquidity();
        }
        s_equityTrancheShares[msg.sender] -= sharesToBurn;
        s_totalEquityShares -= sharesToBurn;
        s_equityTrancheIdleValue -= amountToWithdraw;
        s_totalDeposited -= amountToWithdraw;

        IERC20(i_stableCoin).safeTransfer(msg.sender, amountToWithdraw);

        emit WithdrawnFromEquityTranche(
            msg.sender,
            amountToWithdraw,
            sharesToBurn,
            block.timestamp
        );
    }

    /**
     * @notice Withdraw specific amount from senior tranche
     * @param amount Amount of tokens to withdraw
     */
    function withdrawSeniorTrancheByAmount(
        uint256 amount
    ) external isWhiteListed(msg.sender) nonReentrant {
        if (poolState != PoolState.OPEN && poolState != PoolState.CLOSED) {
            revert TranchePool__WithdrawNotAllowed(poolState);
        }
        if (amount == 0) {
            revert TranchePool__ZeroWithdrawal();
        }
        if (seniorUserIndex[msg.sender] != seniorInterestIndex) {
            revert TranchePool__InterestNotClaimed();
        }

        uint256 userBalance = getSeniorTrancheBalance(msg.sender);

        if (amount > userBalance) {
            revert TranchePool__InsufficientShares();
        }

        if (amount > s_seniorTrancheIdleValue) {
            revert TranchePool__InsufficientLiquidity();
        }

        // Calculate shares to burn for this amount
        uint256 sharesToBurn = (amount * s_totalSeniorShares) /
            (s_seniorTrancheIdleValue);

        // Handle rounding - ensure we don't try to withdraw more than available
        if (sharesToBurn > s_seniorTrancheShares[msg.sender]) {
            sharesToBurn = s_seniorTrancheShares[msg.sender];
        }

        s_seniorTrancheShares[msg.sender] -= sharesToBurn;
        s_totalSeniorShares -= sharesToBurn;
        s_seniorTrancheIdleValue -= amount;
        s_totalDeposited -= amount;

        IERC20(i_stableCoin).safeTransfer(msg.sender, amount);

        emit WithdrawnFromSeniorTranche(
            msg.sender,
            amount,
            sharesToBurn,
            block.timestamp
        );
    }

    /**
     * @notice Withdraw specific amount from junior tranche
     * @param amount Amount of tokens to withdraw
     */
    function withdrawJuniorTrancheByAmount(
        uint256 amount
    ) external isWhiteListed(msg.sender) nonReentrant {
        if (poolState != PoolState.OPEN && poolState != PoolState.CLOSED) {
            revert TranchePool__WithdrawNotAllowed(poolState);
        }
        if (amount == 0) {
            revert TranchePool__ZeroWithdrawal();
        }

        if (juniorUserIndex[msg.sender] != juniorInterestIndex) {
            revert TranchePool__InterestNotClaimed();
        }

        uint256 userBalance = getJuniorTrancheBalance(msg.sender);

        if (amount > userBalance) {
            revert TranchePool__InsufficientShares();
        }

        if (amount > s_juniorTrancheIdleValue) {
            revert TranchePool__InsufficientLiquidity();
        }

        uint256 sharesToBurn = (amount * s_totalJuniorShares) /
            (s_juniorTrancheIdleValue);

        if (sharesToBurn > s_juniorTrancheShares[msg.sender]) {
            sharesToBurn = s_juniorTrancheShares[msg.sender];
        }

        s_juniorTrancheShares[msg.sender] -= sharesToBurn;
        s_totalJuniorShares -= sharesToBurn;
        s_juniorTrancheIdleValue -= amount;
        s_totalDeposited -= amount;

        IERC20(i_stableCoin).safeTransfer(msg.sender, amount);

        emit WithdrawnFromJuniorTranche(
            msg.sender,
            amount,
            sharesToBurn,
            block.timestamp
        );
    }

    function withdrawEquityTrancheByAmount(
        uint256 amount
    ) external isWhiteListedForEquityTranche(msg.sender) nonReentrant {
        if (poolState != PoolState.OPEN && poolState != PoolState.CLOSED) {
            revert TranchePool__WithdrawNotAllowed(poolState);
        }
        if (amount == 0) {
            revert TranchePool__ZeroWithdrawal();
        }

        if (equityUserIndex[msg.sender] != equityInterestIndex) {
            revert TranchePool__InterestNotClaimed();
        }

        uint256 userBalance = getEquityTrancheBalance(msg.sender);

        if (amount > userBalance) {
            revert TranchePool__InsufficientShares();
        }

        if (amount > s_equityTrancheIdleValue) {
            revert TranchePool__InsufficientLiquidity();
        }

        uint256 sharesToBurn = (amount * s_totalEquityShares) /
            (s_equityTrancheIdleValue);

        if (sharesToBurn > s_equityTrancheShares[msg.sender]) {
            sharesToBurn = s_equityTrancheShares[msg.sender];
        }

        s_equityTrancheShares[msg.sender] -= sharesToBurn;
        s_totalEquityShares -= sharesToBurn;
        s_equityTrancheIdleValue -= amount;
        s_totalDeposited -= amount;

        IERC20(i_stableCoin).safeTransfer(msg.sender, amount);

        emit WithdrawnFromEquityTranche(
            msg.sender,
            amount,
            sharesToBurn,
            block.timestamp
        );
    }

    // INTERNAL FUNCTIONS

    function _accrueTrancheTargets() internal {
        uint256 currentTimestamp = block.timestamp;
        uint256 timeElapsed = currentTimestamp - lastTrancheAccrualTimestamp;

        if (timeElapsed == 0) return;

        seniorTargetInterest += InterestMath.accrueTargetInterest(
            s_seniorTrancheDeployedValue,
            s_senior_apr_bps,
            timeElapsed
        );

        juniorTargetInterest += InterestMath.accrueTargetInterest(
            s_juniorTrancheDeployedValue,
            s_target_junior_apr_bps,
            timeElapsed
        );

        lastTrancheAccrualTimestamp = currentTimestamp;
    }

    /**
     * @notice Get the current balance of a user in the senior tranche
     */
    function getSeniorTrancheBalance(
        address user
    ) public view returns (uint256) {
        if (s_totalSeniorShares == 0) return 0;
        return
            (s_seniorTrancheShares[user] * s_seniorTrancheIdleValue) /
            s_totalSeniorShares;
    }

    /**
     * @notice Get the current balance of a user in the junior tranche
     */
    function getJuniorTrancheBalance(
        address user
    ) public view returns (uint256) {
        if (s_totalJuniorShares == 0) return 0;
        return
            (s_juniorTrancheShares[user] * s_juniorTrancheIdleValue) /
            s_totalJuniorShares;
    }

    function getEquityTrancheBalance(
        address user
    ) public view returns (uint256) {
        if (s_totalEquityShares == 0) return 0;
        return
            (s_equityTrancheShares[user] * s_equityTrancheIdleValue) /
            s_totalEquityShares;
    }

    // Admin functions
    function setMinimumDepositAmountJuniorTranche(
        uint256 amount
    ) external onlyOwner {
        if (amount > s_juniorTrancheMaxCap) {
            revert TranchePool__InvalidMinDepositAmount();
        }
        s_minimumDepositAmountJuniorTranche = amount;
    }

    function setMinimumDepositAmountSeniorTranche(
        uint256 amount
    ) external onlyOwner {
        if (amount > s_seniorTrancheMaxCap) {
            revert TranchePool__InvalidMinDepositAmount();
        }
        s_minimumDepositAmountSeniorTranche = amount;
    }

    function setMinimumDepositAmountEquityTranche(
        uint256 amount
    ) external onlyOwner {
        if (amount > s_equityTrancheMaxCap) {
            revert TranchePool__InvalidMinDepositAmount();
        }
        s_minimumDepositAmountEquityTranche = amount;
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
        if (aprbps == 0) {
            revert TranchePool__ZeroAPRError();
        }
        _accrueTrancheTargets();
        s_senior_apr_bps = aprbps;
    }

    function setTargetJuniorAPR(uint256 aprbps) external onlyOwner {
        if (aprbps == 0) {
            revert TranchePool__ZeroAPRError();
        }
        _accrueTrancheTargets();
        s_target_junior_apr_bps = aprbps;
    }

    function setPoolState(PoolState newState) external onlyOwner {
        if (uint256(newState) < uint256(poolState)) {
            revert TranchePool__InvalidStateTransition(newState);
        }

        if (newState == PoolState.CLOSED) {
            if (getTotalDeployedValue() > 0) {
                revert TranchePool__DeployedCapitalExists();
            }
        }

        poolState = newState;

        emit PoolStateUpdated(newState);
    }

    function setLoanEngine(address _loanEngine) external onlyOwner {
        if (_loanEngine == address(0)) {
            revert TranchePool__ZeroAddressError();
        }
        loanEngine = _loanEngine;
    }

    function setMaxAllocationCapSeniorTranche(
        uint256 amount
    ) external onlyOwner {
        if (amount == 0) {
            revert TranchePool__ZeroValueError();
        }
        if (amount < s_minimumDepositAmountSeniorTranche) {
            revert TranchePool__InvalidMaxCapAmount();
        }
        s_seniorTrancheMaxCap = amount;
    }

    function setMaxAllocationCapJuniorTranche(
        uint256 amount
    ) external onlyOwner {
        if (amount == 0) {
            revert TranchePool__ZeroValueError();
        }
        if (amount < s_minimumDepositAmountJuniorTranche) {
            revert TranchePool__InvalidMaxCapAmount();
        }
        s_juniorTrancheMaxCap = amount;
    }

    function setMaxAllocationCapEquityTranche(
        uint256 amount
    ) external onlyOwner {
        if (amount == 0) {
            revert TranchePool__ZeroValueError();
        }
        if (amount < s_minimumDepositAmountEquityTranche) {
            revert TranchePool__InvalidMaxCapAmount();
        }
        s_equityTrancheMaxCap = amount;
    }

    function updateWhitelist(address user, bool status) external onlyOwner {
        whiteListedLps[user] = status;
    }

    function updateEquityTrancheWhiteList(
        address user,
        bool status
    ) external onlyOwner {
        whiteListedForEquityTranche[user] = status;
    }

    // getters

    function getTotalUnclaimedInterest() external view returns (uint256) {
        return s_totalUnclaimedInterest;
    }

    function getSeniorTrancheMaxDepositCap() external view returns (uint256) {
        return s_seniorTrancheMaxCap;
    }

    function getSeniorTrancheMinimumDepositAmount()
        external
        view
        returns (uint256)
    {
        return s_minimumDepositAmountSeniorTranche;
    }

    function getSeniorTrancheShares(
        address user
    ) external view returns (uint256) {
        return s_seniorTrancheShares[user];
    }

    function getTotalSeniorShares() external view returns (uint256) {
        return s_totalSeniorShares;
    }

    function getSeniorTrancheIdleValue() external view returns (uint256) {
        return s_seniorTrancheIdleValue;
    }

    function getSeniorTrancheDeployedValue() external view returns (uint256) {
        return s_seniorTrancheDeployedValue;
    }

    function getSeniorInterestIndex() external view returns (uint256) {
        return seniorInterestIndex;
    }

    function getSeniorUserIndex(address user) external view returns (uint256) {
        return seniorUserIndex[user];
    }

    function getJuniorTrancheMaxDepositCap() external view returns (uint256) {
        return s_juniorTrancheMaxCap;
    }

    function getJuniorInterestIndex() external view returns (uint256) {
        return juniorInterestIndex;
    }

    function getJuniorTrancheMinimumDepositAmount()
        external
        view
        returns (uint256)
    {
        return s_minimumDepositAmountJuniorTranche;
    }

    function getJuniorTrancheShares(
        address user
    ) external view returns (uint256) {
        return s_juniorTrancheShares[user];
    }

    function getTotalJuniorShares() external view returns (uint256) {
        return s_totalJuniorShares;
    }

    function getJuniorTrancheIdleValue() external view returns (uint256) {
        return s_juniorTrancheIdleValue;
    }

    function getJuniorTrancheDeployedValue() external view returns (uint256) {
        return s_juniorTrancheDeployedValue;
    }

    function getJuniorUserIndex(address user) external view returns (uint256) {
        return juniorUserIndex[user];
    }

    function getEquityTrancheMaxDepositCap() external view returns (uint256) {
        return s_equityTrancheMaxCap;
    }

    function getEquityTrancheShares(
        address user
    ) external view returns (uint256) {
        return s_equityTrancheShares[user];
    }

    function getTotalEquityShares() external view returns (uint256) {
        return s_totalEquityShares;
    }

    function getEquityTrancheMinimumDepositAmount()
        external
        view
        returns (uint256)
    {
        return s_minimumDepositAmountEquityTranche;
    }

    function getEquityTrancheIdleValue() external view returns (uint256) {
        return s_equityTrancheIdleValue;
    }

    function getEquityTrancheDeployedValue() external view returns (uint256) {
        return s_equityTrancheDeployedValue;
    }

    function getEquityInterestIndex() external view returns (uint256) {
        return equityInterestIndex;
    }

    function getEquityUserIndex(address user) external view returns (uint256) {
        return equityUserIndex[user];
    }

    function getPoolState() external view returns (PoolState) {
        return poolState;
    }

    function getTotalDeployedValue() public view returns (uint256) {
        return
            s_seniorTrancheDeployedValue +
            s_juniorTrancheDeployedValue +
            s_equityTrancheDeployedValue;
    }

    function getTotalIdleValue() external view returns (uint256) {
        return
            s_seniorTrancheIdleValue +
            s_juniorTrancheIdleValue +
            s_equityTrancheIdleValue;
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

    function getSeniorPrincipalShortfall() external view returns (uint256) {
        return seniorPrincipalShortfall;
    }

    function getJuniorPrincipalShortfall() external view returns (uint256) {
        return juniorPrincipalShortfall;
    }

    function getEquityPrincipalShortfall() external view returns (uint256) {
        return equityPrincipalShortfall;
    }

    /// @notice Pause all deposit functions
    /// @dev Only owner can pause
    function pause() external onlyOwner {
        _pause();
    }

    /// @notice Unpause all deposit functions
    /// @dev Only owner can unpause
    function unpause() external onlyOwner {
        _unpause();
    }
}
