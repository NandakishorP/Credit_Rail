
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.access.manager.IAccessManager import IAccessManager
from pytypes.lib.openzeppelincontracts.contracts.utils.Context import Context
from pytypes.lib.openzeppelincontracts.contracts.utils.Multicall import Multicall



class AccessManager(IAccessManager, Multicall, Context):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#62)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'address', 'name': 'initialAdmin', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\x81>\x94Y': {'inputs': [{'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}], 'name': 'AccessManagerAlreadyScheduled', 'type': 'error'}, b'_\x15\x9ec': {'inputs': [], 'name': 'AccessManagerBadConfirmation', 'type': 'error'}, b'x\xa5\xd6\xe4': {'inputs': [{'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}], 'name': 'AccessManagerExpired', 'type': 'error'}, b'\x08\x13\xad\xa2': {'inputs': [{'internalType': 'address', 'name': 'initialAdmin', 'type': 'address'}], 'name': 'AccessManagerInvalidInitialAdmin', 'type': 'error'}, b'\x18q\xa9\x0c': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}], 'name': 'AccessManagerLockedRole', 'type': 'error'}, b'\x18\xcbkz': {'inputs': [{'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}], 'name': 'AccessManagerNotReady', 'type': 'error'}, b'`\xa2\x99\xb0': {'inputs': [{'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}], 'name': 'AccessManagerNotScheduled', 'type': 'error'}, b'\xf0~\x03\x8f': {'inputs': [{'internalType': 'address', 'name': 'msgsender', 'type': 'address'}, {'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}], 'name': 'AccessManagerUnauthorizedAccount', 'type': 'error'}, b'\x81\xc6\xf2K': {'inputs': [{'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes4', 'name': 'selector', 'type': 'bytes4'}], 'name': 'AccessManagerUnauthorizedCall', 'type': 'error'}, b'?\xe2u\x1c': {'inputs': [{'internalType': 'address', 'name': 'msgsender', 'type': 'address'}, {'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes4', 'name': 'selector', 'type': 'bytes4'}], 'name': 'AccessManagerUnauthorizedCancel', 'type': 'error'}, b'2\x0f\xf7H': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'AccessManagerUnauthorizedConsume', 'type': 'error'}, b'\x99\x96\xb3\x15': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'AddressEmptyCode', 'type': 'error'}, b'\xd6\xbd\xa2u': {'inputs': [], 'name': 'FailedCall', 'type': 'error'}, b'\xcfG\x91\x81': {'inputs': [{'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}], 'name': 'InsufficientBalance', 'type': 'error'}, b'm\xfc\xc6P': {'inputs': [{'internalType': 'uint8', 'name': 'bits', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'SafeCastOverflowedUintDowncast', 'type': 'error'}, b"\xbd\x9a\xc6zn/dc\xb8\t'2c\x103\x8b\xcb\xb4\xbd\xb7\x93l\xe16^\xa3\xe0\x10g\xe7\xb9\xf7": {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'uint32', 'name': 'nonce', 'type': 'uint32'}], 'name': 'OperationCanceled', 'type': 'event'}, b'v\xa2\xa4iSh\x9dHa\xa5\xd3\xf6\xed\x88:\xd7\xe6\xafgJ!\xf8\xe1bpqY\xfc\x9d\xdeaM': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'uint32', 'name': 'nonce', 'type': 'uint32'}], 'name': 'OperationExecuted', 'type': 'event'}, b"\x82\xa2\xda]\xeeT\xea\x80!\xc6T[DDb\x02\x91\xe0~\xe8;\xe6\xddW\xed\xb1u\x06'\x15\xf3\xb4": {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'uint32', 'name': 'nonce', 'type': 'uint32'}, {'indexed': False, 'internalType': 'uint48', 'name': 'schedule', 'type': 'uint48'}, {'indexed': False, 'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'target', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'OperationScheduled', 'type': 'event'}, b'\x1f\xd6\xddv11-\xfa\xc2 [R\x91?\x99\xde\x03\xb4\xd7\xe3\x81\xd5\xd2}=\xbf\xe0q>nc@': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'indexed': True, 'internalType': 'uint64', 'name': 'admin', 'type': 'uint64'}], 'name': 'RoleAdminChanged', 'type': 'event'}, b'\xfe\xb6\x90\x18\xee\x8b\x8f\xd5\x0e\xa8cH\xf1&}\x07g3y\xf7,\xff\xde\xcc\xecc\x85>\xe8\xce\x8bH': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'indexed': False, 'internalType': 'uint32', 'name': 'delay', 'type': 'uint32'}, {'indexed': False, 'internalType': 'uint48', 'name': 'since', 'type': 'uint48'}], 'name': 'RoleGrantDelayChanged', 'type': 'event'}, b"\xf9\x84H\xb9\x87\xf1B\x8e\x0e#\x0e\x1f<n,\xe1[V\x93\xea\xf3\x18'\xfb\xd0\xb1\xecKBJ\xe7\xcf": {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'indexed': True, 'internalType': 'address', 'name': 'account', 'type': 'address'}, {'indexed': False, 'internalType': 'uint32', 'name': 'delay', 'type': 'uint32'}, {'indexed': False, 'internalType': 'uint48', 'name': 'since', 'type': 'uint48'}, {'indexed': False, 'internalType': 'bool', 'name': 'newMember', 'type': 'bool'}], 'name': 'RoleGranted', 'type': 'event'}, b'z\x80Yc\x0b\x89{]\xe4\xc0\x8a\xdei\xf8\xb9\x0c>\xad\x1f\x85\x96\xd6-\x10\xb6\xc4\xd1J\n\xfbJ\xe2': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'indexed': True, 'internalType': 'uint64', 'name': 'guardian', 'type': 'uint64'}], 'name': 'RoleGuardianChanged', 'type': 'event'}, b'\x12V\xf5\xb5\xec\xb8\x9c\xae\xc1-\xb4Is\x8f/\xbc\xd1\xbaX\x06\xcf8\xf3T\x13\xf4\xe5\xc1[\xf6\xa4P': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'indexed': False, 'internalType': 'string', 'name': 'label', 'type': 'string'}], 'name': 'RoleLabel', 'type': 'event'}, b'\xf2)\xba\xa5\x93\xaf(\xc4\x1b\x1d\x16\xb7H\xcdv\x88\xf0\xc8:\xaf\x92\xd4\xbeA\xc4@\x05\xde\xfe\x84\xc1f': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'indexed': True, 'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'RoleRevoked', 'type': 'event'}, b"\xa5kv\x01tS\xf3\x99\xec#'\xba\x007]\xbf\xb1\xfd\x07\x0f\xf8T4\x1a\xd6\x19\x1ej.-\xe1\x9c": {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'target', 'type': 'address'}, {'indexed': False, 'internalType': 'uint32', 'name': 'delay', 'type': 'uint32'}, {'indexed': False, 'internalType': 'uint48', 'name': 'since', 'type': 'uint48'}], 'name': 'TargetAdminDelayUpdated', 'type': 'event'}, b'\x90\xd4\xe7\xbb~]\x937\x92\xb3V.\x17A0o\x8b\xe9H7\xe14\x8d\xac\xef\x9bo\x1d\xf5n\xb18': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'target', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'closed', 'type': 'bool'}], 'name': 'TargetClosed', 'type': 'event'}, b'\x9e\xa6y\x0c}\xad\xfd\x01\xc9\xf8\xb9v+6\x82`z\xf2\xc7\xe7\x9e\x05\xa9\xf9\xfd\xf5X\r\xde\x94\x91Q': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'target', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes4', 'name': 'selector', 'type': 'bytes4'}, {'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}], 'name': 'TargetFunctionRoleUpdated', 'type': 'event'}, b'u\xb28\xfc': {'inputs': [], 'name': 'ADMIN_ROLE', 'outputs': [{'internalType': 'uint64', 'name': '', 'type': 'uint64'}], 'stateMutability': 'view', 'type': 'function'}, b'<\xa7\xc0*': {'inputs': [], 'name': 'PUBLIC_ROLE', 'outputs': [{'internalType': 'uint64', 'name': '', 'type': 'uint64'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb7\x00\x96\x13': {'inputs': [{'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes4', 'name': 'selector', 'type': 'bytes4'}], 'name': 'canCall', 'outputs': [{'internalType': 'bool', 'name': 'immediate', 'type': 'bool'}, {'internalType': 'uint32', 'name': 'delay', 'type': 'uint32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd6\xbbb\xc6': {'inputs': [{'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'cancel', 'outputs': [{'internalType': 'uint32', 'name': '', 'type': 'uint32'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x94\xc7\xd7\xee': {'inputs': [{'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'consumeScheduledOp', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x1c\xffy\xcd': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'execute', 'outputs': [{'internalType': 'uint32', 'name': '', 'type': 'uint32'}], 'stateMutability': 'payable', 'type': 'function'}, b'Fe\tm': {'inputs': [], 'name': 'expiration', 'outputs': [{'internalType': 'uint32', 'name': '', 'type': 'uint32'}], 'stateMutability': 'view', 'type': 'function'}, b'0x\xf1\x14': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'getAccess', 'outputs': [{'internalType': 'uint48', 'name': 'since', 'type': 'uint48'}, {'internalType': 'uint32', 'name': 'currentDelay', 'type': 'uint32'}, {'internalType': 'uint32', 'name': 'pendingDelay', 'type': 'uint32'}, {'internalType': 'uint48', 'name': 'effect', 'type': 'uint48'}], 'stateMutability': 'view', 'type': 'function'}, b'A6\xa3<': {'inputs': [{'internalType': 'bytes32', 'name': 'id', 'type': 'bytes32'}], 'name': 'getNonce', 'outputs': [{'internalType': 'uint32', 'name': '', 'type': 'uint32'}], 'stateMutability': 'view', 'type': 'function'}, b'S\r\xd4V': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}], 'name': 'getRoleAdmin', 'outputs': [{'internalType': 'uint64', 'name': '', 'type': 'uint64'}], 'stateMutability': 'view', 'type': 'function'}, b"\x12\xbe\x87'": {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}], 'name': 'getRoleGrantDelay', 'outputs': [{'internalType': 'uint32', 'name': '', 'type': 'uint32'}], 'stateMutability': 'view', 'type': 'function'}, b'\x0b\n\x93\xba': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}], 'name': 'getRoleGuardian', 'outputs': [{'internalType': 'uint64', 'name': '', 'type': 'uint64'}], 'stateMutability': 'view', 'type': 'function'}, b":\xdc'z": {'inputs': [{'internalType': 'bytes32', 'name': 'id', 'type': 'bytes32'}], 'name': 'getSchedule', 'outputs': [{'internalType': 'uint48', 'name': '', 'type': 'uint48'}], 'stateMutability': 'view', 'type': 'function'}, b'L\x1d\xa1\xe2': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'getTargetAdminDelay', 'outputs': [{'internalType': 'uint32', 'name': '', 'type': 'uint32'}], 'stateMutability': 'view', 'type': 'function'}, b'mQ\x15\xbd': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes4', 'name': 'selector', 'type': 'bytes4'}], 'name': 'getTargetFunctionRole', 'outputs': [{'internalType': 'uint64', 'name': '', 'type': 'uint64'}], 'stateMutability': 'view', 'type': 'function'}, b'%\xc4q\xa0': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint32', 'name': 'executionDelay', 'type': 'uint32'}], 'name': 'grantRole', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd1\xf8V\xee': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'hasRole', 'outputs': [{'internalType': 'bool', 'name': 'isMember', 'type': 'bool'}, {'internalType': 'uint32', 'name': 'executionDelay', 'type': 'uint32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xab\xd9\xbd*': {'inputs': [{'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'hashOperation', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa1f\xaa\x89': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'isTargetClosed', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x855Q\xb8': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'internalType': 'string', 'name': 'label', 'type': 'string'}], 'name': 'labelRole', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xcc\x1bl\x81': {'inputs': [], 'name': 'minSetback', 'outputs': [{'internalType': 'uint32', 'name': '', 'type': 'uint32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xac\x96P\xd8': {'inputs': [{'internalType': 'bytes[]', 'name': 'data', 'type': 'bytes[]'}], 'name': 'multicall', 'outputs': [{'internalType': 'bytes[]', 'name': 'results', 'type': 'bytes[]'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfe\x07v\xf5': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'internalType': 'address', 'name': 'callerConfirmation', 'type': 'address'}], 'name': 'renounceRole', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb7\xd2\xb1b': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'revokeRole', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf8\x01\xa6\x98': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'internalType': 'uint48', 'name': 'when', 'type': 'uint48'}], 'name': 'schedule', 'outputs': [{'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}, {'internalType': 'uint32', 'name': 'nonce', 'type': 'uint32'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa6M\x95\xce': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'internalType': 'uint32', 'name': 'newDelay', 'type': 'uint32'}], 'name': 'setGrantDelay', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'0\xca\xe1\x87': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'admin', 'type': 'uint64'}], 'name': 'setRoleAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'R\x96)R': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'guardian', 'type': 'uint64'}], 'name': 'setRoleGuardian', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd2+Y\x89': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'uint32', 'name': 'newDelay', 'type': 'uint32'}], 'name': 'setTargetAdminDelay', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x16{\xd3\x95': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bool', 'name': 'closed', 'type': 'bool'}], 'name': 'setTargetClosed', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x08\xd6\x12-': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}, {'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}], 'name': 'setTargetFunctionRole', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x18\xff\x18<': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'address', 'name': 'newAuthority', 'type': 'address'}], 'name': 'updateAuthority', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":81,"contract":"lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol:AccessManager","label":"_targets","offset":0,"slot":0,"type":"t_mapping(t_address,t_struct(TargetConfig)36_storage)"},{"astId":86,"contract":"lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol:AccessManager","label":"_roles","offset":0,"slot":1,"type":"t_mapping(t_uint64,t_struct(Role)55_storage)"},{"astId":91,"contract":"lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol:AccessManager","label":"_schedules","offset":0,"slot":2,"type":"t_mapping(t_bytes32,t_struct(Schedule)60_storage)"},{"astId":93,"contract":"lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol:AccessManager","label":"_executionId","offset":0,"slot":3,"type":"t_bytes32"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_mapping(t_address,t_struct(Access)42_storage)":{"encoding":"mapping","label":"mapping(address => struct AccessManager.Access)","numberOfBytes":32,"key":"t_address","value":"t_struct(Access)42_storage"},"t_mapping(t_address,t_struct(TargetConfig)36_storage)":{"encoding":"mapping","label":"mapping(address => struct AccessManager.TargetConfig)","numberOfBytes":32,"key":"t_address","value":"t_struct(TargetConfig)36_storage"},"t_mapping(t_bytes32,t_struct(Schedule)60_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct AccessManager.Schedule)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(Schedule)60_storage"},"t_mapping(t_bytes4,t_uint64)":{"encoding":"mapping","label":"mapping(bytes4 => uint64)","numberOfBytes":32,"key":"t_bytes4","value":"t_uint64"},"t_mapping(t_uint64,t_struct(Role)55_storage)":{"encoding":"mapping","label":"mapping(uint64 => struct AccessManager.Role)","numberOfBytes":32,"key":"t_uint64","value":"t_struct(Role)55_storage"},"t_struct(Access)42_storage":{"encoding":"inplace","label":"struct AccessManager.Access","numberOfBytes":32,"members":[{"astId":38,"contract":"lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol:AccessManager","label":"since","offset":0,"slot":0,"type":"t_uint48"},{"astId":41,"contract":"lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol:AccessManager","label":"delay","offset":6,"slot":0,"type":"t_userDefinedValueType(Delay)6635"}]},"t_struct(Role)55_storage":{"encoding":"inplace","label":"struct AccessManager.Role","numberOfBytes":64,"members":[{"astId":47,"contract":"lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol:AccessManager","label":"members","offset":0,"slot":0,"type":"t_mapping(t_address,t_struct(Access)42_storage)"},{"astId":49,"contract":"lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol:AccessManager","label":"admin","offset":0,"slot":1,"type":"t_uint64"},{"astId":51,"contract":"lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol:AccessManager","label":"guardian","offset":8,"slot":1,"type":"t_uint64"},{"astId":54,"contract":"lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol:AccessManager","label":"grantDelay","offset":16,"slot":1,"type":"t_userDefinedValueType(Delay)6635"}]},"t_struct(Schedule)60_storage":{"encoding":"inplace","label":"struct AccessManager.Schedule","numberOfBytes":32,"members":[{"astId":57,"contract":"lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol:AccessManager","label":"timepoint","offset":0,"slot":0,"type":"t_uint48"},{"astId":59,"contract":"lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol:AccessManager","label":"nonce","offset":6,"slot":0,"type":"t_uint32"}]},"t_struct(TargetConfig)36_storage":{"encoding":"inplace","label":"struct AccessManager.TargetConfig","numberOfBytes":64,"members":[{"astId":30,"contract":"lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol:AccessManager","label":"allowedRoles","offset":0,"slot":0,"type":"t_mapping(t_bytes4,t_uint64)"},{"astId":33,"contract":"lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol:AccessManager","label":"adminDelay","offset":0,"slot":1,"type":"t_userDefinedValueType(Delay)6635"},{"astId":35,"contract":"lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol:AccessManager","label":"closed","offset":14,"slot":1,"type":"t_bool"}]},"t_uint32":{"encoding":"inplace","label":"uint32","numberOfBytes":4},"t_uint48":{"encoding":"inplace","label":"uint48","numberOfBytes":6},"t_uint64":{"encoding":"inplace","label":"uint64","numberOfBytes":8},"t_userDefinedValueType(Delay)6635":{"encoding":"inplace","label":"Time.Delay","numberOfBytes":14}}}
    _creation_code = "6080604052346102b757604051601f61258838819003918201601f19168301916001600160401b0383118484101761015a578084926020946040528339810103126102b757516001600160a01b038116908190036102b75780156102a4575f8181525f5160206125485f395f51905f52602052604090205465ffffffffffff161580156101825765ffffffffffff610096426102bb565b1665ffffffffffff811161016e578060405191604083019383851060018060401b0386111761015a5760409485529183525f60208085018281528783525f5160206125485f395f51905f529091529481209351845495516001600160a01b031990961665ffffffffffff919091161760309590951b600160301b600160a01b0316949094179092555f5160206125685f395f51905f52916060915b65ffffffffffff604051928684521660208301526040820152a360405161225d90816102eb8239f35b634e487b7160e01b5f52604160045260245ffd5b634e487b7160e01b5f52601160045260245ffd5b5f8281525f5160206125485f395f51905f526020526040902054906101a6426102bb565b63ffffffff8360301c169265ffffffffffff808260701c1692168211155f146102925750505b63ffffffff8216801561028b5763ffffffff811161016e575b65ffffffffffff63ffffffff6101fa426102bb565b921691160165ffffffffffff811161016e575f8481525f5160206125485f395f51905f52602090815260408083208054600160301b600160a01b0319169185901b6dffffffffffff0000000000000000169690921b67ffffffff00000000169590951760301b600160301b600160a01b0316949094179093555f5160206125685f395f51905f529160609190610131565b505f6101e5565b63ffffffff9060501c169250506101cc565b630409d6d160e11b5f525f60045260245ffd5b5f80fd5b65ffffffffffff81116102d35765ffffffffffff1690565b6306dfcc6560e41b5f52603060045260245260445ffdfe60806040526004361015610011575f80fd5b5f5f3560e01c806308d6122d1461141b5780630b0a93ba146113d657806312be8727146113b3578063167bd3951461132857806318ff183c146112965780631cff79cd1461117657806325c471a014610eea5780633078f11414610e8f57806330cae18714610df15780633adc277a14610dc25780633ca7c02a14610da05780634136a33c14610d6d5780634665096d14610d4f5780634c1da1e214610d1d5780635296295214610c75578063530dd45614610c405780636d5115bd14610be057806375b238fc14610bc4578063853551b814610b0a57806394c7d7ee14610a44578063a166aa8914610a16578063a64d95ce14610919578063abd9bd2a146108f4578063ac9650d814610747578063b700961314610702578063b7d2b162146106cf578063cc1b6c81146106b1578063d1f856ee1461066c578063d22b59891461059d578063d6bb62c6146103e9578063f801a698146101cc5763fe0776f51461017a575f80fd5b346101c95760403660031901126101c957610193611558565b61019b611512565b90336001600160a01b038316036101ba57906101b691611cbf565b5080f35b635f159e6360e01b8352600483fd5b80fd5b50346101c95760603660031901126101c9576101e66114fc565b906024356001600160401b0381116103e557610206903690600401611584565b919060443565ffffffffffff81168091036103e15761022784838733611a14565b905061024363ffffffff61023a426121d8565b92168092611943565b901580156103c6575b61038d579065ffffffffffff8092169081808211911802181690610272848287336117ce565b93848452600260205265ffffffffffff604085205416801515908161037c575b5061036857604095849361035987947f82a2da5dee54ea8021c6545b4444620291e07ee83be6dd57edb175062715f3b494868b99526002602052600163ffffffff8a8a205460301c160163ffffffff81169989898c9b52600260205281812065ffffffffffff881665ffffffffffff198254161790558981526002602052209063ffffffff60301b82549160301b169063ffffffff60301b19161790558a51948594855233602086015260018060a01b03168b85015260806060850152608084019161178b565b0390a382519182526020820152f35b63813e945960e01b84526004859052602484fd5b6103869150611c69565b155f610292565b6064848761039b8887611a5b565b6381c6f24b60e01b8352336004526001600160a01b039091166024526001600160e01b031916604452fd5b50811515801561024c575065ffffffffffff8116821061024c565b8280fd5b5080fd5b50346101c957610411906103fc36611607565b6104098183949793611a5b565b9286856117ce565b91828452600260205265ffffffffffff604085205416155f146104425763060a299b60e41b84526004839052602484fd5b6001600160a01b0316903382036104b4575b505060209250808252600283526040822065ffffffffffff1981541690558082526002835263ffffffff604083205460301c1680917fbd9ac67a6e2f6463b80927326310338bcbb4bdb7936ce1365ea3e01067e7b9f76040519480a38152f35b65ffffffffffff946104c6335f6116be565b50509616958615159687610580575b505060018060a01b03169485855284602052604085209163ffffffff60e01b169182865260205261053d336105386001600160401b036040892054166001600160401b03165f5260016020526001600160401b03600160405f20015460401c1690565b6118ed565b5090159081610577575b501561045457608492508460405192630ff89d4760e21b8452336004850152602484015260448301526064820152fd5b9050155f610547565b90965065ffffffffffff610593426121d8565b161015955f6104d5565b50346101c95760403660031901126101c9576105b76114fc565b7fa56b76017453f399ec2327ba00375dbfb1fd070ff854341ad6191e6a2e2de19c6105e06115f4565b916105e9611975565b6001600160a01b0316808452602084905260408420600101549092906106199082906001600160701b0316612147565b8486526020868152604080882060010180546001600160701b0319166001600160701b0390951694909417909355825163ffffffff909416845265ffffffffffff90911690830152819081015b0390a280f35b50346101c95760403660031901126101c957610697610689611558565b610691611512565b906118ed565b60408051921515835263ffffffff91909116602083015290f35b50346101c957806003193601126101c9576020604051620697808152f35b50346101c95760403660031901126101c9576101b66106ec611558565b6106f4611512565b906106fd611975565b611cbf565b50346101c95760603660031901126101c95761071c6114fc565b610724611512565b604435916001600160e01b03198316830361074357610697935061185c565b8380fd5b50346101c95760203660031901126101c9576004356001600160401b0381116103e557610778903690600401611528565b9060206040516107888282611689565b84815281810191601f1981013684376107a08561181d565b936107ae6040519586611689565b858552601f196107bd8761181d565b01875b8181106108e557505036819003601e190190875b8781101561086d578060051b82013583811215610869578201908135916001600160401b03831161086557850182360381136108655782610843610849928d898c6001986040519687958487013784018281018481528e519283915e010190815203601f198101835282611689565b30611c9d565b610853828a611834565b5261085e8189611834565b50016107d4565b8a80fd5b8980fd5b88848860405191808301818452825180915260408401918060408360051b870101940192865b8388106108a05786860387f35b9091929394838080600193603f198b8203018752818a518051918291828552018484015e86838284010152601f80199101160101970193019701969093929193610893565b606087820185015283016107c0565b50346101c957602061091161090836611607565b929190916117ce565b604051908152f35b50346101c95760403660031901126101c957610933611558565b6001600160401b036109436115f4565b9161094c611975565b16906001600160401b038214610a02577ffeb69018ee8b8fd50ea86348f1267d07673379f72cffdeccec63853ee8ce8b489082845260016020526109a28160018060701b03600160408820015460801c16612147565b8486526001602081815260408089209092018054600160801b600160f01b03191660809590951b600160801b600160f01b031694909417909355805163ffffffff909416845265ffffffffffff9091169183019190915281908101610666565b63061c6a4360e21b83526004829052602483fd5b50346101c95760203660031901126101c9576020610a3a610a356114fc565b6117ab565b6040519015158152f35b50346101c957610a53366115b1565b91604051638fb3603760e01b8152602081600481335afa908115610aff578591610ab8575b506001600160e01b03191663704c9fc960e01b01610aa55791610aa0916101b69333906117ce565b611a71565b630641fee960e31b845233600452602484fd5b90506020813d602011610af7575b81610ad360209383611689565b81010312610af357516001600160e01b031981168103610af3575f610a78565b8480fd5b3d9150610ac6565b6040513d87823e3d90fd5b50346101c95760403660031901126101c957610b24611558565b602435906001600160401b0382116103e157610b4c6001600160401b03923690600401611584565b929091610b57611975565b169182158015610bb4575b610ba057907f1256f5b5ecb89caec12db449738f2fbcd1ba5806cf38f35413f4e5c15bf6a4509161066660405192839260208452602084019161178b565b63061c6a4360e21b84526004839052602484fd5b506001600160401b038314610b62565b50346101c957806003193601126101c957602090604051908152f35b50346101c95760403660031901126101c957610bfa6114fc565b6024359063ffffffff60e01b82168092036103e1576001600160a01b0316825260208281526040808420928452918152918190205490516001600160401b039091168152f35b50346101c95760203660031901126101c9576020610c64610c5f611558565b611767565b6001600160401b0360405191168152f35b50346101c95760403660031901126101c957610c8f611558565b6001600160401b03610c9f61156e565b91610ca8611975565b169081158015610d0d575b610a02576001600160401b039082845260016020526001604085200180548360401b8360401b16908460401b191617905516907f7a8059630b897b5de4c08ade69f8b90c3ead1f8596d62d10b6c4d14a0afb4ae28380a380f35b506001600160401b038214610cb3565b50346101c95760203660031901126101c9576020610d41610d3c6114fc565b61173b565b63ffffffff60405191168152f35b50346101c957806003193601126101c957602060405162093a808152f35b50346101c95760203660031901126101c95763ffffffff6040602092600435815260028452205460301c16604051908152f35b50346101c957806003193601126101c95760206040516001600160401b038152f35b50346101c95760203660031901126101c9576020610de1600435611711565b65ffffffffffff60405191168152f35b50346101c95760403660031901126101c957610e0b611558565b6001600160401b03610e1b61156e565b91610e24611975565b169081158015610e7f575b610a02576001600160401b0390828452600160205260016040852001828216831982541617905516907f1fd6dd7631312dfac2205b52913f99de03b4d7e381d5d27d3dbfe0713e6e63408380a380f35b506001600160401b038214610e2f565b50346101c95760403660031901126101c957608063ffffffff65ffffffffffff81610ec9610ebb611558565b610ec3611512565b906116be565b93929590918560405197168752166020860152166040840152166060820152f35b50346101c95760603660031901126101c957610f04611558565b610f0c611512565b906044359163ffffffff831680930361074357610f27611975565b6001600160401b03610f3883611659565b9216916001600160401b038314611162578285526001602090815260408087206001600160a01b0385165f908152925290205465ffffffffffff161590811561104b57610f959063ffffffff610f8d426121d8565b911690611943565b604051604081018181106001600160401b03821117611037575f5160206122085f395f51905f5294926110186060959365ffffffffffff936040528383168152602081018a8152898c52600160205260408c2060018060a01b0388165f52602052848060405f2093511616851983541617825560018060701b0390511690611bfd565b60408051988952911660208801528601526001600160a01b031693a380f35b634e487b7160e01b88526041600452602488fd5b508285526001602090815260408087206001600160a01b0385165f90815292529020546110839060301c6001600160701b0316611c2c565b50508463ffffffff82168181115f1461112d570363ffffffff8111611119579165ffffffffffff5f5160206122085f395f51905f52949261111463ffffffff60201b6110e063ffffffff6060985b166110db426121d8565b611943565b9260201b168360401b8360401b16178917888b52600160205260408b2060018060a01b0387165f5260205260405f20611bfd565b611018565b634e487b7160e01b87526011600452602487fd5b50509160609165ffffffffffff5f5160206122085f395f51905f529461111463ffffffff60201b6110e063ffffffff8c6110d1565b63061c6a4360e21b85526004839052602485fd5b50611180366115b1565b909161118e82848333611a14565b93901580611288575b61127a576111a7838284336117ce565b63ffffffff86951615801590611261575b61124f575b50600354926111d56111cf8284611a5b565b84611b3e565b6003556001600160401b03811161123b57604051916111fe601f8301601f191660200184611689565b81835236828201116112375795602082849382998361122598970137830101523491611b62565b5060035563ffffffff60405191168152f35b8680fd5b634e487b7160e01b86526041600452602486fd5b61125a919450611a71565b925f6111bd565b5065ffffffffffff61127282611711565b1615156111b8565b9061039b6064938693611a5b565b5063ffffffff841615611197565b5034611324576040366003190112611324576112b06114fc565b6112b8611512565b906112c1611975565b6001600160a01b031690813b1561132457604051637a9e5e4b60e01b81526001600160a01b039091166004820152905f908290602490829084905af180156113195761130b575080f35b61131791505f90611689565b005b6040513d5f823e3d90fd5b5f80fd5b34611324576040366003190112611324576113416114fc565b602435908115158092036113245760207f90d4e7bb7e5d933792b3562e1741306f8be94837e1348dacef9b6f1df56eb1389161137b611975565b6001600160a01b03165f818152808352604090819020600101805460ff60701b1916607087901b60ff60701b161790555193845292a2005b34611324576020366003190112611324576020610d416113d1611558565b611659565b34611324576020366003190112611324576020610c646113f4611558565b6001600160401b03165f5260016020526001600160401b03600160405f20015460401c1690565b34611324576060366003190112611324576114346114fc565b6024356001600160401b03811161132457611453903690600401611528565b9190604435906001600160401b03821680920361132457611475939293611975565b6001600160a01b03909316925f5b83811015611317578060051b8201359063ffffffff60e01b82168092036113245783867f9ea6790c7dadfd01c9f8b9762b3682607af2c7e79e05a9f9fdf5580dde9491516020600195835f525f825260405f20815f52825260405f20856001600160401b0319825416179055604051908152a301611483565b600435906001600160a01b038216820361132457565b602435906001600160a01b038216820361132457565b9181601f84011215611324578235916001600160401b038311611324576020808501948460051b01011161132457565b600435906001600160401b038216820361132457565b602435906001600160401b038216820361132457565b9181601f84011215611324578235916001600160401b038311611324576020838186019501011161132457565b906040600319830112611324576004356001600160a01b03811681036113245791602435906001600160401b038211611324576115f091600401611584565b9091565b6024359063ffffffff8216820361132457565b6060600319820112611324576004356001600160a01b038116810361132457916024356001600160a01b03811681036113245791604435906001600160401b038211611324576115f091600401611584565b6001600160401b03165f52600160205261168460018060701b03600160405f20015460801c16611c2c565b505090565b90601f801991011681019081106001600160401b038211176116aa57604052565b634e487b7160e01b5f52604160045260245ffd5b6001600160401b03165f9081526001602090815260408083206001600160a01b039094168352929052205465ffffffffffff91611707603083901c6001600160701b0316611c2c565b9490931693909291565b5f52600260205265ffffffffffff60405f20541661172e81611c69565b1561173857505f90565b90565b6001600160a01b03165f90815260208190526040902060010154611684906001600160701b0316611c2c565b6001600160401b03165f5260016020526001600160401b03600160405f2001541690565b908060209392818452848401375f828201840152601f01601f1916010190565b6001600160a01b03165f9081526020819052604090206001015460701c60ff1690565b604080516001600160a01b0392831660208201908152929093169083015260608083015292909161181791839161180991608084019161178b565b03601f198101835282611689565b51902090565b6001600160401b0381116116aa5760051b60200190565b80518210156118485760209160051b010190565b634e487b7160e01b5f52603260045260245ffd5b919091611868836117ab565b15611876575050505f905f90565b6001600160a01b038116300361189a57506118949060035492611b3e565b14905f90565b906118d39260018060a01b03165f525f60205260405f209063ffffffff60e01b165f526020526001600160401b0360405f2054166118ed565b9190156118e65763ffffffff8216159190565b5f91508190565b6001600160401b03818116036119065750506001905f90565b65ffffffffffff9291611918916116be565b50509216801515908161192a57509190565b905065ffffffffffff61193c426121d8565b1610159190565b9065ffffffffffff8091169116019065ffffffffffff821161196157565b634e487b7160e01b5f52601160045260245ffd5b61197f3633611d6e565b90156119885750565b63ffffffff166119bd576001600160401b036119a336611e46565b50905063f07e038f60e01b5f52336004521660245260445ffd5b611a116040516020810190338252306040820152606080820152611a0981602060808201368152365f838301375f823683010152601f19601f360116010103601f198101835282611689565b519020611a71565b50565b909291906001600160a01b0384163003611a32576115f09350611e0b565b9192906004841015611a4857505050505f905f90565b6115f093611a5591611a5b565b9161185c565b9060041161132457356001600160e01b03191690565b5f81815260026020526040902054909190603081901c63ffffffff169065ffffffffffff1680611aae578363060a299b60e41b5f5260045260245ffd5b65ffffffffffff611abe426121d8565b16811115611ad95783630c65b5bd60e11b5f5260045260245ffd5b611ae69093919293611c69565b611b2c578190805f52600260205260405f2065ffffffffffff1981541690557f76a2a46953689d4861a5d3f6ed883ad7e6af674a21f8e162707159fc9dde614d5f80a390565b631e2975b960e21b5f5260045260245ffd5b6001600160a01b03165f9081526001600160e01b0319919091166020526040902090565b91804710611be757815f92916020849351920190855af18080611bd4575b15611b8f57505061173861212e565b15611bb457639996b31560e01b5f9081526001600160a01b0391909116600452602490fd5b3d15611bc5576040513d5f823e3d90fd5b63d6bda27560e01b5f5260045ffd5b503d151580611b805750813b1515611b80565b4763cf47918160e01b5f5260045260245260445ffd5b80546601000000000000600160a01b03191660309290921b6601000000000000600160a01b0316919091179055565b611c35426121d8565b63ffffffff82169165ffffffffffff604082901c811692168211611c5d575090915f91508190565b60201c63ffffffff1692565b65ffffffffffff62093a8091160165ffffffffffff81116119615765ffffffffffff80611c95426121d8565b169116111590565b905f8091602081519101845af48080611bd45715611b8f57505061173861212e565b6001600160401b0316906001600160401b038214611d5b57815f52600160205260405f2060018060a01b0382165f5260205265ffffffffffff60405f20541615611d5557815f52600160205260405f2060018060a01b0382165f526020525f604081205560018060a01b0316907ff229baa593af28c41b1d16b748cd7688f0c83aaf92d4be41c44005defe84c1665f80a3600190565b50505f90565b5063061c6a4360e21b5f5260045260245ffd5b9060048110611dca576001600160a01b0382163014611dea57611d91905f611fcf565b9290911580611ddb575b611dd257611da8916118ed565b9015611dca5763ffffffff808093169116908180821191180218169081159190565b50505f905f90565b5050505f905f90565b50611de5306117ab565b611d9b565b9050600411611324576003546118945f356001600160e01b03191630611b3e565b919060048210611dd2576001600160a01b0383163014611e2f5790611d9191611fcf565b611e399250611a5b565b6118946003549130611b3e565b5f9060048110611fc55780600411611324575f356001600160e01b031916906310a6aa3760e31b82148015611fb5575b8015611fa5575b8015611f95575b8015611f85575b611f795763063fc60f60e21b82148015611f69575b8015611f59575b611f295763012e238d60e51b82148015611f19575b611ee7575030825281602052604082209082526020526001600160401b036040822054169181929190565b90506024116101c957806101c957506004356001600160401b038116810361132457611f1290611767565b6001915f90565b50635be958b160e11b8214611ebc565b915050602411611324576004356001600160a01b0381169081900361132457611f519061173b565b6001915f9190565b506308d6122d60e01b8214611ea7565b5063167bd39560e01b8214611ea0565b5050506001905f905f90565b5063d22b598960e01b8214611e8b565b50635326cae760e11b8214611e84565b5063294b14a960e11b8214611e7d565b506330cae18760e01b8214611e76565b50505f905f905f90565b60048210611fc5576001600160e01b0319611fea8383611a5b565b16916310a6aa3760e31b8314801561211e575b801561210e575b80156120fe575b80156120ee575b611f795763063fc60f60e21b831480156120de575b80156120ce575b6120a75763012e238d60e51b83148015612097575b612070575050305f525f60205260405f20905f526020526001600160401b0360405f205416905f91905f90565b90915060241161132457600401356001600160401b038116810361132457611f1290611767565b50635be958b160e11b8314612043565b909150602411611324576004013560018060a01b03811680910361132457611f519061173b565b506308d6122d60e01b831461202e565b5063167bd39560e01b8314612027565b5063d22b598960e01b8314612012565b50635326cae760e11b831461200b565b5063294b14a960e11b8314612004565b506330cae18760e01b8314611ffd565b604051903d82523d5f602084013e60203d830101604052565b61215863ffffffff91939293611c2c565b505092168063ffffffff84168181115f146121bf570363ffffffff8111611961576121a563ffffffff8063ffffffff60201b935b168062069780118162069780180218166110db426121d8565b9360201b1665ffffffffffff60401b8460401b1617179190565b505063ffffffff60201b6121a563ffffffff805f61218c565b65ffffffffffff81116121f05765ffffffffffff1690565b6306dfcc6560e41b5f52603060045260245260445ffdfef98448b987f1428e0e230e1f3c6e2ce15b5693eaf31827fbd0b1ec4b424ae7cfa26469706673582212208862cbc3347004bb401aa54f7b01e1a143f9205970afe5c5063c70247ac862f464736f6c63430008210033a6eef7e35abe7026729641147f7915573c7e97b47efa546f5f6e3230263bcb49f98448b987f1428e0e230e1f3c6e2ce15b5693eaf31827fbd0b1ec4b424ae7cf"

    @overload
    @classmethod
    def deploy(cls, initialAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#129)

        Args:
            initialAdmin: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, initialAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> AccessManager:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#129)

        Args:
            initialAdmin: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, initialAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#129)

        Args:
            initialAdmin: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, initialAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#129)

        Args:
            initialAdmin: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, initialAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[AccessManager]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#129)

        Args:
            initialAdmin: address
        """
        ...

    @classmethod
    def deploy(cls, initialAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, AccessManager, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[AccessManager]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#129)

        Args:
            initialAdmin: address
        """
        return cls._deploy(request_type, [initialAdmin], return_tx, AccessManager, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class TargetConfig:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#66)

        Attributes:
            allowedRoles (Dict[bytes4, uint64]): mapping(bytes4 => uint64)
            adminDelay (uint112): Time.Delay
            closed (bool): bool
        """
        original_name = 'TargetConfig'

        allowedRoles: Dict[bytes4, uint64]
        adminDelay: uint112
        closed: bool


    @dataclasses.dataclass
    class Access:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#73)

        Attributes:
            since (uint48): uint48
            delay (uint112): Time.Delay
        """
        original_name = 'Access'

        since: uint48
        delay: uint112


    @dataclasses.dataclass
    class Role:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#82)

        Attributes:
            members (Dict[Address, AccessManager.Access]): mapping(address => struct AccessManager.Access)
            admin (uint64): uint64
            guardian (uint64): uint64
            grantDelay (uint112): Time.Delay
        """
        original_name = 'Role'

        members: Dict[Address, AccessManager.Access]
        admin: uint64
        guardian: uint64
        grantDelay: uint112


    @dataclasses.dataclass
    class Schedule:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#94)

        Attributes:
            timepoint (uint48): uint48
            nonce (uint32): uint32
        """
        original_name = 'Schedule'

        timepoint: uint48
        nonce: uint32


    @overload
    def ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint64:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#105)

        Returns:
            ADMIN_ROLE: uint64
        """
        ...

    @overload
    def ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#105)

        Returns:
            ADMIN_ROLE: uint64
        """
        ...

    @overload
    def ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#105)

        Returns:
            ADMIN_ROLE: uint64
        """
        ...

    @overload
    def ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint64]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#105)

        Returns:
            ADMIN_ROLE: uint64
        """
        ...

    def ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint64, TransactionAbc[uint64], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#105)

        Returns:
            ADMIN_ROLE: uint64
        """
        return self._execute(self.chain, request_type, "75b238fc", [], True if request_type == "tx" else False, uint64, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def PUBLIC_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint64:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#110)

        Returns:
            PUBLIC_ROLE: uint64
        """
        ...

    @overload
    def PUBLIC_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#110)

        Returns:
            PUBLIC_ROLE: uint64
        """
        ...

    @overload
    def PUBLIC_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#110)

        Returns:
            PUBLIC_ROLE: uint64
        """
        ...

    @overload
    def PUBLIC_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint64]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#110)

        Returns:
            PUBLIC_ROLE: uint64
        """
        ...

    def PUBLIC_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint64, TransactionAbc[uint64], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#110)

        Returns:
            PUBLIC_ROLE: uint64
        """
        return self._execute(self.chain, request_type, "3ca7c02a", [], True if request_type == "tx" else False, uint64, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def canCall(self, caller: Union[Account, Address], target: Union[Account, Address], selector: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[bool, uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#140)

        Args:
            caller: address
            target: address
            selector: bytes4
        Returns:
            immediate: bool
            delay: uint32
        """
        ...

    @overload
    def canCall(self, caller: Union[Account, Address], target: Union[Account, Address], selector: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#140)

        Args:
            caller: address
            target: address
            selector: bytes4
        Returns:
            immediate: bool
            delay: uint32
        """
        ...

    @overload
    def canCall(self, caller: Union[Account, Address], target: Union[Account, Address], selector: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#140)

        Args:
            caller: address
            target: address
            selector: bytes4
        Returns:
            immediate: bool
            delay: uint32
        """
        ...

    @overload
    def canCall(self, caller: Union[Account, Address], target: Union[Account, Address], selector: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[bool, uint32]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#140)

        Args:
            caller: address
            target: address
            selector: bytes4
        Returns:
            immediate: bool
            delay: uint32
        """
        ...

    def canCall(self, caller: Union[Account, Address], target: Union[Account, Address], selector: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[bool, uint32], TransactionAbc[Tuple[bool, uint32]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#140)

        Args:
            caller: address
            target: address
            selector: bytes4
        Returns:
            immediate: bool
            delay: uint32
        """
        return self._execute(self.chain, request_type, "b7009613", [caller, target, selector], True if request_type == "tx" else False, Tuple[bool, uint32], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def expiration(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#159)

        Returns:
            uint32
        """
        ...

    @overload
    def expiration(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#159)

        Returns:
            uint32
        """
        ...

    @overload
    def expiration(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#159)

        Returns:
            uint32
        """
        ...

    @overload
    def expiration(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#159)

        Returns:
            uint32
        """
        ...

    def expiration(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint32, TransactionAbc[uint32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#159)

        Returns:
            uint32
        """
        return self._execute(self.chain, request_type, "4665096d", [], True if request_type == "tx" else False, uint32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def minSetback(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#164)

        Returns:
            uint32
        """
        ...

    @overload
    def minSetback(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#164)

        Returns:
            uint32
        """
        ...

    @overload
    def minSetback(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#164)

        Returns:
            uint32
        """
        ...

    @overload
    def minSetback(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#164)

        Returns:
            uint32
        """
        ...

    def minSetback(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint32, TransactionAbc[uint32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#164)

        Returns:
            uint32
        """
        return self._execute(self.chain, request_type, "cc1b6c81", [], True if request_type == "tx" else False, uint32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def isTargetClosed(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#169)

        Args:
            target: address
        Returns:
            bool
        """
        ...

    @overload
    def isTargetClosed(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#169)

        Args:
            target: address
        Returns:
            bool
        """
        ...

    @overload
    def isTargetClosed(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#169)

        Args:
            target: address
        Returns:
            bool
        """
        ...

    @overload
    def isTargetClosed(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#169)

        Args:
            target: address
        Returns:
            bool
        """
        ...

    def isTargetClosed(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#169)

        Args:
            target: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "a166aa89", [target], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getTargetFunctionRole(self, target: Union[Account, Address], selector: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint64:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#174)

        Args:
            target: address
            selector: bytes4
        Returns:
            uint64
        """
        ...

    @overload
    def getTargetFunctionRole(self, target: Union[Account, Address], selector: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#174)

        Args:
            target: address
            selector: bytes4
        Returns:
            uint64
        """
        ...

    @overload
    def getTargetFunctionRole(self, target: Union[Account, Address], selector: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#174)

        Args:
            target: address
            selector: bytes4
        Returns:
            uint64
        """
        ...

    @overload
    def getTargetFunctionRole(self, target: Union[Account, Address], selector: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint64]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#174)

        Args:
            target: address
            selector: bytes4
        Returns:
            uint64
        """
        ...

    def getTargetFunctionRole(self, target: Union[Account, Address], selector: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint64, TransactionAbc[uint64], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#174)

        Args:
            target: address
            selector: bytes4
        Returns:
            uint64
        """
        return self._execute(self.chain, request_type, "6d5115bd", [target, selector], True if request_type == "tx" else False, uint64, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getTargetAdminDelay(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#179)

        Args:
            target: address
        Returns:
            uint32
        """
        ...

    @overload
    def getTargetAdminDelay(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#179)

        Args:
            target: address
        Returns:
            uint32
        """
        ...

    @overload
    def getTargetAdminDelay(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#179)

        Args:
            target: address
        Returns:
            uint32
        """
        ...

    @overload
    def getTargetAdminDelay(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#179)

        Args:
            target: address
        Returns:
            uint32
        """
        ...

    def getTargetAdminDelay(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint32, TransactionAbc[uint32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#179)

        Args:
            target: address
        Returns:
            uint32
        """
        return self._execute(self.chain, request_type, "4c1da1e2", [target], True if request_type == "tx" else False, uint32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getRoleAdmin(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint64:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#184)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        ...

    @overload
    def getRoleAdmin(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#184)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        ...

    @overload
    def getRoleAdmin(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#184)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        ...

    @overload
    def getRoleAdmin(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint64]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#184)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        ...

    def getRoleAdmin(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint64, TransactionAbc[uint64], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#184)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        return self._execute(self.chain, request_type, "530dd456", [roleId], True if request_type == "tx" else False, uint64, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getRoleGuardian(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint64:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#189)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        ...

    @overload
    def getRoleGuardian(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#189)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        ...

    @overload
    def getRoleGuardian(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#189)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        ...

    @overload
    def getRoleGuardian(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint64]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#189)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        ...

    def getRoleGuardian(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint64, TransactionAbc[uint64], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#189)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        return self._execute(self.chain, request_type, "0b0a93ba", [roleId], True if request_type == "tx" else False, uint64, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getRoleGrantDelay(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#194)

        Args:
            roleId: uint64
        Returns:
            uint32
        """
        ...

    @overload
    def getRoleGrantDelay(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#194)

        Args:
            roleId: uint64
        Returns:
            uint32
        """
        ...

    @overload
    def getRoleGrantDelay(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#194)

        Args:
            roleId: uint64
        Returns:
            uint32
        """
        ...

    @overload
    def getRoleGrantDelay(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#194)

        Args:
            roleId: uint64
        Returns:
            uint32
        """
        ...

    def getRoleGrantDelay(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint32, TransactionAbc[uint32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#194)

        Args:
            roleId: uint64
        Returns:
            uint32
        """
        return self._execute(self.chain, request_type, "12be8727", [roleId], True if request_type == "tx" else False, uint32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getAccess(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[uint48, uint32, uint32, uint48]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#199)

        Args:
            roleId: uint64
            account: address
        Returns:
            since: uint48
            currentDelay: uint32
            pendingDelay: uint32
            effect: uint48
        """
        ...

    @overload
    def getAccess(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#199)

        Args:
            roleId: uint64
            account: address
        Returns:
            since: uint48
            currentDelay: uint32
            pendingDelay: uint32
            effect: uint48
        """
        ...

    @overload
    def getAccess(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#199)

        Args:
            roleId: uint64
            account: address
        Returns:
            since: uint48
            currentDelay: uint32
            pendingDelay: uint32
            effect: uint48
        """
        ...

    @overload
    def getAccess(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[uint48, uint32, uint32, uint48]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#199)

        Args:
            roleId: uint64
            account: address
        Returns:
            since: uint48
            currentDelay: uint32
            pendingDelay: uint32
            effect: uint48
        """
        ...

    def getAccess(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[uint48, uint32, uint32, uint48], TransactionAbc[Tuple[uint48, uint32, uint32, uint48]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#199)

        Args:
            roleId: uint64
            account: address
        Returns:
            since: uint48
            currentDelay: uint32
            pendingDelay: uint32
            effect: uint48
        """
        return self._execute(self.chain, request_type, "3078f114", [roleId, account], True if request_type == "tx" else False, Tuple[uint48, uint32, uint32, uint48], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def hasRole(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[bool, uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#212)

        Args:
            roleId: uint64
            account: address
        Returns:
            isMember: bool
            executionDelay: uint32
        """
        ...

    @overload
    def hasRole(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#212)

        Args:
            roleId: uint64
            account: address
        Returns:
            isMember: bool
            executionDelay: uint32
        """
        ...

    @overload
    def hasRole(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#212)

        Args:
            roleId: uint64
            account: address
        Returns:
            isMember: bool
            executionDelay: uint32
        """
        ...

    @overload
    def hasRole(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[bool, uint32]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#212)

        Args:
            roleId: uint64
            account: address
        Returns:
            isMember: bool
            executionDelay: uint32
        """
        ...

    def hasRole(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[bool, uint32], TransactionAbc[Tuple[bool, uint32]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#212)

        Args:
            roleId: uint64
            account: address
        Returns:
            isMember: bool
            executionDelay: uint32
        """
        return self._execute(self.chain, request_type, "d1f856ee", [roleId, account], True if request_type == "tx" else False, Tuple[bool, uint32], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def labelRole(self, roleId: uint64, label: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#226)

        Args:
            roleId: uint64
            label: string
        """
        ...

    @overload
    def labelRole(self, roleId: uint64, label: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#226)

        Args:
            roleId: uint64
            label: string
        """
        ...

    @overload
    def labelRole(self, roleId: uint64, label: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#226)

        Args:
            roleId: uint64
            label: string
        """
        ...

    @overload
    def labelRole(self, roleId: uint64, label: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#226)

        Args:
            roleId: uint64
            label: string
        """
        ...

    def labelRole(self, roleId: uint64, label: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#226)

        Args:
            roleId: uint64
            label: string
        """
        return self._execute(self.chain, request_type, "853551b8", [roleId, label], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def grantRole(self, roleId: uint64, account: Union[Account, Address], executionDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#234)

        Args:
            roleId: uint64
            account: address
            executionDelay: uint32
        """
        ...

    @overload
    def grantRole(self, roleId: uint64, account: Union[Account, Address], executionDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#234)

        Args:
            roleId: uint64
            account: address
            executionDelay: uint32
        """
        ...

    @overload
    def grantRole(self, roleId: uint64, account: Union[Account, Address], executionDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#234)

        Args:
            roleId: uint64
            account: address
            executionDelay: uint32
        """
        ...

    @overload
    def grantRole(self, roleId: uint64, account: Union[Account, Address], executionDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#234)

        Args:
            roleId: uint64
            account: address
            executionDelay: uint32
        """
        ...

    def grantRole(self, roleId: uint64, account: Union[Account, Address], executionDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#234)

        Args:
            roleId: uint64
            account: address
            executionDelay: uint32
        """
        return self._execute(self.chain, request_type, "25c471a0", [roleId, account, executionDelay], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def revokeRole(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#239)

        Args:
            roleId: uint64
            account: address
        """
        ...

    @overload
    def revokeRole(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#239)

        Args:
            roleId: uint64
            account: address
        """
        ...

    @overload
    def revokeRole(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#239)

        Args:
            roleId: uint64
            account: address
        """
        ...

    @overload
    def revokeRole(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#239)

        Args:
            roleId: uint64
            account: address
        """
        ...

    def revokeRole(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#239)

        Args:
            roleId: uint64
            account: address
        """
        return self._execute(self.chain, request_type, "b7d2b162", [roleId, account], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def renounceRole(self, roleId: uint64, callerConfirmation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#244)

        Args:
            roleId: uint64
            callerConfirmation: address
        """
        ...

    @overload
    def renounceRole(self, roleId: uint64, callerConfirmation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#244)

        Args:
            roleId: uint64
            callerConfirmation: address
        """
        ...

    @overload
    def renounceRole(self, roleId: uint64, callerConfirmation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#244)

        Args:
            roleId: uint64
            callerConfirmation: address
        """
        ...

    @overload
    def renounceRole(self, roleId: uint64, callerConfirmation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#244)

        Args:
            roleId: uint64
            callerConfirmation: address
        """
        ...

    def renounceRole(self, roleId: uint64, callerConfirmation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#244)

        Args:
            roleId: uint64
            callerConfirmation: address
        """
        return self._execute(self.chain, request_type, "fe0776f5", [roleId, callerConfirmation], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setRoleAdmin(self, roleId: uint64, admin: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#252)

        Args:
            roleId: uint64
            admin: uint64
        """
        ...

    @overload
    def setRoleAdmin(self, roleId: uint64, admin: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#252)

        Args:
            roleId: uint64
            admin: uint64
        """
        ...

    @overload
    def setRoleAdmin(self, roleId: uint64, admin: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#252)

        Args:
            roleId: uint64
            admin: uint64
        """
        ...

    @overload
    def setRoleAdmin(self, roleId: uint64, admin: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#252)

        Args:
            roleId: uint64
            admin: uint64
        """
        ...

    def setRoleAdmin(self, roleId: uint64, admin: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#252)

        Args:
            roleId: uint64
            admin: uint64
        """
        return self._execute(self.chain, request_type, "30cae187", [roleId, admin], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setRoleGuardian(self, roleId: uint64, guardian: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#257)

        Args:
            roleId: uint64
            guardian: uint64
        """
        ...

    @overload
    def setRoleGuardian(self, roleId: uint64, guardian: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#257)

        Args:
            roleId: uint64
            guardian: uint64
        """
        ...

    @overload
    def setRoleGuardian(self, roleId: uint64, guardian: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#257)

        Args:
            roleId: uint64
            guardian: uint64
        """
        ...

    @overload
    def setRoleGuardian(self, roleId: uint64, guardian: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#257)

        Args:
            roleId: uint64
            guardian: uint64
        """
        ...

    def setRoleGuardian(self, roleId: uint64, guardian: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#257)

        Args:
            roleId: uint64
            guardian: uint64
        """
        return self._execute(self.chain, request_type, "52962952", [roleId, guardian], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setGrantDelay(self, roleId: uint64, newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#262)

        Args:
            roleId: uint64
            newDelay: uint32
        """
        ...

    @overload
    def setGrantDelay(self, roleId: uint64, newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#262)

        Args:
            roleId: uint64
            newDelay: uint32
        """
        ...

    @overload
    def setGrantDelay(self, roleId: uint64, newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#262)

        Args:
            roleId: uint64
            newDelay: uint32
        """
        ...

    @overload
    def setGrantDelay(self, roleId: uint64, newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#262)

        Args:
            roleId: uint64
            newDelay: uint32
        """
        ...

    def setGrantDelay(self, roleId: uint64, newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#262)

        Args:
            roleId: uint64
            newDelay: uint32
        """
        return self._execute(self.chain, request_type, "a64d95ce", [roleId, newDelay], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setTargetFunctionRole(self, target: Union[Account, Address], selectors: List[bytes4], roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#375)

        Args:
            target: address
            selectors: bytes4[]
            roleId: uint64
        """
        ...

    @overload
    def setTargetFunctionRole(self, target: Union[Account, Address], selectors: List[bytes4], roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#375)

        Args:
            target: address
            selectors: bytes4[]
            roleId: uint64
        """
        ...

    @overload
    def setTargetFunctionRole(self, target: Union[Account, Address], selectors: List[bytes4], roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#375)

        Args:
            target: address
            selectors: bytes4[]
            roleId: uint64
        """
        ...

    @overload
    def setTargetFunctionRole(self, target: Union[Account, Address], selectors: List[bytes4], roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#375)

        Args:
            target: address
            selectors: bytes4[]
            roleId: uint64
        """
        ...

    def setTargetFunctionRole(self, target: Union[Account, Address], selectors: List[bytes4], roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#375)

        Args:
            target: address
            selectors: bytes4[]
            roleId: uint64
        """
        return self._execute(self.chain, request_type, "08d6122d", [target, selectors, roleId], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setTargetAdminDelay(self, target: Union[Account, Address], newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#396)

        Args:
            target: address
            newDelay: uint32
        """
        ...

    @overload
    def setTargetAdminDelay(self, target: Union[Account, Address], newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#396)

        Args:
            target: address
            newDelay: uint32
        """
        ...

    @overload
    def setTargetAdminDelay(self, target: Union[Account, Address], newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#396)

        Args:
            target: address
            newDelay: uint32
        """
        ...

    @overload
    def setTargetAdminDelay(self, target: Union[Account, Address], newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#396)

        Args:
            target: address
            newDelay: uint32
        """
        ...

    def setTargetAdminDelay(self, target: Union[Account, Address], newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#396)

        Args:
            target: address
            newDelay: uint32
        """
        return self._execute(self.chain, request_type, "d22b5989", [target, newDelay], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setTargetClosed(self, target: Union[Account, Address], closed: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#414)

        Args:
            target: address
            closed: bool
        """
        ...

    @overload
    def setTargetClosed(self, target: Union[Account, Address], closed: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#414)

        Args:
            target: address
            closed: bool
        """
        ...

    @overload
    def setTargetClosed(self, target: Union[Account, Address], closed: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#414)

        Args:
            target: address
            closed: bool
        """
        ...

    @overload
    def setTargetClosed(self, target: Union[Account, Address], closed: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#414)

        Args:
            target: address
            closed: bool
        """
        ...

    def setTargetClosed(self, target: Union[Account, Address], closed: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#414)

        Args:
            target: address
            closed: bool
        """
        return self._execute(self.chain, request_type, "167bd395", [target, closed], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getSchedule(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint48:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#430)

        Args:
            id: bytes32
        Returns:
            uint48
        """
        ...

    @overload
    def getSchedule(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#430)

        Args:
            id: bytes32
        Returns:
            uint48
        """
        ...

    @overload
    def getSchedule(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#430)

        Args:
            id: bytes32
        Returns:
            uint48
        """
        ...

    @overload
    def getSchedule(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint48]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#430)

        Args:
            id: bytes32
        Returns:
            uint48
        """
        ...

    def getSchedule(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint48, TransactionAbc[uint48], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#430)

        Args:
            id: bytes32
        Returns:
            uint48
        """
        return self._execute(self.chain, request_type, "3adc277a", [id], True if request_type == "tx" else False, uint48, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getNonce(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#436)

        Args:
            id: bytes32
        Returns:
            uint32
        """
        ...

    @overload
    def getNonce(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#436)

        Args:
            id: bytes32
        Returns:
            uint32
        """
        ...

    @overload
    def getNonce(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#436)

        Args:
            id: bytes32
        Returns:
            uint32
        """
        ...

    @overload
    def getNonce(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#436)

        Args:
            id: bytes32
        Returns:
            uint32
        """
        ...

    def getNonce(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint32, TransactionAbc[uint32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#436)

        Args:
            id: bytes32
        Returns:
            uint32
        """
        return self._execute(self.chain, request_type, "4136a33c", [id], True if request_type == "tx" else False, uint32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def schedule(self, target: Union[Account, Address], data: Union[bytearray, bytes], when: uint48, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[bytes32, uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#441)

        Args:
            target: address
            data: bytes
            when: uint48
        Returns:
            operationId: bytes32
            nonce: uint32
        """
        ...

    @overload
    def schedule(self, target: Union[Account, Address], data: Union[bytearray, bytes], when: uint48, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#441)

        Args:
            target: address
            data: bytes
            when: uint48
        Returns:
            operationId: bytes32
            nonce: uint32
        """
        ...

    @overload
    def schedule(self, target: Union[Account, Address], data: Union[bytearray, bytes], when: uint48, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#441)

        Args:
            target: address
            data: bytes
            when: uint48
        Returns:
            operationId: bytes32
            nonce: uint32
        """
        ...

    @overload
    def schedule(self, target: Union[Account, Address], data: Union[bytearray, bytes], when: uint48, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[bytes32, uint32]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#441)

        Args:
            target: address
            data: bytes
            when: uint48
        Returns:
            operationId: bytes32
            nonce: uint32
        """
        ...

    def schedule(self, target: Union[Account, Address], data: Union[bytearray, bytes], when: uint48, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[bytes32, uint32], TransactionAbc[Tuple[bytes32, uint32]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#441)

        Args:
            target: address
            data: bytes
            when: uint48
        Returns:
            operationId: bytes32
            nonce: uint32
        """
        return self._execute(self.chain, request_type, "f801a698", [target, data, when], True if request_type == "tx" else False, Tuple[bytes32, uint32], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def execute(self, target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#493)

        Args:
            target: address
            data: bytes
        Returns:
            uint32
        """
        ...

    @overload
    def execute(self, target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#493)

        Args:
            target: address
            data: bytes
        Returns:
            uint32
        """
        ...

    @overload
    def execute(self, target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#493)

        Args:
            target: address
            data: bytes
        Returns:
            uint32
        """
        ...

    @overload
    def execute(self, target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#493)

        Args:
            target: address
            data: bytes
        Returns:
            uint32
        """
        ...

    def execute(self, target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint32, TransactionAbc[uint32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#493)

        Args:
            target: address
            data: bytes
        Returns:
            uint32
        """
        return self._execute(self.chain, request_type, "1cff79cd", [target, data], True if request_type == "tx" else False, uint32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def cancel(self, caller: Union[Account, Address], target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#527)

        Args:
            caller: address
            target: address
            data: bytes
        Returns:
            uint32
        """
        ...

    @overload
    def cancel(self, caller: Union[Account, Address], target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#527)

        Args:
            caller: address
            target: address
            data: bytes
        Returns:
            uint32
        """
        ...

    @overload
    def cancel(self, caller: Union[Account, Address], target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#527)

        Args:
            caller: address
            target: address
            data: bytes
        Returns:
            uint32
        """
        ...

    @overload
    def cancel(self, caller: Union[Account, Address], target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#527)

        Args:
            caller: address
            target: address
            data: bytes
        Returns:
            uint32
        """
        ...

    def cancel(self, caller: Union[Account, Address], target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint32, TransactionAbc[uint32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#527)

        Args:
            caller: address
            target: address
            data: bytes
        Returns:
            uint32
        """
        return self._execute(self.chain, request_type, "d6bb62c6", [caller, target, data], True if request_type == "tx" else False, uint32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def consumeScheduledOp(self, caller: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#551)

        Args:
            caller: address
            data: bytes
        """
        ...

    @overload
    def consumeScheduledOp(self, caller: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#551)

        Args:
            caller: address
            data: bytes
        """
        ...

    @overload
    def consumeScheduledOp(self, caller: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#551)

        Args:
            caller: address
            data: bytes
        """
        ...

    @overload
    def consumeScheduledOp(self, caller: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#551)

        Args:
            caller: address
            data: bytes
        """
        ...

    def consumeScheduledOp(self, caller: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#551)

        Args:
            caller: address
            data: bytes
        """
        return self._execute(self.chain, request_type, "94c7d7ee", [caller, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def hashOperation(self, caller: Union[Account, Address], target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#583)

        Args:
            caller: address
            target: address
            data: bytes
        Returns:
            bytes32
        """
        ...

    @overload
    def hashOperation(self, caller: Union[Account, Address], target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#583)

        Args:
            caller: address
            target: address
            data: bytes
        Returns:
            bytes32
        """
        ...

    @overload
    def hashOperation(self, caller: Union[Account, Address], target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#583)

        Args:
            caller: address
            target: address
            data: bytes
        Returns:
            bytes32
        """
        ...

    @overload
    def hashOperation(self, caller: Union[Account, Address], target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#583)

        Args:
            caller: address
            target: address
            data: bytes
        Returns:
            bytes32
        """
        ...

    def hashOperation(self, caller: Union[Account, Address], target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#583)

        Args:
            caller: address
            target: address
            data: bytes
        Returns:
            bytes32
        """
        return self._execute(self.chain, request_type, "abd9bd2a", [caller, target, data], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def updateAuthority(self, target: Union[Account, Address], newAuthority: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#589)

        Args:
            target: address
            newAuthority: address
        """
        ...

    @overload
    def updateAuthority(self, target: Union[Account, Address], newAuthority: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#589)

        Args:
            target: address
            newAuthority: address
        """
        ...

    @overload
    def updateAuthority(self, target: Union[Account, Address], newAuthority: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#589)

        Args:
            target: address
            newAuthority: address
        """
        ...

    @overload
    def updateAuthority(self, target: Union[Account, Address], newAuthority: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#589)

        Args:
            target: address
            newAuthority: address
        """
        ...

    def updateAuthority(self, target: Union[Account, Address], newAuthority: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/AccessManager.sol#589)

        Args:
            target: address
            newAuthority: address
        """
        return self._execute(self.chain, request_type, "18ff183c", [target, newAuthority], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

AccessManager.ADMIN_ROLE.selector = bytes4(b'u\xb28\xfc')
AccessManager.PUBLIC_ROLE.selector = bytes4(b'<\xa7\xc0*')
AccessManager.canCall.selector = bytes4(b'\xb7\x00\x96\x13')
AccessManager.expiration.selector = bytes4(b'Fe\tm')
AccessManager.minSetback.selector = bytes4(b'\xcc\x1bl\x81')
AccessManager.isTargetClosed.selector = bytes4(b'\xa1f\xaa\x89')
AccessManager.getTargetFunctionRole.selector = bytes4(b'mQ\x15\xbd')
AccessManager.getTargetAdminDelay.selector = bytes4(b'L\x1d\xa1\xe2')
AccessManager.getRoleAdmin.selector = bytes4(b'S\r\xd4V')
AccessManager.getRoleGuardian.selector = bytes4(b'\x0b\n\x93\xba')
AccessManager.getRoleGrantDelay.selector = bytes4(b"\x12\xbe\x87'")
AccessManager.getAccess.selector = bytes4(b'0x\xf1\x14')
AccessManager.hasRole.selector = bytes4(b'\xd1\xf8V\xee')
AccessManager.labelRole.selector = bytes4(b'\x855Q\xb8')
AccessManager.grantRole.selector = bytes4(b'%\xc4q\xa0')
AccessManager.revokeRole.selector = bytes4(b'\xb7\xd2\xb1b')
AccessManager.renounceRole.selector = bytes4(b'\xfe\x07v\xf5')
AccessManager.setRoleAdmin.selector = bytes4(b'0\xca\xe1\x87')
AccessManager.setRoleGuardian.selector = bytes4(b'R\x96)R')
AccessManager.setGrantDelay.selector = bytes4(b'\xa6M\x95\xce')
AccessManager.setTargetFunctionRole.selector = bytes4(b'\x08\xd6\x12-')
AccessManager.setTargetAdminDelay.selector = bytes4(b'\xd2+Y\x89')
AccessManager.setTargetClosed.selector = bytes4(b'\x16{\xd3\x95')
AccessManager.getSchedule.selector = bytes4(b":\xdc'z")
AccessManager.getNonce.selector = bytes4(b'A6\xa3<')
AccessManager.schedule.selector = bytes4(b'\xf8\x01\xa6\x98')
AccessManager.execute.selector = bytes4(b'\x1c\xffy\xcd')
AccessManager.cancel.selector = bytes4(b'\xd6\xbbb\xc6')
AccessManager.consumeScheduledOp.selector = bytes4(b'\x94\xc7\xd7\xee')
AccessManager.hashOperation.selector = bytes4(b'\xab\xd9\xbd*')
AccessManager.updateAuthority.selector = bytes4(b'\x18\xff\x18<')
