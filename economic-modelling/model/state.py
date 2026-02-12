from dataclasses import dataclass, field
from typing import List
from decimal import Decimal

@dataclass
class TrancheState:
    idle: Decimal
    deployed: Decimal
    apr_bps: Decimal

@dataclass
class LoanState:
    loan_id: int
    principal_issued: Decimal
    principal_outstanding: Decimal
    
    # Interest
    interest_accrued: Decimal
    interest_paid: Decimal
    
    # Allocation (Tracking which tranche funded this loan)
    senior_principal_allocated: Decimal
    junior_principal_allocated: Decimal
    
    # Lifecycle
    active: bool
    defaulted: bool
    repaid: bool
    written_off: bool
    
    # Parameters
    apr: Decimal
    term_days: int
    start_timestamp: int
    last_accrual_timestamp: int
    
    total_recovered: Decimal = Decimal("0.0")

@dataclass
class SystemState:
    senior: TrancheState
    junior: TrancheState
    equity: TrancheState
    
    # Global Stats
    total_loss: Decimal = Decimal("0.0")
    total_recovered: Decimal = Decimal("0.0")
    total_unclaimed_interest: Decimal = Decimal("0.0")
    protocol_revenue: Decimal = Decimal("0.0")
    
    # Tranche Interest Buckets (Waterfalls)
    senior_accrued_interest: Decimal = Decimal("0.0")
    junior_accrued_interest: Decimal = Decimal("0.0")
    equity_accrued_interest: Decimal = Decimal("0.0")

    senior_unclaimed_interest: Decimal = Decimal("0.0")
    junior_unclaimed_interest: Decimal = Decimal("0.0")
    equity_unclaimed_interest: Decimal = Decimal("0.0")
    
    # Principal Shortfalls (for recovery targeting)
    senior_principal_shortfall: Decimal = Decimal("0.0")
    junior_principal_shortfall: Decimal = Decimal("0.0")
    equity_principal_shortfall: Decimal = Decimal("0.0")

    # Configuration (Capital Allocation Factors)
    capital_allocation_factor_senior: Decimal = Decimal("0.80")
    capital_allocation_factor_junior: Decimal = Decimal("0.15")
    # Equity is the remainder (0.05)

    loans: List[LoanState] = field(default_factory=list)


def total_value(system: "SystemState") -> Decimal:
    return (
        system.senior.idle + system.senior.deployed +
        system.junior.idle + system.junior.deployed +
        system.equity.idle + system.equity.deployed +
        system.senior_unclaimed_interest +
        system.junior_unclaimed_interest +
        system.equity_unclaimed_interest
    )

def assert_conservation(before: Decimal, after: Decimal, tolerance=Decimal("0.000001")):
    if abs(before - after) > tolerance:
        raise Exception(f"Value not conserved: before={before}, after={after}")