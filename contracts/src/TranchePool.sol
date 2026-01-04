// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import {SafeERC20, IERC20} from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import {ITranchePool} from "./interfaces/ITranchePool.sol";

contract TranchePool is Ownable, ITranchePool {
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
        uint256 time
    );

    event ProfitTransferredToTranchePool(uint256 amount, uint256 timeStamp);
    event CapitalAllocationFactorUpdatedSenior(uint256 newFactor);
    event CapitalAllocationFactorUpdatedJunior(uint256 newFactor);

    enum PoolState {
        OPEN, // deposits allowed
        DEPLOYED, // capital deployed, deposits paused
        HARVEST, // repayments coming in
        DISTRIBUTION, // interest allocation
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

    // Stable coin
    address public s_stableCoin;
    address public loanEngine;

    // Capital allocation factor (e.g., 80 for 80% senior, 15% junior, 5% equity)
    uint256 public s_capital_allocation_factor_senior;
    uint256 public s_capital_allocation_factor_junior;

    uint256 public s_senior_apr;
    uint256 public s_target_junior_apr;

    uint256 public seniorAccruedInterest;
    uint256 public juniorAccruedInterest;

    PoolState public poolState = PoolState.OPEN;

    modifier isWhiteListed(address user) {
        if (!whiteListedLps[user]) {
            revert TranchePool__NotWhiteListed(user);
        }
        _;
    }

    modifier onlyLoanEngine(address user) {
        if (user != loanEngine) {
            revert TranchePool__InvalidCaller(user);
        }
        _;
    }

    modifier isWhiteListedForEquityTranche(address user) {
        if (!whiteListedForEquityTranche[user]) {
            revert TranchePool__NotWhiteListedForEquityTranche(user);
        }
        _;
    }

    constructor(address stableCoin_) Ownable(msg.sender) {
        s_stableCoin = stableCoin_;
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

        // Calculate shares to mint
        uint256 shares;
        if (s_totalSeniorShares == 0) {
            shares = amount;
        } else {
            // can this share be zero?
            // why is this the right logic to mint the shares?
            // can someone gain disproportionate advantage from this equation
            shares =
                (amount * s_totalSeniorShares) /
                (s_seniorTrancheIdleValue + s_seniorTrancheDeployedValue);
        }

        // why we need this check?
        /*
            say total_value = idle +deployed
            so we need amount * s_totalSeniorShares >= totalValue (invariant)
            so if the deposit is smaller than the value of one share then the user will loss money because the floor
            division in solidity will bring it to zero and for the same reason its placed before the tranfer of funds 
            from the user.
        */
        if (shares == 0) {
            revert TranchePool__ZeroSharesMinted();
        }

        IERC20(s_stableCoin).safeTransferFrom(
            msg.sender,
            address(this),
            amount
        );

        s_seniorTrancheShares[msg.sender] += shares;
        s_totalSeniorShares += shares;
        s_seniorTrancheIdleValue += amount;

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

        uint256 shares;
        if (s_totalJuniorShares == 0) {
            shares = amount;
        } else {
            shares =
                (amount * s_totalJuniorShares) /
                (s_juniorTrancheIdleValue + s_juniorTrancheDeployedValue);
        }

        if (shares == 0) {
            revert TranchePool__ZeroSharesMinted();
        }

        IERC20(s_stableCoin).safeTransferFrom(
            msg.sender,
            address(this),
            amount
        );

        s_juniorTrancheShares[msg.sender] += shares;
        s_totalJuniorShares += shares;
        s_juniorTrancheIdleValue += amount;

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

        uint256 shares;

        if (s_totalEquityShares == 0) {
            shares = amount;
        } else {
            shares =
                (amount * s_totalEquityShares) /
                (s_equityTrancheIdleValue + s_equityTrancheDeployedValue);
        }

        if (shares == 0) {
            revert TranchePool__ZeroSharesMinted();
        }

        IERC20(s_stableCoin).safeTransferFrom(
            msg.sender,
            address(this),
            amount
        );
        s_equityTrancheShares[msg.sender] += shares;
        s_totalEquityShares += shares;
        s_equityTrancheIdleValue += amount;

        emit FundsDepositedToEquityTranche(
            msg.sender,
            amount,
            shares,
            block.timestamp
        );
    }

    /**
     * @notice Allocate capital according to the 80/20 split
     * @param totalAmount Total amount to allocate from the pool
     */
    function allocateCapital(
        uint256 totalAmount,
        address deployer
    ) external onlyOwner {
        if (poolState != PoolState.OPEN) {
            revert TranchePool__PoolIsNotOpen();
        }
        uint256 seniorAmount = (totalAmount *
            s_capital_allocation_factor_senior) / 100;
        uint256 juniorAmount = (totalAmount *
            s_capital_allocation_factor_junior) / 100;
        uint256 equityAmount = totalAmount - (seniorAmount + juniorAmount);
        if (
            seniorAmount > s_seniorTrancheIdleValue ||
            juniorAmount > s_juniorTrancheIdleValue ||
            equityAmount > s_equityTrancheIdleValue
        ) {
            revert TranchePool__InsufficientLiquidity();
        }

        // Simply reduce the total value - shares remain unchanged
        s_seniorTrancheIdleValue -= seniorAmount;
        s_juniorTrancheIdleValue -= juniorAmount;
        s_equityTrancheIdleValue -= equityAmount;

        s_seniorTrancheDeployedValue += seniorAmount;
        s_juniorTrancheDeployedValue += juniorAmount;
        s_equityTrancheDeployedValue += equityAmount;
        poolState = PoolState.DEPLOYED;

        // Transfer funds to wherever they're being deployed
        IERC20(s_stableCoin).safeTransfer(deployer, totalAmount);

        emit CapitalAllocated(seniorAmount, juniorAmount, block.timestamp);
    }

    function onRepayment(
        uint256 principal,
        uint256 interest
    ) external onlyLoanEngine(msg.sender) {
        if (principal + interest == 0) {
            revert TranchePool__InvalidTransferAmount(principal + interest);
        }

        if (interest == 0) {
            revert TranchePool__InvalidTransferAmount(interest);
        }

        IERC20(s_stableCoin).safeTransferFrom(
            loanEngine,
            address(this),
            principal + interest
        );

        uint256 remaining = interest;

        uint256 seniorPaid = _minimum(seniorAccruedInterest, remaining);
        seniorAccruedInterest -= seniorPaid;
        s_seniorTrancheIdleValue += seniorPaid;
        remaining -= seniorPaid;

        uint256 juniorPaid = _minimum(juniorAccruedInterest, remaining);

        juniorAccruedInterest -= juniorPaid;
        s_juniorTrancheIdleValue += juniorPaid;
        remaining -= juniorPaid;

        if (remaining > 0) {
            s_equityTrancheIdleValue += remaining;
        }

        if (principal != 0) {
            uint256 seniorAmount = (principal *
                s_capital_allocation_factor_senior) / 100;
            uint256 juniorAmount = (principal *
                s_capital_allocation_factor_junior) / 100;
            uint256 equityAmount = principal - (seniorAmount + juniorAmount);

            s_seniorTrancheDeployedValue -= seniorAmount;
            s_juniorTrancheDeployedValue -= juniorAmount;
            s_equityTrancheDeployedValue -= equityAmount;

            s_seniorTrancheIdleValue += seniorAmount;
            s_juniorTrancheIdleValue += juniorAmount;
            s_equityTrancheIdleValue += equityAmount;
        }
    }

    function onAccrual(
        uint256 seniorInterest,
        uint256 juniorInterest
    ) external onlyLoanEngine(msg.sender) {
        seniorAccruedInterest += seniorInterest;
        juniorAccruedInterest += juniorInterest;
    }

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

    /**
     * @notice Withdraw from senior tranche by burning shares
     * @param shares Number of shares to burn (0 = withdraw all)
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
            (s_seniorTrancheIdleValue + s_seniorTrancheDeployedValue);

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
            (s_juniorTrancheIdleValue + s_juniorTrancheDeployedValue);

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
    ) external isWhiteListed(msg.sender) {
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
            (s_equityTrancheIdleValue + s_equityTrancheDeployedValue);

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
        if (factor > 100) revert TranchePool__InvalidAllocationRatio();
        s_capital_allocation_factor_senior = factor;
        emit CapitalAllocationFactorUpdatedSenior(factor);
    }

    function setTrancheCapitalAllocationFactorJunior(
        uint256 factor
    ) external onlyOwner {
        if (factor > 100) revert TranchePool__InvalidAllocationRatio();
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

        emit PoolStateUpdated(newState);
    }

    function setLoanEngine(address _loanEngine) external onlyOwner {
        loanEngine = _loanEngine;
    }

    function updateWhitelist(address user, bool status) external onlyOwner {
        whiteListedLps[user] = status;
    }

    function updateEqutyTrancheWhiteList(
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
}
