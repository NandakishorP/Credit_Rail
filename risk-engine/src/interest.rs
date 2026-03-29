use crate::types::{BPS_DENOMINATOR, SECONDS_PER_YEAR};

/// Mirrors InterestMath.accrueTargetInterest()
/// (deployedValue * aprBps * timeElapsed) / (SECONDS_PER_YEAR * BPS_DENOMINATOR)
pub fn accrue_target_interest(deployed: i64, apr_bps: u16, seconds: i64) -> i64 {
    if deployed == 0 || seconds == 0 {
        return 0;
    }
    deployed * apr_bps as i64 * seconds / (SECONDS_PER_YEAR * BPS_DENOMINATOR)
}

/// Mirrors InterestMath on loan level:
/// (principalOutstanding * aprBps * timeElapsed) / (SECONDS_PER_YEAR * BPS_DENOMINATOR)
pub fn compute_loan_interest(principal: i64, apr_bps: u16, seconds: i64) -> i64 {
    if principal == 0 || seconds == 0 {
        return 0;
    }
    principal * apr_bps as i64 * seconds / (SECONDS_PER_YEAR * BPS_DENOMINATOR)
}
