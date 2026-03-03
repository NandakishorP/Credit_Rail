# Credit Rail: Private Credit Fund Simulation Report

## 1. Simulation Context
We simulated three realistic Private Credit Fund structures to analyze risk and return profiles under various stress scenarios.
**Key Change:** Loan sizes are now **proportional to capital** (e.g., £100M Fund issues £2.5M loans), introducing realistic concentration risk.

### Fund Profiles Analyzed
1.  **SME Fund (£25M):** 250 loans (~£100k avg). High diversification. 12% Borrower APR.
2.  **Mid-Market Direct Lending (£100M):** 40 loans (~£2.5M avg). High concentration. 14% Borrower APR.
3.  **Special Situations (£50M):** 20 loans (~£2.5M avg). High concentration, High Yield. 20% Borrower APR.

---

## 2. Detailed Stress Test Data

The following table presents the rigorous Monte Carlo analysis results (Mean Return ± Standard Deviation).

| Scenario | Default / Recovery | Junior Return (Mean ± Std) | Equity Return (Mean ± Std) | Net Profit / Loss |
| :--- | :--- | :--- | :--- | :--- |
| **SME Fund (£25M)** | 2.0% / 40% | **7.94%** ±0.08% | **105.8%** ±13.0% | ✅ Highly Profitable |
| **SME Fund (£25M)** | 5.0% / 40% | **7.94%** ±0.07% | **67.9%** ±17.9% | ✅ Profitable |
| **SME Fund (£25M)** | 10.0% / 40% | **1.19%** ±5.93% | **16.5%** ±13.3% | ⚠️ Junior Risk |
| | | | | |
| **Mid-Market (£100M)** | 2.0% / 40% | **8.70%** ±0.96% | **60.4%** ±18.1% | ✅ Good |
| **Mid-Market (£100M)** | 5.0% / 40% | **8.07%** ±3.30% | **37.9%** ±28.4% | ⚠️ High Variance |
| **Mid-Market (£100M)** | 10.0% / 40% | **7.90%** ±4.53% | **5.5%** ±35.5% | ❌ Equity Wipeout Risk |
| | | | | |
| **Spec Sit (£50M)** | 2.0% / 40% | **12.59%** ±1.86% | **65.1%** ±15.1% | 🚀 Massive Yield |
| **Spec Sit (£50M)** | 5.0% / 40% | **12.80%** ±1.80% | **46.0%** ±31.0% | ✅ Strong Buffer |
| **Spec Sit (£50M)** | 10.0% / 40% | **11.83%** ±4.49% | **24.5%** ±38.4% | ✅ Crisis-Resistant |

---

## 3. Analysis & Insights

### A. SME Fund (£25M)
*   **Performance:** Extremely stable at low-to-medium default rates due to diversification (250 loans).
*   **Crisis Risk:** At 10% defaults, the 12% APR isn't enough spread. Junior returns collapse to **1.19%**.
*   **Verdict:** Great for "boring" predictable returns, but vulnerable to macro shocks if spreads are too tight.

### B. Mid-Market Direct Lending (£100M)
*   **Performance:** Solid returns, but **Variance (Risk)** is high.
*   **Crisis Risk:** Standard Deviation is ±4.53% on Junior and ±35.5% on Equity. This means in a bad scenario, Equity loses money (-30%) and Junior takes a hit.
*   **Verdict:** Concentration risk is real. You need strong underwriting because one £2.5M default hurts.

### C. Special Situations (£50M) - The Winner?
*   **Performance:** The **20% Borrower APR** is a superpower.
*   **Crisis Risk:** Even with 10% defaults, the fund is robust. Junior makes ~11.8% and Equity makes ~24.5%.
*   **Verdict:** In Private Credit, **Price for Risk**. High yields protect capital better than diversification alone.

## 4. Final Recommendation
Based on this data:
1.  **Launch Strategy:** Do not compete on price (12% APR) with small capital. You will get crushed by a 10% default wave.
2.  **High Yield Niche:** Target **18-20% APR** deals (Special Situations) for your £10M-£50M launch. This gives you the buffer to survive rookie mistakes or market crashes.
3.  **Interest Rules:** Formalize the rule that "Accrued Interest is Senior to Principal Loss" in your legal docs/Solidity. This is what saved the Equity returns in all 10% default scenarios.
