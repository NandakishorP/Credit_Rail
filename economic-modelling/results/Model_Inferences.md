# Economic Model Inferences

Based on the Python economic simulation, we derived the following inferences regarding the protocol's value flows.

## 1. Value Conservation
**Question:** Is value created or destroyed in the system (except for loss)?
**Inference:** **No.** 
The simulation confirms that **no value is created or destroyed** during capital allocation or principal repayment.
- **Evidence:** Allocating a 1M loan changed the internal state (Idle $\to$ Deployed) but the `Total Value` remained exactly `30,000,000.00`.
- **Conclusion:** The protocol acts as a closed system for principal, conserving total value across state transitions.

## 2. Principal Repayment Mechanics
**Question:** Does principal repayment move funds from Deployed to Idle?
**Inference:** **Yes.**
Principal repayment explicitly shifts value from `Deployed` back to `Idle`.
- **Evidence:** When 500k principal was repaid, the `Deployed` amount decreased by 500k and the `Idle` amount increased by 500k. The total system value remained constant (excluding accrued interest).
- **Conclusion:** Principal repayment recycles capital, making it available for new loans.

## 3. Interest and System Value
**Question:** Does interest increase system value?
**Inference:** **Yes.**
Interest payments enter the system as new value, permanently increasing the `Total Value`.
- **Evidence:** Repaying 50k in interest increased the `Total Value` by 50k (captured as Unclaimed Interest/Protocol Revenue).
- **Conclusion:** Interest matches the definition of "value creation" for the protocol (yield).

## 4. Loss Impact
**Question:** Does loss reduce system value?
**Inference:** **Yes.**
Loan defaults and write-offs permanently reduce the `Total Value`.
- **Evidence:** Writing off a 100k loan reduced the `Total Value` by exactly 100k.
- **Conclusion:** Losses exit the system, reducing the aggregate value of the tranches (absorbed by Equity -> Junior -> Senior buffers).

## 5. Recovery Impact
**Question:** Does recovery increase system value?
**Inference:** **Yes.**
Recoveries inject value back into the system, reversing the effect of losses.
- **Evidence:** Recovering 50k from a written-off loan increased the `Total Value` by 50k.
- **Conclusion:** Recoveries behave like external injections, restoring `Idle` capital and increasing the total value.

## 6. Interest Accounting Invariants
**Question:** Does the system satisfy the `Target >= Accrued >= Unclaimed` invariant for Cumulative Interest?
**Inference:** **Yes.**
The simulated model maintains the hierarchical integrity of interest accounting when tracked cumulatively.

### Senior Tranche
- **Cumulative Target:** 2.22
- **Cumulative Accrued:** 1.27
- **Cumulative Unclaimed (Paid):** 1.27
- **Verification:** $2.22 \ge 1.27 \ge 1.27$ -> **Pass**

### Junior Tranche
- **Cumulative Target:** 1.27
- **Cumulative Accrued:** 0.48
- **Cumulative Unclaimed (Paid):** 0.48
- **Verification:** $1.27 \ge 0.48 \ge 0.48$ -> **Pass**

### Equity Tranche
- **Cumulative Accrued:** 1.43
- **Cumulative Unclaimed (Paid):** 1.43
- **Verification:** $1.43 \ge 1.43$ -> **Pass**

**Conclusion:** The interest waterfall correctly prioritizes targets. The strict equality `Accrued == Unclaimed` in this simulation outcome is because all accrued interest was immediately paid (fully serviced loan) and none was cancelled by loss in this specific scenario path.
