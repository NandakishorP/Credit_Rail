
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.forgestd.src.Test import Test



class InteroperableAddressTest(Test):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#7)
    """
    _abi = {b'p4t\xa1': {'inputs': [], 'name': 'InteroperableAddressEmptyReferenceAndAddress', 'type': 'error'}, b'\xe7\xc8\xd4\xcf': {'inputs': [{'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'InteroperableAddressParsingError', 'type': 'error'}, b'm\xfc\xc6P': {'inputs': [{'internalType': 'uint8', 'name': 'bits', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'SafeCastOverflowedUintDowncast', 'type': 'error'}, b'A0O\xac\xd92=u\xb1\x1b\xcd\xd6\t\xcb8\xef\xff\xfd\xb0W\x10\xf7\xca\xf0\xe9\xb1lm\x9dp\x9fP': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log', 'type': 'event'}, b'z\xe7LRt\x14\xae\x13_\xd9pG\xb1)!\xa5\xec9\x11\xb8\x04\x19xU\xd6~%\xc7\xb7^\xe6\xf3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'log_address', 'type': 'event'}, b'\xfb\x10(e\xd5\n\xdd\xdd\xf6\x9d\xa9\xb5\xaa\x1b\xce\xd6l\x80\xcf\x86\x9a\\\x8d\x04q\xa4g\xe1\x8c\xe9\xca\xb1': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_array', 'type': 'event'}, b'\x89\n\x82g\x9bG\x0f+\xd8(\x16\xed\x9b\x16\x1f\x97\xd8\xb9g\xf3\x7f\xa3d|!\xd5\xbf9t\x9e-\xd5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_array', 'type': 'event'}, b'@\xe1\x84\x0fWi\x07=a\xbd\x017-\x9bu\xba\xa9\x84-V)\xa0\xc9\x9f\xf1\x03\xbe\x11x\xa8\xe9\xe2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_array', 'type': 'event'}, b'#\xb6*\xd0XM$\xa7_\x0b\xf3V\x03\x91\xefVY\xecm\xb1&\x9cV\xe1\x1a\xa2A\xd67\xf1\x9b ': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'log_bytes', 'type': 'event'}, b'\xe8\x16\x99\xb8Q\x13\xee\xa1\xc7>\x10X\x8b+\x03^U\x893ic!s\xaf\xd4?\xeb\x19/\xacd\xe3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'log_bytes32', 'type': 'event'}, b'\x0e\xb5\xd5&$\xc8\xd2\x8a\xda\x9f\xc5Z\x8cP.\xd5\xaa?\xbe/\xb6\xe9\x1bq\xb5\xf3v\x88+\x1d/\xb8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256', 'name': '', 'type': 'int256'}], 'name': 'log_int', 'type': 'event'}, b'\x9cN\x85A\xca\x8f\r\xc1\xc4\x13\xf9\x10\x8ff\xd8-<\xec\xb1\xbd\xdb\xceCza\xca\xa3\x17\\L\xc9o': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address', 'name': 'val', 'type': 'address'}], 'name': 'log_named_address', 'type': 'event'}, b'\x00\xaa\xa3\x9c\x9f\xfb_VzE48\x0cspup.\x1f\x7f\x14\x10\x7f\xc9S(\xe3\xb5l\x03%\xfb': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xa7>\xda\tf/F\xdd\xe7)\xbeF\x118_\xf3O\xe6\xc4O\xbb\xc6\xf7\xe1{\x04+Y\xa3D[W': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_named_array', 'type': 'event'}, b";\xcf\xb2\xae.\x8d\x13-\xd1\xfc\xe7\xcf'\x8a\x9a\x19uj\x9f\xce\xab\xe4p\xdf;\xda\xbbK\xc5w\xd1\xbd": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xd2n\x16\xca\xd4T\x87\x05\xe4\xc9\xe2\xd9O\x98\xee\x91\xc2\x89\x08^\xe4%YO\xd5c_\xa2\x96L\xcf\x18': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'val', 'type': 'bytes'}], 'name': 'log_named_bytes', 'type': 'event'}, b'\xaf\xb7\x95\xc9\xc6\x1eO\xe7F\x8c8o\x92]zT)\xec\xad\x9c\x04\x95\xdd\xb8\xd3\x8di\x06\x14\xd3/\x99': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'val', 'type': 'bytes32'}], 'name': 'log_named_bytes32', 'type': 'event'}, b']\xa6\xce\x9dQ\x15\x1b\xa1\x0c\t\xa5Y\xef$\xd5 \xb9\xda\xc5\xc5\xb8\x81\n\xe8CNM\r\x86A\x1a\x95': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_int', 'type': 'event'}, b"\xeb\x8b\xa4<\xedu7B\x19F\xbdC\xe8(\xb8\xb2\xb8B\x89'\xaa\x8f\x80\x1c\x13\xd94\xbf\x11\xac\xa5{": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_uint', 'type': 'event'}, b'/\xe62w\x91t7CxD*\x8e\x97\x8b\xcc\xfb\xdc\xc1\xd6\xb2\xb0\xd8\x1f~\x8e\xb7v\xab"\x86\xf1h': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}], 'name': 'log_named_int', 'type': 'event'}, b'(\x0fDF\xb2\x8a\x13rA}\xdae\x8d0\xb9[)\x92\xb1*\xc9\xc7\xf3xS_)\xa9z\xcf5\x83': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'val', 'type': 'string'}], 'name': 'log_named_string', 'type': 'event'}, b'\xb2\xde/\xbe\x80\x1a\r\xf6\xc0\xcb\xdd\xfdD\x8b\xa3\xc4\x1dH\xa0@\xca5\xc5l\x81\x96\xef\x0f\xca\xe7!\xa8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}], 'name': 'log_named_uint', 'type': 'event'}, b'\x0b.\x13\xff \xac{GA\x98eU\x83\xed\xf7\r\xed\xd2\xc1\xdc\x98\x0e2\x9cO\xbb/\xc0t\x8byk': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log_string', 'type': 'event'}, b',\xab\x97\x90Q\x0f\xd8\xbd\xfb\xd2\x11R\x88\xdb3\xfe\xc6f\x91\xd4v\xef\xc5B|\xfdL\ti0\x17U': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'log_uint', 'type': 'event'}, b"\xe7\x95\x0e\xde\x03\x94\xb9\xf2\xceJZ\x1b\xf5\xa7\xe1\x85$\x11\xf7\xe6f\x1bC\x08\xc9\x13\xc4\xbf\xd1\x10'\xe4": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'logs', 'type': 'event'}, b'\xfav&\xd4': {'inputs': [], 'name': 'IS_TEST', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb5P\x8a\xa9': {'inputs': [], 'name': 'excludeArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'excludedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe2\x0c\x9fq': {'inputs': [], 'name': 'excludeContracts', 'outputs': [{'internalType': 'address[]', 'name': 'excludedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb0FO\xdc': {'inputs': [], 'name': 'excludeSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'excludedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1e\xd7\x83\x1c': {'inputs': [], 'name': 'excludeSenders', 'outputs': [{'internalType': 'address[]', 'name': 'excludedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbaAO\xa6': {'inputs': [], 'name': 'failed', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbfg\xd2\xc8': {'inputs': [{'internalType': 'bytes', 'name': 'self', 'type': 'bytes'}], 'name': 'parseEvmV1Calldata', 'outputs': [{'internalType': 'uint256', 'name': 'chainid', 'type': 'uint256'}, {'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'stateMutability': 'pure', 'type': 'function'}, b'<iE.': {'inputs': [{'internalType': 'bytes', 'name': 'self', 'type': 'bytes'}], 'name': 'parseV1Calldata', 'outputs': [{'internalType': 'bytes2', 'name': 'chainType', 'type': 'bytes2'}, {'internalType': 'bytes', 'name': 'chainReference', 'type': 'bytes'}, {'internalType': 'bytes', 'name': 'addr', 'type': 'bytes'}], 'stateMutability': 'pure', 'type': 'function'}, b'f\xd9\xa9\xa0': {'inputs': [], 'name': 'targetArtifactSelectors', 'outputs': [{'components': [{'internalType': 'string', 'name': 'artifact', 'type': 'string'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzArtifactSelector[]', 'name': 'targetedArtifactSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x85"l\x81': {'inputs': [], 'name': 'targetArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'targetedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'?r\x86\xf4': {'inputs': [], 'name': 'targetContracts', 'outputs': [{'internalType': 'address[]', 'name': 'targetedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'*\xde8\x80': {'inputs': [], 'name': 'targetInterfaces', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'string[]', 'name': 'artifacts', 'type': 'string[]'}], 'internalType': 'struct StdInvariant.FuzzInterface[]', 'name': 'targetedInterfaces_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x91j\x17\xc6': {'inputs': [], 'name': 'targetSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'targetedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'>^<#': {'inputs': [], 'name': 'targetSenders', 'outputs': [{'internalType': 'address[]', 'name': 'targetedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa9E\xe9t': {'inputs': [{'internalType': 'bytes2', 'name': 'chainType', 'type': 'bytes2'}, {'internalType': 'bytes', 'name': 'chainReference', 'type': 'bytes'}, {'internalType': 'bytes', 'name': 'addr', 'type': 'bytes'}], 'name': 'testFormatParse', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\xb1\x98\xe3\xfa': {'inputs': [{'internalType': 'uint256', 'name': 'chainid', 'type': 'uint256'}, {'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'testFormatParseEVM', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\xea&\xcb\x83': {'inputs': [{'internalType': 'bytes', 'name': 'self', 'type': 'bytes'}], 'name': 'tryParseEvmV1Calldata', 'outputs': [{'internalType': 'bool', 'name': 'success', 'type': 'bool'}, {'internalType': 'uint256', 'name': 'chainid', 'type': 'uint256'}, {'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'stateMutability': 'pure', 'type': 'function'}, b'\xa7o^\xcd': {'inputs': [{'internalType': 'bytes', 'name': 'self', 'type': 'bytes'}], 'name': 'tryParseV1Calldata', 'outputs': [{'internalType': 'bool', 'name': 'success', 'type': 'bool'}, {'internalType': 'bytes2', 'name': 'chainType', 'type': 'bytes2'}, {'internalType': 'bytes', 'name': 'chainReference', 'type': 'bytes'}, {'internalType': 'bytes', 'name': 'addr', 'type': 'bytes'}], 'stateMutability': 'pure', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":46,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"stdstore","offset":0,"slot":0,"type":"t_struct(StdStorage)8331_storage"},{"astId":209,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"_failed","offset":0,"slot":8,"type":"t_bool"},{"astId":2943,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"stdChainsInitialized","offset":1,"slot":8,"type":"t_bool"},{"astId":2964,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"chains","offset":0,"slot":9,"type":"t_mapping(t_string_memory_ptr,t_struct(Chain)2959_storage)"},{"astId":2968,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"defaultRpcUrls","offset":0,"slot":10,"type":"t_mapping(t_string_memory_ptr,t_string_storage)"},{"astId":2972,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"idToAlias","offset":0,"slot":11,"type":"t_mapping(t_uint256,t_string_storage)"},{"astId":2975,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"fallbackToDefaultRpcUrls","offset":0,"slot":12,"type":"t_bool"},{"astId":3931,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"gasMeteringOff","offset":1,"slot":12,"type":"t_bool"},{"astId":6002,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"stdstore","offset":0,"slot":13,"type":"t_struct(StdStorage)8331_storage"},{"astId":6923,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"_excludedContracts","offset":0,"slot":21,"type":"t_array(t_address)dyn_storage"},{"astId":6926,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"_excludedSenders","offset":0,"slot":22,"type":"t_array(t_address)dyn_storage"},{"astId":6929,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"_targetedContracts","offset":0,"slot":23,"type":"t_array(t_address)dyn_storage"},{"astId":6932,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"_targetedSenders","offset":0,"slot":24,"type":"t_array(t_address)dyn_storage"},{"astId":6935,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"_excludedArtifacts","offset":0,"slot":25,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6938,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"_targetedArtifacts","offset":0,"slot":26,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6942,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"_targetedArtifactSelectors","offset":0,"slot":27,"type":"t_array(t_struct(FuzzArtifactSelector)6914_storage)dyn_storage"},{"astId":6946,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"_excludedSelectors","offset":0,"slot":28,"type":"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage"},{"astId":6950,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"_targetedSelectors","offset":0,"slot":29,"type":"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage"},{"astId":6954,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"_targetedInterfaces","offset":0,"slot":30,"type":"t_array(t_struct(FuzzInterface)6920_storage)dyn_storage"},{"astId":13223,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"IS_TEST","offset":0,"slot":31,"type":"t_bool"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_address)dyn_storage":{"encoding":"dynamic_array","label":"address[]","numberOfBytes":32,"base":"t_address"},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_array(t_bytes4)dyn_storage":{"encoding":"dynamic_array","label":"bytes4[]","numberOfBytes":32,"base":"t_bytes4"},"t_array(t_string_storage)dyn_storage":{"encoding":"dynamic_array","label":"string[]","numberOfBytes":32,"base":"t_string_storage"},"t_array(t_struct(FuzzArtifactSelector)6914_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzArtifactSelector[]","numberOfBytes":32,"base":"t_struct(FuzzArtifactSelector)6914_storage"},"t_array(t_struct(FuzzInterface)6920_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzInterface[]","numberOfBytes":32,"base":"t_struct(FuzzInterface)6920_storage"},"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzSelector[]","numberOfBytes":32,"base":"t_struct(FuzzSelector)6908_storage"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))"},"t_mapping(t_bytes32,t_struct(FindData)8306_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)8306_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)8306_storage)"},"t_mapping(t_string_memory_ptr,t_string_storage)":{"encoding":"mapping","label":"mapping(string => string)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_string_storage"},"t_mapping(t_string_memory_ptr,t_struct(Chain)2959_storage)":{"encoding":"mapping","label":"mapping(string => struct StdChains.Chain)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_struct(Chain)2959_storage"},"t_mapping(t_uint256,t_string_storage)":{"encoding":"mapping","label":"mapping(uint256 => string)","numberOfBytes":32,"key":"t_uint256","value":"t_string_storage"},"t_string_memory_ptr":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(Chain)2959_storage":{"encoding":"inplace","label":"struct StdChains.Chain","numberOfBytes":128,"members":[{"astId":2952,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"name","offset":0,"slot":0,"type":"t_string_storage"},{"astId":2954,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"chainId","offset":0,"slot":1,"type":"t_uint256"},{"astId":2956,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"chainAlias","offset":0,"slot":2,"type":"t_string_storage"},{"astId":2958,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"rpcUrl","offset":0,"slot":3,"type":"t_string_storage"}]},"t_struct(FindData)8306_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":8299,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":8301,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":8303,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":8305,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(FuzzArtifactSelector)6914_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzArtifactSelector","numberOfBytes":64,"members":[{"astId":6910,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"artifact","offset":0,"slot":0,"type":"t_string_storage"},{"astId":6913,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(FuzzInterface)6920_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzInterface","numberOfBytes":64,"members":[{"astId":6916,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6919,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"artifacts","offset":0,"slot":1,"type":"t_array(t_string_storage)dyn_storage"}]},"t_struct(FuzzSelector)6908_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzSelector","numberOfBytes":64,"members":[{"astId":6904,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6907,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(StdStorage)8331_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":8315,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))"},{"astId":8318,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":8320,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":8322,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":8324,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":8326,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":8328,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":8330,"contract":"lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol:InteroperableAddressTest","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60808060405234602f57600160ff19600c541617600c55600160ff19601f541617601f55611f1c90816100348239f35b5f80fdfe6080806040526004361015610012575f80fd5b5f905f3560e01c9081631ed7831c14610fc6575080632ade388014610e0b5780633c69452e14610d885780633e5e3c2314610d0b5780633f7286f414610c8e57806366d9a9a014610b6a57806385226c8114610adf578063916a17c614610a36578063a76f5ecd146109bb578063a945e974146105a0578063b0464fdc146104f8578063b198e3fa14610301578063b5508aa914610277578063ba414fa614610252578063bf67d2c8146101f3578063e20c9f7114610165578063ea26cb83146101095763fa7626d4146100e4575f80fd5b34610106578060031936011261010657602060ff601f54166040519015158152f35b80fd5b503461010657602036600319011261010657600435906001600160401b03821161010657606061014561013f3660048601611088565b90611d7a565b60408051931515845260208401929092526001600160a01b031690820152f35b503461010657806003193601126101065760405160158054808352908352909160208301917f55f448fdea98c4d29eb340757ef0a66cd03dbb9538908a6a81d96026b71ec475915b8181106101d4576101d0856101c481870382611217565b60405191829182611022565b0390f35b82546001600160a01b03168452602090930192600192830192016101ad565b503461010657602036600319011261010657600435906001600160401b0382116101065760406102263660048501611088565b61023d6102338284611d7a565b9391949094611685565b82519182526001600160a01b03166020820152f35b5034610106578060031936011261010657602061026d6115ea565b6040519015158152f35b503461010657806003193601126101065760195461029481611238565b916102a26040519384611217565b818352601981527f944998273e477b495144fb8794c914197f3ccb46be2900f4698fd0ef743c9695602084015b8383106102e457604051806101d08782611112565b6001602081926102f38561124f565b8152019201920191906102cf565b5034610106576040366003190112610106576004356024356001600160a01b03811681036104f4578061035f6103536103596103406103af9587611ac7565b61034981611c78565b949192909261185c565b86611b97565b82611bf1565b61038261035361035961037a6103758588611ac7565b611c78565b939091611a74565b604061038e8285611ac7565b8151809481926317ecfa5960e31b8352602060048401526024830190611064565b0381305afa91821561049c57849085936104a7575b50610404926103596103d69286611b97565b60606103e28285611ac7565b6040518094819263ea26cb8360e01b8352602060048401526024830190611064565b0381305afa91821561049c578485918694610439575b50906104369461042c61043193611a74565b611b97565b611bf1565b80f35b935050506060823d606011610494575b8161045660609383611217565b81010312610490576104316104369361046e846115c9565b9061042c6104836040602088015197016115d6565b91969195935061041a9050565b8380fd5b3d9150610449565b6040513d86823e3d90fd5b9250506040823d6040116104ec575b816104c360409383611217565b81010312610490576103d6826103596104e36020610404965193016115d6565b945050906103c4565b3d91506104b6565b8280fd5b5034610106578060031936011261010657601c5461051581611238565b916105236040519384611217565b818352601c81527f0e4562a10381dec21b205ed72637e6b1b523bdd0e4d4d50af5cd23dd4500a211602084015b83831061056557604051806101d08782611171565b60026020600192604051610578816111e8565b848060a01b03865416815261058e85870161131b565b83820152815201920192019190610550565b50346109ae5760603660031901126109ae576004356001600160f01b03198116908181036109ae576024356001600160401b0381116109ae576105e7903690600401611088565b91906044356001600160401b0381116109ae57610608903690600401611088565b91909284158015906109b2575b5f516020611ec75f395f51905f523b156109ae57604051632631f2b160e11b815290151560048201525f816024815f516020611ec75f395f51905f525afa80156109a357610989575b509086610751926106d06106a56106c561068e61067c368c89611538565b610687368b8d611538565b90866117a8565b6106b561069a8261195d565b96919294909461185c565b6001600160f01b0319168d611889565b6106c0368c89611538565b6118ed565b6106c036888a611538565b61070e6106b56106c56106a56107046106ff6106ed368e8b611538565b6106f8368d8f611538565b90886117a8565b61195d565b9592939093611a74565b8161072f61071d368a87611538565b61072836898b611538565b90846117a8565b60405180968192631e34a29760e11b8352602060048401526024830190611064565b0381305afa93841561097e578883849285976108eb575b50956107956107bc949361078a6107a0946107de9a61ffff60f01b1690611889565b6106c0368d8a611538565b6106c036898b611538565b6107ab368986611538565b6107b636888a611538565b916117a8565b6040518094819263a76f5ecd60e01b8352602060048401526024830190611064565b0381305afa9485156108e05787889089948a9861082d575b50926106c0969594926108266104369a6106c09461081661082698611a74565b6001600160f01b03191690611889565b3691611538565b9397505050939291503d8088833e6108458183611217565b8101906080818303126108dc5761085b816115c9565b906108686020820161156e565b9660408201516001600160401b0381116108d85784610888918401611583565b966060830151946001600160401b0386116108d4576104369a6106c0996108166108bd610826946108269a6106c09901611583565b979c91979c9598505094509a5050929495966107f6565b8b80fd5b8a80fd5b8780fd5b6040513d89823e3d90fd5b96505050503d8083863e6108ff8186611217565b8401906060858303126104f4576109158561156e565b9460208101516001600160401b03811161097a5783610935918301611583565b6040820151916001600160401b038311610976576107de9761078a8d6109666107bc986107a0976107959601611583565b9294929a50945050939450610768565b8580fd5b8480fd5b6040513d84823e3d90fd5b610751929197505f61099a91611217565b5f96909161065e565b6040513d5f823e3d90fd5b5f80fd5b50821515610615565b346109ae5760203660031901126109ae576004356001600160401b0381116109ae57610a286109fa6109f46101d0933690600401611088565b906116b9565b929093969495916040519788971515885261ffff60f01b1660208801526080604088015260808701916110b5565b9184830360608601526110b5565b346109ae575f3660031901126109ae57601d54610a5281611238565b90610a606040519283611217565b808252601d5f9081527f6d4407e7be21f808e6509aa9fa9143369579dd7d760fe20a2c09680fc146134f602084015b838310610aa457604051806101d08782611171565b60026020600192604051610ab7816111e8565b848060a01b038654168152610acd85870161131b565b83820152815201920192019190610a8f565b346109ae575f3660031901126109ae57601a54610afb81611238565b90610b096040519283611217565b808252601a5f9081527f057c384a7d1c54f3a1b2e5e67b2617b8224fdfd1ea7234eea573a6ff665ff63e602084015b838310610b4d57604051806101d08782611112565b600160208192610b5c8561124f565b815201920192019190610b38565b346109ae575f3660031901126109ae57601b54610b8681611238565b90610b946040519283611217565b808252601b5f9081526020830191907f3ad8aa4f87544323a9d1e5dd902f40c356527a7955687113db5f9a85ad579dc1835b838310610c5357848660405191829160208301906020845251809152604083019060408160051b85010192915f905b828210610c0457505050500390f35b91936001919395506020610c438192603f198a820301865288519083610c338351604084526040840190611064565b92015190848184039101526110d5565b9601920192018594939192610bf5565b60026020600192604051610c66816111e8565b610c6f8661124f565b8152610c7c85870161131b565b83820152815201920192019190610bc6565b346109ae575f3660031901126109ae57604051601780548083525f91825260208301917fc624b66cc0138b8fabc209247f72d758e1cf3343756d543badbf24212bed8c1591905b818110610cec576101d0856101c481870382611217565b82546001600160a01b0316845260209093019260019283019201610cd5565b346109ae575f3660031901126109ae57604051601880548083525f91825260208301917fb13d2d76d1f4b7be834882e410b3e3a8afaf69f83600ae24db354391d2378d2e91905b818110610d69576101d0856101c481870382611217565b82546001600160a01b0316845260209093019260019283019201610d52565b346109ae5760203660031901126109ae576004356001600160401b0381116109ae576101d0610dbe610ddd923690600401611088565b9190610dfd610dcd84836116b9565b9594999293989199969096611685565b60405196879661ffff60f01b1687526060602088015260608701916110b5565b9184830360408601526110b5565b346109ae575f3660031901126109ae57601e54610e2781611238565b90610e356040519283611217565b808252601e5f9081526020830191907f50bb669a95c7b50b7e8a6f09454034b2b14cf2b85c730dca9a539ca82cb6e350835b838310610f3b57848660405191829160208301906020845251809152604083019060408160051b85010192915f905b828210610ea557505050500390f35b919390929450603f198682030182528451906020604082019260018060a01b0381511683520151916040602083015282518091526060820190602060608260051b8501019401925f5b828110610f105750505050506020806001929601920192018594939192610e96565b9091929394602080610f2e600193605f198782030189528951611064565b9701950193929101610eee565b604051610f47816111e8565b82546001600160a01b03168152600183018054610f6381611238565b91610f716040519384611217565b81835260208301905f5260205f20905f905b838210610fa9575050505060019282602092836002950152815201920192019190610e67565b600160208192610fb88661124f565b815201930191019091610f83565b346109ae575f3660031901126109ae57601654808252602082019060165f5260205f20905f5b818110611003576101d0856101c481870382611217565b82546001600160a01b0316845260209093019260019283019201610fec565b60206040818301928281528451809452019201905f5b8181106110455750505090565b82516001600160a01b0316845260209384019390920191600101611038565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b9181601f840112156109ae578235916001600160401b0383116109ae57602083818601950101116109ae57565b908060209392818452848401375f828201840152601f01601f1916010190565b90602080835192838152019201905f5b8181106110f25750505090565b82516001600160e01b0319168452602093840193909201916001016110e5565b602081016020825282518091526040820191602060408360051b8301019401925f915b83831061114457505050505090565b9091929394602080611162600193603f198682030187528951611064565b97019301930191939290611135565b602081016020825282518091526040820191602060408360051b8301019401925f915b8383106111a357505050505090565b90919293946020806111d9600193603f198682030187526040838b51878060a01b038151168452015191818582015201906110d5565b97019301930191939290611194565b604081019081106001600160401b0382111761120357604052565b634e487b7160e01b5f52604160045260245ffd5b90601f801991011681019081106001600160401b0382111761120357604052565b6001600160401b0381116112035760051b60200190565b90604051915f8154908160011c9260018316928315611311575b6020851084146112fd5784875286939081156112db5750600114611297575b5061129592500383611217565b565b90505f9291925260205f20905f915b8183106112bf575050906020611295928201015f611288565b60209193508060019154838589010152019101909184926112a6565b90506020925061129594915060ff191682840152151560051b8201015f611288565b634e487b7160e01b5f52602260045260245ffd5b93607f1693611269565b90604051918281549182825260208201905f5260205f20925f905b80600783011061147857611295945491818110611459575b81811061143a575b81811061141b575b8181106113fc575b8181106113dd575b8181106113be575b8181106113a1575b1061138c575b500383611217565b6001600160e01b03191681526020015f611384565b602083811b6001600160e01b03191685529093019260010161137e565b604083901b6001600160e01b0319168452602090930192600101611376565b606083901b6001600160e01b031916845260209093019260010161136e565b608083901b6001600160e01b0319168452602090930192600101611366565b60a083901b6001600160e01b031916845260209093019260010161135e565b60c083901b6001600160e01b0319168452602090930192600101611356565b60e083901b6001600160e01b031916845260209093019260010161134e565b916008919350610100600191865463ffffffff60e01b8160e01b16825263ffffffff60e01b8160c01b16602083015263ffffffff60e01b8160a01b16604083015263ffffffff60e01b8160801b16606083015263ffffffff60e01b8160601b16608083015263ffffffff60e01b8160401b1660a083015263ffffffff60e01b8160201b1660c083015263ffffffff60e01b1660e0820152019401920185929391611336565b6001600160401b03811161120357601f01601f191660200190565b9291926115448261151d565b916115526040519384611217565b8294818452818301116109ae578281602093845f960137010152565b51906001600160f01b0319821682036109ae57565b81601f820112156109ae5780519061159a8261151d565b926115a86040519485611217565b828452602083830101116109ae57815f9260208093018386015e8301015290565b519081151582036109ae57565b51906001600160a01b03821682036109ae57565b60085460ff16156115fa57600190565b604051630667f9d760e41b81525f516020611ec75f395f51905f5260048201526519985a5b195960d21b60248201526020816044815f516020611ec75f395f51905f525afa9081156109a3575f91611653575b50151590565b90506020813d60201161167d575b8161166e60209383611217565b810103126109ae57515f61164d565b3d9150611661565b91909115611691575050565b6116b560405192839263e7c8d4cf60e01b84526020600485015260248401916110b5565b0390fd5b60019260068310611797576001600160f01b031982358116016117975760028201356001600160f01b03191692600481111561176f57600483013560f81c9160ff8360060116928383106117835760ff906005011692836005116109ae578284116109ae5760058501946004198501948481101561176f5781013560f81c820160ff1693848110611758578483116109ae5784116109ae578101920390565b5050509450505050505f905f905f905f905f905f90565b634e487b7160e01b5f52603260045260245ffd5b505f95508594508493508392508291508190565b5f9350839250829150819081908190565b90805115801590611852575b15611843576118409160256020836117ce60019551611e44565b96826117da8251611e44565b92604051998a978960f01b848a015261ffff60f01b16602289015260ff60f81b9060f81b1660248801528051918291018688015e85019160ff60f81b9060f81b1684830152805192839101602683015e01015f838201520301601f198101835282611217565b90565b63703474a160e01b5f5260045ffd5b50825115156117b4565b156118645750565b60405163e7c8d4cf60e01b8152602060048201529081906116b5906024830190611064565b90808203611895575050565b5f516020611ec75f395f51905f523b156109ae5760405191637c84c69b60e01b8352600483015260248201525f816044815f516020611ec75f395f51905f525afa80156109a3576118e35750565b5f61129591611217565b5f516020611ec75f395f51905f523b156109ae5761192c5f9161193e6040519485938493639762463160e01b8552604060048601526044850190611064565b83810360031901602485015290611064565b03815f516020611ec75f395f51905f525afa80156109a3576118e35750565b9060019180519160068310611a665760208201516001600160f01b031990811601611a665760228201516001600160f01b031916926004101561176f57602482015160f81c9180519260ff8160060116809410611a555760ff9060050116928151808510818618021880600510816005180281186119db8183611c57565b91602082611a016119eb8661151d565b956119f96040519788611217565b80875261151d565b8583019390601f19013685370392860101905e93825181101561176f576020908301015160f81c9160ff815193830116809310611a4357906118409291611e69565b505050925050505f905f906060908190565b5050925050505f905f906060908190565b5f9350839250606091508190565b1580611a7d5750565b5f516020611ec75f395f51905f523b156109ae57604051630c9fd58160e01b8152901560048201525f816024815f516020611ec75f395f51905f525afa80156109a3576118e35750565b60156025611b3a6118409360018060801b03811160071b6001600160401b0382821c1160061b1763ffffffff82821c1160051b1761ffff82821c1160041b17906040519080602083015260208252611b20604083611217565b81519260ff5f1992821c119060031c176020030190611e69565b938451906020604051968793600160f01b8386015260ff60f81b9060f81b1660248501528051918291018585015e820190600560fa1b848301526001600160601b03199060601b1660268201520301600a19810184520182611217565b90808203611ba3575050565b5f516020611ec75f395f51905f523b156109ae576040519163260a5b1560e21b8352600483015260248201525f816044815f516020611ec75f395f51905f525afa80156109a3576118e35750565b6001600160a01b039081169116808203611c09575050565b5f516020611ec75f395f51905f523b156109ae57604051916328a9b0fb60e11b8352600483015260248201525f816044815f516020611ec75f395f51905f525afa80156109a3576118e35750565b91908203918211611c6457565b634e487b7160e01b5f52601160045260245ffd5b611c819061195d565b939183919391611d67575b5080611d5c575b80611d3e575b15611d3457602082519201519160208110611d22575b6001600160fd1b0381168103611c645760031b61010003916101008311611c645760208451940151936001600160601b031985169460148210611cfd575b50506001921c9260601c91929190565b6bffffffffffffffffffffffff1960149290920360031b82901b161693505f80611ced565b915f198360200360031b1b1691611caf565b5f92508291508190565b5082518015908115611d51575b50611c99565b60149150145f611d4b565b506021825110611c93565b6001600160f01b0319161590505f611c8c565b90611d84916116b9565b959385919593929391611e31575b5080611e27575b80611e15575b15611e0857359060208110611df6575b6001600160fd1b0381168103611c645760031b61010003926101008411611c645735936001600160601b031985169460148210611cfd5750506001921c9260601c91929190565b905f198260200360031b1b1690611daf565b505f935083925082919050565b50841580611d9f575060148514611d9f565b5060218210611d99565b6001600160f01b0319161590505f611d92565b60ff8111611e525760ff1690565b6306dfcc6560e41b5f52600860045260245260445ffd5b9091815190818082109118021891828082109118028218916020611e8d8483611c57565b9380611eb1611e9b8761151d565b96611ea96040519889611217565b80885261151d565b8684019490601f190136863703930101905e9056fe0000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da264697066735822122093fa967334405860a9c1205544e03da0378199c25766c4ea0edd319a0f980a1d64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> InteroperableAddressTest:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[InteroperableAddressTest]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, InteroperableAddressTest, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[InteroperableAddressTest]]:
        return cls._deploy(request_type, [], return_tx, InteroperableAddressTest, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def testFormatParse(self, chainType: bytes2, chainReference: Union[bytearray, bytes], addr: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#10)

        Args:
            chainType: bytes2
            chainReference: bytes
            addr: bytes
        """
        ...

    @overload
    def testFormatParse(self, chainType: bytes2, chainReference: Union[bytearray, bytes], addr: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#10)

        Args:
            chainType: bytes2
            chainReference: bytes
            addr: bytes
        """
        ...

    @overload
    def testFormatParse(self, chainType: bytes2, chainReference: Union[bytearray, bytes], addr: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#10)

        Args:
            chainType: bytes2
            chainReference: bytes
            addr: bytes
        """
        ...

    @overload
    def testFormatParse(self, chainType: bytes2, chainReference: Union[bytearray, bytes], addr: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#10)

        Args:
            chainType: bytes2
            chainReference: bytes
            addr: bytes
        """
        ...

    def testFormatParse(self, chainType: bytes2, chainReference: Union[bytearray, bytes], addr: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#10)

        Args:
            chainType: bytes2
            chainReference: bytes
            addr: bytes
        """
        return self._execute(self.chain, request_type, "a945e974", [chainType, chainReference, addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFormatParseEVM(self, chainid: uint256, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#47)

        Args:
            chainid: uint256
            addr: address
        """
        ...

    @overload
    def testFormatParseEVM(self, chainid: uint256, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#47)

        Args:
            chainid: uint256
            addr: address
        """
        ...

    @overload
    def testFormatParseEVM(self, chainid: uint256, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#47)

        Args:
            chainid: uint256
            addr: address
        """
        ...

    @overload
    def testFormatParseEVM(self, chainid: uint256, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#47)

        Args:
            chainid: uint256
            addr: address
        """
        ...

    def testFormatParseEVM(self, chainid: uint256, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#47)

        Args:
            chainid: uint256
            addr: address
        """
        return self._execute(self.chain, request_type, "b198e3fa", [chainid, addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def parseV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[bytes2, bytearray, bytearray]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#78)

        Args:
            self_: bytes
        Returns:
            chainType: bytes2
            chainReference: bytes
            addr: bytes
        """
        ...

    @overload
    def parseV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#78)

        Args:
            self_: bytes
        Returns:
            chainType: bytes2
            chainReference: bytes
            addr: bytes
        """
        ...

    @overload
    def parseV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#78)

        Args:
            self_: bytes
        Returns:
            chainType: bytes2
            chainReference: bytes
            addr: bytes
        """
        ...

    @overload
    def parseV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[bytes2, bytearray, bytearray]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#78)

        Args:
            self_: bytes
        Returns:
            chainType: bytes2
            chainReference: bytes
            addr: bytes
        """
        ...

    def parseV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[bytes2, bytearray, bytearray], TransactionAbc[Tuple[bytes2, bytearray, bytearray]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#78)

        Args:
            self_: bytes
        Returns:
            chainType: bytes2
            chainReference: bytes
            addr: bytes
        """
        return self._execute(self.chain, request_type, "3c69452e", [self_], True if request_type == "tx" else False, Tuple[bytes2, bytearray, bytearray], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tryParseV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[bool, bytes2, bytearray, bytearray]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#84)

        Args:
            self_: bytes
        Returns:
            success: bool
            chainType: bytes2
            chainReference: bytes
            addr: bytes
        """
        ...

    @overload
    def tryParseV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#84)

        Args:
            self_: bytes
        Returns:
            success: bool
            chainType: bytes2
            chainReference: bytes
            addr: bytes
        """
        ...

    @overload
    def tryParseV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#84)

        Args:
            self_: bytes
        Returns:
            success: bool
            chainType: bytes2
            chainReference: bytes
            addr: bytes
        """
        ...

    @overload
    def tryParseV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[bool, bytes2, bytearray, bytearray]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#84)

        Args:
            self_: bytes
        Returns:
            success: bool
            chainType: bytes2
            chainReference: bytes
            addr: bytes
        """
        ...

    def tryParseV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[bool, bytes2, bytearray, bytearray], TransactionAbc[Tuple[bool, bytes2, bytearray, bytearray]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#84)

        Args:
            self_: bytes
        Returns:
            success: bool
            chainType: bytes2
            chainReference: bytes
            addr: bytes
        """
        return self._execute(self.chain, request_type, "a76f5ecd", [self_], True if request_type == "tx" else False, Tuple[bool, bytes2, bytearray, bytearray], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def parseEvmV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[uint256, Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#90)

        Args:
            self_: bytes
        Returns:
            chainid: uint256
            addr: address
        """
        ...

    @overload
    def parseEvmV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#90)

        Args:
            self_: bytes
        Returns:
            chainid: uint256
            addr: address
        """
        ...

    @overload
    def parseEvmV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#90)

        Args:
            self_: bytes
        Returns:
            chainid: uint256
            addr: address
        """
        ...

    @overload
    def parseEvmV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[uint256, Address]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#90)

        Args:
            self_: bytes
        Returns:
            chainid: uint256
            addr: address
        """
        ...

    def parseEvmV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[uint256, Address], TransactionAbc[Tuple[uint256, Address]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#90)

        Args:
            self_: bytes
        Returns:
            chainid: uint256
            addr: address
        """
        return self._execute(self.chain, request_type, "bf67d2c8", [self_], True if request_type == "tx" else False, Tuple[uint256, Address], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tryParseEvmV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[bool, uint256, Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#94)

        Args:
            self_: bytes
        Returns:
            success: bool
            chainid: uint256
            addr: address
        """
        ...

    @overload
    def tryParseEvmV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#94)

        Args:
            self_: bytes
        Returns:
            success: bool
            chainid: uint256
            addr: address
        """
        ...

    @overload
    def tryParseEvmV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#94)

        Args:
            self_: bytes
        Returns:
            success: bool
            chainid: uint256
            addr: address
        """
        ...

    @overload
    def tryParseEvmV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[bool, uint256, Address]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#94)

        Args:
            self_: bytes
        Returns:
            success: bool
            chainid: uint256
            addr: address
        """
        ...

    def tryParseEvmV1Calldata(self, self_: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[bool, uint256, Address], TransactionAbc[Tuple[bool, uint256, Address]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/draft-InteroperableAddress.t.sol#94)

        Args:
            self_: bytes
        Returns:
            success: bool
            chainid: uint256
            addr: address
        """
        return self._execute(self.chain, request_type, "ea26cb83", [self_], True if request_type == "tx" else False, Tuple[bool, uint256, Address], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

InteroperableAddressTest.testFormatParse.selector = bytes4(b'\xa9E\xe9t')
InteroperableAddressTest.testFormatParseEVM.selector = bytes4(b'\xb1\x98\xe3\xfa')
InteroperableAddressTest.parseV1Calldata.selector = bytes4(b'<iE.')
InteroperableAddressTest.tryParseV1Calldata.selector = bytes4(b'\xa7o^\xcd')
InteroperableAddressTest.parseEvmV1Calldata.selector = bytes4(b'\xbfg\xd2\xc8')
InteroperableAddressTest.tryParseEvmV1Calldata.selector = bytes4(b'\xea&\xcb\x83')
