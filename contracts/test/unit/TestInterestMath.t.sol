// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Test} from "forge-std/Test.sol";
import {InterestMath} from "../../src/libraries/InterestMath.sol";

/**
 * @title TestInterestMath
 * @notice Direct unit tests for the InterestMath library.
 * @dev Tests all three pure functions with zero inputs, known values,
 *      boundary conditions, and precision checks.
 */
contract TestInterestMath is Test {
    uint256 constant INDEX_PRECISION = 1e18;
    uint256 constant SECONDS_PER_YEAR = 365 days;
    uint256 constant BPS_DENOMINATOR = 10_000;

    // =========================================================================
    //                    accrueTargetInterest
    // =========================================================================

    function test_AccrueTargetInterest_ZeroDeployed_ReturnsZero() public pure {
        uint256 result = InterestMath.accrueTargetInterest(0, 500, 365 days);
        assertEq(result, 0, "Should return 0 when deployedValue is 0");
    }

    function test_AccrueTargetInterest_ZeroTime_ReturnsZero() public pure {
        uint256 result = InterestMath.accrueTargetInterest(1_000_000e6, 500, 0);
        assertEq(result, 0, "Should return 0 when timeElapsed is 0");
    }

    function test_AccrueTargetInterest_ZeroBoth_ReturnsZero() public pure {
        uint256 result = InterestMath.accrueTargetInterest(0, 500, 0);
        assertEq(result, 0);
    }

    function test_AccrueTargetInterest_OneYear_5Percent() public pure {
        // 1,000,000 USDC at 5% (500 bps) for 1 year = 50,000 USDC
        uint256 deployed = 1_000_000e6;
        uint256 aprBps = 500;
        uint256 time = SECONDS_PER_YEAR;

        uint256 result = InterestMath.accrueTargetInterest(
            deployed,
            aprBps,
            time
        );
        assertEq(result, 50_000e6, "1M at 5% for 1 year = 50K");
    }

    function test_AccrueTargetInterest_HalfYear_8Percent() public pure {
        // 2,000,000 at 8% (800 bps) for 182.5 days
        uint256 deployed = 2_000_000e6;
        uint256 aprBps = 800;
        uint256 halfYear = SECONDS_PER_YEAR / 2;

        uint256 result = InterestMath.accrueTargetInterest(
            deployed,
            aprBps,
            halfYear
        );
        // Expected: 2M * 800 * (365*86400/2) / (365*86400 * 10000)
        //         = 2M * 800 / (2 * 10000) = 2M * 0.04 = 80,000
        assertEq(result, 80_000e6, "2M at 8% for half year = 80K");
    }

    function test_AccrueTargetInterest_OneDay() public pure {
        // 10,000,000 at 10% for 1 day
        uint256 deployed = 10_000_000e6;
        uint256 aprBps = 1000; // 10%
        uint256 oneDay = 1 days;

        uint256 result = InterestMath.accrueTargetInterest(
            deployed,
            aprBps,
            oneDay
        );
        // Expected: 10M * 1000 * 86400 / (31536000 * 10000) = 2739726027 (≈ 2739.73 USDC)
        uint256 expected = (deployed * aprBps * oneDay) /
            (SECONDS_PER_YEAR * BPS_DENOMINATOR);
        assertEq(result, expected);
        // Sanity: roughly 10M * 10% / 365 ≈ 2739.73
        assertApproxEqAbs(result, 2739726027, 1);
    }

    function test_AccrueTargetInterest_SmallValues_Precision() public pure {
        // Very small: 1 token unit at 1 bps for 1 second → should truncate to 0
        uint256 result = InterestMath.accrueTargetInterest(1, 1, 1);
        assertEq(
            result,
            0,
            "Tiny values should truncate to 0 due to integer division"
        );
    }

    function test_AccrueTargetInterest_LargeValues_NoOverflow() public pure {
        // Max reasonable: $10B (1e10 * 1e6) at 100% (10000 bps) for 10 years
        uint256 deployed = 10_000_000_000e6;
        uint256 aprBps = 10_000;
        uint256 time = 10 * SECONDS_PER_YEAR;

        uint256 result = InterestMath.accrueTargetInterest(
            deployed,
            aprBps,
            time
        );
        // 10B * 100% * 10 years = 100B
        assertEq(result, 100_000_000_000e6);
    }

    // =========================================================================
    //                    calculateClaimable
    // =========================================================================

    function test_CalculateClaimable_ZeroShares_ReturnsZero() public pure {
        uint256 result = InterestMath.calculateClaimable(0, 2e18, 1e18);
        assertEq(result, 0, "Should return 0 when userShares is 0");
    }

    function test_CalculateClaimable_IndexEqual_ReturnsZero() public pure {
        uint256 result = InterestMath.calculateClaimable(1000e6, 1e18, 1e18);
        assertEq(result, 0, "Should return 0 when indices are equal");
    }

    function test_CalculateClaimable_UserIndexHigher_ReturnsZero() public pure {
        uint256 result = InterestMath.calculateClaimable(1000e6, 1e18, 2e18);
        assertEq(result, 0, "Should return 0 when userIndex > currentIndex");
    }

    function test_CalculateClaimable_KnownValues() public pure {
        // 1000 shares, index moved from 1e18 to 1.05e18 (5% increase)
        uint256 userShares = 1000e6;
        uint256 currentIndex = 1.05e18;
        uint256 userIndex = 1e18;

        uint256 result = InterestMath.calculateClaimable(
            userShares,
            currentIndex,
            userIndex
        );
        // Expected: 1000e6 * 0.05e18 / 1e18 = 50e6
        assertEq(result, 50e6, "1000 shares with 5% index delta = 50");
    }

    function test_CalculateClaimable_LargeIndexDelta() public pure {
        // 5M shares, index 1e18 → 2e18 (100% gain)
        uint256 result = InterestMath.calculateClaimable(
            5_000_000e6,
            2e18,
            1e18
        );
        assertEq(result, 5_000_000e6, "5M shares with 100% delta = 5M");
    }

    function test_CalculateClaimable_TinyDelta() public pure {
        // Very small index delta with few shares → truncates to 0
        uint256 result = InterestMath.calculateClaimable(1, 1e18 + 1, 1e18);
        // 1 * 1 / 1e18 = 0
        assertEq(result, 0, "Tiny delta with 1 share truncates to 0");
    }

    // =========================================================================
    //                    computeIndexDelta
    // =========================================================================

    function test_ComputeIndexDelta_ZeroShares_ReturnsZero() public pure {
        uint256 result = InterestMath.computeIndexDelta(1000e6, 0);
        assertEq(result, 0, "Should return 0 when totalShares is 0");
    }

    function test_ComputeIndexDelta_ZeroPaid_ReturnsZero() public pure {
        uint256 result = InterestMath.computeIndexDelta(0, 1000e6);
        assertEq(result, 0, "Should return 0 when paidAmount is 0");
    }

    function test_ComputeIndexDelta_KnownValues() public pure {
        // Distribute 50,000 USDC across 1,000,000 shares
        uint256 paid = 50_000e6;
        uint256 shares = 1_000_000e6;

        uint256 result = InterestMath.computeIndexDelta(paid, shares);
        // Expected: 50_000e6 * 1e18 / 1_000_000e6 = 5e16 (0.05)
        assertEq(result, 5e16, "50K across 1M shares = 0.05 index increment");
    }

    function test_ComputeIndexDelta_EqualAmountAndShares() public pure {
        // Distributing X across X shares = 1e18 index delta
        uint256 result = InterestMath.computeIndexDelta(1000e6, 1000e6);
        assertEq(result, INDEX_PRECISION, "Equal paid/shares = 1.0 index");
    }

    function test_ComputeIndexDelta_PaidGreaterThanShares() public pure {
        // 2x payout → 2.0 index delta
        uint256 result = InterestMath.computeIndexDelta(2000e6, 1000e6);
        assertEq(result, 2e18, "2x payout = 2.0 index delta");
    }

    function test_ComputeIndexDelta_TinyPaid_LargeShares() public pure {
        // 1 unit across 1B shares → 1 * 1e18 / 1e15 = 1000 index-wei
        uint256 result = InterestMath.computeIndexDelta(1, 1_000_000_000e6);
        assertEq(
            result,
            1000,
            "Tiny payout across huge shares = 1000 index-wei"
        );
    }

    // =========================================================================
    //                    Round-trip consistency
    // =========================================================================

    function test_Roundtrip_IndexDelta_ThenClaimable() public pure {
        // Distribute 100K across 2M shares → index delta
        uint256 paid = 100_000e6;
        uint256 totalShares = 2_000_000e6;

        uint256 indexDelta = InterestMath.computeIndexDelta(paid, totalShares);

        // A user with 500K shares should claim 500K/2M * 100K = 25K
        uint256 userShares = 500_000e6;
        uint256 claimable = InterestMath.calculateClaimable(
            userShares,
            INDEX_PRECISION + indexDelta,
            INDEX_PRECISION
        );
        assertEq(claimable, 25_000e6, "25% of shares claims 25% of interest");
    }

    function test_Roundtrip_TotalClaimable_EqualsDistributed() public pure {
        // Two users with equal shares should each claim half
        uint256 paid = 60_000e6;
        uint256 totalShares = 1_000_000e6;

        uint256 indexDelta = InterestMath.computeIndexDelta(paid, totalShares);
        uint256 newIndex = INDEX_PRECISION + indexDelta;

        uint256 claim1 = InterestMath.calculateClaimable(
            500_000e6,
            newIndex,
            INDEX_PRECISION
        );
        uint256 claim2 = InterestMath.calculateClaimable(
            500_000e6,
            newIndex,
            INDEX_PRECISION
        );

        assertEq(claim1, 30_000e6);
        assertEq(claim2, 30_000e6);
        assertEq(
            claim1 + claim2,
            paid,
            "Total claims should equal distributed"
        );
    }
}
