import pandas as pd
import sys

# Check if file exists
try:
    df = pd.read_csv('private_credit_analysis.csv')
except FileNotFoundError:
    print("Error: private_credit_analysis.csv not found.")
    sys.exit(1)

# Group by Scenario, Default, Recovery
grouped = df.groupby(['scenario', 'default_rate', 'recovery_rate'])[[
    'senior_return', 'junior_return', 'equity_return'
]].agg(['mean', 'std'])

# Flatten MultiIndex columns
grouped.columns = ['_'.join(col).strip() for col in grouped.columns.values]
summary = grouped.reset_index()

# Format as percentages
summary['Scenario'] = summary['scenario']
summary['Def/Rec'] = summary.apply(lambda x: f"{x['default_rate']:.1%} / {x['recovery_rate']:.0%}", axis=1)
summary['Junior Return'] = summary['junior_return_mean'].apply(lambda x: f"{x:.2%}") + " ±" + summary['junior_return_std'].apply(lambda x: f"{x:.2%}")
summary['Equity Return'] = summary['equity_return_mean'].apply(lambda x: f"{x:.1%}") + " ±" + summary['equity_return_std'].apply(lambda x: f"{x:.1%}")

# Pivot for cleaner comparison (Focus on 4% Def / 0% Rec first)
# But a flat table is fine too.

final_table = summary[[
    'Scenario', 'Def/Rec', 'Junior Return', 'Equity Return'
]]

print(final_table.to_markdown(index=False))

with open('structural_analysis_summary.md', 'w') as f:
    f.write("# Structural Analysis Summary\n\n")
    f.write(final_table.to_markdown(index=False))
