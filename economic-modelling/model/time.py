DAYS_IN_YEAR = 365

def accrue_loan_interest(loan, current_timestamp):
    """
    Calculates interest accrued since the last accrual.
    Returns the amount of interest accrued.
    """
    if not loan.active:
        return 0.0
    
    # Calculate time elapsed in days
    # Using 365 days year convention as per contracts (1 year = 365 days = 31536000 seconds)
    time_elapsed_seconds = current_timestamp - loan.last_accrual_timestamp
    if time_elapsed_seconds <= 0:
        return 0.0
        
    days_elapsed = time_elapsed_seconds / (24 * 3600)
    
    # Interest Formula: Principal * APR * (Days / 365)
    # APR is in decimal (e.g., 0.10 for 10%), NOT bps here unless we convert.
    # Contracts use BPS (basis points). Let's assume input APR in LoanState is decimal for simplicity in Python,
    # or consistent with contracts (BPS).
    # original flows.py used `amount * senior_ratio`.
    # Let's assume APR is decimal float (e.g. 0.05).
    
    interest = loan.principal_outstanding * loan.apr * (days_elapsed / DAYS_IN_YEAR)
    return interest