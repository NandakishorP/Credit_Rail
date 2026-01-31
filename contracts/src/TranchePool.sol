// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import {SafeERC20, IERC20} from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import {console} from "forge-std/console.sol";

contract TranchePool is Ownable {
    using SafeERC20 for IERC20;

    // Errors
    error TranchePool__NotWhiteListed(address user);
    error TranchePool__LessThanDepositThreshold(uint256 amount);
    error TranchePool__InvalidAllocationRatio();
    error TranchePool__InsufficientLiquidity();
    error TranchePool__InsufficientShares();
    error TranchePool__ZeroWithdrawal();
    error TranchePool__NotWhiteListedForEquityTranche(address user);
    error TranchePool__InvalidTransferAmount(uint256 amount);
    error TranchePool__InvalidCaller(address user);
    error TranchePool__ZeroAPRError();
    error TranchePool__LossExceededCapital(uint256 remaining);
    error TranchePool__ZeroSharesMinted();
    error TranchePool__PoolIsNotOpen();
    error TranchePool__InvalidStateTransition(PoolState state);
    error TranchePool__WithdrawNotAllowed(PoolState state);
    error TranchePool__ZeroValueError();
    error TranchePool__MaxDepositCapExceeded(uint256 maxCap, uint256 amount);
    error TranchePool__PoolIsNotCommited();
    error TranchePool__PrincipalRepaymentExceeded();
    error TranchePool__ZeroAddressError();

    // Events

    event PoolStateUpdated(PoolState newState);

    event LossAllocated(
        uint256 seniorLoss,
        uint256 juniorLoss,
        uint256 equityLoss
    );
    event WithdrawnFromSeniorTranche(
        address indexed user,
        uint256 amount,
        uint256 sharesBurned,
        uint256 time
    );
    event WithdrawnFromJuniorTranche(
        address indexed user,
        uint256 amount,
        uint256 sharesBurned,
        uint256 time
    );
    event WithdrawnFromEquityTranche(
        address indexed user,
        uint256 amount,
        uint256 sharesBurned,
        uint256 time
    );

    event FundsDepositedToSeniorTranche(
        address indexed user,
        uint256 amount,
        uint256 shares,
        uint256 time
    );
    event FundsDepositedToJuniorTranche(
        address indexed user,
        uint256 amount,
        uint256 shares,
        uint256 time
    );
    event FundsDepositedToEquityTranche(
        address indexed user,
        uint256 amount,
        uint256 shares,
        uint256 time
    );
    event CapitalAllocated(
        uint256 seniorAmount,
        uint256 juniorAmount,
        uint256 equityAmount,
        uint256 time
    );
    event RecoverAmountTransferredToTranchePool(
        uint256 amount,
        uint256 timeStamp
    );
    event ProfitTransferredToTranchePool(uint256 amount, uint256 timeStamp);
    event CapitalAllocationFactorUpdatedSenior(uint256 newFactor);
    event CapitalAllocationFactorUpdatedJunior(uint256 newFactor);

    enum PoolState {
        OPEN, // deposits allowed
        COMMITED,
        DEPLOYED, // capital deployed, deposits paused
        CLOSED // withdrawals only
    }

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
    address public s_stableCoin;
    address public loanEngine;

    // Capital allocation factor (e.g., 80 for 80% senior, 15% junior, 5% equity)
    uint256 public s_capital_allocation_factor_senior;
    uint256 public s_capital_allocation_factor_junior;

    uint256 public s_senior_apr;
    uint256 public s_target_junior_apr;

    // why are we tracking the senior and junior interest but not the equity tranche,
    // ans: because we don't have a specific target promise for the equity tranche,what ever is left goes to equity tranche
    // but the senior and junior tranche have a specific target/promised apr so we need to track that specifically
    uint256 public seniorAccruedInterest;
    uint256 public juniorAccruedInterest;

    uint256 public s_seniorTrancheMaxCap;
    uint256 public s_juniorTrancheMaxCap;
    uint256 public s_equityTrancheMaxCap;

    uint256 public s_protocolRevenue;

    PoolState public poolState = PoolState.OPEN;

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
        s_stableCoin = stableCoin_;
        seniorInterestIndex = 1e18;
        juniorInterestIndex = 1e18;
        equityInterestIndex = 1e18;
    }

    function depositSeniorTranche(
        uint256 amount
    ) external isWhiteListed(msg.sender) {
        // q: wy we need a minimum deposit for a tranche?
        // a: in book.
        if (poolState != PoolState.OPEN) {
            revert TranchePool__PoolIsNotOpen();
        }
        if (amount < s_minimumDepositAmountSeniorTranche) {
            revert TranchePool__LessThanDepositThreshold(amount);
        }
        // why there is a max cap exists?
        //
        //  1. to prevent the liquidity from sitting idle.abi
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

        IERC20(s_stableCoin).safeTransferFrom(
            msg.sender,
            address(this),
            amount
        );

        s_seniorTrancheShares[msg.sender] += shares;
        s_totalSeniorShares += shares;
        s_seniorTrancheIdleValue += amount;
        seniorUserIndex[msg.sender] = seniorInterestIndex;

        emit FundsDepositedToSeniorTranche(
            msg.sender,
            amount,
            shares,
            block.timestamp
        );
    }

    function depositJuniorTranche(
        uint256 amount
    ) external isWhiteListed(msg.sender) {
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

        IERC20(s_stableCoin).safeTransferFrom(
            msg.sender,
            address(this),
            amount
        );

        s_juniorTrancheShares[msg.sender] += shares;
        s_totalJuniorShares += shares;
        s_juniorTrancheIdleValue += amount;
        juniorUserIndex[msg.sender] = juniorInterestIndex;

        emit FundsDepositedToJuniorTranche(
            msg.sender,
            amount,
            shares,
            block.timestamp
        );
    }

    function depositEquityTranche(
        uint256 amount
    ) external isWhiteListedForEquityTranche(msg.sender) {
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

        IERC20(s_stableCoin).safeTransferFrom(
            msg.sender,
            address(this),
            amount
        );
        s_equityTrancheShares[msg.sender] += shares;
        s_totalEquityShares += shares;
        s_equityTrancheIdleValue += amount;
        equityUserIndex[msg.sender] = equityInterestIndex;

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
    ) external onlyLoanEngine(msg.sender) {
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

        uint256 seniorAmount = _minimum(targetSenior, s_seniorTrancheIdleValue);

        uint256 juniorAmount = _minimum(targetJunior, s_juniorTrancheIdleValue);

        uint256 equityAmount = _minimum(targetEquity, s_equityTrancheIdleValue);

        uint256 allocated = seniorAmount + juniorAmount + equityAmount;

        uint256 remaining = totalAmount - allocated;

        // Equity absorbs first
        if (remaining > 0 && s_equityTrancheIdleValue > equityAmount) {
            uint256 extra = _minimum(
                remaining,
                s_equityTrancheIdleValue - equityAmount
            );
            equityAmount += extra;
            remaining -= extra;
        }

        // Junior absorbs next
        if (remaining > 0 && s_juniorTrancheIdleValue > juniorAmount) {
            uint256 extra = _minimum(
                remaining,
                s_juniorTrancheIdleValue - juniorAmount
            );
            juniorAmount += extra;
            remaining -= extra;
        }

        // Senior absorbs last
        if (remaining > 0 && s_seniorTrancheIdleValue > seniorAmount) {
            uint256 extra = _minimum(
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

        s_seniorTrancheIdleValue -= seniorAmount;
        s_juniorTrancheIdleValue -= juniorAmount;
        s_equityTrancheIdleValue -= equityAmount;

        s_seniorTrancheDeployedValue += seniorAmount;
        s_juniorTrancheDeployedValue += juniorAmount;
        s_equityTrancheDeployedValue += equityAmount;

        IERC20(s_stableCoin).safeTransfer(deployer, totalDisbursement);

        if (fees > 0) {
            IERC20(s_stableCoin).safeTransfer(feeManager, fees);
        }

        emit CapitalAllocated(
            seniorAmount,
            juniorAmount,
            equityAmount,
            block.timestamp
        );
    }

    function onInterestAccrued(
        uint256 interestAmount,
        uint256 seniorAllocationFactor,
        uint256 juniorAllocationFactor
    ) external onlyLoanEngine(msg.sender) {
        if (interestAmount == 0) return;

        uint256 seniorShare = (interestAmount * seniorAllocationFactor) / 100;
        uint256 juniorShare = (interestAmount * juniorAllocationFactor) / 100;

        seniorAccruedInterest += seniorShare;
        juniorAccruedInterest += juniorShare;
    }

    function onRepayment(
        uint256 principalRepaid,
        uint256 interestRepaid,
        uint256 seniorAllocationRatio,
        uint256 juniorAllocationRatio
    ) external onlyLoanEngine(msg.sender) {
        if (principalRepaid == 0 && interestRepaid == 0) {
            revert TranchePool__InvalidTransferAmount(0);
        }

        /*//////////////////////////////////////////////////////////////
                        INTEREST WATERFALL (INDEXED)
    //////////////////////////////////////////////////////////////*/

        uint256 remainingInterest = interestRepaid;

        // 1️⃣ Senior
        uint256 seniorPaid = _minimum(remainingInterest, seniorAccruedInterest);
        if (seniorPaid > 0 && s_totalSeniorShares > 0) {
            seniorAccruedInterest -= seniorPaid;
            seniorInterestIndex += (seniorPaid * 1e18) / s_totalSeniorShares;
            remainingInterest -= seniorPaid;
        }

        // 2️⃣ Junior
        uint256 juniorPaid = _minimum(remainingInterest, juniorAccruedInterest);
        if (juniorPaid > 0 && s_totalJuniorShares > 0) {
            juniorAccruedInterest -= juniorPaid;
            juniorInterestIndex += (juniorPaid * 1e18) / s_totalJuniorShares;
            remainingInterest -= juniorPaid;
        }

        // 3️⃣ Equity (kept as raw cash or separate index)
        // what if there is no junior or equity and senior obligations are paid off?
        // yet to answer
        if (remainingInterest > 0) {
            if (s_totalEquityShares == 0 && s_totalJuniorShares > 0) {
                juniorInterestIndex +=
                    (remainingInterest * 1e18) /
                    s_totalJuniorShares;
            } else if (s_totalEquityShares > 0) {
                equityInterestIndex +=
                    (remainingInterest * 1e18) /
                    s_totalEquityShares;
            } else {
                // all tranches are done, protocol takes the rest
                s_protocolRevenue += remainingInterest;
            }
        }

        /*//////////////////////////////////////////////////////////////
                        PRINCIPAL (BUFFERED)
    //////////////////////////////////////////////////////////////*/

        if (principalRepaid > 0) {
            uint256 seniorPrincipal = (principalRepaid *
                seniorAllocationRatio) / 100;
            uint256 juniorPrincipal = (principalRepaid *
                juniorAllocationRatio) / 100;
            uint256 equityPrincipal = principalRepaid -
                seniorPrincipal -
                juniorPrincipal;

            if (
                seniorPrincipal > s_seniorTrancheDeployedValue ||
                juniorPrincipal > s_juniorTrancheDeployedValue ||
                equityPrincipal > s_equityTrancheDeployedValue
            ) {
                revert TranchePool__PrincipalRepaymentExceeded();
            }

            s_seniorTrancheDeployedValue -= seniorPrincipal;
            s_juniorTrancheDeployedValue -= juniorPrincipal;
            s_equityTrancheDeployedValue -= equityPrincipal;

            s_seniorTrancheIdleValue += seniorPrincipal;
            s_juniorTrancheIdleValue += juniorPrincipal;
            s_equityTrancheIdleValue += equityPrincipal;
        }
    }

    // lp profit withdrawal is pending but it can only be implemented
    // after the loan enginge implementation which determines how the
    // interest will be accured and the distribution is dependent on the
    // share capacity

    function onLoss(uint256 loss) external onlyLoanEngine(msg.sender) {
        uint256 remaining = loss;

        // 1. Equity absorbs first
        uint256 equityLoss = _minimum(s_equityTrancheDeployedValue, remaining);
        s_equityTrancheDeployedValue -= equityLoss;
        remaining -= equityLoss;

        if (remaining == 0) return;

        // 2. Junior absorbs next
        uint256 juniorLoss = _minimum(s_juniorTrancheDeployedValue, remaining);
        s_juniorTrancheDeployedValue -= juniorLoss;
        remaining -= juniorLoss;

        if (remaining == 0) return;

        // 3. Senior absorbs last
        uint256 seniorLoss = _minimum(s_seniorTrancheDeployedValue, remaining);
        s_seniorTrancheDeployedValue -= seniorLoss;
        remaining -= seniorLoss;

        if (remaining > 0) {
            revert TranchePool__LossExceededCapital(remaining);
        }

        emit LossAllocated(seniorLoss, juniorLoss, equityLoss);
    }

    function onRecovery(
        uint256 amount,
        uint256 seniorAllocationRatio,
        uint256 juniorAllocationRatio
    ) external onlyLoanEngine(msg.sender) {
        if (amount == 0) {
            revert TranchePool__ZeroValueError();
        }
        // treat as pure cash inflow
        uint256 seniorAmount = (amount * seniorAllocationRatio) / 100;
        uint256 juniorAmount = (amount * juniorAllocationRatio) / 100;
        // why this won't overflow, because the total allocation factor is 100 and
        // at most possibility is equity gets zero allocation
        uint256 equityAmount = amount - seniorAmount - juniorAmount;

        s_seniorTrancheIdleValue += seniorAmount;
        s_juniorTrancheIdleValue += juniorAmount;
        s_equityTrancheIdleValue += equityAmount;

        emit RecoverAmountTransferredToTranchePool(amount, block.timestamp);
    }

    function claimSeniorInterest() external {
        uint256 userShares = s_seniorTrancheShares[msg.sender];
        if (userShares == 0) revert TranchePool__InsufficientShares();

        uint256 indexDelta = seniorInterestIndex - seniorUserIndex[msg.sender];

        if (indexDelta == 0) revert TranchePool__ZeroWithdrawal();

        uint256 claimable = (userShares * indexDelta) / 1e18;

        // CHANGED: update user index BEFORE transfer
        seniorUserIndex[msg.sender] = seniorInterestIndex;

        IERC20(s_stableCoin).safeTransfer(msg.sender, claimable);
    }

    function claimJuniorInterest() external {
        uint256 userShares = s_juniorTrancheShares[msg.sender];
        if (userShares == 0) revert TranchePool__InsufficientShares();

        uint256 indexDelta = juniorInterestIndex - juniorUserIndex[msg.sender];

        if (indexDelta == 0) revert TranchePool__ZeroWithdrawal();

        uint256 claimable = (userShares * indexDelta) / 1e18;

        // CHANGED: update user index BEFORE transfer
        juniorUserIndex[msg.sender] = juniorInterestIndex;

        IERC20(s_stableCoin).safeTransfer(msg.sender, claimable);
    }

    function claimEquityInterest()
        external
        isWhiteListedForEquityTranche(msg.sender)
    {
        uint256 userShares = s_equityTrancheShares[msg.sender];
        if (userShares == 0) revert TranchePool__InsufficientShares();

        uint256 indexDelta = equityInterestIndex - equityUserIndex[msg.sender];

        if (indexDelta == 0) revert TranchePool__ZeroWithdrawal();

        uint256 claimable = (userShares * indexDelta) / 1e18;

        // CHANGED: update user index BEFORE transfer
        equityUserIndex[msg.sender] = equityInterestIndex;

        IERC20(s_stableCoin).safeTransfer(msg.sender, claimable);
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
    ) external isWhiteListed(msg.sender) {
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

        // Transfer tokens
        IERC20(s_stableCoin).safeTransfer(msg.sender, amountToWithdraw);

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
    ) external isWhiteListed(msg.sender) {
        if (poolState != PoolState.OPEN && poolState != PoolState.CLOSED) {
            revert TranchePool__WithdrawNotAllowed(poolState);
        }
        uint256 userShares = s_juniorTrancheShares[msg.sender];

        if (userShares == 0) {
            revert TranchePool__InsufficientShares();
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

        IERC20(s_stableCoin).safeTransfer(msg.sender, amountToWithdraw);

        emit WithdrawnFromJuniorTranche(
            msg.sender,
            amountToWithdraw,
            sharesToBurn,
            block.timestamp
        );
    }

    function withdrawEquityTranche(
        uint256 shares
    ) external isWhiteListedForEquityTranche(msg.sender) {
        if (poolState != PoolState.OPEN && poolState != PoolState.CLOSED) {
            revert TranchePool__WithdrawNotAllowed(poolState);
        }
        uint256 userShares = s_equityTrancheShares[msg.sender];

        if (userShares == 0) {
            revert TranchePool__InsufficientShares();
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

        IERC20(s_stableCoin).safeTransfer(msg.sender, amountToWithdraw);

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
    ) external isWhiteListed(msg.sender) {
        if (poolState != PoolState.OPEN && poolState != PoolState.CLOSED) {
            revert TranchePool__WithdrawNotAllowed(poolState);
        }
        if (amount == 0) {
            revert TranchePool__ZeroWithdrawal();
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

        IERC20(s_stableCoin).safeTransfer(msg.sender, amount);

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
    ) external isWhiteListed(msg.sender) {
        if (poolState != PoolState.OPEN && poolState != PoolState.CLOSED) {
            revert TranchePool__WithdrawNotAllowed(poolState);
        }
        if (amount == 0) {
            revert TranchePool__ZeroWithdrawal();
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

        IERC20(s_stableCoin).safeTransfer(msg.sender, amount);

        emit WithdrawnFromJuniorTranche(
            msg.sender,
            amount,
            sharesToBurn,
            block.timestamp
        );
    }

    function withdrawEquityTrancheByAmount(
        uint256 amount
    ) external isWhiteListedForEquityTranche(msg.sender) {
        if (poolState != PoolState.OPEN && poolState != PoolState.CLOSED) {
            revert TranchePool__WithdrawNotAllowed(poolState);
        }
        if (amount == 0) {
            revert TranchePool__ZeroWithdrawal();
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

        IERC20(s_stableCoin).safeTransfer(msg.sender, amount);

        emit WithdrawnFromEquityTranche(
            msg.sender,
            amount,
            sharesToBurn,
            block.timestamp
        );
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
        s_minimumDepositAmountJuniorTranche = amount;
    }

    function setMinimumDepositAmountSeniorTranche(
        uint256 amount
    ) external onlyOwner {
        s_minimumDepositAmountSeniorTranche = amount;
    }

    function setMinimumDepositAmountEquityTranche(
        uint256 amount
    ) external onlyOwner {
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

    function setSeniorAPR(uint256 apr) external onlyOwner {
        if (apr == 0) {
            revert TranchePool__ZeroAPRError();
        }
        s_senior_apr = apr;
    }

    function setTargetJuniorAPR(uint256 apr) external onlyOwner {
        if (apr == 0) {
            revert TranchePool__ZeroAPRError();
        }
        s_target_junior_apr = apr;
    }

    function setPoolState(PoolState newState) external onlyOwner {
        if (uint256(newState) < uint256(poolState)) {
            revert TranchePool__InvalidStateTransition(newState);
        }

        poolState = newState;

        if (poolState == PoolState.CLOSED) {
            _closePool();
        }

        emit PoolStateUpdated(newState);
    }

    function _closePool() private {
        s_seniorTrancheIdleValue += s_seniorTrancheDeployedValue;
        s_juniorTrancheIdleValue += s_juniorTrancheDeployedValue;
        s_equityTrancheIdleValue += s_equityTrancheDeployedValue;

        s_seniorTrancheDeployedValue = 0;
        s_juniorTrancheDeployedValue = 0;
        s_equityTrancheDeployedValue = 0;
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
        s_seniorTrancheMaxCap = amount;
    }

    function setMaxAllocationCapJuniorTranche(
        uint256 amount
    ) external onlyOwner {
        if (amount == 0) {
            revert TranchePool__ZeroValueError();
        }
        s_juniorTrancheMaxCap = amount;
    }

    function setMaxAllocationCapEquityTranche(
        uint256 amount
    ) external onlyOwner {
        if (amount == 0) {
            revert TranchePool__ZeroValueError();
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

    function _minimum(uint256 a, uint256 b) internal pure returns (uint256) {
        if (a > b) {
            return b;
        } else {
            return a;
        }
    }

    // getters

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

    function getEquityUserIndex(address user) external view returns (uint256) {
        return equityUserIndex[user];
    }

    function getPoolState() external view returns (PoolState) {
        return poolState;
    }

    function getTotalDeployedValue() external view returns (uint256) {
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
}
