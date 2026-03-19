/*
 * Certora Verification Spec — InterestMath
 *
 * Pure math library — ideal for formal verification.
 * Properties:
 *   1. Zero inputs produce zero outputs
 *   2. Monotonicity (more time/principal/apr = more interest)
 *   3. Linearity in time
 *   4. Index round-trip: no over-distribution
 *   5. No division by zero panics
 */

using InterestMathHarness as im;

methods {
    function im.accrueTargetInterest(uint256, uint256, uint256) external returns (uint256) envfree;
    function im.calculateClaimable(uint256, uint256, uint256) external returns (uint256) envfree;
    function im.computeIndexDelta(uint256, uint256) external returns (uint256) envfree;
}

// ═══════════════════════════════════════════════════════════════════════
//                     accrueTargetInterest
// ═══════════════════════════════════════════════════════════════════════

/// @title zero-deployed-zero-interest
/// No capital deployed → no interest accrues.
rule zeroDeployedZeroInterest(uint256 aprBps, uint256 timeElapsed) {
    assert im.accrueTargetInterest(0, aprBps, timeElapsed) == 0;
}

/// @title zero-time-zero-interest
/// No time elapsed → no interest accrues.
rule zeroTimeZeroInterest(uint256 deployedValue, uint256 aprBps) {
    assert im.accrueTargetInterest(deployedValue, aprBps, 0) == 0;
}

/// @title interest-monotonic-in-time
/// More time elapsed → equal or more interest.
rule interestMonotonicInTime(uint256 deployed, uint256 apr, uint256 t1, uint256 t2) {
    require deployed <= 10^30;
    require apr <= 10000;
    require t1 <= 365 * 86400;
    require t2 <= 365 * 86400;
    require t1 <= t2;

    uint256 i1 = im.accrueTargetInterest(deployed, apr, t1);
    uint256 i2 = im.accrueTargetInterest(deployed, apr, t2);

    assert i2 >= i1;
}

/// @title interest-monotonic-in-principal
/// More principal → equal or more interest.
rule interestMonotonicInPrincipal(uint256 d1, uint256 d2, uint256 apr, uint256 t) {
    require d1 <= 10^30;
    require d2 <= 10^30;
    require apr <= 10000;
    require t <= 365 * 86400;
    require d1 <= d2;

    uint256 i1 = im.accrueTargetInterest(d1, apr, t);
    uint256 i2 = im.accrueTargetInterest(d2, apr, t);

    assert i2 >= i1;
}

/// @title interest-linear-in-time
/// interest(t1 + t2) == interest(t1) + interest(t2)
/// Holds exactly because the formula is linear (no compounding).
rule interestLinearInTime(uint256 deployed, uint256 apr, uint256 t1, uint256 t2) {
    require deployed <= 10^30;
    require apr <= 10000;
    require t1 <= 180 * 86400;
    require t2 <= 180 * 86400;

    require to_mathint(t1) + to_mathint(t2) <= to_mathint(max_uint256);
    mathint combined = im.accrueTargetInterest(deployed, apr, require_uint256(t1 + t2));
    mathint additive = im.accrueTargetInterest(deployed, apr, t1)
                     + im.accrueTargetInterest(deployed, apr, t2);

    assert combined == additive;
}

// ═══════════════════════════════════════════════════════════════════════
//                     calculateClaimable
// ═══════════════════════════════════════════════════════════════════════

/// @title no-claim-when-index-equal
/// If user's index == current index, claimable is 0.
rule noClaimWhenIndexEqual(uint256 shares, uint256 idx) {
    assert im.calculateClaimable(shares, idx, idx) == 0;
}

/// @title no-claim-with-zero-shares
/// Zero shares → zero claimable.
rule noClaimWithZeroShares(uint256 currentIdx, uint256 userIdx) {
    assert im.calculateClaimable(0, currentIdx, userIdx) == 0;
}

/// @title claimable-monotonic-in-shares
/// More shares → equal or more claimable.
rule claimableMonotonicInShares(uint256 s1, uint256 s2, uint256 curIdx, uint256 userIdx) {
    require s1 <= s2;
    require s1 <= 10^30;
    require s2 <= 10^30;
    require curIdx >= userIdx;
    require curIdx <= 10^30;

    uint256 c1 = im.calculateClaimable(s1, curIdx, userIdx);
    uint256 c2 = im.calculateClaimable(s2, curIdx, userIdx);

    assert c2 >= c1;
}

// ═══════════════════════════════════════════════════════════════════════
//                    computeIndexDelta + round-trip
// ═══════════════════════════════════════════════════════════════════════

/// @title zero-shares-zero-delta
/// If no shares outstanding, index delta is 0 (no division by zero).
rule zeroSharesZeroDelta(uint256 paid) {
    assert im.computeIndexDelta(paid, 0) == 0;
}

/// @title no-over-distribution
/// A single user holding all shares can never claim more than was paid.
rule noOverDistribution(uint256 paid, uint256 totalShares) {
    require totalShares > 0;
    require totalShares <= 10^30;
    require paid <= 10^30;

    uint256 delta = im.computeIndexDelta(paid, totalShares);
    uint256 baseIndex = 1000000000000000000; // 1e18
    require to_mathint(baseIndex) + to_mathint(delta) <= to_mathint(max_uint256);
    uint256 claimable = im.calculateClaimable(totalShares, require_uint256(baseIndex + delta), baseIndex);

    assert claimable <= paid,
        "User can claim more than was distributed - critical accounting bug";
}
