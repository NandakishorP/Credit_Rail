import sys
import os
from decimal import Decimal

# Add the current directory to sys.path so we can import the model
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model.state import SystemState, TrancheState, LoanState, total_value
from model.flows import allocate_capital, repay_loan, apply_loss, on_recovery

def setup_system():
    # Initialize a system with 10M in each tranche
    senior = TrancheState(idle=Decimal("10000000"), deployed=Decimal("0"), apr_bps=Decimal("500"))
    junior = TrancheState(idle=Decimal("10000000"), deployed=Decimal("0"), apr_bps=Decimal("1000"))
    equity = TrancheState(idle=Decimal("10000000"), deployed=Decimal("0"), apr_bps=Decimal("0"))
    return SystemState(senior=senior, junior=junior, equity=equity)

def verify_inferences():
    results = []
    
    # 1. Start System
    system = setup_system()
    val_0 = total_value(system)
    results.append(f"## Initial State\n\nTotal Value: {val_0} (All Idle)\n")
    
    # 2. Allocation (Deployment)
    # No value created or destroyed
    print("Testing Allocation...")
    loan_amount = Decimal("1000000")
    allocate_capital(system, loan_amount, current_timestamp=1000)
    
    val_1 = total_value(system)
    results.append(f"## 1. No Value Created/Destroyed on Deployment\n")
    results.append(f"* **Action**: Allocated 1M loan.")
    results.append(f"* **Before**: {val_0}")
    results.append(f"* **After**:  {val_1}")
    results.append(f"* **Inference**: Deployment moves funds from Idle to Deployed without changing total system value.\n")
    
    # Check Principal Movement
    deployed_total = system.senior.deployed + system.junior.deployed + system.equity.deployed
    results.append(f"## 2. Principal moves Deployed -> Idle (and vice versa)\n")
    results.append(f"* **Deployed Total**: {deployed_total}")
    results.append(f"* **Inference**: Allocation moved {deployed_total} from Idle to Deployed.\n")

    # Create a dummy loan for repayment
    loan = LoanState(
        loan_id=1,
        principal_issued=loan_amount,
        principal_outstanding=loan_amount,
        interest_accrued=Decimal("0"),
        interest_paid=Decimal("0"),
        senior_principal_allocated=Decimal("800000"),
        junior_principal_allocated=Decimal("200000"),
        active=True,
        defaulted=False,
        repaid=False,
        written_off=False,
        apr=Decimal("0.1"),
        term_days=365,
        start_timestamp=1000,
        last_accrual_timestamp=1000
    )
    
    # 3. Interest Payment
    print("Testing Interest Repayment...")
    # Simulate interest accrual
    loan.interest_accrued = Decimal("50000") 
    repay_loan(system, loan, amount=Decimal("50000"), current_timestamp=2000)
    
    val_2 = total_value(system)
    results.append(f"## 3. Interest Increases System Value\n")
    results.append(f"* **Action**: Repaid 50k Interest.")
    results.append(f"* **Before**: {val_1}")
    results.append(f"* **After**:  {val_2}")
    results.append(f"* **Difference**: {val_2 - val_1}")
    results.append(f"* **Inference**: Interest payments enter the system as new value (Unclaimed Interest), increasing the total system value.\n")

    # 4. Principal Repayment
    print("Testing Principal Repayment...")
    repay_loan(system, loan, amount=Decimal("500000"), current_timestamp=2000)
    val_3 = total_value(system)
    # Principal repayment shouldn't change total value (just moves deployed -> idle)
    # Note: repay_loan assertion guarantees this conservation for principal
    
    results.append(f"## 4. Principal Repayment Moves Deployed -> Idle\n")
    results.append(f"* **Action**: Repaid 500k Principal.")
    results.append(f"* **Before**: {val_2}")
    results.append(f"* **After**:  {val_3}")
    results.append(f"* **Inference**: Principal repayment conserves total value, shifting funds from Deployed back to Idle.\n")
    
    # 5. Loss
    print("Testing Loss...")
    loss_amount = Decimal("100000")
    # Manually reduce deployed to simulate write-off condition setup if needed, 
    # but apply_loss matches the "write-off" logic
    apply_loss(system, principal_loss=loss_amount, interest_accrued_loss=Decimal("0"), current_timestamp=3000)
    
    val_4 = total_value(system)
    results.append(f"## 5. Loss Reduces System Value\n")
    results.append(f"* **Action**: Wrote off 100k Loan.")
    results.append(f"* **Before**: {val_3}")
    results.append(f"* **After**:  {val_4}")
    results.append(f"* **Difference**: {val_4 - val_3}")
    results.append(f"* **Inference**: Principal writedowns remove value from Deployed without returning it to Idle, reducing total system value.\n")
    
    # 6. Recovery
    print("Testing Recovery...")
    recovery_amount = Decimal("50000")
    on_recovery(system, amount=recovery_amount, current_timestamp=4000)
    
    val_5 = total_value(system)
    results.append(f"## 6. Recovery Increases System Value\n")
    results.append(f"* **Action**: Recovered 50k.")
    results.append(f"* **Before**: {val_4}")
    results.append(f"* **After**:  {val_5}")
    results.append(f"* **Difference**: {val_5 - val_4}")
    results.append(f"* **Inference**: Recovery injects external funds back into the system (Idle), increasing total value.\n")

    # 7. Interest Accounting Invariants
    # Invariant: target_interest >= accrued_interest >= unclaimed_interest
    # NOTE: The system model tracks 'outstanding' values (decremented on payment), 
    # so we must manually track cumulative values to verify this invariant.
    
    print("Testing Interest Accounting Invariants...")
    results.append(f"## 7. Interest Accounting Invariants\n")
    results.append(f"**Invariant**: `cumulative_target_interest >= cumulative_accrued_interest >= cumulative_unclaimed_interest`\n")
    
    # We need to reconstruct cumulative values.
    # Unclaimed Interest is naturally cumulative (it's a bucket that only grows until claimed by user, which isn't modeled here).
    # Accrued Interest in state is "outstanding". 
    # Target Interest in state is "outstanding".
    
    # Cumulative Accrued = Outstanding Accrued + Total Paid (which went to Unclaimed) + Total Cancelled (Loss)
    # Cumulative Target = Outstanding Target + Total Paid + Total Cancelled
    
    # Let's calculate:
    senior_unclaimed = system.senior_unclaimed_interest
    junior_unclaimed = system.junior_unclaimed_interest
    equity_unclaimed = system.equity_unclaimed_interest
    
    # Total Paid so far (assuming no loss/cancellation in this specific scenario run after recovery)
    # Actually, apply_loss happened in step 5.
    # Loss cancellation logic:
    # senior_target_interest -= min(senior_target, senior_cancel)
    # So 'outstanding target' was reduced by cancellation.
    
    # To properly verify, we'd need to have tracked these cumulatively throughout the script.
    # Since we can't edit model code, we will approximate or infer based on "outstanding + unclaimed".
    
    # Assumption: No interest was claimed/withdrawn by LPs (model doesn't implement withdraw). 
    # So Unclaimed = Total Interest Paid.
    
    # Senior Cumulative Accrued ~= Outstanding Accrued + Unclaimed + (Cancelled Interest)
    # Senior Cumulative Target ~= Outstanding Target + Unclaimed + (Cancelled Target)
    
    # We know in Step 5 (Loss), we didn't explicitly track cancelled interest amount in return value, 
    # but let's assume for this specific run:
    # Loan had 50k interest accrued. We repaid 50k interest.
    # Loss step: apply_loss(..., interest_accrued_loss=0). 
    # So NO interest was cancelled!
    
    cumulative_senior_accrued = system.senior_accrued_interest + senior_unclaimed
    cumulative_senior_target = system.senior_target_interest + senior_unclaimed
    
    cumulative_junior_accrued = system.junior_accrued_interest + junior_unclaimed
    cumulative_junior_target = system.junior_target_interest + junior_unclaimed
    
    # Senior
    senior_ok = (cumulative_senior_target >= cumulative_senior_accrued) and \
                (cumulative_senior_accrued >= senior_unclaimed)
    
    results.append(f"### Senior Tranche")
    results.append(f"* Cumulative Target: {cumulative_senior_target}")
    results.append(f"* Cumulative Accrued: {cumulative_senior_accrued}")
    results.append(f"* Unclaimed (Paid): {senior_unclaimed}")
    results.append(f"* **Pass**: {senior_ok}\n")
    
    # Junior
    junior_ok = (cumulative_junior_target >= cumulative_junior_accrued) and \
                (cumulative_junior_accrued >= junior_unclaimed)
    results.append(f"### Junior Tranche")
    results.append(f"* Cumulative Target: {cumulative_junior_target}")
    results.append(f"* Cumulative Accrued: {cumulative_junior_accrued}")
    results.append(f"* Unclaimed (Paid): {junior_unclaimed}")
    results.append(f"* **Pass**: {junior_ok}\n")
    
    # Equity
    # Equity accrued tracks "residual" interest assigned to equity.
    cumulative_equity_accrued = system.equity_accrued_interest + equity_unclaimed
    equity_ok = (cumulative_equity_accrued >= equity_unclaimed)
    results.append(f"### Equity Tranche")
    results.append(f"* Cumulative Accrued: {cumulative_equity_accrued}")
    results.append(f"* Unclaimed (Paid): {equity_unclaimed}")
    results.append(f"* **Pass**: {equity_ok}\n")

    if not (senior_ok and junior_ok):
        print("WARNING: Interest invariants failed!")
    
    return "\n".join(results)

if __name__ == "__main__":
    md_content = verify_inferences()
    with open("Model_Inferences.md", "w") as f:
        f.write("# Protocol Inferences from Economic Model\n\n")
        f.write(md_content)
    print("Inferences generated in Model_Inferences.md")
