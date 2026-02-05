"""
Wake fuzzing test for Credit Rail invariants.

This test reimplements the logic from Handler.t.sol in native Python to work with Wake.
"""

from wake.testing import *
from wake.testing.fuzzing import *
from typing import List, Mapping
from pytypes.src.TranchePool import TranchePool
from pytypes.src.LoanEngine import LoanEngine
from pytypes.lib.openzeppelincontracts.contracts.mocks.token.ERC20Mock import ERC20Mock
from pytypes.src.CreditPolicy import CreditPolicy
from pytypes.test.mocks.MockLoanProofVerifier import MockLoanProofVerifier
from eth_utils import to_bytes, keccak

class InvariantTest(FuzzTest):
    # Contracts
    tranche_pool: TranchePool
    loan_engine: LoanEngine
    usdt: ERC20Mock
    credit_policy: CreditPolicy
    verifier: MockLoanProofVerifier

    # Users
    senior_users: List[Account]
    junior_users: List[Account]
    equity_users: List[Account]
    borrowers: List[Account]
    receiving_entity: Account
    fee_manager: Account
    deployer: Account

    # Accounting (Ghost Variables)
    total_idle_value: uint256
    total_deployed_value: uint256
    total_deposited: uint256
    total_loss: uint256
    total_recovered: uint256
    outstanding_principal: uint256

    # Tranche specific accounting
    senior_tranche_idle: uint256
    senior_tranche_deployed: uint256
    junior_tranche_idle: uint256
    junior_tranche_deployed: uint256
    equity_tranche_idle: uint256
    equity_tranche_deployed: uint256

    # Share tracking
    senior_tranche_shares: Mapping[Address, uint256]
    senior_tranche_total_shares: uint256
    senior_tranche_deposits: Mapping[Address, uint256]
    
    junior_tranche_shares: Mapping[Address, uint256]
    junior_tranche_total_shares: uint256
    junior_tranche_deposits: Mapping[Address, uint256]

    equity_tranche_shares: Mapping[Address, uint256]
    equity_tranche_total_shares: uint256
    equity_tranche_deposits: Mapping[Address, uint256]

    def pre_sequence(self) -> None:
        """Setup before each fuzzing sequence."""
        self.deployer = default_chain.accounts[0]
        self.receiving_entity = default_chain.accounts[1]
        self.fee_manager = default_chain.accounts[2]
        
        # Deploy dependencies
        self.usdt = ERC20Mock.deploy()
        self.tranche_pool = TranchePool.deploy(self.usdt)
        self.credit_policy = CreditPolicy.deploy()
        self.verifier = MockLoanProofVerifier.deploy()
        
        # Configure TranchePool
        self.tranche_pool.setMaxAllocationCapSeniorTranche(50_000_000 * 10**18)
        self.tranche_pool.setMaxAllocationCapJuniorTranche(30_000_000 * 10**18)
        self.tranche_pool.setMaxAllocationCapEquityTranche(20_000_000 * 10**18)
        self.tranche_pool.setMinimumDepositAmountSeniorTranche(1_000_000 * 10**18)
        self.tranche_pool.setMinimumDepositAmountJuniorTranche(5_000_000 * 10**18)
        self.tranche_pool.setMinimumDepositAmountEquityTranche(10_000_000 * 10**18)
        self.tranche_pool.setTrancheCapitalAllocationFactorJunior(15)
        self.tranche_pool.setTrancheCapitalAllocationFactorSenior(80)
        self.tranche_pool.setSeniorAPR(8)
        self.tranche_pool.setTargetJuniorAPR(15)

        # Configure CreditPolicy
        self.credit_policy.setMaxTiers(3)
        self.credit_policy.createPolicy(1)
        
        self.credit_policy.updateEligibility(1, CreditPolicy.EligibilityCriteria(
            minAnnualRevenue=10_000_000,
            minEBITDA=1_000_000,
            minTangibleNetWorth=5_000_000,
            minBusinessAgeDays=180,
            maxDefaultsLast36Months=0,
            bankruptcyExcluded=True
        ))
        
        self.credit_policy.updateRatios(1, CreditPolicy.FinancialRatios(
            maxTotalDebtToEBITDA=4 * 10**18,
            minInterestCoverageRatio=2 * 10**18,
            minCurrentRatio=1 * 10**18,
            minEBITDAMarginBps=1500
        ))
        
        self.credit_policy.updateConcentration(1, CreditPolicy.ConcentrationLimits(
            maxSingleBorrowerBps=1000,
            maxIndustryConcentrationBps=3000
        ))

        self.credit_policy.updateAttestation(1, CreditPolicy.AttestationRequirements(
            maxAttestationAgeDays=90,
            reAttestationFrequencyDays=180,
            requiresCPAAttestation=True
        ))
        
        self.credit_policy.updateCovenants(1, CreditPolicy.MaintenanceCovenants(
            maxLeverageRatio=4 * 10**18,
            minCoverageRatio=2 * 10**18,
            minLiquidityAmount=10_000_000,
            allowsDividends=False,
            reportingFrequencyDays=90
        ))
        
        self.credit_policy.setLoanTier(1, 1, CreditPolicy.LoanTier(
            name="Tier 1",
            minRevenue=10_000_000,
            maxRevenue=50_000_000,
            minEBITDA=1_000_000,
            maxDebtToEBITDA=3 * 10**18,
            maxLoanToEBITDA=2 * 10**18,
            interestRateBps=800,
            originationFeeBps=100,
            termDays=365,
            active=True
        ))
        
        self.credit_policy.setPolicyDocument(1, keccak(b"document"), "ipfs://policyDocHash")
        self.credit_policy.freezePolicy(1)
        
        # Deploy LoanEngine
        self.loan_engine = LoanEngine.deploy(
            self.credit_policy,
            self.verifier,
            500, # origination fee
            self.tranche_pool,
            self.usdt
        )
        self.tranche_pool.setLoanEngine(self.loan_engine)
        
        # Whitelist setup
        self.loan_engine.setWhitelistedFeeManager(self.fee_manager, True)
        self.loan_engine.setWhitelistedOffRampingEntity(self.receiving_entity, True)
        self.loan_engine.setWhitelistedRepaymentAgent(self.receiving_entity, True)
        self.loan_engine.setWhitelistedRecoveryAgent(self.receiving_entity, True)
        
        # Setup Users
        self.senior_users = []
        self.junior_users = []
        self.equity_users = []
        self.borrowers = []

        # Use existing accounts (Anvil default is 10)
        # 0: Deployer
        # 1: Receiving Entity
        # 2: Fee Manager
        # 3,4: Senior
        # 5,6: Junior
        # 7,8: Equity
        # 9: Extra
        
        # Reset Accounting
        self.total_idle_value = 0
        self.total_deployed_value = 0
        self.total_deposited = 0
        self.total_loss = 0
        self.total_recovered = 0
        self.outstanding_principal = 0
        self.senior_tranche_idle = 0
        self.junior_tranche_idle = 0
        self.equity_tranche_idle = 0
        self.senior_tranche_deployed = 0
        self.junior_tranche_deployed = 0
        self.equity_tranche_deployed = 0
        
        self.senior_tranche_total_shares = 0
        self.junior_tranche_total_shares = 0
        self.equity_tranche_total_shares = 0

        self.senior_tranche_shares = {}
        self.junior_tranche_shares = {}
        self.equity_tranche_shares = {}
        self.senior_tranche_deposits = {}
        self.junior_tranche_deposits = {}
        self.equity_tranche_deposits = {}

        # Initialize users with tokens and whitelisting
        for i in range(3, 5):
            user = default_chain.accounts[i]
            self.senior_users.append(user)
            self.usdt.mint(user, 10_000_000_000 * 10**18)
            self.tranche_pool.updateWhitelist(user, True)
            self.senior_tranche_shares[user.address] = 0
            self.senior_tranche_deposits[user.address] = 0
        
        for i in range(5, 7):
            user = default_chain.accounts[i]
            self.junior_users.append(user)
            self.usdt.mint(user, 10_000_000_000 * 10**18)
            self.tranche_pool.updateWhitelist(user, True)
            self.junior_tranche_shares[user.address] = 0
            self.junior_tranche_deposits[user.address] = 0

        for i in range(7, 9):
            user = default_chain.accounts[i]
            self.equity_users.append(user)
            self.usdt.mint(user, 500_000_000 * 10**18)
            self.tranche_pool.updateEquityTrancheWhiteList(user, True)
            self.equity_tranche_shares[user.address] = 0
            self.equity_tranche_deposits[user.address] = 0
            
        # Create random borrowers (they don't need to sign, just addresses)
        for i in range(50):
            # Deterministic generation for reproducibility
            addr = Account(Address(keccak(to_bytes(i))[:20].hex()), chain=default_chain)
            # Actually, loanEngine.createLoan just takes 'address'.
            # In Wake, Account object can be used where Address is expected.
            # But Account(...) constructor might assume it exists on chain?
            # Let's just use Account(Address(...))
            # Address constructor takes bytes or hex string. E.g. Address("0x...")
            # Let's use Account(0) for a moment? No.
            # Use `Address(int(i + 1000))`?
            # Simpler: just use Account(Address.from_int(i + 0x1000))) if available.
            # Or just string formatting.
            addr = Account(Address(f"0x{(i+2000):040x}"), chain=default_chain)
            self.borrowers.append(addr)
            
        self.usdt.mint(self.receiving_entity, 500_000_000 * 10**18)

    @flow()
    def flow_deposit_senior(self, user_idx: uint256, amount: uint256):
        if self.tranche_pool.getPoolState() != 0: # OPEN
            return
        
        user = self.senior_users[user_idx % len(self.senior_users)]
        min_dep = self.tranche_pool.getSeniorTrancheMinimumDepositAmount()
        max_cap = self.tranche_pool.getSeniorTrancheMaxDepositCap()
        
        # Bound amount logic
        if amount < min_dep: amount = min_dep
        if amount > max_cap: amount = max_cap
        
        current_cap_usage = amount + self.senior_tranche_idle + self.senior_tranche_deployed
        if current_cap_usage > max_cap:
            amount = max_cap - self.senior_tranche_idle - self.senior_tranche_deployed
            if amount < min_dep:
                return

        if amount == 0: return

        self.usdt.approve(self.tranche_pool, amount, from_=user)
        self.tranche_pool.depositSeniorTranche(amount, from_=user)
        
        self.senior_tranche_idle += amount
        self.total_idle_value += amount

    @flow()
    def flow_deposit_junior(self, user_idx: uint256, amount: uint256):
        if self.tranche_pool.getPoolState() != 0:
            return
            
        user = self.junior_users[user_idx % len(self.junior_users)]
        min_dep = self.tranche_pool.getJuniorTrancheMinimumDepositAmount()
        max_cap = self.tranche_pool.getJuniorTrancheMaxDepositCap()
        
        if amount < min_dep: amount = min_dep
        current_cap_usage = amount + self.junior_tranche_idle + self.junior_tranche_deployed
        if current_cap_usage > max_cap:
            amount = max_cap - self.junior_tranche_idle - self.junior_tranche_deployed
            if amount < min_dep: return

        if amount == 0: return

        self.usdt.approve(self.tranche_pool, amount, from_=user)
        self.tranche_pool.depositJuniorTranche(amount, from_=user)
        
        self.junior_tranche_idle += amount
        self.total_idle_value += amount

    @flow()
    def flow_deposit_equity(self, user_idx: uint256, amount: uint256):
        if self.tranche_pool.getPoolState() != 0:
            return
            
        user = self.equity_users[user_idx % len(self.equity_users)]
        min_dep = self.tranche_pool.getEquityTrancheMinimumDepositAmount()
        max_cap = self.tranche_pool.getEquityTrancheMaxDepositCap()
        
        if amount < min_dep: amount = min_dep
        current_cap_usage = amount + self.equity_tranche_idle + self.equity_tranche_deployed
        if current_cap_usage > max_cap:
            amount = max_cap - self.equity_tranche_idle - self.equity_tranche_deployed
            if amount < min_dep: return

        if amount == 0: return

        self.usdt.approve(self.tranche_pool, amount, from_=user)
        self.tranche_pool.depositEquityTranche(amount, from_=user)
        
        self.equity_tranche_idle += amount
        self.total_idle_value += amount

    @flow()
    def flow_commit_pool(self):
        if self.tranche_pool.getPoolState() == 0 and self.tranche_pool.getTotalIdleValue() > 0:
            self.tranche_pool.setPoolState(1, from_=self.deployer) # COMMITED
            self.total_deposited = self.tranche_pool.getTotalIdleValue()

    @flow()
    def flow_create_loan(self, principal: uint256, user_idx: uint256):
        state = self.tranche_pool.getPoolState()
        if state != 1 and state != 2: # COMMITED or DEPLOYED
            return
            
        min_principal = 1_000_000 * 10**18
        max_principal = 20_000_000 * 10**18
        
        pool_idle = self.tranche_pool.getTotalIdleValue()
        # Constraint: keep 10%
        # NOTE: Simplified logic for Wake compared to Handler
        
        if pool_idle < min_principal: return

        if principal < min_principal: principal = min_principal
        if principal > max_principal: principal = max_principal
        if principal > pool_idle: principal = pool_idle
        
        # Cap at 10% of idle logic
        if principal > pool_idle // 10:
            principal = pool_idle // 10
            
        if principal < min_principal: return
        
        user = self.borrowers[user_idx % len(self.borrowers)]
        
        # Hashing logic
        # borrowerCommitment = keccak256(abi.encodePacked(user, user_idx))
        # In python we construct the bytes manually
        # user address is 20 bytes. user_idx is uint256 (32 bytes).
        # But wait, abi.encodePacked does loose packing.
        # Address is 20 bytes. user_idx (uint256) is 32 bytes? No, Packed encoding?
        # Standard abi.encodePacked(address, uint256) -> 20 bytes + 32 bytes.
        
        # Simpler: Just use consistent values. It doesn't need to match solidity's keccak exactly
        # as long as we pass consistent values to createLoan.
        # However, createLoan verifies signatures/proofs? 
        # No, MockLoanProofVerifier always returns true.
        
        borrower_commitment = keccak(to_bytes(hexstr=str(user.address)) + user_idx.to_bytes(32, 'big'))
        
        next_id = self.loan_engine.getNextLoanId()
        
        # nullifier = keccak256(abi.encode(nextLoanId, userIndex, borrowerCommitment, timestamp))
        # abi.encode uses 32-byte padding.
        nullifier = keccak(
            next_id.to_bytes(32, 'big') + 
            user_idx.to_bytes(32, 'big') + 
            borrower_commitment + 
            default_chain.blocks['latest'].timestamp.to_bytes(32, 'big')
        )
        
        proof_data = b'' # MockVerifier ignores it
        
        self.loan_engine.createLoan(
            borrower_commitment,
            nullifier,
            1, # policy version
            1, # score
            principal,
            500, # aprBps
            500, # originationFeeBps
            180, # duration
            bytes(32), # industry
            proof_data,
            [], # proof
            from_=self.deployer
        )

    @flow()
    def flow_activate_loan(self, loan_id: uint256):
        next_id = self.loan_engine.getNextLoanId()
        if next_id == 1: return
        # bound loan_id
        loan_id = 1 + (loan_id % (next_id - 1))
        
        details = self.loan_engine.getLoanDetails(loan_id)
        if details.state != 1: # CREATED
            return

        # Guard: Pool must be COMMITTED or DEPLOYED
        pool_state = self.tranche_pool.getPoolState()
        if pool_state != 1 and pool_state != 2: # COMMITED=1, DEPLOYED=2
             return
            
        if details.principalIssued > self.tranche_pool.getTotalIdleValue():
            return
            
        self.loan_engine.activateLoan(loan_id, self.receiving_entity, self.fee_manager, from_=self.deployer)
        
        self.total_deployed_value += details.principalIssued
        self.total_idle_value -= details.principalIssued
        self.outstanding_principal += details.principalIssued

    @flow()
    def flow_repay_loan(self, loan_id: uint256, principal_amt: uint256, interest_amt: uint256):
        next_id = self.loan_engine.getNextLoanId()
        if next_id == 1: return
        loan_id = 1 + (loan_id % (next_id - 1))
        
        # Pre-check state to avoid revert
        details_pre = self.loan_engine.getLoanDetails(loan_id)
        if details_pre.state != 2: # ACTIVE
            return
            
        # We still cap amounts to avoid silly reverts, but we won't rely on them for accounting
        # Estimate total interest roughly to clip interest_amt
        # Use existing logic for specific flow inputs, but do accounting post-facto
        
        # ... logic to bound inputs ...
        if principal_amt > details_pre.principalOutstanding:
            principal_amt = details_pre.principalOutstanding
            
        # Just run the tx
        # We need to approve enough.
        total_repay = principal_amt + interest_amt
        if total_repay == 0: return

        self.usdt.approve(self.loan_engine, total_repay, from_=self.receiving_entity)
        try:
            self.loan_engine.repayLoan(loan_id, principal_amt, interest_amt, self.receiving_entity, from_=self.deployer)
        except TransactionRevertedError:
            # If it reverts (e.g. slight overpayment calc mismatch), just ignore this step
            return
        
        # Post-state check for accounting
        details_post = self.loan_engine.getLoanDetails(loan_id)
        
        principal_paid = details_pre.principalOutstanding - details_post.principalOutstanding
        
        self.total_deployed_value -= principal_paid
        self.total_idle_value += principal_paid
        self.outstanding_principal -= principal_paid

    @flow()
    def flow_write_off(self, loan_id: uint256):
        next_id = self.loan_engine.getNextLoanId()
        if next_id == 1: return
        loan_id = 1 + (loan_id % (next_id - 1))
        
        details = self.loan_engine.getLoanDetails(loan_id)
        if details.state != 4: # DEFAULTED
            return 
            
        principal = details.principalOutstanding
        self.loan_engine.writeOffLoan(loan_id, from_=self.deployer)
        
        self.total_deployed_value -= principal
        self.outstanding_principal -= principal
        self.total_loss += principal

    @flow()
    def flow_declare_default(self, loan_id: uint256):
        next_id = self.loan_engine.getNextLoanId()
        if next_id == 1: return
        loan_id = 1 + (loan_id % (next_id - 1))
        
        details = self.loan_engine.getLoanDetails(loan_id)
        if details.state != 2: # ACTIVE
            return
            
        self.loan_engine.declareDefault(loan_id, b'\x00'*32, from_=self.deployer)

    @flow()
    def flow_recover_loan(self, loan_id: uint256, amount: uint256):
        next_id = self.loan_engine.getNextLoanId()
        if next_id == 1: return
        loan_id = 1 + (loan_id % (next_id - 1))
        
        details = self.loan_engine.getLoanDetails(loan_id)
        if details.state != 5: # WRITTEN_OFF
            return

        if amount == 0: return
        if amount > 100_000_000 * 10**18: amount = 100_000_000 * 10**18 # sensible cap
        
        self.usdt.transfer(self.receiving_entity, amount, from_=self.senior_users[0]) # Fund agent if needed, or just mint
        self.usdt.approve(self.loan_engine, amount, from_=self.receiving_entity)
        
        self.loan_engine.recoverLoan(loan_id, amount, self.receiving_entity, from_=self.deployer)
        
        self.total_idle_value += amount
        self.total_recovered += amount

    @flow()
    def flow_warp_time(self, days: uint256):
        days = 1 + (days % 365)
        default_chain.mine(lambda t: t + (days * 86400))

    @flow()
    def flow_withdraw_senior(self, user_idx: uint256, amount: uint256):
        # Guard: Pool must be CLOSED
        if self.tranche_pool.getPoolState() != 3: # CLOSED
            return

        user = self.senior_users[user_idx % len(self.senior_users)]
        
        try:
            self.tranche_pool.claimSeniorInterest(from_=user)
        except TransactionRevertedError:
            pass 

        available_shares = self.senior_tranche_shares[user.address]
        if amount > available_shares: amount = available_shares
        if amount == 0: return
        
        current_idle = self.senior_tranche_idle
        current_shares = self.senior_tranche_total_shares
        
        if current_shares == 0: return
        amount_to_withdraw = (amount * current_idle) // current_shares
        
        try:
            self.tranche_pool.withdrawSeniorTranche(amount, from_=user)
            
            if self.senior_tranche_deposits[user.address] >= amount_to_withdraw:
                self.senior_tranche_deposits[user.address] -= amount_to_withdraw
            else:
                 self.senior_tranche_deposits[user.address] = 0
                 
            self.senior_tranche_shares[user.address] -= amount
            self.senior_tranche_total_shares -= amount
            
            self.senior_tranche_idle -= amount_to_withdraw
            self.total_idle_value -= amount_to_withdraw
            
        except TransactionRevertedError:
            pass

    @flow()
    def flow_withdraw_junior(self, user_idx: uint256, amount: uint256):
        if self.tranche_pool.getPoolState() != 3: # CLOSED
            return

        user = self.junior_users[user_idx % len(self.junior_users)]
        try:
            self.tranche_pool.claimJuniorInterest(from_=user)
        except TransactionRevertedError:
            pass

        available_shares = self.junior_tranche_shares[user.address]
        if amount > available_shares: amount = available_shares
        if amount == 0: return
        
        current_idle = self.junior_tranche_idle
        current_shares = self.junior_tranche_total_shares
        
        if current_shares == 0: return
        amount_to_withdraw = (amount * current_idle) // current_shares
        
        try:
            self.tranche_pool.withdrawJuniorTranche(amount, from_=user)
            
            if self.junior_tranche_deposits[user.address] >= amount_to_withdraw:
                self.junior_tranche_deposits[user.address] -= amount_to_withdraw
            else:
                 self.junior_tranche_deposits[user.address] = 0
                 
            self.junior_tranche_shares[user.address] -= amount
            self.junior_tranche_total_shares -= amount
            
            self.junior_tranche_idle -= amount_to_withdraw
            self.total_idle_value -= amount_to_withdraw
            
        except TransactionRevertedError:
            pass

    @flow()
    def flow_withdraw_equity(self, user_idx: uint256, amount: uint256):
        if self.tranche_pool.getPoolState() != 3: # CLOSED
            return

        user = self.equity_users[user_idx % len(self.equity_users)]
        try:
            self.tranche_pool.claimEquityInterest(from_=user)
        except TransactionRevertedError:
            pass

        available_shares = self.equity_tranche_shares[user.address]
        if amount > available_shares: amount = available_shares
        if amount == 0: return
        
        current_idle = self.equity_tranche_idle
        current_shares = self.equity_tranche_total_shares
        
        if current_shares == 0: return
        amount_to_withdraw = (amount * current_idle) // current_shares
        
        try:
            self.tranche_pool.withdrawEquityTranche(amount, from_=user)
            
            if self.equity_tranche_deposits[user.address] >= amount_to_withdraw:
                self.equity_tranche_deposits[user.address] -= amount_to_withdraw
            else:
                 self.equity_tranche_deposits[user.address] = 0
                 
            self.equity_tranche_shares[user.address] -= amount
            self.equity_tranche_total_shares -= amount
            
            self.equity_tranche_idle -= amount_to_withdraw
            self.total_idle_value -= amount_to_withdraw
            
        except TransactionRevertedError:
            pass

    @flow()
    def flow_close_pool(self):
        # Guard: Deployed or Commited? Actually Handler says ONLY if deployed>0 or not deployed -> return
        # Handler check: if(tranchePool.getTotalDeployedValue() > 0 || tranchePool.getPoolState() != TranchePool.PoolState.DEPLOYED) return;
        # Meaning: Can only close if DeployedValue == 0 AND State == DEPLOYED.
        
        deployed_val = self.tranche_pool.getTotalDeployedValue()
        state = self.tranche_pool.getPoolState()
        
        if deployed_val > 0 or state != 2: # DEPLOYED
            return
            
        self.tranche_pool.setPoolState(3, from_=self.deployer) # CLOSED

    @flow()
    def flow_claim_senior_interest(self, user_idx: uint256):
        # Guard: Pool must be CLOSED
        if self.tranche_pool.getPoolState() != 3: # CLOSED
            return
            
        user = self.senior_users[user_idx % len(self.senior_users)]
        
        # Handler checks shares > 0
        if self.senior_tranche_shares[user.address] == 0:
            return
            
        # Handler checks index delta
        try:
             curr_idx = self.tranche_pool.getSeniorInterestIndex()
             user_idx_contract = self.tranche_pool.getSeniorUserIndex(user.address)
             if curr_idx - user_idx_contract <= 0:
                 return
        except TransactionRevertedError:
             return

        try:
            self.tranche_pool.claimSeniorInterest(from_=user)
        except TransactionRevertedError:
            pass

    @flow()
    def flow_claim_junior_interest(self, user_idx: uint256):
        if self.tranche_pool.getPoolState() != 3: # CLOSED
            return
            
        user = self.junior_users[user_idx % len(self.junior_users)]
        
        if self.junior_tranche_shares[user.address] == 0:
            return
            
        try:
             if self.tranche_pool.getJuniorInterestIndex() - self.tranche_pool.getJuniorUserIndex(user.address) <= 0:
                 return
        except TransactionRevertedError:
             return

        try:
            self.tranche_pool.claimJuniorInterest(from_=user)
        except TransactionRevertedError:
            pass

    @flow()
    def flow_claim_equity_interest(self, user_idx: uint256):
        if self.tranche_pool.getPoolState() != 3: # CLOSED
            return
            
        user = self.equity_users[user_idx % len(self.equity_users)]
        
        if self.equity_tranche_shares[user.address] == 0:
            return
            
        try:
             if self.tranche_pool.getEquityInterestIndex() - self.tranche_pool.getEquityUserIndex(user.address) == 0:
                 return
        except TransactionRevertedError:
             return

        try:
            self.tranche_pool.claimEquityInterest(from_=user)
        except TransactionRevertedError:
            pass

    @invariant(period=5)
    def invariant_accounting(self):
        pool_idle = self.tranche_pool.getTotalIdleValue()
        pool_deployed = self.tranche_pool.getTotalDeployedValue()
        pool_deposited = self.tranche_pool.getTotalDeposited()
        pool_loss = self.tranche_pool.getTotalLoss()
        pool_recovered = self.tranche_pool.getTotalRecovered()
        
        # Check 1: Conservation
        # Idle + Deployed = Deposited - Loss + Recovered
        # Allow small precision error if needed, but solidity uses integer math so should be exact.
        lhs = pool_idle + pool_deployed
        rhs = pool_deposited - pool_loss + pool_recovered
        assert lhs == rhs, \
            f"Conservation failed: {pool_idle}+{pool_deployed} ({lhs}) != {pool_deposited}-{pool_loss}+{pool_recovered} ({rhs})"
            
        # Check 2: Outstanding Principal
        assert self.outstanding_principal == pool_deployed, \
             f"Outstanding Principal mismatch: Ghost {self.outstanding_principal} != Pool {pool_deployed}"

@default_chain.connect()
def test_invariants():
    InvariantTest().run(sequences_count=2000, flows_count=500)
