
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.forgestd.src.Test import Test
from pytypes.lib.openzeppelincontracts.contracts.mocks.token.ERC20Mock import ERC20Mock
from pytypes.src.CreditPolicy import CreditPolicy
from pytypes.src.LoanEngine import LoanEngine
from pytypes.src.TranchePool import TranchePool



class Handler(Test):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#11)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'contract LoanEngine', 'name': '_loanEngine', 'type': 'address'}, {'internalType': 'contract TranchePool', 'name': '_tranchePool', 'type': 'address'}, {'internalType': 'contract CreditPolicy', 'name': '_creditPolicy', 'type': 'address'}, {'internalType': 'contract ERC20Mock', 'name': '_usdt', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'A0O\xac\xd92=u\xb1\x1b\xcd\xd6\t\xcb8\xef\xff\xfd\xb0W\x10\xf7\xca\xf0\xe9\xb1lm\x9dp\x9fP': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log', 'type': 'event'}, b'z\xe7LRt\x14\xae\x13_\xd9pG\xb1)!\xa5\xec9\x11\xb8\x04\x19xU\xd6~%\xc7\xb7^\xe6\xf3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'log_address', 'type': 'event'}, b'\xfb\x10(e\xd5\n\xdd\xdd\xf6\x9d\xa9\xb5\xaa\x1b\xce\xd6l\x80\xcf\x86\x9a\\\x8d\x04q\xa4g\xe1\x8c\xe9\xca\xb1': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_array', 'type': 'event'}, b'\x89\n\x82g\x9bG\x0f+\xd8(\x16\xed\x9b\x16\x1f\x97\xd8\xb9g\xf3\x7f\xa3d|!\xd5\xbf9t\x9e-\xd5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_array', 'type': 'event'}, b'@\xe1\x84\x0fWi\x07=a\xbd\x017-\x9bu\xba\xa9\x84-V)\xa0\xc9\x9f\xf1\x03\xbe\x11x\xa8\xe9\xe2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_array', 'type': 'event'}, b'#\xb6*\xd0XM$\xa7_\x0b\xf3V\x03\x91\xefVY\xecm\xb1&\x9cV\xe1\x1a\xa2A\xd67\xf1\x9b ': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'log_bytes', 'type': 'event'}, b'\xe8\x16\x99\xb8Q\x13\xee\xa1\xc7>\x10X\x8b+\x03^U\x893ic!s\xaf\xd4?\xeb\x19/\xacd\xe3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'log_bytes32', 'type': 'event'}, b'\x0e\xb5\xd5&$\xc8\xd2\x8a\xda\x9f\xc5Z\x8cP.\xd5\xaa?\xbe/\xb6\xe9\x1bq\xb5\xf3v\x88+\x1d/\xb8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256', 'name': '', 'type': 'int256'}], 'name': 'log_int', 'type': 'event'}, b'\x9cN\x85A\xca\x8f\r\xc1\xc4\x13\xf9\x10\x8ff\xd8-<\xec\xb1\xbd\xdb\xceCza\xca\xa3\x17\\L\xc9o': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address', 'name': 'val', 'type': 'address'}], 'name': 'log_named_address', 'type': 'event'}, b'\x00\xaa\xa3\x9c\x9f\xfb_VzE48\x0cspup.\x1f\x7f\x14\x10\x7f\xc9S(\xe3\xb5l\x03%\xfb': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xa7>\xda\tf/F\xdd\xe7)\xbeF\x118_\xf3O\xe6\xc4O\xbb\xc6\xf7\xe1{\x04+Y\xa3D[W': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_named_array', 'type': 'event'}, b";\xcf\xb2\xae.\x8d\x13-\xd1\xfc\xe7\xcf'\x8a\x9a\x19uj\x9f\xce\xab\xe4p\xdf;\xda\xbbK\xc5w\xd1\xbd": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xd2n\x16\xca\xd4T\x87\x05\xe4\xc9\xe2\xd9O\x98\xee\x91\xc2\x89\x08^\xe4%YO\xd5c_\xa2\x96L\xcf\x18': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'val', 'type': 'bytes'}], 'name': 'log_named_bytes', 'type': 'event'}, b'\xaf\xb7\x95\xc9\xc6\x1eO\xe7F\x8c8o\x92]zT)\xec\xad\x9c\x04\x95\xdd\xb8\xd3\x8di\x06\x14\xd3/\x99': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'val', 'type': 'bytes32'}], 'name': 'log_named_bytes32', 'type': 'event'}, b']\xa6\xce\x9dQ\x15\x1b\xa1\x0c\t\xa5Y\xef$\xd5 \xb9\xda\xc5\xc5\xb8\x81\n\xe8CNM\r\x86A\x1a\x95': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_int', 'type': 'event'}, b"\xeb\x8b\xa4<\xedu7B\x19F\xbdC\xe8(\xb8\xb2\xb8B\x89'\xaa\x8f\x80\x1c\x13\xd94\xbf\x11\xac\xa5{": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_uint', 'type': 'event'}, b'/\xe62w\x91t7CxD*\x8e\x97\x8b\xcc\xfb\xdc\xc1\xd6\xb2\xb0\xd8\x1f~\x8e\xb7v\xab"\x86\xf1h': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}], 'name': 'log_named_int', 'type': 'event'}, b'(\x0fDF\xb2\x8a\x13rA}\xdae\x8d0\xb9[)\x92\xb1*\xc9\xc7\xf3xS_)\xa9z\xcf5\x83': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'val', 'type': 'string'}], 'name': 'log_named_string', 'type': 'event'}, b'\xb2\xde/\xbe\x80\x1a\r\xf6\xc0\xcb\xdd\xfdD\x8b\xa3\xc4\x1dH\xa0@\xca5\xc5l\x81\x96\xef\x0f\xca\xe7!\xa8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}], 'name': 'log_named_uint', 'type': 'event'}, b'\x0b.\x13\xff \xac{GA\x98eU\x83\xed\xf7\r\xed\xd2\xc1\xdc\x98\x0e2\x9cO\xbb/\xc0t\x8byk': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log_string', 'type': 'event'}, b',\xab\x97\x90Q\x0f\xd8\xbd\xfb\xd2\x11R\x88\xdb3\xfe\xc6f\x91\xd4v\xef\xc5B|\xfdL\ti0\x17U': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'log_uint', 'type': 'event'}, b"\xe7\x95\x0e\xde\x03\x94\xb9\xf2\xceJZ\x1b\xf5\xa7\xe1\x85$\x11\xf7\xe6f\x1bC\x08\xc9\x13\xc4\xbf\xd1\x10'\xe4": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'logs', 'type': 'event'}, b'\xfav&\xd4': {'inputs': [], 'name': 'IS_TEST', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc5ND\xeb': {'inputs': [], 'name': 'USDT', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'FD\x00M': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'activateLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'v\xde\x06\xf3': {'inputs': [], 'name': 'activePolicyVersion', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb9\xfa\xe6P': {'inputs': [{'internalType': 'uint256', 'name': 'principalIssued', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'originationFeeBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'termDays', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'userIndex', 'type': 'uint256'}], 'name': 'createLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x8b\xc1(\xf1': {'inputs': [], 'name': 'defaultCounter', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'9d\x92K': {'inputs': [{'internalType': 'uint256', 'name': 'userIndex', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'depositEquityTranche', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'WL\xa1\x86': {'inputs': [{'internalType': 'uint256', 'name': 'userIndex', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'depositJuniorTranche', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'zI?/': {'inputs': [{'internalType': 'uint256', 'name': 'userIndex', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'depositSeniorTranche', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa3\xb9?\xff': {'inputs': [], 'name': 'equityTrancheDeployedValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb7\xc9\xd5\xb6': {'inputs': [], 'name': 'equityTrancheIdleValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x9e\x95O\xd0': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'equityUsers', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb5P\x8a\xa9': {'inputs': [], 'name': 'excludeArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'excludedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe2\x0c\x9fq': {'inputs': [], 'name': 'excludeContracts', 'outputs': [{'internalType': 'address[]', 'name': 'excludedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb0FO\xdc': {'inputs': [], 'name': 'excludeSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'excludedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1e\xd7\x83\x1c': {'inputs': [], 'name': 'excludeSenders', 'outputs': [{'internalType': 'address[]', 'name': 'excludedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'p\x99\xc9\x0c': {'inputs': [], 'name': 'expectedPrincipal', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbaAO\xa6': {'inputs': [], 'name': 'failed', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd0\xfb\x02\x03': {'inputs': [], 'name': 'feeManager', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\x89\xb7\xd9-': {'inputs': [], 'name': 'getJuniorTrancheIdleValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe3\xe1\xde\x86': {'inputs': [], 'name': 'getJuniorTrancheTotalShares', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xebx6\\': {'inputs': [], 'name': 'getSeniorTrancheIdleValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'p{\xaf7': {'inputs': [], 'name': 'getSeniorTrancheTotalShares', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'b\xb8\x14G': {'inputs': [], 'name': 'juniorTrancheDeployedValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x8a\xde\x00\xb7': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'juniorTrancheDeposits', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xcd\xf92\x9e': {'inputs': [], 'name': 'juniorTrancheIdleValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'P\x01Ok': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'juniorTrancheShares', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xca\xb2\x84[': {'inputs': [], 'name': 'juniorTrancheTotalShares', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd2\xbe\xb9&': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'juniorUserIndex', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xf5\xd6V\x96': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'juniorUsers', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'jt\xc5H': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'loanBorrowers', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'M\xf2\xd3\x88': {'inputs': [], 'name': 'maximumLoanPrincipal', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'K\xa0r\xae': {'inputs': [], 'name': 'maximumTermDays', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'P\x7f%?': {'inputs': [], 'name': 'maybeCommitPool', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'.\xc3\xad\x92': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'reasonHash', 'type': 'bytes32'}], 'name': 'maybeDeclareDefault', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa6\xb5\x90\xe8': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'agentIndex', 'type': 'uint256'}], 'name': 'maybeRecoverLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x85!\x83D': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'maybeWriteOffLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf8`\xf2\xc8': {'inputs': [], 'name': 'minimumLoanPrincipal', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xac\x135!': {'inputs': [], 'name': 'minimumOriginationFeeBps', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b';a\xf6^': {'inputs': [], 'name': 'minimumTermDays', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe6\x91\xbb\x9e': {'inputs': [], 'name': 'outStandingPrincipal', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbb\x85\xe7\x9c': {'inputs': [], 'name': 'recevingEntity', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'h\xf0\xc7\x13': {'inputs': [], 'name': 'recoveryCounter', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x8c\x84\x89\xf2': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'principalAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestAmount', 'type': 'uint256'}], 'name': 'repayLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'@k\xf6p': {'inputs': [], 'name': 'seniorTrancheDeployedValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe9\xe9tB': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'seniorTrancheDeposits', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe5\x1eC\xc2': {'inputs': [], 'name': 'seniorTrancheIdleValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'z""\xdd': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'seniorTrancheShares', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbb8\x05\xfa': {'inputs': [], 'name': 'seniorTrancheTotalShares', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x8f8\xdf\x91': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'seniorUserIndex', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x85&n\x18': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'seniorUsers', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'f\xd9\xa9\xa0': {'inputs': [], 'name': 'targetArtifactSelectors', 'outputs': [{'components': [{'internalType': 'string', 'name': 'artifact', 'type': 'string'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzArtifactSelector[]', 'name': 'targetedArtifactSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x85"l\x81': {'inputs': [], 'name': 'targetArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'targetedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'?r\x86\xf4': {'inputs': [], 'name': 'targetContracts', 'outputs': [{'internalType': 'address[]', 'name': 'targetedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'*\xde8\x80': {'inputs': [], 'name': 'targetInterfaces', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'string[]', 'name': 'artifacts', 'type': 'string[]'}], 'internalType': 'struct StdInvariant.FuzzInterface[]', 'name': 'targetedInterfaces_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x91j\x17\xc6': {'inputs': [], 'name': 'targetSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'targetedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'>^<#': {'inputs': [], 'name': 'targetSenders', 'outputs': [{'internalType': 'address[]', 'name': 'targetedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'-\x8dC]': {'inputs': [], 'name': 'totalDeployedValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xffP\xab\xdc': {'inputs': [], 'name': 'totalDeposited', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'%\xcd\xcf\x05': {'inputs': [], 'name': 'totalExpectedJuniorDeposits', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'G%x1': {'inputs': [], 'name': 'totalExpectedJuniorShares', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b')\x1a\x14~': {'inputs': [], 'name': 'totalExpectedSeniorDeposits', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'A\xe8\xbcM': {'inputs': [], 'name': 'totalExpectedSeniorShares', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xfc[\x08@': {'inputs': [], 'name': 'totalIdleValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\rE~\xe1': {'inputs': [], 'name': 'totalLoss', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xca\x1ao\xbb': {'inputs': [], 'name': 'totalRecovered', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x9b\xdd\xaf\xe8': {'inputs': [{'internalType': 'uint256', 'name': 'daysToWarp', 'type': 'uint256'}], 'name': 'warpTime', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'{\xe2t\xe1': {'inputs': [], 'name': 'writeOffCounter', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":46,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"stdstore","offset":0,"slot":0,"type":"t_struct(StdStorage)8331_storage"},{"astId":209,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_failed","offset":0,"slot":8,"type":"t_bool"},{"astId":2943,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"stdChainsInitialized","offset":1,"slot":8,"type":"t_bool"},{"astId":2964,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"chains","offset":0,"slot":9,"type":"t_mapping(t_string_memory_ptr,t_struct(Chain)2959_storage)"},{"astId":2968,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"defaultRpcUrls","offset":0,"slot":10,"type":"t_mapping(t_string_memory_ptr,t_string_storage)"},{"astId":2972,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"idToAlias","offset":0,"slot":11,"type":"t_mapping(t_uint256,t_string_storage)"},{"astId":2975,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"fallbackToDefaultRpcUrls","offset":0,"slot":12,"type":"t_bool"},{"astId":3931,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"gasMeteringOff","offset":1,"slot":12,"type":"t_bool"},{"astId":6002,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"stdstore","offset":0,"slot":13,"type":"t_struct(StdStorage)8331_storage"},{"astId":6923,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_excludedContracts","offset":0,"slot":21,"type":"t_array(t_address)dyn_storage"},{"astId":6926,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_excludedSenders","offset":0,"slot":22,"type":"t_array(t_address)dyn_storage"},{"astId":6929,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_targetedContracts","offset":0,"slot":23,"type":"t_array(t_address)dyn_storage"},{"astId":6932,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_targetedSenders","offset":0,"slot":24,"type":"t_array(t_address)dyn_storage"},{"astId":6935,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_excludedArtifacts","offset":0,"slot":25,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6938,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_targetedArtifacts","offset":0,"slot":26,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6942,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_targetedArtifactSelectors","offset":0,"slot":27,"type":"t_array(t_struct(FuzzArtifactSelector)6914_storage)dyn_storage"},{"astId":6946,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_excludedSelectors","offset":0,"slot":28,"type":"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage"},{"astId":6950,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_targetedSelectors","offset":0,"slot":29,"type":"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage"},{"astId":6954,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_targetedInterfaces","offset":0,"slot":30,"type":"t_array(t_struct(FuzzInterface)6920_storage)dyn_storage"},{"astId":13223,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"IS_TEST","offset":0,"slot":31,"type":"t_bool"},{"astId":48301,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"loanEngine","offset":1,"slot":31,"type":"t_contract(LoanEngine)44023"},{"astId":48304,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"tranchePool","offset":0,"slot":32,"type":"t_contract(TranchePool)47199"},{"astId":48307,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"usdt","offset":0,"slot":33,"type":"t_contract(ERC20Mock)40221"},{"astId":48310,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"creditPolicy","offset":0,"slot":34,"type":"t_contract(CreditPolicy)42678"},{"astId":48315,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"deployer","offset":0,"slot":35,"type":"t_address"},{"astId":48318,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"USDT","offset":0,"slot":36,"type":"t_uint256"},{"astId":48321,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"allowFullDeployment","offset":0,"slot":37,"type":"t_bool"},{"astId":48326,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"expectedPrincipal","offset":0,"slot":38,"type":"t_uint256"},{"astId":48331,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"minimumLoanPrincipal","offset":0,"slot":39,"type":"t_uint256"},{"astId":48336,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"maximumLoanPrincipal","offset":0,"slot":40,"type":"t_uint256"},{"astId":48339,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"minimumOriginationFeeBps","offset":0,"slot":41,"type":"t_uint256"},{"astId":48342,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"minimumTermDays","offset":0,"slot":42,"type":"t_uint256"},{"astId":48345,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"maximumTermDays","offset":0,"slot":43,"type":"t_uint256"},{"astId":48348,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"seniorUsers","offset":0,"slot":44,"type":"t_array(t_address)dyn_storage"},{"astId":48351,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"juniorUsers","offset":0,"slot":45,"type":"t_array(t_address)dyn_storage"},{"astId":48354,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"equityUsers","offset":0,"slot":46,"type":"t_array(t_address)dyn_storage"},{"astId":48357,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"activePolicyVersion","offset":0,"slot":47,"type":"t_uint256"},{"astId":48359,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"defaultCounter","offset":0,"slot":48,"type":"t_uint256"},{"astId":48361,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"writeOffCounter","offset":0,"slot":49,"type":"t_uint256"},{"astId":48363,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"recoveryCounter","offset":0,"slot":50,"type":"t_uint256"},{"astId":48365,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"seniorTrancheIdleValue","offset":0,"slot":51,"type":"t_uint256"},{"astId":48367,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"seniorTrancheDeployedValue","offset":0,"slot":52,"type":"t_uint256"},{"astId":48369,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"juniorTrancheIdleValue","offset":0,"slot":53,"type":"t_uint256"},{"astId":48371,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"juniorTrancheDeployedValue","offset":0,"slot":54,"type":"t_uint256"},{"astId":48373,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"equityTrancheIdleValue","offset":0,"slot":55,"type":"t_uint256"},{"astId":48375,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"equityTrancheDeployedValue","offset":0,"slot":56,"type":"t_uint256"},{"astId":48377,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"seniorTrancheTotalShares","offset":0,"slot":57,"type":"t_uint256"},{"astId":48381,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"seniorTrancheShares","offset":0,"slot":58,"type":"t_mapping(t_address,t_uint256)"},{"astId":48385,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"seniorTrancheDeposits","offset":0,"slot":59,"type":"t_mapping(t_address,t_uint256)"},{"astId":48389,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"seniorUserIndex","offset":0,"slot":60,"type":"t_mapping(t_address,t_uint256)"},{"astId":48391,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"juniorTrancheTotalShares","offset":0,"slot":61,"type":"t_uint256"},{"astId":48395,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"juniorTrancheShares","offset":0,"slot":62,"type":"t_mapping(t_address,t_uint256)"},{"astId":48399,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"juniorTrancheDeposits","offset":0,"slot":63,"type":"t_mapping(t_address,t_uint256)"},{"astId":48403,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"juniorUserIndex","offset":0,"slot":64,"type":"t_mapping(t_address,t_uint256)"},{"astId":48406,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"loanBorrowers","offset":0,"slot":65,"type":"t_array(t_address)dyn_storage"},{"astId":48411,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"recevingEntity","offset":0,"slot":66,"type":"t_address"},{"astId":48416,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"feeManager","offset":0,"slot":67,"type":"t_address"},{"astId":48418,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"totalIdleValue","offset":0,"slot":68,"type":"t_uint256"},{"astId":48420,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"totalDeployedValue","offset":0,"slot":69,"type":"t_uint256"},{"astId":48422,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"totalDeposited","offset":0,"slot":70,"type":"t_uint256"},{"astId":48424,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"totalLoss","offset":0,"slot":71,"type":"t_uint256"},{"astId":48426,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"totalRecovered","offset":0,"slot":72,"type":"t_uint256"},{"astId":48428,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"outStandingPrincipal","offset":0,"slot":73,"type":"t_uint256"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_address)dyn_storage":{"encoding":"dynamic_array","label":"address[]","numberOfBytes":32,"base":"t_address"},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_array(t_bytes4)dyn_storage":{"encoding":"dynamic_array","label":"bytes4[]","numberOfBytes":32,"base":"t_bytes4"},"t_array(t_string_storage)dyn_storage":{"encoding":"dynamic_array","label":"string[]","numberOfBytes":32,"base":"t_string_storage"},"t_array(t_struct(FuzzArtifactSelector)6914_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzArtifactSelector[]","numberOfBytes":32,"base":"t_struct(FuzzArtifactSelector)6914_storage"},"t_array(t_struct(FuzzInterface)6920_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzInterface[]","numberOfBytes":32,"base":"t_struct(FuzzInterface)6920_storage"},"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzSelector[]","numberOfBytes":32,"base":"t_struct(FuzzSelector)6908_storage"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_contract(CreditPolicy)42678":{"encoding":"inplace","label":"contract CreditPolicy","numberOfBytes":20},"t_contract(ERC20Mock)40221":{"encoding":"inplace","label":"contract ERC20Mock","numberOfBytes":20},"t_contract(LoanEngine)44023":{"encoding":"inplace","label":"contract LoanEngine","numberOfBytes":20},"t_contract(TranchePool)47199":{"encoding":"inplace","label":"contract TranchePool","numberOfBytes":20},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))"},"t_mapping(t_address,t_uint256)":{"encoding":"mapping","label":"mapping(address => uint256)","numberOfBytes":32,"key":"t_address","value":"t_uint256"},"t_mapping(t_bytes32,t_struct(FindData)8306_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)8306_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)8306_storage)"},"t_mapping(t_string_memory_ptr,t_string_storage)":{"encoding":"mapping","label":"mapping(string => string)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_string_storage"},"t_mapping(t_string_memory_ptr,t_struct(Chain)2959_storage)":{"encoding":"mapping","label":"mapping(string => struct StdChains.Chain)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_struct(Chain)2959_storage"},"t_mapping(t_uint256,t_string_storage)":{"encoding":"mapping","label":"mapping(uint256 => string)","numberOfBytes":32,"key":"t_uint256","value":"t_string_storage"},"t_string_memory_ptr":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(Chain)2959_storage":{"encoding":"inplace","label":"struct StdChains.Chain","numberOfBytes":128,"members":[{"astId":2952,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"name","offset":0,"slot":0,"type":"t_string_storage"},{"astId":2954,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"chainId","offset":0,"slot":1,"type":"t_uint256"},{"astId":2956,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"chainAlias","offset":0,"slot":2,"type":"t_string_storage"},{"astId":2958,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"rpcUrl","offset":0,"slot":3,"type":"t_string_storage"}]},"t_struct(FindData)8306_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":8299,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":8301,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":8303,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":8305,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(FuzzArtifactSelector)6914_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzArtifactSelector","numberOfBytes":64,"members":[{"astId":6910,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"artifact","offset":0,"slot":0,"type":"t_string_storage"},{"astId":6913,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(FuzzInterface)6920_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzInterface","numberOfBytes":64,"members":[{"astId":6916,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6919,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"artifacts","offset":0,"slot":1,"type":"t_array(t_string_storage)dyn_storage"}]},"t_struct(FuzzSelector)6908_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzSelector","numberOfBytes":64,"members":[{"astId":6904,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6907,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(StdStorage)8331_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":8315,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))"},{"astId":8318,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":8320,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":8322,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":8324,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":8326,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":8328,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":8330,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60808060405234610eeb575f9060808161586380380380916100218285610f88565b833981010312610eeb578051916001600160a01b0383168303610eeb5760208201516001600160a01b03811690819003610eeb5760408301516001600160a01b0381169390849003610eeb57606001516001600160a01b0381169290839003610eeb57600160ff19600c541617600c55600160ff19601f541617601f556040516100ac604082610f88565b6008815260208101673232b83637bcb2b960c11b815260405160208101906100ec60208286518087875e81015f838201520301601f198101835282610f88565b5190206040519063ffa1864960e01b825260048201526020816024815f5160206158435f395f51905f525afa908115610ee0575f91610f46575b505f5160206158435f395f51905f523b15610eeb575f906064604051809481936318caf8e360e31b835260018060a01b031696876004840152604060248401525180918160448501528484015e8181018301859052601f01601f19168101030181835f5160206158435f395f51905f525af18015610ee057610f31575b5060018060a01b03196023541617602355670de0b6b3a7640000602455600160ff196025541617602555506a52b7d2dcc80cd2e40000006026555f9369d3c21bcecceda10000006027556a108b2a2c28029094000000602855603260295560b4602a556101e0602b556001602f5560405161021f604082610f88565b600e8152602081016d7265636576696e67456e7469747960901b8152604051602081019061026560208286518087875e81015f838201520301601f198101835282610f88565b5190206040519063ffa1864960e01b825260048201526020816024815f5160206158435f395f51905f525afa908115610ee0575f91610eef575b505f5160206158435f395f51905f523b15610eeb575f906064604051809481936318caf8e360e31b835260018060a01b031696876004840152604060248401525180918160448501528484015e8181018301859052601f01601f19168101030181835f5160206158435f395f51905f525af18015610ee057610ecb575b5060018060a01b0319604254161760425560405161033b604082610f88565b600a81528560208201693332b2a6b0b730b3b2b960b11b8152604051602081019061037e60208287518087875e810187838201520301601f198101835282610f88565b5190206040519063ffa1864960e01b825260048201526020816024815f5160206158435f395f51905f525afa908115610798578391610e89575b505f5160206158435f395f51905f523b1561077f5782906064604051809481936318caf8e360e31b835260018060a01b031697886004840152604060248401525180918160448501528484015e8181018301859052601f01601f19168101030181835f5160206158435f395f51905f525af1801561077457610e70575b5050604380546001600160a01b0319908116929092179055601f8054610100600160a81b03191660089390931b610100600160a81b03169290921790915560208054821692909217909155602180548216929092179091556022805490911691909117905560235481906001600160a01b03165f5160206158435f395f51905f523b15610e6d57604051906303223eab60e11b825260048201528181602481835f5160206158435f395f51905f525af1801561077457610e58575b50601f546043546001600160a01b0360089290921c82169116813b15610e00578291604483926040519485938492631f9dd86960e21b84526004840152600160248401525af1801561077457610e43575b50601f546042546001600160a01b0360089290921c82169116813b15610e00578291604483926040519485938492630c1159b160e21b84526004840152600160248401525af1801561077457610e2e575b50601f546042546001600160a01b0360089290921c82169116813b15610e005782916044839260405194859384926319b52c2160e01b84526004840152600160248401525af1801561077457610e19575b50601f546042546001600160a01b0360089290921c82169116813b15610e0057829160448392604051948593849263ee48145560e01b84526004840152600160248401525af1801561077457610e04575b505060015b6001600160a01b038116606481101561094357602c546801000000000000000081101561092f576001810180602c5581101561091b57602c84527f7416c943b4a09859521022fd2e90eac0dd9026dad28fa317782a135f28a860910180546001600160a01b031916821790558290600183166107a3576021546001600160a01b0316803b1561077f578280916044604051809481936340c10f1960e01b83528760048401526b033b2e3c9fd0803ce800000060248401525af1908115610798578391610783575b50506020546001600160a01b031690813b1561077f578291604483926040519485938492630d392cd960e01b84526004840152600160248401525af180156107745761075b575b50505b6001016001600160a01b0316610639565b8161076591610f88565b61077057815f610747565b5080fd5b6040513d84823e3d90fd5b8280fd5b8161078d91610f88565b61077057815f610700565b6040513d85823e3d90fd5b6001600160a01b03600382061661087d576021546001600160a01b0316803b1561077f578280916044604051809481936340c10f1960e01b83528760048401526b1027e72f1f1281308800000060248401525af1908115610798578391610868575b50506020546001600160a01b031690813b1561077f578291604483926040519485938492630d392cd960e01b84526004840152600160248401525af1801561077457610853575b505061074a565b8161085d91610f88565b61077057815f61084c565b8161087291610f88565b61077057815f610805565b6021546001600160a01b0316803b1561077f578280916044604051809481936340c10f1960e01b83528760048401526c01431e0fae6d7217caa000000060248401525af19081156107985783916108685750506020546001600160a01b031690813b1561077f578291604483926040519485938492630d392cd960e01b84526004840152600160248401525af180156107745761085357505061074a565b634e487b7160e01b84526032600452602484fd5b634e487b7160e01b84526041600452602484fd5b8260015b6001600160a01b038116600a811015610b5c57602d546801000000000000000081101561092f576001810180602d5581101561091b57602d84527f4a2cc91ee622da3bc833a54c37ffcb6f3ec23b7793efc5eaf5e71b7b406c5c060180546001600160a01b03191682179055829060018316610a93576021546001600160a01b0316803b1561077f578280916044604051809481936340c10f1960e01b83528760048401526ba18f07d736b90be55000000060248401525af1908115610798578391610a7e575b50506020546001600160a01b031690813b1561077f578291604483926040519485938492630d392cd960e01b84526004840152600160248401525af1801561077457610a69575b50505b6001016001600160a01b0316610947565b81610a7391610f88565b610770578183610a55565b81610a8891610f88565b610770578185610a0e565b6020546001600160a01b0316803b1561077f57828091604460405180948193630d392cd960e01b8352876004840152600160248401525af1908115610798578391610b47575b50506021546001600160a01b031690813b1561077f5782916044839260405194859384926340c10f1960e01b845260048401526b204fce5e3e2502611000000060248401525af1801561077457610b32575b5050610a58565b81610b3c91610f88565b610770578183610b2b565b81610b5191610f88565b610770578185610ad9565b8260015b6001600160a01b0381166005811015610ca457602e546801000000000000000081101561092f576001810180602e5581101561091b57602e84527f37fa166cbdbfbb1561ccd9ea985ec0218b5e68502e230525f544285b2bdf3d7e0180546001600160a01b031916821790556021548391906001600160a01b0316803b1561077f578280916044604051809481936340c10f1960e01b83528760048401526b1027e72f1f1281308800000060248401525af1908115610798578391610c8f575b50506020546001600160a01b031690813b1561077f5782916044839260405194859384926307e95e9360e31b84526004840152600160248401525af1801561077457610c7a575b50506001016001600160a01b0316610b60565b81610c8491610f88565b610770578183610c67565b81610c9991610f88565b610770578185610c20565b8260c85b6001600160a01b03811660dc811015610d26576041546801000000000000000081101561092f57600181018060415581101561091b57604184527f7c9785e8241615bc80415d89775984a1337d15dc1bf4ce50f41988b2a2b336a70180546001600160a01b03191690911790556001016001600160a01b0316610ca8565b602154604254849182916001600160a01b039182169116813b15610e005782916044839260405194859384926340c10f1960e01b845260048401526b1027e72f1f1281308800000060248401525af1801561077457610deb575b50505f5160206158435f395f51905f523b15610de8576040516390c5013b60e01b81528181600481835f5160206158435f395f51905f525af1801561077457610dd3575b6040516148839081610fc08239f35b610dde828092610f88565b610de85780610dc4565b80fd5b81610df591610f88565b610de8578082610d80565b5050fd5b81610e0e91610f88565b610de857805f610634565b81610e2391610f88565b610de857805f6105e3565b81610e3891610f88565b610de857805f610592565b81610e4d91610f88565b610de857805f610541565b81610e6291610f88565b610de857805f6104f0565b50fd5b81610e7a91610f88565b610e8557855f610435565b8580fd5b90506020813d602011610ec3575b81610ea460209383610f88565b8101031261077f57516001600160a01b038116810361077f575f6103b8565b3d9150610e97565b610ed89196505f90610f88565b5f945f61031c565b6040513d5f823e3d90fd5b5f80fd5b90506020813d602011610f29575b81610f0a60209383610f88565b81010312610eeb57516001600160a01b0381168103610eeb575f61029f565b3d9150610efd565b610f3e9192505f90610f88565b5f905f6101a3565b90506020813d602011610f80575b81610f6160209383610f88565b81010312610eeb57516001600160a01b0381168103610eeb575f610126565b3d9150610f54565b601f909101601f19168101906001600160401b03821190821017610fab57604052565b634e487b7160e01b5f52604160045260245ffdfe6080806040526004361015610012575f80fd5b5f905f3560e01c9081630d457ee1146115e2575080631ed7831c1461156557806325cdcf0514611503578063291a147e146114a15780632ade3880146112e65780632d8d435d146112c95780632ec3ad92146112aa5780633964924b146112935780633b61f65e146112765780633e5e3c23146111f95780633f7286f41461117c578063406bf6701461115f57806341e8bc4d146110fd5780634644004d146110df578063472578311461107d5780634ba072ae146110605780634df2d3881461104357806350014f6b14611007578063507f253f14610dca578063574ca18614610db257806362b8144714610d9457806366d9a9a014610c7357806368f0c71314610c555780636a74c54814610c2a578063707baf37146105de5780637099c90c14610c0c57806376de06f314610bee5780637a2222dd14610bb15780637a493f2f14610b995780637be274e114610b7b5780638521834414610b5e57806385226c8114610ad457806385266e1814610aa957806389b7d92d1461055b5780638ade00b714610a6c5780638bc128f114610a4e5780638c8489f214610a365780638f38df91146109f9578063916a17c6146109515780639bddafe81461081a5780639e954fd0146107ef578063a3b93fff146107d1578063a6b590e8146107b8578063ac1335211461079a578063b0464fdc146106f2578063b5508aa914610668578063b7c9d5b61461064a578063b9fae65014610621578063ba414fa6146105fc578063bb3805fa146105de578063bb85e79c146105b5578063c54e44eb14610597578063ca1a6fbb14610579578063cab2845b1461044a578063cdf9329e1461055b578063d0fb020314610532578063d2beb926146104f6578063e20c9f7114610468578063e3e1de861461044a578063e51e43c2146103cd578063e691bb9e1461042c578063e9e97442146103eb578063eb78365c146103cd578063f5d6569614610389578063f860f2c81461036b578063fa7626d414610348578063fc5b08401461032a5763ff50abdc1461030a575f80fd5b346103275780600319360112610327576020604654604051908152f35b80fd5b50346103275780600319360112610327576020604454604051908152f35b5034610327578060031936011261032757602060ff601f54166040519015158152f35b50346103275780600319360112610327576020602754604051908152f35b50346103275760203660031901126103275760043590602d548210156103275760206103b4836116b5565b905460405160039290921b1c6001600160a01b03168152f35b50346103275780600319360112610327576020603354604051908152f35b5034610327576020366003190112610327576004356001600160a01b03811690819003610428578160409160209352603b83522054604051908152f35b5080fd5b50346103275780600319360112610327576020604954604051908152f35b50346103275780600319360112610327576020603d54604051908152f35b503461032757806003193601126103275760405160158054808352908352909160208301917f55f448fdea98c4d29eb340757ef0a66cd03dbb9538908a6a81d96026b71ec475915b8181106104d7576104d3856104c781870382611849565b604051918291826115fc565b0390f35b82546001600160a01b03168452602090930192600192830192016104b0565b5034610327576020366003190112610327576004356001600160a01b038116908190036104285781604091602093528183522054604051908152f35b50346103275780600319360112610327576043546040516001600160a01b039091168152602090f35b50346103275780600319360112610327576020603554604051908152f35b50346103275780600319360112610327576020604854604051908152f35b50346103275780600319360112610327576020602454604051908152f35b50346103275780600319360112610327576042546040516001600160a01b039091168152602090f35b50346103275780600319360112610327576020603954604051908152f35b5034610327578060031936011261032757602061061761445e565b6040519015158152f35b503461032757608036600319011261032757610647606435604435602435600435613d5f565b80f35b50346103275780600319360112610327576020603754604051908152f35b50346103275780600319360112610327576019546106858161188c565b916106936040519384611849565b818352601981527f944998273e477b495144fb8794c914197f3ccb46be2900f4698fd0ef743c9695602084015b8383106106d557604051806104d38782611729565b6001602081926106e4856118a4565b8152019201920191906106c0565b5034610327578060031936011261032757601c5461070f8161188c565b9161071d6040519384611849565b818352601c81527f0e4562a10381dec21b205ed72637e6b1b523bdd0e4d4d50af5cd23dd4500a211602084015b83831061075f57604051806104d387826117a2565b6002602060019260405161077281611819565b848060a01b038654168152610788858701612be8565b8382015281520192019201919061074a565b50346103275780600319360112610327576020602954604051908152f35b5034610327576106476107ca36611788565b5090613974565b50346103275780600319360112610327576020603854604051908152f35b50346103275760203660031901126103275760043590602e548210156103275760206103b483611711565b50346103275760203660031901126103275761083c61016d60016004356146a3565b818060405161084a81611819565b600c81526b109bdd5b99081c995cdd5b1d60a21b60208201526040516108a18161088d6020820194632d839cb360e21b865260406024840152606483019061163e565b87604483015203601f198101835282611849565b51906a636f6e736f6c652e6c6f675afa506201518081029080820462015180149015171561093d576108d482914261186b565b5f51602061482e5f395f51905f523b1561093a57604051906372eb5f8160e11b825260048201528181602481835f51602061482e5f395f51905f525af1801561092f5761091e5750f35b8161092891611849565b6103275780f35b6040513d84823e3d90fd5b50fd5b634e487b7160e01b82526011600452602482fd5b5034610327578060031936011261032757601d5461096e8161188c565b9161097c6040519384611849565b818352601d81527f6d4407e7be21f808e6509aa9fa9143369579dd7d760fe20a2c09680fc146134f602084015b8383106109be57604051806104d387826117a2565b600260206001926040516109d181611819565b848060a01b0386541681526109e7858701612be8565b838201528152019201920191906109a9565b5034610327576020366003190112610327576004356001600160a01b03811690819003610428578160409160209352603c83522054604051908152f35b503461032757610647610a4836611788565b91613551565b50346103275780600319360112610327576020603054604051908152f35b5034610327576020366003190112610327576004356001600160a01b03811690819003610428578160409160209352603f83522054604051908152f35b50346103275760203660031901126103275760043590602c548210156103275760206103b4836116e1565b5034610327578060031936011261032757601a54610af18161188c565b91610aff6040519384611849565b818352601a81527f057c384a7d1c54f3a1b2e5e67b2617b8224fdfd1ea7234eea573a6ff665ff63e602084015b838310610b4157604051806104d38782611729565b600160208192610b50856118a4565b815201920192019190610b2c565b5034610327576020366003190112610327576106476004356132bd565b50346103275780600319360112610327576020603154604051908152f35b503461032757610647610bab36611662565b90612dea565b5034610327576020366003190112610327576004356001600160a01b03811690819003610428578160409160209352603a83522054604051908152f35b50346103275780600319360112610327576020602f54604051908152f35b50346103275780600319360112610327576020602654604051908152f35b503461032757602036600319011261032757600435906041548210156103275760206103b4836116f9565b50346103275780600319360112610327576020603254604051908152f35b5034610327578060031936011261032757601b54610c908161188c565b610c9d6040519182611849565b818152601b83526020810191837f3ad8aa4f87544323a9d1e5dd902f40c356527a7955687113db5f9a85ad579dc1845b838310610d5957868587604051928392602084019060208552518091526040840160408260051b8601019392905b828210610d0a57505050500390f35b91936001919395506020610d498192603f198a820301865288519083610d39835160408452604084019061163e565b9201519084818403910152611678565b9601920192018594939192610cfb565b60026020600192604051610d6c81611819565b610d75866118a4565b8152610d82858701612be8565b83820152815201920192019190610ccd565b50346103275780600319360112610327576020603654604051908152f35b503461032757610647610dc436611662565b90612710565b5034610f21575f366003190112610f21576020805460405163217ac23760e01b81526001600160a01b039091169181600481855afa908115610f55575f91610fd8575b506004811015610fc457159081610f60575b50610e275780f35b6023546001600160a01b03165f51602061482e5f395f51905f523b15610f21576040519063ca669fa760e01b825260048201525f81602481835f51602061482e5f395f51905f525af18015610f5557610f42575b5060205481906001600160a01b0316803b1561093a578180916024604051809481936377dd846960e01b8352600160048401525af1801561092f57610f2d575b50506020805460405163b3d814f560e01b81529190829060049082906001600160a01b03165afa90811561092f578291610ef7575b5060465580f35b90506020813d602011610f25575b81610f1260209383611849565b81010312610f2157515f610ef0565b5f80fd5b3d9150610f05565b81610f3791611849565b61032757805f610ebb565b610f4e91505f90611849565b5f5f610e7b565b6040513d5f823e3d90fd5b60405163b3d814f560e01b81529150602090829060049082905afa908115610f55575f91610f92575b5015155f610e1f565b90506020813d602011610fbc575b81610fad60209383611849565b81010312610f2157515f610f89565b3d9150610fa0565b634e487b7160e01b5f52602160045260245ffd5b610ffa915060203d602011611000575b610ff28183611849565b810190611cd4565b5f610e0d565b503d610fe8565b34610f21576020366003190112610f21576004356001600160a01b03811690819003610f21575f52603e602052602060405f2054604051908152f35b34610f21575f366003190112610f21576020602854604051908152f35b34610f21575f366003190112610f21576020602b54604051908152f35b34610f21575f366003190112610f21575f5f90602d545b8083106110a657602082604051908152f35b906110d66001916110b6856116b5565b848060a01b0391549060031b1c165f52603e60205260405f20549061186b565b92019190611094565b34610f21576020366003190112610f21576110fb6004356122db565b005b34610f21575f366003190112610f21575f5f90602c545b80831061112657602082604051908152f35b90611156600191611136856116e1565b848060a01b0391549060031b1c165f52603a60205260405f20549061186b565b92019190611114565b34610f21575f366003190112610f21576020603454604051908152f35b34610f21575f366003190112610f2157604051601780548083525f91825260208301917fc624b66cc0138b8fabc209247f72d758e1cf3343756d543badbf24212bed8c1591905b8181106111da576104d3856104c781870382611849565b82546001600160a01b03168452602090930192600192830192016111c3565b34610f21575f366003190112610f2157604051601880548083525f91825260208301917fb13d2d76d1f4b7be834882e410b3e3a8afaf69f83600ae24db354391d2378d2e91905b818110611257576104d3856104c781870382611849565b82546001600160a01b0316845260209093019260019283019201611240565b34610f21575f366003190112610f21576020602a54604051908152f35b34610f21576110fb6112a436611662565b90611d3d565b34610f21576040366003190112610f21576110fb602435600435611a9e565b34610f21575f366003190112610f21576020604554604051908152f35b34610f21575f366003190112610f2157601e546113028161188c565b906113106040519283611849565b808252601e5f9081526020830191907f50bb669a95c7b50b7e8a6f09454034b2b14cf2b85c730dca9a539ca82cb6e350835b83831061141657848660405191829160208301906020845251809152604083019060408160051b85010192915f905b82821061138057505050500390f35b919390929450603f198682030182528451906020604082019260018060a01b0381511683520151916040602083015282518091526060820190602060608260051b8501019401925f5b8281106113eb5750505050506020806001929601920192018594939192611371565b9091929394602080611409600193605f19878203018952895161163e565b97019501939291016113c9565b60405161142281611819565b82546001600160a01b0316815260018301805461143e8161188c565b9161144c6040519384611849565b81835260208301905f5260205f20905f905b838210611484575050505060019282602092836002950152815201920192019190611342565b600160208192611493866118a4565b81520193019101909161145e565b34610f21575f366003190112610f21575f5f90602c545b8083106114ca57602082604051908152f35b906114fa6001916114da856116e1565b848060a01b0391549060031b1c165f52603b60205260405f20549061186b565b920191906114b8565b34610f21575f366003190112610f21575f5f90602d545b80831061152c57602082604051908152f35b9061155c60019161153c856116b5565b848060a01b0391549060031b1c165f52603f60205260405f20549061186b565b9201919061151a565b34610f21575f366003190112610f2157604051601680548083525f91825260208301917fd833147d7dc355ba459fc788f669e58cfaf9dc25ddcd0702e87d69c7b512428991905b8181106115c3576104d3856104c781870382611849565b82546001600160a01b03168452602090930192600192830192016115ac565b34610f21575f366003190112610f21576020906047548152f35b60206040818301928281528451809452019201905f5b81811061161f5750505090565b82516001600160a01b0316845260209384019390920191600101611612565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b6040906003190112610f21576004359060243590565b90602080835192838152019201905f5b8181106116955750505090565b82516001600160e01b031916845260209384019390920191600101611688565b602d548110156116cd57602d5f5260205f2001905f90565b634e487b7160e01b5f52603260045260245ffd5b602c548110156116cd57602c5f5260205f2001905f90565b6041548110156116cd5760415f5260205f2001905f90565b602e548110156116cd57602e5f5260205f2001905f90565b602081016020825282518091526040820191602060408360051b8301019401925f915b83831061175b57505050505090565b9091929394602080611779600193603f19868203018752895161163e565b9701930193019193929061174c565b6060906003190112610f2157600435906024359060443590565b602081016020825282518091526040820191602060408360051b8301019401925f915b8383106117d457505050505090565b909192939460208061180a600193603f198682030187526040838b51878060a01b03815116845201519181858201520190611678565b970193019301919392906117c5565b6040810190811067ffffffffffffffff82111761183557604052565b634e487b7160e01b5f52604160045260245ffd5b90601f8019910116810190811067ffffffffffffffff82111761183557604052565b9190820180921161187857565b634e487b7160e01b5f52601160045260245ffd5b67ffffffffffffffff81116118355760051b60200190565b90604051915f8154908160011c9260018316928315611966575b60208510841461195257848752869390811561193057506001146118ec575b506118ea92500383611849565b565b90505f9291925260205f20905f915b8183106119145750509060206118ea928201015f6118dd565b60209193508060019154838589010152019101909184926118fb565b9050602092506118ea94915060ff191682840152151560051b8201015f6118dd565b634e487b7160e01b5f52602260045260245ffd5b93607f16936118be565b90816020910312610f21575190565b5f1981146118785760010190565b9190820391821161187857565b9081610240910312610f215760405190610240820182811067ffffffffffffffff82111761183557604052805182526020810151602083015260408101516040830152606081015160ff81168103610f215760608301526080810151608083015260a081015160a083015260c081015160c083015260e081015160e08301526101008101516101008301526101208101516101208301526101408101516101408301526101608101516101608301526101808101516101808301526101a08101516101a08301526101c0810151906006821015610f2157610220916101c08401526101e08101516101e0840152610200810151610200840152015161022082015290565b601f54604051636146dd6f60e01b81525f9360089290921c6001600160a01b03169290602081600481875afa8015610f55575f90611ca1575b6001915014611c9b57611aeb60305461197f565b603055604051636146dd6f60e01b8152602081600481875afa908115610f55575f91611c69575b505f19810190811161187857611b2d610240916024936144f9565b93604051928380926366877b8d60e01b82528760048301525afa8015610f55576101c0915f91611c3a575b5001516006811015610fc45760011901611c35576023546001600160a01b03165f51602061482e5f395f51905f523b15610f21576040519063ca669fa760e01b825260048201525f81602481835f51602061482e5f395f51905f525af18015610f5557611c20575b50601f5460081c6001600160a01b031691823b15611c1c5790604484928360405195869485936321c221d760e01b8552600485015260248401525af1801561092f57611c0a575050565b611c15828092611849565b6103275750565b8380fd5b611c2d9193505f90611849565b5f915f611bc0565b505050565b611c5c91506102403d8111611c62575b611c548183611849565b81019061199a565b5f611b58565b503d611c4a565b90506020813d602011611c93575b81611c8460209383611849565b81010312610f2157515f611b12565b3d9150611c77565b50505050565b506020813d602011611ccc575b81611cbb60209383611849565b81010312610f215760019051611ad7565b3d9150611cae565b90816020910312610f2157516004811015610f215790565b8115611cf6570690565b634e487b7160e01b5f52601260045260245ffd5b90816020910312610f2157518015158103610f215790565b6001600160a01b039091168152602081019190915260400190565b6020805460405163217ac23760e01b81525f946001600160a01b0390921693919281600481875afa908115610f55575f916122bc575b506004811015610fc457611c9b57611d91611d9691602e5490611cec565b611711565b905460405163469fab6f60e11b815260039290921b1c6001600160a01b031691602082600481875afa918215610f55575f92612288575b50604051635d8d43b960e11b815291602083600481885afa918215610f55575f92612252575b611dfd9350614589565b91604051635b00b19760e11b8152602081600481855afa8015610f55575f9061221e575b611e2c91508461186b565b60405163338ef3f160e01b815290602082600481865afa908115610f55575f916121e8575b611e5b925061186b565b604051635d8d43b960e11b815290602082600481865afa918215610f55575f926121b4575b501161202a575b508115611c35575f51602061482e5f395f51905f523b15610f2157604051906303223eab60e11b825260048201525f81602481835f51602061482e5f395f51905f525af18015610f5557612015575b506021546020805460405163095ea7b360e01b81529283916001600160a01b0391821691839188918391611f10918a911660048401611d22565b03925af18015611fd957611fe8575b506020546001600160a01b0316803b15611fe457828091602460405180948193637a3ad89360e01b83528760048401525af18015611fd957908391611fc4575b505080611f71611f7c9260375461186b565b60375560445461186b565b6044555f51602061482e5f395f51905f523b15610327576040516390c5013b60e01b81528181600481835f51602061482e5f395f51905f525af1801561092f57611c0a575050565b81611fce91611849565b61042857815f611f5f565b6040513d85823e3d90fd5b8280fd5b6120099060203d60201161200e575b6120018183611849565b810190611d0a565b611f1f565b503d611ff7565b6120229192505f90611849565b5f905f611ed6565b604051635d8d43b960e11b8152909250602081600481865afa908115610f55575f91612182575b50604051635b00b19760e11b815290602082600481875afa908115610f55575f9161214c575b612081925061198d565b60405163338ef3f160e01b815290602082600481875afa918215610f55575f92612116575b506120b560049260209261198d565b936040519283809263469fab6f60e11b82525afa908115610f55575f916120e4575b508210611c35575f611e87565b90506020813d60201161210e575b816120ff60209383611849565b81010312610f2157515f6120d7565b3d91506120f2565b91506020823d602011612144575b8161213160209383611849565b81010312610f21579051906120b56120a6565b3d9150612124565b90506020823d60201161217a575b8161216760209383611849565b81010312610f2157612081915190612077565b3d915061215a565b90506020813d6020116121ac575b8161219d60209383611849565b81010312610f2157515f612051565b3d9150612190565b9091506020813d6020116121e0575b816121d060209383611849565b81010312610f215751905f611e80565b3d91506121c3565b90506020823d602011612216575b8161220360209383611849565b81010312610f2157611e5b915190611e51565b3d91506121f6565b506020813d60201161224a575b8161223860209383611849565b81010312610f2157611e2c9051611e21565b3d915061222b565b91506020833d602011612280575b8161226d60209383611849565b81010312610f2157611dfd925191611df3565b3d9150612260565b9091506020813d6020116122b4575b816122a460209383611849565b81010312610f215751905f611dcd565b3d9150612297565b6122d5915060203d60201161100057610ff28183611849565b5f611d73565b601f54604051636146dd6f60e01b81525f929160081c6001600160a01b031690602081600481855afa8015610f55575f906126dd575b600191500361266b575b6040516366877b8d60e01b81526004810183905261024081602481855afa8015610f55576101c0915f9161264c575b5001516006811015610fc4575f1901611c3557610240602491604051928380926366877b8d60e01b82528660048301525afa908115610f55576004916080915f9161262d575b5001516020805460405163b3d814f560e01b815293849182906001600160a01b03165afa918215610f55575f926125f9575b50116125f5576023546001600160a01b03165f51602061482e5f395f51905f523b15610f21576040519063ca669fa760e01b825260048201525f81602481835f51602061482e5f395f51905f525af18015610f55576125e0575b50601f5460425460435460089290921c6001600160a01b039081169281169116823b156125dc5790606485928360405195869485936319e4bc1160e01b8552896004860152602485015260448401525af18015611fd9579083916125c7575b5050601f546040516366877b8d60e01b81526004810183905260089190911c6001600160a01b0316919061024081602481865afa90811561259d576124cf9160809186916125a8575b50015160455461186b565b6045556040516366877b8d60e01b81526004810182905261024081602481865afa90811561259d5760806102409392612514928791612580575b50015160445461198d565b6044556024604051809481936366877b8d60e01b835260048301525afa918215612574576125509260809290612555575b50015160495461186b565b604955565b61256e91506102403d8111611c6257611c548183611849565b5f612545565b604051903d90823e3d90fd5b6125979150853d8111611c6257611c548183611849565b5f612509565b6040513d86823e3d90fd5b6125c191506102403d8111611c6257611c548183611849565b5f6124c4565b816125d191611849565b61042857815f61247b565b8480fd5b6125ed9192505f90611849565b5f905f61241c565b5050565b9091506020813d602011612625575b8161261560209383611849565b81010312610f215751905f6123c2565b3d9150612608565b61264691506102403d8111611c6257611c548183611849565b5f612390565b61266591506102403d8111611c6257611c548183611849565b5f61234a565b90604051636146dd6f60e01b8152602081600481865afa908115610f55575f916126ab575b505f198101908111611878576126a5916144f9565b9061231b565b90506020813d6020116126d5575b816126c660209383611849565b81010312610f2157515f612690565b3d91506126b9565b506020813d602011612708575b816126f760209383611849565b81010312610f215760019051612311565b3d91506126ea565b6020805460405163217ac23760e01b81525f94936001600160a01b039092169281600481865afa908115610f55575f91612bc9575b506004811015610fc457611c9b5761276361276891602d5490611cec565b6116b5565b90546040516341b77a6760e11b815260039290921b1c6001600160a01b031692602082600481865afa918215610f55575f92612b95575b5060405163088eafbd60e21b815291602083600481875afa918215610f55575f92612b5f575b6127cf9350614589565b906035546127dd818461186b565b906127eb603654809361186b565b60405163088eafbd60e21b815290602082600481885afa918215610f55575f92612b2b575b5011612a52575b5050508015611c35575f51602061482e5f395f51905f523b15610f21576040516303223eab60e11b8152600481018390525f81602481835f51602061482e5f395f51905f525af18015610f5557612a3d575b506021546020805460405163095ea7b360e01b81529283916001600160a01b03918216918391899183916128a3918a911660048401611d22565b03925af1801561259d57612a20575b506020546001600160a01b0316803b15611c1c57838091602460405180948193637c2c195160e01b83528760048401525af1801561259d57908491612a0b575b5050906129538261290760049460355461186b565b603555828552603f6020526040852061292182825461186b565b9055828552603e6020526040852061293a82825461186b565b905561294881603d5461186b565b603d5560445461186b565b60445560208054604051633638f70360e01b815293849182906001600160a01b03165afa918215611fd95783926129d7575b508252604060205260408220555f51602061482e5f395f51905f523b15610327576040516390c5013b60e01b81528181600481835f51602061482e5f395f51905f525af1801561092f57611c0a575050565b9091506020813d602011612a03575b816129f360209383611849565b81010312610f215751905f612985565b3d91506129e6565b81612a1591611849565b611fe457825f6128f2565b612a389060203d60201161200e576120018183611849565b6128b2565b612a4a9193505f90611849565b5f915f612869565b60405163088eafbd60e21b81529293509091602081600481875afa908115610f55575f91612af6575b50600492612a8e602093612a939361198d565b61198d565b92604051928380926341b77a6760e11b82525afa908115610f55575f91612ac4575b508110611c35575f8080612817565b90506020813d602011612aee575b81612adf60209383611849565b81010312610f2157515f612ab5565b3d9150612ad2565b9190506020823d602011612b23575b81612b1260209383611849565b81010312610f215790516004612a7b565b3d9150612b05565b9091506020813d602011612b57575b81612b4760209383611849565b81010312610f215751905f612810565b3d9150612b3a565b91506020833d602011612b8d575b81612b7a60209383611849565b81010312610f21576127cf9251916127c5565b3d9150612b6d565b9091506020813d602011612bc1575b81612bb160209383611849565b81010312610f215751905f61279f565b3d9150612ba4565b612be2915060203d60201161100057610ff28183611849565b5f612745565b90604051918281549182825260208201905f5260205f20925f905b806007830110612d45576118ea945491818110612d26575b818110612d07575b818110612ce8575b818110612cc9575b818110612caa575b818110612c8b575b818110612c6e575b10612c59575b500383611849565b6001600160e01b03191681526020015f612c51565b602083811b6001600160e01b031916855290930192600101612c4b565b604083901b6001600160e01b0319168452602090930192600101612c43565b606083901b6001600160e01b0319168452602090930192600101612c3b565b608083901b6001600160e01b0319168452602090930192600101612c33565b60a083901b6001600160e01b0319168452602090930192600101612c2b565b60c083901b6001600160e01b0319168452602090930192600101612c23565b60e083901b6001600160e01b0319168452602090930192600101612c1b565b916008919350610100600191865463ffffffff60e01b8160e01b16825263ffffffff60e01b8160c01b16602083015263ffffffff60e01b8160a01b16604083015263ffffffff60e01b8160801b16606083015263ffffffff60e01b8160601b16608083015263ffffffff60e01b8160401b1660a083015263ffffffff60e01b8160201b1660c083015263ffffffff60e01b1660e0820152019401920185929391612c03565b6020805460405163217ac23760e01b81525f94936001600160a01b039092169281600481865afa908115610f55575f9161329e575b506004811015610fc457611c9b57612e3d612e4291602c5490611cec565b6116e1565b9054604051633b6e159160e01b815260039290921b1c6001600160a01b031692602082600481865afa918215610f55575f9261326a575b506040516306fa495360e41b815291602083600481875afa918215610f55575f92613234575b612ea99350614589565b90603354612eb7818461186b565b90612ec5603454809361186b565b6040516306fa495360e41b815290602082600481885afa918215610f55575f92613200575b501161312c575b5050508015611c35575f51602061482e5f395f51905f523b15610f21576040516303223eab60e11b8152600481018390525f81602481835f51602061482e5f395f51905f525af18015610f5557613117575b506021546020805460405163095ea7b360e01b81529283916001600160a01b0391821691839189918391612f7d918a911660048401611d22565b03925af1801561259d576130fa575b506020546001600160a01b0316803b15611c1c578380916024604051809481936302ad35ed60e51b83528760048401525af1801561259d579084916130e5575b50509061302d82612fe160049460335461186b565b603355828552603b60205260408520612ffb82825461186b565b9055828552603a6020526040852061301482825461186b565b90556130228160395461186b565b60395560445461186b565b6044556020805460405163415b47c560e01b815293849182906001600160a01b03165afa918215611fd95783926130b1575b508252603c60205260408220555f51602061482e5f395f51905f523b15610327576040516390c5013b60e01b81528181600481835f51602061482e5f395f51905f525af1801561092f57611c0a575050565b9091506020813d6020116130dd575b816130cd60209383611849565b81010312610f215751905f61305f565b3d91506130c0565b816130ef91611849565b611fe457825f612fcc565b6131129060203d60201161200e576120018183611849565b612f8c565b6131249193505f90611849565b5f915f612f43565b6040516306fa495360e41b81529293509091602081600481875afa908115610f55575f916131cb575b50600492612a8e6020936131689361198d565b9260405192838092633b6e159160e01b82525afa908115610f55575f91613199575b508110611c35575f8080612ef1565b90506020813d6020116131c3575b816131b460209383611849565b81010312610f2157515f61318a565b3d91506131a7565b9190506020823d6020116131f8575b816131e760209383611849565b81010312610f215790516004613155565b3d91506131da565b9091506020813d60201161322c575b8161321c60209383611849565b81010312610f215751905f612eea565b3d915061320f565b91506020833d602011613262575b8161324f60209383611849565b81010312610f2157612ea9925191612e9f565b3d9150613242565b9091506020813d602011613296575b8161328660209383611849565b81010312610f215751905f612e79565b3d9150613279565b6132b7915060203d60201161100057610ff28183611849565b5f612e1f565b601f54604051636146dd6f60e01b815260089190911c6001600160a01b0316915f91602081600481875afa8015610f55575f9061351e575b6001915014611c355761330960315461197f565b603155604051636146dd6f60e01b8152602081600481875afa908115610f55575f916134ec575b505f19810190811161187857613345916144f9565b916040516366877b8d60e01b815283600482015261024081602481855afa8015610f55576101c0915f916134cd575b5001516006811015610fc45760031901611c3557610240602491604051928380926366877b8d60e01b82528760048301525afa8015610f555760a0915f916134ae575b5001516023549092906001600160a01b03165f51602061482e5f395f51905f523b15610f21576040519063ca669fa760e01b825260048201525f81602481835f51602061482e5f395f51905f525af18015610f5557613499575b50601f5460081c6001600160a01b031690813b15611fe4578291602483926040519485938492631c9f7dd760e21b845260048401525af1801561092f57613484575b50508061346561347f9260455461198d565b6045556134748160495461198d565b60495560475461186b565b604755565b61348f828092611849565b6103275780613453565b6134a69192505f90611849565b5f905f613411565b6134c791506102403d8111611c6257611c548183611849565b5f6133b7565b6134e691506102403d8111611c6257611c548183611849565b5f613374565b90506020813d602011613516575b8161350760209383611849565b81010312610f2157515f613330565b3d91506134fa565b506020813d602011613549575b8161353860209383611849565b81010312610f2157600190516132f5565b3d915061352b565b601f54604051636146dd6f60e01b815291935f939092909160081c6001600160a01b031690602081600481855afa8015610f55575f9061392e575b60019150146138d457604051636146dd6f60e01b8152602081600481855afa908115610f55575f916138fc575b505f198101908111611878576135d4610240916024976144f9565b91604051968780926366877b8d60e01b82528560048301525afa948515610f55575f956138db575b506101c08501516006811015610fc457600119016138d45761362460a086019283519061457e565b9161364861364161010061363785614594565b980197885161186b565b809561457e565b93831580806138cc575b6138c2571590816138b9575b816138af575b506138a757613687613676858561186b565b965161368184614594565b9061186b565b8087101561389e575061369b865b8761198d565b9051808210156138965750945b6042546001600160a01b03165f51602061482e5f395f51905f523b15610f21576040519063ca669fa760e01b825260048201525f81602481835f51602061482e5f395f51905f525af18015610f5557613880575b50602154601f5460405163095ea7b360e01b81529260209284926001600160a01b039182169284928b92849261373b92909160081c1660048401611d22565b03925af1801561385857613863575b506023546001600160a01b03165f51602061482e5f395f51905f523b156125dc576040519063ca669fa760e01b825260048201528481602481835f51602061482e5f395f51905f525af1801561385857908591613843575b5050601f546042546001600160a01b0360089290921c82169116813b1561383f5791856084928195946040519788968795630b43a5bf60e11b875260048701526024860152604485015260648401525af1801561092f5761382a575b5050806138106125509260455461198d565b60455561381f8160445461186b565b60445560495461198d565b613835828092611849565b61032757806137fe565b8580fd5b8161384d91611849565b611c1c57835f6137a2565b6040513d87823e3d90fd5b61387b9060203d60201161200e576120018183611849565b61374a565b61388d9195505f90611849565b5f9360206136fc565b9050946136a8565b61369b90613695565b505050505050565b905015155f613664565b8515915061365e565b5050505050505050565b508515613652565b5050505050565b6138f59195506102403d8111611c6257611c548183611849565b935f6135fc565b90506020813d602011613926575b8161391760209383611849565b81010312610f2157515f6135b9565b3d915061390a565b506020813d602011613959575b8161394860209383611849565b81010312610f21576001905161358c565b3d915061393b565b8181029291811591840414171561187857565b601f54604051636146dd6f60e01b815291925f9260089290921c6001600160a01b031691602081600481865afa8015610f55575f90613d2c575b6001915014611c9b57601e6139c460325461197f565b8060325506611c9b57604051636146dd6f60e01b8152602081600481865afa908115610f55575f91613cfa575b505f19810190811161187857613a0c610240916024966144f9565b92604051958680926366877b8d60e01b82528660048301525afa938415610f55575f94613cd9575b506101c08401516006811015610fc45760041901611c9b57613a6690608060018060a01b0360425416950151906144f9565b925f51602061482e5f395f51905f523b15610f21576040516303223eab60e11b8152600481018290525f81602481835f51602061482e5f395f51905f525af18015610f5557613cc4575b506021546001600160a01b0316803b15611c1c578360405180926340c10f1960e01b8252818381613ae58b8960048401611d22565b03925af1801561259d57908491613caf575b5050613b3560208560018060a01b036021541660018060a01b03601f5460081c168760405180968195829463095ea7b360e01b845260048401611d22565b03925af1801561259d57613c92575b505f51602061482e5f395f51905f523b15611fe4576040516390c5013b60e01b81528381600481835f51602061482e5f395f51905f525af1801561259d57908491613c7d575b50506023546001600160a01b03165f51602061482e5f395f51905f523b15611c1c576040519063ca669fa760e01b825260048201528381602481835f51602061482e5f395f51905f525af1801561259d57908491613c68575b5050601f5460081c6001600160a01b031691823b15611c1c5790606484928360405195869485936348abb7e360e01b8552600485015289602485015260448401525af1801561092f57613c53575b505080613c43613c4e9260445461186b565b60445560485461186b565b604855565b613c5e828092611849565b6103275780613c31565b81613c7291611849565b611fe457825f613be3565b81613c8791611849565b611fe457825f613b8a565b613caa9060203d60201161200e576120018183611849565b613b44565b81613cb991611849565b611fe457825f613af7565b613cd19193505f90611849565b5f915f613ab0565b613cf39194506102403d8111611c6257611c548183611849565b925f613a34565b90506020813d602011613d24575b81613d1560209383611849565b81010312610f2157515f6139f1565b3d9150613d08565b506020813d602011613d57575b81613d4660209383611849565b81010312610f2157600190516139ae565b3d9150613d39565b6020805460405163217ac23760e01b81525f969495936001600160a01b039092169281600481865afa908115610f55575f9161443f575b506004811015610fc45760011415806143e8575b6138a7576027549060ff602554165f1461436f5760405163b3d814f560e01b8152602081600481875afa8015610f555783915f9161433a575b50106142e4575b60405163b3d814f560e01b8152602081600481875afa8015610f555783915f916142af575b50106142a65760285460405163b3d814f560e01b81529290602084600481885afa8015610f55575f90614272575b613e5194508082101561426a575091614589565b9060405163b3d814f560e01b8152602081600481855afa8015610f55575f90614237575b600a91500482116141d1575b50602954601f54604051636780f97760e01b815260089190911c6001600160a01b0316956020826004818a5afa918215610f55575f9261419b575b5090613ed892613ecb92614589565b92602a54602b5491614589565b60018060a01b03602254166020602f54602460405180948193634c2d62b760e01b835260048301525afa908115610f55575f9161417c575b50156138a7576004906020613f2f613f2a60415488611cec565b6116f9565b90549060031b1c604051828101916bffffffffffffffffffffffff199060601b16825287603482015260348152613f67605482611849565b5190209660405193848092636146dd6f60e01b82525afa918215610f55575f92614148575b50604051918060208401528560408401528360608401528460808401528160a084015260a08352613fbe60c084611849565b6023546001600160a01b03165f51602061482e5f395f51905f523b15610f21576040519063ca669fa760e01b825260048201525f81602481835f51602061482e5f395f51905f525af18015610f5557614133575b5060018060a01b03601f5460081c1695604051906020820192835260408201528760608201524260808201526080815261404d60a082611849565b51902093602f5493602094604051966140668789611849565b8a88525f368137883b1561412f5760405163d63792a760e01b8152600481019a909a5260248a015260448901526001606489015260848801526101f460a488015260c487015260e4860152610104850186905261016061012486015285938593909290916140d99061016486019061163e565b84810360031901610144860152825180825290820192820191865b82811061411557505050508383809203925af1801561092f57611c0a575050565b8351855289975088965093810193928101926001016140f4565b8a80fd5b6141409198505f90611849565b5f965f614012565b9091506020813d602011614174575b8161416460209383611849565b81010312610f215751905f613f8c565b3d9150614157565b614195915060203d60201161200e576120018183611849565b5f613f10565b91506020823d6020116141c9575b816141b660209383611849565b81010312610f2157905190613ed8613ebc565b3d91506141a9565b60405163b3d814f560e01b81529150602090829060049082905afa8015610f55575f90614204575b600a9150045f613e81565b506020813d60201161422f575b8161421e60209383611849565b81010312610f2157600a90516141f9565b3d9150614211565b506020813d602011614262575b8161425160209383611849565b81010312610f2157600a9051613e75565b3d9150614244565b905091614589565b506020843d60201161429e575b8161428c60209383611849565b81010312610f2157613e519351613e3d565b3d915061427f565b50505050505050565b9150506020813d6020116142dc575b816142cb60209383611849565b81010312610f21578290515f613e0f565b3d91506142be565b60405163b3d814f560e01b8152602081600481875afa8015610f555761430b575b50613dea565b61432c9060203d602011614333575b6143248183611849565b810190611970565b505f614305565b503d61431a565b9150506020813d602011614367575b8161435660209383611849565b81010312610f21578290515f613de3565b3d9150614349565b60405163b3d814f560e01b8152602081600481875afa908115610f55575f916143b6575b50600a830290838204600a1484151715611878571015613dea5750505050505050565b90506020813d6020116143e0575b816143d160209383611849565b81010312610f2157515f614393565b3d91506143c4565b5060405163217ac23760e01b8152602081600481865afa908115610f55575f91614420575b506004811015610fc45760021415613daa565b614439915060203d60201161100057610ff28183611849565b5f61440d565b614458915060203d60201161100057610ff28183611849565b5f613d96565b60085460ff161561446e57600190565b604051630667f9d760e41b81525f51602061482e5f395f51905f5260048201526519985a5b195960d21b60248201526020816044815f51602061482e5f395f51905f525afa908115610f55575f916144c7575b50151590565b90506020813d6020116144f1575b816144e260209383611849565b81010312610f2157515f6144c1565b3d91506144d5565b906001614505926146a3565b905f8060405161451481611819565b600c81526b109bdd5b99081c995cdd5b1d60a21b602082015260405161456b816145576020820194632d839cb360e21b865260406024840152606483019061163e565b88604483015203601f198101835282611849565b51906a636f6e736f6c652e6c6f675afa50565b905f614505926146a3565b9061450592916146a3565b601f54604051636146dd6f60e01b815260089190911c6001600160a01b031691602082600481865afa918215610f55575f9261466f575b505f19820191821161187857610240916145e4916144f9565b6024604051809481936366877b8d60e01b835260048301525afa908115610f55575f91614650575b5061461c6101408201514261198d565b60a0820151908115614649576146406146459260c064496cebb80095015190613961565b613961565b0490565b5050505f90565b61466991506102403d8111611c6257611c548183611849565b5f61460c565b9091506020813d60201161469b575b8161468b60209383611849565b81010312610f215751905f6145cb565b3d915061467e565b5f908383116147c257828110918215806147b8575b6147b0576146c6848661198d565b9260018401809411611878576003831115806147a7575b614798576003198310158061478e575b61477a5785831115614732575050906147098461470e9361198d565b611cec565b90811561472d5761471f925061186b565b5f1981019081116118785790565b505090565b9594929190956147425750505050565b8394955061470990614754939461198d565b90811561472d57614765925061198d565b6001810180911161187857905f808080611c9b565b5050905061478b929150199061198d565b90565b50821984116146ed565b505091905061478b925061186b565b508284116146dd565b509250505090565b50848211156146b8565b60405162461bcd60e51b815260206004820152603e60248201527f5374645574696c7320626f756e642875696e743235362c75696e743235362c7560448201527f696e74323536293a204d6178206973206c657373207468616e206d696e2e00006064820152608490fdfe0000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da26469706673582212201597b4f3cae672f9776982316ebf88df8cfce9a9b6621f65e60ea945dcea28c864736f6c634300082100330000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12d"

    @overload
    @classmethod
    def deploy(cls, _loanEngine: LoanEngine, _tranchePool: TranchePool, _creditPolicy: CreditPolicy, _usdt: ERC20Mock, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#66)

        Args:
            _loanEngine: contract LoanEngine
            _tranchePool: contract TranchePool
            _creditPolicy: contract CreditPolicy
            _usdt: contract ERC20Mock
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _loanEngine: LoanEngine, _tranchePool: TranchePool, _creditPolicy: CreditPolicy, _usdt: ERC20Mock, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Handler:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#66)

        Args:
            _loanEngine: contract LoanEngine
            _tranchePool: contract TranchePool
            _creditPolicy: contract CreditPolicy
            _usdt: contract ERC20Mock
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _loanEngine: LoanEngine, _tranchePool: TranchePool, _creditPolicy: CreditPolicy, _usdt: ERC20Mock, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#66)

        Args:
            _loanEngine: contract LoanEngine
            _tranchePool: contract TranchePool
            _creditPolicy: contract CreditPolicy
            _usdt: contract ERC20Mock
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _loanEngine: LoanEngine, _tranchePool: TranchePool, _creditPolicy: CreditPolicy, _usdt: ERC20Mock, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#66)

        Args:
            _loanEngine: contract LoanEngine
            _tranchePool: contract TranchePool
            _creditPolicy: contract CreditPolicy
            _usdt: contract ERC20Mock
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _loanEngine: LoanEngine, _tranchePool: TranchePool, _creditPolicy: CreditPolicy, _usdt: ERC20Mock, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Handler]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#66)

        Args:
            _loanEngine: contract LoanEngine
            _tranchePool: contract TranchePool
            _creditPolicy: contract CreditPolicy
            _usdt: contract ERC20Mock
        """
        ...

    @classmethod
    def deploy(cls, _loanEngine: LoanEngine, _tranchePool: TranchePool, _creditPolicy: CreditPolicy, _usdt: ERC20Mock, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, Handler, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[Handler]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#66)

        Args:
            _loanEngine: contract LoanEngine
            _tranchePool: contract TranchePool
            _creditPolicy: contract CreditPolicy
            _usdt: contract ERC20Mock
        """
        return cls._deploy(request_type, [_loanEngine, _tranchePool, _creditPolicy, _usdt], return_tx, Handler, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#17)

        Returns:
            USDT: uint256
        """
        ...

    @overload
    def USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#17)

        Returns:
            USDT: uint256
        """
        ...

    @overload
    def USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#17)

        Returns:
            USDT: uint256
        """
        ...

    @overload
    def USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#17)

        Returns:
            USDT: uint256
        """
        ...

    def USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#17)

        Returns:
            USDT: uint256
        """
        return self._execute(self.chain, request_type, "c54e44eb", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def expectedPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#20)

        Returns:
            expectedPrincipal: uint256
        """
        ...

    @overload
    def expectedPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#20)

        Returns:
            expectedPrincipal: uint256
        """
        ...

    @overload
    def expectedPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#20)

        Returns:
            expectedPrincipal: uint256
        """
        ...

    @overload
    def expectedPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#20)

        Returns:
            expectedPrincipal: uint256
        """
        ...

    def expectedPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#20)

        Returns:
            expectedPrincipal: uint256
        """
        return self._execute(self.chain, request_type, "7099c90c", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def minimumLoanPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#21)

        Returns:
            minimumLoanPrincipal: uint256
        """
        ...

    @overload
    def minimumLoanPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#21)

        Returns:
            minimumLoanPrincipal: uint256
        """
        ...

    @overload
    def minimumLoanPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#21)

        Returns:
            minimumLoanPrincipal: uint256
        """
        ...

    @overload
    def minimumLoanPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#21)

        Returns:
            minimumLoanPrincipal: uint256
        """
        ...

    def minimumLoanPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#21)

        Returns:
            minimumLoanPrincipal: uint256
        """
        return self._execute(self.chain, request_type, "f860f2c8", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def maximumLoanPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#22)

        Returns:
            maximumLoanPrincipal: uint256
        """
        ...

    @overload
    def maximumLoanPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#22)

        Returns:
            maximumLoanPrincipal: uint256
        """
        ...

    @overload
    def maximumLoanPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#22)

        Returns:
            maximumLoanPrincipal: uint256
        """
        ...

    @overload
    def maximumLoanPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#22)

        Returns:
            maximumLoanPrincipal: uint256
        """
        ...

    def maximumLoanPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#22)

        Returns:
            maximumLoanPrincipal: uint256
        """
        return self._execute(self.chain, request_type, "4df2d388", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def minimumOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#23)

        Returns:
            minimumOriginationFeeBps: uint256
        """
        ...

    @overload
    def minimumOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#23)

        Returns:
            minimumOriginationFeeBps: uint256
        """
        ...

    @overload
    def minimumOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#23)

        Returns:
            minimumOriginationFeeBps: uint256
        """
        ...

    @overload
    def minimumOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#23)

        Returns:
            minimumOriginationFeeBps: uint256
        """
        ...

    def minimumOriginationFeeBps(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#23)

        Returns:
            minimumOriginationFeeBps: uint256
        """
        return self._execute(self.chain, request_type, "ac133521", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def minimumTermDays(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#24)

        Returns:
            minimumTermDays: uint256
        """
        ...

    @overload
    def minimumTermDays(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#24)

        Returns:
            minimumTermDays: uint256
        """
        ...

    @overload
    def minimumTermDays(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#24)

        Returns:
            minimumTermDays: uint256
        """
        ...

    @overload
    def minimumTermDays(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#24)

        Returns:
            minimumTermDays: uint256
        """
        ...

    def minimumTermDays(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#24)

        Returns:
            minimumTermDays: uint256
        """
        return self._execute(self.chain, request_type, "3b61f65e", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def maximumTermDays(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#25)

        Returns:
            maximumTermDays: uint256
        """
        ...

    @overload
    def maximumTermDays(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#25)

        Returns:
            maximumTermDays: uint256
        """
        ...

    @overload
    def maximumTermDays(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#25)

        Returns:
            maximumTermDays: uint256
        """
        ...

    @overload
    def maximumTermDays(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#25)

        Returns:
            maximumTermDays: uint256
        """
        ...

    def maximumTermDays(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#25)

        Returns:
            maximumTermDays: uint256
        """
        return self._execute(self.chain, request_type, "4ba072ae", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def seniorUsers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#26)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    @overload
    def seniorUsers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#26)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    @overload
    def seniorUsers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#26)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    @overload
    def seniorUsers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#26)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    def seniorUsers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#26)

        Args:
            index0: uint256
        Returns:
            address
        """
        return self._execute(self.chain, request_type, "85266e18", [index0], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def juniorUsers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#27)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    @overload
    def juniorUsers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#27)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    @overload
    def juniorUsers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#27)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    @overload
    def juniorUsers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#27)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    def juniorUsers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#27)

        Args:
            index0: uint256
        Returns:
            address
        """
        return self._execute(self.chain, request_type, "f5d65696", [index0], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def equityUsers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#28)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    @overload
    def equityUsers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#28)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    @overload
    def equityUsers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#28)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    @overload
    def equityUsers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#28)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    def equityUsers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#28)

        Args:
            index0: uint256
        Returns:
            address
        """
        return self._execute(self.chain, request_type, "9e954fd0", [index0], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def activePolicyVersion(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#29)

        Returns:
            activePolicyVersion: uint256
        """
        ...

    @overload
    def activePolicyVersion(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#29)

        Returns:
            activePolicyVersion: uint256
        """
        ...

    @overload
    def activePolicyVersion(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#29)

        Returns:
            activePolicyVersion: uint256
        """
        ...

    @overload
    def activePolicyVersion(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#29)

        Returns:
            activePolicyVersion: uint256
        """
        ...

    def activePolicyVersion(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#29)

        Returns:
            activePolicyVersion: uint256
        """
        return self._execute(self.chain, request_type, "76de06f3", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def defaultCounter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#30)

        Returns:
            defaultCounter: uint256
        """
        ...

    @overload
    def defaultCounter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#30)

        Returns:
            defaultCounter: uint256
        """
        ...

    @overload
    def defaultCounter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#30)

        Returns:
            defaultCounter: uint256
        """
        ...

    @overload
    def defaultCounter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#30)

        Returns:
            defaultCounter: uint256
        """
        ...

    def defaultCounter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#30)

        Returns:
            defaultCounter: uint256
        """
        return self._execute(self.chain, request_type, "8bc128f1", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def writeOffCounter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#31)

        Returns:
            writeOffCounter: uint256
        """
        ...

    @overload
    def writeOffCounter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#31)

        Returns:
            writeOffCounter: uint256
        """
        ...

    @overload
    def writeOffCounter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#31)

        Returns:
            writeOffCounter: uint256
        """
        ...

    @overload
    def writeOffCounter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#31)

        Returns:
            writeOffCounter: uint256
        """
        ...

    def writeOffCounter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#31)

        Returns:
            writeOffCounter: uint256
        """
        return self._execute(self.chain, request_type, "7be274e1", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def recoveryCounter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#32)

        Returns:
            recoveryCounter: uint256
        """
        ...

    @overload
    def recoveryCounter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#32)

        Returns:
            recoveryCounter: uint256
        """
        ...

    @overload
    def recoveryCounter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#32)

        Returns:
            recoveryCounter: uint256
        """
        ...

    @overload
    def recoveryCounter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#32)

        Returns:
            recoveryCounter: uint256
        """
        ...

    def recoveryCounter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#32)

        Returns:
            recoveryCounter: uint256
        """
        return self._execute(self.chain, request_type, "68f0c713", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def seniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#34)

        Returns:
            seniorTrancheIdleValue: uint256
        """
        ...

    @overload
    def seniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#34)

        Returns:
            seniorTrancheIdleValue: uint256
        """
        ...

    @overload
    def seniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#34)

        Returns:
            seniorTrancheIdleValue: uint256
        """
        ...

    @overload
    def seniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#34)

        Returns:
            seniorTrancheIdleValue: uint256
        """
        ...

    def seniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#34)

        Returns:
            seniorTrancheIdleValue: uint256
        """
        return self._execute(self.chain, request_type, "e51e43c2", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def seniorTrancheDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#35)

        Returns:
            seniorTrancheDeployedValue: uint256
        """
        ...

    @overload
    def seniorTrancheDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#35)

        Returns:
            seniorTrancheDeployedValue: uint256
        """
        ...

    @overload
    def seniorTrancheDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#35)

        Returns:
            seniorTrancheDeployedValue: uint256
        """
        ...

    @overload
    def seniorTrancheDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#35)

        Returns:
            seniorTrancheDeployedValue: uint256
        """
        ...

    def seniorTrancheDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#35)

        Returns:
            seniorTrancheDeployedValue: uint256
        """
        return self._execute(self.chain, request_type, "406bf670", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def juniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#37)

        Returns:
            juniorTrancheIdleValue: uint256
        """
        ...

    @overload
    def juniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#37)

        Returns:
            juniorTrancheIdleValue: uint256
        """
        ...

    @overload
    def juniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#37)

        Returns:
            juniorTrancheIdleValue: uint256
        """
        ...

    @overload
    def juniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#37)

        Returns:
            juniorTrancheIdleValue: uint256
        """
        ...

    def juniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#37)

        Returns:
            juniorTrancheIdleValue: uint256
        """
        return self._execute(self.chain, request_type, "cdf9329e", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def juniorTrancheDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#38)

        Returns:
            juniorTrancheDeployedValue: uint256
        """
        ...

    @overload
    def juniorTrancheDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#38)

        Returns:
            juniorTrancheDeployedValue: uint256
        """
        ...

    @overload
    def juniorTrancheDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#38)

        Returns:
            juniorTrancheDeployedValue: uint256
        """
        ...

    @overload
    def juniorTrancheDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#38)

        Returns:
            juniorTrancheDeployedValue: uint256
        """
        ...

    def juniorTrancheDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#38)

        Returns:
            juniorTrancheDeployedValue: uint256
        """
        return self._execute(self.chain, request_type, "62b81447", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def equityTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#40)

        Returns:
            equityTrancheIdleValue: uint256
        """
        ...

    @overload
    def equityTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#40)

        Returns:
            equityTrancheIdleValue: uint256
        """
        ...

    @overload
    def equityTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#40)

        Returns:
            equityTrancheIdleValue: uint256
        """
        ...

    @overload
    def equityTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#40)

        Returns:
            equityTrancheIdleValue: uint256
        """
        ...

    def equityTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#40)

        Returns:
            equityTrancheIdleValue: uint256
        """
        return self._execute(self.chain, request_type, "b7c9d5b6", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def equityTrancheDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#41)

        Returns:
            equityTrancheDeployedValue: uint256
        """
        ...

    @overload
    def equityTrancheDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#41)

        Returns:
            equityTrancheDeployedValue: uint256
        """
        ...

    @overload
    def equityTrancheDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#41)

        Returns:
            equityTrancheDeployedValue: uint256
        """
        ...

    @overload
    def equityTrancheDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#41)

        Returns:
            equityTrancheDeployedValue: uint256
        """
        ...

    def equityTrancheDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#41)

        Returns:
            equityTrancheDeployedValue: uint256
        """
        return self._execute(self.chain, request_type, "a3b93fff", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def seniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#43)

        Returns:
            seniorTrancheTotalShares: uint256
        """
        ...

    @overload
    def seniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#43)

        Returns:
            seniorTrancheTotalShares: uint256
        """
        ...

    @overload
    def seniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#43)

        Returns:
            seniorTrancheTotalShares: uint256
        """
        ...

    @overload
    def seniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#43)

        Returns:
            seniorTrancheTotalShares: uint256
        """
        ...

    def seniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#43)

        Returns:
            seniorTrancheTotalShares: uint256
        """
        return self._execute(self.chain, request_type, "bb3805fa", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def seniorTrancheShares(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#44)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def seniorTrancheShares(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#44)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def seniorTrancheShares(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#44)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def seniorTrancheShares(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#44)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    def seniorTrancheShares(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#44)

        Args:
            key0: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "7a2222dd", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def seniorTrancheDeposits(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#45)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def seniorTrancheDeposits(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#45)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def seniorTrancheDeposits(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#45)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def seniorTrancheDeposits(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#45)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    def seniorTrancheDeposits(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#45)

        Args:
            key0: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "e9e97442", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def seniorUserIndex(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#46)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def seniorUserIndex(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#46)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def seniorUserIndex(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#46)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def seniorUserIndex(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#46)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    def seniorUserIndex(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#46)

        Args:
            key0: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "8f38df91", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def juniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#48)

        Returns:
            juniorTrancheTotalShares: uint256
        """
        ...

    @overload
    def juniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#48)

        Returns:
            juniorTrancheTotalShares: uint256
        """
        ...

    @overload
    def juniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#48)

        Returns:
            juniorTrancheTotalShares: uint256
        """
        ...

    @overload
    def juniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#48)

        Returns:
            juniorTrancheTotalShares: uint256
        """
        ...

    def juniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#48)

        Returns:
            juniorTrancheTotalShares: uint256
        """
        return self._execute(self.chain, request_type, "cab2845b", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def juniorTrancheShares(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#49)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def juniorTrancheShares(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#49)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def juniorTrancheShares(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#49)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def juniorTrancheShares(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#49)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    def juniorTrancheShares(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#49)

        Args:
            key0: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "50014f6b", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def juniorTrancheDeposits(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#50)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def juniorTrancheDeposits(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#50)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def juniorTrancheDeposits(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#50)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def juniorTrancheDeposits(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#50)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    def juniorTrancheDeposits(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#50)

        Args:
            key0: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "8ade00b7", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def juniorUserIndex(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#51)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def juniorUserIndex(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#51)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def juniorUserIndex(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#51)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def juniorUserIndex(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#51)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    def juniorUserIndex(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#51)

        Args:
            key0: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "d2beb926", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def loanBorrowers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#53)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    @overload
    def loanBorrowers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#53)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    @overload
    def loanBorrowers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#53)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    @overload
    def loanBorrowers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#53)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    def loanBorrowers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#53)

        Args:
            index0: uint256
        Returns:
            address
        """
        return self._execute(self.chain, request_type, "6a74c548", [index0], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def recevingEntity(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#55)

        Returns:
            recevingEntity: address
        """
        ...

    @overload
    def recevingEntity(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#55)

        Returns:
            recevingEntity: address
        """
        ...

    @overload
    def recevingEntity(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#55)

        Returns:
            recevingEntity: address
        """
        ...

    @overload
    def recevingEntity(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#55)

        Returns:
            recevingEntity: address
        """
        ...

    def recevingEntity(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#55)

        Returns:
            recevingEntity: address
        """
        return self._execute(self.chain, request_type, "bb85e79c", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def feeManager(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#56)

        Returns:
            feeManager: address
        """
        ...

    @overload
    def feeManager(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#56)

        Returns:
            feeManager: address
        """
        ...

    @overload
    def feeManager(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#56)

        Returns:
            feeManager: address
        """
        ...

    @overload
    def feeManager(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#56)

        Returns:
            feeManager: address
        """
        ...

    def feeManager(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#56)

        Returns:
            feeManager: address
        """
        return self._execute(self.chain, request_type, "d0fb0203", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#58)

        Returns:
            totalIdleValue: uint256
        """
        ...

    @overload
    def totalIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#58)

        Returns:
            totalIdleValue: uint256
        """
        ...

    @overload
    def totalIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#58)

        Returns:
            totalIdleValue: uint256
        """
        ...

    @overload
    def totalIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#58)

        Returns:
            totalIdleValue: uint256
        """
        ...

    def totalIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#58)

        Returns:
            totalIdleValue: uint256
        """
        return self._execute(self.chain, request_type, "fc5b0840", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#59)

        Returns:
            totalDeployedValue: uint256
        """
        ...

    @overload
    def totalDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#59)

        Returns:
            totalDeployedValue: uint256
        """
        ...

    @overload
    def totalDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#59)

        Returns:
            totalDeployedValue: uint256
        """
        ...

    @overload
    def totalDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#59)

        Returns:
            totalDeployedValue: uint256
        """
        ...

    def totalDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#59)

        Returns:
            totalDeployedValue: uint256
        """
        return self._execute(self.chain, request_type, "2d8d435d", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalDeposited(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#60)

        Returns:
            totalDeposited: uint256
        """
        ...

    @overload
    def totalDeposited(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#60)

        Returns:
            totalDeposited: uint256
        """
        ...

    @overload
    def totalDeposited(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#60)

        Returns:
            totalDeposited: uint256
        """
        ...

    @overload
    def totalDeposited(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#60)

        Returns:
            totalDeposited: uint256
        """
        ...

    def totalDeposited(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#60)

        Returns:
            totalDeposited: uint256
        """
        return self._execute(self.chain, request_type, "ff50abdc", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalLoss(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#61)

        Returns:
            totalLoss: uint256
        """
        ...

    @overload
    def totalLoss(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#61)

        Returns:
            totalLoss: uint256
        """
        ...

    @overload
    def totalLoss(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#61)

        Returns:
            totalLoss: uint256
        """
        ...

    @overload
    def totalLoss(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#61)

        Returns:
            totalLoss: uint256
        """
        ...

    def totalLoss(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#61)

        Returns:
            totalLoss: uint256
        """
        return self._execute(self.chain, request_type, "0d457ee1", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalRecovered(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#62)

        Returns:
            totalRecovered: uint256
        """
        ...

    @overload
    def totalRecovered(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#62)

        Returns:
            totalRecovered: uint256
        """
        ...

    @overload
    def totalRecovered(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#62)

        Returns:
            totalRecovered: uint256
        """
        ...

    @overload
    def totalRecovered(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#62)

        Returns:
            totalRecovered: uint256
        """
        ...

    def totalRecovered(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#62)

        Returns:
            totalRecovered: uint256
        """
        return self._execute(self.chain, request_type, "ca1a6fbb", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def outStandingPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#64)

        Returns:
            outStandingPrincipal: uint256
        """
        ...

    @overload
    def outStandingPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#64)

        Returns:
            outStandingPrincipal: uint256
        """
        ...

    @overload
    def outStandingPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#64)

        Returns:
            outStandingPrincipal: uint256
        """
        ...

    @overload
    def outStandingPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#64)

        Returns:
            outStandingPrincipal: uint256
        """
        ...

    def outStandingPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#64)

        Returns:
            outStandingPrincipal: uint256
        """
        return self._execute(self.chain, request_type, "e691bb9e", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def depositSeniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#120)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def depositSeniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#120)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def depositSeniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#120)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def depositSeniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#120)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    def depositSeniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#120)

        Args:
            userIndex: uint256
            amount: uint256
        """
        return self._execute(self.chain, request_type, "7a493f2f", [userIndex, amount], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def depositJuniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#155)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def depositJuniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#155)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def depositJuniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#155)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def depositJuniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#155)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    def depositJuniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#155)

        Args:
            userIndex: uint256
            amount: uint256
        """
        return self._execute(self.chain, request_type, "574ca186", [userIndex, amount], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def depositEquityTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#190)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def depositEquityTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#190)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def depositEquityTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#190)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def depositEquityTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#190)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    def depositEquityTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#190)

        Args:
            userIndex: uint256
            amount: uint256
        """
        return self._execute(self.chain, request_type, "3964924b", [userIndex, amount], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def maybeCommitPool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#223)
        """
        ...

    @overload
    def maybeCommitPool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#223)
        """
        ...

    @overload
    def maybeCommitPool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#223)
        """
        ...

    @overload
    def maybeCommitPool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#223)
        """
        ...

    def maybeCommitPool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#223)
        """
        return self._execute(self.chain, request_type, "507f253f", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def createLoan(self, principalIssued: uint256, originationFeeBps: uint256, termDays: uint256, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#234)

        Args:
            principalIssued: uint256
            originationFeeBps: uint256
            termDays: uint256
            userIndex: uint256
        """
        ...

    @overload
    def createLoan(self, principalIssued: uint256, originationFeeBps: uint256, termDays: uint256, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#234)

        Args:
            principalIssued: uint256
            originationFeeBps: uint256
            termDays: uint256
            userIndex: uint256
        """
        ...

    @overload
    def createLoan(self, principalIssued: uint256, originationFeeBps: uint256, termDays: uint256, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#234)

        Args:
            principalIssued: uint256
            originationFeeBps: uint256
            termDays: uint256
            userIndex: uint256
        """
        ...

    @overload
    def createLoan(self, principalIssued: uint256, originationFeeBps: uint256, termDays: uint256, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#234)

        Args:
            principalIssued: uint256
            originationFeeBps: uint256
            termDays: uint256
            userIndex: uint256
        """
        ...

    def createLoan(self, principalIssued: uint256, originationFeeBps: uint256, termDays: uint256, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#234)

        Args:
            principalIssued: uint256
            originationFeeBps: uint256
            termDays: uint256
            userIndex: uint256
        """
        return self._execute(self.chain, request_type, "b9fae650", [principalIssued, originationFeeBps, termDays, userIndex], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def activateLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#311)

        Args:
            loanId: uint256
        """
        ...

    @overload
    def activateLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#311)

        Args:
            loanId: uint256
        """
        ...

    @overload
    def activateLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#311)

        Args:
            loanId: uint256
        """
        ...

    @overload
    def activateLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#311)

        Args:
            loanId: uint256
        """
        ...

    def activateLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#311)

        Args:
            loanId: uint256
        """
        return self._execute(self.chain, request_type, "4644004d", [loanId], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#339)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
        """
        ...

    @overload
    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#339)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
        """
        ...

    @overload
    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#339)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
        """
        ...

    @overload
    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#339)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
        """
        ...

    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#339)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
        """
        return self._execute(self.chain, request_type, "8c8489f2", [loanId, principalAmount, interestAmount], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def warpTime(self, daysToWarp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#398)

        Args:
            daysToWarp: uint256
        """
        ...

    @overload
    def warpTime(self, daysToWarp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#398)

        Args:
            daysToWarp: uint256
        """
        ...

    @overload
    def warpTime(self, daysToWarp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#398)

        Args:
            daysToWarp: uint256
        """
        ...

    @overload
    def warpTime(self, daysToWarp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#398)

        Args:
            daysToWarp: uint256
        """
        ...

    def warpTime(self, daysToWarp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#398)

        Args:
            daysToWarp: uint256
        """
        return self._execute(self.chain, request_type, "9bddafe8", [daysToWarp], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def maybeDeclareDefault(self, loanId: uint256, reasonHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#403)

        Args:
            loanId: uint256
            reasonHash: bytes32
        """
        ...

    @overload
    def maybeDeclareDefault(self, loanId: uint256, reasonHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#403)

        Args:
            loanId: uint256
            reasonHash: bytes32
        """
        ...

    @overload
    def maybeDeclareDefault(self, loanId: uint256, reasonHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#403)

        Args:
            loanId: uint256
            reasonHash: bytes32
        """
        ...

    @overload
    def maybeDeclareDefault(self, loanId: uint256, reasonHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#403)

        Args:
            loanId: uint256
            reasonHash: bytes32
        """
        ...

    def maybeDeclareDefault(self, loanId: uint256, reasonHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#403)

        Args:
            loanId: uint256
            reasonHash: bytes32
        """
        return self._execute(self.chain, request_type, "2ec3ad92", [loanId, reasonHash], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def maybeWriteOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#424)

        Args:
            loanId: uint256
        """
        ...

    @overload
    def maybeWriteOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#424)

        Args:
            loanId: uint256
        """
        ...

    @overload
    def maybeWriteOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#424)

        Args:
            loanId: uint256
        """
        ...

    @overload
    def maybeWriteOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#424)

        Args:
            loanId: uint256
        """
        ...

    def maybeWriteOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#424)

        Args:
            loanId: uint256
        """
        return self._execute(self.chain, request_type, "85218344", [loanId], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def maybeRecoverLoan(self, loanId: uint256, amount: uint256, agentIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#455)

        Args:
            loanId: uint256
            amount: uint256
            agentIndex: uint256
        """
        ...

    @overload
    def maybeRecoverLoan(self, loanId: uint256, amount: uint256, agentIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#455)

        Args:
            loanId: uint256
            amount: uint256
            agentIndex: uint256
        """
        ...

    @overload
    def maybeRecoverLoan(self, loanId: uint256, amount: uint256, agentIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#455)

        Args:
            loanId: uint256
            amount: uint256
            agentIndex: uint256
        """
        ...

    @overload
    def maybeRecoverLoan(self, loanId: uint256, amount: uint256, agentIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#455)

        Args:
            loanId: uint256
            amount: uint256
            agentIndex: uint256
        """
        ...

    def maybeRecoverLoan(self, loanId: uint256, amount: uint256, agentIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#455)

        Args:
            loanId: uint256
            amount: uint256
            agentIndex: uint256
        """
        return self._execute(self.chain, request_type, "a6b590e8", [loanId, amount, agentIndex], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalExpectedSeniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#494)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedSeniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#494)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedSeniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#494)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedSeniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#494)

        Returns:
            uint256
        """
        ...

    def totalExpectedSeniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#494)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "291a147e", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalExpectedJuniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#502)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedJuniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#502)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedJuniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#502)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedJuniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#502)

        Returns:
            uint256
        """
        ...

    def totalExpectedJuniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#502)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "25cdcf05", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalExpectedSeniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#510)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedSeniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#510)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedSeniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#510)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedSeniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#510)

        Returns:
            uint256
        """
        ...

    def totalExpectedSeniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#510)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "41e8bc4d", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalExpectedJuniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#518)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedJuniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#518)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedJuniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#518)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedJuniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#518)

        Returns:
            uint256
        """
        ...

    def totalExpectedJuniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#518)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "47257831", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getSeniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#526)

        Returns:
            uint256
        """
        ...

    @overload
    def getSeniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#526)

        Returns:
            uint256
        """
        ...

    @overload
    def getSeniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#526)

        Returns:
            uint256
        """
        ...

    @overload
    def getSeniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#526)

        Returns:
            uint256
        """
        ...

    def getSeniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#526)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "eb78365c", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getJuniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#530)

        Returns:
            uint256
        """
        ...

    @overload
    def getJuniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#530)

        Returns:
            uint256
        """
        ...

    @overload
    def getJuniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#530)

        Returns:
            uint256
        """
        ...

    @overload
    def getJuniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#530)

        Returns:
            uint256
        """
        ...

    def getJuniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#530)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "89b7d92d", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getSeniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#534)

        Returns:
            uint256
        """
        ...

    @overload
    def getSeniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#534)

        Returns:
            uint256
        """
        ...

    @overload
    def getSeniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#534)

        Returns:
            uint256
        """
        ...

    @overload
    def getSeniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#534)

        Returns:
            uint256
        """
        ...

    def getSeniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#534)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "707baf37", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getJuniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#538)

        Returns:
            uint256
        """
        ...

    @overload
    def getJuniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#538)

        Returns:
            uint256
        """
        ...

    @overload
    def getJuniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#538)

        Returns:
            uint256
        """
        ...

    @overload
    def getJuniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#538)

        Returns:
            uint256
        """
        ...

    def getJuniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#538)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "e3e1de86", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

Handler.USDT.selector = bytes4(b'\xc5ND\xeb')
Handler.expectedPrincipal.selector = bytes4(b'p\x99\xc9\x0c')
Handler.minimumLoanPrincipal.selector = bytes4(b'\xf8`\xf2\xc8')
Handler.maximumLoanPrincipal.selector = bytes4(b'M\xf2\xd3\x88')
Handler.minimumOriginationFeeBps.selector = bytes4(b'\xac\x135!')
Handler.minimumTermDays.selector = bytes4(b';a\xf6^')
Handler.maximumTermDays.selector = bytes4(b'K\xa0r\xae')
Handler.seniorUsers.selector = bytes4(b'\x85&n\x18')
Handler.juniorUsers.selector = bytes4(b'\xf5\xd6V\x96')
Handler.equityUsers.selector = bytes4(b'\x9e\x95O\xd0')
Handler.activePolicyVersion.selector = bytes4(b'v\xde\x06\xf3')
Handler.defaultCounter.selector = bytes4(b'\x8b\xc1(\xf1')
Handler.writeOffCounter.selector = bytes4(b'{\xe2t\xe1')
Handler.recoveryCounter.selector = bytes4(b'h\xf0\xc7\x13')
Handler.seniorTrancheIdleValue.selector = bytes4(b'\xe5\x1eC\xc2')
Handler.seniorTrancheDeployedValue.selector = bytes4(b'@k\xf6p')
Handler.juniorTrancheIdleValue.selector = bytes4(b'\xcd\xf92\x9e')
Handler.juniorTrancheDeployedValue.selector = bytes4(b'b\xb8\x14G')
Handler.equityTrancheIdleValue.selector = bytes4(b'\xb7\xc9\xd5\xb6')
Handler.equityTrancheDeployedValue.selector = bytes4(b'\xa3\xb9?\xff')
Handler.seniorTrancheTotalShares.selector = bytes4(b'\xbb8\x05\xfa')
Handler.seniorTrancheShares.selector = bytes4(b'z""\xdd')
Handler.seniorTrancheDeposits.selector = bytes4(b'\xe9\xe9tB')
Handler.seniorUserIndex.selector = bytes4(b'\x8f8\xdf\x91')
Handler.juniorTrancheTotalShares.selector = bytes4(b'\xca\xb2\x84[')
Handler.juniorTrancheShares.selector = bytes4(b'P\x01Ok')
Handler.juniorTrancheDeposits.selector = bytes4(b'\x8a\xde\x00\xb7')
Handler.juniorUserIndex.selector = bytes4(b'\xd2\xbe\xb9&')
Handler.loanBorrowers.selector = bytes4(b'jt\xc5H')
Handler.recevingEntity.selector = bytes4(b'\xbb\x85\xe7\x9c')
Handler.feeManager.selector = bytes4(b'\xd0\xfb\x02\x03')
Handler.totalIdleValue.selector = bytes4(b'\xfc[\x08@')
Handler.totalDeployedValue.selector = bytes4(b'-\x8dC]')
Handler.totalDeposited.selector = bytes4(b'\xffP\xab\xdc')
Handler.totalLoss.selector = bytes4(b'\rE~\xe1')
Handler.totalRecovered.selector = bytes4(b'\xca\x1ao\xbb')
Handler.outStandingPrincipal.selector = bytes4(b'\xe6\x91\xbb\x9e')
Handler.depositSeniorTranche.selector = bytes4(b'zI?/')
Handler.depositJuniorTranche.selector = bytes4(b'WL\xa1\x86')
Handler.depositEquityTranche.selector = bytes4(b'9d\x92K')
Handler.maybeCommitPool.selector = bytes4(b'P\x7f%?')
Handler.createLoan.selector = bytes4(b'\xb9\xfa\xe6P')
Handler.activateLoan.selector = bytes4(b'FD\x00M')
Handler.repayLoan.selector = bytes4(b'\x8c\x84\x89\xf2')
Handler.warpTime.selector = bytes4(b'\x9b\xdd\xaf\xe8')
Handler.maybeDeclareDefault.selector = bytes4(b'.\xc3\xad\x92')
Handler.maybeWriteOffLoan.selector = bytes4(b'\x85!\x83D')
Handler.maybeRecoverLoan.selector = bytes4(b'\xa6\xb5\x90\xe8')
Handler.totalExpectedSeniorDeposits.selector = bytes4(b')\x1a\x14~')
Handler.totalExpectedJuniorDeposits.selector = bytes4(b'%\xcd\xcf\x05')
Handler.totalExpectedSeniorShares.selector = bytes4(b'A\xe8\xbcM')
Handler.totalExpectedJuniorShares.selector = bytes4(b'G%x1')
Handler.getSeniorTrancheIdleValue.selector = bytes4(b'\xebx6\\')
Handler.getJuniorTrancheIdleValue.selector = bytes4(b'\x89\xb7\xd9-')
Handler.getSeniorTrancheTotalShares.selector = bytes4(b'p{\xaf7')
Handler.getJuniorTrancheTotalShares.selector = bytes4(b'\xe3\xe1\xde\x86')
