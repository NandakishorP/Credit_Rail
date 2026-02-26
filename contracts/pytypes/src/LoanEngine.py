
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.proxy.utils.Initializable import Initializable
from pytypes.lib.openzeppelincontracts.contracts.proxy.utils.UUPSUpgradeable import UUPSUpgradeable
from pytypes.lib.openzeppelincontracts.contracts.utils.ReentrancyGuard import ReentrancyGuard
from pytypes.lib.openzeppelincontractsupgradeable.contracts.access.AccessControlUpgradeable import AccessControlUpgradeable
from pytypes.lib.openzeppelincontractsupgradeable.contracts.utils.PausableUpgradeable import PausableUpgradeable
from pytypes.src.interfaces.ICreditPolicy import ICreditPolicy
from pytypes.src.interfaces.ILoanEngine import ILoanEngine
from pytypes.src.interfaces.IPoseidon2 import IPoseidon2
from pytypes.src.interfaces.ITranchePool import ITranchePool
from pytypes.src.interfaces.IVerifier import IVerifier



class LoanEngine(ILoanEngine, UUPSUpgradeable, PausableUpgradeable, ReentrancyGuard, AccessControlUpgradeable, Initializable):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#36)
    """
    _abi = {'constructor': {'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'f\x97\xb22': {'inputs': [], 'name': 'AccessControlBadConfirmation', 'type': 'error'}, b'\xe2Q}?': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'neededRole', 'type': 'bytes32'}], 'name': 'AccessControlUnauthorizedAccount', 'type': 'error'}, b'\x99\x96\xb3\x15': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'AddressEmptyCode', 'type': 'error'}, b'L\x9c\x8c\xe3': {'inputs': [{'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'ERC1967InvalidImplementation', 'type': 'error'}, b'\xb3\x98\x97\x9f': {'inputs': [], 'name': 'ERC1967NonPayable', 'type': 'error'}, b'\xd9<\x06e': {'inputs': [], 'name': 'EnforcedPause', 'type': 'error'}, b'\x8d\xfc +': {'inputs': [], 'name': 'ExpectedPause', 'type': 'error'}, b'\xd6\xbd\xa2u': {'inputs': [], 'name': 'FailedCall', 'type': 'error'}, b'\xf9.\xe8\xa9': {'inputs': [], 'name': 'InvalidInitialization', 'type': 'error'}, b'\xe8#\xe1\x9f': {'inputs': [{'internalType': 'uint256', 'name': 'policyVersion', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}], 'name': 'LoanEngine__IndustryExcluded', 'type': 'error'}, b'\xe3\x99\xa5\x89': {'inputs': [], 'name': 'LoanEngine__InsufficientPoolLiquidity', 'type': 'error'}, b'\x89\x04\xa3v': {'inputs': [{'internalType': 'address', 'name': 'manager', 'type': 'address'}], 'name': 'LoanEngine__InvalidFeeManagerEntity', 'type': 'error'}, b'7\x14tP': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'principalIssued', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'aprBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'termDays', 'type': 'uint256'}], 'name': 'LoanEngine__InvalidLoanParameters', 'type': 'error'}, b'\n\x82N-': {'inputs': [{'internalType': 'address', 'name': 'entity', 'type': 'address'}], 'name': 'LoanEngine__InvalidOffRampingEntity', 'type': 'error'}, b'\xe0w\x12\xed': {'inputs': [], 'name': 'LoanEngine__InvalidProof', 'type': 'error'}, b'\x9e\xe6_\xeb': {'inputs': [], 'name': 'LoanEngine__InvalidPublicInputs', 'type': 'error'}, b'\x0e\x16\xbe\xc0': {'inputs': [], 'name': 'LoanEngine__InvalidPublicInputsLength', 'type': 'error'}, b'CFU\x0e': {'inputs': [{'internalType': 'address', 'name': 'agent', 'type': 'address'}], 'name': 'LoanEngine__InvalidRecoveryAgent', 'type': 'error'}, b'\xe0\x90*\n': {'inputs': [], 'name': 'LoanEngine__InvalidRepayment', 'type': 'error'}, b'\xe8P\xfc\xdb': {'inputs': [{'internalType': 'address', 'name': 'agent', 'type': 'address'}], 'name': 'LoanEngine__InvalidRepaymentAgent', 'type': 'error'}, b'AU\x99\xc0': {'inputs': [], 'name': 'LoanEngine__InvalidUnderwriterKey', 'type': 'error'}, b'\x86\xdcI\xfc': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'LoanEngine__LoanExists', 'type': 'error'}, b'\x13\x90j\x9e': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'LoanEngine__LoanIsNotActive', 'type': 'error'}, b' \x93P\xad': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'LoanEngine__LoanIsNotDefaulted', 'type': 'error'}, b'\xf5\x85_2': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'LoanEngine__LoanIsNotInCreatedState', 'type': 'error'}, b'\xf8\x90@\x85': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'LoanEngine__LoanNotRecoverable', 'type': 'error'}, b'\xa9\x0e5o': {'inputs': [{'internalType': 'uint256', 'name': 'policyVersion', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}], 'name': 'LoanEngine__LoanTierIsNotInPolicy', 'type': 'error'}, b'\x9c\xcc\xf9\xc7': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'originationFeeBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxOriginationFeeBps', 'type': 'uint256'}], 'name': 'LoanEngine__MaxOriginationFeeExceeded', 'type': 'error'}, b'1s\x91\xc6': {'inputs': [{'internalType': 'uint256', 'name': 'policyVersion', 'type': 'uint256'}], 'name': 'LoanEngine__PolicyNotFrozen', 'type': 'error'}, b'h\xf6f\xad': {'inputs': [], 'name': 'LoanEngine__PoolNotDeployed', 'type': 'error'}, b'{L\x1bL': {'inputs': [], 'name': 'LoanEngine__ProofAlreadyUsed', 'type': 'error'}, b'O\x16\xf6\xa0': {'inputs': [{'internalType': 'uint256', 'name': 'proofTimestamp', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'currentTimestamp', 'type': 'uint256'}], 'name': 'LoanEngine__ProofExpired', 'type': 'error'}, b'\xbf\xaa3\x9e': {'inputs': [{'internalType': 'uint256', 'name': 'proofTimestamp', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'currentTimestamp', 'type': 'uint256'}], 'name': 'LoanEngine__ProofFromFuture', 'type': 'error'}, b'\xe5\x9dxy': {'inputs': [], 'name': 'LoanEngine__ZeroAddress', 'type': 'error'}, b'w\x00\xd1\x80': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'LoanEngine__ZeroLossOnWriteOff', 'type': 'error'}, b'\x01a[k': {'inputs': [], 'name': 'LoanEngine__ZeroRecovery', 'type': 'error'}, b'\xd7\xe6\xbc\xf8': {'inputs': [], 'name': 'NotInitializing', 'type': 'error'}, b'>\xe5\xae\xb5': {'inputs': [], 'name': 'ReentrancyGuardReentrantCall', 'type': 'error'}, b'Rt\xaf\xe7': {'inputs': [{'internalType': 'address', 'name': 'token', 'type': 'address'}], 'name': 'SafeERC20FailedOperation', 'type': 'error'}, b'\xe0|\x8d\xba': {'inputs': [], 'name': 'UUPSUnauthorizedCallContext', 'type': 'error'}, b'\xaa\x1dI\xa4': {'inputs': [{'internalType': 'bytes32', 'name': 'slot', 'type': 'bytes32'}], 'name': 'UUPSUnsupportedProxiableUUID', 'type': 'error'}, b'\xc7\xf5\x05\xb2\xf3q\xae!u\xeeI\x13\xf4I\x9e\x1f&3\xa7\xb5\x93c!\xee\xd1\xcd\xae\xb6\x11Q\x81\xd2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint64', 'name': 'version', 'type': 'uint64'}], 'name': 'Initialized', 'type': 'event'}, b'\x1a\x19\x0b)5\xd0\xfe\xac=Bs\xc05fBM\xa2\xabyrj\x06\xbblg\xd7\x11\xa5\xe7U\xe7\xd2': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'principalIssued', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'startTimestamp', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'maturityTimestamp', 'type': 'uint256'}], 'name': 'LoanActivated', 'type': 'event'}, b'\xfa\xf7\x89\xd2\x9e.\xacV\xfd\xd8\xf0L\xd3t\x14\xd6wQ\x15%\x9a\x9c\xfe\xd11\xd9\xce\xcf\x04\x16\x81\x93': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanClosed', 'type': 'event'}, b'\x9e\xbe\xaf\x9a\xd3(\xdftEq\xfe\x8f"\x9f%\xc1\xfe\xa3\x83\xa3g+\x1b\xabS\xe0\x85\x18\xeaA\xb0\xdf': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': True, 'internalType': 'bytes32', 'name': 'borrowerCommitment', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'principalIssued', 'type': 'uint256'}, {'indexed': True, 'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanCreated', 'type': 'event'}, b"\xc9\x19\xe7\x89\xb9\xf52\xc4\xa0s\x1f\xa1\x0b]Z\xf1\xcc\xb69\xd9M\x9c\x96\x8c\xc6#T5c'\x02}": {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': True, 'internalType': 'bytes32', 'name': 'reasonHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanDefaulted', 'type': 'event'}, b'\x83\x90\xc0\x9c\xcb\xcd\x8a\r\xadLD\xaf_\xd7\xfcRj\x0f]\xf7\xa0\xd2\xc32\xf5\xea\xca-\xa5\x17"W': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanRecovered', 'type': 'event'}, b'r\xd1E\x1cf\x1b\x05\xf1\x88l\x7f7J\x9a\xcb\xa5\xe4\xdf2Y\xb0\xfc\xc8\x1ed\x06`j\xbbV\x15$': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'principalRepaid', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'interestRepaid', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanRepaid', 'type': 'event'}, b'\xf7\xb19B\x1e\x94\xc5e\xac\xe7\xa7\xa3\xfc{\x03\xf5~\xc6\xfd\xfb\xa3\xb5>\x9f-\xb7\xb4\x86\x9f\x18\x18\x8a': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanWrittenOff', 'type': 'event'}, b':%#\x11\xd3\x13#\xf97\xfd\xb6\x97\x9a\x19\x90\xcff\xa6\xec\tVG\x81D\x8f\xfcv\xca\xe2O+M': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'newMaxFeeBps', 'type': 'uint256'}], 'name': 'MaxOriginationFeeBpsUpdated', 'type': 'event'}, b'b\xe7\x8c\xea\x01\xbe\xe3 \xcdNB\x02p\xb5\xeat\x00\r\x11\xb0\xc9\xf7GT\xeb\xdb\xfcTK\x05\xa2X': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'Paused', 'type': 'event'}, b'\xbdy\xb8o\xfe\n\xb8\xe8waQQB\x17\xcd|\xac\xd5,\x90\x9ffG\\:\xf4N\x12\x9f\x0b\x00\xff': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'role', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'bytes32', 'name': 'previousAdminRole', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'bytes32', 'name': 'newAdminRole', 'type': 'bytes32'}], 'name': 'RoleAdminChanged', 'type': 'event'}, b"/\x87\x88\x11~~\xff\x1d\x82\xe9&\xecyI\x01\xd1|x\x02JP'\t@0E@\xa73eo\r": {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'role', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'address', 'name': 'account', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'RoleGranted', 'type': 'event'}, b'\xf69\x1f\\2\xd9\xc6\x9d*G\xeag\x0bD)t\xb595\xd1\xed\xc7\xfdd\xeb!\xe0G\xa89\x17\x1b': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'role', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'address', 'name': 'account', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'RoleRevoked', 'type': 'event'}, b'\xc4e\xcc\xf7\xe4)\x83a\xae\xe1n\xdc\xd9\x18yn\x8b\xec\x81c\xf6\xc36SH\xb8\xa8\xfc\xad\x14\xd2>': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'keyHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'keyX', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'keyY', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'bool', 'name': 'isAuthorized', 'type': 'bool'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'UnderwriterAuthorizationUpdated', 'type': 'event'}, b']\xb9\xee\nI[\xf2\xe6\xff\x9c\x91\xa7\x83L\x1b\xa4\xfd\xd2D\xa5\xe8\xaaNS{\xd3\x8a\xea\xe4\xb0s\xaa': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'Unpaused', 'type': 'event'}, b'\xbc|\xd7Z \xee\'\xfd\x9a\xde\xba\xb3 A\xf7U!M\xbck\xff\xa9\x0c\xc0"[9\xda.\\-;': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'Upgraded', 'type': 'event'}, b'\x8c\xc6"\x9e\x9ep4\xab\xc8\x0cd\x10U\x7f\xcc\x97\x0b\xe1\xb8\x00\xe0\xf0w\xf7\xfb\x82FH\xcb\xc2\xb48': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'manager', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'isWhitelisted', 'type': 'bool'}], 'name': 'WhitelistedFeeManagerUpdated', 'type': 'event'}, b'\x00fZ4uN5\xd9\xe0\xf1\xe9\xef\x08\x82\xa2\xb1\xbb\xedZ\xf0\x1b\xbd\xe2C\x01\xc8\nZe\x92\r\t': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'entity', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'isWhitelisted', 'type': 'bool'}], 'name': 'WhitelistedOffRampingEntityUpdated', 'type': 'event'}, b"\xef\xbe\xda\xd4\xeb\xf9\x80\xaa\xf9'\xfe\x0f\x06l`\x1c%\xd6\xa40\xbd]\xad0\xa0\x007I\x90Y$,": {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'agent', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'isWhitelisted', 'type': 'bool'}], 'name': 'WhitelistedRecoveryAgentUpdated', 'type': 'event'}, b'\x0byt \xda$\xb4\xe5\x9a\x91\xf0\xc0m\xd2\x04\xae\x86\xe5B\x97\xea\x97\xc9U0\xfd\xc6\xfc\x04Y.\xc7': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'agent', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'isWhitelisted', 'type': 'bool'}], 'name': 'WhitelistedRepaymentAgentUpdated', 'type': 'event'}, b'\xc7\x8e\xf2\x8c': {'inputs': [], 'name': 'CONFIG_ADMIN_ROLE', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa2\x17\xfd\xdf': {'inputs': [], 'name': 'DEFAULT_ADMIN_ROLE', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'nv\xfc\x8f': {'inputs': [], 'name': 'EMERGENCY_ADMIN_ROLE', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'/\x83\xa6\xbc': {'inputs': [], 'name': 'FUND_MANAGER_ROLE', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\x97@\xadf': {'inputs': [], 'name': 'LOAN_HASH_INDEX', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x87\xa1\xb0\xa1': {'inputs': [], 'name': 'NULLIFIER_HASH_INDEX', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb1\x938\x02': {'inputs': [], 'name': 'POLICY_VERSION_HASH_INDEX', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x00\x05\xc4\xb3': {'inputs': [], 'name': 'PROOF_MAX_AGE', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'O\x16\xb4%': {'inputs': [], 'name': 'RISK_ADMIN_ROLE', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\t\xa0\x16\x08': {'inputs': [], 'name': 'SERVICER_ROLE', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b"\x96\x86'\xe0": {'inputs': [], 'name': 'TOTAL_PUBLIC_INPUTS', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xad<\xb1\xcc': {'inputs': [], 'name': 'UPGRADE_INTERFACE_VERSION', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x19\xe4\xbc\x11': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'receivingEntity', 'type': 'address'}, {'internalType': 'address', 'name': 'feeManager', 'type': 'address'}], 'name': 'activateLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'<6\xbf\r': {'inputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'authorizedUnderwriters', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x120\xa3e': {'inputs': [{'components': [{'internalType': 'bytes32', 'name': 'borrowerCommitment', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 'nullifierHash', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'policyVersion', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'principalIssued', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'aprBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'originationFeeBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'termDays', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 'underwriterKeyX', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 'underwriterKeyY', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'proofTimestamp', 'type': 'uint256'}], 'internalType': 'struct ILoanEngine.CreateLoanParams', 'name': 'params', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'proofData', 'type': 'bytes'}, {'internalType': 'bytes32[]', 'name': 'publicInputs', 'type': 'bytes32[]'}], 'name': 'createLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfa\xad\xdb\x94': {'inputs': [], 'name': 'creditPolicy', 'outputs': [{'internalType': 'contract ICreditPolicy', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa1\xa0j\x8c': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'reasonHash', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'declareDefault', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'f\x87{\x8d': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'getLoanDetails', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'borrowerCommitment', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'policyVersion', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'principalIssued', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'principalOutstanding', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'aprBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'originationFeeBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestAccrued', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestPaid', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lastAccrualTimestamp', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'startTimestamp', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maturityTimestamp', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'termDays', 'type': 'uint256'}, {'internalType': 'enum ILoanEngine.LoanState', 'name': 'state', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'totalRecovered', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'seniorPrincipalAllocated', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'juniorPrincipalAllocated', 'type': 'uint256'}], 'internalType': 'struct ILoanEngine.Loan', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, b'g\x80\xf9w': {'inputs': [], 'name': 'getMaxOriginationFeeBps', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'aF\xddo': {'inputs': [], 'name': 'getNextLoanId', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'$\x8a\x9c\xa3': {'inputs': [{'internalType': 'bytes32', 'name': 'role', 'type': 'bytes32'}], 'name': 'getRoleAdmin', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'//\xf1]': {'inputs': [{'internalType': 'bytes32', 'name': 'role', 'type': 'bytes32'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'grantRole', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x91\xd1HT': {'inputs': [{'internalType': 'bytes32', 'name': 'role', 'type': 'bytes32'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'hasRole', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'mBd\xfa': {'inputs': [], 'name': 'i_creditPolicy', 'outputs': [{'internalType': 'contract ICreditPolicy', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe9\xaf\x0b\xbb': {'inputs': [], 'name': 'i_loanProofVerifier', 'outputs': [{'internalType': 'contract IVerifier', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'm^\x93q': {'inputs': [], 'name': 'i_poseidon2', 'outputs': [{'internalType': 'contract IPoseidon2', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'_@\x7f\\': {'inputs': [], 'name': 'i_stableCoin', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'DH\xb39': {'inputs': [], 'name': 'i_tranchePool', 'outputs': [{'internalType': 'contract ITranchePool', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\x9e\x0b\xac\xa8': {'inputs': [{'internalType': 'address', 'name': '_creditPolicyContract', 'type': 'address'}, {'internalType': 'address', 'name': '_loanProofVerifier', 'type': 'address'}, {'internalType': 'uint256', 'name': '_maxOriginationFeeBps', 'type': 'uint256'}, {'internalType': 'address', 'name': '_tranchePool', 'type': 'address'}, {'internalType': 'address', 'name': '_stableCoinAddress', 'type': 'address'}, {'internalType': 'address', 'name': '_poseidon2', 'type': 'address'}, {'internalType': 'address', 'name': '_initialAdmin', 'type': 'address'}], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb5k\\)': {'inputs': [], 'name': 'loanProofVerifier', 'outputs': [{'internalType': 'contract IVerifier', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\x84V\xcbY': {'inputs': [], 'name': 'pause', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\\\x97Z\xbb': {'inputs': [], 'name': 'paused', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xca^\xe4\xb2': {'inputs': [], 'name': 'poseidon2', 'outputs': [{'internalType': 'contract IPoseidon2', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'R\xd1\x90-': {'inputs': [], 'name': 'proxiableUUID', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'H\xab\xb7\xe3': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'recoveryAgent', 'type': 'address'}], 'name': 'recoverLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'6V\x8a\xbe': {'inputs': [{'internalType': 'bytes32', 'name': 'role', 'type': 'bytes32'}, {'internalType': 'address', 'name': 'callerConfirmation', 'type': 'address'}], 'name': 'renounceRole', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf3\xe7\xc1N': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'principalAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestAmount', 'type': 'uint256'}, {'internalType': 'address', 'name': 'repaymentAgent', 'type': 'address'}, {'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'repayLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd5Gt\x1f': {'inputs': [{'internalType': 'bytes32', 'name': 'role', 'type': 'bytes32'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'revokeRole', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x91\xb5\xa9\xb6': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 's_loans', 'outputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'borrowerCommitment', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'policyVersion', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'principalIssued', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'principalOutstanding', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'aprBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'originationFeeBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestAccrued', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestPaid', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lastAccrualTimestamp', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'startTimestamp', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maturityTimestamp', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'termDays', 'type': 'uint256'}, {'internalType': 'enum ILoanEngine.LoanState', 'name': 'state', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'totalRecovered', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'seniorPrincipalAllocated', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'juniorPrincipalAllocated', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xefi\x7fk': {'inputs': [], 'name': 's_maxOriginationFeeBps', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x10\xc6\xb6j': {'inputs': [], 'name': 's_nextLoanId', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'e\x17J\xf8': {'inputs': [{'internalType': 'bytes32', 'name': 'nullifierHash', 'type': 'bytes32'}], 'name': 's_nullifierHashes', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd7\xd5,\x9e': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 's_originationFees', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'/E\xbc\x8e': {'inputs': [{'internalType': 'uint256', 'name': '_maxOriginationFeeBps', 'type': 'uint256'}], 'name': 'setMaxOriginationFeeBps', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'shzd': {'inputs': [{'internalType': 'bytes32', 'name': 'keyX', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 'keyY', 'type': 'bytes32'}, {'internalType': 'bool', 'name': 'isAuthorized', 'type': 'bool'}], 'name': 'setUnderwriterAuthorization', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'~wa\xa4': {'inputs': [{'internalType': 'address', 'name': 'manager', 'type': 'address'}, {'internalType': 'bool', 'name': 'isWhitelisted', 'type': 'bool'}], 'name': 'setWhitelistedFeeManager', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'0Ef\xc4': {'inputs': [{'internalType': 'address', 'name': 'entity', 'type': 'address'}, {'internalType': 'bool', 'name': 'isWhitelisted', 'type': 'bool'}], 'name': 'setWhitelistedOffRampingEntity', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xeeH\x14U': {'inputs': [{'internalType': 'address', 'name': 'agent', 'type': 'address'}, {'internalType': 'bool', 'name': 'isWhitelisted', 'type': 'bool'}], 'name': 'setWhitelistedRecoveryAgent', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x19\xb5,!': {'inputs': [{'internalType': 'address', 'name': 'agent', 'type': 'address'}, {'internalType': 'bool', 'name': 'isWhitelisted', 'type': 'bool'}], 'name': 'setWhitelistedRepaymentAgent', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x99&B\xe5': {'inputs': [], 'name': 'stableCoin', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\x01\xff\xc9\xa7': {'inputs': [{'internalType': 'bytes4', 'name': 'interfaceId', 'type': 'bytes4'}], 'name': 'supportsInterface', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'}\xf0\xa8\x06': {'inputs': [], 'name': 'tranchePool', 'outputs': [{'internalType': 'contract ITranchePool', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'?K\xa8:': {'inputs': [], 'name': 'unpause', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'O\x1e\xf2\x86': {'inputs': [{'internalType': 'address', 'name': 'newImplementation', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'upgradeToAndCall', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, b'-c\xf3\xd4': {'inputs': [{'internalType': 'address', 'name': 'whiteListedFeeManager', 'type': 'address'}], 'name': 'whitelistedFeeManagers', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe5\xd2\xeeC': {'inputs': [{'internalType': 'address', 'name': 'whitelistedOffRampingEntity', 'type': 'address'}], 'name': 'whitelistedOffRampingEntities', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\\\xd1\xd6s': {'inputs': [{'internalType': 'address', 'name': 'whiteListedRecoveryAgent', 'type': 'address'}], 'name': 'whitelistedRecoveryAgents', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe6V\xfd\x8c': {'inputs': [{'internalType': 'address', 'name': 'whiteListedRepaymentAgent', 'type': 'address'}], 'name': 'whitelistedRepaymentAgents', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'r}\xf7\\': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'writeOffLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":8914,"contract":"src/LoanEngine.sol:LoanEngine","label":"i_creditPolicy","offset":0,"slot":0,"type":"t_contract(ICreditPolicy)14450"},{"astId":8917,"contract":"src/LoanEngine.sol:LoanEngine","label":"i_loanProofVerifier","offset":0,"slot":1,"type":"t_contract(IVerifier)15332"},{"astId":8920,"contract":"src/LoanEngine.sol:LoanEngine","label":"i_tranchePool","offset":0,"slot":2,"type":"t_contract(ITranchePool)15319"},{"astId":8925,"contract":"src/LoanEngine.sol:LoanEngine","label":"s_loans","offset":0,"slot":3,"type":"t_mapping(t_uint256,t_struct(Loan)14706_storage)"},{"astId":8929,"contract":"src/LoanEngine.sol:LoanEngine","label":"s_originationFees","offset":0,"slot":4,"type":"t_mapping(t_uint256,t_uint256)"},{"astId":8933,"contract":"src/LoanEngine.sol:LoanEngine","label":"whitelistedOffRampingEntities","offset":0,"slot":5,"type":"t_mapping(t_address,t_bool)"},{"astId":8937,"contract":"src/LoanEngine.sol:LoanEngine","label":"whitelistedRecoveryAgents","offset":0,"slot":6,"type":"t_mapping(t_address,t_bool)"},{"astId":8941,"contract":"src/LoanEngine.sol:LoanEngine","label":"whitelistedRepaymentAgents","offset":0,"slot":7,"type":"t_mapping(t_address,t_bool)"},{"astId":8945,"contract":"src/LoanEngine.sol:LoanEngine","label":"whitelistedFeeManagers","offset":0,"slot":8,"type":"t_mapping(t_address,t_bool)"},{"astId":8949,"contract":"src/LoanEngine.sol:LoanEngine","label":"s_nullifierHashes","offset":0,"slot":9,"type":"t_mapping(t_bytes32,t_bool)"},{"astId":8952,"contract":"src/LoanEngine.sol:LoanEngine","label":"s_nextLoanId","offset":0,"slot":10,"type":"t_uint256"},{"astId":8954,"contract":"src/LoanEngine.sol:LoanEngine","label":"s_maxOriginationFeeBps","offset":0,"slot":11,"type":"t_uint256"},{"astId":8956,"contract":"src/LoanEngine.sol:LoanEngine","label":"i_stableCoin","offset":0,"slot":12,"type":"t_address"},{"astId":8960,"contract":"src/LoanEngine.sol:LoanEngine","label":"authorizedUnderwriters","offset":0,"slot":13,"type":"t_mapping(t_bytes32,t_bool)"},{"astId":8966,"contract":"src/LoanEngine.sol:LoanEngine","label":"i_poseidon2","offset":0,"slot":14,"type":"t_contract(IPoseidon2)14907"},{"astId":10546,"contract":"src/LoanEngine.sol:LoanEngine","label":"__gap","offset":0,"slot":15,"type":"t_array(t_uint256)50_storage"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_uint256)50_storage":{"encoding":"inplace","label":"uint256[50]","numberOfBytes":1600,"base":"t_uint256"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_contract(ICreditPolicy)14450":{"encoding":"inplace","label":"contract ICreditPolicy","numberOfBytes":20},"t_contract(IPoseidon2)14907":{"encoding":"inplace","label":"contract IPoseidon2","numberOfBytes":20},"t_contract(ITranchePool)15319":{"encoding":"inplace","label":"contract ITranchePool","numberOfBytes":20},"t_contract(IVerifier)15332":{"encoding":"inplace","label":"contract IVerifier","numberOfBytes":20},"t_enum(LoanState)14668":{"encoding":"inplace","label":"enum ILoanEngine.LoanState","numberOfBytes":1},"t_mapping(t_address,t_bool)":{"encoding":"mapping","label":"mapping(address => bool)","numberOfBytes":32,"key":"t_address","value":"t_bool"},"t_mapping(t_bytes32,t_bool)":{"encoding":"mapping","label":"mapping(bytes32 => bool)","numberOfBytes":32,"key":"t_bytes32","value":"t_bool"},"t_mapping(t_uint256,t_struct(Loan)14706_storage)":{"encoding":"mapping","label":"mapping(uint256 => struct ILoanEngine.Loan)","numberOfBytes":32,"key":"t_uint256","value":"t_struct(Loan)14706_storage"},"t_mapping(t_uint256,t_uint256)":{"encoding":"mapping","label":"mapping(uint256 => uint256)","numberOfBytes":32,"key":"t_uint256","value":"t_uint256"},"t_struct(Loan)14706_storage":{"encoding":"inplace","label":"struct ILoanEngine.Loan","numberOfBytes":576,"members":[{"astId":14670,"contract":"src/LoanEngine.sol:LoanEngine","label":"loanId","offset":0,"slot":0,"type":"t_uint256"},{"astId":14672,"contract":"src/LoanEngine.sol:LoanEngine","label":"borrowerCommitment","offset":0,"slot":1,"type":"t_bytes32"},{"astId":14674,"contract":"src/LoanEngine.sol:LoanEngine","label":"policyVersion","offset":0,"slot":2,"type":"t_uint256"},{"astId":14676,"contract":"src/LoanEngine.sol:LoanEngine","label":"tierId","offset":0,"slot":3,"type":"t_uint8"},{"astId":14678,"contract":"src/LoanEngine.sol:LoanEngine","label":"principalIssued","offset":0,"slot":4,"type":"t_uint256"},{"astId":14680,"contract":"src/LoanEngine.sol:LoanEngine","label":"principalOutstanding","offset":0,"slot":5,"type":"t_uint256"},{"astId":14682,"contract":"src/LoanEngine.sol:LoanEngine","label":"aprBps","offset":0,"slot":6,"type":"t_uint256"},{"astId":14684,"contract":"src/LoanEngine.sol:LoanEngine","label":"originationFeeBps","offset":0,"slot":7,"type":"t_uint256"},{"astId":14686,"contract":"src/LoanEngine.sol:LoanEngine","label":"interestAccrued","offset":0,"slot":8,"type":"t_uint256"},{"astId":14688,"contract":"src/LoanEngine.sol:LoanEngine","label":"interestPaid","offset":0,"slot":9,"type":"t_uint256"},{"astId":14690,"contract":"src/LoanEngine.sol:LoanEngine","label":"lastAccrualTimestamp","offset":0,"slot":10,"type":"t_uint256"},{"astId":14692,"contract":"src/LoanEngine.sol:LoanEngine","label":"startTimestamp","offset":0,"slot":11,"type":"t_uint256"},{"astId":14694,"contract":"src/LoanEngine.sol:LoanEngine","label":"maturityTimestamp","offset":0,"slot":12,"type":"t_uint256"},{"astId":14696,"contract":"src/LoanEngine.sol:LoanEngine","label":"termDays","offset":0,"slot":13,"type":"t_uint256"},{"astId":14699,"contract":"src/LoanEngine.sol:LoanEngine","label":"state","offset":0,"slot":14,"type":"t_enum(LoanState)14668"},{"astId":14701,"contract":"src/LoanEngine.sol:LoanEngine","label":"totalRecovered","offset":0,"slot":15,"type":"t_uint256"},{"astId":14703,"contract":"src/LoanEngine.sol:LoanEngine","label":"seniorPrincipalAllocated","offset":0,"slot":16,"type":"t_uint256"},{"astId":14705,"contract":"src/LoanEngine.sol:LoanEngine","label":"juniorPrincipalAllocated","offset":0,"slot":17,"type":"t_uint256"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32},"t_uint8":{"encoding":"inplace","label":"uint8","numberOfBytes":1}}}
    _creation_code = "60a080604052346100eb5760017f9b779b17422d0df92223018b32b4d1fa46e071723d6817e2486d003becc55f0055306080526001600a555f5160206136955f395f51905f525460ff8160401c166100dc576002600160401b03196001600160401b03821601610089575b6040516135a590816100f082396080518181816113f901526114d50152f35b6001600160401b0319166001600160401b039081175f5160206136955f395f51905f525581527fc7f505b2f371ae2175ee4913f4499e1f2633a7b5936321eed1cdaeb6115181d290602090a15f8061006a565b63f92ee8a960e01b5f5260045ffd5b5f80fdfe610100806040526004361015610013575f80fd5b5f905f3560e01c90816205c4b3146129c15750806301ffc9a71461296b57806309a016081461294457806310c6b66a146129275780631230a36514611e6e57806319b52c2114611df057806319e4bc1114611b16578063248a9ca314611af05780632d63f3d414611ab35780632f2ff15d14611a825780632f45bc8e14611a365780632f83a6bc14611a0f578063304566c41461197857806336568abe146119325780633c36bf0d146119035780633f4ba83a146118855780634448b3391461185d57806348abb7e3146116e25780634f16b425146116ba5780634f1ef2861461144d57806352d1902d146113e65780635c975abb146113b75780635cd1d673146113785780635f407f5c14610b725780636146dd6f1461135a57806365174af81461132b57806366877b8d146110cc5780636780f977146105615780636d4264fa146110a55780636d5e9371146107255780636e76fc8f1461107d578063727df75c14610f4357806373687a6414610e935780637df0a80614610e6a5780637e7761a414610deb5780638456cb5914610d7857806387a1b0a114610d5c57806391b5a9b614610c2957806391d1485414610bd3578063968627e014610bb75780639740ad6614610b9b578063992642e514610b725780639e0baca8146108a8578063a1a06a8c146107ee578063a217fddf14610776578063ad3cb1cc14610792578063b193380214610776578063b56b5c2914610619578063c78ef28c1461074e578063ca5ee4b214610725578063d547741f146106ea578063d7d52c9e146106c0578063e5d2ee4314610681578063e656fd8c14610642578063e9af0bbb14610619578063ee4814551461057f578063ef697f6b14610561578063f3e7c14e146102d05763faaddb94146102a7575f80fd5b346102cd57806003193601126102cd57546040516001600160a01b039091168152602090f35b80fd5b50346102cd5760a03660031901126102cd576004356102ed612a1d565b608435906102f9612b5c565b6001600160a01b0381168085526007602052604085205460ff161561054f5750610321612ca4565b828452600360205260408420600e81019060ff825416600681101561053b5760020361052757610355604435602435612ae8565b928315610518579061038a846103ac959493610371888a6131b7565b600c546002546001600160a01b03908116929116613125565b600881018054600583018054919492908587111561050e578597888098612ac8565b838111156104ff57506103cc6103c484998a98612ac8565b988994612ac8565b92839255600985016103df888254612ae8565b9055551594856104f6575b50846104e5575b5060025487906001600160a01b0316803b156104e15781809160446040518094819363271a61a160e21b83528960048401528a60248401525af180156104d6576104bd575b50507f72d1451c661b05f1886c7f374a9acba5e4df3259b0fcc81e6406606abb5615249160609154936040519182526020820152856040820152a261048b575b8260015f5160206134d05f395f51905f525580f35b60207ffaf789d29e2eac56fdd8f04cd37414d6775115259a9cfed131d9cecf0416819391604051908152a25f80610476565b816104c791612a72565b6104d257865f610436565b8680fd5b6040513d84823e3d90fd5b5080fd5b805460ff191660031790555f6103f1565b1594505f6103ea565b6103c46103cc91998a98612ac8565b8697888098612ac8565b637048150560e11b8752600487fd5b6309c8354f60e11b86526004859052602486fd5b634e487b7160e01b87526021600452602487fd5b63e850fcdb60e01b8552600452602484fd5b50346102cd57806003193601126102cd576020600b54604051908152f35b50346102cd5760403660031901126102cd576105996129db565b6105a1612a33565b906105aa612b13565b6001600160a01b031690811561060a5760207fefbedad4ebf980aaf927fe0f066c601c25d6a430bd5dad30a00037499059242c91838552600682526105fe81604087209060ff801983541691151516179055565b6040519015158152a280f35b63e59d787960e01b8352600483fd5b50346102cd57806003193601126102cd576001546040516001600160a01b039091168152602090f35b50346102cd5760203660031901126102cd5760209060ff906040906001600160a01b0361066d6129db565b168152600784522054166040519015158152f35b50346102cd5760203660031901126102cd5760209060ff906040906001600160a01b036106ac6129db565b168152600584522054166040519015158152f35b50346102cd5760203660031901126102cd5760406020916004358152600483522054604051908152f35b50346102cd5760403660031901126102cd5761072160043561070a6129f1565b9061071c61071782612af5565b612c37565b613089565b5080f35b50346102cd57806003193601126102cd57600e546040516001600160a01b039091168152602090f35b50346102cd57806003193601126102cd5760206040515f5160206133d05f395f51905f528152f35b50346102cd57806003193601126102cd57602090604051908152f35b50346102cd57806003193601126102cd57604080516107b18282612a72565b6005815260208101640352e302e360dc1b81528251938492602084525180928160208601528585015e828201840152601f01601f19168101030190f35b50346102cd5760603660031901126102cd5760443560043561080e612bee565b610816612c7d565b8083526003602052600e604084200160ff8154166006811015610894576002036108805761084483836131b7565b600460ff198254161790556040519182527fc919e789b9f532c4a0731fa10b5d5af1ccb639d94d9c968cc62354356327027d602060243593a380f35b6309c8354f60e11b84526004829052602484fd5b634e487b7160e01b85526021600452602485fd5b50346102cd5760e03660031901126102cd576108c26129db565b906108cb6129f1565b916044356108d7612a1d565b6084356001600160a01b03811690819003610b6e5760a4356001600160a01b0381169290839003610b6a5760c435936001600160a01b03851691828603610b66575f5160206135105f395f51905f52549660ff8860401c1615976001600160401b03811680159081610b5e575b6001149081610b54575b159081610b4b575b50610b3c5767ffffffffffffffff1981166001175f5160206135105f395f51905f525588610b10575b506001600160a01b0316988915610b01576001600160a01b0316908115610b01576001600160a01b0316928315610b01578415610b01578515610b015715610af2576127108211610ac857610a6d9697986109d8613298565b6109e0613298565b60018060a01b03198a541617895560018060a01b03196001541617600155600b5560018060a01b0319600254161760025560018060a01b0319600c541617600c5560018060a01b0319600e541617600e556001600a55610a3f81612cdc565b50610a4981612d78565b50610a5381612df8565b50610a5d81612e78565b50610a6781612ef8565b50612f78565b50610a755780f35b60ff60401b195f5160206135105f395f51905f5254165f5160206135105f395f51905f52557fc7f505b2f371ae2175ee4913f4499e1f2633a7b5936321eed1cdaeb6115181d2602060405160018152a180f35b6084828960405191630371474560e41b835281600484015281602484015260448301526064820152fd5b63e59d787960e01b8852600488fd5b63e59d787960e01b8952600489fd5b68ffffffffffffffffff191668010000000000000001175f5160206135105f395f51905f52555f61097f565b63f92ee8a960e01b8a5260048afd5b9050155f610956565b303b15915061094e565b8a9150610944565b8780fd5b8580fd5b8480fd5b50346102cd57806003193601126102cd57600c546040516001600160a01b039091168152602090f35b50346102cd57806003193601126102cd57602060405160018152f35b50346102cd57806003193601126102cd57602060405160038152f35b50346102cd5760403660031901126102cd576040610bef6129f1565b9160043581525f5160206134705f395f51905f52602052209060018060a01b03165f52602052602060ff60405f2054166040519015158152f35b50346102cd5760203660031901126102cd57600435815260036020526040902080808054600182015460e0526002820154600383015460ff16600484015460058501546006860154600787015490600888015492600989015494600a8a015496600b8b015498600c8c01549a600d8d01549c600e015460ff169d600f01549e60108101546080526011015460c05260405160a05260a0515260e05160a0516020015260a0516040015260a0516060015260a0516080015260a05160a0015260a05160c0015260a05160e0015260a051610100015260a051610120015260a051610140015260a051610160015260a051610180015260a0516101a0015260a0516101c001610d3591612a93565b60a0516101e0015260805160a051610200015260c05160a051610220015260a05161024090f35b50346102cd57806003193601126102cd57602060405160028152f35b50346102cd57806003193601126102cd57610d91612ba5565b610d99612c7d565b600160ff195f5160206134b05f395f51905f525416175f5160206134b05f395f51905f52557f62e78cea01bee320cd4e420270b5ea74000d11b0c9f74754ebdbfc544b05a2586020604051338152a180f35b50346102cd5760403660031901126102cd57610e056129db565b610e0d612a33565b90610e16612b13565b6001600160a01b031690811561060a5760207f8cc6229e9e7034abc80c6410557fcc970be1b800e0f077f7fb824648cbc2b43891838552600882526105fe81604087209060ff801983541691151516179055565b50346102cd57806003193601126102cd576002546040516001600160a01b039091168152602090f35b50346102cd5760603660031901126102cd57604435801515602435600435828403610b6e577fc465ccf7e4298361aee16edcd918796e8bec8163f6c3365348b8a8fcad14d23e92608092610ee5612b13565b610f29604051602081019085825283604082015260408152610f08606082612a72565b51902096878952600d602052604089209060ff801983541691151516179055565b60405192835260208301526040820152426060820152a280f35b50346102cd5760203660031901126102cd5760043590610f61612bee565b610f69612c7d565b81815260036020526040812091600e83019260ff84541660068110156110695760040361105557600581019060088254910194855492821561104257948096818096975555600560ff1982541617905560018060a01b036002541691823b1561103e57604484928360405195869485936396fd07ed60e01b8552600485015260248401525af180156104d657611029575b50507ff7b139421e94c565ace7a7a3fc7b03f57ec6fdfba3b53e9f2db7b4869f18188a6020604051428152a280f35b8161103391612a72565b6104e157815f610ffa565b8380fd5b62ee01a360e71b86526004859052602486fd5b63209350ad60e01b83526004829052602483fd5b634e487b7160e01b84526021600452602484fd5b50346102cd57806003193601126102cd5760206040515f5160206135305f395f51905f528152f35b50346102cd57806003193601126102cd57546040516001600160a01b039091168152602090f35b50346102cd5760203660031901126102cd57806102206040516110ee81612a42565b8281528260208201528260408201528260608201528260808201528260a08201528260c08201528260e08201528261010082015282610120820152826101408201528261016082015282610180820152826101a0820152826101c0820152826101e08201528261020082015201526004358152600360205260408120906040519061117882612a42565b82548252600183015460208301526002830154604083015260ff600384015416606083015260048301546080830152600583015460a0830152600683015460c0830152600783015460e083015260088301546101008301526009830154610120830152600a830154610140830152600b830154610160830152600c830154610180830152600d8301546101a083015260ff600e840154169060068210156113175750610240926011916101c0840152600f8101546101e0840152601081015461020084015201546102208201526102206040519180518352602081015160208401526040810151604084015260ff60608201511660608401526080810151608084015260a081015160a084015260c081015160c084015260e081015160e08401526101008101516101008401526101208101516101208401526101408101516101408401526101608101516101608401526101808101516101808401526101a08101516101a08401526112f56101c08201516101c0850190612a93565b6101e08101516101e08401526102008101516102008401520151610220820152f35b634e487b7160e01b81526021600452602490fd5b50346102cd5760203660031901126102cd5760ff60406020926004358152600984522054166040519015158152f35b50346102cd57806003193601126102cd576020600a54604051908152f35b50346102cd5760203660031901126102cd5760209060ff906040906001600160a01b036113a36129db565b168152600684522054166040519015158152f35b50346102cd57806003193601126102cd57602060ff5f5160206134b05f395f51905f5254166040519015158152f35b50346102cd57806003193601126102cd577f00000000000000000000000000000000000000000000000000000000000000006001600160a01b0316300361143e5760206040515f5160206133f05f395f51905f528152f35b63703e46dd60e11b8152600490fd5b5060403660031901126102cd576114626129db565b90602435916001600160401b0383116104e157366023840112156104e15782600401356001600160401b0381116116a657604051936114ab601f8301601f191660200186612a72565b818552366024838301011161103e5781849260246020930183880137850101526001600160a01b037f000000000000000000000000000000000000000000000000000000000000000016308114908115611684575b50611675578180525f5160206134705f395f51905f5260209081526040808420335f908152925290205460ff161561165d576040516352d1902d60e01b8152926001600160a01b0382169190602085600481865afa80958596611625575b5061157757634c9c8ce360e01b84526004839052602484fd5b9091845f5160206133f05f395f51905f5281036116135750823b15611601575f5160206133f05f395f51905f5280546001600160a01b031916821790557fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b8480a28051156115e857610721916132c3565b5050346115f25780f35b63b398979f60e01b8152600490fd5b634c9c8ce360e01b8452600452602483fd5b632a87526960e21b8552600452602484fd5b9095506020813d602011611655575b8161164160209383612a72565b810103126116515751945f61155e565b5f80fd5b3d9150611634565b63e2517d3f60e01b8252336004526024829052604482fd5b63703e46dd60e11b8252600482fd5b5f5160206133f05f395f51905f52546001600160a01b0316141590505f611500565b634e487b7160e01b83526041600452602483fd5b50346102cd57806003193601126102cd5760206040515f5160206133905f395f51905f528152f35b503461165157606036600319011261165157600435602435611702612a07565b61170a612b5c565b6001600160a01b0381165f8181526006602052604090205460ff161561184b5750825f52600360205260405f2060ff600e820154166006811015611837576005036118245782156118155761178491600f849201611769838254612ae8565b9055600c546002546001600160a01b03908116929116613125565b6002546001600160a01b0316803b15611651575f80916024604051809481936325574bd360e11b83528760048401525af1801561180a576117f4575b5060407f8390c09ccbcd8a0dad4c44af5fd7fc526a0f5df7a0d2c332f5eaca2da5172257918151908152426020820152a280f35b6118019193505f90612a72565b5f9160406117c0565b6040513d5f823e3d90fd5b6301615b6b60e01b5f5260045ffd5b8363f890408560e01b5f5260045260245ffd5b634e487b7160e01b5f52602160045260245ffd5b6321a32a8760e11b5f5260045260245ffd5b34611651575f366003190112611651576002546040516001600160a01b039091168152602090f35b34611651575f3660031901126116515761189d612ba5565b5f5160206134b05f395f51905f525460ff8116156118f45760ff19165f5160206134b05f395f51905f52557f5db9ee0a495bf2e6ff9c91a7834c1ba4fdd244a5e8aa4e537bd38aeae4b073aa6020604051338152a1005b638dfc202b60e01b5f5260045ffd5b34611651576020366003190112611651576004355f52600d602052602060ff60405f2054166040519015158152f35b346116515760403660031901126116515761194b6129f1565b336001600160a01b038216036119695761196790600435613089565b005b63334bd91960e11b5f5260045ffd5b34611651576040366003190112611651576119916129db565b611999612a33565b906119a2612b13565b6001600160a01b0316908115611a005760207e665a34754e35d9e0f1e9ef0882a2b1bbed5af01bbde24301c80a5a65920d0991835f52600582526119f58160405f209060ff801983541691151516179055565b6040519015158152a2005b63e59d787960e01b5f5260045ffd5b34611651575f3660031901126116515760206040515f5160206134305f395f51905f528152f35b34611651576020366003190112611651577f3a252311d31323f937fdb6979a1990cf66a6ec09564781448ffc76cae24f2b4d6020600435611a75612b13565b80600b55604051908152a1005b3461165157604036600319011261165157611967600435611aa16129f1565b90611aae61071782612af5565b612ff8565b34611651576020366003190112611651576001600160a01b03611ad46129db565b165f526008602052602060ff60405f2054166040519015158152f35b34611651576020366003190112611651576020611b0e600435612af5565b604051908152f35b3461165157606036600319011261165157600435611b326129f1565b611b3a612a07565b90611b43612b5c565b6001600160a01b03165f8181526005602052604090205490919060ff1615611ddd576001600160a01b03165f8181526008602052604090205460ff1615611dcb57611b8c612ca4565b611b94612c7d565b825f52600360205260405f20600e81019160ff835416600681101561183757600103611db85760048201549485600584015542600a84015542600b840155600d83015462015180810290808204620151801490151715611da457611bf89042612ae8565b9384600c850155600260ff19825416179055612710611c1b600785015488612ad5565b04905f5260046020528060405f205560018060a01b036002541660405163b3d814f560e01b8152602081600481855afa90811561180a575f91611d72575b508711611d63576060925f608492611c71858b612ac8565b92604051998a968795631ef894cd60e21b875260048701526024860152604485015260648401525af1801561180a575f5f91611d09575b6010830155601182015554604080519485524260208601819052908501526060840191909152917f1a190b2935d0feac3d4273c03566424da2ab79726a06bb6c67d711a5e755e7d29150608090a260015f5160206134d05f395f51905f5255005b50506060833d606011611d5b575b81611d2460609383612a72565b81010312611651578260207f1a190b2935d0feac3d4273c03566424da2ab79726a06bb6c67d711a5e755e7d2945191015190611ca8565b3d9150611d17565b63e399a58960e01b5f5260045ffd5b90506020813d602011611d9c575b81611d8d60209383612a72565b81010312611651575188611c59565b3d9150611d80565b634e487b7160e01b5f52601160045260245ffd5b84637ac2af9960e11b5f5260045260245ffd5b63448251bb60e11b5f5260045260245ffd5b50630a824e2d60e01b5f5260045260245ffd5b3461165157604036600319011261165157611e096129db565b611e11612a33565b90611e1a612b13565b6001600160a01b0316908115611a005760207f0b797420da24b4e59a91f0c06dd204ae86e54297ea97c95530fdc6fc04592ec791835f52600782526119f58160405f209060ff801983541691151516179055565b346116515736600319016101c08112611651576101801361165157610184356001600160401b0381116116515736602382011215611651578060040135906001600160401b038211611651573660248383010111611651576101a435906001600160401b0382116116515736602383011215611651578160040135916001600160401b03831161165157602481018360051b91366024848301011161165157335f9081525f5160206134505f395f51905f52602052604090205460ff161561290357611f38612c7d565b600385036128f55760025460405163217ac23760e01b81526001600160a01b039091169290602081600481875afa90811561180a575f916128ba575b50600481101561183757600281141590816128ae575b5061289f5760018060a01b035f54169360443595604051634c2d62b760e01b81528760048201526020816024818a5afa90811561180a575f91612880575b501561286d576101043592604051637d27ad4360e11b81528860048201528460248201526020816044818b5afa90811561180a575f9161284e575b5061283757612010612ab8565b60ff60405191631259673760e21b83528a60048401521660248201526020816044818b5afa90811561180a575f91612818575b50156127f65760243596875f52600960205260ff60405f2054166127e757891561270457602060249160405192838092638055c5a960e01b82528d60048301525afa90811561180a575f916127b5575b508135036126f557886002101561270457866064860135036126f5576101243592610144359a60405160208101908682528d6040820152604081526120d9606082612a72565b5190205f52600d60205260ff60405f205416156127a6575f5160206134105f395f51905f529a61018098604051966121118b89612a72565b600b88526020880190601f198c013683376004359e8f101561276557885115612704578e82525f5160206134105f395f51905f52811015612765578851600110156127045760408901525f5160206134105f395f51905f528f101561276557875160021015612704575f5160206134105f395f51905f529e606089015260ff612198612ab8565b169e8f101561276557875160031015612704575f5160206134105f395f51905f529e60808901526084359e8f101561276557875160041015612704578e60a089015260a435995f5160206134105f395f51905f528b101561276557885160051015612704578a60c08a015260c435985f5160206134105f395f51905f528a101561276557805160061015612704578960e082015260e4359a5f5160206134105f395f51905f528c101561276557815160071015612704578b6101008301525f5160206134105f395f51905f52811015612765578151600810156127045761012082015261016435915f5160206134105f395f51905f52831015612765578151600910156127045782610140830152600a54935f5160206134105f395f51905f52851015612765578251600a1015612704576101608301859052600e546040516340ec6e4960e01b8152602060048201529351602485018190526001600160a01b039091169184916044830191905f5b81811061274c5750505091818060209403915afa91821561180a575f92612718575b5085600110156127045760440135036126f5574281116126df57610e106123508242612ac8565b116126c957508e1580156126c1575b80156126b9575b61268a57600b549081891161267057505060206004916040519283809263b3d814f560e01b82525afa90811561180a575f9161263e575b508d11611d635760018060a01b03600154169180602460405197633a94343960e21b8952604060048a01528260448a01520160648801375f60648288010152601f801991011685019060031960648784030101602487015280606483015260018060fb1b0310611651575f602086606486858398859a60848699013701010301925af190811561180a575f9161260f575b501561260057600a549260ff612442612ab8565b6040519861244f8a612a42565b868a528a60208b015260408a01521660608801528860808801525f60a088015260c087015260e08601525f6101008601525f6101208601525f6101408601525f6101608601525f838601526101a085015260016101c08501525f6101e08501525f6102008501525f6102208501525f198114611da45760018101600a555f52600360205260405f20908351825560208401516001830155604084015160028301556003820160ff60608601511660ff198254161790556080840151600483015560a0840151600583015560c0840151600683015560e0840151600783015561010084015160088301556101208401516009830155610140840151600a830155610160840151600b830155830151600c8201556101a0830151600d820155600e81016101c084015160068110156118375760ff801983541691161790556101e0830151600f820155610200830151601082015560116102208401519101555f52600960205260405f20600160ff19825416179055517f9ebeaf9ad328df744571fe8f229f25c1fea383a3672b1bab53e08518ea41b0df604060ff6125f0612ab8565b16948151908152426020820152a4005b63e07712ed60e01b5f5260045ffd5b612631915060203d602011612637575b6126298183612a72565b810190612aa0565b8961242e565b503d61261f565b90506020813d602011612668575b8161265960209383612a72565b8101031261165157518e61239d565b3d915061264c565b8890639cccf9c760e01b5f5260045260245260445260645ffd5b604051630371474560e41b81526004810191909152602481018f9052604481018a905260648101899052608490fd5b508815612366565b50891561235f565b630278b7b560e51b5f526004524260245260445ffd5b635fd519cf60e11b5f526004524260245260445ffd5b639ee65feb60e01b5f5260045ffd5b634e487b7160e01b5f52603260045260245ffd5b9091506020813d602011612744575b8161273460209383612a72565b810103126116515751905f612329565b3d9150612727565b8251845287945060209384019390920191600101612307565b60405162461bcd60e51b81526020600482015260196024820152784669656c643a20696e70757420697320746f6f206c6172676560381b6044820152606490fd5b630105566760e61b5f5260045ffd5b90506020813d6020116127df575b816127d060209383612a72565b8101031261165157518b612093565b3d91506127c3565b631ed306d360e21b5f5260045ffd5b60ff88612801612ab8565b9063a90e356f60e01b5f526004521660245260445ffd5b612831915060203d602011612637576126298183612a72565b8b612043565b838863e823e19f60e01b5f5260045260245260445ffd5b612867915060203d602011612637576126298183612a72565b8b612003565b866318b9c8e360e11b5f5260045260245ffd5b612899915060203d602011612637576126298183612a72565b8a611fc8565b6368f666ad60e01b5f5260045ffd5b60019150141588611f8a565b90506020813d6020116128ed575b816128d560209383612a72565b81010312611651575160048110156116515788611f74565b3d91506128c8565b62385afb60e61b5f5260045ffd5b63e2517d3f60e01b5f52336004525f5160206134305f395f51905f5260245260445ffd5b34611651575f366003190112611651576020600a54604051908152f35b34611651575f3660031901126116515760206040515f5160206133b05f395f51905f528152f35b346116515760203660031901126116515760043563ffffffff60e01b811680910361165157602090637965db0b60e01b81149081156129b0575b506040519015158152f35b6301ffc9a760e01b149050826129a5565b34611651575f3660031901126116515780610e1060209252f35b600435906001600160a01b038216820361165157565b602435906001600160a01b038216820361165157565b604435906001600160a01b038216820361165157565b606435906001600160a01b038216820361165157565b60243590811515820361165157565b61024081019081106001600160401b03821117612a5e57604052565b634e487b7160e01b5f52604160045260245ffd5b90601f801991011681019081106001600160401b03821117612a5e57604052565b9060068210156118375752565b90816020910312611651575180151581036116515790565b60643560ff811681036116515790565b91908203918211611da457565b81810292918115918404141715611da457565b91908201809211611da457565b5f525f5160206134705f395f51905f52602052600160405f20015490565b335f9081525f5160206135505f395f51905f52602052604090205460ff1615612b3857565b63e2517d3f60e01b5f52336004525f5160206133d05f395f51905f5260245260445ffd5b335f9081525f5160206133705f395f51905f52602052604090205460ff1615612b8157565b63e2517d3f60e01b5f52336004525f5160206133b05f395f51905f5260245260445ffd5b335f9081525f5160206134f05f395f51905f52602052604090205460ff1615612bca57565b63e2517d3f60e01b5f52336004525f5160206135305f395f51905f5260245260445ffd5b335f9081525f5160206134905f395f51905f52602052604090205460ff1615612c1357565b63e2517d3f60e01b5f52336004525f5160206133905f395f51905f5260245260445ffd5b5f8181525f5160206134705f395f51905f526020908152604080832033845290915290205460ff1615612c675750565b63e2517d3f60e01b5f523360045260245260445ffd5b60ff5f5160206134b05f395f51905f525416612c9557565b63d93c066560e01b5f5260045ffd5b60025f5160206134d05f395f51905f525414612ccd5760025f5160206134d05f395f51905f5255565b633ee5aeb560e01b5f5260045ffd5b6001600160a01b0381165f9081527fb7db2dd08fcb62d0c9e08c51941cae53c267786a0b75803fb7960902fc8ef97d602052604090205460ff16612d73576001600160a01b03165f8181527fb7db2dd08fcb62d0c9e08c51941cae53c267786a0b75803fb7960902fc8ef97d60205260408120805460ff191660011790553391905f5160206133505f395f51905f528180a4600190565b505f90565b6001600160a01b0381165f9081525f5160206134505f395f51905f52602052604090205460ff16612d73576001600160a01b03165f8181525f5160206134505f395f51905f5260205260408120805460ff191660011790553391905f5160206134305f395f51905f52905f5160206133505f395f51905f529080a4600190565b6001600160a01b0381165f9081525f5160206133705f395f51905f52602052604090205460ff16612d73576001600160a01b03165f8181525f5160206133705f395f51905f5260205260408120805460ff191660011790553391905f5160206133b05f395f51905f52905f5160206133505f395f51905f529080a4600190565b6001600160a01b0381165f9081525f5160206134905f395f51905f52602052604090205460ff16612d73576001600160a01b03165f8181525f5160206134905f395f51905f5260205260408120805460ff191660011790553391905f5160206133905f395f51905f52905f5160206133505f395f51905f529080a4600190565b6001600160a01b0381165f9081525f5160206135505f395f51905f52602052604090205460ff16612d73576001600160a01b03165f8181525f5160206135505f395f51905f5260205260408120805460ff191660011790553391905f5160206133d05f395f51905f52905f5160206133505f395f51905f529080a4600190565b6001600160a01b0381165f9081525f5160206134f05f395f51905f52602052604090205460ff16612d73576001600160a01b03165f8181525f5160206134f05f395f51905f5260205260408120805460ff191660011790553391905f5160206135305f395f51905f52905f5160206133505f395f51905f529080a4600190565b5f8181525f5160206134705f395f51905f52602090815260408083206001600160a01b038616845290915290205460ff16613083575f8181525f5160206134705f395f51905f52602090815260408083206001600160a01b0395909516808452949091528120805460ff19166001179055339291905f5160206133505f395f51905f529080a4600190565b50505f90565b5f8181525f5160206134705f395f51905f52602090815260408083206001600160a01b038616845290915290205460ff1615613083575f8181525f5160206134705f395f51905f52602090815260408083206001600160a01b0395909516808452949091528120805460ff19169055339291907ff6391f5c32d9c69d2a47ea670b442974b53935d1edc7fd64eb21e047a839171b9080a4600190565b6040516323b872dd60e01b5f9081526001600160a01b039384166004529290931660245260449390935260209060648180865af19060015f5114821615613196575b6040525f606052156131765750565b635274afe760e01b5f9081526001600160a01b0391909116600452602490fd5b9060018115166131ae57823b15153d15161690613167565b503d5f823e3d90fd5b805f52600360205260405f209060ff600e830154166006811015611837576002036132865750600a8101916131ed835482612ac8565b6005830154801561327e5764496cebb8009161321161321692600687015490612ad5565b612ad5565b04925581613222575050565b600801613230828254612ae8565b90556002546001600160a01b031690813b15611651575f9160248392604051948593849263073259fd60e01b845260048401525af1801561180a576132725750565b5f61327c91612a72565b565b505091905055565b6309c8354f60e11b5f5260045260245ffd5b60ff5f5160206135105f395f51905f525460401c16156132b457565b631afcd79f60e31b5f5260045ffd5b905f8091602081519101845af4808061333c575b156132f75750506040513d81523d5f602083013e60203d82010160405290565b1561331c57639996b31560e01b5f9081526001600160a01b0391909116600452602490fd5b3d1561332d576040513d5f823e3d90fd5b63d6bda27560e01b5f5260045ffd5b503d1515806132d75750813b15156132d756fe2f8788117e7eff1d82e926ec794901d17c78024a50270940304540a733656f0d265ec2c7f23b289e86ed2d877ad4b447b70ac08332783d1ba335eb6541af8c3c870ee5500b98ca09b5fcd7de4a95293916740021c92172d268dad85baec3c85f250b76734a070a69c7b3930477dd35007ad9c9d0952e97903fdafb2db6980537b92d52e77ebaa0cae5c23e882d85609efbcb44029214147dd132daf9ef1018af360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc30644e72e131a029b85045b68181585d2833e84879b9709143e1f593f00000010b84ee281e5cf521a9ad54a86fafe78946b157177e231bd8ae785af4d3b3620f48ce10f4f7616f06256ebdb7d81e03056199b13e52d95951937b97a5e9b84d6702dd7bc7dec4dceedda775e58dd541e08a116c6c53815c0bd028192f7b6268007e09f44205da34db221ad47c71eca063c660e0943f078a1d8d58c56ac1a41fc7cd5ed15c6e187e77e9aee88184c21f4f2182ab5827cb3b7e07fbedcd63f033009b779b17422d0df92223018b32b4d1fa46e071723d6817e2486d003becc55f007bcff4f162ccdfbe249cdf3a524fc79b31c8aeaae0e727c4887b8e830a8a2e2df0c57e16840df040f15088dc2f81fe391c3923bec73e23a9662efc9c229c6a005358bcfd81d1ef3da152b1755e1c3c6739686fa7e83dbcad0071568cc4b73a63985e7e44dfcb208cb67a8ab5f4ddea68569700462a8bdd41960667c1dc173537a2646970667358221220770fe3d032717f3c207186de00d32229026c92f79ae5f2ab8d07a03e4333f1d764736f6c63430008210033f0c57e16840df040f15088dc2f81fe391c3923bec73e23a9662efc9c229c6a00"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#139)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> LoanEngine:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#139)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#139)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#139)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[LoanEngine]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#139)
        """
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, LoanEngine, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[LoanEngine]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#139)
        """
        return cls._deploy(request_type, [], return_tx, LoanEngine, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def FUND_MANAGER_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#50)

        Returns:
            FUND_MANAGER_ROLE: bytes32
        """
        ...

    @overload
    def FUND_MANAGER_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#50)

        Returns:
            FUND_MANAGER_ROLE: bytes32
        """
        ...

    @overload
    def FUND_MANAGER_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#50)

        Returns:
            FUND_MANAGER_ROLE: bytes32
        """
        ...

    @overload
    def FUND_MANAGER_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#50)

        Returns:
            FUND_MANAGER_ROLE: bytes32
        """
        ...

    def FUND_MANAGER_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#50)

        Returns:
            FUND_MANAGER_ROLE: bytes32
        """
        return self._execute(self.chain, request_type, "2f83a6bc", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def SERVICER_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#51)

        Returns:
            SERVICER_ROLE: bytes32
        """
        ...

    @overload
    def SERVICER_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#51)

        Returns:
            SERVICER_ROLE: bytes32
        """
        ...

    @overload
    def SERVICER_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#51)

        Returns:
            SERVICER_ROLE: bytes32
        """
        ...

    @overload
    def SERVICER_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#51)

        Returns:
            SERVICER_ROLE: bytes32
        """
        ...

    def SERVICER_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#51)

        Returns:
            SERVICER_ROLE: bytes32
        """
        return self._execute(self.chain, request_type, "09a01608", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def RISK_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#52)

        Returns:
            RISK_ADMIN_ROLE: bytes32
        """
        ...

    @overload
    def RISK_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#52)

        Returns:
            RISK_ADMIN_ROLE: bytes32
        """
        ...

    @overload
    def RISK_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#52)

        Returns:
            RISK_ADMIN_ROLE: bytes32
        """
        ...

    @overload
    def RISK_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#52)

        Returns:
            RISK_ADMIN_ROLE: bytes32
        """
        ...

    def RISK_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#52)

        Returns:
            RISK_ADMIN_ROLE: bytes32
        """
        return self._execute(self.chain, request_type, "4f16b425", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def CONFIG_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#53)

        Returns:
            CONFIG_ADMIN_ROLE: bytes32
        """
        ...

    @overload
    def CONFIG_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#53)

        Returns:
            CONFIG_ADMIN_ROLE: bytes32
        """
        ...

    @overload
    def CONFIG_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#53)

        Returns:
            CONFIG_ADMIN_ROLE: bytes32
        """
        ...

    @overload
    def CONFIG_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#53)

        Returns:
            CONFIG_ADMIN_ROLE: bytes32
        """
        ...

    def CONFIG_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#53)

        Returns:
            CONFIG_ADMIN_ROLE: bytes32
        """
        return self._execute(self.chain, request_type, "c78ef28c", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def EMERGENCY_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#54)

        Returns:
            EMERGENCY_ADMIN_ROLE: bytes32
        """
        ...

    @overload
    def EMERGENCY_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#54)

        Returns:
            EMERGENCY_ADMIN_ROLE: bytes32
        """
        ...

    @overload
    def EMERGENCY_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#54)

        Returns:
            EMERGENCY_ADMIN_ROLE: bytes32
        """
        ...

    @overload
    def EMERGENCY_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#54)

        Returns:
            EMERGENCY_ADMIN_ROLE: bytes32
        """
        ...

    def EMERGENCY_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#54)

        Returns:
            EMERGENCY_ADMIN_ROLE: bytes32
        """
        return self._execute(self.chain, request_type, "6e76fc8f", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def i_creditPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ICreditPolicy:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#105)

        Returns:
            i_creditPolicy: contract ICreditPolicy
        """
        ...

    @overload
    def i_creditPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#105)

        Returns:
            i_creditPolicy: contract ICreditPolicy
        """
        ...

    @overload
    def i_creditPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#105)

        Returns:
            i_creditPolicy: contract ICreditPolicy
        """
        ...

    @overload
    def i_creditPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ICreditPolicy]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#105)

        Returns:
            i_creditPolicy: contract ICreditPolicy
        """
        ...

    def i_creditPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[ICreditPolicy, TransactionAbc[ICreditPolicy], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#105)

        Returns:
            i_creditPolicy: contract ICreditPolicy
        """
        return self._execute(self.chain, request_type, "6d4264fa", [], True if request_type == "tx" else False, ICreditPolicy, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def i_loanProofVerifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> IVerifier:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#106)

        Returns:
            i_loanProofVerifier: contract IVerifier
        """
        ...

    @overload
    def i_loanProofVerifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#106)

        Returns:
            i_loanProofVerifier: contract IVerifier
        """
        ...

    @overload
    def i_loanProofVerifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#106)

        Returns:
            i_loanProofVerifier: contract IVerifier
        """
        ...

    @overload
    def i_loanProofVerifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[IVerifier]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#106)

        Returns:
            i_loanProofVerifier: contract IVerifier
        """
        ...

    def i_loanProofVerifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[IVerifier, TransactionAbc[IVerifier], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#106)

        Returns:
            i_loanProofVerifier: contract IVerifier
        """
        return self._execute(self.chain, request_type, "e9af0bbb", [], True if request_type == "tx" else False, IVerifier, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def i_tranchePool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ITranchePool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#107)

        Returns:
            i_tranchePool: contract ITranchePool
        """
        ...

    @overload
    def i_tranchePool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#107)

        Returns:
            i_tranchePool: contract ITranchePool
        """
        ...

    @overload
    def i_tranchePool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#107)

        Returns:
            i_tranchePool: contract ITranchePool
        """
        ...

    @overload
    def i_tranchePool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ITranchePool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#107)

        Returns:
            i_tranchePool: contract ITranchePool
        """
        ...

    def i_tranchePool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[ITranchePool, TransactionAbc[ITranchePool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#107)

        Returns:
            i_tranchePool: contract ITranchePool
        """
        return self._execute(self.chain, request_type, "4448b339", [], True if request_type == "tx" else False, ITranchePool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def s_loans(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ILoanEngine.Loan:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#109)

        Args:
            key0: uint256
        Returns:
            struct ILoanEngine.Loan
        """
        ...

    @overload
    def s_loans(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#109)

        Args:
            key0: uint256
        Returns:
            struct ILoanEngine.Loan
        """
        ...

    @overload
    def s_loans(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#109)

        Args:
            key0: uint256
        Returns:
            struct ILoanEngine.Loan
        """
        ...

    @overload
    def s_loans(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ILoanEngine.Loan]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#109)

        Args:
            key0: uint256
        Returns:
            struct ILoanEngine.Loan
        """
        ...

    def s_loans(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[ILoanEngine.Loan, TransactionAbc[ILoanEngine.Loan], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#109)

        Args:
            key0: uint256
        Returns:
            struct ILoanEngine.Loan
        """
        return self._execute(self.chain, request_type, "91b5a9b6", [key0], True if request_type == "tx" else False, ILoanEngine.Loan, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def s_originationFees(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#110)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def s_originationFees(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#110)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def s_originationFees(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#110)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def s_originationFees(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#110)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    def s_originationFees(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#110)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "d7d52c9e", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def whitelistedOffRampingEntities(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#111)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedOffRampingEntities(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#111)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedOffRampingEntities(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#111)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedOffRampingEntities(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#111)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    def whitelistedOffRampingEntities(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#111)

        Args:
            key0: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "e5d2ee43", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def whitelistedRecoveryAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#113)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedRecoveryAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#113)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedRecoveryAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#113)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedRecoveryAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#113)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    def whitelistedRecoveryAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#113)

        Args:
            key0: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "5cd1d673", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def whitelistedRepaymentAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#116)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedRepaymentAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#116)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedRepaymentAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#116)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedRepaymentAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#116)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    def whitelistedRepaymentAgents(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#116)

        Args:
            key0: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "e656fd8c", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def whitelistedFeeManagers(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#119)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedFeeManagers(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#119)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedFeeManagers(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#119)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def whitelistedFeeManagers(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#119)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    def whitelistedFeeManagers(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#119)

        Args:
            key0: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "2d63f3d4", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def s_nullifierHashes(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#121)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def s_nullifierHashes(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#121)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def s_nullifierHashes(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#121)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def s_nullifierHashes(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#121)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        ...

    def s_nullifierHashes(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#121)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "65174af8", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def s_nextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#122)

        Returns:
            s_nextLoanId: uint256
        """
        ...

    @overload
    def s_nextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#122)

        Returns:
            s_nextLoanId: uint256
        """
        ...

    @overload
    def s_nextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#122)

        Returns:
            s_nextLoanId: uint256
        """
        ...

    @overload
    def s_nextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#122)

        Returns:
            s_nextLoanId: uint256
        """
        ...

    def s_nextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#122)

        Returns:
            s_nextLoanId: uint256
        """
        return self._execute(self.chain, request_type, "10c6b66a", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def s_maxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#123)

        Returns:
            s_maxOriginationFeeBps: uint256
        """
        ...

    @overload
    def s_maxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#123)

        Returns:
            s_maxOriginationFeeBps: uint256
        """
        ...

    @overload
    def s_maxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#123)

        Returns:
            s_maxOriginationFeeBps: uint256
        """
        ...

    @overload
    def s_maxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#123)

        Returns:
            s_maxOriginationFeeBps: uint256
        """
        ...

    def s_maxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#123)

        Returns:
            s_maxOriginationFeeBps: uint256
        """
        return self._execute(self.chain, request_type, "ef697f6b", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def i_stableCoin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#124)

        Returns:
            i_stableCoin: address
        """
        ...

    @overload
    def i_stableCoin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#124)

        Returns:
            i_stableCoin: address
        """
        ...

    @overload
    def i_stableCoin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#124)

        Returns:
            i_stableCoin: address
        """
        ...

    @overload
    def i_stableCoin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#124)

        Returns:
            i_stableCoin: address
        """
        ...

    def i_stableCoin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#124)

        Returns:
            i_stableCoin: address
        """
        return self._execute(self.chain, request_type, "5f407f5c", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def authorizedUnderwriters(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#125)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def authorizedUnderwriters(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#125)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def authorizedUnderwriters(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#125)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def authorizedUnderwriters(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#125)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        ...

    def authorizedUnderwriters(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#125)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "3c36bf0d", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def PROOF_MAX_AGE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#126)

        Returns:
            PROOF_MAX_AGE: uint256
        """
        ...

    @overload
    def PROOF_MAX_AGE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#126)

        Returns:
            PROOF_MAX_AGE: uint256
        """
        ...

    @overload
    def PROOF_MAX_AGE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#126)

        Returns:
            PROOF_MAX_AGE: uint256
        """
        ...

    @overload
    def PROOF_MAX_AGE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#126)

        Returns:
            PROOF_MAX_AGE: uint256
        """
        ...

    def PROOF_MAX_AGE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#126)

        Returns:
            PROOF_MAX_AGE: uint256
        """
        return self._execute(self.chain, request_type, "0005c4b3", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def i_poseidon2(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> IPoseidon2:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#127)

        Returns:
            i_poseidon2: contract IPoseidon2
        """
        ...

    @overload
    def i_poseidon2(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#127)

        Returns:
            i_poseidon2: contract IPoseidon2
        """
        ...

    @overload
    def i_poseidon2(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#127)

        Returns:
            i_poseidon2: contract IPoseidon2
        """
        ...

    @overload
    def i_poseidon2(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[IPoseidon2]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#127)

        Returns:
            i_poseidon2: contract IPoseidon2
        """
        ...

    def i_poseidon2(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[IPoseidon2, TransactionAbc[IPoseidon2], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#127)

        Returns:
            i_poseidon2: contract IPoseidon2
        """
        return self._execute(self.chain, request_type, "6d5e9371", [], True if request_type == "tx" else False, IPoseidon2, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def POLICY_VERSION_HASH_INDEX(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#129)

        Returns:
            POLICY_VERSION_HASH_INDEX: uint256
        """
        ...

    @overload
    def POLICY_VERSION_HASH_INDEX(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#129)

        Returns:
            POLICY_VERSION_HASH_INDEX: uint256
        """
        ...

    @overload
    def POLICY_VERSION_HASH_INDEX(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#129)

        Returns:
            POLICY_VERSION_HASH_INDEX: uint256
        """
        ...

    @overload
    def POLICY_VERSION_HASH_INDEX(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#129)

        Returns:
            POLICY_VERSION_HASH_INDEX: uint256
        """
        ...

    def POLICY_VERSION_HASH_INDEX(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#129)

        Returns:
            POLICY_VERSION_HASH_INDEX: uint256
        """
        return self._execute(self.chain, request_type, "b1933802", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def LOAN_HASH_INDEX(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#130)

        Returns:
            LOAN_HASH_INDEX: uint256
        """
        ...

    @overload
    def LOAN_HASH_INDEX(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#130)

        Returns:
            LOAN_HASH_INDEX: uint256
        """
        ...

    @overload
    def LOAN_HASH_INDEX(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#130)

        Returns:
            LOAN_HASH_INDEX: uint256
        """
        ...

    @overload
    def LOAN_HASH_INDEX(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#130)

        Returns:
            LOAN_HASH_INDEX: uint256
        """
        ...

    def LOAN_HASH_INDEX(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#130)

        Returns:
            LOAN_HASH_INDEX: uint256
        """
        return self._execute(self.chain, request_type, "9740ad66", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def NULLIFIER_HASH_INDEX(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#131)

        Returns:
            NULLIFIER_HASH_INDEX: uint256
        """
        ...

    @overload
    def NULLIFIER_HASH_INDEX(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#131)

        Returns:
            NULLIFIER_HASH_INDEX: uint256
        """
        ...

    @overload
    def NULLIFIER_HASH_INDEX(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#131)

        Returns:
            NULLIFIER_HASH_INDEX: uint256
        """
        ...

    @overload
    def NULLIFIER_HASH_INDEX(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#131)

        Returns:
            NULLIFIER_HASH_INDEX: uint256
        """
        ...

    def NULLIFIER_HASH_INDEX(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#131)

        Returns:
            NULLIFIER_HASH_INDEX: uint256
        """
        return self._execute(self.chain, request_type, "87a1b0a1", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def TOTAL_PUBLIC_INPUTS(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#132)

        Returns:
            TOTAL_PUBLIC_INPUTS: uint256
        """
        ...

    @overload
    def TOTAL_PUBLIC_INPUTS(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#132)

        Returns:
            TOTAL_PUBLIC_INPUTS: uint256
        """
        ...

    @overload
    def TOTAL_PUBLIC_INPUTS(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#132)

        Returns:
            TOTAL_PUBLIC_INPUTS: uint256
        """
        ...

    @overload
    def TOTAL_PUBLIC_INPUTS(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#132)

        Returns:
            TOTAL_PUBLIC_INPUTS: uint256
        """
        ...

    def TOTAL_PUBLIC_INPUTS(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#132)

        Returns:
            TOTAL_PUBLIC_INPUTS: uint256
        """
        return self._execute(self.chain, request_type, "968627e0", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def initialize(self, _creditPolicyContract: Union[Account, Address], _loanProofVerifier: Union[Account, Address], _maxOriginationFeeBps: uint256, _tranchePool: Union[Account, Address], _stableCoinAddress: Union[Account, Address], _poseidon2: Union[Account, Address], _initialAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#152)

        Args:
            _creditPolicyContract: address
            _loanProofVerifier: address
            _maxOriginationFeeBps: uint256
            _tranchePool: address
            _stableCoinAddress: address
            _poseidon2: address
            _initialAdmin: address
        """
        ...

    @overload
    def initialize(self, _creditPolicyContract: Union[Account, Address], _loanProofVerifier: Union[Account, Address], _maxOriginationFeeBps: uint256, _tranchePool: Union[Account, Address], _stableCoinAddress: Union[Account, Address], _poseidon2: Union[Account, Address], _initialAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#152)

        Args:
            _creditPolicyContract: address
            _loanProofVerifier: address
            _maxOriginationFeeBps: uint256
            _tranchePool: address
            _stableCoinAddress: address
            _poseidon2: address
            _initialAdmin: address
        """
        ...

    @overload
    def initialize(self, _creditPolicyContract: Union[Account, Address], _loanProofVerifier: Union[Account, Address], _maxOriginationFeeBps: uint256, _tranchePool: Union[Account, Address], _stableCoinAddress: Union[Account, Address], _poseidon2: Union[Account, Address], _initialAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#152)

        Args:
            _creditPolicyContract: address
            _loanProofVerifier: address
            _maxOriginationFeeBps: uint256
            _tranchePool: address
            _stableCoinAddress: address
            _poseidon2: address
            _initialAdmin: address
        """
        ...

    @overload
    def initialize(self, _creditPolicyContract: Union[Account, Address], _loanProofVerifier: Union[Account, Address], _maxOriginationFeeBps: uint256, _tranchePool: Union[Account, Address], _stableCoinAddress: Union[Account, Address], _poseidon2: Union[Account, Address], _initialAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#152)

        Args:
            _creditPolicyContract: address
            _loanProofVerifier: address
            _maxOriginationFeeBps: uint256
            _tranchePool: address
            _stableCoinAddress: address
            _poseidon2: address
            _initialAdmin: address
        """
        ...

    def initialize(self, _creditPolicyContract: Union[Account, Address], _loanProofVerifier: Union[Account, Address], _maxOriginationFeeBps: uint256, _tranchePool: Union[Account, Address], _stableCoinAddress: Union[Account, Address], _poseidon2: Union[Account, Address], _initialAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#152)

        Args:
            _creditPolicyContract: address
            _loanProofVerifier: address
            _maxOriginationFeeBps: uint256
            _tranchePool: address
            _stableCoinAddress: address
            _poseidon2: address
            _initialAdmin: address
        """
        return self._execute(self.chain, request_type, "9e0baca8", [_creditPolicyContract, _loanProofVerifier, _maxOriginationFeeBps, _tranchePool, _stableCoinAddress, _poseidon2, _initialAdmin], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def createLoan(self, params: ILoanEngine.CreateLoanParams, proofData: Union[bytearray, bytes], publicInputs: List[bytes32], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#220)

        Args:
            params: struct ILoanEngine.CreateLoanParams
            proofData: bytes
            publicInputs: bytes32[]
        """
        ...

    @overload
    def createLoan(self, params: ILoanEngine.CreateLoanParams, proofData: Union[bytearray, bytes], publicInputs: List[bytes32], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#220)

        Args:
            params: struct ILoanEngine.CreateLoanParams
            proofData: bytes
            publicInputs: bytes32[]
        """
        ...

    @overload
    def createLoan(self, params: ILoanEngine.CreateLoanParams, proofData: Union[bytearray, bytes], publicInputs: List[bytes32], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#220)

        Args:
            params: struct ILoanEngine.CreateLoanParams
            proofData: bytes
            publicInputs: bytes32[]
        """
        ...

    @overload
    def createLoan(self, params: ILoanEngine.CreateLoanParams, proofData: Union[bytearray, bytes], publicInputs: List[bytes32], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#220)

        Args:
            params: struct ILoanEngine.CreateLoanParams
            proofData: bytes
            publicInputs: bytes32[]
        """
        ...

    def createLoan(self, params: ILoanEngine.CreateLoanParams, proofData: Union[bytearray, bytes], publicInputs: List[bytes32], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#220)

        Args:
            params: struct ILoanEngine.CreateLoanParams
            proofData: bytes
            publicInputs: bytes32[]
        """
        return self._execute(self.chain, request_type, "1230a365", [params, proofData, publicInputs], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def activateLoan(self, loanId: uint256, receivingEntity: Union[Account, Address], feeManager: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#397)

        Args:
            loanId: uint256
            receivingEntity: address
            feeManager: address
        """
        ...

    @overload
    def activateLoan(self, loanId: uint256, receivingEntity: Union[Account, Address], feeManager: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#397)

        Args:
            loanId: uint256
            receivingEntity: address
            feeManager: address
        """
        ...

    @overload
    def activateLoan(self, loanId: uint256, receivingEntity: Union[Account, Address], feeManager: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#397)

        Args:
            loanId: uint256
            receivingEntity: address
            feeManager: address
        """
        ...

    @overload
    def activateLoan(self, loanId: uint256, receivingEntity: Union[Account, Address], feeManager: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#397)

        Args:
            loanId: uint256
            receivingEntity: address
            feeManager: address
        """
        ...

    def activateLoan(self, loanId: uint256, receivingEntity: Union[Account, Address], feeManager: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#397)

        Args:
            loanId: uint256
            receivingEntity: address
            feeManager: address
        """
        return self._execute(self.chain, request_type, "19e4bc11", [loanId, receivingEntity, feeManager], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, repaymentAgent: Union[Account, Address], timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#463)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
            repaymentAgent: address
            timestamp: uint256
        """
        ...

    @overload
    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, repaymentAgent: Union[Account, Address], timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#463)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
            repaymentAgent: address
            timestamp: uint256
        """
        ...

    @overload
    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, repaymentAgent: Union[Account, Address], timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#463)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
            repaymentAgent: address
            timestamp: uint256
        """
        ...

    @overload
    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, repaymentAgent: Union[Account, Address], timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#463)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
            repaymentAgent: address
            timestamp: uint256
        """
        ...

    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, repaymentAgent: Union[Account, Address], timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#463)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
            repaymentAgent: address
            timestamp: uint256
        """
        return self._execute(self.chain, request_type, "f3e7c14e", [loanId, principalAmount, interestAmount, repaymentAgent, timestamp], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def declareDefault(self, loanId: uint256, reasonHash: bytes32, timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#543)

        Args:
            loanId: uint256
            reasonHash: bytes32
            timestamp: uint256
        """
        ...

    @overload
    def declareDefault(self, loanId: uint256, reasonHash: bytes32, timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#543)

        Args:
            loanId: uint256
            reasonHash: bytes32
            timestamp: uint256
        """
        ...

    @overload
    def declareDefault(self, loanId: uint256, reasonHash: bytes32, timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#543)

        Args:
            loanId: uint256
            reasonHash: bytes32
            timestamp: uint256
        """
        ...

    @overload
    def declareDefault(self, loanId: uint256, reasonHash: bytes32, timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#543)

        Args:
            loanId: uint256
            reasonHash: bytes32
            timestamp: uint256
        """
        ...

    def declareDefault(self, loanId: uint256, reasonHash: bytes32, timestamp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#543)

        Args:
            loanId: uint256
            reasonHash: bytes32
            timestamp: uint256
        """
        return self._execute(self.chain, request_type, "a1a06a8c", [loanId, reasonHash, timestamp], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def writeOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#567)

        Args:
            loanId: uint256
        """
        ...

    @overload
    def writeOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#567)

        Args:
            loanId: uint256
        """
        ...

    @overload
    def writeOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#567)

        Args:
            loanId: uint256
        """
        ...

    @overload
    def writeOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#567)

        Args:
            loanId: uint256
        """
        ...

    def writeOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#567)

        Args:
            loanId: uint256
        """
        return self._execute(self.chain, request_type, "727df75c", [loanId], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def recoverLoan(self, loanId: uint256, amount: uint256, recoveryAgent: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#598)

        Args:
            loanId: uint256
            amount: uint256
            recoveryAgent: address
        """
        ...

    @overload
    def recoverLoan(self, loanId: uint256, amount: uint256, recoveryAgent: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#598)

        Args:
            loanId: uint256
            amount: uint256
            recoveryAgent: address
        """
        ...

    @overload
    def recoverLoan(self, loanId: uint256, amount: uint256, recoveryAgent: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#598)

        Args:
            loanId: uint256
            amount: uint256
            recoveryAgent: address
        """
        ...

    @overload
    def recoverLoan(self, loanId: uint256, amount: uint256, recoveryAgent: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#598)

        Args:
            loanId: uint256
            amount: uint256
            recoveryAgent: address
        """
        ...

    def recoverLoan(self, loanId: uint256, amount: uint256, recoveryAgent: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#598)

        Args:
            loanId: uint256
            amount: uint256
            recoveryAgent: address
        """
        return self._execute(self.chain, request_type, "48abb7e3", [loanId, amount, recoveryAgent], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setMaxOriginationFeeBps(self, _maxOriginationFeeBps: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#659)

        Args:
            _maxOriginationFeeBps: uint256
        """
        ...

    @overload
    def setMaxOriginationFeeBps(self, _maxOriginationFeeBps: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#659)

        Args:
            _maxOriginationFeeBps: uint256
        """
        ...

    @overload
    def setMaxOriginationFeeBps(self, _maxOriginationFeeBps: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#659)

        Args:
            _maxOriginationFeeBps: uint256
        """
        ...

    @overload
    def setMaxOriginationFeeBps(self, _maxOriginationFeeBps: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#659)

        Args:
            _maxOriginationFeeBps: uint256
        """
        ...

    def setMaxOriginationFeeBps(self, _maxOriginationFeeBps: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#659)

        Args:
            _maxOriginationFeeBps: uint256
        """
        return self._execute(self.chain, request_type, "2f45bc8e", [_maxOriginationFeeBps], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def pause(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#667)
        """
        ...

    @overload
    def pause(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#667)
        """
        ...

    @overload
    def pause(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#667)
        """
        ...

    @overload
    def pause(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#667)
        """
        ...

    def pause(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#667)
        """
        return self._execute(self.chain, request_type, "8456cb59", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def unpause(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#672)
        """
        ...

    @overload
    def unpause(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#672)
        """
        ...

    @overload
    def unpause(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#672)
        """
        ...

    @overload
    def unpause(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#672)
        """
        ...

    def unpause(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#672)
        """
        return self._execute(self.chain, request_type, "3f4ba83a", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setWhitelistedOffRampingEntity(self, entity: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#679)

        Args:
            entity: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedOffRampingEntity(self, entity: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#679)

        Args:
            entity: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedOffRampingEntity(self, entity: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#679)

        Args:
            entity: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedOffRampingEntity(self, entity: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#679)

        Args:
            entity: address
            isWhitelisted: bool
        """
        ...

    def setWhitelistedOffRampingEntity(self, entity: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#679)

        Args:
            entity: address
            isWhitelisted: bool
        """
        return self._execute(self.chain, request_type, "304566c4", [entity, isWhitelisted], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setWhitelistedRecoveryAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#691)

        Args:
            agent: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedRecoveryAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#691)

        Args:
            agent: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedRecoveryAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#691)

        Args:
            agent: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedRecoveryAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#691)

        Args:
            agent: address
            isWhitelisted: bool
        """
        ...

    def setWhitelistedRecoveryAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#691)

        Args:
            agent: address
            isWhitelisted: bool
        """
        return self._execute(self.chain, request_type, "ee481455", [agent, isWhitelisted], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setWhitelistedRepaymentAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#703)

        Args:
            agent: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedRepaymentAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#703)

        Args:
            agent: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedRepaymentAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#703)

        Args:
            agent: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedRepaymentAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#703)

        Args:
            agent: address
            isWhitelisted: bool
        """
        ...

    def setWhitelistedRepaymentAgent(self, agent: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#703)

        Args:
            agent: address
            isWhitelisted: bool
        """
        return self._execute(self.chain, request_type, "19b52c21", [agent, isWhitelisted], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setWhitelistedFeeManager(self, manager: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#715)

        Args:
            manager: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedFeeManager(self, manager: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#715)

        Args:
            manager: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedFeeManager(self, manager: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#715)

        Args:
            manager: address
            isWhitelisted: bool
        """
        ...

    @overload
    def setWhitelistedFeeManager(self, manager: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#715)

        Args:
            manager: address
            isWhitelisted: bool
        """
        ...

    def setWhitelistedFeeManager(self, manager: Union[Account, Address], isWhitelisted: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#715)

        Args:
            manager: address
            isWhitelisted: bool
        """
        return self._execute(self.chain, request_type, "7e7761a4", [manager, isWhitelisted], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getMaxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#725)

        Returns:
            uint256
        """
        ...

    @overload
    def getMaxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#725)

        Returns:
            uint256
        """
        ...

    @overload
    def getMaxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#725)

        Returns:
            uint256
        """
        ...

    @overload
    def getMaxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#725)

        Returns:
            uint256
        """
        ...

    def getMaxOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#725)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "6780f977", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setUnderwriterAuthorization(self, keyX: bytes32, keyY: bytes32, isAuthorized: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#737)

        Args:
            keyX: bytes32
            keyY: bytes32
            isAuthorized: bool
        """
        ...

    @overload
    def setUnderwriterAuthorization(self, keyX: bytes32, keyY: bytes32, isAuthorized: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#737)

        Args:
            keyX: bytes32
            keyY: bytes32
            isAuthorized: bool
        """
        ...

    @overload
    def setUnderwriterAuthorization(self, keyX: bytes32, keyY: bytes32, isAuthorized: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#737)

        Args:
            keyX: bytes32
            keyY: bytes32
            isAuthorized: bool
        """
        ...

    @overload
    def setUnderwriterAuthorization(self, keyX: bytes32, keyY: bytes32, isAuthorized: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#737)

        Args:
            keyX: bytes32
            keyY: bytes32
            isAuthorized: bool
        """
        ...

    def setUnderwriterAuthorization(self, keyX: bytes32, keyY: bytes32, isAuthorized: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#737)

        Args:
            keyX: bytes32
            keyY: bytes32
            isAuthorized: bool
        """
        return self._execute(self.chain, request_type, "73687a64", [keyX, keyY, isAuthorized], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getNextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#758)

        Returns:
            uint256
        """
        ...

    @overload
    def getNextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#758)

        Returns:
            uint256
        """
        ...

    @overload
    def getNextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#758)

        Returns:
            uint256
        """
        ...

    @overload
    def getNextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#758)

        Returns:
            uint256
        """
        ...

    def getNextLoanId(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#758)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "6146dd6f", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getLoanDetails(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ILoanEngine.Loan:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#765)

        Args:
            loanId: uint256
        Returns:
            struct ILoanEngine.Loan
        """
        ...

    @overload
    def getLoanDetails(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#765)

        Args:
            loanId: uint256
        Returns:
            struct ILoanEngine.Loan
        """
        ...

    @overload
    def getLoanDetails(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#765)

        Args:
            loanId: uint256
        Returns:
            struct ILoanEngine.Loan
        """
        ...

    @overload
    def getLoanDetails(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ILoanEngine.Loan]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#765)

        Args:
            loanId: uint256
        Returns:
            struct ILoanEngine.Loan
        """
        ...

    def getLoanDetails(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[ILoanEngine.Loan, TransactionAbc[ILoanEngine.Loan], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#765)

        Args:
            loanId: uint256
        Returns:
            struct ILoanEngine.Loan
        """
        return self._execute(self.chain, request_type, "66877b8d", [loanId], True if request_type == "tx" else False, ILoanEngine.Loan, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def poseidon2(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> IPoseidon2:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#771)

        Returns:
            contract IPoseidon2
        """
        ...

    @overload
    def poseidon2(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#771)

        Returns:
            contract IPoseidon2
        """
        ...

    @overload
    def poseidon2(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#771)

        Returns:
            contract IPoseidon2
        """
        ...

    @overload
    def poseidon2(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[IPoseidon2]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#771)

        Returns:
            contract IPoseidon2
        """
        ...

    def poseidon2(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[IPoseidon2, TransactionAbc[IPoseidon2], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#771)

        Returns:
            contract IPoseidon2
        """
        return self._execute(self.chain, request_type, "ca5ee4b2", [], True if request_type == "tx" else False, IPoseidon2, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def creditPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ICreditPolicy:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#775)

        Returns:
            contract ICreditPolicy
        """
        ...

    @overload
    def creditPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#775)

        Returns:
            contract ICreditPolicy
        """
        ...

    @overload
    def creditPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#775)

        Returns:
            contract ICreditPolicy
        """
        ...

    @overload
    def creditPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ICreditPolicy]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#775)

        Returns:
            contract ICreditPolicy
        """
        ...

    def creditPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[ICreditPolicy, TransactionAbc[ICreditPolicy], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#775)

        Returns:
            contract ICreditPolicy
        """
        return self._execute(self.chain, request_type, "faaddb94", [], True if request_type == "tx" else False, ICreditPolicy, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tranchePool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ITranchePool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#779)

        Returns:
            contract ITranchePool
        """
        ...

    @overload
    def tranchePool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#779)

        Returns:
            contract ITranchePool
        """
        ...

    @overload
    def tranchePool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#779)

        Returns:
            contract ITranchePool
        """
        ...

    @overload
    def tranchePool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ITranchePool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#779)

        Returns:
            contract ITranchePool
        """
        ...

    def tranchePool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[ITranchePool, TransactionAbc[ITranchePool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#779)

        Returns:
            contract ITranchePool
        """
        return self._execute(self.chain, request_type, "7df0a806", [], True if request_type == "tx" else False, ITranchePool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def loanProofVerifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> IVerifier:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#783)

        Returns:
            contract IVerifier
        """
        ...

    @overload
    def loanProofVerifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#783)

        Returns:
            contract IVerifier
        """
        ...

    @overload
    def loanProofVerifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#783)

        Returns:
            contract IVerifier
        """
        ...

    @overload
    def loanProofVerifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[IVerifier]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#783)

        Returns:
            contract IVerifier
        """
        ...

    def loanProofVerifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[IVerifier, TransactionAbc[IVerifier], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#783)

        Returns:
            contract IVerifier
        """
        return self._execute(self.chain, request_type, "b56b5c29", [], True if request_type == "tx" else False, IVerifier, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def stableCoin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#787)

        Returns:
            address
        """
        ...

    @overload
    def stableCoin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#787)

        Returns:
            address
        """
        ...

    @overload
    def stableCoin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#787)

        Returns:
            address
        """
        ...

    @overload
    def stableCoin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#787)

        Returns:
            address
        """
        ...

    def stableCoin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/LoanEngine.sol#787)

        Returns:
            address
        """
        return self._execute(self.chain, request_type, "992642e5", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

LoanEngine.FUND_MANAGER_ROLE.selector = bytes4(b'/\x83\xa6\xbc')
LoanEngine.SERVICER_ROLE.selector = bytes4(b'\t\xa0\x16\x08')
LoanEngine.RISK_ADMIN_ROLE.selector = bytes4(b'O\x16\xb4%')
LoanEngine.CONFIG_ADMIN_ROLE.selector = bytes4(b'\xc7\x8e\xf2\x8c')
LoanEngine.EMERGENCY_ADMIN_ROLE.selector = bytes4(b'nv\xfc\x8f')
LoanEngine.i_creditPolicy.selector = bytes4(b'mBd\xfa')
LoanEngine.i_loanProofVerifier.selector = bytes4(b'\xe9\xaf\x0b\xbb')
LoanEngine.i_tranchePool.selector = bytes4(b'DH\xb39')
LoanEngine.s_loans.selector = bytes4(b'\x91\xb5\xa9\xb6')
LoanEngine.s_originationFees.selector = bytes4(b'\xd7\xd5,\x9e')
LoanEngine.whitelistedOffRampingEntities.selector = bytes4(b'\xe5\xd2\xeeC')
LoanEngine.whitelistedRecoveryAgents.selector = bytes4(b'\\\xd1\xd6s')
LoanEngine.whitelistedRepaymentAgents.selector = bytes4(b'\xe6V\xfd\x8c')
LoanEngine.whitelistedFeeManagers.selector = bytes4(b'-c\xf3\xd4')
LoanEngine.s_nullifierHashes.selector = bytes4(b'e\x17J\xf8')
LoanEngine.s_nextLoanId.selector = bytes4(b'\x10\xc6\xb6j')
LoanEngine.s_maxOriginationFeeBps.selector = bytes4(b'\xefi\x7fk')
LoanEngine.i_stableCoin.selector = bytes4(b'_@\x7f\\')
LoanEngine.authorizedUnderwriters.selector = bytes4(b'<6\xbf\r')
LoanEngine.PROOF_MAX_AGE.selector = bytes4(b'\x00\x05\xc4\xb3')
LoanEngine.i_poseidon2.selector = bytes4(b'm^\x93q')
LoanEngine.POLICY_VERSION_HASH_INDEX.selector = bytes4(b'\xb1\x938\x02')
LoanEngine.LOAN_HASH_INDEX.selector = bytes4(b'\x97@\xadf')
LoanEngine.NULLIFIER_HASH_INDEX.selector = bytes4(b'\x87\xa1\xb0\xa1')
LoanEngine.TOTAL_PUBLIC_INPUTS.selector = bytes4(b"\x96\x86'\xe0")
LoanEngine.initialize.selector = bytes4(b'\x9e\x0b\xac\xa8')
LoanEngine.createLoan.selector = bytes4(b'\x120\xa3e')
LoanEngine.activateLoan.selector = bytes4(b'\x19\xe4\xbc\x11')
LoanEngine.repayLoan.selector = bytes4(b'\xf3\xe7\xc1N')
LoanEngine.declareDefault.selector = bytes4(b'\xa1\xa0j\x8c')
LoanEngine.writeOffLoan.selector = bytes4(b'r}\xf7\\')
LoanEngine.recoverLoan.selector = bytes4(b'H\xab\xb7\xe3')
LoanEngine.setMaxOriginationFeeBps.selector = bytes4(b'/E\xbc\x8e')
LoanEngine.pause.selector = bytes4(b'\x84V\xcbY')
LoanEngine.unpause.selector = bytes4(b'?K\xa8:')
LoanEngine.setWhitelistedOffRampingEntity.selector = bytes4(b'0Ef\xc4')
LoanEngine.setWhitelistedRecoveryAgent.selector = bytes4(b'\xeeH\x14U')
LoanEngine.setWhitelistedRepaymentAgent.selector = bytes4(b'\x19\xb5,!')
LoanEngine.setWhitelistedFeeManager.selector = bytes4(b'~wa\xa4')
LoanEngine.getMaxOriginationFeeBps.selector = bytes4(b'g\x80\xf9w')
LoanEngine.setUnderwriterAuthorization.selector = bytes4(b'shzd')
LoanEngine.getNextLoanId.selector = bytes4(b'aF\xddo')
LoanEngine.getLoanDetails.selector = bytes4(b'f\x87{\x8d')
LoanEngine.poseidon2.selector = bytes4(b'\xca^\xe4\xb2')
LoanEngine.creditPolicy.selector = bytes4(b'\xfa\xad\xdb\x94')
LoanEngine.tranchePool.selector = bytes4(b'}\xf0\xa8\x06')
LoanEngine.loanProofVerifier.selector = bytes4(b'\xb5k\\)')
LoanEngine.stableCoin.selector = bytes4(b'\x99&B\xe5')
