// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import {TranchePool} from "../TranchePool.sol";

interface ITranchePool {
    // logic functions

    function withdrawEquityTrancheByAmount(uint256 amount) external;

    function withdrawJuniorTrancheByAmount(uint256 amount) external;

    function withdrawSeniorTrancheByAmount(uint256 amount) external;

    function withdrawEquityTranche(uint256 shares) external;

    function withdrawJuniorTranche(uint256 shares) external;

    function withdrawSeniorTranche(uint256 shares) external;

    function onRepayment(uint256 principal, uint256 interest) external;

    function onRecovery(uint256 amount) external;

    function allocateCapital(
        uint256 totalDisbursement,
        uint256 fees,
        address deployer,
        address feeManager
    ) external;

    function depositEquityTranche(uint256 amount) external;

    function depositJuniorTranche(uint256 amount) external;

    function depositSeniorTranche(uint256 amount) external;

    // updaters
    function updateEqutyTrancheWhiteList(address user, bool status) external;

    function updateWhitelist(address user, bool status) external;

    // setters

    function onLoss(uint256 loss) external;

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

    function getPoolState() external view returns (TranchePool.PoolState);
}
