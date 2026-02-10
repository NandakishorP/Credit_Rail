## Model Scope

This model represents the economic behavior of a tranche-based lending system.

Included:
- Capital flows between idle and deployed
- Interest accrual over time
- Defaults, write-offs, and recoveries
- Tranche loss waterfalls
- Repayment ordering (interest → principal)

Excluded:
- Access control
- Whitelists
- ZK proofs
- Timelock / multisig
- ERC20 transfer mechanics
- Reentrancy and atomicity assumptions

The model assumes all actions are authorized and successfully executed.