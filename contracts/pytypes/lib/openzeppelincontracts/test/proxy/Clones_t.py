
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.forgestd.src.Test import Test



class ClonesTest(Test):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#8)
    """
    _abi = {b'\x94(\x90T': {'inputs': [], 'name': 'CloneArgumentsTooLong', 'type': 'error'}, b'L\xa2I\xdc': {'inputs': [], 'name': 'Create2EmptyBytecode', 'type': 'error'}, b'\xb0n\xbf=': {'inputs': [], 'name': 'FailedDeployment', 'type': 'error'}, b'\xcfG\x91\x81': {'inputs': [{'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}], 'name': 'InsufficientBalance', 'type': 'error'}, b'A0O\xac\xd92=u\xb1\x1b\xcd\xd6\t\xcb8\xef\xff\xfd\xb0W\x10\xf7\xca\xf0\xe9\xb1lm\x9dp\x9fP': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log', 'type': 'event'}, b'z\xe7LRt\x14\xae\x13_\xd9pG\xb1)!\xa5\xec9\x11\xb8\x04\x19xU\xd6~%\xc7\xb7^\xe6\xf3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'log_address', 'type': 'event'}, b'\xfb\x10(e\xd5\n\xdd\xdd\xf6\x9d\xa9\xb5\xaa\x1b\xce\xd6l\x80\xcf\x86\x9a\\\x8d\x04q\xa4g\xe1\x8c\xe9\xca\xb1': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_array', 'type': 'event'}, b'\x89\n\x82g\x9bG\x0f+\xd8(\x16\xed\x9b\x16\x1f\x97\xd8\xb9g\xf3\x7f\xa3d|!\xd5\xbf9t\x9e-\xd5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_array', 'type': 'event'}, b'@\xe1\x84\x0fWi\x07=a\xbd\x017-\x9bu\xba\xa9\x84-V)\xa0\xc9\x9f\xf1\x03\xbe\x11x\xa8\xe9\xe2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_array', 'type': 'event'}, b'#\xb6*\xd0XM$\xa7_\x0b\xf3V\x03\x91\xefVY\xecm\xb1&\x9cV\xe1\x1a\xa2A\xd67\xf1\x9b ': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'log_bytes', 'type': 'event'}, b'\xe8\x16\x99\xb8Q\x13\xee\xa1\xc7>\x10X\x8b+\x03^U\x893ic!s\xaf\xd4?\xeb\x19/\xacd\xe3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'log_bytes32', 'type': 'event'}, b'\x0e\xb5\xd5&$\xc8\xd2\x8a\xda\x9f\xc5Z\x8cP.\xd5\xaa?\xbe/\xb6\xe9\x1bq\xb5\xf3v\x88+\x1d/\xb8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256', 'name': '', 'type': 'int256'}], 'name': 'log_int', 'type': 'event'}, b'\x9cN\x85A\xca\x8f\r\xc1\xc4\x13\xf9\x10\x8ff\xd8-<\xec\xb1\xbd\xdb\xceCza\xca\xa3\x17\\L\xc9o': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address', 'name': 'val', 'type': 'address'}], 'name': 'log_named_address', 'type': 'event'}, b'\x00\xaa\xa3\x9c\x9f\xfb_VzE48\x0cspup.\x1f\x7f\x14\x10\x7f\xc9S(\xe3\xb5l\x03%\xfb': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xa7>\xda\tf/F\xdd\xe7)\xbeF\x118_\xf3O\xe6\xc4O\xbb\xc6\xf7\xe1{\x04+Y\xa3D[W': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_named_array', 'type': 'event'}, b";\xcf\xb2\xae.\x8d\x13-\xd1\xfc\xe7\xcf'\x8a\x9a\x19uj\x9f\xce\xab\xe4p\xdf;\xda\xbbK\xc5w\xd1\xbd": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xd2n\x16\xca\xd4T\x87\x05\xe4\xc9\xe2\xd9O\x98\xee\x91\xc2\x89\x08^\xe4%YO\xd5c_\xa2\x96L\xcf\x18': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'val', 'type': 'bytes'}], 'name': 'log_named_bytes', 'type': 'event'}, b'\xaf\xb7\x95\xc9\xc6\x1eO\xe7F\x8c8o\x92]zT)\xec\xad\x9c\x04\x95\xdd\xb8\xd3\x8di\x06\x14\xd3/\x99': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'val', 'type': 'bytes32'}], 'name': 'log_named_bytes32', 'type': 'event'}, b']\xa6\xce\x9dQ\x15\x1b\xa1\x0c\t\xa5Y\xef$\xd5 \xb9\xda\xc5\xc5\xb8\x81\n\xe8CNM\r\x86A\x1a\x95': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_int', 'type': 'event'}, b"\xeb\x8b\xa4<\xedu7B\x19F\xbdC\xe8(\xb8\xb2\xb8B\x89'\xaa\x8f\x80\x1c\x13\xd94\xbf\x11\xac\xa5{": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_uint', 'type': 'event'}, b'/\xe62w\x91t7CxD*\x8e\x97\x8b\xcc\xfb\xdc\xc1\xd6\xb2\xb0\xd8\x1f~\x8e\xb7v\xab"\x86\xf1h': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}], 'name': 'log_named_int', 'type': 'event'}, b'(\x0fDF\xb2\x8a\x13rA}\xdae\x8d0\xb9[)\x92\xb1*\xc9\xc7\xf3xS_)\xa9z\xcf5\x83': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'val', 'type': 'string'}], 'name': 'log_named_string', 'type': 'event'}, b'\xb2\xde/\xbe\x80\x1a\r\xf6\xc0\xcb\xdd\xfdD\x8b\xa3\xc4\x1dH\xa0@\xca5\xc5l\x81\x96\xef\x0f\xca\xe7!\xa8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}], 'name': 'log_named_uint', 'type': 'event'}, b'\x0b.\x13\xff \xac{GA\x98eU\x83\xed\xf7\r\xed\xd2\xc1\xdc\x98\x0e2\x9cO\xbb/\xc0t\x8byk': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log_string', 'type': 'event'}, b',\xab\x97\x90Q\x0f\xd8\xbd\xfb\xd2\x11R\x88\xdb3\xfe\xc6f\x91\xd4v\xef\xc5B|\xfdL\ti0\x17U': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'log_uint', 'type': 'event'}, b"\xe7\x95\x0e\xde\x03\x94\xb9\xf2\xceJZ\x1b\xf5\xa7\xe1\x85$\x11\xf7\xe6f\x1bC\x08\xc9\x13\xc4\xbf\xd1\x10'\xe4": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'logs', 'type': 'event'}, b'\xfav&\xd4': {'inputs': [], 'name': 'IS_TEST', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb5P\x8a\xa9': {'inputs': [], 'name': 'excludeArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'excludedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe2\x0c\x9fq': {'inputs': [], 'name': 'excludeContracts', 'outputs': [{'internalType': 'address[]', 'name': 'excludedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb0FO\xdc': {'inputs': [], 'name': 'excludeSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'excludedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1e\xd7\x83\x1c': {'inputs': [], 'name': 'excludeSenders', 'outputs': [{'internalType': 'address[]', 'name': 'excludedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbaAO\xa6': {'inputs': [], 'name': 'failed', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xf2\xc9\xec\xd8': {'inputs': [], 'name': 'getNumber', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'pure', 'type': 'function'}, b'f\xd9\xa9\xa0': {'inputs': [], 'name': 'targetArtifactSelectors', 'outputs': [{'components': [{'internalType': 'string', 'name': 'artifact', 'type': 'string'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzArtifactSelector[]', 'name': 'targetedArtifactSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x85"l\x81': {'inputs': [], 'name': 'targetArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'targetedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'?r\x86\xf4': {'inputs': [], 'name': 'targetContracts', 'outputs': [{'internalType': 'address[]', 'name': 'targetedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'*\xde8\x80': {'inputs': [], 'name': 'targetInterfaces', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'string[]', 'name': 'artifacts', 'type': 'string[]'}], 'internalType': 'struct StdInvariant.FuzzInterface[]', 'name': 'targetedInterfaces_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x91j\x17\xc6': {'inputs': [], 'name': 'targetSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'targetedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'>^<#': {'inputs': [], 'name': 'targetSenders', 'outputs': [{'internalType': 'address[]', 'name': 'targetedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b';\xcf\xb7#': {'inputs': [{'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}], 'name': 'testCloneDeterministicDirty', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x029\xed\xbe': {'inputs': [], 'name': 'testCloneDirty', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd55j\x89': {'inputs': [{'internalType': 'bytes', 'name': 'args', 'type': 'bytes'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}], 'name': 'testFetchCloneArgs', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xeb\xfb\xddF': {'inputs': [{'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}], 'name': 'testPredictDeterministicAddressDirty', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\xb3\t[\x99': {'inputs': [{'internalType': 'address', 'name': 'implementation', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}], 'name': 'testSymbolicPredictDeterministicAddressSpillage', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'R\x01[\xbf': {'inputs': [{'internalType': 'address', 'name': 'implementation', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'args', 'type': 'bytes'}], 'name': 'testSymbolicPredictDeterministicAddressWithImmutableArgsSpillage', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":46,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"stdstore","offset":0,"slot":0,"type":"t_struct(StdStorage)8331_storage"},{"astId":209,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"_failed","offset":0,"slot":8,"type":"t_bool"},{"astId":2943,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"stdChainsInitialized","offset":1,"slot":8,"type":"t_bool"},{"astId":2964,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"chains","offset":0,"slot":9,"type":"t_mapping(t_string_memory_ptr,t_struct(Chain)2959_storage)"},{"astId":2968,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"defaultRpcUrls","offset":0,"slot":10,"type":"t_mapping(t_string_memory_ptr,t_string_storage)"},{"astId":2972,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"idToAlias","offset":0,"slot":11,"type":"t_mapping(t_uint256,t_string_storage)"},{"astId":2975,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"fallbackToDefaultRpcUrls","offset":0,"slot":12,"type":"t_bool"},{"astId":3931,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"gasMeteringOff","offset":1,"slot":12,"type":"t_bool"},{"astId":6002,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"stdstore","offset":0,"slot":13,"type":"t_struct(StdStorage)8331_storage"},{"astId":6923,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"_excludedContracts","offset":0,"slot":21,"type":"t_array(t_address)dyn_storage"},{"astId":6926,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"_excludedSenders","offset":0,"slot":22,"type":"t_array(t_address)dyn_storage"},{"astId":6929,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"_targetedContracts","offset":0,"slot":23,"type":"t_array(t_address)dyn_storage"},{"astId":6932,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"_targetedSenders","offset":0,"slot":24,"type":"t_array(t_address)dyn_storage"},{"astId":6935,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"_excludedArtifacts","offset":0,"slot":25,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6938,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"_targetedArtifacts","offset":0,"slot":26,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6942,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"_targetedArtifactSelectors","offset":0,"slot":27,"type":"t_array(t_struct(FuzzArtifactSelector)6914_storage)dyn_storage"},{"astId":6946,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"_excludedSelectors","offset":0,"slot":28,"type":"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage"},{"astId":6950,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"_targetedSelectors","offset":0,"slot":29,"type":"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage"},{"astId":6954,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"_targetedInterfaces","offset":0,"slot":30,"type":"t_array(t_struct(FuzzInterface)6920_storage)dyn_storage"},{"astId":13223,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"IS_TEST","offset":0,"slot":31,"type":"t_bool"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_address)dyn_storage":{"encoding":"dynamic_array","label":"address[]","numberOfBytes":32,"base":"t_address"},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_array(t_bytes4)dyn_storage":{"encoding":"dynamic_array","label":"bytes4[]","numberOfBytes":32,"base":"t_bytes4"},"t_array(t_string_storage)dyn_storage":{"encoding":"dynamic_array","label":"string[]","numberOfBytes":32,"base":"t_string_storage"},"t_array(t_struct(FuzzArtifactSelector)6914_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzArtifactSelector[]","numberOfBytes":32,"base":"t_struct(FuzzArtifactSelector)6914_storage"},"t_array(t_struct(FuzzInterface)6920_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzInterface[]","numberOfBytes":32,"base":"t_struct(FuzzInterface)6920_storage"},"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzSelector[]","numberOfBytes":32,"base":"t_struct(FuzzSelector)6908_storage"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))"},"t_mapping(t_bytes32,t_struct(FindData)8306_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)8306_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)8306_storage)"},"t_mapping(t_string_memory_ptr,t_string_storage)":{"encoding":"mapping","label":"mapping(string => string)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_string_storage"},"t_mapping(t_string_memory_ptr,t_struct(Chain)2959_storage)":{"encoding":"mapping","label":"mapping(string => struct StdChains.Chain)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_struct(Chain)2959_storage"},"t_mapping(t_uint256,t_string_storage)":{"encoding":"mapping","label":"mapping(uint256 => string)","numberOfBytes":32,"key":"t_uint256","value":"t_string_storage"},"t_string_memory_ptr":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(Chain)2959_storage":{"encoding":"inplace","label":"struct StdChains.Chain","numberOfBytes":128,"members":[{"astId":2952,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"name","offset":0,"slot":0,"type":"t_string_storage"},{"astId":2954,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"chainId","offset":0,"slot":1,"type":"t_uint256"},{"astId":2956,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"chainAlias","offset":0,"slot":2,"type":"t_string_storage"},{"astId":2958,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"rpcUrl","offset":0,"slot":3,"type":"t_string_storage"}]},"t_struct(FindData)8306_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":8299,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":8301,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":8303,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":8305,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(FuzzArtifactSelector)6914_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzArtifactSelector","numberOfBytes":64,"members":[{"astId":6910,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"artifact","offset":0,"slot":0,"type":"t_string_storage"},{"astId":6913,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(FuzzInterface)6920_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzInterface","numberOfBytes":64,"members":[{"astId":6916,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6919,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"artifacts","offset":0,"slot":1,"type":"t_array(t_string_storage)dyn_storage"}]},"t_struct(FuzzSelector)6908_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzSelector","numberOfBytes":64,"members":[{"astId":6904,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6907,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(StdStorage)8331_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":8315,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))"},{"astId":8318,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":8320,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":8322,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":8324,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":8326,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":8328,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":8330,"contract":"lib/openzeppelin-contracts/test/proxy/Clones.t.sol:ClonesTest","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60808060405234602f57600160ff19600c541617600c55600160ff19601f541617601f5561193690816100348239f35b5f80fdfe60806040526004361015610011575f80fd5b5f5f3560e01c80630239edbe14610fb95780631ed7831c14610f3c5780632ade388014610d815780633bcfb72314610ba35780633e5e3c2314610b265780633f7286f414610aa957806352015bbf146109c757806366d9a9a0146108a657806385226c811461081c578063916a17c614610774578063b0464fdc146106cc578063b3095b991461063d578063b5508aa9146105b3578063ba414fa61461058e578063d5356a8914610281578063e20c9f71146101f3578063ebfbdd461461012c578063f2c9ecd8146101105763fa7626d4146100eb575f80fd5b3461010d578060031936011261010d57602060ff601f54166040519015158152f35b80fd5b503461010d578060031936011261010d576020604051602a8152f35b503461010d57602036600319011261010d578060043561014d3082306117b8565b906001600160a01b039061016d9030906001600160a01b031982176117b8565b6001600160a01b039092169116808203610185575050f35b5f5160206118e15f395f51905f523b156101ef57604051916328a9b0fb60e11b83526004830152602482015281816044815f5160206118e15f395f51905f525afa80156101e4576101d35750f35b816101dd91611095565b61010d5780f35b6040513d84823e3d90fd5b5050fd5b503461010d578060031936011261010d5760405160158054808352908352909160208301917f55f448fdea98c4d29eb340757ef0a66cd03dbb9538908a6a81d96026b71ec475915b8181106102625761025e8561025281870382611095565b60405191829182610fe9565b0390f35b82546001600160a01b031684526020909301926001928301920161023b565b503461010d57604036600319011261010d5760043567ffffffffffffffff811161058a576102b39036906004016110d3565b8161bfd38251105f5160206118e15f395f51905f523b1561058a5760405190632631f2b160e11b8252600482015281816024815f5160206118e15f395f51905f525afa80156101e457610575575b505061030d813061181a565b60208151910183f06001600160a01b0381169190821561056657610331823061181a565b8051156105575780516024359160200186f5926001600160a01b03841680156105365760206004926103746103658661122c565b61036e8961122c565b906115d3565b604051631e593d9b60e31b815293849182905afa918215610477578692610502575b50604051631e593d9b60e31b815291602083600481305afa9283156104f75787936104bf575b50906103cc60049360209361164d565b604051631e593d9b60e31b815292839182905afa9081156104b4578591610482575b50604051631e593d9b60e31b815290602082600481305afa91821561047757869261043b575b50836104336104339461042e610438989561042e9561164d565b6116a7565b6115d3565b80f35b949150916020853d60201161046f575b8161045860209383611095565b8101031261046b57935190939183610414565b5f80fd5b3d915061044b565b6040513d88823e3d90fd5b90506020813d6020116104ac575b8161049d60209383611095565b8101031261046b57515f6103ee565b3d9150610490565b6040513d87823e3d90fd5b9250906020833d6020116104ef575b816104db60209383611095565b8101031261046b57915191906103cc6103bc565b3d91506104ce565b6040513d89823e3d90fd5b9091506020813d60201161052e575b8161051e60209383611095565b8101031261046b5751905f610396565b3d9150610511565b853d61054b5763b06ebf3d60e01b8152600490fd5b604051903d90823e3d90fd5b631328927760e21b8552600485fd5b63b06ebf3d60e01b8452600484fd5b8161057f91611095565b61058a57815f610301565b5080fd5b503461010d578060031936011261010d5760206105a9611538565b6040519015158152f35b503461010d578060031936011261010d576019546105d081611252565b916105de6040519384611095565b818352601981527f944998273e477b495144fb8794c914197f3ccb46be2900f4698fd0ef743c9695602084015b838310610620576040518061025e8782611156565b60016020819261062f8561126a565b81520192019201919061060b565b503461010d57604036600319011261010d578061065861104f565b6001600160a01b031990610671903090602435906117b8565b168061067a5750f35b5f5160206118e15f395f51905f523b156106c95760405190637c84c69b60e01b8252600482015281602482015281816044815f5160206118e15f395f51905f525afa80156101e4576101d35750f35b50fd5b503461010d578060031936011261010d57601c546106e981611252565b916106f76040519384611095565b818352601c81527f0e4562a10381dec21b205ed72637e6b1b523bdd0e4d4d50af5cd23dd4500a211602084015b838310610739576040518061025e87826111b5565b6002602060019260405161074c81611065565b848060a01b038654168152610762858701611336565b83820152815201920192019190610724565b503461010d578060031936011261010d57601d5461079181611252565b9161079f6040519384611095565b818352601d81527f6d4407e7be21f808e6509aa9fa9143369579dd7d760fe20a2c09680fc146134f602084015b8383106107e1576040518061025e87826111b5565b600260206001926040516107f481611065565b848060a01b03865416815261080a858701611336565b838201528152019201920191906107cc565b503461010d578060031936011261010d57601a5461083981611252565b916108476040519384611095565b818352601a81527f057c384a7d1c54f3a1b2e5e67b2617b8224fdfd1ea7234eea573a6ff665ff63e602084015b838310610889576040518061025e8782611156565b6001602081926108988561126a565b815201920192019190610874565b503461010d578060031936011261010d57601b546108c381611252565b6108d06040519182611095565b818152601b83526020810191837f3ad8aa4f87544323a9d1e5dd902f40c356527a7955687113db5f9a85ad579dc1845b83831061098c57868587604051928392602084019060208552518091526040840160408260051b8601019392905b82821061093d57505050500390f35b9193600191939550602061097c8192603f198a82030186528851908361096c835160408452604084019061102b565b9201519084818403910152611119565b960192019201859493919261092e565b6002602060019260405161099f81611065565b6109a88661126a565b81526109b5858701611336565b83820152815201920192019190610900565b503461046b57606036600319011261046b576109e161104f565b60443567ffffffffffffffff811161046b57610a019036906004016110d3565b9061bfd38251105f5160206118e15f395f51905f523b1561046b5760405190632631f2b160e11b825260048201525f816024815f5160206118e15f395f51905f525afa8015610a9e57610a7e575b50610a5e60ff92600b9261181a565b602081519101206040519060408201526024356020820152308152015380f35b600b91935060ff92610a935f610a5e93611095565b5f9492509250610a4f565b6040513d5f823e3d90fd5b3461046b575f36600319011261046b57604051601780548083525f91825260208301917fc624b66cc0138b8fabc209247f72d758e1cf3343756d543badbf24212bed8c1591905b818110610b075761025e8561025281870382611095565b82546001600160a01b0316845260209093019260019283019201610af0565b3461046b575f36600319011261046b57604051601880548083525f91825260208301917fb13d2d76d1f4b7be834882e410b3e3a8afaf69f83600ae24db354391d2378d2e91905b818110610b845761025e8561025281870382611095565b82546001600160a01b0316845260209093019260019283019201610b6d565b3461046b57602036600319011261046b57600480356020610bd9610bc78330611764565b9219306001600160a01b031917611764565b91610bef610be68261122c565b61036e8561122c565b604051631e593d9b60e31b815293849182906001600160a01b03165afa918215610a9e575f92610d4d575b50604051631e593d9b60e31b815291602083600481305afa928315610a9e575f93610d15575b5090610c5060049360209361164d565b604051631e593d9b60e31b815292839182906001600160a01b03165afa908115610a9e575f91610ce3575b50604051631e593d9b60e31b815290602082600481305afa908115610a9e575f91610cad575b610cab925061164d565b005b90506020823d602011610cdb575b81610cc860209383611095565b8101031261046b57610cab915190610ca1565b3d9150610cbb565b90506020813d602011610d0d575b81610cfe60209383611095565b8101031261046b575181610c7b565b3d9150610cf1565b9250906020833d602011610d45575b81610d3160209383611095565b8101031261046b5791519190610c50610c40565b3d9150610d24565b9091506020813d602011610d79575b81610d6960209383611095565b8101031261046b57519082610c1a565b3d9150610d5c565b3461046b575f36600319011261046b57601e54610d9d81611252565b90610dab6040519283611095565b808252601e5f9081526020830191907f50bb669a95c7b50b7e8a6f09454034b2b14cf2b85c730dca9a539ca82cb6e350835b838310610eb157848660405191829160208301906020845251809152604083019060408160051b85010192915f905b828210610e1b57505050500390f35b919390929450603f198682030182528451906020604082019260018060a01b0381511683520151916040602083015282518091526060820190602060608260051b8501019401925f5b828110610e865750505050506020806001929601920192018594939192610e0c565b9091929394602080610ea4600193605f19878203018952895161102b565b9701950193929101610e64565b604051610ebd81611065565b82546001600160a01b03168152600183018054610ed981611252565b91610ee76040519384611095565b81835260208301905f5260205f20905f905b838210610f1f575050505060019282602092836002950152815201920192019190610ddd565b600160208192610f2e8661126a565b815201930191019091610ef9565b3461046b575f36600319011261046b57604051601680548083525f91825260208301917fd833147d7dc355ba459fc788f669e58cfaf9dc25ddcd0702e87d69c7b512428991905b818110610f9a5761025e8561025281870382611095565b82546001600160a01b0316845260209093019260019283019201610f83565b3461046b575f36600319011261046b576004610fd430611701565b6020610bd9306001600160a01b031917611701565b60206040818301928281528451809452019201905f5b81811061100c5750505090565b82516001600160a01b0316845260209384019390920191600101610fff565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b600435906001600160a01b038216820361046b57565b6040810190811067ffffffffffffffff82111761108157604052565b634e487b7160e01b5f52604160045260245ffd5b90601f8019910116810190811067ffffffffffffffff82111761108157604052565b67ffffffffffffffff811161108157601f01601f191660200190565b81601f8201121561046b578035906110ea826110b7565b926110f86040519485611095565b8284526020838301011161046b57815f926020809301838601378301015290565b90602080835192838152019201905f5b8181106111365750505090565b82516001600160e01b031916845260209384019390920191600101611129565b602081016020825282518091526040820191602060408360051b8301019401925f915b83831061118857505050505090565b90919293946020806111a6600193603f19868203018752895161102b565b97019301930191939290611179565b602081016020825282518091526040820191602060408360051b8301019401925f915b8383106111e757505050505090565b909192939460208061121d600193603f198682030187526040838b51878060a01b03815116845201519181858201520190611119565b970193019301919392906111d8565b90813b5f611239826110b7565b936112476040519586611095565b82855260208501903c565b67ffffffffffffffff81116110815760051b60200190565b90604051915f8154908160011c926001831692831561132c575b6020851084146113185784875286939081156112f657506001146112b2575b506112b092500383611095565b565b90505f9291925260205f20905f915b8183106112da5750509060206112b0928201015f6112a3565b60209193508060019154838589010152019101909184926112c1565b9050602092506112b094915060ff191682840152151560051b8201015f6112a3565b634e487b7160e01b5f52602260045260245ffd5b93607f1693611284565b90604051918281549182825260208201905f5260205f20925f905b806007830110611493576112b0945491818110611474575b818110611455575b818110611436575b818110611417575b8181106113f8575b8181106113d9575b8181106113bc575b106113a7575b500383611095565b6001600160e01b03191681526020015f61139f565b602083811b6001600160e01b031916855290930192600101611399565b604083901b6001600160e01b0319168452602090930192600101611391565b606083901b6001600160e01b0319168452602090930192600101611389565b608083901b6001600160e01b0319168452602090930192600101611381565b60a083901b6001600160e01b0319168452602090930192600101611379565b60c083901b6001600160e01b0319168452602090930192600101611371565b60e083901b6001600160e01b0319168452602090930192600101611369565b916008919350610100600191865463ffffffff60e01b8160e01b16825263ffffffff60e01b8160c01b16602083015263ffffffff60e01b8160a01b16604083015263ffffffff60e01b8160801b16606083015263ffffffff60e01b8160601b16608083015263ffffffff60e01b8160401b1660a083015263ffffffff60e01b8160201b1660c083015263ffffffff60e01b1660e0820152019401920185929391611351565b60085460ff161561154857600190565b604051630667f9d760e41b81525f5160206118e15f395f51905f5260048201526519985a5b195960d21b60248201526020816044815f5160206118e15f395f51905f525afa908115610a9e575f916115a1575b50151590565b90506020813d6020116115cb575b816115bc60209383611095565b8101031261046b57515f61159b565b3d91506115af565b5f5160206118e15f395f51905f523b1561046b576116125f916116246040519485938493639762463160e01b855260406004860152604485019061102b565b8381036003190160248501529061102b565b03815f5160206118e15f395f51905f525afa8015610a9e576116435750565b5f6112b091611095565b90808203611659575050565b5f5160206118e15f395f51905f523b1561046b576040519163260a5b1560e21b8352600483015260248201525f816044815f5160206118e15f395f51905f525afa8015610a9e576116435750565b803b90602c1982019182116116ed57602d6116da6116c4846110b7565b936116d26040519586611095565b8085526110b7565b6020840190601f19013682378351923c90565b634e487b7160e01b5f52601160045260245ffd5b6e5af43d82803e903d91602b57fd5bf390763d602d80600a3d3981f3363d3d373d3d3d363d7300000062ffffff8260881c16175f5260781b17602052603760095ff0906001600160a01b0382161561175557565b63b06ebf3d60e01b5f5260045ffd5b6e5af43d82803e903d91602b57fd5bf390763d602d80600a3d3981f3363d3d373d3d3d363d7300000062ffffff8260881c16175f5260781b17602052603760095ff5906001600160a01b0382161561175557565b60405160388101939093526f5af43d82803e903d91602b57fd5bf3ff60248401526014830152733d602d80600a3d3981f3363d3d373d3d3d363d73825260588201526037600c820120607882015260556043909101206001600160a01b031690565b90615fd38151116118d157805190602d82018092116116ed57604051606160f81b60208281019190915260f09390931b6001600160f01b0319166021820152703d81600a3d39f3363d3d373d3d3d363d7360781b602382015260609390931b6bffffffffffffffffffffffff191660348401526e5af43d82803e903d91602b57fd5bf360881b604884015280516118ce926057928592918291018385015e81015f838201520301601f198101835282611095565b90565b63250a241560e21b5f5260045ffdfe0000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da2646970667358221220f3b6bd9d44ba66ba290d977f449243559ff9f6a2aa2752a1f7729d1ab2f0e08364736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ClonesTest:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ClonesTest]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ClonesTest, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ClonesTest]]:
        return cls._deploy(request_type, [], return_tx, ClonesTest, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def getNumber(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#9)

        Returns:
            uint256
        """
        ...

    @overload
    def getNumber(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#9)

        Returns:
            uint256
        """
        ...

    @overload
    def getNumber(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#9)

        Returns:
            uint256
        """
        ...

    @overload
    def getNumber(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#9)

        Returns:
            uint256
        """
        ...

    def getNumber(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#9)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "f2c9ecd8", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testSymbolicPredictDeterministicAddressSpillage(self, implementation: Union[Account, Address], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#13)

        Args:
            implementation: address
            salt: bytes32
        """
        ...

    @overload
    def testSymbolicPredictDeterministicAddressSpillage(self, implementation: Union[Account, Address], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#13)

        Args:
            implementation: address
            salt: bytes32
        """
        ...

    @overload
    def testSymbolicPredictDeterministicAddressSpillage(self, implementation: Union[Account, Address], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#13)

        Args:
            implementation: address
            salt: bytes32
        """
        ...

    @overload
    def testSymbolicPredictDeterministicAddressSpillage(self, implementation: Union[Account, Address], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#13)

        Args:
            implementation: address
            salt: bytes32
        """
        ...

    def testSymbolicPredictDeterministicAddressSpillage(self, implementation: Union[Account, Address], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#13)

        Args:
            implementation: address
            salt: bytes32
        """
        return self._execute(self.chain, request_type, "b3095b99", [implementation, salt], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testSymbolicPredictDeterministicAddressWithImmutableArgsSpillage(self, implementation: Union[Account, Address], salt: bytes32, args: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#22)

        Args:
            implementation: address
            salt: bytes32
            args: bytes
        """
        ...

    @overload
    def testSymbolicPredictDeterministicAddressWithImmutableArgsSpillage(self, implementation: Union[Account, Address], salt: bytes32, args: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#22)

        Args:
            implementation: address
            salt: bytes32
            args: bytes
        """
        ...

    @overload
    def testSymbolicPredictDeterministicAddressWithImmutableArgsSpillage(self, implementation: Union[Account, Address], salt: bytes32, args: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#22)

        Args:
            implementation: address
            salt: bytes32
            args: bytes
        """
        ...

    @overload
    def testSymbolicPredictDeterministicAddressWithImmutableArgsSpillage(self, implementation: Union[Account, Address], salt: bytes32, args: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#22)

        Args:
            implementation: address
            salt: bytes32
            args: bytes
        """
        ...

    def testSymbolicPredictDeterministicAddressWithImmutableArgsSpillage(self, implementation: Union[Account, Address], salt: bytes32, args: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#22)

        Args:
            implementation: address
            salt: bytes32
            args: bytes
        """
        return self._execute(self.chain, request_type, "52015bbf", [implementation, salt, args], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testCloneDirty(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#38)
        """
        ...

    @overload
    def testCloneDirty(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#38)
        """
        ...

    @overload
    def testCloneDirty(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#38)
        """
        ...

    @overload
    def testCloneDirty(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#38)
        """
        ...

    def testCloneDirty(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#38)
        """
        return self._execute(self.chain, request_type, "0239edbe", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testCloneDeterministicDirty(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#50)

        Args:
            salt: bytes32
        """
        ...

    @overload
    def testCloneDeterministicDirty(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#50)

        Args:
            salt: bytes32
        """
        ...

    @overload
    def testCloneDeterministicDirty(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#50)

        Args:
            salt: bytes32
        """
        ...

    @overload
    def testCloneDeterministicDirty(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#50)

        Args:
            salt: bytes32
        """
        ...

    def testCloneDeterministicDirty(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#50)

        Args:
            salt: bytes32
        """
        return self._execute(self.chain, request_type, "3bcfb723", [salt], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testPredictDeterministicAddressDirty(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#62)

        Args:
            salt: bytes32
        """
        ...

    @overload
    def testPredictDeterministicAddressDirty(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#62)

        Args:
            salt: bytes32
        """
        ...

    @overload
    def testPredictDeterministicAddressDirty(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#62)

        Args:
            salt: bytes32
        """
        ...

    @overload
    def testPredictDeterministicAddressDirty(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#62)

        Args:
            salt: bytes32
        """
        ...

    def testPredictDeterministicAddressDirty(self, salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#62)

        Args:
            salt: bytes32
        """
        return self._execute(self.chain, request_type, "ebfbdd46", [salt], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFetchCloneArgs(self, args: Union[bytearray, bytes], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#70)

        Args:
            args: bytes
            salt: bytes32
        """
        ...

    @overload
    def testFetchCloneArgs(self, args: Union[bytearray, bytes], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#70)

        Args:
            args: bytes
            salt: bytes32
        """
        ...

    @overload
    def testFetchCloneArgs(self, args: Union[bytearray, bytes], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#70)

        Args:
            args: bytes
            salt: bytes32
        """
        ...

    @overload
    def testFetchCloneArgs(self, args: Union[bytearray, bytes], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#70)

        Args:
            args: bytes
            salt: bytes32
        """
        ...

    def testFetchCloneArgs(self, args: Union[bytearray, bytes], salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/proxy/Clones.t.sol#70)

        Args:
            args: bytes
            salt: bytes32
        """
        return self._execute(self.chain, request_type, "d5356a89", [args, salt], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ClonesTest.getNumber.selector = bytes4(b'\xf2\xc9\xec\xd8')
ClonesTest.testSymbolicPredictDeterministicAddressSpillage.selector = bytes4(b'\xb3\t[\x99')
ClonesTest.testSymbolicPredictDeterministicAddressWithImmutableArgsSpillage.selector = bytes4(b'R\x01[\xbf')
ClonesTest.testCloneDirty.selector = bytes4(b'\x029\xed\xbe')
ClonesTest.testCloneDeterministicDirty.selector = bytes4(b';\xcf\xb7#')
ClonesTest.testPredictDeterministicAddressDirty.selector = bytes4(b'\xeb\xfb\xddF')
ClonesTest.testFetchCloneArgs.selector = bytes4(b'\xd55j\x89')
