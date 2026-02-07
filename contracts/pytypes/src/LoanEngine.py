
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.access.Ownable import Ownable
from pytypes.lib.openzeppelincontracts.contracts.utils.ReentrancyGuard import ReentrancyGuard
from pytypes.src.interfaces.ICreditPolicy import ICreditPolicy



class LoanEngine(ReentrancyGuard, Ownable):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#12)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'address', 'name': '_creditPolicyContract', 'type': 'address'}, {'internalType': 'address', 'name': '_loanProofVerifier', 'type': 'address'}, {'internalType': 'uint256', 'name': '_maxOriginationFeeBps', 'type': 'uint256'}, {'internalType': 'address', 'name': '_tranchePool', 'type': 'address'}, {'internalType': 'address', 'name': '_stableCoinAddress', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\xe3\x99\xa5\x89': {'inputs': [], 'name': 'LoanEngine__InsufficientPoolLiquidity', 'type': 'error'}, b'\x89\x04\xa3v': {'inputs': [{'internalType': 'address', 'name': 'manager', 'type': 'address'}], 'name': 'LoanEngine__InvalidFeeManagerEntity', 'type': 'error'}, b'7\x14tP': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'principalIssued', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'aprBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'termDays', 'type': 'uint256'}], 'name': 'LoanEngine__InvalidLoanParameters', 'type': 'error'}, b'\n\x82N-': {'inputs': [{'internalType': 'address', 'name': 'entity', 'type': 'address'}], 'name': 'LoanEngine__InvalidOffRampingEntity', 'type': 'error'}, b'\xe0w\x12\xed': {'inputs': [], 'name': 'LoanEngine__InvalidProof', 'type': 'error'}, b'CFU\x0e': {'inputs': [{'internalType': 'address', 'name': 'agent', 'type': 'address'}], 'name': 'LoanEngine__InvalidRecoveryAgent', 'type': 'error'}, b'\xe0\x90*\n': {'inputs': [], 'name': 'LoanEngine__InvalidRepayment', 'type': 'error'}, b'\xe8P\xfc\xdb': {'inputs': [{'internalType': 'address', 'name': 'agent', 'type': 'address'}], 'name': 'LoanEngine__InvalidRepaymentAgent', 'type': 'error'}, b'\x86\xdcI\xfc': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'LoanEngine__LoanExists', 'type': 'error'}, b'\x13\x90j\x9e': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'LoanEngine__LoanIsNotActive', 'type': 'error'}, b' \x93P\xad': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'LoanEngine__LoanIsNotDefaulted', 'type': 'error'}, b'\xf5\x85_2': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'LoanEngine__LoanIsNotInCreatedState', 'type': 'error'}, b'\xf8\x90@\x85': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'LoanEngine__LoanNotRecoverable', 'type': 'error'}, b'\xa9\x0e5o': {'inputs': [{'internalType': 'uint256', 'name': 'policyVersion', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}], 'name': 'LoanEngine__LoanTierIsNotInPolicy', 'type': 'error'}, b'\x9c\xcc\xf9\xc7': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'originationFeeBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxOriginationFeeBps', 'type': 'uint256'}], 'name': 'LoanEngine__MaxOriginationFeeExceeded', 'type': 'error'}, b'1s\x91\xc6': {'inputs': [{'internalType': 'uint256', 'name': 'policyVersion', 'type': 'uint256'}], 'name': 'LoanEngine__PolicyNotFrozen', 'type': 'error'}, b'h\xf6f\xad': {'inputs': [], 'name': 'LoanEngine__PoolNotDeployed', 'type': 'error'}, b'{L\x1bL': {'inputs': [], 'name': 'LoanEngine__ProofAlreadyUsed', 'type': 'error'}, b'w\x00\xd1\x80': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'LoanEngine__ZeroLossOnWriteOff', 'type': 'error'}, b'\x01a[k': {'inputs': [], 'name': 'LoanEngine__ZeroRecovery', 'type': 'error'}, b'\x1eO\xbd\xf7': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'OwnableInvalidOwner', 'type': 'error'}, b'\x11\x8c\xda\xa7': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'OwnableUnauthorizedAccount', 'type': 'error'}, b'>\xe5\xae\xb5': {'inputs': [], 'name': 'ReentrancyGuardReentrantCall', 'type': 'error'}, b'Rt\xaf\xe7': {'inputs': [{'internalType': 'address', 'name': 'token', 'type': 'address'}], 'name': 'SafeERC20FailedOperation', 'type': 'error'}, b'\x1a\x19\x0b)5\xd0\xfe\xac=Bs\xc05fBM\xa2\xabyrj\x06\xbblg\xd7\x11\xa5\xe7U\xe7\xd2': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'principalIssued', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'startTimestamp', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'maturityTimestamp', 'type': 'uint256'}], 'name': 'LoanActivated', 'type': 'event'}, b'\xfa\xf7\x89\xd2\x9e.\xacV\xfd\xd8\xf0L\xd3t\x14\xd6wQ\x15%\x9a\x9c\xfe\xd11\xd9\xce\xcf\x04\x16\x81\x93': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanClosed', 'type': 'event'}, b'\x9e\xbe\xaf\x9a\xd3(\xdftEq\xfe\x8f"\x9f%\xc1\xfe\xa3\x83\xa3g+\x1b\xabS\xe0\x85\x18\xeaA\xb0\xdf': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'borrowerCommitment', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'principalIssued', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanCreated', 'type': 'event'}, b"\xc9\x19\xe7\x89\xb9\xf52\xc4\xa0s\x1f\xa1\x0b]Z\xf1\xcc\xb69\xd9M\x9c\x96\x8c\xc6#T5c'\x02}": {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'reasonHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanDefaulted', 'type': 'event'}, b'\x83\x90\xc0\x9c\xcb\xcd\x8a\r\xadLD\xaf_\xd7\xfcRj\x0f]\xf7\xa0\xd2\xc32\xf5\xea\xca-\xa5\x17"W': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanRecovered', 'type': 'event'}, b'r\xd1E\x1cf\x1b\x05\xf1\x88l\x7f7J\x9a\xcb\xa5\xe4\xdf2Y\xb0\xfc\xc8\x1ed\x06`j\xbbV\x15$': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'principalRepaid', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'interestRepaid', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanRepaid', 'type': 'event'}, b'\xf7\xb19B\x1e\x94\xc5e\xac\xe7\xa7\xa3\xfc{\x03\xf5~\xc6\xfd\xfb\xa3\xb5>\x9f-\xb7\xb4\x86\x9f\x18\x18\x8a': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanWrittenOff', 'type': 'event'}, b'\x8b\xe0\x07\x9cS\x16Y\x14\x13D\xcd\x1f\xd0\xa4\xf2\x84\x19I\x7f\x97"\xa3\xda\xaf\xe3\xb4\x18okdW\xe0': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'previousOwner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'newOwner', 'type': 'address'}], 'name': 'OwnershipTransferred', 'type': 'event'}, b'\xe0m(\x93': {'inputs': [], 'name': 'STANDARD_BPS', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x19\xe4\xbc\x11': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'receivingEntity', 'type': 'address'}, {'internalType': 'address', 'name': 'feeManager', 'type': 'address'}], 'name': 'activateLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd67\x92\xa7': {'inputs': [{'internalType': 'bytes32', 'name': 'borrowerCommitment', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 'nullifierHash', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'policyVersion', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'principalIssued', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'aprBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'originationFeeBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'termDays', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'proofData', 'type': 'bytes'}, {'internalType': 'bytes32[]', 'name': 'publicInputs', 'type': 'bytes32[]'}], 'name': 'createLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa7\xe3p\xb3': {'inputs': [], 'name': 'creditPolicyContract', 'outputs': [{'internalType': 'contract ICreditPolicy', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'!\xc2!\xd7': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'reasonHash', 'type': 'bytes32'}], 'name': 'declareDefault', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'f\x87{\x8d': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'getLoanDetails', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'borrowerCommitment', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'policyVersion', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'principalIssued', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'principalOutstanding', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'aprBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'originationFeeBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestAccrued', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestPaid', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lastAccrualTimestamp', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'startTimestamp', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maturityTimestamp', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'termDays', 'type': 'uint256'}, {'internalType': 'enum LoanEngine.LoanState', 'name': 'state', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'totalRecovered', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'seniorPrincipalAllocated', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'juniorPrincipalAllocated', 'type': 'uint256'}], 'internalType': 'struct LoanEngine.Loan', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, b'g\x80\xf9w': {'inputs': [], 'name': 'getMaxOriginationFeeBps', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'aF\xddo': {'inputs': [], 'name': 'getNextLoanId', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x8d\xa5\xcb[': {'inputs': [], 'name': 'owner', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'H\xab\xb7\xe3': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'recoveryAgent', 'type': 'address'}], 'name': 'recoverLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'qP\x18\xa6': {'inputs': [], 'name': 'renounceOwnership', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x16\x87K~': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'principalAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'repaymentAgent', 'type': 'address'}], 'name': 'repayLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x91\xb5\xa9\xb6': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 's_loans', 'outputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'borrowerCommitment', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'policyVersion', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'principalIssued', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'principalOutstanding', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'aprBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'originationFeeBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestAccrued', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestPaid', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lastAccrualTimestamp', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'startTimestamp', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maturityTimestamp', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'termDays', 'type': 'uint256'}, {'internalType': 'enum LoanEngine.LoanState', 'name': 'state', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'totalRecovered', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'seniorPrincipalAllocated', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'juniorPrincipalAllocated', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xefi\x7fk': {'inputs': [], 'name': 's_maxOriginationFeeBps', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x10\xc6\xb6j': {'inputs': [], 'name': 's_nextLoanId', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'e\x17J\xf8': {'inputs': [{'internalType': 'bytes32', 'name': 'nullifierHash', 'type': 'bytes32'}], 'name': 's_nullifierHashes', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd7\xd5,\x9e': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 's_originationFees', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xed\x0f6\x1b': {'inputs': [], 'name': 's_stableCoinAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'/E\xbc\x8e': {'inputs': [{'internalType': 'uint256', 'name': '_maxOriginationFeeBps', 'type': 'uint256'}], 'name': 'setMaxOriginationFeeBps', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'~wa\xa4': {'inputs': [{'internalType': 'address', 'name': 'manager', 'type': 'address'}, {'internalType': 'bool', 'name': 'isWhitelisted', 'type': 'bool'}], 'name': 'setWhitelistedFeeManager', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'0Ef\xc4': {'inputs': [{'internalType': 'address', 'name': 'entity', 'type': 'address'}, {'internalType': 'bool', 'name': 'isWhitelisted', 'type': 'bool'}], 'name': 'setWhitelistedOffRampingEntity', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xeeH\x14U': {'inputs': [{'internalType': 'address', 'name': 'agent', 'type': 'address'}, {'internalType': 'bool', 'name': 'isWhitelisted', 'type': 'bool'}], 'name': 'setWhitelistedRecoveryAgent', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x19\xb5,!': {'inputs': [{'internalType': 'address', 'name': 'agent', 'type': 'address'}, {'internalType': 'bool', 'name': 'isWhitelisted', 'type': 'bool'}], 'name': 'setWhitelistedRepaymentAgent', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf2\xfd\xe3\x8b': {'inputs': [{'internalType': 'address', 'name': 'newOwner', 'type': 'address'}], 'name': 'transferOwnership', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'-c\xf3\xd4': {'inputs': [{'internalType': 'address', 'name': 'whiteListedFeeManager', 'type': 'address'}], 'name': 'whitelistedFeeManagers', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe5\xd2\xeeC': {'inputs': [{'internalType': 'address', 'name': 'whitelistedOffRampingEntity', 'type': 'address'}], 'name': 'whitelistedOffRampingEntities', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\\\xd1\xd6s': {'inputs': [{'internalType': 'address', 'name': 'whiteListedRecoveryAgent', 'type': 'address'}], 'name': 'whitelistedRecoveryAgents', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe6V\xfd\x8c': {'inputs': [{'internalType': 'address', 'name': 'whiteListedRepaymentAgent', 'type': 'address'}], 'name': 'whitelistedRepaymentAgents', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'r}\xf7\\': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'writeOffLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":8,"contract":"src/LoanEngine.sol:LoanEngine","label":"_owner","offset":0,"slot":0,"type":"t_address"},{"astId":3084,"contract":"src/LoanEngine.sol:LoanEngine","label":"creditPolicyContract","offset":0,"slot":1,"type":"t_contract(ICreditPolicy)7649"},{"astId":3087,"contract":"src/LoanEngine.sol:LoanEngine","label":"loanProofVerifier","offset":0,"slot":2,"type":"t_contract(IVerifier)7853"},{"astId":3090,"contract":"src/LoanEngine.sol:LoanEngine","label":"tranchePool","offset":0,"slot":3,"type":"t_contract(ITranchePool)7840"},{"astId":3095,"contract":"src/LoanEngine.sol:LoanEngine","label":"s_loans","offset":0,"slot":4,"type":"t_mapping(t_uint256,t_struct(Loan)3174_storage)"},{"astId":3099,"contract":"src/LoanEngine.sol:LoanEngine","label":"s_originationFees","offset":0,"slot":5,"type":"t_mapping(t_uint256,t_uint256)"},{"astId":3103,"contract":"src/LoanEngine.sol:LoanEngine","label":"whitelistedOffRampingEntities","offset":0,"slot":6,"type":"t_mapping(t_address,t_bool)"},{"astId":3107,"contract":"src/LoanEngine.sol:LoanEngine","label":"whitelistedRecoveryAgents","offset":0,"slot":7,"type":"t_mapping(t_address,t_bool)"},{"astId":3111,"contract":"src/LoanEngine.sol:LoanEngine","label":"whitelistedRepaymentAgents","offset":0,"slot":8,"type":"t_mapping(t_address,t_bool)"},{"astId":3115,"contract":"src/LoanEngine.sol:LoanEngine","label":"whitelistedFeeManagers","offset":0,"slot":9,"type":"t_mapping(t_address,t_bool)"},{"astId":3119,"contract":"src/LoanEngine.sol:LoanEngine","label":"s_nullifierHashes","offset":0,"slot":10,"type":"t_mapping(t_bytes32,t_bool)"},{"astId":3122,"contract":"src/LoanEngine.sol:LoanEngine","label":"s_nextLoanId","offset":0,"slot":11,"type":"t_uint256"},{"astId":3124,"contract":"src/LoanEngine.sol:LoanEngine","label":"s_maxOriginationFeeBps","offset":0,"slot":12,"type":"t_uint256"},{"astId":3126,"contract":"src/LoanEngine.sol:LoanEngine","label":"s_stableCoinAddress","offset":0,"slot":13,"type":"t_address"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_contract(ICreditPolicy)7649":{"encoding":"inplace","label":"contract ICreditPolicy","numberOfBytes":20},"t_contract(ITranchePool)7840":{"encoding":"inplace","label":"contract ITranchePool","numberOfBytes":20},"t_contract(IVerifier)7853":{"encoding":"inplace","label":"contract IVerifier","numberOfBytes":20},"t_enum(LoanState)3136":{"encoding":"inplace","label":"enum LoanEngine.LoanState","numberOfBytes":1},"t_mapping(t_address,t_bool)":{"encoding":"mapping","label":"mapping(address => bool)","numberOfBytes":32,"key":"t_address","value":"t_bool"},"t_mapping(t_bytes32,t_bool)":{"encoding":"mapping","label":"mapping(bytes32 => bool)","numberOfBytes":32,"key":"t_bytes32","value":"t_bool"},"t_mapping(t_uint256,t_struct(Loan)3174_storage)":{"encoding":"mapping","label":"mapping(uint256 => struct LoanEngine.Loan)","numberOfBytes":32,"key":"t_uint256","value":"t_struct(Loan)3174_storage"},"t_mapping(t_uint256,t_uint256)":{"encoding":"mapping","label":"mapping(uint256 => uint256)","numberOfBytes":32,"key":"t_uint256","value":"t_uint256"},"t_struct(Loan)3174_storage":{"encoding":"inplace","label":"struct LoanEngine.Loan","numberOfBytes":576,"members":[{"astId":3138,"contract":"src/LoanEngine.sol:LoanEngine","label":"loanId","offset":0,"slot":0,"type":"t_uint256"},{"astId":3140,"contract":"src/LoanEngine.sol:LoanEngine","label":"borrowerCommitment","offset":0,"slot":1,"type":"t_bytes32"},{"astId":3142,"contract":"src/LoanEngine.sol:LoanEngine","label":"policyVersion","offset":0,"slot":2,"type":"t_uint256"},{"astId":3144,"contract":"src/LoanEngine.sol:LoanEngine","label":"tierId","offset":0,"slot":3,"type":"t_uint8"},{"astId":3146,"contract":"src/LoanEngine.sol:LoanEngine","label":"principalIssued","offset":0,"slot":4,"type":"t_uint256"},{"astId":3148,"contract":"src/LoanEngine.sol:LoanEngine","label":"principalOutstanding","offset":0,"slot":5,"type":"t_uint256"},{"astId":3150,"contract":"src/LoanEngine.sol:LoanEngine","label":"aprBps","offset":0,"slot":6,"type":"t_uint256"},{"astId":3152,"contract":"src/LoanEngine.sol:LoanEngine","label":"originationFeeBps","offset":0,"slot":7,"type":"t_uint256"},{"astId":3154,"contract":"src/LoanEngine.sol:LoanEngine","label":"interestAccrued","offset":0,"slot":8,"type":"t_uint256"},{"astId":3156,"contract":"src/LoanEngine.sol:LoanEngine","label":"interestPaid","offset":0,"slot":9,"type":"t_uint256"},{"astId":3158,"contract":"src/LoanEngine.sol:LoanEngine","label":"lastAccrualTimestamp","offset":0,"slot":10,"type":"t_uint256"},{"astId":3160,"contract":"src/LoanEngine.sol:LoanEngine","label":"startTimestamp","offset":0,"slot":11,"type":"t_uint256"},{"astId":3162,"contract":"src/LoanEngine.sol:LoanEngine","label":"maturityTimestamp","offset":0,"slot":12,"type":"t_uint256"},{"astId":3164,"contract":"src/LoanEngine.sol:LoanEngine","label":"termDays","offset":0,"slot":13,"type":"t_uint256"},{"astId":3167,"contract":"src/LoanEngine.sol:LoanEngine","label":"state","offset":0,"slot":14,"type":"t_enum(LoanState)3136"},{"astId":3169,"contract":"src/LoanEngine.sol:LoanEngine","label":"totalRecovered","offset":0,"slot":15,"type":"t_uint256"},{"astId":3171,"contract":"src/LoanEngine.sol:LoanEngine","label":"seniorPrincipalAllocated","offset":0,"slot":16,"type":"t_uint256"},{"astId":3173,"contract":"src/LoanEngine.sol:LoanEngine","label":"juniorPrincipalAllocated","offset":0,"slot":17,"type":"t_uint256"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32},"t_uint8":{"encoding":"inplace","label":"uint8","numberOfBytes":1}}}
    _creation_code = "60803461015d57601f611ee238819003918201601f19168301916001600160401b038311848410176101615780849260a09460405283398101031261015d5761004781610175565b9061005460208201610175565b906040810151610072608061006b60608501610175565b9301610175565b92331561014a575f8054336001600160a01b0319821681178355604051979290916001600160a01b0316907f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e09080a360017f9b779b17422d0df92223018b32b4d1fa46e071723d6817e2486d003becc55f00819055600b81905580546001600160a01b03199081166001600160a01b039384161790915560028054821693831693909317909255600c9290925560038054821693831693909317909255600d80549092169216919091179055611d58908161018a8239f35b631e4fbdf760e01b5f525f60045260245ffd5b5f80fd5b634e487b7160e01b5f52604160045260245ffd5b51906001600160a01b038216820361015d5756fe610100806040526004361015610013575f80fd5b5f905f3560e01c90816310c6b66a146119855750806316874b7e146116e057806319b52c21146116a157806319e4bc111461138a57806321c221d7146112ed5780632d63f3d4146112ae5780632f45bc8e1461128b578063304566c41461124c57806348abb7e3146110ee5780635cd1d673146110af5780636146dd6f1461109157806365174af81461106257806366877b8d14610e035780636780f977146101e6578063715018a614610da9578063727df75c14610c685780637e7761a414610c295780638da5cb5b14610c0257806391b5a9b614610acf578063a7e370b314610aa6578063d63792a714610333578063d7d52c9e14610309578063e06d2893146102ed578063e5d2ee43146102ae578063e656fd8c1461026f578063ed0f361b14610246578063ee48145514610204578063ef697f6b146101e65763f2fde38b1461015e575f80fd5b346101e35760203660031901126101e3576101776119b5565b61017f611ae9565b6001600160a01b031680156101cf5781546001600160a01b03198116821783556001600160a01b03167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e08380a380f35b631e4fbdf760e01b82526004829052602482fd5b80fd5b50346101e357806003193601126101e3576020600c54604051908152f35b50346101e357610243610216366119cb565b9061021f611ae9565b60018060a01b031683526007602052604083209060ff801983541691151516179055565b80f35b50346101e357806003193601126101e357600d546040516001600160a01b039091168152602090f35b50346101e35760203660031901126101e35760209060ff906040906001600160a01b0361029a6119b5565b168152600884522054166040519015158152f35b50346101e35760203660031901126101e35760209060ff906040906001600160a01b036102d96119b5565b168152600684522054166040519015158152f35b50346101e357806003193601126101e357602060405160648152f35b50346101e35760203660031901126101e35760406020916004358152600583522054604051908152f35b50346101e3576101603660031901126101e35760643560443560ff82168203610aa25760a43560e43560c4356101243567ffffffffffffffff8111610a9e5736602382011215610a9e57806004013567ffffffffffffffff8111610a9a573660248284010111610a9a57610144359067ffffffffffffffff8211610a965736602383011215610a965781600401359067ffffffffffffffff8211610a92578160051b923660248583010111610a8e576103ea611ae9565b600b54808c52600460205260408c20600e015460ff166006811015610a7a57610a685750600154604051634c2d62b760e01b8152600481018b90526001600160a01b0390911690602081602481855afa908115610a3e578d91610a49575b5015610a0b57604051637d27ad4360e11b8152600481018b9052610104356024820152602081604481855afa908115610a3e578d91610a1f575b50610a0b57604051631259673760e21b8152600481018b905260ff8c16602482015290602090829060449082905afa908115610a00578c916109e1575b50156109c6576024358b52600a60205260ff60408c2054166109b7578a60018060a01b03600254169280602460405198633a94343960e21b8a52604060048b01528260448b015201606489013786810160649081018390526060601f909201601f191688018881039290920160248901528101859052936001600160fb1b03106101e357602086606487829784996024859801608483013701010301925af1908115610858578791610988575b50156109795760035460405163217ac23760e01b81526001600160a01b0390911690602081600481855afa90811561094f57889161095a575b50600481101561090c5760021415806108d4575b6108c5576084351580156108bd575b80156108b5575b61088057600c54808311610863575060206004916040519283809263b3d814f560e01b82525afa908115610858578791610822575b506084351161081357600b54926040519461061e86611a35565b8486526004356020870152604086015260ff8616606086015260843560808601528660a086015260c085015260e084015284610100840152846101208401528461014084015284610160840152846101808401526101a083015260016101c0830152836101e083015283610200830152836102208301525f1981146107ff5760018101600b5583526004602052604083208151815560208201516001820155604082015160028201556003810160ff60608401511660ff198254161790556080820151600482015560a0820151600582015560c0820151600682015560e0820151600782015561010082015160088201556101208201516009820155610140820151600a820155610160820151600b820155610180820151600c8201556101a0820151600d820155600e81016101c083015160068110156107eb57917f9ebeaf9ad328df744571fe8f229f25c1fea383a3672b1bab53e08518ea41b0df939160809360ff801983541691161790556101e0820151600f820155610200820151601082015560116102208301519101556024358552600a60205260408520600160ff19825416179055519260ff6040519160043583526084356020840152166040820152426060820152a280f35b634e487b7160e01b86526021600452602486fd5b634e487b7160e01b84526011600452602484fd5b63e399a58960e01b8652600486fd5b90506020813d602011610850575b8161083d60209383611a66565b8101031261084c57515f610604565b5f80fd5b3d9150610830565b6040513d89823e3d90fd5b600b54639cccf9c760e01b89526004526024839052604452606487fd5b5050600b54604051630371474560e41b8152600481019190915260848035602483015260448201939093526064810191909152fd5b5082156105cf565b5083156105c8565b6368f666ad60e01b8752600487fd5b5060405163217ac23760e01b8152602081600481855afa90811561094f578891610920575b50600481101561090c57600114156105b9565b634e487b7160e01b88526021600452602488fd5b610942915060203d602011610948575b61093a8183611a66565b810190611ad1565b5f6108f9565b503d610930565b6040513d8a823e3d90fd5b610973915060203d6020116109485761093a8183611a66565b5f6105a5565b63e07712ed60e01b8652600486fd5b6109aa915060203d6020116109b0575b6109a28183611a66565b810190611ab9565b5f61056c565b503d610998565b631ed306d360e21b8b5260048bfd5b63a90e356f60e01b8b52600489905260ff8a1660245260448bfd5b6109fa915060203d6020116109b0576109a28183611a66565b5f6104bf565b6040513d8e823e3d90fd5b6318b9c8e360e11b8c5260048a905260248cfd5b610a38915060203d6020116109b0576109a28183611a66565b5f610482565b6040513d8f823e3d90fd5b610a62915060203d6020116109b0576109a28183611a66565b5f610448565b6321b7127f60e21b8c5260045260248bfd5b634e487b7160e01b8d52602160045260248dfd5b8a80fd5b8980fd5b8880fd5b8780fd5b8680fd5b8280fd5b50346101e357806003193601126101e3576001546040516001600160a01b039091168152602090f35b50346101e35760203660031901126101e357600435815260046020526040902080808054600182015460e0526002820154600383015460ff16600484015460058501546006860154600787015490600888015492600989015494600a8a015496600b8b015498600c8c01549a600d8d01549c600e015460ff169d600f01549e60108101546080526011015460c05260405160a05260a0515260e05160a0516020015260a0516040015260a0516060015260a0516080015260a05160a0015260a05160c0015260a05160e0015260a051610100015260a051610120015260a051610140015260a051610160015260a051610180015260a0516101a0015260a0516101c001610bdb916119fa565b60a0516101e0015260805160a051610200015260c05160a051610220015260a05161024090f35b50346101e357806003193601126101e357546040516001600160a01b039091168152602090f35b50346101e357610243610c3b366119cb565b90610c44611ae9565b60018060a01b031683526009602052604083209060ff801983541691151516179055565b50346101e35760203660031901126101e35760043590610c86611ae9565b81815260046020526040812091600e83019260ff8454166006811015610d9557600403610d81576005810190600882549101948554928215610d6e57948096818096975555600560ff1982541617905560018060a01b036003541691823b15610d6a57604484928360405195869485936396fd07ed60e01b8552600485015260248401525af18015610d5f57610d46575b50507ff7b139421e94c565ace7a7a3fc7b03f57ec6fdfba3b53e9f2db7b4869f18188a6020604051428152a280f35b81610d5091611a66565b610d5b57815f610d17565b5080fd5b6040513d84823e3d90fd5b8380fd5b62ee01a360e71b86526004859052602486fd5b63209350ad60e01b83526004829052602483fd5b634e487b7160e01b84526021600452602484fd5b50346101e357806003193601126101e357610dc2611ae9565b80546001600160a01b03198116825581906001600160a01b03167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e08280a380f35b50346101e35760203660031901126101e35780610220604051610e2581611a35565b8281528260208201528260408201528260608201528260808201528260a08201528260c08201528260e08201528261010082015282610120820152826101408201528261016082015282610180820152826101a0820152826101c0820152826101e082015282610200820152015260043581526004602052604081209060405190610eaf82611a35565b82548252600183015460208301526002830154604083015260ff600384015416606083015260048301546080830152600583015460a0830152600683015460c0830152600783015460e083015260088301546101008301526009830154610120830152600a830154610140830152600b830154610160830152600c830154610180830152600d8301546101a083015260ff600e8401541690600682101561104e5750610240926011916101c0840152600f8101546101e0840152601081015461020084015201546102208201526102206040519180518352602081015160208401526040810151604084015260ff60608201511660608401526080810151608084015260a081015160a084015260c081015160c084015260e081015160e08401526101008101516101008401526101208101516101208401526101408101516101408401526101608101516101608401526101808101516101808401526101a08101516101a084015261102c6101c08201516101c08501906119fa565b6101e08101516101e08401526102008101516102008401520151610220820152f35b634e487b7160e01b81526021600452602490fd5b50346101e35760203660031901126101e35760ff60406020926004358152600a84522054166040519015158152f35b50346101e357806003193601126101e3576020600b54604051908152f35b50346101e35760203660031901126101e35760209060ff906040906001600160a01b036110da6119b5565b168152600784522054166040519015158152f35b50346101e35760603660031901126101e35760043560243561110e61199f565b611116611ae9565b6001600160a01b0381168085526007602052604085205460ff161561123a575082845260046020526040842060ff600e8201541660068110156107eb576005036112265782156112175761118f91600f849201611174838254611a07565b9055600d546003546001600160a01b03908116929116611c70565b60035483906001600160a01b0316803b15610d5b578180916024604051809481936325574bd360e11b83528860048401525af18015610d5f57611202575b505060407f8390c09ccbcd8a0dad4c44af5fd7fc526a0f5df7a0d2c332f5eaca2da5172257918151908152426020820152a280f35b8161120c91611a66565b610aa257825f6111cd565b6301615b6b60e01b8552600485fd5b63f890408560e01b85526004849052602485fd5b6321a32a8760e11b8552600452602484fd5b50346101e35761024361125e366119cb565b90611267611ae9565b60018060a01b031683526006602052604083209060ff801983541691151516179055565b50346101e35760203660031901126101e3576112a5611ae9565b600435600c5580f35b50346101e35760203660031901126101e35760209060ff906040906001600160a01b036112d96119b5565b168152600984522054166040519015158152f35b50346101e35760403660031901126101e35760043561130a611ae9565b8082526004602052600e604083200160ff8154166006811015610d95576002036113765761133782611b47565b600460ff198254161790557fc919e789b9f532c4a0731fa10b5d5af1ccb639d94d9c968cc62354356327027d604080516024358152426020820152a280f35b6309c8354f60e11b83526004829052602483fd5b50346101e35760603660031901126101e3576004356024356001600160a01b03811690819003610aa2576113bc61199f565b6113c4611ae9565b818452600660205260ff6040852054161561168d576001600160a01b03168084526009602052604084205490919060ff161561167957611402611b0f565b82845260046020526040842091600e83019160ff8354166006811015611665576001036116515760048401948554600586015542600a860155600b850192428455600d8601546201518081029080820462015180149015171561163d576114699042611a07565b94600c8701958655600260ff1982541617905561271061148f8854600789015490611a88565b049188526005602052816040892055865460018060a01b03600354169060405163b3d814f560e01b8152602081600481865afa908115611632578b91611600575b5081116115f15791896084926114e98660609796611a28565b926040519788968795631ef894cd60e21b875260048701526024860152604485015260648401525af19081156115e65786908792611587575b506010850155601184015591549254915490546040805193845242602085015283019190915260608201527f1a190b2935d0feac3d4273c03566424da2ab79726a06bb6c67d711a5e755e7d290608090a260015f516020611d035f395f51905f525580f35b9150506060813d6060116115de575b816115a360609383611a66565b810103126115da578051602090910151907f1a190b2935d0feac3d4273c03566424da2ab79726a06bb6c67d711a5e755e7d2611522565b8580fd5b3d9150611596565b6040513d88823e3d90fd5b63e399a58960e01b8a5260048afd5b90506020813d60201161162a575b8161161b60209383611a66565b8101031261084c57515f6114d0565b3d915061160e565b6040513d8d823e3d90fd5b634e487b7160e01b89526011600452602489fd5b637ac2af9960e11b86526004859052602486fd5b634e487b7160e01b87526021600452602487fd5b63448251bb60e11b84526004829052602484fd5b630a824e2d60e01b84526004829052602484fd5b50346101e3576102436116b3366119cb565b906116bc611ae9565b60018060a01b031683526008602052604083209060ff801983541691151516179055565b503461084c57608036600319011261084c576004356064356001600160a01b03811680820361084c57611711611ae9565b805f52600860205260ff60405f20541615611973575061172f611b0f565b815f52600460205260405f2090600e82019160ff835416600681101561195f5760020361194c57611764604435602435611a07565b90811561193d57611795826117b29461177c88611b47565b600d546003546001600160a01b03908116929116611c70565b600881019384548084115f14611930576117e98195868096611a28565b6005850180549093918181111561192457506117d081978893611a28565b809955600986016117e2898254611a07565b9055611a28565b80915515948561191b575b508461190a575b506003546001600160a01b0316803b1561084c575f809160446040518094819363271a61a160e21b83528860048401528960248401525af180156118ff576118c7575b505460408051928352602083019390935242928201929092527f72d1451c661b05f1886c7f374a9acba5e4df3259b0fcc81e6406606abb56152490606090a2611897575b5060015f516020611d035f395f51905f525580f35b7ffaf789d29e2eac56fdd8f04cd37414d6775115259a9cfed131d9cecf041681936020604051428152a25f611882565b7f72d1451c661b05f1886c7f374a9acba5e4df3259b0fcc81e6406606abb561524929196505f6118f691611a66565b5f95909161183e565b6040513d5f823e3d90fd5b805460ff191660031790555f6117fb565b1594505f6117f4565b6117d090978893611a28565b6117e98495868096611a28565b637048150560e11b5f5260045ffd5b836309c8354f60e11b5f5260045260245ffd5b634e487b7160e01b5f52602160045260245ffd5b63e850fcdb60e01b5f5260045260245ffd5b3461084c575f36600319011261084c57602090600b548152f35b604435906001600160a01b038216820361084c57565b600435906001600160a01b038216820361084c57565b604090600319011261084c576004356001600160a01b038116810361084c5790602435801515810361084c5790565b90600682101561195f5752565b91908201809211611a1457565b634e487b7160e01b5f52601160045260245ffd5b91908203918211611a1457565b610240810190811067ffffffffffffffff821117611a5257604052565b634e487b7160e01b5f52604160045260245ffd5b90601f8019910116810190811067ffffffffffffffff821117611a5257604052565b81810292918115918404141715611a1457565b8115611aa5570490565b634e487b7160e01b5f52601260045260245ffd5b9081602091031261084c5751801515810361084c5790565b9081602091031261084c5751600481101561084c5790565b5f546001600160a01b03163303611afc57565b63118cdaa760e01b5f523360045260245ffd5b60025f516020611d035f395f51905f525414611b385760025f516020611d035f395f51905f5255565b633ee5aeb560e01b5f5260045ffd5b805f52600460205260405f209060ff600e83015416600681101561195f57600203611c5e5750600a810190611b7d825442611a28565b60058201548015611c565764496cebb80091611ba1611ba692600686015490611a88565b611a88565b0480611bb4575b5050429055565b60088201611bc3828254611a07565b9055611bf26004830154611be46011611be983611be4601089015488611a88565b611a9b565b95015484611a88565b6003546001600160a01b0316803b1561084c5760405163439e925760e11b8152600481019390935260248301939093526044820152905f908290606490829084905af180156118ff57611c46575b80611bad565b5f611c5091611a66565b5f611c40565b505050429055565b6309c8354f60e11b5f5260045260245ffd5b6040516323b872dd60e01b5f9081526001600160a01b039384166004529290931660245260449390935260209060648180865af19060015f5114821615611ce1575b6040525f60605215611cc15750565b635274afe760e01b5f9081526001600160a01b0391909116600452602490fd5b906001811516611cf957823b15153d15161690611cb2565b503d5f823e3d90fdfe9b779b17422d0df92223018b32b4d1fa46e071723d6817e2486d003becc55f00a2646970667358221220dc9aaf67f888a600ead504705526f04cf93548a2d148a41b4b42011684222de764736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, _creditPolicyContract: Union[Account, Address], _loanProofVerifier: Union[Account, Address], _maxOriginationFeeBps: uint256, _tranchePool: Union[Account, Address], _stableCoinAddress: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#194)

        Args:
            _creditPolicyContract: address
            _loanProofVerifier: address
            _maxOriginationFeeBps: uint256
            _tranchePool: address
            _stableCoinAddress: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _creditPolicyContract: Union[Account, Address], _loanProofVerifier: Union[Account, Address], _maxOriginationFeeBps: uint256, _tranchePool: Union[Account, Address], _stableCoinAddress: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> LoanEngine:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#194)

        Args:
            _creditPolicyContract: address
            _loanProofVerifier: address
            _maxOriginationFeeBps: uint256
            _tranchePool: address
            _stableCoinAddress: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _creditPolicyContract: Union[Account, Address], _loanProofVerifier: Union[Account, Address], _maxOriginationFeeBps: uint256, _tranchePool: Union[Account, Address], _stableCoinAddress: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#194)

        Args:
            _creditPolicyContract: address
            _loanProofVerifier: address
            _maxOriginationFeeBps: uint256
            _tranchePool: address
            _stableCoinAddress: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _creditPolicyContract: Union[Account, Address], _loanProofVerifier: Union[Account, Address], _maxOriginationFeeBps: uint256, _tranchePool: Union[Account, Address], _stableCoinAddress: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#194)

        Args:
            _creditPolicyContract: address
            _loanProofVerifier: address
            _maxOriginationFeeBps: uint256
            _tranchePool: address
            _stableCoinAddress: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _creditPolicyContract: Union[Account, Address], _loanProofVerifier: Union[Account, Address], _maxOriginationFeeBps: uint256, _tranchePool: Union[Account, Address], _stableCoinAddress: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[LoanEngine]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#194)

        Args:
            _creditPolicyContract: address
            _loanProofVerifier: address
            _maxOriginationFeeBps: uint256
            _tranchePool: address
            _stableCoinAddress: address
        """
        ...

    @classmethod
    def deploy(cls, _creditPolicyContract: Union[Account, Address], _loanProofVerifier: Union[Account, Address], _maxOriginationFeeBps: uint256, _tranchePool: Union[Account, Address], _stableCoinAddress: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, LoanEngine, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[LoanEngine]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#194)

        Args:
            _creditPolicyContract: address
            _loanProofVerifier: address
            _maxOriginationFeeBps: uint256
            _tranchePool: address
            _stableCoinAddress: address
        """
        return cls._deploy(request_type, [_creditPolicyContract, _loanProofVerifier, _maxOriginationFeeBps, _tranchePool, _stableCoinAddress], return_tx, LoanEngine, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    class LoanState(IntEnum):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#115)

        """
        NONE = 0
        CREATED = 1
        ACTIVE = 2
        REPAID = 3
        DEFAULTED = 4
        WRITTEN_OFF = 5


    @dataclasses.dataclass
    class Loan:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#124)

        Attributes:
            loanId (uint256): uint256
            borrowerCommitment (bytes32): bytes32
            policyVersion (uint256): uint256
            tierId (uint8): uint8
            principalIssued (uint256): uint256
            principalOutstanding (uint256): uint256
            aprBps (uint256): uint256
            originationFeeBps (uint256): uint256
            interestAccrued (uint256): uint256
            interestPaid (uint256): uint256
            lastAccrualTimestamp (uint256): uint256
            startTimestamp (uint256): uint256
            maturityTimestamp (uint256): uint256
            termDays (uint256): uint256
            state (LoanEngine.LoanState): enum LoanEngine.LoanState
            totalRecovered (uint256): uint256
            seniorPrincipalAllocated (uint256): uint256
            juniorPrincipalAllocated (uint256): uint256
        """
        original_name = 'Loan'

        loanId: uint256
        borrowerCommitment: bytes32
        policyVersion: uint256
        tierId: uint8
        principalIssued: uint256
        principalOutstanding: uint256
        aprBps: uint256
        originationFeeBps: uint256
        interestAccrued: uint256
        interestPaid: uint256
        lastAccrualTimestamp: uint256
        startTimestamp: uint256
        maturityTimestamp: uint256
        termDays: uint256
        state: LoanEngine.LoanState
        totalRecovered: uint256
        seniorPrincipalAllocated: uint256
        juniorPrincipalAllocated: uint256


    @dataclasses.dataclass
    class LoanEngine__PolicyNotFrozen(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#18)

        Attributes:
            policyVersion (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'policyVersion', 'type': 'uint256'}], 'name': 'LoanEngine__PolicyNotFrozen', 'type': 'error'}
        original_name = 'LoanEngine__PolicyNotFrozen'
        selector = bytes4(b'1s\x91\xc6')

        policyVersion: uint256


    @dataclasses.dataclass
    class LoanEngine__InvalidProof(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#19)
        """
        _abi = {'inputs': [], 'name': 'LoanEngine__InvalidProof', 'type': 'error'}
        original_name = 'LoanEngine__InvalidProof'
        selector = bytes4(b'\xe0w\x12\xed')



    @dataclasses.dataclass
    class LoanEngine__LoanTierIsNotInPolicy(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#20)

        Attributes:
            policyVersion (uint256): uint256
            tierId (uint8): uint8
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'policyVersion', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}], 'name': 'LoanEngine__LoanTierIsNotInPolicy', 'type': 'error'}
        original_name = 'LoanEngine__LoanTierIsNotInPolicy'
        selector = bytes4(b'\xa9\x0e5o')

        policyVersion: uint256
        tierId: uint8


    @dataclasses.dataclass
    class LoanEngine__InvalidLoanParameters(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#24)

        Attributes:
            loanId (uint256): uint256
            principalIssued (uint256): uint256
            aprBps (uint256): uint256
            termDays (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'principalIssued', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'aprBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'termDays', 'type': 'uint256'}], 'name': 'LoanEngine__InvalidLoanParameters', 'type': 'error'}
        original_name = 'LoanEngine__InvalidLoanParameters'
        selector = bytes4(b'7\x14tP')

        loanId: uint256
        principalIssued: uint256
        aprBps: uint256
        termDays: uint256


    @dataclasses.dataclass
    class LoanEngine__MaxOriginationFeeExceeded(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#30)

        Attributes:
            loanId (uint256): uint256
            originationFeeBps (uint256): uint256
            maxOriginationFeeBps (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'originationFeeBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxOriginationFeeBps', 'type': 'uint256'}], 'name': 'LoanEngine__MaxOriginationFeeExceeded', 'type': 'error'}
        original_name = 'LoanEngine__MaxOriginationFeeExceeded'
        selector = bytes4(b'\x9c\xcc\xf9\xc7')

        loanId: uint256
        originationFeeBps: uint256
        maxOriginationFeeBps: uint256


    @dataclasses.dataclass
    class LoanEngine__PoolNotDeployed(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#35)
        """
        _abi = {'inputs': [], 'name': 'LoanEngine__PoolNotDeployed', 'type': 'error'}
        original_name = 'LoanEngine__PoolNotDeployed'
        selector = bytes4(b'h\xf6f\xad')



    @dataclasses.dataclass
    class LoanEngine__InvalidOffRampingEntity(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#36)

        Attributes:
            entity (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'entity', 'type': 'address'}], 'name': 'LoanEngine__InvalidOffRampingEntity', 'type': 'error'}
        original_name = 'LoanEngine__InvalidOffRampingEntity'
        selector = bytes4(b'\n\x82N-')

        entity: Address


    @dataclasses.dataclass
    class LoanEngine__LoanExists(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#37)

        Attributes:
            loanId (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'LoanEngine__LoanExists', 'type': 'error'}
        original_name = 'LoanEngine__LoanExists'
        selector = bytes4(b'\x86\xdcI\xfc')

        loanId: uint256


    @dataclasses.dataclass
    class LoanEngine__LoanIsNotInCreatedState(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#38)

        Attributes:
            loanId (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'LoanEngine__LoanIsNotInCreatedState', 'type': 'error'}
        original_name = 'LoanEngine__LoanIsNotInCreatedState'
        selector = bytes4(b'\xf5\x85_2')

        loanId: uint256


    @dataclasses.dataclass
    class LoanEngine__LoanIsNotActive(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#39)

        Attributes:
            loanId (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'LoanEngine__LoanIsNotActive', 'type': 'error'}
        original_name = 'LoanEngine__LoanIsNotActive'
        selector = bytes4(b'\x13\x90j\x9e')

        loanId: uint256


    @dataclasses.dataclass
    class LoanEngine__LoanIsNotDefaulted(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#40)

        Attributes:
            loanId (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'LoanEngine__LoanIsNotDefaulted', 'type': 'error'}
        original_name = 'LoanEngine__LoanIsNotDefaulted'
        selector = bytes4(b' \x93P\xad')

        loanId: uint256


    @dataclasses.dataclass
    class LoanEngine__InvalidRepayment(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#41)
        """
        _abi = {'inputs': [], 'name': 'LoanEngine__InvalidRepayment', 'type': 'error'}
        original_name = 'LoanEngine__InvalidRepayment'
        selector = bytes4(b'\xe0\x90*\n')



    @dataclasses.dataclass
    class LoanEngine__ZeroRecovery(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#42)
        """
        _abi = {'inputs': [], 'name': 'LoanEngine__ZeroRecovery', 'type': 'error'}
        original_name = 'LoanEngine__ZeroRecovery'
        selector = bytes4(b'\x01a[k')



    @dataclasses.dataclass
    class LoanEngine__LoanNotRecoverable(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#43)

        Attributes:
            loanId (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'LoanEngine__LoanNotRecoverable', 'type': 'error'}
        original_name = 'LoanEngine__LoanNotRecoverable'
        selector = bytes4(b'\xf8\x90@\x85')

        loanId: uint256


    @dataclasses.dataclass
    class LoanEngine__ZeroLossOnWriteOff(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#44)

        Attributes:
            loanId (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'LoanEngine__ZeroLossOnWriteOff', 'type': 'error'}
        original_name = 'LoanEngine__ZeroLossOnWriteOff'
        selector = bytes4(b'w\x00\xd1\x80')

        loanId: uint256


    @dataclasses.dataclass
    class LoanEngine__InvalidFeeManagerEntity(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#45)

        Attributes:
            manager (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'manager', 'type': 'address'}], 'name': 'LoanEngine__InvalidFeeManagerEntity', 'type': 'error'}
        original_name = 'LoanEngine__InvalidFeeManagerEntity'
        selector = bytes4(b'\x89\x04\xa3v')

        manager: Address


    @dataclasses.dataclass
    class LoanEngine__InvalidRecoveryAgent(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#46)

        Attributes:
            agent (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'agent', 'type': 'address'}], 'name': 'LoanEngine__InvalidRecoveryAgent', 'type': 'error'}
        original_name = 'LoanEngine__InvalidRecoveryAgent'
        selector = bytes4(b'CFU\x0e')

        agent: Address


    @dataclasses.dataclass
    class LoanEngine__InvalidRepaymentAgent(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#47)

        Attributes:
            agent (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'agent', 'type': 'address'}], 'name': 'LoanEngine__InvalidRepaymentAgent', 'type': 'error'}
        original_name = 'LoanEngine__InvalidRepaymentAgent'
        selector = bytes4(b'\xe8P\xfc\xdb')

        agent: Address


    @dataclasses.dataclass
    class LoanEngine__InsufficientPoolLiquidity(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#48)
        """
        _abi = {'inputs': [], 'name': 'LoanEngine__InsufficientPoolLiquidity', 'type': 'error'}
        original_name = 'LoanEngine__InsufficientPoolLiquidity'
        selector = bytes4(b'\xe3\x99\xa5\x89')



    @dataclasses.dataclass
    class LoanEngine__ProofAlreadyUsed(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#49)
        """
        _abi = {'inputs': [], 'name': 'LoanEngine__ProofAlreadyUsed', 'type': 'error'}
        original_name = 'LoanEngine__ProofAlreadyUsed'
        selector = bytes4(b'{L\x1bL')



    @dataclasses.dataclass
    class LoanCreated:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#155)

        Attributes:
            loanId (uint256): indexed uint256
            borrowerCommitment (bytes32): bytes32
            principalIssued (uint256): uint256
            tierId (uint8): uint8
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'borrowerCommitment', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'principalIssued', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanCreated', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'LoanCreated'
        selector = bytes32(b'\x9e\xbe\xaf\x9a\xd3(\xdftEq\xfe\x8f"\x9f%\xc1\xfe\xa3\x83\xa3g+\x1b\xabS\xe0\x85\x18\xeaA\xb0\xdf')

        loanId: uint256
        borrowerCommitment: bytes32
        principalIssued: uint256
        tierId: uint8
        timestamp: uint256


    @dataclasses.dataclass
    class LoanActivated:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#163)

        Attributes:
            loanId (uint256): indexed uint256
            principalIssued (uint256): uint256
            timestamp (uint256): uint256
            startTimestamp (uint256): uint256
            maturityTimestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'principalIssued', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'startTimestamp', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'maturityTimestamp', 'type': 'uint256'}], 'name': 'LoanActivated', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'LoanActivated'
        selector = bytes32(b'\x1a\x19\x0b)5\xd0\xfe\xac=Bs\xc05fBM\xa2\xabyrj\x06\xbblg\xd7\x11\xa5\xe7U\xe7\xd2')

        loanId: uint256
        principalIssued: uint256
        timestamp: uint256
        startTimestamp: uint256
        maturityTimestamp: uint256


    @dataclasses.dataclass
    class LoanRepaid:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#171)

        Attributes:
            loanId (uint256): indexed uint256
            principalRepaid (uint256): uint256
            interestRepaid (uint256): uint256
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'principalRepaid', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'interestRepaid', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanRepaid', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'LoanRepaid'
        selector = bytes32(b'r\xd1E\x1cf\x1b\x05\xf1\x88l\x7f7J\x9a\xcb\xa5\xe4\xdf2Y\xb0\xfc\xc8\x1ed\x06`j\xbbV\x15$')

        loanId: uint256
        principalRepaid: uint256
        interestRepaid: uint256
        timestamp: uint256


    @dataclasses.dataclass
    class LoanClosed:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#178)

        Attributes:
            loanId (uint256): indexed uint256
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanClosed', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'LoanClosed'
        selector = bytes32(b'\xfa\xf7\x89\xd2\x9e.\xacV\xfd\xd8\xf0L\xd3t\x14\xd6wQ\x15%\x9a\x9c\xfe\xd11\xd9\xce\xcf\x04\x16\x81\x93')

        loanId: uint256
        timestamp: uint256


    @dataclasses.dataclass
    class LoanDefaulted:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#180)

        Attributes:
            loanId (uint256): indexed uint256
            reasonHash (bytes32): bytes32
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'reasonHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanDefaulted', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'LoanDefaulted'
        selector = bytes32(b"\xc9\x19\xe7\x89\xb9\xf52\xc4\xa0s\x1f\xa1\x0b]Z\xf1\xcc\xb69\xd9M\x9c\x96\x8c\xc6#T5c'\x02}")

        loanId: uint256
        reasonHash: bytes32
        timestamp: uint256


    @dataclasses.dataclass
    class LoanWrittenOff:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#186)

        Attributes:
            loanId (uint256): indexed uint256
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanWrittenOff', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'LoanWrittenOff'
        selector = bytes32(b'\xf7\xb19B\x1e\x94\xc5e\xac\xe7\xa7\xa3\xfc{\x03\xf5~\xc6\xfd\xfb\xa3\xb5>\x9f-\xb7\xb4\x86\x9f\x18\x18\x8a')

        loanId: uint256
        timestamp: uint256


    @dataclasses.dataclass
    class LoanRecovered:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#188)

        Attributes:
            loanId (uint256): indexed uint256
            amount (uint256): uint256
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanRecovered', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'LoanRecovered'
        selector = bytes32(b'\x83\x90\xc0\x9c\xcb\xcd\x8a\r\xadLD\xaf_\xd7\xfcRj\x0f]\xf7\xa0\xd2\xc32\xf5\xea\xca-\xa5\x17"W')

        loanId: uint256
        amount: uint256
        timestamp: uint256


    @overload
    def creditPolicyContract(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ICreditPolicy:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#94)

        Returns:
            creditPolicyContract: contract ICreditPolicy
        """
        ...

    @overload
    def creditPolicyContract(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#94)

        Returns:
            creditPolicyContract: contract ICreditPolicy
        """
        ...

    @overload
    def creditPolicyContract(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#94)

        Returns:
            creditPolicyContract: contract ICreditPolicy
        """
        ...

    @overload
    def creditPolicyContract(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ICreditPolicy]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#94)

        Returns:
            creditPolicyContract: contract ICreditPolicy
        """
        ...

    def creditPolicyContract(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[ICreditPolicy, TransactionAbc[ICreditPolicy], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#94)

        Returns:
            creditPolicyContract: contract ICreditPolicy
        """
        return self._execute(self.chain, request_type, "a7e370b3", [], True if request_type == "tx" else False, ICreditPolicy, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def s_loans(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> LoanEngine.Loan:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#98)

        Args:
            key0: uint256
        Returns:
            struct LoanEngine.Loan
        """
        ...

    @overload
    def s_loans(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#98)

        Args:
            key0: uint256
        Returns:
            struct LoanEngine.Loan
        """
        ...

    @overload
    def s_loans(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#98)

        Args:
            key0: uint256
        Returns:
            struct LoanEngine.Loan
        """
        ...

    @overload
    def s_loans(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[LoanEngine.Loan]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#98)

        Args:
            key0: uint256
        Returns:
            struct LoanEngine.Loan
        """
        ...

    def s_loans(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[LoanEngine.Loan, TransactionAbc[LoanEngine.Loan], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#98)

        Args:
            key0: uint256
        Returns:
            struct LoanEngine.Loan
        """
        return self._execute(self.chain, request_type, "91b5a9b6", [key0], True if request_type == "tx" else False, LoanEngine.Loan, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def s_originationFees(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#99)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def s_originationFees(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#99)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def s_originationFees(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#99)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def s_originationFees(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#99)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    def s_originationFees(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#99)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "d7d52c9e", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def whitelistedOffRampingEntities(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#100)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedOffRampingEntities(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#100)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedOffRampingEntities(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#100)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedOffRampingEntities(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#100)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    def whitelistedOffRampingEntities(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#100)

        Args:
            key0: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "e5d2ee43", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def whitelistedRecoveryAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#102)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedRecoveryAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#102)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedRecoveryAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#102)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedRecoveryAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#102)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    def whitelistedRecoveryAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#102)

        Args:
            key0: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "5cd1d673", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def whitelistedRepaymentAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#105)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedRepaymentAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#105)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedRepaymentAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#105)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedRepaymentAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#105)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    def whitelistedRepaymentAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#105)

        Args:
            key0: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "e656fd8c", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def whitelistedFeeManagers(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#108)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedFeeManagers(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#108)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedFeeManagers(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#108)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedFeeManagers(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#108)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    def whitelistedFeeManagers(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#108)

        Args:
            key0: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "2d63f3d4", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def s_nullifierHashes(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#110)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def s_nullifierHashes(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#110)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def s_nullifierHashes(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#110)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def s_nullifierHashes(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#110)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        ...

    def s_nullifierHashes(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#110)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "65174af8", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def s_nextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#111)

        Returns:
            s_nextLoanId: uint256
        """
        ...

    @overload
    def s_nextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#111)

        Returns:
            s_nextLoanId: uint256
        """
        ...

    @overload
    def s_nextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#111)

        Returns:
            s_nextLoanId: uint256
        """
        ...

    @overload
    def s_nextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#111)

        Returns:
            s_nextLoanId: uint256
        """
        ...

    def s_nextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#111)

        Returns:
            s_nextLoanId: uint256
        """
        return self._execute(self.chain, request_type, "10c6b66a", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def s_maxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#112)

        Returns:
            s_maxOriginationFeeBps: uint256
        """
        ...

    @overload
    def s_maxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#112)

        Returns:
            s_maxOriginationFeeBps: uint256
        """
        ...

    @overload
    def s_maxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#112)

        Returns:
            s_maxOriginationFeeBps: uint256
        """
        ...

    @overload
    def s_maxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#112)

        Returns:
            s_maxOriginationFeeBps: uint256
        """
        ...

    def s_maxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#112)

        Returns:
            s_maxOriginationFeeBps: uint256
        """
        return self._execute(self.chain, request_type, "ef697f6b", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def s_stableCoinAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#113)

        Returns:
            s_stableCoinAddress: address
        """
        ...

    @overload
    def s_stableCoinAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#113)

        Returns:
            s_stableCoinAddress: address
        """
        ...

    @overload
    def s_stableCoinAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#113)

        Returns:
            s_stableCoinAddress: address
        """
        ...

    @overload
    def s_stableCoinAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#113)

        Returns:
            s_stableCoinAddress: address
        """
        ...

    def s_stableCoinAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#113)

        Returns:
            s_stableCoinAddress: address
        """
        return self._execute(self.chain, request_type, "ed0f361b", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def STANDARD_BPS(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#114)

        Returns:
            STANDARD_BPS: uint256
        """
        ...

    @overload
    def STANDARD_BPS(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#114)

        Returns:
            STANDARD_BPS: uint256
        """
        ...

    @overload
    def STANDARD_BPS(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#114)

        Returns:
            STANDARD_BPS: uint256
        """
        ...

    @overload
    def STANDARD_BPS(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#114)

        Returns:
            STANDARD_BPS: uint256
        """
        ...

    def STANDARD_BPS(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#114)

        Returns:
            STANDARD_BPS: uint256
        """
        return self._execute(self.chain, request_type, "e06d2893", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def createLoan(self, borrowerCommitment: bytes32, nullifierHash: bytes32, policyVersion: uint256, tierId: uint8, principalIssued: uint256, aprBps: uint256, originationFeeBps: uint256, termDays: uint256, industry: bytes32, proofData: Union[bytearray, bytes], publicInputs: List[bytes32], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#214)

        Args:
            borrowerCommitment: bytes32
            nullifierHash: bytes32
            policyVersion: uint256
            tierId: uint8
            principalIssued: uint256
            aprBps: uint256
            originationFeeBps: uint256
            termDays: uint256
            industry: bytes32
            proofData: bytes
            publicInputs: bytes32[]
        """
        ...

    @overload
    def createLoan(self, borrowerCommitment: bytes32, nullifierHash: bytes32, policyVersion: uint256, tierId: uint8, principalIssued: uint256, aprBps: uint256, originationFeeBps: uint256, termDays: uint256, industry: bytes32, proofData: Union[bytearray, bytes], publicInputs: List[bytes32], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#214)

        Args:
            borrowerCommitment: bytes32
            nullifierHash: bytes32
            policyVersion: uint256
            tierId: uint8
            principalIssued: uint256
            aprBps: uint256
            originationFeeBps: uint256
            termDays: uint256
            industry: bytes32
            proofData: bytes
            publicInputs: bytes32[]
        """
        ...

    @overload
    def createLoan(self, borrowerCommitment: bytes32, nullifierHash: bytes32, policyVersion: uint256, tierId: uint8, principalIssued: uint256, aprBps: uint256, originationFeeBps: uint256, termDays: uint256, industry: bytes32, proofData: Union[bytearray, bytes], publicInputs: List[bytes32], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#214)

        Args:
            borrowerCommitment: bytes32
            nullifierHash: bytes32
            policyVersion: uint256
            tierId: uint8
            principalIssued: uint256
            aprBps: uint256
            originationFeeBps: uint256
            termDays: uint256
            industry: bytes32
            proofData: bytes
            publicInputs: bytes32[]
        """
        ...

    @overload
    def createLoan(self, borrowerCommitment: bytes32, nullifierHash: bytes32, policyVersion: uint256, tierId: uint8, principalIssued: uint256, aprBps: uint256, originationFeeBps: uint256, termDays: uint256, industry: bytes32, proofData: Union[bytearray, bytes], publicInputs: List[bytes32], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#214)

        Args:
            borrowerCommitment: bytes32
            nullifierHash: bytes32
            policyVersion: uint256
            tierId: uint8
            principalIssued: uint256
            aprBps: uint256
            originationFeeBps: uint256
            termDays: uint256
            industry: bytes32
            proofData: bytes
            publicInputs: bytes32[]
        """
        ...

    def createLoan(self, borrowerCommitment: bytes32, nullifierHash: bytes32, policyVersion: uint256, tierId: uint8, principalIssued: uint256, aprBps: uint256, originationFeeBps: uint256, termDays: uint256, industry: bytes32, proofData: Union[bytearray, bytes], publicInputs: List[bytes32], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#214)

        Args:
            borrowerCommitment: bytes32
            nullifierHash: bytes32
            policyVersion: uint256
            tierId: uint8
            principalIssued: uint256
            aprBps: uint256
            originationFeeBps: uint256
            termDays: uint256
            industry: bytes32
            proofData: bytes
            publicInputs: bytes32[]
        """
        return self._execute(self.chain, request_type, "d63792a7", [borrowerCommitment, nullifierHash, policyVersion, tierId, principalIssued, aprBps, originationFeeBps, termDays, industry, proofData, publicInputs], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def activateLoan(self, loanId: uint256, receivingEntity: Union[Account, Address], feeManager: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#318)

        Args:
            loanId: uint256
            receivingEntity: address
            feeManager: address
        """
        ...

    @overload
    def activateLoan(self, loanId: uint256, receivingEntity: Union[Account, Address], feeManager: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#318)

        Args:
            loanId: uint256
            receivingEntity: address
            feeManager: address
        """
        ...

    @overload
    def activateLoan(self, loanId: uint256, receivingEntity: Union[Account, Address], feeManager: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#318)

        Args:
            loanId: uint256
            receivingEntity: address
            feeManager: address
        """
        ...

    @overload
    def activateLoan(self, loanId: uint256, receivingEntity: Union[Account, Address], feeManager: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#318)

        Args:
            loanId: uint256
            receivingEntity: address
            feeManager: address
        """
        ...

    def activateLoan(self, loanId: uint256, receivingEntity: Union[Account, Address], feeManager: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#318)

        Args:
            loanId: uint256
            receivingEntity: address
            feeManager: address
        """
        return self._execute(self.chain, request_type, "19e4bc11", [loanId, receivingEntity, feeManager], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, repaymentAgent: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#371)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
            repaymentAgent: address
        """
        ...

    @overload
    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, repaymentAgent: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#371)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
            repaymentAgent: address
        """
        ...

    @overload
    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, repaymentAgent: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#371)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
            repaymentAgent: address
        """
        ...

    @overload
    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, repaymentAgent: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#371)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
            repaymentAgent: address
        """
        ...

    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, repaymentAgent: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#371)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
            repaymentAgent: address
        """
        return self._execute(self.chain, request_type, "16874b7e", [loanId, principalAmount, interestAmount, repaymentAgent], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def declareDefault(self, loanId: uint256, reasonHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#441)

        Args:
            loanId: uint256
            reasonHash: bytes32
        """
        ...

    @overload
    def declareDefault(self, loanId: uint256, reasonHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#441)

        Args:
            loanId: uint256
            reasonHash: bytes32
        """
        ...

    @overload
    def declareDefault(self, loanId: uint256, reasonHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#441)

        Args:
            loanId: uint256
            reasonHash: bytes32
        """
        ...

    @overload
    def declareDefault(self, loanId: uint256, reasonHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#441)

        Args:
            loanId: uint256
            reasonHash: bytes32
        """
        ...

    def declareDefault(self, loanId: uint256, reasonHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#441)

        Args:
            loanId: uint256
            reasonHash: bytes32
        """
        return self._execute(self.chain, request_type, "21c221d7", [loanId, reasonHash], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def writeOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#455)

        Args:
            loanId: uint256
        """
        ...

    @overload
    def writeOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#455)

        Args:
            loanId: uint256
        """
        ...

    @overload
    def writeOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#455)

        Args:
            loanId: uint256
        """
        ...

    @overload
    def writeOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#455)

        Args:
            loanId: uint256
        """
        ...

    def writeOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#455)

        Args:
            loanId: uint256
        """
        return self._execute(self.chain, request_type, "727df75c", [loanId], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def recoverLoan(self, loanId: uint256, amount: uint256, recoveryAgent: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#474)

        Args:
            loanId: uint256
            amount: uint256
            recoveryAgent: address
        """
        ...

    @overload
    def recoverLoan(self, loanId: uint256, amount: uint256, recoveryAgent: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#474)

        Args:
            loanId: uint256
            amount: uint256
            recoveryAgent: address
        """
        ...

    @overload
    def recoverLoan(self, loanId: uint256, amount: uint256, recoveryAgent: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#474)

        Args:
            loanId: uint256
            amount: uint256
            recoveryAgent: address
        """
        ...

    @overload
    def recoverLoan(self, loanId: uint256, amount: uint256, recoveryAgent: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#474)

        Args:
            loanId: uint256
            amount: uint256
            recoveryAgent: address
        """
        ...

    def recoverLoan(self, loanId: uint256, amount: uint256, recoveryAgent: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#474)

        Args:
            loanId: uint256
            amount: uint256
            recoveryAgent: address
        """
        return self._execute(self.chain, request_type, "48abb7e3", [loanId, amount, recoveryAgent], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setMaxOriginationFeeBps(self, _maxOriginationFeeBps: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#531)

        Args:
            _maxOriginationFeeBps: uint256
        """
        ...

    @overload
    def setMaxOriginationFeeBps(self, _maxOriginationFeeBps: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#531)

        Args:
            _maxOriginationFeeBps: uint256
        """
        ...

    @overload
    def setMaxOriginationFeeBps(self, _maxOriginationFeeBps: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#531)

        Args:
            _maxOriginationFeeBps: uint256
        """
        ...

    @overload
    def setMaxOriginationFeeBps(self, _maxOriginationFeeBps: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#531)

        Args:
            _maxOriginationFeeBps: uint256
        """
        ...

    def setMaxOriginationFeeBps(self, _maxOriginationFeeBps: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#531)

        Args:
            _maxOriginationFeeBps: uint256
        """
        return self._execute(self.chain, request_type, "2f45bc8e", [_maxOriginationFeeBps], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setWhitelistedOffRampingEntity(self, entity: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#537)

        Args:
            entity: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedOffRampingEntity(self, entity: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#537)

        Args:
            entity: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedOffRampingEntity(self, entity: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#537)

        Args:
            entity: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedOffRampingEntity(self, entity: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#537)

        Args:
            entity: address
            isWhitelisted: bool
        """
        ...

    def setWhitelistedOffRampingEntity(self, entity: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#537)

        Args:
            entity: address
            isWhitelisted: bool
        """
        return self._execute(self.chain, request_type, "304566c4", [entity, isWhitelisted], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setWhitelistedRecoveryAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#544)

        Args:
            agent: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedRecoveryAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#544)

        Args:
            agent: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedRecoveryAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#544)

        Args:
            agent: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedRecoveryAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#544)

        Args:
            agent: address
            isWhitelisted: bool
        """
        ...

    def setWhitelistedRecoveryAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#544)

        Args:
            agent: address
            isWhitelisted: bool
        """
        return self._execute(self.chain, request_type, "ee481455", [agent, isWhitelisted], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setWhitelistedRepaymentAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#551)

        Args:
            agent: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedRepaymentAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#551)

        Args:
            agent: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedRepaymentAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#551)

        Args:
            agent: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedRepaymentAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#551)

        Args:
            agent: address
            isWhitelisted: bool
        """
        ...

    def setWhitelistedRepaymentAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#551)

        Args:
            agent: address
            isWhitelisted: bool
        """
        return self._execute(self.chain, request_type, "19b52c21", [agent, isWhitelisted], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setWhitelistedFeeManager(self, manager: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#558)

        Args:
            manager: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedFeeManager(self, manager: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#558)

        Args:
            manager: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedFeeManager(self, manager: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#558)

        Args:
            manager: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedFeeManager(self, manager: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#558)

        Args:
            manager: address
            isWhitelisted: bool
        """
        ...

    def setWhitelistedFeeManager(self, manager: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#558)

        Args:
            manager: address
            isWhitelisted: bool
        """
        return self._execute(self.chain, request_type, "7e7761a4", [manager, isWhitelisted], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getMaxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#565)

        Returns:
            uint256
        """
        ...

    @overload
    def getMaxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#565)

        Returns:
            uint256
        """
        ...

    @overload
    def getMaxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#565)

        Returns:
            uint256
        """
        ...

    @overload
    def getMaxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#565)

        Returns:
            uint256
        """
        ...

    def getMaxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#565)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "6780f977", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getNextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#569)

        Returns:
            uint256
        """
        ...

    @overload
    def getNextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#569)

        Returns:
            uint256
        """
        ...

    @overload
    def getNextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#569)

        Returns:
            uint256
        """
        ...

    @overload
    def getNextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#569)

        Returns:
            uint256
        """
        ...

    def getNextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#569)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "6146dd6f", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getLoanDetails(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> LoanEngine.Loan:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#573)

        Args:
            loanId: uint256
        Returns:
            struct LoanEngine.Loan
        """
        ...

    @overload
    def getLoanDetails(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#573)

        Args:
            loanId: uint256
        Returns:
            struct LoanEngine.Loan
        """
        ...

    @overload
    def getLoanDetails(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#573)

        Args:
            loanId: uint256
        Returns:
            struct LoanEngine.Loan
        """
        ...

    @overload
    def getLoanDetails(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[LoanEngine.Loan]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#573)

        Args:
            loanId: uint256
        Returns:
            struct LoanEngine.Loan
        """
        ...

    def getLoanDetails(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[LoanEngine.Loan, TransactionAbc[LoanEngine.Loan], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#573)

        Args:
            loanId: uint256
        Returns:
            struct LoanEngine.Loan
        """
        return self._execute(self.chain, request_type, "66877b8d", [loanId], True if request_type == "tx" else False, LoanEngine.Loan, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

LoanEngine.creditPolicyContract.selector = bytes4(b'\xa7\xe3p\xb3')
LoanEngine.s_loans.selector = bytes4(b'\x91\xb5\xa9\xb6')
LoanEngine.s_originationFees.selector = bytes4(b'\xd7\xd5,\x9e')
LoanEngine.whitelistedOffRampingEntities.selector = bytes4(b'\xe5\xd2\xeeC')
LoanEngine.whitelistedRecoveryAgents.selector = bytes4(b'\\\xd1\xd6s')
LoanEngine.whitelistedRepaymentAgents.selector = bytes4(b'\xe6V\xfd\x8c')
LoanEngine.whitelistedFeeManagers.selector = bytes4(b'-c\xf3\xd4')
LoanEngine.s_nullifierHashes.selector = bytes4(b'e\x17J\xf8')
LoanEngine.s_nextLoanId.selector = bytes4(b'\x10\xc6\xb6j')
LoanEngine.s_maxOriginationFeeBps.selector = bytes4(b'\xefi\x7fk')
LoanEngine.s_stableCoinAddress.selector = bytes4(b'\xed\x0f6\x1b')
LoanEngine.STANDARD_BPS.selector = bytes4(b'\xe0m(\x93')
LoanEngine.createLoan.selector = bytes4(b'\xd67\x92\xa7')
LoanEngine.activateLoan.selector = bytes4(b'\x19\xe4\xbc\x11')
LoanEngine.repayLoan.selector = bytes4(b'\x16\x87K~')
LoanEngine.declareDefault.selector = bytes4(b'!\xc2!\xd7')
LoanEngine.writeOffLoan.selector = bytes4(b'r}\xf7\\')
LoanEngine.recoverLoan.selector = bytes4(b'H\xab\xb7\xe3')
LoanEngine.setMaxOriginationFeeBps.selector = bytes4(b'/E\xbc\x8e')
LoanEngine.setWhitelistedOffRampingEntity.selector = bytes4(b'0Ef\xc4')
LoanEngine.setWhitelistedRecoveryAgent.selector = bytes4(b'\xeeH\x14U')
LoanEngine.setWhitelistedRepaymentAgent.selector = bytes4(b'\x19\xb5,!')
LoanEngine.setWhitelistedFeeManager.selector = bytes4(b'~wa\xa4')
LoanEngine.getMaxOriginationFeeBps.selector = bytes4(b'g\x80\xf9w')
LoanEngine.getNextLoanId.selector = bytes4(b'aF\xddo')
LoanEngine.getLoanDetails.selector = bytes4(b'f\x87{\x8d')
