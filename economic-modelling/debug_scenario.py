import sys
import os
from decimal import Decimal, getcontext
import random

# Set precision
getcontext().prec = 28

# Add path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model.state import SystemState, TrancheState, LoanState, total_value
from model.flows import allocate_capital, repay_loan, apply_loss, on_recovery

def log_interest(step_name, system):
    print(f"\n[{step_name}] Interest Distribution")
    print(f"  Senior Accrued: {system.senior_accrued_interest:.2f} | Unclaimed: {system.senior_unclaimed_interest:.2f}")
    print(f"  Junior Accrued: {system.junior_accrued_interest:.2f} | Unclaimed: {system.junior_unclaimed_interest:.2f}")
    print(f"  Equity Accrued: {system.equity_accrued_interest:.2f} | Unclaimed: {system.equity_unclaimed_interest:.2f}")

def run_debug():
    print("=== DEBUG SCENARIO: WATERFALL PRIORITY ===")
    
    # Initialize System 
    # Senior needs lots of interest so we can starve Junior/Equity to prove priority
    system = SystemState(
        senior=TrancheState(idle=Decimal("800000"), deployed=Decimal("0"), apr_bps=Decimal("500")),
        junior=TrancheState(idle=Decimal("150000"), deployed=Decimal("0"), apr_bps=Decimal("800")),
        equity=TrancheState(idle=Decimal("50000"), deployed=Decimal("0"), apr_bps=Decimal("0"))
    )
    
    # Create Loan
    loan_amount = Decimal("10000")
    allocation = allocate_capital(system, loan_amount)
    
    loan = LoanState(
        loan_id=1,
        principal_issued=loan_amount,
        principal_outstanding=loan_amount,
        interest_accrued=Decimal("0"),
        interest_paid=Decimal("0"),
        senior_principal_allocated=allocation["senior_allocated"],
        junior_principal_allocated=allocation["junior_allocated"],
        active=True,
        defaulted=False,
        repaid=False,
        written_off=False,
        apr=Decimal("0.12"),
        term_days=365,
        start_timestamp=0,
        last_accrual_timestamp=0
    )
    system.loans.append(loan)
    
    # --- SCENARIO 1: PARTIAL INTEREST PAYMENT ---
    # Accrue interest for 1 year
    # Interest Due = 1200
    # Senior Claim = 8000 * 5% = 400
    # Junior Claim = 1500 * 8% = 120
    # Equity Claim = Remainder = 680
    
    # Suppose we pay ONLY 300 interest (less than Senior's claim).
    # Expected: Senior gets 300. Junior gets 0. Equity gets 0.
    
    print("\n--- Test 1: Insufficient Interest (300) ---")
    repay_loan(system, loan, Decimal("300"), 365 * 24 * 3600)
    
    log_interest("AFTER PARTIAL PAYMENT", system)
    
    if system.senior_unclaimed_interest == Decimal("300") and system.junior_unclaimed_interest == Decimal("0") and system.equity_unclaimed_interest == Decimal("0"):
        print("PASS: Senior took all available interest. Priority respected.")
    else:
        print("FAIL: Priority Violation!")

    # --- SCENARIO 2: EXCESS INTEREST PAYMENT ---
    # Suppose we pay remaining 900 interest (Total 1200).
    # Remaining Senior Claim = 100.
    # Junior Claim = 120.
    # Equity Claim = 680.
    
    print("\n--- Test 2: Full Interest Payment (900 more) ---")
    # Reset unclaimed for clarity
    system.senior_unclaimed_interest = Decimal("0")
    system.junior_unclaimed_interest = Decimal("0")
    system.equity_unclaimed_interest = Decimal("0")
    
    # Accrued balances are updated by repay_loan logic internally based on time elapsed?
    # Actually, repay_loan calls accrue_loan_interest -> on_interest_accrued.
    # on_interest_accrued fills the buckets based on time elapsed since last check.
    # Since we already ran repay_loan with full 1 year elapsed, the buckets are full!
    # They just haven't been drained because we only paid 300.
    
    # Check buckets before payment
    print(f"Buckets before 2nd payment: S={system.senior_accrued_interest} J={system.junior_accrued_interest}")
    
    # Pay 900 interest
    repay_loan(system, loan, Decimal("900"), 365 * 24 * 3600) # stats don't change, just payout
    
    log_interest("AFTER REMAINDER PAYMENT", system)
    
    # Recovered stats
    # Senior should have taken 100 more (Total 400).
    # Junior should have taken 120.
    # Equity should have taken rest (680).
    
    if system.senior_unclaimed_interest == Decimal("100") and system.junior_unclaimed_interest == Decimal("120"):
         print("PASS: Waterfall filled Senior -> Junior -> Equity correctly.")
    else:
         print(f"FAIL: Distribution incorrect. S={system.senior_unclaimed_interest} J={system.junior_unclaimed_interest}")

if __name__ == "__main__":
    run_debug()
