
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class IAccessManager(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#6)
    """
    _abi = {b'\x81>\x94Y': {'inputs': [{'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}], 'name': 'AccessManagerAlreadyScheduled', 'type': 'error'}, b'_\x15\x9ec': {'inputs': [], 'name': 'AccessManagerBadConfirmation', 'type': 'error'}, b'x\xa5\xd6\xe4': {'inputs': [{'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}], 'name': 'AccessManagerExpired', 'type': 'error'}, b'\x08\x13\xad\xa2': {'inputs': [{'internalType': 'address', 'name': 'initialAdmin', 'type': 'address'}], 'name': 'AccessManagerInvalidInitialAdmin', 'type': 'error'}, b'\x18q\xa9\x0c': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}], 'name': 'AccessManagerLockedRole', 'type': 'error'}, b'\x18\xcbkz': {'inputs': [{'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}], 'name': 'AccessManagerNotReady', 'type': 'error'}, b'`\xa2\x99\xb0': {'inputs': [{'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}], 'name': 'AccessManagerNotScheduled', 'type': 'error'}, b'\xf0~\x03\x8f': {'inputs': [{'internalType': 'address', 'name': 'msgsender', 'type': 'address'}, {'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}], 'name': 'AccessManagerUnauthorizedAccount', 'type': 'error'}, b'\x81\xc6\xf2K': {'inputs': [{'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes4', 'name': 'selector', 'type': 'bytes4'}], 'name': 'AccessManagerUnauthorizedCall', 'type': 'error'}, b'?\xe2u\x1c': {'inputs': [{'internalType': 'address', 'name': 'msgsender', 'type': 'address'}, {'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes4', 'name': 'selector', 'type': 'bytes4'}], 'name': 'AccessManagerUnauthorizedCancel', 'type': 'error'}, b'2\x0f\xf7H': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'AccessManagerUnauthorizedConsume', 'type': 'error'}, b"\xbd\x9a\xc6zn/dc\xb8\t'2c\x103\x8b\xcb\xb4\xbd\xb7\x93l\xe16^\xa3\xe0\x10g\xe7\xb9\xf7": {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'uint32', 'name': 'nonce', 'type': 'uint32'}], 'name': 'OperationCanceled', 'type': 'event'}, b'v\xa2\xa4iSh\x9dHa\xa5\xd3\xf6\xed\x88:\xd7\xe6\xafgJ!\xf8\xe1bpqY\xfc\x9d\xdeaM': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'uint32', 'name': 'nonce', 'type': 'uint32'}], 'name': 'OperationExecuted', 'type': 'event'}, b"\x82\xa2\xda]\xeeT\xea\x80!\xc6T[DDb\x02\x91\xe0~\xe8;\xe6\xddW\xed\xb1u\x06'\x15\xf3\xb4": {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'uint32', 'name': 'nonce', 'type': 'uint32'}, {'indexed': False, 'internalType': 'uint48', 'name': 'schedule', 'type': 'uint48'}, {'indexed': False, 'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'target', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'OperationScheduled', 'type': 'event'}, b'\x1f\xd6\xddv11-\xfa\xc2 [R\x91?\x99\xde\x03\xb4\xd7\xe3\x81\xd5\xd2}=\xbf\xe0q>nc@': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'indexed': True, 'internalType': 'uint64', 'name': 'admin', 'type': 'uint64'}], 'name': 'RoleAdminChanged', 'type': 'event'}, b'\xfe\xb6\x90\x18\xee\x8b\x8f\xd5\x0e\xa8cH\xf1&}\x07g3y\xf7,\xff\xde\xcc\xecc\x85>\xe8\xce\x8bH': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'indexed': False, 'internalType': 'uint32', 'name': 'delay', 'type': 'uint32'}, {'indexed': False, 'internalType': 'uint48', 'name': 'since', 'type': 'uint48'}], 'name': 'RoleGrantDelayChanged', 'type': 'event'}, b"\xf9\x84H\xb9\x87\xf1B\x8e\x0e#\x0e\x1f<n,\xe1[V\x93\xea\xf3\x18'\xfb\xd0\xb1\xecKBJ\xe7\xcf": {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'indexed': True, 'internalType': 'address', 'name': 'account', 'type': 'address'}, {'indexed': False, 'internalType': 'uint32', 'name': 'delay', 'type': 'uint32'}, {'indexed': False, 'internalType': 'uint48', 'name': 'since', 'type': 'uint48'}, {'indexed': False, 'internalType': 'bool', 'name': 'newMember', 'type': 'bool'}], 'name': 'RoleGranted', 'type': 'event'}, b'z\x80Yc\x0b\x89{]\xe4\xc0\x8a\xdei\xf8\xb9\x0c>\xad\x1f\x85\x96\xd6-\x10\xb6\xc4\xd1J\n\xfbJ\xe2': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'indexed': True, 'internalType': 'uint64', 'name': 'guardian', 'type': 'uint64'}], 'name': 'RoleGuardianChanged', 'type': 'event'}, b'\x12V\xf5\xb5\xec\xb8\x9c\xae\xc1-\xb4Is\x8f/\xbc\xd1\xbaX\x06\xcf8\xf3T\x13\xf4\xe5\xc1[\xf6\xa4P': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'indexed': False, 'internalType': 'string', 'name': 'label', 'type': 'string'}], 'name': 'RoleLabel', 'type': 'event'}, b'\xf2)\xba\xa5\x93\xaf(\xc4\x1b\x1d\x16\xb7H\xcdv\x88\xf0\xc8:\xaf\x92\xd4\xbeA\xc4@\x05\xde\xfe\x84\xc1f': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'indexed': True, 'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'RoleRevoked', 'type': 'event'}, b"\xa5kv\x01tS\xf3\x99\xec#'\xba\x007]\xbf\xb1\xfd\x07\x0f\xf8T4\x1a\xd6\x19\x1ej.-\xe1\x9c": {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'target', 'type': 'address'}, {'indexed': False, 'internalType': 'uint32', 'name': 'delay', 'type': 'uint32'}, {'indexed': False, 'internalType': 'uint48', 'name': 'since', 'type': 'uint48'}], 'name': 'TargetAdminDelayUpdated', 'type': 'event'}, b'\x90\xd4\xe7\xbb~]\x937\x92\xb3V.\x17A0o\x8b\xe9H7\xe14\x8d\xac\xef\x9bo\x1d\xf5n\xb18': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'target', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'closed', 'type': 'bool'}], 'name': 'TargetClosed', 'type': 'event'}, b'\x9e\xa6y\x0c}\xad\xfd\x01\xc9\xf8\xb9v+6\x82`z\xf2\xc7\xe7\x9e\x05\xa9\xf9\xfd\xf5X\r\xde\x94\x91Q': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'target', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes4', 'name': 'selector', 'type': 'bytes4'}, {'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}], 'name': 'TargetFunctionRoleUpdated', 'type': 'event'}, b'\xb7\x00\x96\x13': {'inputs': [{'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes4', 'name': 'selector', 'type': 'bytes4'}], 'name': 'canCall', 'outputs': [{'internalType': 'bool', 'name': 'allowed', 'type': 'bool'}, {'internalType': 'uint32', 'name': 'delay', 'type': 'uint32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd6\xbbb\xc6': {'inputs': [{'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'cancel', 'outputs': [{'internalType': 'uint32', 'name': '', 'type': 'uint32'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x94\xc7\xd7\xee': {'inputs': [{'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'consumeScheduledOp', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x1c\xffy\xcd': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'execute', 'outputs': [{'internalType': 'uint32', 'name': '', 'type': 'uint32'}], 'stateMutability': 'payable', 'type': 'function'}, b'Fe\tm': {'inputs': [], 'name': 'expiration', 'outputs': [{'internalType': 'uint32', 'name': '', 'type': 'uint32'}], 'stateMutability': 'view', 'type': 'function'}, b'0x\xf1\x14': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'getAccess', 'outputs': [{'internalType': 'uint48', 'name': 'since', 'type': 'uint48'}, {'internalType': 'uint32', 'name': 'currentDelay', 'type': 'uint32'}, {'internalType': 'uint32', 'name': 'pendingDelay', 'type': 'uint32'}, {'internalType': 'uint48', 'name': 'effect', 'type': 'uint48'}], 'stateMutability': 'view', 'type': 'function'}, b'A6\xa3<': {'inputs': [{'internalType': 'bytes32', 'name': 'id', 'type': 'bytes32'}], 'name': 'getNonce', 'outputs': [{'internalType': 'uint32', 'name': '', 'type': 'uint32'}], 'stateMutability': 'view', 'type': 'function'}, b'S\r\xd4V': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}], 'name': 'getRoleAdmin', 'outputs': [{'internalType': 'uint64', 'name': '', 'type': 'uint64'}], 'stateMutability': 'view', 'type': 'function'}, b"\x12\xbe\x87'": {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}], 'name': 'getRoleGrantDelay', 'outputs': [{'internalType': 'uint32', 'name': '', 'type': 'uint32'}], 'stateMutability': 'view', 'type': 'function'}, b'\x0b\n\x93\xba': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}], 'name': 'getRoleGuardian', 'outputs': [{'internalType': 'uint64', 'name': '', 'type': 'uint64'}], 'stateMutability': 'view', 'type': 'function'}, b":\xdc'z": {'inputs': [{'internalType': 'bytes32', 'name': 'id', 'type': 'bytes32'}], 'name': 'getSchedule', 'outputs': [{'internalType': 'uint48', 'name': '', 'type': 'uint48'}], 'stateMutability': 'view', 'type': 'function'}, b'L\x1d\xa1\xe2': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'getTargetAdminDelay', 'outputs': [{'internalType': 'uint32', 'name': '', 'type': 'uint32'}], 'stateMutability': 'view', 'type': 'function'}, b'mQ\x15\xbd': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes4', 'name': 'selector', 'type': 'bytes4'}], 'name': 'getTargetFunctionRole', 'outputs': [{'internalType': 'uint64', 'name': '', 'type': 'uint64'}], 'stateMutability': 'view', 'type': 'function'}, b'%\xc4q\xa0': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint32', 'name': 'executionDelay', 'type': 'uint32'}], 'name': 'grantRole', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd1\xf8V\xee': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'hasRole', 'outputs': [{'internalType': 'bool', 'name': 'isMember', 'type': 'bool'}, {'internalType': 'uint32', 'name': 'executionDelay', 'type': 'uint32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xab\xd9\xbd*': {'inputs': [{'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'hashOperation', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa1f\xaa\x89': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'isTargetClosed', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x855Q\xb8': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'internalType': 'string', 'name': 'label', 'type': 'string'}], 'name': 'labelRole', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xcc\x1bl\x81': {'inputs': [], 'name': 'minSetback', 'outputs': [{'internalType': 'uint32', 'name': '', 'type': 'uint32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xfe\x07v\xf5': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'internalType': 'address', 'name': 'callerConfirmation', 'type': 'address'}], 'name': 'renounceRole', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb7\xd2\xb1b': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'revokeRole', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf8\x01\xa6\x98': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'internalType': 'uint48', 'name': 'when', 'type': 'uint48'}], 'name': 'schedule', 'outputs': [{'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}, {'internalType': 'uint32', 'name': 'nonce', 'type': 'uint32'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa6M\x95\xce': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'internalType': 'uint32', 'name': 'newDelay', 'type': 'uint32'}], 'name': 'setGrantDelay', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'0\xca\xe1\x87': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'admin', 'type': 'uint64'}], 'name': 'setRoleAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'R\x96)R': {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'guardian', 'type': 'uint64'}], 'name': 'setRoleGuardian', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd2+Y\x89': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'uint32', 'name': 'newDelay', 'type': 'uint32'}], 'name': 'setTargetAdminDelay', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x16{\xd3\x95': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bool', 'name': 'closed', 'type': 'bool'}], 'name': 'setTargetClosed', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x08\xd6\x12-': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}, {'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}], 'name': 'setTargetFunctionRole', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x18\xff\x18<': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'address', 'name': 'newAuthority', 'type': 'address'}], 'name': 'updateAuthority', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> IAccessManager:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[IAccessManager]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, IAccessManager, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[IAccessManager]]:
        raise Exception("Cannot deploy interface")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an interface")

    @dataclasses.dataclass
    class AccessManagerAlreadyScheduled(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#78)

        Attributes:
            operationId (bytes32): bytes32
        """
        _abi = {'inputs': [{'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}], 'name': 'AccessManagerAlreadyScheduled', 'type': 'error'}
        original_name = 'AccessManagerAlreadyScheduled'
        selector = bytes4(b'\x81>\x94Y')

        operationId: bytes32


    @dataclasses.dataclass
    class AccessManagerNotScheduled(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#79)

        Attributes:
            operationId (bytes32): bytes32
        """
        _abi = {'inputs': [{'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}], 'name': 'AccessManagerNotScheduled', 'type': 'error'}
        original_name = 'AccessManagerNotScheduled'
        selector = bytes4(b'`\xa2\x99\xb0')

        operationId: bytes32


    @dataclasses.dataclass
    class AccessManagerNotReady(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#80)

        Attributes:
            operationId (bytes32): bytes32
        """
        _abi = {'inputs': [{'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}], 'name': 'AccessManagerNotReady', 'type': 'error'}
        original_name = 'AccessManagerNotReady'
        selector = bytes4(b'\x18\xcbkz')

        operationId: bytes32


    @dataclasses.dataclass
    class AccessManagerExpired(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#81)

        Attributes:
            operationId (bytes32): bytes32
        """
        _abi = {'inputs': [{'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}], 'name': 'AccessManagerExpired', 'type': 'error'}
        original_name = 'AccessManagerExpired'
        selector = bytes4(b'x\xa5\xd6\xe4')

        operationId: bytes32


    @dataclasses.dataclass
    class AccessManagerLockedRole(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#82)

        Attributes:
            roleId (uint64): uint64
        """
        _abi = {'inputs': [{'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}], 'name': 'AccessManagerLockedRole', 'type': 'error'}
        original_name = 'AccessManagerLockedRole'
        selector = bytes4(b'\x18q\xa9\x0c')

        roleId: uint64


    @dataclasses.dataclass
    class AccessManagerBadConfirmation(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#83)
        """
        _abi = {'inputs': [], 'name': 'AccessManagerBadConfirmation', 'type': 'error'}
        original_name = 'AccessManagerBadConfirmation'
        selector = bytes4(b'_\x15\x9ec')



    @dataclasses.dataclass
    class AccessManagerUnauthorizedAccount(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#84)

        Attributes:
            msgsender (Address): address
            roleId (uint64): uint64
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'msgsender', 'type': 'address'}, {'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}], 'name': 'AccessManagerUnauthorizedAccount', 'type': 'error'}
        original_name = 'AccessManagerUnauthorizedAccount'
        selector = bytes4(b'\xf0~\x03\x8f')

        msgsender: Address
        roleId: uint64


    @dataclasses.dataclass
    class AccessManagerUnauthorizedCall(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#85)

        Attributes:
            caller (Address): address
            target (Address): address
            selector_ (bytes4): bytes4
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes4', 'name': 'selector', 'type': 'bytes4'}], 'name': 'AccessManagerUnauthorizedCall', 'type': 'error'}
        original_name = 'AccessManagerUnauthorizedCall'
        selector = bytes4(b'\x81\xc6\xf2K')

        caller: Address
        target: Address
        selector_: bytes4 = dataclasses.field(metadata={"original_name": "selector"})


    @dataclasses.dataclass
    class AccessManagerUnauthorizedConsume(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#86)

        Attributes:
            target (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'AccessManagerUnauthorizedConsume', 'type': 'error'}
        original_name = 'AccessManagerUnauthorizedConsume'
        selector = bytes4(b'2\x0f\xf7H')

        target: Address


    @dataclasses.dataclass
    class AccessManagerUnauthorizedCancel(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#87)

        Attributes:
            msgsender (Address): address
            caller (Address): address
            target (Address): address
            selector_ (bytes4): bytes4
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'msgsender', 'type': 'address'}, {'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'bytes4', 'name': 'selector', 'type': 'bytes4'}], 'name': 'AccessManagerUnauthorizedCancel', 'type': 'error'}
        original_name = 'AccessManagerUnauthorizedCancel'
        selector = bytes4(b'?\xe2u\x1c')

        msgsender: Address
        caller: Address
        target: Address
        selector_: bytes4 = dataclasses.field(metadata={"original_name": "selector"})


    @dataclasses.dataclass
    class AccessManagerInvalidInitialAdmin(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#88)

        Attributes:
            initialAdmin (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'initialAdmin', 'type': 'address'}], 'name': 'AccessManagerInvalidInitialAdmin', 'type': 'error'}
        original_name = 'AccessManagerInvalidInitialAdmin'
        selector = bytes4(b'\x08\x13\xad\xa2')

        initialAdmin: Address


    @dataclasses.dataclass
    class OperationScheduled:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#10)

        Attributes:
            operationId (bytes32): indexed bytes32
            nonce (uint32): indexed uint32
            schedule (uint48): uint48
            caller (Address): address
            target (Address): address
            data (bytearray): bytes
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'uint32', 'name': 'nonce', 'type': 'uint32'}, {'indexed': False, 'internalType': 'uint48', 'name': 'schedule', 'type': 'uint48'}, {'indexed': False, 'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'target', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'OperationScheduled', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'OperationScheduled'
        selector = bytes32(b"\x82\xa2\xda]\xeeT\xea\x80!\xc6T[DDb\x02\x91\xe0~\xe8;\xe6\xddW\xed\xb1u\x06'\x15\xf3\xb4")

        operationId: bytes32
        nonce: uint32
        schedule: uint48
        caller: Address
        target: Address
        data: bytearray


    @dataclasses.dataclass
    class OperationExecuted:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#22)

        Attributes:
            operationId (bytes32): indexed bytes32
            nonce (uint32): indexed uint32
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'uint32', 'name': 'nonce', 'type': 'uint32'}], 'name': 'OperationExecuted', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'OperationExecuted'
        selector = bytes32(b'v\xa2\xa4iSh\x9dHa\xa5\xd3\xf6\xed\x88:\xd7\xe6\xafgJ!\xf8\xe1bpqY\xfc\x9d\xdeaM')

        operationId: bytes32
        nonce: uint32


    @dataclasses.dataclass
    class OperationCanceled:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#27)

        Attributes:
            operationId (bytes32): indexed bytes32
            nonce (uint32): indexed uint32
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'operationId', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'uint32', 'name': 'nonce', 'type': 'uint32'}], 'name': 'OperationCanceled', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'OperationCanceled'
        selector = bytes32(b"\xbd\x9a\xc6zn/dc\xb8\t'2c\x103\x8b\xcb\xb4\xbd\xb7\x93l\xe16^\xa3\xe0\x10g\xe7\xb9\xf7")

        operationId: bytes32
        nonce: uint32


    @dataclasses.dataclass
    class RoleLabel:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#32)

        Attributes:
            roleId (uint64): indexed uint64
            label (str): string
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'indexed': False, 'internalType': 'string', 'name': 'label', 'type': 'string'}], 'name': 'RoleLabel', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'RoleLabel'
        selector = bytes32(b'\x12V\xf5\xb5\xec\xb8\x9c\xae\xc1-\xb4Is\x8f/\xbc\xd1\xbaX\x06\xcf8\xf3T\x13\xf4\xe5\xc1[\xf6\xa4P')

        roleId: uint64
        label: str


    @dataclasses.dataclass
    class RoleGranted:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#41)

        Attributes:
            roleId (uint64): indexed uint64
            account (Address): indexed address
            delay (uint32): uint32
            since (uint48): uint48
            newMember (bool): bool
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'indexed': True, 'internalType': 'address', 'name': 'account', 'type': 'address'}, {'indexed': False, 'internalType': 'uint32', 'name': 'delay', 'type': 'uint32'}, {'indexed': False, 'internalType': 'uint48', 'name': 'since', 'type': 'uint48'}, {'indexed': False, 'internalType': 'bool', 'name': 'newMember', 'type': 'bool'}], 'name': 'RoleGranted', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'RoleGranted'
        selector = bytes32(b"\xf9\x84H\xb9\x87\xf1B\x8e\x0e#\x0e\x1f<n,\xe1[V\x93\xea\xf3\x18'\xfb\xd0\xb1\xecKBJ\xe7\xcf")

        roleId: uint64
        account: Address
        delay: uint32
        since: uint48
        newMember: bool


    @dataclasses.dataclass
    class RoleRevoked:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#46)

        Attributes:
            roleId (uint64): indexed uint64
            account (Address): indexed address
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'indexed': True, 'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'RoleRevoked', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'RoleRevoked'
        selector = bytes32(b'\xf2)\xba\xa5\x93\xaf(\xc4\x1b\x1d\x16\xb7H\xcdv\x88\xf0\xc8:\xaf\x92\xd4\xbeA\xc4@\x05\xde\xfe\x84\xc1f')

        roleId: uint64
        account: Address


    @dataclasses.dataclass
    class RoleAdminChanged:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#51)

        Attributes:
            roleId (uint64): indexed uint64
            admin (uint64): indexed uint64
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'indexed': True, 'internalType': 'uint64', 'name': 'admin', 'type': 'uint64'}], 'name': 'RoleAdminChanged', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'RoleAdminChanged'
        selector = bytes32(b'\x1f\xd6\xddv11-\xfa\xc2 [R\x91?\x99\xde\x03\xb4\xd7\xe3\x81\xd5\xd2}=\xbf\xe0q>nc@')

        roleId: uint64
        admin: uint64


    @dataclasses.dataclass
    class RoleGuardianChanged:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#56)

        Attributes:
            roleId (uint64): indexed uint64
            guardian (uint64): indexed uint64
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'indexed': True, 'internalType': 'uint64', 'name': 'guardian', 'type': 'uint64'}], 'name': 'RoleGuardianChanged', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'RoleGuardianChanged'
        selector = bytes32(b'z\x80Yc\x0b\x89{]\xe4\xc0\x8a\xdei\xf8\xb9\x0c>\xad\x1f\x85\x96\xd6-\x10\xb6\xc4\xd1J\n\xfbJ\xe2')

        roleId: uint64
        guardian: uint64


    @dataclasses.dataclass
    class RoleGrantDelayChanged:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#61)

        Attributes:
            roleId (uint64): indexed uint64
            delay (uint32): uint32
            since (uint48): uint48
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}, {'indexed': False, 'internalType': 'uint32', 'name': 'delay', 'type': 'uint32'}, {'indexed': False, 'internalType': 'uint48', 'name': 'since', 'type': 'uint48'}], 'name': 'RoleGrantDelayChanged', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'RoleGrantDelayChanged'
        selector = bytes32(b'\xfe\xb6\x90\x18\xee\x8b\x8f\xd5\x0e\xa8cH\xf1&}\x07g3y\xf7,\xff\xde\xcc\xecc\x85>\xe8\xce\x8bH')

        roleId: uint64
        delay: uint32
        since: uint48


    @dataclasses.dataclass
    class TargetClosed:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#66)

        Attributes:
            target (Address): indexed address
            closed (bool): bool
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'target', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'closed', 'type': 'bool'}], 'name': 'TargetClosed', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'TargetClosed'
        selector = bytes32(b'\x90\xd4\xe7\xbb~]\x937\x92\xb3V.\x17A0o\x8b\xe9H7\xe14\x8d\xac\xef\x9bo\x1d\xf5n\xb18')

        target: Address
        closed: bool


    @dataclasses.dataclass
    class TargetFunctionRoleUpdated:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#71)

        Attributes:
            target (Address): indexed address
            selector_ (bytes4): bytes4
            roleId (uint64): indexed uint64
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'target', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes4', 'name': 'selector', 'type': 'bytes4'}, {'indexed': True, 'internalType': 'uint64', 'name': 'roleId', 'type': 'uint64'}], 'name': 'TargetFunctionRoleUpdated', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'TargetFunctionRoleUpdated'
        selector = bytes32(b'\x9e\xa6y\x0c}\xad\xfd\x01\xc9\xf8\xb9v+6\x82`z\xf2\xc7\xe7\x9e\x05\xa9\xf9\xfd\xf5X\r\xde\x94\x91Q')

        target: Address
        selector_: bytes4 = dataclasses.field(metadata={"original_name": "selector"})
        roleId: uint64


    @dataclasses.dataclass
    class TargetAdminDelayUpdated:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#76)

        Attributes:
            target (Address): indexed address
            delay (uint32): uint32
            since (uint48): uint48
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'target', 'type': 'address'}, {'indexed': False, 'internalType': 'uint32', 'name': 'delay', 'type': 'uint32'}, {'indexed': False, 'internalType': 'uint48', 'name': 'since', 'type': 'uint48'}], 'name': 'TargetAdminDelayUpdated', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'TargetAdminDelayUpdated'
        selector = bytes32(b"\xa5kv\x01tS\xf3\x99\xec#'\xba\x007]\xbf\xb1\xfd\x07\x0f\xf8T4\x1a\xd6\x19\x1ej.-\xe1\x9c")

        target: Address
        delay: uint32
        since: uint48


    @overload
    def canCall(self, caller: Union[Account, Address], target: Union[Account, Address], selector: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[bool, uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#110)

        Args:
            caller: address
            target: address
            selector: bytes4
        Returns:
            allowed: bool
            delay: uint32
        """
        ...

    @overload
    def canCall(self, caller: Union[Account, Address], target: Union[Account, Address], selector: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#110)

        Args:
            caller: address
            target: address
            selector: bytes4
        Returns:
            allowed: bool
            delay: uint32
        """
        ...

    @overload
    def canCall(self, caller: Union[Account, Address], target: Union[Account, Address], selector: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#110)

        Args:
            caller: address
            target: address
            selector: bytes4
        Returns:
            allowed: bool
            delay: uint32
        """
        ...

    @overload
    def canCall(self, caller: Union[Account, Address], target: Union[Account, Address], selector: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[bool, uint32]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#110)

        Args:
            caller: address
            target: address
            selector: bytes4
        Returns:
            allowed: bool
            delay: uint32
        """
        ...

    def canCall(self, caller: Union[Account, Address], target: Union[Account, Address], selector: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[bool, uint32], TransactionAbc[Tuple[bool, uint32]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#110)

        Args:
            caller: address
            target: address
            selector: bytes4
        Returns:
            allowed: bool
            delay: uint32
        """
        return self._execute(self.chain, request_type, "b7009613", [caller, target, selector], True if request_type == "tx" else False, Tuple[bool, uint32], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def expiration(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#122)

        Returns:
            uint32
        """
        ...

    @overload
    def expiration(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#122)

        Returns:
            uint32
        """
        ...

    @overload
    def expiration(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#122)

        Returns:
            uint32
        """
        ...

    @overload
    def expiration(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#122)

        Returns:
            uint32
        """
        ...

    def expiration(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint32, TransactionAbc[uint32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#122)

        Returns:
            uint32
        """
        return self._execute(self.chain, request_type, "4665096d", [], True if request_type == "tx" else False, uint32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def minSetback(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#129)

        Returns:
            uint32
        """
        ...

    @overload
    def minSetback(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#129)

        Returns:
            uint32
        """
        ...

    @overload
    def minSetback(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#129)

        Returns:
            uint32
        """
        ...

    @overload
    def minSetback(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#129)

        Returns:
            uint32
        """
        ...

    def minSetback(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint32, TransactionAbc[uint32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#129)

        Returns:
            uint32
        """
        return self._execute(self.chain, request_type, "cc1b6c81", [], True if request_type == "tx" else False, uint32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def isTargetClosed(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#136)

        Args:
            target: address
        Returns:
            bool
        """
        ...

    @overload
    def isTargetClosed(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#136)

        Args:
            target: address
        Returns:
            bool
        """
        ...

    @overload
    def isTargetClosed(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#136)

        Args:
            target: address
        Returns:
            bool
        """
        ...

    @overload
    def isTargetClosed(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#136)

        Args:
            target: address
        Returns:
            bool
        """
        ...

    def isTargetClosed(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#136)

        Args:
            target: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "a166aa89", [target], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getTargetFunctionRole(self, target: Union[Account, Address], selector: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint64:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#141)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#141)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#141)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#141)

        Args:
            target: address
            selector: bytes4
        Returns:
            uint64
        """
        ...

    def getTargetFunctionRole(self, target: Union[Account, Address], selector: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint64, TransactionAbc[uint64], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#141)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#146)

        Args:
            target: address
        Returns:
            uint32
        """
        ...

    @overload
    def getTargetAdminDelay(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#146)

        Args:
            target: address
        Returns:
            uint32
        """
        ...

    @overload
    def getTargetAdminDelay(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#146)

        Args:
            target: address
        Returns:
            uint32
        """
        ...

    @overload
    def getTargetAdminDelay(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#146)

        Args:
            target: address
        Returns:
            uint32
        """
        ...

    def getTargetAdminDelay(self, target: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint32, TransactionAbc[uint32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#146)

        Args:
            target: address
        Returns:
            uint32
        """
        return self._execute(self.chain, request_type, "4c1da1e2", [target], True if request_type == "tx" else False, uint32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getRoleAdmin(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint64:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#154)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        ...

    @overload
    def getRoleAdmin(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#154)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        ...

    @overload
    def getRoleAdmin(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#154)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        ...

    @overload
    def getRoleAdmin(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint64]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#154)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        ...

    def getRoleAdmin(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint64, TransactionAbc[uint64], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#154)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        return self._execute(self.chain, request_type, "530dd456", [roleId], True if request_type == "tx" else False, uint64, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getRoleGuardian(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint64:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#161)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        ...

    @overload
    def getRoleGuardian(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#161)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        ...

    @overload
    def getRoleGuardian(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#161)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        ...

    @overload
    def getRoleGuardian(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint64]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#161)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        ...

    def getRoleGuardian(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint64, TransactionAbc[uint64], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#161)

        Args:
            roleId: uint64
        Returns:
            uint64
        """
        return self._execute(self.chain, request_type, "0b0a93ba", [roleId], True if request_type == "tx" else False, uint64, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getRoleGrantDelay(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#169)

        Args:
            roleId: uint64
        Returns:
            uint32
        """
        ...

    @overload
    def getRoleGrantDelay(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#169)

        Args:
            roleId: uint64
        Returns:
            uint32
        """
        ...

    @overload
    def getRoleGrantDelay(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#169)

        Args:
            roleId: uint64
        Returns:
            uint32
        """
        ...

    @overload
    def getRoleGrantDelay(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#169)

        Args:
            roleId: uint64
        Returns:
            uint32
        """
        ...

    def getRoleGrantDelay(self, roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint32, TransactionAbc[uint32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#169)

        Args:
            roleId: uint64
        Returns:
            uint32
        """
        return self._execute(self.chain, request_type, "12be8727", [roleId], True if request_type == "tx" else False, uint32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getAccess(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[uint48, uint32, uint32, uint48]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#182)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#182)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#182)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#182)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#182)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#191)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#191)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#191)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#191)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#191)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#202)

        Args:
            roleId: uint64
            label: string
        """
        ...

    @overload
    def labelRole(self, roleId: uint64, label: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#202)

        Args:
            roleId: uint64
            label: string
        """
        ...

    @overload
    def labelRole(self, roleId: uint64, label: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#202)

        Args:
            roleId: uint64
            label: string
        """
        ...

    @overload
    def labelRole(self, roleId: uint64, label: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#202)

        Args:
            roleId: uint64
            label: string
        """
        ...

    def labelRole(self, roleId: uint64, label: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#202)

        Args:
            roleId: uint64
            label: string
        """
        return self._execute(self.chain, request_type, "853551b8", [roleId, label], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def grantRole(self, roleId: uint64, account: Union[Account, Address], executionDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#224)

        Args:
            roleId: uint64
            account: address
            executionDelay: uint32
        """
        ...

    @overload
    def grantRole(self, roleId: uint64, account: Union[Account, Address], executionDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#224)

        Args:
            roleId: uint64
            account: address
            executionDelay: uint32
        """
        ...

    @overload
    def grantRole(self, roleId: uint64, account: Union[Account, Address], executionDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#224)

        Args:
            roleId: uint64
            account: address
            executionDelay: uint32
        """
        ...

    @overload
    def grantRole(self, roleId: uint64, account: Union[Account, Address], executionDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#224)

        Args:
            roleId: uint64
            account: address
            executionDelay: uint32
        """
        ...

    def grantRole(self, roleId: uint64, account: Union[Account, Address], executionDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#224)

        Args:
            roleId: uint64
            account: address
            executionDelay: uint32
        """
        return self._execute(self.chain, request_type, "25c471a0", [roleId, account, executionDelay], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def revokeRole(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#237)

        Args:
            roleId: uint64
            account: address
        """
        ...

    @overload
    def revokeRole(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#237)

        Args:
            roleId: uint64
            account: address
        """
        ...

    @overload
    def revokeRole(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#237)

        Args:
            roleId: uint64
            account: address
        """
        ...

    @overload
    def revokeRole(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#237)

        Args:
            roleId: uint64
            account: address
        """
        ...

    def revokeRole(self, roleId: uint64, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#237)

        Args:
            roleId: uint64
            account: address
        """
        return self._execute(self.chain, request_type, "b7d2b162", [roleId, account], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def renounceRole(self, roleId: uint64, callerConfirmation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#249)

        Args:
            roleId: uint64
            callerConfirmation: address
        """
        ...

    @overload
    def renounceRole(self, roleId: uint64, callerConfirmation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#249)

        Args:
            roleId: uint64
            callerConfirmation: address
        """
        ...

    @overload
    def renounceRole(self, roleId: uint64, callerConfirmation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#249)

        Args:
            roleId: uint64
            callerConfirmation: address
        """
        ...

    @overload
    def renounceRole(self, roleId: uint64, callerConfirmation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#249)

        Args:
            roleId: uint64
            callerConfirmation: address
        """
        ...

    def renounceRole(self, roleId: uint64, callerConfirmation: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#249)

        Args:
            roleId: uint64
            callerConfirmation: address
        """
        return self._execute(self.chain, request_type, "fe0776f5", [roleId, callerConfirmation], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setRoleAdmin(self, roleId: uint64, admin: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#260)

        Args:
            roleId: uint64
            admin: uint64
        """
        ...

    @overload
    def setRoleAdmin(self, roleId: uint64, admin: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#260)

        Args:
            roleId: uint64
            admin: uint64
        """
        ...

    @overload
    def setRoleAdmin(self, roleId: uint64, admin: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#260)

        Args:
            roleId: uint64
            admin: uint64
        """
        ...

    @overload
    def setRoleAdmin(self, roleId: uint64, admin: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#260)

        Args:
            roleId: uint64
            admin: uint64
        """
        ...

    def setRoleAdmin(self, roleId: uint64, admin: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#260)

        Args:
            roleId: uint64
            admin: uint64
        """
        return self._execute(self.chain, request_type, "30cae187", [roleId, admin], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setRoleGuardian(self, roleId: uint64, guardian: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#271)

        Args:
            roleId: uint64
            guardian: uint64
        """
        ...

    @overload
    def setRoleGuardian(self, roleId: uint64, guardian: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#271)

        Args:
            roleId: uint64
            guardian: uint64
        """
        ...

    @overload
    def setRoleGuardian(self, roleId: uint64, guardian: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#271)

        Args:
            roleId: uint64
            guardian: uint64
        """
        ...

    @overload
    def setRoleGuardian(self, roleId: uint64, guardian: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#271)

        Args:
            roleId: uint64
            guardian: uint64
        """
        ...

    def setRoleGuardian(self, roleId: uint64, guardian: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#271)

        Args:
            roleId: uint64
            guardian: uint64
        """
        return self._execute(self.chain, request_type, "52962952", [roleId, guardian], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setGrantDelay(self, roleId: uint64, newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#282)

        Args:
            roleId: uint64
            newDelay: uint32
        """
        ...

    @overload
    def setGrantDelay(self, roleId: uint64, newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#282)

        Args:
            roleId: uint64
            newDelay: uint32
        """
        ...

    @overload
    def setGrantDelay(self, roleId: uint64, newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#282)

        Args:
            roleId: uint64
            newDelay: uint32
        """
        ...

    @overload
    def setGrantDelay(self, roleId: uint64, newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#282)

        Args:
            roleId: uint64
            newDelay: uint32
        """
        ...

    def setGrantDelay(self, roleId: uint64, newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#282)

        Args:
            roleId: uint64
            newDelay: uint32
        """
        return self._execute(self.chain, request_type, "a64d95ce", [roleId, newDelay], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setTargetFunctionRole(self, target: Union[Account, Address], selectors: List[bytes4], roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#293)

        Args:
            target: address
            selectors: bytes4[]
            roleId: uint64
        """
        ...

    @overload
    def setTargetFunctionRole(self, target: Union[Account, Address], selectors: List[bytes4], roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#293)

        Args:
            target: address
            selectors: bytes4[]
            roleId: uint64
        """
        ...

    @overload
    def setTargetFunctionRole(self, target: Union[Account, Address], selectors: List[bytes4], roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#293)

        Args:
            target: address
            selectors: bytes4[]
            roleId: uint64
        """
        ...

    @overload
    def setTargetFunctionRole(self, target: Union[Account, Address], selectors: List[bytes4], roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#293)

        Args:
            target: address
            selectors: bytes4[]
            roleId: uint64
        """
        ...

    def setTargetFunctionRole(self, target: Union[Account, Address], selectors: List[bytes4], roleId: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#293)

        Args:
            target: address
            selectors: bytes4[]
            roleId: uint64
        """
        return self._execute(self.chain, request_type, "08d6122d", [target, selectors, roleId], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setTargetAdminDelay(self, target: Union[Account, Address], newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#304)

        Args:
            target: address
            newDelay: uint32
        """
        ...

    @overload
    def setTargetAdminDelay(self, target: Union[Account, Address], newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#304)

        Args:
            target: address
            newDelay: uint32
        """
        ...

    @overload
    def setTargetAdminDelay(self, target: Union[Account, Address], newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#304)

        Args:
            target: address
            newDelay: uint32
        """
        ...

    @overload
    def setTargetAdminDelay(self, target: Union[Account, Address], newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#304)

        Args:
            target: address
            newDelay: uint32
        """
        ...

    def setTargetAdminDelay(self, target: Union[Account, Address], newDelay: uint32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#304)

        Args:
            target: address
            newDelay: uint32
        """
        return self._execute(self.chain, request_type, "d22b5989", [target, newDelay], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setTargetClosed(self, target: Union[Account, Address], closed: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#317)

        Args:
            target: address
            closed: bool
        """
        ...

    @overload
    def setTargetClosed(self, target: Union[Account, Address], closed: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#317)

        Args:
            target: address
            closed: bool
        """
        ...

    @overload
    def setTargetClosed(self, target: Union[Account, Address], closed: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#317)

        Args:
            target: address
            closed: bool
        """
        ...

    @overload
    def setTargetClosed(self, target: Union[Account, Address], closed: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#317)

        Args:
            target: address
            closed: bool
        """
        ...

    def setTargetClosed(self, target: Union[Account, Address], closed: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#317)

        Args:
            target: address
            closed: bool
        """
        return self._execute(self.chain, request_type, "167bd395", [target, closed], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getSchedule(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint48:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#323)

        Args:
            id: bytes32
        Returns:
            uint48
        """
        ...

    @overload
    def getSchedule(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#323)

        Args:
            id: bytes32
        Returns:
            uint48
        """
        ...

    @overload
    def getSchedule(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#323)

        Args:
            id: bytes32
        Returns:
            uint48
        """
        ...

    @overload
    def getSchedule(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint48]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#323)

        Args:
            id: bytes32
        Returns:
            uint48
        """
        ...

    def getSchedule(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint48, TransactionAbc[uint48], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#323)

        Args:
            id: bytes32
        Returns:
            uint48
        """
        return self._execute(self.chain, request_type, "3adc277a", [id], True if request_type == "tx" else False, uint48, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getNonce(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#329)

        Args:
            id: bytes32
        Returns:
            uint32
        """
        ...

    @overload
    def getNonce(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#329)

        Args:
            id: bytes32
        Returns:
            uint32
        """
        ...

    @overload
    def getNonce(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#329)

        Args:
            id: bytes32
        Returns:
            uint32
        """
        ...

    @overload
    def getNonce(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#329)

        Args:
            id: bytes32
        Returns:
            uint32
        """
        ...

    def getNonce(self, id: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint32, TransactionAbc[uint32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#329)

        Args:
            id: bytes32
        Returns:
            uint32
        """
        return self._execute(self.chain, request_type, "4136a33c", [id], True if request_type == "tx" else False, uint32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def schedule(self, target: Union[Account, Address], data: Union[bytearray, bytes], when: uint48, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[bytes32, uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#346)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#346)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#346)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#346)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#346)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#361)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#361)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#361)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#361)

        Args:
            target: address
            data: bytes
        Returns:
            uint32
        """
        ...

    def execute(self, target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint32, TransactionAbc[uint32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#361)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#373)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#373)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#373)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#373)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#373)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#384)

        Args:
            caller: address
            data: bytes
        """
        ...

    @overload
    def consumeScheduledOp(self, caller: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#384)

        Args:
            caller: address
            data: bytes
        """
        ...

    @overload
    def consumeScheduledOp(self, caller: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#384)

        Args:
            caller: address
            data: bytes
        """
        ...

    @overload
    def consumeScheduledOp(self, caller: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#384)

        Args:
            caller: address
            data: bytes
        """
        ...

    def consumeScheduledOp(self, caller: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#384)

        Args:
            caller: address
            data: bytes
        """
        return self._execute(self.chain, request_type, "94c7d7ee", [caller, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def hashOperation(self, caller: Union[Account, Address], target: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#389)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#389)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#389)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#389)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#389)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#398)

        Args:
            target: address
            newAuthority: address
        """
        ...

    @overload
    def updateAuthority(self, target: Union[Account, Address], newAuthority: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#398)

        Args:
            target: address
            newAuthority: address
        """
        ...

    @overload
    def updateAuthority(self, target: Union[Account, Address], newAuthority: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#398)

        Args:
            target: address
            newAuthority: address
        """
        ...

    @overload
    def updateAuthority(self, target: Union[Account, Address], newAuthority: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#398)

        Args:
            target: address
            newAuthority: address
        """
        ...

    def updateAuthority(self, target: Union[Account, Address], newAuthority: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/access/manager/IAccessManager.sol#398)

        Args:
            target: address
            newAuthority: address
        """
        return self._execute(self.chain, request_type, "18ff183c", [target, newAuthority], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

IAccessManager.canCall.selector = bytes4(b'\xb7\x00\x96\x13')
IAccessManager.expiration.selector = bytes4(b'Fe\tm')
IAccessManager.minSetback.selector = bytes4(b'\xcc\x1bl\x81')
IAccessManager.isTargetClosed.selector = bytes4(b'\xa1f\xaa\x89')
IAccessManager.getTargetFunctionRole.selector = bytes4(b'mQ\x15\xbd')
IAccessManager.getTargetAdminDelay.selector = bytes4(b'L\x1d\xa1\xe2')
IAccessManager.getRoleAdmin.selector = bytes4(b'S\r\xd4V')
IAccessManager.getRoleGuardian.selector = bytes4(b'\x0b\n\x93\xba')
IAccessManager.getRoleGrantDelay.selector = bytes4(b"\x12\xbe\x87'")
IAccessManager.getAccess.selector = bytes4(b'0x\xf1\x14')
IAccessManager.hasRole.selector = bytes4(b'\xd1\xf8V\xee')
IAccessManager.labelRole.selector = bytes4(b'\x855Q\xb8')
IAccessManager.grantRole.selector = bytes4(b'%\xc4q\xa0')
IAccessManager.revokeRole.selector = bytes4(b'\xb7\xd2\xb1b')
IAccessManager.renounceRole.selector = bytes4(b'\xfe\x07v\xf5')
IAccessManager.setRoleAdmin.selector = bytes4(b'0\xca\xe1\x87')
IAccessManager.setRoleGuardian.selector = bytes4(b'R\x96)R')
IAccessManager.setGrantDelay.selector = bytes4(b'\xa6M\x95\xce')
IAccessManager.setTargetFunctionRole.selector = bytes4(b'\x08\xd6\x12-')
IAccessManager.setTargetAdminDelay.selector = bytes4(b'\xd2+Y\x89')
IAccessManager.setTargetClosed.selector = bytes4(b'\x16{\xd3\x95')
IAccessManager.getSchedule.selector = bytes4(b":\xdc'z")
IAccessManager.getNonce.selector = bytes4(b'A6\xa3<')
IAccessManager.schedule.selector = bytes4(b'\xf8\x01\xa6\x98')
IAccessManager.execute.selector = bytes4(b'\x1c\xffy\xcd')
IAccessManager.cancel.selector = bytes4(b'\xd6\xbbb\xc6')
IAccessManager.consumeScheduledOp.selector = bytes4(b'\x94\xc7\xd7\xee')
IAccessManager.hashOperation.selector = bytes4(b'\xab\xd9\xbd*')
IAccessManager.updateAuthority.selector = bytes4(b'\x18\xff\x18<')
