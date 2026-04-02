use chrono::{DateTime, Utc};

// ── Scenario knobs ──────────────────────────────────────────────────
pub const SECONDS_PER_YEAR: i64 = 365 * 24 * 3600;
pub const BPS_DENOMINATOR: i64 = 10_000;

// Pool deposits (idle capital before any loans)
pub const SENIOR_DEPOSIT: i64 = 70_000;
pub const JUNIOR_DEPOSIT: i64 = 20_000;
pub const EQUITY_DEPOSIT: i64 = 10_000;

// Allocation ratios (must sum to 100)
pub const SENIOR_ALLOC_PCT: i64 = 70;
pub const JUNIOR_ALLOC_PCT: i64 = 20;
pub const EQUITY_ALLOC_PCT: i64 = 10;

// Tranche target APRs
pub const SENIOR_APR_BPS: u16 = 500; // 5 %
pub const JUNIOR_APR_BPS: u16 = 1200; // 8 %

// Tick duration
pub const ONE_MONTH_SECS: i64 = 30 * 24 * 3600;

// Tranche indices (mirrors Solidity SENIOR=0, JUNIOR=1, EQUITY=2)
pub const SENIOR: usize = 0;
pub const JUNIOR: usize = 1;
pub const EQUITY: usize = 2;

#[derive(Debug, Clone, PartialEq)]
pub enum LoanState {
    Active,
    Repaid,
    Defaulted,
    WrittenOff,
}

#[derive(Debug, Clone)]
pub struct Loan {
    pub id: u32,
    pub principal_issued: i64,
    pub principal_outstanding: i64,
    pub apr_bps: u16,
    pub interest_accrued: i64,
    pub interest_paid: i64,
    pub last_accrual_ts: DateTime<Utc>,
    pub start_ts: DateTime<Utc>,
    pub maturity_ts: DateTime<Utc>,
    pub total_recovered: i64,
    pub state: LoanState,
}

#[derive(Debug, Clone)]
pub struct Tranche {
    pub name: &'static str,
    pub idle: i64,
    pub deployed: i64,
    pub shortfall: i64,
    pub apr_bps: u16,
    pub target_interest: i64,
    pub accrued_interest: i64,
    pub paid_interest: i64,
}

#[derive(Debug, Clone)]
pub struct Pool {
    pub idle: i64,
    pub deployed: i64,
    pub shortfall: i64,
    pub total_loss: i64,
    pub total_recovered: i64,
}

#[derive(Debug, Clone)]
pub struct State {
    pub now: DateTime<Utc>,
    pub last_tranche_accrual_ts: DateTime<Utc>,
    pub loans: Vec<Loan>,
    pub pool: Pool,
    pub tranches: Vec<Tranche>,
}

#[derive(Debug, Clone)]
pub enum Event {
    Allocate { id: u32, principal: i64, apr_bps: u16, maturity_days: i64 },
    Repay { id: u32, amount: i64 },
    Default { id: u32 },
    WriteOff { id: u32 },
    Recover { id: u32, amount: i64 },
    Tick(i64),
}
