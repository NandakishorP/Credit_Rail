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