// SPDX-License-Identifier: MIT
pragma solidity 0.8.30;

import {InterestMath} from "../../src/libraries/InterestMath.sol";

/// @title InterestMathHarness
/// @notice Wraps the internal library functions as external for Certora verification.
contract InterestMathHarness {

    function accrueTargetInterest(
        uint256 deployedValue,
        uint256 aprBps,
        uint256 timeElapsed
    ) external pure returns (uint256) {
        return InterestMath.accrueTargetInterest(deployedValue, aprBps, timeElapsed);
    }

    function calculateClaimable(
        uint256 userShares,
        uint256 currentIndex,
        uint256 userIndex
    ) external pure returns (uint256) {
        return InterestMath.calculateClaimable(userShares, currentIndex, userIndex);
    }

    function computeIndexDelta(
        uint256 paidAmount,
        uint256 totalShares
    ) external pure returns (uint256) {
        return InterestMath.computeIndexDelta(paidAmount, totalShares);
    }
}
