use chrono::Duration;

use crate::interest::compute_loan_interest;
use crate::pool;
use crate::types::*;

/// Mirrors LoanEngine._accrueInterest() — accrues interest on a single loan
/// and notifies the pool via on_interest_accrued.
fn accrue_interest(state: &mut State, loan_id: u32) {
    // Compute interest on the loan
    let (interest, accrued_ts) = {
        let loan = match state.loans.iter().find(|l| l.id == loan_id) {
            Some(l) => l,
            None => return,
        };
        if loan.state != LoanState::Active {
            return;
        }
        let elapsed = (state.now - loan.last_accrual_ts).num_seconds();
        let interest =
            compute_loan_interest(loan.principal_outstanding, loan.apr_bps, elapsed);
        (interest, state.now)
    };

    // Update the loan
    let loan = state.loans.iter_mut().find(|l| l.id == loan_id).unwrap();
    loan.last_accrual_ts = accrued_ts;
    if interest > 0 {
        loan.interest_accrued += interest;
        // Notify pool — mirrors i_tranchePool.onInterestAccrued(interest)
        pool::on_interest_accrued(state, interest);
    }
}

/// Mirrors LoanEngine.activateLoan() — creates loan and allocates capital.
pub fn allocate_loan(
    state: &mut State,
    id: u32,
    principal: i64,
    apr_bps: u16,
    maturity_days: i64,
) {
    let loan = Loan {
        id,
        principal_issued: principal,
        principal_outstanding: principal,
        apr_bps,
        interest_accrued: 0,
        interest_paid: 0,
        last_accrual_ts: state.now,
        start_ts: state.now,
        maturity_ts: state.now + Duration::days(maturity_days),
        total_recovered: 0,
        state: LoanState::Active,
    };
    state.loans.push(loan);

    // Mirrors i_tranchePool.allocateCapital(principal)
    pool::allocate_capital(state, principal);
}

/// Mirrors LoanEngine.repayLoan() — accrues interest, splits payment
/// interest-first then principal, notifies pool.
pub fn repay_loan(state: &mut State, id: u32, total_payment: i64) {
    // Step 1: accrue interest up to now (calls on_interest_accrued internally)
    accrue_interest(state, id);

    // Step 2: split payment — interest first, then principal
    let (principal_paid, interest_paid) = {
        let loan = match state.loans.iter_mut().find(|l| l.id == id) {
            Some(l) => l,
            None => return,
        };

        let interest_due = loan.interest_accrued - loan.interest_paid;
        let interest_paid = total_payment.min(interest_due);
        let remaining = total_payment - interest_paid;
        let principal_paid = remaining.min(loan.principal_outstanding);

        loan.interest_paid += interest_paid;
        loan.interest_accrued -= interest_paid;
        loan.principal_outstanding -= principal_paid;

        if loan.principal_outstanding == 0 && loan.interest_accrued == 0 {
            loan.state = LoanState::Repaid;
        }

        (principal_paid, interest_paid)
    };

    // Step 3: notify pool — mirrors i_tranchePool.onRepayment(principal, interest)
    pool::on_repayment(state, principal_paid, interest_paid);
}

/// Mirrors LoanEngine.declareDefault() — accrues interest and marks defaulted.
/// No pool state changes — loss is deferred to write_off.
pub fn declare_default(state: &mut State, id: u32) {
    // Accrue interest up to now (calls on_interest_accrued internally)
    accrue_interest(state, id);

    if let Some(loan) = state.loans.iter_mut().find(|l| l.id == id) {
        loan.state = LoanState::Defaulted;
    }
}

/// Mirrors LoanEngine.writeOffLoan() — zeros loan, calls onLoss with
/// both principal and interest losses.
pub fn write_off_loan(state: &mut State, id: u32) {
    let (principal_loss, interest_loss) = {
        let loan = match state.loans.iter_mut().find(|l| l.id == id) {
            Some(l) => l,
            None => return,
        };

        let principal_loss = loan.principal_outstanding;
        let interest_loss = loan.interest_accrued;

        // Zero out the loan
        loan.principal_outstanding = 0;
        loan.interest_accrued = 0;
        loan.state = LoanState::WrittenOff;

        (principal_loss, interest_loss)
    };

    // Mirrors i_tranchePool.onLoss(principalLoss, interestLoss)
    pool::on_loss(state, principal_loss, interest_loss);
}

/// Mirrors recovery flow — records recovery on loan, notifies pool.
pub fn recover(state: &mut State, id: u32, amount: i64) {
    if let Some(loan) = state.loans.iter_mut().find(|l| l.id == id) {
        loan.total_recovered += amount;
    }

    pool::on_recovery(state, amount);
}

/// Advance the simulation clock. Accrues interest on all active loans
/// (which triggers on_interest_accrued per loan) and accrues tranche targets.
pub fn tick(state: &mut State, seconds: i64) {
    state.now = state.now + Duration::seconds(seconds);

    // Accrue interest on every active loan — each one notifies the pool
    let active_ids: Vec<u32> = state
        .loans
        .iter()
        .filter(|l| l.state == LoanState::Active)
        .map(|l| l.id)
        .collect();

    for id in active_ids {
        accrue_interest(state, id);
    }

    // Ensure tranche targets are up to date even if there are no active loans
    pool::accrue_tranche_targets(state);
}
