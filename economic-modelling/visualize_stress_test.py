import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Check if file exists
try:
    df = pd.read_csv('stress_test_results.csv')
except FileNotFoundError:
    print("Error: stress_test_results.csv not found. Run simulate_scenario.py first.")
    sys.exit(1)

# Convert rates to percentages for better readability
df['default_rate_pct'] = df['default_rate'] * 100
df['recovery_rate_pct'] = df['recovery_rate'] * 100
df['senior_return_pct'] = df['senior_return'] * 100
df['junior_return_pct'] = df['junior_return'] * 100
df['equity_return_pct'] = df['equity_return'] * 100

# Group by Scenario
grouped = df.groupby(['default_rate_pct', 'recovery_rate_pct'])[['senior_return_pct', 'junior_return_pct', 'equity_return_pct']].mean().reset_index()

# Set up the matplotlib figure
plt.figure(figsize=(20, 15))

# 1. Junior Return Heatmap
plt.subplot(2, 2, 1)
pivot_junior = grouped.pivot(index="default_rate_pct", columns="recovery_rate_pct", values="junior_return_pct")
sns.heatmap(pivot_junior, annot=True, fmt=".2f", cmap="RdYlGn", center=5)
plt.title('Average Junior Return (%)')
plt.xlabel('Recovery Rate (%)')
plt.ylabel('Default Rate (%)')

# 2. Equity Return Heatmap
plt.subplot(2, 2, 2)
pivot_equity = grouped.pivot(index="default_rate_pct", columns="recovery_rate_pct", values="equity_return_pct")
sns.heatmap(pivot_equity, annot=True, fmt=".1f", cmap="RdYlGn", center=0)
plt.title('Average Equity Return (%)')
plt.xlabel('Recovery Rate (%)')
plt.ylabel('Default Rate (%)')

# 3. Distribution of Junior Returns (Violin Plot)
plt.subplot(2, 2, 3)
sns.violinplot(x="default_rate_pct", y="junior_return_pct", hue="recovery_rate_pct", data=df, palette="muted")
plt.title('Distribution of Junior Returns')
plt.xlabel('Default Rate (%)')
plt.ylabel('Return (%)')
plt.grid(True, alpha=0.3)

# 4. Distribution of Equity Returns (Violin Plot)
plt.subplot(2, 2, 4)
sns.violinplot(x="default_rate_pct", y="equity_return_pct", hue="recovery_rate_pct", data=df, palette="muted")
plt.title('Distribution of Equity Returns')
plt.xlabel('Default Rate (%)')
plt.ylabel('Return (%)')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('stress_test_visualization.png')
print("Visualization saved to stress_test_visualization.png")
# plt.show() # Uncomment to show interactive window
