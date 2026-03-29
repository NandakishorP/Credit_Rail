use crate::interest::accrue_target_interest;
use crate::types::*;

/// Mirrors _accrueTrancheTargets() — called at the start of EVERY operation.
/// Updates target_interest for senior/junior based on elapsed time.
pub fn accrue_tranche_targets(state: &mut State) {
    let elapsed = (state.now - state.last_tranche_accrual_ts).num_seconds();
    if elapsed <= 0 {
        return;
    }

    for tranche in state.tranches.iter_mut() {
        if tranche.apr_bps > 0 {
            tranche.target_interest +=
                accrue_target_interest(tranche.deployed, tranche.apr_bps, elapsed);
        }
    }

    state.last_tranche_accrual_ts = state.now;
}

/// Mirrors allocateCapital() — move idle → deployed per allocation ratio.
pub fn allocate_capital(state: &mut State, principal: i64) {
    accrue_tranche_targets(state);

    let alloc_pcts = [SENIOR_ALLOC_PCT, JUNIOR_ALLOC_PCT, EQUITY_ALLOC_PCT];

    state.pool.idle -= principal;
    state.pool.deployed += principal;

    for (tranche, pct) in state.tranches.iter_mut().zip(alloc_pcts.iter()) {
        let allocate = principal * pct / 100;
        tranche.idle -= allocate;
        tranche.deployed += allocate;
    }
}

/// Mirrors onInterestAccrued() — waterfall loan interest into tranche accrued_interest.
/// Senior fills up to (target - accrued), then Junior, then Equity gets residual.
pub fn on_interest_accrued(state: &mut State, interest_amount: i64) {
    if interest_amount == 0 {
        return;
    }

    accrue_tranche_targets(state);

    let mut remaining = interest_amount;

    // Senior: capped at target - accrued
    let senior = &mut state.tranches[SENIOR];
    let senior_owed = (senior.target_interest - senior.accrued_interest).max(0);
    let senior_credited = remaining.min(senior_owed);
    senior.accrued_interest += senior_credited;
    remaining -= senior_credited;

    // Junior: capped at target - accrued
    let junior = &mut state.tranches[JUNIOR];
    let junior_owed = (junior.target_interest - junior.accrued_interest).max(0);
    let junior_credited = remaining.min(junior_owed);
    junior.accrued_interest += junior_credited;
    remaining -= junior_credited;

    // Equity: gets residual
    if remaining > 0 {
        state.tranches[EQUITY].accrued_interest += remaining;
    }
}

/// Mirrors onRepayment() — pay out interest from accrued, deduct accrued & target,
/// then redeem principal (deployed → idle) in seniority order.
pub fn on_repayment(state: &mut State, principal_repaid: i64, interest_repaid: i64) {
    if principal_repaid == 0 && interest_repaid == 0 {
        return;
    }

    accrue_tranche_targets(state);

    // ── Interest waterfall: pay from accrued_interest ──
    let mut remaining_interest = interest_repaid;

    // Senior
    let senior = &mut state.tranches[SENIOR];
    let senior_pay = remaining_interest.min(senior.accrued_interest);
    if senior_pay > 0 {
        senior.accrued_interest -= senior_pay;
        senior.target_interest -= senior.target_interest.min(senior_pay);
        senior.paid_interest += senior_pay;
        remaining_interest -= senior_pay;
    }

    // Junior
    let junior = &mut state.tranches[JUNIOR];
    let junior_pay = remaining_interest.min(junior.accrued_interest);
    if junior_pay > 0 {
        junior.accrued_interest -= junior_pay;
        junior.target_interest -= junior.target_interest.min(junior_pay);
        junior.paid_interest += junior_pay;
        remaining_interest -= junior_pay;
    }

    // Equity: receives residual
    if remaining_interest > 0 {
        let equity = &mut state.tranches[EQUITY];
        let equity_pay = remaining_interest.min(equity.accrued_interest);
        equity.accrued_interest -= equity_pay;
        equity.paid_interest += equity_pay;
        // Any overflow beyond accrued could be protocol revenue — ignored in sim
    }

    // ── Principal redemption: deployed → idle, senior first ──
    state.pool.idle += principal_repaid;
    state.pool.deployed -= principal_repaid;

    let mut remaining_principal = principal_repaid;
    for tranche in state.tranches.iter_mut() {
        let redeem = remaining_principal.min(tranche.deployed);
        tranche.deployed -= redeem;
        tranche.idle += redeem;
        remaining_principal -= redeem;
        if remaining_principal == 0 {
            break;
        }
    }
}

/// Mirrors onLoss() — cancel ghost interest, then absorb principal loss equity-first.
/// Called by writeOff after loan principal/interest are zeroed.
pub fn on_loss(state: &mut State, principal_loss: i64, interest_loss: i64) {
    accrue_tranche_targets(state);

    // ── Phase 1: Cancel ghost interest (senior → junior) ──
    let mut remaining_interest = interest_loss;

    // Senior: cancel accrued interest that will never be paid
    let senior = &mut state.tranches[SENIOR];
    let senior_cancel = remaining_interest.min(senior.accrued_interest);
    if senior_cancel > 0 {
        senior.accrued_interest -= senior_cancel;
        senior.target_interest -= senior.target_interest.min(senior_cancel);
        remaining_interest -= senior_cancel;
    }

    // Junior
    let junior = &mut state.tranches[JUNIOR];
    let junior_cancel = remaining_interest.min(junior.accrued_interest);
    if junior_cancel > 0 {
        junior.accrued_interest -= junior_cancel;
        junior.target_interest -= junior.target_interest.min(junior_cancel);
        remaining_interest -= junior_cancel;
    }

    // Equity: cancel whatever accrued
    if remaining_interest > 0 {
        let equity = &mut state.tranches[EQUITY];
        let equity_cancel = remaining_interest.min(equity.accrued_interest);
        equity.accrued_interest -= equity_cancel;
    }

    // ── Phase 2: Principal loss absorption (equity → junior → senior) ──
    state.pool.deployed -= principal_loss;
    state.pool.shortfall += principal_loss;
    state.pool.total_loss += principal_loss;

    let mut remaining_loss = principal_loss;
    for tranche in state.tranches.iter_mut().rev() {
        let absorb = remaining_loss.min(tranche.deployed);
        tranche.deployed -= absorb;
        tranche.shortfall += absorb;
        remaining_loss -= absorb;
        if remaining_loss == 0 {
            break;
        }
    }
}

/// Mirrors onRecovery() — restore shortfall senior-first, add to idle.
pub fn on_recovery(state: &mut State, amount: i64) {
    accrue_tranche_targets(state);

    state.pool.idle += amount;
    state.pool.shortfall -= amount.min(state.pool.shortfall);
    state.pool.total_recovered += amount;

    let mut remaining = amount;
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
