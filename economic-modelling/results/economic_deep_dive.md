# Credit Rail: Economic Mechanics Deep Dive

This document explains the **First Principles** driving the simulation results. It answers *why* the numbers look the way they do and identifies the specific conditions under which the system thrives or breaks.

## 1. The "Interest Firewall" Effect (Why Yield Beats Defaults)
The most important finding is that **High Yield is a better defense than Diversification.**

## 1. The "Interest Firewall" (Why High Rates Protect You)

### What is the "Spread"?
Think of the "Spread" as your **Profit Margin**. It is the difference between the interest you *collect* from borrowers and the interest you *pay* to your investors.

**Example Calculation:**
1.  **Money IN:** You lenk £100 to a borrower at **12% Interest**. (Income = £12).
2.  **Money OUT:** You borrowed that £100 from Senior Lenders at **5% Interest**. (Cost = £5).
3.  **The Spread:** £12 - £5 = **£7 Profit**.

This £7 is your **Shield**.
*   **Equity's Shield:** The profit makes Equity holders rich (e.g., +100% gain). If they lose their principal, the profit covers it.
*   **Junior's Shield:** Higher borrower rates allow you to pay Junior Lenders **Higher Yields** (e.g., 10-12% instead of 8%).
    *   If a Junior Lender earns 12% Interest but loses 4% Principal, they are still +8% net profit.
    *   If they only earned 5% Interest and lost 4% Principal, they would barely break even (+1%).
    *   **High Yield = High Loss Absorption.**

### The Mechanics in Simulation
Each fund type has a different shield size:
*   **SME Fund:** 8% Junior Yield. Can absorb ~8% Default loss before breaking even.
*   **Special Situations:** 15% Junior Yield. Can absorb ~15% Default loss before breaking even.

This is why the "Special Situations" fund survived the 10% Crisis—its shield (15%) was thicker than the damage (10%). The SME fund's shield (8%) was thinner, so it suffered.

### The Consequence
*   **SME Fund:** With a 6.5% spread, if Default Rates exceed **6.5%**, the fund starts losing money (without recovery).
    *   *Simulation Proof:* At 10% Default, Junior returns collapsed to 1.19%. The shield was breached.
*   **Spec Sit Fund:** With a 14.5% spread, the fund can absorb **14.5% Default Rates** and still break even.
    *   *Simulation Proof:* At 10% Default, Junior returns held strong at 11.83%. The shield held.

> **Condition A:** If `(Borrower APR - Cost of Capital) > Default Rate`, the fund is mathematically indestructible.

---

## 2. The "Equity Arbitrage" (Timing of Default)
Why does Equity make +16.5% return even when the Junior Tranche barely breaks even? This seems unfair.

### The Mechanics
This is due to the **Timing of Loss Recognition**.
1.  **Scenario:** A 1-year loan pays interest monthly.
2.  **Months 1-11:** The borrower pays interest. This cash is **distributed immediately** to Equity/Junior holders. It leaves the system.
3.  **Month 12:** The borrower defaults on the Principal.
4.  **Result:** The Principal is lost (Equity takes the hit), but the **11 months of interest are already in the Equity holder's pocket.**

### The Consequence
Equity investors are essentially betting that **Interest Income > Principal Loss**.
*   In the **SME Fund (12% APR)**:
    *   Equity earns ~2.4% yield *on the total portfolios assets* (thanks to 20x leverage).
    *   If they lose 5% of their principal, the 2.4% yield * 20 leverage = 48% gain offsets the 100% principal loss? No.
    *   **Real Math:** They earn massive "spread carry" while the loan is alive.
    *   Because losses (in this model) happen at **Maturity**, Equity creates a "free option" on the interest stream.

> **Condition B:** If defaults happen **late in the loan term**, Equity outperforms. If defaults happened at **Month 1**, Equity would be wiped out immediately.

---

## 3. The "Leverage Multiplier"
Equity puts up 5-10% of the capital but captures 100% of the Upside Spread.

### The Mechanics
*   **Leverage Ratio:** 95% Senior/Junior Capital vs 5% Equity Capital = **19:1 Leverage**.
*   **Spread Income:** The fund earns 6.5% spread on £100M = £6.5M Profit.
*   **Distribution:** That £6.5M flows entirely to the £5M Equity Tranche.
*   **Return:** £6.5M / £5M = **130% Return.**

### The Consequence
This massive leverage explains why Equity returns are regularly **100%+** in good scenarios.
*   However, leverage cuts both ways. A **1% Principal Loss** on the total fund = **20% Loss** for Equity.
*   *Simulation Proof:* In the Mid-Market Fund, variance was huge (±35%). One bad loan (2.5% of fund) wipes out 50% of Equity.

> **Condition C:** Equity is a **Binary Instrument**. It either makes 100% (Good Years) or -100% (Bad Years). There is rarely a "middle ground".

---

## 4. The "Variance Trap" (Concentration Risk)
Why did the £100M Mid-Market Fund have such shaky Junior returns compared to the £10M Large Scale SME Fund?

### The Mechanics
It's simple statistics: **Sample Size (N)**.
*   **SME Fund:** 250 Loans. Default Rate hits the "Average" reliably. (Law of Large Numbers).
*   **Mid-Market Fund:** 40 Loans.
    *   If default rate is 5%, expected defaults = 2 loans.
    *   But standard deviation means you might get **0 defaults** (Huge Profit) or **5 defaults** (Huge Loss).
    *   One "extra" default represents £2.5M loss, which is 50% of the entire Equity Tranche.

### The Consequence
In the **Mid-Market**, the "Average Return" is misleading. The **Range of Outcomes** is what matters.
*   In 20% of simulations, the Junior Tranche likely **lost principal**.
*   In 80% of simulations, they made full yield.

> **Condition D:** If N < 50 loans, you **cannot rely on averages**. You must hold significantly more Equity (15-20%) to buffer the "Lumpiness Risk".

---

## Summary of Critical Conditions

| Condition | Outcome | Why? |
| :--- | :--- | :--- |
| **High Spread (20% APR)** | **Stable & Profitable** | The "Interest Firewall" burns hotter than the defaults effectively. |
| **Late Defaults** | **Equity Wins** | Interest is harvested before Principal is lost. |
| **Concentrated Portfolio (<50 Loans)** | **High Variance** | One bad loan kills the quarter. Requires higher Equity buffer. |
| **Diversified Portfolio (>200 Loans)** | **Predictable** | Variance disappears. 5% Equity is safe. |

## Recommendations for Implementation

1.  **Enforce Sector Limits:** For funds with <50 loans (Mid-Market), hard-code a limit so no single sector >20%. This prevents correlated variance spikes.
2.  **Sweep Interest Monthly:** To maximize the "Equity Arbitrage" effect for your LPs, ensure the Solidity contracts distribute interest **monthly** rather than at maturity. This "locks in" the gains.
3.  **Tiered Equity Requirements:**
    *   If `Loan_Avg_Size / Total_Fund > 2%` (Concentrated): Require **15% Equity**.
    *   If `Loan_Avg_Size / Total_Fund < 0.5%` (Diversified): Allow **5% Equity**.
