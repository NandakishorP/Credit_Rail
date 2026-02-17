// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

interface ITranchePool {
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
    error TranchePool__DeployedCapitalExists();
    error TranchePool__InvalidMaxCapAmount();
    error TranchePool__InvalidMinDepositAmount();
    error TranchePool__InterestNotClaimed();
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

    // logic functions

    function withdrawEquityTrancheByAmount(uint256 amount) external;

    function withdrawJuniorTrancheByAmount(uint256 amount) external;

    function withdrawSeniorTrancheByAmount(uint256 amount) external;

    function withdrawEquityTranche(uint256 shares) external;

    function withdrawJuniorTranche(uint256 shares) external;

    function withdrawSeniorTranche(uint256 shares) external;

    function onInterestAccrued(uint256 interestAmount) external;

    function onRepayment(
        uint256 principalRepaid,
        uint256 interestRepaid
    ) external;

    function onRecovery(uint256 amount) external;

    function allocateCapital(
        uint256 totalDisbursement,
        uint256 fees,
        address deployer,
        address feeManager
    )
        external
        returns (
            uint256 seniorAmount,
            uint256 juniorAmount,
            uint256 equityAmount
        );

    function depositEquityTranche(uint256 amount) external;

    function depositJuniorTranche(uint256 amount) external;

    function depositSeniorTranche(uint256 amount) external;

    // updaters
    function updateEquityTrancheWhiteList(address user, bool status) external;

    function updateWhitelist(address user, bool status) external;

    // setters

    function onLoss(uint256 principalLoss, uint256 interestAccrued) external;

    function setLoanEngine(address _loanEngine) external;

    function setTargetJuniorAPR(uint256 apr) external;

    function setSeniorAPR(uint256 apr) external;

    function setTrancheCapitalAllocationFactorJunior(uint256 factor) external;

    function setTrancheCapitalAllocationFactorSenior(uint256 factor) external;

    function setMinimumDepositAmountEquityTranche(uint256 amount) external;

    function setMinimumDepositAmountSeniorTranche(uint256 amount) external;

    function setMinimumDepositAmountJuniorTranche(uint256 amount) external;

    // getters
    function getEquityTrancheBalance(
        address user
    ) external view returns (uint256);

    function getJuniorTrancheBalance(
        address user
    ) external view returns (uint256);

    function getSeniorTrancheBalance(
        address user
    ) external view returns (uint256);

    function getPoolState() external view returns (PoolState);

    function getSeniorAllocationRatio() external view returns (uint256);

    function getJuniorAllocationRatio() external view returns (uint256);

    function getTotalIdleValue() external view returns (uint256);
}
