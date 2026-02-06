
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.lib.forgestd.src.Test import Test



class StdStorageTest(Test):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#7)
    """
    _abi = {b'\x9c\x95U\xb1\xe3\x10.<\xf4\x8fB}y\xcbg\x8f]\x9b\xd1\xed\n\xd5t8\x94a\xe2U\xf9Qp\xed': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'who', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes4', 'name': 'fsig', 'type': 'bytes4'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'keysHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'slot', 'type': 'uint256'}], 'name': 'SlotFound', 'type': 'event'}, b'\x08\x0f\xc4\xa9f \xc4F.p[#\xf3FA?\xe3yk\xb6<o\x8d\x85\x91\xba\xec\x0e#\x15w\xa5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'who', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'slot', 'type': 'uint256'}], 'name': 'WARNING_UninitedSlot', 'type': 'event'}, b'A0O\xac\xd92=u\xb1\x1b\xcd\xd6\t\xcb8\xef\xff\xfd\xb0W\x10\xf7\xca\xf0\xe9\xb1lm\x9dp\x9fP': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log', 'type': 'event'}, b'z\xe7LRt\x14\xae\x13_\xd9pG\xb1)!\xa5\xec9\x11\xb8\x04\x19xU\xd6~%\xc7\xb7^\xe6\xf3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'log_address', 'type': 'event'}, b'\xfb\x10(e\xd5\n\xdd\xdd\xf6\x9d\xa9\xb5\xaa\x1b\xce\xd6l\x80\xcf\x86\x9a\\\x8d\x04q\xa4g\xe1\x8c\xe9\xca\xb1': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_array', 'type': 'event'}, b'\x89\n\x82g\x9bG\x0f+\xd8(\x16\xed\x9b\x16\x1f\x97\xd8\xb9g\xf3\x7f\xa3d|!\xd5\xbf9t\x9e-\xd5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_array', 'type': 'event'}, b'@\xe1\x84\x0fWi\x07=a\xbd\x017-\x9bu\xba\xa9\x84-V)\xa0\xc9\x9f\xf1\x03\xbe\x11x\xa8\xe9\xe2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_array', 'type': 'event'}, b'#\xb6*\xd0XM$\xa7_\x0b\xf3V\x03\x91\xefVY\xecm\xb1&\x9cV\xe1\x1a\xa2A\xd67\xf1\x9b ': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'log_bytes', 'type': 'event'}, b'\xe8\x16\x99\xb8Q\x13\xee\xa1\xc7>\x10X\x8b+\x03^U\x893ic!s\xaf\xd4?\xeb\x19/\xacd\xe3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'log_bytes32', 'type': 'event'}, b'\x0e\xb5\xd5&$\xc8\xd2\x8a\xda\x9f\xc5Z\x8cP.\xd5\xaa?\xbe/\xb6\xe9\x1bq\xb5\xf3v\x88+\x1d/\xb8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256', 'name': '', 'type': 'int256'}], 'name': 'log_int', 'type': 'event'}, b'\x9cN\x85A\xca\x8f\r\xc1\xc4\x13\xf9\x10\x8ff\xd8-<\xec\xb1\xbd\xdb\xceCza\xca\xa3\x17\\L\xc9o': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address', 'name': 'val', 'type': 'address'}], 'name': 'log_named_address', 'type': 'event'}, b'\x00\xaa\xa3\x9c\x9f\xfb_VzE48\x0cspup.\x1f\x7f\x14\x10\x7f\xc9S(\xe3\xb5l\x03%\xfb': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xa7>\xda\tf/F\xdd\xe7)\xbeF\x118_\xf3O\xe6\xc4O\xbb\xc6\xf7\xe1{\x04+Y\xa3D[W': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_named_array', 'type': 'event'}, b";\xcf\xb2\xae.\x8d\x13-\xd1\xfc\xe7\xcf'\x8a\x9a\x19uj\x9f\xce\xab\xe4p\xdf;\xda\xbbK\xc5w\xd1\xbd": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xd2n\x16\xca\xd4T\x87\x05\xe4\xc9\xe2\xd9O\x98\xee\x91\xc2\x89\x08^\xe4%YO\xd5c_\xa2\x96L\xcf\x18': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'val', 'type': 'bytes'}], 'name': 'log_named_bytes', 'type': 'event'}, b'\xaf\xb7\x95\xc9\xc6\x1eO\xe7F\x8c8o\x92]zT)\xec\xad\x9c\x04\x95\xdd\xb8\xd3\x8di\x06\x14\xd3/\x99': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'val', 'type': 'bytes32'}], 'name': 'log_named_bytes32', 'type': 'event'}, b']\xa6\xce\x9dQ\x15\x1b\xa1\x0c\t\xa5Y\xef$\xd5 \xb9\xda\xc5\xc5\xb8\x81\n\xe8CNM\r\x86A\x1a\x95': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_int', 'type': 'event'}, b"\xeb\x8b\xa4<\xedu7B\x19F\xbdC\xe8(\xb8\xb2\xb8B\x89'\xaa\x8f\x80\x1c\x13\xd94\xbf\x11\xac\xa5{": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_uint', 'type': 'event'}, b'/\xe62w\x91t7CxD*\x8e\x97\x8b\xcc\xfb\xdc\xc1\xd6\xb2\xb0\xd8\x1f~\x8e\xb7v\xab"\x86\xf1h': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}], 'name': 'log_named_int', 'type': 'event'}, b'(\x0fDF\xb2\x8a\x13rA}\xdae\x8d0\xb9[)\x92\xb1*\xc9\xc7\xf3xS_)\xa9z\xcf5\x83': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'val', 'type': 'string'}], 'name': 'log_named_string', 'type': 'event'}, b'\xb2\xde/\xbe\x80\x1a\r\xf6\xc0\xcb\xdd\xfdD\x8b\xa3\xc4\x1dH\xa0@\xca5\xc5l\x81\x96\xef\x0f\xca\xe7!\xa8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}], 'name': 'log_named_uint', 'type': 'event'}, b'\x0b.\x13\xff \xac{GA\x98eU\x83\xed\xf7\r\xed\xd2\xc1\xdc\x98\x0e2\x9cO\xbb/\xc0t\x8byk': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log_string', 'type': 'event'}, b',\xab\x97\x90Q\x0f\xd8\xbd\xfb\xd2\x11R\x88\xdb3\xfe\xc6f\x91\xd4v\xef\xc5B|\xfdL\ti0\x17U': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'log_uint', 'type': 'event'}, b"\xe7\x95\x0e\xde\x03\x94\xb9\xf2\xceJZ\x1b\xf5\xa7\xe1\x85$\x11\xf7\xe6f\x1bC\x08\xc9\x13\xc4\xbf\xd1\x10'\xe4": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'logs', 'type': 'event'}, b'\xfav&\xd4': {'inputs': [], 'name': 'IS_TEST', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb5P\x8a\xa9': {'inputs': [], 'name': 'excludeArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'excludedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe2\x0c\x9fq': {'inputs': [], 'name': 'excludeContracts', 'outputs': [{'internalType': 'address[]', 'name': 'excludedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb0FO\xdc': {'inputs': [], 'name': 'excludeSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'excludedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1e\xd7\x83\x1c': {'inputs': [], 'name': 'excludeSenders', 'outputs': [{'internalType': 'address[]', 'name': 'excludedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbaAO\xa6': {'inputs': [], 'name': 'failed', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'R\xe5*\xc6': {'inputs': [], 'name': 'readNonBoolValue', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\n\x92T\xe4': {'inputs': [], 'name': 'setUp', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'f\xd9\xa9\xa0': {'inputs': [], 'name': 'targetArtifactSelectors', 'outputs': [{'components': [{'internalType': 'string', 'name': 'artifact', 'type': 'string'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzArtifactSelector[]', 'name': 'targetedArtifactSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x85"l\x81': {'inputs': [], 'name': 'targetArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'targetedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'?r\x86\xf4': {'inputs': [], 'name': 'targetContracts', 'outputs': [{'internalType': 'address[]', 'name': 'targetedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'*\xde8\x80': {'inputs': [], 'name': 'targetInterfaces', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'string[]', 'name': 'artifacts', 'type': 'string[]'}], 'internalType': 'struct StdInvariant.FuzzInterface[]', 'name': 'targetedInterfaces_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x91j\x17\xc6': {'inputs': [], 'name': 'targetSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'targetedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'>^<#': {'inputs': [], 'name': 'targetSenders', 'outputs': [{'internalType': 'address[]', 'name': 'targetedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd9Rf\xeb': {'inputs': [], 'name': 'testEdgeCaseArray', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Y\x93w\xdd': {'inputs': [{'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'elemToGet', 'type': 'uint8'}], 'name': 'testFuzz_Packed', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'l\xc4\x87\x82': {'inputs': [{'internalType': 'uint256', 'name': 'nvars', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'seed', 'type': 'uint256'}], 'name': 'testFuzz_Packed2', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'/dN\x92': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'uint128', 'name': 'value', 'type': 'uint128'}], 'name': 'testFuzz_StorageCheckedWriteMapPacked', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'e\xbe\xe9I': {'inputs': [{'internalType': 'uint248', 'name': 'val1', 'type': 'uint248'}, {'internalType': 'uint248', 'name': 'val2', 'type': 'uint248'}, {'internalType': 'bool', 'name': 'boolVal1', 'type': 'bool'}, {'internalType': 'bool', 'name': 'boolVal2', 'type': 'bool'}], 'name': 'testFuzz_StorageNativePack', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xed`R\x9b': {'inputs': [], 'name': 'test_RevertIf_ReadingNonBoolValue', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b"\xeb\xef\xd7'": {'inputs': [], 'name': 'test_RevertStorageConst', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa2\x99\xaa^': {'inputs': [], 'name': 'test_StorageCheckedWriteDeepMap', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b';a\xa9P': {'inputs': [], 'name': 'test_StorageCheckedWriteDeepMapStructA', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb4t{ ': {'inputs': [], 'name': 'test_StorageCheckedWriteDeepMapStructB', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xe1fM\x98': {'inputs': [], 'name': 'test_StorageCheckedWriteHidden', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'mB+\xe6': {'inputs': [], 'name': 'test_StorageCheckedWriteMapAddr', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'M\xefd\xda': {'inputs': [], 'name': 'test_StorageCheckedWriteMapBool', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x05\xa7\xc0\xb4': {'inputs': [], 'name': 'test_StorageCheckedWriteMapPackedFullSuccess', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'I_\x07A': {'inputs': [], 'name': 'test_StorageCheckedWriteMapStructA', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'&\xd9}\x0b': {'inputs': [], 'name': 'test_StorageCheckedWriteMapStructB', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf2\xda\x110': {'inputs': [], 'name': 'test_StorageCheckedWriteMapUint', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xe8{\xfd\x9d': {'inputs': [], 'name': 'test_StorageCheckedWriteObvious', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x87\\\xeb\x10': {'inputs': [], 'name': 'test_StorageCheckedWriteSignedIntegerHidden', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Y\xfa\xf38': {'inputs': [], 'name': 'test_StorageCheckedWriteSignedIntegerObvious', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'm\xc32Q': {'inputs': [], 'name': 'test_StorageCheckedWriteStructA', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x89\xe6\xcf\xe4': {'inputs': [], 'name': 'test_StorageCheckedWriteStructB', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x84\x99\xd1\xab': {'inputs': [], 'name': 'test_StorageDeepMap', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'9.f\n': {'inputs': [], 'name': 'test_StorageDeepMapStructA', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xab\x86\x1d$': {'inputs': [], 'name': 'test_StorageDeepMapStructB', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xc7\x98\x03\xc3': {'inputs': [], 'name': 'test_StorageExtraSload', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b"\x96+'\xba": {'inputs': [], 'name': 'test_StorageHidden', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'lB\x8e\xf8': {'inputs': [], 'name': 'test_StorageMapAddrFound', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x03\x8c\xd1\x92': {'inputs': [], 'name': 'test_StorageMapAddrRoot', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'q\xe0\xa2T': {'inputs': [], 'name': 'test_StorageMapStructA', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xe9\x94\xe0\xb5': {'inputs': [], 'name': 'test_StorageMapStructB', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd8\xc1r\xbf': {'inputs': [], 'name': 'test_StorageMapUintFound', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'j\xf4\xe7\xbe': {'inputs': [], 'name': 'test_StorageObvious', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xe1\xb9C\xa2': {'inputs': [], 'name': 'test_StorageReadAddress', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xed\xf3\xc6\x9a': {'inputs': [], 'name': 'test_StorageReadBool_False', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd8\xe2LC': {'inputs': [], 'name': 'test_StorageReadBool_True', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'7\x9aB\xae': {'inputs': [], 'name': 'test_StorageReadBytes32', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x97\x92Fk': {'inputs': [], 'name': 'test_StorageReadInt', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf1]So': {'inputs': [], 'name': 'test_StorageReadUint', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf7:\xa1\x9a': {'inputs': [], 'name': 'test_StorageStructA', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'J\xca\xea\x91': {'inputs': [], 'name': 'test_StorageStructB', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":61,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"stdstore","offset":0,"slot":0,"type":"t_struct(StdStorage)8017_storage"},{"astId":218,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_failed","offset":0,"slot":8,"type":"t_bool"},{"astId":2719,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"stdChainsInitialized","offset":1,"slot":8,"type":"t_bool"},{"astId":2740,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"chains","offset":0,"slot":9,"type":"t_mapping(t_string_memory_ptr,t_struct(Chain)2735_storage)"},{"astId":2744,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"defaultRpcUrls","offset":0,"slot":10,"type":"t_mapping(t_string_memory_ptr,t_string_storage)"},{"astId":2748,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"idToAlias","offset":0,"slot":11,"type":"t_mapping(t_uint256,t_string_storage)"},{"astId":2751,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"fallbackToDefaultRpcUrls","offset":0,"slot":12,"type":"t_bool"},{"astId":3680,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"gasMeteringOff","offset":1,"slot":12,"type":"t_bool"},{"astId":5747,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"stdstore","offset":0,"slot":13,"type":"t_struct(StdStorage)8017_storage"},{"astId":6623,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_excludedContracts","offset":0,"slot":21,"type":"t_array(t_address)dyn_storage"},{"astId":6626,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_excludedSenders","offset":0,"slot":22,"type":"t_array(t_address)dyn_storage"},{"astId":6629,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_targetedContracts","offset":0,"slot":23,"type":"t_array(t_address)dyn_storage"},{"astId":6632,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_targetedSenders","offset":0,"slot":24,"type":"t_array(t_address)dyn_storage"},{"astId":6635,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_excludedArtifacts","offset":0,"slot":25,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6638,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_targetedArtifacts","offset":0,"slot":26,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6642,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_targetedArtifactSelectors","offset":0,"slot":27,"type":"t_array(t_struct(FuzzArtifactSelector)6614_storage)dyn_storage"},{"astId":6646,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_excludedSelectors","offset":0,"slot":28,"type":"t_array(t_struct(FuzzSelector)6608_storage)dyn_storage"},{"astId":6650,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_targetedSelectors","offset":0,"slot":29,"type":"t_array(t_struct(FuzzSelector)6608_storage)dyn_storage"},{"astId":6654,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_targetedInterfaces","offset":0,"slot":30,"type":"t_array(t_struct(FuzzInterface)6620_storage)dyn_storage"},{"astId":12907,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"IS_TEST","offset":0,"slot":31,"type":"t_bool"},{"astId":39062,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"test","offset":1,"slot":31,"type":"t_contract(StorageTest)41624"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_address)dyn_storage":{"encoding":"dynamic_array","label":"address[]","numberOfBytes":32,"base":"t_address"},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_array(t_bytes4)dyn_storage":{"encoding":"dynamic_array","label":"bytes4[]","numberOfBytes":32,"base":"t_bytes4"},"t_array(t_string_storage)dyn_storage":{"encoding":"dynamic_array","label":"string[]","numberOfBytes":32,"base":"t_string_storage"},"t_array(t_struct(FuzzArtifactSelector)6614_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzArtifactSelector[]","numberOfBytes":32,"base":"t_struct(FuzzArtifactSelector)6614_storage"},"t_array(t_struct(FuzzInterface)6620_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzInterface[]","numberOfBytes":32,"base":"t_struct(FuzzInterface)6620_storage"},"t_array(t_struct(FuzzSelector)6608_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzSelector[]","numberOfBytes":32,"base":"t_struct(FuzzSelector)6608_storage"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_contract(StorageTest)41624":{"encoding":"inplace","label":"contract StorageTest","numberOfBytes":20},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage))"},"t_mapping(t_bytes32,t_struct(FindData)7992_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)7992_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)7992_storage)"},"t_mapping(t_string_memory_ptr,t_string_storage)":{"encoding":"mapping","label":"mapping(string => string)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_string_storage"},"t_mapping(t_string_memory_ptr,t_struct(Chain)2735_storage)":{"encoding":"mapping","label":"mapping(string => struct StdChains.Chain)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_struct(Chain)2735_storage"},"t_mapping(t_uint256,t_string_storage)":{"encoding":"mapping","label":"mapping(uint256 => string)","numberOfBytes":32,"key":"t_uint256","value":"t_string_storage"},"t_string_memory_ptr":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(Chain)2735_storage":{"encoding":"inplace","label":"struct StdChains.Chain","numberOfBytes":128,"members":[{"astId":2728,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"name","offset":0,"slot":0,"type":"t_string_storage"},{"astId":2730,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"chainId","offset":0,"slot":1,"type":"t_uint256"},{"astId":2732,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"chainAlias","offset":0,"slot":2,"type":"t_string_storage"},{"astId":2734,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"rpcUrl","offset":0,"slot":3,"type":"t_string_storage"}]},"t_struct(FindData)7992_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":7985,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":7987,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":7989,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":7991,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(FuzzArtifactSelector)6614_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzArtifactSelector","numberOfBytes":64,"members":[{"astId":6610,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"artifact","offset":0,"slot":0,"type":"t_string_storage"},{"astId":6613,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(FuzzInterface)6620_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzInterface","numberOfBytes":64,"members":[{"astId":6616,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6619,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"artifacts","offset":0,"slot":1,"type":"t_array(t_string_storage)dyn_storage"}]},"t_struct(FuzzSelector)6608_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzSelector","numberOfBytes":64,"members":[{"astId":6604,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6607,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(StdStorage)8017_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":8001,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage)))"},{"astId":8004,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":8006,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":8008,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":8010,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":8012,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":8014,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":8016,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StdStorageTest","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60808060405234602f57600160ff19600c541617600c55600160ff19601f541617601f556187ea90816100348239f35b5f80fdfe60806040526004361015610011575f80fd5b5f5f3560e01c8063038cd1921461347957806305a7c0b41461328e5780630a9254e4146132275780631ed7831c146131a957806326d97d0b146130db5780632ade388014612f1c5780632f644e9214612d48578063379a42ae14612c78578063392e660a14612bc45780633b61a95014612ae35780633e5e3c2314612a655780633f7286f4146129e7578063495f0741146129155780634acaea911461286c5780634def64da1461274d57806352e52ac6146126f7578063599377dd146122cd57806359faf3381461223c57806365bee94914611ef357806366d9a9a014611dca5780636af4e7be14611d4f5780636c428ef814611ccf5780636cc48782146118865780636d422be6146117e65780636dc332511461172357806371e0a2541461169f5780638499d1ab146115fd57806385226c8114611569578063875ceb10146114a357806389e6cfe4146113df578063916a17c614611337578063962b27ba146112545780639792466b14611197578063a299aa5e146110e7578063ab861d241461101d578063b0464fdc14610f75578063b4747b2014610e83578063b5508aa914610de8578063ba414fa614610dc3578063c79803c314610d1f578063d8c172bf14610c97578063d8e24c4314610bf2578063d95266eb14610aa5578063e1664d9814610a14578063e1b943a214610949578063e20c9f71146108bb578063e87bfd9d146107f5578063e994e0b514610747578063ebefd72714610629578063ed60529b14610555578063edf3c69a146104b0578063f15d536f14610440578063f2da113014610360578063f73aa19a1461029c5763fa7626d414610277575f80fd5b34610299578060031936011261029957602060ff601f54166040519015158152f35b80fd5b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff19166315e8b345179055806003556102f2615563565b545f5160206187555f395f51905f523b1561035c576040519063260a5b1560e21b82526007600483015260248201525f816044815f5160206187555f395f51905f525afa801561035157610344575080f35b5f61034e91613a64565b80f35b6040513d5f823e3d90fd5b5f80fd5b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916636a56c3d41790556103b2614415565b6103ba6148e7565b601f54604051631a95b0f560e21b815260646004820152906020908290602490829060081c6001600160a01b03165afa8015610435578290610401575b61034e91506140eb565b506020813d60201161042d575b8161041b60209383613a64565b8101031261035c5761034e90516103f7565b3d915061040e565b6040513d84823e3d90fd5b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663267c4ae41790556104926167b2565b6020815191818082019384920101031261035c5761034e90516141db565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff19166357351c451790556105026152e2565b5f5160206187555f395f51905f523b1561035c5760405163f7fe347760e01b815290151560048201525f60248201819052816044815f5160206187555f395f51905f525afa801561035157610344575080f35b50346102995780600319360112610299575f5160206187555f395f51905f523b156102995760405163f28dceb360e01b815260206004820152605260248201526105a160448201613f8c565b81808260a481835f5160206187555f395f51905f525af1801561060557610612575b5050303b1561029957604051632972956360e11b815281808260048183305af18015610605576105f05780f35b6105f991613a64565b805f12610299575f8180f35b50604051903d90823e3d90fd5b61061b91613a64565b805f12610299575f816105c3565b5034610299578060031936011261029957601f54604051611093808201939260081c6001600160a01b0316906001600160401b0385118386101761073357839460209284926176a28439815203019082f08015610605575f5160206187555f395f51905f523b1561070e5760405163f28dceb360e01b8152602060048201528281806106b760248201613f35565b0381835f5160206187555f395f51905f525af18015610728578390610711575b50506001600160a01b0316803b1561070e5781809160046040518095819363fc5aec2b60e01b83525af18015610605576105f05780f35b50fd5b61071a91613a64565b815f1261070e575f826106d7565b6040513d85823e3d90fd5b634e487b7160e01b84526041600452602484fd5b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663504429bf17905561079a306143e1565b60016003556107a7615563565b54604051602081019030825260046040820152604081526107c9606082613a64565b519020600181018091116107e1579061034e9161422b565b634e487b7160e01b83526011600452602483fd5b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663267c4ae41790556108476148e7565b601f5460405163099f12b960e21b8152906020908290600490829060081c6001600160a01b03165afa8015610435578290610887575b61034e915061409b565b506020813d6020116108b3575b816108a160209383613a64565b8101031261035c5761034e905161087d565b3d9150610894565b503461029957806003193601126102995760405160158054808352908352909160208301917f55f448fdea98c4d29eb340757ef0a66cd03dbb9538908a6a81d96026b71ec475915b81811061092a576109268561091a81870382613a64565b604051918291826138b5565b0390f35b82546001600160a01b0316845260209093019260019283019201610903565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff19166308f23aad17905561099b6167b2565b602081805181010312610a1057602001516001600160a01b03811690819003610a10575f5160206187555f395f51905f523b1561035c57604051906328a9b0fb60e11b8252600482015261053960248201525f816044815f5160206187555f395f51905f525afa801561035157610344575080f35b5080fd5b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663aef6d4b1179055610a666148e7565b601f5460405163aef6d4b160e01b8152906020908290600490829060081c6001600160a01b03165afa80156104355782906108875761034e915061409b565b503461029957806003193601126102995760018060a01b03601f5460081c1660018060a01b03196004541617600455610b1d6020604051610ae7604082613a64565b6016815275656467654361736541727261792875696e743235362960501b9101526002805463ffffffff191663e92e9dc4179055565b600154600160401b811015610bde576001810180600155811015610bca575f9060018252602082200155610b4f614c3b565b601f54604051633a4ba77160e21b815260048101839052906020908290602490829060081c6001600160a01b03165afa8015610435578290610b96575b61034e91506141db565b506020813d602011610bc2575b81610bb060209383613a64565b8101031261035c5761034e9051610b8c565b3d9150610ba3565b634e487b7160e01b5f52603260045260245ffd5b634e487b7160e01b5f52604160045260245ffd5b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916634f87aeb7179055610c446152e2565b5f5160206187555f395f51905f523b1561035c5760405163f7fe347760e01b81529015156004820152600160248201525f816044815f5160206187555f395f51905f525afa801561035157610344575080f35b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916636a56c3d4179055610ce9614415565b61034e610cf4615563565b546040516020810190606482526002604082015260408152610d17606082613a64565b51902061422b565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916639e7936e6179055610d71615563565b545f5160206187555f395f51905f523b1561035c576040519063260a5b1560e21b82526010600483015260248201525f816044815f5160206187555f395f51905f525afa801561035157610344575080f35b50346102995780600319360112610299576020610dde613e9a565b6040519015158152f35b5034610299578060031936011261029957601954610e0581613a9b565b90610e136040519283613a64565b80825260195f9081527f944998273e477b495144fb8794c914197f3ccb46be2900f4698fd0ef743c9695602084015b838310610e5757604051806109268782613958565b600160208192604051610e7581610e6e8189613aea565b0382613a64565b815201920192019190610e42565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916630310c060179055610ed6306143e1565b610edf306143e1565b6001600355610eec6148e7565b601f54604080516218860360e51b815291829060081c6001600160a01b03168180610f1b308060048401613ba7565b03915afa80156104355761034e9183908492610f41575b50610f3c9061413b565b6140eb565b610f3c9250610f68915060403d604011610f6e575b610f608183613a64565b810190613a85565b91610f32565b503d610f56565b5034610299578060031936011261029957601c54610f9281613a9b565b91610fa06040519384613a64565b818352601c81527f0e4562a10381dec21b205ed72637e6b1b523bdd0e4d4d50af5cd23dd4500a211602084015b838310610fe2576040518061092687826139b7565b60026020600192604051610ff581613a2e565b848060a01b03865416815261100b858701613c5b565b83820152815201920192019190610fcd565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916630310c060179055611070306143e1565b611079306143e1565b6001600355611086615563565b54604051602081019030825260066040820152604081526110a8606082613a64565b5190206040516110cf816110c160208201943086613b6b565b03601f198101835282613a64565b519020600181018091116107e1579061034e9161427a565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916638cd8156d17905561113a306143e1565b611143306143e1565b61114b6148e7565b601f54604051638cd8156d60e01b815290602090829060081c6001600160a01b0316818061117d308060048401613ba7565b03915afa80156104355782906104015761034e91506140eb565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663e5ed1efe1790556111e96167b2565b6020815191818082019384920101031261035c57515f5160206187555f395f51905f523b1561035c5760405163fe74f05b60e01b81526004810191909152600160ff1b60248201525f816044815f5160206187555f395f51905f525afa801561035157610344575080f35b503461029957806003193601126102995760018060a01b03601f5460081c1660018060a01b031960045416176004556112be6020604051611296604082613a64565b600881526768696464656e282960c01b9101526002805463ffffffff191663aef6d4b1179055565b6112c6615563565b545f5160206187555f395f51905f523b1561035c576040519063260a5b1560e21b82527fb27fb258786eae8f9ffde06a5bfd55f5193cb73bd64e533d5d75fd7cb46652ff600483015260248201525f816044815f5160206187555f395f51905f525afa801561035157610344575080f35b5034610299578060031936011261029957601d5461135481613a9b565b916113626040519384613a64565b818352601d81527f6d4407e7be21f808e6509aa9fa9143369579dd7d760fe20a2c09680fc146134f602084015b8383106113a4576040518061092687826139b7565b600260206001926040516113b781613a2e565b848060a01b0386541681526113cd858701613c5b565b8382015281520192019201919061138f565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff19166315e8b34517905560016003556114366148e7565b601f54604080516315e8b34560e01b8152918290600490829060081c6001600160a01b03165afa80156104355761034e918390849261147f575b5061147a9061418a565b61409b565b61147a925061149d915060403d604011610f6e57610f608183613a64565b91611470565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663aef6d4b11790556114f5614f8e565b601f5460405163aef6d4b160e01b8152906020908290600490829060081c6001600160a01b03165afa8015610435578290611535575b61034e915061433b565b506020813d602011611561575b8161154f60209383613a64565b8101031261035c5761034e905161152b565b3d9150611542565b5034610299578060031936011261029957601a5461158681613a9b565b906115946040519283613a64565b808252601a5f9081527f057c384a7d1c54f3a1b2e5e67b2617b8224fdfd1ea7234eea573a6ff665ff63e602084015b8383106115d857604051806109268782613958565b6001602081926040516115ef81610e6e8189613aea565b8152019201920191906115c3565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916638cd8156d179055611650306143e1565b611659306143e1565b61034e611664615563565b5460405160208101903082526005604082015260408152611686606082613a64565b519020604051610d17816110c160208201943086613b6b565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663504429bf1790556116f2306143e1565b8060035561034e611701615563565b5460405160208101903082526004604082015260408152610d17606082613a64565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff19166315e8b345179055806003556117796148e7565b601f54604080516315e8b34560e01b8152918290600490829060081c6001600160a01b03165afa80156104355761034e91839084926117c2575b506117bd9061409b565b61418a565b6117bd92506117e0915060403d604011610f6e57610f608183613a64565b916117b3565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663a73e40cc179055611839306143e1565b6118416148e7565b601f546040516329cf903360e21b8152306004820152906020908290602490829060081c6001600160a01b03165afa80156104355782906104015761034e91506140eb565b5034610299576040366003190112610299576024356118aa60146001600435615360565b60405f8082516118ba8482613a64565b600c81526b109bdd5b99081c995cdd5b1d60a21b6020820152835161190f816118fb6020820194632d839cb360e21b865288602484015260648301906138f7565b88604483015203601f198101835282613a64565b51906a636f6e736f6c652e6c6f675afa506101009261192d83613bdb565b9361193784613bdb565b9061194185613bdb565b9287915b868310611b2e57505050855b848110611ac55750855b848110611966578680f35b6006805460ff19166001179055601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556119c86119a4613e5f565b63ffffffff60e01b90602081519101201660e01c63ffffffff196002541617600255565b6119db6119d58284613c0d565b516143e1565b6119e86119d58285613c0d565b6119f06167b2565b6020815191818082019384920101031261035c5751601f5490919060081c6001600160a01b03166020611a238386613c0d565b516044611a308589613c0d565b5191895194859384926306aa112d60e21b8452600484015260248301525afa908115611abb578991611a89575b50611a8390611a79600194611a72858c613c0d565b519061422b565b611a72838a613c0d565b0161195b565b90506020813d8211611ab3575b81611aa360209383613a64565b8101031261035c57516001611a5d565b3d9150611a96565b86513d8b823e3d90fd5b6001908160ff196006541617600655818060a01b03601f5460081c16828060a01b03196004541617600455611afb6119a4613e5f565b611b086119d58285613c0d565b611b156119d58286613c0d565b611b28611b228289613c0d565b516144a4565b01611951565b82611c9f57885b611b3f8487613c0d565b52611b53611b4d8489613bce565b82613bce565b60018101809111611c8b576101008401808511611c775791611b9a611c2c92600180958b5160208101918983528d8201528c8152611b92606082613a64565b519020615360565b5f808a611beb611bff8251611baf8482613a64565b600c81526b109bdd5b99081c995cdd5b1d60a21b602082015283519283916020830195632d839cb360e21b8752602484015260648301906138f7565b87604483015203601f198101835282613a64565b51906a636f6e736f6c652e6c6f675afa50611c1a8688613c0d565b52611c258587613c0d565b5190613bce565b92611c655f1983611c3d8489613c0d565b511b0188516020810190868252848b8201528a8152611c5d606082613a64565b5190206142c9565b611c6f828b613c0d565b520191611945565b634e487b7160e01b8b52601160045260248bfd5b634e487b7160e01b8a52601160045260248afd5b5f198301838111611c8b5780611cc3611cbb611cca9389613c0d565b519187613c0d565b5190613b86565b611b35565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663a73e40cc179055611d22306143e1565b61034e611d2d615563565b5460405160208101903082526001604082015260408152610d17606082613a64565b503461029957806003193601126102995760018060a01b03601f5460081c1660018060a01b03196004541617600455611db96020604051611d91604082613a64565b6008815267657869737473282960c01b9101526002805463ffffffff191663267c4ae4179055565b61034e611dc4615563565b5461413b565b5034610299578060031936011261029957601b54611de781613a9b565b611df46040519182613a64565b818152601b83526020810191837f3ad8aa4f87544323a9d1e5dd902f40c356527a7955687113db5f9a85ad579dc1845b838310611eb057868587604051928392602084019060208552518091526040840160408260051b8601019392905b828210611e6157505050500390f35b91936001919395506020611ea08192603f198a820301865288519083611e9083516040845260408401906138f7565b920151908481840391015261391b565b9601920192018594939192611e52565b60026020600192604051611ec381613a2e565b604051611ed481610e6e818a613aea565b8152611ee1858701613c5b565b83820152815201920192019190611e24565b5034610299576080366003190112610299576004356001600160f81b0381169081900361035c576024356001600160f81b0381169081900361035c57604435801515810361035c5760643590811515820361035c576006805460ff19166001179055601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff19166379da7e4d179055611f97846144a4565b6006805460ff19166001179055601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff19166357351c45179055611fe6816144a4565b6006805460ff19166001179055601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663eb53f990179055612035826144a4565b6006805460ff19166001179055601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663e4c62a11179055612084836144a4565b601f546040516379da7e4d60e01b815260089190911c6001600160a01b031694602082600481895afa8015612231576120cd928891612162575b506001600160f81b031661422b565b6040516357351c4560e01b815290602082600481885afa80156122265786906121e7575b6120fb925061438e565b604051630eb53f9960e41b8152602081600481875afa9081156121dc578591612191575b509261212f60209260049561438e565b60405163e4c62a1160e01b815293849182905afa80156107285761034e92849161216257506001600160f81b031661422b565b612184915060203d60201161218a575b61217c8183613a64565b810190613c3c565b5f6120be565b503d612172565b9390506020843d6020116121d4575b816121ad60209383613a64565b810103126121d05761212f6020926121c6600496613bc1565b929550925061211f565b8480fd5b3d91506121a0565b6040513d87823e3d90fd5b506020823d60201161221e575b8161220160209383613a64565b8101031261221a576122156120fb92613bc1565b6120f1565b8580fd5b3d91506121f4565b6040513d88823e3d90fd5b6040513d89823e3d90fd5b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663e5ed1efe17905561228e614f8e565b601f546040516372f68f7f60e11b8152906020908290600490829060081c6001600160a01b03165afa80156104355782906115355761034e915061433b565b50346102995760403660031901126102995760043560243560ff81168103612698576001905b600582106122ff578380f35b5f198201908282116126e35760ff918261231992166142c9565b169261232482613bdb565b93815b83811061269c5750601f5460081c6001600160a01b0316803b15612698578280916024604051809481936355231c1360e11b83528a60048401525af18015610728578390612681575b90505081928280945b87518610156123cd57838610156123a35761239a600191611cc3888b613c0d565b955b0194612379565b948084036123b4575b60019061239c565b936123c5600191611cc3878b613c0d565b9490506123ac565b90959450929091926123f2826123ed6123e6878b613c0d565b5184613b86565b613b86565b6101000390610100821161266d576124179161240d91613b86565b9185831b92613b86565b1c9060018060a01b03601f5460081c1660018060a01b03196004541617600455600160ff196006541617600655606063ffffffff602460405161245a8482613a64565b818152636e74382960e01b604060208301927f67657452616e646f6d5061636b65642875696e74382c75696e74385b5d2c7569845201522060e01c1663ffffffff19600254161760025560405180978560808301938560208501528060408501528251809552602060a0850193018a5b8681106126545750506124e9945083015203601f198101885287613a64565b85516001600160401b03811161264057612504600754613ab2565b601f81116125df575b506020601f821160011461257a5786978293949596979261256f575b50508160011b915f199060031b1c1916176007555b6125475f616881565b6020815191818082019384920101031261035c57600192612568915161422b565b01906122f3565b015190505f80612529565b6007875280872090601f198316885b8181106125c757509883600195969798999a106125af575b505050811b0160075561253e565b01515f1960f88460031b161c191690555f80806125a1565b9192602060018192868e015181550194019201612589565b8181111561250d5760078752612632907fa66cc928b5edb82af9bd49922954155ab7b0942694bea4ce44661d9a8736c68890601f840160051c9060208510612638575b601f82910160051c0391016154eb565b5f61250d565b899150612622565b634e487b7160e01b86526041600452602486fd5b815185526020948501948a9450909101906001016124ca565b634e487b7160e01b87526011600452602487fd5b61268a91613a64565b815f12610a10575f82612370565b8280fd5b600181018082116126cf576001600160fd1b03811681036126cf579060019160031b6126c88289613c0d565b5201612327565b634e487b7160e01b84526011600452602484fd5b634e487b7160e01b85526011600452602485fd5b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663b7e19e291790556127496152e2565b5080f35b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916638c6b45511790556127a0306143e1565b6127a8614c3b565b601f54604051638c6b455160e01b8152306004820152906020908290602490829060081c6001600160a01b03165afa908115610435578291612832575b505f5160206187555f395f51905f523b15610a1057604051630c9fd58160e01b815290151560048201528180826024815f5160206187555f395f51905f525afa8015610605576105f05780f35b90506020813d602011612864575b8161284d60209383613a64565b81010312610a105761285e90613bc1565b5f6127e5565b3d9150612840565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff19166315e8b34517905560016003556128c3615563565b545f5160206187555f395f51905f523b1561035c576040519063260a5b1560e21b82526008600483015260248201525f816044815f5160206187555f395f51905f525afa801561035157610344575080f35b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663504429bf179055612968306143e1565b806003556129746148e7565b601f546040805163504429bf60e01b8152306004820152918290602490829060081c6001600160a01b03165afa80156104355761034e91839084926129c3575b506129be9061409b565b61404c565b6129be92506129e1915060403d604011610f6e57610f608183613a64565b916129b4565b503461029957806003193601126102995760405160178054808352908352909160208301917fc624b66cc0138b8fabc209247f72d758e1cf3343756d543badbf24212bed8c15915b818110612a46576109268561091a81870382613a64565b82546001600160a01b0316845260209093019260019283019201612a2f565b503461029957806003193601126102995760405160188054808352908352909160208301917fb13d2d76d1f4b7be834882e410b3e3a8afaf69f83600ae24db354391d2378d2e915b818110612ac4576109268561091a81870382613a64565b82546001600160a01b0316845260209093019260019283019201612aad565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916630310c060179055612b36306143e1565b612b3f306143e1565b80600355612b4b6148e7565b601f54604080516218860360e51b815291829060081c6001600160a01b03168180612b7a308060048401613ba7565b03915afa80156104355761034e9183908492612ba0575b50612b9b906140eb565b61413b565b612b9b9250612bbe915060403d604011610f6e57610f608183613a64565b91612b91565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff1916630310c060179055612c7690612c1b306143e1565b612c24306143e1565b80600355612c30615563565b549060405160208101903082526006604082015260408152612c53606082613a64565b519020604051612c6c816110c160208201943086613b6b565b519020905061427a565b005b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663b7e19e29179055612cca6167b2565b6020815191818082019384920101031261035c578190515f5160206187555f395f51905f523b1561070e57604051637c84c69b60e01b8152600481019190915261133760f01b602482015281816044815f5160206187555f395f51905f525afa801561043557612d375750f35b81612d4191613a64565b6102995780f35b5034610299576040366003190112610299576004356001600160a01b03811690819003610a10576024356001600160801b03811690819003612698576006805460ff19166001179055601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff19166341b6edb2179055612dd3826143e1565b612ddc816144a4565b601f546040516320db76d960e11b81526004810184905260089190911c6001600160a01b031690602081602481855afa80156121dc5783908690612ee6575b612e25925061422b565b6006805460ff19166001179055600480546001600160a01b0319169190911790556002805463ffffffff1916633eae2218179055612e62826143e1565b612e6b816144a4565b601f546040516307d5c44360e31b815260048101939093526020908390602490829060081c6001600160a01b03165afa8015610728578390612eb2575b61034e925061422b565b506020823d602011612ede575b81612ecc60209383613a64565b8101031261035c5761034e9151612ea8565b3d9150612ebf565b50506020813d602011612f14575b81612f0160209383613a64565b8101031261035c5782612e259151612e1b565b3d9150612ef4565b5034610299578060031936011261029957601e54612f3981613a9b565b612f466040519182613a64565b818152601e83526020810191837f50bb669a95c7b50b7e8a6f09454034b2b14cf2b85c730dca9a539ca82cb6e350845b83831061304a5786858760405192839260208401906020855251809152604084019160408260051b8601019392815b838310612fb25786860387f35b919395509193603f198782030183528551906020604082019260018060a01b0381511683520151916040602083015282518091526060820190602060608260051b850101940192855b82811061301f57505050505060208060019297019301930190928695949293612fa5565b909192939460208061303d600193605f1987820301895289516138f7565b9701950193929101612ffb565b60405161305681613a2e565b82546001600160a01b0316815260018301805461307281613a9b565b916130806040519384613a64565b8183528a526020808b20908b9084015b8382106130b6575050505060019282602092836002950152815201920192019190612f76565b6001602081926040516130cd81610e6e818a613aea565b815201930191019091613090565b5034610299578060031936011261029957601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663504429bf17905561312e306143e1565b600160035561313b6148e7565b601f546040805163504429bf60e01b8152306004820152918290602490829060081c6001600160a01b03165afa80156104355761034e9183908492613185575b5061147a9061404c565b61147a92506131a3915060403d604011610f6e57610f608183613a64565b9161317b565b503461029957806003193601126102995760405160168054808352908352909160208301917fd833147d7dc355ba459fc788f669e58cfaf9dc25ddcd0702e87d69c7b5124289915b818110613208576109268561091a81870382613a64565b82546001600160a01b03168452602090930192600192830192016131f1565b5034610299578060031936011261029957604051610b2f808201908282106001600160401b0383111761073357908291616b738339039082f0801561060557601f8054610100600160a81b03191660089290921b610100600160a81b031691909117905580f35b5034610299578060031936011261029957601f54604051632e11ff4f60e11b81526105396004820152919060081c6001600160a01b0316602083602481845afa928315610435578293613445575b50600480546001600160a01b0319169190911790556002805463ffffffff1916635c23fe9e17905560015491600160401b83101561343157600183018060015583101561341d57600182526105395f5160206187755f395f51905f5290930183905590918291613357906001600160801b03191682176144a4565b601f546040516320db76d960e11b815260048101839052906020908290602490829060081c6001600160a01b03165afa9081156107285783916133e8575b505f5160206187555f395f51905f523b156133e4576040519163260a5b1560e21b83526004830152602482015281816044815f5160206187555f395f51905f525afa801561043557612d375750f35b5050fd5b9250506020823d602011613415575b8161340460209383613a64565b8101031261035c578291515f613395565b3d91506133f7565b634e487b7160e01b82526032600452602482fd5b634e487b7160e01b82526041600452602482fd5b9092506020813d602011613471575b8161346160209383613a64565b8101031261035c5751915f6132dc565b3d9150613454565b503461035c575f36600319011261035c57601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663a73e40cc1790556134cc306143e1565b60018060a01b03600454166003545f5160206187555f395f51905f523b1561035c5760405162fa5c1760e61b81525f81600481835f5160206187555f395f51905f525af1801561035157613894575b506135509161353460609261352e615563565b54613bce565b6040516343b7127360e11b815293849283929060048401613b6b565b0381855f5160206187555f395f51905f525af1908115610435578283918493613871575b50156137685782905f5160206187555f395f51905f523b15610a10576040516328a9b0fb60e11b8152908290829081906135bc9030906001600160a01b031660048401613ba7565b03815f5160206187555f395f51905f525afa80156104355761385c575b50506135e490613ff2565b601f54600480546001600160a01b03191660089290921c6001600160a01b03169190911790556002805463ffffffff191663a73e40cc179055613626306143e1565b60018060a01b03600454166003545f5160206187555f395f51905f523b156126985760405162fa5c1760e61b815283908181600481835f5160206187555f395f51905f525af1801561043557613847575b50506136859061352e615563565b6136a760608492604051809381926343b7127360e11b83528760048401613b6b565b0381875f5160206187555f395f51905f525af1801561375d5784918591613824575b50908015613768575b6136e0578361034e83613ff2565b6040516343b7127360e11b815290915060608180613702858760048401613b6b565b0381875f5160206187555f395f51905f525af1801561375d578491859161372b575b50906136d2565b905061374e915060603d8111613756575b6137468183613a64565b81019061444d565b90505f613724565b503d61373c565b6040513d86823e3d90fd5b60405162461bcd60e51b815260206004820152607c60248201527f73746453746f7261676520726561645f626f6f6c2853746453746f726167652960448201527f3a2043616e6e6f742066696e6420706172656e742e204d616b6520737572652060648201527f796f752067697665206120736c6f7420616e642073746172744d617070696e6760848201527f5265636f7264696e67282920686173206265656e2063616c6c65642e0000000060a48201528060c481015b0390fd5b905061383f915060603d606011613756576137468183613a64565b90505f6136c9565b8161385191613a64565b61269857825f613677565b8161386691613a64565b610a1057815f6135d9565b91505061388d915060603d606011613756576137468183613a64565b915f613574565b6060919350916138a75f61355094613a64565b6135345f949250509161351b565b60206040818301928281528451809452019201905f5b8181106138d85750505090565b82516001600160a01b03168452602093840193909201916001016138cb565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b90602080835192838152019201905f5b8181106139385750505090565b82516001600160e01b03191684526020938401939092019160010161392b565b602081016020825282518091526040820191602060408360051b8301019401925f915b83831061398a57505050505090565b90919293946020806139a8600193603f1986820301875289516138f7565b9701930193019193929061397b565b602081016020825282518091526040820191602060408360051b8301019401925f915b8383106139e957505050505090565b9091929394602080613a1f600193603f198682030187526040838b51878060a01b0381511684520151918185820152019061391b565b970193019301919392906139da565b604081019081106001600160401b03821117610bde57604052565b608081019081106001600160401b03821117610bde57604052565b90601f801991011681019081106001600160401b03821117610bde57604052565b919082604091031261035c576020825192015190565b6001600160401b038111610bde5760051b60200190565b90600182811c92168015613ae0575b6020831014613acc57565b634e487b7160e01b5f52602260045260245ffd5b91607f1691613ac1565b5f9291815491613af983613ab2565b8083529260018116908115613b4e5750600114613b1557505050565b5f9081526020812093945091925b838310613b34575060209250010190565b600181602092949394548385870101520191019190613b23565b915050602093945060ff929192191683830152151560051b010190565b6001600160a01b039091168152602081019190915260400190565b91908201809211613b9357565b634e487b7160e01b5f52601160045260245ffd5b6001600160a01b0391821681529116602082015260400190565b5190811515820361035c57565b91908203918211613b9357565b90613be582613a9b565b613bf26040519182613a64565b8281528092613c03601f1991613a9b565b0190602036910137565b8051821015610bca5760209160051b010190565b6001600160401b038111610bde57601f01601f191660200190565b9081602091031261035c57516001600160f81b038116810361035c5790565b90604051918281549182825260208201905f5260205f20925f905b806007830110613dba57613ccc945491818110613d9b575b818110613d7c575b818110613d5d575b818110613d3e575b818110613d1f575b818110613d00575b818110613ce3575b10613cce575b500383613a64565b565b6001600160e01b03191681526020015f613cc4565b602083811b6001600160e01b031916855290930192600101613cbe565b604083901b6001600160e01b0319168452602090930192600101613cb6565b606083901b6001600160e01b0319168452602090930192600101613cae565b608083901b6001600160e01b0319168452602090930192600101613ca6565b60a083901b6001600160e01b0319168452602090930192600101613c9e565b60c083901b6001600160e01b0319168452602090930192600101613c96565b60e083901b6001600160e01b0319168452602090930192600101613c8e565b916008919350610100600191865463ffffffff60e01b8160e01b16825263ffffffff60e01b8160c01b16602083015263ffffffff60e01b8160a01b16604083015263ffffffff60e01b8160801b16606083015263ffffffff60e01b8160601b16608083015263ffffffff60e01b8160401b1660a083015263ffffffff60e01b8160201b1660c083015263ffffffff60e01b1660e0820152019401920185929391613c76565b60405190613e6e604083613a64565b602082527f67657452616e646f6d5061636b65642875696e743235362c75696e74323536296020830152565b60085460ff168015613ea95790565b50604051630667f9d760e41b81525f5160206187555f395f51905f5260048201526519985a5b195960d21b60248201526020816044815f5160206187555f395f51905f525afa908115610351575f91613f03575b50151590565b90506020813d602011613f2d575b81613f1e60209383613a64565b8101031261035c57515f613efd565b3d9150613f11565b606090604081527f73746453746f726167652066696e642853746453746f72616765293a204e6f2060208201527f73746f726167652075736520646574656374656420666f72207461726765742e60408201520190565b6040713932903932b0b234b7339030903137b7b61760711b917f73746453746f7261676520726561645f626f6f6c2853746453746f726167652981527f3a2043616e6e6f74206465636f64652e204d616b65207375726520796f75206160208201520152565b5f5160206187555f395f51905f523b1561035c576040519063260a5b1560e21b82526001600483015260248201525f816044815f5160206187555f395f51905f525afa8015610351576140425750565b5f613ccc91613a64565b5f5160206187555f395f51905f523b1561035c576040519063260a5b1560e21b825260048201525f60248201525f816044815f5160206187555f395f51905f525afa8015610351576140425750565b5f5160206187555f395f51905f523b1561035c576040519063260a5b1560e21b82526004820152606460248201525f816044815f5160206187555f395f51905f525afa8015610351576140425750565b5f5160206187555f395f51905f523b1561035c576040519063260a5b1560e21b82526064600483015260248201525f816044815f5160206187555f395f51905f525afa8015610351576140425750565b5f5160206187555f395f51905f523b1561035c576040519063260a5b1560e21b82525f600483015260248201525f816044815f5160206187555f395f51905f525afa8015610351576140425750565b5f5160206187555f395f51905f523b1561035c576040519063260a5b1560e21b8252600482015261053960248201525f816044815f5160206187555f395f51905f525afa8015610351576140425750565b5f5160206187555f395f51905f523b1561035c576040519063260a5b1560e21b82526004820152600160248201525f816044815f5160206187555f395f51905f525afa8015610351576140425750565b905f5160206187555f395f51905f523b1561035c576040519163260a5b1560e21b8352600483015260248201525f816044815f5160206187555f395f51905f525afa8015610351576140425750565b905f5160206187555f395f51905f523b1561035c5760405191637c84c69b60e01b8352600483015260248201525f816044815f5160206187555f395f51905f525afa8015610351576140425750565b905f6142d492615360565b905f806040516142e5604082613a64565b600c81526b109bdd5b99081c995cdd5b1d60a21b6020820152604051614328816118fb6020820194632d839cb360e21b86526040602484015260648301906138f7565b51906a636f6e736f6c652e6c6f675afa50565b5f5160206187555f395f51905f523b1561035c5760405163fe74f05b60e01b8152600481019190915260631960248201525f816044815f5160206187555f395f51905f525afa8015610351576140425750565b905f5160206187555f395f51905f523b1561035c5760405163f7fe347760e01b81529115156004830152151560248201525f816044815f5160206187555f395f51905f525afa8015610351576140425750565b600154600160401b811015610bde576001810180600155811015610bca5760015f525f5160206187755f395f51905f520155565b600154600160401b811015610bde576001810180600155811015610bca5760015f5260645f5160206187755f395f51905f5290910155565b9081606091031261035c5761446181613bc1565b916040602083015192015190565b60209291908391805192839101825e019081520190565b604091949392606082019560018060a01b0316825260208201520152565b6004546002546003545f9493926001600160a01b03169160e01b6144c7866165a9565b90835f525f60205260405f209063ffffffff60e01b1690815f5260205260405f2060405160208101906144ff816110c188888661446f565b5190205f5260205260ff600360405f20015416156148d8575b835f525f60205260405f20905f526020526110c161454560405f209360405192839160208301958661446f565b5190205f5260205260405f2060018101549260028201546145668186613b86565b614763575b82549060405195630667f9d760e41b87526020878061458e868a60048401613b6b565b03815f5160206187555f395f51905f525afa968715610351575f9761472f575b506001908201610100031b5f1901811b198616915f5160206187555f395f51905f523b1561035c576040516370ca10bb60e01b8152925f92849283926145fd9288901b17908960048501614486565b0381835f5160206187555f395f51905f525af180156103515761471a575b506146258661668d565b91901591821561470f575b50506146435750505090613ccc9061693a565b8492935054905f5160206187555f395f51905f523b156126985761467b60405194859384936370ca10bb60e01b855260048501614486565b0381835f5160206187555f395f51905f525af18015610435576146fa575b60405162461bcd60e51b815260206004820152603360248201527f73746453746f726167652066696e642853746453746f72616765293a204661696044820152723632b2103a37903bb934ba32903b30b63ab29760691b6064820152608490fd5b614705828092613a64565b6102995780614699565b141590505f80614630565b6147279196505f90613a64565b5f945f61461b565b9096506020813d60201161475b575b8161474b60209383613a64565b8101031261035c575195816145ae565b3d915061473e565b61476d8186613b86565b610100036101008111613b935760ff8111613b935760405163348051d760e11b8152600190911b600482018190525f826024815f5160206187555f395f51905f525afa918215610351575f92614856575b50614825606a6020936040519485915f5160206187955f395f51905f52828401525f5160206187355f395f51905f52604084015269030ba32b9103a3430b7160b51b60608401528051918291018484015e81015f838201520301601f198101845283613a64565b831015614832575061456b565b60405162461bcd60e51b8152602060048201529081906138209060248301906138f7565b91503d805f843e6148678184613a64565b82019160208184031261035c578051906001600160401b03821161035c570182601f8201121561035c5780519061489d82613c21565b936148ab6040519586613a64565b8285526020838301011161035c576020935f85846148259582606a96018386015e830101529350506147be565b6148e15f615da4565b50614518565b6004546002546003545f93926001600160a01b03169160e01b614909856165a9565b90835f525f60205260405f209063ffffffff60e01b1690815f5260205260405f206040516020810190614941816110c188888661446f565b5190205f5260205260ff600360405f2001541615614c2c575b835f525f60205260405f20905f526020526110c161498760405f209360405192839160208301958661446f565b5190205f5260205260405f209060018201549160028101546149a98185613b86565b614ada575b81549060405194630667f9d760e41b8652602086806149d1868960048401613b6b565b03815f5160206187555f395f51905f525afa958615610351575f96614aa6575b506001908201610100031b5f1901811b198516915f5160206187555f395f51905f523b1561035c576040516370ca10bb60e01b8152925f9284928392614a41926064901b17908860048501614486565b0381835f5160206187555f395f51905f525af1801561035157614a91575b50614a698561668d565b9015908115614a85575b506146435750505090613ccc9061693a565b6064915014155f614a73565b614a9e9195505f90613a64565b5f935f614a5f565b9095506020813d602011614ad2575b81614ac260209383613a64565b8101031261035c575194816149f1565b3d9150614ab5565b614ae48185613b86565b610100036101008111613b935760ff8111613b935760405163348051d760e11b8152600190911b600482018190525f826024815f5160206187555f395f51905f525afa918215610351575f92614baa575b50614b9c606a6020936040519485915f5160206187955f395f51905f52828401525f5160206187355f395f51905f52604084015269030ba32b9103a3430b7160b51b60608401528051918291018484015e81015f838201520301601f198101845283613a64565b6064101561483257506149ae565b91503d805f843e614bbb8184613a64565b82019160208184031261035c578051906001600160401b03821161035c570182601f8201121561035c57805190614bf182613c21565b93614bff6040519586613a64565b8285526020838301011161035c576020935f8584614b9c9582606a96018386015e83010152935050614b35565b614c355f615da4565b5061495a565b6004546002546003545f93926001600160a01b03169160e01b614c5d856165a9565b90835f525f60205260405f209063ffffffff60e01b1690815f5260205260405f206040516020810190614c95816110c188888661446f565b5190205f5260205260ff600360405f2001541615614f7f575b835f525f60205260405f20905f526020526110c1614cdb60405f209360405192839160208301958661446f565b5190205f5260205260405f20906001820154916002810154614cfd8185613b86565b614e2d575b81549060405194630667f9d760e41b865260208680614d25868960048401613b6b565b03815f5160206187555f395f51905f525afa958615610351575f96614df9575b506001908201610100031b5f1901811b198516915f5160206187555f395f51905f523b1561035c576040516370ca10bb60e01b8152925f9284928392614d95926001901b17908860048501614486565b0381835f5160206187555f395f51905f525af1801561035157614de4575b50614dbd8561668d565b9015908115614dd857506146435750505090613ccc9061693a565b6001915014155f614a73565b614df19195505f90613a64565b5f935f614db3565b9095506020813d602011614e25575b81614e1560209383613a64565b8101031261035c57519481614d45565b3d9150614e08565b614e378185613b86565b610100036101008111613b935760ff8111613b935760405163348051d760e11b8152600190911b600482018190525f826024815f5160206187555f395f51905f525afa918215610351575f92614efd575b50614eef606a6020936040519485915f5160206187955f395f51905f52828401525f5160206187355f395f51905f52604084015269030ba32b9103a3430b7160b51b60608401528051918291018484015e81015f838201520301601f198101845283613a64565b600110156148325750614d02565b91503d805f843e614f0e8184613a64565b82019160208184031261035c578051906001600160401b03821161035c570182601f8201121561035c57805190614f4482613c21565b93614f526040519586613a64565b8285526020838301011161035c576020935f8584614eef9582606a96018386015e83010152935050614e88565b614f885f615da4565b50614cae565b6004546002546003545f93926001600160a01b03169160e01b614fb0856165a9565b90835f525f60205260405f209063ffffffff60e01b1690815f5260205260405f206040516020810190614fe8816110c188888661446f565b5190205f5260205260ff600360405f20015416156152d3575b835f525f60205260405f20905f526020526110c161502e60405f209360405192839160208301958661446f565b5190205f5260205260405f209060018201549160028101546150508185613b86565b615180575b81549060405194630667f9d760e41b865260208680615078868960048401613b6b565b03815f5160206187555f395f51905f525afa958615610351575f9661514c575b506001908201610100031b5f1901811b1985165f5160206187555f395f51905f523b1561035c575f916150e760405194859384936370ca10bb60e01b8552606319901b17908860048501614486565b0381835f5160206187555f395f51905f525af1801561035157615137575b5061510f8561668d565b901590811561512a57506146435750505090613ccc9061693a565b606319141590505f614a73565b6151449195505f90613a64565b5f935f615105565b9095506020813d602011615178575b8161516860209383613a64565b8101031261035c57519481615098565b3d915061515b565b61518a8185613b86565b610100036101008111613b935760ff8111613b935760405163348051d760e11b8152600190911b600482018190525f826024815f5160206187555f395f51905f525afa918215610351575f92615251575b50615242606a6020936040519485915f5160206187955f395f51905f52828401525f5160206187355f395f51905f52604084015269030ba32b9103a3430b7160b51b60608401528051918291018484015e81015f838201520301601f198101845283613a64565b60631910156148325750615055565b91503d805f843e6152628184613a64565b82019160208184031261035c578051906001600160401b03821161035c570182601f8201121561035c5780519061529882613c21565b936152a66040519586613a64565b8285526020838301011161035c576020935f85846152429582606a96018386015e830101529350506151db565b6152dc5f615da4565b50615001565b6152eb5f616881565b6020815191818082019384920101031261035c5751801561533d576001146153385760405162461bcd60e51b8152602060048201526052602482015260a49061533660448201613f8c565bfd5b600190565b505f90565b811561534c570690565b634e487b7160e01b5f52601260045260245ffd5b5f908383116154805782811091821580615476575b61546e576153838486613bce565b9260018401809411613b9357600383111580615465575b615456576003198310158061544c575b61543857858311156153ef575050906153c6846153cb93613bce565b615342565b9081156153ea576153dc9250613b86565b5f198101908111613b935790565b505090565b959492919095615400575b50505050565b839495506153c6906154129394613bce565b9081156153ea576154239250613bce565b60018101809111613b9357905f8080806153fa565b505090506154499291501990613bce565b90565b50821984116153aa565b50509190506154499250613b86565b5082841161539a565b509250505090565b5084821115615375565b60405162461bcd60e51b815260206004820152603e60248201527f5374645574696c7320626f756e642875696e743235362c75696e743235362c7560448201527f696e74323536293a204d6178206973206c657373207468616e206d696e2e00006064820152608490fd5b5f5b8281106154f957505050565b5f828201556001016154ed565b9080601f8301121561035c57815161551d81613a9b565b9261552b6040519485613a64565b81845260208085019260051b82010192831161035c57602001905b8282106155535750505090565b8151815260209182019101615546565b6004546002546003546001600160a01b03909216915f9160e01b615586836165a9565b90845f525f60205260405f209063ffffffff60e01b1690815f5260205260405f2060405160208101906155be816110c188888661446f565b5190205f5260205260ff600360405f20015416615d5b575f5160206187555f395f51905f523b1561035c5760405163266cf10960e01b81525f81600481835f5160206187555f395f51905f525af1801561035157615d46575b506156218461668d565b6040516365bc948160e01b81526004810188905291508582602481835f5160206187555f395f51905f525af1918215612226578692615cd8575b508151806156835760405162461bcd60e51b8152602060048201528061382060248201613f35565b9190915b801561266d57906156be915f19019060206156a28383613c0d565b5160405180958192630667f9d760e41b83528d60048401613b6b565b03815f5160206187555f395f51905f525afa928315615ccd578893615c9a575b508215615c56575b6156f08282613c0d565b5160018060a01b036004541690604051630667f9d760e41b81526020818061571c858760048401613b6b565b03815f5160206187555f395f51905f525afa908115615c4b578b91615c1a575b506157468b61668d565b91909382155f14615c13575f19905b5f5160206187555f395f51905f523b15615bfa57848e9161578a60405194859384936370ca10bb60e01b855260048501614486565b0381835f5160206187555f395f51905f525af18015615b7657908d91615bfe575b506157b59061668d565b600454909491506001600160a01b03165f5160206187555f395f51905f523b15615bfa57908d916157fa60405194859384936370ca10bb60e01b855260048501614486565b0381835f5160206187555f395f51905f525af18015615bef57908c91615bd6575b505082615bcb575b505015615bc3578886888a968b9660ff60065416615a42575b6001898901610100031b5f1901881b16871c8103615a325750927f9c9555b1e3102e3cf48f427d79cb678f5d9bd1ed0ad574389461e255f95170ed60806158c894600397946110c161589d6159509c9960405192839160208301958661446f565b5190206158aa8686613c0d565b51906040519283528c602084015260408301526060820152a1613c0d565b5192604051936158d785613a49565b845260208401918252604084019081526060840191600183528a8a528960205260408a20878b5260205260408a20886110c161591e8c60405192839160208301958661446f565b5190208b5260205260408a209451855551600185015551600284015551151591019060ff801983541691151516179055565b848452836020526040842081855260205260408420604051602081019061597c816110c188888661446f565b519020855260205260ff600360408620015416156159d5576040946159a08561693a565b8452836020528484209084526020526110c16159c985852093865192839160208301958661446f565b51902082526020522090565b60405162461bcd60e51b815260206004820152602f60248201527f73746453746f726167652066696e642853746453746f72616765293a20536c6f60448201526e3a143994903737ba103337bab7321760891b6064820152608490fd5b955050505092505b919091615687565b975092505050615a829350615a578383613c0d565b519460208660018060a01b03600454166040519788928392630667f9d760e41b845260048401613b6b565b03815f5160206187555f395f51905f525afa948515615bb8578a95615b85575b50615aad868b6169f4565b959096615aba818d616abe565b60045490939192906001600160a01b03165f5160206187555f395f51905f523b15615b8157908e91615b0060405194859384936370ca10bb60e01b855260048501614486565b0381835f5160206187555f395f51905f525af18015615b7657928e95928e8d96938f96615b4c575b50508a615b44575b50979861583c575095505050509250615a3a565b99505f615b30565b909396508391949750615b60929550613a64565b615b72579289928b928e958e5f615b28565b8b80fd5b6040513d8f823e3d90fd5b8e80fd5b9094506020813d8211615bb0575b81615ba060209383613a64565b8101031261035c5751935f615aa2565b3d9150615b93565b6040513d8c823e3d90fd5b929150615a3a565b141590505f80615823565b81615be091613a64565b615beb578a5f61581b565b8a80fd5b6040513d8e823e3d90fd5b8d80fd5b81615c0891613a64565b615b72578b5f6157ab565b8c90615755565b90506020813d8211615c43575b81615c3460209383613a64565b8101031261035c57515f61573c565b3d9150615c27565b6040513d8d823e3d90fd5b7f080fc4a96620c4462e705b23f346413fe3796bb63c6f8d8591baec0e231577a5615c92615c848484613c0d565b516040519182918d83613b6b565b0390a16156e6565b9092506020813d8211615cc5575b81615cb560209383613a64565b8101031261035c5751915f6156de565b3d9150615ca8565b6040513d8a823e3d90fd5b9091503d8087833e615cea8183613a64565b8101604082820312615d425781516001600160401b038111615d3e5781615d12918401615506565b916020810151906001600160401b038211615d3a57615d32929101615506565b50905f61565b565b8880fd5b8780fd5b8680fd5b615d539194505f90613a64565b5f925f615617565b9193909250615d695f61693a565b5f525f60205260405f20905f526020526110c1615d9560405f209360405192839160208301958661446f565b5190205f5260205260405f2090565b6004810154600282015460038301546001600160a01b03909216925f929160e01b615dce826165a9565b9160018060a01b0386165f528060205260405f2063ffffffff60e01b83165f5260205260405f206040516020810190615e0c816110c189898661446f565b5190205f5260205260ff600360405f20015416616568575f5160206187555f395f51905f523b1561035c5760405163266cf10960e01b81525f81600481835f5160206187555f395f51905f525af1801561035157616553575b50615e6f8161668d565b6040516365bc948160e01b81526004810189905291508682602481835f5160206187555f395f51905f525af19182156122315787926164ed575b50815180615ed15760405162461bcd60e51b8152602060048201528061382060248201613f35565b9190915b80156164d95790615f0e915f1901906020615ef08383613c0d565b51604051630667f9d760e41b81529485918291908e60048401613b6b565b03815f5160206187555f395f51905f525afa9283156164ce57899361649b575b508215616457575b615f408282613c0d565b5160018060a01b0360048701541690604051630667f9d760e41b815260208180615f6e858760048401613b6b565b03815f5160206187555f395f51905f525afa908115615bef578c91616426575b50615f988861668d565b91909382155f1461641f575f19905b5f5160206187555f395f51905f523b15615b8157848f91615fdc60405194859384936370ca10bb60e01b855260048501614486565b0381835f5160206187555f395f51905f525af1801561639e57908e9161640a575b50506160088961668d565b60048b0154909491506001600160a01b03165f5160206187555f395f51905f523b15615b8157908e9161604f60405194859384936370ca10bb60e01b855260048501614486565b0381835f5160206187555f395f51905f525af18015615b7657908d916163f5575b5050826163ea575b5050156163e2578987898b968c9660ff60068b015416616265575b6001898901610100031b5f1901881b16871c81036162555750927f9c9555b1e3102e3cf48f427d79cb678f5d9bd1ed0ad574389461e255f95170ed608061612894600397946110c16160f46161c19c9960405192839160208301958661446f565b5190206161018686613c0d565b51906040519283528d63ffffffff60e01b16602084015260408301526060820152a1613c0d565b51926040519361613785613a49565b8452602080850192835260408086019283526001606087019081526001600160a01b038e165f9081528984528290206001600160e01b03198b168e528352818d20915190949281019061618f816110c18f8f8661446f565b5190208c5260205260408b209451855551600185015551600284015551151591019060ff801983541691151516179055565b6001600160a01b0386165f90815260208281526040918290206001600160e01b0319851688528152818720915190810190616201816110c189898661446f565b519020865260205260ff600360408720015416156159d55760409560018060a01b03165f52602052845f209063ffffffff60e01b1684526020526110c16159c985852093865192839160208301958661446f565b955050505092505b919091615ed5565b9750925050506162a7935061627a8383613c0d565b519460208660018060a01b0360048a0154166040519788928392630667f9d760e41b845260048401613b6b565b03815f5160206187555f395f51905f525afa948515615c4b578b956163af575b506162d286886169f4565b9590966162df818a616abe565b60048b015490939192906001600160a01b03165f5160206187555f395f51905f523b156163ab57908f9161632760405194859384936370ca10bb60e01b855260048501614486565b0381835f5160206187555f395f51905f525af1801561639e57928f95928f8f95938f9794616374575b50508a61636c575b50979861609357509550505050925061625d565b99505f616358565b909396508391949750616388929550613a64565b61639a57928a928c928f958f5f616350565b8c80fd5b8e604051903d90823e3d90fd5b8f80fd5b9094506020813d82116163da575b816163ca60209383613a64565b8101031261035c5751935f6162c7565b3d91506163bd565b92915061625d565b141590505f80616078565b816163ff91613a64565b615b72578b5f616070565b8161641491613a64565b61639a578c5f615ffd565b8d90615fa7565b90506020813d821161644f575b8161644060209383613a64565b8101031261035c57515f615f8e565b3d9150616433565b7f080fc4a96620c4462e705b23f346413fe3796bb63c6f8d8591baec0e231577a56164828383613c0d565b518b61649360405192839283613b6b565b0390a1615f36565b9092506020813d82116164c6575b816164b660209383613a64565b8101031261035c5751915f615f2e565b3d91506164a9565b6040513d8b823e3d90fd5b634e487b7160e01b88526011600452602488fd5b9091503d8088833e6164ff8183613a64565b8101604082820312615d3e5781516001600160401b038111615d3a5781616527918401615506565b916020810151906001600160401b03821161654f57616547929101615506565b50905f615ea9565b8980fd5b6165609195505f90613a64565b5f935f615e65565b919350919360018060a01b03165f5260205260405f209063ffffffff60e01b165f526020526110c1615d9560405f209360405192839160208301958661446f565b60078101906165b88254613ab2565b61667957600191500190604051808360208295549384815201905f5260205f20925f5b8181106166605750506165f092500383613a64565b81518060051b9080820460201490151715613b935761660e81613c21565b9061661c6040519283613a64565b80825261662b601f1991613c21565b013660208301375f5b835181101561665b578061664a60019286613c0d565b5160208260051b8501015201616634565b509150565b84548352600194850194879450602090930192016165db565b50615449610e6e9160405192838092613aea565b905f806020600285015460e01b6166dd60246166a8886165a9565b6040519485918183019563ffffffff60e01b1686528051918291018484015e810186838201520301601f198101845283613a64565b60048601549151916001600160a01b03165afa3d156167a85760033d9361670385613c21565b946167116040519687613a64565b85523d5f602087013e5b0154600581901b906001600160fb1b03811603613b93575f938051602081115f146167a257506020905b5f925b82841061675757505050509190565b909192956167658783613b86565b8351811015610bca57830160200151600388901b91906001600160f81b031916881560088a8504141715613b93576001921c179601929190616748565b90616745565b600360609361671b565b6168086167be5f615da4565b600181810154600283015492916020918401610100031b5f1901831b600480549354604051630667f9d760e41b8152969294879384939092916001600160a01b0316908401613b6b565b03815f5160206187555f395f51905f525afa928315610351575f9361684d575b506168325f61693a565b6040519216901c602082015260208152615449604082613a64565b9092506020813d602011616879575b8161686960209383613a64565b8101031261035c5751915f616828565b3d915061685c565b6168da9061688e81615da4565b600181810154600283015493916020918501610100031b5f1901841b6004838101549454604051630667f9d760e41b8152979295889384939092916001600160a01b0316908401613b6b565b03815f5160206187555f395f51905f525afa938415610351575f94616904575b506168329061693a565b9093506020813d602011616932575b8161692060209383613a64565b8101031261035c5751926168326168fa565b3d9150616913565b6004810180546001600160a01b031916905560028101805463ffffffff191690556001810180545f825590816169d2575b50505f600382015560068101805460ff19169055600701805461698d90613ab2565b9081616997575050565b81601f5f93116001146169a8575055565b818352602083206169c591601f0160051c841901906001016154eb565b8082528160208120915555565b5f5260205f205f5b8281106169e7575061696b565b5f828201556001016169da565b91905f5b6101008110616a0b57505090505f905f90565b8060ff0360ff8111613b93576004850154600190911b906001600160a01b03165f5160206187555f395f51905f523b1561035c57835f91616a6060405194859384936370ca10bb60e01b855260048501614486565b0381835f5160206187555f395f51905f525af1801561035157616aae575b50616a888461668d565b81616aa4575b50616a9b576001016169f8565b92505060019190565b905015155f616a8e565b5f616ab891613a64565b5f616a7e565b91905f5b6101008110616ad557505090505f905f90565b60048401546001821b906001600160a01b03165f5160206187555f395f51905f523b1561035c57835f91616b1d60405194859384936370ca10bb60e01b855260048501614486565b0381835f5160206187555f395f51905f525af1801561035157616b62575b50616b458461668d565b81616b58575b50616a9b57600101616ac2565b905015155f616b4b565b5f616b6c91613a64565b5f616b3b56fe6080604052346101755760015f819055610100600a5561133760f01b600c55600d80546001600160a01b031916610539179055600160ff1b600e55600f805460ff19169091179055600161ecc960f01b03601055604051606081016001600160401b0381118282101761011c57604052600381526003602082015260036040820152601254600360125580600310610147575b5060125f5260205f20905f5b6003811061013057604080519081016001600160401b0381118282101761011c57610539916020916040528281520152610539600755610539600855335f52600360205270010000000000000000000000000000000160405f20556105395f526003602052600160801b60405f20556040516109b5908161017a8239f35b634e487b7160e01b5f52604160045260245ffd5b600190602060ff845116930192818501550161009e565b60125f5260205f209060021901905f5b828110610165575050610092565b5f82820160030155600101610157565b5f80fdfe60806040526004361015610011575f80fd5b5f3560e01c80630310c060146101c457806308f23aad146101bf57806315e8b345146101ba5780631971f00b146101b55780631aa844b4146101b0578063267c4ae4146101ab5780633b80a793146101a65780633eae2218146101a157806341b6edb21461019c5780634f87aeb714610197578063504429bf1461019257806357351c451461018d5780635c23fe9e1461018857806361a97569146101835780636a56c3d41461017e57806379da7e4d146101795780638c6b4551146101745780638cd8156d1461016f5780639e7936e61461016a578063a73e40cc14610165578063aa46382614610160578063aef6d4b11461015b578063b7e19e2914610156578063e4c62a1114610151578063e5ed1efe1461014c578063e92e9dc4146101475763eb53f99014610142575f80fd5b6107f8565b6107a8565b61078b565b61076b565b61074e565b610712565b6106f9565b6106c1565b61069a565b610643565b610606565b6105de565b6105b4565b6104de565b610464565b610442565b6103f1565b6103cf565b61038f565b610354565b610334565b610318565b6102e9565b6102b6565b61028e565b610266565b6101f9565b600435906001600160a01b03821682036101df57565b5f80fd5b602435906001600160a01b03821682036101df57565b346101df5760403660031901126101df576102466102156101c9565b61021d6101e3565b9060018060a01b03165f52600660205260405f209060018060a01b03165f5260205260405f2090565b8054600190910154604080519283526020830191909152819081015b0390f35b346101df575f3660031901126101df57600d546040516001600160a01b039091168152602090f35b346101df575f3660031901126101df5760075460085460408051928352602083019190915290f35b346101df5760603660031901126101df576011805460016024351b5f190160443590811b1990911660043590911b179055005b346101df5760403660031901126101df576011546040516024359190911c60016004351b5f1901168152602090f35b346101df575f3660031901126101df5760205f54604051908152f35b346101df575f3660031901126101df5760405161133760f01b8152602090f35b346101df5760203660031901126101df576001600160a01b036103756101c9565b165f526003602052602060405f205460801c604051908152f35b346101df5760203660031901126101df576001600160a01b036103b06101c9565b165f526003602052602060018060801b0360405f205416604051908152f35b346101df575f3660031901126101df57602060ff600f54166040519015158152f35b346101df5760203660031901126101df576001600160a01b036104126101c9565b165f52600460205260405f2060018154910154906102626040519283928360209093929193604081019481520152565b346101df575f3660031901126101df57602060095460f81c6040519015158152f35b346101df5760203660031901126101df576001600160a01b036104856101c9565b165f526003602052602060405f2054604051908152f35b6004359060ff821682036101df57565b6044359060ff821682036101df57565b359060ff821682036101df57565b634e487b7160e01b5f52604160045260245ffd5b346101df5760603660031901126101df576104f761049c565b60243567ffffffffffffffff81116101df57366023820112156101df5780600401359067ffffffffffffffff82116105af578160051b60405192601f19603f830116840184811067ffffffffffffffff8211176105af57604052835260246020840191830101913683116101df57602401905b8282106105975761026261058786866105816104ac565b916108ac565b6040519081529081906020820190565b602080916105a4846104bc565b81520191019061056a565b6104ca565b346101df5760203660031901126101df576004355f526002602052602060405f2054604051908152f35b346101df575f3660031901126101df576009546040516001600160f81b039091168152602090f35b346101df5760203660031901126101df576001600160a01b036106276101c9565b165f52600b602052602060ff60405f2054166040519015158152f35b346101df5760403660031901126101df5760206106916106616101c9565b6106696101e3565b6001600160a01b039182165f9081526005855260408082209290931681526020919091522090565b54604051908152f35b346101df575f3660031901126101df575f808080600c545afa506020601054604051908152f35b346101df5760203660031901126101df576001600160a01b036106e26101c9565b165f526001602052602060405f2054604051908152f35b346101df5760203660031901126101df57600435601155005b346101df575f3660031901126101df5760207fb27fb258786eae8f9ffde06a5bfd55f5193cb73bd64e533d5d75fd7cb46652ff54604051908152f35b346101df575f3660031901126101df576020600c54604051908152f35b346101df575f3660031901126101df576020600a5460081c604051908152f35b346101df575f3660031901126101df576020600e54604051908152f35b346101df5760203660031901126101df576004356012548110156101df5760125f527fbb8a6a4669ba250d26cd7a459eca9d215f8307e33aebe50379bc5a3617ec34440154604051908152602090f35b346101df575f3660031901126101df57602060ff600a54166040519015158152f35b1561082157565b60405162461bcd60e51b815260206004820152600560248201526421656c656d60d81b6044820152606490fd5b80518210156108625760209160051b010190565b634e487b7160e01b5f52603260045260245ffd5b634e487b7160e01b5f52601160045260245ffd5b9190820180921161089757565b610876565b6101000390610100821161089757565b929160ff806108bf92169416841061081a565b5f905f935f925b82518410156109395781841015610909576109006001916108fa6108f46108ed888861084e565b5160ff1690565b60ff1690565b9061088a565b935b01926108c6565b9280820361091a575b600190610902565b946109316001916108fa6108f46108ed8a8861084e565b959050610912565b9061097b935061096a8661096561095f6108f46108ed6108fa9661096f999c9b9c61084e565b8561088a565b61088a565b61089c565b91601154831b9261088a565b1c9056fea2646970667358221220a5b91f9f4413b16d57ef507d7fb64b65d823919ca9ca4a91cab9ca25e1c9c08564736f6c63430008210033608034607057601f61109338819003918201601f19168301916001600160401b03831184841017607457808492602094604052833981010312607057516001600160a01b03811690819003607057600880546001600160a01b03191691909117905560405161100a90816100898239f35b5f80fd5b634e487b7160e01b5f52604160045260245ffdfe60806040526004361015610011575f80fd5b5f3560e01c63fc5aec2b14610024575f80fd5b3461008e575f36600319011261008e5760018060a01b036008541660018060a01b0319600454161760045560076020604051610061604082610092565b8281520166636f6e7374282960c81b81522060e01c63ffffffff19600254161760025561008c61018b565b005b5f80fd5b90601f8019910116810190811067ffffffffffffffff8211176100b457604052565b634e487b7160e01b5f52604160045260245ffd5b67ffffffffffffffff81116100b457601f01601f191660200190565b60209291908391805192839101825e019081520190565b9080601f8301121561008e5781519167ffffffffffffffff83116100b4578260051b906040519361012f6020840186610092565b845260208085019282010192831161008e57602001905b8282106101535750505090565b8151815260209182019101610146565b80518210156101775760209160051b010190565b634e487b7160e01b5f52603260045260245ffd5b6004546002546003546001600160a01b03909216915f9160e01b6101ae83610a9c565b90845f525f60205260405f209063ffffffff60e01b1690815f5260205260405f2060405160208101906101f4816101e68888866100e4565b03601f198101835282610092565b5190205f5260205260ff600360405f20015416610a1b575f516020610fb55f395f51905f523b1561008e5760405163266cf10960e01b81525f81600481835f516020610fb55f395f51905f525af18015610a10576109fb575b5061025784610cf3565b90506040516365bc948160e01b81528660048201528581602481835f516020610fb55f395f51905f525af19081156109f0578691610982575b5080518061030257608460405162461bcd60e51b815260206004820152604060248201527f73746453746f726167652066696e642853746453746f72616765293a204e6f2060448201527f73746f726167652075736520646574656374656420666f72207461726765742e6064820152fd5b801561096e579061034e915f190190602061031d8383610163565b51604051630667f9d760e41b81526001600160a01b038c166004820152602481019190915293849081906044820190565b03815f516020610fb55f395f51905f525afa928315610963578893610930575b5082156108f1575b6103808282610163565b5160048054604051630667f9d760e41b81526001600160a01b03909116918101829052602481018390529091906020816044815f516020610fb55f395f51905f525afa9081156108e6578b916108b5575b506103db8b610cf3565b91909382155f146108ae575f19905b5f516020610fb55f395f51905f523b1561089557848e9161041f60405194859384936370ca10bb60e01b855260048501610e18565b0381835f516020610fb55f395f51905f525af1801561081257908d91610899575b5061044a90610cf3565b600454909491506001600160a01b03165f516020610fb55f395f51905f523b1561089557908d9161048f60405194859384936370ca10bb60e01b855260048501610e18565b0381835f516020610fb55f395f51905f525af1801561088a57908c91610871575b505082610866575b50501561085f578793889360ff600654166106eb575b6001858701610100031b5f1901851b16841c81036106e2575090610554917f9c9555b1e3102e3cf48f427d79cb678f5d9bd1ed0ad574389461e255f95170ed60808b896101e66105298d6040519283916020830195866100e4565b5190206105368686610163565b51906040519283528a602084015260408301526060820152a1610163565b5190604051916080830183811067ffffffffffffffff8211176106ce57906003939291604052825260208201938452604082019081526060820193600185528989528860205260408920868a526020526040892060405160208101906105bf816101e68d8d866100e4565b5190208a526020526040892092518355516001830155516002820155019051151560ff801983541691161790558484528360205260408420818552602052604084206040516020810190610618816101e68888866100e4565b519020855260205260ff600360408620015416156106715760409461063c85610c22565b8452836020528484209084526020526101e66106658585209386519283916020830195866100e4565b51902082526020522090565b60405162461bcd60e51b815260206004820152602f60248201527f73746453746f726167652066696e642853746453746f72616765293a20536c6f60448201526e3a143994903737ba103337bab7321760891b6064820152608490fd5b634e487b7160e01b89526041600452602489fd5b93509150610302565b945061073993506106fc8383610163565b5160048054604051630667f9d760e41b81526001600160a01b03909116918101919091526024810182905290959094602090869081906044820190565b03815f516020610fb55f395f51905f525afa948515610854578a95610821575b50610764868b610e36565b959096610771818d610f00565b60045490939192906001600160a01b03165f516020610fb55f395f51905f523b1561081d57908e916107b760405194859384936370ca10bb60e01b855260048501610e18565b0381835f516020610fb55f395f51905f525af1801561081257908d916107f9575b5050876107f1575b5094956104ce575093509150610302565b96505f6107e0565b8161080391610092565b61080e578b5f6107d8565b8b80fd5b6040513d8f823e3d90fd5b8e80fd5b9094506020813d821161084c575b8161083c60209383610092565b8101031261008e5751935f610759565b3d915061082f565b6040513d8c823e3d90fd5b9150610302565b141590505f806104b8565b8161087b91610092565b610886578a5f6104b0565b8a80fd5b6040513d8e823e3d90fd5b8d80fd5b816108a391610092565b61080e578b5f610440565b8c906103ea565b90506020813d82116108de575b816108cf60209383610092565b8101031261008e57515f6103d1565b3d91506108c2565b6040513d8d823e3d90fd5b7f080fc4a96620c4462e705b23f346413fe3796bb63c6f8d8591baec0e231577a5604061091e8484610163565b518151908c82526020820152a1610376565b9092506020813d821161095b575b8161094b60209383610092565b8101031261008e5751915f61036e565b3d915061093e565b6040513d8a823e3d90fd5b634e487b7160e01b87526011600452602487fd5b90503d8087833e6109938183610092565b81016040828203126109ec57815167ffffffffffffffff81116109e857816109bc9184016100fb565b9160208101519067ffffffffffffffff82116109e4576109dd9291016100fb565b505f610290565b8880fd5b8780fd5b8680fd5b6040513d88823e3d90fd5b610a089194505f90610092565b5f925f61024d565b6040513d5f823e3d90fd5b9193909250610a295f610c22565b5f525f60205260405f20905f526020526101e6610a5560405f20936040519283916020830195866100e4565b5190205f5260205260405f2090565b90600182811c92168015610a92575b6020831014610a7e57565b634e487b7160e01b5f52602260045260245ffd5b91607f1691610a73565b60078101908154610aac81610a64565b610b825750600191500190604051808360208295549384815201905f5260205f20925f5b818110610b69575050610ae592500383610092565b81518060051b9080820460201490151715610b5557610b03816100c8565b90610b116040519283610092565b808252610b20601f19916100c8565b013660208301375f5b8351811015610b505780610b3f60019286610163565b5160208260051b8501015201610b29565b509150565b634e487b7160e01b5f52601160045260245ffd5b8454835260019485019487945060209093019201610ad0565b905060405180925f90610b9484610a64565b8084529360018116908115610c005750600114610bbc575b50610bb992500382610092565b90565b90505f9291925260205f20905f915b818310610be4575050906020610bb9928201015f610bac565b6020919350806001915483858801015201910190918392610bcb565b905060209250610bb994915060ff191682840152151560051b8201015f610bac565b6004810180546001600160a01b031916905560028101805463ffffffff191690556001810180545f82559081610cd1575b50506007905f60038201556006810160ff1981541690550190610c768254610a64565b9182610c8157509050565b601f8311600114610c93575f90559050565b5f8181526020812093601f0160051c5f1901905b818110610cc15750505f9192508082528160208120915555565b6001905f82828801015501610ca7565b5f5260205f205f5b828110610ce65750610c53565b5f82820155600101610cd9565b905f806020600285015460e01b610d436024610d0e88610a9c565b6040519485918183019563ffffffff60e01b1686528051918291018484015e810186838201520301601f198101845283610092565b60048601549151916001600160a01b03165afa3d15610e0e5760033d93610d69856100c8565b94610d776040519687610092565b85523d5f602087013e5b0154600581901b906001600160fb1b03811603610b55575f938051602081115f14610e0857506020905b5f925b828410610dbd57505050509190565b90919295868201808311610b5557835181101561017757830160200151600388901b91906001600160f81b031916881560088a8504141715610b55576001921c179601929190610dae565b90610dab565b6003606093610d81565b604091949392606082019560018060a01b0316825260208201520152565b91905f5b6101008110610e4d57505090505f905f90565b8060ff0360ff8111610b55576004850154600190911b906001600160a01b03165f516020610fb55f395f51905f523b1561008e57835f91610ea260405194859384936370ca10bb60e01b855260048501610e18565b0381835f516020610fb55f395f51905f525af18015610a1057610ef0575b50610eca84610cf3565b81610ee6575b50610edd57600101610e3a565b92505060019190565b905015155f610ed0565b5f610efa91610092565b5f610ec0565b91905f5b6101008110610f1757505090505f905f90565b60048401546001821b906001600160a01b03165f516020610fb55f395f51905f523b1561008e57835f91610f5f60405194859384936370ca10bb60e01b855260048501610e18565b0381835f516020610fb55f395f51905f525af18015610a1057610fa4575b50610f8784610cf3565b81610f9a575b50610edd57600101610f04565b905015155f610f8d565b5f610fae91610092565b5f610f7d56fe0000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da2646970667358221220c65f166fc3f6c972570d7c44a8fce87fe2b6805aac0751ac4a86249ee1259f3764736f6c634300082100336b656420736c6f742e2057652063616e2774206669742076616c7565206772650000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12db10e2d527612073b26eecdfd717e6a320cf44b4afac2b0732d9fcbe2b7fa0cf673746453746f726167652066696e642853746453746f72616765293a20506163a2646970667358221220feda49bb0812189c253d662479292ce2e741082115d065387f31260abd1764c564736f6c63430008210033"

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#12)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#12)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#12)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#12)
        """
        ...

    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#12)
        """
        return self._execute(self.chain, request_type, "0a9254e4", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#16)
        """
        ...

    @overload
    def test_StorageHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#16)
        """
        ...

    @overload
    def test_StorageHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#16)
        """
        ...

    @overload
    def test_StorageHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#16)
        """
        ...

    def test_StorageHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#16)
        """
        return self._execute(self.chain, request_type, "962b27ba", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#20)
        """
        ...

    @overload
    def test_StorageObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#20)
        """
        ...

    @overload
    def test_StorageObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#20)
        """
        ...

    @overload
    def test_StorageObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#20)
        """
        ...

    def test_StorageObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#20)
        """
        return self._execute(self.chain, request_type, "6af4e7be", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageExtraSload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#24)
        """
        ...

    @overload
    def test_StorageExtraSload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#24)
        """
        ...

    @overload
    def test_StorageExtraSload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#24)
        """
        ...

    @overload
    def test_StorageExtraSload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#24)
        """
        ...

    def test_StorageExtraSload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#24)
        """
        return self._execute(self.chain, request_type, "c79803c3", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#28)
        """
        ...

    @overload
    def test_StorageCheckedWriteHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#28)
        """
        ...

    @overload
    def test_StorageCheckedWriteHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#28)
        """
        ...

    @overload
    def test_StorageCheckedWriteHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#28)
        """
        ...

    def test_StorageCheckedWriteHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#28)
        """
        return self._execute(self.chain, request_type, "e1664d98", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#33)
        """
        ...

    @overload
    def test_StorageCheckedWriteObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#33)
        """
        ...

    @overload
    def test_StorageCheckedWriteObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#33)
        """
        ...

    @overload
    def test_StorageCheckedWriteObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#33)
        """
        ...

    def test_StorageCheckedWriteObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#33)
        """
        return self._execute(self.chain, request_type, "e87bfd9d", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteSignedIntegerHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#38)
        """
        ...

    @overload
    def test_StorageCheckedWriteSignedIntegerHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#38)
        """
        ...

    @overload
    def test_StorageCheckedWriteSignedIntegerHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#38)
        """
        ...

    @overload
    def test_StorageCheckedWriteSignedIntegerHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#38)
        """
        ...

    def test_StorageCheckedWriteSignedIntegerHidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#38)
        """
        return self._execute(self.chain, request_type, "875ceb10", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteSignedIntegerObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#43)
        """
        ...

    @overload
    def test_StorageCheckedWriteSignedIntegerObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#43)
        """
        ...

    @overload
    def test_StorageCheckedWriteSignedIntegerObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#43)
        """
        ...

    @overload
    def test_StorageCheckedWriteSignedIntegerObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#43)
        """
        ...

    def test_StorageCheckedWriteSignedIntegerObvious(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#43)
        """
        return self._execute(self.chain, request_type, "59faf338", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#48)
        """
        ...

    @overload
    def test_StorageMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#48)
        """
        ...

    @overload
    def test_StorageMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#48)
        """
        ...

    @overload
    def test_StorageMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#48)
        """
        ...

    def test_StorageMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#48)
        """
        return self._execute(self.chain, request_type, "71e0a254", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#54)
        """
        ...

    @overload
    def test_StorageMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#54)
        """
        ...

    @overload
    def test_StorageMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#54)
        """
        ...

    @overload
    def test_StorageMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#54)
        """
        ...

    def test_StorageMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#54)
        """
        return self._execute(self.chain, request_type, "e994e0b5", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#60)
        """
        ...

    @overload
    def test_StorageDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#60)
        """
        ...

    @overload
    def test_StorageDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#60)
        """
        ...

    @overload
    def test_StorageDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#60)
        """
        ...

    def test_StorageDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#60)
        """
        return self._execute(self.chain, request_type, "8499d1ab", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#67)
        """
        ...

    @overload
    def test_StorageCheckedWriteDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#67)
        """
        ...

    @overload
    def test_StorageCheckedWriteDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#67)
        """
        ...

    @overload
    def test_StorageCheckedWriteDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#67)
        """
        ...

    def test_StorageCheckedWriteDeepMap(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#67)
        """
        return self._execute(self.chain, request_type, "a299aa5e", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#73)
        """
        ...

    @overload
    def test_StorageDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#73)
        """
        ...

    @overload
    def test_StorageDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#73)
        """
        ...

    @overload
    def test_StorageDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#73)
        """
        ...

    def test_StorageDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#73)
        """
        return self._execute(self.chain, request_type, "392e660a", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#82)
        """
        ...

    @overload
    def test_StorageDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#82)
        """
        ...

    @overload
    def test_StorageDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#82)
        """
        ...

    @overload
    def test_StorageDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#82)
        """
        ...

    def test_StorageDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#82)
        """
        return self._execute(self.chain, request_type, "ab861d24", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#91)
        """
        ...

    @overload
    def test_StorageCheckedWriteDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#91)
        """
        ...

    @overload
    def test_StorageCheckedWriteDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#91)
        """
        ...

    @overload
    def test_StorageCheckedWriteDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#91)
        """
        ...

    def test_StorageCheckedWriteDeepMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#91)
        """
        return self._execute(self.chain, request_type, "3b61a950", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#100)
        """
        ...

    @overload
    def test_StorageCheckedWriteDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#100)
        """
        ...

    @overload
    def test_StorageCheckedWriteDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#100)
        """
        ...

    @overload
    def test_StorageCheckedWriteDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#100)
        """
        ...

    def test_StorageCheckedWriteDeepMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#100)
        """
        return self._execute(self.chain, request_type, "b4747b20", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#109)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#109)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#109)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#109)
        """
        ...

    def test_StorageCheckedWriteMapStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#109)
        """
        return self._execute(self.chain, request_type, "495f0741", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#116)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#116)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#116)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#116)
        """
        ...

    def test_StorageCheckedWriteMapStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#116)
        """
        return self._execute(self.chain, request_type, "26d97d0b", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#123)
        """
        ...

    @overload
    def test_StorageStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#123)
        """
        ...

    @overload
    def test_StorageStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#123)
        """
        ...

    @overload
    def test_StorageStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#123)
        """
        ...

    def test_StorageStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#123)
        """
        return self._execute(self.chain, request_type, "f73aa19a", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#128)
        """
        ...

    @overload
    def test_StorageStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#128)
        """
        ...

    @overload
    def test_StorageStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#128)
        """
        ...

    @overload
    def test_StorageStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#128)
        """
        ...

    def test_StorageStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#128)
        """
        return self._execute(self.chain, request_type, "4acaea91", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#133)
        """
        ...

    @overload
    def test_StorageCheckedWriteStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#133)
        """
        ...

    @overload
    def test_StorageCheckedWriteStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#133)
        """
        ...

    @overload
    def test_StorageCheckedWriteStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#133)
        """
        ...

    def test_StorageCheckedWriteStructA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#133)
        """
        return self._execute(self.chain, request_type, "6dc33251", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#140)
        """
        ...

    @overload
    def test_StorageCheckedWriteStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#140)
        """
        ...

    @overload
    def test_StorageCheckedWriteStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#140)
        """
        ...

    @overload
    def test_StorageCheckedWriteStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#140)
        """
        ...

    def test_StorageCheckedWriteStructB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#140)
        """
        return self._execute(self.chain, request_type, "89e6cfe4", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageMapAddrFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#147)
        """
        ...

    @overload
    def test_StorageMapAddrFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#147)
        """
        ...

    @overload
    def test_StorageMapAddrFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#147)
        """
        ...

    @overload
    def test_StorageMapAddrFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#147)
        """
        ...

    def test_StorageMapAddrFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#147)
        """
        return self._execute(self.chain, request_type, "6c428ef8", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageMapAddrRoot(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#152)
        """
        ...

    @overload
    def test_StorageMapAddrRoot(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#152)
        """
        ...

    @overload
    def test_StorageMapAddrRoot(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#152)
        """
        ...

    @overload
    def test_StorageMapAddrRoot(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#152)
        """
        ...

    def test_StorageMapAddrRoot(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#152)
        """
        return self._execute(self.chain, request_type, "038cd192", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageMapUintFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#161)
        """
        ...

    @overload
    def test_StorageMapUintFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#161)
        """
        ...

    @overload
    def test_StorageMapUintFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#161)
        """
        ...

    @overload
    def test_StorageMapUintFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#161)
        """
        ...

    def test_StorageMapUintFound(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#161)
        """
        return self._execute(self.chain, request_type, "d8c172bf", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteMapUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#166)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#166)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#166)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#166)
        """
        ...

    def test_StorageCheckedWriteMapUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#166)
        """
        return self._execute(self.chain, request_type, "f2da1130", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteMapAddr(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#171)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapAddr(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#171)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapAddr(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#171)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapAddr(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#171)
        """
        ...

    def test_StorageCheckedWriteMapAddr(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#171)
        """
        return self._execute(self.chain, request_type, "6d422be6", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteMapBool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#176)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapBool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#176)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapBool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#176)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapBool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#176)
        """
        ...

    def test_StorageCheckedWriteMapBool(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#176)
        """
        return self._execute(self.chain, request_type, "4def64da", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_StorageCheckedWriteMapPacked(self, addr: Union[Account, Address], value_: uint128, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#181)

        Args:
            addr: address
            value_: uint128
        """
        ...

    @overload
    def testFuzz_StorageCheckedWriteMapPacked(self, addr: Union[Account, Address], value_: uint128, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#181)

        Args:
            addr: address
            value_: uint128
        """
        ...

    @overload
    def testFuzz_StorageCheckedWriteMapPacked(self, addr: Union[Account, Address], value_: uint128, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#181)

        Args:
            addr: address
            value_: uint128
        """
        ...

    @overload
    def testFuzz_StorageCheckedWriteMapPacked(self, addr: Union[Account, Address], value_: uint128, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#181)

        Args:
            addr: address
            value_: uint128
        """
        ...

    def testFuzz_StorageCheckedWriteMapPacked(self, addr: Union[Account, Address], value_: uint128, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#181)

        Args:
            addr: address
            value_: uint128
        """
        return self._execute(self.chain, request_type, "2f644e92", [addr, value_], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageCheckedWriteMapPackedFullSuccess(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#191)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapPackedFullSuccess(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#191)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapPackedFullSuccess(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#191)
        """
        ...

    @overload
    def test_StorageCheckedWriteMapPackedFullSuccess(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#191)
        """
        ...

    def test_StorageCheckedWriteMapPackedFullSuccess(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#191)
        """
        return self._execute(self.chain, request_type, "05a7c0b4", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_RevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#201)
        """
        ...

    @overload
    def test_RevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#201)
        """
        ...

    @overload
    def test_RevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#201)
        """
        ...

    @overload
    def test_RevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#201)
        """
        ...

    def test_RevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#201)
        """
        return self._execute(self.chain, request_type, "ebefd727", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_StorageNativePack(self, val1: uint248, val2: uint248, boolVal1: bool, boolVal2: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#208)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#208)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#208)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#208)

        Args:
            val1: uint248
            val2: uint248
            boolVal1: bool
            boolVal2: bool
        """
        ...

    def testFuzz_StorageNativePack(self, val1: uint248, val2: uint248, boolVal1: bool, boolVal2: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#208)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#220)
        """
        ...

    @overload
    def test_StorageReadBytes32(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#220)
        """
        ...

    @overload
    def test_StorageReadBytes32(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#220)
        """
        ...

    @overload
    def test_StorageReadBytes32(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#220)
        """
        ...

    def test_StorageReadBytes32(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#220)
        """
        return self._execute(self.chain, request_type, "379a42ae", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageReadBool_False(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#225)
        """
        ...

    @overload
    def test_StorageReadBool_False(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#225)
        """
        ...

    @overload
    def test_StorageReadBool_False(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#225)
        """
        ...

    @overload
    def test_StorageReadBool_False(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#225)
        """
        ...

    def test_StorageReadBool_False(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#225)
        """
        return self._execute(self.chain, request_type, "edf3c69a", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageReadBool_True(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#230)
        """
        ...

    @overload
    def test_StorageReadBool_True(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#230)
        """
        ...

    @overload
    def test_StorageReadBool_True(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#230)
        """
        ...

    @overload
    def test_StorageReadBool_True(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#230)
        """
        ...

    def test_StorageReadBool_True(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#230)
        """
        return self._execute(self.chain, request_type, "d8e24c43", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_RevertIf_ReadingNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#235)
        """
        ...

    @overload
    def test_RevertIf_ReadingNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#235)
        """
        ...

    @overload
    def test_RevertIf_ReadingNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#235)
        """
        ...

    @overload
    def test_RevertIf_ReadingNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#235)
        """
        ...

    def test_RevertIf_ReadingNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#235)
        """
        return self._execute(self.chain, request_type, "ed60529b", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def readNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#240)
        """
        ...

    @overload
    def readNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#240)
        """
        ...

    @overload
    def readNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#240)
        """
        ...

    @overload
    def readNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#240)
        """
        ...

    def readNonBoolValue(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#240)
        """
        return self._execute(self.chain, request_type, "52e52ac6", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageReadAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#244)
        """
        ...

    @overload
    def test_StorageReadAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#244)
        """
        ...

    @overload
    def test_StorageReadAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#244)
        """
        ...

    @overload
    def test_StorageReadAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#244)
        """
        ...

    def test_StorageReadAddress(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#244)
        """
        return self._execute(self.chain, request_type, "e1b943a2", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageReadUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#249)
        """
        ...

    @overload
    def test_StorageReadUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#249)
        """
        ...

    @overload
    def test_StorageReadUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#249)
        """
        ...

    @overload
    def test_StorageReadUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#249)
        """
        ...

    def test_StorageReadUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#249)
        """
        return self._execute(self.chain, request_type, "f15d536f", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StorageReadInt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#254)
        """
        ...

    @overload
    def test_StorageReadInt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#254)
        """
        ...

    @overload
    def test_StorageReadInt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#254)
        """
        ...

    @overload
    def test_StorageReadInt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#254)
        """
        ...

    def test_StorageReadInt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#254)
        """
        return self._execute(self.chain, request_type, "9792466b", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_Packed(self, val: uint256, elemToGet: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#259)

        Args:
            val: uint256
            elemToGet: uint8
        """
        ...

    @overload
    def testFuzz_Packed(self, val: uint256, elemToGet: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#259)

        Args:
            val: uint256
            elemToGet: uint8
        """
        ...

    @overload
    def testFuzz_Packed(self, val: uint256, elemToGet: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#259)

        Args:
            val: uint256
            elemToGet: uint8
        """
        ...

    @overload
    def testFuzz_Packed(self, val: uint256, elemToGet: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#259)

        Args:
            val: uint256
            elemToGet: uint8
        """
        ...

    def testFuzz_Packed(self, val: uint256, elemToGet: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#259)

        Args:
            val: uint256
            elemToGet: uint8
        """
        return self._execute(self.chain, request_type, "599377dd", [val, elemToGet], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_Packed2(self, nvars: uint256, seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#301)

        Args:
            nvars: uint256
            seed: uint256
        """
        ...

    @overload
    def testFuzz_Packed2(self, nvars: uint256, seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#301)

        Args:
            nvars: uint256
            seed: uint256
        """
        ...

    @overload
    def testFuzz_Packed2(self, nvars: uint256, seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#301)

        Args:
            nvars: uint256
            seed: uint256
        """
        ...

    @overload
    def testFuzz_Packed2(self, nvars: uint256, seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#301)

        Args:
            nvars: uint256
            seed: uint256
        """
        ...

    def testFuzz_Packed2(self, nvars: uint256, seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#301)

        Args:
            nvars: uint256
            seed: uint256
        """
        return self._execute(self.chain, request_type, "6cc48782", [nvars, seed], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testEdgeCaseArray(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#351)
        """
        ...

    @overload
    def testEdgeCaseArray(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#351)
        """
        ...

    @overload
    def testEdgeCaseArray(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#351)
        """
        ...

    @overload
    def testEdgeCaseArray(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#351)
        """
        ...

    def testEdgeCaseArray(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#351)
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
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#357)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'contract StorageTest', 'name': 'test_', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\x9c\x95U\xb1\xe3\x10.<\xf4\x8fB}y\xcbg\x8f]\x9b\xd1\xed\n\xd5t8\x94a\xe2U\xf9Qp\xed': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'who', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes4', 'name': 'fsig', 'type': 'bytes4'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'keysHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'slot', 'type': 'uint256'}], 'name': 'SlotFound', 'type': 'event'}, b'\x08\x0f\xc4\xa9f \xc4F.p[#\xf3FA?\xe3yk\xb6<o\x8d\x85\x91\xba\xec\x0e#\x15w\xa5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'who', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'slot', 'type': 'uint256'}], 'name': 'WARNING_UninitedSlot', 'type': 'event'}, b'\xfcZ\xec+': {'inputs': [], 'name': 'expectRevertStorageConst', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":41229,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"stdstore","offset":0,"slot":0,"type":"t_struct(StdStorage)8017_storage"},{"astId":41232,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"test","offset":0,"slot":8,"type":"t_contract(StorageTest)41624"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_contract(StorageTest)41624":{"encoding":"inplace","label":"contract StorageTest","numberOfBytes":20},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage))"},"t_mapping(t_bytes32,t_struct(FindData)7992_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)7992_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)7992_storage)"},"t_struct(FindData)7992_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":7985,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":7987,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":7989,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":7991,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(StdStorage)8017_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":8001,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage)))"},{"astId":8004,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":8006,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":8008,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":8010,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":8012,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":8014,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":8016,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTestTarget","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "608034607057601f61109338819003918201601f19168301916001600160401b03831184841017607457808492602094604052833981010312607057516001600160a01b03811690819003607057600880546001600160a01b03191691909117905560405161100a90816100898239f35b5f80fd5b634e487b7160e01b5f52604160045260245ffdfe60806040526004361015610011575f80fd5b5f3560e01c63fc5aec2b14610024575f80fd5b3461008e575f36600319011261008e5760018060a01b036008541660018060a01b0319600454161760045560076020604051610061604082610092565b8281520166636f6e7374282960c81b81522060e01c63ffffffff19600254161760025561008c61018b565b005b5f80fd5b90601f8019910116810190811067ffffffffffffffff8211176100b457604052565b634e487b7160e01b5f52604160045260245ffd5b67ffffffffffffffff81116100b457601f01601f191660200190565b60209291908391805192839101825e019081520190565b9080601f8301121561008e5781519167ffffffffffffffff83116100b4578260051b906040519361012f6020840186610092565b845260208085019282010192831161008e57602001905b8282106101535750505090565b8151815260209182019101610146565b80518210156101775760209160051b010190565b634e487b7160e01b5f52603260045260245ffd5b6004546002546003546001600160a01b03909216915f9160e01b6101ae83610a9c565b90845f525f60205260405f209063ffffffff60e01b1690815f5260205260405f2060405160208101906101f4816101e68888866100e4565b03601f198101835282610092565b5190205f5260205260ff600360405f20015416610a1b575f516020610fb55f395f51905f523b1561008e5760405163266cf10960e01b81525f81600481835f516020610fb55f395f51905f525af18015610a10576109fb575b5061025784610cf3565b90506040516365bc948160e01b81528660048201528581602481835f516020610fb55f395f51905f525af19081156109f0578691610982575b5080518061030257608460405162461bcd60e51b815260206004820152604060248201527f73746453746f726167652066696e642853746453746f72616765293a204e6f2060448201527f73746f726167652075736520646574656374656420666f72207461726765742e6064820152fd5b801561096e579061034e915f190190602061031d8383610163565b51604051630667f9d760e41b81526001600160a01b038c166004820152602481019190915293849081906044820190565b03815f516020610fb55f395f51905f525afa928315610963578893610930575b5082156108f1575b6103808282610163565b5160048054604051630667f9d760e41b81526001600160a01b03909116918101829052602481018390529091906020816044815f516020610fb55f395f51905f525afa9081156108e6578b916108b5575b506103db8b610cf3565b91909382155f146108ae575f19905b5f516020610fb55f395f51905f523b1561089557848e9161041f60405194859384936370ca10bb60e01b855260048501610e18565b0381835f516020610fb55f395f51905f525af1801561081257908d91610899575b5061044a90610cf3565b600454909491506001600160a01b03165f516020610fb55f395f51905f523b1561089557908d9161048f60405194859384936370ca10bb60e01b855260048501610e18565b0381835f516020610fb55f395f51905f525af1801561088a57908c91610871575b505082610866575b50501561085f578793889360ff600654166106eb575b6001858701610100031b5f1901851b16841c81036106e2575090610554917f9c9555b1e3102e3cf48f427d79cb678f5d9bd1ed0ad574389461e255f95170ed60808b896101e66105298d6040519283916020830195866100e4565b5190206105368686610163565b51906040519283528a602084015260408301526060820152a1610163565b5190604051916080830183811067ffffffffffffffff8211176106ce57906003939291604052825260208201938452604082019081526060820193600185528989528860205260408920868a526020526040892060405160208101906105bf816101e68d8d866100e4565b5190208a526020526040892092518355516001830155516002820155019051151560ff801983541691161790558484528360205260408420818552602052604084206040516020810190610618816101e68888866100e4565b519020855260205260ff600360408620015416156106715760409461063c85610c22565b8452836020528484209084526020526101e66106658585209386519283916020830195866100e4565b51902082526020522090565b60405162461bcd60e51b815260206004820152602f60248201527f73746453746f726167652066696e642853746453746f72616765293a20536c6f60448201526e3a143994903737ba103337bab7321760891b6064820152608490fd5b634e487b7160e01b89526041600452602489fd5b93509150610302565b945061073993506106fc8383610163565b5160048054604051630667f9d760e41b81526001600160a01b03909116918101919091526024810182905290959094602090869081906044820190565b03815f516020610fb55f395f51905f525afa948515610854578a95610821575b50610764868b610e36565b959096610771818d610f00565b60045490939192906001600160a01b03165f516020610fb55f395f51905f523b1561081d57908e916107b760405194859384936370ca10bb60e01b855260048501610e18565b0381835f516020610fb55f395f51905f525af1801561081257908d916107f9575b5050876107f1575b5094956104ce575093509150610302565b96505f6107e0565b8161080391610092565b61080e578b5f6107d8565b8b80fd5b6040513d8f823e3d90fd5b8e80fd5b9094506020813d821161084c575b8161083c60209383610092565b8101031261008e5751935f610759565b3d915061082f565b6040513d8c823e3d90fd5b9150610302565b141590505f806104b8565b8161087b91610092565b610886578a5f6104b0565b8a80fd5b6040513d8e823e3d90fd5b8d80fd5b816108a391610092565b61080e578b5f610440565b8c906103ea565b90506020813d82116108de575b816108cf60209383610092565b8101031261008e57515f6103d1565b3d91506108c2565b6040513d8d823e3d90fd5b7f080fc4a96620c4462e705b23f346413fe3796bb63c6f8d8591baec0e231577a5604061091e8484610163565b518151908c82526020820152a1610376565b9092506020813d821161095b575b8161094b60209383610092565b8101031261008e5751915f61036e565b3d915061093e565b6040513d8a823e3d90fd5b634e487b7160e01b87526011600452602487fd5b90503d8087833e6109938183610092565b81016040828203126109ec57815167ffffffffffffffff81116109e857816109bc9184016100fb565b9160208101519067ffffffffffffffff82116109e4576109dd9291016100fb565b505f610290565b8880fd5b8780fd5b8680fd5b6040513d88823e3d90fd5b610a089194505f90610092565b5f925f61024d565b6040513d5f823e3d90fd5b9193909250610a295f610c22565b5f525f60205260405f20905f526020526101e6610a5560405f20936040519283916020830195866100e4565b5190205f5260205260405f2090565b90600182811c92168015610a92575b6020831014610a7e57565b634e487b7160e01b5f52602260045260245ffd5b91607f1691610a73565b60078101908154610aac81610a64565b610b825750600191500190604051808360208295549384815201905f5260205f20925f5b818110610b69575050610ae592500383610092565b81518060051b9080820460201490151715610b5557610b03816100c8565b90610b116040519283610092565b808252610b20601f19916100c8565b013660208301375f5b8351811015610b505780610b3f60019286610163565b5160208260051b8501015201610b29565b509150565b634e487b7160e01b5f52601160045260245ffd5b8454835260019485019487945060209093019201610ad0565b905060405180925f90610b9484610a64565b8084529360018116908115610c005750600114610bbc575b50610bb992500382610092565b90565b90505f9291925260205f20905f915b818310610be4575050906020610bb9928201015f610bac565b6020919350806001915483858801015201910190918392610bcb565b905060209250610bb994915060ff191682840152151560051b8201015f610bac565b6004810180546001600160a01b031916905560028101805463ffffffff191690556001810180545f82559081610cd1575b50506007905f60038201556006810160ff1981541690550190610c768254610a64565b9182610c8157509050565b601f8311600114610c93575f90559050565b5f8181526020812093601f0160051c5f1901905b818110610cc15750505f9192508082528160208120915555565b6001905f82828801015501610ca7565b5f5260205f205f5b828110610ce65750610c53565b5f82820155600101610cd9565b905f806020600285015460e01b610d436024610d0e88610a9c565b6040519485918183019563ffffffff60e01b1686528051918291018484015e810186838201520301601f198101845283610092565b60048601549151916001600160a01b03165afa3d15610e0e5760033d93610d69856100c8565b94610d776040519687610092565b85523d5f602087013e5b0154600581901b906001600160fb1b03811603610b55575f938051602081115f14610e0857506020905b5f925b828410610dbd57505050509190565b90919295868201808311610b5557835181101561017757830160200151600388901b91906001600160f81b031916881560088a8504141715610b55576001921c179601929190610dae565b90610dab565b6003606093610d81565b604091949392606082019560018060a01b0316825260208201520152565b91905f5b6101008110610e4d57505090505f905f90565b8060ff0360ff8111610b55576004850154600190911b906001600160a01b03165f516020610fb55f395f51905f523b1561008e57835f91610ea260405194859384936370ca10bb60e01b855260048501610e18565b0381835f516020610fb55f395f51905f525af18015610a1057610ef0575b50610eca84610cf3565b81610ee6575b50610edd57600101610e3a565b92505060019190565b905015155f610ed0565b5f610efa91610092565b5f610ec0565b91905f5b6101008110610f1757505090505f905f90565b60048401546001821b906001600160a01b03165f516020610fb55f395f51905f523b1561008e57835f91610f5f60405194859384936370ca10bb60e01b855260048501610e18565b0381835f516020610fb55f395f51905f525af18015610a1057610fa4575b50610f8784610cf3565b81610f9a575b50610edd57600101610f04565b905015155f610f8d565b5f610fae91610092565b5f610f7d56fe0000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da2646970667358221220c65f166fc3f6c972570d7c44a8fce87fe2b6805aac0751ac4a86249ee1259f3764736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, test_: StorageTest, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#363)

        Args:
            test_: contract StorageTest
        """
        ...

    @overload
    @classmethod
    def deploy(cls, test_: StorageTest, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> StorageTestTarget:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#363)

        Args:
            test_: contract StorageTest
        """
        ...

    @overload
    @classmethod
    def deploy(cls, test_: StorageTest, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#363)

        Args:
            test_: contract StorageTest
        """
        ...

    @overload
    @classmethod
    def deploy(cls, test_: StorageTest, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#363)

        Args:
            test_: contract StorageTest
        """
        ...

    @overload
    @classmethod
    def deploy(cls, test_: StorageTest, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[StorageTestTarget]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#363)

        Args:
            test_: contract StorageTest
        """
        ...

    @classmethod
    def deploy(cls, test_: StorageTest, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, StorageTestTarget, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[StorageTestTarget]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#363)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#367)
        """
        ...

    @overload
    def expectRevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#367)
        """
        ...

    @overload
    def expectRevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#367)
        """
        ...

    @overload
    def expectRevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#367)
        """
        ...

    def expectRevertStorageConst(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#367)
        """
        return self._execute(self.chain, request_type, "fc5aec2b", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

StorageTestTarget.expectRevertStorageConst.selector = bytes4(b'\xfcZ\xec+')
class StorageTest(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#372)
    """
    _abi = {'constructor': {'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\x15\xe8\xb3E': {'inputs': [], 'name': 'basic', 'outputs': [{'internalType': 'uint256', 'name': 'a', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'b', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b';\x80\xa7\x93': {'inputs': [], 'name': 'const', 'outputs': [{'internalType': 'bytes32', 'name': 't', 'type': 'bytes32'}], 'stateMutability': 'pure', 'type': 'function'}, b'\x8c\xd8\x15m': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'deep_map', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x03\x10\xc0`': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'deep_map_struct', 'outputs': [{'internalType': 'uint256', 'name': 'a', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'b', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe9.\x9d\xc4': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'edgeCaseArray', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'&|J\xe4': {'inputs': [], 'name': 'exists', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x9ey6\xe6': {'inputs': [], 'name': 'extra_sload', 'outputs': [{'internalType': 'bytes32', 'name': 't', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1a\xa8D\xb4': {'inputs': [{'internalType': 'uint256', 'name': 'size', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'offset', 'type': 'uint256'}], 'name': 'getRandomPacked', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'a\xa9ui': {'inputs': [{'internalType': 'uint8', 'name': 'shifts', 'type': 'uint8'}, {'internalType': 'uint8[]', 'name': 'shiftSizes', 'type': 'uint8[]'}, {'internalType': 'uint8', 'name': 'elem', 'type': 'uint8'}], 'name': 'getRandomPacked', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xae\xf6\xd4\xb1': {'inputs': [], 'name': 'hidden', 'outputs': [{'internalType': 'bytes32', 'name': 't', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa7>@\xcc': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'map_addr', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x8ckEQ': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'map_bool', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\\#\xfe\x9e': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'map_packed', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'PD)\xbf': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'map_struct', 'outputs': [{'internalType': 'uint256', 'name': 'a', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'b', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'jV\xc3\xd4': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'map_uint', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'A\xb6\xed\xb2': {'inputs': [{'internalType': 'address', 'name': 'who', 'type': 'address'}], 'name': 'read_struct_lower', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'>\xae"\x18': {'inputs': [{'internalType': 'address', 'name': 'who', 'type': 'address'}], 'name': 'read_struct_upper', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x19q\xf0\x0b': {'inputs': [{'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'size', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'offset', 'type': 'uint256'}], 'name': 'setRandomPacking', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xaaF8&': {'inputs': [{'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}], 'name': 'setRandomPacking', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'y\xda~M': {'inputs': [], 'name': 'tA', 'outputs': [{'internalType': 'uint248', 'name': '', 'type': 'uint248'}], 'stateMutability': 'view', 'type': 'function'}, b'W5\x1cE': {'inputs': [], 'name': 'tB', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xebS\xf9\x90': {'inputs': [], 'name': 'tC', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe4\xc6*\x11': {'inputs': [], 'name': 'tD', 'outputs': [{'internalType': 'uint248', 'name': '', 'type': 'uint248'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb7\xe1\x9e)': {'inputs': [], 'name': 'tE', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\x08\xf2:\xad': {'inputs': [], 'name': 'tF', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe5\xed\x1e\xfe': {'inputs': [], 'name': 'tG', 'outputs': [{'internalType': 'int256', 'name': '', 'type': 'int256'}], 'stateMutability': 'view', 'type': 'function'}, b'O\x87\xae\xb7': {'inputs': [], 'name': 'tH', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":41265,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"exists","offset":0,"slot":0,"type":"t_uint256"},{"astId":41269,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"map_addr","offset":0,"slot":1,"type":"t_mapping(t_address,t_uint256)"},{"astId":41273,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"map_uint","offset":0,"slot":2,"type":"t_mapping(t_uint256,t_uint256)"},{"astId":41277,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"map_packed","offset":0,"slot":3,"type":"t_mapping(t_address,t_uint256)"},{"astId":41282,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"map_struct","offset":0,"slot":4,"type":"t_mapping(t_address,t_struct(UnpackedStruct)41313_storage)"},{"astId":41288,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"deep_map","offset":0,"slot":5,"type":"t_mapping(t_address,t_mapping(t_address,t_uint256))"},{"astId":41295,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"deep_map_struct","offset":0,"slot":6,"type":"t_mapping(t_address,t_mapping(t_address,t_struct(UnpackedStruct)41313_storage))"},{"astId":41298,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"basic","offset":0,"slot":7,"type":"t_struct(UnpackedStruct)41313_storage"},{"astId":41300,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"tA","offset":0,"slot":9,"type":"t_uint248"},{"astId":41302,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"tB","offset":31,"slot":9,"type":"t_bool"},{"astId":41305,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"tC","offset":0,"slot":10,"type":"t_bool"},{"astId":41308,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"tD","offset":1,"slot":10,"type":"t_uint248"},{"astId":41317,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"map_bool","offset":0,"slot":11,"type":"t_mapping(t_address,t_bool)"},{"astId":41320,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"tE","offset":0,"slot":12,"type":"t_bytes32"},{"astId":41326,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"tF","offset":0,"slot":13,"type":"t_address"},{"astId":41333,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"tG","offset":0,"slot":14,"type":"t_int256"},{"astId":41336,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"tH","offset":0,"slot":15,"type":"t_bool"},{"astId":41343,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"tI","offset":0,"slot":16,"type":"t_bytes32"},{"astId":41345,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"randomPacking","offset":0,"slot":17,"type":"t_uint256"},{"astId":41352,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"edgeCaseArray","offset":0,"slot":18,"type":"t_array(t_uint256)dyn_storage"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_uint256)dyn_storage":{"encoding":"dynamic_array","label":"uint256[]","numberOfBytes":32,"base":"t_uint256"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_int256":{"encoding":"inplace","label":"int256","numberOfBytes":32},"t_mapping(t_address,t_bool)":{"encoding":"mapping","label":"mapping(address => bool)","numberOfBytes":32,"key":"t_address","value":"t_bool"},"t_mapping(t_address,t_mapping(t_address,t_struct(UnpackedStruct)41313_storage))":{"encoding":"mapping","label":"mapping(address => mapping(address => struct StorageTest.UnpackedStruct))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_address,t_struct(UnpackedStruct)41313_storage)"},"t_mapping(t_address,t_mapping(t_address,t_uint256))":{"encoding":"mapping","label":"mapping(address => mapping(address => uint256))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_address,t_uint256)"},"t_mapping(t_address,t_struct(UnpackedStruct)41313_storage)":{"encoding":"mapping","label":"mapping(address => struct StorageTest.UnpackedStruct)","numberOfBytes":32,"key":"t_address","value":"t_struct(UnpackedStruct)41313_storage"},"t_mapping(t_address,t_uint256)":{"encoding":"mapping","label":"mapping(address => uint256)","numberOfBytes":32,"key":"t_address","value":"t_uint256"},"t_mapping(t_uint256,t_uint256)":{"encoding":"mapping","label":"mapping(uint256 => uint256)","numberOfBytes":32,"key":"t_uint256","value":"t_uint256"},"t_struct(UnpackedStruct)41313_storage":{"encoding":"inplace","label":"struct StorageTest.UnpackedStruct","numberOfBytes":64,"members":[{"astId":41310,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"a","offset":0,"slot":0,"type":"t_uint256"},{"astId":41312,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol:StorageTest","label":"b","offset":0,"slot":1,"type":"t_uint256"}]},"t_uint248":{"encoding":"inplace","label":"uint248","numberOfBytes":31},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "6080604052346101755760015f819055610100600a5561133760f01b600c55600d80546001600160a01b031916610539179055600160ff1b600e55600f805460ff19169091179055600161ecc960f01b03601055604051606081016001600160401b0381118282101761011c57604052600381526003602082015260036040820152601254600360125580600310610147575b5060125f5260205f20905f5b6003811061013057604080519081016001600160401b0381118282101761011c57610539916020916040528281520152610539600755610539600855335f52600360205270010000000000000000000000000000000160405f20556105395f526003602052600160801b60405f20556040516109b5908161017a8239f35b634e487b7160e01b5f52604160045260245ffd5b600190602060ff845116930192818501550161009e565b60125f5260205f209060021901905f5b828110610165575050610092565b5f82820160030155600101610157565b5f80fdfe60806040526004361015610011575f80fd5b5f3560e01c80630310c060146101c457806308f23aad146101bf57806315e8b345146101ba5780631971f00b146101b55780631aa844b4146101b0578063267c4ae4146101ab5780633b80a793146101a65780633eae2218146101a157806341b6edb21461019c5780634f87aeb714610197578063504429bf1461019257806357351c451461018d5780635c23fe9e1461018857806361a97569146101835780636a56c3d41461017e57806379da7e4d146101795780638c6b4551146101745780638cd8156d1461016f5780639e7936e61461016a578063a73e40cc14610165578063aa46382614610160578063aef6d4b11461015b578063b7e19e2914610156578063e4c62a1114610151578063e5ed1efe1461014c578063e92e9dc4146101475763eb53f99014610142575f80fd5b6107f8565b6107a8565b61078b565b61076b565b61074e565b610712565b6106f9565b6106c1565b61069a565b610643565b610606565b6105de565b6105b4565b6104de565b610464565b610442565b6103f1565b6103cf565b61038f565b610354565b610334565b610318565b6102e9565b6102b6565b61028e565b610266565b6101f9565b600435906001600160a01b03821682036101df57565b5f80fd5b602435906001600160a01b03821682036101df57565b346101df5760403660031901126101df576102466102156101c9565b61021d6101e3565b9060018060a01b03165f52600660205260405f209060018060a01b03165f5260205260405f2090565b8054600190910154604080519283526020830191909152819081015b0390f35b346101df575f3660031901126101df57600d546040516001600160a01b039091168152602090f35b346101df575f3660031901126101df5760075460085460408051928352602083019190915290f35b346101df5760603660031901126101df576011805460016024351b5f190160443590811b1990911660043590911b179055005b346101df5760403660031901126101df576011546040516024359190911c60016004351b5f1901168152602090f35b346101df575f3660031901126101df5760205f54604051908152f35b346101df575f3660031901126101df5760405161133760f01b8152602090f35b346101df5760203660031901126101df576001600160a01b036103756101c9565b165f526003602052602060405f205460801c604051908152f35b346101df5760203660031901126101df576001600160a01b036103b06101c9565b165f526003602052602060018060801b0360405f205416604051908152f35b346101df575f3660031901126101df57602060ff600f54166040519015158152f35b346101df5760203660031901126101df576001600160a01b036104126101c9565b165f52600460205260405f2060018154910154906102626040519283928360209093929193604081019481520152565b346101df575f3660031901126101df57602060095460f81c6040519015158152f35b346101df5760203660031901126101df576001600160a01b036104856101c9565b165f526003602052602060405f2054604051908152f35b6004359060ff821682036101df57565b6044359060ff821682036101df57565b359060ff821682036101df57565b634e487b7160e01b5f52604160045260245ffd5b346101df5760603660031901126101df576104f761049c565b60243567ffffffffffffffff81116101df57366023820112156101df5780600401359067ffffffffffffffff82116105af578160051b60405192601f19603f830116840184811067ffffffffffffffff8211176105af57604052835260246020840191830101913683116101df57602401905b8282106105975761026261058786866105816104ac565b916108ac565b6040519081529081906020820190565b602080916105a4846104bc565b81520191019061056a565b6104ca565b346101df5760203660031901126101df576004355f526002602052602060405f2054604051908152f35b346101df575f3660031901126101df576009546040516001600160f81b039091168152602090f35b346101df5760203660031901126101df576001600160a01b036106276101c9565b165f52600b602052602060ff60405f2054166040519015158152f35b346101df5760403660031901126101df5760206106916106616101c9565b6106696101e3565b6001600160a01b039182165f9081526005855260408082209290931681526020919091522090565b54604051908152f35b346101df575f3660031901126101df575f808080600c545afa506020601054604051908152f35b346101df5760203660031901126101df576001600160a01b036106e26101c9565b165f526001602052602060405f2054604051908152f35b346101df5760203660031901126101df57600435601155005b346101df575f3660031901126101df5760207fb27fb258786eae8f9ffde06a5bfd55f5193cb73bd64e533d5d75fd7cb46652ff54604051908152f35b346101df575f3660031901126101df576020600c54604051908152f35b346101df575f3660031901126101df576020600a5460081c604051908152f35b346101df575f3660031901126101df576020600e54604051908152f35b346101df5760203660031901126101df576004356012548110156101df5760125f527fbb8a6a4669ba250d26cd7a459eca9d215f8307e33aebe50379bc5a3617ec34440154604051908152602090f35b346101df575f3660031901126101df57602060ff600a54166040519015158152f35b1561082157565b60405162461bcd60e51b815260206004820152600560248201526421656c656d60d81b6044820152606490fd5b80518210156108625760209160051b010190565b634e487b7160e01b5f52603260045260245ffd5b634e487b7160e01b5f52601160045260245ffd5b9190820180921161089757565b610876565b6101000390610100821161089757565b929160ff806108bf92169416841061081a565b5f905f935f925b82518410156109395781841015610909576109006001916108fa6108f46108ed888861084e565b5160ff1690565b60ff1690565b9061088a565b935b01926108c6565b9280820361091a575b600190610902565b946109316001916108fa6108f46108ed8a8861084e565b959050610912565b9061097b935061096a8661096561095f6108f46108ed6108fa9661096f999c9b9c61084e565b8561088a565b61088a565b61089c565b91601154831b9261088a565b1c9056fea2646970667358221220a5b91f9f4413b16d57ef507d7fb64b65d823919ca9ca4a91cab9ca25e1c9c08564736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#406)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> StorageTest:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#406)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#406)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#406)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[StorageTest]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#406)
        """
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, StorageTest, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[StorageTest]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#406)
        """
        return cls._deploy(request_type, [], return_tx, StorageTest, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class UnpackedStruct:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#388)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#373)

        Returns:
            exists: uint256
        """
        ...

    @overload
    def exists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#373)

        Returns:
            exists: uint256
        """
        ...

    @overload
    def exists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#373)

        Returns:
            exists: uint256
        """
        ...

    @overload
    def exists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#373)

        Returns:
            exists: uint256
        """
        ...

    def exists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#373)

        Returns:
            exists: uint256
        """
        return self._execute(self.chain, request_type, "267c4ae4", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def map_addr(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#374)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def map_addr(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#374)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def map_addr(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#374)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def map_addr(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#374)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    def map_addr(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#374)

        Args:
            key0: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "a73e40cc", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def map_uint(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#375)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def map_uint(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#375)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def map_uint(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#375)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def map_uint(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#375)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    def map_uint(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#375)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "6a56c3d4", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def map_packed(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#376)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def map_packed(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#376)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def map_packed(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#376)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def map_packed(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#376)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    def map_packed(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#376)

        Args:
            key0: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "5c23fe9e", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def map_struct(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> StorageTest.UnpackedStruct:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#377)

        Args:
            key0: address
        Returns:
            struct StorageTest.UnpackedStruct
        """
        ...

    @overload
    def map_struct(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#377)

        Args:
            key0: address
        Returns:
            struct StorageTest.UnpackedStruct
        """
        ...

    @overload
    def map_struct(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#377)

        Args:
            key0: address
        Returns:
            struct StorageTest.UnpackedStruct
        """
        ...

    @overload
    def map_struct(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[StorageTest.UnpackedStruct]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#377)

        Args:
            key0: address
        Returns:
            struct StorageTest.UnpackedStruct
        """
        ...

    def map_struct(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[StorageTest.UnpackedStruct, TransactionAbc[StorageTest.UnpackedStruct], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#377)

        Args:
            key0: address
        Returns:
            struct StorageTest.UnpackedStruct
        """
        return self._execute(self.chain, request_type, "504429bf", [key0], True if request_type == "tx" else False, StorageTest.UnpackedStruct, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deep_map(self, key0: Union[Account, Address], key1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#378)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#378)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#378)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#378)

        Args:
            key0: address
            key1: address
        Returns:
            uint256
        """
        ...

    def deep_map(self, key0: Union[Account, Address], key1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#378)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#379)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#379)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#379)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#379)

        Args:
            key0: address
            key1: address
        Returns:
            struct StorageTest.UnpackedStruct
        """
        ...

    def deep_map_struct(self, key0: Union[Account, Address], key1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[StorageTest.UnpackedStruct, TransactionAbc[StorageTest.UnpackedStruct], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#379)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#380)

        Returns:
            basic: struct StorageTest.UnpackedStruct
        """
        ...

    @overload
    def basic(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#380)

        Returns:
            basic: struct StorageTest.UnpackedStruct
        """
        ...

    @overload
    def basic(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#380)

        Returns:
            basic: struct StorageTest.UnpackedStruct
        """
        ...

    @overload
    def basic(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[StorageTest.UnpackedStruct]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#380)

        Returns:
            basic: struct StorageTest.UnpackedStruct
        """
        ...

    def basic(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[StorageTest.UnpackedStruct, TransactionAbc[StorageTest.UnpackedStruct], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#380)

        Returns:
            basic: struct StorageTest.UnpackedStruct
        """
        return self._execute(self.chain, request_type, "15e8b345", [], True if request_type == "tx" else False, StorageTest.UnpackedStruct, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint248:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#382)

        Returns:
            tA: uint248
        """
        ...

    @overload
    def tA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#382)

        Returns:
            tA: uint248
        """
        ...

    @overload
    def tA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#382)

        Returns:
            tA: uint248
        """
        ...

    @overload
    def tA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint248]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#382)

        Returns:
            tA: uint248
        """
        ...

    def tA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint248, TransactionAbc[uint248], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#382)

        Returns:
            tA: uint248
        """
        return self._execute(self.chain, request_type, "79da7e4d", [], True if request_type == "tx" else False, uint248, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#383)

        Returns:
            tB: bool
        """
        ...

    @overload
    def tB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#383)

        Returns:
            tB: bool
        """
        ...

    @overload
    def tB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#383)

        Returns:
            tB: bool
        """
        ...

    @overload
    def tB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#383)

        Returns:
            tB: bool
        """
        ...

    def tB(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#383)

        Returns:
            tB: bool
        """
        return self._execute(self.chain, request_type, "57351c45", [], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#385)

        Returns:
            tC: bool
        """
        ...

    @overload
    def tC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#385)

        Returns:
            tC: bool
        """
        ...

    @overload
    def tC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#385)

        Returns:
            tC: bool
        """
        ...

    @overload
    def tC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#385)

        Returns:
            tC: bool
        """
        ...

    def tC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#385)

        Returns:
            tC: bool
        """
        return self._execute(self.chain, request_type, "eb53f990", [], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint248:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#386)

        Returns:
            tD: uint248
        """
        ...

    @overload
    def tD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#386)

        Returns:
            tD: uint248
        """
        ...

    @overload
    def tD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#386)

        Returns:
            tD: uint248
        """
        ...

    @overload
    def tD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint248]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#386)

        Returns:
            tD: uint248
        """
        ...

    def tD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint248, TransactionAbc[uint248], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#386)

        Returns:
            tD: uint248
        """
        return self._execute(self.chain, request_type, "e4c62a11", [], True if request_type == "tx" else False, uint248, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def map_bool(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#393)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def map_bool(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#393)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def map_bool(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#393)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    @overload
    def map_bool(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#393)

        Args:
            key0: address
        Returns:
            bool
        """
        ...

    def map_bool(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#393)

        Args:
            key0: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "8c6b4551", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#395)

        Returns:
            tE: bytes32
        """
        ...

    @overload
    def tE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#395)

        Returns:
            tE: bytes32
        """
        ...

    @overload
    def tE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#395)

        Returns:
            tE: bytes32
        """
        ...

    @overload
    def tE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#395)

        Returns:
            tE: bytes32
        """
        ...

    def tE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#395)

        Returns:
            tE: bytes32
        """
        return self._execute(self.chain, request_type, "b7e19e29", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tF(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#396)

        Returns:
            tF: address
        """
        ...

    @overload
    def tF(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#396)

        Returns:
            tF: address
        """
        ...

    @overload
    def tF(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#396)

        Returns:
            tF: address
        """
        ...

    @overload
    def tF(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#396)

        Returns:
            tF: address
        """
        ...

    def tF(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#396)

        Returns:
            tF: address
        """
        return self._execute(self.chain, request_type, "08f23aad", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tG(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#397)

        Returns:
            tG: int256
        """
        ...

    @overload
    def tG(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#397)

        Returns:
            tG: int256
        """
        ...

    @overload
    def tG(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#397)

        Returns:
            tG: int256
        """
        ...

    @overload
    def tG(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[int256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#397)

        Returns:
            tG: int256
        """
        ...

    def tG(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[int256, TransactionAbc[int256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#397)

        Returns:
            tG: int256
        """
        return self._execute(self.chain, request_type, "e5ed1efe", [], True if request_type == "tx" else False, int256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tH(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#398)

        Returns:
            tH: bool
        """
        ...

    @overload
    def tH(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#398)

        Returns:
            tH: bool
        """
        ...

    @overload
    def tH(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#398)

        Returns:
            tH: bool
        """
        ...

    @overload
    def tH(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#398)

        Returns:
            tH: bool
        """
        ...

    def tH(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#398)

        Returns:
            tH: bool
        """
        return self._execute(self.chain, request_type, "4f87aeb7", [], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def edgeCaseArray(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#404)

        Args:
            index0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def edgeCaseArray(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#404)

        Args:
            index0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def edgeCaseArray(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#404)

        Args:
            index0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def edgeCaseArray(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#404)

        Args:
            index0: uint256
        Returns:
            uint256
        """
        ...

    def edgeCaseArray(self, index0: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#404)

        Args:
            index0: uint256
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "e92e9dc4", [index0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def read_struct_upper(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#414)

        Args:
            who: address
        Returns:
            uint256
        """
        ...

    @overload
    def read_struct_upper(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#414)

        Args:
            who: address
        Returns:
            uint256
        """
        ...

    @overload
    def read_struct_upper(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#414)

        Args:
            who: address
        Returns:
            uint256
        """
        ...

    @overload
    def read_struct_upper(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#414)

        Args:
            who: address
        Returns:
            uint256
        """
        ...

    def read_struct_upper(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#414)

        Args:
            who: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "3eae2218", [who], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def read_struct_lower(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#418)

        Args:
            who: address
        Returns:
            uint256
        """
        ...

    @overload
    def read_struct_lower(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#418)

        Args:
            who: address
        Returns:
            uint256
        """
        ...

    @overload
    def read_struct_lower(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#418)

        Args:
            who: address
        Returns:
            uint256
        """
        ...

    @overload
    def read_struct_lower(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#418)

        Args:
            who: address
        Returns:
            uint256
        """
        ...

    def read_struct_lower(self, who: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#418)

        Args:
            who: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "41b6edb2", [who], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def hidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#422)

        Returns:
            t: bytes32
        """
        ...

    @overload
    def hidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#422)

        Returns:
            t: bytes32
        """
        ...

    @overload
    def hidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#422)

        Returns:
            t: bytes32
        """
        ...

    @overload
    def hidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#422)

        Returns:
            t: bytes32
        """
        ...

    def hidden(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#422)

        Returns:
            t: bytes32
        """
        return self._execute(self.chain, request_type, "aef6d4b1", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def const(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#430)

        Returns:
            t: bytes32
        """
        ...

    @overload
    def const(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#430)

        Returns:
            t: bytes32
        """
        ...

    @overload
    def const(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#430)

        Returns:
            t: bytes32
        """
        ...

    @overload
    def const(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#430)

        Returns:
            t: bytes32
        """
        ...

    def const(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#430)

        Returns:
            t: bytes32
        """
        return self._execute(self.chain, request_type, "3b80a793", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def extra_sload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#434)

        Returns:
            t: bytes32
        """
        ...

    @overload
    def extra_sload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#434)

        Returns:
            t: bytes32
        """
        ...

    @overload
    def extra_sload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#434)

        Returns:
            t: bytes32
        """
        ...

    @overload
    def extra_sload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#434)

        Returns:
            t: bytes32
        """
        ...

    def extra_sload(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#434)

        Returns:
            t: bytes32
        """
        return self._execute(self.chain, request_type, "9e7936e6", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setRandomPacking(self, val: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#442)

        Args:
            val: uint256
        """
        ...

    @overload
    def setRandomPacking(self, val: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#442)

        Args:
            val: uint256
        """
        ...

    @overload
    def setRandomPacking(self, val: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#442)

        Args:
            val: uint256
        """
        ...

    @overload
    def setRandomPacking(self, val: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#442)

        Args:
            val: uint256
        """
        ...

    def setRandomPacking(self, val: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#442)

        Args:
            val: uint256
        """
        return self._execute(self.chain, request_type, "aa463826", [val], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setRandomPacking_(self, val: uint256, size: uint256, offset: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#453)

        Args:
            val: uint256
            size: uint256
            offset: uint256
        """
        ...

    @overload
    def setRandomPacking_(self, val: uint256, size: uint256, offset: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#453)

        Args:
            val: uint256
            size: uint256
            offset: uint256
        """
        ...

    @overload
    def setRandomPacking_(self, val: uint256, size: uint256, offset: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#453)

        Args:
            val: uint256
            size: uint256
            offset: uint256
        """
        ...

    @overload
    def setRandomPacking_(self, val: uint256, size: uint256, offset: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#453)

        Args:
            val: uint256
            size: uint256
            offset: uint256
        """
        ...

    def setRandomPacking_(self, val: uint256, size: uint256, offset: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#453)

        Args:
            val: uint256
            size: uint256
            offset: uint256
        """
        return self._execute(self.chain, request_type, "1971f00b", [val, size, offset], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getRandomPacked(self, size: uint256, offset: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#462)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#462)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#462)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#462)

        Args:
            size: uint256
            offset: uint256
        Returns:
            uint256
        """
        ...

    def getRandomPacked(self, size: uint256, offset: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#462)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#469)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#469)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#469)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#469)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdStorage.t.sol#469)

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
