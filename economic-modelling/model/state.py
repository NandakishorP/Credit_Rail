from dataclasses import dataclass, field
from typing import List

@dataclass
class TrancheState:
    idle: float
    deployed: float

@dataclass
class LoanState:
    loan_id: int
    principal_issued: float
    principal_outstanding: float
    
    # Interest
    interest_accrued: float
    interest_paid: float
    
    # Allocation (Tracking which tranche funded this loan)
    senior_principal_allocated: float
    junior_principal_allocated: float
    
    # Lifecycle
    active: bool
    defaulted: bool
    repaid: bool
    written_off: bool
    
    # Parameters
    apr: float
    term_days: int
    start_timestamp: int
    last_accrual_timestamp: int
    
    total_recovered: float = 0.0

@dataclass
class SystemState:
    senior: TrancheState
    junior: TrancheState
    equity: TrancheState
    
    # Global Stats
    total_loss: float = 0.0
    total_recovered: float = 0.0
    total_unclaimed_interest: float = 0.0
    protocol_revenue: float = 0.0
    
    # Tranche Interest Buckets (Waterfalls)
    senior_accrued_interest: float = 0.0
    junior_accrued_interest: float = 0.0
    equity_accrued_interest: float = 0.0
    
    # Principal Shortfalls (for recovery targeting)
    senior_principal_shortfall: float = 0.0
    junior_principal_shortfall: float = 0.0
    equity_principal_shortfall: float = 0.0

    # Configuration (Capital Allocation Factors)
    capital_allocation_factor_senior: float = 0.80
    capital_allocation_factor_junior: float = 0.15
    # Equity is the remainder (0.05)

    loans: List[LoanState] = field(default_factory=list)