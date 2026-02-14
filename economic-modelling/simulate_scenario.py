import sys
import os
from decimal import Decimal, getcontext
import random
import statistics
import csv
import math
from model.state import total_value
from model.flows import on_recovery
# Set precision to 28 digits
getcontext().prec = 28

# Add the current directory to sys.path so we can import model
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model.state import SystemState, TrancheState, LoanState
from model.flows import allocate_capital, repay_loan, apply_loss


def simulate_portfolio(n_loans, default_rate, recovery_rate, 
                       total_capital=Decimal("1000000"),
                       allocation=(Decimal("0.80"), Decimal("0.15"), Decimal("0.05")),
                       yields=(Decimal("500"), Decimal("800")),
                       borrower_apr=Decimal("0.12")):
    # print("\n--- Portfolio Simulation ---") # Reduce noise

    senior_cap = total_capital * allocation[0]
    junior_cap = total_capital * allocation[1]
    equity_cap = total_capital * allocation[2]

    start_senior_apr = yields[0]
    start_junior_apr = yields[1]

    system = SystemState(
        senior=TrancheState(idle=senior_cap, deployed=Decimal("0"), apr_bps=start_senior_apr),
        junior=TrancheState(idle=junior_cap, deployed=Decimal("0"), apr_bps=start_junior_apr),
        equity=TrancheState(idle=equity_cap, deployed=Decimal("0"), apr_bps=Decimal("0"))
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

    # Calculate average loan size based on Capital Scale
    # Private Credit Logic:
    # - Small Fund (£10M): Loans might be £250k - £500k (SME)
    # - Mid Fund (£100M): Loans might be £1M - £5M (Mid-Market)
    # - Large Fund (£500M+): Loans might be £10M - £50M (Calculated Logic)
    
    avg_loan_size = total_capital / Decimal(n_loans) 
    min_loan = avg_loan_size * Decimal("0.5")
    max_loan = avg_loan_size * Decimal("1.5")

    # Deploy all loans at T=0
    for i in range(n_loans):
        loan_amount = Decimal(str(random.randint(int(min_loan), int(max_loan))))
        
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
            apr=borrower_apr,
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

    # Calculate Returns
    senior_return = (final_s - initial_s) / initial_s
    junior_return = (final_j - initial_j) / initial_j
    equity_return = (final_e - initial_e) / initial_e

    # Capital conservation invariant
    manual_total = (
        system.senior.idle + system.senior.deployed +
        system.junior.idle + system.junior.deployed +
        system.equity.idle + system.equity.deployed +
        system.senior_unclaimed_interest +
        system.junior_unclaimed_interest +
        system.equity_unclaimed_interest
    )
    assert abs(total_value(system) - manual_total) < Decimal("1e-6"), f"Invariant failed: {total_value(system)} != {manual_total}"

    return {
        "senior_return": float(senior_return),
        "junior_return": float(junior_return),
        "equity_return": float(equity_return),
        "total_final_value": float(total_value(system))
    }

def run_stress_grid():
    default_rates = [0.02, 0.05, 0.10] # 2% (Safe), 5% (Stressed), 10% (Crisis)
    recovery_rates = [0.4] # Assume standard distressed recovery
    
    # Private Credit Fund Profiles
    scenarios = [
        # 1. SME Lending (Granular, Diversified)
        # £25M AUM, ~250 Loans (Avg £100k)
        # Yields: Senior 5%, Junior 8% | Borrower: 12%
        {"name": "SME Fund (£25M)", "capital": Decimal("25000000"), "n_loans": 250, 
         "alloc": (Decimal("0.80"), Decimal("0.15"), Decimal("0.05")), "yields": (Decimal("500"), Decimal("800")), "borrower_apr": Decimal("0.12")},

        # 2. Mid-Market Direct Lending (Concentrated)
        # £100M AUM, ~40 Loans (Avg £2.5M)
        # Yields: Senior 6%, Junior 10% | Borrower: 14% (Riskier)
        {"name": "Mid-Market DL (£100M)", "capital": Decimal("100000000"), "n_loans": 40,
         "alloc": (Decimal("0.70"), Decimal("0.20"), Decimal("0.10")), "yields": (Decimal("600"), Decimal("1000")), "borrower_apr": Decimal("0.14")},
         
        # 3. Special Situations / Distressed (High Risk/Return)
        # £50M AUM, ~20 Loans (Avg £2.5M)
        # Yields: Senior 8%, Junior 15% | Borrower: 20%
        # High Default expected, but compensated by yield.
        {"name": "Spec Sit Fund (£50M)", "capital": Decimal("50000000"), "n_loans": 20,
         "alloc": (Decimal("0.60"), Decimal("0.25"), Decimal("0.15")), "yields": (Decimal("800"), Decimal("1500")), "borrower_apr": Decimal("0.20")},
    ]

    ITERATIONS = 50 
    
    results_file = "private_credit_analysis.csv"
    
    with open(results_file, 'w', newline='') as csvfile:
        fieldnames = ['scenario', 'default_rate', 'recovery_rate', 'iteration', 'senior_return', 'junior_return', 'equity_return', 'total_final_value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for sc in scenarios:
            print(f"\n=== Scenario: {sc['name']} ===")
            
            for d in default_rates:
                for r in recovery_rates:
                    print(f"  Default={d:.1%}, Recovery={r:.0%} ({ITERATIONS} runs)...", end="", flush=True)
                    
                    s_returns = []
                    j_returns = []
                    e_returns = []
                    
                    for i in range(ITERATIONS):
                        res = simulate_portfolio(sc['n_loans'], d, r, 
                                               total_capital=sc['capital'],
                                               allocation=sc['alloc'],
                                               yields=sc['yields'],
                                               borrower_apr=sc['borrower_apr'])
                        
                        row = {
                            'scenario': sc['name'],
                            'default_rate': d,
                            'recovery_rate': r,
                            'iteration': i,
                            'senior_return': res['senior_return'],
                            'junior_return': res['junior_return'],
                            'equity_return': res['equity_return'],
                            'total_final_value': res['total_final_value']
                        }
                        writer.writerow(row)
                        
                        s_returns.append(res['senior_return'])
                        j_returns.append(res['junior_return'])
                        e_returns.append(res['equity_return'])

                    print(" Done.")
                    avg_j = statistics.mean(j_returns)
                    avg_e = statistics.mean(e_returns)
                    std_j = statistics.stdev(j_returns)
                    std_e = statistics.stdev(e_returns)
                    print(f"    Junior: {avg_j*100:.2f}% (±{std_j*100:.2f}%) | Equity: {avg_e*100:.2f}% (±{std_e*100:.2f}%)")
                
                # Calculate Stats
                avg_s = statistics.mean(s_returns)
                avg_j = statistics.mean(j_returns)
                avg_e = statistics.mean(e_returns)
                
                std_s = statistics.stdev(s_returns) if len(s_returns) > 1 else 0
                std_j = statistics.stdev(j_returns) if len(j_returns) > 1 else 0
                std_e = statistics.stdev(e_returns) if len(e_returns) > 1 else 0
                
                print(f"Results for Default={d:.1%}, Recovery={r:.0%}:")
                print(f"  Senior: Mean={avg_s*100:.2f}% (Std={std_s*100:.2f}%)")
                print(f"  Junior: Mean={avg_j*100:.2f}% (Std={std_j*100:.2f}%)")
                print(f"  Equity: Mean={avg_e*100:.2f}% (Std={std_e*100:.2f}%)")

if __name__ == "__main__":
    run_stress_grid()
