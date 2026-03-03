# Economic Model

Python simulation of Credit Rail's tranche-based capital accounting. Used to validate conservation laws and stress-test the waterfall mechanics before encoding invariants in Solidity.

## Core Model

| File | Purpose |
|---|---|
| `model/state.py` | `SystemState`, `TrancheState`, `LoanState` dataclasses |
| `model/flows.py` | `allocate_capital`, `repay_loan`, `apply_loss`, `on_recovery` |
| `model/time.py` | `accrue_loan_interest` — time-weighted interest accrual |

## Scripts

| Script | What It Does |
|---|---|
| `verify_inferences.py` | Runs 6 conservation law assertions across scenario paths |
| `simulate_scenario.py` | Monte Carlo stress testing (1,000+ paths per scenario) |
| `visualize_stress_test.py` | Matplotlib visualization of stress test results |
| `analyze_results.py` | Aggregates `stress_test_results.csv` → `stress_test_summary.md` |
| `analyze_structure.py` | Aggregates `private_credit_analysis.csv` → `structural_analysis_summary.md` |

## Results

| File | Contents |
|---|---|
| `Model_Inferences.md` | 6 key economic inferences (value conservation, interest mechanics, loss/recovery) |
| `economic_deep_dive.md` | Detailed analysis of waterfall behavior under stress |
| `stress_test_summary.md` | Return distribution by default/recovery rate |
| `structural_analysis_summary.md` | Cross-scenario fund structure comparison |
| `stress_test_visualization.png` | Visualization of Monte Carlo results |

## Quick Start

```bash
python3 -m venv venv && source venv/bin/activate
pip install numpy matplotlib
python3 verify_inferences.py      # Validate conservation laws
python3 simulate_scenario.py      # Run Monte Carlo stress tests
python3 visualize_stress_test.py  # Generate charts
```

## What This Validates

- `Idle + Deployed = Deposited − Loss + Recovered` after every operation
- Interest waterfall distributes correctly: Senior → Junior → Equity (residual)
- Loss absorption follows reverse seniority: Equity → Junior → Senior
- Recovery restores shortfalls: Senior → Junior → Equity
- No value is created or destroyed except through interest and loss
