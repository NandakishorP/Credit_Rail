
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
    _abi = {'constructor': {'inputs': [{'internalType': 'contract LoanEngine', 'name': '_loanEngine', 'type': 'address'}, {'internalType': 'contract TranchePool', 'name': '_tranchePool', 'type': 'address'}, {'internalType': 'contract CreditPolicy', 'name': '_creditPolicy', 'type': 'address'}, {'internalType': 'contract ERC20Mock', 'name': '_usdt', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'A0O\xac\xd92=u\xb1\x1b\xcd\xd6\t\xcb8\xef\xff\xfd\xb0W\x10\xf7\xca\xf0\xe9\xb1lm\x9dp\x9fP': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log', 'type': 'event'}, b'z\xe7LRt\x14\xae\x13_\xd9pG\xb1)!\xa5\xec9\x11\xb8\x04\x19xU\xd6~%\xc7\xb7^\xe6\xf3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'log_address', 'type': 'event'}, b'\xfb\x10(e\xd5\n\xdd\xdd\xf6\x9d\xa9\xb5\xaa\x1b\xce\xd6l\x80\xcf\x86\x9a\\\x8d\x04q\xa4g\xe1\x8c\xe9\xca\xb1': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_array', 'type': 'event'}, b'\x89\n\x82g\x9bG\x0f+\xd8(\x16\xed\x9b\x16\x1f\x97\xd8\xb9g\xf3\x7f\xa3d|!\xd5\xbf9t\x9e-\xd5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_array', 'type': 'event'}, b'@\xe1\x84\x0fWi\x07=a\xbd\x017-\x9bu\xba\xa9\x84-V)\xa0\xc9\x9f\xf1\x03\xbe\x11x\xa8\xe9\xe2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_array', 'type': 'event'}, b'#\xb6*\xd0XM$\xa7_\x0b\xf3V\x03\x91\xefVY\xecm\xb1&\x9cV\xe1\x1a\xa2A\xd67\xf1\x9b ': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'log_bytes', 'type': 'event'}, b'\xe8\x16\x99\xb8Q\x13\xee\xa1\xc7>\x10X\x8b+\x03^U\x893ic!s\xaf\xd4?\xeb\x19/\xacd\xe3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'log_bytes32', 'type': 'event'}, b'\x0e\xb5\xd5&$\xc8\xd2\x8a\xda\x9f\xc5Z\x8cP.\xd5\xaa?\xbe/\xb6\xe9\x1bq\xb5\xf3v\x88+\x1d/\xb8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256', 'name': '', 'type': 'int256'}], 'name': 'log_int', 'type': 'event'}, b'\x9cN\x85A\xca\x8f\r\xc1\xc4\x13\xf9\x10\x8ff\xd8-<\xec\xb1\xbd\xdb\xceCza\xca\xa3\x17\\L\xc9o': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address', 'name': 'val', 'type': 'address'}], 'name': 'log_named_address', 'type': 'event'}, b'\x00\xaa\xa3\x9c\x9f\xfb_VzE48\x0cspup.\x1f\x7f\x14\x10\x7f\xc9S(\xe3\xb5l\x03%\xfb': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xa7>\xda\tf/F\xdd\xe7)\xbeF\x118_\xf3O\xe6\xc4O\xbb\xc6\xf7\xe1{\x04+Y\xa3D[W': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_named_array', 'type': 'event'}, b";\xcf\xb2\xae.\x8d\x13-\xd1\xfc\xe7\xcf'\x8a\x9a\x19uj\x9f\xce\xab\xe4p\xdf;\xda\xbbK\xc5w\xd1\xbd": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xd2n\x16\xca\xd4T\x87\x05\xe4\xc9\xe2\xd9O\x98\xee\x91\xc2\x89\x08^\xe4%YO\xd5c_\xa2\x96L\xcf\x18': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'val', 'type': 'bytes'}], 'name': 'log_named_bytes', 'type': 'event'}, b'\xaf\xb7\x95\xc9\xc6\x1eO\xe7F\x8c8o\x92]zT)\xec\xad\x9c\x04\x95\xdd\xb8\xd3\x8di\x06\x14\xd3/\x99': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'val', 'type': 'bytes32'}], 'name': 'log_named_bytes32', 'type': 'event'}, b']\xa6\xce\x9dQ\x15\x1b\xa1\x0c\t\xa5Y\xef$\xd5 \xb9\xda\xc5\xc5\xb8\x81\n\xe8CNM\r\x86A\x1a\x95': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_int', 'type': 'event'}, b"\xeb\x8b\xa4<\xedu7B\x19F\xbdC\xe8(\xb8\xb2\xb8B\x89'\xaa\x8f\x80\x1c\x13\xd94\xbf\x11\xac\xa5{": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_uint', 'type': 'event'}, b'/\xe62w\x91t7CxD*\x8e\x97\x8b\xcc\xfb\xdc\xc1\xd6\xb2\xb0\xd8\x1f~\x8e\xb7v\xab"\x86\xf1h': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}], 'name': 'log_named_int', 'type': 'event'}, b'(\x0fDF\xb2\x8a\x13rA}\xdae\x8d0\xb9[)\x92\xb1*\xc9\xc7\xf3xS_)\xa9z\xcf5\x83': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'val', 'type': 'string'}], 'name': 'log_named_string', 'type': 'event'}, b'\xb2\xde/\xbe\x80\x1a\r\xf6\xc0\xcb\xdd\xfdD\x8b\xa3\xc4\x1dH\xa0@\xca5\xc5l\x81\x96\xef\x0f\xca\xe7!\xa8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}], 'name': 'log_named_uint', 'type': 'event'}, b'\x0b.\x13\xff \xac{GA\x98eU\x83\xed\xf7\r\xed\xd2\xc1\xdc\x98\x0e2\x9cO\xbb/\xc0t\x8byk': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log_string', 'type': 'event'}, b',\xab\x97\x90Q\x0f\xd8\xbd\xfb\xd2\x11R\x88\xdb3\xfe\xc6f\x91\xd4v\xef\xc5B|\xfdL\ti0\x17U': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'log_uint', 'type': 'event'}, b"\xe7\x95\x0e\xde\x03\x94\xb9\xf2\xceJZ\x1b\xf5\xa7\xe1\x85$\x11\xf7\xe6f\x1bC\x08\xc9\x13\xc4\xbf\xd1\x10'\xe4": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'logs', 'type': 'event'}, b'\xfav&\xd4': {'inputs': [], 'name': 'IS_TEST', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc5ND\xeb': {'inputs': [], 'name': 'USDT', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'FD\x00M': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'activateLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'v\xde\x06\xf3': {'inputs': [], 'name': 'activePolicyVersion', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x85F\x14\xc3': {'inputs': [{'internalType': 'uint256', 'name': 'userIndex', 'type': 'uint256'}], 'name': 'claimEquityTrancheInterest', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xffV\n\x9b': {'inputs': [{'internalType': 'uint256', 'name': 'userIndex', 'type': 'uint256'}], 'name': 'claimJuniorTrancheInterest', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x17\xf8\xe9\xf5': {'inputs': [{'internalType': 'uint256', 'name': 'userIndex', 'type': 'uint256'}], 'name': 'claimSeniorTrancheInterest', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb9\xfa\xe6P': {'inputs': [{'internalType': 'uint256', 'name': 'principalIssued', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'originationFeeBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'termDays', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'userIndex', 'type': 'uint256'}], 'name': 'createLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x8b\xc1(\xf1': {'inputs': [], 'name': 'defaultCounter', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'9d\x92K': {'inputs': [{'internalType': 'uint256', 'name': 'userIndex', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'depositEquityTranche', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'WL\xa1\x86': {'inputs': [{'internalType': 'uint256', 'name': 'userIndex', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'depositJuniorTranche', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'zI?/': {'inputs': [{'internalType': 'uint256', 'name': 'userIndex', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'depositSeniorTranche', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa3\xb9?\xff': {'inputs': [], 'name': 'equityTrancheDeployedValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x97\xbe\x04.': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'equityTrancheDeposits', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb7\xc9\xd5\xb6': {'inputs': [], 'name': 'equityTrancheIdleValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xf7\xed\xfa\x96': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'equityTrancheShares', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xf60h>': {'inputs': [], 'name': 'equityTrancheTotalShares', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x81\xeb(\t': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'equityUserIndex', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x9e\x95O\xd0': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'equityUsers', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb5P\x8a\xa9': {'inputs': [], 'name': 'excludeArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'excludedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe2\x0c\x9fq': {'inputs': [], 'name': 'excludeContracts', 'outputs': [{'internalType': 'address[]', 'name': 'excludedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb0FO\xdc': {'inputs': [], 'name': 'excludeSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'excludedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1e\xd7\x83\x1c': {'inputs': [], 'name': 'excludeSenders', 'outputs': [{'internalType': 'address[]', 'name': 'excludedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'p\x99\xc9\x0c': {'inputs': [], 'name': 'expectedPrincipal', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbaAO\xa6': {'inputs': [], 'name': 'failed', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd0\xfb\x02\x03': {'inputs': [], 'name': 'feeManager', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\x89\xb7\xd9-': {'inputs': [], 'name': 'getJuniorTrancheIdleValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe3\xe1\xde\x86': {'inputs': [], 'name': 'getJuniorTrancheTotalShares', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xebx6\\': {'inputs': [], 'name': 'getSeniorTrancheIdleValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'p{\xaf7': {'inputs': [], 'name': 'getSeniorTrancheTotalShares', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'b\xb8\x14G': {'inputs': [], 'name': 'juniorTrancheDeployedValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x8a\xde\x00\xb7': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'juniorTrancheDeposits', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xcd\xf92\x9e': {'inputs': [], 'name': 'juniorTrancheIdleValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'P\x01Ok': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'juniorTrancheShares', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xca\xb2\x84[': {'inputs': [], 'name': 'juniorTrancheTotalShares', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd2\xbe\xb9&': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'juniorUserIndex', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xf5\xd6V\x96': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'juniorUsers', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'jt\xc5H': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'loanBorrowers', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'M\xf2\xd3\x88': {'inputs': [], 'name': 'maximumLoanPrincipal', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'K\xa0r\xae': {'inputs': [], 'name': 'maximumTermDays', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x96\x0b/\x9d': {'inputs': [], 'name': 'mayClosePool', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'P\x7f%?': {'inputs': [], 'name': 'maybeCommitPool', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'.\xc3\xad\x92': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'reasonHash', 'type': 'bytes32'}], 'name': 'maybeDeclareDefault', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa6\xb5\x90\xe8': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'agentIndex', 'type': 'uint256'}], 'name': 'maybeRecoverLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x85!\x83D': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}], 'name': 'maybeWriteOffLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf8`\xf2\xc8': {'inputs': [], 'name': 'minimumLoanPrincipal', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xac\x135!': {'inputs': [], 'name': 'minimumOriginationFeeBps', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b';a\xf6^': {'inputs': [], 'name': 'minimumTermDays', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe6\x91\xbb\x9e': {'inputs': [], 'name': 'outStandingPrincipal', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbb\x85\xe7\x9c': {'inputs': [], 'name': 'recevingEntity', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'h\xf0\xc7\x13': {'inputs': [], 'name': 'recoveryCounter', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x8c\x84\x89\xf2': {'inputs': [{'internalType': 'uint256', 'name': 'loanId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'principalAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestAmount', 'type': 'uint256'}], 'name': 'repayLoan', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'@k\xf6p': {'inputs': [], 'name': 'seniorTrancheDeployedValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe9\xe9tB': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'seniorTrancheDeposits', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe5\x1eC\xc2': {'inputs': [], 'name': 'seniorTrancheIdleValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'z""\xdd': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'seniorTrancheShares', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbb8\x05\xfa': {'inputs': [], 'name': 'seniorTrancheTotalShares', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x8f8\xdf\x91': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'seniorUserIndex', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x85&n\x18': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'seniorUsers', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'f\xd9\xa9\xa0': {'inputs': [], 'name': 'targetArtifactSelectors', 'outputs': [{'components': [{'internalType': 'string', 'name': 'artifact', 'type': 'string'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzArtifactSelector[]', 'name': 'targetedArtifactSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x85"l\x81': {'inputs': [], 'name': 'targetArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'targetedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'?r\x86\xf4': {'inputs': [], 'name': 'targetContracts', 'outputs': [{'internalType': 'address[]', 'name': 'targetedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'*\xde8\x80': {'inputs': [], 'name': 'targetInterfaces', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'string[]', 'name': 'artifacts', 'type': 'string[]'}], 'internalType': 'struct StdInvariant.FuzzInterface[]', 'name': 'targetedInterfaces_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x91j\x17\xc6': {'inputs': [], 'name': 'targetSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'targetedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'>^<#': {'inputs': [], 'name': 'targetSenders', 'outputs': [{'internalType': 'address[]', 'name': 'targetedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'-\x8dC]': {'inputs': [], 'name': 'totalDeployedValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xffP\xab\xdc': {'inputs': [], 'name': 'totalDeposited', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'%\xcd\xcf\x05': {'inputs': [], 'name': 'totalExpectedJuniorDeposits', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'G%x1': {'inputs': [], 'name': 'totalExpectedJuniorShares', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b')\x1a\x14~': {'inputs': [], 'name': 'totalExpectedSeniorDeposits', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'A\xe8\xbcM': {'inputs': [], 'name': 'totalExpectedSeniorShares', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xfc[\x08@': {'inputs': [], 'name': 'totalIdleValue', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\rE~\xe1': {'inputs': [], 'name': 'totalLoss', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xca\x1ao\xbb': {'inputs': [], 'name': 'totalRecovered', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x9a.\xf2\xeb': {'inputs': [], 'name': 'totalUnclaimedInterest', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x9b\xdd\xaf\xe8': {'inputs': [{'internalType': 'uint256', 'name': 'daysToWarp', 'type': 'uint256'}], 'name': 'warpTime', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\t3]T': {'inputs': [{'internalType': 'uint256', 'name': 'userIndex', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'withdrawEquityTranche', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'uu\xdc\xb1': {'inputs': [{'internalType': 'uint256', 'name': 'userIndex', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'withdrawJuniorTranche', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x84\x7f"a': {'inputs': [{'internalType': 'uint256', 'name': 'userIndex', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'withdrawSeniorTranche', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'{\xe2t\xe1': {'inputs': [], 'name': 'writeOffCounter', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":46,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"stdstore","offset":0,"slot":0,"type":"t_struct(StdStorage)8331_storage"},{"astId":209,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_failed","offset":0,"slot":8,"type":"t_bool"},{"astId":2943,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"stdChainsInitialized","offset":1,"slot":8,"type":"t_bool"},{"astId":2964,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"chains","offset":0,"slot":9,"type":"t_mapping(t_string_memory_ptr,t_struct(Chain)2959_storage)"},{"astId":2968,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"defaultRpcUrls","offset":0,"slot":10,"type":"t_mapping(t_string_memory_ptr,t_string_storage)"},{"astId":2972,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"idToAlias","offset":0,"slot":11,"type":"t_mapping(t_uint256,t_string_storage)"},{"astId":2975,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"fallbackToDefaultRpcUrls","offset":0,"slot":12,"type":"t_bool"},{"astId":3931,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"gasMeteringOff","offset":1,"slot":12,"type":"t_bool"},{"astId":6002,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"stdstore","offset":0,"slot":13,"type":"t_struct(StdStorage)8331_storage"},{"astId":6923,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_excludedContracts","offset":0,"slot":21,"type":"t_array(t_address)dyn_storage"},{"astId":6926,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_excludedSenders","offset":0,"slot":22,"type":"t_array(t_address)dyn_storage"},{"astId":6929,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_targetedContracts","offset":0,"slot":23,"type":"t_array(t_address)dyn_storage"},{"astId":6932,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_targetedSenders","offset":0,"slot":24,"type":"t_array(t_address)dyn_storage"},{"astId":6935,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_excludedArtifacts","offset":0,"slot":25,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6938,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_targetedArtifacts","offset":0,"slot":26,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6942,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_targetedArtifactSelectors","offset":0,"slot":27,"type":"t_array(t_struct(FuzzArtifactSelector)6914_storage)dyn_storage"},{"astId":6946,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_excludedSelectors","offset":0,"slot":28,"type":"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage"},{"astId":6950,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_targetedSelectors","offset":0,"slot":29,"type":"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage"},{"astId":6954,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_targetedInterfaces","offset":0,"slot":30,"type":"t_array(t_struct(FuzzInterface)6920_storage)dyn_storage"},{"astId":13223,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"IS_TEST","offset":0,"slot":31,"type":"t_bool"},{"astId":48578,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"loanEngine","offset":1,"slot":31,"type":"t_contract(LoanEngine)44023"},{"astId":48581,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"tranchePool","offset":0,"slot":32,"type":"t_contract(TranchePool)47301"},{"astId":48584,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"usdt","offset":0,"slot":33,"type":"t_contract(ERC20Mock)40221"},{"astId":48587,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"creditPolicy","offset":0,"slot":34,"type":"t_contract(CreditPolicy)42678"},{"astId":48592,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"deployer","offset":0,"slot":35,"type":"t_address"},{"astId":48595,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"USDT","offset":0,"slot":36,"type":"t_uint256"},{"astId":48598,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"allowFullDeployment","offset":0,"slot":37,"type":"t_bool"},{"astId":48603,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"expectedPrincipal","offset":0,"slot":38,"type":"t_uint256"},{"astId":48608,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"minimumLoanPrincipal","offset":0,"slot":39,"type":"t_uint256"},{"astId":48613,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"maximumLoanPrincipal","offset":0,"slot":40,"type":"t_uint256"},{"astId":48616,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"minimumOriginationFeeBps","offset":0,"slot":41,"type":"t_uint256"},{"astId":48619,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"minimumTermDays","offset":0,"slot":42,"type":"t_uint256"},{"astId":48622,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"maximumTermDays","offset":0,"slot":43,"type":"t_uint256"},{"astId":48625,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"seniorUsers","offset":0,"slot":44,"type":"t_array(t_address)dyn_storage"},{"astId":48628,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"juniorUsers","offset":0,"slot":45,"type":"t_array(t_address)dyn_storage"},{"astId":48631,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"equityUsers","offset":0,"slot":46,"type":"t_array(t_address)dyn_storage"},{"astId":48634,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"activePolicyVersion","offset":0,"slot":47,"type":"t_uint256"},{"astId":48636,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"defaultCounter","offset":0,"slot":48,"type":"t_uint256"},{"astId":48638,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"writeOffCounter","offset":0,"slot":49,"type":"t_uint256"},{"astId":48640,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"recoveryCounter","offset":0,"slot":50,"type":"t_uint256"},{"astId":48642,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"seniorTrancheIdleValue","offset":0,"slot":51,"type":"t_uint256"},{"astId":48644,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"seniorTrancheDeployedValue","offset":0,"slot":52,"type":"t_uint256"},{"astId":48646,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"juniorTrancheIdleValue","offset":0,"slot":53,"type":"t_uint256"},{"astId":48648,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"juniorTrancheDeployedValue","offset":0,"slot":54,"type":"t_uint256"},{"astId":48650,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"equityTrancheIdleValue","offset":0,"slot":55,"type":"t_uint256"},{"astId":48652,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"equityTrancheDeployedValue","offset":0,"slot":56,"type":"t_uint256"},{"astId":48654,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"seniorTrancheTotalShares","offset":0,"slot":57,"type":"t_uint256"},{"astId":48658,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"seniorTrancheShares","offset":0,"slot":58,"type":"t_mapping(t_address,t_uint256)"},{"astId":48662,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"seniorTrancheDeposits","offset":0,"slot":59,"type":"t_mapping(t_address,t_uint256)"},{"astId":48666,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"seniorUserIndex","offset":0,"slot":60,"type":"t_mapping(t_address,t_uint256)"},{"astId":48668,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"juniorTrancheTotalShares","offset":0,"slot":61,"type":"t_uint256"},{"astId":48672,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"juniorTrancheShares","offset":0,"slot":62,"type":"t_mapping(t_address,t_uint256)"},{"astId":48676,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"juniorTrancheDeposits","offset":0,"slot":63,"type":"t_mapping(t_address,t_uint256)"},{"astId":48680,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"juniorUserIndex","offset":0,"slot":64,"type":"t_mapping(t_address,t_uint256)"},{"astId":48682,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"equityTrancheTotalShares","offset":0,"slot":65,"type":"t_uint256"},{"astId":48686,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"equityTrancheShares","offset":0,"slot":66,"type":"t_mapping(t_address,t_uint256)"},{"astId":48690,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"equityTrancheDeposits","offset":0,"slot":67,"type":"t_mapping(t_address,t_uint256)"},{"astId":48694,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"equityUserIndex","offset":0,"slot":68,"type":"t_mapping(t_address,t_uint256)"},{"astId":48697,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"loanBorrowers","offset":0,"slot":69,"type":"t_array(t_address)dyn_storage"},{"astId":48702,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"recevingEntity","offset":0,"slot":70,"type":"t_address"},{"astId":48707,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"feeManager","offset":0,"slot":71,"type":"t_address"},{"astId":48709,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"totalIdleValue","offset":0,"slot":72,"type":"t_uint256"},{"astId":48711,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"totalDeployedValue","offset":0,"slot":73,"type":"t_uint256"},{"astId":48713,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"totalDeposited","offset":0,"slot":74,"type":"t_uint256"},{"astId":48715,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"totalLoss","offset":0,"slot":75,"type":"t_uint256"},{"astId":48717,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"totalRecovered","offset":0,"slot":76,"type":"t_uint256"},{"astId":48719,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"totalUnclaimedInterest","offset":0,"slot":77,"type":"t_uint256"},{"astId":48721,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"outStandingPrincipal","offset":0,"slot":78,"type":"t_uint256"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_address)dyn_storage":{"encoding":"dynamic_array","label":"address[]","numberOfBytes":32,"base":"t_address"},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_array(t_bytes4)dyn_storage":{"encoding":"dynamic_array","label":"bytes4[]","numberOfBytes":32,"base":"t_bytes4"},"t_array(t_string_storage)dyn_storage":{"encoding":"dynamic_array","label":"string[]","numberOfBytes":32,"base":"t_string_storage"},"t_array(t_struct(FuzzArtifactSelector)6914_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzArtifactSelector[]","numberOfBytes":32,"base":"t_struct(FuzzArtifactSelector)6914_storage"},"t_array(t_struct(FuzzInterface)6920_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzInterface[]","numberOfBytes":32,"base":"t_struct(FuzzInterface)6920_storage"},"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzSelector[]","numberOfBytes":32,"base":"t_struct(FuzzSelector)6908_storage"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_contract(CreditPolicy)42678":{"encoding":"inplace","label":"contract CreditPolicy","numberOfBytes":20},"t_contract(ERC20Mock)40221":{"encoding":"inplace","label":"contract ERC20Mock","numberOfBytes":20},"t_contract(LoanEngine)44023":{"encoding":"inplace","label":"contract LoanEngine","numberOfBytes":20},"t_contract(TranchePool)47301":{"encoding":"inplace","label":"contract TranchePool","numberOfBytes":20},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))"},"t_mapping(t_address,t_uint256)":{"encoding":"mapping","label":"mapping(address => uint256)","numberOfBytes":32,"key":"t_address","value":"t_uint256"},"t_mapping(t_bytes32,t_struct(FindData)8306_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)8306_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)8306_storage)"},"t_mapping(t_string_memory_ptr,t_string_storage)":{"encoding":"mapping","label":"mapping(string => string)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_string_storage"},"t_mapping(t_string_memory_ptr,t_struct(Chain)2959_storage)":{"encoding":"mapping","label":"mapping(string => struct StdChains.Chain)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_struct(Chain)2959_storage"},"t_mapping(t_uint256,t_string_storage)":{"encoding":"mapping","label":"mapping(uint256 => string)","numberOfBytes":32,"key":"t_uint256","value":"t_string_storage"},"t_string_memory_ptr":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(Chain)2959_storage":{"encoding":"inplace","label":"struct StdChains.Chain","numberOfBytes":128,"members":[{"astId":2952,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"name","offset":0,"slot":0,"type":"t_string_storage"},{"astId":2954,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"chainId","offset":0,"slot":1,"type":"t_uint256"},{"astId":2956,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"chainAlias","offset":0,"slot":2,"type":"t_string_storage"},{"astId":2958,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"rpcUrl","offset":0,"slot":3,"type":"t_string_storage"}]},"t_struct(FindData)8306_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":8299,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":8301,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":8303,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":8305,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(FuzzArtifactSelector)6914_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzArtifactSelector","numberOfBytes":64,"members":[{"astId":6910,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"artifact","offset":0,"slot":0,"type":"t_string_storage"},{"astId":6913,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(FuzzInterface)6920_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzInterface","numberOfBytes":64,"members":[{"astId":6916,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6919,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"artifacts","offset":0,"slot":1,"type":"t_array(t_string_storage)dyn_storage"}]},"t_struct(FuzzSelector)6908_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzSelector","numberOfBytes":64,"members":[{"astId":6904,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6907,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(StdStorage)8331_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":8315,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))"},{"astId":8318,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":8320,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":8322,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":8324,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":8326,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":8328,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":8330,"contract":"test/fuzz/invariant/Handler.t.sol:Handler","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60808060405234610eeb575f9060808161725680380380916100218285610f88565b833981010312610eeb578051916001600160a01b0383168303610eeb5760208201516001600160a01b03811690819003610eeb5760408301516001600160a01b0381169390849003610eeb57606001516001600160a01b0381169290839003610eeb57600160ff19600c541617600c55600160ff19601f541617601f556040516100ac604082610f88565b6008815260208101673232b83637bcb2b960c11b815260405160208101906100ec60208286518087875e81015f838201520301601f198101835282610f88565b5190206040519063ffa1864960e01b825260048201526020816024815f5160206172365f395f51905f525afa908115610ee0575f91610f46575b505f5160206172365f395f51905f523b15610eeb575f906064604051809481936318caf8e360e31b835260018060a01b031696876004840152604060248401525180918160448501528484015e8181018301859052601f01601f19168101030181835f5160206172365f395f51905f525af18015610ee057610f31575b5060018060a01b03196023541617602355670de0b6b3a7640000602455600160ff196025541617602555506a52b7d2dcc80cd2e40000006026555f9369d3c21bcecceda10000006027556a108b2a2c28029094000000602855603260295560b4602a556101e0602b556001602f5560405161021f604082610f88565b600e8152602081016d7265636576696e67456e7469747960901b8152604051602081019061026560208286518087875e81015f838201520301601f198101835282610f88565b5190206040519063ffa1864960e01b825260048201526020816024815f5160206172365f395f51905f525afa908115610ee0575f91610eef575b505f5160206172365f395f51905f523b15610eeb575f906064604051809481936318caf8e360e31b835260018060a01b031696876004840152604060248401525180918160448501528484015e8181018301859052601f01601f19168101030181835f5160206172365f395f51905f525af18015610ee057610ecb575b5060018060a01b0319604654161760465560405161033b604082610f88565b600a81528560208201693332b2a6b0b730b3b2b960b11b8152604051602081019061037e60208287518087875e810187838201520301601f198101835282610f88565b5190206040519063ffa1864960e01b825260048201526020816024815f5160206172365f395f51905f525afa908115610798578391610e89575b505f5160206172365f395f51905f523b1561077f5782906064604051809481936318caf8e360e31b835260018060a01b031697886004840152604060248401525180918160448501528484015e8181018301859052601f01601f19168101030181835f5160206172365f395f51905f525af1801561077457610e70575b5050604780546001600160a01b0319908116929092179055601f8054610100600160a81b03191660089390931b610100600160a81b03169290921790915560208054821692909217909155602180548216929092179091556022805490911691909117905560235481906001600160a01b03165f5160206172365f395f51905f523b15610e6d57604051906303223eab60e11b825260048201528181602481835f5160206172365f395f51905f525af1801561077457610e58575b50601f546047546001600160a01b0360089290921c82169116813b15610e00578291604483926040519485938492631f9dd86960e21b84526004840152600160248401525af1801561077457610e43575b50601f546046546001600160a01b0360089290921c82169116813b15610e00578291604483926040519485938492630c1159b160e21b84526004840152600160248401525af1801561077457610e2e575b50601f546046546001600160a01b0360089290921c82169116813b15610e005782916044839260405194859384926319b52c2160e01b84526004840152600160248401525af1801561077457610e19575b50601f546046546001600160a01b0360089290921c82169116813b15610e0057829160448392604051948593849263ee48145560e01b84526004840152600160248401525af1801561077457610e04575b505060015b6001600160a01b038116606481101561094357602c546801000000000000000081101561092f576001810180602c5581101561091b57602c84527f7416c943b4a09859521022fd2e90eac0dd9026dad28fa317782a135f28a860910180546001600160a01b031916821790558290600183166107a3576021546001600160a01b0316803b1561077f578280916044604051809481936340c10f1960e01b83528760048401526b033b2e3c9fd0803ce800000060248401525af1908115610798578391610783575b50506020546001600160a01b031690813b1561077f578291604483926040519485938492630d392cd960e01b84526004840152600160248401525af180156107745761075b575b50505b6001016001600160a01b0316610639565b8161076591610f88565b61077057815f610747565b5080fd5b6040513d84823e3d90fd5b8280fd5b8161078d91610f88565b61077057815f610700565b6040513d85823e3d90fd5b6001600160a01b03600382061661087d576021546001600160a01b0316803b1561077f578280916044604051809481936340c10f1960e01b83528760048401526b1027e72f1f1281308800000060248401525af1908115610798578391610868575b50506020546001600160a01b031690813b1561077f578291604483926040519485938492630d392cd960e01b84526004840152600160248401525af1801561077457610853575b505061074a565b8161085d91610f88565b61077057815f61084c565b8161087291610f88565b61077057815f610805565b6021546001600160a01b0316803b1561077f578280916044604051809481936340c10f1960e01b83528760048401526c01431e0fae6d7217caa000000060248401525af19081156107985783916108685750506020546001600160a01b031690813b1561077f578291604483926040519485938492630d392cd960e01b84526004840152600160248401525af180156107745761085357505061074a565b634e487b7160e01b84526032600452602484fd5b634e487b7160e01b84526041600452602484fd5b8260015b6001600160a01b038116600a811015610b5c57602d546801000000000000000081101561092f576001810180602d5581101561091b57602d84527f4a2cc91ee622da3bc833a54c37ffcb6f3ec23b7793efc5eaf5e71b7b406c5c060180546001600160a01b03191682179055829060018316610a93576021546001600160a01b0316803b1561077f578280916044604051809481936340c10f1960e01b83528760048401526ba18f07d736b90be55000000060248401525af1908115610798578391610a7e575b50506020546001600160a01b031690813b1561077f578291604483926040519485938492630d392cd960e01b84526004840152600160248401525af1801561077457610a69575b50505b6001016001600160a01b0316610947565b81610a7391610f88565b610770578183610a55565b81610a8891610f88565b610770578185610a0e565b6020546001600160a01b0316803b1561077f57828091604460405180948193630d392cd960e01b8352876004840152600160248401525af1908115610798578391610b47575b50506021546001600160a01b031690813b1561077f5782916044839260405194859384926340c10f1960e01b845260048401526b204fce5e3e2502611000000060248401525af1801561077457610b32575b5050610a58565b81610b3c91610f88565b610770578183610b2b565b81610b5191610f88565b610770578185610ad9565b8260015b6001600160a01b0381166005811015610ca457602e546801000000000000000081101561092f576001810180602e5581101561091b57602e84527f37fa166cbdbfbb1561ccd9ea985ec0218b5e68502e230525f544285b2bdf3d7e0180546001600160a01b031916821790556021548391906001600160a01b0316803b1561077f578280916044604051809481936340c10f1960e01b83528760048401526b1027e72f1f1281308800000060248401525af1908115610798578391610c8f575b50506020546001600160a01b031690813b1561077f5782916044839260405194859384926307e95e9360e31b84526004840152600160248401525af1801561077457610c7a575b50506001016001600160a01b0316610b60565b81610c8491610f88565b610770578183610c67565b81610c9991610f88565b610770578185610c20565b8260c85b6001600160a01b03811660dc811015610d26576045546801000000000000000081101561092f57600181018060455581101561091b57604584527fa80a8fcc11760162f08bb091d2c9389d07f2b73d0e996161dfac6f1043b5fc0b0180546001600160a01b03191690911790556001016001600160a01b0316610ca8565b602154604654849182916001600160a01b039182169116813b15610e005782916044839260405194859384926340c10f1960e01b845260048401526b1027e72f1f1281308800000060248401525af1801561077457610deb575b50505f5160206172365f395f51905f523b15610de8576040516390c5013b60e01b81528181600481835f5160206172365f395f51905f525af1801561077457610dd3575b6040516162769081610fc08239f35b610dde828092610f88565b610de85780610dc4565b80fd5b81610df591610f88565b610de8578082610d80565b5050fd5b81610e0e91610f88565b610de857805f610634565b81610e2391610f88565b610de857805f6105e3565b81610e3891610f88565b610de857805f610592565b81610e4d91610f88565b610de857805f610541565b81610e6291610f88565b610de857805f6104f0565b50fd5b81610e7a91610f88565b610e8557855f610435565b8580fd5b90506020813d602011610ec3575b81610ea460209383610f88565b8101031261077f57516001600160a01b038116810361077f575f6103b8565b3d9150610e97565b610ed89196505f90610f88565b5f945f61031c565b6040513d5f823e3d90fd5b5f80fd5b90506020813d602011610f29575b81610f0a60209383610f88565b81010312610eeb57516001600160a01b0381168103610eeb575f61029f565b3d9150610efd565b610f3e9192505f90610f88565b5f905f6101a3565b90506020813d602011610f80575b81610f6160209383610f88565b81010312610eeb57516001600160a01b0381168103610eeb575f610126565b3d9150610f54565b601f909101601f19168101906001600160401b03821190821017610fab57604052565b634e487b7160e01b5f52604160045260245ffdfe60806040526004361015610011575f80fd5b5f5f3560e01c806309335d54146118075780630d457ee1146117ea57806317f8e9f5146117ce5780631ed7831c1461175157806325cdcf05146116ef578063291a147e1461168d5780632ade3880146114d25780632d8d435d146114b55780632ec3ad92146114965780633964924b1461147f5780633b61f65e146114625780633e5e3c23146113e55780633f7286f414611368578063406bf6701461134b57806341e8bc4d146112e95780634644004d146112cb57806347257831146112695780634ba072ae1461124c5780634df2d3881461122f57806350014f6b146111f3578063507f253f14610fb6578063574ca18614610f9e57806362b8144714610f8057806366d9a9a014610e5f57806368f0c71314610e415780636a74c54814610e16578063707baf37146106d95780637099c90c14610df85780637575dcb114610de057806376de06f314610dc25780637a2222dd14610d855780637a493f2f14610d6d5780637be274e114610d4f57806381eb280914610d12578063847f226114610cfa5780638521834414610cdd57806385226c8114610c5357806385266e1814610c28578063854614c314610c0b57806389b7d92d146106565780638ade00b714610bce5780638bc128f114610bb05780638c8489f214610b985780638f38df9114610b5b578063916a17c614610ab3578063960b2f9d14610a9a57806397be042e14610a5d5780639a2ef2eb14610a3f5780639bddafe8146109115780639e954fd0146108e6578063a3b93fff146108c8578063a6b590e8146108b0578063ac13352114610892578063b0464fdc146107ea578063b5508aa914610760578063b7c9d5b614610742578063b9fae6501461071c578063ba414fa6146106f7578063bb3805fa146106d9578063bb85e79c146106b0578063c54e44eb14610692578063ca1a6fbb14610674578063cab2845b14610545578063cdf9329e14610656578063d0fb02031461062d578063d2beb926146105f1578063e20c9f7114610563578063e3e1de8614610545578063e51e43c2146104cc578063e691bb9e14610527578063e9e97442146104ea578063eb78365c146104cc578063f5d6569614610488578063f630683e1461046a578063f7edfa9614610429578063f860f2c81461040b578063fa7626d4146103e8578063fc5b0840146103ca578063ff50abdc146103ac5763ff560a9b1461038a575f80fd5b346103a95760203660031901126103a9576103a6600435615b88565b80f35b80fd5b50346103a957806003193601126103a9576020604a54604051908152f35b50346103a957806003193601126103a9576020604854604051908152f35b50346103a957806003193601126103a957602060ff601f54166040519015158152f35b50346103a957806003193601126103a9576020602754604051908152f35b50346103a95760203660031901126103a9576004356001600160a01b03811690819003610466578160409160209352604283522054604051908152f35b5080fd5b50346103a957806003193601126103a9576020604154604051908152f35b50346103a95760203660031901126103a95760043590602d548210156103a95760206104b3836118d7565b905460405160039290921b1c6001600160a01b03168152f35b50346103a957806003193601126103a9576020603354604051908152f35b50346103a95760203660031901126103a9576004356001600160a01b03811690819003610466578160409160209352603b83522054604051908152f35b50346103a957806003193601126103a9576020604e54604051908152f35b50346103a957806003193601126103a9576020603d54604051908152f35b50346103a957806003193601126103a95760405160158054808352908352909160208301917f55f448fdea98c4d29eb340757ef0a66cd03dbb9538908a6a81d96026b71ec475915b8181106105d2576105ce856105c281870382611a6b565b60405191829182611834565b0390f35b82546001600160a01b03168452602090930192600192830192016105ab565b50346103a95760203660031901126103a9576004356001600160a01b038116908190036104665781604091602093528183522054604051908152f35b50346103a957806003193601126103a9576047546040516001600160a01b039091168152602090f35b50346103a957806003193601126103a9576020603554604051908152f35b50346103a957806003193601126103a9576020604c54604051908152f35b50346103a957806003193601126103a9576020602454604051908152f35b50346103a957806003193601126103a9576046546040516001600160a01b039091168152602090f35b50346103a957806003193601126103a9576020603954604051908152f35b50346103a957806003193601126103a9576020610712615aed565b6040519015158152f35b50346103a95760803660031901126103a9576103a66064356044356024356004356153ee565b50346103a957806003193601126103a9576020603754604051908152f35b50346103a957806003193601126103a95760195461077d81612227565b9161078b6040519384611a6b565b818352601981527f944998273e477b495144fb8794c914197f3ccb46be2900f4698fd0ef743c9695602084015b8383106107cd57604051806105ce878261194b565b6001602081926107dc8561223f565b8152019201920191906107b8565b50346103a957806003193601126103a957601c5461080781612227565b916108156040519384611a6b565b818352601c81527f0e4562a10381dec21b205ed72637e6b1b523bdd0e4d4d50af5cd23dd4500a211602084015b83831061085757604051806105ce87826119c4565b6002602060019260405161086a81611a3b565b848060a01b038654168152610880858701613690565b83820152815201920192019190610842565b50346103a957806003193601126103a9576020602954604051908152f35b50346103a9576103a66108c2366119aa565b91614fed565b50346103a957806003193601126103a9576020603854604051908152f35b50346103a95760203660031901126103a95760043590602e548210156103a95760206104b383611933565b50346103a95760203660031901126103a95761093361016d600160043561607c565b6109a061098761099b60405161094a604082611a6b565b600c81526b109bdd5b99081c995cdd5b1d60a21b6020820152604051928391632d839cb360e21b6020840152604060248401526064830190611876565b85604483015203601f198101835282611a6b565b616206565b62015180810290808204620151801490151715610a2b576109c282914261221a565b5f5160206162215f395f51905f523b15610a2857604051906372eb5f8160e11b825260048201528181602481835f5160206162215f395f51905f525af18015610a1d57610a0c5750f35b81610a1691611a6b565b6103a95780f35b6040513d84823e3d90fd5b50fd5b634e487b7160e01b82526011600452602482fd5b50346103a957806003193601126103a9576020604d54604051908152f35b50346103a95760203660031901126103a9576004356001600160a01b03811690819003610466578160409160209352604383522054604051908152f35b50346103a957806003193601126103a9576103a6614e70565b50346103a957806003193601126103a957601d54610ad081612227565b91610ade6040519384611a6b565b818352601d81527f6d4407e7be21f808e6509aa9fa9143369579dd7d760fe20a2c09680fc146134f602084015b838310610b2057604051806105ce87826119c4565b60026020600192604051610b3381611a3b565b848060a01b038654168152610b49858701613690565b83820152815201920192019190610b0b565b50346103a95760203660031901126103a9576004356001600160a01b03811690819003610466578160409160209352603c83522054604051908152f35b50346103a9576103a6610baa366119aa565b916149e6565b50346103a957806003193601126103a9576020603054604051908152f35b50346103a95760203660031901126103a9576004356001600160a01b03811690819003610466578160409160209352603f83522054604051908152f35b50346103a95760203660031901126103a9576103a660043561464f565b50346103a95760203660031901126103a95760043590602c548210156103a95760206104b383611903565b50346103a957806003193601126103a957601a54610c7081612227565b91610c7e6040519384611a6b565b818352601a81527f057c384a7d1c54f3a1b2e5e67b2617b8224fdfd1ea7234eea573a6ff665ff63e602084015b838310610cc057604051806105ce878261194b565b600160208192610ccf8561223f565b815201920192019190610cab565b50346103a95760203660031901126103a9576103a66004356143b3565b50346103a9576103a6610d0c3661181e565b9061408c565b50346103a95760203660031901126103a9576004356001600160a01b03811690819003610466578160409160209352604483522054604051908152f35b50346103a957806003193601126103a9576020603154604051908152f35b50346103a9576103a6610d7f3661181e565b90613bb9565b50346103a95760203660031901126103a9576004356001600160a01b03811690819003610466578160409160209352603a83522054604051908152f35b50346103a957806003193601126103a9576020602f54604051908152f35b50346103a9576103a6610df23661181e565b90613892565b50346103a957806003193601126103a9576020602654604051908152f35b50346103a95760203660031901126103a957600435906045548210156103a95760206104b38361191b565b50346103a957806003193601126103a9576020603254604051908152f35b50346103a957806003193601126103a957601b54610e7c81612227565b610e896040519182611a6b565b818152601b83526020810191837f3ad8aa4f87544323a9d1e5dd902f40c356527a7955687113db5f9a85ad579dc1845b838310610f4557868587604051928392602084019060208552518091526040840160408260051b8601019392905b828210610ef657505050500390f35b91936001919395506020610f358192603f198a820301865288519083610f258351604084526040840190611876565b920151908481840391015261189a565b9601920192018594939192610ee7565b60026020600192604051610f5881611a3b565b610f618661223f565b8152610f6e858701613690565b83820152815201920192019190610eb9565b50346103a957806003193601126103a9576020603654604051908152f35b50346103a9576103a6610fb03661181e565b906131b8565b503461110d575f36600319011261110d576020805460405163217ac23760e01b81526001600160a01b039091169181600481855afa908115611141575f916111c4575b5060048110156111b05715908161114c575b506110135780f35b6023546001600160a01b03165f5160206162215f395f51905f523b1561110d576040519063ca669fa760e01b825260048201525f81602481835f5160206162215f395f51905f525af180156111415761112e575b5060205481906001600160a01b0316803b15610a28578180916024604051809481936377dd846960e01b8352600160048401525af18015610a1d57611119575b50506020805460405163b3d814f560e01b81529190829060049082906001600160a01b03165afa908115610a1d5782916110e3575b50604a5580f35b90506020813d602011611111575b816110fe60209383611a6b565b8101031261110d57515f6110dc565b5f80fd5b3d91506110f1565b8161112391611a6b565b6103a957805f6110a7565b61113a91505f90611a6b565b5f5f611067565b6040513d5f823e3d90fd5b60405163b3d814f560e01b81529150602090829060049082905afa908115611141575f9161117e575b5015155f61100b565b90506020813d6020116111a8575b8161119960209383611a6b565b8101031261110d57515f611175565b3d915061118c565b634e487b7160e01b5f52602160045260245ffd5b6111e6915060203d6020116111ec575b6111de8183611a6b565b810190611a8d565b5f610ff9565b503d6111d4565b3461110d57602036600319011261110d576004356001600160a01b0381169081900361110d575f52603e602052602060405f2054604051908152f35b3461110d575f36600319011261110d576020602854604051908152f35b3461110d575f36600319011261110d576020602b54604051908152f35b3461110d575f36600319011261110d575f5f90602d545b80831061129257602082604051908152f35b906112c26001916112a2856118d7565b848060a01b0391549060031b1c165f52603e60205260405f20549061221a565b92019190611280565b3461110d57602036600319011261110d576112e7600435612cde565b005b3461110d575f36600319011261110d575f5f90602c545b80831061131257602082604051908152f35b9061134260019161132285611903565b848060a01b0391549060031b1c165f52603a60205260405f20549061221a565b92019190611300565b3461110d575f36600319011261110d576020603454604051908152f35b3461110d575f36600319011261110d57604051601780548083525f91825260208301917fc624b66cc0138b8fabc209247f72d758e1cf3343756d543badbf24212bed8c1591905b8181106113c6576105ce856105c281870382611a6b565b82546001600160a01b03168452602090930192600192830192016113af565b3461110d575f36600319011261110d57604051601880548083525f91825260208301917fb13d2d76d1f4b7be834882e410b3e3a8afaf69f83600ae24db354391d2378d2e91905b818110611443576105ce856105c281870382611a6b565b82546001600160a01b031684526020909301926001928301920161142c565b3461110d575f36600319011261110d576020602a54604051908152f35b3461110d576112e76114903661181e565b90612681565b3461110d57604036600319011261110d576112e7602435600435612427565b3461110d575f36600319011261110d576020604954604051908152f35b3461110d575f36600319011261110d57601e546114ee81612227565b906114fc6040519283611a6b565b808252601e5f9081526020830191907f50bb669a95c7b50b7e8a6f09454034b2b14cf2b85c730dca9a539ca82cb6e350835b83831061160257848660405191829160208301906020845251809152604083019060408160051b85010192915f905b82821061156c57505050500390f35b919390929450603f198682030182528451906020604082019260018060a01b0381511683520151916040602083015282518091526060820190602060608260051b8501019401925f5b8281106115d7575050505050602080600192960192019201859493919261155d565b90919293946020806115f5600193605f198782030189528951611876565b97019501939291016115b5565b60405161160e81611a3b565b82546001600160a01b0316815260018301805461162a81612227565b916116386040519384611a6b565b81835260208301905f5260205f20905f905b83821061167057505050506001928260209283600295015281520192019201919061152e565b60016020819261167f8661223f565b81520193019101909161164a565b3461110d575f36600319011261110d575f5f90602c545b8083106116b657602082604051908152f35b906116e66001916116c685611903565b848060a01b0391549060031b1c165f52603b60205260405f20549061221a565b920191906116a4565b3461110d575f36600319011261110d575f5f90602d545b80831061171857602082604051908152f35b90611748600191611728856118d7565b848060a01b0391549060031b1c165f52603f60205260405f20549061221a565b92019190611706565b3461110d575f36600319011261110d57604051601680548083525f91825260208301917fd833147d7dc355ba459fc788f669e58cfaf9dc25ddcd0702e87d69c7b512428991905b8181106117af576105ce856105c281870382611a6b565b82546001600160a01b0316845260209093019260019283019201611798565b3461110d57602036600319011261110d576112e7600435611e5d565b3461110d575f36600319011261110d576020604b54604051908152f35b3461110d576112e76118183661181e565b90611b06565b604090600319011261110d576004359060243590565b60206040818301928281528451809452019201905f5b8181106118575750505090565b82516001600160a01b031684526020938401939092019160010161184a565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b90602080835192838152019201905f5b8181106118b75750505090565b82516001600160e01b0319168452602093840193909201916001016118aa565b602d548110156118ef57602d5f5260205f2001905f90565b634e487b7160e01b5f52603260045260245ffd5b602c548110156118ef57602c5f5260205f2001905f90565b6045548110156118ef5760455f5260205f2001905f90565b602e548110156118ef57602e5f5260205f2001905f90565b602081016020825282518091526040820191602060408360051b8301019401925f915b83831061197d57505050505090565b909192939460208061199b600193603f198682030187528951611876565b9701930193019193929061196e565b606090600319011261110d57600435906024359060443590565b602081016020825282518091526040820191602060408360051b8301019401925f915b8383106119f657505050505090565b9091929394602080611a2c600193603f198682030187526040838b51878060a01b0381511684520151918185820152019061189a565b970193019301919392906119e7565b6040810190811067ffffffffffffffff821117611a5757604052565b634e487b7160e01b5f52604160045260245ffd5b90601f8019910116810190811067ffffffffffffffff821117611a5757604052565b9081602091031261110d5751600481101561110d5790565b91908203918211611ab257565b634e487b7160e01b5f52601160045260245ffd5b9081602091031261110d575190565b81810292918115918404141715611ab257565b8115611af2570490565b634e487b7160e01b5f52601260045260245ffd5b6020805460405163217ac23760e01b81525f9594936001600160a01b039092169281600481865afa908115611141575f91611e3e575b5060048110156111b057600303611e3757602e545f198101908111611ab257611b6491615f1f565b611b6d81611933565b9054604051632183fd1760e21b815260039290921b1c6001600160a01b03166004820181905293602082602481875afa908115611141575f91611e01575b611bb59250615f1f565b918215611d8157604051631e9ea63960e11b815290602082600481845afa918215611141575f92611dcc575b50906020602492604051938480926346d13a7b60e01b82528960048301525afa918215611141575f92611d98575b5003611d89575b50603754604154908115611d815790611c32611c379284611ad5565b611ae8565b915f5160206162215f395f51905f523b1561110d5760405163ca669fa760e01b8152600481018290525f81602481835f5160206162215f395f51905f525af1801561114157611d6c575b5060205485906001600160a01b0316803b15610466578190602460405180948193638b5de60360e01b83528860048401525af18015611d6157611d48575b509060408583611d1794611d319798526043602052858383205410155f14611d36578082526043602052828220611cf7878254611aa5565b90555b8152604260205220611d0d828254611aa5565b9055604154611aa5565b604155611d2681603754611aa5565b603755604854611aa5565b604855565b80825260436020528183812055611cfa565b611d53868092611a6b565b611d5d575f611cbf565b8480fd5b6040513d88823e3d90fd5b611d799195505f90611a6b565b5f935f611c81565b505050509050565b611d929061464f565b5f611c16565b9091506020813d602011611dc4575b81611db460209383611a6b565b8101031261110d5751905f611c0f565b3d9150611da7565b91506020823d602011611df9575b81611de760209383611a6b565b8101031261110d579051906020611be1565b3d9150611dda565b90506020823d602011611e2f575b81611e1c60209383611a6b565b8101031261110d57611bb5915190611bab565b3d9150611e0f565b5050509050565b611e57915060203d6020116111ec576111de8183611a6b565b5f611b3c565b602c545f91905f198101908111611ab257611e7791615f1f565b6020805460405163641ad8a960e01b81526001600160a01b03909116929181600481865afa908115611141575f916121fb575b5060048110156111b05760030361215c57611ec490611903565b905460405163071dd98160e11b815260039290921b1c6001600160a01b0316600482018190529190602081602481855afa908115611141575f916121c9575b501561215c5760405163415b47c560e01b8152602081600481855afa908115611141575f91612197575b5060405163078d049d60e51b81526004810184905290602082602481865afa908115611141575f91612161575b611f649250611aa5565b1561215c5760405163071dd98160e11b81526004810183905290602082602481845afa918215611141575f92612128575b5060405163415b47c560e01b815290602082600481845afa918215611141575f926120f3575b509060206024926040519384809263078d049d60e51b82528860048301525afa918215611141575f926120bd575b5061201392612004670de0b6b3a76400009361200a93611aa5565b90611ad5565b04604d54611aa5565b604d555f5160206162215f395f51905f523b1561110d576040519063ca669fa760e01b825260048201525f81602481835f5160206162215f395f51905f525af18015611141576120aa575b506020546001600160a01b0316803b1561046657818091600460405180948193638660af9760e01b83525af18015610a1d57612098575050565b6120a3828092611a6b565b6103a95750565b6120b691505f90611a6b565b5f5f61205e565b91506020823d6020116120eb575b816120d860209383611a6b565b8101031261110d57905190612013611fe9565b3d91506120cb565b91506020823d602011612120575b8161210e60209383611a6b565b8101031261110d579051906020611fbb565b3d9150612101565b9091506020813d602011612154575b8161214460209383611a6b565b8101031261110d5751905f611f95565b3d9150612137565b505050565b90506020823d60201161218f575b8161217c60209383611a6b565b8101031261110d57611f64915190611f5a565b3d915061216f565b90506020813d6020116121c1575b816121b260209383611a6b565b8101031261110d57515f611f2d565b3d91506121a5565b90506020813d6020116121f3575b816121e460209383611a6b565b8101031261110d57515f611f03565b3d91506121d7565b612214915060203d6020116111ec576111de8183611a6b565b5f611eaa565b91908201809211611ab257565b67ffffffffffffffff8111611a575760051b60200190565b90604051915f8154908160011c9260018316928315612301575b6020851084146122ed5784875286939081156122cb5750600114612287575b5061228592500383611a6b565b565b90505f9291925260205f20905f915b8183106122af575050906020612285928201015f612278565b6020919350806001915483858901015201910190918492612296565b90506020925061228594915060ff191682840152151560051b8201015f612278565b634e487b7160e01b5f52602260045260245ffd5b93607f1693612259565b5f198114611ab25760010190565b8115611af2570690565b908161024091031261110d5760405190610240820182811067ffffffffffffffff821117611a5757604052805182526020810151602083015260408101516040830152606081015160ff8116810361110d5760608301526080810151608083015260a081015160a083015260c081015160c083015260e081015160e08301526101008101516101008301526101208101516101208301526101408101516101408301526101608101516101608301526101808101516101808301526101a08101516101a08301526101c081015190600682101561110d57610220916101c08401526101e08101516101e0840152610200810151610200840152015161022082015290565b601f54604051636146dd6f60e01b81525f9360089290921c6001600160a01b03169290602081600481875afa8015611141575f9061261b575b600191501461261557600a61247660305461230b565b806030550661261557604051636146dd6f60e01b8152602081600481875afa908115611141575f916125e3575b505f198101908111611ab2576124be61024091602493615f56565b93604051928380926366877b8d60e01b82528760048301525afa8015611141576101c0915f916125b4575b50015160068110156111b0576001190161215c576023546001600160a01b03165f5160206162215f395f51905f523b1561110d576040519063ca669fa760e01b825260048201525f81602481835f5160206162215f395f51905f525af180156111415761259f575b50601f5460081c6001600160a01b031691823b1561259b5790604484928360405195869485936321c221d760e01b8552600485015260248401525af18015610a1d57612098575050565b8380fd5b6125ac9193505f90611a6b565b5f915f612551565b6125d691506102403d81116125dc575b6125ce8183611a6b565b810190612323565b5f6124e9565b503d6125c4565b90506020813d60201161260d575b816125fe60209383611a6b565b8101031261110d57515f6124a3565b3d91506125f1565b50505050565b506020813d602011612646575b8161263560209383611a6b565b8101031261110d5760019051612460565b3d9150612628565b9081602091031261110d5751801515810361110d5790565b6001600160a01b039091168152602081019190915260400190565b6020805460405163217ac23760e01b81525f94936001600160a01b039092169281600481865afa908115611141575f91612cbf575b5060048110156111b057612615576126d46126d991602e5490612319565b611933565b905460405163469fab6f60e11b815260039290921b1c6001600160a01b031692602082600481865afa918215611141575f92612c8b575b50604051635d8d43b960e11b815291602083600481875afa918215611141575f92612c55575b6127409350615f62565b90604051635b00b19760e11b8152602081600481855afa8015611141575f90612c21575b61276f91508361221a565b60405163338ef3f160e01b815290602082600481865afa908115611141575f91612beb575b61279e925061221a565b604051635d8d43b960e11b815290602082600481865afa918215611141575f92612bb7575b5011612a2d575b50801561215c575f5160206162215f395f51905f523b1561110d576040516303223eab60e11b8152600481018390525f81602481835f5160206162215f395f51905f525af1801561114157612a18575b506021546020805460405163095ea7b360e01b81529283916001600160a01b0391821691839189918391612854918a911660048401612666565b03925af180156129e0576129eb575b506020546001600160a01b0316803b1561259b57838091602460405180948193637a3ad89360e01b83528760048401525af180156129e0579084916129c7575b505090612904826128b860049460375461221a565b6037558285526043602052604085206128d282825461221a565b90558285526042602052604085206128eb82825461221a565b90556128f98160415461221a565b60415560485461221a565b60485560208054604051631e9ea63960e11b815293849182906001600160a01b03165afa9182156129bc578392612988575b508252604460205260408220555f5160206162215f395f51905f523b156103a9576040516390c5013b60e01b81528181600481835f5160206162215f395f51905f525af18015610a1d57612098575050565b9091506020813d6020116129b4575b816129a460209383611a6b565b8101031261110d5751905f612936565b3d9150612997565b6040513d85823e3d90fd5b816129d191611a6b565b6129dc57825f6128a3565b8280fd5b6040513d86823e3d90fd5b612a0c9060203d602011612a11575b612a048183611a6b565b81019061264e565b612863565b503d6129fa565b612a259193505f90611a6b565b5f915f61281a565b604051635d8d43b960e11b8152909150602081600481855afa908115611141575f91612b85575b50604051635b00b19760e11b815290602082600481865afa908115611141575f91612b4f575b612a849250611aa5565b60405163338ef3f160e01b815290602082600481865afa918215611141575f92612b19575b50612ab8600492602092611aa5565b926040519283809263469fab6f60e11b82525afa908115611141575f91612ae7575b50811061215c575f6127ca565b90506020813d602011612b11575b81612b0260209383611a6b565b8101031261110d57515f612ada565b3d9150612af5565b91506020823d602011612b47575b81612b3460209383611a6b565b8101031261110d57905190612ab8612aa9565b3d9150612b27565b90506020823d602011612b7d575b81612b6a60209383611a6b565b8101031261110d57612a84915190612a7a565b3d9150612b5d565b90506020813d602011612baf575b81612ba060209383611a6b565b8101031261110d57515f612a54565b3d9150612b93565b9091506020813d602011612be3575b81612bd360209383611a6b565b8101031261110d5751905f6127c3565b3d9150612bc6565b90506020823d602011612c19575b81612c0660209383611a6b565b8101031261110d5761279e915190612794565b3d9150612bf9565b506020813d602011612c4d575b81612c3b60209383611a6b565b8101031261110d5761276f9051612764565b3d9150612c2e565b91506020833d602011612c83575b81612c7060209383611a6b565b8101031261110d57612740925191612736565b3d9150612c63565b9091506020813d602011612cb7575b81612ca760209383611a6b565b8101031261110d5751905f612710565b3d9150612c9a565b612cd8915060203d6020116111ec576111de8183611a6b565b5f6126b6565b601f54604051636146dd6f60e01b81525f929160081c6001600160a01b031690602081600481855afa8015611141575f90613185575b6001915003613113575b6040516366877b8d60e01b81526004810183905261024081602481855afa8015611141576101c0915f916130f4575b50015160068110156111b0575f190161215c576020805460405163217ac23760e01b81526001600160a01b039091169181600481855afa908115611141575f916130d5575b5060048110156111b057600114158061307e575b61261557610240602492604051938480926366877b8d60e01b82528760048301525afa80156111415760806020916004945f9161305f575b500151916040519384809263b3d814f560e01b82525afa918215611141575f9261302b575b5011613027576023546001600160a01b03165f5160206162215f395f51905f523b1561110d576040519063ca669fa760e01b825260048201525f81602481835f5160206162215f395f51905f525af1801561114157613012575b50601f5460465460475460089290921c6001600160a01b039081169281169116823b15611d5d5790606485928360405195869485936319e4bc1160e01b8552896004860152602485015260448401525af180156129bc57908391612ffd575b5050601f546040516366877b8d60e01b81526004810183905260089190911c6001600160a01b0316919061024081602481865afa9081156129e057612f10916080918691612fde575b50015160495461221a565b6049556040516366877b8d60e01b81526004810182905261024081602481865afa9081156129e05760806102409392612f55928791612fc1575b500151604854611aa5565b6048556024604051809481936366877b8d60e01b835260048301525afa918215612fb557612f919260809290612f96575b500151604e5461221a565b604e55565b612faf91506102403d81116125dc576125ce8183611a6b565b5f612f86565b604051903d90823e3d90fd5b612fd89150853d81116125dc576125ce8183611a6b565b5f612f4a565b612ff791506102403d81116125dc576125ce8183611a6b565b5f612f05565b8161300791611a6b565b61046657815f612ebc565b61301f9192505f90611a6b565b5f905f612e5d565b5050565b9091506020813d602011613057575b8161304760209383611a6b565b8101031261110d5751905f612e03565b3d915061303a565b61307891506102403d81116125dc576125ce8183611a6b565b5f612dde565b5060405163217ac23760e01b8152602081600481855afa908115611141575f916130b6575b5060048110156111b05760021415612da6565b6130cf915060203d6020116111ec576111de8183611a6b565b5f6130a3565b6130ee915060203d6020116111ec576111de8183611a6b565b5f612d92565b61310d91506102403d81116125dc576125ce8183611a6b565b5f612d4d565b90604051636146dd6f60e01b8152602081600481865afa908115611141575f91613153575b505f198101908111611ab25761314d91615f56565b90612d1e565b90506020813d60201161317d575b8161316e60209383611a6b565b8101031261110d57515f613138565b3d9150613161565b506020813d6020116131b0575b8161319f60209383611a6b565b8101031261110d5760019051612d14565b3d9150613192565b6020805460405163217ac23760e01b81525f94936001600160a01b039092169281600481865afa908115611141575f91613671575b5060048110156111b0576126155761320b61321091602d5490612319565b6118d7565b90546040516341b77a6760e11b815260039290921b1c6001600160a01b031692602082600481865afa918215611141575f9261363d575b5060405163088eafbd60e21b815291602083600481875afa918215611141575f92613607575b6132779350615f62565b90603554613285818461221a565b90613293603654809361221a565b60405163088eafbd60e21b815290602082600481885afa918215611141575f926135d3575b50116134fa575b505050801561215c575f5160206162215f395f51905f523b1561110d576040516303223eab60e11b8152600481018390525f81602481835f5160206162215f395f51905f525af18015611141576134e5575b506021546020805460405163095ea7b360e01b81529283916001600160a01b039182169183918991839161334b918a911660048401612666565b03925af180156129e0576134c8575b506020546001600160a01b0316803b1561259b57838091602460405180948193637c2c195160e01b83528760048401525af180156129e0579084916134b3575b5050906133fb826133af60049460355461221a565b603555828552603f602052604085206133c982825461221a565b9055828552603e602052604085206133e282825461221a565b90556133f081603d5461221a565b603d5560485461221a565b60485560208054604051633638f70360e01b815293849182906001600160a01b03165afa9182156129bc57839261347f575b508252604060205260408220555f5160206162215f395f51905f523b156103a9576040516390c5013b60e01b81528181600481835f5160206162215f395f51905f525af18015610a1d57612098575050565b9091506020813d6020116134ab575b8161349b60209383611a6b565b8101031261110d5751905f61342d565b3d915061348e565b816134bd91611a6b565b6129dc57825f61339a565b6134e09060203d602011612a1157612a048183611a6b565b61335a565b6134f29193505f90611a6b565b5f915f613311565b60405163088eafbd60e21b81529293509091602081600481875afa908115611141575f9161359e575b5060049261353660209361353b93611aa5565b611aa5565b92604051928380926341b77a6760e11b82525afa908115611141575f9161356c575b50811061215c575f80806132bf565b90506020813d602011613596575b8161358760209383611a6b565b8101031261110d57515f61355d565b3d915061357a565b9190506020823d6020116135cb575b816135ba60209383611a6b565b8101031261110d5790516004613523565b3d91506135ad565b9091506020813d6020116135ff575b816135ef60209383611a6b565b8101031261110d5751905f6132b8565b3d91506135e2565b91506020833d602011613635575b8161362260209383611a6b565b8101031261110d5761327792519161326d565b3d9150613615565b9091506020813d602011613669575b8161365960209383611a6b565b8101031261110d5751905f613247565b3d915061364c565b61368a915060203d6020116111ec576111de8183611a6b565b5f6131ed565b90604051918281549182825260208201905f5260205f20925f905b8060078301106137ed576122859454918181106137ce575b8181106137af575b818110613790575b818110613771575b818110613752575b818110613733575b818110613716575b10613701575b500383611a6b565b6001600160e01b03191681526020015f6136f9565b602083811b6001600160e01b0319168552909301926001016136f3565b604083901b6001600160e01b03191684526020909301926001016136eb565b606083901b6001600160e01b03191684526020909301926001016136e3565b608083901b6001600160e01b03191684526020909301926001016136db565b60a083901b6001600160e01b03191684526020909301926001016136d3565b60c083901b6001600160e01b03191684526020909301926001016136cb565b60e083901b6001600160e01b03191684526020909301926001016136c3565b916008919350610100600191865463ffffffff60e01b8160e01b16825263ffffffff60e01b8160c01b16602083015263ffffffff60e01b8160a01b16604083015263ffffffff60e01b8160801b16606083015263ffffffff60e01b8160601b16608083015263ffffffff60e01b8160401b1660a083015263ffffffff60e01b8160201b1660c083015263ffffffff60e01b1660e08201520194019201859293916136ab565b6020805460405163217ac23760e01b81525f9594936001600160a01b039092169281600481865afa908115611141575f91613b9a575b5060048110156111b057600303611e3757602d545f198101908111611ab2576138f091615f1f565b6138f9816118d7565b905460405163261497ad60e01b815260039290921b1c6001600160a01b03166004820181905293602082602481875afa908115611141575f91613b64575b6139419250615f1f565b918215611d8157604051633638f70360e01b815290602082600481845afa918215611141575f92613b2f575b5090602060249260405193848092630f37802160e11b82528960048301525afa918215611141575f92613afb575b5003613aec575b506139b6603554611c32603d549184611ad5565b915f5160206162215f395f51905f523b1561110d5760405163ca669fa760e01b8152600481018290525f81602481835f5160206162215f395f51905f525af1801561114157613ad7575b5060205485906001600160a01b0316803b1561046657819060246040518094819363527a7df960e01b83528860048401525af18015611d6157613ac2575b509060408583613a9694611d31979852603f602052858383205410155f14613ab057808252603f602052828220613a76878254611aa5565b90555b8152603e60205220613a8c828254611aa5565b9055603d54611aa5565b603d55613aa581603554611aa5565b603555604854611aa5565b808252603f6020528183812055613a79565b613acd868092611a6b565b611d5d575f613a3e565b613ae49195505f90611a6b565b5f935f613a00565b613af590615b88565b5f6139a2565b9091506020813d602011613b27575b81613b1760209383611a6b565b8101031261110d5751905f61399b565b3d9150613b0a565b91506020823d602011613b5c575b81613b4a60209383611a6b565b8101031261110d57905190602061396d565b3d9150613b3d565b90506020823d602011613b92575b81613b7f60209383611a6b565b8101031261110d57613941915190613937565b3d9150613b72565b613bb3915060203d6020116111ec576111de8183611a6b565b5f6138c8565b6020805460405163217ac23760e01b81525f94936001600160a01b039092169281600481865afa908115611141575f9161406d575b5060048110156111b05761261557613c0c613c1191602c5490612319565b611903565b9054604051633b6e159160e01b815260039290921b1c6001600160a01b031692602082600481865afa918215611141575f92614039575b506040516306fa495360e41b815291602083600481875afa918215611141575f92614003575b613c789350615f62565b90603354613c86818461221a565b90613c94603454809361221a565b6040516306fa495360e41b815290602082600481885afa918215611141575f92613fcf575b5011613efb575b505050801561215c575f5160206162215f395f51905f523b1561110d576040516303223eab60e11b8152600481018390525f81602481835f5160206162215f395f51905f525af1801561114157613ee6575b506021546020805460405163095ea7b360e01b81529283916001600160a01b0391821691839189918391613d4c918a911660048401612666565b03925af180156129e057613ec9575b506020546001600160a01b0316803b1561259b578380916024604051809481936302ad35ed60e51b83528760048401525af180156129e057908491613eb4575b505090613dfc82613db060049460335461221a565b603355828552603b60205260408520613dca82825461221a565b9055828552603a60205260408520613de382825461221a565b9055613df18160395461221a565b60395560485461221a565b6048556020805460405163415b47c560e01b815293849182906001600160a01b03165afa9182156129bc578392613e80575b508252603c60205260408220555f5160206162215f395f51905f523b156103a9576040516390c5013b60e01b81528181600481835f5160206162215f395f51905f525af18015610a1d57612098575050565b9091506020813d602011613eac575b81613e9c60209383611a6b565b8101031261110d5751905f613e2e565b3d9150613e8f565b81613ebe91611a6b565b6129dc57825f613d9b565b613ee19060203d602011612a1157612a048183611a6b565b613d5b565b613ef39193505f90611a6b565b5f915f613d12565b6040516306fa495360e41b81529293509091602081600481875afa908115611141575f91613f9a575b50600492613536602093613f3793611aa5565b9260405192838092633b6e159160e01b82525afa908115611141575f91613f68575b50811061215c575f8080613cc0565b90506020813d602011613f92575b81613f8360209383611a6b565b8101031261110d57515f613f59565b3d9150613f76565b9190506020823d602011613fc7575b81613fb660209383611a6b565b8101031261110d5790516004613f24565b3d9150613fa9565b9091506020813d602011613ffb575b81613feb60209383611a6b565b8101031261110d5751905f613cb9565b3d9150613fde565b91506020833d602011614031575b8161401e60209383611a6b565b8101031261110d57613c78925191613c6e565b3d9150614011565b9091506020813d602011614065575b8161405560209383611a6b565b8101031261110d5751905f613c48565b3d9150614048565b614086915060203d6020116111ec576111de8183611a6b565b5f613bee565b6020805460405163217ac23760e01b81525f9594936001600160a01b039092169281600481865afa908115611141575f91614394575b5060048110156111b057600303611e3757602c545f198101908111611ab2576140ea91615f1f565b6140f381611903565b905460405163071dd98160e11b815260039290921b1c6001600160a01b03166004820181905293602082602481875afa908115611141575f9161435e575b61413b9250615f1f565b918215611d815760405163415b47c560e01b815290602082600481845afa918215611141575f92614329575b509060206024926040519384809263078d049d60e51b82528960048301525afa918215611141575f926142f5575b50036142e6575b506141b0603354611c326039549184611ad5565b915f5160206162215f395f51905f523b1561110d5760405163ca669fa760e01b8152600481018290525f81602481835f5160206162215f395f51905f525af18015611141576142d1575b5060205485906001600160a01b0316803b15610466578190602460405180948193639dc79d0960e01b83528860048401525af18015611d61576142bc575b50906040858361429094611d31979852603b602052858383205410155f146142aa57808252603b602052828220614270878254611aa5565b90555b8152603a60205220614286828254611aa5565b9055603954611aa5565b60395561429f81603354611aa5565b603355604854611aa5565b808252603b6020528183812055614273565b6142c7868092611a6b565b611d5d575f614238565b6142de9195505f90611a6b565b5f935f6141fa565b6142ef90611e5d565b5f61419c565b9091506020813d602011614321575b8161431160209383611a6b565b8101031261110d5751905f614195565b3d9150614304565b91506020823d602011614356575b8161434460209383611a6b565b8101031261110d579051906020614167565b3d9150614337565b90506020823d60201161438c575b8161437960209383611a6b565b8101031261110d5761413b915190614131565b3d915061436c565b6143ad915060203d6020116111ec576111de8183611a6b565b5f6140c2565b601f54604051636146dd6f60e01b815260089190911c6001600160a01b0316915f91602081600481875afa8015611141575f9061461c575b600191501461215c57601461440160315461230b565b806031550661215c57604051636146dd6f60e01b8152602081600481875afa908115611141575f916145ea575b505f198101908111611ab25761444391615f56565b916040516366877b8d60e01b815283600482015261024081602481855afa8015611141576101c0915f916145cb575b50015160068110156111b0576003190161215c57610240602491604051928380926366877b8d60e01b82528760048301525afa80156111415760a0915f916145ac575b5001516023549092906001600160a01b03165f5160206162215f395f51905f523b1561110d576040519063ca669fa760e01b825260048201525f81602481835f5160206162215f395f51905f525af1801561114157614597575b50601f5460081c6001600160a01b031690813b156129dc578291602483926040519485938492631c9f7dd760e21b845260048401525af18015610a1d57614582575b50508061456361457d92604954611aa5565b60495561457281604e54611aa5565b604e55604b5461221a565b604b55565b61458d828092611a6b565b6103a95780614551565b6145a49192505f90611a6b565b5f905f61450f565b6145c591506102403d81116125dc576125ce8183611a6b565b5f6144b5565b6145e491506102403d81116125dc576125ce8183611a6b565b5f614472565b90506020813d602011614614575b8161460560209383611a6b565b8101031261110d57515f61442e565b3d91506145f8565b506020813d602011614647575b8161463660209383611a6b565b8101031261110d57600190516143eb565b3d9150614629565b602e545f91905f198101908111611ab25761466991615f1f565b6020805460405163641ad8a960e01b81526001600160a01b03909116929181600481865afa908115611141575f916149c7575b5060048110156111b05760030361215c576146b690611933565b9054604051632183fd1760e21b815260039290921b1c6001600160a01b0316600482018190529190602081602481855afa908115611141575f91614995575b501561215c57604051631e9ea63960e11b8152602081600481855afa908115611141575f91614963575b506040516346d13a7b60e01b81526004810184905290602082602481865afa908115611141575f9161492d575b6147569250611aa5565b1561215c57604051632183fd1760e21b81526004810183905290602082602481845afa918215611141575f926148f9575b50604051631e9ea63960e11b815290602082600481845afa918215611141575f926148c4575b50906020602492604051938480926346d13a7b60e01b82528860048301525afa918215611141575f9261488e575b506147f692612004670de0b6b3a76400009361200a93611aa5565b604d555f5160206162215f395f51905f523b1561110d576040519063ca669fa760e01b825260048201525f81602481835f5160206162215f395f51905f525af180156111415761487b575b506020546001600160a01b0316803b156104665781809160046040518094819363782de3d760e11b83525af18015610a1d57612098575050565b61488791505f90611a6b565b5f5f614841565b91506020823d6020116148bc575b816148a960209383611a6b565b8101031261110d579051906147f66147db565b3d915061489c565b91506020823d6020116148f1575b816148df60209383611a6b565b8101031261110d5790519060206147ad565b3d91506148d2565b9091506020813d602011614925575b8161491560209383611a6b565b8101031261110d5751905f614787565b3d9150614908565b90506020823d60201161495b575b8161494860209383611a6b565b8101031261110d5761475691519061474c565b3d915061493b565b90506020813d60201161498d575b8161497e60209383611a6b565b8101031261110d57515f61471f565b3d9150614971565b90506020813d6020116149bf575b816149b060209383611a6b565b8101031261110d57515f6146f5565b3d91506149a3565b6149e0915060203d6020116111ec576111de8183611a6b565b5f61469c565b601f54604051636146dd6f60e01b815291935f939092909160081c6001600160a01b031690602081600481855afa8015611141575f90614e3d575b6001915014614de357604051636146dd6f60e01b8152602081600481855afa908115611141575f91614e0b575b505f198101908111611ab257614a6961024091602497615f56565b91604051968780926366877b8d60e01b82528560048301525afa948515611141575f95614dea575b506101c085015160068110156111b05760011901614de3575f80604051614ab9604082611a6b565b60048152636865726560e01b6020820152604051614b0281614af4602082019463104c13eb60e21b8652602060248401526044830190611876565b03601f198101835282611a6b565b51906a636f6e736f6c652e6c6f675afa50614b2360a0860192835190615f1f565b91614b47614b40610100614b3685615f6d565b980197885161221a565b8095615f1f565b9383158080614ddb575b614dd157159081614dc8575b81614dbe575b50614db657614b86614b75858561221a565b9651614b8084615f6d565b9061221a565b80871015614db0575085905b614b9c8288611aa5565b905180821015614da85750955b6046546001600160a01b03165f5160206162215f395f51905f523b1561110d576040519063ca669fa760e01b825260048201525f81602481835f5160206162215f395f51905f525af1801561114157614d92575b50602154601f5460405163095ea7b360e01b81529260209284926001600160a01b039182169284928c928492614c3c92909160081c1660048401612666565b03925af18015611d615790614c5a9291614d75575b50604d5461221a565b604d556023546001600160a01b03165f5160206162215f395f51905f523b15611d5d576040519063ca669fa760e01b825260048201528481602481835f5160206162215f395f51905f525af18015614d6a57908591614d55575b5050601f546046546001600160a01b0360089290921c82169116813b15614d515791856084928195946040519788968795630b43a5bf60e11b875260048701526024860152604485015260648401525af18015610a1d57614d3c575b505080614d22612f9192604954611aa5565b604955614d318160485461221a565b604855604e54611aa5565b614d47828092611a6b565b6103a95780614d10565b8580fd5b81614d5f91611a6b565b61259b57835f614cb4565b6040513d87823e3d90fd5b614d8d9060203d602011612a1157612a048183611a6b565b614c51565b614d9f9196505f90611a6b565b5f946020614bfd565b905095614ba9565b90614b92565b505050505050565b905015155f614b63565b85159150614b5d565b5050505050505050565b508515614b51565b5050505050565b614e049195506102403d81116125dc576125ce8183611a6b565b935f614a91565b90506020813d602011614e35575b81614e2660209383611a6b565b8101031261110d57515f614a4e565b3d9150614e19565b506020813d602011614e68575b81614e5760209383611a6b565b8101031261110d5760019051614a21565b3d9150614e4a565b602080546040516303c7543760e41b81525f926001600160a01b039092169181600481855afa908115611141575f91614fbb575b501590811591614f5f575b50614f5c576023546001600160a01b03165f5160206162215f395f51905f523b1561110d576040519063ca669fa760e01b825260048201525f81602481835f5160206162215f395f51905f525af1801561114157614f49575b506020546001600160a01b0316803b15610466578180916024604051809481936377dd846960e01b8352600360048401525af18015610a1d57612098575050565b614f5591505f90611a6b565b5f5f614f08565b50565b60405163217ac23760e01b81529150602090829060049082905afa908115611141575f91614f9c575b5060048110156111b057600214155f614eaf565b614fb5915060203d6020116111ec576111de8183611a6b565b5f614f88565b90506020813d602011614fe5575b81614fd660209383611a6b565b8101031261110d57515f614ea4565b3d9150614fc9565b601f54604051636146dd6f60e01b815291935f9360089290921c6001600160a01b031692909190602081600481875afa8015611141575f906153bb575b6001915014614de357601e61504060325461230b565b8060325506614de357604051636146dd6f60e01b8152602081600481875afa908115611141575f91615389575b505f198101908111611ab25761508861024091602497615f56565b93604051968780926366877b8d60e01b82528760048301525afa948515611141575f95615368575b506101c085015160068110156111b05760041901614de35760806150dd613c0c6150f594602c5490612319565b60018060a01b0391549060031b1c1695015190615f56565b925f5160206162215f395f51905f523b1561110d576040516303223eab60e11b8152600481018290525f81602481835f5160206162215f395f51905f525af1801561114157615353575b506021546001600160a01b0316803b1561259b578360405180926340c10f1960e01b82528183816151748b8960048401612666565b03925af180156129e05790849161533e575b50506151c460208560018060a01b036021541660018060a01b03601f5460081c168760405180968195829463095ea7b360e01b845260048401612666565b03925af180156129e057615321575b505f5160206162215f395f51905f523b156129dc576040516390c5013b60e01b81528381600481835f5160206162215f395f51905f525af180156129e05790849161530c575b50506023546001600160a01b03165f5160206162215f395f51905f523b1561259b576040519063ca669fa760e01b825260048201528381602481835f5160206162215f395f51905f525af180156129e0579084916152f7575b5050601f5460081c6001600160a01b031691823b1561259b5790606484928360405195869485936348abb7e360e01b8552600485015289602485015260448401525af18015610a1d576152e2575b5050806152d26152dd9260485461221a565b604855604c5461221a565b604c55565b6152ed828092611a6b565b6103a957806152c0565b8161530191611a6b565b6129dc57825f615272565b8161531691611a6b565b6129dc57825f615219565b6153399060203d602011612a1157612a048183611a6b565b6151d3565b8161534891611a6b565b6129dc57825f615186565b6153609193505f90611a6b565b5f915f61513f565b6153829195506102403d81116125dc576125ce8183611a6b565b935f6150b0565b90506020813d6020116153b3575b816153a460209383611a6b565b8101031261110d57515f61506d565b3d9150615397565b506020813d6020116153e6575b816153d560209383611a6b565b8101031261110d576001905161502a565b3d91506153c8565b6020805460405163217ac23760e01b81525f969495936001600160a01b039092169281600481865afa908115611141575f91615ace575b5060048110156111b0576001141580615a77575b614db6576027549060ff602554165f146159fe5760405163b3d814f560e01b8152602081600481875afa80156111415783915f916159c9575b5010615973575b60405163b3d814f560e01b8152602081600481875afa80156111415783915f9161593e575b50106159355760285460405163b3d814f560e01b81529290602084600481885afa8015611141575f90615901575b6154e09450808210156158f9575091615f62565b9060405163b3d814f560e01b8152602081600481855afa8015611141575f906158c6575b600a9150048211615860575b50602954601f54604051636780f97760e01b815260089190911c6001600160a01b0316956020826004818a5afa918215611141575f9261582a575b50906155679261555a92615f62565b92602a54602b5491615f62565b60018060a01b03602254166020602f54602460405180948193634c2d62b760e01b835260048301525afa908115611141575f9161580b575b5015614db65760049060206155be6155b960455488612319565b61191b565b90549060031b1c604051828101916bffffffffffffffffffffffff199060601b168252876034820152603481526155f6605482611a6b565b5190209660405193848092636146dd6f60e01b82525afa918215611141575f926157d7575b50604051918060208401528560408401528360608401528460808401528160a084015260a0835261564d60c084611a6b565b6023546001600160a01b03165f5160206162215f395f51905f523b1561110d576040519063ca669fa760e01b825260048201525f81602481835f5160206162215f395f51905f525af18015611141576157c2575b5060018060a01b03601f5460081c169560405190602082019283526040820152876060820152426080820152608081526156dc60a082611a6b565b51902093602f5493602094604051966156f58789611a6b565b8a88525f368137883b156157be5760405163d63792a760e01b8152600481019a909a5260248a015260448901526001606489015260848801526101f460a488015260c487015260e48601526101048501869052610160610124860152859385939092909161576890610164860190611876565b84810360031901610144860152825180825290820192820191865b8281106157a457505050508383809203925af18015610a1d57612098575050565b835185528997508896509381019392810192600101615783565b8a80fd5b6157cf9198505f90611a6b565b5f965f6156a1565b9091506020813d602011615803575b816157f360209383611a6b565b8101031261110d5751905f61561b565b3d91506157e6565b615824915060203d602011612a1157612a048183611a6b565b5f61559f565b91506020823d602011615858575b8161584560209383611a6b565b8101031261110d5790519061556761554b565b3d9150615838565b60405163b3d814f560e01b81529150602090829060049082905afa8015611141575f90615893575b600a9150045f615510565b506020813d6020116158be575b816158ad60209383611a6b565b8101031261110d57600a9051615888565b3d91506158a0565b506020813d6020116158f1575b816158e060209383611a6b565b8101031261110d57600a9051615504565b3d91506158d3565b905091615f62565b506020843d60201161592d575b8161591b60209383611a6b565b8101031261110d576154e093516154cc565b3d915061590e565b50505050505050565b9150506020813d60201161596b575b8161595a60209383611a6b565b8101031261110d578290515f61549e565b3d915061594d565b60405163b3d814f560e01b8152602081600481875afa80156111415761599a575b50615479565b6159bb9060203d6020116159c2575b6159b38183611a6b565b810190611ac6565b505f615994565b503d6159a9565b9150506020813d6020116159f6575b816159e560209383611a6b565b8101031261110d578290515f615472565b3d91506159d8565b60405163b3d814f560e01b8152602081600481875afa908115611141575f91615a45575b50600a830290838204600a1484151715611ab25710156154795750505050505050565b90506020813d602011615a6f575b81615a6060209383611a6b565b8101031261110d57515f615a22565b3d9150615a53565b5060405163217ac23760e01b8152602081600481865afa908115611141575f91615aaf575b5060048110156111b05760021415615439565b615ac8915060203d6020116111ec576111de8183611a6b565b5f615a9c565b615ae7915060203d6020116111ec576111de8183611a6b565b5f615425565b60085460ff1615615afd57600190565b604051630667f9d760e41b81525f5160206162215f395f51905f5260048201526519985a5b195960d21b60248201526020816044815f5160206162215f395f51905f525afa908115611141575f91615b56575b50151590565b90506020813d602011615b80575b81615b7160209383611a6b565b8101031261110d57515f615b50565b3d9150615b64565b602d545f91905f198101908111611ab257615ba291615f1f565b6020805460405163641ad8a960e01b81526001600160a01b03909116929181600481865afa908115611141575f91615f00575b5060048110156111b05760030361215c57615bef906118d7565b905460405163261497ad60e01b815260039290921b1c6001600160a01b0316600482018190529190602081602481855afa908115611141575f91615ece575b501561215c57604051633638f70360e01b8152602081600481855afa908115611141575f91615e9c575b50604051630f37802160e11b81526004810184905290602082602481865afa908115611141575f91615e66575b615c8f9250611aa5565b1561215c5760405163261497ad60e01b81526004810183905290602082602481845afa918215611141575f92615e32575b50604051633638f70360e01b815290602082600481845afa918215611141575f92615dfd575b5090602060249260405193848092630f37802160e11b82528860048301525afa918215611141575f92615dc7575b50615d2f92612004670de0b6b3a76400009361200a93611aa5565b604d555f5160206162215f395f51905f523b1561110d576040519063ca669fa760e01b825260048201525f81602481835f5160206162215f395f51905f525af1801561114157615db4575b506020546001600160a01b0316803b15610466578180916004604051809481936331366ca160e01b83525af18015610a1d57612098575050565b615dc091505f90611a6b565b5f5f615d7a565b91506020823d602011615df5575b81615de260209383611a6b565b8101031261110d57905190615d2f615d14565b3d9150615dd5565b91506020823d602011615e2a575b81615e1860209383611a6b565b8101031261110d579051906020615ce6565b3d9150615e0b565b9091506020813d602011615e5e575b81615e4e60209383611a6b565b8101031261110d5751905f615cc0565b3d9150615e41565b90506020823d602011615e94575b81615e8160209383611a6b565b8101031261110d57615c8f915190615c85565b3d9150615e74565b90506020813d602011615ec6575b81615eb760209383611a6b565b8101031261110d57515f615c58565b3d9150615eaa565b90506020813d602011615ef8575b81615ee960209383611a6b565b8101031261110d57515f615c2e565b3d9150615edc565b615f19915060203d6020116111ec576111de8183611a6b565b5f615bd5565b905f615f2a9261607c565b90612285615f4261099b60405161094a604082611a6b565b86604483015203601f198101835282611a6b565b906001615f2a9261607c565b90615f2a929161607c565b601f54604051636146dd6f60e01b815260089190911c6001600160a01b031691602082600481865afa918215611141575f92616048575b505f198201918211611ab25761024091615fbd91615f56565b6024604051809481936366877b8d60e01b835260048301525afa908115611141575f91616029575b50615ff561014082015142611aa5565b60a08201519081156160225761601961601e9260c064496cebb80095015190611ad5565b611ad5565b0490565b5050505f90565b61604291506102403d81116125dc576125ce8183611a6b565b5f615fe5565b9091506020813d602011616074575b8161606460209383611a6b565b8101031261110d5751905f615fa4565b3d9150616057565b5f9083831161619b5782811091821580616191575b6161895761609f8486611aa5565b9260018401809411611ab257600383111580616180575b6161715760031983101580616167575b616153578583111561610b575050906160e2846160e793611aa5565b612319565b908115616106576160f8925061221a565b5f198101908111611ab25790565b505090565b95949291909561611b5750505050565b839495506160e29061612d9394611aa5565b9081156161065761613e9250611aa5565b60018101809111611ab257905f808080612615565b505090506161649291501990611aa5565b90565b50821984116160c6565b5050919050616164925061221a565b508284116160b6565b509250505090565b5084821115616091565b60405162461bcd60e51b815260206004820152603e60248201527f5374645574696c7320626f756e642875696e743235362c75696e743235362c7560448201527f696e74323536293a204d6178206973206c657373207468616e206d696e2e00006064820152608490fd5b5f80916020815191016a636f6e736f6c652e6c6f675afa5056fe0000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da264697066735822122090953c6b2f64be49c03e7e4a886801f08f42017559ebe753810c133e9ee79f2b64736f6c634300082100330000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12d"

    @overload
    @classmethod
    def deploy(cls, _loanEngine: LoanEngine, _tranchePool: TranchePool, _creditPolicy: CreditPolicy, _usdt: ERC20Mock, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#72)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#72)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#72)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#72)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#72)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#72)

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
    def equityTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#53)

        Returns:
            equityTrancheTotalShares: uint256
        """
        ...

    @overload
    def equityTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#53)

        Returns:
            equityTrancheTotalShares: uint256
        """
        ...

    @overload
    def equityTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#53)

        Returns:
            equityTrancheTotalShares: uint256
        """
        ...

    @overload
    def equityTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#53)

        Returns:
            equityTrancheTotalShares: uint256
        """
        ...

    def equityTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#53)

        Returns:
            equityTrancheTotalShares: uint256
        """
        return self._execute(self.chain, request_type, "f630683e", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def equityTrancheShares(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#54)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def equityTrancheShares(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#54)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def equityTrancheShares(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#54)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def equityTrancheShares(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#54)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    def equityTrancheShares(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#54)

        Args:
            key0: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "f7edfa96", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def equityTrancheDeposits(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#55)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def equityTrancheDeposits(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#55)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def equityTrancheDeposits(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#55)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def equityTrancheDeposits(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#55)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    def equityTrancheDeposits(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#55)

        Args:
            key0: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "97be042e", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def equityUserIndex(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#56)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def equityUserIndex(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#56)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def equityUserIndex(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#56)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def equityUserIndex(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#56)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    def equityUserIndex(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#56)

        Args:
            key0: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "81eb2809", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def loanBorrowers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#58)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    @overload
    def loanBorrowers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#58)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    @overload
    def loanBorrowers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#58)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    @overload
    def loanBorrowers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#58)

        Args:
            index0: uint256
        Returns:
            address
        """
        ...

    def loanBorrowers(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#58)

        Args:
            index0: uint256
        Returns:
            address
        """
        return self._execute(self.chain, request_type, "6a74c548", [index0], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def recevingEntity(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#60)

        Returns:
            recevingEntity: address
        """
        ...

    @overload
    def recevingEntity(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#60)

        Returns:
            recevingEntity: address
        """
        ...

    @overload
    def recevingEntity(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#60)

        Returns:
            recevingEntity: address
        """
        ...

    @overload
    def recevingEntity(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#60)

        Returns:
            recevingEntity: address
        """
        ...

    def recevingEntity(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#60)

        Returns:
            recevingEntity: address
        """
        return self._execute(self.chain, request_type, "bb85e79c", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def feeManager(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#61)

        Returns:
            feeManager: address
        """
        ...

    @overload
    def feeManager(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#61)

        Returns:
            feeManager: address
        """
        ...

    @overload
    def feeManager(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#61)

        Returns:
            feeManager: address
        """
        ...

    @overload
    def feeManager(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#61)

        Returns:
            feeManager: address
        """
        ...

    def feeManager(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#61)

        Returns:
            feeManager: address
        """
        return self._execute(self.chain, request_type, "d0fb0203", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#63)

        Returns:
            totalIdleValue: uint256
        """
        ...

    @overload
    def totalIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#63)

        Returns:
            totalIdleValue: uint256
        """
        ...

    @overload
    def totalIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#63)

        Returns:
            totalIdleValue: uint256
        """
        ...

    @overload
    def totalIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#63)

        Returns:
            totalIdleValue: uint256
        """
        ...

    def totalIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#63)

        Returns:
            totalIdleValue: uint256
        """
        return self._execute(self.chain, request_type, "fc5b0840", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#64)

        Returns:
            totalDeployedValue: uint256
        """
        ...

    @overload
    def totalDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#64)

        Returns:
            totalDeployedValue: uint256
        """
        ...

    @overload
    def totalDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#64)

        Returns:
            totalDeployedValue: uint256
        """
        ...

    @overload
    def totalDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#64)

        Returns:
            totalDeployedValue: uint256
        """
        ...

    def totalDeployedValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#64)

        Returns:
            totalDeployedValue: uint256
        """
        return self._execute(self.chain, request_type, "2d8d435d", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalDeposited(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#65)

        Returns:
            totalDeposited: uint256
        """
        ...

    @overload
    def totalDeposited(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#65)

        Returns:
            totalDeposited: uint256
        """
        ...

    @overload
    def totalDeposited(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#65)

        Returns:
            totalDeposited: uint256
        """
        ...

    @overload
    def totalDeposited(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#65)

        Returns:
            totalDeposited: uint256
        """
        ...

    def totalDeposited(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#65)

        Returns:
            totalDeposited: uint256
        """
        return self._execute(self.chain, request_type, "ff50abdc", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalLoss(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#66)

        Returns:
            totalLoss: uint256
        """
        ...

    @overload
    def totalLoss(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#66)

        Returns:
            totalLoss: uint256
        """
        ...

    @overload
    def totalLoss(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#66)

        Returns:
            totalLoss: uint256
        """
        ...

    @overload
    def totalLoss(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#66)

        Returns:
            totalLoss: uint256
        """
        ...

    def totalLoss(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#66)

        Returns:
            totalLoss: uint256
        """
        return self._execute(self.chain, request_type, "0d457ee1", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalRecovered(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#67)

        Returns:
            totalRecovered: uint256
        """
        ...

    @overload
    def totalRecovered(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#67)

        Returns:
            totalRecovered: uint256
        """
        ...

    @overload
    def totalRecovered(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#67)

        Returns:
            totalRecovered: uint256
        """
        ...

    @overload
    def totalRecovered(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#67)

        Returns:
            totalRecovered: uint256
        """
        ...

    def totalRecovered(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#67)

        Returns:
            totalRecovered: uint256
        """
        return self._execute(self.chain, request_type, "ca1a6fbb", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalUnclaimedInterest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#68)

        Returns:
            totalUnclaimedInterest: uint256
        """
        ...

    @overload
    def totalUnclaimedInterest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#68)

        Returns:
            totalUnclaimedInterest: uint256
        """
        ...

    @overload
    def totalUnclaimedInterest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#68)

        Returns:
            totalUnclaimedInterest: uint256
        """
        ...

    @overload
    def totalUnclaimedInterest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#68)

        Returns:
            totalUnclaimedInterest: uint256
        """
        ...

    def totalUnclaimedInterest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#68)

        Returns:
            totalUnclaimedInterest: uint256
        """
        return self._execute(self.chain, request_type, "9a2ef2eb", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def outStandingPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#70)

        Returns:
            outStandingPrincipal: uint256
        """
        ...

    @overload
    def outStandingPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#70)

        Returns:
            outStandingPrincipal: uint256
        """
        ...

    @overload
    def outStandingPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#70)

        Returns:
            outStandingPrincipal: uint256
        """
        ...

    @overload
    def outStandingPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#70)

        Returns:
            outStandingPrincipal: uint256
        """
        ...

    def outStandingPrincipal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#70)

        Returns:
            outStandingPrincipal: uint256
        """
        return self._execute(self.chain, request_type, "e691bb9e", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def depositSeniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#126)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def depositSeniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#126)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def depositSeniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#126)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def depositSeniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#126)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    def depositSeniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#126)

        Args:
            userIndex: uint256
            amount: uint256
        """
        return self._execute(self.chain, request_type, "7a493f2f", [userIndex, amount], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def depositJuniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#161)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def depositJuniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#161)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def depositJuniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#161)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def depositJuniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#161)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    def depositJuniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#161)

        Args:
            userIndex: uint256
            amount: uint256
        """
        return self._execute(self.chain, request_type, "574ca186", [userIndex, amount], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def depositEquityTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#196)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def depositEquityTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#196)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def depositEquityTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#196)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def depositEquityTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#196)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    def depositEquityTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#196)

        Args:
            userIndex: uint256
            amount: uint256
        """
        return self._execute(self.chain, request_type, "3964924b", [userIndex, amount], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def maybeCommitPool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#236)
        """
        ...

    @overload
    def maybeCommitPool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#236)
        """
        ...

    @overload
    def maybeCommitPool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#236)
        """
        ...

    @overload
    def maybeCommitPool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#236)
        """
        ...

    def maybeCommitPool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#236)
        """
        return self._execute(self.chain, request_type, "507f253f", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def createLoan(self, principalIssued: uint256, originationFeeBps: uint256, termDays: uint256, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#247)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#247)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#247)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#247)

        Args:
            principalIssued: uint256
            originationFeeBps: uint256
            termDays: uint256
            userIndex: uint256
        """
        ...

    def createLoan(self, principalIssued: uint256, originationFeeBps: uint256, termDays: uint256, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#247)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#329)

        Args:
            loanId: uint256
        """
        ...

    @overload
    def activateLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#329)

        Args:
            loanId: uint256
        """
        ...

    @overload
    def activateLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#329)

        Args:
            loanId: uint256
        """
        ...

    @overload
    def activateLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#329)

        Args:
            loanId: uint256
        """
        ...

    def activateLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#329)

        Args:
            loanId: uint256
        """
        return self._execute(self.chain, request_type, "4644004d", [loanId], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#363)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
        """
        ...

    @overload
    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#363)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
        """
        ...

    @overload
    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#363)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
        """
        ...

    @overload
    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#363)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
        """
        ...

    def repayLoan(self, loanId: uint256, principalAmount: uint256, interestAmount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#363)

        Args:
            loanId: uint256
            principalAmount: uint256
            interestAmount: uint256
        """
        return self._execute(self.chain, request_type, "8c8489f2", [loanId, principalAmount, interestAmount], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def warpTime(self, daysToWarp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#423)

        Args:
            daysToWarp: uint256
        """
        ...

    @overload
    def warpTime(self, daysToWarp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#423)

        Args:
            daysToWarp: uint256
        """
        ...

    @overload
    def warpTime(self, daysToWarp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#423)

        Args:
            daysToWarp: uint256
        """
        ...

    @overload
    def warpTime(self, daysToWarp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#423)

        Args:
            daysToWarp: uint256
        """
        ...

    def warpTime(self, daysToWarp: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#423)

        Args:
            daysToWarp: uint256
        """
        return self._execute(self.chain, request_type, "9bddafe8", [daysToWarp], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def maybeDeclareDefault(self, loanId: uint256, reasonHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#428)

        Args:
            loanId: uint256
            reasonHash: bytes32
        """
        ...

    @overload
    def maybeDeclareDefault(self, loanId: uint256, reasonHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#428)

        Args:
            loanId: uint256
            reasonHash: bytes32
        """
        ...

    @overload
    def maybeDeclareDefault(self, loanId: uint256, reasonHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#428)

        Args:
            loanId: uint256
            reasonHash: bytes32
        """
        ...

    @overload
    def maybeDeclareDefault(self, loanId: uint256, reasonHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#428)

        Args:
            loanId: uint256
            reasonHash: bytes32
        """
        ...

    def maybeDeclareDefault(self, loanId: uint256, reasonHash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#428)

        Args:
            loanId: uint256
            reasonHash: bytes32
        """
        return self._execute(self.chain, request_type, "2ec3ad92", [loanId, reasonHash], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def maybeWriteOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#451)

        Args:
            loanId: uint256
        """
        ...

    @overload
    def maybeWriteOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#451)

        Args:
            loanId: uint256
        """
        ...

    @overload
    def maybeWriteOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#451)

        Args:
            loanId: uint256
        """
        ...

    @overload
    def maybeWriteOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#451)

        Args:
            loanId: uint256
        """
        ...

    def maybeWriteOffLoan(self, loanId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#451)

        Args:
            loanId: uint256
        """
        return self._execute(self.chain, request_type, "85218344", [loanId], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def maybeRecoverLoan(self, loanId: uint256, amount: uint256, agentIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#484)

        Args:
            loanId: uint256
            amount: uint256
            agentIndex: uint256
        """
        ...

    @overload
    def maybeRecoverLoan(self, loanId: uint256, amount: uint256, agentIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#484)

        Args:
            loanId: uint256
            amount: uint256
            agentIndex: uint256
        """
        ...

    @overload
    def maybeRecoverLoan(self, loanId: uint256, amount: uint256, agentIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#484)

        Args:
            loanId: uint256
            amount: uint256
            agentIndex: uint256
        """
        ...

    @overload
    def maybeRecoverLoan(self, loanId: uint256, amount: uint256, agentIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#484)

        Args:
            loanId: uint256
            amount: uint256
            agentIndex: uint256
        """
        ...

    def maybeRecoverLoan(self, loanId: uint256, amount: uint256, agentIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#484)

        Args:
            loanId: uint256
            amount: uint256
            agentIndex: uint256
        """
        return self._execute(self.chain, request_type, "a6b590e8", [loanId, amount, agentIndex], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def mayClosePool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#523)
        """
        ...

    @overload
    def mayClosePool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#523)
        """
        ...

    @overload
    def mayClosePool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#523)
        """
        ...

    @overload
    def mayClosePool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#523)
        """
        ...

    def mayClosePool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#523)
        """
        return self._execute(self.chain, request_type, "960b2f9d", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def claimSeniorTrancheInterest(self, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#531)

        Args:
            userIndex: uint256
        """
        ...

    @overload
    def claimSeniorTrancheInterest(self, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#531)

        Args:
            userIndex: uint256
        """
        ...

    @overload
    def claimSeniorTrancheInterest(self, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#531)

        Args:
            userIndex: uint256
        """
        ...

    @overload
    def claimSeniorTrancheInterest(self, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#531)

        Args:
            userIndex: uint256
        """
        ...

    def claimSeniorTrancheInterest(self, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#531)

        Args:
            userIndex: uint256
        """
        return self._execute(self.chain, request_type, "17f8e9f5", [userIndex], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def claimJuniorTrancheInterest(self, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#552)

        Args:
            userIndex: uint256
        """
        ...

    @overload
    def claimJuniorTrancheInterest(self, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#552)

        Args:
            userIndex: uint256
        """
        ...

    @overload
    def claimJuniorTrancheInterest(self, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#552)

        Args:
            userIndex: uint256
        """
        ...

    @overload
    def claimJuniorTrancheInterest(self, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#552)

        Args:
            userIndex: uint256
        """
        ...

    def claimJuniorTrancheInterest(self, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#552)

        Args:
            userIndex: uint256
        """
        return self._execute(self.chain, request_type, "ff560a9b", [userIndex], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def claimEquityTrancheInterest(self, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#573)

        Args:
            userIndex: uint256
        """
        ...

    @overload
    def claimEquityTrancheInterest(self, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#573)

        Args:
            userIndex: uint256
        """
        ...

    @overload
    def claimEquityTrancheInterest(self, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#573)

        Args:
            userIndex: uint256
        """
        ...

    @overload
    def claimEquityTrancheInterest(self, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#573)

        Args:
            userIndex: uint256
        """
        ...

    def claimEquityTrancheInterest(self, userIndex: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#573)

        Args:
            userIndex: uint256
        """
        return self._execute(self.chain, request_type, "854614c3", [userIndex], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def withdrawSeniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#594)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def withdrawSeniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#594)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def withdrawSeniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#594)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def withdrawSeniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#594)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    def withdrawSeniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#594)

        Args:
            userIndex: uint256
            amount: uint256
        """
        return self._execute(self.chain, request_type, "847f2261", [userIndex, amount], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def withdrawJuniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#633)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def withdrawJuniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#633)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def withdrawJuniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#633)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def withdrawJuniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#633)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    def withdrawJuniorTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#633)

        Args:
            userIndex: uint256
            amount: uint256
        """
        return self._execute(self.chain, request_type, "7575dcb1", [userIndex, amount], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def withdrawEquityTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#667)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def withdrawEquityTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#667)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def withdrawEquityTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#667)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    @overload
    def withdrawEquityTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#667)

        Args:
            userIndex: uint256
            amount: uint256
        """
        ...

    def withdrawEquityTranche(self, userIndex: uint256, amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#667)

        Args:
            userIndex: uint256
            amount: uint256
        """
        return self._execute(self.chain, request_type, "09335d54", [userIndex, amount], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalExpectedSeniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#703)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedSeniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#703)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedSeniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#703)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedSeniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#703)

        Returns:
            uint256
        """
        ...

    def totalExpectedSeniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#703)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "291a147e", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalExpectedJuniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#711)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedJuniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#711)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedJuniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#711)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedJuniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#711)

        Returns:
            uint256
        """
        ...

    def totalExpectedJuniorDeposits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#711)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "25cdcf05", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalExpectedSeniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#719)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedSeniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#719)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedSeniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#719)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedSeniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#719)

        Returns:
            uint256
        """
        ...

    def totalExpectedSeniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#719)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "41e8bc4d", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalExpectedJuniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#727)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedJuniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#727)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedJuniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#727)

        Returns:
            uint256
        """
        ...

    @overload
    def totalExpectedJuniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#727)

        Returns:
            uint256
        """
        ...

    def totalExpectedJuniorShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#727)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "47257831", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getSeniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#735)

        Returns:
            uint256
        """
        ...

    @overload
    def getSeniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#735)

        Returns:
            uint256
        """
        ...

    @overload
    def getSeniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#735)

        Returns:
            uint256
        """
        ...

    @overload
    def getSeniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#735)

        Returns:
            uint256
        """
        ...

    def getSeniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#735)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "eb78365c", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getJuniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#739)

        Returns:
            uint256
        """
        ...

    @overload
    def getJuniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#739)

        Returns:
            uint256
        """
        ...

    @overload
    def getJuniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#739)

        Returns:
            uint256
        """
        ...

    @overload
    def getJuniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#739)

        Returns:
            uint256
        """
        ...

    def getJuniorTrancheIdleValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#739)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "89b7d92d", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getSeniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#743)

        Returns:
            uint256
        """
        ...

    @overload
    def getSeniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#743)

        Returns:
            uint256
        """
        ...

    @overload
    def getSeniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#743)

        Returns:
            uint256
        """
        ...

    @overload
    def getSeniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#743)

        Returns:
            uint256
        """
        ...

    def getSeniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#743)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "707baf37", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getJuniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#747)

        Returns:
            uint256
        """
        ...

    @overload
    def getJuniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#747)

        Returns:
            uint256
        """
        ...

    @overload
    def getJuniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#747)

        Returns:
            uint256
        """
        ...

    @overload
    def getJuniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#747)

        Returns:
            uint256
        """
        ...

    def getJuniorTrancheTotalShares(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/fuzz/invariant/Handler.t.sol#747)

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
Handler.equityTrancheTotalShares.selector = bytes4(b'\xf60h>')
Handler.equityTrancheShares.selector = bytes4(b'\xf7\xed\xfa\x96')
Handler.equityTrancheDeposits.selector = bytes4(b'\x97\xbe\x04.')
Handler.equityUserIndex.selector = bytes4(b'\x81\xeb(\t')
Handler.loanBorrowers.selector = bytes4(b'jt\xc5H')
Handler.recevingEntity.selector = bytes4(b'\xbb\x85\xe7\x9c')
Handler.feeManager.selector = bytes4(b'\xd0\xfb\x02\x03')
Handler.totalIdleValue.selector = bytes4(b'\xfc[\x08@')
Handler.totalDeployedValue.selector = bytes4(b'-\x8dC]')
Handler.totalDeposited.selector = bytes4(b'\xffP\xab\xdc')
Handler.totalLoss.selector = bytes4(b'\rE~\xe1')
Handler.totalRecovered.selector = bytes4(b'\xca\x1ao\xbb')
Handler.totalUnclaimedInterest.selector = bytes4(b'\x9a.\xf2\xeb')
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
Handler.mayClosePool.selector = bytes4(b'\x96\x0b/\x9d')
Handler.claimSeniorTrancheInterest.selector = bytes4(b'\x17\xf8\xe9\xf5')
Handler.claimJuniorTrancheInterest.selector = bytes4(b'\xffV\n\x9b')
Handler.claimEquityTrancheInterest.selector = bytes4(b'\x85F\x14\xc3')
Handler.withdrawSeniorTranche.selector = bytes4(b'\x84\x7f"a')
Handler.withdrawJuniorTranche.selector = bytes4(b'uu\xdc\xb1')
Handler.withdrawEquityTranche.selector = bytes4(b'\t3]T')
Handler.totalExpectedSeniorDeposits.selector = bytes4(b')\x1a\x14~')
Handler.totalExpectedJuniorDeposits.selector = bytes4(b'%\xcd\xcf\x05')
Handler.totalExpectedSeniorShares.selector = bytes4(b'A\xe8\xbcM')
Handler.totalExpectedJuniorShares.selector = bytes4(b'G%x1')
Handler.getSeniorTrancheIdleValue.selector = bytes4(b'\xebx6\\')
Handler.getJuniorTrancheIdleValue.selector = bytes4(b'\x89\xb7\xd9-')
Handler.getSeniorTrancheTotalShares.selector = bytes4(b'p{\xaf7')
Handler.getJuniorTrancheTotalShares.selector = bytes4(b'\xe3\xe1\xde\x86')
