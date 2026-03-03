# Economic Model

Python simulation of Credit Rail's tranche-based capital accounting. Used to validate conservation laws and stress-test the waterfall mechanics before encoding invariants in Solidity.

## Directory Structure

```
economic-modelling/
├── model/                          # Core simulation engine
│   ├── state.py                    #   SystemState, TrancheState, LoanState
│   ├── flows.py                    #   allocate_capital, repay_loan, apply_loss, on_recovery
│   └── time.py                     #   accrue_loan_interest (time-weighted)
├── scripts/                        # Runnable analysis scripts
│   ├── verify_inferences.py        #   Conservation law assertions (6 tests)
│   ├── simulate_scenario.py        #   Monte Carlo stress testing (1,000+ paths)
│   ├── visualize_stress_test.py    #   Matplotlib heatmaps + violin plots
│   ├── analyze_results.py          #   Aggregates stress_test_results.csv → summary
│   └── analyze_structure.py        #   Aggregates private_credit_analysis.csv → summary
└── results/                        # Generated outputs (committed for reference)
    ├── Model_Inferences.md         #   6 key economic inferences
    ├── economic_deep_dive.md       #   Detailed waterfall analysis
    ├── economic_stress_test_report.md  # Stress test methodology + findings
    ├── stress_test_summary.md      #   Return distribution by default/recovery rate
    ├── structural_analysis_summary.md  # Cross-scenario fund comparison
    ├── stress_test_results.csv     #   Raw Monte Carlo data
    ├── private_credit_analysis.csv #   Raw multi-scenario data
    ├── structural_analysis_results.csv # Raw structural analysis data
    └── stress_test_visualization.png   # Heatmap + violin plot charts
```

## Quick Start

```bash
python3 -m venv venv && source venv/bin/activate
pip install numpy matplotlib pandas seaborn tabulate

# Validate conservation laws
python3 scripts/verify_inferences.py

# Run Monte Carlo stress tests
python3 scripts/simulate_scenario.py

# Generate charts
python3 scripts/visualize_stress_test.py

# Aggregate results into summary tables
python3 scripts/analyze_results.py
python3 scripts/analyze_structure.py
```

## What This Validates

- `Idle + Deployed = Deposited − Loss + Recovered` after every operation
- Interest waterfall distributes correctly: Senior → Junior → Equity (residual)
- Loss absorption follows reverse seniority: Equity → Junior → Senior
- Recovery restores shortfalls: Senior → Junior → Equity
- No value is created or destroyed except through interest and loss
