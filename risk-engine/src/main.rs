use chrono::{DateTime, Duration, Utc};

// ── Scenario knobs ──────────────────────────────────────────────────
const SECONDS_PER_YEAR: i64 = 365 * 24 * 3600;
const BPS_DENOMINATOR: i64 = 10_000;

// Loan parameters
const LOAN_PRINCIPAL: i64 = 100000; // 100k
const LOAN_APR_BPS: u16 = 1000; // 10 %
const LOAN_MATURITY_DAYS: i64 = 720;

// Tranche sizes
const SENIOR_DEPLOYED: i64 = 70000; // 70k
const JUNIOR_DEPLOYED: i64 = 20000; // 20k
const EQUITY_DEPLOYED: i64 = 10000; // 10k

// Tranche target APRs (each tranche has its own cap)
const SENIOR_APR_BPS: u16 = 500;  // 5 % — senior gets a lower, safer rate
const JUNIOR_APR_BPS: u16 = 800;  // 8 % — junior takes more risk, higher cap
                                   // Equity has no target APR — it gets the residual

// Tick duration
const ONE_MONTH_SECS: i64 = 30 * 24 * 3600;

#[derive(Debug, Clone)]
enum LoanState {
    Active,
    Repaid,
    Defaulted,
    WrittenOff,
}

#[derive(Debug, Clone)]
struct Loan {
    id: u32,
    principal_issued: i64,
    principal_outstanding: i64,
    apr_bps: u16,
    interest_accrued: i64,
    interest_paid: i64,
    last_accrual_ts: DateTime<Utc>,
    start_ts: DateTime<Utc>,
    maturity_ts: DateTime<Utc>,
    total_recovered: i64,
    senior_principal_allocated: i64,
    junior_principal_allocated: i64,
    state: LoanState,
}

#[derive(Debug, Clone)]
struct Tranche {
    name: &'static str,
    idle: i64,
    deployed: i64,
    shortfall: i64,
    apr_bps: u16,          // tranche's own target APR (0 for equity = residual)
    target_interest: i64,  // time-weighted ceiling of what this tranche should earn
    accrued_interest: i64, // interest credited to this tranche via waterfall
    paid_interest: i64,    // interest actually paid out (stands in for interest index)
}

#[derive(Debug, Clone)]
struct Pool {
    idle: i64,
    deployed: i64,
    shortfall: i64,
}

#[derive(Debug, Clone)]
struct State {
    now: DateTime<Utc>,
    loan: Vec<Loan>,
    pool: Pool,
    tranches: Vec<Tranche>,
}
#[derive(Debug, Clone)]
enum Event {
    Allocate(i64),
    Repay(i64),
    Default,
    WriteOff,
    Recover(i64),
    /// Advance the clock by `seconds` — accrues interest on every active loan
    /// and distributes it to tranches as target_interest.
    Tick(i64),
}

fn apply_event(mut state: State, event: Event, id: u32) -> State {
    
    match event {
        Event::Allocate(amount) => {
            state.pool.idle -= amount;
            state.pool.deployed += amount;
            for tranche in state.tranches.iter_mut() {
                let allocate = amount.min(tranche.idle);
                tranche.idle -= allocate;
                tranche.deployed += allocate;

                if allocate == amount {
                    break;
                }
            }
        }
        Event::Repay(amount) => {
            // Split repayment into principal + interest portions
            let (principal_portion, interest_portion) = if let Some(loan) =
                state.loan.iter_mut().find(|l| l.id == id)
            {
                accrue_interest(loan, state.now);
                let interest = amount.min(loan.interest_accrued - loan.interest_paid);
                let principal = amount - interest;
                loan.interest_paid += interest;
                loan.principal_outstanding -= principal;
                if loan.principal_outstanding == 0 {
                    loan.state = LoanState::Repaid;
                }
                (principal, interest)
            } else {
                (amount, 0)
            };

            // Return principal to pool & tranches
            state.pool.idle += principal_portion;
            state.pool.deployed -= principal_portion;
            let mut remaining = principal_portion;
            for tranche in state.tranches.iter_mut() {
                let repay = remaining.min(tranche.deployed);
                tranche.deployed -= repay;
                tranche.idle += repay;
                remaining -= repay;
                if remaining == 0 {
                    break;
                }
            }

            // Step 1: onInterestAccrued — waterfall into accrued_interest
            //   Senior/Junior: capped at (target - accrued), Equity: residual
            let mut remaining_interest = interest_portion;
            for tranche in state.tranches.iter_mut() {
                if tranche.apr_bps > 0 {
                    let owed = (tranche.target_interest - tranche.accrued_interest).max(0);
                    let credited = remaining_interest.min(owed);
                    tranche.accrued_interest += credited;
                    remaining_interest -= credited;
                } else {
                    tranche.accrued_interest += remaining_interest;
                    remaining_interest = 0;
                }
            }

            // Step 2: onRepayment — pay out from accrued, deduct both accrued & target
            //   Senior → Junior → Equity
            let mut remaining_payout = interest_portion;
            for tranche in state.tranches.iter_mut() {
                let pay = remaining_payout.min(tranche.accrued_interest);
                tranche.accrued_interest -= pay;
                tranche.target_interest -= tranche.target_interest.min(pay);
                tranche.paid_interest += pay;
                remaining_payout -= pay;
            }
        }

        Event::Default => {
            if let Some(loan) = state.loan.iter_mut().find(|l| l.id == id) {
                loan.state = LoanState::Defaulted;
            }
        }

        Event::WriteOff => {
            if let Some(loan) = state.loan.iter_mut().find(|l| l.id == id) {
                loan.state = LoanState::WrittenOff;
            }

            let mut loss = state.pool.deployed;
            state.pool.deployed = 0;

            // Equity → Junior → Senior
            for tranche in state.tranches.iter_mut().rev() {
                let absorb = loss.min(tranche.deployed);
                tranche.deployed -= absorb;
                tranche.shortfall += absorb;
                loss -= absorb;

                if loss == 0 {
                    break;
                }
            }
        }

        Event::Recover(amount) => {
            state.pool.idle += amount;

            let mut remaining = amount;

            // Senior → Junior → Equity (reverse of loss)
            for tranche in state.tranches.iter_mut() {
                let restore = remaining.min(tranche.shortfall);
                tranche.idle += restore;
                tranche.shortfall -= restore;
                remaining -= restore;

                if remaining == 0 {
                    break;
                }
            }
        }

        Event::Tick(seconds) => {
            let new_now = state.now + Duration::seconds(seconds);

            // 1. Accrue interest on every active loan (borrower's debt)
            for loan in state.loan.iter_mut() {
                if matches!(loan.state, LoanState::Active) {
                    accrue_interest(loan, new_now);
                }
            }

            // 2. Accrue tranche targets — each tranche uses its OWN apr_bps
            //    Mirrors on-chain _accrueTrancheTargets():
            //      targetInterest += deployedValue * aprBps * dt / (YEAR * 10000)
            //    Equity (apr_bps = 0) gets no target — it receives the residual on repay.
            for tranche in state.tranches.iter_mut() {
                if tranche.apr_bps > 0 {
                    let target = tranche.deployed
                        * tranche.apr_bps as i64
                        * seconds
                        / (SECONDS_PER_YEAR * BPS_DENOMINATOR);
                    tranche.target_interest += target;
                }
            }

            state.now = new_now;
        }
    }

    state
}

