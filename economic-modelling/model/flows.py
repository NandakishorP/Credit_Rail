from .state import SystemState, LoanState
from .time import accrue_loan_interest
import math

def allocate_capital(system: SystemState, amount: float, origination_fee: float = 0.0):
    """
    Allocates capital from tranches to fund a loan, following the 80/20 rule 
    with detailed absorption logic from TranchePool.sol.
    """
    total_disbursement = amount - origination_fee
    total_amount = amount 
    
    # 1. Target Amounts
    target_senior = total_amount * system.capital_allocation_factor_senior
    target_junior = total_amount * system.capital_allocation_factor_junior
    target_equity = total_amount - target_senior - target_junior
    
    # 2. Initial Allocation (capped by idle)
    senior_amt = min(target_senior, system.senior.idle)
    junior_amt = min(target_junior, system.junior.idle)
    equity_amt = min(target_equity, system.equity.idle)
    
    allocated = senior_amt + junior_amt + equity_amt
    remaining = total_amount - allocated
    
    if remaining > 0 and system.equity.idle > equity_amt:
        extra = min(remaining, system.equity.idle - equity_amt)
        equity_amt += extra
        remaining -= extra
        
    # Junior absorbs next
    if remaining > 0 and system.junior.idle > junior_amt:
        extra = min(remaining, system.junior.idle - junior_amt)
        junior_amt += extra
        remaining -= extra
        
    # Senior absorbs last
    if remaining > 0 and system.senior.idle > senior_amt:
        extra = min(remaining, system.senior.idle - senior_amt)
        senior_amt += extra
        remaining -= extra
        
    if remaining > 1e-9: # Float precision check
        raise ValueError(f"Insufficient Liquidity: Missing {remaining}")
        
    # 4. Update State
    system.senior.idle -= senior_amt
    system.senior.deployed += senior_amt
    
    system.junior.idle -= junior_amt
    system.junior.deployed += junior_amt
    
    system.equity.idle -= equity_amt
    system.equity.deployed += equity_amt
    
    if origination_fee > 0:
        pass
        
    return {
        "senior_allocated": senior_amt,
        "junior_allocated": junior_amt,
        "equity_allocated": equity_amt
    }

def on_interest_accrued(system: SystemState, interest_amount: float, senior_principal: float, junior_principal: float, total_principal: float):
    """
    Splits accrued interest into tranche buckets based on principal allocation.
    """
    if interest_amount <= 0 or total_principal <= 0:
        return

    senior_interest = (interest_amount * senior_principal) / total_principal
    junior_interest = (interest_amount * junior_principal) / total_principal
    equity_interest = interest_amount - senior_interest - junior_interest
    
    system.senior_accrued_interest += senior_interest
    system.junior_accrued_interest += junior_interest
    system.equity_accrued_interest += equity_interest

def repay_loan(system: SystemState, loan: LoanState, amount: float, current_timestamp: int):
    """
    Handles loan repayment.
    1. Accrue interest up to now.
    2. Split payment into Interest and Principal.
    3. Apply Interest Waterfall.
    4. Apply Principal Waterfall.
    """
    new_interest = accrue_loan_interest(loan, current_timestamp)
    if new_interest > 0:
        loan.interest_accrued += new_interest
        on_interest_accrued(system, new_interest, loan.senior_principal_allocated, loan.junior_principal_allocated, loan.principal_issued)
        loan.last_accrual_timestamp = current_timestamp

    total_payment = amount
    interest_due = loan.interest_accrued
    interest_paid = min(total_payment, interest_due)
    
    remaining_for_principal = total_payment - interest_paid
    principal_due = loan.principal_outstanding
    principal_paid = min(remaining_for_principal, principal_due)
    
    loan.interest_accrued -= interest_paid
    loan.interest_paid += interest_paid
    loan.principal_outstanding -= principal_paid
    
    if loan.principal_outstanding <= 1e-9 and loan.interest_accrued <= 1e-9:
        loan.state = "REPAID"
        loan.repaid = True
        loan.active = False
        
    apply_interest_waterfall(system, interest_paid)
    
    apply_principal_repayment(system, principal_paid)
    
    return {
        "interest_paid": interest_paid,
        "principal_paid": principal_paid,
        "remaining": total_payment - interest_paid - principal_paid # Should be 0 usually
    }

