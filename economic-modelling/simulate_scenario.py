import sys
import os
from decimal import Decimal, getcontext
import random
from model.state import total_value
from model.flows import on_recovery
# Set precision to 28 digits
getcontext().prec = 28

# Add the current directory to sys.path so we can import model
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model.state import SystemState, TrancheState, LoanState
from model.flows import allocate_capital, repay_loan, apply_loss

def test_happy_path():
    print("--- Test Happy Path ---")
    # 1. Initialize System
    system = SystemState(
        senior=TrancheState(idle=Decimal("80000.0"), deployed=Decimal("0.0"), apr_bps=Decimal("500")),
        junior=TrancheState(idle=Decimal("15000.0"), deployed=Decimal("0.0"), apr_bps=Decimal("800")),
        equity=TrancheState(idle=Decimal("5000.0"), deployed=Decimal("0.0"), apr_bps=Decimal("0"))
    )
    
    print(f"Initial System Idle: S={system.senior.idle}, J={system.junior.idle}, E={system.equity.idle}")

    # 2. Allocate Capital
    loan_amount = Decimal("10000.0")
    allocation = allocate_capital(system, loan_amount)
    print(f"Allocation: {allocation}")
    
    # Verify Allocation
    assert allocation['senior_allocated'] == Decimal("8000.0")
    assert allocation['junior_allocated'] == Decimal("1500.0")
    assert allocation['equity_allocated'] == Decimal("500.0")
    
    # 3. Create Loan
    loan = LoanState(
        loan_id=1,
        principal_issued=loan_amount,
        principal_outstanding=loan_amount,
        interest_accrued=Decimal("0.0"),
        interest_paid=Decimal("0.0"),
        senior_principal_allocated=allocation['senior_allocated'],
        junior_principal_allocated=allocation['junior_allocated'],
        active=True,
        defaulted=False,
        repaid=False,
        written_off=False,
        apr=Decimal("0.10"), # 10%
        term_days=365,
        start_timestamp=0,
        last_accrual_timestamp=0
    )
    system.loans.append(loan)
    
    # 4. Advance Time & Repay
    # 6 months later (approx)
    timestamp = int(182.5 * 24 * 3600)
    
    # Accrued Interest should be approx 500
    # Payment: 5500 (500 interest, 5000 principal)
    payment_result = repay_loan(system, loan, Decimal("5500.0"), timestamp)
    print(f"Payment Result: {payment_result}")
    
    print(f"Loan Principal Outstanding: {loan.principal_outstanding}")
    print(f"System State Deployed: S={system.senior.deployed}, J={system.junior.deployed}, E={system.equity.deployed}")
    
    # Verify Interest Waterfall
    # Total Interest = 10000 * 0.1 * (182.5/365) = 500.0
    # Split: S=400, J=75, E=25
    
    # Paid: 500 (fully covers interest)
    # Remaining Payment: 5000 (Principal)
    
    # Principal Waterfall:
    # Senior deployed: 8000 -> 3000? 
    # Logic: Senior -> Junior -> Equity.
    # 5000 paid.
    # Senior deployed was 8000. 5000 < 8000.
    # Senior deployed becomes 3000.
    
    assert abs(system.senior.deployed - Decimal("3000.0")) < Decimal("1e-9")
    assert abs(system.junior.deployed - Decimal("1500.0")) < Decimal("1e-9")
    assert abs(system.equity.deployed - Decimal("500.0")) < Decimal("1e-9")
    
    # Check Accrued Interest Balances (Should be reduced by payment)
    # They should be 0 because we paid exact interest amount.
    print(f"System Accrued Interest Balances: S={system.senior_accrued_interest}, J={system.junior_accrued_interest}, E={system.equity_accrued_interest}")
    assert abs(system.senior_accrued_interest) < Decimal("1e-9")
    assert abs(system.junior_accrued_interest) < Decimal("1e-9")
    assert abs(system.equity_accrued_interest) < Decimal("1e-9")
    
    print("Happy Path Passed!")