fn new_tranche(name: &'static str, deployed: i64, apr_bps: u16) -> Tranche {
    Tranche {
        name,
        idle: 0,
        deployed,
        shortfall: 0,
        apr_bps,
        target_interest: 0,
        accrued_interest: 0,
        paid_interest: 0,
    }
}

fn accrue_interest(loan: &mut Loan, now: DateTime<Utc>) {
    let dt = now - loan.last_accrual_ts;
    let seconds = dt.num_seconds() as i64;

    let interest = loan.principal_outstanding
        * loan.apr_bps as i64
        * seconds
        / (SECONDS_PER_YEAR * BPS_DENOMINATOR);

    loan.interest_accrued += interest;
    loan.last_accrual_ts = now;
}

fn initial_state() -> State {
    let senior = new_tranche("Senior", SENIOR_DEPLOYED, SENIOR_APR_BPS);
    let junior = new_tranche("Junior", JUNIOR_DEPLOYED, JUNIOR_APR_BPS);
    let equity = new_tranche("Equity", EQUITY_DEPLOYED, 0); // equity = residual, no target APR

    let start = Utc::now();
    State {
        now: start,
        loan: vec![Loan {
            id: 1,
            principal_issued: LOAN_PRINCIPAL,
            principal_outstanding: LOAN_PRINCIPAL,
            apr_bps: LOAN_APR_BPS,
            interest_accrued: 0,
            interest_paid: 0,
            last_accrual_ts: start,
            start_ts: start,
            maturity_ts: start + Duration::days(LOAN_MATURITY_DAYS),
            total_recovered: 0,
            senior_principal_allocated: SENIOR_DEPLOYED,
            junior_principal_allocated: JUNIOR_DEPLOYED + EQUITY_DEPLOYED,
            state: LoanState::Active,
        }],
        pool: Pool {
            
            idle: 0,
            deployed: LOAN_PRINCIPAL,
            shortfall: 0,
        },
        tranches: vec![senior, junior, equity],
    }
}

fn main() {
    let mut state = initial_state();

    println!("Initial: {:#?}", state);

    let events = vec![
        Event::Tick(ONE_MONTH_SECS),     // 1 month passes, interest accrues
        Event::Repay(40000),
        Event::Tick(ONE_MONTH_SECS),     // another month
        Event::Default,
        Event::WriteOff,
        Event::Recover(30000),
    ];

    let loan_id = 1;
    for event in events {
        println!("applied event: {:#?}", event);
        state = apply_event(state, event, loan_id);
        println!("After event: {:#?}", state);
    }

    let senior_tranche_idle_value = state.tranches.iter().find(|t| t.name == "Senior").unwrap().idle;
    let senior_tranche_deployed_value = state.tranches.iter().find(|t| t.name == "Senior").unwrap().deployed;
    let junior_tranche_idle_value = state.tranches.iter().find(|t| t.name == "Junior").unwrap().idle;
    let junior_tranche_deployed_value = state.tranches.iter().find(|t| t.name == "Junior").unwrap().deployed;
    let equity_tranche_idle_value = state.tranches.iter().find(|t| t.name == "Equity").unwrap().idle;
    let equity_tranche_deployed_value = state.tranches.iter().find(|t| t.name == "Equity").unwrap().deployed;
    if senior_tranche_idle_value + junior_tranche_idle_value + equity_tranche_idle_value == state.pool.idle {
        println!("Idle value is consistent with pool idle");
    } else {
        println!("Idle value is NOT consistent with pool idle");
    }

    if senior_tranche_deployed_value + junior_tranche_deployed_value + equity_tranche_deployed_value == state.pool.deployed{
        println!("Deployed value is consistent with pool deployed");
    } else {
        println!("Deployed value is NOT consistent with pool deployed");
    }
}
