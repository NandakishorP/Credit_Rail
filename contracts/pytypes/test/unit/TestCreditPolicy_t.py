
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.forgestd.src.Test import Test



class TestCreditPolicy(Test):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#6)
    """
    _abi = {b'\x12\x10\xd3\xec\xd9r\xf2^\x1e"Qb~\xc8?\xb0\x0c\xb0\xe45\xdb\xe0\xc5\xab\xad\xf3*\x9eP\xee\x9f6': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'IndustryExcluded', 'type': 'event'}, b'\xb0g\xf0\x9a\x9e\x7f\xaf4e\xd2W \xc4\xdc\xa9\xd6I\xffX=\x8a\xc9\xa1b\xdc\x1a- Z\xe9\xb3\x8e': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'IndustryIncluded', 'type': 'event'}, b'\x9c\x88\x9e\xdd\xe3\xe1\x84\x91Z\xa8u\x8b\xed\xa1=\x0bT\x8d\xec\xc0\xb5\xa7\x9f;"\xff\xa3\xd9\xd5}\n\xb2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanTierUpdated', 'type': 'event'}, b'\x809\xca^z\xb2\x80\x89M\xd9\x80\xcer\xff\xf4g-\xe5\x8c\xbeB\x19\xce\xe5\xda`Y\xab\x85\xdb(\x91': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint8', 'name': 'maxTiers', 'type': 'uint8'}], 'name': 'MaxTiersChanged', 'type': 'event'}, b'H\x16U\x97Ped\xc2>8O\xdea\xcf\x1f!e\x91\xbc\xa2\xc8\xa1\xce\x0b\xbb!S\xd4\xc3\xd8\xeb\xc4': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'newAdmin', 'type': 'address'}], 'name': 'PolicyAdminChanged', 'type': 'event'}, b'\xdb\xb6\xd3\x14u\xbe\xc9\x84\x9f\xbf5*|5<\xdf\tmn-\x97,\xf7\x8b\xbadJ\x80&\x9d\xd3{': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyAttestationUpdated', 'type': 'event'}, b'|\x8ac\xa0\xb6\xc9\x98\x1e\x93\xea\xaf\x880{\x94\xe7\xa4\x8aYM\x03P\xa6\x05\xad\xf1\xcf\x9f\xcd\x8e\xc5S': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyConcentrationUpdated', 'type': 'event'}, b'\x968\xa3Q\x9a?\xc3\xe7\xd5\xc0\x10\x14\xe1\x07\x17\x1b#\x8d\x1b\xfe\xd1\xc6\xb8[G.\x18&\xa1\xcf\xc6\xd6': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyCovenantsUpdated', 'type': 'event'}, b'\r(\xab-\xec\x81\xaa\xeb\xf8i\x15\xa8e5:D\xc9w\x9f\xa1\xc6\x15\x8ao\xf7H\xdc\x8e\x14\x84(\x85': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyCreated', 'type': 'event'}, b"j\xc7\xbb6\x99\x0b\xe2\n\xfe\x8d'w\xe0:\x1c&\x84\xa4X\x9aQME\xa4\xd6\xf7~Sq\xaa\xfd\xa5": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'hash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'string', 'name': 'uri', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyDocumentSet', 'type': 'event'}, b'jP\xb7\x17K\x84DN\xe4\xfc\x85/0\xebMQ\x05\xa8^`\xb1+\x83\x12$\xdcV-\xaa\xbc=\xcd': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyEligibilityUpdated', 'type': 'event'}, b'\x15\xb1\x8a\xed\x16\xee\rwW\x87\xb6YO\xcfUj\xec!~>V\xf0\x81x\x10\x8d~\xcb\xd5\x99\\+': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyFrozen', 'type': 'event'}, b'&\xa7\xb1\xd1\x89/\x9b\x11ZUaz8\xa1\xbb\xf2\x16\xb6l\x17\x03\xee\x89\xce\xbc\\\x83r]\xa2\xf9$': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyRatiosUpdated', 'type': 'event'}, b'A0O\xac\xd92=u\xb1\x1b\xcd\xd6\t\xcb8\xef\xff\xfd\xb0W\x10\xf7\xca\xf0\xe9\xb1lm\x9dp\x9fP': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log', 'type': 'event'}, b'z\xe7LRt\x14\xae\x13_\xd9pG\xb1)!\xa5\xec9\x11\xb8\x04\x19xU\xd6~%\xc7\xb7^\xe6\xf3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'log_address', 'type': 'event'}, b'\xfb\x10(e\xd5\n\xdd\xdd\xf6\x9d\xa9\xb5\xaa\x1b\xce\xd6l\x80\xcf\x86\x9a\\\x8d\x04q\xa4g\xe1\x8c\xe9\xca\xb1': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_array', 'type': 'event'}, b'\x89\n\x82g\x9bG\x0f+\xd8(\x16\xed\x9b\x16\x1f\x97\xd8\xb9g\xf3\x7f\xa3d|!\xd5\xbf9t\x9e-\xd5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_array', 'type': 'event'}, b'@\xe1\x84\x0fWi\x07=a\xbd\x017-\x9bu\xba\xa9\x84-V)\xa0\xc9\x9f\xf1\x03\xbe\x11x\xa8\xe9\xe2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_array', 'type': 'event'}, b'#\xb6*\xd0XM$\xa7_\x0b\xf3V\x03\x91\xefVY\xecm\xb1&\x9cV\xe1\x1a\xa2A\xd67\xf1\x9b ': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'log_bytes', 'type': 'event'}, b'\xe8\x16\x99\xb8Q\x13\xee\xa1\xc7>\x10X\x8b+\x03^U\x893ic!s\xaf\xd4?\xeb\x19/\xacd\xe3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'log_bytes32', 'type': 'event'}, b'\x0e\xb5\xd5&$\xc8\xd2\x8a\xda\x9f\xc5Z\x8cP.\xd5\xaa?\xbe/\xb6\xe9\x1bq\xb5\xf3v\x88+\x1d/\xb8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256', 'name': '', 'type': 'int256'}], 'name': 'log_int', 'type': 'event'}, b'\x9cN\x85A\xca\x8f\r\xc1\xc4\x13\xf9\x10\x8ff\xd8-<\xec\xb1\xbd\xdb\xceCza\xca\xa3\x17\\L\xc9o': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address', 'name': 'val', 'type': 'address'}], 'name': 'log_named_address', 'type': 'event'}, b'\x00\xaa\xa3\x9c\x9f\xfb_VzE48\x0cspup.\x1f\x7f\x14\x10\x7f\xc9S(\xe3\xb5l\x03%\xfb': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xa7>\xda\tf/F\xdd\xe7)\xbeF\x118_\xf3O\xe6\xc4O\xbb\xc6\xf7\xe1{\x04+Y\xa3D[W': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_named_array', 'type': 'event'}, b";\xcf\xb2\xae.\x8d\x13-\xd1\xfc\xe7\xcf'\x8a\x9a\x19uj\x9f\xce\xab\xe4p\xdf;\xda\xbbK\xc5w\xd1\xbd": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xd2n\x16\xca\xd4T\x87\x05\xe4\xc9\xe2\xd9O\x98\xee\x91\xc2\x89\x08^\xe4%YO\xd5c_\xa2\x96L\xcf\x18': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'val', 'type': 'bytes'}], 'name': 'log_named_bytes', 'type': 'event'}, b'\xaf\xb7\x95\xc9\xc6\x1eO\xe7F\x8c8o\x92]zT)\xec\xad\x9c\x04\x95\xdd\xb8\xd3\x8di\x06\x14\xd3/\x99': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'val', 'type': 'bytes32'}], 'name': 'log_named_bytes32', 'type': 'event'}, b']\xa6\xce\x9dQ\x15\x1b\xa1\x0c\t\xa5Y\xef$\xd5 \xb9\xda\xc5\xc5\xb8\x81\n\xe8CNM\r\x86A\x1a\x95': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_int', 'type': 'event'}, b"\xeb\x8b\xa4<\xedu7B\x19F\xbdC\xe8(\xb8\xb2\xb8B\x89'\xaa\x8f\x80\x1c\x13\xd94\xbf\x11\xac\xa5{": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_uint', 'type': 'event'}, b'/\xe62w\x91t7CxD*\x8e\x97\x8b\xcc\xfb\xdc\xc1\xd6\xb2\xb0\xd8\x1f~\x8e\xb7v\xab"\x86\xf1h': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}], 'name': 'log_named_int', 'type': 'event'}, b'(\x0fDF\xb2\x8a\x13rA}\xdae\x8d0\xb9[)\x92\xb1*\xc9\xc7\xf3xS_)\xa9z\xcf5\x83': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'val', 'type': 'string'}], 'name': 'log_named_string', 'type': 'event'}, b'\xb2\xde/\xbe\x80\x1a\r\xf6\xc0\xcb\xdd\xfdD\x8b\xa3\xc4\x1dH\xa0@\xca5\xc5l\x81\x96\xef\x0f\xca\xe7!\xa8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}], 'name': 'log_named_uint', 'type': 'event'}, b'\x0b.\x13\xff \xac{GA\x98eU\x83\xed\xf7\r\xed\xd2\xc1\xdc\x98\x0e2\x9cO\xbb/\xc0t\x8byk': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log_string', 'type': 'event'}, b',\xab\x97\x90Q\x0f\xd8\xbd\xfb\xd2\x11R\x88\xdb3\xfe\xc6f\x91\xd4v\xef\xc5B|\xfdL\ti0\x17U': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'log_uint', 'type': 'event'}, b"\xe7\x95\x0e\xde\x03\x94\xb9\xf2\xceJZ\x1b\xf5\xa7\xe1\x85$\x11\xf7\xe6f\x1bC\x08\xc9\x13\xc4\xbf\xd1\x10'\xe4": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'logs', 'type': 'event'}, b'\xfav&\xd4': {'inputs': [], 'name': 'IS_TEST', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb5P\x8a\xa9': {'inputs': [], 'name': 'excludeArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'excludedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe2\x0c\x9fq': {'inputs': [], 'name': 'excludeContracts', 'outputs': [{'internalType': 'address[]', 'name': 'excludedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb0FO\xdc': {'inputs': [], 'name': 'excludeSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'excludedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1e\xd7\x83\x1c': {'inputs': [], 'name': 'excludeSenders', 'outputs': [{'internalType': 'address[]', 'name': 'excludedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbaAO\xa6': {'inputs': [], 'name': 'failed', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\n\x92T\xe4': {'inputs': [], 'name': 'setUp', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'f\xd9\xa9\xa0': {'inputs': [], 'name': 'targetArtifactSelectors', 'outputs': [{'components': [{'internalType': 'string', 'name': 'artifact', 'type': 'string'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzArtifactSelector[]', 'name': 'targetedArtifactSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x85"l\x81': {'inputs': [], 'name': 'targetArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'targetedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'?r\x86\xf4': {'inputs': [], 'name': 'targetContracts', 'outputs': [{'internalType': 'address[]', 'name': 'targetedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'*\xde8\x80': {'inputs': [], 'name': 'targetInterfaces', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'string[]', 'name': 'artifacts', 'type': 'string[]'}], 'internalType': 'struct StdInvariant.FuzzInterface[]', 'name': 'targetedInterfaces_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x91j\x17\xc6': {'inputs': [], 'name': 'targetSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'targetedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'>^<#': {'inputs': [], 'name': 'targetSenders', 'outputs': [{'internalType': 'address[]', 'name': 'targetedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x01\x87\xfa\xf2': {'inputs': [], 'name': 'testAdminRevertIfNewAdminIsZeroAddress', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'c\xfc\x93\xa4': {'inputs': [], 'name': 'testCannotFreezeDeactivatedPolicy', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'/\xe6\x86\x03': {'inputs': [], 'name': 'testChaingePolicyAdminRevertsIfNotAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf2\xd6\xc9h': {'inputs': [], 'name': 'testChangePolicyAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf5\x0cA\x1e': {'inputs': [], 'name': 'testChangePolicyAdminEmitsEvent', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xaf\x99!?': {'inputs': [], 'name': 'testCompletePolicyLifecycle', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'`Y\x9a\x8c': {'inputs': [], 'name': 'testCreatePolicy', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xdai\xac\xa6': {'inputs': [], 'name': 'testCreatePolicyRevertIfOwnerIsNotAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf5\x97\x08C': {'inputs': [], 'name': 'testCreatePolicyRevertsIfVersionExists', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xac\xc45\xdb': {'inputs': [], 'name': 'testCreatePolicyRevertsIfVersionIsZero', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'E\xdd\xfa\xd4': {'inputs': [], 'name': 'testDeactivatePolicy', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b"'V\xbf\xb1": {'inputs': [], 'name': 'testDeactivatePolicyIsIdempotent', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd3\x06\xfe\xec': {'inputs': [], 'name': 'testDeactivatePolicyRevertIfOwnerIsNotAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'rkQ\xf3': {'inputs': [], 'name': 'testDeactivatePolicyRevertsIfPolicyDontExist', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'q\xcb\x19\xdb': {'inputs': [], 'name': 'testDeactivateUpdatesLastUpdated', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'dY\xb9\xcf': {'inputs': [], 'name': 'testEligibilityWithZeroValues', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x196\x92\xe9': {'inputs': [], 'name': 'testExcludeIndustryIsIdempotent', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf6\x86\x0cN': {'inputs': [], 'name': 'testExcludeIndustryRevertsIfDataIsZeroHash', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'<\xa2\x92\x8d': {'inputs': [], 'name': 'testExcludeIndustryRevertsIfNotAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf1\x07x\xb6': {'inputs': [], 'name': 'testExcludeIndustryRevertsIfPolicyDontExist', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x94{\xf4\xaf': {'inputs': [], 'name': 'testExcludeIndustryRevertsIfPolicyIsFrozen', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xbe\xe8\x1cP': {'inputs': [], 'name': 'testExcludeIndustryUnitTest', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfb\x95\x14\x8c': {'inputs': [], 'name': 'testFreezeDoesNotDeactivatePolicy', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'kgf\x8c': {'inputs': [], 'name': 'testFreezePolicyMarksPolicyAsFrozen', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x9b\x8f\xa0y': {'inputs': [], 'name': 'testFreezePolicyReverstIfPolicyIsNotActive', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfe[\xc5\xab': {'inputs': [], 'name': 'testFreezePolicyRevertIfOwnerIsNotAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x12\xeaX\\': {'inputs': [], 'name': 'testFreezePolicyRevertsIfAlreadyFrozen', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x8f\x16*\xf2': {'inputs': [], 'name': 'testFreezePolicyRevertsIfNoAttestationSet', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xe3!3f': {'inputs': [], 'name': 'testFreezePolicyRevertsIfNoConcentrationSet', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x99+.\x0e': {'inputs': [], 'name': 'testFreezePolicyRevertsIfNoCovenantsSet', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xe9z\x18z': {'inputs': [], 'name': 'testFreezePolicyRevertsIfNoDocumentHashSet', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'g\xd6\xe1\x02': {'inputs': [], 'name': 'testFreezePolicyRevertsIfNoEligibilitySet', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'0L8\xff': {'inputs': [], 'name': 'testFreezePolicyRevertsIfNoLoanTiersSet', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'"\xba\xdc;': {'inputs': [], 'name': 'testFreezePolicyRevertsIfNoRatiosSet', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xc0/k\xad': {'inputs': [], 'name': 'testFreezePolicyRevertsIfPolicyDontExist', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'?\xaf\xa9\xf1': {'inputs': [], 'name': 'testFreezePolicyUnitTest', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\nzi\xb8': {'inputs': [], 'name': 'testFreezeUpdatesLastUpdated', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'8\xe9t\xa4': {'inputs': [], 'name': 'testFrozenPolicyIsFullyImmutable', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfc\xdaW\xaa': {'inputs': [], 'name': 'testIncludeIndustryRevertsIfDataIsZeroHash', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfb\x925_': {'inputs': [], 'name': 'testIncludeIndustryRevertsIfNotAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd0[\\\x9f': {'inputs': [], 'name': 'testIncludeIndustryRevertsIfPolicyDontExist', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x15\xd1\xf7>': {'inputs': [], 'name': 'testIncludeIndustryRevertsIfPolicyIsFrozen', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'C\xb0\x0f(': {'inputs': [], 'name': 'testIncludeIndustryUnitTest', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x87\x01\x84y': {'inputs': [], 'name': 'testIncludeNeverExcludedIndustry', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd7\xe0\r\xb3': {'inputs': [], 'name': 'testIndustryExclusionState', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb7\xe7\x9c\xb3': {'inputs': [], 'name': 'testIsPolicyActiveGetter', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'F\xff\xcbT': {'inputs': [], 'name': 'testIsPolicyFrozenGetter', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'~f\xe8\xf0': {'inputs': [], 'name': 'testLastUpdatedAlwaysMovesForward', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xdfpq\x1d': {'inputs': [], 'name': 'testLastUpdatedTimestamp', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'|_\x87\x80': {'inputs': [], 'name': 'testLoanTierWithEmptyName', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x9a3\x1c\xd1': {'inputs': [], 'name': 'testMultipleEligibilityUpdates', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'(\x8eS\xa6': {'inputs': [], 'name': 'testMultipleIndustryExclusions', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x97\\\x81\xfc': {'inputs': [], 'name': 'testMultiplePolicyVersions', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xaf\xdfK\xca': {'inputs': [], 'name': 'testMultipleTierManagement', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xc0\x01\xfe\xa2': {'inputs': [], 'name': 'testNewAdminCanCreatePolicy', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfc\x8ag\xa2': {'inputs': [], 'name': 'testNewAdminCanManageExistingPolicy', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf4M>\xe3': {'inputs': [], 'name': 'testOldAdminLosesAccessAfterAdminChange', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xbe89\xcc': {'inputs': [], 'name': 'testOverwriteExistingTier', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b']\xb3\xff\xd0': {'inputs': [], 'name': 'testPolicyVersionIsolation', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'g5\x13_': {'inputs': [], 'name': 'testPolicyWithLargeVersionNumber', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Q\x0b\xf4p': {'inputs': [], 'name': 'testSetLoanTier', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'=\xb0\xe7\xc5': {'inputs': [], 'name': 'testSetLoanTierIncrementsTotalTiers', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf3bDQ': {'inputs': [], 'name': 'testSetLoanTierRevertsIfNotAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb8\xbf\xd2\x99': {'inputs': [], 'name': 'testSetLoanTierRevertsIfPolicyDontExist', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf3Y\xec\x85': {'inputs': [], 'name': 'testSetLoanTierRevertsIfPolicyIsFrozen', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'n{\xdbH': {'inputs': [], 'name': 'testSetLoanTierStoresDataCorrectly', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xafE\x9b\xeb': {'inputs': [], 'name': 'testSetLoanTierWithMaxUint8RevertBecauseOfMaxTierLimit', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Y\xf1V"': {'inputs': [], 'name': 'testSetMaxTiersRevertIfItsMoreThan255', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x9c\x92\x87\xd5': {'inputs': [], 'name': 'testSetMaxTiersRevertsIfNotAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb5*\xff]': {'inputs': [], 'name': 'testSetMaxTiersUnitTest', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'+\x84\x9cG': {'inputs': [], 'name': 'testSetPolicyDocumentRevertsIfNotAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'`<\xa1\xd3': {'inputs': [], 'name': 'testSetPolicyDocumentRevertsIfPolicyDontExist', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa4\x89\xd7\x10': {'inputs': [], 'name': 'testSetPolicyDocumentRevertsIfPolicyIsFrozen', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'q3\x03H': {'inputs': [], 'name': 'testSetPolicyDocumentStoresCorrectly', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xe6\xbb\x1d\xee': {'inputs': [], 'name': 'testSetPolicyDocumentUnitTest', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xbc\xe5\xbd\xac': {'inputs': [], 'name': 'testSetPolicyDocumentWithEmptyURI', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'BWIN': {'inputs': [], 'name': 'testTierExistsGetter', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\\\x13*Y': {'inputs': [], 'name': 'testTotalTiersDoesNotDecrease', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'_:\xd5\xbc': {'inputs': [], 'name': 'testUnAuthorizedUpdateAttestationRequirements', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xc2N\xd2l': {'inputs': [], 'name': 'testUnAuthorizedUpdateConcentrationLimits', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xe4\xc2b\x07': {'inputs': [], 'name': 'testUnAuthorizedUpdateCovenants', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\\\x9bEb': {'inputs': [], 'name': 'testUnAuthorizedUpdateEligibility', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa9\\`I': {'inputs': [], 'name': 'testUnAuthorizedUpdateFinancialRatios', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xde\xd4\x1a\x92': {'inputs': [], 'name': 'testUpdateAttestationRequirments', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Ym(\xd8': {'inputs': [], 'name': 'testUpdateAttestationRequirmentsRevertIfPolicyDontExist', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xba%\x1f\xb1': {'inputs': [], 'name': 'testUpdateAttestationRequirmentsRevertsIfPolicyIsFrozen', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xe0G\x9f{': {'inputs': [], 'name': 'testUpdateAttestationStoresDataCorrectly', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x10\x01\x15\xef': {'inputs': [], 'name': 'testUpdateConcentrationLimits', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x86>\x08\xcf': {'inputs': [], 'name': 'testUpdateConcentrationLimitsRevertIfPolicyDontExist', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xbd\xf9\xcc9': {'inputs': [], 'name': 'testUpdateConcentrationLimitsRevertsIfPolicyIsFrozen', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'^\xa7\x86\xde': {'inputs': [], 'name': 'testUpdateConcentrationStoresDataCorrectly', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd6\x12@Z': {'inputs': [], 'name': 'testUpdateCovenants', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'cA\x1f\x83': {'inputs': [], 'name': 'testUpdateCovenantsRevertIfPolicyDontExist', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd6i\xa9-': {'inputs': [], 'name': 'testUpdateCovenantsRevertsIfPolicyIsFrozen', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa0\xb4\xd1\x87': {'inputs': [], 'name': 'testUpdateCovenantsStoresDataCorrectly', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'w`4\x88': {'inputs': [], 'name': 'testUpdateEligibility', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xcb\x99u\x00': {'inputs': [], 'name': 'testUpdateEligibilityRevertsIfPolicyDontExist', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xc9\xbb\xa5\xe0': {'inputs': [], 'name': 'testUpdateEligibilityRevertsIfPolicyIsFrozen', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb5\x7f\xc0U': {'inputs': [], 'name': 'testUpdateEligibilityStoresDataCorrectly', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd9Z,\xb1': {'inputs': [], 'name': 'testUpdateFinancialRatios', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x8a6K\x02': {'inputs': [], 'name': 'testUpdateFinancialRatiosRevertIfPolicyDontExist', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xc6\xd7\xf0\x9e': {'inputs': [], 'name': 'testUpdateFinancialRatiosRevertsIfPolicyIsFrozen', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'7\xc7w\xbe': {'inputs': [], 'name': 'testUpdatePolicyDocumentMultipleTimes', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x0e\xe8z\xb9': {'inputs': [], 'name': 'testUpdateRatiosStoresDataCorrectly', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xe2\x88\xed9': {'inputs': [], 'name': 'testUpdateRevertsIfPolicyInactive', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":46,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"stdstore","offset":0,"slot":0,"type":"t_struct(StdStorage)8331_storage"},{"astId":209,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"_failed","offset":0,"slot":8,"type":"t_bool"},{"astId":2943,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"stdChainsInitialized","offset":1,"slot":8,"type":"t_bool"},{"astId":2964,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"chains","offset":0,"slot":9,"type":"t_mapping(t_string_memory_ptr,t_struct(Chain)2959_storage)"},{"astId":2968,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"defaultRpcUrls","offset":0,"slot":10,"type":"t_mapping(t_string_memory_ptr,t_string_storage)"},{"astId":2972,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"idToAlias","offset":0,"slot":11,"type":"t_mapping(t_uint256,t_string_storage)"},{"astId":2975,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"fallbackToDefaultRpcUrls","offset":0,"slot":12,"type":"t_bool"},{"astId":3931,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"gasMeteringOff","offset":1,"slot":12,"type":"t_bool"},{"astId":6002,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"stdstore","offset":0,"slot":13,"type":"t_struct(StdStorage)8331_storage"},{"astId":6923,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"_excludedContracts","offset":0,"slot":21,"type":"t_array(t_address)dyn_storage"},{"astId":6926,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"_excludedSenders","offset":0,"slot":22,"type":"t_array(t_address)dyn_storage"},{"astId":6929,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"_targetedContracts","offset":0,"slot":23,"type":"t_array(t_address)dyn_storage"},{"astId":6932,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"_targetedSenders","offset":0,"slot":24,"type":"t_array(t_address)dyn_storage"},{"astId":6935,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"_excludedArtifacts","offset":0,"slot":25,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6938,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"_targetedArtifacts","offset":0,"slot":26,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6942,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"_targetedArtifactSelectors","offset":0,"slot":27,"type":"t_array(t_struct(FuzzArtifactSelector)6914_storage)dyn_storage"},{"astId":6946,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"_excludedSelectors","offset":0,"slot":28,"type":"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage"},{"astId":6950,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"_targetedSelectors","offset":0,"slot":29,"type":"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage"},{"astId":6954,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"_targetedInterfaces","offset":0,"slot":30,"type":"t_array(t_struct(FuzzInterface)6920_storage)dyn_storage"},{"astId":13223,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"IS_TEST","offset":0,"slot":31,"type":"t_bool"},{"astId":41052,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"deployer","offset":1,"slot":31,"type":"t_address"},{"astId":41057,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"seniorUser1","offset":0,"slot":32,"type":"t_address"},{"astId":41062,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"seniorUser2","offset":0,"slot":33,"type":"t_address"},{"astId":41065,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"creditPolicy","offset":0,"slot":34,"type":"t_contract(CreditPolicy)40909"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_address)dyn_storage":{"encoding":"dynamic_array","label":"address[]","numberOfBytes":32,"base":"t_address"},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_array(t_bytes4)dyn_storage":{"encoding":"dynamic_array","label":"bytes4[]","numberOfBytes":32,"base":"t_bytes4"},"t_array(t_string_storage)dyn_storage":{"encoding":"dynamic_array","label":"string[]","numberOfBytes":32,"base":"t_string_storage"},"t_array(t_struct(FuzzArtifactSelector)6914_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzArtifactSelector[]","numberOfBytes":32,"base":"t_struct(FuzzArtifactSelector)6914_storage"},"t_array(t_struct(FuzzInterface)6920_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzInterface[]","numberOfBytes":32,"base":"t_struct(FuzzInterface)6920_storage"},"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzSelector[]","numberOfBytes":32,"base":"t_struct(FuzzSelector)6908_storage"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_contract(CreditPolicy)40909":{"encoding":"inplace","label":"contract CreditPolicy","numberOfBytes":20},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))"},"t_mapping(t_bytes32,t_struct(FindData)8306_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)8306_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)8306_storage)"},"t_mapping(t_string_memory_ptr,t_string_storage)":{"encoding":"mapping","label":"mapping(string => string)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_string_storage"},"t_mapping(t_string_memory_ptr,t_struct(Chain)2959_storage)":{"encoding":"mapping","label":"mapping(string => struct StdChains.Chain)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_struct(Chain)2959_storage"},"t_mapping(t_uint256,t_string_storage)":{"encoding":"mapping","label":"mapping(uint256 => string)","numberOfBytes":32,"key":"t_uint256","value":"t_string_storage"},"t_string_memory_ptr":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(Chain)2959_storage":{"encoding":"inplace","label":"struct StdChains.Chain","numberOfBytes":128,"members":[{"astId":2952,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"name","offset":0,"slot":0,"type":"t_string_storage"},{"astId":2954,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"chainId","offset":0,"slot":1,"type":"t_uint256"},{"astId":2956,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"chainAlias","offset":0,"slot":2,"type":"t_string_storage"},{"astId":2958,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"rpcUrl","offset":0,"slot":3,"type":"t_string_storage"}]},"t_struct(FindData)8306_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":8299,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":8301,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":8303,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":8305,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(FuzzArtifactSelector)6914_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzArtifactSelector","numberOfBytes":64,"members":[{"astId":6910,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"artifact","offset":0,"slot":0,"type":"t_string_storage"},{"astId":6913,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(FuzzInterface)6920_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzInterface","numberOfBytes":64,"members":[{"astId":6916,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6919,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"artifacts","offset":0,"slot":1,"type":"t_array(t_string_storage)dyn_storage"}]},"t_struct(FuzzSelector)6908_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzSelector","numberOfBytes":64,"members":[{"astId":6904,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6907,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(StdStorage)8331_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":8315,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))"},{"astId":8318,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":8320,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":8322,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":8324,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":8326,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":8328,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":8330,"contract":"test/unit/TestCreditPolicy.t.sol:TestCreditPolicy","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60806040523461048f575f600160ff19600c541617600c55600160ff19601f541617601f556040516100326040826104d7565b6008815260208101673232b83637bcb2b960c11b8152604051602081019061007260208286518087875e81015f838201520301601f1981018352826104d7565b519020916040519263ffa1864960e01b845260048401526020836024815f51602062010f875f395f51905f525afa928315610484575f93610493575b505f51602062010f875f395f51905f523b1561048f575f906064604051809481936318caf8e360e31b835260018060a01b0388166004840152604060248401525180918160448501528484015e8181018301859052601f01601f19168101030181835f51602062010f875f395f51905f525af180156104845761046f575b50601f8054610100600160a81b03191660089290921b610100600160a81b0316919091179055604080519061016190826104d7565b600b815281602082016a73656e696f72557365723160a81b815260405160208101906101a560208287518087875e810187838201520301601f1981018352826104d7565b5190206040519063ffa1864960e01b825260048201526020816024815f51602062010f875f395f51905f525afa90811561040957839161042d575b505f51602062010f875f395f51905f523b156103c35782906064604051809481936318caf8e360e31b835260018060a01b031697886004840152604060248401525180918160448501528484015e8181018301859052601f01601f19168101030181835f51602062010f875f395f51905f525af180156103b857610414575b505060018060a01b03196020541617602055604051906102806040836104d7565b600b8252602082016a39b2b734b7b92ab9b2b91960a91b815260405160208101906102c360208287518087875e810187838201520301601f1981018352826104d7565b5190206040519063ffa1864960e01b825260048201526020816024815f51602062010f875f395f51905f525afa9081156104095783916103c7575b505f51602062010f875f395f51905f523b156103c35782906064604051809481936318caf8e360e31b835260018060a01b031697886004840152604060248401525180918160448501528484015e8181018301859052601f01601f19168101030181835f51602062010f875f395f51905f525af180156103b8576103a0575b602180546001600160a01b0319168417905560405162010a7890816200050f8239f35b6103ab8280926104d7565b6103b5578061037d565b80fd5b6040513d84823e3d90fd5b8280fd5b90506020813d602011610401575b816103e2602093836104d7565b810103126103c357516001600160a01b03811681036103c3575f6102fe565b3d91506103d5565b6040513d85823e3d90fd5b8161041e916104d7565b61042957815f61025f565b5080fd5b90506020813d602011610467575b81610448602093836104d7565b810103126103c357516001600160a01b03811681036103c3575f6101e0565b3d915061043b565b61047c9192505f906104d7565b5f905f61012c565b6040513d5f823e3d90fd5b5f80fd5b9092506020813d6020116104cf575b816104af602093836104d7565b8101031261048f57516001600160a01b038116810361048f57915f6100ae565b3d91506104a2565b601f909101601f19168101906001600160401b038211908210176104fa57604052565b634e487b7160e01b5f52604160045260245ffdfe6080806040526004361015610012575f80fd5b5f905f3560e01c9081630187faf21461d6c8575080630a7a69b81461d11f5780630a9254e41461cfbd5780630ee87ab91461cd50578063100115ef1461cc1657806312ea585c1461cb6657806315d1f73e1461ca47578063193692e91461c7fa5780631ed7831c1461c77c57806322badc3b1461c6b15780632756bfb11461c37b578063288e53a61461c0ad5780632ade38801461bef65780632b849c471461be075780632fe686031461bcd8578063304c38ff1461ba6f57806337c777be1461b76d57806338e974a41461b03a5780633ca2928d1461af4b5780633db0e7c51461ab725780633e5e3c231461aaf45780633f7286f41461aa765780633fafa9f11461a5605780634257494e1461a38c57806343b00f281461a14b57806345ddfad414619fab57806346ffcb5414619e0b578063510bf47014619cc6578063596d28d814619bdc57806359f1562214619a845780635c132a59146198355780635c9b4562146197465780635db3ffd0146194695780635ea786de146192245780635f3ad5bc14619135578063603ca1d31461904b57806360599a8c14618d2c57806363411f8314618c4257806363fc93a4146188515780636459b9cf146186b757806366d9a9a0146185965780636735135f1461847b57806367d6e102146183215780636b67668c14617e735780636e7bdb4814617c8957806371330348146179f157806371cb19db1461778a578063726b51f314617675578063776034881461753b5780637c5f8780146173ae5780637e66e8f01461716b57806385226c81146170e1578063863e08cf14616ff75780638701847914616eaa5780638a364b0214616dc05780638f162af214616c00578063916a17c614616b58578063947bf4af14616a39578063975c81fc146166f6578063992b2e0e146164f35780639a331cd1146160d55780639b8fa07914615ec95780639c9287d514615d99578063a0b4d18714615bcb578063a489d71014615a96578063a95c6049146159a7578063acc435db1461587d578063af459beb146156e3578063af99213f14614fbc578063afdf4bca14614bef578063b0464fdc14614b47578063b52aff5d14614917578063b5508aa91461488d578063b57fc05514614601578063b7e79cb314614425578063b8bfd29914614338578063ba251fb114614203578063ba414fa6146141de578063bce5bdac14614047578063bdf9cc3914613f28578063be3839cc14613c17578063bee81c5014613ac7578063c001fea214613866578063c02f6bad14613751578063c24ed26c14613608578063c6d7f09e146134d3578063c9bba5e014613439578063cb9975001461334f578063d05b5c9f14613265578063d306feec14613135578063d612405a14612ffb578063d669a92d14612edc578063d7e00db314612b59578063d95a2cb1146129f2578063da69aca6146128e0578063ded41a9214612779578063df70711d1461250e578063e0479f7b1461236f578063e20c9f71146122e1578063e288ed3914612100578063e321336614611e0b578063e4c2620714611cd9578063e6bb1dee14611b33578063e97a187a146116f5578063f10778b6146115b4578063f2d6c9681461145e578063f359ec851461133c578063f3624451146111ed578063f44d3ee314610ff9578063f50c411e14610e8c578063f597084314610d2c578063f6860c4e14610bf3578063fa7626d414610bd0578063fb92355f14610a8a578063fb95148c14610960578063fc8a67a2146107ba578063fcda57aa146106815763fe5bc5ab14610530575f80fd5b3461064657806003193601126106465761054861e2e4565b60205481906001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761066c575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b815263793e95df60e01b600482015281908181602481835f51602062010a235f395f51905f525af1801561064957610657575b506022546001600160a01b0316803b156106545781809160246040518094819363fb4dcb8b60e01b8352600160048401525af18015610649576106355750f35b8161063f9161da4e565b6106465780f35b80fd5b6040513d84823e3d90fd5b50fd5b816106619161da4e565b61064657805f6105f5565b816106769161da4e565b61064657805f6105a0565b503461064657806003193601126106465761069a61e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576107a5575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b815263036d8cb960e61b600482015281908181602481835f51602062010a235f395f51905f525af1801561064957610790575b506022546001600160a01b0316803b156106545781809160446040518094819363030d4a7760e21b8352600160048401528160248401525af18015610649576106355750f35b8161079a9161da4e565b61064657805f61074a565b816107af9161da4e565b61064657805f6106f5565b50346106465780600319360112610646576107d361e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761094b575b506022546020546001600160a01b039182169116813b1561091d57829160248392604051948593849263f770713b60e01b845260048401525af1801561064957610936575b506020546001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957610921575b506022546001600160a01b03166108df61e3a7565b90803b1561091d576040516377e4d4ad60e01b8152918391839182908490829061090c906004830161da6f565b03925af18015610649576106355750f35b5050fd5b8161092b9161da4e565b61064657805f6108ca565b816109409161da4e565b61064657805f610873565b816109559161da4e565b61064657805f61082e565b503461064657806003193601126106465761097961e9b3565b602254604051634a096d2b60e01b8152600160048201526001600160a01b0390911690602081602481855afa908115610a7f578391610a36575b506024916109c260209261eeff565b604051635037f17b60e01b81526001600482015292839182905afa80156106495782906109f7575b6109f4915061eeff565b80f35b506020813d602011610a2e575b81610a116020938361da4e565b81010312610a2a57610a256109f49161dc9b565b6109ea565b5080fd5b3d9150610a04565b90506020813d602011610a77575b81610a516020938361da4e565b81010312610a73576024916109c2610a6a60209361dc9b565b925050916109b3565b8280fd5b3d9150610a44565b6040513d85823e3d90fd5b5034610646578060031936011261064657610aa361e2e4565b60205481906001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957610bbb575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b815263793e95df60e01b600482015281908181602481835f51602062010a235f395f51905f525af1801561064957610ba6575b506022546001600160a01b0316610b6561dc4e565b60208151910120813b1561091d57829160448392604051948593849263030d4a7760e21b84526001600485015260248401525af18015610649576106355750f35b81610bb09161da4e565b61064657805f610b50565b81610bc59161da4e565b61064657805f610afb565b5034610646578060031936011261064657602060ff601f54166040519015158152f35b5034610646578060031936011261064657610c0c61e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957610d17575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b815263036d8cb960e61b600482015281908181602481835f51602062010a235f395f51905f525af1801561064957610d02575b506022546001600160a01b0316803b156106545781809160446040518094819363267d3d7b60e11b8352600160048401528160248401525af18015610649576106355750f35b81610d0c9161da4e565b61064657805f610cbc565b81610d219161da4e565b61064657805f610c67565b5034610646578060031936011261064657610d4561e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957610e77575b506040516362e01ad560e11b60208201526001602482015260248152610dc760448261da4e565b5f51602062010a235f395f51905f523b156106545781610e03916040518093819263f28dceb360e01b835260206004840152602483019061d860565b0381835f51602062010a235f395f51905f525af1801561064957610e62575b506022546001600160a01b0316803b15610654578180916024604051809481936304bd12bb60e01b8352600160048401525af18015610649576106355750f35b81610e6c9161da4e565b61064657805f610e22565b81610e819161da4e565b61064657805f610da0565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957610fe4575b50505f51602062010a235f395f51905f523b15610646578060405163248e63e160e11b815260016004820152600160248201528160448201528160648201528181608481835f51602062010a235f395f51905f525af1801561064957610fcf575b5060018060a01b03602054167f48165597506564c23e384fde61cf1f216591bca2c8a1ce0bbb2153d4c3d8ebc46020604051838152a16022546001600160a01b031690813b1561091d57829160248392604051948593849263f770713b60e01b845260048401525af18015610649576106355750f35b81610fd99161da4e565b61064657805f610f59565b81610fee9161da4e565b61064657805f610ef8565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576111d8575b506022546020546001600160a01b039182169116813b1561091d57829160248392604051948593849263f770713b60e01b845260048401525af18015610649576111c3575b50601f5460081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576111ae575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b815263793e95df60e01b600482015281908181602481835f51602062010a235f395f51905f525af1801561064957611199575b506022546001600160a01b0316803b15610654578180916024604051809481936304bd12bb60e01b8352606360048401525af18015610649576106355750f35b816111a39161da4e565b61064657805f611159565b816111b89161da4e565b61064657805f611104565b816111cd9161da4e565b61064657805f6110aa565b816111e29161da4e565b61064657805f611065565b503461064657806003193601126106465761120661e2e4565b60205481906001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957611327575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b815263793e95df60e01b600482015281908181602481835f51602062010a235f395f51905f525af1801561064957611312575b506022546001600160a01b03166112d06112cb61dca8565b61e53b565b90803b1561091d5761090c8392918392604051948580948193632dc3f61760e11b8352600160048401526001602484015260606044840152606483019061db6f565b8161131c9161da4e565b61064657805f6112b3565b816113319161da4e565b61064657805f61125e565b503461064657806003193601126106465761135561e9b3565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957611449575b50604051630a1f679b60e01b602082015260016024820152602481526113d760448261da4e565b5f51602062010a235f395f51905f523b156106545781611413916040518093819263f28dceb360e01b835260206004840152602483019061d860565b0381835f51602062010a235f395f51905f525af180156106495761131257506022546001600160a01b03166112d06112cb61dca8565b816114539161da4e565b61064657805f6113b0565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761159f575b506022546020546001600160a01b039182169116813b1561091d57829160248392604051948593849263f770713b60e01b845260048401525af180156106495761158a575b5050602254604051632c728c4b60e11b815290602090829060049082906001600160a01b03165afa8015610649576109f491839161155b575b506020546001600160a01b03169061f1ce565b61157d915060203d602011611583575b611575818361da4e565b81019061e2c5565b5f611548565b503d61156b565b816115949161da4e565b61064657805f61150f565b816115a99161da4e565b61064657805f6114ca565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576116e0575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b81526362f4a20760e01b600482015281908181602481835f51602062010a235f395f51905f525af18015610649576116cb575b506022546001600160a01b031661168a61dc4e565b60208151910120813b1561091d57829160448392604051948593849263267d3d7b60e11b84526001600485015260248401525af18015610649576106355750f35b816116d59161da4e565b61064657805f611675565b816116ea9161da4e565b61064657805f611620565b503461064657806003193601126106465761170e61e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957611b1e575b506022546001600160a01b031661177e61e3a7565b90803b1561091d576040516377e4d4ad60e01b815291839183918290849082906117ab906004830161da6f565b03925af1801561064957611b09575b506022546001600160a01b03166117cf61e40f565b90803b1561091d57604051635269237d60e11b815291839183918290849082906117fc906004830161dab6565b03925af1801561064957611af4575b506022546001600160a01b031661182061e46d565b813b1561091d576020606484928360405195869485936369b6533160e01b85526001600486015280516024860152015160448401525af1801561064957611adf575b506022546001600160a01b031661187761e49d565b90803b1561091d57604051630cc6160160e31b815291839183918290849082906118a4906004830161dae7565b03925af1801561064957611aca575b506022546001600160a01b03166118c861e4d7565b90803b1561091d57604051633608d1c360e11b815291839183918290849082906118f5906004830161db10565b03925af1801561064957611ab5575b506022546001600160a01b031661191c6112cb61dca8565b90803b1561091d5761195d8392918392604051948580948193632dc3f61760e11b83526001600484015283602484015260606044840152606483019061db6f565b03925af1801561064957611aa0575b5060405163111e73bd60e01b6020820152600160248201526024815261199360448261da4e565b5f51602062010a235f395f51905f523b1561065457816119cf916040518093819263f28dceb360e01b835260206004840152602483019061d860565b0381835f51602062010a235f395f51905f525af1801561064957611a8b575b506022546001600160a01b0316803b156106545781809160246040518094819363fb4dcb8b60e01b8352600160048401525af1801561064957611a76575b50505f51602062010a235f395f51905f523b15610646576040516390c5013b60e01b815281908181600481835f51602062010a235f395f51905f525af18015610649576106355750f35b81611a809161da4e565b61064657805f611a2c565b81611a959161da4e565b61064657805f6119ee565b81611aaa9161da4e565b61064657805f61196c565b81611abf9161da4e565b61064657805f611904565b81611ad49161da4e565b61064657805f6118b3565b81611ae99161da4e565b61064657805f611862565b81611afe9161da4e565b61064657805f61180b565b81611b139161da4e565b61064657805f6117ba565b81611b289161da4e565b61064657805f611769565b5034610646578060031936011261064657611b4c61e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957611cc4575b50505f51602062010a235f395f51905f523b156106465760405163248e63e160e11b81528190818180611bdc6004820161dc31565b0381835f51602062010a235f395f51905f525af1801561064957611caf575b50507f6ac7bb36990be20afe8d2777e03a1c2684a4589a514d45a4d6f77e5371aafda5611c2661dccc565b60208151910120604051906001825260208201526080604082015280611c4e6080820161dcf2565b4260608301520390a160225481906001600160a01b0316611c6d61dccc565b60208151910120813b1561091d578290604051928391633927a4c360e01b83526001600484015260248301526060604483015281838161090c6064820161dcf2565b81611cb99161da4e565b61064657805f611bfb565b81611cce9161da4e565b61064657805f611ba7565b5034610646578060031936011261064657611cf261e2e4565b60205481906001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957611df6575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b815263793e95df60e01b600482015281908181602481835f51602062010a235f395f51905f525af1801561064957611de1575b506022546001600160a01b0316611db461e4d7565b90803b1561091d57604051633608d1c360e11b8152918391839182908490829061090c906004830161db10565b81611deb9161da4e565b61064657805f611d9f565b81611e009161da4e565b61064657805f611d4a565b5034610646578060031936011261064657611e2461e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576120eb575b506022546001600160a01b0316611e9461e3a7565b90803b1561091d576040516377e4d4ad60e01b81529183918391829084908290611ec1906004830161da6f565b03925af18015610649576120d6575b506022546001600160a01b0316611ee561e40f565b90803b1561091d57604051635269237d60e11b81529183918391829084908290611f12906004830161dab6565b03925af18015610649576120c1575b506022546001600160a01b0316611f3661e49d565b90803b1561091d57604051630cc6160160e31b81529183918391829084908290611f63906004830161dae7565b03925af18015610649576120ac575b506022546001600160a01b0316611f8761e4d7565b90803b1561091d57604051633608d1c360e11b81529183918391829084908290611fb4906004830161db10565b03925af1801561064957612097575b506022546001600160a01b0316611fdb6112cb61dca8565b90803b1561091d5761201c8392918392604051948580948193632dc3f61760e11b83526001600484015283602484015260606044840152606483019061db6f565b03925af1801561064957612082575b506022546001600160a01b031661204061dccc565b60208151910120813b1561091d578290604051928391633927a4c360e01b83526001600484015260248301526060604483015281838161195d6064820161dcf2565b8161208c9161da4e565b61064657805f61202b565b816120a19161da4e565b61064657805f611fc3565b816120b69161da4e565b61064657805f611f72565b816120cb9161da4e565b61064657805f611f21565b816120e09161da4e565b61064657805f611ed0565b816120f59161da4e565b61064657805f611e7f565b503461064657806003193601126106465761211961e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576122cc575b506022546001600160a01b0316803b15610654578180916024604051809481936301dbd4b760e31b8352600160048401525af18015610649576122b7575b50601f5460081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576122a2575b50604051630a1f679b60e01b6020820152600160248201526024815261223360448261da4e565b5f51602062010a235f395f51905f523b15610654578161226f916040518093819263f28dceb360e01b835260206004840152602483019061d860565b0381835f51602062010a235f395f51905f525af180156106495761092157506022546001600160a01b03166108df61e3a7565b816122ac9161da4e565b61064657805f61220c565b816122c19161da4e565b61064657805f6121b2565b816122d69161da4e565b61064657805f612174565b503461064657806003193601126106465760405160158054808352908352909160208301917f55f448fdea98c4d29eb340757ef0a66cd03dbb9538908a6a81d96026b71ec475915b8181106123505761234c856123408187038261da4e565b6040519182918261d81e565b0390f35b82546001600160a01b0316845260209093019260019283019201612329565b503461064657806003193601126106465761238861e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576124f9575b506022546001600160a01b03166123f861e49d565b90803b1561091d57604051630cc6160160e31b81529183918391829084908290612425906004830161dae7565b03925af18015610649576124e4575b50506022546040516336101a6560e11b81526001600482015290606090829060249082906001600160a01b03165afa801561064957828392849261248e575b506109f4926124846124899261e840565b61e89d565b61eeff565b925050506060813d6060116124dc575b816124ab6060938361da4e565b81010312610a2a57806124896109f492516124846124d060406020860151950161dc9b565b93949192506124739050565b3d915061249e565b816124ee9161da4e565b61064657805f612434565b816125039161da4e565b61064657805f6123e3565b503461064657806003193601126106465761252761e2e4565b6022546040516312514a9160e11b81526001600482015290602090829060249082906001600160a01b03165afa908115610649578291612747575b506103e842018042116127335782905f51602062010a235f395f51905f523b15610a2a57604051906372eb5f8160e11b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761271e575b50601f5460081c6001600160a01b03165f51602062010a235f395f51905f523b15610a2a576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957612709575b506022546001600160a01b031661262a61e3a7565b90803b15610a73576040516377e4d4ad60e01b81529183918391829084908290612657906004830161da6f565b03925af18015610649576126f4575b50506022546040516312514a9160e11b8152600160048201529190602090839060249082906001600160a01b03165afa918215610a7f5783926126ba575b50906126b36109f4928261e956565b429061e8fa565b91506020823d6020116126ec575b816126d56020938361da4e565b810103126126e8579051906126b36126a4565b5f80fd5b3d91506126c8565b816126fe9161da4e565b610a2a57815f612666565b816127139161da4e565b610a2a57815f612615565b816127289161da4e565b610a2a57815f6125bb565b634e487b7160e01b83526011600452602483fd5b90506020813d602011612771575b816127626020938361da4e565b810103126126e857515f612562565b3d9150612755565b503461064657806003193601126106465761279261e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576128cb575b50505f51602062010a235f395f51905f523b156106465760405163248e63e160e11b815281908181806128226004820161dc31565b0381835f51602062010a235f395f51905f525af18015610649576128b6575b50507fdbb6d31475bec9849fbf352a7c353cdf096d6e2d972cf78bba644a80269dd37b6040805160018152426020820152a160225481906001600160a01b031661288961e49d565b90803b1561091d57604051630cc6160160e31b8152918391839182908490829061090c906004830161dae7565b816128c09161da4e565b61064657805f612841565b816128d59161da4e565b61064657805f6127ed565b503461064657806003193601126106465760205481906001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576129dd575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b815263793e95df60e01b600482015281908181602481835f51602062010a235f395f51905f525af1801561064957610e6257506022546001600160a01b0316803b15610654578180916024604051809481936304bd12bb60e01b8352600160048401525af18015610649576106355750f35b816129e79161da4e565b61064657805f612949565b5034610646578060031936011261064657612a0b61e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957612b44575b50505f51602062010a235f395f51905f523b156106465760405163248e63e160e11b81528190818180612a9b6004820161dc31565b0381835f51602062010a235f395f51905f525af1801561064957612b2f575b50507f26a7b1d1892f9b115a55617a38a1bbf216b66c1703ee89cebc5c83725da2f9246040805160018152426020820152a160225481906001600160a01b0316612b0261e40f565b90803b1561091d57604051635269237d60e11b8152918391839182908490829061090c906004830161dab6565b81612b399161da4e565b61064657805f612aba565b81612b4e9161da4e565b61064657805f612a66565b5034610646578060031936011261064657612b7261e2e4565b6040600d60208251612b84848261da4e565b828152016c4d616e75666163747572696e6760981b815220906044602060018060a01b036022541683519283809263a75a047160e01b8252600160048301528760248301525afa8015612e6d578490612ea1575b612be2915061f0d6565b601f54839060081c6001600160a01b03165f51602062010a235f395f51905f523b15610a2a5782519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015612e0f57612e8c575b506022546001600160a01b0316803b15610a2a57818091604485518094819363267d3d7b60e11b8352600160048401528960248401525af18015612e0f57612e77575b5050602254815163a75a047160e01b8152600160048201526024810184905290602090829060449082906001600160a01b03165afa8015612e6d578490612e2e575b612ccb915061f077565b601f54839060081c6001600160a01b03165f51602062010a235f395f51905f523b15610a2a5782519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015612e0f57612e19575b506022546001600160a01b0316803b15610a2a57818091604485518094819363030d4a7760e21b8352600160048401528960248401525af18015612e0f57612dfa575b5050602254815163a75a047160e01b8152600160048201526024810193909352602090839060449082906001600160a01b03165afa908115612df157508290612db6575b6109f4915061f0d6565b506020813d602011612de9575b81612dd06020938361da4e565b81010312610a2a57612de46109f49161dc9b565b612dac565b3d9150612dc3565b513d84823e3d90fd5b81612e049161da4e565b610a7357825f612d68565b83513d84823e3d90fd5b81612e239161da4e565b610a7357825f612d25565b506020813d602011612e65575b81612e486020938361da4e565b81010312612e6157612e5c612ccb9161dc9b565b612cc1565b8380fd5b3d9150612e3b565b82513d86823e3d90fd5b81612e819161da4e565b610a7357825f612c7f565b81612e969161da4e565b610a7357825f612c3c565b506020813d602011612ed4575b81612ebb6020938361da4e565b81010312612e6157612ecf612be29161dc9b565b612bd8565b3d9150612eae565b5034610646578060031936011261064657612ef561e9b3565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957612fe6575b50604051630a1f679b60e01b60208201526001602482015260248152612f7760448261da4e565b5f51602062010a235f395f51905f523b156106545781612fb3916040518093819263f28dceb360e01b835260206004840152602483019061d860565b0381835f51602062010a235f395f51905f525af1801561064957611de157506022546001600160a01b0316611db461e4d7565b81612ff09161da4e565b61064657805f612f50565b503461064657806003193601126106465761301461e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957613120575b50505f51602062010a235f395f51905f523b156106465760405163248e63e160e11b815281908181806130a46004820161dc31565b0381835f51602062010a235f395f51905f525af180156106495761310b575b50507f9638a3519a3fc3e7d5c01014e107171b238d1bfed1c6b85b472e1826a1cfc6d66040805160018152426020820152a160225481906001600160a01b0316611db461e4d7565b816131159161da4e565b61064657805f6130c3565b8161312a9161da4e565b61064657805f61306f565b503461064657806003193601126106465761314e61e2e4565b60205481906001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957613250575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b815263793e95df60e01b600482015281908181602481835f51602062010a235f395f51905f525af180156106495761323b575b506022546001600160a01b0316803b15610654578180916024604051809481936301dbd4b760e31b8352600160048401525af18015610649576106355750f35b816132459161da4e565b61064657805f6131fb565b8161325a9161da4e565b61064657805f6131a6565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761333a575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b81526362f4a20760e01b600482015281908181602481835f51602062010a235f395f51905f525af1801561064957610ba657506022546001600160a01b0316610b6561dc4e565b816133449161da4e565b61064657805f6132d1565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957613424575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b81526362f4a20760e01b600482015281908181602481835f51602062010a235f395f51905f525af180156106495761092157506022546001600160a01b03166108df61e3a7565b8161342e9161da4e565b61064657805f6133bb565b503461064657806003193601126106465761345261e9b3565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576122a25750604051630a1f679b60e01b6020820152600160248201526024815261223360448261da4e565b50346106465780600319360112610646576134ec61e9b3565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576135f3575b50604051630a1f679b60e01b6020820152600160248201526024815261356e60448261da4e565b5f51602062010a235f395f51905f523b1561065457816135aa916040518093819263f28dceb360e01b835260206004840152602483019061d860565b0381835f51602062010a235f395f51905f525af18015610649576135de575b506022546001600160a01b0316612b0261e40f565b816135e89161da4e565b61064657805f6135c9565b816135fd9161da4e565b61064657805f613547565b503461064657806003193601126106465761362161e2e4565b60205481906001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761373c575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b815263793e95df60e01b600482015281908181602481835f51602062010a235f395f51905f525af1801561064957613727575b506022546001600160a01b03166136e361e46d565b813b1561091d576020606484928360405195869485936369b6533160e01b85526001600486015280516024860152015160448401525af18015610649576106355750f35b816137319161da4e565b61064657805f6136ce565b816137469161da4e565b61064657805f613679565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957613851575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b81526362f4a20760e01b600482015281908181602481835f51602062010a235f395f51905f525af180156106495761065757506022546001600160a01b0316803b156106545781809160246040518094819363fb4dcb8b60e01b8352600160048401525af18015610649576106355750f35b8161385b9161da4e565b61064657805f6137bd565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957613ab2575b506022546020546001600160a01b039182169116813b1561091d57829160248392604051948593849263f770713b60e01b845260048401525af1801561064957613a9d575b506020546001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957613a88575b506022546001600160a01b0316803b15610654578180916024604051809481936304bd12bb60e01b8352606360048401525af1801561064957613a73575b5050602254604051632574690d60e11b8152606360048201526001600160a01b0390911690602081602481855afa908115610a7f578391613a2e575b506004916139f760209261f077565b604051632c728c4b60e11b815292839182905afa8015610649576109f491839161155b57506020546001600160a01b03169061f1ce565b90506020813d602011613a6b575b81613a496020938361da4e565b81010312610a73576004916139f7613a6260209361dc9b565b925050916139e8565b3d9150613a3c565b81613a7d9161da4e565b61064657805f6139ac565b81613a929161da4e565b61064657805f61396e565b81613aa79161da4e565b61064657805f613917565b81613abc9161da4e565b61064657805f6138d2565b5034610646578060031936011261064657613ae061e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957613c02575b50505f51602062010a235f395f51905f523b156106465760405163248e63e160e11b81528190818180613b706004820161dc31565b0381835f51602062010a235f395f51905f525af1801561064957613bed575b50507f1210d3ecd972f25e1e2251627ec83fb00cb0e435dbe0c5abadf32a9e50ee9f366060613bbc61dc4e565b6020815191012060405190600182526020820152426040820152a160225481906001600160a01b031661168a61dc4e565b81613bf79161da4e565b61064657805f613b8f565b81613c0c9161da4e565b61064657805f613b3b565b5034610646578060031936011261064657613c3061e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957613f13575b5050806040613cb98151613c9f838261da4e565b600881526713dc9a59da5b985b60c21b602082015261e53b565b61032060c08201526022546001600160a01b0316803b15613ef957613d0c84929183928551948580948193632dc3f61760e11b83526001600484015283602484015260606044840152606483019061db6f565b03925af18015613ea657908391613efe575b5050613d2b6112cb61e2a0565b61038460c08201526022546001600160a01b0316803b15613ef957613d7e84929183928551948580948193632dc3f61760e11b83526001600484015283602484015260606044840152606483019061db6f565b03925af18015613ea657908391613ee4575b506022548251635bffd88f60e01b815260016004820152602481018390529190829060449082906001600160a01b03165afa908115613ea65783908492613eb2575b50613de590613ddf61e2a0565b9061f005565b6103848103613e38575b505f51602062010a235f395f51905f523b156106545780516390c5013b60e01b8152908282600481835f51602062010a235f395f51905f525af1908115612df157506106355750f35b5f51602062010a235f395f51905f523b1561091d5781519063260a5b1560e21b82526004820152610384602482015282816044815f51602062010a235f395f51905f525afa8015613ea657908391613e91575b50613def565b81613e9b9161da4e565b61065457815f613e8b565b505051903d90823e3d90fd5b613de59250613ed391503d8086833e613ecb818361da4e565b81019061e19c565b505050969594505050505090613dd2565b81613eee9161da4e565b61065457815f613d90565b505050fd5b81613f089161da4e565b61065457815f613d1e565b81613f1d9161da4e565b61064657805f613c8b565b5034610646578060031936011261064657613f4161e9b3565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957614032575b50604051630a1f679b60e01b60208201526001602482015260248152613fc360448261da4e565b5f51602062010a235f395f51905f523b156106545781613fff916040518093819263f28dceb360e01b835260206004840152602483019061d860565b0381835f51602062010a235f395f51905f525af180156106495761372757506022546001600160a01b03166136e361e46d565b8161403c9161da4e565b61064657805f613f9c565b503461064657806003193601126106465761406061e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576141c9575b505060018060a01b0360225416816040916004602084516140dc868261da4e565b82815201630d0c2e6d60e31b815220813b15610a735782916084839286519485938492633927a4c360e01b8452600160048501526024840152606060448401528160648401525af180156141bc576141a7575b5060225482516335ed308360e11b8152600160048201529190829060249082906001600160a01b03165afa908115613ea657916109f4928492614183575b50519061417b60208361da4e565b83825261f005565b6141a09192503d8086833e614198818361da4e565b81019061debd565b905f61416d565b816141b19161da4e565b610a2a57815f61412f565b50505051903d90823e3d90fd5b816141d39161da4e565b61064657805f6140bb565b503461064657806003193601126106465760206141f961e203565b6040519015158152f35b503461064657806003193601126106465761421c61e9b3565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957614323575b50604051630a1f679b60e01b6020820152600160248201526024815261429e60448261da4e565b5f51602062010a235f395f51905f523b1561065457816142da916040518093819263f28dceb360e01b835260206004840152602483019061d860565b0381835f51602062010a235f395f51905f525af180156106495761430e575b506022546001600160a01b031661288961e49d565b816143189161da4e565b61064657805f6142f9565b8161432d9161da4e565b61064657805f614277565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957614410575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b81526362f4a20760e01b600482015281908181602481835f51602062010a235f395f51905f525af180156106495761131257506022546001600160a01b03166112d06112cb61dca8565b8161441a9161da4e565b61064657805f6143a4565b503461064657806003193601126106465761443e61e2e4565b602254604051635ec57d2360e11b81526001600482015290602090829060249082906001600160a01b03165afa80156106495782906145c6575b614482915061eeff565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576145b1575b506022546001600160a01b0316803b15610654578180916024604051809481936301dbd4b760e31b8352600160048401525af180156106495761459c575b5050602254604051635ec57d2360e11b81526001600482015290602090829060249082906001600160a01b03165afa8015610649578290614561575b6109f4915061ef54565b506020813d602011614594575b8161457b6020938361da4e565b81010312610a2a5761458f6109f49161dc9b565b614557565b3d915061456e565b816145a69161da4e565b61064657805f61451b565b816145bb9161da4e565b61064657805f6144dd565b506020813d6020116145f9575b816145e06020938361da4e565b81010312610a2a576145f46144829161dc9b565b614478565b3d91506145d3565b503461064657806003193601126106465761461a61e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957614878575b506022546001600160a01b031661468a61e3a7565b90803b1561091d576040516377e4d4ad60e01b815291839183918290849082906146b7906004830161da6f565b03925af1801561064957614863575b5050602254604051637a861adb60e01b8152600160048201529060c090829060249082906001600160a01b03165afa8015610649578283808190829383968496614821575b506147159061e7df565b620f424081036147b1575b506302faf0808103614749575b50506109f49261473f6147449261e89d565b61e786565b61f077565b5f51602062010a235f395f51905f523b15610a2a576040519063260a5b1560e21b825260048201526302faf080602482015281816044815f51602062010a235f395f51905f525afa8015610649571561472d57816147a69161da4e565b612e6157835f61472d565b5f51602062010a235f395f51905f523b15610a73576040519063260a5b1560e21b82526004820152620f4240602482015282816044815f51602062010a235f395f51905f525afa908115610a7f57839161480c575b50614720565b816148169161da4e565b610a2a57815f614806565b939650505050614715925061484e915060c03d60c01161485c575b614846818361da4e565b81019061df3e565b90969095919490939161470b565b503d61483c565b8161486d9161da4e565b61064657805f6146c6565b816148829161da4e565b61064657805f614675565b50346106465780600319360112610646576019546148aa8161dd19565b916148b8604051938461da4e565b818352601981527f944998273e477b495144fb8794c914197f3ccb46be2900f4698fd0ef743c9695602084015b8383106148fa576040518061234c878261d8c1565b6001602081926149098561dd58565b8152019201920191906148e5565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957614b32575b50505f51602062010a235f395f51905f523b156106465760405163248e63e160e11b815281908181806149b86004820161dc31565b0381835f51602062010a235f395f51905f525af1801561064957614b1d575b50507f8039ca5e7ab280894dd980ce72fff4672de58cbe4219cee5da6059ab85db2891602060405160148152a160225481906001600160a01b0316803b156106545781809160246040518094819363a3a1da7b60e01b8352601460048401525af1801561064957614b08575b50602254604051634d4f717760e01b815290602090829060049082906001600160a01b03165afa80156106495760ff918391614ad9575b501660148103614a875750f35b5f51602062010a235f395f51905f523b15610654576040519063260a5b1560e21b825260048201526014602482015281816044815f51602062010a235f395f51905f525afa8015610649576106355750f35b614afb915060203d602011614b01575b614af3818361da4e565b81019061df05565b5f614a7a565b503d614ae9565b81614b129161da4e565b61064657805f614a43565b81614b279161da4e565b61064657805f6149d7565b81614b3c9161da4e565b61064657805f614983565b5034610646578060031936011261064657601c54614b648161dd19565b91614b72604051938461da4e565b818352601c81527f0e4562a10381dec21b205ed72637e6b1b523bdd0e4d4d50af5cd23dd4500a211602084015b838310614bb4576040518061234c878261d920565b60026020600192604051614bc78161d997565b848060a01b038654168152614bdd85870161df70565b83820152815201920192019190614b9f565b5034610646578060031936011261064657614c0861e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957614fa7575b505b8160ff82166005811015614d205760018060a01b036022541690614cb16040516402a34b2b9160dd1b602082015260ff60f81b8660f81b166025820152600681526112cb60268261da4e565b823b15612e6157614cef92849283604051809681958294632dc3f61760e11b845260016004850152602484015260606044840152606483019061db6f565b03925af1801561064957614d0b575b505060010160ff16614c65565b81614d159161da4e565b610a2a57815f614cfe565b5060225460405163fe26d96560e01b81526001600482015282916001600160a01b031690602081602481855afa8015610a7f5760ff918491614f88575b501660058103614f1a575b50604090614d938251614d7b848261da4e565b60068152652a34b2b9101b60d11b602082015261e53b565b90803b15613ef9578251632dc3f61760e11b81526001600482015260066024820152606060448201529184918391829084908290614dd590606483019061db6f565b03925af18015613ea657908391614f05575b5050602254815163fe26d96560e01b81526001600482015290602090829060249082906001600160a01b03165afa908115613ea6579060ff918491614ee6575b501660078103614e7a57505f51602062010a235f395f51905f523b156106545780516390c5013b60e01b8152908282600481835f51602062010a235f395f51905f525af1908115612df157506106355750f35b5f51602062010a235f395f51905f523b1561091d5781519063260a5b1560e21b825260048201526007602482015282816044815f51602062010a235f395f51905f525afa8015613ea657908391614ed15750613def565b81614edb9161da4e565b610654578184613e8b565b614eff915060203d602011614b0157614af3818361da4e565b85614e27565b81614f0f9161da4e565b610654578184614de7565b5f51602062010a235f395f51905f523b1561091d576040519063260a5b1560e21b825260048201526005602482015282816044815f51602062010a235f395f51905f525afa908115610a7f578391614f73575b50614d68565b81614f7d9161da4e565b610654578184614f6d565b614fa1915060203d602011614b0157614af3818361da4e565b85614d5d565b81614fb19161da4e565b61064657805f614c63565b5034610646578060031936011261064657614fd561e2e4565b602254604051634a096d2b60e01b8152600160048201526001600160a01b0390911690602081602481855afa908115610a7f57839161569e575b5060249161501e60209261eeff565b604051635037f17b60e01b81526001600482015292839182905afa8015610649578290615663575b615050915061ef54565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761564e575b506022546001600160a01b03166150c061e3a7565b90803b1561091d576040516377e4d4ad60e01b815291839183918290849082906150ed906004830161da6f565b03925af1801561064957615639575b506022546001600160a01b031661511161e40f565b90803b1561091d57604051635269237d60e11b8152918391839182908490829061513e906004830161dab6565b03925af1801561064957615624575b506022546001600160a01b031661516261e46d565b813b1561091d576020606484928360405195869485936369b6533160e01b85526001600486015280516024860152015160448401525af180156106495761560f575b506022546001600160a01b03166151b961e49d565b90803b1561091d57604051630cc6160160e31b815291839183918290849082906151e6906004830161dae7565b03925af18015610649576155fa575b506022546001600160a01b031661520a61e4d7565b90803b1561091d57604051633608d1c360e11b81529183918391829084908290615237906004830161db10565b03925af18015610649576155e5575b506022546001600160a01b031661525e6112cb61df1e565b90803b1561091d5761529f8392918392604051948580948193632dc3f61760e11b83526001600484015283602484015260606044840152606483019061db6f565b03925af18015610649576155d0575b506022546001600160a01b03166152c361dbe6565b6020815191012090803b1561091d57604051633927a4c360e01b815291839183918290849082906152f7906004830161dc07565b03925af18015610649576155bb575b50505f51602062010a235f395f51905f523b15610646576040516390c5013b60e01b815281908181600481835f51602062010a235f395f51905f525af18015610649576155a6575b505061535861f131565b602254604051635037f17b60e01b8152600160048201526001600160a01b0390911690602081602481855afa908115610a7f578391615561575b506024916153a160209261eeff565b604051634a096d2b60e01b81526001600482015292839182905afa8015610649578290615526575b6153d3915061eeff565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957615511575b506022546001600160a01b0316803b15610654578180916024604051809481936301dbd4b760e31b8352600160048401525af18015610649576154fc575b5050602254604051634a096d2b60e01b8152600160048201526001600160a01b0390911690602081602481855afa908115610a7f5783916154b7575b506024916109c260209261ef54565b90506020813d6020116154f4575b816154d26020938361da4e565b81010312610a73576024916109c26154eb60209361dc9b565b925050916154a8565b3d91506154c5565b816155069161da4e565b61064657805f61546c565b8161551b9161da4e565b61064657805f61542e565b506020813d602011615559575b816155406020938361da4e565b81010312610a2a576155546153d39161dc9b565b6153c9565b3d9150615533565b90506020813d60201161559e575b8161557c6020938361da4e565b81010312610a73576024916153a161559560209361dc9b565b92505091615392565b3d915061556f565b816155b09161da4e565b61064657805f61534e565b816155c59161da4e565b61064657805f615306565b816155da9161da4e565b61064657805f6152ae565b816155ef9161da4e565b61064657805f615246565b816156049161da4e565b61064657805f6151f5565b816156199161da4e565b61064657805f6151a4565b8161562e9161da4e565b61064657805f61514d565b816156439161da4e565b61064657805f6150fc565b816156589161da4e565b61064657805f6150ab565b506020813d602011615696575b8161567d6020938361da4e565b81010312610a2a576156916150509161dc9b565b615046565b3d9150615670565b90506020813d6020116156db575b816156b96020938361da4e565b81010312610a735760249161501e6156d260209361dc9b565b9250509161500f565b3d91506156ac565b50346106465780600319360112610646576156fc61e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957615868575b506040516342e5795760e01b602082015260ff60248201526024815261577e60448261da4e565b5f51602062010a235f395f51905f523b1561065457816157ba916040518093819263f28dceb360e01b835260206004840152602483019061d860565b0381835f51602062010a235f395f51905f525af1801561064957615853575b5060018060a01b03602254166158106040516157f660408261da4e565b600881526726b0bc102a34b2b960c11b602082015261e53b565b90803b1561091d57604051632dc3f61760e11b81526001600482015260ff602482015260606044820152918391839182908490829061090c90606483019061db6f565b8161585d9161da4e565b61064657805f6157d9565b816158729161da4e565b61064657805f615757565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957615992575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b81526362f4a20760e01b600482015281908181602481835f51602062010a235f395f51905f525af180156106495761597d575b506022546001600160a01b0316803b15610654578180916024604051809481936304bd12bb60e01b83528160048401525af18015610649576106355750f35b816159879161da4e565b61064657805f61593e565b8161599c9161da4e565b61064657805f6158e9565b50346106465780600319360112610646576159c061e2e4565b60205481906001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957615a81575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b815263793e95df60e01b600482015281908181602481835f51602062010a235f395f51905f525af18015610649576135de57506022546001600160a01b0316612b0261e40f565b81615a8b9161da4e565b61064657805f615a18565b5034610646578060031936011261064657615aaf61e9b3565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957615bb6575b50604051630a1f679b60e01b60208201526001602482015260248152615b3160448261da4e565b5f51602062010a235f395f51905f523b156106545781615b6d916040518093819263f28dceb360e01b835260206004840152602483019061d860565b0381835f51602062010a235f395f51905f525af1801561064957615ba1575b506022546001600160a01b0316611c6d61dccc565b81615bab9161da4e565b61064657805f615b8c565b81615bc09161da4e565b61064657805f615b0a565b5034610646578060031936011261064657615be461e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957615d84575b506022546001600160a01b0316615c5461e4d7565b90803b1561091d57604051633608d1c360e11b81529183918391829084908290615c81906004830161db10565b03925af1801561064957615d6f575b50506022546040516328f4ca3160e01b8152600160048201529060a090829060249082906001600160a01b03165afa8015610649578283849185948694615cff575b50615cfa92615cf06109f49693615ceb615cf59461e5ec565b61e661565b61e7df565b61ef54565b61e840565b94505050505060a0813d60a011615d67575b81615d1e60a0938361da4e565b81010312610a2a5780615cfa6109f49251615cf5602084015193615cf06040820151615ceb6080615d516060860161dc9b565b9401519597919395979450509396505092615cd2565b3d9150615d11565b81615d799161da4e565b61064657805f615c90565b81615d8e9161da4e565b61064657805f615c3f565b5034610646578060031936011261064657615db261e2e4565b60205481906001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957615eb4575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b815263793e95df60e01b600482015281908181602481835f51602062010a235f395f51905f525af1801561064957615e9f575b506022546001600160a01b0316803b156106545781809160246040518094819363a3a1da7b60e01b8352601e60048401525af18015610649576106355750f35b81615ea99161da4e565b61064657805f615e5f565b81615ebe9161da4e565b61064657805f615e0a565b5034610646578060031936011261064657615ee261e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576160c0575b506022546001600160a01b0316803b15610654578180916024604051809481936301dbd4b760e31b8352600160048401525af18015610649576160ab575b50601f5460081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957616096575b50604051634b52888f60e01b60208201526001602482015260248152615ffc60448261da4e565b5f51602062010a235f395f51905f523b156106545781616038916040518093819263f28dceb360e01b835260206004840152602483019061d860565b0381835f51602062010a235f395f51905f525af180156106495761065757506022546001600160a01b0316803b156106545781809160246040518094819363fb4dcb8b60e01b8352600160048401525af18015610649576106355750f35b816160a09161da4e565b61064657805f615fd5565b816160b59161da4e565b61064657805f615f7b565b816160ca9161da4e565b61064657805f615f3d565b50346106465780600319360112610646576160ee61e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576164de575b506022546001600160a01b031661615e61e3a7565b813b1561091d578291616187916040519485809481936377e4d4ad60e01b83526004830161da6f565b03925af18015610649576164c9575b506022546040516312514a9160e11b8152600160048201529190602090839060249082906001600160a01b03165afa9182156164bc578192616488575b5060644201918242116164745781925f51602062010a235f395f51905f523b1561091d57604051906372eb5f8160e11b825260048201528281602481835f51602062010a235f395f51905f525af1908115610a7f57839161645f575b505060405161623d8161d9c6565b6301312d008152621e848060208201526305f5e100604082015261016d60608201526001608082015260a081018390526022546001600160a01b0316803b15613ef9576040516377e4d4ad60e01b815291849183918290849082906162a5906004830161da6f565b03925af1908115610a7f57839161644a575b50506022546040516312514a9160e11b8152600160048201526001600160a01b039091169190602081602481865afa90811561643f578491616404575b509161630460c09260249461e956565b604051637a861adb60e01b81526001600482015292839182905afa9081156106495782916163e0575b506301312d0081036163835750505f51602062010a235f395f51905f523b15610646576040516390c5013b60e01b815281908181600481835f51602062010a235f395f51905f525af18015610649576106355750f35b5f51602062010a235f395f51905f523b15610654576040519063260a5b1560e21b825260048201526301312d00602482015281816044815f51602062010a235f395f51905f525afa80156106495715611a2c5781611a809161da4e565b6163f9915060c03d60c01161485c57614846818361da4e565b50505050505f61632d565b929350506020823d602011616437575b816164216020938361da4e565b810103126126e8579051839291906163046162f4565b3d9150616414565b6040513d86823e3d90fd5b816164549161da4e565b61065457815f6162b7565b816164699161da4e565b61065457815f61622f565b634e487b7160e01b82526011600452602482fd5b9091506020813d6020116164b4575b816164a46020938361da4e565b810103126126e85751905f6161d3565b3d9150616497565b50604051903d90823e3d90fd5b6164d482809261da4e565b610646575f616196565b816164e89161da4e565b61064657805f616149565b503461064657806003193601126106465761650c61e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576166e1575b506022546001600160a01b031661657c61e3a7565b90803b1561091d576040516377e4d4ad60e01b815291839183918290849082906165a9906004830161da6f565b03925af18015610649576166cc575b506022546001600160a01b03166165cd61e40f565b90803b1561091d57604051635269237d60e11b815291839183918290849082906165fa906004830161dab6565b03925af18015610649576166b7575b506022546001600160a01b031661661e61e46d565b813b1561091d576020606484928360405195869485936369b6533160e01b85526001600486015280516024860152015160448401525af18015610649576166a2575b506022546001600160a01b031661667561e49d565b90803b1561091d57604051630cc6160160e31b81529183918391829084908290611fb4906004830161dae7565b816166ac9161da4e565b61064657805f616660565b816166c19161da4e565b61064657805f616609565b816166d69161da4e565b61064657805f6165b8565b816166eb9161da4e565b61064657805f616567565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957616a24575b506022546001600160a01b0316803b15610654578180916024604051809481936304bd12bb60e01b8352600160048401525af1801561064957616a0f575b506022546001600160a01b0316803b15610654578180916024604051809481936304bd12bb60e01b8352600260048401525af18015610649576169fa575b506022546001600160a01b0316803b15610654578180916024604051809481936304bd12bb60e01b8352600360048401525af18015610649576169e5575b50505f51602062010a235f395f51905f523b15610646576040516390c5013b60e01b815281908181600481835f51602062010a235f395f51905f525af18015610649576169d0575b5050602254604051632574690d60e11b8152600160048201526001600160a01b0390911690602081602481855afa8015610a7f578390616995575b6168a9915061f077565b604051632574690d60e11b815260026004820152602081602481855afa908115610a7f578391616950575b506024916168e360209261f077565b604051632574690d60e11b81526003600482015292839182905afa8015610649578290616915575b6109f4915061f077565b506020813d602011616948575b8161692f6020938361da4e565b81010312610a2a576169436109f49161dc9b565b61690b565b3d9150616922565b90506020813d60201161698d575b8161696b6020938361da4e565b81010312610a73576024916168e361698460209361dc9b565b925050916168d4565b3d915061695e565b506020813d6020116169c8575b816169af6020938361da4e565b81010312610a73576169c36168a99161dc9b565b61689f565b3d91506169a2565b816169da9161da4e565b61064657805f616864565b816169ef9161da4e565b61064657805f61681c565b81616a049161da4e565b61064657805f6167de565b81616a199161da4e565b61064657805f6167a0565b81616a2e9161da4e565b61064657805f616762565b5034610646578060031936011261064657616a5261e9b3565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957616b43575b50604051630a1f679b60e01b60208201526001602482015260248152616ad460448261da4e565b5f51602062010a235f395f51905f523b156106545781616b10916040518093819263f28dceb360e01b835260206004840152602483019061d860565b0381835f51602062010a235f395f51905f525af18015610649576116cb57506022546001600160a01b031661168a61dc4e565b81616b4d9161da4e565b61064657805f616aad565b5034610646578060031936011261064657601d54616b758161dd19565b91616b83604051938461da4e565b818352601d81527f6d4407e7be21f808e6509aa9fa9143369579dd7d760fe20a2c09680fc146134f602084015b838310616bc5576040518061234c878261d920565b60026020600192604051616bd88161d997565b848060a01b038654168152616bee85870161df70565b83820152815201920192019190616bb0565b5034610646578060031936011261064657616c1961e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957616dab575b506022546001600160a01b0316616c8961e3a7565b90803b1561091d576040516377e4d4ad60e01b81529183918391829084908290616cb6906004830161da6f565b03925af1801561064957616d96575b506022546001600160a01b0316616cda61e40f565b90803b1561091d57604051635269237d60e11b81529183918391829084908290616d07906004830161dab6565b03925af1801561064957616d81575b506022546001600160a01b0316616d2b61e46d565b813b1561091d576020606484928360405195869485936369b6533160e01b85526001600486015280516024860152015160448401525af18015610649576120ac57506022546001600160a01b0316611f8761e4d7565b81616d8b9161da4e565b61064657805f616d16565b81616da09161da4e565b61064657805f616cc5565b81616db59161da4e565b61064657805f616c74565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957616e95575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b81526362f4a20760e01b600482015281908181602481835f51602062010a235f395f51905f525af18015610649576135de57506022546001600160a01b0316612b0261e40f565b81616e9f9161da4e565b61064657805f616e2c565b5034610646578060031936011261064657616ec361e2e4565b6040600460208251616ed5848261da4e565b82815201630a8cac6d60e31b815220908260018060a01b03601f5460081c165f51602062010a235f395f51905f523b15610a2a5782519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015612e0f57616fe2575b506022546001600160a01b0316803b15610a2a57818091604485518094819363030d4a7760e21b8352600160048401528960248401525af18015612e0f57616fcd575b5050602254815163a75a047160e01b8152600160048201526024810193909352602090839060449082906001600160a01b03165afa908115612df157508290614561576109f4915061ef54565b81616fd79161da4e565b610a7357825f616f80565b81616fec9161da4e565b610a7357825f616f3d565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576170cc575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b81526362f4a20760e01b600482015281908181602481835f51602062010a235f395f51905f525af180156106495761372757506022546001600160a01b03166136e361e46d565b816170d69161da4e565b61064657805f617063565b5034610646578060031936011261064657601a546170fe8161dd19565b9161710c604051938461da4e565b818352601a81527f057c384a7d1c54f3a1b2e5e67b2617b8224fdfd1ea7234eea573a6ff665ff63e602084015b83831061714e576040518061234c878261d8c1565b60016020819261715d8561dd58565b815201920192019190617139565b503461064657806003193601126106465761718461e2e4565b6022546040516312514a9160e11b81526001600482015290602090829060249082906001600160a01b03165afa90811561064957829161737c575b50600a42018042116127335782905f51602062010a235f395f51905f523b15610a2a57604051906372eb5f8160e11b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957617367575b50601f5460081c6001600160a01b03165f51602062010a235f395f51905f523b15610a2a576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957617352575b506022546001600160a01b031661728661e40f565b90803b15610a7357604051635269237d60e11b815291839183918290849082906172b3906004830161dab6565b03925af180156106495761733d575b50506022546040516312514a9160e11b8152600160048201529190602090839060249082906001600160a01b03165afa8015610a7f578390617309575b6109f4925061e956565b506020823d602011617335575b816173236020938361da4e565b810103126126e8576109f491516172ff565b3d9150617316565b816173479161da4e565b610a2a57815f6172c2565b8161735c9161da4e565b610a2a57815f617271565b816173719161da4e565b610a2a57815f617217565b90506020813d6020116173a6575b816173976020938361da4e565b810103126126e857515f6171bf565b3d915061738a565b50346106465780600319360112610646576173c761e2e4565b806173e16040516173d960208261da4e565b82815261e53b565b601f5460081c6001600160a01b03165f51602062010a235f395f51905f523b1561091d576040519063ca669fa760e01b825260048201528281602481835f51602062010a235f395f51905f525af1908115610a7f578391617526575b50506022546001600160a01b0316803b1561091d5761748b8392918392604051948580948193632dc3f61760e11b83526001600484015283602484015260606044840152606483019061db6f565b03925af1801561064957617511575b50602254604051635bffd88f60e01b815260016004820152602481018390529190829060449082906001600160a01b03165afa8015610649576109f49183916174ee575b506040519061417b60208361da4e565b61750291503d8085833e613ecb818361da4e565b5050505050505050505f6174de565b8161751b9161da4e565b61064657805f61749a565b816175309161da4e565b61065457815f61743d565b503461064657806003193601126106465761755461e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957617660575b50505f51602062010a235f395f51905f523b156106465760405163248e63e160e11b815281908181806175e46004820161dc31565b0381835f51602062010a235f395f51905f525af180156106495761764b575b50507f6a50b7174b84444ee4fc852f30eb4d5105a85e60b12b831224dc562daabc3dcd6040805160018152426020820152a160225481906001600160a01b03166108df61e3a7565b816176559161da4e565b61064657805f617603565b8161766a9161da4e565b61064657805f6175af565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957617775575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b81526362f4a20760e01b600482015281908181602481835f51602062010a235f395f51905f525af180156106495761323b57506022546001600160a01b0316803b15610654578180916024604051809481936301dbd4b760e31b8352600160048401525af18015610649576106355750f35b8161777f9161da4e565b61064657805f6176e1565b50346106465780600319360112610646576177a361e2e4565b6022546040516312514a9160e11b81526001600482015290602090829060249082906001600160a01b03165afa9081156106495782916179bf575b50606442018042116127335782905f51602062010a235f395f51905f523b15610a2a57604051906372eb5f8160e11b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576179aa575b50601f5460081c6001600160a01b03165f51602062010a235f395f51905f523b15610a2a576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957617995575b506022546001600160a01b0316803b15610a2a578180916024604051809481936301dbd4b760e31b8352600160048401525af1801561064957617980575b50506022546040516312514a9160e11b8152600160048201526001600160a01b039091169190602081602481865afa90811561643f57849161794d575b5060249261791c602092429061e8fa565b6040516312514a9160e11b81526001600482015293849182905afa8015610a7f578390617309576109f4925061e956565b90506020813d602011617978575b816179686020938361da4e565b810103126126e85751602461790b565b3d915061795b565b8161798a9161da4e565b610a2a57815f6178ce565b8161799f9161da4e565b610a2a57815f617890565b816179b49161da4e565b610a2a57815f617836565b90506020813d6020116179e9575b816179da6020938361da4e565b810103126126e857515f6177de565b3d91506179cd565b5034610646578060031936011261064657617a0a61e2e4565b6040600e60208251617a1c848261da4e565b828152016d1c1bdb1a58de511bd8dd5b595b9d60921b8152208151617a41838261da4e565b600d81526c34b833399d1797a8b6ac17171760991b6020820152601f54849060081c6001600160a01b03165f51602062010a235f395f51905f523b15610a2a5784519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af18015617c6a57617c74575b506022546001600160a01b0316803b15610a2a578185518092633927a4c360e01b82526001600483015286602483015260606044830152818381617afc606482018a61d860565b03925af18015617c6a57617c55575b50506022548351633bf365b160e01b8152600160048201526001600160a01b0390911692602082602481875afa8015617c4b578690617c17575b617b4f925061efa9565b82516335ed308360e11b8152600160048201528481602481865afa908115617c0d576020926024959492617b8a928891617bf3575b5061f005565b82516312514a9160e11b81526001600482015293849182905afa908115612df157508290617bbf575b6109f49150429061e8fa565b506020813d602011617beb575b81617bd96020938361da4e565b810103126126e8576109f49051617bb3565b3d9150617bcc565b617c0791503d808a833e614198818361da4e565b5f617b84565b84513d87823e3d90fd5b506020823d602011617c43575b81617c316020938361da4e565b810103126126e857617b4f9151617b45565b3d9150617c24565b85513d88823e3d90fd5b81617c5f9161da4e565b612e6157835f617b0b565b85513d84823e3d90fd5b81617c7e9161da4e565b612e6157835f617ab5565b5034610646578060031936011261064657617ca261e2e4565b80617cae6112cb61e172565b6103b660c0820152601f5460081c6001600160a01b03165f51602062010a235f395f51905f523b1561091d576040519063ca669fa760e01b825260048201528281602481835f51602062010a235f395f51905f525af1908115610a7f578391617e5e575b50506022546001600160a01b0316803b1561091d57617d608392918392604051948580948193632dc3f61760e11b83526001600484015283602484015260606044840152606483019061db6f565b03925af1801561064957617e49575b50602254604051635bffd88f60e01b81526001600482015260248101839052908290829060449082906001600160a01b03165afa9081156106495782908392617e1f575b50617dc090613ddf61e172565b6103b68103617dcc5750f35b5f51602062010a235f395f51905f523b15610654576040519063260a5b1560e21b825260048201526103b6602482015281816044815f51602062010a235f395f51905f525afa8015610649576106355750f35b617dc09250617e3891503d8085833e613ecb818361da4e565b505050969594505050505090617db3565b81617e539161da4e565b61064657805f617d6f565b81617e689161da4e565b61065457815f617d12565b5034610646578060031936011261064657617e8c61e2e4565b602254604051634a096d2b60e01b81526001600482015290602090829060249082906001600160a01b03165afa80156106495782906182e6575b617ed0915061f077565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af18015610649576182d1575b506022546001600160a01b0316617f4061e3a7565b90803b1561091d576040516377e4d4ad60e01b81529183918391829084908290617f6d906004830161da6f565b03925af18015610649576182bc575b506022546001600160a01b0316617f9161e40f565b90803b1561091d57604051635269237d60e11b81529183918391829084908290617fbe906004830161dab6565b03925af18015610649576182a7575b506022546001600160a01b0316617fe261e46d565b813b1561091d576020606484928360405195869485936369b6533160e01b85526001600486015280516024860152015160448401525af1801561064957618292575b506022546001600160a01b031661803961e49d565b90803b1561091d57604051630cc6160160e31b81529183918391829084908290618066906004830161dae7565b03925af180156106495761827d575b506022546001600160a01b031661808a61e4d7565b90803b1561091d57604051633608d1c360e11b815291839183918290849082906180b7906004830161db10565b03925af1801561064957618268575b506022546001600160a01b03166180de6112cb61dca8565b90803b1561091d5761811f8392918392604051948580948193632dc3f61760e11b83526001600484015283602484015260606044840152606483019061db6f565b03925af1801561064957618253575b506022546001600160a01b031661814361dccc565b60208151910120813b1561091d578290604051928391633927a4c360e01b8352600160048401526024830152606060448301528183816181856064820161dcf2565b03925af180156106495761823e575b50505f51602062010a235f395f51905f523b15610646576040516390c5013b60e01b815281908181600481835f51602062010a235f395f51905f525af1801561064957618229575b50506181e661f131565b602254604051635037f17b60e01b81526001600482015290602090829060249082906001600160a01b03165afa8015610649578290616915576109f4915061f077565b816182339161da4e565b61064657805f6181dc565b816182489161da4e565b61064657805f618194565b8161825d9161da4e565b61064657805f61812e565b816182729161da4e565b61064657805f6180c6565b816182879161da4e565b61064657805f618075565b8161829c9161da4e565b61064657805f618024565b816182b19161da4e565b61064657805f617fcd565b816182c69161da4e565b61064657805f617f7c565b816182db9161da4e565b61064657805f617f2b565b506020813d602011618319575b816183006020938361da4e565b81010312610a2a57618314617ed09161dc9b565b617ec6565b3d91506182f3565b503461064657806003193601126106465761833a61e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957618466575b506022546001600160a01b03166183aa61e40f565b90803b1561091d57604051635269237d60e11b815291839183918290849082906183d7906004830161dab6565b03925af1801561064957618451575b506022546001600160a01b03166183fb61e46d565b813b1561091d576020606484928360405195869485936369b6533160e01b85526001600486015280516024860152015160448401525af18015610649576120c157506022546001600160a01b0316611f3661e49d565b8161845b9161da4e565b61064657805f6183e6565b816184709161da4e565b61064657805f618395565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957618581575b506022546001600160a01b0316803b15610654578180916024604051809481936304bd12bb60e01b835260011960048401525af180156106495761856c575b5050602254604051632574690d60e11b8152600119600482015290602090829060249082906001600160a01b03165afa80156106495782906109f7576109f4915061eeff565b816185769161da4e565b61064657805f618526565b8161858b9161da4e565b61064657805f6184e7565b5034610646578060031936011261064657601b546185b38161dd19565b6185c0604051918261da4e565b818152601b83526020810191837f3ad8aa4f87544323a9d1e5dd902f40c356527a7955687113db5f9a85ad579dc1845b83831061867c57868587604051928392602084019060208552518091526040840160408260051b8601019392905b82821061862d57505050500390f35b9193600191939550602061866c8192603f198a82030186528851908361865c835160408452604084019061d860565b920151908481840391015261d884565b960192019201859493919261861e565b6002602060019260405161868f8161d997565b6186988661dd58565b81526186a585870161df70565b838201528152019201920191906185f0565b50346106465780600319360112610646576186d061e2e4565b806040516186dd8161d9c6565b8181528160208201528160408201528160608201528160808201528160a082015260018060a01b03601f5460081c165f51602062010a235f395f51905f523b1561091d576040519063ca669fa760e01b825260048201528281602481835f51602062010a235f395f51905f525af1908115610a7f57839161883c575b50506022546001600160a01b0316803b1561091d576040516377e4d4ad60e01b81529183918391829084908290618793906004830161da6f565b03925af1801561064957618827575b5050602254604051637a861adb60e01b8152600160048201529060c090829060249082906001600160a01b03165afa908115610649576109f49183849085926187f5575b615cf592935061473f9061e786565b505050615cf561881661473f9260c03d60c01161485c57614846818361da4e565b9496509394508592506187e6915050565b816188319161da4e565b61064657805f6187a2565b816188469161da4e565b61065457815f618759565b503461064657806003193601126106465761886a61e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957618c2d575b506022546001600160a01b03166188da61e3a7565b90803b1561091d576040516377e4d4ad60e01b81529183918391829084908290618907906004830161da6f565b03925af1801561064957618c18575b506022546001600160a01b031661892b61e40f565b90803b1561091d57604051635269237d60e11b81529183918391829084908290618958906004830161dab6565b03925af1801561064957618c03575b506022546001600160a01b031661897c61e46d565b813b1561091d576020606484928360405195869485936369b6533160e01b85526001600486015280516024860152015160448401525af1801561064957618bee575b506022546001600160a01b03166189d361e49d565b90803b1561091d57604051630cc6160160e31b81529183918391829084908290618a00906004830161dae7565b03925af1801561064957618bd9575b506022546001600160a01b0316618a2461e4d7565b90803b1561091d57604051633608d1c360e11b81529183918391829084908290618a51906004830161db10565b03925af1801561064957618bc4575b506022546001600160a01b0316618a786112cb61df1e565b90803b1561091d57618ab98392918392604051948580948193632dc3f61760e11b83526001600484015283602484015260606044840152606483019061db6f565b03925af1801561064957618baf575b506022546001600160a01b0316618add61dbe6565b6020815191012090803b1561091d57604051633927a4c360e01b81529183918391829084908290618b11906004830161dc07565b03925af1801561064957618b9a575b506022546001600160a01b0316803b15610654578180916024604051809481936301dbd4b760e31b8352600160048401525af1801561064957618b85575b50604051634b52888f60e01b6020820152600160248201526024815261199360448261da4e565b81618b8f9161da4e565b61064657805f618b5e565b81618ba49161da4e565b61064657805f618b20565b81618bb99161da4e565b61064657805f618ac8565b81618bce9161da4e565b61064657805f618a60565b81618be39161da4e565b61064657805f618a0f565b81618bf89161da4e565b61064657805f6189be565b81618c0d9161da4e565b61064657805f618967565b81618c229161da4e565b61064657805f618916565b81618c379161da4e565b61064657805f6188c5565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957618d17575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b81526362f4a20760e01b600482015281908181602481835f51602062010a235f395f51905f525af1801561064957611de157506022546001600160a01b0316611db461e4d7565b81618d219161da4e565b61064657805f618cae565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957619036575b50505f51602062010a235f395f51905f523b15610646578060405163248e63e160e11b81526001600482015260016024820152816044820152600160648201528181608481835f51602062010a235f395f51905f525af1801561064957619021575b50507f0d28ab2dec81aaebf86915a865353a44c9779fa1c6158a6ff748dc8e148428856040805160018152426020820152a160225481906001600160a01b0316803b15610654578180916024604051809481936304bd12bb60e01b8352600160048401525af180156106495761900c575b5050602254604051632574690d60e11b8152600160048201526001600160a01b0390911690602081602481855afa8015610a7f578390618fd1575b618eb0915061f077565b604051634a096d2b60e01b815260016004820152602081602481855afa8015610a7f578390618f96575b618ee4915061f077565b604051635037f17b60e01b815260016004820152602081602481855afa908115610a7f578391618f51575b50602491618f1e60209261f0d6565b6040516312514a9160e11b81526001600482015292839182905afa8015610649578290617bbf576109f49150429061e8fa565b90506020813d602011618f8e575b81618f6c6020938361da4e565b81010312610a7357602491618f1e618f8560209361dc9b565b92505091618f0f565b3d9150618f5f565b506020813d602011618fc9575b81618fb06020938361da4e565b81010312610a7357618fc4618ee49161dc9b565b618eda565b3d9150618fa3565b506020813d602011619004575b81618feb6020938361da4e565b81010312610a7357618fff618eb09161dc9b565b618ea6565b3d9150618fde565b816190169161da4e565b61064657805f618e6b565b8161902b9161da4e565b61064657805f618dfa565b816190409161da4e565b61064657805f618d98565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957619120575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b81526362f4a20760e01b600482015281908181602481835f51602062010a235f395f51905f525af1801561064957615ba157506022546001600160a01b0316611c6d61dccc565b8161912a9161da4e565b61064657805f6190b7565b503461064657806003193601126106465761914e61e2e4565b60205481906001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761920f575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b815263793e95df60e01b600482015281908181602481835f51602062010a235f395f51905f525af180156106495761430e57506022546001600160a01b031661288961e49d565b816192199161da4e565b61064657805f6191a6565b503461064657806003193601126106465761923d61e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957619454575b506022546001600160a01b03166192ad61e46d565b813b1561091d576020606484928360405195869485936369b6533160e01b85526001600486015280516024860152015160448401525af180156106495761943f575b506022546040805163d402ab2760e01b81526001600482015291829060249082906001600160a01b03165afa9081156106495782908392619405575b506103e88103619396575b50610bb881036193435750f35b5f51602062010a235f395f51905f523b15610654576040519063260a5b1560e21b82526004820152610bb8602482015281816044815f51602062010a235f395f51905f525afa8015610649576106355750f35b5f51602062010a235f395f51905f523b1561091d576040519063260a5b1560e21b825260048201526103e8602482015282816044815f51602062010a235f395f51905f525afa908115610a7f5783916193f0575b50619336565b816193fa9161da4e565b61065457815f6193ea565b9150506040813d604011619437575b816194216040938361da4e565b810103126106545760208151910151905f61932b565b3d9150619414565b816194499161da4e565b61064657805f6192ef565b8161945e9161da4e565b61064657805f619298565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957619731575b506022546001600160a01b0316803b15610654578180916024604051809481936304bd12bb60e01b8352600160048401525af180156106495761971c575b506022546001600160a01b0316803b15610654578180916024604051809481936304bd12bb60e01b8352600260048401525af1801561064957619707575b505061955b61dc75565b805160209091012060225482906001600160a01b0316803b15610a2a5781809160446040518094819363267d3d7b60e11b8352600160048401528860248401525af18015610649576196f2575b505060225460405163a75a047160e01b815260016004820152602481018390526001600160a01b0390911691602082604481865afa91821561643f5784926196b2575b506195f760209261eeff565b60446040518094819363a75a047160e01b83526002600484015260248301525afa8015610649578290619677575b61962f915061ef54565b5f51602062010a235f395f51905f523b15610646576040516390c5013b60e01b815281908181600481835f51602062010a235f395f51905f525af18015610649576106355750f35b506020813d6020116196aa575b816196916020938361da4e565b81010312610a2a576196a561962f9161dc9b565b619625565b3d9150619684565b91506020823d6020116196ea575b816196cd6020938361da4e565b81010312612e61576195f76196e360209361dc9b565b92506195eb565b3d91506196c0565b816196fc9161da4e565b610a2a57815f6195a8565b816197119161da4e565b61064657805f619551565b816197269161da4e565b61064657805f619513565b8161973b9161da4e565b61064657805f6194d5565b503461064657806003193601126106465761975f61e2e4565b60205481906001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957619820575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b815263793e95df60e01b600482015281908181602481835f51602062010a235f395f51905f525af180156106495761092157506022546001600160a01b03166108df61e3a7565b8161982a9161da4e565b61064657805f6197b7565b503461064657806003193601126106465761984e61e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957619a6f575b505060018060a01b0360225416816040916198dd83516198c9858261da4e565b6002815261543560f01b602082015261e53b565b90803b15610a73578351632dc3f61760e11b8152600160048201526005602482015260606044820152918391839182908490829061991f90606483019061db6f565b03925af180156141bc57619a5a575b50602254825163fe26d96560e01b8152600160048201526001600160a01b0390911690602081602481855afa908115619a50576199769160ff918591619a1c575b501661e729565b6199816112cb61dee5565b90803b15610a73578351632dc3f61760e11b815260016004820152600260248201526060604482015291839183918290849082906199c390606483019061db6f565b03925af180156141bc57619a3b575b5050602254815163fe26d96560e01b81526001600482015290602090829060249082906001600160a01b03165afa918215612df157506109f49160ff918491619a1c57501661e729565b619a35915060203d602011614b0157614af3818361da4e565b5f61996f565b81619a459161da4e565b610a2a57815f6199d2565b84513d85823e3d90fd5b81619a649161da4e565b610a2a57815f61992e565b81619a799161da4e565b61064657805f6198a9565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957619bc7575b506040516342e5795760e01b602082015260ff602482015260248152619b1760448261da4e565b5f51602062010a235f395f51905f523b156106545781619b53916040518093819263f28dceb360e01b835260206004840152602483019061d860565b0381835f51602062010a235f395f51905f525af1801561064957619bb2575b506022546001600160a01b0316803b156106545781809160246040518094819363a3a1da7b60e01b835260ff60048401525af18015610649576106355750f35b81619bbc9161da4e565b61064657805f619b72565b81619bd19161da4e565b61064657805f619af0565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957619cb1575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b81526362f4a20760e01b600482015281908181602481835f51602062010a235f395f51905f525af180156106495761430e57506022546001600160a01b031661288961e49d565b81619cbb9161da4e565b61064657805f619c48565b5034610646578060031936011261064657619cdf61e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957619df6575b50505f51602062010a235f395f51905f523b156106465760405163248e63e160e11b81528190818180619d6f6004820161dc31565b0381835f51602062010a235f395f51905f525af1801561064957619de1575b50507f9c889edde3e184915aa8758beda13d0b548decc0b5a79f3b22ffa3d9d57d0ab260606040516001815260016020820152426040820152a160225481906001600160a01b03166112d06112cb61dca8565b81619deb9161da4e565b61064657805f619d8e565b81619e009161da4e565b61064657805f619d3a565b5034610646578060031936011261064657619e2461e9b3565b602254604051634c2d62b760e01b81526001600482015290602090829060249082906001600160a01b03165afa8015610649578290619f70575b619e68915061eeff565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af1801561064957619f5b575b506022546001600160a01b0316803b15610654578180916024604051809481936304bd12bb60e01b8352600260048401525af1801561064957619f46575b5050602254604051634c2d62b760e01b81526002600482015290602090829060249082906001600160a01b03165afa8015610649578290614561576109f4915061ef54565b81619f509161da4e565b61064657805f619f01565b81619f659161da4e565b61064657805f619ec3565b506020813d602011619fa3575b81619f8a6020938361da4e565b81010312610a2a57619f9e619e689161dc9b565b619e5e565b3d9150619f7d565b5034610646578060031936011261064657619fc461e2e4565b602254604051634a096d2b60e01b81526001600482015290602090829060249082906001600160a01b03165afa801561064957829061a110575b61a008915061f077565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761a0fb575b506022546001600160a01b0316803b15610654578180916024604051809481936301dbd4b760e31b8352600160048401525af180156106495761a0e6575b5050602254604051634a096d2b60e01b81526001600482015290602090829060249082906001600160a01b03165afa8015610649578290612db6576109f4915061f0d6565b8161a0f09161da4e565b61064657805f61a0a1565b8161a1059161da4e565b61064657805f61a063565b506020813d60201161a143575b8161a12a6020938361da4e565b81010312610a2a5761a13e61a0089161dc9b565b619ffe565b3d915061a11d565b503461064657806003193601126106465761a16461e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761a377575b506022546001600160a01b031661a1d461dc4e565b60208151910120813b1561091d57829160448392604051948593849263267d3d7b60e11b84526001600485015260248401525af180156106495761a362575b50505f51602062010a235f395f51905f523b156106465760405163248e63e160e11b8152819081818061a2486004820161dc31565b0381835f51602062010a235f395f51905f525af180156106495761a34d575b50507fb067f09a9e7faf3465d25720c4dca9d649ff583d8ac9a162dc1a2d205ae9b38e606061a29461dc4e565b6020815191012060405190600182526020820152426040820152a160225481906001600160a01b031661a2c561dc4e565b60208151910120813b1561091d57829160448392604051948593849263030d4a7760e21b84526001600485015260248401525af1801561064957611a765750505f51602062010a235f395f51905f523b15610646576040516390c5013b60e01b815281908181600481835f51602062010a235f395f51905f525af18015610649576106355750f35b8161a3579161da4e565b61064657805f61a267565b8161a36c9161da4e565b61064657805f61a213565b8161a3819161da4e565b61064657805f61a1bf565b503461064657806003193601126106465761a3a561e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761a54b575b506022546001600160a01b031661a4186112cb61db4d565b90803b1561091d5761a4598392918392604051948580948193632dc3f61760e11b83526001600484015283602484015260606044840152606483019061db6f565b03925af180156106495761a536575b5050602254604051631259673760e21b815260016004820152602481018390526001600160a01b0390911690602081604481855afa908115610a7f57839161a4f1575b5060449161a4ba60209261eeff565b60405192838092631259673760e21b825260016004830152600160248301525afa8015610649578290614561576109f4915061ef54565b90506020813d60201161a52e575b8161a50c6020938361da4e565b81010312610a735760449161a4ba61a52560209361dc9b565b9250509161a4ab565b3d915061a4ff565b8161a5409161da4e565b61064657805f61a468565b8161a5559161da4e565b61064657805f61a400565b503461064657806003193601126106465761a57961e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761aa61575b506022546001600160a01b031661a5e961e3a7565b90803b1561091d576040516377e4d4ad60e01b8152918391839182908490829061a616906004830161da6f565b03925af180156106495761aa4c575b506022546001600160a01b031661a63a61e40f565b90803b1561091d57604051635269237d60e11b8152918391839182908490829061a667906004830161dab6565b03925af180156106495761aa37575b506022546001600160a01b031661a68b61e46d565b813b1561091d576020606484928360405195869485936369b6533160e01b85526001600486015280516024860152015160448401525af180156106495761aa22575b506022546001600160a01b031661a6e261e49d565b90803b1561091d57604051630cc6160160e31b8152918391839182908490829061a70f906004830161dae7565b03925af180156106495761aa0d575b506022546001600160a01b031661a73361e4d7565b90803b1561091d57604051633608d1c360e11b8152918391839182908490829061a760906004830161db10565b03925af180156106495761a9f8575b506022546001600160a01b031661a7876112cb61dca8565b90803b1561091d5761a7c88392918392604051948580948193632dc3f61760e11b83526001600484015283602484015260606044840152606483019061db6f565b03925af180156106495761a9e3575b506022546001600160a01b031661a7ec61dccc565b60208151910120813b1561091d578290604051928391633927a4c360e01b83526001600484015260248301526060604483015281838161a82e6064820161dcf2565b03925af180156106495761a9ce575b50505f51602062010a235f395f51905f523b156106465760405163248e63e160e11b8152819081818061a8726004820161dc31565b0381835f51602062010a235f395f51905f525af180156106495761a9b9575b50507f15b18aed16ee0d775787b6594fcf556aec217e3e56f08178108d7ecbd5995c2b6040805160018152426020820152a160225481906001600160a01b0316803b156106545781809160246040518094819363fb4dcb8b60e01b8352600160048401525af180156106495761a9a4575b50505f51602062010a235f395f51905f523b15610646576040516390c5013b60e01b815281908181600481835f51602062010a235f395f51905f525af180156106495761a98f575b5050602254604051635037f17b60e01b81526001600482015290602090829060249082906001600160a01b03165afa8015610649578290616915576109f4915061f077565b8161a9999161da4e565b61064657805f61a94a565b8161a9ae9161da4e565b61064657805f61a902565b8161a9c39161da4e565b61064657805f61a891565b8161a9d89161da4e565b61064657805f61a83d565b8161a9ed9161da4e565b61064657805f61a7d7565b8161aa029161da4e565b61064657805f61a76f565b8161aa179161da4e565b61064657805f61a71e565b8161aa2c9161da4e565b61064657805f61a6cd565b8161aa419161da4e565b61064657805f61a676565b8161aa569161da4e565b61064657805f61a625565b8161aa6b9161da4e565b61064657805f61a5d4565b503461064657806003193601126106465760405160178054808352908352909160208301917fc624b66cc0138b8fabc209247f72d758e1cf3343756d543badbf24212bed8c15915b81811061aad55761234c856123408187038261da4e565b82546001600160a01b031684526020909301926001928301920161aabe565b503461064657806003193601126106465760405160188054808352908352909160208301917fb13d2d76d1f4b7be834882e410b3e3a8afaf69f83600ae24db354391d2378d2e915b81811061ab535761234c856123408187038261da4e565b82546001600160a01b031684526020909301926001928301920161ab3c565b503461064657806003193601126106465761ab8b61e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761af36575b506022546001600160a01b031661abfe6112cb61dca8565b90803b1561091d5761ac3f8392918392604051948580948193632dc3f61760e11b83526001600484015283602484015260606044840152606483019061db6f565b03925af180156106495761af21575b5060225460405163fe26d96560e01b8152600160048201526001600160a01b0390911690602081602481855afa8015610a7f5760ff91849161af02575b50166001810361ae94575b5060409061acc1825161aca9848261da4e565b60068152652a34b2b9101960d11b602082015261e53b565b90803b15613ef95761ad0284929183928551948580948193632dc3f61760e11b8352600160048401526001602484015260606044840152606483019061db6f565b03925af18015613ea65790839161ae7f575b5050602254815163fe26d96560e01b8152600160048201526001600160a01b0390911690602081602481855afa9081156141bc5761ad5d9160ff91869161ae4b575b501661e6cc565b61ad686112cb61dca8565b90803b15613ef95761ada884929183928551948580948193632dc3f61760e11b83526001600484015283602484015260606044840152606483019061db6f565b03925af18015613ea65790839161ae6a575b5050602254815163fe26d96560e01b81526001600482015290602090829060249082906001600160a01b03165afa908115613ea65761ae039160ff91859161ae4b57501661e6cc565b5f51602062010a235f395f51905f523b156106545780516390c5013b60e01b8152908282600481835f51602062010a235f395f51905f525af1908115612df157506106355750f35b61ae64915060203d602011614b0157614af3818361da4e565b5f61ad56565b8161ae749161da4e565b61065457815f61adba565b8161ae899161da4e565b61065457815f61ad14565b5f51602062010a235f395f51905f523b1561091d576040519063260a5b1560e21b825260048201526001602482015282816044815f51602062010a235f395f51905f525afa908115610a7f57839161aeed575b5061ac96565b8161aef79161da4e565b61065457815f61aee7565b61af1b915060203d602011614b0157614af3818361da4e565b5f61ac8b565b8161af2b9161da4e565b61064657805f61ac4e565b8161af409161da4e565b61064657805f61abe6565b503461064657806003193601126106465761af6461e2e4565b60205481906001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761b025575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b815263793e95df60e01b600482015281908181602481835f51602062010a235f395f51905f525af18015610649576116cb57506022546001600160a01b031661168a61dc4e565b8161b02f9161da4e565b61064657805f61afbc565b503461064657806003193601126106465761b05361e9b3565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761b758575b50505f51602062010a235f395f51905f523b1561064657604051633d21120560e21b815281908181600481835f51602062010a235f395f51905f525af180156106495761b743575b506022546001600160a01b031661b10b61e3a7565b90803b1561091d576040516377e4d4ad60e01b8152918391839182908490829061b138906004830161da6f565b03925af180156106495761b72e575b50505f51602062010a235f395f51905f523b1561064657604051633d21120560e21b815281908181600481835f51602062010a235f395f51905f525af180156106495761b719575b506022546001600160a01b031661b1a461e40f565b90803b1561091d57604051635269237d60e11b8152918391839182908490829061b1d1906004830161dab6565b03925af180156106495761b704575b50505f51602062010a235f395f51905f523b1561064657604051633d21120560e21b815281908181600481835f51602062010a235f395f51905f525af180156106495761b6ef575b506022546001600160a01b031661b23d61e46d565b813b1561091d576020606484928360405195869485936369b6533160e01b85526001600486015280516024860152015160448401525af180156106495761b6da575b50505f51602062010a235f395f51905f523b1561064657604051633d21120560e21b815281908181600481835f51602062010a235f395f51905f525af180156106495761b6c5575b506022546001600160a01b031661b2dc61e49d565b90803b1561091d57604051630cc6160160e31b8152918391839182908490829061b309906004830161dae7565b03925af180156106495761b6b0575b50505f51602062010a235f395f51905f523b1561064657604051633d21120560e21b815281908181600481835f51602062010a235f395f51905f525af180156106495761b69b575b506022546001600160a01b031661b37561e4d7565b90803b1561091d57604051633608d1c360e11b8152918391839182908490829061b3a2906004830161db10565b03925af180156106495761b686575b50505f51602062010a235f395f51905f523b1561064657604051633d21120560e21b815281908181600481835f51602062010a235f395f51905f525af180156106495761b671575b506022546001600160a01b031661b4116112cb61dee5565b90803b1561091d5761b4538392918392604051948580948193632dc3f61760e11b8352600160048401526001602484015260606044840152606483019061db6f565b03925af180156106495761b65c575b50505f51602062010a235f395f51905f523b1561064657604051633d21120560e21b815281908181600481835f51602062010a235f395f51905f525af180156106495761b647575b5060018060a01b036022541660409060016020835161b4c9858261da4e565b82815201600b60fb1b815220813b15613ef9578391604483928551948593849263267d3d7b60e11b84526001600485015260248401525af18015613ea65790839161b632575b50505f51602062010a235f395f51905f523b15610654578051633d21120560e21b81528281600481835f51602062010a235f395f51905f525af18015613ea65790839161b61d575b505060018060a01b036022541660016020835161b574858261da4e565b82815201600f60fb1b81522090803b15613ef9578251633927a4c360e01b8152918491839182908490829061b5ac906004830161dc07565b03925af18015613ea65790839161b608575b50505f51602062010a235f395f51905f523b156106545780516390c5013b60e01b8152908282600481835f51602062010a235f395f51905f525af1908115612df157506106355750f35b8161b6129161da4e565b61065457815f61b5be565b8161b6279161da4e565b61065457815f61b557565b8161b63c9161da4e565b61065457815f61b50f565b8161b6519161da4e565b61064657805f61b4aa565b8161b6669161da4e565b61064657805f61b462565b8161b67b9161da4e565b61064657805f61b3f9565b8161b6909161da4e565b61064657805f61b3b1565b8161b6a59161da4e565b61064657805f61b360565b8161b6ba9161da4e565b61064657805f61b318565b8161b6cf9161da4e565b61064657805f61b2c7565b8161b6e49161da4e565b61064657805f61b27f565b8161b6f99161da4e565b61064657805f61b228565b8161b70e9161da4e565b61064657805f61b1e0565b8161b7239161da4e565b61064657805f61b18f565b8161b7389161da4e565b61064657805f61b147565b8161b74d9161da4e565b61064657805f61b0f6565b8161b7629161da4e565b61064657805f61b0ae565b503461064657806003193601126106465761b78661e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761ba5a575b506022546001600160a01b031661b7f661de24565b60208151910120813b1561091d57829160a483926040519485938492633927a4c360e01b84526001600485015260248401526060604484015260046064840152637572693160e01b60848401525af180156106495761ba45575b50602254604051633bf365b160e01b8152600160048201526001600160a01b0390911690602081602481855afa908115610a7f57839161ba0d575b5061b8a59061b89861de24565b602081519101209061efa9565b61b8ad61de46565b60208151910120813b1561091d57829160a483926040519485938492633927a4c360e01b84526001600485015260248401526060604484015260046064840152633ab9349960e11b60848401525af180156106495761b9f8575b5050602254604051633bf365b160e01b8152600160048201526001600160a01b03909116908290602081602481865afa90811561064957829161b9c1575b509161b95560249361b89861de46565b6040516335ed308360e11b81526001600482015292839182905afa80156106495761962f91839161b9a7575b506040519061b99160408361da4e565b60048252633ab9349960e11b602083015261f005565b61b9bb91503d8085833e614198818361da4e565b5f61b981565b9150506020813d60201161b9f0575b8161b9dd6020938361da4e565b810103126126e85751829061b95561b945565b3d915061b9d0565b8161ba029161da4e565b61064657805f61b907565b9250506020823d60201161ba3d575b8161ba296020938361da4e565b810103126126e85761b8a58392519061b88b565b3d915061ba1c565b8161ba4f9161da4e565b61064657805f61b850565b8161ba649161da4e565b61064657805f61b7e1565b503461064657806003193601126106465761ba8861e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761bcc3575b506022546001600160a01b031661baf861e3a7565b90803b1561091d576040516377e4d4ad60e01b8152918391839182908490829061bb25906004830161da6f565b03925af180156106495761bcae575b506022546001600160a01b031661bb4961e40f565b90803b1561091d57604051635269237d60e11b8152918391839182908490829061bb76906004830161dab6565b03925af180156106495761bc99575b506022546001600160a01b031661bb9a61e46d565b813b1561091d576020606484928360405195869485936369b6533160e01b85526001600486015280516024860152015160448401525af180156106495761bc84575b506022546001600160a01b031661bbf161e49d565b90803b1561091d57604051630cc6160160e31b8152918391839182908490829061bc1e906004830161dae7565b03925af180156106495761bc6f575b506022546001600160a01b031661bc4261e4d7565b90803b1561091d57604051633608d1c360e11b8152918391839182908490829061201c906004830161db10565b8161bc799161da4e565b61064657805f61bc2d565b8161bc8e9161da4e565b61064657805f61bbdc565b8161bca39161da4e565b61064657805f61bb85565b8161bcb89161da4e565b61064657805f61bb34565b8161bccd9161da4e565b61064657805f61bae3565b503461064657806003193601126106465760205481906001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761bdf2575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b815263793e95df60e01b600482015281908181602481835f51602062010a235f395f51905f525af180156106495761bddd575b506022546021546001600160a01b039182169116813b1561091d57829160248392604051948593849263f770713b60e01b845260048401525af18015610649576106355750f35b8161bde79161da4e565b61064657805f61bd96565b8161bdfc9161da4e565b61064657805f61bd41565b503461064657806003193601126106465761be2061e2e4565b60205481906001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761bee1575b50505f51602062010a235f395f51905f523b1561064657604051630618f58760e51b815263793e95df60e01b600482015281908181602481835f51602062010a235f395f51905f525af1801561064957615ba157506022546001600160a01b0316611c6d61dccc565b8161beeb9161da4e565b61064657805f61be78565b5034610646578060031936011261064657601e5461bf138161dd19565b61bf20604051918261da4e565b818152601e83526020810191837f50bb669a95c7b50b7e8a6f09454034b2b14cf2b85c730dca9a539ca82cb6e350845b83831061c0245786858760405192839260208401906020855251809152604084019160408260051b8601019392815b83831061bf8c5786860387f35b919395509193603f198782030183528551906020604082019260018060a01b0381511683520151916040602083015282518091526060820190602060608260051b850101940192855b82811061bff95750505050506020806001929701930193019092869594929361bf7f565b909192939460208061c017600193605f19878203018952895161d860565b970195019392910161bfd5565b60405161c0308161d997565b82546001600160a01b0316815260018301805461c04c8161dd19565b9161c05a604051938461da4e565b8183528a526020808b20908b9084015b83821061c09057505050506001928260209283600295015281520192019201919061bf50565b60016020819261c09f8661dd58565b81520193019101909161c06a565b503461064657806003193601126106465761c0c661e2e4565b60405161c0d460808261da4e565b6003815260208101606036823761c0e961dc75565b602081519101209082511561c3675752604060076020825161c10b848261da4e565b8281520166546f626163636f60c81b81522082516001101561c367578183015260086020825161c13b848261da4e565b828152016743616e6e6162697360c01b81522082516002101561c367576060830152601f54839060081c6001600160a01b03165f51602062010a235f395f51905f523b15610a2a578251906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af18015612e0f5761c352575b505b825181101561c23b5760225484906001600160a01b031661c1da838661dd30565b51813b15610a73578291604483928751948593849263267d3d7b60e11b84526001600485015260248401525af1801561c2315761c21c575b505060010161c1b9565b8161c2269161da4e565b612e6157835f61c212565b84513d84823e3d90fd5b5091905f51602062010a235f395f51905f523b15610a2a5782516390c5013b60e01b81528281600481835f51602062010a235f395f51905f525af18015619a505790839161c33d575b5060225491926001600160a01b03909216915b835181101561c3395761c2aa818561dd30565b5185519063a75a047160e01b8252600160048301526024820152602081604481875afa90811561c32f57839161c2ee575b509061c2e860019261eeff565b0161c297565b90506020813d821161c327575b8161c3086020938361da4e565b81010312610a73579061c2e861c31f60019361dc9b565b91925061c2db565b3d915061c2fb565b86513d85823e3d90fd5b5080f35b8161c3479161da4e565b610a2a57815f61c284565b8161c35c9161da4e565b610a7357825f61c1b7565b634e487b7160e01b84526032600452602484fd5b503461064657806003193601126106465761c39461e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761c69c575b506022546001600160a01b0316803b15610654578180916024604051809481936301dbd4b760e31b8352600160048401525af180156106495761c687575b50506022546040516312514a9160e11b81526001600482015290602090829060249082906001600160a01b03165afa90811561064957829161c655575b50600a42018042116127335782905f51602062010a235f395f51905f523b15610a2a57604051906372eb5f8160e11b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761c640575b50601f5460081c6001600160a01b03165f51602062010a235f395f51905f523b15610a2a576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761c62b575b506022546001600160a01b0316803b15610a2a578180916024604051809481936301dbd4b760e31b8352600160048401525af180156106495761c616575b5050602254604051634a096d2b60e01b8152600160048201526001600160a01b039091169190602081602481865afa801561643f57849061c5db575b61c5a0915061ef54565b6040516312514a9160e11b815260016004820152602081602481865afa90811561643f57849161794d575060249261791c602092429061e8fa565b506020813d60201161c60e575b8161c5f56020938361da4e565b81010312612e615761c60961c5a09161dc9b565b61c596565b3d915061c5e8565b8161c6209161da4e565b610a2a57815f61c55a565b8161c6359161da4e565b610a2a57815f61c51c565b8161c64a9161da4e565b610a2a57815f61c4c2565b90506020813d60201161c67f575b8161c6706020938361da4e565b810103126126e857515f61c46a565b3d915061c663565b8161c6919161da4e565b61064657805f61c42d565b8161c6a69161da4e565b61064657805f61c3ef565b503461064657806003193601126106465761c6ca61e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761c767575b506022546001600160a01b031661c73a61e3a7565b90803b1561091d576040516377e4d4ad60e01b815291839183918290849082906183d7906004830161da6f565b8161c7719161da4e565b61064657805f61c725565b503461064657806003193601126106465760405160168054808352908352909160208301917fd833147d7dc355ba459fc788f669e58cfaf9dc25ddcd0702e87d69c7b5124289915b81811061c7db5761234c856123408187038261da4e565b82546001600160a01b031684526020909301926001928301920161c7c4565b503461064657806003193601126106465761c81361e2e4565b61c81b61dc75565b805160209190910120601f54829060081c6001600160a01b03165f51602062010a235f395f51905f523b15610a2a57604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761ca32575b506022546001600160a01b0316803b15610a2a5781809160446040518094819363267d3d7b60e11b8352600160048401528860248401525af180156106495761ca1d575b5060225460405163a75a047160e01b815260016004820152602481018490526001600160a01b0390911690602081604481855afa8015610a7f57839061c9e2575b61c90e915061eeff565b803b15610a2a5781809160446040518094819363267d3d7b60e11b8352600160048401528860248401525af180156106495761c9cd575b505060225460405163a75a047160e01b8152600160048201526024810192909252602090829060449082906001600160a01b03165afa801561064957829061c992575b61962f915061eeff565b506020813d60201161c9c5575b8161c9ac6020938361da4e565b81010312610a2a5761c9c061962f9161dc9b565b61c988565b3d915061c99f565b8161c9d79161da4e565b610a2a57815f61c945565b506020813d60201161ca15575b8161c9fc6020938361da4e565b81010312610a735761ca1061c90e9161dc9b565b61c904565b3d915061c9ef565b8161ca279161da4e565b610a2a57815f61c8c3565b8161ca3c9161da4e565b610a2a57815f61c87f565b503461064657806003193601126106465761ca6061e9b3565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761cb51575b50604051630a1f679b60e01b6020820152600160248201526024815261cae260448261da4e565b5f51602062010a235f395f51905f523b15610654578161cb1e916040518093819263f28dceb360e01b835260206004840152602483019061d860565b0381835f51602062010a235f395f51905f525af1801561064957610ba657506022546001600160a01b0316610b6561dc4e565b8161cb5b9161da4e565b61064657805f61cabb565b503461064657806003193601126106465761cb7f61e9b3565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761cc01575b506040516327cbff9960e11b60208201526001602482015260248152615ffc60448261da4e565b8161cc0b9161da4e565b61064657805f61cbda565b503461064657806003193601126106465761cc2f61e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761cd3b575b50505f51602062010a235f395f51905f523b156106465760405163248e63e160e11b8152819081818061ccbf6004820161dc31565b0381835f51602062010a235f395f51905f525af180156106495761cd26575b50507f7c8a63a0b6c9981e93eaaf88307b94e7a48a594d0350a605adf1cf9fcd8ec5536040805160018152426020820152a160225481906001600160a01b03166136e361e46d565b8161cd309161da4e565b61064657805f61ccde565b8161cd459161da4e565b61064657805f61cc8a565b503461064657806003193601126106465761cd6961e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b15610654576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761cfa8575b506022546001600160a01b031661cdd961e40f565b90803b1561091d57604051635269237d60e11b8152918391839182908490829061ce06906004830161dab6565b03925af180156106495761cf93575b50602254604051633b8ee43560e11b81526001600482015290608090829060249082906001600160a01b03165afa908115610649578283908492859461cf49575b5090615ceb61ce649261e5ec565b670de0b6b3a7640000810361ced4575b506105dc810361ce815750f35b5f51602062010a235f395f51905f523b15610654576040519063260a5b1560e21b825260048201526105dc602482015281816044815f51602062010a235f395f51905f525afa8015610649576106355750f35b5f51602062010a235f395f51905f523b1561091d576040519063260a5b1560e21b82526004820152670de0b6b3a7640000602482015282816044815f51602062010a235f395f51905f525afa908115610a7f57839161cf34575b5061ce74565b8161cf3e9161da4e565b61065457815f61cf2e565b93505050506080813d60801161cf8b575b8161cf676080938361da4e565b81010312610654578051602082015160408301516060909301519291615ceb61ce56565b3d915061cf5a565b8161cf9d9161da4e565b61064657805f61ce15565b8161cfb29161da4e565b61064657805f61cdc4565b5034610646578060031936011261064657601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761d10a575b5050604051906117ec91828101928184106001600160401b0385111761d0f657829382916200f2378339039082f080156164bc57602280546001600160a01b0319166001600160a01b03929092169182179055803b156106545781809160246040518094819363a3a1da7b60e01b8352603260048401525af1801561064957611a765750505f51602062010a235f395f51905f523b15610646576040516390c5013b60e01b815281908181600481835f51602062010a235f395f51905f525af18015610649576106355750f35b634e487b7160e01b83526041600452602483fd5b8161d1149161da4e565b61064657805f61d029565b503461064657806003193601126106465761d13861e2e4565b601f54819060081c6001600160a01b03165f51602062010a235f395f51905f523b1561065457604051906303223eab60e11b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761d6b3575b506022546001600160a01b031661d1a861e3a7565b90803b1561091d576040516377e4d4ad60e01b8152918391839182908490829061d1d5906004830161da6f565b03925af180156106495761d69e575b506022546001600160a01b031661d1f961e40f565b90803b1561091d57604051635269237d60e11b8152918391839182908490829061d226906004830161dab6565b03925af180156106495761d689575b506022546001600160a01b031661d24a61e46d565b813b1561091d576020606484928360405195869485936369b6533160e01b85526001600486015280516024860152015160448401525af180156106495761d674575b506022546001600160a01b031661d2a161e49d565b90803b1561091d57604051630cc6160160e31b8152918391839182908490829061d2ce906004830161dae7565b03925af180156106495761d65f575b506022546001600160a01b031661d2f261e4d7565b90803b1561091d57604051633608d1c360e11b8152918391839182908490829061d31f906004830161db10565b03925af180156106495761d64a575b506022546001600160a01b031661d3466112cb61db4d565b90803b1561091d5761d3878392918392604051948580948193632dc3f61760e11b83526001600484015283602484015260606044840152606483019061db6f565b03925af180156106495761d635575b506022546001600160a01b031661d3ab61dbe6565b6020815191012090803b1561091d57604051633927a4c360e01b8152918391839182908490829061d3df906004830161dc07565b03925af180156106495761d620575b50505f51602062010a235f395f51905f523b15610646576040516390c5013b60e01b815281908181600481835f51602062010a235f395f51905f525af180156106495761d60b575b50506022546040516312514a9160e11b81526001600482015290602090829060249082906001600160a01b03165afa90811561064957829161d5d9575b50600a42018042116127335782905f51602062010a235f395f51905f523b15610a2a57604051906372eb5f8160e11b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761d5c4575b50601f5460081c6001600160a01b03165f51602062010a235f395f51905f523b15610a2a576040519063ca669fa760e01b825260048201528181602481835f51602062010a235f395f51905f525af180156106495761d5af575b506022546001600160a01b0316803b15610a2a5781809160246040518094819363fb4dcb8b60e01b8352600160048401525af18015610649576179805750506022546040516312514a9160e11b8152600160048201526001600160a01b039091169190602081602481865afa90811561643f57849161794d575060249261791c602092429061e8fa565b8161d5b99161da4e565b610a2a57815f61d525565b8161d5ce9161da4e565b610a2a57815f61d4cb565b90506020813d60201161d603575b8161d5f46020938361da4e565b810103126126e857515f61d473565b3d915061d5e7565b8161d6159161da4e565b61064657805f61d436565b8161d62a9161da4e565b61064657805f61d3ee565b8161d63f9161da4e565b61064657805f61d396565b8161d6549161da4e565b61064657805f61d32e565b8161d6699161da4e565b61064657805f61d2dd565b8161d67e9161da4e565b61064657805f61d28c565b8161d6939161da4e565b61064657805f61d235565b8161d6a89161da4e565b61064657805f61d1e4565b8161d6bd9161da4e565b61064657805f61d193565b9050346126e8575f3660031901126126e857601f5460081c6001600160a01b03165f51602062010a235f395f51905f523b156126e85763ca669fa760e01b825260048201525f81602481835f51602062010a235f395f51905f525af1801561d8135761d800575b50604051631c077a6760e01b602082015260048152819061d75160248261da4e565b5f51602062010a235f395f51905f523b15610654578161d78d916040518093819263f28dceb360e01b835260206004840152602483019061d860565b0381835f51602062010a235f395f51905f525af180156106495761d7eb575b506022546001600160a01b0316803b156106545781809160246040518094819363f770713b60e01b83528160048401525af18015610649576106355750f35b8161d7f59161da4e565b61064657805f61d7ac565b61d80c91505f9061da4e565b5f5f61d72f565b6040513d5f823e3d90fd5b60206040818301928281528451809452019201905f5b81811061d8415750505090565b82516001600160a01b031684526020938401939092019160010161d834565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b90602080835192838152019201905f5b81811061d8a15750505090565b82516001600160e01b03191684526020938401939092019160010161d894565b602081016020825282518091526040820191602060408360051b8301019401925f915b83831061d8f357505050505090565b909192939460208061d911600193603f19868203018752895161d860565b9701930193019193929061d8e4565b602081016020825282518091526040820191602060408360051b8301019401925f915b83831061d95257505050505090565b909192939460208061d988600193603f198682030187526040838b51878060a01b0381511684520151918185820152019061d884565b9701930193019193929061d943565b604081019081106001600160401b0382111761d9b257604052565b634e487b7160e01b5f52604160045260245ffd5b60c081019081106001600160401b0382111761d9b257604052565b608081019081106001600160401b0382111761d9b257604052565b606081019081106001600160401b0382111761d9b257604052565b60a081019081106001600160401b0382111761d9b257604052565b61014081019081106001600160401b0382111761d9b257604052565b90601f801991011681019081106001600160401b0382111761d9b257604052565b91909160c060a060e0830194600184528051602085015260208101516040850152604081015160608501526060810151608085015260808101518285015201511515910152565b9190916080606060a08301946001845280516020850152602081015160408501526040810151828501520151910152565b919091606060406080830194600184528051602085015260208101518285015201511515910152565b91909160a0608060c08301946001845280516020850152602081015160408501526040810151606085015260608101511515828501520151910152565b6040519061db5c60408361da4e565b60048252632a34b2b960e11b6020830152565b906101208061db898451610140855261014085019061d860565b936020810151602085015260408101516040850152606081015160608501526080810151608085015260a081015160a085015260c081015160c085015260e081015160e08501526101008101516101008501520151151591015290565b6040519061dbf560408361da4e565b6003825262646f6360e81b6020830152565b60a09160018252602082015260606040820152600360608201526275726960e81b60808201520190565b906001606060808401938281525f60208201525f60408201520152565b6040519061dc5d60408361da4e565b6009825268496e6475737472794160b81b6020830152565b6040519061dc8460408361da4e565b600882526747616d626c696e6760c01b6020830152565b519081151582036126e857565b6040519061dcb760408361da4e565b600682526554696572203160d01b6020830152565b6040519061dcdb60408361da4e565b6008825267191bd8dd5b595b9d60c21b6020830152565b60148152730d2e0cce6745e5ee0ded8d2c6f288dec690c2e6d60631b602082015260400190565b6001600160401b03811161d9b25760051b60200190565b805182101561dd445760209160051b010190565b634e487b7160e01b5f52603260045260245ffd5b90604051915f8154908160011c926001831692831561de1a575b60208510841461de0657848752869390811561dde4575060011461dda0575b5061dd9e9250038361da4e565b565b90505f9291925260205f20905f915b81831061ddc857505090602061dd9e928201015f61dd91565b602091935080600191548385890101520191019091849261ddaf565b90506020925061dd9e94915060ff191682840152151560051b8201015f61dd91565b634e487b7160e01b5f52602260045260245ffd5b93607f169361dd72565b6040519061de3360408361da4e565b6004825263646f633160e01b6020830152565b6040519061de5560408361da4e565b60048252633237b19960e11b6020830152565b81601f820112156126e8578051906001600160401b03821161d9b2576040519261de9c601f8401601f19166020018561da4e565b828452602083830101116126e857815f9260208093018386015e8301015290565b906020828203126126e85781516001600160401b0381116126e85761dee2920161de68565b90565b6040519061def460408361da4e565b60028252612a1960f11b6020830152565b908160209103126126e8575160ff811681036126e85790565b6040519061df2d60408361da4e565b6002825261543160f01b6020830152565b91908260c09103126126e85781519160208101519160408201519160608101519161dee260a06080840151930161dc9b565b90604051918281549182825260208201905f5260205f20925f905b80600783011061e0cd5761dd9e94549181811061e0ae575b81811061e08f575b81811061e070575b81811061e051575b81811061e032575b81811061e013575b81811061dff6575b1061dfe1575b50038361da4e565b6001600160e01b03191681526020015f61dfd9565b602083811b6001600160e01b03191685529093019260010161dfd3565b604083901b6001600160e01b031916845260209093019260010161dfcb565b606083901b6001600160e01b031916845260209093019260010161dfc3565b608083901b6001600160e01b031916845260209093019260010161dfbb565b60a083901b6001600160e01b031916845260209093019260010161dfb3565b60c083901b6001600160e01b031916845260209093019260010161dfab565b60e083901b6001600160e01b031916845260209093019260010161dfa3565b916008919350610100600191865463ffffffff60e01b8160e01b16825263ffffffff60e01b8160c01b16602083015263ffffffff60e01b8160a01b16604083015263ffffffff60e01b8160801b16606083015263ffffffff60e01b8160601b16608083015263ffffffff60e01b8160401b1660a083015263ffffffff60e01b8160201b1660c083015263ffffffff60e01b1660e082015201940192018592939161df8b565b6040519061e18160408361da4e565b600c82526b283932b6b4bab6902a34b2b960a11b6020830152565b9190610140838203126126e8578251906001600160401b0382116126e85761e1c591840161de68565b9160208101519160408201519160608101519160808201519160a08101519160c08201519160e08101519161dee2610120610100840151930161dc9b565b60085460ff161561e21357600190565b604051630667f9d760e41b81525f51602062010a235f395f51905f5260048201526519985a5b195960d21b60248201526020816044815f51602062010a235f395f51905f525afa90811561d813575f9161e26e575b50151590565b90506020813d60201161e298575b8161e2896020938361da4e565b810103126126e857515f61e268565b3d915061e27c565b6040519061e2af60408361da4e565b6007825266155c19185d195960ca1b6020830152565b908160209103126126e857516001600160a01b03811681036126e85790565b601f545f905f51602062010a235f395f51905f523b156126e85760405163ca669fa760e01b815260089190911c6001600160a01b031660048201525f81602481835f51602062010a235f395f51905f525af1801561d8135761e394575b506022546001600160a01b0316803b15610a2a578180916024604051809481936304bd12bb60e01b8352600160048401525af180156106495761e382575050565b61e38d82809261da4e565b6106465750565b61e3a091505f9061da4e565b5f5f61e341565b5f60a060405161e3b68161d9c6565b828152826020820152826040820152826060820152826080820152015260405161e3df8161d9c6565b629896808152620f424060208201526302faf080604082015260b460608201525f6080820152600160a082015290565b5f606060405161e41e8161d9e1565b828152826020820152826040820152015260405161e43b8161d9e1565b673782dace9d9000008152671bc16d674ec800006020820152670de0b6b3a764000060408201526105dc606082015290565b5f602060405161e47c8161d997565b828152015260405161e48d8161d997565b6103e88152610bb8602082015290565b5f6040805161e4ab8161d9fc565b828152826020820152015260405161e4c28161d9fc565b605a815260b460208201526001604082015290565b5f608060405161e4e68161da17565b828152826020820152826040820152826060820152015260405161e5098161da17565b673782dace9d9000008152671bc16d674ec8000060208201526298968060408201525f6060820152605a608082015290565b5f61012060405161e54b8161da32565b606081528260208201528260408201528260608201528260808201528260a08201528260c08201528260e08201528261010082015201526040519061e58f8261da32565b81526298968060208201526302faf0806040820152620f424060608201526729a2241af62c00006080820152671bc16d674ec8000060a082015261032060c0820152606460e082015261016d610100820152600161012082015290565b673782dace9d900000810361e5fe5750565b5f51602062010a235f395f51905f523b156126e8576040519063260a5b1560e21b82526004820152673782dace9d90000060248201525f816044815f51602062010a235f395f51905f525afa801561d8135761e6575750565b5f61dd9e9161da4e565b671bc16d674ec80000810361e6735750565b5f51602062010a235f395f51905f523b156126e8576040519063260a5b1560e21b82526004820152671bc16d674ec8000060248201525f816044815f51602062010a235f395f51905f525afa801561d8135761e6575750565b6002810361e6d75750565b5f51602062010a235f395f51905f523b156126e8576040519063260a5b1560e21b82526004820152600260248201525f816044815f51602062010a235f395f51905f525afa801561d8135761e6575750565b6006810361e7345750565b5f51602062010a235f395f51905f523b156126e8576040519063260a5b1560e21b82526004820152600660248201525f816044815f51602062010a235f395f51905f525afa801561d8135761e6575750565b8061e78e5750565b5f51602062010a235f395f51905f523b156126e8576040519063260a5b1560e21b825260048201525f60248201525f816044815f51602062010a235f395f51905f525afa801561d8135761e6575750565b62989680810361e7ec5750565b5f51602062010a235f395f51905f523b156126e8576040519063260a5b1560e21b825260048201526298968060248201525f816044815f51602062010a235f395f51905f525afa801561d8135761e6575750565b605a810361e84b5750565b5f51602062010a235f395f51905f523b156126e8576040519063260a5b1560e21b82526004820152605a60248201525f816044815f51602062010a235f395f51905f525afa801561d8135761e6575750565b60b4810361e8a85750565b5f51602062010a235f395f51905f523b156126e8576040519063260a5b1560e21b8252600482015260b460248201525f816044815f51602062010a235f395f51905f525afa801561d8135761e6575750565b9080820361e906575050565b5f51602062010a235f395f51905f523b156126e8576040519163260a5b1560e21b8352600483015260248201525f816044815f51602062010a235f395f51905f525afa801561d8135761e6575750565b908082111561e963575050565b5f51602062010a235f395f51905f523b156126e85760405191636d83fe6960e11b8352600483015260248201525f816044815f51602062010a235f395f51905f525afa801561d8135761e6575750565b601f545f905f51602062010a235f395f51905f523b156126e85760405163ca669fa760e01b815260089190911c6001600160a01b031660048201525f81602481835f51602062010a235f395f51905f525af1801561d8135761eeec575b506022546001600160a01b0316803b15610a2a578180916024604051809481936304bd12bb60e01b8352600160048401525af180156106495761eed7575b5050601f545f905f51602062010a235f395f51905f523b156126e8576040516303223eab60e11b815260089190911c6001600160a01b031660048201525f81602481835f51602062010a235f395f51905f525af1801561d8135761eec4575b506022546001600160a01b031661eac261e3a7565b813b15610a735761eaec839283926040519485809481936377e4d4ad60e01b83526004830161da6f565b03925af180156106495790829161eeaf575b50506022546001600160a01b031661eb1461e40f565b813b15610a735761eb3e83928392604051948580948193635269237d60e11b83526004830161dab6565b03925af180156106495790829161ee9a575b50506022546001600160a01b031661eb6661e46d565b813b15610a73576020606484928360405195869485936369b6533160e01b85526001600486015280516024860152015160448401525af180156106495790829161ee85575b50506022546001600160a01b031661ebc161e49d565b813b15610a735761ebeb83928392604051948580948193630cc6160160e31b83526004830161dae7565b03925af180156106495790829161ee70575b50506022546001600160a01b031661ec1361e4d7565b813b15610a735761ec3d83928392604051948580948193633608d1c360e11b83526004830161db10565b03925af180156106495790829161ee5b575b50506022546001600160a01b031661ec686112cb61dca8565b813b15610a735761eca783928392604051948580948193632dc3f61760e11b83526001600484015283602484015260606044840152606483019061db6f565b03925af180156106495790829161ee46575b50506022546001600160a01b031661eccf61dccc565b60208151910120813b15610a73578290604051928391633927a4c360e01b83526001600484015260248301526060604483015281838161ed116064820161dcf2565b03925af180156106495790829161ee31575b50505f51602062010a235f395f51905f523b15610646576040516390c5013b60e01b81528181600481835f51602062010a235f395f51905f525af180156106495761ee1c575b5050601f545f905f51602062010a235f395f51905f523b156126e85760405163ca669fa760e01b815260089190911c6001600160a01b031660048201525f81602481835f51602062010a235f395f51905f525af1801561d8135761ee09575b506022546001600160a01b0316803b15610a2a5781809160246040518094819363fb4dcb8b60e01b8352600160048401525af180156106495761e382575050565b61ee1591505f9061da4e565b5f5f61edc8565b61ee2782809261da4e565b610646578061ed69565b8161ee3b9161da4e565b61064657805f61ed23565b8161ee509161da4e565b61064657805f61ecb9565b8161ee659161da4e565b61064657805f61ec4f565b8161ee7a9161da4e565b61064657805f61ebfd565b8161ee8f9161da4e565b61064657805f61ebab565b8161eea49161da4e565b61064657805f61eb50565b8161eeb99161da4e565b61064657805f61eafe565b61eed091505f9061da4e565b5f5f61eaad565b61eee282809261da4e565b610646578061ea4e565b61eef891505f9061da4e565b5f5f61ea10565b158061ef085750565b5f51602062010a235f395f51905f523b156126e857604051630c9fd58160e01b8152901560048201525f816024815f51602062010a235f395f51905f525afa801561d8135761e6575750565b8061ef5c5750565b5f51602062010a235f395f51905f523b156126e85760405163a598288560e01b815290151560048201525f816024815f51602062010a235f395f51905f525afa801561d8135761e6575750565b9080820361efb5575050565b5f51602062010a235f395f51905f523b156126e85760405191637c84c69b60e01b8352600483015260248201525f816044815f51602062010a235f395f51905f525afa801561d8135761e6575750565b5f51602062010a235f395f51905f523b156126e85761f0455f9161f057604051948593849363f320d96360e01b855260406004860152604485019061d860565b8381036003190160248501529061d860565b03815f51602062010a235f395f51905f525afa801561d8135761e6575750565b15156001810361f0845750565b5f51602062010a235f395f51905f523b156126e8576040519063f7fe347760e01b82526004820152600160248201525f816044815f51602062010a235f395f51905f525afa801561d8135761e6575750565b15158061f0e05750565b5f51602062010a235f395f51905f523b156126e8576040519063f7fe347760e01b825260048201525f60248201525f816044815f51602062010a235f395f51905f525afa801561d8135761e6575750565b601f545f905f51602062010a235f395f51905f523b156126e85760405163ca669fa760e01b815260089190911c6001600160a01b031660048201525f81602481835f51602062010a235f395f51905f525af1801561d8135761ee0957506022546001600160a01b0316803b15610a2a5781809160246040518094819363fb4dcb8b60e01b8352600160048401525af180156106495761e382575050565b6001600160a01b03908116911680820361f1e6575050565b5f51602062010a235f395f51905f523b156126e857604051916328a9b0fb60e11b8352600483015260248201525f816044815f51602062010a235f395f51905f525afa801561d8135761e657575056fe608080604052346026575f80546001600160a01b031916331790556117c1908161002b8239f35b5f80fdfe60806040526004361015610011575f80fd5b5f3560e01c806304bd12bb1461150d5780630c3529dc1461146e5780630edea5b8146113f857806324a29522146113ce57806328f4ca31146113735780633927a4c31461114c5780633bf365b11461112257806349659cdc146106bb5780634a096d2b146104ea5780634ae8d21a146110f35780634c2d62b714610fec5780634cfa7af61461103d5780634d4f71771461101b5780635037f17b14610fec57806358e5189614610fc55780635b87ec2e14610c995780635bffd88f14610bd7578063634a1cd414610ba85780636630b00814610ad857806369b6533114610a315780636a58fc3014610a025780636bda6106146109c05780636c11a386146108df5780636c2034ca14610899578063771dc86a1461084d57806377e4d4ad146107655780637a861adb146106ff5780638b624b10146106bb57806390ff8adf1461068c578063a3a1da7b146105ff578063a4d246fa14610548578063a75a0471146103d2578063b632d57c14610519578063bd8afa46146104ea578063d402ab27146104b7578063d9e5c35d14610488578063f770713b14610406578063fa4f5a86146103d2578063fb4dcb8b1461023c578063fe26d9651461020f5763feca4699146101dc575f80fd5b3461020b57602036600319011261020b576004355f526010602052602060ff60405f2054166040519015158152f35b5f80fd5b3461020b57602036600319011261020b576004355f526008602052602060ff60405f205416604051908152f35b3461020b57602036600319011261020b5760043561025861170c565b6102618161172e565b805f52600260205260ff60405f2054166103c057805f52600360205260ff60405f205416156103ae57805f52601060205260ff60405f205416158015610397575b8015610380575b8015610369575b8015610352575b801561033b575b61032957805f52600e60205260405f205415610329576040817f15b18aed16ee0d775787b6594fcf556aec217e3e56f08178108d7ecbd5995c2b925f526002602052815f20600160ff19825416179055805f52600460205242825f20558151908152426020820152a1005b63111e73bd60e01b5f5260045260245ffd5b50805f52601560205260ff60405f205416156102be565b50805f52601460205260ff60405f205416156102b7565b50805f52601360205260ff60405f205416156102b0565b50805f52601260205260ff60405f205416156102a9565b50805f52601160205260ff60405f205416156102a2565b634b52888f60e01b5f5260045260245ffd5b6327cbff9960e11b5f5260045260245ffd5b3461020b576103e0366115cf565b905f52600b60205260405f20905f52602052602060ff60405f2054166040519015158152f35b3461020b57602036600319011261020b576004356001600160a01b0381169081900361020b5761043461170c565b8015610479575f80546001600160a01b031916821790556040519081527f48165597506564c23e384fde61cf1f216591bca2c8a1ce0bbb2153d4c3d8ebc490602090a1005b631c077a6760e01b5f5260045ffd5b3461020b57602036600319011261020b576004355f526013602052602060ff60405f2054166040519015158152f35b3461020b57602036600319011261020b576004355f52600a6020526040805f206001815491015482519182526020820152f35b3461020b57602036600319011261020b576004355f526003602052602060ff60405f2054166040519015158152f35b3461020b57602036600319011261020b576004355f526011602052602060ff60405f2054166040519015158152f35b3461020b5760a036600319011261020b57600435608036602319011261020b5760407f26a7b1d1892f9b115a55617a38a1bbf216b66c1703ee89cebc5c83725da2f9249161059461170c565b61059d8161172e565b6105a681611744565b805f526006602052815f206024358155604435600182015560643560028201556003608435910155805f52600460205242825f2055805f526011602052815f20600160ff198254161790558151908152426020820152a1005b3461020b57602036600319011261020b5760043560ff81169081810361020b5761062761170c565b60ff8214610679575f805460ff60a01b191660a09290921b60ff60a01b169190911790556040519081527f8039ca5e7ab280894dd980ce72fff4672de58cbe4219cee5da6059ab85db289190602090a1005b506342e5795760e01b5f5260045260245ffd5b3461020b57602036600319011261020b576004355f526012602052602060ff60405f2054166040519015158152f35b3461020b57604036600319011261020b576106d46115e5565b6004355f52600960205260ff60405f2091165f52602052602060ff60405f2054166040519015158152f35b3461020b57602036600319011261020b576004355f52600560205260c060405f20805490600181015490600281015460038201549060ff6005600485015494015416936040519586526020860152604085015260608401526080830152151560a0820152f35b3461020b5760e036600319011261020b5760043560c036602319011261020b5761078d61170c565b6107968161172e565b61079f81611744565b805f52600560205260405f2090602435825560443560018301556064356002830155608435600383015560a435600483015560c43590811515820361020b5761081c8260057f6a50b7174b84444ee4fc852f30eb4d5105a85e60b12b831224dc562daabc3dcd9560409550019060ff801983541691151516179055565b805f52600460205242825f2055805f526010602052815f20600160ff198254161790558151908152426020820152a1005b3461020b57602036600319011261020b576004355f526006602052608060405f208054906001810154906003600282015491015491604051938452602084015260408301526060820152f35b3461020b57602036600319011261020b576004355f52600c602052606060405f2080549060ff600260018301549201541690604051928352602083015215156040820152f35b3461020b5760c036600319011261020b5760043560a036602319011261020b5761090761170c565b6109108161172e565b61091981611744565b805f52600d60205260405f209060243582556044356001830155606435600283015560843590811515820361020b577f9638a3519a3fc3e7d5c01014e107171b238d1bfed1c6b85b472e1826a1cfc6d6926109878360409450600383019060ff801983541691151516179055565b600460a435910155805f52600460205242825f2055805f526014602052815f20600160ff198254161790558151908152426020820152a1005b3461020b57602036600319011261020b576004355f52600f6020526109fe6109ea60405f2061162d565b6040519182916020835260208301906116e8565b0390f35b3461020b57602036600319011261020b576004355f526015602052602060ff60405f2054166040519015158152f35b3461020b57606036600319011261020b57600435604036602319011261020b5760407f7c8a63a0b6c9981e93eaaf88307b94e7a48a594d0350a605adf1cf9fcd8ec55391610a7d61170c565b610a868161172e565b610a8f81611744565b805f52600a602052815f2060243581556001604435910155805f52600460205242825f2055805f526012602052815f20600160ff198254161790558151908152426020820152a1005b3461020b57608036600319011261020b57600435606036602319011261020b57610b0061170c565b610b098161172e565b610b1281611744565b805f52600c60205260405f20906024358255604435600183015560643590811515820361020b57610b778260027fdbb6d31475bec9849fbf352a7c353cdf096d6e2d972cf78bba644a80269dd37b9560409550019060ff801983541691151516179055565b805f52600460205242825f2055805f526013602052815f20600160ff198254161790558151908152426020820152a1005b3461020b57602036600319011261020b576004355f526014602052602060ff60405f2054166040519015158152f35b3461020b57604036600319011261020b57610bf06115e5565b6004355f52600760205260ff60405f2091165f52602052610c6360405f20610c178161162d565b9060018101549060028101549060038101546004820154600583015460068401549160078501549360ff6009600888015497015416966040519a8b9a6101408c526101408c01906116e8565b9860208b015260408a01526060890152608088015260a087015260c086015260e085015261010084015215156101208301520390f35b3461020b57606036600319011261020b57600435610cb56115e5565b9060443567ffffffffffffffff811161020b578036039061014060031983011261020b57610ce161170c565b610cea8361172e565b610cf383611744565b60ff805f5460a01c16941693841015610fb257825f52600760205260405f20845f5260205260405f20918160040135906022190181121561020b57810160048101359067ffffffffffffffff821161020b57813603602482011361020b57610d5b84546115f5565b601f8111610f61575b505f90601f8311600114610ef2576101249392915f9183610ee4575b50508160011b915f199060031b1c19161783555b6024810135600184015560448101356002840155606481013560038401556084810135600484015560a4810135600584015560c4810135600684015560e4810135600784015561010481013560088401550135801515810361020b576009610e0892019060ff801983541691151516179055565b805f52600960205260405f20825f5260205260405f20600160ff19825416179055805f52600860205260ff60405f205416821015610e9f575b807f9c889edde3e184915aa8758beda13d0b548decc0b5a79f3b22ffa3d9d57d0ab2926060925f52601560205260405f20600160ff19825416179055815f5260046020524260405f20556040519182526020820152426040820152a1005b600182019060ff8211610ed0575f818152600860205260409020805460ff191660ff90931692909217909155610e41565b634e487b7160e01b5f52601160045260245ffd5b016024013590508780610d80565b601f19831691855f5260205f20925f5b818110610f46575091600193918561012497969410610f29575b505050811b018355610d94565b6024910101355f19600384901b60f8161c19169055878080610f1c565b60248484010135855560019094019360209283019201610f02565b82811115610d6457845f5260205f20601f840160051c9060208510610faa575b81601f9101920160051c03905f5b828110610f9d575050610d64565b5f82820155600101610f8f565b5f9150610f81565b836342e5795760e01b5f5260045260245ffd5b3461020b575f36600319011261020b575f546040516001600160a01b039091168152602090f35b3461020b57602036600319011261020b576004355f526002602052602060ff60405f2054166040519015158152f35b3461020b575f36600319011261020b57602060ff5f5460a01c16604051908152f35b3461020b5761104b366115cf565b9061105461170c565b61105d8161172e565b61106681611744565b81156110e4577f1210d3ecd972f25e1e2251627ec83fb00cb0e435dbe0c5abadf32a9e50ee9f3691815f52600b60205260405f20815f5260205260405f20600160ff19825416179055815f5260046020524260405f20556110df6040519283924291846040919493926060820195825260208201520152565b0390a1005b63036d8cb960e61b5f5260045ffd5b3461020b57602036600319011261020b576004355f526001602052602060ff60405f2054166040519015158152f35b3461020b57602036600319011261020b576004355f52600e602052602060405f2054604051908152f35b3461020b57606036600319011261020b5760043560243560443567ffffffffffffffff811161020b573660238201121561020b5780600401359067ffffffffffffffff821161020b57366024838301011161020b576111a961170c565b6111b28461172e565b6111bb84611744565b835f52600e6020528260405f2055835f52600f60205260405f206111df81546115f5565b601f8111611322575b505f601f8411600114611291579260247f6ac7bb36990be20afe8d2777e03a1c2684a4589a514d45a4d6f77e5371aafda5969382938360a0975f91611284575b508460011b905f198660031b1c19161790555b845f5260046020524260405f2055604051968795865260208601526080604086015282608086015201848401375f828201840152426060830152601f01601f19168101030190a1005b849150830101358a611228565b601f19841690825f5260205f20915f5b8181106113075750938593849360249360a0987f6ac7bb36990be20afe8d2777e03a1c2684a4589a514d45a4d6f77e5371aafda59b98106112ec575b5050600184811b01905561123b565b83018401355f19600387901b60f8161c1916905589806112dd565b91926020600181926024878a010135815501940192016112a1565b838111156111e857815f5260205f20601f850160051c906020861061136b575b81601f9101920160051c03905f5b82811061135e5750506111e8565b5f82820155600101611350565b5f9150611342565b3461020b57602036600319011261020b576004355f52600d60205260a060405f208054906001810154906002810154600460ff6003840154169201549260405194855260208501526040840152151560608301526080820152f35b3461020b57602036600319011261020b576004355f526004602052602060405f2054604051908152f35b3461020b57602036600319011261020b577f644f3bc1a6ec9d9bf253b21949e5669036171733d6566a3bbe54f02cd479700b604060043561143761170c565b6114408161172e565b805f526003602052815f2060ff198154169055805f52600460205242825f20558151908152426020820152a1005b3461020b5761147c366115cf565b9061148561170c565b61148e8161172e565b61149781611744565b81156110e4577fb067f09a9e7faf3465d25720c4dca9d649ff583d8ac9a162dc1a2d205ae9b38e91815f52600b60205260405f20815f5260205260405f2060ff198154169055815f5260046020524260405f20556110df6040519283924291846040919493926060820195825260208201520152565b3461020b57602036600319011261020b5760043561152961170c565b80156115c057805f52600160205260ff60405f2054166115ae576040817f0d28ab2dec81aaebf86915a865353a44c9779fa1c6158a6ff748dc8e14842885925f526001602052815f20600160ff19825416179055805f526003602052815f20600160ff19825416179055805f52600460205242825f20558151908152426020820152a1005b6362e01ad560e11b5f5260045260245ffd5b6362f4a20760e01b5f5260045ffd5b604090600319011261020b576004359060243590565b6024359060ff8216820361020b57565b90600182811c92168015611623575b602083101461160f57565b634e487b7160e01b5f52602260045260245ffd5b91607f1691611604565b90604051915f90805490611640826115f5565b80865291600181169081156116ca5750600114611692575b5050829003601f01601f1916820167ffffffffffffffff81118382101761167e57604052565b634e487b7160e01b5f52604160045260245ffd5b9091505f5260205f205f905b8282106116b45750602091508301015f80611658565b600181602092548385890101520191019061169e565b9150506020925060ff191682850152151560051b8301015f80611658565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b5f546001600160a01b0316330361171f57565b63793e95df60e01b5f5260045ffd5b5f52600160205260ff60405f205416156115c057565b805f52600260205260ff60405f2054168015611774575b6117625750565b630a1f679b60e01b5f5260045260245ffd5b50805f52600360205260ff60405f2054161561175b56fea26469706673582212207cf62a015fb4ef13a4770395702ec6950ba1d2fdc723171d262d2b30800ea51d64736f6c634300082100330000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da2646970667358221220247e1686b2fa8f140d3dabae18659011bfc0a36a7e443f953e7c8cd96abbdeaa64736f6c634300082100330000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12d"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TestCreditPolicy:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[TestCreditPolicy]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, TestCreditPolicy, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[TestCreditPolicy]]:
        return cls._deploy(request_type, [], return_tx, TestCreditPolicy, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#12)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#12)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#12)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#12)
        """
        ...

    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#12)
        """
        return self._execute(self.chain, request_type, "0a9254e4", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testCreatePolicyRevertIfOwnerIsNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#147)
        """
        ...

    @overload
    def testCreatePolicyRevertIfOwnerIsNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#147)
        """
        ...

    @overload
    def testCreatePolicyRevertIfOwnerIsNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#147)
        """
        ...

    @overload
    def testCreatePolicyRevertIfOwnerIsNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#147)
        """
        ...

    def testCreatePolicyRevertIfOwnerIsNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#147)
        """
        return self._execute(self.chain, request_type, "da69aca6", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testCreatePolicyRevertsIfVersionIsZero(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#153)
        """
        ...

    @overload
    def testCreatePolicyRevertsIfVersionIsZero(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#153)
        """
        ...

    @overload
    def testCreatePolicyRevertsIfVersionIsZero(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#153)
        """
        ...

    @overload
    def testCreatePolicyRevertsIfVersionIsZero(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#153)
        """
        ...

    def testCreatePolicyRevertsIfVersionIsZero(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#153)
        """
        return self._execute(self.chain, request_type, "acc435db", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testCreatePolicyRevertsIfVersionExists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#159)
        """
        ...

    @overload
    def testCreatePolicyRevertsIfVersionExists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#159)
        """
        ...

    @overload
    def testCreatePolicyRevertsIfVersionExists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#159)
        """
        ...

    @overload
    def testCreatePolicyRevertsIfVersionExists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#159)
        """
        ...

    def testCreatePolicyRevertsIfVersionExists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#159)
        """
        return self._execute(self.chain, request_type, "f5970843", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testCreatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#171)
        """
        ...

    @overload
    def testCreatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#171)
        """
        ...

    @overload
    def testCreatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#171)
        """
        ...

    @overload
    def testCreatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#171)
        """
        ...

    def testCreatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#171)
        """
        return self._execute(self.chain, request_type, "60599a8c", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testMultiplePolicyVersions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#183)
        """
        ...

    @overload
    def testMultiplePolicyVersions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#183)
        """
        ...

    @overload
    def testMultiplePolicyVersions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#183)
        """
        ...

    @overload
    def testMultiplePolicyVersions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#183)
        """
        ...

    def testMultiplePolicyVersions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#183)
        """
        return self._execute(self.chain, request_type, "975c81fc", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testPolicyVersionIsolation(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#195)
        """
        ...

    @overload
    def testPolicyVersionIsolation(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#195)
        """
        ...

    @overload
    def testPolicyVersionIsolation(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#195)
        """
        ...

    @overload
    def testPolicyVersionIsolation(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#195)
        """
        ...

    def testPolicyVersionIsolation(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#195)
        """
        return self._execute(self.chain, request_type, "5db3ffd0", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testDeactivatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#212)
        """
        ...

    @overload
    def testDeactivatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#212)
        """
        ...

    @overload
    def testDeactivatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#212)
        """
        ...

    @overload
    def testDeactivatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#212)
        """
        ...

    def testDeactivatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#212)
        """
        return self._execute(self.chain, request_type, "45ddfad4", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testDeactivatePolicyRevertIfOwnerIsNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#222)
        """
        ...

    @overload
    def testDeactivatePolicyRevertIfOwnerIsNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#222)
        """
        ...

    @overload
    def testDeactivatePolicyRevertIfOwnerIsNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#222)
        """
        ...

    @overload
    def testDeactivatePolicyRevertIfOwnerIsNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#222)
        """
        ...

    def testDeactivatePolicyRevertIfOwnerIsNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#222)
        """
        return self._execute(self.chain, request_type, "d306feec", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testDeactivatePolicyRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#229)
        """
        ...

    @overload
    def testDeactivatePolicyRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#229)
        """
        ...

    @overload
    def testDeactivatePolicyRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#229)
        """
        ...

    @overload
    def testDeactivatePolicyRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#229)
        """
        ...

    def testDeactivatePolicyRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#229)
        """
        return self._execute(self.chain, request_type, "726b51f3", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testDeactivateUpdatesLastUpdated(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#235)
        """
        ...

    @overload
    def testDeactivateUpdatesLastUpdated(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#235)
        """
        ...

    @overload
    def testDeactivateUpdatesLastUpdated(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#235)
        """
        ...

    @overload
    def testDeactivateUpdatesLastUpdated(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#235)
        """
        ...

    def testDeactivateUpdatesLastUpdated(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#235)
        """
        return self._execute(self.chain, request_type, "71cb19db", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testDeactivatePolicyIsIdempotent(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#247)
        """
        ...

    @overload
    def testDeactivatePolicyIsIdempotent(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#247)
        """
        ...

    @overload
    def testDeactivatePolicyIsIdempotent(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#247)
        """
        ...

    @overload
    def testDeactivatePolicyIsIdempotent(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#247)
        """
        ...

    def testDeactivatePolicyIsIdempotent(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#247)
        """
        return self._execute(self.chain, request_type, "2756bfb1", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateRevertsIfPolicyInactive(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#264)
        """
        ...

    @overload
    def testUpdateRevertsIfPolicyInactive(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#264)
        """
        ...

    @overload
    def testUpdateRevertsIfPolicyInactive(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#264)
        """
        ...

    @overload
    def testUpdateRevertsIfPolicyInactive(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#264)
        """
        ...

    def testUpdateRevertsIfPolicyInactive(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#264)
        """
        return self._execute(self.chain, request_type, "e288ed39", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFreezePolicyUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#283)
        """
        ...

    @overload
    def testFreezePolicyUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#283)
        """
        ...

    @overload
    def testFreezePolicyUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#283)
        """
        ...

    @overload
    def testFreezePolicyUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#283)
        """
        ...

    def testFreezePolicyUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#283)
        """
        return self._execute(self.chain, request_type, "3fafa9f1", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFreezePolicyRevertIfOwnerIsNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#304)
        """
        ...

    @overload
    def testFreezePolicyRevertIfOwnerIsNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#304)
        """
        ...

    @overload
    def testFreezePolicyRevertIfOwnerIsNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#304)
        """
        ...

    @overload
    def testFreezePolicyRevertIfOwnerIsNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#304)
        """
        ...

    def testFreezePolicyRevertIfOwnerIsNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#304)
        """
        return self._execute(self.chain, request_type, "fe5bc5ab", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFreezePolicyRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#311)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#311)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#311)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#311)
        """
        ...

    def testFreezePolicyRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#311)
        """
        return self._execute(self.chain, request_type, "c02f6bad", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFreezePolicyReverstIfPolicyIsNotActive(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#317)
        """
        ...

    @overload
    def testFreezePolicyReverstIfPolicyIsNotActive(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#317)
        """
        ...

    @overload
    def testFreezePolicyReverstIfPolicyIsNotActive(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#317)
        """
        ...

    @overload
    def testFreezePolicyReverstIfPolicyIsNotActive(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#317)
        """
        ...

    def testFreezePolicyReverstIfPolicyIsNotActive(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#317)
        """
        return self._execute(self.chain, request_type, "9b8fa079", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFreezePolicyRevertsIfAlreadyFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#329)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfAlreadyFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#329)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfAlreadyFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#329)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfAlreadyFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#329)
        """
        ...

    def testFreezePolicyRevertsIfAlreadyFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#329)
        """
        return self._execute(self.chain, request_type, "12ea585c", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFreezePolicyMarksPolicyAsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#339)
        """
        ...

    @overload
    def testFreezePolicyMarksPolicyAsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#339)
        """
        ...

    @overload
    def testFreezePolicyMarksPolicyAsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#339)
        """
        ...

    @overload
    def testFreezePolicyMarksPolicyAsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#339)
        """
        ...

    def testFreezePolicyMarksPolicyAsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#339)
        """
        return self._execute(self.chain, request_type, "6b67668c", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFreezeUpdatesLastUpdated(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#359)
        """
        ...

    @overload
    def testFreezeUpdatesLastUpdated(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#359)
        """
        ...

    @overload
    def testFreezeUpdatesLastUpdated(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#359)
        """
        ...

    @overload
    def testFreezeUpdatesLastUpdated(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#359)
        """
        ...

    def testFreezeUpdatesLastUpdated(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#359)
        """
        return self._execute(self.chain, request_type, "0a7a69b8", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFreezeDoesNotDeactivatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#382)
        """
        ...

    @overload
    def testFreezeDoesNotDeactivatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#382)
        """
        ...

    @overload
    def testFreezeDoesNotDeactivatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#382)
        """
        ...

    @overload
    def testFreezeDoesNotDeactivatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#382)
        """
        ...

    def testFreezeDoesNotDeactivatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#382)
        """
        return self._execute(self.chain, request_type, "fb95148c", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFrozenPolicyIsFullyImmutable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#388)
        """
        ...

    @overload
    def testFrozenPolicyIsFullyImmutable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#388)
        """
        ...

    @overload
    def testFrozenPolicyIsFullyImmutable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#388)
        """
        ...

    @overload
    def testFrozenPolicyIsFullyImmutable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#388)
        """
        ...

    def testFrozenPolicyIsFullyImmutable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#388)
        """
        return self._execute(self.chain, request_type, "38e974a4", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFreezePolicyRevertsIfNoEligibilitySet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#413)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoEligibilitySet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#413)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoEligibilitySet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#413)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoEligibilitySet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#413)
        """
        ...

    def testFreezePolicyRevertsIfNoEligibilitySet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#413)
        """
        return self._execute(self.chain, request_type, "67d6e102", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFreezePolicyRevertsIfNoRatiosSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#437)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoRatiosSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#437)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoRatiosSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#437)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoRatiosSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#437)
        """
        ...

    def testFreezePolicyRevertsIfNoRatiosSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#437)
        """
        return self._execute(self.chain, request_type, "22badc3b", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFreezePolicyRevertsIfNoConcentrationSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#461)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoConcentrationSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#461)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoConcentrationSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#461)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoConcentrationSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#461)
        """
        ...

    def testFreezePolicyRevertsIfNoConcentrationSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#461)
        """
        return self._execute(self.chain, request_type, "e3213366", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFreezePolicyRevertsIfNoAttestationSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#485)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoAttestationSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#485)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoAttestationSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#485)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoAttestationSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#485)
        """
        ...

    def testFreezePolicyRevertsIfNoAttestationSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#485)
        """
        return self._execute(self.chain, request_type, "8f162af2", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFreezePolicyRevertsIfNoCovenantsSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#509)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoCovenantsSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#509)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoCovenantsSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#509)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoCovenantsSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#509)
        """
        ...

    def testFreezePolicyRevertsIfNoCovenantsSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#509)
        """
        return self._execute(self.chain, request_type, "992b2e0e", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFreezePolicyRevertsIfNoLoanTiersSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#533)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoLoanTiersSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#533)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoLoanTiersSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#533)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoLoanTiersSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#533)
        """
        ...

    def testFreezePolicyRevertsIfNoLoanTiersSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#533)
        """
        return self._execute(self.chain, request_type, "304c38ff", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFreezePolicyRevertsIfNoDocumentHashSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#557)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoDocumentHashSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#557)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoDocumentHashSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#557)
        """
        ...

    @overload
    def testFreezePolicyRevertsIfNoDocumentHashSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#557)
        """
        ...

    def testFreezePolicyRevertsIfNoDocumentHashSet(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#557)
        """
        return self._execute(self.chain, request_type, "e97a187a", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testChangePolicyAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#582)
        """
        ...

    @overload
    def testChangePolicyAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#582)
        """
        ...

    @overload
    def testChangePolicyAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#582)
        """
        ...

    @overload
    def testChangePolicyAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#582)
        """
        ...

    def testChangePolicyAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#582)
        """
        return self._execute(self.chain, request_type, "f2d6c968", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testChaingePolicyAdminRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#588)
        """
        ...

    @overload
    def testChaingePolicyAdminRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#588)
        """
        ...

    @overload
    def testChaingePolicyAdminRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#588)
        """
        ...

    @overload
    def testChaingePolicyAdminRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#588)
        """
        ...

    def testChaingePolicyAdminRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#588)
        """
        return self._execute(self.chain, request_type, "2fe68603", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testAdminRevertIfNewAdminIsZeroAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#594)
        """
        ...

    @overload
    def testAdminRevertIfNewAdminIsZeroAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#594)
        """
        ...

    @overload
    def testAdminRevertIfNewAdminIsZeroAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#594)
        """
        ...

    @overload
    def testAdminRevertIfNewAdminIsZeroAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#594)
        """
        ...

    def testAdminRevertIfNewAdminIsZeroAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#594)
        """
        return self._execute(self.chain, request_type, "0187faf2", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testChangePolicyAdminEmitsEvent(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#602)
        """
        ...

    @overload
    def testChangePolicyAdminEmitsEvent(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#602)
        """
        ...

    @overload
    def testChangePolicyAdminEmitsEvent(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#602)
        """
        ...

    @overload
    def testChangePolicyAdminEmitsEvent(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#602)
        """
        ...

    def testChangePolicyAdminEmitsEvent(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#602)
        """
        return self._execute(self.chain, request_type, "f50c411e", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testOldAdminLosesAccessAfterAdminChange(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#609)
        """
        ...

    @overload
    def testOldAdminLosesAccessAfterAdminChange(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#609)
        """
        ...

    @overload
    def testOldAdminLosesAccessAfterAdminChange(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#609)
        """
        ...

    @overload
    def testOldAdminLosesAccessAfterAdminChange(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#609)
        """
        ...

    def testOldAdminLosesAccessAfterAdminChange(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#609)
        """
        return self._execute(self.chain, request_type, "f44d3ee3", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testNewAdminCanCreatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#618)
        """
        ...

    @overload
    def testNewAdminCanCreatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#618)
        """
        ...

    @overload
    def testNewAdminCanCreatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#618)
        """
        ...

    @overload
    def testNewAdminCanCreatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#618)
        """
        ...

    def testNewAdminCanCreatePolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#618)
        """
        return self._execute(self.chain, request_type, "c001fea2", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testNewAdminCanManageExistingPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#629)
        """
        ...

    @overload
    def testNewAdminCanManageExistingPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#629)
        """
        ...

    @overload
    def testNewAdminCanManageExistingPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#629)
        """
        ...

    @overload
    def testNewAdminCanManageExistingPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#629)
        """
        ...

    def testNewAdminCanManageExistingPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#629)
        """
        return self._execute(self.chain, request_type, "fc8a67a2", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateEligibility(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#643)
        """
        ...

    @overload
    def testUpdateEligibility(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#643)
        """
        ...

    @overload
    def testUpdateEligibility(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#643)
        """
        ...

    @overload
    def testUpdateEligibility(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#643)
        """
        ...

    def testUpdateEligibility(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#643)
        """
        return self._execute(self.chain, request_type, "77603488", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testMultipleEligibilityUpdates(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#651)
        """
        ...

    @overload
    def testMultipleEligibilityUpdates(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#651)
        """
        ...

    @overload
    def testMultipleEligibilityUpdates(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#651)
        """
        ...

    @overload
    def testMultipleEligibilityUpdates(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#651)
        """
        ...

    def testMultipleEligibilityUpdates(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#651)
        """
        return self._execute(self.chain, request_type, "9a331cd1", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateEligibilityStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#678)
        """
        ...

    @overload
    def testUpdateEligibilityStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#678)
        """
        ...

    @overload
    def testUpdateEligibilityStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#678)
        """
        ...

    @overload
    def testUpdateEligibilityStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#678)
        """
        ...

    def testUpdateEligibilityStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#678)
        """
        return self._execute(self.chain, request_type, "b57fc055", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateEligibilityRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#700)
        """
        ...

    @overload
    def testUpdateEligibilityRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#700)
        """
        ...

    @overload
    def testUpdateEligibilityRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#700)
        """
        ...

    @overload
    def testUpdateEligibilityRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#700)
        """
        ...

    def testUpdateEligibilityRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#700)
        """
        return self._execute(self.chain, request_type, "c9bba5e0", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateEligibilityRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#712)
        """
        ...

    @overload
    def testUpdateEligibilityRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#712)
        """
        ...

    @overload
    def testUpdateEligibilityRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#712)
        """
        ...

    @overload
    def testUpdateEligibilityRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#712)
        """
        ...

    def testUpdateEligibilityRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#712)
        """
        return self._execute(self.chain, request_type, "cb997500", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUnAuthorizedUpdateEligibility(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#718)
        """
        ...

    @overload
    def testUnAuthorizedUpdateEligibility(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#718)
        """
        ...

    @overload
    def testUnAuthorizedUpdateEligibility(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#718)
        """
        ...

    @overload
    def testUnAuthorizedUpdateEligibility(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#718)
        """
        ...

    def testUnAuthorizedUpdateEligibility(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#718)
        """
        return self._execute(self.chain, request_type, "5c9b4562", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testEligibilityWithZeroValues(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#725)
        """
        ...

    @overload
    def testEligibilityWithZeroValues(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#725)
        """
        ...

    @overload
    def testEligibilityWithZeroValues(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#725)
        """
        ...

    @overload
    def testEligibilityWithZeroValues(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#725)
        """
        ...

    def testEligibilityWithZeroValues(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#725)
        """
        return self._execute(self.chain, request_type, "6459b9cf", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateFinancialRatios(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#751)
        """
        ...

    @overload
    def testUpdateFinancialRatios(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#751)
        """
        ...

    @overload
    def testUpdateFinancialRatios(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#751)
        """
        ...

    @overload
    def testUpdateFinancialRatios(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#751)
        """
        ...

    def testUpdateFinancialRatios(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#751)
        """
        return self._execute(self.chain, request_type, "d95a2cb1", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateRatiosStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#759)
        """
        ...

    @overload
    def testUpdateRatiosStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#759)
        """
        ...

    @overload
    def testUpdateRatiosStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#759)
        """
        ...

    @overload
    def testUpdateRatiosStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#759)
        """
        ...

    def testUpdateRatiosStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#759)
        """
        return self._execute(self.chain, request_type, "0ee87ab9", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateFinancialRatiosRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#776)
        """
        ...

    @overload
    def testUpdateFinancialRatiosRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#776)
        """
        ...

    @overload
    def testUpdateFinancialRatiosRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#776)
        """
        ...

    @overload
    def testUpdateFinancialRatiosRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#776)
        """
        ...

    def testUpdateFinancialRatiosRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#776)
        """
        return self._execute(self.chain, request_type, "c6d7f09e", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateFinancialRatiosRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#788)
        """
        ...

    @overload
    def testUpdateFinancialRatiosRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#788)
        """
        ...

    @overload
    def testUpdateFinancialRatiosRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#788)
        """
        ...

    @overload
    def testUpdateFinancialRatiosRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#788)
        """
        ...

    def testUpdateFinancialRatiosRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#788)
        """
        return self._execute(self.chain, request_type, "8a364b02", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUnAuthorizedUpdateFinancialRatios(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#794)
        """
        ...

    @overload
    def testUnAuthorizedUpdateFinancialRatios(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#794)
        """
        ...

    @overload
    def testUnAuthorizedUpdateFinancialRatios(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#794)
        """
        ...

    @overload
    def testUnAuthorizedUpdateFinancialRatios(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#794)
        """
        ...

    def testUnAuthorizedUpdateFinancialRatios(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#794)
        """
        return self._execute(self.chain, request_type, "a95c6049", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateConcentrationLimits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#805)
        """
        ...

    @overload
    def testUpdateConcentrationLimits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#805)
        """
        ...

    @overload
    def testUpdateConcentrationLimits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#805)
        """
        ...

    @overload
    def testUpdateConcentrationLimits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#805)
        """
        ...

    def testUpdateConcentrationLimits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#805)
        """
        return self._execute(self.chain, request_type, "100115ef", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateConcentrationStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#813)
        """
        ...

    @overload
    def testUpdateConcentrationStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#813)
        """
        ...

    @overload
    def testUpdateConcentrationStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#813)
        """
        ...

    @overload
    def testUpdateConcentrationStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#813)
        """
        ...

    def testUpdateConcentrationStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#813)
        """
        return self._execute(self.chain, request_type, "5ea786de", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateConcentrationLimitsRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#825)
        """
        ...

    @overload
    def testUpdateConcentrationLimitsRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#825)
        """
        ...

    @overload
    def testUpdateConcentrationLimitsRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#825)
        """
        ...

    @overload
    def testUpdateConcentrationLimitsRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#825)
        """
        ...

    def testUpdateConcentrationLimitsRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#825)
        """
        return self._execute(self.chain, request_type, "bdf9cc39", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateConcentrationLimitsRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#837)
        """
        ...

    @overload
    def testUpdateConcentrationLimitsRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#837)
        """
        ...

    @overload
    def testUpdateConcentrationLimitsRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#837)
        """
        ...

    @overload
    def testUpdateConcentrationLimitsRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#837)
        """
        ...

    def testUpdateConcentrationLimitsRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#837)
        """
        return self._execute(self.chain, request_type, "863e08cf", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUnAuthorizedUpdateConcentrationLimits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#843)
        """
        ...

    @overload
    def testUnAuthorizedUpdateConcentrationLimits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#843)
        """
        ...

    @overload
    def testUnAuthorizedUpdateConcentrationLimits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#843)
        """
        ...

    @overload
    def testUnAuthorizedUpdateConcentrationLimits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#843)
        """
        ...

    def testUnAuthorizedUpdateConcentrationLimits(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#843)
        """
        return self._execute(self.chain, request_type, "c24ed26c", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateAttestationRequirments(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#854)
        """
        ...

    @overload
    def testUpdateAttestationRequirments(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#854)
        """
        ...

    @overload
    def testUpdateAttestationRequirments(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#854)
        """
        ...

    @overload
    def testUpdateAttestationRequirments(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#854)
        """
        ...

    def testUpdateAttestationRequirments(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#854)
        """
        return self._execute(self.chain, request_type, "ded41a92", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateAttestationStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#862)
        """
        ...

    @overload
    def testUpdateAttestationStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#862)
        """
        ...

    @overload
    def testUpdateAttestationStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#862)
        """
        ...

    @overload
    def testUpdateAttestationStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#862)
        """
        ...

    def testUpdateAttestationStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#862)
        """
        return self._execute(self.chain, request_type, "e0479f7b", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateAttestationRequirmentsRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#874)
        """
        ...

    @overload
    def testUpdateAttestationRequirmentsRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#874)
        """
        ...

    @overload
    def testUpdateAttestationRequirmentsRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#874)
        """
        ...

    @overload
    def testUpdateAttestationRequirmentsRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#874)
        """
        ...

    def testUpdateAttestationRequirmentsRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#874)
        """
        return self._execute(self.chain, request_type, "ba251fb1", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateAttestationRequirmentsRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#886)
        """
        ...

    @overload
    def testUpdateAttestationRequirmentsRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#886)
        """
        ...

    @overload
    def testUpdateAttestationRequirmentsRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#886)
        """
        ...

    @overload
    def testUpdateAttestationRequirmentsRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#886)
        """
        ...

    def testUpdateAttestationRequirmentsRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#886)
        """
        return self._execute(self.chain, request_type, "596d28d8", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUnAuthorizedUpdateAttestationRequirements(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#892)
        """
        ...

    @overload
    def testUnAuthorizedUpdateAttestationRequirements(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#892)
        """
        ...

    @overload
    def testUnAuthorizedUpdateAttestationRequirements(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#892)
        """
        ...

    @overload
    def testUnAuthorizedUpdateAttestationRequirements(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#892)
        """
        ...

    def testUnAuthorizedUpdateAttestationRequirements(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#892)
        """
        return self._execute(self.chain, request_type, "5f3ad5bc", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateCovenants(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#903)
        """
        ...

    @overload
    def testUpdateCovenants(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#903)
        """
        ...

    @overload
    def testUpdateCovenants(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#903)
        """
        ...

    @overload
    def testUpdateCovenants(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#903)
        """
        ...

    def testUpdateCovenants(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#903)
        """
        return self._execute(self.chain, request_type, "d612405a", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateCovenantsStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#911)
        """
        ...

    @overload
    def testUpdateCovenantsStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#911)
        """
        ...

    @overload
    def testUpdateCovenantsStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#911)
        """
        ...

    @overload
    def testUpdateCovenantsStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#911)
        """
        ...

    def testUpdateCovenantsStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#911)
        """
        return self._execute(self.chain, request_type, "a0b4d187", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateCovenantsRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#931)
        """
        ...

    @overload
    def testUpdateCovenantsRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#931)
        """
        ...

    @overload
    def testUpdateCovenantsRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#931)
        """
        ...

    @overload
    def testUpdateCovenantsRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#931)
        """
        ...

    def testUpdateCovenantsRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#931)
        """
        return self._execute(self.chain, request_type, "d669a92d", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdateCovenantsRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#943)
        """
        ...

    @overload
    def testUpdateCovenantsRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#943)
        """
        ...

    @overload
    def testUpdateCovenantsRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#943)
        """
        ...

    @overload
    def testUpdateCovenantsRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#943)
        """
        ...

    def testUpdateCovenantsRevertIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#943)
        """
        return self._execute(self.chain, request_type, "63411f83", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUnAuthorizedUpdateCovenants(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#949)
        """
        ...

    @overload
    def testUnAuthorizedUpdateCovenants(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#949)
        """
        ...

    @overload
    def testUnAuthorizedUpdateCovenants(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#949)
        """
        ...

    @overload
    def testUnAuthorizedUpdateCovenants(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#949)
        """
        ...

    def testUnAuthorizedUpdateCovenants(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#949)
        """
        return self._execute(self.chain, request_type, "e4c26207", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testSetLoanTier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#960)
        """
        ...

    @overload
    def testSetLoanTier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#960)
        """
        ...

    @overload
    def testSetLoanTier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#960)
        """
        ...

    @overload
    def testSetLoanTier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#960)
        """
        ...

    def testSetLoanTier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#960)
        """
        return self._execute(self.chain, request_type, "510bf470", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testSetLoanTierWithMaxUint8RevertBecauseOfMaxTierLimit(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#968)
        """
        ...

    @overload
    def testSetLoanTierWithMaxUint8RevertBecauseOfMaxTierLimit(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#968)
        """
        ...

    @overload
    def testSetLoanTierWithMaxUint8RevertBecauseOfMaxTierLimit(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#968)
        """
        ...

    @overload
    def testSetLoanTierWithMaxUint8RevertBecauseOfMaxTierLimit(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#968)
        """
        ...

    def testSetLoanTierWithMaxUint8RevertBecauseOfMaxTierLimit(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#968)
        """
        return self._execute(self.chain, request_type, "af459beb", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testSetLoanTierStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#980)
        """
        ...

    @overload
    def testSetLoanTierStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#980)
        """
        ...

    @overload
    def testSetLoanTierStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#980)
        """
        ...

    @overload
    def testSetLoanTierStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#980)
        """
        ...

    def testSetLoanTierStoresDataCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#980)
        """
        return self._execute(self.chain, request_type, "6e7bdb48", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testSetLoanTierRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#994)
        """
        ...

    @overload
    def testSetLoanTierRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#994)
        """
        ...

    @overload
    def testSetLoanTierRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#994)
        """
        ...

    @overload
    def testSetLoanTierRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#994)
        """
        ...

    def testSetLoanTierRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#994)
        """
        return self._execute(self.chain, request_type, "f3624451", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testSetLoanTierRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1001)
        """
        ...

    @overload
    def testSetLoanTierRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1001)
        """
        ...

    @overload
    def testSetLoanTierRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1001)
        """
        ...

    @overload
    def testSetLoanTierRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1001)
        """
        ...

    def testSetLoanTierRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1001)
        """
        return self._execute(self.chain, request_type, "b8bfd299", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testSetLoanTierRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1007)
        """
        ...

    @overload
    def testSetLoanTierRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1007)
        """
        ...

    @overload
    def testSetLoanTierRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1007)
        """
        ...

    @overload
    def testSetLoanTierRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1007)
        """
        ...

    def testSetLoanTierRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1007)
        """
        return self._execute(self.chain, request_type, "f359ec85", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testSetLoanTierIncrementsTotalTiers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1019)
        """
        ...

    @overload
    def testSetLoanTierIncrementsTotalTiers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1019)
        """
        ...

    @overload
    def testSetLoanTierIncrementsTotalTiers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1019)
        """
        ...

    @overload
    def testSetLoanTierIncrementsTotalTiers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1019)
        """
        ...

    def testSetLoanTierIncrementsTotalTiers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1019)
        """
        return self._execute(self.chain, request_type, "3db0e7c5", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testMultipleTierManagement(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1035)
        """
        ...

    @overload
    def testMultipleTierManagement(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1035)
        """
        ...

    @overload
    def testMultipleTierManagement(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1035)
        """
        ...

    @overload
    def testMultipleTierManagement(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1035)
        """
        ...

    def testMultipleTierManagement(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1035)
        """
        return self._execute(self.chain, request_type, "afdf4bca", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testTotalTiersDoesNotDecrease(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1054)
        """
        ...

    @overload
    def testTotalTiersDoesNotDecrease(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1054)
        """
        ...

    @overload
    def testTotalTiersDoesNotDecrease(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1054)
        """
        ...

    @overload
    def testTotalTiersDoesNotDecrease(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1054)
        """
        ...

    def testTotalTiersDoesNotDecrease(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1054)
        """
        return self._execute(self.chain, request_type, "5c132a59", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testTierExistsGetter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1065)
        """
        ...

    @overload
    def testTierExistsGetter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1065)
        """
        ...

    @overload
    def testTierExistsGetter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1065)
        """
        ...

    @overload
    def testTierExistsGetter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1065)
        """
        ...

    def testTierExistsGetter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1065)
        """
        return self._execute(self.chain, request_type, "4257494e", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testOverwriteExistingTier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1074)
        """
        ...

    @overload
    def testOverwriteExistingTier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1074)
        """
        ...

    @overload
    def testOverwriteExistingTier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1074)
        """
        ...

    @overload
    def testOverwriteExistingTier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1074)
        """
        ...

    def testOverwriteExistingTier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1074)
        """
        return self._execute(self.chain, request_type, "be3839cc", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testExcludeIndustryUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1097)
        """
        ...

    @overload
    def testExcludeIndustryUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1097)
        """
        ...

    @overload
    def testExcludeIndustryUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1097)
        """
        ...

    @overload
    def testExcludeIndustryUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1097)
        """
        ...

    def testExcludeIndustryUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1097)
        """
        return self._execute(self.chain, request_type, "bee81c50", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testExcludeIndustryRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1109)
        """
        ...

    @overload
    def testExcludeIndustryRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1109)
        """
        ...

    @overload
    def testExcludeIndustryRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1109)
        """
        ...

    @overload
    def testExcludeIndustryRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1109)
        """
        ...

    def testExcludeIndustryRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1109)
        """
        return self._execute(self.chain, request_type, "3ca2928d", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testExcludeIndustryIsIdempotent(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1116)
        """
        ...

    @overload
    def testExcludeIndustryIsIdempotent(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1116)
        """
        ...

    @overload
    def testExcludeIndustryIsIdempotent(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1116)
        """
        ...

    @overload
    def testExcludeIndustryIsIdempotent(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1116)
        """
        ...

    def testExcludeIndustryIsIdempotent(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1116)
        """
        return self._execute(self.chain, request_type, "193692e9", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testExcludeIndustryRevertsIfDataIsZeroHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1129)
        """
        ...

    @overload
    def testExcludeIndustryRevertsIfDataIsZeroHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1129)
        """
        ...

    @overload
    def testExcludeIndustryRevertsIfDataIsZeroHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1129)
        """
        ...

    @overload
    def testExcludeIndustryRevertsIfDataIsZeroHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1129)
        """
        ...

    def testExcludeIndustryRevertsIfDataIsZeroHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1129)
        """
        return self._execute(self.chain, request_type, "f6860c4e", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testExcludeIndustryRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1138)
        """
        ...

    @overload
    def testExcludeIndustryRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1138)
        """
        ...

    @overload
    def testExcludeIndustryRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1138)
        """
        ...

    @overload
    def testExcludeIndustryRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1138)
        """
        ...

    def testExcludeIndustryRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1138)
        """
        return self._execute(self.chain, request_type, "f10778b6", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testExcludeIndustryRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1144)
        """
        ...

    @overload
    def testExcludeIndustryRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1144)
        """
        ...

    @overload
    def testExcludeIndustryRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1144)
        """
        ...

    @overload
    def testExcludeIndustryRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1144)
        """
        ...

    def testExcludeIndustryRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1144)
        """
        return self._execute(self.chain, request_type, "947bf4af", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testIncludeIndustryUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1156)
        """
        ...

    @overload
    def testIncludeIndustryUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1156)
        """
        ...

    @overload
    def testIncludeIndustryUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1156)
        """
        ...

    @overload
    def testIncludeIndustryUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1156)
        """
        ...

    def testIncludeIndustryUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1156)
        """
        return self._execute(self.chain, request_type, "43b00f28", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testIncludeNeverExcludedIndustry(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1171)
        """
        ...

    @overload
    def testIncludeNeverExcludedIndustry(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1171)
        """
        ...

    @overload
    def testIncludeNeverExcludedIndustry(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1171)
        """
        ...

    @overload
    def testIncludeNeverExcludedIndustry(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1171)
        """
        ...

    def testIncludeNeverExcludedIndustry(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1171)
        """
        return self._execute(self.chain, request_type, "87018479", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testIncludeIndustryRevertsIfDataIsZeroHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1181)
        """
        ...

    @overload
    def testIncludeIndustryRevertsIfDataIsZeroHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1181)
        """
        ...

    @overload
    def testIncludeIndustryRevertsIfDataIsZeroHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1181)
        """
        ...

    @overload
    def testIncludeIndustryRevertsIfDataIsZeroHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1181)
        """
        ...

    def testIncludeIndustryRevertsIfDataIsZeroHash(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1181)
        """
        return self._execute(self.chain, request_type, "fcda57aa", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testIncludeIndustryRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1190)
        """
        ...

    @overload
    def testIncludeIndustryRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1190)
        """
        ...

    @overload
    def testIncludeIndustryRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1190)
        """
        ...

    @overload
    def testIncludeIndustryRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1190)
        """
        ...

    def testIncludeIndustryRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1190)
        """
        return self._execute(self.chain, request_type, "fb92355f", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testIncludeIndustryRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1197)
        """
        ...

    @overload
    def testIncludeIndustryRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1197)
        """
        ...

    @overload
    def testIncludeIndustryRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1197)
        """
        ...

    @overload
    def testIncludeIndustryRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1197)
        """
        ...

    def testIncludeIndustryRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1197)
        """
        return self._execute(self.chain, request_type, "d05b5c9f", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testIncludeIndustryRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1203)
        """
        ...

    @overload
    def testIncludeIndustryRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1203)
        """
        ...

    @overload
    def testIncludeIndustryRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1203)
        """
        ...

    @overload
    def testIncludeIndustryRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1203)
        """
        ...

    def testIncludeIndustryRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1203)
        """
        return self._execute(self.chain, request_type, "15d1f73e", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testIndustryExclusionState(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1215)
        """
        ...

    @overload
    def testIndustryExclusionState(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1215)
        """
        ...

    @overload
    def testIndustryExclusionState(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1215)
        """
        ...

    @overload
    def testIndustryExclusionState(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1215)
        """
        ...

    def testIndustryExclusionState(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1215)
        """
        return self._execute(self.chain, request_type, "d7e00db3", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testMultipleIndustryExclusions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1230)
        """
        ...

    @overload
    def testMultipleIndustryExclusions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1230)
        """
        ...

    @overload
    def testMultipleIndustryExclusions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1230)
        """
        ...

    @overload
    def testMultipleIndustryExclusions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1230)
        """
        ...

    def testMultipleIndustryExclusions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1230)
        """
        return self._execute(self.chain, request_type, "288e53a6", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testSetPolicyDocumentUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1252)
        """
        ...

    @overload
    def testSetPolicyDocumentUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1252)
        """
        ...

    @overload
    def testSetPolicyDocumentUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1252)
        """
        ...

    @overload
    def testSetPolicyDocumentUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1252)
        """
        ...

    def testSetPolicyDocumentUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1252)
        """
        return self._execute(self.chain, request_type, "e6bb1dee", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testSetPolicyDocumentStoresCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1269)
        """
        ...

    @overload
    def testSetPolicyDocumentStoresCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1269)
        """
        ...

    @overload
    def testSetPolicyDocumentStoresCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1269)
        """
        ...

    @overload
    def testSetPolicyDocumentStoresCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1269)
        """
        ...

    def testSetPolicyDocumentStoresCorrectly(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1269)
        """
        return self._execute(self.chain, request_type, "71330348", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testUpdatePolicyDocumentMultipleTimes(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1282)
        """
        ...

    @overload
    def testUpdatePolicyDocumentMultipleTimes(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1282)
        """
        ...

    @overload
    def testUpdatePolicyDocumentMultipleTimes(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1282)
        """
        ...

    @overload
    def testUpdatePolicyDocumentMultipleTimes(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1282)
        """
        ...

    def testUpdatePolicyDocumentMultipleTimes(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1282)
        """
        return self._execute(self.chain, request_type, "37c777be", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testSetPolicyDocumentRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1295)
        """
        ...

    @overload
    def testSetPolicyDocumentRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1295)
        """
        ...

    @overload
    def testSetPolicyDocumentRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1295)
        """
        ...

    @overload
    def testSetPolicyDocumentRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1295)
        """
        ...

    def testSetPolicyDocumentRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1295)
        """
        return self._execute(self.chain, request_type, "2b849c47", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testSetPolicyDocumentRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1306)
        """
        ...

    @overload
    def testSetPolicyDocumentRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1306)
        """
        ...

    @overload
    def testSetPolicyDocumentRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1306)
        """
        ...

    @overload
    def testSetPolicyDocumentRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1306)
        """
        ...

    def testSetPolicyDocumentRevertsIfPolicyDontExist(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1306)
        """
        return self._execute(self.chain, request_type, "603ca1d3", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testSetPolicyDocumentRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1316)
        """
        ...

    @overload
    def testSetPolicyDocumentRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1316)
        """
        ...

    @overload
    def testSetPolicyDocumentRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1316)
        """
        ...

    @overload
    def testSetPolicyDocumentRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1316)
        """
        ...

    def testSetPolicyDocumentRevertsIfPolicyIsFrozen(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1316)
        """
        return self._execute(self.chain, request_type, "a489d710", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testLastUpdatedTimestamp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1336)
        """
        ...

    @overload
    def testLastUpdatedTimestamp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1336)
        """
        ...

    @overload
    def testLastUpdatedTimestamp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1336)
        """
        ...

    @overload
    def testLastUpdatedTimestamp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1336)
        """
        ...

    def testLastUpdatedTimestamp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1336)
        """
        return self._execute(self.chain, request_type, "df70711d", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testLastUpdatedAlwaysMovesForward(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1350)
        """
        ...

    @overload
    def testLastUpdatedAlwaysMovesForward(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1350)
        """
        ...

    @overload
    def testLastUpdatedAlwaysMovesForward(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1350)
        """
        ...

    @overload
    def testLastUpdatedAlwaysMovesForward(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1350)
        """
        ...

    def testLastUpdatedAlwaysMovesForward(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1350)
        """
        return self._execute(self.chain, request_type, "7e66e8f0", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testCompletePolicyLifecycle(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1361)
        """
        ...

    @overload
    def testCompletePolicyLifecycle(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1361)
        """
        ...

    @overload
    def testCompletePolicyLifecycle(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1361)
        """
        ...

    @overload
    def testCompletePolicyLifecycle(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1361)
        """
        ...

    def testCompletePolicyLifecycle(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1361)
        """
        return self._execute(self.chain, request_type, "af99213f", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testCannotFreezeDeactivatedPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1390)
        """
        ...

    @overload
    def testCannotFreezeDeactivatedPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1390)
        """
        ...

    @overload
    def testCannotFreezeDeactivatedPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1390)
        """
        ...

    @overload
    def testCannotFreezeDeactivatedPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1390)
        """
        ...

    def testCannotFreezeDeactivatedPolicy(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1390)
        """
        return self._execute(self.chain, request_type, "63fc93a4", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testIsPolicyActiveGetter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1410)
        """
        ...

    @overload
    def testIsPolicyActiveGetter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1410)
        """
        ...

    @overload
    def testIsPolicyActiveGetter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1410)
        """
        ...

    @overload
    def testIsPolicyActiveGetter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1410)
        """
        ...

    def testIsPolicyActiveGetter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1410)
        """
        return self._execute(self.chain, request_type, "b7e79cb3", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testIsPolicyFrozenGetter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1419)
        """
        ...

    @overload
    def testIsPolicyFrozenGetter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1419)
        """
        ...

    @overload
    def testIsPolicyFrozenGetter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1419)
        """
        ...

    @overload
    def testIsPolicyFrozenGetter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1419)
        """
        ...

    def testIsPolicyFrozenGetter(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1419)
        """
        return self._execute(self.chain, request_type, "46ffcb54", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testPolicyWithLargeVersionNumber(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1428)
        """
        ...

    @overload
    def testPolicyWithLargeVersionNumber(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1428)
        """
        ...

    @overload
    def testPolicyWithLargeVersionNumber(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1428)
        """
        ...

    @overload
    def testPolicyWithLargeVersionNumber(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1428)
        """
        ...

    def testPolicyWithLargeVersionNumber(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1428)
        """
        return self._execute(self.chain, request_type, "6735135f", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testLoanTierWithEmptyName(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1436)
        """
        ...

    @overload
    def testLoanTierWithEmptyName(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1436)
        """
        ...

    @overload
    def testLoanTierWithEmptyName(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1436)
        """
        ...

    @overload
    def testLoanTierWithEmptyName(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1436)
        """
        ...

    def testLoanTierWithEmptyName(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1436)
        """
        return self._execute(self.chain, request_type, "7c5f8780", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testSetMaxTiersRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1447)
        """
        ...

    @overload
    def testSetMaxTiersRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1447)
        """
        ...

    @overload
    def testSetMaxTiersRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1447)
        """
        ...

    @overload
    def testSetMaxTiersRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1447)
        """
        ...

    def testSetMaxTiersRevertsIfNotAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1447)
        """
        return self._execute(self.chain, request_type, "9c9287d5", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testSetMaxTiersRevertIfItsMoreThan255(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1454)
        """
        ...

    @overload
    def testSetMaxTiersRevertIfItsMoreThan255(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1454)
        """
        ...

    @overload
    def testSetMaxTiersRevertIfItsMoreThan255(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1454)
        """
        ...

    @overload
    def testSetMaxTiersRevertIfItsMoreThan255(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1454)
        """
        ...

    def testSetMaxTiersRevertIfItsMoreThan255(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1454)
        """
        return self._execute(self.chain, request_type, "59f15622", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testSetMaxTiersUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1465)
        """
        ...

    @overload
    def testSetMaxTiersUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1465)
        """
        ...

    @overload
    def testSetMaxTiersUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1465)
        """
        ...

    @overload
    def testSetMaxTiersUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1465)
        """
        ...

    def testSetMaxTiersUnitTest(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1465)
        """
        return self._execute(self.chain, request_type, "b52aff5d", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testSetPolicyDocumentWithEmptyURI(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1475)
        """
        ...

    @overload
    def testSetPolicyDocumentWithEmptyURI(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1475)
        """
        ...

    @overload
    def testSetPolicyDocumentWithEmptyURI(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1475)
        """
        ...

    @overload
    def testSetPolicyDocumentWithEmptyURI(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1475)
        """
        ...

    def testSetPolicyDocumentWithEmptyURI(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/test/unit/TestCreditPolicy.t.sol#1475)
        """
        return self._execute(self.chain, request_type, "bce5bdac", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

TestCreditPolicy.setUp.selector = bytes4(b'\n\x92T\xe4')
TestCreditPolicy.testCreatePolicyRevertIfOwnerIsNotAdmin.selector = bytes4(b'\xdai\xac\xa6')
TestCreditPolicy.testCreatePolicyRevertsIfVersionIsZero.selector = bytes4(b'\xac\xc45\xdb')
TestCreditPolicy.testCreatePolicyRevertsIfVersionExists.selector = bytes4(b'\xf5\x97\x08C')
TestCreditPolicy.testCreatePolicy.selector = bytes4(b'`Y\x9a\x8c')
TestCreditPolicy.testMultiplePolicyVersions.selector = bytes4(b'\x97\\\x81\xfc')
TestCreditPolicy.testPolicyVersionIsolation.selector = bytes4(b']\xb3\xff\xd0')
TestCreditPolicy.testDeactivatePolicy.selector = bytes4(b'E\xdd\xfa\xd4')
TestCreditPolicy.testDeactivatePolicyRevertIfOwnerIsNotAdmin.selector = bytes4(b'\xd3\x06\xfe\xec')
TestCreditPolicy.testDeactivatePolicyRevertsIfPolicyDontExist.selector = bytes4(b'rkQ\xf3')
TestCreditPolicy.testDeactivateUpdatesLastUpdated.selector = bytes4(b'q\xcb\x19\xdb')
TestCreditPolicy.testDeactivatePolicyIsIdempotent.selector = bytes4(b"'V\xbf\xb1")
TestCreditPolicy.testUpdateRevertsIfPolicyInactive.selector = bytes4(b'\xe2\x88\xed9')
TestCreditPolicy.testFreezePolicyUnitTest.selector = bytes4(b'?\xaf\xa9\xf1')
TestCreditPolicy.testFreezePolicyRevertIfOwnerIsNotAdmin.selector = bytes4(b'\xfe[\xc5\xab')
TestCreditPolicy.testFreezePolicyRevertsIfPolicyDontExist.selector = bytes4(b'\xc0/k\xad')
TestCreditPolicy.testFreezePolicyReverstIfPolicyIsNotActive.selector = bytes4(b'\x9b\x8f\xa0y')
TestCreditPolicy.testFreezePolicyRevertsIfAlreadyFrozen.selector = bytes4(b'\x12\xeaX\\')
TestCreditPolicy.testFreezePolicyMarksPolicyAsFrozen.selector = bytes4(b'kgf\x8c')
TestCreditPolicy.testFreezeUpdatesLastUpdated.selector = bytes4(b'\nzi\xb8')
TestCreditPolicy.testFreezeDoesNotDeactivatePolicy.selector = bytes4(b'\xfb\x95\x14\x8c')
TestCreditPolicy.testFrozenPolicyIsFullyImmutable.selector = bytes4(b'8\xe9t\xa4')
TestCreditPolicy.testFreezePolicyRevertsIfNoEligibilitySet.selector = bytes4(b'g\xd6\xe1\x02')
TestCreditPolicy.testFreezePolicyRevertsIfNoRatiosSet.selector = bytes4(b'"\xba\xdc;')
TestCreditPolicy.testFreezePolicyRevertsIfNoConcentrationSet.selector = bytes4(b'\xe3!3f')
TestCreditPolicy.testFreezePolicyRevertsIfNoAttestationSet.selector = bytes4(b'\x8f\x16*\xf2')
TestCreditPolicy.testFreezePolicyRevertsIfNoCovenantsSet.selector = bytes4(b'\x99+.\x0e')
TestCreditPolicy.testFreezePolicyRevertsIfNoLoanTiersSet.selector = bytes4(b'0L8\xff')
TestCreditPolicy.testFreezePolicyRevertsIfNoDocumentHashSet.selector = bytes4(b'\xe9z\x18z')
TestCreditPolicy.testChangePolicyAdmin.selector = bytes4(b'\xf2\xd6\xc9h')
TestCreditPolicy.testChaingePolicyAdminRevertsIfNotAdmin.selector = bytes4(b'/\xe6\x86\x03')
TestCreditPolicy.testAdminRevertIfNewAdminIsZeroAddress.selector = bytes4(b'\x01\x87\xfa\xf2')
TestCreditPolicy.testChangePolicyAdminEmitsEvent.selector = bytes4(b'\xf5\x0cA\x1e')
TestCreditPolicy.testOldAdminLosesAccessAfterAdminChange.selector = bytes4(b'\xf4M>\xe3')
TestCreditPolicy.testNewAdminCanCreatePolicy.selector = bytes4(b'\xc0\x01\xfe\xa2')
TestCreditPolicy.testNewAdminCanManageExistingPolicy.selector = bytes4(b'\xfc\x8ag\xa2')
TestCreditPolicy.testUpdateEligibility.selector = bytes4(b'w`4\x88')
TestCreditPolicy.testMultipleEligibilityUpdates.selector = bytes4(b'\x9a3\x1c\xd1')
TestCreditPolicy.testUpdateEligibilityStoresDataCorrectly.selector = bytes4(b'\xb5\x7f\xc0U')
TestCreditPolicy.testUpdateEligibilityRevertsIfPolicyIsFrozen.selector = bytes4(b'\xc9\xbb\xa5\xe0')
TestCreditPolicy.testUpdateEligibilityRevertsIfPolicyDontExist.selector = bytes4(b'\xcb\x99u\x00')
TestCreditPolicy.testUnAuthorizedUpdateEligibility.selector = bytes4(b'\\\x9bEb')
TestCreditPolicy.testEligibilityWithZeroValues.selector = bytes4(b'dY\xb9\xcf')
TestCreditPolicy.testUpdateFinancialRatios.selector = bytes4(b'\xd9Z,\xb1')
TestCreditPolicy.testUpdateRatiosStoresDataCorrectly.selector = bytes4(b'\x0e\xe8z\xb9')
TestCreditPolicy.testUpdateFinancialRatiosRevertsIfPolicyIsFrozen.selector = bytes4(b'\xc6\xd7\xf0\x9e')
TestCreditPolicy.testUpdateFinancialRatiosRevertIfPolicyDontExist.selector = bytes4(b'\x8a6K\x02')
TestCreditPolicy.testUnAuthorizedUpdateFinancialRatios.selector = bytes4(b'\xa9\\`I')
TestCreditPolicy.testUpdateConcentrationLimits.selector = bytes4(b'\x10\x01\x15\xef')
TestCreditPolicy.testUpdateConcentrationStoresDataCorrectly.selector = bytes4(b'^\xa7\x86\xde')
TestCreditPolicy.testUpdateConcentrationLimitsRevertsIfPolicyIsFrozen.selector = bytes4(b'\xbd\xf9\xcc9')
TestCreditPolicy.testUpdateConcentrationLimitsRevertIfPolicyDontExist.selector = bytes4(b'\x86>\x08\xcf')
TestCreditPolicy.testUnAuthorizedUpdateConcentrationLimits.selector = bytes4(b'\xc2N\xd2l')
TestCreditPolicy.testUpdateAttestationRequirments.selector = bytes4(b'\xde\xd4\x1a\x92')
TestCreditPolicy.testUpdateAttestationStoresDataCorrectly.selector = bytes4(b'\xe0G\x9f{')
TestCreditPolicy.testUpdateAttestationRequirmentsRevertsIfPolicyIsFrozen.selector = bytes4(b'\xba%\x1f\xb1')
TestCreditPolicy.testUpdateAttestationRequirmentsRevertIfPolicyDontExist.selector = bytes4(b'Ym(\xd8')
TestCreditPolicy.testUnAuthorizedUpdateAttestationRequirements.selector = bytes4(b'_:\xd5\xbc')
TestCreditPolicy.testUpdateCovenants.selector = bytes4(b'\xd6\x12@Z')
TestCreditPolicy.testUpdateCovenantsStoresDataCorrectly.selector = bytes4(b'\xa0\xb4\xd1\x87')
TestCreditPolicy.testUpdateCovenantsRevertsIfPolicyIsFrozen.selector = bytes4(b'\xd6i\xa9-')
TestCreditPolicy.testUpdateCovenantsRevertIfPolicyDontExist.selector = bytes4(b'cA\x1f\x83')
TestCreditPolicy.testUnAuthorizedUpdateCovenants.selector = bytes4(b'\xe4\xc2b\x07')
TestCreditPolicy.testSetLoanTier.selector = bytes4(b'Q\x0b\xf4p')
TestCreditPolicy.testSetLoanTierWithMaxUint8RevertBecauseOfMaxTierLimit.selector = bytes4(b'\xafE\x9b\xeb')
TestCreditPolicy.testSetLoanTierStoresDataCorrectly.selector = bytes4(b'n{\xdbH')
TestCreditPolicy.testSetLoanTierRevertsIfNotAdmin.selector = bytes4(b'\xf3bDQ')
TestCreditPolicy.testSetLoanTierRevertsIfPolicyDontExist.selector = bytes4(b'\xb8\xbf\xd2\x99')
TestCreditPolicy.testSetLoanTierRevertsIfPolicyIsFrozen.selector = bytes4(b'\xf3Y\xec\x85')
TestCreditPolicy.testSetLoanTierIncrementsTotalTiers.selector = bytes4(b'=\xb0\xe7\xc5')
TestCreditPolicy.testMultipleTierManagement.selector = bytes4(b'\xaf\xdfK\xca')
TestCreditPolicy.testTotalTiersDoesNotDecrease.selector = bytes4(b'\\\x13*Y')
TestCreditPolicy.testTierExistsGetter.selector = bytes4(b'BWIN')
TestCreditPolicy.testOverwriteExistingTier.selector = bytes4(b'\xbe89\xcc')
TestCreditPolicy.testExcludeIndustryUnitTest.selector = bytes4(b'\xbe\xe8\x1cP')
TestCreditPolicy.testExcludeIndustryRevertsIfNotAdmin.selector = bytes4(b'<\xa2\x92\x8d')
TestCreditPolicy.testExcludeIndustryIsIdempotent.selector = bytes4(b'\x196\x92\xe9')
TestCreditPolicy.testExcludeIndustryRevertsIfDataIsZeroHash.selector = bytes4(b'\xf6\x86\x0cN')
TestCreditPolicy.testExcludeIndustryRevertsIfPolicyDontExist.selector = bytes4(b'\xf1\x07x\xb6')
TestCreditPolicy.testExcludeIndustryRevertsIfPolicyIsFrozen.selector = bytes4(b'\x94{\xf4\xaf')
TestCreditPolicy.testIncludeIndustryUnitTest.selector = bytes4(b'C\xb0\x0f(')
TestCreditPolicy.testIncludeNeverExcludedIndustry.selector = bytes4(b'\x87\x01\x84y')
TestCreditPolicy.testIncludeIndustryRevertsIfDataIsZeroHash.selector = bytes4(b'\xfc\xdaW\xaa')
TestCreditPolicy.testIncludeIndustryRevertsIfNotAdmin.selector = bytes4(b'\xfb\x925_')
TestCreditPolicy.testIncludeIndustryRevertsIfPolicyDontExist.selector = bytes4(b'\xd0[\\\x9f')
TestCreditPolicy.testIncludeIndustryRevertsIfPolicyIsFrozen.selector = bytes4(b'\x15\xd1\xf7>')
TestCreditPolicy.testIndustryExclusionState.selector = bytes4(b'\xd7\xe0\r\xb3')
TestCreditPolicy.testMultipleIndustryExclusions.selector = bytes4(b'(\x8eS\xa6')
TestCreditPolicy.testSetPolicyDocumentUnitTest.selector = bytes4(b'\xe6\xbb\x1d\xee')
TestCreditPolicy.testSetPolicyDocumentStoresCorrectly.selector = bytes4(b'q3\x03H')
TestCreditPolicy.testUpdatePolicyDocumentMultipleTimes.selector = bytes4(b'7\xc7w\xbe')
TestCreditPolicy.testSetPolicyDocumentRevertsIfNotAdmin.selector = bytes4(b'+\x84\x9cG')
TestCreditPolicy.testSetPolicyDocumentRevertsIfPolicyDontExist.selector = bytes4(b'`<\xa1\xd3')
TestCreditPolicy.testSetPolicyDocumentRevertsIfPolicyIsFrozen.selector = bytes4(b'\xa4\x89\xd7\x10')
TestCreditPolicy.testLastUpdatedTimestamp.selector = bytes4(b'\xdfpq\x1d')
TestCreditPolicy.testLastUpdatedAlwaysMovesForward.selector = bytes4(b'~f\xe8\xf0')
TestCreditPolicy.testCompletePolicyLifecycle.selector = bytes4(b'\xaf\x99!?')
TestCreditPolicy.testCannotFreezeDeactivatedPolicy.selector = bytes4(b'c\xfc\x93\xa4')
TestCreditPolicy.testIsPolicyActiveGetter.selector = bytes4(b'\xb7\xe7\x9c\xb3')
TestCreditPolicy.testIsPolicyFrozenGetter.selector = bytes4(b'F\xff\xcbT')
TestCreditPolicy.testPolicyWithLargeVersionNumber.selector = bytes4(b'g5\x13_')
TestCreditPolicy.testLoanTierWithEmptyName.selector = bytes4(b'|_\x87\x80')
TestCreditPolicy.testSetMaxTiersRevertsIfNotAdmin.selector = bytes4(b'\x9c\x92\x87\xd5')
TestCreditPolicy.testSetMaxTiersRevertIfItsMoreThan255.selector = bytes4(b'Y\xf1V"')
TestCreditPolicy.testSetMaxTiersUnitTest.selector = bytes4(b'\xb5*\xff]')
TestCreditPolicy.testSetPolicyDocumentWithEmptyURI.selector = bytes4(b'\xbc\xe5\xbd\xac')
