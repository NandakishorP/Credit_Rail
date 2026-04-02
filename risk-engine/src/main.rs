mod engine;
mod interest;
mod pool;
mod types;

use chrono::Utc;
use types::*;

fn new_tranche(name: &'static str, idle: i64, apr_bps: u16) -> Tranche {
    Tranche {
        name,
        idle,
        deployed: 0,
        shortfall: 0,
        apr_bps,
        target_interest: 0,
        accrued_interest: 0,
        paid_interest: 0,
    }
}

fn initial_state() -> State {
    let now = Utc::now();
    State {
        now,
        last_tranche_accrual_ts: now,
        loans: vec![],
        pool: Pool {
            idle: SENIOR_DEPOSIT + JUNIOR_DEPOSIT + EQUITY_DEPOSIT,
            deployed: 0,
            shortfall: 0,
            total_loss: 0,
            total_recovered: 0,
        },
        tranches: vec![
            new_tranche("Senior", SENIOR_DEPOSIT, SENIOR_APR_BPS),
            new_tranche("Junior", JUNIOR_DEPOSIT, JUNIOR_APR_BPS),
            new_tranche("Equity", EQUITY_DEPOSIT, 0),
        ],
    }
}

fn apply_event(state: &mut State, event: Event) {
    match event {
        Event::Allocate { id, principal, apr_bps, maturity_days } => {
            engine::allocate_loan(state, id, principal, apr_bps, maturity_days);
        }
        Event::Repay { id, amount } => {
            engine::repay_loan(state, id, amount);
        }
        Event::Default { id } => {
            engine::declare_default(state, id);
        }
        Event::WriteOff { id } => {
            engine::write_off_loan(state, id);
        }
        Event::Recover { id, amount } => {
            engine::recover(state, id, amount);
        }
        Event::Tick(seconds) => {
            engine::tick(state, seconds);
        }
    }
}

// ── Scenario ────────────────────────────────────────────────────────
// Edit this function to define your simulation.
fn scenario() -> Vec<Event> {
    vec![
        // Loan 1: 60k at 10% for 2 years
        Event::Allocate { id: 1, principal: 60_000, apr_bps: 1000, maturity_days: 720 },
        Event::Tick(ONE_MONTH_SECS),

        // Loan 2: 30k at 12% for 1 year
        Event::Allocate { id: 2, principal: 30_000, apr_bps: 1200, maturity_days: 365 },
        Event::Tick(ONE_MONTH_SECS),

        // Loan 1 partial repay
        Event::Repay { id: 1, amount: 20_000 },
        Event::Tick(ONE_MONTH_SECS),

        // Loan 2 defaults
        Event::Default { id: 2 },
        Event::WriteOff { id: 2 },

        Event::Tick(ONE_MONTH_SECS),

        // Recover some from loan 2
        Event::Recover { id: 2, amount: 15_000 },

        // Loan 1 full repay
        Event::Repay { id: 1, amount: 40_000 },

        Event::Tick(ONE_MONTH_SECS),

        Event::Tick(ONE_MONTH_SECS),

        Event::Recover { id: 2, amount: 15_000 },

        Event::Repay { id: 1, amount: 996 },

    ]
}

fn csv_header() -> String {
    [
        "step", "event",
        "pool_idle", "pool_deployed", "pool_shortfall", "pool_loss", "pool_recovered",
        "sr_idle", "sr_deployed", "sr_shortfall", "sr_target", "sr_accrued", "sr_paid",
        "jr_idle", "jr_deployed", "jr_shortfall", "jr_target", "jr_accrued", "jr_paid",
        "eq_idle", "eq_deployed", "eq_shortfall", "eq_target", "eq_accrued", "eq_paid",
        "loan_1_outstanding", "loan_1_interest_accrued", "loan_1_interest_paid", "loan_1_state",
        "loan_2_outstanding", "loan_2_interest_accrued", "loan_2_interest_paid", "loan_2_state",
    ]
    .join(",")
}

fn event_label(event: &Event) -> String {
    match event {
        Event::Allocate { id, principal, .. } => format!("Allocate(id={} amt={})", id, principal),
        Event::Repay { id, amount } => format!("Repay(id={} amt={})", id, amount),
        Event::Default { id } => format!("Default(id={})", id),
        Event::WriteOff { id } => format!("WriteOff(id={})", id),
        Event::Recover { id, amount } => format!("Recover(id={} amt={})", id, amount),
        Event::Tick(s) => format!("Tick({}d)", s / (24 * 3600)),
    }
}

fn loan_fields(state: &State, id: u32) -> String {
    if let Some(loan) = state.loans.iter().find(|l| l.id == id) {
        format!(
            "{},{},{},{:?}",
            loan.principal_outstanding, loan.interest_accrued,
            loan.interest_paid, loan.state
        )
    } else {
        ",,, ".to_string()
    }
}

fn csv_row(step: usize, event: &Event, state: &State) -> String {
    let p = &state.pool;
    let sr = &state.tranches[SENIOR];
    let jr = &state.tranches[JUNIOR];
    let eq = &state.tranches[EQUITY];

    format!(
        "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}",
        step,
        event_label(event),
        p.idle, p.deployed, p.shortfall, p.total_loss, p.total_recovered,
        sr.idle, sr.deployed, sr.shortfall, sr.target_interest, sr.accrued_interest, sr.paid_interest,
        jr.idle, jr.deployed, jr.shortfall, jr.target_interest, jr.accrued_interest, jr.paid_interest,
        eq.idle, eq.deployed, eq.shortfall, eq.target_interest, eq.accrued_interest, eq.paid_interest,
        loan_fields(state, 1),
        loan_fields(state, 2),
    )
}

fn main() {
    use std::fs::File;
    use std::io::Write;

    let mut state = initial_state();
    let mut rows = Vec::new();

    rows.push(csv_header());

    for (i, event) in scenario().into_iter().enumerate() {
        apply_event(&mut state, event.clone());
        rows.push(csv_row(i + 1, &event, &state));
    }

    // Invariant checks as final row
    let tranche_idle: i64 = state.tranches.iter().map(|t| t.idle).sum();
    let tranche_deployed: i64 = state.tranches.iter().map(|t| t.deployed).sum();
    let tranche_shortfall: i64 = state.tranches.iter().map(|t| t.shortfall).sum();

    let idle_ok = state.pool.idle == tranche_idle;
    let deployed_ok = state.pool.deployed == tranche_deployed;
    let shortfall_ok = state.pool.shortfall == tranche_shortfall;

    rows.push(format!(
        ",INVARIANTS,idle={},deployed={},shortfall={},,,,,,,,,,,,,,,,,,,,,,,,,,,,",
        if idle_ok { "OK" } else { "MISMATCH" },
        if deployed_ok { "OK" } else { "MISMATCH" },
        if shortfall_ok { "OK" } else { "MISMATCH" },
    ));

    let csv = rows.join("\n");

    // Write to file
    let path = "output.csv";
    let mut file = File::create(path).expect("could not create output.csv");
    file.write_all(csv.as_bytes()).expect("could not write output.csv");

    println!("Wrote {} rows to {}", rows.len() - 1, path);
    println!(
        "Invariants: idle={} deployed={} shortfall={}",
        if idle_ok { "OK" } else { "MISMATCH" },
        if deployed_ok { "OK" } else { "MISMATCH" },
        if shortfall_ok { "OK" } else { "MISMATCH" },
    );
}