def simulate_portfolio(n_loans, default_rate, recovery_rate):
    print("\n--- Portfolio Simulation ---")

    system = SystemState(
        senior=TrancheState(idle=Decimal("800000"), deployed=Decimal("0"), apr_bps=Decimal("500")),
        junior=TrancheState(idle=Decimal("150000"), deployed=Decimal("0"), apr_bps=Decimal("800")),
        equity=TrancheState(idle=Decimal("50000"), deployed=Decimal("0"), apr_bps=Decimal("0"))
    )

    initial_s = system.senior.idle
    initial_j = system.junior.idle
    initial_e = system.equity.idle
    initial_total = total_value(system)

    total_principal_loss = Decimal("0")
    total_interest_loss = Decimal("0")
    total_recovery = Decimal("0")
    
    sim_time = 0
    SECONDS_IN_YEAR = 365 * 24 * 3600

    # Deploy all loans at T=0
    for i in range(n_loans):
        loan_amount = Decimal(str(random.randint(2000, 8000)))  # Smaller loans to fit 100 in 1M capital
        
        # Check if we have enough liquidity
        total_idle = system.senior.idle + system.junior.idle + system.equity.idle
        if loan_amount > total_idle:
            continue  # Skip this loan if insufficient liquidity
            
        allocation = allocate_capital(system, loan_amount, sim_time)

        loan = LoanState(
            loan_id=i,
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
            start_timestamp=sim_time,
            last_accrual_timestamp=sim_time
        )

        system.loans.append(loan)

    # Fast-forward to maturity (1 year)
    sim_time = SECONDS_IN_YEAR

    # Process all loan outcomes at maturity
    for loan in system.loans:
        if random.random() < default_rate:
            loan.defaulted = True
            loan.active = False
            
            loss = loan.principal_outstanding
            # Immediate loss recognition
            apply_loss(system, loss, Decimal("0"), sim_time)
            
            total_principal_loss += loss 
            total_recovery += loss * Decimal(str(recovery_rate))

        else:
            full_payment = loan.principal_outstanding * (Decimal("1") + loan.apr)
            repay_loan(system, loan, full_payment, sim_time)

    # -------------------------------------------------
    # RECOVERY (Still deferred/batch)
    # -------------------------------------------------

    if total_recovery > 0:
        on_recovery(system, total_recovery, sim_time)

    # -------------------------------------------------

    final_s = system.senior.idle + system.senior.deployed + system.senior_unclaimed_interest
    final_j = system.junior.idle + system.junior.deployed + system.junior_unclaimed_interest
    final_e = system.equity.idle + system.equity.deployed + system.equity_unclaimed_interest

    print("Final Senior:", final_s)
    print("Final Junior:", final_j)
    print("Final Equity:", final_e)

    print("Total Initial:", initial_total)
    print("Total Final:", total_value(system))
    print(f"Senior Breakdown: Idle={system.senior.idle} Deployed={system.senior.deployed} Unclaimed={system.senior_unclaimed_interest}")
    print(f"Junior Breakdown: Idle={system.junior.idle} Deployed={system.junior.deployed} Unclaimed={system.junior_unclaimed_interest}")
    print(f"Equity Breakdown: Idle={system.equity.idle} Deployed={system.equity.deployed} Unclaimed={system.equity_unclaimed_interest}")

    senior_return = (final_s - initial_s) / initial_s
    junior_return = (final_j - initial_j) / initial_j
    equity_return = (final_e - initial_e) / initial_e

    print("Senior Return:", round(float(senior_return * 100), 2), "%")
    print("Junior Return:", round(float(junior_return * 100), 2), "%")
    print("Equity Return:", round(float(equity_return * 100), 2), "%")

    # Capital conservation invariant
    # Capital conservation invariant
    # Total Value = Idle + Deployed + Unclaimed Interest
    manual_total = (
        system.senior.idle + system.senior.deployed +
        system.junior.idle + system.junior.deployed +
        system.equity.idle + system.equity.deployed +
        system.senior_unclaimed_interest +
        system.junior_unclaimed_interest +
        system.equity_unclaimed_interest
    )
    assert abs(total_value(system) - manual_total) < Decimal("1e-6"), f"Invariant failed: {total_value(system)} != {manual_total}"

def run_stress_grid():
    default_rates = [0.005, 0.01, 0.02, 0.04]
    recovery_rates = [0.5, 0.6, 0.7]

    for d in default_rates:
        for r in recovery_rates:
            print("\n==============================")
            print(f"Default Rate: {d}, Recovery Rate: {r}")
            simulate_portfolio(200, d, r)

if __name__ == "__main__":
    run_stress_grid()
