import pandas as pd
import sys

# Check if file exists
try:
    df = pd.read_csv('stress_test_results.csv')
except FileNotFoundError:
    print("Error: stress_test_results.csv not found. Run simulate_scenario.py first.")
    sys.exit(1)

# Group by Scenario and calculate Mean and Std Dev
grouped = df.groupby(['default_rate', 'recovery_rate'])[[
    'senior_return', 'junior_return', 'equity_return', 'total_final_value'
]].agg(['mean', 'std'])

# Flatten MultiIndex columns
grouped.columns = ['_'.join(col).strip() for col in grouped.columns.values]

# Reset index to make default_rate and recovery_rate columns again
summary = grouped.reset_index()

# Format as percentages
summary['Default Rate'] = summary['default_rate'].apply(lambda x: f"{x:.1%}")
summary['Recovery Rate'] = summary['recovery_rate'].apply(lambda x: f"{x:.0%}")

summary['Senior Return'] = summary['senior_return_mean'].apply(lambda x: f"{x:.2%}") + " ±" + summary['senior_return_std'].apply(lambda x: f"{x:.2%}")
summary['Junior Return'] = summary['junior_return_mean'].apply(lambda x: f"{x:.2%}") + " ±" + summary['junior_return_std'].apply(lambda x: f"{x:.2%}")
summary['Equity Return'] = summary['equity_return_mean'].apply(lambda x: f"{x:.1%}") + " ±" + summary['equity_return_std'].apply(lambda x: f"{x:.1%}")

# Select final columns for the clean table
final_table = summary[[
    'Default Rate', 'Recovery Rate', 
    'Senior Return', 'Junior Return', 'Equity Return'
]]

# Output to Markdown file
markdown_table = final_table.to_markdown(index=False)

with open('stress_test_summary.md', 'w') as f:
    f.write("# Stress Test Analysis Summary\n\n")
    f.write(markdown_table)

print("Analysis complete. Summary saved to 'stress_test_summary.md'.")
print("\n" + markdown_table)
