## Loan Origination Flow

Preconditions:
- Underwriter is active.
- Underwriter has sufficient remaining exposure capacity.
- Borrower possesses a valid underwriting credential.
- ZK proof verifies eligibility.

Steps:
1. Borrower submits ZK proof and loan request.
2. Contract verifies proof.
3. Contract checks pool utilization limits.
4. Capital is allocated from tranches.
5. Loan state is created as ACTIVE.
6. Events are emitted for off-chain systems.

Postconditions:
- Pool deployed capital increases.
- Underwriter active exposure increases.


## Repayment Flow

Preconditions:
- Loan is ACTIVE.

Steps:
1. Borrower submits repayment.
2. Interest is computed.
3. Senior tranche receives fixed yield.
4. Junior tranche receives residual.
5. Loan state transitions to REPAID.

Postconditions:
- Pool deployed capital decreases.
- Loan closed.

## Default Flow

Preconditions:
- Loan is ACTIVE.
- Current time > loan maturity + grace period.

Steps:
1. Anyone may call markDefault().
2. Loan transitions to DEFAULTED.
3. Loss amount is calculated.
4. Loss is absorbed via waterfall.
5. Underwriter metrics updated.
6. Default event emitted.

Postconditions:
- Pool capital reduced.
- Off-chain enforcement triggered.


## Recovery Distribution Flow

Preconditions:
- Loan was DEFAULTED.
- Recovery funds are available.

Steps:
1. Governance submits recovery amount.
2. Senior tranche reimbursed first.
3. Junior tranche reimbursed next.
4. Remaining funds handled by governance policy.

Postconditions:
- Tranche losses reduced.

