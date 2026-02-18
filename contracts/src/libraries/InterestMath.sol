// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/**
 * @title InterestMath
 * @notice Pure math helpers for tranche interest calculations.
 * @dev All functions are `internal pure` / `internal view`-free so the
 *      compiler inlines them and there is zero deployment overhead.
 *
 *  Conventions
 *  ───────────
 *  • APR is expressed in basis points (1 bp = 0.01 %).
 *  • Interest indices use 1e18 fixed-point precision.
 *  • Time is in seconds; a year is 365 days (31 536 000 s).
 */
library InterestMath {
    /// @dev 1e18 — the base scaling factor for interest indices.
    uint256 internal constant INDEX_PRECISION = 1e18;

    /// @dev Seconds in a 365-day year.
    uint256 internal constant SECONDS_PER_YEAR = 365 days;

    /// @dev Basis-point denominator (100 % = 10 000 bp).
    uint256 internal constant BPS_DENOMINATOR = 10_000;

    /**
     * @notice Compute the target interest accrued over `timeElapsed` for a
     *         given principal at a given APR.
     * @param deployedValue  The principal deployed (idle capital does NOT accrue).
     * @param aprBps         Annual percentage rate in basis points.
     * @param timeElapsed    Seconds since the last accrual.
     * @return accrued       The interest amount that should be added to the
     *                       tranche's target.
     */
    function accrueTargetInterest(
        uint256 deployedValue,
        uint256 aprBps,
        uint256 timeElapsed
    ) internal pure returns (uint256 accrued) {
        if (deployedValue == 0 || timeElapsed == 0) return 0;
        accrued =
            (deployedValue * aprBps * timeElapsed) /
            (SECONDS_PER_YEAR * BPS_DENOMINATOR);
    }

    /**
     * @notice Compute how much interest a user can claim using the global
     *         index-delta pattern.
     * @param userShares     Number of shares the user holds in the tranche.
     * @param currentIndex   The tranche's current global interest index (1e18).
     * @param userIndex      The user's last-claimed index snapshot (1e18).
     * @return claimable     Amount of stablecoin interest the user may withdraw.
     */
    function calculateClaimable(
        uint256 userShares,
        uint256 currentIndex,
        uint256 userIndex
    ) internal pure returns (uint256 claimable) {
        if (userShares == 0 || currentIndex <= userIndex) return 0;
        claimable = (userShares * (currentIndex - userIndex)) / INDEX_PRECISION;
    }

    /**
     * @notice Compute the new interest index increment when distributing
     *         `paidAmount` across `totalShares`.
     * @param paidAmount     Amount of interest being distributed.
     * @param totalShares    Total shares outstanding in the tranche.
     * @return indexDelta    The value to add to the global interest index.
     */
    function computeIndexDelta(
        uint256 paidAmount,
        uint256 totalShares
    ) internal pure returns (uint256 indexDelta) {
        if (totalShares == 0) return 0;
        indexDelta = (paidAmount * INDEX_PRECISION) / totalShares;
    }
}
