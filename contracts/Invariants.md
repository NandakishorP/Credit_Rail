## Invariants

1. Losses are applied in the following order Underwriter first loss ->  Junior -> Senior.
2. Senoir cannot loss capital before the junior got exhausted.
3. One underwriting collateral == One loan.
4. Underwriter exposure <= stake * leverage.
5. Defaulted loans cannot be repaid.
6. No user cannot take more amount than specified user cap and it will be determined dynamically based on pool's liquidity conditions
7. No underwriter can issue more loan amount than the tier capacity of the borrower.
8. 
