
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.forgestd.src.Test import Test



class StdStorageTest(Test):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#7)
    """
    _abi = {b'\x9c\x95U\xb1\xe3\x10.<\xf4\x8fB}y\xcbg\x8f]\x9b\xd1\xed\n\xd5t8\x94a\xe2U\xf9Qp\xed': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'who', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes4', 'name': 'fsig', 'type': 'bytes4'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'keysHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'slot', 'type': 'uint256'}], 'name': 'SlotFound', 'type': 'event'}, b'\x08\x0f\xc4\xa9f \xc4F.p[#\xf3FA?\xe3yk\xb6<o\x8d\x85\x91\xba\xec\x0e#\x15w\xa5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'who', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'slot', 'type': 'uint256'}], 'name': 'WARNING_UninitedSlot', 'type': 'event'}, b'A0O\xac\xd92=u\xb1\x1b\xcd\xd6\t\xcb8\xef\xff\xfd\xb0W\x10\xf7\xca\xf0\xe9\xb1lm\x9dp\x9fP': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log', 'type': 'event'}, b'z\xe7LRt\x14\xae\x13_\xd9pG\xb1)!\xa5\xec9\x11\xb8\x04\x19xU\xd6~%\xc7\xb7^\xe6\xf3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'log_address', 'type': 'event'}, b'\xfb\x10(e\xd5\n\xdd\xdd\xf6\x9d\xa9\xb5\xaa\x1b\xce\xd6l\x80\xcf\x86\x9a\\\x8d\x04q\xa4g\xe1\x8c\xe9\xca\xb1': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_array', 'type': 'event'}, b'\x89\n\x82g\x9bG\x0f+\xd8(\x16\xed\x9b\x16\x1f\x97\xd8\xb9g\xf3\x7f\xa3d|!\xd5\xbf9t\x9e-\xd5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_array', 'type': 'event'}, b'@\xe1\x84\x0fWi\x07=a\xbd\x017-\x9bu\xba\xa9\x84-V)\xa0\xc9\x9f\xf1\x03\xbe\x11x\xa8\xe9\xe2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_array', 'type': 'event'}, b'#\xb6*\xd0XM$\xa7_\x0b\xf3V\x03\x91\xefVY\xecm\xb1&\x9cV\xe1\x1a\xa2A\xd67\xf1\x9b ': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'log_bytes', 'type': 'event'}, b'\xe8\x16\x99\xb8Q\x13\xee\xa1\xc7>\x10X\x8b+\x03^U\x893ic!s\xaf\xd4?\xeb\x19/\xacd\xe3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'log_bytes32', 'type': 'event'}, b'\x0e\xb5\xd5&$\xc8\xd2\x8a\xda\x9f\xc5Z\x8cP.\xd5\xaa?\xbe/\xb6\xe9\x1bq\xb5\xf3v\x88+\x1d/\xb8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256', 'name': '', 'type': 'int256'}], 'name': 'log_int', 'type': 'event'}, b'\x9cN\x85A\xca\x8f\r\xc1\xc4\x13\xf9\x10\x8ff\xd8-<\xec\xb1\xbd\xdb\xceCza\xca\xa3\x17\\L\xc9o': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address', 'name': 'val', 'type': 'address'}], 'name': 'log_named_address', 'type': 'event'}, b'\x00\xaa\xa3\x9c\x9f\xfb_VzE48\x0cspup.\x1f\x7f\x14\x10\x7f\xc9S(\xe3\xb5l\x03%\xfb': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xa7>\xda\tf/F\xdd\xe7)\xbeF\x118_\xf3O\xe6\xc4O\xbb\xc6\xf7\xe1{\x04+Y\xa3D[W': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_named_array', 'type': 'event'}, b";\xcf\xb2\xae.\x8d\x13-\xd1\xfc\xe7\xcf'\x8a\x9a\x19uj\x9f\xce\xab\xe4p\xdf;\xda\xbbK\xc5w\xd1\xbd": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xd2n\x16\xca\xd4T\x87\x05\xe4\xc9\xe2\xd9O\x98\xee\x91\xc2\x89\x08^\xe4%YO\xd5c_\xa2\x96L\xcf\x18': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'val', 'type': 'bytes'}], 'name': 'log_named_bytes', 'type': 'event'}, b'\xaf\xb7\x95\xc9\xc6\x1eO\xe7F\x8c8o\x92]zT)\xec\xad\x9c\x04\x95\xdd\xb8\xd3\x8di\x06\x14\xd3/\x99': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'val', 'type': 'bytes32'}], 'name': 'log_named_bytes32', 'type': 'event'}, b']\xa6\xce\x9dQ\x15\x1b\xa1\x0c\t\xa5Y\xef$\xd5 \xb9\xda\xc5\xc5\xb8\x81\n\xe8CNM\r\x86A\x1a\x95': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_int', 'type': 'event'}, b"\xeb\x8b\xa4<\xedu7B\x19F\xbdC\xe8(\xb8\xb2\xb8B\x89'\xaa\x8f\x80\x1c\x13\xd94\xbf\x11\xac\xa5{": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_uint', 'type': 'event'}, b'/\xe62w\x91t7CxD*\x8e\x97\x8b\xcc\xfb\xdc\xc1\xd6\xb2\xb0\xd8\x1f~\x8e\xb7v\xab"\x86\xf1h': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}], 'name': 'log_named_int', 'type': 'event'}, b'(\x0fDF\xb2\x8a\x13rA}\xdae\x8d0\xb9[)\x92\xb1*\xc9\xc7\xf3xS_)\xa9z\xcf5\x83': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'val', 'type': 'string'}], 'name': 'log_named_string', 'type': 'event'}, b'\xb2\xde/\xbe\x80\x1a\r\xf6\xc0\xcb\xdd\xfdD\x8b\xa3\xc4\x1dH\xa0@\xca5\xc5l\x81\x96\xef\x0f\xca\xe7!\xa8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}], 'name': 'log_named_uint', 'type': 'event'}, b'\x0b.\x13\xff \xac{GA\x98eU\x83\xed\xf7\r\xed\xd2\xc1\xdc\x98\x0e2\x9cO\xbb/\xc0t\x8byk': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log_string', 'type': 'event'}, b',\xab\x97\x90Q\x0f\xd8\xbd\xfb\xd2\x11R\x88\xdb3\xfe\xc6f\x91\xd4v\xef\xc5B|\xfdL\ti0\x17U': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'log_uint', 'type': 'event'}, b"\xe7\x95\x0e\xde\x03\x94\xb9\xf2\xceJZ\x1b\xf5\xa7\xe1\x85$\x11\xf7\xe6f\x1bC\x08\xc9\x13\xc4\xbf\xd1\x10'\xe4": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'logs', 'type': 'event'}, b'\xfav&\xd4': {'inputs': [], 'name': 'IS_TEST', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb5P\x8a\xa9': {'inputs': [], 'name': 'excludeArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'excludedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe2\x0c\x9fq': {'inputs': [], 'name': 'excludeContracts', 'outputs': [{'internalType': 'address[]', 'name': 'excludedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb0FO\xdc': {'inputs': [], 'name': 'excludeSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'excludedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1e\xd7\x83\x1c': {'inputs': [], 'name': 'excludeSenders', 'outputs': [{'internalType': 'address[]', 'name': 'excludedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbaAO\xa6': {'inputs': [], 'name': 'failed', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'R\xe5*\xc6': {'inputs': [], 'name': 'readNonBoolValue', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\n\x92T\xe4': {'inputs': [], 'name': 'setUp', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'f\xd9\xa9\xa0': {'inputs': [], 'name': 'targetArtifactSelectors', 'outputs': [{'components': [{'internalType': 'string', 'name': 'artifact', 'type': 'string'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzArtifactSelector[]', 'name': 'targetedArtifactSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x85"l\x81': {'inputs': [], 'name': 'targetArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'targetedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'?r\x86\xf4': {'inputs': [], 'name': 'targetContracts', 'outputs': [{'internalType': 'address[]', 'name': 'targetedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'*\xde8\x80': {'inputs': [], 'name': 'targetInterfaces', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'string[]', 'name': 'artifacts', 'type': 'string[]'}], 'internalType': 'struct StdInvariant.FuzzInterface[]', 'name': 'targetedInterfaces_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x91j\x17\xc6': {'inputs': [], 'name': 'targetSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'targetedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'>^<#': {'inputs': [], 'name': 'targetSenders', 'outputs': [{'internalType': 'address[]', 'name': 'targetedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd9Rf\xeb': {'inputs': [], 'name': 'testEdgeCaseArray', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Y\x93w\xdd': {'inputs': [{'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'elemToGet', 'type': 'uint8'}], 'name': 'testFuzz_Packed', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'l\xc4\x87\x82': {'inputs': [{'internalType': 'uint256', 'name': 'nvars', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'seed', 'type': 'uint256'}], 'name': 'testFuzz_Packed2', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'/dN\x92': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'uint128', 'name': 'value', 'type': 'uint128'}], 'name': 'testFuzz_StorageCheckedWriteMapPacked', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'e\xbe\xe9I': {'inputs': [{'internalType': 'uint248', 'name': 'val1', 'type': 'uint248'}, {'internalType': 'uint248', 'name': 'val2', 'type': 'uint248'}, {'internalType': 'bool', 'name': 'boolVal1', 'type': 'bool'}, {'internalType': 'bool', 'name': 'boolVal2', 'type': 'bool'}], 'name': 'testFuzz_StorageNativePack', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xed`R\x9b': {'inputs': [], 'name': 'test_RevertIf_ReadingNonBoolValue', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b"\xeb\xef\xd7'": {'inputs': [], 'name': 'test_RevertStorageConst', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa2\x99\xaa^': {'inputs': [], 'name': 'test_StorageCheckedWriteDeepMap', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b';a\xa9P': {'inputs': [], 'name': 'test_StorageCheckedWriteDeepMapStructA', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb4t{ ': {'inputs': [], 'name': 'test_StorageCheckedWriteDeepMapStructB', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xe1fM\x98': {'inputs': [], 'name': 'test_StorageCheckedWriteHidden', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'mB+\xe6': {'inputs': [], 'name': 'test_StorageCheckedWriteMapAddr', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'M\xefd\xda': {'inputs': [], 'name': 'test_StorageCheckedWriteMapBool', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x05\xa7\xc0\xb4': {'inputs': [], 'name': 'test_StorageCheckedWriteMapPackedFullSuccess', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'I_\x07A': {'inputs': [], 'name': 'test_StorageCheckedWriteMapStructA', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'&\xd9}\x0b': {'inputs': [], 'name': 'test_StorageCheckedWriteMapStructB', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf2\xda\x110': {'inputs': [], 'name': 'test_StorageCheckedWriteMapUint', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xe8{\xfd\x9d': {'inputs': [], 'name': 'test_StorageCheckedWriteObvious', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x87\\\xeb\x10': {'inputs': [], 'name': 'test_StorageCheckedWriteSignedIntegerHidden', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Y\xfa\xf38': {'inputs': [], 'name': 'test_StorageCheckedWriteSignedIntegerObvious', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'm\xc32Q': {'inputs': [], 'name': 'test_StorageCheckedWriteStructA', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x89\xe6\xcf\xe4': {'inputs': [], 'name': 'test_StorageCheckedWriteStructB', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x84\x99\xd1\xab': {'inputs': [], 'name': 'test_StorageDeepMap', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'9.f\n': {'inputs': [], 'name': 'test_StorageDeepMapStructA', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xab\x86\x1d$': {'inputs': [], 'name': 'test_StorageDeepMapStructB', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xc7\x98\x03\xc3': {'inputs': [], 'name': 'test_StorageExtraSload', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b"\x96+'\xba": {'inputs': [], 'name': 'test_StorageHidden', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'lB\x8e\xf8': {'inputs': [], 'name': 'test_StorageMapAddrFound', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x03\x8c\xd1\x92': {'inputs': [], 'name': 'test_StorageMapAddrRoot', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'q\xe0\xa2T': {'inputs': [], 'name': 'test_StorageMapStructA', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xe9\x94\xe0\xb5': {'inputs': [], 'name': 'test_StorageMapStructB', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd8\xc1r\xbf': {'inputs': [], 'name': 'test_StorageMapUintFound', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'j\xf4\xe7\xbe': {'inputs': [], 'name': 'test_StorageObvious', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xe1\xb9C\xa2': {'inputs': [], 'name': 'test_StorageReadAddress', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xed\xf3\xc6\x9a': {'inputs': [], 'name': 'test_StorageReadBool_False', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd8\xe2LC': {'inputs': [], 'name': 'test_StorageReadBool_True', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'7\x9aB\xae': {'inputs': [], 'name': 'test_StorageReadBytes32', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x97\x92Fk': {'inputs': [], 'name': 'test_StorageReadInt', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf1]So': {'inputs': [], 'name': 'test_StorageReadUint', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf7:\xa1\x9a': {'inputs': [], 'name': 'test_StorageStructA', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'J\xca\xea\x91': {'inputs': [], 'name': 'test_StorageStructB', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":46,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"stdstore","offset":0,"slot":0,"type":"t_struct(StdStorage)8331_storage"},{"astId":209,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_failed","offset":0,"slot":8,"type":"t_bool"},{"astId":2943,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"stdChainsInitialized","offset":1,"slot":8,"type":"t_bool"},{"astId":2964,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"chains","offset":0,"slot":9,"type":"t_mapping(t_string_memory_ptr,t_struct(Chain)2959_storage)"},{"astId":2968,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"defaultRpcUrls","offset":0,"slot":10,"type":"t_mapping(t_string_memory_ptr,t_string_storage)"},{"astId":2972,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"idToAlias","offset":0,"slot":11,"type":"t_mapping(t_uint256,t_string_storage)"},{"astId":2975,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"fallbackToDefaultRpcUrls","offset":0,"slot":12,"type":"t_bool"},{"astId":3931,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"gasMeteringOff","offset":1,"slot":12,"type":"t_bool"},{"astId":6002,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"stdstore","offset":0,"slot":13,"type":"t_struct(StdStorage)8331_storage"},{"astId":6923,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_excludedContracts","offset":0,"slot":21,"type":"t_array(t_address)dyn_storage"},{"astId":6926,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_excludedSenders","offset":0,"slot":22,"type":"t_array(t_address)dyn_storage"},{"astId":6929,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_targetedContracts","offset":0,"slot":23,"type":"t_array(t_address)dyn_storage"},{"astId":6932,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_targetedSenders","offset":0,"slot":24,"type":"t_array(t_address)dyn_storage"},{"astId":6935,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_excludedArtifacts","offset":0,"slot":25,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6938,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_targetedArtifacts","offset":0,"slot":26,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6942,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_targetedArtifactSelectors","offset":0,"slot":27,"type":"t_array(t_struct(FuzzArtifactSelector)6914_storage)dyn_storage"},{"astId":6946,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_excludedSelectors","offset":0,"slot":28,"type":"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage"},{"astId":6950,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_targetedSelectors","offset":0,"slot":29,"type":"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage"},{"astId":6954,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_targetedInterfaces","offset":0,"slot":30,"type":"t_array(t_struct(FuzzInterface)6920_storage)dyn_storage"},{"astId":13223,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"IS_TEST","offset":0,"slot":31,"type":"t_bool"},{"astId":39821,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"test","offset":1,"slot":31,"type":"t_contract(StorageTest)42383"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_address)dyn_storage":{"encoding":"dynamic_array","label":"address[]","numberOfBytes":32,"base":"t_address"},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_array(t_bytes4)dyn_storage":{"encoding":"dynamic_array","label":"bytes4[]","numberOfBytes":32,"base":"t_bytes4"},"t_array(t_string_storage)dyn_storage":{"encoding":"dynamic_array","label":"string[]","numberOfBytes":32,"base":"t_string_storage"},"t_array(t_struct(FuzzArtifactSelector)6914_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzArtifactSelector[]","numberOfBytes":32,"base":"t_struct(FuzzArtifactSelector)6914_storage"},"t_array(t_struct(FuzzInterface)6920_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzInterface[]","numberOfBytes":32,"base":"t_struct(FuzzInterface)6920_storage"},"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzSelector[]","numberOfBytes":32,"base":"t_struct(FuzzSelector)6908_storage"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_contract(StorageTest)42383":{"encoding":"inplace","label":"contract StorageTest","numberOfBytes":20},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))"},"t_mapping(t_bytes32,t_struct(FindData)8306_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)8306_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)8306_storage)"},"t_mapping(t_string_memory_ptr,t_string_storage)":{"encoding":"mapping","label":"mapping(string => string)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_string_storage"},"t_mapping(t_string_memory_ptr,t_struct(Chain)2959_storage)":{"encoding":"mapping","label":"mapping(string => struct StdChains.Chain)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_struct(Chain)2959_storage"},"t_mapping(t_uint256,t_string_storage)":{"encoding":"mapping","label":"mapping(uint256 => string)","numberOfBytes":32,"key":"t_uint256","value":"t_string_storage"},"t_string_memory_ptr":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(Chain)2959_storage":{"encoding":"inplace","label":"struct StdChains.Chain","numberOfBytes":128,"members":[{"astId":2952,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"name","offset":0,"slot":0,"type":"t_string_storage"},{"astId":2954,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"chainId","offset":0,"slot":1,"type":"t_uint256"},{"astId":2956,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"chainAlias","offset":0,"slot":2,"type":"t_string_storage"},{"astId":2958,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"rpcUrl","offset":0,"slot":3,"type":"t_string_storage"}]},"t_struct(FindData)8306_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":8299,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":8301,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":8303,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":8305,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(FuzzArtifactSelector)6914_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzArtifactSelector","numberOfBytes":64,"members":[{"astId":6910,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"artifact","offset":0,"slot":0,"type":"t_string_storage"},{"astId":6913,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(FuzzInterface)6920_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzInterface","numberOfBytes":64,"members":[{"astId":6916,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6919,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"artifacts","offset":0,"slot":1,"type":"t_array(t_string_storage)dyn_storage"}]},"t_struct(FuzzSelector)6908_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzSelector","numberOfBytes":64,"members":[{"astId":6904,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6907,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(StdStorage)8331_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":8315,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))"},{"astId":8318,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":8320,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":8322,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":8324,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":8326,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":8328,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":8330,"contract":"lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60808060405234602f57600160ff19600c541617600c55600160ff19601f541617601f5561891290816100348239f35b5f80fdfe60806040526004361015610011575f80fd5b5f5f3560e01c8063038cd1921461352d57806305a7c0b4146133375780630a9254e4146132d05780631ed7831c1461325257806326d97d0b146131845780632ade388014612fc55780632f644e9214612df1578063379a42ae14612d12578063392e660a14612c5e5780633b61a95014612b7d5780633e5e3c2314612aff5780633f7286f414612a81578063495f0741146129af5780634acaea91146128fa5780634def64da146127bd57806352e52ac61461276b578063599377dd1461234157806359faf338146122b057806365bee94914611f6757806366d9a9a014611e3e5780636af4e7be14611dc35780636c428ef814611d435780636cc48782146118fa5780636d422be61461185a5780636dc332511461179757806371e0a254146117135780638499d1ab1461167157806385226c81146115dd578063875ceb101461151757806389e6cfe414611453578063916a17c6146113ab578063962b27ba1461129d5780639792466b146111d1578063a299aa5e14611121578063ab861d2414611057578063b0464fdc14610faf578063b4747b2014610ebd578063b5508aa914610e22578063ba414fa614610dfd578063c79803c314610d4d578063d8c172bf14610cc5578063d8e24c4314610c14578063d95266eb14610ac7578063e1664d9814610a36578063e1b943a21461095e578063e20c9f71146108d0578063e87bfd9d1461080a578063e994e0b51461075c578063ebefd7271461063e578063ed60529b1461056a578063edf3c69a146104bd578063f15d536f1461044d578063f2da11301461036d578063f73aa19a1461029c5763fa7626d414610277575f80fd5b34610299578060031936011261029957602060ff601f54166040519015158152f35b80fd5b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff19166315e8b345179055806003556102f261568e565b5480600703610300575b5080f35b5f51602061887d5f395f51905f523b15610369576040519063260a5b1560e21b82526007600483015260248201525f816044815f51602061887d5f395f51905f525afa801561035e57610351575080f35b5f61035b91613b1b565b80f35b6040513d5f823e3d90fd5b5f80fd5b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916636a56c3d41790556103bf614540565b6103c7614a12565b601f54604051631a95b0f560e21b815260646004820152906020908290602490829060081c6001600160a01b03165afa801561044257829061040e575b61035b91506141c0565b506020813d60201161043a575b8161042860209383613b1b565b810103126103695761035b9051610404565b3d915061041b565b6040513d84823e3d90fd5b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663267c4ae417905561049f6168db565b602081519181808201938492010103126103695761035b90516142cf565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff19166357351c4517905561050f61540d565b15158061051a575080f35b5f51602061887d5f395f51905f523b15610369576040519063f7fe347760e01b825260048201525f60248201525f816044815f51602061887d5f395f51905f525afa801561035e57610351575080f35b50346102995780600319360112610299575f51602061887d5f395f51905f523b156102995760405163f28dceb360e01b815260206004820152605260248201526105b660448201614043565b81808260a481835f51602061887d5f395f51905f525af1801561061a57610627575b5050303b1561029957604051632972956360e11b815281808260048183305af1801561061a576106055780f35b61060e91613b1b565b805f12610299575f8180f35b50604051903d90823e3d90fd5b61063091613b1b565b805f12610299575f816105d8565b5034610299578060031936011261029957601f54604051611092808201939260081c6001600160a01b0316906001600160401b0385118386101761074857839460209284926177cb8439815203019082f0801561061a575f51602061887d5f395f51905f523b156107235760405163f28dceb360e01b8152602060048201528281806106cc60248201613fec565b0381835f51602061887d5f395f51905f525af1801561073d578390610726575b50506001600160a01b0316803b156107235781809160046040518095819363fc5aec2b60e01b83525af1801561061a576106055780f35b50fd5b61072f91613b1b565b815f12610723575f826106ec565b6040513d85823e3d90fd5b634e487b7160e01b84526041600452602484fd5b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663504429bf1790556107af3061450c565b60016003556107bc61568e565b54604051602081019030825260046040820152604081526107de606082613b1b565b519020600181018091116107f6579061035b9161432a565b634e487b7160e01b83526011600452602483fd5b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663267c4ae417905561085c614a12565b601f5460405163099f12b960e21b8152906020908290600490829060081c6001600160a01b03165afa801561044257829061089c575b61035b9150614165565b506020813d6020116108c8575b816108b660209383613b1b565b810103126103695761035b9051610892565b3d91506108a9565b503461029957806003193601126102995760405160158054808352908352909160208301917f55f448fdea98c4d29eb340757ef0a66cd03dbb9538908a6a81d96026b71ec475915b81811061093f5761093b8561092f81870382613b1b565b6040519182918261396c565b0390f35b82546001600160a01b0316845260209093019260019283019201610918565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff19166308f23aad1790556109b06168db565b602081805181010312610a3257602001516001600160a01b03811690819003610a325761053981036109e0575080f35b5f51602061887d5f395f51905f523b1561036957604051906328a9b0fb60e11b8252600482015261053960248201525f816044815f51602061887d5f395f51905f525afa801561035e57610351575080f35b5080fd5b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663aef6d4b1179055610a88614a12565b601f5460405163aef6d4b160e01b8152906020908290600490829060081c6001600160a01b03165afa801561044257829061089c5761035b9150614165565b503461029957806003193601126102995760018060a01b03601f5460081c1660018060a01b03196004541617600455610b3f6020604051610b09604082613b1b565b6016815275656467654361736541727261792875696e743235362960501b9101526002805463ffffffff191663e92e9dc4179055565b600154600160401b811015610c00576001810180600155811015610bec575f9060018252602082200155610b71614d66565b601f54604051633a4ba77160e21b815260048101839052906020908290602490829060081c6001600160a01b03165afa8015610442578290610bb8575b61035b91506142cf565b506020813d602011610be4575b81610bd260209383613b1b565b810103126103695761035b9051610bae565b3d9150610bc5565b634e487b7160e01b5f52603260045260245ffd5b634e487b7160e01b5f52604160045260245ffd5b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916634f87aeb7179055610c6661540d565b151560018103610c74575080f35b5f51602061887d5f395f51905f523b15610369576040519063f7fe347760e01b82526004820152600160248201525f816044815f51602061887d5f395f51905f525afa801561035e57610351575080f35b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916636a56c3d4179055610d17614540565b61035b610d2261568e565b546040516020810190606482526002604082015260408152610d45606082613b1b565b51902061432a565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916639e7936e6179055610d9f61568e565b5480601003610dac575080f35b5f51602061887d5f395f51905f523b15610369576040519063260a5b1560e21b82526010600483015260248201525f816044815f51602061887d5f395f51905f525afa801561035e57610351575080f35b50346102995780600319360112610299576020610e18613f51565b6040519015158152f35b5034610299578060031936011261029957601954610e3f81613b52565b90610e4d6040519283613b1b565b80825260195f9081527f944998273e477b495144fb8794c914197f3ccb46be2900f4698fd0ef743c9695602084015b838310610e91576040518061093b8782613a0f565b600160208192604051610eaf81610ea88189613ba1565b0382613b1b565b815201920192019190610e7c565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916630310c060179055610f103061450c565b610f193061450c565b6001600355610f26614a12565b601f54604080516218860360e51b815291829060081c6001600160a01b03168180610f55308060048401613c5e565b03915afa80156104425761035b9183908492610f7b575b50610f769061421b565b6141c0565b610f769250610fa2915060403d604011610fa8575b610f9a8183613b1b565b810190613b3c565b91610f6c565b503d610f90565b5034610299578060031936011261029957601c54610fcc81613b52565b91610fda6040519384613b1b565b818352601c81527f0e4562a10381dec21b205ed72637e6b1b523bdd0e4d4d50af5cd23dd4500a211602084015b83831061101c576040518061093b8782613a6e565b6002602060019260405161102f81613ae5565b848060a01b038654168152611045858701613d12565b83820152815201920192019190611007565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916630310c0601790556110aa3061450c565b6110b33061450c565b60016003556110c061568e565b54604051602081019030825260066040820152604081526110e2606082613b1b565b519020604051611109816110fb60208201943086613c22565b03601f198101835282613b1b565b519020600181018091116107f6579061035b91614384565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916638cd8156d1790556111743061450c565b61117d3061450c565b611185614a12565b601f54604051638cd8156d60e01b815290602090829060081c6001600160a01b031681806111b7308060048401613c5e565b03915afa801561044257829061040e5761035b91506141c0565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663e5ed1efe1790556112236168db565b602081519181808201938492010103126103695751600160ff1b8101611247575080f35b5f51602061887d5f395f51905f523b156103695760405163fe74f05b60e01b81526004810191909152600160ff1b60248201525f816044815f51602061887d5f395f51905f525afa801561035e57610351575080f35b503461029957806003193601126102995760018060a01b03601f5460081c1660018060a01b0319600454161760045561130760206040516112df604082613b1b565b600881526768696464656e282960c01b9101526002805463ffffffff191663aef6d4b1179055565b61130f61568e565b54807fb27fb258786eae8f9ffde06a5bfd55f5193cb73bd64e533d5d75fd7cb46652ff0361133b575080f35b5f51602061887d5f395f51905f523b15610369576040519063260a5b1560e21b82527fb27fb258786eae8f9ffde06a5bfd55f5193cb73bd64e533d5d75fd7cb46652ff600483015260248201525f816044815f51602061887d5f395f51905f525afa801561035e57610351575080f35b5034610299578060031936011261029957601d546113c881613b52565b916113d66040519384613b1b565b818352601d81527f6d4407e7be21f808e6509aa9fa9143369579dd7d760fe20a2c09680fc146134f602084015b838310611418576040518061093b8782613a6e565b6002602060019260405161142b81613ae5565b848060a01b038654168152611441858701613d12565b83820152815201920192019190611403565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff19166315e8b34517905560016003556114aa614a12565b601f54604080516315e8b34560e01b8152918290600490829060081c6001600160a01b03165afa80156104425761035b91839084926114f3575b506114ee90614272565b614165565b6114ee9250611511915060403d604011610fa857610f9a8183613b1b565b916114e4565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663aef6d4b11790556115696150b9565b601f5460405163aef6d4b160e01b8152906020908290600490829060081c6001600160a01b03165afa80156104425782906115a9575b61035b9150614450565b506020813d6020116115d5575b816115c360209383613b1b565b810103126103695761035b905161159f565b3d91506115b6565b5034610299578060031936011261029957601a546115fa81613b52565b906116086040519283613b1b565b808252601a5f9081527f057c384a7d1c54f3a1b2e5e67b2617b8224fdfd1ea7234eea573a6ff665ff63e602084015b83831061164c576040518061093b8782613a0f565b60016020819260405161166381610ea88189613ba1565b815201920192019190611637565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916638cd8156d1790556116c43061450c565b6116cd3061450c565b61035b6116d861568e565b54604051602081019030825260056040820152604081526116fa606082613b1b565b519020604051610d45816110fb60208201943086613c22565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663504429bf1790556117663061450c565b8060035561035b61177561568e565b5460405160208101903082526004604082015260408152610d45606082613b1b565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff19166315e8b345179055806003556117ed614a12565b601f54604080516315e8b34560e01b8152918290600490829060081c6001600160a01b03165afa80156104425761035b9183908492611836575b5061183190614165565b614272565b6118319250611854915060403d604011610fa857610f9a8183613b1b565b91611827565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663a73e40cc1790556118ad3061450c565b6118b5614a12565b601f546040516329cf903360e21b8152306004820152906020908290602490829060081c6001600160a01b03165afa801561044257829061040e5761035b91506141c0565b50346102995760403660031901126102995760243561191e6014600160043561548b565b60405f80825161192e8482613b1b565b600c81526b109bdd5b99081c995cdd5b1d60a21b602082015283516119838161196f6020820194632d839cb360e21b865288602484015260648301906139ae565b88604483015203601f198101835282613b1b565b51906a636f6e736f6c652e6c6f675afa50610100926119a183613c92565b936119ab84613c92565b906119b585613c92565b9287915b868310611ba257505050855b848110611b395750855b8481106119da578680f35b6006805460ff19166001179055601f54600480546001600160a01b03191660089290921c6001600160a01b0316919091179055611a3c611a18613f16565b63ffffffff60e01b90602081519101201660e01c63ffffffff196002541617600255565b611a4f611a498284613cc4565b5161450c565b611a5c611a498285613cc4565b611a646168db565b602081519181808201938492010103126103695751601f5490919060081c6001600160a01b03166020611a978386613cc4565b516044611aa48589613cc4565b5191895194859384926306aa112d60e21b8452600484015260248301525afa908115611b2f578991611afd575b50611af790611aed600194611ae6858c613cc4565b519061432a565b611ae6838a613cc4565b016119cf565b90506020813d8211611b27575b81611b1760209383613b1b565b8101031261036957516001611ad1565b3d9150611b0a565b86513d8b823e3d90fd5b6001908160ff196006541617600655818060a01b03601f5460081c16828060a01b03196004541617600455611b6f611a18613f16565b611b7c611a498285613cc4565b611b89611a498286613cc4565b611b9c611b968289613cc4565b516145cf565b016119c5565b82611d1357885b611bb38487613cc4565b52611bc7611bc18489613c85565b82613c85565b60018101809111611cff576101008401808511611ceb5791611c0e611ca092600180958b5160208101918983528d8201528c8152611c06606082613b1b565b51902061548b565b5f808a611c5f611c738251611c238482613b1b565b600c81526b109bdd5b99081c995cdd5b1d60a21b602082015283519283916020830195632d839cb360e21b8752602484015260648301906139ae565b87604483015203601f198101835282613b1b565b51906a636f6e736f6c652e6c6f675afa50611c8e8688613cc4565b52611c998587613cc4565b5190613c85565b92611cd95f1983611cb18489613cc4565b511b0188516020810190868252848b8201528a8152611cd1606082613b1b565b5190206143de565b611ce3828b613cc4565b5201916119b9565b634e487b7160e01b8b52601160045260248bfd5b634e487b7160e01b8a52601160045260248afd5b5f198301838111611cff5780611d37611d2f611d3e9389613cc4565b519187613cc4565b5190613c3d565b611ba9565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663a73e40cc179055611d963061450c565b61035b611da161568e565b5460405160208101903082526001604082015260408152610d45606082613b1b565b503461029957806003193601126102995760018060a01b03601f5460081c1660018060a01b03196004541617600455611e2d6020604051611e05604082613b1b565b6008815267657869737473282960c01b9101526002805463ffffffff191663267c4ae4179055565b61035b611e3861568e565b5461421b565b5034610299578060031936011261029957601b54611e5b81613b52565b611e686040519182613b1b565b818152601b83526020810191837f3ad8aa4f87544323a9d1e5dd902f40c356527a7955687113db5f9a85ad579dc1845b838310611f2457868587604051928392602084019060208552518091526040840160408260051b8601019392905b828210611ed557505050500390f35b91936001919395506020611f148192603f198a820301865288519083611f0483516040845260408401906139ae565b92015190848184039101526139d2565b9601920192018594939192611ec6565b60026020600192604051611f3781613ae5565b604051611f4881610ea8818a613ba1565b8152611f55858701613d12565b83820152815201920192019190611e98565b5034610299576080366003190112610299576004356001600160f81b03811690819003610369576024356001600160f81b0381169081900361036957604435801515810361036957606435908115158203610369576006805460ff19166001179055601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff19166379da7e4d17905561200b846145cf565b6006805460ff19166001179055601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff19166357351c4517905561205a816145cf565b6006805460ff19166001179055601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663eb53f9901790556120a9826145cf565b6006805460ff19166001179055601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663e4c62a111790556120f8836145cf565b601f546040516379da7e4d60e01b815260089190911c6001600160a01b031694602082600481895afa80156122a5576121419288916121d6575b506001600160f81b031661432a565b6040516357351c4560e01b815290602082600481885afa801561229a57869061225b575b61216f92506144ae565b604051630eb53f9960e41b8152602081600481875afa908115612250578591612205575b50926121a36020926004956144ae565b60405163e4c62a1160e01b815293849182905afa801561073d5761035b9284916121d657506001600160f81b031661432a565b6121f8915060203d6020116121fe575b6121f08183613b1b565b810190613cf3565b5f612132565b503d6121e6565b9390506020843d602011612248575b8161222160209383613b1b565b81010312612244576121a360209261223a600496613c78565b9295509250612193565b8480fd5b3d9150612214565b6040513d87823e3d90fd5b506020823d602011612292575b8161227560209383613b1b565b8101031261228e5761228961216f92613c78565b612165565b8580fd5b3d9150612268565b6040513d88823e3d90fd5b6040513d89823e3d90fd5b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663e5ed1efe1790556123026150b9565b601f546040516372f68f7f60e11b8152906020908290600490829060081c6001600160a01b03165afa80156104425782906115a95761035b9150614450565b50346102995760403660031901126102995760043560243560ff8116810361270c576001905b60058210612373578380f35b5f198201908282116127575760ff918261238d92166143de565b169261239882613c92565b93815b8381106127105750601f5460081c6001600160a01b0316803b1561270c578280916024604051809481936355231c1360e11b83528a60048401525af1801561073d5783906126f5575b90505081928280945b875186101561244157838610156124175761240e600191611d37888b613cc4565b955b01946123ed565b94808403612428575b600190612410565b93612439600191611d37878b613cc4565b949050612420565b90959450929091926124668261246161245a878b613cc4565b5184613c3d565b613c3d565b610100039061010082116126e15761248b9161248191613c3d565b9185831b92613c3d565b1c9060018060a01b03601f5460081c1660018060a01b03196004541617600455600160ff196006541617600655606063ffffffff60246040516124ce8482613b1b565b818152636e74382960e01b604060208301927f67657452616e646f6d5061636b65642875696e74382c75696e74385b5d2c7569845201522060e01c1663ffffffff19600254161760025560405180978560808301938560208501528060408501528251809552602060a0850193018a5b8681106126c857505061255d945083015203601f198101885287613b1b565b85516001600160401b0381116126b457612578600754613b69565b601f8111612653575b506020601f82116001146125ee578697829394959697926125e3575b50508160011b915f199060031b1c1916176007555b6125bb5f6169aa565b60208151918180820193849201010312610369576001926125dc915161432a565b0190612367565b015190505f8061259d565b6007875280872090601f198316885b81811061263b57509883600195969798999a10612623575b505050811b016007556125b2565b01515f1960f88460031b161c191690555f8080612615565b9192602060018192868e0151815501940192016125fd565b8181111561258157600787526126a6907fa66cc928b5edb82af9bd49922954155ab7b0942694bea4ce44661d9a8736c68890601f840160051c90602085106126ac575b601f82910160051c039101615616565b5f612581565b899150612696565b634e487b7160e01b86526041600452602486fd5b815185526020948501948a94509091019060010161253e565b634e487b7160e01b87526011600452602487fd5b6126fe91613b1b565b815f12610a32575f826123e4565b8280fd5b60018101808211612743576001600160fd1b0381168103612743579060019160031b61273c8289613cc4565b520161239b565b634e487b7160e01b84526011600452602484fd5b634e487b7160e01b85526011600452602485fd5b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663b7e19e291790556102fc61540d565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916638c6b45511790556128103061450c565b612818614d66565b601f54604051638c6b455160e01b8152306004820152906020908290602490829060081c6001600160a01b03165afa9081156104425782916128c0575b501580612860575080f35b5f51602061887d5f395f51905f523b15610a3257604051630c9fd58160e01b8152901560048201528180826024815f51602061887d5f395f51905f525afa801561061a576128ad57505080f35b6128b691613b1b565b805f126102995780f35b90506020813d6020116128f2575b816128db60209383613b1b565b81010312610a32576128ec90613c78565b5f612855565b3d91506128ce565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff19166315e8b345179055600160035561295161568e565b548060080361295e575080f35b5f51602061887d5f395f51905f523b15610369576040519063260a5b1560e21b82526008600483015260248201525f816044815f51602061887d5f395f51905f525afa801561035e57610351575080f35b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663504429bf179055612a023061450c565b80600355612a0e614a12565b601f546040805163504429bf60e01b8152306004820152918290602490829060081c6001600160a01b03165afa80156104425761035b9183908492612a5d575b50612a5890614165565b61410e565b612a589250612a7b915060403d604011610fa857610f9a8183613b1b565b91612a4e565b503461029957806003193601126102995760405160178054808352908352909160208301917fc624b66cc0138b8fabc209247f72d758e1cf3343756d543badbf24212bed8c15915b818110612ae05761093b8561092f81870382613b1b565b82546001600160a01b0316845260209093019260019283019201612ac9565b503461029957806003193601126102995760405160188054808352908352909160208301917fb13d2d76d1f4b7be834882e410b3e3a8afaf69f83600ae24db354391d2378d2e915b818110612b5e5761093b8561092f81870382613b1b565b82546001600160a01b0316845260209093019260019283019201612b47565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916630310c060179055612bd03061450c565b612bd93061450c565b80600355612be5614a12565b601f54604080516218860360e51b815291829060081c6001600160a01b03168180612c14308060048401613c5e565b03915afa80156104425761035b9183908492612c3a575b50612c35906141c0565b61421b565b612c359250612c58915060403d604011610fa857610f9a8183613b1b565b91612c2b565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916630310c060179055612d1090612cb53061450c565b612cbe3061450c565b80600355612cca61568e565b549060405160208101903082526006604082015260408152612ced606082613b1b565b519020604051612d06816110fb60208201943086613c22565b5190209050614384565b005b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663b7e19e29179055612d646168db565b602081519181808201938492010103126103695751819061ecc960f01b8101612d8a5750f35b5f51602061887d5f395f51905f523b1561072357604051637c84c69b60e01b8152600481019190915261133760f01b602482015281816044815f51602061887d5f395f51905f525afa801561044257612de05750f35b81612dea91613b1b565b6102995780f35b5034610299576040366003190112610299576004356001600160a01b03811690819003610a32576024356001600160801b0381169081900361270c576006805460ff19166001179055601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff19166341b6edb2179055612e7c8261450c565b612e85816145cf565b601f546040516320db76d960e11b81526004810184905260089190911c6001600160a01b031690602081602481855afa80156122505783908690612f8f575b612ece925061432a565b6006805460ff19166001179055600480546001600160a01b0319169190911790556002805463ffffffff1916633eae2218179055612f0b8261450c565b612f14816145cf565b601f546040516307d5c44360e31b815260048101939093526020908390602490829060081c6001600160a01b03165afa801561073d578390612f5b575b61035b925061432a565b506020823d602011612f87575b81612f7560209383613b1b565b810103126103695761035b9151612f51565b3d9150612f68565b50506020813d602011612fbd575b81612faa60209383613b1b565b810103126103695782612ece9151612ec4565b3d9150612f9d565b5034610299578060031936011261029957601e54612fe281613b52565b612fef6040519182613b1b565b818152601e83526020810191837f50bb669a95c7b50b7e8a6f09454034b2b14cf2b85c730dca9a539ca82cb6e350845b8383106130f35786858760405192839260208401906020855251809152604084019160408260051b8601019392815b83831061305b5786860387f35b919395509193603f198782030183528551906020604082019260018060a01b0381511683520151916040602083015282518091526060820190602060608260051b850101940192855b8281106130c85750505050506020806001929701930193019092869594929361304e565b90919293946020806130e6600193605f1987820301895289516139ae565b97019501939291016130a4565b6040516130ff81613ae5565b82546001600160a01b0316815260018301805461311b81613b52565b916131296040519384613b1b565b8183528a526020808b20908b9084015b83821061315f57505050506001928260209283600295015281520192019201919061301f565b60016020819260405161317681610ea8818a613ba1565b815201930191019091613139565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663504429bf1790556131d73061450c565b60016003556131e4614a12565b601f546040805163504429bf60e01b8152306004820152918290602490829060081c6001600160a01b03165afa80156104425761035b918390849261322e575b506114ee9061410e565b6114ee925061324c915060403d604011610fa857610f9a8183613b1b565b91613224565b503461029957806003193601126102995760405160168054808352908352909160208301917fd833147d7dc355ba459fc788f669e58cfaf9dc25ddcd0702e87d69c7b5124289915b8181106132b15761093b8561092f81870382613b1b565b82546001600160a01b031684526020909301926001928301920161329a565b5034610299578060031936011261029957604051610b2f808201908282106001600160401b0383111761074857908291616c9c8339039082f0801561061a57601f8054610100600160a81b03191660089290921b610100600160a81b031691909117905580f35b5034610299578060031936011261029957601f54604051632e11ff4f60e11b81526105396004820152919060081c6001600160a01b0316602083602481845afa9283156104425782936134f9575b50600480546001600160a01b0319169190911790556002805463ffffffff1916635c23fe9e17905560015491600160401b8310156134e55760018301806001558310156134d157600182526105395f51602061889d5f395f51905f5290930183905590918291613400906001600160801b03191682176145cf565b601f546040516320db76d960e11b815260048101839052906020908290602490829060081c6001600160a01b03165afa90811561073d57839161349c575b5080820361344a575050f35b5f51602061887d5f395f51905f523b15613498576040519163260a5b1560e21b83526004830152602482015281816044815f51602061887d5f395f51905f525afa801561044257612de05750f35b5050fd5b9250506020823d6020116134c9575b816134b860209383613b1b565b81010312610369578291515f61343e565b3d91506134ab565b634e487b7160e01b82526032600452602482fd5b634e487b7160e01b82526041600452602482fd5b9092506020813d602011613525575b8161351560209383613b1b565b810103126103695751915f613385565b3d9150613508565b5034610369575f36600319011261036957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663a73e40cc1790556135803061450c565b60018060a01b03600454166003545f51602061887d5f395f51905f523b156103695760405162fa5c1760e61b81525f81600481835f51602061887d5f395f51905f525af1801561035e5761394b575b50613604916135e86060926135e261568e565b54613c85565b6040516343b7127360e11b815293849283929060048401613c22565b03815f51602061887d5f395f51905f525afa908115610442578283918493613928575b50156137cd5782906001600160a01b03163081036138c1575b505061364b906140a9565b601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663a73e40cc17905561368d3061450c565b60018060a01b03600454166003545f51602061887d5f395f51905f523b1561270c5760405162fa5c1760e61b815283908181600481835f51602061887d5f395f51905f525af18015610442576138ac575b50506136ec906135e261568e565b61370e60608492604051809381926343b7127360e11b83528760048401613c22565b03815f51602061887d5f395f51905f525afa80156137c25784918591613889575b509080156137cd575b613746578361035b836140a9565b6040516343b7127360e11b815290915060608180613768858760048401613c22565b03815f51602061887d5f395f51905f525afa80156137c25784918591613790575b5090613738565b90506137b3915060603d81116137bb575b6137ab8183613b1b565b810190614578565b90505f613789565b503d6137a1565b6040513d86823e3d90fd5b60405162461bcd60e51b815260206004820152607c60248201527f73746453746f7261676520726561645f626f6f6c2853746453746f726167652960448201527f3a2043616e6e6f742066696e6420706172656e742e204d616b6520737572652060648201527f796f752067697665206120736c6f7420616e642073746172744d617070696e6760848201527f5265636f7264696e67282920686173206265656e2063616c6c65642e0000000060a48201528060c481015b0390fd5b90506138a4915060603d6060116137bb576137ab8183613b1b565b90505f61372f565b816138b691613b1b565b61270c57825f6136de565b5f51602061887d5f395f51905f523b15610a3257816138f691604051809381926328a9b0fb60e11b8352309060048401613c5e565b03815f51602061887d5f395f51905f525afa80156104425715613640578161391d91613b1b565b610a3257815f613640565b915050613944915060603d6060116137bb576137ab8183613b1b565b915f613627565b60609193509161395e5f61360494613b1b565b6135e85f94925050916135cf565b60206040818301928281528451809452019201905f5b81811061398f5750505090565b82516001600160a01b0316845260209384019390920191600101613982565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b90602080835192838152019201905f5b8181106139ef5750505090565b82516001600160e01b0319168452602093840193909201916001016139e2565b602081016020825282518091526040820191602060408360051b8301019401925f915b838310613a4157505050505090565b9091929394602080613a5f600193603f1986820301875289516139ae565b97019301930191939290613a32565b602081016020825282518091526040820191602060408360051b8301019401925f915b838310613aa057505050505090565b9091929394602080613ad6600193603f198682030187526040838b51878060a01b038151168452015191818582015201906139d2565b97019301930191939290613a91565b604081019081106001600160401b03821117610c0057604052565b608081019081106001600160401b03821117610c0057604052565b90601f801991011681019081106001600160401b03821117610c0057604052565b9190826040910312610369576020825192015190565b6001600160401b038111610c005760051b60200190565b90600182811c92168015613b97575b6020831014613b8357565b634e487b7160e01b5f52602260045260245ffd5b91607f1691613b78565b5f9291815491613bb083613b69565b8083529260018116908115613c055750600114613bcc57505050565b5f9081526020812093945091925b838310613beb575060209250010190565b600181602092949394548385870101520191019190613bda565b915050602093945060ff929192191683830152151560051b010190565b6001600160a01b039091168152602081019190915260400190565b91908201809211613c4a57565b634e487b7160e01b5f52601160045260245ffd5b6001600160a01b0391821681529116602082015260400190565b5190811515820361036957565b91908203918211613c4a57565b90613c9c82613b52565b613ca96040519182613b1b565b8281528092613cba601f1991613b52565b0190602036910137565b8051821015610bec5760209160051b010190565b6001600160401b038111610c0057601f01601f191660200190565b9081602091031261036957516001600160f81b03811681036103695790565b90604051918281549182825260208201905f5260205f20925f905b806007830110613e7157613d83945491818110613e52575b818110613e33575b818110613e14575b818110613df5575b818110613dd6575b818110613db7575b818110613d9a575b10613d85575b500383613b1b565b565b6001600160e01b03191681526020015f613d7b565b602083811b6001600160e01b031916855290930192600101613d75565b604083901b6001600160e01b0319168452602090930192600101613d6d565b606083901b6001600160e01b0319168452602090930192600101613d65565b608083901b6001600160e01b0319168452602090930192600101613d5d565b60a083901b6001600160e01b0319168452602090930192600101613d55565b60c083901b6001600160e01b0319168452602090930192600101613d4d565b60e083901b6001600160e01b0319168452602090930192600101613d45565b916008919350610100600191865463ffffffff60e01b8160e01b16825263ffffffff60e01b8160c01b16602083015263ffffffff60e01b8160a01b16604083015263ffffffff60e01b8160801b16606083015263ffffffff60e01b8160601b16608083015263ffffffff60e01b8160401b1660a083015263ffffffff60e01b8160201b1660c083015263ffffffff60e01b1660e0820152019401920185929391613d2d565b60405190613f25604083613b1b565b602082527f67657452616e646f6d5061636b65642875696e743235362c75696e74323536296020830152565b60085460ff1615613f6157600190565b604051630667f9d760e41b81525f51602061887d5f395f51905f5260048201526519985a5b195960d21b60248201526020816044815f51602061887d5f395f51905f525afa90811561035e575f91613fba575b50151590565b90506020813d602011613fe4575b81613fd560209383613b1b565b8101031261036957515f613fb4565b3d9150613fc8565b606090604081527f73746453746f726167652066696e642853746453746f72616765293a204e6f2060208201527f73746f726167652075736520646574656374656420666f72207461726765742e60408201520190565b6040713932903932b0b234b7339030903137b7b61760711b917f73746453746f7261676520726561645f626f6f6c2853746453746f726167652981527f3a2043616e6e6f74206465636f64652e204d616b65207375726520796f75206160208201520152565b806001036140b45750565b5f51602061887d5f395f51905f523b15610369576040519063260a5b1560e21b82526001600483015260248201525f816044815f51602061887d5f395f51905f525afa801561035e576141045750565b5f613d8391613b1b565b806141165750565b5f51602061887d5f395f51905f523b15610369576040519063260a5b1560e21b825260048201525f60248201525f816044815f51602061887d5f395f51905f525afa801561035e576141045750565b606481036141705750565b5f51602061887d5f395f51905f523b15610369576040519063260a5b1560e21b82526004820152606460248201525f816044815f51602061887d5f395f51905f525afa801561035e576141045750565b806064036141cb5750565b5f51602061887d5f395f51905f523b15610369576040519063260a5b1560e21b82526064600483015260248201525f816044815f51602061887d5f395f51905f525afa801561035e576141045750565b806142235750565b5f51602061887d5f395f51905f523b15610369576040519063260a5b1560e21b82525f600483015260248201525f816044815f51602061887d5f395f51905f525afa801561035e576141045750565b610539810361427e5750565b5f51602061887d5f395f51905f523b15610369576040519063260a5b1560e21b8252600482015261053960248201525f816044815f51602061887d5f395f51905f525afa801561035e576141045750565b600181036142da5750565b5f51602061887d5f395f51905f523b15610369576040519063260a5b1560e21b82526004820152600160248201525f816044815f51602061887d5f395f51905f525afa801561035e576141045750565b90808203614336575050565b5f51602061887d5f395f51905f523b15610369576040519163260a5b1560e21b8352600483015260248201525f816044815f51602061887d5f395f51905f525afa801561035e576141045750565b90808203614390575050565b5f51602061887d5f395f51905f523b156103695760405191637c84c69b60e01b8352600483015260248201525f816044815f51602061887d5f395f51905f525afa801561035e576141045750565b905f6143e99261548b565b905f806040516143fa604082613b1b565b600c81526b109bdd5b99081c995cdd5b1d60a21b602082015260405161443d8161196f6020820194632d839cb360e21b86526040602484015260648301906139ae565b51906a636f6e736f6c652e6c6f675afa50565b6064810161445b5750565b5f51602061887d5f395f51905f523b156103695760405163fe74f05b60e01b8152600481019190915260631960248201525f816044815f51602061887d5f395f51905f525afa801561035e576141045750565b15159015158082036144be575050565b5f51602061887d5f395f51905f523b15610369576040519163f7fe347760e01b8352600483015260248201525f816044815f51602061887d5f395f51905f525afa801561035e576141045750565b600154600160401b811015610c00576001810180600155811015610bec5760015f525f51602061889d5f395f51905f520155565b600154600160401b811015610c00576001810180600155811015610bec5760015f5260645f51602061889d5f395f51905f5290910155565b908160609103126103695761458c81613c78565b916040602083015192015190565b60209291908391805192839101825e019081520190565b604091949392606082019560018060a01b0316825260208201520152565b6004546002546003545f9493926001600160a01b03169160e01b6145f2866166d2565b90835f525f60205260405f209063ffffffff60e01b1690815f5260205260405f20604051602081019061462a816110fb88888661459a565b5190205f5260205260ff600360405f2001541615614a03575b835f525f60205260405f20905f526020526110fb61467060405f209360405192839160208301958661459a565b5190205f5260205260405f2060018101549260028201546146918186613c3d565b61488e575b82549060405195630667f9d760e41b8752602087806146b9868a60048401613c22565b03815f51602061887d5f395f51905f525afa96871561035e575f9761485a575b506001908201610100031b5f1901811b198616915f51602061887d5f395f51905f523b15610369576040516370ca10bb60e01b8152925f92849283926147289288901b179089600485016145b1565b0381835f51602061887d5f395f51905f525af1801561035e57614845575b50614750866167b6565b91901591821561483a575b505061476e5750505090613d8390616a63565b8492935054905f51602061887d5f395f51905f523b1561270c576147a660405194859384936370ca10bb60e01b8552600485016145b1565b0381835f51602061887d5f395f51905f525af1801561044257614825575b60405162461bcd60e51b815260206004820152603360248201527f73746453746f726167652066696e642853746453746f72616765293a204661696044820152723632b2103a37903bb934ba32903b30b63ab29760691b6064820152608490fd5b614830828092613b1b565b61029957806147c4565b141590505f8061475b565b6148529196505f90613b1b565b5f945f614746565b9096506020813d602011614886575b8161487660209383613b1b565b81010312610369575195816146d9565b3d9150614869565b6148988186613c3d565b610100036101008111613c4a5760ff8111613c4a5760405163348051d760e11b8152600190911b600482018190525f826024815f51602061887d5f395f51905f525afa91821561035e575f92614981575b50614950606a6020936040519485915f5160206188bd5f395f51905f52828401525f51602061885d5f395f51905f52604084015269030ba32b9103a3430b7160b51b60608401528051918291018484015e81015f838201520301601f198101845283613b1b565b83101561495d5750614696565b60405162461bcd60e51b8152602060048201529081906138859060248301906139ae565b91503d805f843e6149928184613b1b565b820191602081840312610369578051906001600160401b038211610369570182601f82011215610369578051906149c882613cd8565b936149d66040519586613b1b565b82855260208383010111610369576020935f85846149509582606a96018386015e830101529350506148e9565b614a0c5f615ece565b50614643565b6004546002546003545f93926001600160a01b03169160e01b614a34856166d2565b90835f525f60205260405f209063ffffffff60e01b1690815f5260205260405f206040516020810190614a6c816110fb88888661459a565b5190205f5260205260ff600360405f2001541615614d57575b835f525f60205260405f20905f526020526110fb614ab260405f209360405192839160208301958661459a565b5190205f5260205260405f20906001820154916002810154614ad48185613c3d565b614c05575b81549060405194630667f9d760e41b865260208680614afc868960048401613c22565b03815f51602061887d5f395f51905f525afa95861561035e575f96614bd1575b506001908201610100031b5f1901811b198516915f51602061887d5f395f51905f523b15610369576040516370ca10bb60e01b8152925f9284928392614b6c926064901b179088600485016145b1565b0381835f51602061887d5f395f51905f525af1801561035e57614bbc575b50614b94856167b6565b9015908115614bb0575b5061476e5750505090613d8390616a63565b6064915014155f614b9e565b614bc99195505f90613b1b565b5f935f614b8a565b9095506020813d602011614bfd575b81614bed60209383613b1b565b8101031261036957519481614b1c565b3d9150614be0565b614c0f8185613c3d565b610100036101008111613c4a5760ff8111613c4a5760405163348051d760e11b8152600190911b600482018190525f826024815f51602061887d5f395f51905f525afa91821561035e575f92614cd5575b50614cc7606a6020936040519485915f5160206188bd5f395f51905f52828401525f51602061885d5f395f51905f52604084015269030ba32b9103a3430b7160b51b60608401528051918291018484015e81015f838201520301601f198101845283613b1b565b6064101561495d5750614ad9565b91503d805f843e614ce68184613b1b565b820191602081840312610369578051906001600160401b038211610369570182601f8201121561036957805190614d1c82613cd8565b93614d2a6040519586613b1b565b82855260208383010111610369576020935f8584614cc79582606a96018386015e83010152935050614c60565b614d605f615ece565b50614a85565b6004546002546003545f93926001600160a01b03169160e01b614d88856166d2565b90835f525f60205260405f209063ffffffff60e01b1690815f5260205260405f206040516020810190614dc0816110fb88888661459a565b5190205f5260205260ff600360405f20015416156150aa575b835f525f60205260405f20905f526020526110fb614e0660405f209360405192839160208301958661459a565b5190205f5260205260405f20906001820154916002810154614e288185613c3d565b614f58575b81549060405194630667f9d760e41b865260208680614e50868960048401613c22565b03815f51602061887d5f395f51905f525afa95861561035e575f96614f24575b506001908201610100031b5f1901811b198516915f51602061887d5f395f51905f523b15610369576040516370ca10bb60e01b8152925f9284928392614ec0926001901b179088600485016145b1565b0381835f51602061887d5f395f51905f525af1801561035e57614f0f575b50614ee8856167b6565b9015908115614f03575061476e5750505090613d8390616a63565b6001915014155f614b9e565b614f1c9195505f90613b1b565b5f935f614ede565b9095506020813d602011614f50575b81614f4060209383613b1b565b8101031261036957519481614e70565b3d9150614f33565b614f628185613c3d565b610100036101008111613c4a5760ff8111613c4a5760405163348051d760e11b8152600190911b600482018190525f826024815f51602061887d5f395f51905f525afa91821561035e575f92615028575b5061501a606a6020936040519485915f5160206188bd5f395f51905f52828401525f51602061885d5f395f51905f52604084015269030ba32b9103a3430b7160b51b60608401528051918291018484015e81015f838201520301601f198101845283613b1b565b6001101561495d5750614e2d565b91503d805f843e6150398184613b1b565b820191602081840312610369578051906001600160401b038211610369570182601f820112156103695780519061506f82613cd8565b9361507d6040519586613b1b565b82855260208383010111610369576020935f858461501a9582606a96018386015e83010152935050614fb3565b6150b35f615ece565b50614dd9565b6004546002546003545f93926001600160a01b03169160e01b6150db856166d2565b90835f525f60205260405f209063ffffffff60e01b1690815f5260205260405f206040516020810190615113816110fb88888661459a565b5190205f5260205260ff600360405f20015416156153fe575b835f525f60205260405f20905f526020526110fb61515960405f209360405192839160208301958661459a565b5190205f5260205260405f2090600182015491600281015461517b8185613c3d565b6152ab575b81549060405194630667f9d760e41b8652602086806151a3868960048401613c22565b03815f51602061887d5f395f51905f525afa95861561035e575f96615277575b506001908201610100031b5f1901811b1985165f51602061887d5f395f51905f523b15610369575f9161521260405194859384936370ca10bb60e01b8552606319901b179088600485016145b1565b0381835f51602061887d5f395f51905f525af1801561035e57615262575b5061523a856167b6565b9015908115615255575061476e5750505090613d8390616a63565b606319141590505f614b9e565b61526f9195505f90613b1b565b5f935f615230565b9095506020813d6020116152a3575b8161529360209383613b1b565b81010312610369575194816151c3565b3d9150615286565b6152b58185613c3d565b610100036101008111613c4a5760ff8111613c4a5760405163348051d760e11b8152600190911b600482018190525f826024815f51602061887d5f395f51905f525afa91821561035e575f9261537c575b5061536d606a6020936040519485915f5160206188bd5f395f51905f52828401525f51602061885d5f395f51905f52604084015269030ba32b9103a3430b7160b51b60608401528051918291018484015e81015f838201520301601f198101845283613b1b565b606319101561495d5750615180565b91503d805f843e61538d8184613b1b565b820191602081840312610369578051906001600160401b038211610369570182601f82011215610369578051906153c382613cd8565b936153d16040519586613b1b565b82855260208383010111610369576020935f858461536d9582606a96018386015e83010152935050615306565b6154075f615ece565b5061512c565b6154165f6169aa565b6020815191818082019384920101031261036957518015615468576001146154635760405162461bcd60e51b8152602060048201526052602482015260a49061546160448201614043565bfd5b600190565b505f90565b8115615477570690565b634e487b7160e01b5f52601260045260245ffd5b5f908383116155ab57828110918215806155a1575b615599576154ae8486613c85565b9260018401809411613c4a57600383111580615590575b6155815760031983101580615577575b615563578583111561551a575050906154f1846154f693613c85565b61546d565b908115615515576155079250613c3d565b5f198101908111613c4a5790565b505090565b95949291909561552b575b50505050565b839495506154f19061553d9394613c85565b9081156155155761554e9250613c85565b60018101809111613c4a57905f808080615525565b505090506155749291501990613c85565b90565b50821984116154d5565b50509190506155749250613c3d565b508284116154c5565b509250505090565b50848211156154a0565b60405162461bcd60e51b815260206004820152603e60248201527f5374645574696c7320626f756e642875696e743235362c75696e743235362c7560448201527f696e74323536293a204d6178206973206c657373207468616e206d696e2e00006064820152608490fd5b5f5b82811061562457505050565b5f82820155600101615618565b9080601f8301121561036957815161564881613b52565b926156566040519485613b1b565b81845260208085019260051b82010192831161036957602001905b82821061567e5750505090565b8151815260209182019101615671565b6004546002546003546001600160a01b03909216915f9160e01b6156b1836166d2565b90845f525f60205260405f209063ffffffff60e01b1690815f5260205260405f2060405160208101906156e9816110fb88888661459a565b5190205f5260205260ff600360405f20015416615e85575f51602061887d5f395f51905f523b156103695760405163266cf10960e01b81525f81600481835f51602061887d5f395f51905f525af1801561035e57615e70575b5061574c846167b6565b6040516365bc948160e01b815260048101889052915085826024815f51602061887d5f395f51905f525afa91821561229a578692615e02575b508151806157ad5760405162461bcd60e51b8152602060048201528061388560248201613fec565b9190915b80156126e157906157e8915f19019060206157cc8383613cc4565b5160405180958192630667f9d760e41b83528d60048401613c22565b03815f51602061887d5f395f51905f525afa928315615df7578893615dc4575b508215615d80575b61581a8282613cc4565b5160018060a01b036004541690604051630667f9d760e41b815260208180615846858760048401613c22565b03815f51602061887d5f395f51905f525afa908115615d75578b91615d44575b506158708b6167b6565b91909382155f14615d3d575f19905b5f51602061887d5f395f51905f523b15615d2457848e916158b460405194859384936370ca10bb60e01b8552600485016145b1565b0381835f51602061887d5f395f51905f525af18015615ca057908d91615d28575b506158df906167b6565b600454909491506001600160a01b03165f51602061887d5f395f51905f523b15615d2457908d9161592460405194859384936370ca10bb60e01b8552600485016145b1565b0381835f51602061887d5f395f51905f525af18015615d1957908c91615d00575b505082615cf5575b505015615ced578886888a968b9660ff60065416615b6c575b6001898901610100031b5f1901881b16871c8103615b5c5750927f9c9555b1e3102e3cf48f427d79cb678f5d9bd1ed0ad574389461e255f95170ed60806159f294600397946110fb6159c7615a7a9c9960405192839160208301958661459a565b5190206159d48686613cc4565b51906040519283528c602084015260408301526060820152a1613cc4565b519260405193615a0185613b00565b845260208401918252604084019081526060840191600183528a8a528960205260408a20878b5260205260408a20886110fb615a488c60405192839160208301958661459a565b5190208b5260205260408a209451855551600185015551600284015551151591019060ff801983541691151516179055565b8484528360205260408420818552602052604084206040516020810190615aa6816110fb88888661459a565b519020855260205260ff60036040862001541615615aff57604094615aca85616a63565b8452836020528484209084526020526110fb615af385852093865192839160208301958661459a565b51902082526020522090565b60405162461bcd60e51b815260206004820152602f60248201527f73746453746f726167652066696e642853746453746f72616765293a20536c6f60448201526e3a143994903737ba103337bab7321760891b6064820152608490fd5b955050505092505b9190916157b1565b975092505050615bac9350615b818383613cc4565b519460208660018060a01b03600454166040519788928392630667f9d760e41b845260048401613c22565b03815f51602061887d5f395f51905f525afa948515615ce2578a95615caf575b50615bd7868b616b1d565b959096615be4818d616be7565b60045490939192906001600160a01b03165f51602061887d5f395f51905f523b15615cab57908e91615c2a60405194859384936370ca10bb60e01b8552600485016145b1565b0381835f51602061887d5f395f51905f525af18015615ca057928e95928e8d96938f96615c76575b50508a615c6e575b509798615966575095505050509250615b64565b99505f615c5a565b909396508391949750615c8a929550613b1b565b615c9c579289928b928e958e5f615c52565b8b80fd5b6040513d8f823e3d90fd5b8e80fd5b9094506020813d8211615cda575b81615cca60209383613b1b565b810103126103695751935f615bcc565b3d9150615cbd565b6040513d8c823e3d90fd5b929150615b64565b141590505f8061594d565b81615d0a91613b1b565b615d15578a5f615945565b8a80fd5b6040513d8e823e3d90fd5b8d80fd5b81615d3291613b1b565b615c9c578b5f6158d5565b8c9061587f565b90506020813d8211615d6d575b81615d5e60209383613b1b565b8101031261036957515f615866565b3d9150615d51565b6040513d8d823e3d90fd5b7f080fc4a96620c4462e705b23f346413fe3796bb63c6f8d8591baec0e231577a5615dbc615dae8484613cc4565b516040519182918d83613c22565b0390a1615810565b9092506020813d8211615def575b81615ddf60209383613b1b565b810103126103695751915f615808565b3d9150615dd2565b6040513d8a823e3d90fd5b9091503d8087833e615e148183613b1b565b8101604082820312615e6c5781516001600160401b038111615e685781615e3c918401615631565b916020810151906001600160401b038211615e6457615e5c929101615631565b50905f615785565b8880fd5b8780fd5b8680fd5b615e7d9194505f90613b1b565b5f925f615742565b9193909250615e935f616a63565b5f525f60205260405f20905f526020526110fb615ebf60405f209360405192839160208301958661459a565b5190205f5260205260405f2090565b6004810154600282015460038301546001600160a01b03909216925f929160e01b615ef8826166d2565b9160018060a01b0386165f528060205260405f2063ffffffff60e01b83165f5260205260405f206040516020810190615f36816110fb89898661459a565b5190205f5260205260ff600360405f20015416616691575f51602061887d5f395f51905f523b156103695760405163266cf10960e01b81525f81600481835f51602061887d5f395f51905f525af1801561035e5761667c575b50615f99816167b6565b6040516365bc948160e01b815260048101899052915086826024815f51602061887d5f395f51905f525afa9182156122a5578792616616575b50815180615ffa5760405162461bcd60e51b8152602060048201528061388560248201613fec565b9190915b80156166025790616037915f19019060206160198383613cc4565b51604051630667f9d760e41b81529485918291908e60048401613c22565b03815f51602061887d5f395f51905f525afa9283156165f75789936165c4575b508215616580575b6160698282613cc4565b5160018060a01b0360048701541690604051630667f9d760e41b815260208180616097858760048401613c22565b03815f51602061887d5f395f51905f525afa908115615d19578c9161654f575b506160c1886167b6565b91909382155f14616548575f19905b5f51602061887d5f395f51905f523b15615cab57848f9161610560405194859384936370ca10bb60e01b8552600485016145b1565b0381835f51602061887d5f395f51905f525af180156164c757908e91616533575b5050616131896167b6565b60048b0154909491506001600160a01b03165f51602061887d5f395f51905f523b15615cab57908e9161617860405194859384936370ca10bb60e01b8552600485016145b1565b0381835f51602061887d5f395f51905f525af18015615ca057908d9161651e575b505082616513575b50501561650b578987898b968c9660ff60068b01541661638e575b6001898901610100031b5f1901881b16871c810361637e5750927f9c9555b1e3102e3cf48f427d79cb678f5d9bd1ed0ad574389461e255f95170ed608061625194600397946110fb61621d6162ea9c9960405192839160208301958661459a565b51902061622a8686613cc4565b51906040519283528d63ffffffff60e01b16602084015260408301526060820152a1613cc4565b51926040519361626085613b00565b8452602080850192835260408086019283526001606087019081526001600160a01b038e165f9081528984528290206001600160e01b03198b168e528352818d2091519094928101906162b8816110fb8f8f8661459a565b5190208c5260205260408b209451855551600185015551600284015551151591019060ff801983541691151516179055565b6001600160a01b0386165f90815260208281526040918290206001600160e01b031985168852815281872091519081019061632a816110fb89898661459a565b519020865260205260ff60036040872001541615615aff5760409560018060a01b03165f52602052845f209063ffffffff60e01b1684526020526110fb615af385852093865192839160208301958661459a565b955050505092505b919091615ffe565b9750925050506163d093506163a38383613cc4565b519460208660018060a01b0360048a0154166040519788928392630667f9d760e41b845260048401613c22565b03815f51602061887d5f395f51905f525afa948515615d75578b956164d8575b506163fb8688616b1d565b959096616408818a616be7565b60048b015490939192906001600160a01b03165f51602061887d5f395f51905f523b156164d457908f9161645060405194859384936370ca10bb60e01b8552600485016145b1565b0381835f51602061887d5f395f51905f525af180156164c757928f95928f8f95938f979461649d575b50508a616495575b5097986161bc575095505050509250616386565b99505f616481565b9093965083919497506164b1929550613b1b565b6164c357928a928c928f958f5f616479565b8c80fd5b8e604051903d90823e3d90fd5b8f80fd5b9094506020813d8211616503575b816164f360209383613b1b565b810103126103695751935f6163f0565b3d91506164e6565b929150616386565b141590505f806161a1565b8161652891613b1b565b615c9c578b5f616199565b8161653d91613b1b565b6164c3578c5f616126565b8d906160d0565b90506020813d8211616578575b8161656960209383613b1b565b8101031261036957515f6160b7565b3d915061655c565b7f080fc4a96620c4462e705b23f346413fe3796bb63c6f8d8591baec0e231577a56165ab8383613cc4565b518b6165bc60405192839283613c22565b0390a161605f565b9092506020813d82116165ef575b816165df60209383613b1b565b810103126103695751915f616057565b3d91506165d2565b6040513d8b823e3d90fd5b634e487b7160e01b88526011600452602488fd5b9091503d8088833e6166288183613b1b565b8101604082820312615e685781516001600160401b038111615e645781616650918401615631565b916020810151906001600160401b03821161667857616670929101615631565b50905f615fd2565b8980fd5b6166899195505f90613b1b565b5f935f615f8f565b919350919360018060a01b03165f5260205260405f209063ffffffff60e01b165f526020526110fb615ebf60405f209360405192839160208301958661459a565b60078101906166e18254613b69565b6167a257600191500190604051808360208295549384815201905f5260205f20925f5b81811061678957505061671992500383613b1b565b81518060051b9080820460201490151715613c4a5761673781613cd8565b906167456040519283613b1b565b808252616754601f1991613cd8565b013660208301375f5b8351811015616784578061677360019286613cc4565b5160208260051b850101520161675d565b509150565b8454835260019485019487945060209093019201616704565b50615574610ea89160405192838092613ba1565b905f806020600285015460e01b61680660246167d1886166d2565b6040519485918183019563ffffffff60e01b1686528051918291018484015e810186838201520301601f198101845283613b1b565b60048601549151916001600160a01b03165afa3d156168d15760033d9361682c85613cd8565b9461683a6040519687613b1b565b85523d5f602087013e5b0154600581901b906001600160fb1b03811603613c4a575f938051602081115f146168cb57506020905b5f925b82841061688057505050509190565b9091929561688e8783613c3d565b8351811015610bec57830160200151600388901b91906001600160f81b031916881560088a8504141715613c4a576001921c179601929190616871565b9061686e565b6003606093616844565b6169316168e75f615ece565b600181810154600283015492916020918401610100031b5f1901831b600480549354604051630667f9d760e41b8152969294879384939092916001600160a01b0316908401613c22565b03815f51602061887d5f395f51905f525afa92831561035e575f93616976575b5061695b5f616a63565b6040519216901c602082015260208152615574604082613b1b565b9092506020813d6020116169a2575b8161699260209383613b1b565b810103126103695751915f616951565b3d9150616985565b616a03906169b781615ece565b600181810154600283015493916020918501610100031b5f1901841b6004838101549454604051630667f9d760e41b8152979295889384939092916001600160a01b0316908401613c22565b03815f51602061887d5f395f51905f525afa93841561035e575f94616a2d575b5061695b90616a63565b9093506020813d602011616a5b575b81616a4960209383613b1b565b8101031261036957519261695b616a23565b3d9150616a3c565b6004810180546001600160a01b031916905560028101805463ffffffff191690556001810180545f82559081616afb575b50505f600382015560068101805460ff191690556007018054616ab690613b69565b9081616ac0575050565b81601f5f9311600114616ad1575055565b81835260208320616aee91601f0160051c84190190600101615616565b8082528160208120915555565b5f5260205f205f5b828110616b105750616a94565b5f82820155600101616b03565b91905f5b6101008110616b3457505090505f905f90565b8060ff0360ff8111613c4a576004850154600190911b906001600160a01b03165f51602061887d5f395f51905f523b1561036957835f91616b8960405194859384936370ca10bb60e01b8552600485016145b1565b0381835f51602061887d5f395f51905f525af1801561035e57616bd7575b50616bb1846167b6565b81616bcd575b50616bc457600101616b21565b92505060019190565b905015155f616bb7565b5f616be191613b1b565b5f616ba7565b91905f5b6101008110616bfe57505090505f905f90565b60048401546001821b906001600160a01b03165f51602061887d5f395f51905f523b1561036957835f91616c4660405194859384936370ca10bb60e01b8552600485016145b1565b0381835f51602061887d5f395f51905f525af1801561035e57616c8b575b50616c6e846167b6565b81616c81575b50616bc457600101616beb565b905015155f616c74565b5f616c9591613b1b565b5f616c6456fe6080604052346101755760015f819055610100600a5561133760f01b600c55600d80546001600160a01b031916610539179055600160ff1b600e55600f805460ff19169091179055600161ecc960f01b03601055604051606081016001600160401b0381118282101761011c57604052600381526003602082015260036040820152601254600360125580600310610147575b5060125f5260205f20905f5b6003811061013057604080519081016001600160401b0381118282101761011c57610539916020916040528281520152610539600755610539600855335f52600360205270010000000000000000000000000000000160405f20556105395f526003602052600160801b60405f20556040516109b5908161017a8239f35b634e487b7160e01b5f52604160045260245ffd5b600190602060ff845116930192818501550161009e565b60125f5260205f209060021901905f5b828110610165575050610092565b5f82820160030155600101610157565b5f80fdfe60806040526004361015610011575f80fd5b5f3560e01c80630310c060146101c457806308f23aad146101bf57806315e8b345146101ba5780631971f00b146101b55780631aa844b4146101b0578063267c4ae4146101ab5780633b80a793146101a65780633eae2218146101a157806341b6edb21461019c5780634f87aeb714610197578063504429bf1461019257806357351c451461018d5780635c23fe9e1461018857806361a97569146101835780636a56c3d41461017e57806379da7e4d146101795780638c6b4551146101745780638cd8156d1461016f5780639e7936e61461016a578063a73e40cc14610165578063aa46382614610160578063aef6d4b11461015b578063b7e19e2914610156578063e4c62a1114610151578063e5ed1efe1461014c578063e92e9dc4146101475763eb53f99014610142575f80fd5b6107f8565b6107a8565b61078b565b61076b565b61074e565b610712565b6106f9565b6106c1565b61069a565b610643565b610606565b6105de565b6105b4565b6104de565b610464565b610442565b6103f1565b6103cf565b61038f565b610354565b610334565b610318565b6102e9565b6102b6565b61028e565b610266565b6101f9565b600435906001600160a01b03821682036101df57565b5f80fd5b602435906001600160a01b03821682036101df57565b346101df5760403660031901126101df576102466102156101c9565b61021d6101e3565b9060018060a01b03165f52600660205260405f209060018060a01b03165f5260205260405f2090565b8054600190910154604080519283526020830191909152819081015b0390f35b346101df575f3660031901126101df57600d546040516001600160a01b039091168152602090f35b346101df575f3660031901126101df5760075460085460408051928352602083019190915290f35b346101df5760603660031901126101df576011805460016024351b5f190160443590811b1990911660043590911b179055005b346101df5760403660031901126101df576011546040516024359190911c60016004351b5f1901168152602090f35b346101df575f3660031901126101df5760205f54604051908152f35b346101df575f3660031901126101df5760405161133760f01b8152602090f35b346101df5760203660031901126101df576001600160a01b036103756101c9565b165f526003602052602060405f205460801c604051908152f35b346101df5760203660031901126101df576001600160a01b036103b06101c9565b165f526003602052602060018060801b0360405f205416604051908152f35b346101df575f3660031901126101df57602060ff600f54166040519015158152f35b346101df5760203660031901126101df576001600160a01b036104126101c9565b165f52600460205260405f2060018154910154906102626040519283928360209093929193604081019481520152565b346101df575f3660031901126101df57602060095460f81c6040519015158152f35b346101df5760203660031901126101df576001600160a01b036104856101c9565b165f526003602052602060405f2054604051908152f35b6004359060ff821682036101df57565b6044359060ff821682036101df57565b359060ff821682036101df57565b634e487b7160e01b5f52604160045260245ffd5b346101df5760603660031901126101df576104f761049c565b60243567ffffffffffffffff81116101df57366023820112156101df5780600401359067ffffffffffffffff82116105af578160051b60405192601f19603f830116840184811067ffffffffffffffff8211176105af57604052835260246020840191830101913683116101df57602401905b8282106105975761026261058786866105816104ac565b916108ac565b6040519081529081906020820190565b602080916105a4846104bc565b81520191019061056a565b6104ca565b346101df5760203660031901126101df576004355f526002602052602060405f2054604051908152f35b346101df575f3660031901126101df576009546040516001600160f81b039091168152602090f35b346101df5760203660031901126101df576001600160a01b036106276101c9565b165f52600b602052602060ff60405f2054166040519015158152f35b346101df5760403660031901126101df5760206106916106616101c9565b6106696101e3565b6001600160a01b039182165f9081526005855260408082209290931681526020919091522090565b54604051908152f35b346101df575f3660031901126101df575f808080600c545afa506020601054604051908152f35b346101df5760203660031901126101df576001600160a01b036106e26101c9565b165f526001602052602060405f2054604051908152f35b346101df5760203660031901126101df57600435601155005b346101df575f3660031901126101df5760207fb27fb258786eae8f9ffde06a5bfd55f5193cb73bd64e533d5d75fd7cb46652ff54604051908152f35b346101df575f3660031901126101df576020600c54604051908152f35b346101df575f3660031901126101df576020600a5460081c604051908152f35b346101df575f3660031901126101df576020600e54604051908152f35b346101df5760203660031901126101df576004356012548110156101df5760125f527fbb8a6a4669ba250d26cd7a459eca9d215f8307e33aebe50379bc5a3617ec34440154604051908152602090f35b346101df575f3660031901126101df57602060ff600a54166040519015158152f35b1561082157565b60405162461bcd60e51b815260206004820152600560248201526421656c656d60d81b6044820152606490fd5b80518210156108625760209160051b010190565b634e487b7160e01b5f52603260045260245ffd5b634e487b7160e01b5f52601160045260245ffd5b9190820180921161089757565b610876565b6101000390610100821161089757565b929160ff806108bf92169416841061081a565b5f905f935f925b82518410156109395781841015610909576109006001916108fa6108f46108ed888861084e565b5160ff1690565b60ff1690565b9061088a565b935b01926108c6565b9280820361091a575b600190610902565b946109316001916108fa6108f46108ed8a8861084e565b959050610912565b9061097b935061096a8661096561095f6108f46108ed6108fa9661096f999c9b9c61084e565b8561088a565b61088a565b61089c565b91601154831b9261088a565b1c9056fea2646970667358221220a12b94a02f9d5621f3851d7ba3361198c90539c37a2031672e27c29b213d711964736f6c63430008210033608034607057601f61109238819003918201601f19168301916001600160401b03831184841017607457808492602094604052833981010312607057516001600160a01b03811690819003607057600880546001600160a01b03191691909117905560405161100990816100898239f35b5f80fd5b634e487b7160e01b5f52604160045260245ffdfe60806040526004361015610011575f80fd5b5f3560e01c63fc5aec2b14610024575f80fd5b3461008e575f36600319011261008e5760018060a01b036008541660018060a01b0319600454161760045560076020604051610061604082610092565b8281520166636f6e7374282960c81b81522060e01c63ffffffff19600254161760025561008c61018b565b005b5f80fd5b90601f8019910116810190811067ffffffffffffffff8211176100b457604052565b634e487b7160e01b5f52604160045260245ffd5b67ffffffffffffffff81116100b457601f01601f191660200190565b60209291908391805192839101825e019081520190565b9080601f8301121561008e5781519167ffffffffffffffff83116100b4578260051b906040519361012f6020840186610092565b845260208085019282010192831161008e57602001905b8282106101535750505090565b8151815260209182019101610146565b80518210156101775760209160051b010190565b634e487b7160e01b5f52603260045260245ffd5b6004546002546003546001600160a01b03909216915f9160e01b6101ae83610a9b565b90845f525f60205260405f209063ffffffff60e01b1690815f5260205260405f2060405160208101906101f4816101e68888866100e4565b03601f198101835282610092565b5190205f5260205260ff600360405f20015416610a1a575f516020610fb45f395f51905f523b1561008e5760405163266cf10960e01b81525f81600481835f516020610fb45f395f51905f525af18015610a0f576109fa575b5061025784610cf2565b90506040516365bc948160e01b815286600482015285816024815f516020610fb45f395f51905f525afa9081156109ef578691610981575b5080518061030157608460405162461bcd60e51b815260206004820152604060248201527f73746453746f726167652066696e642853746453746f72616765293a204e6f2060448201527f73746f726167652075736520646574656374656420666f72207461726765742e6064820152fd5b801561096d579061034d915f190190602061031c8383610163565b51604051630667f9d760e41b81526001600160a01b038c166004820152602481019190915293849081906044820190565b03815f516020610fb45f395f51905f525afa92831561096257889361092f575b5082156108f0575b61037f8282610163565b5160048054604051630667f9d760e41b81526001600160a01b03909116918101829052602481018390529091906020816044815f516020610fb45f395f51905f525afa9081156108e5578b916108b4575b506103da8b610cf2565b91909382155f146108ad575f19905b5f516020610fb45f395f51905f523b1561089457848e9161041e60405194859384936370ca10bb60e01b855260048501610e17565b0381835f516020610fb45f395f51905f525af1801561081157908d91610898575b5061044990610cf2565b600454909491506001600160a01b03165f516020610fb45f395f51905f523b1561089457908d9161048e60405194859384936370ca10bb60e01b855260048501610e17565b0381835f516020610fb45f395f51905f525af1801561088957908c91610870575b505082610865575b50501561085e578793889360ff600654166106ea575b6001858701610100031b5f1901851b16841c81036106e1575090610553917f9c9555b1e3102e3cf48f427d79cb678f5d9bd1ed0ad574389461e255f95170ed60808b896101e66105288d6040519283916020830195866100e4565b5190206105358686610163565b51906040519283528a602084015260408301526060820152a1610163565b5190604051916080830183811067ffffffffffffffff8211176106cd57906003939291604052825260208201938452604082019081526060820193600185528989528860205260408920868a526020526040892060405160208101906105be816101e68d8d866100e4565b5190208a526020526040892092518355516001830155516002820155019051151560ff801983541691161790558484528360205260408420818552602052604084206040516020810190610617816101e68888866100e4565b519020855260205260ff600360408620015416156106705760409461063b85610c21565b8452836020528484209084526020526101e66106648585209386519283916020830195866100e4565b51902082526020522090565b60405162461bcd60e51b815260206004820152602f60248201527f73746453746f726167652066696e642853746453746f72616765293a20536c6f60448201526e3a143994903737ba103337bab7321760891b6064820152608490fd5b634e487b7160e01b89526041600452602489fd5b93509150610301565b945061073893506106fb8383610163565b5160048054604051630667f9d760e41b81526001600160a01b03909116918101919091526024810182905290959094602090869081906044820190565b03815f516020610fb45f395f51905f525afa948515610853578a95610820575b50610763868b610e35565b959096610770818d610eff565b60045490939192906001600160a01b03165f516020610fb45f395f51905f523b1561081c57908e916107b660405194859384936370ca10bb60e01b855260048501610e17565b0381835f516020610fb45f395f51905f525af1801561081157908d916107f8575b5050876107f0575b5094956104cd575093509150610301565b96505f6107df565b8161080291610092565b61080d578b5f6107d7565b8b80fd5b6040513d8f823e3d90fd5b8e80fd5b9094506020813d821161084b575b8161083b60209383610092565b8101031261008e5751935f610758565b3d915061082e565b6040513d8c823e3d90fd5b9150610301565b141590505f806104b7565b8161087a91610092565b610885578a5f6104af565b8a80fd5b6040513d8e823e3d90fd5b8d80fd5b816108a291610092565b61080d578b5f61043f565b8c906103e9565b90506020813d82116108dd575b816108ce60209383610092565b8101031261008e57515f6103d0565b3d91506108c1565b6040513d8d823e3d90fd5b7f080fc4a96620c4462e705b23f346413fe3796bb63c6f8d8591baec0e231577a5604061091d8484610163565b518151908c82526020820152a1610375565b9092506020813d821161095a575b8161094a60209383610092565b8101031261008e5751915f61036d565b3d915061093d565b6040513d8a823e3d90fd5b634e487b7160e01b87526011600452602487fd5b90503d8087833e6109928183610092565b81016040828203126109eb57815167ffffffffffffffff81116109e757816109bb9184016100fb565b9160208101519067ffffffffffffffff82116109e3576109dc9291016100fb565b505f61028f565b8880fd5b8780fd5b8680fd5b6040513d88823e3d90fd5b610a079194505f90610092565b5f925f61024d565b6040513d5f823e3d90fd5b9193909250610a285f610c21565b5f525f60205260405f20905f526020526101e6610a5460405f20936040519283916020830195866100e4565b5190205f5260205260405f2090565b90600182811c92168015610a91575b6020831014610a7d57565b634e487b7160e01b5f52602260045260245ffd5b91607f1691610a72565b60078101908154610aab81610a63565b610b815750600191500190604051808360208295549384815201905f5260205f20925f5b818110610b68575050610ae492500383610092565b81518060051b9080820460201490151715610b5457610b02816100c8565b90610b106040519283610092565b808252610b1f601f19916100c8565b013660208301375f5b8351811015610b4f5780610b3e60019286610163565b5160208260051b8501015201610b28565b509150565b634e487b7160e01b5f52601160045260245ffd5b8454835260019485019487945060209093019201610acf565b905060405180925f90610b9384610a63565b8084529360018116908115610bff5750600114610bbb575b50610bb892500382610092565b90565b90505f9291925260205f20905f915b818310610be3575050906020610bb8928201015f610bab565b6020919350806001915483858801015201910190918392610bca565b905060209250610bb894915060ff191682840152151560051b8201015f610bab565b6004810180546001600160a01b031916905560028101805463ffffffff191690556001810180545f82559081610cd0575b50506007905f60038201556006810160ff1981541690550190610c758254610a63565b9182610c8057509050565b601f8311600114610c92575f90559050565b5f8181526020812093601f0160051c5f1901905b818110610cc05750505f9192508082528160208120915555565b6001905f82828801015501610ca6565b5f5260205f205f5b828110610ce55750610c52565b5f82820155600101610cd8565b905f806020600285015460e01b610d426024610d0d88610a9b565b6040519485918183019563ffffffff60e01b1686528051918291018484015e810186838201520301601f198101845283610092565b60048601549151916001600160a01b03165afa3d15610e0d5760033d93610d68856100c8565b94610d766040519687610092565b85523d5f602087013e5b0154600581901b906001600160fb1b03811603610b54575f938051602081115f14610e0757506020905b5f925b828410610dbc57505050509190565b90919295868201808311610b5457835181101561017757830160200151600388901b91906001600160f81b031916881560088a8504141715610b54576001921c179601929190610dad565b90610daa565b6003606093610d80565b604091949392606082019560018060a01b0316825260208201520152565b91905f5b6101008110610e4c57505090505f905f90565b8060ff0360ff8111610b54576004850154600190911b906001600160a01b03165f516020610fb45f395f51905f523b1561008e57835f91610ea160405194859384936370ca10bb60e01b855260048501610e17565b0381835f516020610fb45f395f51905f525af18015610a0f57610eef575b50610ec984610cf2565b81610ee5575b50610edc57600101610e39565b92505060019190565b905015155f610ecf565b5f610ef991610092565b5f610ebf565b91905f5b6101008110610f1657505090505f905f90565b60048401546001821b906001600160a01b03165f516020610fb45f395f51905f523b1561008e57835f91610f5e60405194859384936370ca10bb60e01b855260048501610e17565b0381835f516020610fb45f395f51905f525af18015610a0f57610fa3575b50610f8684610cf2565b81610f99575b50610edc57600101610f03565b905015155f610f8c565b5f610fad91610092565b5f610f7c56fe0000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da264697066735822122002f559c5d7a664602eedbb89efb180782a6528788cada338cbdf6bd3932b534d64736f6c634300082100336b656420736c6f742e2057652063616e2774206669742076616c7565206772650000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12db10e2d527612073b26eecdfd717e6a320cf44b4afac2b0732d9fcbe2b7fa0cf673746453746f726167652066696e642853746453746f72616765293a20506163a2646970667358221220a617a654321be8990b6eeb2649c13514d5db82b2b9f848d8e7acbb058b5a65a064736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> StdStorageTest:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[StdStorageTest]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, StdStorageTest, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[StdStorageTest]]:
        return cls._deploy(request_type, [], return_tx, StdStorageTest, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#12)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#12)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#12)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#12)
        """
        ...

    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#12)
        """
        return self._execute(self.chain, request_type, "0a9254e4", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#16)
        """
        ...

    @overload
    def test_StorageHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#16)
        """
        ...

    @overload
    def test_StorageHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#16)
        """
        ...

    @overload
    def test_StorageHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#16)
        """
        ...

    def test_StorageHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#16)
        """
        return self._execute(self.chain, request_type, "962b27ba", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#20)
        """
        ...

    @overload
    def test_StorageObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#20)
        """
        ...

    @overload
    def test_StorageObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#20)
        """
        ...

    @overload
    def test_StorageObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#20)
        """
        ...

    def test_StorageObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#20)
        """
        return self._execute(self.chain, request_type, "6af4e7be", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageExtraSload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#24)
        """
        ...

    @overload
    def test_StorageExtraSload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#24)
        """
        ...

    @overload
    def test_StorageExtraSload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#24)
        """
        ...

    @overload
    def test_StorageExtraSload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#24)
        """
        ...

    def test_StorageExtraSload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#24)
        """
        return self._execute(self.chain, request_type, "c79803c3", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#28)
        """
        ...

    @overload
    def test_StorageCheckedWriteHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#28)
        """
        ...

    @overload
    def test_StorageCheckedWriteHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#28)
        """
        ...

    @overload
    def test_StorageCheckedWriteHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#28)
        """
        ...

    def test_StorageCheckedWriteHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#28)
        """
        return self._execute(self.chain, request_type, "e1664d98", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#33)
        """
        ...

    @overload
    def test_StorageCheckedWriteObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#33)
        """
        ...

    @overload
    def test_StorageCheckedWriteObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#33)
        """
        ...

    @overload
    def test_StorageCheckedWriteObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#33)
        """
        ...

    def test_StorageCheckedWriteObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#33)
        """
        return self._execute(self.chain, request_type, "e87bfd9d", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteSignedIntegerHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#38)
        """
        ...

    @overload
    def test_StorageCheckedWriteSignedIntegerHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#38)
        """
        ...

    @overload
    def test_StorageCheckedWriteSignedIntegerHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#38)
        """
        ...

    @overload
    def test_StorageCheckedWriteSignedIntegerHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#38)
        """
        ...

    def test_StorageCheckedWriteSignedIntegerHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#38)
        """
        return self._execute(self.chain, request_type, "875ceb10", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteSignedIntegerObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#43)
        """
        ...

    @overload
    def test_StorageCheckedWriteSignedIntegerObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#43)
        """
        ...

    @overload
    def test_StorageCheckedWriteSignedIntegerObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#43)
        """
        ...

    @overload
    def test_StorageCheckedWriteSignedIntegerObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#43)
        """
        ...

    def test_StorageCheckedWriteSignedIntegerObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#43)
        """
        return self._execute(self.chain, request_type, "59faf338", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#48)
        """
        ...

    @overload
    def test_StorageMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#48)
        """
        ...

    @overload
    def test_StorageMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#48)
        """
        ...

    @overload
    def test_StorageMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#48)
        """
        ...

    def test_StorageMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#48)
        """
        return self._execute(self.chain, request_type, "71e0a254", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#54)
        """
        ...

    @overload
    def test_StorageMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#54)
        """
        ...

    @overload
    def test_StorageMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#54)
        """
        ...

    @overload
    def test_StorageMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#54)
        """
        ...

    def test_StorageMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#54)
        """
        return self._execute(self.chain, request_type, "e994e0b5", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#60)
        """
        ...

    @overload
    def test_StorageDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#60)
        """
        ...

    @overload
    def test_StorageDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#60)
        """
        ...

    @overload
    def test_StorageDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#60)
        """
        ...

    def test_StorageDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#60)
        """
        return self._execute(self.chain, request_type, "8499d1ab", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#66)
        """
        ...

    @overload
    def test_StorageCheckedWriteDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#66)
        """
        ...

    @overload
    def test_StorageCheckedWriteDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#66)
        """
        ...

    @overload
    def test_StorageCheckedWriteDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#66)
        """
        ...

    def test_StorageCheckedWriteDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#66)
        """
        return self._execute(self.chain, request_type, "a299aa5e", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#72)
        """
        ...

    @overload
    def test_StorageDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#72)
        """
        ...

    @overload
    def test_StorageDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#72)
        """
        ...

    @overload
    def test_StorageDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#72)
        """
        ...

    def test_StorageDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#72)
        """
        return self._execute(self.chain, request_type, "392e660a", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#83)
        """
        ...

    @overload
    def test_StorageDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#83)
        """
        ...

    @overload
    def test_StorageDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#83)
        """
        ...

    @overload
    def test_StorageDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#83)
        """
        ...

    def test_StorageDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#83)
        """
        return self._execute(self.chain, request_type, "ab861d24", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#94)
        """
        ...

    @overload
    def test_StorageCheckedWriteDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#94)
        """
        ...

    @overload
    def test_StorageCheckedWriteDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#94)
        """
        ...

    @overload
    def test_StorageCheckedWriteDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#94)
        """
        ...

    def test_StorageCheckedWriteDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#94)
        """
        return self._execute(self.chain, request_type, "3b61a950", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#102)
        """
        ...

    @overload
    def test_StorageCheckedWriteDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#102)
        """
        ...

    @overload
    def test_StorageCheckedWriteDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#102)
        """
        ...

    @overload
    def test_StorageCheckedWriteDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#102)
        """
        ...

    def test_StorageCheckedWriteDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#102)
        """
        return self._execute(self.chain, request_type, "b4747b20", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#110)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#110)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#110)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#110)
        """
        ...

    def test_StorageCheckedWriteMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#110)
        """
        return self._execute(self.chain, request_type, "495f0741", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#117)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#117)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#117)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#117)
        """
        ...

    def test_StorageCheckedWriteMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#117)
        """
        return self._execute(self.chain, request_type, "26d97d0b", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#124)
        """
        ...

    @overload
    def test_StorageStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#124)
        """
        ...

    @overload
    def test_StorageStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#124)
        """
        ...

    @overload
    def test_StorageStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#124)
        """
        ...

    def test_StorageStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#124)
        """
        return self._execute(self.chain, request_type, "f73aa19a", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#129)
        """
        ...

    @overload
    def test_StorageStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#129)
        """
        ...

    @overload
    def test_StorageStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#129)
        """
        ...

    @overload
    def test_StorageStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#129)
        """
        ...

    def test_StorageStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#129)
        """
        return self._execute(self.chain, request_type, "4acaea91", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#134)
        """
        ...

    @overload
    def test_StorageCheckedWriteStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#134)
        """
        ...

    @overload
    def test_StorageCheckedWriteStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#134)
        """
        ...

    @overload
    def test_StorageCheckedWriteStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#134)
        """
        ...

    def test_StorageCheckedWriteStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#134)
        """
        return self._execute(self.chain, request_type, "6dc33251", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#141)
        """
        ...

    @overload
    def test_StorageCheckedWriteStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#141)
        """
        ...

    @overload
    def test_StorageCheckedWriteStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#141)
        """
        ...

    @overload
    def test_StorageCheckedWriteStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#141)
        """
        ...

    def test_StorageCheckedWriteStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#141)
        """
        return self._execute(self.chain, request_type, "89e6cfe4", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageMapAddrFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#148)
        """
        ...

    @overload
    def test_StorageMapAddrFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#148)
        """
        ...

    @overload
    def test_StorageMapAddrFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#148)
        """
        ...

    @overload
    def test_StorageMapAddrFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#148)
        """
        ...

    def test_StorageMapAddrFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#148)
        """
        return self._execute(self.chain, request_type, "6c428ef8", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageMapAddrRoot(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#153)
        """
        ...

    @overload
    def test_StorageMapAddrRoot(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#153)
        """
        ...

    @overload
    def test_StorageMapAddrRoot(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#153)
        """
        ...

    @overload
    def test_StorageMapAddrRoot(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#153)
        """
        ...

    def test_StorageMapAddrRoot(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#153)
        """
        return self._execute(self.chain, request_type, "038cd192", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageMapUintFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#162)
        """
        ...

    @overload
    def test_StorageMapUintFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#162)
        """
        ...

    @overload
    def test_StorageMapUintFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#162)
        """
        ...

    @overload
    def test_StorageMapUintFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#162)
        """
        ...

    def test_StorageMapUintFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#162)
        """
        return self._execute(self.chain, request_type, "d8c172bf", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteMapUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#167)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#167)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#167)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#167)
        """
        ...

    def test_StorageCheckedWriteMapUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#167)
        """
        return self._execute(self.chain, request_type, "f2da1130", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteMapAddr(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#172)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapAddr(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#172)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapAddr(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#172)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapAddr(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#172)
        """
        ...

    def test_StorageCheckedWriteMapAddr(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#172)
        """
        return self._execute(self.chain, request_type, "6d422be6", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteMapBool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#177)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapBool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#177)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapBool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#177)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapBool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#177)
        """
        ...

    def test_StorageCheckedWriteMapBool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#177)
        """
        return self._execute(self.chain, request_type, "4def64da", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_StorageCheckedWriteMapPacked(self, addr: Union[Account, Address], value_: uint128, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#182)

        Args:
            addr: address
            value_: uint128
        """
        ...

    @overload
    def testFuzz_StorageCheckedWriteMapPacked(self, addr: Union[Account, Address], value_: uint128, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#182)

        Args:
            addr: address
            value_: uint128
        """
        ...

    @overload
    def testFuzz_StorageCheckedWriteMapPacked(self, addr: Union[Account, Address], value_: uint128, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#182)

        Args:
            addr: address
            value_: uint128
        """
        ...

    @overload
    def testFuzz_StorageCheckedWriteMapPacked(self, addr: Union[Account, Address], value_: uint128, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#182)

        Args:
            addr: address
            value_: uint128
        """
        ...

    def testFuzz_StorageCheckedWriteMapPacked(self, addr: Union[Account, Address], value_: uint128, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#182)

        Args:
            addr: address
            value_: uint128
        """
        return self._execute(self.chain, request_type, "2f644e92", [addr, value_], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteMapPackedFullSuccess(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#192)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapPackedFullSuccess(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#192)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapPackedFullSuccess(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#192)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapPackedFullSuccess(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#192)
        """
        ...

    def test_StorageCheckedWriteMapPackedFullSuccess(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#192)
        """
        return self._execute(self.chain, request_type, "05a7c0b4", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_RevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#201)
        """
        ...

    @overload
    def test_RevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#201)
        """
        ...

    @overload
    def test_RevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#201)
        """
        ...

    @overload
    def test_RevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#201)
        """
        ...

    def test_RevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#201)
        """
        return self._execute(self.chain, request_type, "ebefd727", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_StorageNativePack(self, val1: uint248, val2: uint248, boolVal1: bool, boolVal2: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#208)

        Args:
            val1: uint248
            val2: uint248
            boolVal1: bool
            boolVal2: bool
        """
        ...

    @overload
    def testFuzz_StorageNativePack(self, val1: uint248, val2: uint248, boolVal1: bool, boolVal2: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#208)

        Args:
            val1: uint248
            val2: uint248
            boolVal1: bool
            boolVal2: bool
        """
        ...

    @overload
    def testFuzz_StorageNativePack(self, val1: uint248, val2: uint248, boolVal1: bool, boolVal2: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#208)

        Args:
            val1: uint248
            val2: uint248
            boolVal1: bool
            boolVal2: bool
        """
        ...

    @overload
    def testFuzz_StorageNativePack(self, val1: uint248, val2: uint248, boolVal1: bool, boolVal2: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#208)

        Args:
            val1: uint248
            val2: uint248
            boolVal1: bool
            boolVal2: bool
        """
        ...

    def testFuzz_StorageNativePack(self, val1: uint248, val2: uint248, boolVal1: bool, boolVal2: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#208)

        Args:
            val1: uint248
            val2: uint248
            boolVal1: bool
            boolVal2: bool
        """
        return self._execute(self.chain, request_type, "65bee949", [val1, val2, boolVal1, boolVal2], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageReadBytes32(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#220)
        """
        ...

    @overload
    def test_StorageReadBytes32(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#220)
        """
        ...

    @overload
    def test_StorageReadBytes32(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#220)
        """
        ...

    @overload
    def test_StorageReadBytes32(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#220)
        """
        ...

    def test_StorageReadBytes32(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#220)
        """
        return self._execute(self.chain, request_type, "379a42ae", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageReadBool_False(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#225)
        """
        ...

    @overload
    def test_StorageReadBool_False(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#225)
        """
        ...

    @overload
    def test_StorageReadBool_False(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#225)
        """
        ...

    @overload
    def test_StorageReadBool_False(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#225)
        """
        ...

    def test_StorageReadBool_False(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#225)
        """
        return self._execute(self.chain, request_type, "edf3c69a", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageReadBool_True(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#230)
        """
        ...

    @overload
    def test_StorageReadBool_True(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#230)
        """
        ...

    @overload
    def test_StorageReadBool_True(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#230)
        """
        ...

    @overload
    def test_StorageReadBool_True(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#230)
        """
        ...

    def test_StorageReadBool_True(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#230)
        """
        return self._execute(self.chain, request_type, "d8e24c43", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_RevertIf_ReadingNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#235)
        """
        ...

    @overload
    def test_RevertIf_ReadingNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#235)
        """
        ...

    @overload
    def test_RevertIf_ReadingNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#235)
        """
        ...

    @overload
    def test_RevertIf_ReadingNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#235)
        """
        ...

    def test_RevertIf_ReadingNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#235)
        """
        return self._execute(self.chain, request_type, "ed60529b", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def readNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#240)
        """
        ...

    @overload
    def readNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#240)
        """
        ...

    @overload
    def readNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#240)
        """
        ...

    @overload
    def readNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#240)
        """
        ...

    def readNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#240)
        """
        return self._execute(self.chain, request_type, "52e52ac6", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageReadAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#244)
        """
        ...

    @overload
    def test_StorageReadAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#244)
        """
        ...

    @overload
    def test_StorageReadAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#244)
        """
        ...

    @overload
    def test_StorageReadAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#244)
        """
        ...

    def test_StorageReadAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#244)
        """
        return self._execute(self.chain, request_type, "e1b943a2", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageReadUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#249)
        """
        ...

    @overload
    def test_StorageReadUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#249)
        """
        ...

    @overload
    def test_StorageReadUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#249)
        """
        ...

    @overload
    def test_StorageReadUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#249)
        """
        ...

    def test_StorageReadUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#249)
        """
        return self._execute(self.chain, request_type, "f15d536f", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageReadInt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#254)
        """
        ...

    @overload
    def test_StorageReadInt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#254)
        """
        ...

    @overload
    def test_StorageReadInt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#254)
        """
        ...

    @overload
    def test_StorageReadInt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#254)
        """
        ...

    def test_StorageReadInt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#254)
        """
        return self._execute(self.chain, request_type, "9792466b", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_Packed(self, val: uint256, elemToGet: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#259)

        Args:
            val: uint256
            elemToGet: uint8
        """
        ...

    @overload
    def testFuzz_Packed(self, val: uint256, elemToGet: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#259)

        Args:
            val: uint256
            elemToGet: uint8
        """
        ...

    @overload
    def testFuzz_Packed(self, val: uint256, elemToGet: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#259)

        Args:
            val: uint256
            elemToGet: uint8
        """
        ...

    @overload
    def testFuzz_Packed(self, val: uint256, elemToGet: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#259)

        Args:
            val: uint256
            elemToGet: uint8
        """
        ...

    def testFuzz_Packed(self, val: uint256, elemToGet: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#259)

        Args:
            val: uint256
            elemToGet: uint8
        """
        return self._execute(self.chain, request_type, "599377dd", [val, elemToGet], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_Packed2(self, nvars: uint256, seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#301)

        Args:
            nvars: uint256
            seed: uint256
        """
        ...

    @overload
    def testFuzz_Packed2(self, nvars: uint256, seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#301)

        Args:
            nvars: uint256
            seed: uint256
        """
        ...

    @overload
    def testFuzz_Packed2(self, nvars: uint256, seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#301)

        Args:
            nvars: uint256
            seed: uint256
        """
        ...

    @overload
    def testFuzz_Packed2(self, nvars: uint256, seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#301)

        Args:
            nvars: uint256
            seed: uint256
        """
        ...

    def testFuzz_Packed2(self, nvars: uint256, seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#301)

        Args:
            nvars: uint256
            seed: uint256
        """
        return self._execute(self.chain, request_type, "6cc48782", [nvars, seed], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testEdgeCaseArray(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#349)
        """
        ...

    @overload
    def testEdgeCaseArray(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#349)
        """
        ...

    @overload
    def testEdgeCaseArray(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#349)
        """
        ...

    @overload
    def testEdgeCaseArray(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#349)
        """
        ...

    def testEdgeCaseArray(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#349)
        """
        return self._execute(self.chain, request_type, "d95266eb", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

StdStorageTest.setUp.selector = bytes4(b'\n\x92T\xe4')
StdStorageTest.test_StorageHidden.selector = bytes4(b"\x96+'\xba")
StdStorageTest.test_StorageObvious.selector = bytes4(b'j\xf4\xe7\xbe')
StdStorageTest.test_StorageExtraSload.selector = bytes4(b'\xc7\x98\x03\xc3')
StdStorageTest.test_StorageCheckedWriteHidden.selector = bytes4(b'\xe1fM\x98')
StdStorageTest.test_StorageCheckedWriteObvious.selector = bytes4(b'\xe8{\xfd\x9d')
StdStorageTest.test_StorageCheckedWriteSignedIntegerHidden.selector = bytes4(b'\x87\\\xeb\x10')
StdStorageTest.test_StorageCheckedWriteSignedIntegerObvious.selector = bytes4(b'Y\xfa\xf38')
StdStorageTest.test_StorageMapStructA.selector = bytes4(b'q\xe0\xa2T')
StdStorageTest.test_StorageMapStructB.selector = bytes4(b'\xe9\x94\xe0\xb5')
StdStorageTest.test_StorageDeepMap.selector = bytes4(b'\x84\x99\xd1\xab')
StdStorageTest.test_StorageCheckedWriteDeepMap.selector = bytes4(b'\xa2\x99\xaa^')
StdStorageTest.test_StorageDeepMapStructA.selector = bytes4(b'9.f\n')
StdStorageTest.test_StorageDeepMapStructB.selector = bytes4(b'\xab\x86\x1d$')
StdStorageTest.test_StorageCheckedWriteDeepMapStructA.selector = bytes4(b';a\xa9P')
StdStorageTest.test_StorageCheckedWriteDeepMapStructB.selector = bytes4(b'\xb4t{ ')
StdStorageTest.test_StorageCheckedWriteMapStructA.selector = bytes4(b'I_\x07A')
StdStorageTest.test_StorageCheckedWriteMapStructB.selector = bytes4(b'&\xd9}\x0b')
StdStorageTest.test_StorageStructA.selector = bytes4(b'\xf7:\xa1\x9a')
StdStorageTest.test_StorageStructB.selector = bytes4(b'J\xca\xea\x91')
StdStorageTest.test_StorageCheckedWriteStructA.selector = bytes4(b'm\xc32Q')
StdStorageTest.test_StorageCheckedWriteStructB.selector = bytes4(b'\x89\xe6\xcf\xe4')
StdStorageTest.test_StorageMapAddrFound.selector = bytes4(b'lB\x8e\xf8')
StdStorageTest.test_StorageMapAddrRoot.selector = bytes4(b'\x03\x8c\xd1\x92')
StdStorageTest.test_StorageMapUintFound.selector = bytes4(b'\xd8\xc1r\xbf')
StdStorageTest.test_StorageCheckedWriteMapUint.selector = bytes4(b'\xf2\xda\x110')
StdStorageTest.test_StorageCheckedWriteMapAddr.selector = bytes4(b'mB+\xe6')
StdStorageTest.test_StorageCheckedWriteMapBool.selector = bytes4(b'M\xefd\xda')
StdStorageTest.testFuzz_StorageCheckedWriteMapPacked.selector = bytes4(b'/dN\x92')
StdStorageTest.test_StorageCheckedWriteMapPackedFullSuccess.selector = bytes4(b'\x05\xa7\xc0\xb4')
StdStorageTest.test_RevertStorageConst.selector = bytes4(b"\xeb\xef\xd7'")
StdStorageTest.testFuzz_StorageNativePack.selector = bytes4(b'e\xbe\xe9I')
StdStorageTest.test_StorageReadBytes32.selector = bytes4(b'7\x9aB\xae')
StdStorageTest.test_StorageReadBool_False.selector = bytes4(b'\xed\xf3\xc6\x9a')
StdStorageTest.test_StorageReadBool_True.selector = bytes4(b'\xd8\xe2LC')
StdStorageTest.test_RevertIf_ReadingNonBoolValue.selector = bytes4(b'\xed`R\x9b')
StdStorageTest.readNonBoolValue.selector = bytes4(b'R\xe5*\xc6')
StdStorageTest.test_StorageReadAddress.selector = bytes4(b'\xe1\xb9C\xa2')
StdStorageTest.test_StorageReadUint.selector = bytes4(b'\xf1]So')
StdStorageTest.test_StorageReadInt.selector = bytes4(b'\x97\x92Fk')
StdStorageTest.testFuzz_Packed.selector = bytes4(b'Y\x93w\xdd')
StdStorageTest.testFuzz_Packed2.selector = bytes4(b'l\xc4\x87\x82')
StdStorageTest.testEdgeCaseArray.selector = bytes4(b'\xd9Rf\xeb')
class StorageTestTarget(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#355)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'contract StorageTest', 'name': 'test_', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\x9c\x95U\xb1\xe3\x10.<\xf4\x8fB}y\xcbg\x8f]\x9b\xd1\xed\n\xd5t8\x94a\xe2U\xf9Qp\xed': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'who', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes4', 'name': 'fsig', 'type': 'bytes4'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'keysHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'slot', 'type': 'uint256'}], 'name': 'SlotFound', 'type': 'event'}, b'\x08\x0f\xc4\xa9f \xc4F.p[#\xf3FA?\xe3yk\xb6<o\x8d\x85\x91\xba\xec\x0e#\x15w\xa5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'who', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'slot', 'type': 'uint256'}], 'name': 'WARNING_UninitedSlot', 'type': 'event'}, b'\xfcZ\xec+': {'inputs': [], 'name': 'expectRevertStorageConst', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":41988,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"stdstore","offset":0,"slot":0,"type":"t_struct(StdStorage)8331_storage"},{"astId":41991,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"test","offset":0,"slot":8,"type":"t_contract(StorageTest)42383"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_contract(StorageTest)42383":{"encoding":"inplace","label":"contract StorageTest","numberOfBytes":20},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))"},"t_mapping(t_bytes32,t_struct(FindData)8306_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)8306_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)8306_storage)"},"t_struct(FindData)8306_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":8299,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":8301,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":8303,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":8305,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(StdStorage)8331_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":8315,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))"},{"astId":8318,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":8320,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":8322,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":8324,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":8326,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":8328,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":8330,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "608034607057601f61109238819003918201601f19168301916001600160401b03831184841017607457808492602094604052833981010312607057516001600160a01b03811690819003607057600880546001600160a01b03191691909117905560405161100990816100898239f35b5f80fd5b634e487b7160e01b5f52604160045260245ffdfe60806040526004361015610011575f80fd5b5f3560e01c63fc5aec2b14610024575f80fd5b3461008e575f36600319011261008e5760018060a01b036008541660018060a01b0319600454161760045560076020604051610061604082610092565b8281520166636f6e7374282960c81b81522060e01c63ffffffff19600254161760025561008c61018b565b005b5f80fd5b90601f8019910116810190811067ffffffffffffffff8211176100b457604052565b634e487b7160e01b5f52604160045260245ffd5b67ffffffffffffffff81116100b457601f01601f191660200190565b60209291908391805192839101825e019081520190565b9080601f8301121561008e5781519167ffffffffffffffff83116100b4578260051b906040519361012f6020840186610092565b845260208085019282010192831161008e57602001905b8282106101535750505090565b8151815260209182019101610146565b80518210156101775760209160051b010190565b634e487b7160e01b5f52603260045260245ffd5b6004546002546003546001600160a01b03909216915f9160e01b6101ae83610a9b565b90845f525f60205260405f209063ffffffff60e01b1690815f5260205260405f2060405160208101906101f4816101e68888866100e4565b03601f198101835282610092565b5190205f5260205260ff600360405f20015416610a1a575f516020610fb45f395f51905f523b1561008e5760405163266cf10960e01b81525f81600481835f516020610fb45f395f51905f525af18015610a0f576109fa575b5061025784610cf2565b90506040516365bc948160e01b815286600482015285816024815f516020610fb45f395f51905f525afa9081156109ef578691610981575b5080518061030157608460405162461bcd60e51b815260206004820152604060248201527f73746453746f726167652066696e642853746453746f72616765293a204e6f2060448201527f73746f726167652075736520646574656374656420666f72207461726765742e6064820152fd5b801561096d579061034d915f190190602061031c8383610163565b51604051630667f9d760e41b81526001600160a01b038c166004820152602481019190915293849081906044820190565b03815f516020610fb45f395f51905f525afa92831561096257889361092f575b5082156108f0575b61037f8282610163565b5160048054604051630667f9d760e41b81526001600160a01b03909116918101829052602481018390529091906020816044815f516020610fb45f395f51905f525afa9081156108e5578b916108b4575b506103da8b610cf2565b91909382155f146108ad575f19905b5f516020610fb45f395f51905f523b1561089457848e9161041e60405194859384936370ca10bb60e01b855260048501610e17565b0381835f516020610fb45f395f51905f525af1801561081157908d91610898575b5061044990610cf2565b600454909491506001600160a01b03165f516020610fb45f395f51905f523b1561089457908d9161048e60405194859384936370ca10bb60e01b855260048501610e17565b0381835f516020610fb45f395f51905f525af1801561088957908c91610870575b505082610865575b50501561085e578793889360ff600654166106ea575b6001858701610100031b5f1901851b16841c81036106e1575090610553917f9c9555b1e3102e3cf48f427d79cb678f5d9bd1ed0ad574389461e255f95170ed60808b896101e66105288d6040519283916020830195866100e4565b5190206105358686610163565b51906040519283528a602084015260408301526060820152a1610163565b5190604051916080830183811067ffffffffffffffff8211176106cd57906003939291604052825260208201938452604082019081526060820193600185528989528860205260408920868a526020526040892060405160208101906105be816101e68d8d866100e4565b5190208a526020526040892092518355516001830155516002820155019051151560ff801983541691161790558484528360205260408420818552602052604084206040516020810190610617816101e68888866100e4565b519020855260205260ff600360408620015416156106705760409461063b85610c21565b8452836020528484209084526020526101e66106648585209386519283916020830195866100e4565b51902082526020522090565b60405162461bcd60e51b815260206004820152602f60248201527f73746453746f726167652066696e642853746453746f72616765293a20536c6f60448201526e3a143994903737ba103337bab7321760891b6064820152608490fd5b634e487b7160e01b89526041600452602489fd5b93509150610301565b945061073893506106fb8383610163565b5160048054604051630667f9d760e41b81526001600160a01b03909116918101919091526024810182905290959094602090869081906044820190565b03815f516020610fb45f395f51905f525afa948515610853578a95610820575b50610763868b610e35565b959096610770818d610eff565b60045490939192906001600160a01b03165f516020610fb45f395f51905f523b1561081c57908e916107b660405194859384936370ca10bb60e01b855260048501610e17565b0381835f516020610fb45f395f51905f525af1801561081157908d916107f8575b5050876107f0575b5094956104cd575093509150610301565b96505f6107df565b8161080291610092565b61080d578b5f6107d7565b8b80fd5b6040513d8f823e3d90fd5b8e80fd5b9094506020813d821161084b575b8161083b60209383610092565b8101031261008e5751935f610758565b3d915061082e565b6040513d8c823e3d90fd5b9150610301565b141590505f806104b7565b8161087a91610092565b610885578a5f6104af565b8a80fd5b6040513d8e823e3d90fd5b8d80fd5b816108a291610092565b61080d578b5f61043f565b8c906103e9565b90506020813d82116108dd575b816108ce60209383610092565b8101031261008e57515f6103d0565b3d91506108c1565b6040513d8d823e3d90fd5b7f080fc4a96620c4462e705b23f346413fe3796bb63c6f8d8591baec0e231577a5604061091d8484610163565b518151908c82526020820152a1610375565b9092506020813d821161095a575b8161094a60209383610092565b8101031261008e5751915f61036d565b3d915061093d565b6040513d8a823e3d90fd5b634e487b7160e01b87526011600452602487fd5b90503d8087833e6109928183610092565b81016040828203126109eb57815167ffffffffffffffff81116109e757816109bb9184016100fb565b9160208101519067ffffffffffffffff82116109e3576109dc9291016100fb565b505f61028f565b8880fd5b8780fd5b8680fd5b6040513d88823e3d90fd5b610a079194505f90610092565b5f925f61024d565b6040513d5f823e3d90fd5b9193909250610a285f610c21565b5f525f60205260405f20905f526020526101e6610a5460405f20936040519283916020830195866100e4565b5190205f5260205260405f2090565b90600182811c92168015610a91575b6020831014610a7d57565b634e487b7160e01b5f52602260045260245ffd5b91607f1691610a72565b60078101908154610aab81610a63565b610b815750600191500190604051808360208295549384815201905f5260205f20925f5b818110610b68575050610ae492500383610092565b81518060051b9080820460201490151715610b5457610b02816100c8565b90610b106040519283610092565b808252610b1f601f19916100c8565b013660208301375f5b8351811015610b4f5780610b3e60019286610163565b5160208260051b8501015201610b28565b509150565b634e487b7160e01b5f52601160045260245ffd5b8454835260019485019487945060209093019201610acf565b905060405180925f90610b9384610a63565b8084529360018116908115610bff5750600114610bbb575b50610bb892500382610092565b90565b90505f9291925260205f20905f915b818310610be3575050906020610bb8928201015f610bab565b6020919350806001915483858801015201910190918392610bca565b905060209250610bb894915060ff191682840152151560051b8201015f610bab565b6004810180546001600160a01b031916905560028101805463ffffffff191690556001810180545f82559081610cd0575b50506007905f60038201556006810160ff1981541690550190610c758254610a63565b9182610c8057509050565b601f8311600114610c92575f90559050565b5f8181526020812093601f0160051c5f1901905b818110610cc05750505f9192508082528160208120915555565b6001905f82828801015501610ca6565b5f5260205f205f5b828110610ce55750610c52565b5f82820155600101610cd8565b905f806020600285015460e01b610d426024610d0d88610a9b565b6040519485918183019563ffffffff60e01b1686528051918291018484015e810186838201520301601f198101845283610092565b60048601549151916001600160a01b03165afa3d15610e0d5760033d93610d68856100c8565b94610d766040519687610092565b85523d5f602087013e5b0154600581901b906001600160fb1b03811603610b54575f938051602081115f14610e0757506020905b5f925b828410610dbc57505050509190565b90919295868201808311610b5457835181101561017757830160200151600388901b91906001600160f81b031916881560088a8504141715610b54576001921c179601929190610dad565b90610daa565b6003606093610d80565b604091949392606082019560018060a01b0316825260208201520152565b91905f5b6101008110610e4c57505090505f905f90565b8060ff0360ff8111610b54576004850154600190911b906001600160a01b03165f516020610fb45f395f51905f523b1561008e57835f91610ea160405194859384936370ca10bb60e01b855260048501610e17565b0381835f516020610fb45f395f51905f525af18015610a0f57610eef575b50610ec984610cf2565b81610ee5575b50610edc57600101610e39565b92505060019190565b905015155f610ecf565b5f610ef991610092565b5f610ebf565b91905f5b6101008110610f1657505090505f905f90565b60048401546001821b906001600160a01b03165f516020610fb45f395f51905f523b1561008e57835f91610f5e60405194859384936370ca10bb60e01b855260048501610e17565b0381835f516020610fb45f395f51905f525af18015610a0f57610fa3575b50610f8684610cf2565b81610f99575b50610edc57600101610f03565b905015155f610f8c565b5f610fad91610092565b5f610f7c56fe0000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da264697066735822122002f559c5d7a664602eedbb89efb180782a6528788cada338cbdf6bd3932b534d64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, test_: StorageTest, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#361)

        Args:
            test_: contract StorageTest
        """
        ...

    @overload
    @classmethod
    def deploy(cls, test_: StorageTest, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> StorageTestTarget:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#361)

        Args:
            test_: contract StorageTest
        """
        ...

    @overload
    @classmethod
    def deploy(cls, test_: StorageTest, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#361)

        Args:
            test_: contract StorageTest
        """
        ...

    @overload
    @classmethod
    def deploy(cls, test_: StorageTest, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#361)

        Args:
            test_: contract StorageTest
        """
        ...

    @overload
    @classmethod
    def deploy(cls, test_: StorageTest, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[StorageTestTarget]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#361)

        Args:
            test_: contract StorageTest
        """
        ...

    @classmethod
    def deploy(cls, test_: StorageTest, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, StorageTestTarget, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[StorageTestTarget]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#361)

        Args:
            test_: contract StorageTest
        """
        return cls._deploy(request_type, [test_], return_tx, StorageTestTarget, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def expectRevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#365)
        """
        ...

    @overload
    def expectRevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#365)
        """
        ...

    @overload
    def expectRevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#365)
        """
        ...

    @overload
    def expectRevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#365)
        """
        ...

    def expectRevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#365)
        """
        return self._execute(self.chain, request_type, "fc5aec2b", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

StorageTestTarget.expectRevertStorageConst.selector = bytes4(b'\xfcZ\xec+')
class StorageTest(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#370)
    """
    _abi = {'constructor': {'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\x15\xe8\xb3E': {'inputs': [], 'name': 'basic', 'outputs': [{'internalType': 'uint256', 'name': 'a', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'b', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b';\x80\xa7\x93': {'inputs': [], 'name': 'const', 'outputs': [{'internalType': 'bytes32', 'name': 't', 'type': 'bytes32'}], 'stateMutability': 'pure', 'type': 'function'}, b'\x8c\xd8\x15m': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'deep_map', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x03\x10\xc0`': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'deep_map_struct', 'outputs': [{'internalType': 'uint256', 'name': 'a', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'b', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe9.\x9d\xc4': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'edgeCaseArray', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'&|J\xe4': {'inputs': [], 'name': 'exists', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x9ey6\xe6': {'inputs': [], 'name': 'extra_sload', 'outputs': [{'internalType': 'bytes32', 'name': 't', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1a\xa8D\xb4': {'inputs': [{'internalType': 'uint256', 'name': 'size', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'offset', 'type': 'uint256'}], 'name': 'getRandomPacked', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'a\xa9ui': {'inputs': [{'internalType': 'uint8', 'name': 'shifts', 'type': 'uint8'}, {'internalType': 'uint8[]', 'name': 'shiftSizes', 'type': 'uint8[]'}, {'internalType': 'uint8', 'name': 'elem', 'type': 'uint8'}], 'name': 'getRandomPacked', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xae\xf6\xd4\xb1': {'inputs': [], 'name': 'hidden', 'outputs': [{'internalType': 'bytes32', 'name': 't', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa7>@\xcc': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'map_addr', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x8ckEQ': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'map_bool', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\\#\xfe\x9e': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'map_packed', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'PD)\xbf': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'map_struct', 'outputs': [{'internalType': 'uint256', 'name': 'a', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'b', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'jV\xc3\xd4': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'map_uint', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'A\xb6\xed\xb2': {'inputs': [{'internalType': 'address', 'name': 'who', 'type': 'address'}], 'name': 'read_struct_lower', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'>\xae"\x18': {'inputs': [{'internalType': 'address', 'name': 'who', 'type': 'address'}], 'name': 'read_struct_upper', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x19q\xf0\x0b': {'inputs': [{'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'size', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'offset', 'type': 'uint256'}], 'name': 'setRandomPacking', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xaaF8&': {'inputs': [{'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}], 'name': 'setRandomPacking', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'y\xda~M': {'inputs': [], 'name': 'tA', 'outputs': [{'internalType': 'uint248', 'name': '', 'type': 'uint248'}], 'stateMutability': 'view', 'type': 'function'}, b'W5\x1cE': {'inputs': [], 'name': 'tB', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xebS\xf9\x90': {'inputs': [], 'name': 'tC', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe4\xc6*\x11': {'inputs': [], 'name': 'tD', 'outputs': [{'internalType': 'uint248', 'name': '', 'type': 'uint248'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb7\xe1\x9e)': {'inputs': [], 'name': 'tE', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\x08\xf2:\xad': {'inputs': [], 'name': 'tF', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe5\xed\x1e\xfe': {'inputs': [], 'name': 'tG', 'outputs': [{'internalType': 'int256', 'name': '', 'type': 'int256'}], 'stateMutability': 'view', 'type': 'function'}, b'O\x87\xae\xb7': {'inputs': [], 'name': 'tH', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":42024,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"exists","offset":0,"slot":0,"type":"t_uint256"},{"astId":42028,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"map_addr","offset":0,"slot":1,"type":"t_mapping(t_address,t_uint256)"},{"astId":42032,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"map_uint","offset":0,"slot":2,"type":"t_mapping(t_uint256,t_uint256)"},{"astId":42036,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"map_packed","offset":0,"slot":3,"type":"t_mapping(t_address,t_uint256)"},{"astId":42041,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"map_struct","offset":0,"slot":4,"type":"t_mapping(t_address,t_struct(UnpackedStruct)42072_storage)"},{"astId":42047,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"deep_map","offset":0,"slot":5,"type":"t_mapping(t_address,t_mapping(t_address,t_uint256))"},{"astId":42054,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"deep_map_struct","offset":0,"slot":6,"type":"t_mapping(t_address,t_mapping(t_address,t_struct(UnpackedStruct)42072_storage))"},{"astId":42057,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"basic","offset":0,"slot":7,"type":"t_struct(UnpackedStruct)42072_storage"},{"astId":42059,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"tA","offset":0,"slot":9,"type":"t_uint248"},{"astId":42061,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"tB","offset":31,"slot":9,"type":"t_bool"},{"astId":42064,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"tC","offset":0,"slot":10,"type":"t_bool"},{"astId":42067,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"tD","offset":1,"slot":10,"type":"t_uint248"},{"astId":42076,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"map_bool","offset":0,"slot":11,"type":"t_mapping(t_address,t_bool)"},{"astId":42079,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"tE","offset":0,"slot":12,"type":"t_bytes32"},{"astId":42085,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"tF","offset":0,"slot":13,"type":"t_address"},{"astId":42092,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"tG","offset":0,"slot":14,"type":"t_int256"},{"astId":42095,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"tH","offset":0,"slot":15,"type":"t_bool"},{"astId":42102,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"tI","offset":0,"slot":16,"type":"t_bytes32"},{"astId":42104,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"randomPacking","offset":0,"slot":17,"type":"t_uint256"},{"astId":42111,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"edgeCaseArray","offset":0,"slot":18,"type":"t_array(t_uint256)dyn_storage"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_uint256)dyn_storage":{"encoding":"dynamic_array","label":"uint256[]","numberOfBytes":32,"base":"t_uint256"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_int256":{"encoding":"inplace","label":"int256","numberOfBytes":32},"t_mapping(t_address,t_bool)":{"encoding":"mapping","label":"mapping(address => bool)","numberOfBytes":32,"key":"t_address","value":"t_bool"},"t_mapping(t_address,t_mapping(t_address,t_struct(UnpackedStruct)42072_storage))":{"encoding":"mapping","label":"mapping(address => mapping(address => struct StorageTest.UnpackedStruct))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_address,t_struct(UnpackedStruct)42072_storage)"},"t_mapping(t_address,t_mapping(t_address,t_uint256))":{"encoding":"mapping","label":"mapping(address => mapping(address => uint256))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_address,t_uint256)"},"t_mapping(t_address,t_struct(UnpackedStruct)42072_storage)":{"encoding":"mapping","label":"mapping(address => struct StorageTest.UnpackedStruct)","numberOfBytes":32,"key":"t_address","value":"t_struct(UnpackedStruct)42072_storage"},"t_mapping(t_address,t_uint256)":{"encoding":"mapping","label":"mapping(address => uint256)","numberOfBytes":32,"key":"t_address","value":"t_uint256"},"t_mapping(t_uint256,t_uint256)":{"encoding":"mapping","label":"mapping(uint256 => uint256)","numberOfBytes":32,"key":"t_uint256","value":"t_uint256"},"t_struct(UnpackedStruct)42072_storage":{"encoding":"inplace","label":"struct StorageTest.UnpackedStruct","numberOfBytes":64,"members":[{"astId":42069,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"a","offset":0,"slot":0,"type":"t_uint256"},{"astId":42071,"contract":"lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"b","offset":0,"slot":1,"type":"t_uint256"}]},"t_uint248":{"encoding":"inplace","label":"uint248","numberOfBytes":31},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "6080604052346101755760015f819055610100600a5561133760f01b600c55600d80546001600160a01b031916610539179055600160ff1b600e55600f805460ff19169091179055600161ecc960f01b03601055604051606081016001600160401b0381118282101761011c57604052600381526003602082015260036040820152601254600360125580600310610147575b5060125f5260205f20905f5b6003811061013057604080519081016001600160401b0381118282101761011c57610539916020916040528281520152610539600755610539600855335f52600360205270010000000000000000000000000000000160405f20556105395f526003602052600160801b60405f20556040516109b5908161017a8239f35b634e487b7160e01b5f52604160045260245ffd5b600190602060ff845116930192818501550161009e565b60125f5260205f209060021901905f5b828110610165575050610092565b5f82820160030155600101610157565b5f80fdfe60806040526004361015610011575f80fd5b5f3560e01c80630310c060146101c457806308f23aad146101bf57806315e8b345146101ba5780631971f00b146101b55780631aa844b4146101b0578063267c4ae4146101ab5780633b80a793146101a65780633eae2218146101a157806341b6edb21461019c5780634f87aeb714610197578063504429bf1461019257806357351c451461018d5780635c23fe9e1461018857806361a97569146101835780636a56c3d41461017e57806379da7e4d146101795780638c6b4551146101745780638cd8156d1461016f5780639e7936e61461016a578063a73e40cc14610165578063aa46382614610160578063aef6d4b11461015b578063b7e19e2914610156578063e4c62a1114610151578063e5ed1efe1461014c578063e92e9dc4146101475763eb53f99014610142575f80fd5b6107f8565b6107a8565b61078b565b61076b565b61074e565b610712565b6106f9565b6106c1565b61069a565b610643565b610606565b6105de565b6105b4565b6104de565b610464565b610442565b6103f1565b6103cf565b61038f565b610354565b610334565b610318565b6102e9565b6102b6565b61028e565b610266565b6101f9565b600435906001600160a01b03821682036101df57565b5f80fd5b602435906001600160a01b03821682036101df57565b346101df5760403660031901126101df576102466102156101c9565b61021d6101e3565b9060018060a01b03165f52600660205260405f209060018060a01b03165f5260205260405f2090565b8054600190910154604080519283526020830191909152819081015b0390f35b346101df575f3660031901126101df57600d546040516001600160a01b039091168152602090f35b346101df575f3660031901126101df5760075460085460408051928352602083019190915290f35b346101df5760603660031901126101df576011805460016024351b5f190160443590811b1990911660043590911b179055005b346101df5760403660031901126101df576011546040516024359190911c60016004351b5f1901168152602090f35b346101df575f3660031901126101df5760205f54604051908152f35b346101df575f3660031901126101df5760405161133760f01b8152602090f35b346101df5760203660031901126101df576001600160a01b036103756101c9565b165f526003602052602060405f205460801c604051908152f35b346101df5760203660031901126101df576001600160a01b036103b06101c9565b165f526003602052602060018060801b0360405f205416604051908152f35b346101df575f3660031901126101df57602060ff600f54166040519015158152f35b346101df5760203660031901126101df576001600160a01b036104126101c9565b165f52600460205260405f2060018154910154906102626040519283928360209093929193604081019481520152565b346101df575f3660031901126101df57602060095460f81c6040519015158152f35b346101df5760203660031901126101df576001600160a01b036104856101c9565b165f526003602052602060405f2054604051908152f35b6004359060ff821682036101df57565b6044359060ff821682036101df57565b359060ff821682036101df57565b634e487b7160e01b5f52604160045260245ffd5b346101df5760603660031901126101df576104f761049c565b60243567ffffffffffffffff81116101df57366023820112156101df5780600401359067ffffffffffffffff82116105af578160051b60405192601f19603f830116840184811067ffffffffffffffff8211176105af57604052835260246020840191830101913683116101df57602401905b8282106105975761026261058786866105816104ac565b916108ac565b6040519081529081906020820190565b602080916105a4846104bc565b81520191019061056a565b6104ca565b346101df5760203660031901126101df576004355f526002602052602060405f2054604051908152f35b346101df575f3660031901126101df576009546040516001600160f81b039091168152602090f35b346101df5760203660031901126101df576001600160a01b036106276101c9565b165f52600b602052602060ff60405f2054166040519015158152f35b346101df5760403660031901126101df5760206106916106616101c9565b6106696101e3565b6001600160a01b039182165f9081526005855260408082209290931681526020919091522090565b54604051908152f35b346101df575f3660031901126101df575f808080600c545afa506020601054604051908152f35b346101df5760203660031901126101df576001600160a01b036106e26101c9565b165f526001602052602060405f2054604051908152f35b346101df5760203660031901126101df57600435601155005b346101df575f3660031901126101df5760207fb27fb258786eae8f9ffde06a5bfd55f5193cb73bd64e533d5d75fd7cb46652ff54604051908152f35b346101df575f3660031901126101df576020600c54604051908152f35b346101df575f3660031901126101df576020600a5460081c604051908152f35b346101df575f3660031901126101df576020600e54604051908152f35b346101df5760203660031901126101df576004356012548110156101df5760125f527fbb8a6a4669ba250d26cd7a459eca9d215f8307e33aebe50379bc5a3617ec34440154604051908152602090f35b346101df575f3660031901126101df57602060ff600a54166040519015158152f35b1561082157565b60405162461bcd60e51b815260206004820152600560248201526421656c656d60d81b6044820152606490fd5b80518210156108625760209160051b010190565b634e487b7160e01b5f52603260045260245ffd5b634e487b7160e01b5f52601160045260245ffd5b9190820180921161089757565b610876565b6101000390610100821161089757565b929160ff806108bf92169416841061081a565b5f905f935f925b82518410156109395781841015610909576109006001916108fa6108f46108ed888861084e565b5160ff1690565b60ff1690565b9061088a565b935b01926108c6565b9280820361091a575b600190610902565b946109316001916108fa6108f46108ed8a8861084e565b959050610912565b9061097b935061096a8661096561095f6108f46108ed6108fa9661096f999c9b9c61084e565b8561088a565b61088a565b61089c565b91601154831b9261088a565b1c9056fea2646970667358221220a12b94a02f9d5621f3851d7ba3361198c90539c37a2031672e27c29b213d711964736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#404)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> StorageTest:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#404)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#404)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#404)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[StorageTest]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#404)
        """
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, StorageTest, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[StorageTest]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#404)
        """
        return cls._deploy(request_type, [], return_tx, StorageTest, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class UnpackedStruct:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#386)

        Attributes:
            a (uint256): uint256
            b (uint256): uint256
        """
        original_name = 'UnpackedStruct'

        a: uint256
        b: uint256


    @overload
    def exists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#371)

        Returns:
            exists: uint256
        """
        ...

    @overload
    def exists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#371)

        Returns:
            exists: uint256
        """
        ...

    @overload
    def exists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#371)

        Returns:
            exists: uint256
        """
        ...

    @overload
    def exists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#371)

        Returns:
            exists: uint256
        """
        ...

    def exists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#371)

        Returns:
            exists: uint256
        """
        return self._execute(self.chain, request_type, "267c4ae4", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def map_addr(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#372)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def map_addr(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#372)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def map_addr(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#372)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def map_addr(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#372)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    def map_addr(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#372)

        Args:
            key0: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "a73e40cc", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def map_uint(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#373)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def map_uint(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#373)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def map_uint(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#373)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def map_uint(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#373)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    def map_uint(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#373)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "6a56c3d4", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def map_packed(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#374)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def map_packed(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#374)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def map_packed(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#374)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def map_packed(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#374)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    def map_packed(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#374)

        Args:
            key0: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "5c23fe9e", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def map_struct(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> StorageTest.UnpackedStruct:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#375)

        Args:
            key0: address
        Returns:
            struct StorageTest.UnpackedStruct
        """
        ...

    @overload
    def map_struct(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#375)

        Args:
            key0: address
        Returns:
            struct StorageTest.UnpackedStruct
        """
        ...

    @overload
    def map_struct(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#375)

        Args:
            key0: address
        Returns:
            struct StorageTest.UnpackedStruct
        """
        ...

    @overload
    def map_struct(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[StorageTest.UnpackedStruct]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#375)

        Args:
            key0: address
        Returns:
            struct StorageTest.UnpackedStruct
        """
        ...

    def map_struct(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[StorageTest.UnpackedStruct, TransactionAbc[StorageTest.UnpackedStruct], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#375)

        Args:
            key0: address
        Returns:
            struct StorageTest.UnpackedStruct
        """
        return self._execute(self.chain, request_type, "504429bf", [key0], True if request_type == "tx" else False, StorageTest.UnpackedStruct, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deep_map(self, key0: Union[Account, Address], key1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#376)

        Args:
            key0: address
            key1: address
        Returns:
            uint256
        """
        ...

    @overload
    def deep_map(self, key0: Union[Account, Address], key1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#376)

        Args:
            key0: address
            key1: address
        Returns:
            uint256
        """
        ...

    @overload
    def deep_map(self, key0: Union[Account, Address], key1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#376)

        Args:
            key0: address
            key1: address
        Returns:
            uint256
        """
        ...

    @overload
    def deep_map(self, key0: Union[Account, Address], key1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#376)

        Args:
            key0: address
            key1: address
        Returns:
            uint256
        """
        ...

    def deep_map(self, key0: Union[Account, Address], key1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#376)

        Args:
            key0: address
            key1: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "8cd8156d", [key0, key1], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deep_map_struct(self, key0: Union[Account, Address], key1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> StorageTest.UnpackedStruct:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#377)

        Args:
            key0: address
            key1: address
        Returns:
            struct StorageTest.UnpackedStruct
        """
        ...

    @overload
    def deep_map_struct(self, key0: Union[Account, Address], key1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#377)

        Args:
            key0: address
            key1: address
        Returns:
            struct StorageTest.UnpackedStruct
        """
        ...

    @overload
    def deep_map_struct(self, key0: Union[Account, Address], key1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#377)

        Args:
            key0: address
            key1: address
        Returns:
            struct StorageTest.UnpackedStruct
        """
        ...

    @overload
    def deep_map_struct(self, key0: Union[Account, Address], key1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[StorageTest.UnpackedStruct]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#377)

        Args:
            key0: address
            key1: address
        Returns:
            struct StorageTest.UnpackedStruct
        """
        ...

    def deep_map_struct(self, key0: Union[Account, Address], key1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[StorageTest.UnpackedStruct, TransactionAbc[StorageTest.UnpackedStruct], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#377)

        Args:
            key0: address
            key1: address
        Returns:
            struct StorageTest.UnpackedStruct
        """
        return self._execute(self.chain, request_type, "0310c060", [key0, key1], True if request_type == "tx" else False, StorageTest.UnpackedStruct, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def basic(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> StorageTest.UnpackedStruct:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#378)

        Returns:
            basic: struct StorageTest.UnpackedStruct
        """
        ...

    @overload
    def basic(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#378)

        Returns:
            basic: struct StorageTest.UnpackedStruct
        """
        ...

    @overload
    def basic(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#378)

        Returns:
            basic: struct StorageTest.UnpackedStruct
        """
        ...

    @overload
    def basic(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[StorageTest.UnpackedStruct]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#378)

        Returns:
            basic: struct StorageTest.UnpackedStruct
        """
        ...

    def basic(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[StorageTest.UnpackedStruct, TransactionAbc[StorageTest.UnpackedStruct], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#378)

        Returns:
            basic: struct StorageTest.UnpackedStruct
        """
        return self._execute(self.chain, request_type, "15e8b345", [], True if request_type == "tx" else False, StorageTest.UnpackedStruct, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint248:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#380)

        Returns:
            tA: uint248
        """
        ...

    @overload
    def tA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#380)

        Returns:
            tA: uint248
        """
        ...

    @overload
    def tA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#380)

        Returns:
            tA: uint248
        """
        ...

    @overload
    def tA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint248]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#380)

        Returns:
            tA: uint248
        """
        ...

    def tA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint248, TransactionAbc[uint248], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#380)

        Returns:
            tA: uint248
        """
        return self._execute(self.chain, request_type, "79da7e4d", [], True if request_type == "tx" else False, uint248, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#381)

        Returns:
            tB: bool
        """
        ...

    @overload
    def tB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#381)

        Returns:
            tB: bool
        """
        ...

    @overload
    def tB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#381)

        Returns:
            tB: bool
        """
        ...

    @overload
    def tB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#381)

        Returns:
            tB: bool
        """
        ...

    def tB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#381)

        Returns:
            tB: bool
        """
        return self._execute(self.chain, request_type, "57351c45", [], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#383)

        Returns:
            tC: bool
        """
        ...

    @overload
    def tC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#383)

        Returns:
            tC: bool
        """
        ...

    @overload
    def tC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#383)

        Returns:
            tC: bool
        """
        ...

    @overload
    def tC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#383)

        Returns:
            tC: bool
        """
        ...

    def tC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#383)

        Returns:
            tC: bool
        """
        return self._execute(self.chain, request_type, "eb53f990", [], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint248:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#384)

        Returns:
            tD: uint248
        """
        ...

    @overload
    def tD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#384)

        Returns:
            tD: uint248
        """
        ...

    @overload
    def tD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#384)

        Returns:
            tD: uint248
        """
        ...

    @overload
    def tD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint248]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#384)

        Returns:
            tD: uint248
        """
        ...

    def tD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint248, TransactionAbc[uint248], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#384)

        Returns:
            tD: uint248
        """
        return self._execute(self.chain, request_type, "e4c62a11", [], True if request_type == "tx" else False, uint248, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def map_bool(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#391)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def map_bool(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#391)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def map_bool(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#391)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def map_bool(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#391)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    def map_bool(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#391)

        Args:
            key0: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "8c6b4551", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#393)

        Returns:
            tE: bytes32
        """
        ...

    @overload
    def tE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#393)

        Returns:
            tE: bytes32
        """
        ...

    @overload
    def tE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#393)

        Returns:
            tE: bytes32
        """
        ...

    @overload
    def tE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#393)

        Returns:
            tE: bytes32
        """
        ...

    def tE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#393)

        Returns:
            tE: bytes32
        """
        return self._execute(self.chain, request_type, "b7e19e29", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tF(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#394)

        Returns:
            tF: address
        """
        ...

    @overload
    def tF(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#394)

        Returns:
            tF: address
        """
        ...

    @overload
    def tF(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#394)

        Returns:
            tF: address
        """
        ...

    @overload
    def tF(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#394)

        Returns:
            tF: address
        """
        ...

    def tF(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#394)

        Returns:
            tF: address
        """
        return self._execute(self.chain, request_type, "08f23aad", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tG(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#395)

        Returns:
            tG: int256
        """
        ...

    @overload
    def tG(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#395)

        Returns:
            tG: int256
        """
        ...

    @overload
    def tG(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#395)

        Returns:
            tG: int256
        """
        ...

    @overload
    def tG(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[int256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#395)

        Returns:
            tG: int256
        """
        ...

    def tG(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[int256, TransactionAbc[int256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#395)

        Returns:
            tG: int256
        """
        return self._execute(self.chain, request_type, "e5ed1efe", [], True if request_type == "tx" else False, int256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tH(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#396)

        Returns:
            tH: bool
        """
        ...

    @overload
    def tH(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#396)

        Returns:
            tH: bool
        """
        ...

    @overload
    def tH(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#396)

        Returns:
            tH: bool
        """
        ...

    @overload
    def tH(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#396)

        Returns:
            tH: bool
        """
        ...

    def tH(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#396)

        Returns:
            tH: bool
        """
        return self._execute(self.chain, request_type, "4f87aeb7", [], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def edgeCaseArray(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#402)

        Args:
            index0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def edgeCaseArray(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#402)

        Args:
            index0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def edgeCaseArray(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#402)

        Args:
            index0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def edgeCaseArray(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#402)

        Args:
            index0: uint256
        Returns:
            uint256
        """
        ...

    def edgeCaseArray(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#402)

        Args:
            index0: uint256
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "e92e9dc4", [index0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def read_struct_upper(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#412)

        Args:
            who: address
        Returns:
            uint256
        """
        ...

    @overload
    def read_struct_upper(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#412)

        Args:
            who: address
        Returns:
            uint256
        """
        ...

    @overload
    def read_struct_upper(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#412)

        Args:
            who: address
        Returns:
            uint256
        """
        ...

    @overload
    def read_struct_upper(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#412)

        Args:
            who: address
        Returns:
            uint256
        """
        ...

    def read_struct_upper(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#412)

        Args:
            who: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "3eae2218", [who], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def read_struct_lower(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#416)

        Args:
            who: address
        Returns:
            uint256
        """
        ...

    @overload
    def read_struct_lower(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#416)

        Args:
            who: address
        Returns:
            uint256
        """
        ...

    @overload
    def read_struct_lower(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#416)

        Args:
            who: address
        Returns:
            uint256
        """
        ...

    @overload
    def read_struct_lower(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#416)

        Args:
            who: address
        Returns:
            uint256
        """
        ...

    def read_struct_lower(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#416)

        Args:
            who: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "41b6edb2", [who], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def hidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#420)

        Returns:
            t: bytes32
        """
        ...

    @overload
    def hidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#420)

        Returns:
            t: bytes32
        """
        ...

    @overload
    def hidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#420)

        Returns:
            t: bytes32
        """
        ...

    @overload
    def hidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#420)

        Returns:
            t: bytes32
        """
        ...

    def hidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#420)

        Returns:
            t: bytes32
        """
        return self._execute(self.chain, request_type, "aef6d4b1", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def const(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#428)

        Returns:
            t: bytes32
        """
        ...

    @overload
    def const(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#428)

        Returns:
            t: bytes32
        """
        ...

    @overload
    def const(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#428)

        Returns:
            t: bytes32
        """
        ...

    @overload
    def const(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#428)

        Returns:
            t: bytes32
        """
        ...

    def const(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#428)

        Returns:
            t: bytes32
        """
        return self._execute(self.chain, request_type, "3b80a793", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def extra_sload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#432)

        Returns:
            t: bytes32
        """
        ...

    @overload
    def extra_sload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#432)

        Returns:
            t: bytes32
        """
        ...

    @overload
    def extra_sload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#432)

        Returns:
            t: bytes32
        """
        ...

    @overload
    def extra_sload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#432)

        Returns:
            t: bytes32
        """
        ...

    def extra_sload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#432)

        Returns:
            t: bytes32
        """
        return self._execute(self.chain, request_type, "9e7936e6", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setRandomPacking(self, val: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#440)

        Args:
            val: uint256
        """
        ...

    @overload
    def setRandomPacking(self, val: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#440)

        Args:
            val: uint256
        """
        ...

    @overload
    def setRandomPacking(self, val: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#440)

        Args:
            val: uint256
        """
        ...

    @overload
    def setRandomPacking(self, val: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#440)

        Args:
            val: uint256
        """
        ...

    def setRandomPacking(self, val: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#440)

        Args:
            val: uint256
        """
        return self._execute(self.chain, request_type, "aa463826", [val], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setRandomPacking_(self, val: uint256, size: uint256, offset: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#451)

        Args:
            val: uint256
            size: uint256
            offset: uint256
        """
        ...

    @overload
    def setRandomPacking_(self, val: uint256, size: uint256, offset: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#451)

        Args:
            val: uint256
            size: uint256
            offset: uint256
        """
        ...

    @overload
    def setRandomPacking_(self, val: uint256, size: uint256, offset: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#451)

        Args:
            val: uint256
            size: uint256
            offset: uint256
        """
        ...

    @overload
    def setRandomPacking_(self, val: uint256, size: uint256, offset: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#451)

        Args:
            val: uint256
            size: uint256
            offset: uint256
        """
        ...

    def setRandomPacking_(self, val: uint256, size: uint256, offset: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#451)

        Args:
            val: uint256
            size: uint256
            offset: uint256
        """
        return self._execute(self.chain, request_type, "1971f00b", [val, size, offset], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getRandomPacked(self, size: uint256, offset: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#460)

        Args:
            size: uint256
            offset: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def getRandomPacked(self, size: uint256, offset: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#460)

        Args:
            size: uint256
            offset: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def getRandomPacked(self, size: uint256, offset: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#460)

        Args:
            size: uint256
            offset: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def getRandomPacked(self, size: uint256, offset: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#460)

        Args:
            size: uint256
            offset: uint256
        Returns:
            uint256
        """
        ...

    def getRandomPacked(self, size: uint256, offset: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#460)

        Args:
            size: uint256
            offset: uint256
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "1aa844b4", [size, offset], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getRandomPacked_(self, shifts: uint8, shiftSizes: List[uint8], elem: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#467)

        Args:
            shifts: uint8
            shiftSizes: uint8[]
            elem: uint8
        Returns:
            uint256
        """
        ...

    @overload
    def getRandomPacked_(self, shifts: uint8, shiftSizes: List[uint8], elem: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#467)

        Args:
            shifts: uint8
            shiftSizes: uint8[]
            elem: uint8
        Returns:
            uint256
        """
        ...

    @overload
    def getRandomPacked_(self, shifts: uint8, shiftSizes: List[uint8], elem: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#467)

        Args:
            shifts: uint8
            shiftSizes: uint8[]
            elem: uint8
        Returns:
            uint256
        """
        ...

    @overload
    def getRandomPacked_(self, shifts: uint8, shiftSizes: List[uint8], elem: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#467)

        Args:
            shifts: uint8
            shiftSizes: uint8[]
            elem: uint8
        Returns:
            uint256
        """
        ...

    def getRandomPacked_(self, shifts: uint8, shiftSizes: List[uint8], elem: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdStorage.t.sol#467)

        Args:
            shifts: uint8
            shiftSizes: uint8[]
            elem: uint8
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "61a97569", [shifts, shiftSizes, elem], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

StorageTest.exists.selector = bytes4(b'&|J\xe4')
StorageTest.map_addr.selector = bytes4(b'\xa7>@\xcc')
StorageTest.map_uint.selector = bytes4(b'jV\xc3\xd4')
StorageTest.map_packed.selector = bytes4(b'\\#\xfe\x9e')
StorageTest.map_struct.selector = bytes4(b'PD)\xbf')
StorageTest.deep_map.selector = bytes4(b'\x8c\xd8\x15m')
StorageTest.deep_map_struct.selector = bytes4(b'\x03\x10\xc0`')
StorageTest.basic.selector = bytes4(b'\x15\xe8\xb3E')
StorageTest.tA.selector = bytes4(b'y\xda~M')
StorageTest.tB.selector = bytes4(b'W5\x1cE')
StorageTest.tC.selector = bytes4(b'\xebS\xf9\x90')
StorageTest.tD.selector = bytes4(b'\xe4\xc6*\x11')
StorageTest.map_bool.selector = bytes4(b'\x8ckEQ')
StorageTest.tE.selector = bytes4(b'\xb7\xe1\x9e)')
StorageTest.tF.selector = bytes4(b'\x08\xf2:\xad')
StorageTest.tG.selector = bytes4(b'\xe5\xed\x1e\xfe')
StorageTest.tH.selector = bytes4(b'O\x87\xae\xb7')
StorageTest.edgeCaseArray.selector = bytes4(b'\xe9.\x9d\xc4')
StorageTest.read_struct_upper.selector = bytes4(b'>\xae"\x18')
StorageTest.read_struct_lower.selector = bytes4(b'A\xb6\xed\xb2')
StorageTest.hidden.selector = bytes4(b'\xae\xf6\xd4\xb1')
StorageTest.const.selector = bytes4(b';\x80\xa7\x93')
StorageTest.extra_sload.selector = bytes4(b'\x9ey6\xe6')
StorageTest.setRandomPacking.selector = bytes4(b'\xaaF8&')
StorageTest.setRandomPacking_.selector = bytes4(b'\x19q\xf0\x0b')
StorageTest.getRandomPacked.selector = bytes4(b'\x1a\xa8D\xb4')
StorageTest.getRandomPacked_.selector = bytes4(b'a\xa9ui')