def apply_interest_waterfall(system: SystemState, interest_paid: float):
    remaining = interest_paid
    system.total_unclaimed_interest += interest_paid
    
    # Senior
    if remaining > 0 and system.senior_accrued_interest > 0:
        senior_pay = min(remaining, system.senior_accrued_interest)
        system.senior_accrued_interest -= senior_pay
        remaining -= senior_pay
        
    # Junior
    if remaining > 0 and system.junior_accrued_interest > 0:
        junior_pay = min(remaining, system.junior_accrued_interest)
        system.junior_accrued_interest -= junior_pay
        remaining -= junior_pay
        
    # Equity / Overflow
    if remaining > 0:
        # Simplification: Assume equity exists
        # In contracts: Add to equity index -> equityAccruedInterest reduction is optimization (min check)
        # We need to reduce the accrued interest tracking for equity as well
        if system.equity_accrued_interest > 0:
             equity_pay = min(remaining, system.equity_accrued_interest)
             system.equity_accrued_interest -= equity_pay
             remaining -= equity_pay # Remaining is now truly "overflow" (protocol revenue) if any
        
        if remaining > 0:
            system.protocol_revenue += remaining

def apply_principal_repayment(system: SystemState, principal_paid: float):
    remaining = principal_paid
    
    # Senior (Restore deployed to idle)
    if remaining > 0 and system.senior.deployed > 0:
        senior_pay = min(remaining, system.senior.deployed)
        system.senior.deployed -= senior_pay
        system.senior.idle += senior_pay
        remaining -= senior_pay
        
    # Junior
    if remaining > 0 and system.junior.deployed > 0:
        junior_pay = min(remaining, system.junior.deployed)
        system.junior.deployed -= junior_pay
        system.junior.idle += junior_pay
        remaining -= junior_pay
        
    # Equity
    if remaining > 0 and system.equity.deployed > 0:
        equity_pay = min(remaining, system.equity.deployed)
        system.equity.deployed -= equity_pay
        system.equity.idle += equity_pay
        remaining -= equity_pay

def apply_loss(system: SystemState, principal_loss: float, interest_accrued_loss: float):
    """
    Handles default/write-off.
    1. Cancel ghost interest (Senior -> Junior).
    2. Principal loss absorption (Equity -> Junior -> Senior).
    """
    # 1. Cancel Ghost Interest
    remaining_interest = interest_accrued_loss
    
    if remaining_interest > 0 and system.senior_accrued_interest > 0:
        senior_cancel = min(remaining_interest, system.senior_accrued_interest)
        system.senior_accrued_interest -= senior_cancel
        remaining_interest -= senior_cancel
        
    if remaining_interest > 0 and system.junior_accrued_interest > 0:
        junior_cancel = min(remaining_interest, system.junior_accrued_interest)
        system.junior_accrued_interest -= junior_cancel
        remaining_interest -= junior_cancel
        
    # 2. Principal Loss Waterfall
    system.total_loss += principal_loss
    remaining = principal_loss
    
    # Equity absorbs first
    if remaining > 0 and system.equity.deployed > 0:
        equity_loss = min(remaining, system.equity.deployed)
        system.equity.deployed -= equity_loss
        system.equity_principal_shortfall += equity_loss
        remaining -= equity_loss
        
    # Junior next
    if remaining > 0 and system.junior.deployed > 0:
        junior_loss = min(remaining, system.junior.deployed)
        system.junior.deployed -= junior_loss
        system.junior_principal_shortfall += junior_loss
        remaining -= junior_loss
        
    # Senior last
    if remaining > 0 and system.senior.deployed > 0:
        senior_loss = min(remaining, system.senior.deployed)
        system.senior.deployed -= senior_loss
        system.senior_principal_shortfall += senior_loss
        remaining -= senior_loss
        
    if remaining > 1e-9:
        raise ValueError(f"Loss exceeded capital: {remaining}")

def on_recovery(system: SystemState, amount: float):
    """
    Reverse of loss waterfall.
    Senior -> Junior -> Equity
    """
    system.total_recovered += amount
    remaining = amount
    
    # Senior
    if remaining > 0 and system.senior_principal_shortfall > 0:
        senior_pay = min(remaining, system.senior_principal_shortfall)
        system.senior_principal_shortfall -= senior_pay
        system.senior.idle += senior_pay
        remaining -= senior_pay
        
    # Junior
    if remaining > 0 and system.junior_principal_shortfall > 0:
        junior_pay = min(remaining, system.junior_principal_shortfall)
        system.junior_principal_shortfall -= junior_pay
        system.junior.idle += junior_pay
        remaining -= junior_pay
        
    # Equity
    if remaining > 0 and system.equity_principal_shortfall > 0:
        equity_pay = min(remaining, system.equity_principal_shortfall)
        system.equity_principal_shortfall -= equity_pay
        system.equity.idle += equity_pay
        remaining -= equity_pay
        
    # Excess (Upside) -> Equity
    if remaining > 0:
        system.equity.idle += remaining

    
    
    