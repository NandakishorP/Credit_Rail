
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.forgestd.src.LibVariable import LibVariable
from pytypes.lib.forgestd.src.Test import Test

from pytypes.lib.forgestd.src.LibVariable import Type
from pytypes.lib.forgestd.src.LibVariable import Variable



class LibVariableTest(Test):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#7)
    """
    _abi = {b'\xb0,\xf7\x1d': {'inputs': [{'internalType': 'string', 'name': 'expected', 'type': 'string'}, {'internalType': 'string', 'name': 'actual', 'type': 'string'}], 'name': 'TypeMismatch', 'type': 'error'}, b'A0O\xac\xd92=u\xb1\x1b\xcd\xd6\t\xcb8\xef\xff\xfd\xb0W\x10\xf7\xca\xf0\xe9\xb1lm\x9dp\x9fP': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log', 'type': 'event'}, b'z\xe7LRt\x14\xae\x13_\xd9pG\xb1)!\xa5\xec9\x11\xb8\x04\x19xU\xd6~%\xc7\xb7^\xe6\xf3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'log_address', 'type': 'event'}, b'\xfb\x10(e\xd5\n\xdd\xdd\xf6\x9d\xa9\xb5\xaa\x1b\xce\xd6l\x80\xcf\x86\x9a\\\x8d\x04q\xa4g\xe1\x8c\xe9\xca\xb1': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_array', 'type': 'event'}, b'\x89\n\x82g\x9bG\x0f+\xd8(\x16\xed\x9b\x16\x1f\x97\xd8\xb9g\xf3\x7f\xa3d|!\xd5\xbf9t\x9e-\xd5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_array', 'type': 'event'}, b'@\xe1\x84\x0fWi\x07=a\xbd\x017-\x9bu\xba\xa9\x84-V)\xa0\xc9\x9f\xf1\x03\xbe\x11x\xa8\xe9\xe2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_array', 'type': 'event'}, b'#\xb6*\xd0XM$\xa7_\x0b\xf3V\x03\x91\xefVY\xecm\xb1&\x9cV\xe1\x1a\xa2A\xd67\xf1\x9b ': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'log_bytes', 'type': 'event'}, b'\xe8\x16\x99\xb8Q\x13\xee\xa1\xc7>\x10X\x8b+\x03^U\x893ic!s\xaf\xd4?\xeb\x19/\xacd\xe3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'log_bytes32', 'type': 'event'}, b'\x0e\xb5\xd5&$\xc8\xd2\x8a\xda\x9f\xc5Z\x8cP.\xd5\xaa?\xbe/\xb6\xe9\x1bq\xb5\xf3v\x88+\x1d/\xb8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256', 'name': '', 'type': 'int256'}], 'name': 'log_int', 'type': 'event'}, b'\x9cN\x85A\xca\x8f\r\xc1\xc4\x13\xf9\x10\x8ff\xd8-<\xec\xb1\xbd\xdb\xceCza\xca\xa3\x17\\L\xc9o': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address', 'name': 'val', 'type': 'address'}], 'name': 'log_named_address', 'type': 'event'}, b'\x00\xaa\xa3\x9c\x9f\xfb_VzE48\x0cspup.\x1f\x7f\x14\x10\x7f\xc9S(\xe3\xb5l\x03%\xfb': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xa7>\xda\tf/F\xdd\xe7)\xbeF\x118_\xf3O\xe6\xc4O\xbb\xc6\xf7\xe1{\x04+Y\xa3D[W': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_named_array', 'type': 'event'}, b";\xcf\xb2\xae.\x8d\x13-\xd1\xfc\xe7\xcf'\x8a\x9a\x19uj\x9f\xce\xab\xe4p\xdf;\xda\xbbK\xc5w\xd1\xbd": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xd2n\x16\xca\xd4T\x87\x05\xe4\xc9\xe2\xd9O\x98\xee\x91\xc2\x89\x08^\xe4%YO\xd5c_\xa2\x96L\xcf\x18': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'val', 'type': 'bytes'}], 'name': 'log_named_bytes', 'type': 'event'}, b'\xaf\xb7\x95\xc9\xc6\x1eO\xe7F\x8c8o\x92]zT)\xec\xad\x9c\x04\x95\xdd\xb8\xd3\x8di\x06\x14\xd3/\x99': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'val', 'type': 'bytes32'}], 'name': 'log_named_bytes32', 'type': 'event'}, b']\xa6\xce\x9dQ\x15\x1b\xa1\x0c\t\xa5Y\xef$\xd5 \xb9\xda\xc5\xc5\xb8\x81\n\xe8CNM\r\x86A\x1a\x95': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_int', 'type': 'event'}, b"\xeb\x8b\xa4<\xedu7B\x19F\xbdC\xe8(\xb8\xb2\xb8B\x89'\xaa\x8f\x80\x1c\x13\xd94\xbf\x11\xac\xa5{": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_uint', 'type': 'event'}, b'/\xe62w\x91t7CxD*\x8e\x97\x8b\xcc\xfb\xdc\xc1\xd6\xb2\xb0\xd8\x1f~\x8e\xb7v\xab"\x86\xf1h': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}], 'name': 'log_named_int', 'type': 'event'}, b'(\x0fDF\xb2\x8a\x13rA}\xdae\x8d0\xb9[)\x92\xb1*\xc9\xc7\xf3xS_)\xa9z\xcf5\x83': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'val', 'type': 'string'}], 'name': 'log_named_string', 'type': 'event'}, b'\xb2\xde/\xbe\x80\x1a\r\xf6\xc0\xcb\xdd\xfdD\x8b\xa3\xc4\x1dH\xa0@\xca5\xc5l\x81\x96\xef\x0f\xca\xe7!\xa8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}], 'name': 'log_named_uint', 'type': 'event'}, b'\x0b.\x13\xff \xac{GA\x98eU\x83\xed\xf7\r\xed\xd2\xc1\xdc\x98\x0e2\x9cO\xbb/\xc0t\x8byk': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log_string', 'type': 'event'}, b',\xab\x97\x90Q\x0f\xd8\xbd\xfb\xd2\x11R\x88\xdb3\xfe\xc6f\x91\xd4v\xef\xc5B|\xfdL\ti0\x17U': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'log_uint', 'type': 'event'}, b"\xe7\x95\x0e\xde\x03\x94\xb9\xf2\xceJZ\x1b\xf5\xa7\xe1\x85$\x11\xf7\xe6f\x1bC\x08\xc9\x13\xc4\xbf\xd1\x10'\xe4": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'logs', 'type': 'event'}, b'\xfav&\xd4': {'inputs': [], 'name': 'IS_TEST', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb5P\x8a\xa9': {'inputs': [], 'name': 'excludeArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'excludedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe2\x0c\x9fq': {'inputs': [], 'name': 'excludeContracts', 'outputs': [{'internalType': 'address[]', 'name': 'excludedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb0FO\xdc': {'inputs': [], 'name': 'excludeSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'excludedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1e\xd7\x83\x1c': {'inputs': [], 'name': 'excludeSenders', 'outputs': [{'internalType': 'address[]', 'name': 'excludedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbaAO\xa6': {'inputs': [], 'name': 'failed', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\n\x92T\xe4': {'inputs': [], 'name': 'setUp', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'f\xd9\xa9\xa0': {'inputs': [], 'name': 'targetArtifactSelectors', 'outputs': [{'components': [{'internalType': 'string', 'name': 'artifact', 'type': 'string'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzArtifactSelector[]', 'name': 'targetedArtifactSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x85"l\x81': {'inputs': [], 'name': 'targetArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'targetedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'?r\x86\xf4': {'inputs': [], 'name': 'targetContracts', 'outputs': [{'internalType': 'address[]', 'name': 'targetedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'*\xde8\x80': {'inputs': [], 'name': 'targetInterfaces', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'string[]', 'name': 'artifacts', 'type': 'string[]'}], 'internalType': 'struct StdInvariant.FuzzInterface[]', 'name': 'targetedInterfaces_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x91j\x17\xc6': {'inputs': [], 'name': 'targetSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'targetedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'>^<#': {'inputs': [], 'name': 'targetSenders', 'outputs': [{'internalType': 'address[]', 'name': 'targetedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\n\x1c\x9ct': {'inputs': [], 'name': 'testRevert_NotInitialized', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xad\xec\xb4\xaf': {'inputs': [], 'name': 'testRevert_TypeMismatch', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'`\xe9\xd8$': {'inputs': [], 'name': 'testRevert_UnsafeCast', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xafXN\xee': {'inputs': [], 'name': 'testRevert_assertExists', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa4\xb9\xd9\xed': {'inputs': [], 'name': 'test_Coercion', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\xd4D6\xcb': {'inputs': [], 'name': 'test_Downcasting', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\t\xbdu\x9b': {'inputs': [], 'name': 'test_TypeHelpers', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":46,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"stdstore","offset":0,"slot":0,"type":"t_struct(StdStorage)10176_storage"},{"astId":2054,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"_failed","offset":0,"slot":8,"type":"t_bool"},{"astId":4788,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"stdChainsInitialized","offset":1,"slot":8,"type":"t_bool"},{"astId":4809,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"chains","offset":0,"slot":9,"type":"t_mapping(t_string_memory_ptr,t_struct(Chain)4804_storage)"},{"astId":4813,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"defaultRpcUrls","offset":0,"slot":10,"type":"t_mapping(t_string_memory_ptr,t_string_storage)"},{"astId":4817,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"idToAlias","offset":0,"slot":11,"type":"t_mapping(t_uint256,t_string_storage)"},{"astId":4820,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"fallbackToDefaultRpcUrls","offset":0,"slot":12,"type":"t_bool"},{"astId":5776,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"gasMeteringOff","offset":1,"slot":12,"type":"t_bool"},{"astId":7847,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"stdstore","offset":0,"slot":13,"type":"t_struct(StdStorage)10176_storage"},{"astId":8768,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"_excludedContracts","offset":0,"slot":21,"type":"t_array(t_address)dyn_storage"},{"astId":8771,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"_excludedSenders","offset":0,"slot":22,"type":"t_array(t_address)dyn_storage"},{"astId":8774,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"_targetedContracts","offset":0,"slot":23,"type":"t_array(t_address)dyn_storage"},{"astId":8777,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"_targetedSenders","offset":0,"slot":24,"type":"t_array(t_address)dyn_storage"},{"astId":8780,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"_excludedArtifacts","offset":0,"slot":25,"type":"t_array(t_string_storage)dyn_storage"},{"astId":8783,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"_targetedArtifacts","offset":0,"slot":26,"type":"t_array(t_string_storage)dyn_storage"},{"astId":8787,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"_targetedArtifactSelectors","offset":0,"slot":27,"type":"t_array(t_struct(FuzzArtifactSelector)8759_storage)dyn_storage"},{"astId":8791,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"_excludedSelectors","offset":0,"slot":28,"type":"t_array(t_struct(FuzzSelector)8753_storage)dyn_storage"},{"astId":8795,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"_targetedSelectors","offset":0,"slot":29,"type":"t_array(t_struct(FuzzSelector)8753_storage)dyn_storage"},{"astId":8799,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"_targetedInterfaces","offset":0,"slot":30,"type":"t_array(t_struct(FuzzInterface)8765_storage)dyn_storage"},{"astId":15068,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"IS_TEST","offset":0,"slot":31,"type":"t_bool"},{"astId":41672,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"helper","offset":1,"slot":31,"type":"t_contract(LibVariableHelper)43784"},{"astId":41674,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"expectedErr","offset":0,"slot":32,"type":"t_bytes_storage"},{"astId":41677,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"uninitVar","offset":0,"slot":33,"type":"t_struct(Variable)71_storage"},{"astId":41680,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"boolVar","offset":0,"slot":35,"type":"t_struct(Variable)71_storage"},{"astId":41683,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"addressVar","offset":0,"slot":37,"type":"t_struct(Variable)71_storage"},{"astId":41686,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"bytes32Var","offset":0,"slot":39,"type":"t_struct(Variable)71_storage"},{"astId":41689,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"uintVar","offset":0,"slot":41,"type":"t_struct(Variable)71_storage"},{"astId":41692,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"intVar","offset":0,"slot":43,"type":"t_struct(Variable)71_storage"},{"astId":41695,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"stringVar","offset":0,"slot":45,"type":"t_struct(Variable)71_storage"},{"astId":41698,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"bytesVar","offset":0,"slot":47,"type":"t_struct(Variable)71_storage"},{"astId":41701,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"boolArrayVar","offset":0,"slot":49,"type":"t_struct(Variable)71_storage"},{"astId":41704,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"addressArrayVar","offset":0,"slot":51,"type":"t_struct(Variable)71_storage"},{"astId":41707,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"bytes32ArrayVar","offset":0,"slot":53,"type":"t_struct(Variable)71_storage"},{"astId":41710,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"uintArrayVar","offset":0,"slot":55,"type":"t_struct(Variable)71_storage"},{"astId":41713,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"intArrayVar","offset":0,"slot":57,"type":"t_struct(Variable)71_storage"},{"astId":41716,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"stringArrayVar","offset":0,"slot":59,"type":"t_struct(Variable)71_storage"},{"astId":41719,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"bytesArrayVar","offset":0,"slot":61,"type":"t_struct(Variable)71_storage"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_address)dyn_storage":{"encoding":"dynamic_array","label":"address[]","numberOfBytes":32,"base":"t_address"},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_array(t_bytes4)dyn_storage":{"encoding":"dynamic_array","label":"bytes4[]","numberOfBytes":32,"base":"t_bytes4"},"t_array(t_string_storage)dyn_storage":{"encoding":"dynamic_array","label":"string[]","numberOfBytes":32,"base":"t_string_storage"},"t_array(t_struct(FuzzArtifactSelector)8759_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzArtifactSelector[]","numberOfBytes":32,"base":"t_struct(FuzzArtifactSelector)8759_storage"},"t_array(t_struct(FuzzInterface)8765_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzInterface[]","numberOfBytes":32,"base":"t_struct(FuzzInterface)8765_storage"},"t_array(t_struct(FuzzSelector)8753_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzSelector[]","numberOfBytes":32,"base":"t_struct(FuzzSelector)8753_storage"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_contract(LibVariableHelper)43784":{"encoding":"inplace","label":"contract LibVariableHelper","numberOfBytes":20},"t_enum(TypeKind)86":{"encoding":"inplace","label":"enum TypeKind","numberOfBytes":1},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)10151_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)10151_storage))"},"t_mapping(t_bytes32,t_struct(FindData)10151_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)10151_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)10151_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)10151_storage)"},"t_mapping(t_string_memory_ptr,t_string_storage)":{"encoding":"mapping","label":"mapping(string => string)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_string_storage"},"t_mapping(t_string_memory_ptr,t_struct(Chain)4804_storage)":{"encoding":"mapping","label":"mapping(string => struct StdChains.Chain)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_struct(Chain)4804_storage"},"t_mapping(t_uint256,t_string_storage)":{"encoding":"mapping","label":"mapping(uint256 => string)","numberOfBytes":32,"key":"t_uint256","value":"t_string_storage"},"t_string_memory_ptr":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(Chain)4804_storage":{"encoding":"inplace","label":"struct StdChains.Chain","numberOfBytes":128,"members":[{"astId":4797,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"name","offset":0,"slot":0,"type":"t_string_storage"},{"astId":4799,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"chainId","offset":0,"slot":1,"type":"t_uint256"},{"astId":4801,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"chainAlias","offset":0,"slot":2,"type":"t_string_storage"},{"astId":4803,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"rpcUrl","offset":0,"slot":3,"type":"t_string_storage"}]},"t_struct(FindData)10151_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":10144,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":10146,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":10148,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":10150,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(FuzzArtifactSelector)8759_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzArtifactSelector","numberOfBytes":64,"members":[{"astId":8755,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"artifact","offset":0,"slot":0,"type":"t_string_storage"},{"astId":8758,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(FuzzInterface)8765_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzInterface","numberOfBytes":64,"members":[{"astId":8761,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":8764,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"artifacts","offset":0,"slot":1,"type":"t_array(t_string_storage)dyn_storage"}]},"t_struct(FuzzSelector)8753_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzSelector","numberOfBytes":64,"members":[{"astId":8749,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":8752,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(StdStorage)10176_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":10160,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)10151_storage)))"},{"astId":10163,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":10165,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":10167,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":10169,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":10171,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":10173,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":10175,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_struct(Type)77_storage":{"encoding":"inplace","label":"struct Type","numberOfBytes":32,"members":[{"astId":74,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"kind","offset":0,"slot":0,"type":"t_enum(TypeKind)86"},{"astId":76,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"isArray","offset":1,"slot":0,"type":"t_bool"}]},"t_struct(Variable)71_storage":{"encoding":"inplace","label":"struct Variable","numberOfBytes":64,"members":[{"astId":68,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"ty","offset":0,"slot":0,"type":"t_struct(Type)77_storage"},{"astId":70,"contract":"lib/forge-std/test/LibVariable.t.sol:LibVariableTest","label":"data","offset":0,"slot":1,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60808060405234602f57600160ff19600c541617600c55600160ff19601f541617601f5561881d90816100348239f35b5f80fdfe60806040526004361015610011575f80fd5b5f5f3560e01c806309bd759b1461517e5780630a1c9c7414614fcc5780630a9254e4146135e35780631ed7831c146135655780632ade3880146133a65780633e5e3c23146133285780633f7286f4146132aa57806360e9d8241461233257806366d9a9a01461220957806385226c8114612177578063916a17c6146120cf578063a4b9d9ed146116d7578063adecb4af14610e92578063af584eee14610dd5578063b0464fdc14610d2d578063b5508aa914610c94578063ba414fa614610c6f578063d44436cb146101a9578063e20c9f711461011b5763fa7626d4146100f6575f80fd5b34610118578060031936011261011857602060ff601f54166040519015158152f35b80fd5b503461011857806003193601126101185760405160158054808352908352909160208301917f55f448fdea98c4d29eb340757ef0a66cd03dbb9538908a6a81d96026b71ec475915b81811061018a576101868561017a818703826155bc565b60405191829182615414565b0390f35b82546001600160a01b0316845260209093019260019283019201610163565b5034610118578060031936011261011857604051906101c78261558d565b6004825280602083015260405160646020820152602081526101ea6040826155bc565b604051926101f78461558d565b8352602083015260018060a01b03601f5460081c1660405163713c108f60e01b81526020818061022a8760048301615bd0565b0381855afa9081156107aa5790610251918491610c40575b506001600160801b031661645a565b6040516308edc3c960e31b81526020818061026f8760048301615bd0565b0381855afa9081156107aa578391610bfa575b506001600160401b03610295911661645a565b604051638ec7637b60e01b8152602081806102b38760048301615bd0565b0381855afa9081156107aa578391610bb7575b5063ffffffff6102d6911661645a565b60405163296a2f4160e01b8152602081806102f48760048301615bd0565b0381855afa9081156107aa578391610b78575b506103359361031b61ffff6020931661645a565b60405180958192631e65222160e21b835260048301615bd0565b0381845afa92831561072d578293610b30575b5061035860ff6103f7941661645a565b6040516103666060826155bc565b60028152604090839082366020830137600a61038182615ad1565b52601461038d82615af2565b526103bb6103c9604051926103a18461558d565b600484526001602085015260405192839160208301615b02565b03601f1981018352826155bc565b604051916103d68361558d565b825260208201526040518096819263f3283fb760e01b835260048301615bd0565b0381855afa80156107aa578390610a98575b83945060ff61041782615ad1565b5116600a8103610a2c575b5061042e60ff91615af2565b5116601481036109c0575b50604051906104478261558d565b60058252836020830152604051606460208201526020815261046a6040826155bc565b604051926104778461558d565b8352602083015260405161048a8161558d565b600581528460208201526040516063196020820152602081526104ae6040826155bc565b604051916104bb8361558d565b82526020820152604051633ded041d60e21b8152602081806104e08760048301615bd0565b0381885afa801561094b576104ff918791610991575b50600f0b6164b5565b604051637da8228d60e11b81526020818061051d8560048301615bd0565b0381885afa801561094b578690610956575b61053c915060070b616510565b604051630ad9a76d60e31b81526020818061055a8760048301615bd0565b0381885afa90811561094b57869161090d575b5061059a9161058060209260030b6164b5565b60405180938192632f50931360e01b835260048301615bd0565b0381875afa9081156109025785916108c4575b506105da926105c060209260010b616510565b60405180948192633fb5872b60e01b835260048301615bd0565b0381865afa80156108b95784928391610872575b50926105fe61068c94840b6164b5565b6040519161060d6060846155bc565b6002835236602084013760091961062383615ad1565b52601461062f83615af2565b526103bb61065d604051936106438561558d565b600585526001602086015260405192839160208301615b02565b6040519261066a8461558d565b8352602083015260405180809581946304f33e3760e01b835260048301615bd0565b03915afa90811561072d5782916107b9575b506106a881615ad1565b51820b600a810161073b575b506106be90615af2565b51810b601481036106cc5750f35b5f5160206187c85f395f51905f523b15610738576040519063fe74f05b60e01b825260048201526014602482015281816044815f5160206187c85f395f51905f525afa801561072d5761071c5750f35b81610726916155bc565b6101185780f35b6040513d84823e3d90fd5b50fd5b5f5160206187c85f395f51905f523b156107b55760405163fe74f05b60e01b81526004810191909152600919602482015282816044815f5160206187c85f395f51905f525afa9081156107aa578391610795575b506106b4565b8161079f916155bc565b61073857815f61078f565b6040513d85823e3d90fd5b5050fd5b9150503d8083833e6107cb81836155bc565b81019060208183031261086a578051906001600160401b03821161086e57019080601f8301121561086a5781519061080282615a25565b9261081060405194856155bc565b82845260208085019360051b820101918211610866579060208594939201915b818310610840575050505f61069e565b9091809394505180860b81036108625781528493926020908101929101610830565b8580fd5b8480fd5b8280fd5b8380fd5b919250506020813d6020116108b1575b8161088f602093836155bc565b810103126108ac57519081840b82036108ac5783916105fe6105ee565b505050fd5b3d9150610882565b6040513d86823e3d90fd5b90506020813d6020116108fa575b816108df602093836155bc565b8101031261086657518060010b8103610866576105da6105ad565b3d91506108d2565b6040513d87823e3d90fd5b90506020813d602011610943575b81610928602093836155bc565b8101031261086257518060030b81036108625761059a61056d565b3d915061091b565b6040513d88823e3d90fd5b506020813d602011610989575b81610970602093836155bc565b810103126108625761098461053c91615ca4565b61052f565b3d9150610963565b6109b3915060203d6020116109b9575b6109ab81836155bc565b810190615c30565b5f6104f6565b503d6109a1565b5f5160206187c85f395f51905f523b156108ac576040519063260a5b1560e21b825260048201526014602482015283816044815f5160206187c85f395f51905f525afa9081156108b9578491610a17575b50610439565b81610a21916155bc565b6107b557825f610a11565b5f5160206187c85f395f51905f523b15610866576040519063260a5b1560e21b82526004820152600a602482015284816044815f5160206187c85f395f51905f525afa908115610902578591610a83575b50610422565b81610a8d916155bc565b6108ac57835f610a7d565b503d8084863e610aa881866155bc565b84019360208186031261086e578051906001600160401b038211610866570184601f8201121561086e57805194610ade86615a25565b91610aec60405193846155bc565b86835260208084019760051b82010191821161086257602001955b818710610b18575050839450610409565b60208091610b258961610f565b815201960195610b07565b92506020833d602011610b70575b81610b4b602093836155bc565b81010312610b6c5761035860ff610b646103f79561610f565b945050610348565b5080fd5b3d9150610b3e565b90506020813d602011610baf575b81610b93602093836155bc565b8101031261086a575161ffff8116810361086a57610335610307565b3d9150610b86565b90506020813d602011610bf2575b81610bd2602093836155bc565b8101031261086a575163ffffffff8116810361086a5763ffffffff6102c6565b3d9150610bc5565b90506020813d602011610c38575b81610c15602093836155bc565b8101031261086a576001600160401b03610c3161029592615c49565b9150610282565b3d9150610c08565b610c62915060203d602011610c68575b610c5a81836155bc565b810190615b99565b5f610242565b503d610c50565b50346101185780600319360112610118576020610c8a616074565b6040519015158152f35b5034610118578060031936011261011857601954610cb181615a25565b91610cbf60405193846155bc565b818352601981527f944998273e477b495144fb8794c914197f3ccb46be2900f4698fd0ef743c9695602084015b838310610d01576040518061018687826154b7565b600160208192604051610d1f81610d188189615889565b03826155bc565b815201920192019190610cec565b5034610118578060031936011261011857601c54610d4a81615a25565b91610d5860405193846155bc565b818352601c81527f0e4562a10381dec21b205ed72637e6b1b523bdd0e4d4d50af5cd23dd4500a211602084015b838310610d9a57604051806101868782615516565b60026020600192604051610dad8161558d565b848060a01b038654168152610dc3858701615d33565b83820152815201920192019190610d85565b50346101185780600319360112610118575f5160206187c85f395f51905f523b1561011857604051630618f58760e51b81526321c4e35760e21b600482015281908181602481835f5160206187c85f395f51905f525af1801561072d57610e7d575b50601f5460081c6001600160a01b0316803b1561073857816040518092632b6a7e0960e21b82528180610e6c6004820161590a565b03915afa801561072d5761071c5750f35b81610e87916155bc565b61011857805f610e37565b503461011857806003193601126101185760405163b02cf71d60e01b60208201528190610ec5816103bb6024820161602e565b5f5160206187c85f395f51905f523b156107385781610f00916040518093819263f28dceb360e01b8352602060048401526024830190615456565b0381835f5160206187c85f395f51905f525af1801561072d576116c2575b5050601f54604051630e30ca3760e31b815290602090829060081c6001600160a01b03168180610f5060048201615945565b03915afa801561072d5761168f575b508060405163b02cf71d60e01b60208201526040602482015260076064820152666164647265737360c81b608482015260806044820152600660a482015265737472696e6760d01b60c482015260c48152610fbb60e4826155bc565b5f5160206187c85f395f51905f523b156107385781610ff6916040518093819263f28dceb360e01b8352602060048401526024830190615456565b0381835f5160206187c85f395f51905f525af1801561072d5761167a575b5050601f546040516319ab8c2360e11b815290602090829060081c6001600160a01b031681806110466004820161597d565b03915afa801561072d57611643575b508060405163b02cf71d60e01b602082015260406024820152600960648201526875696e743235365b5d60b81b60848201526080604482015261109e816103bb60a4820161605b565b5f5160206187c85f395f51905f523b1561073857816110d9916040518093819263f28dceb360e01b8352602060048401526024830190615456565b0381835f5160206187c85f395f51905f525af1801561072d5761162e575b5050601f546040516301a9fdf360e01b8152908290829060081c6001600160a01b03168180611128600482016159b5565b03915afa801561072d576115a1575b508060405163b02cf71d60e01b6020820152604060248201526009606482015268616464726573735b5d60b81b608482015260806044820152600860a482015267737472696e675b5d60c01b60c482015260c4815261119760e4826155bc565b5f5160206187c85f395f51905f523b1561073857816111d2916040518093819263f28dceb360e01b8352602060048401526024830190615456565b0381835f5160206187c85f395f51905f525af1801561072d5761158c575b5050601f54604051633a03e44560e21b8152908290829060081c6001600160a01b03168180611221600482016159ed565b03915afa801561072d5761156c575b508060405163b02cf71d60e01b60208201526040602482015261126d816103bb61125c6064830161605b565b828103602319016044840152616017565b5f5160206187c85f395f51905f523b1561073857816112a8916040518093819263f28dceb360e01b8352602060048401526024830190615456565b0381835f5160206187c85f395f51905f525af1801561072d57611557575b5050601f5460405163144925ab60e11b8152908290829060081c6001600160a01b031681806112f760048201615945565b03915afa801561072d57611537575b508060405163b02cf71d60e01b602082015260406024820152611343816103bb61133260648301616017565b82810360231901604484015261605b565b5f5160206187c85f395f51905f523b15610738578161137e916040518093819263f28dceb360e01b8352602060048401526024830190615456565b0381835f5160206187c85f395f51905f525af1801561072d57611522575b5050601f54604051631b8c25c760e01b815290602090829060081c6001600160a01b031681806113ce600482016159b5565b03915afa801561072d576114eb575b5060405163b02cf71d60e01b60208201528190611400816103bb6024820161602e565b5f5160206187c85f395f51905f523b15610738578161143b916040518093819263f28dceb360e01b8352602060048401526024830190615456565b0381835f5160206187c85f395f51905f525af1801561072d576114d6575b5060018060a01b03601f5460081c166040516114748161558d565b60048152826020820152813b156107b5576114c76084849260405194859384926307498c5b60e11b845260ff6023546114b2600487018383166157b8565b60081c16151560248501526044840190615bb8565b5afa801561072d5761071c5750f35b816114e0916155bc565b61011857805f611459565b6020813d60201161151a575b81611504602093836155bc565b81010312610b6c57611515906157ab565b6113dd565b3d91506114f7565b8161152c916155bc565b61011857805f61139c565b611552903d8084833e61154a81836155bc565b810190615f96565b611306565b81611561916155bc565b61011857805f6112c6565b611587903d8084833e61157f81836155bc565b810190615a50565b611230565b81611596916155bc565b61011857805f6111f0565b3d8083833e6115b081836155bc565b81019060208183031261086a578051906001600160401b03821161086e57019080601f8301121561086a5781516115e681615a25565b926115f460405194856155bc565b81845260208085019260051b82010192831161086657602001905b82821061161e57505050611137565b815181526020918201910161160f565b81611638916155bc565b61011857805f6110f7565b6020813d602011611672575b8161165c602093836155bc565b81010312610b6c5761166d90615a3c565b611055565b3d915061164f565b81611684916155bc565b61011857805f611014565b6020813d6020116116ba575b816116a8602093836155bc565b810103126116b65751610f5f565b5f80fd5b3d915061169b565b816116cc916155bc565b61011857805f610f1e565b5034610118578060031936011261011857601f54604051631b8c25c760e01b815260089190911c6001600160a01b0316906020818061171860048201615945565b0381855afa80156107aa578390612094575b6117349150616312565b816040516319ab8c2360e11b81526020600482015260248101602060ff602554611760848383166157b8565b60081c1615159101526060606482015260208180611782608482016026615889565b0381865afa90811561072d57829161205a575b506001600160a01b031663deadbeee198101611ff4575b5060405163a29eeb7960e01b81526020600482015260248101602060ff6027546117d8848383166157b8565b60081c16151591015260606064820152602081806117fa608482016028615889565b0381865afa90811561072d578291611fbf575b50602a8103611f5c575b50604051630e30ca3760e31b81526020600482015260248101602060ff602954611843848383166157b8565b60081c161515910152606060648201526020818061186560848201602a615889565b0381865afa90811561072d578291611f27575b50607b8103611ec4575b506040516317436ff560e21b81526020600482015260248101602060ff602b546118ae848383166157b8565b60081c16151591015260606064820152602081806118d060848201602c615889565b0381865afa90811561072d578291611e92575b50607b8101611e2c575b5050604051631b0dbf5b60e11b815282818061190b6004820161597d565b0381855afa9081156107aa578391611def575b5061194f60409182519061193284836155bc565b600b82526a1a195b1b1bc81ddbdc9b1960aa1b60208301526161f8565b82815163e31d23e560e01b81526020600482015260248101602060ff602f5461197a848383166157b8565b60081c1615159101526060606482015281818061199b608482016030615889565b0381875afa908115611ccd578291611d9f575b508251906119bc84836155bc565b6003825262607ff760e91b60208301525f5160206187c85f395f51905f523b1561086a57611a098391611a1b86519485938493639762463160e01b85528960048601526044850190615456565b83810360031901602485015290615456565b03815f5160206187c85f395f51905f525afa8015611ccd57611d8a575b5050805163144925ab60e11b8152838180611a55600482016159b5565b0381865afa908115611d8057611a9c91611a94918691611d66575b50611a7b81516163ff565b611a8f611a8782615ad1565b511515616312565b615af2565b511515616365565b828151633a03e44560e21b81526020600482015260248101602060ff603354611ac7848383166157b8565b60081c16151591015260606064820152818180611ae8608482016034615889565b0381875afa908115611ccd578291611d4c575b50611b0681516163ff565b6001600160a01b03611b1782615ad1565b511660018103611cd7575b506001600160a01b0390611b3590615af2565b511660028103611c6b575b508151630663113f60e21b81529283908180611b5e600482016159ed565b03915afa918215611c61578392611ba9575b83611ba6611b9d85611b8281516163ff565b611a8f611b8e82615ad1565b51611b97615b57565b906161f8565b51611b97615b78565b80f35b9091503d8084833e611bbb81836155bc565b81019060208183031261086e578051906001600160401b038211610866570181601f8201121561086e578051611bfc611bf382615a25565b945194856155bc565b80845260208085019160051b830101918383116108625760208101915b838310611c30575050505050611b9d611ba6611b70565b82516001600160401b038111611c5d57602091611c5287848094870101615f7c565b815201920191611c19565b8780fd5b81513d85823e3d90fd5b5f5160206187c85f395f51905f523b15610b6c578251906328a9b0fb60e11b825260048201526002602482015281816044815f5160206187c85f395f51905f525afa8015611ccd5715611b405781611cc2916155bc565b61086a57825f611b40565b83513d84823e3d90fd5b5f5160206187c85f395f51905f523b1561086a578351906328a9b0fb60e11b825260048201526001602482015282816044815f5160206187c85f395f51905f525afa8015611d4257908391611d2d575b50611b22565b81611d37916155bc565b610b6c57815f611d27565b84513d85823e3d90fd5b611d6091503d8084833e61157f81836155bc565b5f611afb565b611d7a91503d8088833e61154a81836155bc565b5f611a70565b82513d86823e3d90fd5b81611d94916155bc565b61086a57825f611a38565b90503d8083833e611db081836155bc565b81019060208183031261086a578051906001600160401b03821161086e57019080601f8301121561086a578151611de992602001615f37565b5f6119ae565b90503d8084833e611e0081836155bc565b810160208282031261086e5781516001600160401b03811161086657611e269201615f7c565b5f61191e565b5f5160206187c85f395f51905f523b15610b6c5760405163fe74f05b60e01b81526004810191909152607a19602482015281816044815f5160206187c85f395f51905f525afa801561072d57156118ed5781611e87916155bc565b610b6c57815f6118ed565b90506020813d602011611ebc575b81611ead602093836155bc565b81010312610b6c57515f6118e3565b3d9150611ea0565b5f5160206187c85f395f51905f523b15610b6c576040519063260a5b1560e21b82526004820152607b602482015281816044815f5160206187c85f395f51905f525afa801561072d57156118825781611f1c916155bc565b610b6c57815f611882565b9150506020813d602011611f54575b81611f43602093836155bc565b810103126116b6578290515f611878565b3d9150611f36565b5f5160206187c85f395f51905f523b15610b6c5760405190637c84c69b60e01b82526004820152602a602482015281816044815f5160206187c85f395f51905f525afa801561072d57156118175781611fb4916155bc565b610b6c57815f611817565b9150506020813d602011611fec575b81611fdb602093836155bc565b810103126116b6578290515f61180d565b3d9150611fce565b5f5160206187c85f395f51905f523b15610b6c57604051906328a9b0fb60e11b8252600482015263deadbeef602482015281816044815f5160206187c85f395f51905f525afa801561072d57156117ac578161204f916155bc565b610b6c57815f6117ac565b90506020813d60201161208c575b81612075602093836155bc565b81010312610b6c5761208690615a3c565b5f611795565b3d9150612068565b506020813d6020116120c7575b816120ae602093836155bc565b8101031261086a576120c2611734916157ab565b61172a565b3d91506120a1565b5034610118578060031936011261011857601d546120ec81615a25565b916120fa60405193846155bc565b818352601d81527f6d4407e7be21f808e6509aa9fa9143369579dd7d760fe20a2c09680fc146134f602084015b83831061213c57604051806101868782615516565b6002602060019260405161214f8161558d565b848060a01b038654168152612165858701615d33565b83820152815201920192019190612127565b5034610118578060031936011261011857601a5461219481615a25565b916121a260405193846155bc565b818352601a81527f057c384a7d1c54f3a1b2e5e67b2617b8224fdfd1ea7234eea573a6ff665ff63e602084015b8383106121e4576040518061018687826154b7565b6001602081926040516121fb81610d188189615889565b8152019201920191906121cf565b5034610118578060031936011261011857601b5461222681615a25565b61223360405191826155bc565b818152601b83526020810191837f3ad8aa4f87544323a9d1e5dd902f40c356527a7955687113db5f9a85ad579dc1845b8383106122ef57868587604051928392602084019060208552518091526040840160408260051b8601019392905b8282106122a057505050500390f35b919360019193955060206122df8192603f198a8203018652885190836122cf8351604084526040840190615456565b920151908481840391015261547a565b9601920192018594939192612291565b600260206001926040516123028161558d565b60405161231381610d18818a615889565b8152612320858701615d33565b83820152815201920192019190612263565b5034610118578060031936011261011857604051906123508261558d565b60048252806020830152604051600160801b6020820152602081526123766040826155bc565b604051926123838461558d565b8352602083015260405191639f9ddabb60e01b602084015260206024840152601f60448401527f76616c756520646f6573206e6f742066697420696e202775696e7431323827006064840152606483526123de6084846155bc565b82516001600160401b038111612d26576123f96020546157c5565b601f811161324d575b506020601f82116001146131ec578394829394926131e1575b50508160011b915f199060031b1c1916176020555b5f5160206187c85f395f51905f523b15610b6c5760405163f28dceb360e01b8152602060048201528290818180612469602482016157fd565b0381835f5160206187c85f395f51905f525af1801561072d576131cc575b505060206124b89160018060a01b03601f5460081c16604051808095819463713c108f60e01b835260048301615bd0565b03915afa801561072d576131af575b50604051906124d58261558d565b600582528060208301526001607f1b604051906020820152602081526124fc6040826155bc565b604051926125098461558d565b8352602083015260405191639f9ddabb60e01b602084015261253f8361253160248201615bf8565b03601f1981018552846155bc565b82516001600160401b038111612d265761255a6020546157c5565b601f8111613152575b506020601f82116001146130f1578394829394926130e6575b50508160011b915f199060031b1c1916176020555b5f5160206187c85f395f51905f523b15610b6c5760405163f28dceb360e01b81526020600482015282908181806125ca602482016157fd565b0381835f5160206187c85f395f51905f525af1801561072d576130d1575b505060206126199160018060a01b03601f5460081c166040518080958194633ded041d60e21b835260048301615bd0565b03915afa801561072d576130b4575b50604051906126368261558d565b600582526020808301829052604080516001607f1b198184015291825261265d90826155bc565b6040519261266a8461558d565b8352602083015260405191639f9ddabb60e01b60208401526126928361253160248201615bf8565b82516001600160401b038111612d26576126ad6020546157c5565b601f8111613057575b506020601f8211600114612ff657839482939492612feb575b50508160011b915f199060031b1c1916176020555b5f5160206187c85f395f51905f523b15610b6c5760405163f28dceb360e01b815260206004820152829081818061271d602482016157fd565b0381835f5160206187c85f395f51905f525af1801561072d57612fd6575b5050602061276c9160018060a01b03601f5460081c166040518080958194633ded041d60e21b835260048301615bd0565b03915afa801561072d57612fb9575b506040519061278b6060836155bc565b60028252604080366020850137600a6127a384615ad1565b52600160401b6127b284615af2565b526103bb6127e0604051946127c68661558d565b600486526001602087015260405192839160208301615b02565b604051936127ed8561558d565b8452602084015260405192639f9ddabb60e01b602085015260206024850152602760448501527f76616c756520696e20617272617920646f6573206e6f742066697420696e202760648501526675696e7436342760c81b60848501526084845261285860a4856155bc565b83516001600160401b038111612fa5576128736020546157c5565b601f8111612f48575b50602094601f8211600114612ee6579484958293949592612edb575b50508160011b915f199060031b1c1916176020555b5f5160206187c85f395f51905f523b1561086a5760405163f28dceb360e01b81526020600482015283908181806128e6602482016157fd565b0381835f5160206187c85f395f51905f525af1801561072d57612ec6575b50601f546040516318b6d84960e01b815292839160081c6001600160a01b031690829081906129369060048301615bd0565b03915afa80156107aa57612e31575b50604051906129556060836155bc565b60028252366020830137600a61296a82615ad1565b526001603f1b61297982615af2565b52604051916129878361558d565b60058352600160208401526040516129a6816103bb8560208301615b02565b604051936129b38561558d565b8452602084015260405192639f9ddabb60e01b60208501526129e9846129db60248201615c5d565b03601f1981018652856155bc565b83516001600160401b038111612d2657612a046020546157c5565b601f8111612dd4575b50602094601f8211600114612d72579483949582939492612d67575b50508160011b915f199060031b1c1916176020555b5f5160206187c85f395f51905f523b15610b6c5760405163f28dceb360e01b815260206004820152828180612a75602482016157fd565b0381835f5160206187c85f395f51905f525af180156107aa57908391612d52575b50601f5460405163cd8ceaad60e01b815292839160081c6001600160a01b03169082908190612ac89060048301615bd0565b03915afa801561072d57612d3a575b50600a612ae383615ad1565b526001603f1b19612af383615af2565b526103bb612b07604051936106438561558d565b60405192612b148461558d565b8352602083015260405191639f9ddabb60e01b6020840152612b3c8361253160248201615c5d565b82516001600160401b038111612d2657612b576020546157c5565b601f8111612cc9575b506020601f8211600114612c6857839482939492612c5d575b50508160011b915f199060031b1c1916176020555b5f5160206187c85f395f51905f523b15610b6c5760405163f28dceb360e01b8152602060048201528290818180612bc7602482016157fd565b0381835f5160206187c85f395f51905f525af1801561072d57612c48575b50601f5460405163cd8ceaad60e01b815292839160081c6001600160a01b03169082908190612c179060048301615bd0565b03915afa801561072d57612c29575080f35b612c44903d8084833e612c3c81836155bc565b810190615cb2565b5080f35b612c538280926155bc565b610118575f612be5565b015190505f80612b79565b80845280842090601f198316855b818110612cb157509583600195969710612c99575b505050811b01602055612b8e565b01515f1960f88460031b161c191690555f8080612c8b565b9192602060018192868b015181550194019201612c76565b81811115612b60576020808552601f830160051c905f5160206187a85f395f51905f52908410612d1e575b81601f9101920160051c0390845b828110612d10575050612b60565b808660019284015501612d02565b859150612cf4565b634e487b7160e01b83526041600452602483fd5b612d4d903d8084833e612c3c81836155bc565b612ad7565b81612d5c916155bc565b610b6c57815f612a96565b015190505f80612a29565b601f1982169580855280852091855b888110612dbc57508360019596979810612da4575b505050811b01602055612a3e565b01515f1960f88460031b161c191690555f8080612d96565b91926020600181928685015181550194019201612d81565b81811115612a0d576020808552601f830160051c905f5160206187a85f395f51905f52908410612e29575b81601f9101920160051c0390845b828110612e1b575050612a0d565b808660019284015501612e0d565b859150612dff565b3d8084833e612e4081836155bc565b81019060208183031261086e578051906001600160401b03821161086657019080601f8301121561086e578151612e7681615a25565b92612e8460405194856155bc565b81845260208085019260051b82010192831161086257602001905b828210612eae57505050612945565b60208091612ebb84615c49565b815201910190612e9f565b612ed18280926155bc565b610118575f612904565b015190505f80612898565b601f1982169580865280862091865b888110612f3057508360019596979810612f18575b505050811b016020556128ad565b01515f1960f88460031b161c191690555f8080612f0a565b91926020600181928685015181550194019201612ef5565b8181111561287c576020808652601f830160051c905f5160206187a85f395f51905f52908410612f9d575b81601f9101920160051c0390855b828110612f8f57505061287c565b808760019284015501612f81565b869150612f73565b634e487b7160e01b84526041600452602484fd5b612fd19060203d6020116109b9576109ab81836155bc565b61277b565b81612fe0916155bc565b610b6c57815f61273b565b015190505f806126cf565b80845280842090601f198316855b81811061303f57509583600195969710613027575b505050811b016020556126e4565b01515f1960f88460031b161c191690555f8080613019565b9192602060018192868b015181550194019201613004565b818111156126b6576020808552601f830160051c905f5160206187a85f395f51905f529084106130ac575b81601f9101920160051c0390845b82811061309e5750506126b6565b808660019284015501613090565b859150613082565b6130cc9060203d6020116109b9576109ab81836155bc565b612628565b816130db916155bc565b610b6c57815f6125e8565b015190505f8061257c565b80845280842090601f198316855b81811061313a57509583600195969710613122575b505050811b01602055612591565b01515f1960f88460031b161c191690555f8080613114565b9192602060018192868b0151815501940192016130ff565b81811115612563576020808552601f830160051c905f5160206187a85f395f51905f529084106131a7575b81601f9101920160051c0390845b828110613199575050612563565b80866001928401550161318b565b85915061317d565b6131c79060203d602011610c6857610c5a81836155bc565b6124c7565b816131d6916155bc565b610b6c57815f612487565b015190505f8061241b565b80845280842090601f198316855b8181106132355750958360019596971061321d575b505050811b01602055612430565b01515f1960f88460031b161c191690555f808061320f565b9192602060018192868b0151815501940192016131fa565b81811115612402576020808552601f830160051c905f5160206187a85f395f51905f529084106132a2575b81601f9101920160051c0390845b828110613294575050612402565b808660019284015501613286565b859150613278565b503461011857806003193601126101185760405160178054808352908352909160208301917fc624b66cc0138b8fabc209247f72d758e1cf3343756d543badbf24212bed8c15915b818110613309576101868561017a818703826155bc565b82546001600160a01b03168452602090930192600192830192016132f2565b503461011857806003193601126101185760405160188054808352908352909160208301917fb13d2d76d1f4b7be834882e410b3e3a8afaf69f83600ae24db354391d2378d2e915b818110613387576101868561017a818703826155bc565b82546001600160a01b0316845260209093019260019283019201613370565b5034610118578060031936011261011857601e546133c381615a25565b6133d060405191826155bc565b818152601e83526020810191837f50bb669a95c7b50b7e8a6f09454034b2b14cf2b85c730dca9a539ca82cb6e350845b8383106134d45786858760405192839260208401906020855251809152604084019160408260051b8601019392815b83831061343c5786860387f35b919395509193603f198782030183528551906020604082019260018060a01b0381511683520151916040602083015282518091526060820190602060608260051b850101940192855b8281106134a95750505050506020806001929701930193019092869594929361342f565b90919293946020806134c7600193605f198782030189528951615456565b9701950193929101613485565b6040516134e08161558d565b82546001600160a01b031681526001830180546134fc81615a25565b9161350a60405193846155bc565b8183528a526020808b20908b9084015b838210613540575050505060019282602092836002950152815201920192019190613400565b60016020819260405161355781610d18818a615889565b81520193019101909161351a565b503461011857806003193601126101185760405160168054808352908352909160208301917fd833147d7dc355ba459fc788f669e58cfaf9dc25ddcd0702e87d69c7b5124289915b8181106135c4576101868561017a818703826155bc565b82546001600160a01b03168452602090930192600192830192016135ad565b5034610118578060031936011261011857604051612239808201908282106001600160401b03831117612fa55790829161656f8339039082f08015614fbf57601f8054610100600160a81b03191660089290921b610100600160a81b0316919091179055604051906136548261558d565b8082528060208301526040519161366a8361558d565b825260405160209261367c84836155bc565b8282528381019182525180519060088210156144775760ff61ff0086602154930151151560081b1692169061ffff19161717602155519081516001600160401b038111614a80576136ce6022546157c5565b601f8111614f6e575b508392601f8211600114614f0d57928293829392614f02575b50508160011b915f199060031b1c1916176022555b6040516137118161558d565b60018152828101828152604051916001858401528483526137336040846155bc565b846040516137408161558d565b82815201928352519060088210156144775760ff61ff006023549251151560081b1692169061ffff19161717602355519081516001600160401b038111614a805761378c6024546157c5565b601f8111614eb1575b508392601f8211600114614e5057928293829392614e45575b50508160011b915f199060031b1c1916176024555b6040516137cf8161558d565b600281528281018281526040519163deadbeef858401528483526137f46040846155bc565b846040516138018161558d565b82815201928352519060088210156144775760ff61ff006025549251151560081b1692169061ffff19161717602555519081516001600160401b038111614a805761384d6026546157c5565b601f8111614df4575b508392601f8211600114614d9357928293829392614d88575b50508160011b915f199060031b1c1916176026555b6040516138908161558d565b6003815282810182815260405191602a858401528483526138b26040846155bc565b846040516138bf8161558d565b82815201928352519060088210156144775760ff61ff006027549251151560081b1692169061ffff19161717602755519081516001600160401b038111614a805761390b6028546157c5565b601f8111614d37575b508392601f8211600114614cd657928293829392614ccb575b50508160011b915f199060031b1c1916176028555b60405161394e8161558d565b6004815282810182815260405191607b858401528483526139706040846155bc565b8460405161397d8161558d565b82815201928352519060088210156144775760ff61ff006029549251151560081b1692169061ffff19161717602955519081516001600160401b038111614a80576139c9602a546157c5565b601f8111614c7a575b508392601f8211600114614c1957928293829392614c0e575b50508160011b915f199060031b1c191617602a555b604051613a0c8161558d565b6005815282810182815260405191607a1985840152848352613a2f6040846155bc565b84604051613a3c8161558d565b82815201928352519060088210156144775760ff61ff00602b549251151560081b1692169061ffff19161717602b55519081516001600160401b038111614a8057613a88602c546157c5565b601f8111614bbd575b508392601f8211600114614b5c57928293829392614b51575b50508160011b915f199060031b1c191617602c555b604051613acb8161558d565b60068152828101828152604051918480840152600b60408401526a1a195b1b1bc81ddbdc9b1960aa1b606084015260608352613b086080846155bc565b84604051613b158161558d565b82815201928352519060088210156144775760ff61ff00602d549251151560081b1692169061ffff19161717602d55519081516001600160401b038111614a8057613b61602e546157c5565b601f8111614b00575b508392601f8211600114614a9f57928293829392614a94575b50508160011b915f199060031b1c191617602e555b604051613ba48161558d565b600781528281018281526040519184808401526003604084015262607ff760e91b606084015260608352613bd96080846155bc565b84604051613be68161558d565b82815201928352519060088210156144775760ff61ff00602f549251151560081b1692169061ffff19161717602f55519081516001600160401b038111614a8057613c326030546157c5565b601f8111614a2f575b508392601f82116001146149ce579282938293926149c3575b50508160011b915f199060031b1c1916176030555b6060604051613c7882826155bc565b60028152838101601f19830191823683376001613c9482615ad1565b5284613c9f82615af2565b52604051613cac8161558d565b600181528681019160018352604051809460408201928a80840152518093528782019092895b8b8282106149aa57505050613cf0925003601f1981018552846155bc565b86604051613cfd8161558d565b82815201928352519060088210156145975760ff61ff006031549251151560081b1692169061ffff19161717603155518051906001600160401b038211614583578190613d4b6032546157c5565b601f8111614951575b508690601f83116001146148ed5786926148e2575b50508160011b915f199060031b1c1916176032555b612531604051613d8e84826155bc565b600281528236878301376001613da382615ad1565b526002613daf82615af2565b52604051613dbc8161558d565b60028152613dd987820192600184526040519485918a8301615414565b86604051613de68161558d565b82815201928352519060088210156145975760ff61ff006033549251151560081b1692169061ffff19161717603355518051906001600160401b038211614583578190613e346034546157c5565b601f8111614889575b508690601f831160011461482557869261481a575b50508160011b915f199060031b1c1916176034555b604051613e7483826155bc565b6002815284810190823683376001613e8b82615ad1565b526002613e9782615af2565b52604051613ea48161558d565b600381528681019160018352604051809460408201928a80840152518093528782019092895b8b82821061480357505050613ee8925003601f1981018552846155bc565b86604051613ef58161558d565b82815201928352519060088210156145975760ff61ff006035549251151560081b1692169061ffff19161717603555518051906001600160401b038211614583578190613f436036546157c5565b601f81116147aa575b508690601f831160011461474657869261473b575b50508160011b915f199060031b1c1916176036555b612531604051613f8684826155bc565b600281528236878301376001613f9b82615ad1565b526002613fa782615af2565b52604051613fb48161558d565b60048152613fd187820192600184526040519485918a8301615b02565b86604051613fde8161558d565b82815201928352519060088210156145975760ff61ff006037549251151560081b1692169061ffff19161717603755518051906001600160401b03821161458357819061402c6038546157c5565b601f81116146e2575b508690601f831160011461467e578692614673575b50508160011b915f199060031b1c1916176038555b61253160405161406f84826155bc565b600281528236878301375f1961408482615ad1565b52600261409082615af2565b5260405161409d8161558d565b600581526140ba87820192600184526040519485918a8301615b02565b866040516140c78161558d565b82815201928352519060088210156145975760ff61ff006039549251151560081b1692169061ffff19161717603955518051906001600160401b038211614583578190614115603a546157c5565b601f811161461a575b508690601f83116001146145b65786926145ab575b50508160011b915f199060031b1c191617603a555b61253160405161415884826155bc565b6002815261416883878301615b3b565b614170615b57565b61417982615ad1565b5261418381615ad1565b5061418c615b78565b61419582615af2565b5261419f81615af2565b506040516141ac8161558d565b600681526141c987820192600184526040519485918a83016154b7565b866040516141d68161558d565b82815201928352519060088210156145975760ff61ff00603b549251151560081b1692169061ffff19161717603b55518051906001600160401b038211614583578190614224603c546157c5565b601f811161452a575b508690601f83116001146144c65786926144bb575b50508160011b915f199060031b1c191617603c555b60405161426483826155bc565b600281526142758582019283615b3b565b846040805161428482826155bc565b60018152600160f81b8382015261429a84615ad1565b526142a483615ad1565b5080516142b182826155bc565b60018152600160f91b838201526142c784615af2565b526142d183615af2565b508051926142de8461558d565b600784528284019460018652825196879284840190868086015251809152818401918160051b85010192918a905b82821061448b57505050509061432a9103601f1981018752866155bc565b516143348161558d565b82815201928352519060088210156144775760ff61ff00603d549251151560081b1692169061ffff19161717603d5551918251906001600160401b038211612d2657614381603e546157c5565b601f8111614426575b5080601f83116001146143c4575082938293926143b9575b50508160011b915f199060031b1c191617603e5580f35b015190505f806143a2565b90601f19831694603e85528285209285905b87821061440e5750508360019596106143f6575b505050811b01603e5580f35b01515f1960f88460031b161c191690555f80806143ea565b806001859682949686015181550195019301906143d6565b8281111561438a57603e8452818420601f840160051c9083851061446f575b81601f9101920160051c0390845b82811061446157505061438a565b808660019284015501614453565b859150614445565b634e487b7160e01b84526021600452602484fd5b92959660019295506144a9819295605f198d82030186528851615456565b9601920192019288938b96959361430c565b015190505f80614242565b603c87528787209250601f198416875b898282106145145750509084600195949392106144fc575b505050811b01603c55614257565b01515f1960f88460031b161c191690555f80806144ee565b60018596829396860151815501950193016144d6565b8281111561422d57909150603c8652868620601f840160051c9088851061457b575b849392601f0160051c8290039101875b82811061456a57505061422d565b80820189905585945060010161455c565b87915061454c565b634e487b7160e01b85526041600452602485fd5b634e487b7160e01b86526021600452602486fd5b015190505f80614133565b603a87528787209250601f198416875b898282106146045750509084600195949392106145ec575b505050811b01603a55614148565b01515f1960f88460031b161c191690555f80806145de565b60018596829396860151815501950193016145c6565b8281111561411e57909150603a8652868620601f840160051c9088851061466b575b849392601f0160051c8290039101875b82811061465a57505061411e565b80820189905585945060010161464c565b87915061463c565b015190505f8061404a565b603887528787209250601f198416875b898282106146cc5750509084600195949392106146b4575b505050811b0160385561405f565b01515f1960f88460031b161c191690555f80806146a6565b600185968293968601518155019501930161468e565b828111156140355790915060388652868620601f840160051c90888510614733575b849392601f0160051c8290039101875b828110614722575050614035565b808201899055859450600101614714565b879150614704565b015190505f80613f61565b603687528787209250601f198416875b8982821061479457505090846001959493921061477c575b505050811b01603655613f76565b01515f1960f88460031b161c191690555f808061476e565b6001859682939686015181550195019301614756565b82811115613f4c5790915060368652868620601f840160051c908885106147fb575b849392601f0160051c8290039101875b8281106147ea575050613f4c565b8082018990558594506001016147dc565b8791506147cc565b855184529485019488945090920191600101613eca565b015190505f80613e52565b603487528787209250601f198416875b8982821061487357505090846001959493921061485b575b505050811b01603455613e67565b01515f1960f88460031b161c191690555f808061484d565b6001859682939686015181550195019301614835565b82811115613e3d5790915060348652868620601f840160051c908885106148da575b849392601f0160051c8290039101875b8281106148c9575050613e3d565b8082018990558594506001016148bb565b8791506148ab565b015190505f80613d69565b603287528787209250601f198416875b8982821061493b575050908460019594939210614923575b505050811b01603255613d7e565b01515f1960f88460031b161c191690555f8080614915565b60018596829396860151815501950193016148fd565b82811115613d545790915060328652868620601f840160051c908885106149a2575b849392601f0160051c8290039101875b828110614991575050613d54565b808201899055859450600101614983565b879150614973565b8551151584529485019488945090920191600101613cd2565b015190505f80613c54565b601f198216936030845285842091845b87878210614a19575050836001959610614a01575b505050811b01603055613c69565b01515f1960f88460031b161c191690555f80806149f3565b60018495829395850151815501940192016149de565b81811115613c3b5760308352848320601f830160051c90868410614a78575b81601f9101920160051c0390835b828110614a6a575050613c3b565b808560019284015501614a5c565b849150614a4e565b634e487b7160e01b82526041600452602482fd5b015190505f80613b83565b601f19821693602e845285842091845b87878210614aea575050836001959610614ad2575b505050811b01602e55613b98565b01515f1960f88460031b161c191690555f8080614ac4565b6001849582939585015181550194019201614aaf565b81811115613b6a57602e8352848320601f830160051c90868410614b49575b81601f9101920160051c0390835b828110614b3b575050613b6a565b808560019284015501614b2d565b849150614b1f565b015190505f80613aaa565b601f19821693602c845285842091845b87878210614ba7575050836001959610614b8f575b505050811b01602c55613abf565b01515f1960f88460031b161c191690555f8080614b81565b6001849582939585015181550194019201614b6c565b81811115613a9157602c8352848320601f830160051c90868410614c06575b81601f9101920160051c0390835b828110614bf8575050613a91565b808560019284015501614bea565b849150614bdc565b015190505f806139eb565b601f19821693602a845285842091845b87878210614c64575050836001959610614c4c575b505050811b01602a55613a00565b01515f1960f88460031b161c191690555f8080614c3e565b6001849582939585015181550194019201614c29565b818111156139d257602a8352848320601f830160051c90868410614cc3575b81601f9101920160051c0390835b828110614cb55750506139d2565b808560019284015501614ca7565b849150614c99565b015190505f8061392d565b601f198216936028845285842091845b87878210614d21575050836001959610614d09575b505050811b01602855613942565b01515f1960f88460031b161c191690555f8080614cfb565b6001849582939585015181550194019201614ce6565b818111156139145760288352848320601f830160051c90868410614d80575b81601f9101920160051c0390835b828110614d72575050613914565b808560019284015501614d64565b849150614d56565b015190505f8061386f565b601f198216936026845285842091845b87878210614dde575050836001959610614dc6575b505050811b01602655613884565b01515f1960f88460031b161c191690555f8080614db8565b6001849582939585015181550194019201614da3565b818111156138565760268352848320601f830160051c90868410614e3d575b81601f9101920160051c0390835b828110614e2f575050613856565b808560019284015501614e21565b849150614e13565b015190505f806137ae565b601f198216936024845285842091845b87878210614e9b575050836001959610614e83575b505050811b016024556137c3565b01515f1960f88460031b161c191690555f8080614e75565b6001849582939585015181550194019201614e60565b818111156137955760248352848320601f830160051c90868410614efa575b81601f9101920160051c0390835b828110614eec575050613795565b808560019284015501614ede565b849150614ed0565b015190505f806136f0565b601f198216936022845285842091845b87878210614f58575050836001959610614f40575b505050811b01602255613705565b01515f1960f88460031b161c191690555f8080614f32565b6001849582939585015181550194019201614f1d565b818111156136d75760228352848320601f830160051c90868410614fb7575b81601f9101920160051c0390835b828110614fa95750506136d7565b808560019284015501614f9b565b849150614f8d565b50604051903d90823e3d90fd5b50346116b6575f3660031901126116b6575f5160206187c85f395f51905f523b156116b657604051630618f58760e51b81526321c4e35760e21b60048201525f81602481835f5160206187c85f395f51905f525af1801561517357615160575b50601f54604051631b8c25c760e01b815290602090829060081c6001600160a01b0316818061505d6004820161590a565b03915afa801561072d57615129575b505f5160206187c85f395f51905f523b1561011857604051630618f58760e51b81526321c4e35760e21b600482015281908181602481835f5160206187c85f395f51905f525af1801561072d57615114575b5050601f54604051633a03e44560e21b8152908290829060081c6001600160a01b031681806150ef6004820161590a565b03915afa801561072d57615101575080f35b612c44903d8084833e61157f81836155bc565b8161511e916155bc565b61011857805f6150be565b6020813d602011615158575b81615142602093836155bc565b81010312610b6c57615153906157ab565b61506c565b3d9150615135565b61516c91505f906155bc565b5f5f61502c565b6040513d5f823e3d90fd5b346116b6575f3660031901126116b6576151a16151996155dd565b611b976155dd565b6151b46151ac61611d565b611b976155ff565b6151c76151bf616125565b611b97615621565b6151da6151d261612d565b611b97615646565b6151ed6151e5616135565b611b9761566b565b6152006151f861613d565b611b97615690565b61521361520b616145565b611b976156b4565b61522661521e61614d565b611b976156d8565b615239615231616257565b611b976156fb565b61524c61524461625f565b611b9761571d565b6152576151d261612d565b61526a6151ac61526561575e565b616267565b61541261529d60405161527c8161558d565b60ff60315461528d8282168461573e565b60081c1615156020820152616267565b6152c86040918251906152b084836155bc565b6006825265626f6f6c5b5d60d01b60208301526161f8565b6152ea6151e582516152d98161558d565b60ff60295461528d8282168461573e565b6153206152f861526561578a565b82519061530584836155bc565b600982526875696e743235365b5d60b81b60208301526161f8565b61534261519982516153318161558d565b60ff60215461528d8282168461573e565b61537061536b61535061575e565b83519061535c8261558d565b600182525f60208301526162db565b616312565b61539f61539a61537e61575e565b83519061538a8261558d565b60018252600160208301526162db565b616365565b6153c861539a6153ad61575e565b8351906153b98261558d565b600282525f60208301526162db565b6153ee6153d361575e565b8251906153df8261558d565b600182525f60208301526163b8565b6153f661578a565b9051906154028261558d565b60048252600160208301526163b8565b005b60206040818301928281528451809452019201905f5b8181106154375750505090565b82516001600160a01b031684526020938401939092019160010161542a565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b90602080835192838152019201905f5b8181106154975750505090565b82516001600160e01b03191684526020938401939092019160010161548a565b602081016020825282518091526040820191602060408360051b8301019401925f915b8383106154e957505050505090565b9091929394602080615507600193603f198682030187528951615456565b970193019301919392906154da565b602081016020825282518091526040820191602060408360051b8301019401925f915b83831061554857505050505090565b909192939460208061557e600193603f198682030187526040838b51878060a01b0381511684520151918185820152019061547a565b97019301930191939290615539565b604081019081106001600160401b038211176155a857604052565b634e487b7160e01b5f52604160045260245ffd5b90601f801991011681019081106001600160401b038211176155a857604052565b604051906155ec6040836155bc565b60048252636e6f6e6560e01b6020830152565b6040519061560e6040836155bc565b6004825263189bdbdb60e21b6020830152565b604051906156306040836155bc565b60078252666164647265737360c81b6020830152565b604051906156556040836155bc565b6007825266313cba32b9999960c91b6020830152565b6040519061567a6040836155bc565b60078252663ab4b73a191a9b60c91b6020830152565b6040519061569f6040836155bc565b600682526534b73a191a9b60d11b6020830152565b604051906156c36040836155bc565b6006825265737472696e6760d01b6020830152565b604051906156e76040836155bc565b6005825264627974657360d81b6020830152565b6040519061570a6040836155bc565b60048252631d5a5b9d60e21b6020830152565b6040519061572c6040836155bc565b60038252621a5b9d60ea1b6020830152565b600882101561574a5752565b634e487b7160e01b5f52602160045260245ffd5b6040519061576b8261558d565b81602060ff60235461577f8282168561573e565b60081c161515910152565b604051906157978261558d565b81602060ff60375461577f8282168561573e565b519081151582036116b657565b90600882101561574a5752565b90600182811c921680156157f3575b60208310146157df57565b634e487b7160e01b5f52602260045260245ffd5b91607f16916157d4565b6020545f929161580c826157c5565b808252916001811690811561586d5750600114615827575050565b60205f9081529293509091905f5160206187a85f395f51905f525b838310615853575060209250010190565b600181602092949394548385870101520191019190615842565b9050602093945060ff929192191683830152151560051b010190565b5f9291815491615898836157c5565b80835292600181169081156158ed57506001146158b457505050565b5f9081526020812093945091925b8383106158d3575060209250010190565b6001816020929493945483858701015201910191906158c2565b915050602093945060ff929192191683830152151560051b010190565b6080615942916020815260208101602060ff60215461592b848383166157b8565b60081c161515910152606080820152016022615889565b90565b6080615942916020815260208101602060ff602354615966848383166157b8565b60081c161515910152606080820152016024615889565b6080615942916020815260208101602060ff602d5461599e848383166157b8565b60081c16151591015260608082015201602e615889565b6080615942916020815260208101602060ff6031546159d6848383166157b8565b60081c161515910152606080820152016032615889565b6080615942916020815260208101602060ff603b54615a0e848383166157b8565b60081c16151591015260608082015201603c615889565b6001600160401b0381116155a85760051b60200190565b51906001600160a01b03821682036116b657565b6020818303126116b6578051906001600160401b0382116116b657019080601f830112156116b6578151615a8381615a25565b92615a9160405194856155bc565b81845260208085019260051b8201019283116116b657602001905b828210615ab95750505090565b60208091615ac684615a3c565b815201910190615aac565b805115615ade5760200190565b634e487b7160e01b5f52603260045260245ffd5b805160011015615ade5760400190565b60206040818301928281528451809452019201905f5b818110615b255750505090565b8251845260209384019390920191600101615b18565b5f5b828110615b4957505050565b606082820152602001615b3d565b60405190615b666040836155bc565b60038252626f6e6560e81b6020830152565b60405190615b876040836155bc565b600382526274776f60e81b6020830152565b908160209103126116b657516001600160801b03811681036116b65790565b60208091615bc78482516157b8565b01511515910152565b6080602061594293818452615be88285018251615bb8565b0151916060808201520190615456565b60609060208152601e60208201527f76616c756520646f6573206e6f742066697420696e2027696e7431323827000060408201520190565b908160209103126116b6575180600f0b81036116b65790565b51906001600160401b03821682036116b657565b60809060208152602660208201527f76616c756520696e20617272617920646f6573206e6f742066697420696e2027604082015265696e7436342760d01b60608201520190565b51908160070b82036116b657565b6020818303126116b6578051906001600160401b0382116116b657019080601f830112156116b6578151615ce581615a25565b92615cf360405194856155bc565b81845260208085019260051b8201019283116116b657602001905b828210615d1b5750505090565b60208091615d2884615ca4565b815201910190615d0e565b90604051918281549182825260208201905f5260205f20925f905b806007830110615e9257615da4945491818110615e73575b818110615e54575b818110615e35575b818110615e16575b818110615df7575b818110615dd8575b818110615dbb575b10615da6575b5003836155bc565b565b6001600160e01b03191681526020015f615d9c565b602083811b6001600160e01b031916855290930192600101615d96565b604083901b6001600160e01b0319168452602090930192600101615d8e565b606083901b6001600160e01b0319168452602090930192600101615d86565b608083901b6001600160e01b0319168452602090930192600101615d7e565b60a083901b6001600160e01b0319168452602090930192600101615d76565b60c083901b6001600160e01b0319168452602090930192600101615d6e565b60e083901b6001600160e01b0319168452602090930192600101615d66565b916008919350610100600191865463ffffffff60e01b8160e01b16825263ffffffff60e01b8160c01b16602083015263ffffffff60e01b8160a01b16604083015263ffffffff60e01b8160801b16606083015263ffffffff60e01b8160601b16608083015263ffffffff60e01b8160401b1660a083015263ffffffff60e01b8160201b1660c083015263ffffffff60e01b1660e0820152019401920185929391615d4e565b9291926001600160401b0382116155a85760405191615f60601f8201601f1916602001846155bc565b8294818452818301116116b6578281602093845f96015e010152565b9080601f830112156116b657815161594292602001615f37565b6020818303126116b6578051906001600160401b0382116116b657019080601f830112156116b6578151615fc981615a25565b92615fd760405194856155bc565b81845260208085019260051b8201019283116116b657602001905b828210615fff5750505090565b6020809161600c846157ab565b815201910190615ff2565b6004815263189bdbdb60e21b602082015260400190565b6080615942916040815260076040820152663ab4b73a191a9b60c91b606082015281602082015201616017565b6006815265626f6f6c5b5d60d01b602082015260400190565b60085460ff161561608457600190565b604051630667f9d760e41b81525f5160206187c85f395f51905f5260048201526519985a5b195960d21b60248201526020816044815f5160206187c85f395f51905f525afa908115615173575f916160dd575b50151590565b90506020813d602011616107575b816160f8602093836155bc565b810103126116b657515f6160d7565b3d91506160eb565b519060ff821682036116b657565b6159426155ff565b615942615621565b615942615646565b61594261566b565b615942615690565b6159426156b4565b6159426156d8565b600881101561574a57600181146161ca57600281146161c157600381146161b857600481146161af57600581146161a6576006811461619d5760071461614d576159426155dd565b506159426156b4565b50615942615690565b5061594261566b565b50615942615646565b50615942615621565b506159426155ff565b90916161ea61594293604084526040840190615456565b916020818403910152615456565b5f5160206187c85f395f51905f523b156116b65760405163f320d96360e01b8152915f918391829161622e9190600484016161d3565b03815f5160206187c85f395f51905f525afa80156151735761624d5750565b5f615da4916155bc565b6159426156fb565b61594261571d565b8051600881101561574a5761627b90616155565b906020810151159081156162c8575b50156162935790565b6159426002602080936040519481869251918291018484015e8101615b5d60f01b838201520301601d198101845201826155bc565b905051600881101561574a57155f61628a565b908151600881101561574a57815190600882101561574a571491826162ff57505090565b6020919250810151151591015115151490565b158061631b5750565b5f5160206187c85f395f51905f523b156116b657604051630c9fd58160e01b8152901560048201525f816024815f5160206187c85f395f51905f525afa80156151735761624d5750565b8061636d5750565b5f5160206187c85f395f51905f523b156116b65760405163a598288560e01b815290151560048201525f816024815f5160206187c85f395f51905f525afa80156151735761624d5750565b906163c381836162db565b156163cc575050565b6163d86163de91616267565b91616267565b60405163b02cf71d60e01b81529182916163fb91600484016161d3565b0390fd5b6002810361640a5750565b5f5160206187c85f395f51905f523b156116b6576040519063260a5b1560e21b82526004820152600260248201525f816044815f5160206187c85f395f51905f525afa80156151735761624d5750565b606481036164655750565b5f5160206187c85f395f51905f523b156116b6576040519063260a5b1560e21b82526004820152606460248201525f816044815f5160206187c85f395f51905f525afa80156151735761624d5750565b606481036164c05750565b5f5160206187c85f395f51905f523b156116b6576040519063fe74f05b60e01b82526004820152606460248201525f816044815f5160206187c85f395f51905f525afa80156151735761624d5750565b6064810161651b5750565b5f5160206187c85f395f51905f523b156116b65760405163fe74f05b60e01b8152600481019190915260631960248201525f816044815f5160206187c85f395f51905f525afa80156151735761624d575056fe6080806040523460155761221f908161001a8239f35b5f80fdfe60806040526004361015610011575f80fd5b5f5f3560e01c806301a9fdf314611b4657806304f33e3714611a3a5780630e9318b6146119b557806318b6d849146118af578063198c44fc1461176d5780631b8c25c714611716578063269279201461160f57806328924b5614611506578063296a2f41146114975780632f5093131461141657806333571846146113b5578063361b7eb61461134b5780633fb5872b146112cd578063476e1e481461125457806356cd3b68146111cf5780635d0dbfd4146111bc578063713c108f14611142578063718651b81461112757806373dea9ff1461100b5780637994888414610f9e578063825b7bfd14610ea15780638ec7637b14610e29578063938b79b114610d14578063a29eeb7914610cc6578063a59ecfd614610bb6578063a5e1f79214610ab7578063a9cc756b14610975578063ada9f824146108b3578063cd8ceaad1461078d578063e31d23e514610705578063e374b6ac1461060a578063e80f9114146104ec578063ebd42628146103d9578063f3283fb7146102c7578063f7b410741461023b5763fb50451a146101a6575f80fd5b34610238576101bc6101b736611c06565b611ed2565b677fffffffffffffff81138015610226575b6101e0576020906040519060070b8152f35b604051639f9ddabb60e01b815260206004820152601d60248201527f76616c756520646f6573206e6f742066697420696e2027696e743634270000006044820152606490fd5b50677fffffffffffffff1981126101ce565b80fd5b50346102385761024d6101b736611c06565b60016001607f1b03811380156102b6575b6102705760209060405190600f0b8152f35b604051639f9ddabb60e01b815260206004820152601e60248201527f76616c756520646f6573206e6f742066697420696e2027696e743132382700006044820152606490fd5b5060016001607f1b0319811261025e565b5034610238576102de6102d936611c06565b611d05565b9081516103036102ed82611db5565b916102fb6040519384611bca565b808352611db5565b602082019290601f1901368437805b84518110156103915760ff6103278287611dcc565b511161034f578060ff61033c60019388611dcc565b51166103488286611dcc565b5201610312565b604051639f9ddabb60e01b815260206004820152602660248201525f5160206121ca5f395f51905f5260448201526575696e74382760d01b6064820152608490fd5b50925090604051928392602084019060208552518091526040840192915b8181106103bd575050500390f35b825160ff168452859450602093840193909201916001016103af565b50346102385760206103ea36611c06565b6104136040516103f981611b9b565b6005815260018482015261040c83611fcd565b8251611df4565b015180518101906020818184019303126104e4576020810151906001600160401b0382116104e8570181603f820112156104e45760208101519161045683611db5565b916104646040519384611bca565b8383526020830190602080839660051b830101019283116104e057604001905b8282106104d05750505090604051928392602084019060208552518091526040840192915b8181106104b7575050500390f35b82518452859450602093840193909201916001016104a9565b8151815260209182019101610484565b8580fd5b8280fd5b8380fd5b50346102385760206104fd36611c06565b61051f60405161050c81611b9b565b6002815260018482015261040c83611fcd565b015180518101906020818184019303126104e4576020810151906001600160401b0382116104e857019080603f830112156104e45760208201519161056383611db5565b916105716040519384611bca565b8383526020830191602080849660051b830101019182116104e057604001915b8183106105e65750505090604051928392602084019060208552518091526040840192915b8181106105c4575050500390f35b82516001600160a01b03168452859450602093840193909201916001016105b6565b82516001600160a01b038116810361060657815260209283019201610591565b8680fd5b50346102385761061c6102d936611c06565b90815161062b6102ed82611db5565b602082019290601f1901368437805b84518110156106bc5761ffff6106508287611dcc565b5111610679578061ffff61066660019388611dcc565b51166106728286611dcc565b520161063a565b604051639f9ddabb60e01b815260206004820152602760248201525f5160206121ca5f395f51905f5260448201526675696e7431362760c81b6064820152608490fd5b50925090604051928392602084019060208552518091526040840192915b8181106106e8575050500390f35b825161ffff168452859450602093840193909201916001016106da565b503461023857602061071636611c06565b61073760405161072581611b9b565b60078152848482015261040c83611fcd565b01519081518201602083820312610789576020830151916001600160401b0383116102385761078561077185602086818701920101611e81565b604051918291602083526020830190611ce1565b0390f35b5080fd5b5034610238576107a461079f36611c06565b611f30565b9081516107b36102ed82611db5565b602082019290601f1901368437805b845181101561086b57677fffffffffffffff6107de8287611dcc565b5113801561084f575b61080d57806107f860019287611dcc565b5160070b6108068286611dcc565b52016107c2565b604051639f9ddabb60e01b815260206004820152602660248201525f5160206121ca5f395f51905f52604482015265696e7436342760d01b6064820152608490fd5b50677fffffffffffffff196108648287611dcc565b51126107e7565b50925090604051928392602084019060208552518091526040840192915b818110610897575050500390f35b825160070b845285945060209384019390920191600101610889565b5034610971576108c236611c06565b73__$580cbf57661c63d0b788ab76fa58c193a5$__90813b1561097157604051630ad7c7f760e11b81526020600482015281518051919390600883101561095d578461093260205f9681849795859660248701520151151560448501520151606060648401526084830190611ce1565b03915af4801561095257610944575080f35b61095091505f90611bca565b005b6040513d5f823e3d90fd5b634e487b7160e01b5f52602160045260245ffd5b5f80fd5b3461097157602061098536611c06565b6109a760405161099481611b9b565b6007815260018482015261040c83611fcd565b01518051810190602081818401930312610971576020810151906001600160401b03821161097157019080603f83011215610971576020820151906109eb82611db5565b926109f96040519485611bca565b8284526020840190602080839560051b83010101918383116109715760408201905b838210610a8857858760405191829160208301906020845251809152604083019060408160051b85010192915f905b828210610a5957505050500390f35b91936001919395506020610a788192603f198a82030186528851611ce1565b9601920192018594939192610a4a565b81516001600160401b03811161097157602091610aac878480809589010101611e81565b815201910190610a1b565b34610971576020610ac736611c06565b610ae9604051610ad681611b9b565b6003815260018482015261040c83611fcd565b01518051810190602081818401930312610971576020810151906001600160401b03821161097157019080603f8301121561097157602082015190610b2d82611db5565b92610b3b6040519485611bca565b8284526020840190602080839560051b8301010192831161097157604001905b828210610ba6578385604051918291602083019060208452518091526040830191905f5b818110610b8d575050500390f35b8251845285945060209384019390920191600101610b7f565b8151815260209182019101610b5b565b3461097157610bc761079f36611c06565b8051610bd56102ed82611db5565b602082019190601f19013683375f5b8351811015610c8057617fff610bfa8286611dcc565b51138015610c6a575b610c285780610c1460019286611dcc565b51820b610c218285611dcc565b5201610be4565b604051639f9ddabb60e01b815260206004820152602660248201525f5160206121ca5f395f51905f52604482015265696e7431362760d01b6064820152608490fd5b50617fff19610c798286611dcc565b5112610c03565b50604051918291602083019060208452518091526040830191905f5b818110610caa575050500390f35b8251600190810b85528695506020948501949093019201610c9c565b34610971576020610cd636611c06565b610cf7604051610ce581611b9b565b600381525f8482015261040c83611fcd565b015160208180518101031261097157602080910151604051908152f35b3461097157610d2561079f36611c06565b8051610d336102ed82611db5565b602082019190601f19013683375f5b8351811015610de357637fffffff610d5a8286611dcc565b51138015610dcb575b610d895780610d7460019286611dcc565b5160030b610d828285611dcc565b5201610d42565b604051639f9ddabb60e01b815260206004820152602660248201525f5160206121ca5f395f51905f52604482015265696e7433322760d01b6064820152608490fd5b50637fffffff19610ddc8286611dcc565b5112610d63565b50604051918291602083019060208452518091526040830191905f5b818110610e0d575050500390f35b825160030b845285945060209384019390920191600101610dff565b3461097157610e3f610e3a36611c06565b611f0c565b63ffffffff8111610e5b5760209063ffffffff60405191168152f35b604051639f9ddabb60e01b815260206004820152601e60248201527f76616c756520646f6573206e6f742066697420696e202775696e7433322700006044820152606490fd5b3461097157610eb26102d936611c06565b8051610ec06102ed82611db5565b602082019190601f19013683375f5b8351811015610f555763ffffffff610ee78286611dcc565b5111610f12578063ffffffff610eff60019387611dcc565b5116610f0b8285611dcc565b5201610ecf565b604051639f9ddabb60e01b815260206004820152602760248201525f5160206121ca5f395f51905f5260448201526675696e7433322760c81b6064820152608490fd5b50604051918291602083019060208452518091526040830191905f5b818110610f7f575050500390f35b825163ffffffff16845285945060209384019390920191600101610f71565b3461097157610faf610e3a36611c06565b60ff8111610fc55760209060ff60405191168152f35b604051639f9ddabb60e01b815260206004820152601d60248201527f76616c756520646f6573206e6f742066697420696e202775696e7438270000006044820152606490fd5b346109715761101c61079f36611c06565b805161102a6102ed82611db5565b602082019190601f19013683375f5b83518110156110e15760016001607f1b036110548286611dcc565b511380156110c6575b611083578061106e60019286611dcc565b51600f0b61107c8285611dcc565b5201611039565b604051639f9ddabb60e01b815260206004820152602760248201525f5160206121ca5f395f51905f52604482015266696e743132382760c81b6064820152608490fd5b5060016001607f1b03196110da8286611dcc565b511261105d565b50604051918291602083019060208452518091526040830191905f5b81811061110b575050500390f35b8251600f0b8452859450602093840193909201916001016110fd565b3461097157602061113a610e3a36611c06565b604051908152f35b3461097157611153610e3a36611c06565b6001600160801b038111611176576040516001600160801b039091168152602090f35b604051639f9ddabb60e01b815260206004820152601f60248201527f76616c756520646f6573206e6f742066697420696e202775696e7431323827006044820152606490fd5b3461097157602061113a6101b736611c06565b34610971576111e06101b736611c06565b637fffffff81138015611246575b611200576020906040519060030b8152f35b604051639f9ddabb60e01b815260206004820152601d60248201527f76616c756520646f6573206e6f742066697420696e2027696e743332270000006044820152606490fd5b50637fffffff1981126111ee565b3461097157611265610e3a36611c06565b6001600160401b038111611287576020906001600160401b0360405191168152f35b604051639f9ddabb60e01b815260206004820152601e60248201527f76616c756520646f6573206e6f742066697420696e202775696e7436342700006044820152606490fd5b34610971576112de6101b736611c06565b607f81138015611340575b6112fa57602090604051905f0b8152f35b604051639f9ddabb60e01b815260206004820152601c60248201527f76616c756520646f6573206e6f742066697420696e2027696e743827000000006044820152606490fd5b50607f1981126112e9565b3461097157602061135b36611c06565b61137c60405161136a81611b9b565b600681525f8482015261040c83611fcd565b01518051810190602081830312610971576020810151906001600160401b03821161097157602061077192816107859501920101611e81565b346109715760206113c536611c06565b6113e66040516113d481611b9b565b600281525f8482015261040c83611fcd565b015160208180518101031261097157602001516001600160a01b0381169081900361097157602090604051908152f35b34610971576114276101b736611c06565b617fff8113801561148b575b611445576020906040519060010b8152f35b604051639f9ddabb60e01b815260206004820152601d60248201527f76616c756520646f6573206e6f742066697420696e2027696e743136270000006044820152606490fd5b50617fff198112611433565b34610971576114a8610e3a36611c06565b61ffff81116114c05760209061ffff60405191168152f35b604051639f9ddabb60e01b815260206004820152601e60248201527f76616c756520646f6573206e6f742066697420696e202775696e7431362700006044820152606490fd5b3461097157602061151636611c06565b61153860405161152581611b9b565b6001815260018482015261040c83611fcd565b01518051810190602081818401930312610971576020810151906001600160401b03821161097157019080603f830112156109715760208201519061157c82611db5565b9261158a6040519485611bca565b8284526020840190602080839560051b8301010192831161097157604001905b8282106115f7578385604051918291602083019060208452518091526040830191905f5b8181106115dc575050500390f35b825115158452859450602093840193909201916001016115ce565b6020809161160484611ec5565b8152019101906115aa565b34610971576116206102d936611c06565b805161162e6102ed82611db5565b602082019190601f19013683375f5b83518110156116ca576001600160801b036116588286611dcc565b5111611686576001906001600160801b036116738287611dcc565b511661167f8285611dcc565b520161163d565b604051639f9ddabb60e01b815260206004820152602860248201525f5160206121ca5f395f51905f5260448201526775696e743132382760c01b6064820152608490fd5b50604051918291602083019060208452518091526040830191905f5b8181106116f4575050500390f35b82516001600160801b03168452859450602093840193909201916001016116e6565b3461097157602061172636611c06565b61174760405161173581611b9b565b600181525f8482015261040c83611fcd565b0151602081805181010312610971576117636020809201611ec5565b6040519015158152f35b3461097157602061177d36611c06565b61179f60405161178c81611b9b565b6006815260018482015261040c83611fcd565b01518051810190602081818401930312610971576020810151906001600160401b03821161097157019080603f83011215610971576020820151906117e382611db5565b926117f16040519485611bca565b8284526020840190602080839560051b83010101918383116109715760408201905b83821061188057858760405191829160208301906020845251809152604083019060408160051b85010192915f905b82821061185157505050500390f35b919360019193955060206118708192603f198a82030186528851611ce1565b9601920192018594939192611842565b81516001600160401b038111610971576020916118a4878480809589010101611e81565b815201910190611813565b34610971576118c06102d936611c06565b80516118ce6102ed82611db5565b602082019190601f19013683375f5b8351811015611969576001600160401b036118f88286611dcc565b511161192657806001600160401b0361191360019387611dcc565b511661191f8285611dcc565b52016118dd565b604051639f9ddabb60e01b815260206004820152602760248201525f5160206121ca5f395f51905f5260448201526675696e7436342760c81b6064820152608490fd5b50604051918291602083019060208452518091526040830191905f5b818110611993575050500390f35b82516001600160401b0316845285945060209384019390920191600101611985565b346109715736600319016080811261097157604013610971576040516119da81611b9b565b60043560088110156109715781526024358015158103610971576020820152604036604319011261097157604051611a1181611b9b565b604435600881101561097157815260643591821515830361097157610950926020830152611df4565b3461097157611a4b61079f36611c06565b8051611a596102ed82611db5565b602082019190601f19013683375f5b8351811015611b0157607f611a7d8286611dcc565b51138015611aec575b611aab5780611a9760019286611dcc565b515f0b611aa48285611dcc565b5201611a68565b604051639f9ddabb60e01b815260206004820152602560248201525f5160206121ca5f395f51905f52604482015264696e74382760d81b6064820152608490fd5b50607f19611afa8286611dcc565b5112611a86565b50604051918291602083019060208452518091526040830191905f5b818110611b2b575050500390f35b82515f0b845285945060209384019390920191600101611b1d565b3461097157611b576102d936611c06565b6040518091602082016020835281518091526020604084019201905f5b818110611b82575050500390f35b8251845285945060209384019390920191600101611b74565b604081019081106001600160401b03821117611bb657604052565b634e487b7160e01b5f52604160045260245ffd5b90601f801991011681019081106001600160401b03821117611bb657604052565b6001600160401b038111611bb657601f01601f191660200190565b602060031982011261097157600435906001600160401b03821161097157606082820360031901126109715760405191611c3f83611b9b565b806004016040818403126109715760405190611c5a82611b9b565b80359060088210156109715760209183520135801515810361097157602082015283526044810135906001600160401b03821161097157018160238201121561097157600481013590611cac82611beb565b92611cba6040519485611bca565b8284526024828401011161097157815f926024602093018386013783010152602082015290565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b602090611d2a604051611d1781611b9b565b6004815260018482015261040c83611fcd565b01518051810190602081818401930312610971576020810151906001600160401b03821161097157019080603f83011215610971576020820151611d6d81611db5565b92611d7b6040519485611bca565b8184526020808086019360051b8301010192831161097157604001905b828210611da55750505090565b8151815260209182019101611d98565b6001600160401b038111611bb65760051b60200190565b8051821015611de05760209160051b010190565b634e487b7160e01b5f52603260045260245ffd5b908151600881101561095d57815190600882101561095d571480611e6c575b15611e1c575050565b90611e68611e35611e2f611e5694611fee565b92611fee565b60405193849363b02cf71d60e01b8552604060048601526044850190611ce1565b83810360031901602485015290611ce1565b0390fd5b50602082015115156020820151151514611e13565b81601f8201121561097157602081519101611e9b82611beb565b92611ea96040519485611bca565b8284528282011161097157815f926020928386015e8301015290565b5190811515820361097157565b602090611ef6604051611ee481611b9b565b600581525f8482015261040c83611fcd565b0151602081805181010312610971576020015190565b602090611ef6604051611f1e81611b9b565b600481525f8482015261040c83611fcd565b602090611f426040516103f981611b9b565b01518051810190602081818401930312610971576020810151906001600160401b03821161097157019080603f83011215610971576020820151611f8581611db5565b92611f936040519485611bca565b8184526020808086019360051b8301010192831161097157604001905b828210611fbd5750505090565b8151815260209182019101611fb0565b5151600881101561095d5715611fdf57565b6321c4e35760e21b5f5260045ffd5b8051600881101561095d5761200290612065565b90602081015115908115612052575b501561201a5790565b61204f6002602080936040519481869251918291018484015e8101615b5d60f01b838201520301601d19810184520182611bca565b90565b905051600881101561095d57155f612011565b600881101561095d57600181146121a65760028114612180576003811461215a5760048114612134576005811461210f57600681146120ea576007146120c7576040516120b3604082611bca565b60048152636e6f6e6560e01b602082015290565b6040516120d5604082611bca565b6005815264627974657360d81b602082015290565b506040516120f9604082611bca565b6006815265737472696e6760d01b602082015290565b5060405161211e604082611bca565b600681526534b73a191a9b60d11b602082015290565b50604051612143604082611bca565b60078152663ab4b73a191a9b60c91b602082015290565b50604051612169604082611bca565b6007815266313cba32b9999960c91b602082015290565b5060405161218f604082611bca565b60078152666164647265737360c81b602082015290565b506040516121b5604082611bca565b6004815263189bdbdb60e21b60208201529056fe76616c756520696e20617272617920646f6573206e6f742066697420696e2027a26469706673582212200c97d5d8488b07778f13860b856bd3685fc854121aa4b40bac8e96cacd7b8e5564736f6c63430008210033c97bfaf2f8ee708c303a06d134f5ecd8389ae0432af62dc132a24118292866bb0000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da2646970667358221220195a1fe4fb87f7fa2595253aeca3270b53d5df853f7e8c7b0edca6e00c750fbd64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, libVariable: Optional[Union[LibVariable, Address]] = None, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, libVariable: Optional[Union[LibVariable, Address]] = None, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> LibVariableTest:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, libVariable: Optional[Union[LibVariable, Address]] = None, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, libVariable: Optional[Union[LibVariable, Address]] = None, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], libVariable: Optional[Union[LibVariable, Address]] = None, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[LibVariableTest]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, libVariable: Optional[Union[LibVariable, Address]] = None, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, LibVariableTest, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[LibVariableTest]]:
        return cls._deploy(request_type, [], return_tx, LibVariableTest, from_, value, gas_limit, {b'X\x0c\xbfWf\x1cc\xd0\xb7\x88\xabv\xfaX\xc1\x93\xa5': (libVariable, 'LibVariable')}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls, libVariable: Union[LibVariable, Address]) -> bytes:
        return cls._get_creation_code({b'X\x0c\xbfWf\x1cc\xd0\xb7\x88\xabv\xfaX\xc1\x93\xa5': (libVariable, 'LibVariable')})

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#30)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#30)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#30)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#30)
        """
        ...

    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#30)
        """
        return self._execute(self.chain, request_type, "0a9254e4", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_TypeHelpers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#84)
        """
        ...

    @overload
    def test_TypeHelpers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#84)
        """
        ...

    @overload
    def test_TypeHelpers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#84)
        """
        ...

    @overload
    def test_TypeHelpers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#84)
        """
        ...

    def test_TypeHelpers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#84)
        """
        return self._execute(self.chain, request_type, "09bd759b", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_Coercion(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#117)
        """
        ...

    @overload
    def test_Coercion(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#117)
        """
        ...

    @overload
    def test_Coercion(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#117)
        """
        ...

    @overload
    def test_Coercion(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#117)
        """
        ...

    def test_Coercion(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#117)
        """
        return self._execute(self.chain, request_type, "a4b9d9ed", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_Downcasting(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#146)
        """
        ...

    @overload
    def test_Downcasting(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#146)
        """
        ...

    @overload
    def test_Downcasting(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#146)
        """
        ...

    @overload
    def test_Downcasting(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#146)
        """
        ...

    def test_Downcasting(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#146)
        """
        return self._execute(self.chain, request_type, "d44436cb", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testRevert_NotInitialized(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#185)
        """
        ...

    @overload
    def testRevert_NotInitialized(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#185)
        """
        ...

    @overload
    def testRevert_NotInitialized(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#185)
        """
        ...

    @overload
    def testRevert_NotInitialized(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#185)
        """
        ...

    def testRevert_NotInitialized(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#185)
        """
        return self._execute(self.chain, request_type, "0a1c9c74", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testRevert_assertExists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#193)
        """
        ...

    @overload
    def testRevert_assertExists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#193)
        """
        ...

    @overload
    def testRevert_assertExists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#193)
        """
        ...

    @overload
    def testRevert_assertExists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#193)
        """
        ...

    def testRevert_assertExists(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#193)
        """
        return self._execute(self.chain, request_type, "af584eee", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testRevert_TypeMismatch(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#198)
        """
        ...

    @overload
    def testRevert_TypeMismatch(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#198)
        """
        ...

    @overload
    def testRevert_TypeMismatch(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#198)
        """
        ...

    @overload
    def testRevert_TypeMismatch(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#198)
        """
        ...

    def testRevert_TypeMismatch(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#198)
        """
        return self._execute(self.chain, request_type, "adecb4af", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testRevert_UnsafeCast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#226)
        """
        ...

    @overload
    def testRevert_UnsafeCast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#226)
        """
        ...

    @overload
    def testRevert_UnsafeCast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#226)
        """
        ...

    @overload
    def testRevert_UnsafeCast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#226)
        """
        ...

    def testRevert_UnsafeCast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#226)
        """
        return self._execute(self.chain, request_type, "60e9d824", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

LibVariableTest.setUp.selector = bytes4(b'\n\x92T\xe4')
LibVariableTest.test_TypeHelpers.selector = bytes4(b'\t\xbdu\x9b')
LibVariableTest.test_Coercion.selector = bytes4(b'\xa4\xb9\xd9\xed')
LibVariableTest.test_Downcasting.selector = bytes4(b'\xd4D6\xcb')
LibVariableTest.testRevert_NotInitialized.selector = bytes4(b'\n\x1c\x9ct')
LibVariableTest.testRevert_assertExists.selector = bytes4(b'\xafXN\xee')
LibVariableTest.testRevert_TypeMismatch.selector = bytes4(b'\xad\xec\xb4\xaf')
LibVariableTest.testRevert_UnsafeCast.selector = bytes4(b'`\xe9\xd8$')
class LibVariableHelper(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#280)
    """
    _abi = {b'\x87\x13\x8d\\': {'inputs': [], 'name': 'NotInitialized', 'type': 'error'}, b'\xb0,\xf7\x1d': {'inputs': [{'internalType': 'string', 'name': 'expected', 'type': 'string'}, {'internalType': 'string', 'name': 'actual', 'type': 'string'}], 'name': 'TypeMismatch', 'type': 'error'}, b'\x9f\x9d\xda\xbb': {'inputs': [{'internalType': 'string', 'name': 'message', 'type': 'string'}], 'name': 'UnsafeCast', 'type': 'error'}, b'\x0e\x93\x18\xb6': {'inputs': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 't1', 'type': 'tuple'}, {'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 't2', 'type': 'tuple'}], 'name': 'assertEq', 'outputs': [], 'stateMutability': 'pure', 'type': 'function'}, b'\xad\xa9\xf8$': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'assertExists', 'outputs': [], 'stateMutability': 'pure', 'type': 'function'}, b'3W\x18F': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toAddress', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'pure', 'type': 'function'}, b'\xe8\x0f\x91\x14': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toAddressArray', 'outputs': [{'internalType': 'address[]', 'name': '', 'type': 'address[]'}], 'stateMutability': 'pure', 'type': 'function'}, b'\x1b\x8c%\xc7': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toBool', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'pure', 'type': 'function'}, b'(\x92KV': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toBoolArray', 'outputs': [{'internalType': 'bool[]', 'name': '', 'type': 'bool[]'}], 'stateMutability': 'pure', 'type': 'function'}, b'\xe3\x1d#\xe5': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toBytes', 'outputs': [{'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'stateMutability': 'pure', 'type': 'function'}, b'\xa2\x9e\xeby': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toBytes32', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'pure', 'type': 'function'}, b'\xa5\xe1\xf7\x92': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toBytes32Array', 'outputs': [{'internalType': 'bytes32[]', 'name': '', 'type': 'bytes32[]'}], 'stateMutability': 'pure', 'type': 'function'}, b'\xa9\xccuk': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toBytesArray', 'outputs': [{'internalType': 'bytes[]', 'name': '', 'type': 'bytes[]'}], 'stateMutability': 'pure', 'type': 'function'}, b'\xf7\xb4\x10t': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toInt128', 'outputs': [{'internalType': 'int128', 'name': '', 'type': 'int128'}], 'stateMutability': 'pure', 'type': 'function'}, b's\xde\xa9\xff': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toInt128Array', 'outputs': [{'internalType': 'int128[]', 'name': '', 'type': 'int128[]'}], 'stateMutability': 'pure', 'type': 'function'}, b'/P\x93\x13': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toInt16', 'outputs': [{'internalType': 'int16', 'name': '', 'type': 'int16'}], 'stateMutability': 'pure', 'type': 'function'}, b'\xa5\x9e\xcf\xd6': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toInt16Array', 'outputs': [{'internalType': 'int16[]', 'name': '', 'type': 'int16[]'}], 'stateMutability': 'pure', 'type': 'function'}, b']\r\xbf\xd4': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toInt256', 'outputs': [{'internalType': 'int256', 'name': '', 'type': 'int256'}], 'stateMutability': 'pure', 'type': 'function'}, b'\xeb\xd4&(': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toInt256Array', 'outputs': [{'internalType': 'int256[]', 'name': '', 'type': 'int256[]'}], 'stateMutability': 'pure', 'type': 'function'}, b'V\xcd;h': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toInt32', 'outputs': [{'internalType': 'int32', 'name': '', 'type': 'int32'}], 'stateMutability': 'pure', 'type': 'function'}, b'\x93\x8by\xb1': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toInt32Array', 'outputs': [{'internalType': 'int32[]', 'name': '', 'type': 'int32[]'}], 'stateMutability': 'pure', 'type': 'function'}, b'\xfbPE\x1a': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toInt64', 'outputs': [{'internalType': 'int64', 'name': '', 'type': 'int64'}], 'stateMutability': 'pure', 'type': 'function'}, b'\xcd\x8c\xea\xad': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toInt64Array', 'outputs': [{'internalType': 'int64[]', 'name': '', 'type': 'int64[]'}], 'stateMutability': 'pure', 'type': 'function'}, b'?\xb5\x87+': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toInt8', 'outputs': [{'internalType': 'int8', 'name': '', 'type': 'int8'}], 'stateMutability': 'pure', 'type': 'function'}, b'\x04\xf3>7': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toInt8Array', 'outputs': [{'internalType': 'int8[]', 'name': '', 'type': 'int8[]'}], 'stateMutability': 'pure', 'type': 'function'}, b'6\x1b~\xb6': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toString', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'pure', 'type': 'function'}, b'\x19\x8cD\xfc': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toStringArray', 'outputs': [{'internalType': 'string[]', 'name': '', 'type': 'string[]'}], 'stateMutability': 'pure', 'type': 'function'}, b'q<\x10\x8f': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toUint128', 'outputs': [{'internalType': 'uint128', 'name': '', 'type': 'uint128'}], 'stateMutability': 'pure', 'type': 'function'}, b'&\x92y ': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toUint128Array', 'outputs': [{'internalType': 'uint128[]', 'name': '', 'type': 'uint128[]'}], 'stateMutability': 'pure', 'type': 'function'}, b')j/A': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toUint16', 'outputs': [{'internalType': 'uint16', 'name': '', 'type': 'uint16'}], 'stateMutability': 'pure', 'type': 'function'}, b'\xe3t\xb6\xac': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toUint16Array', 'outputs': [{'internalType': 'uint16[]', 'name': '', 'type': 'uint16[]'}], 'stateMutability': 'pure', 'type': 'function'}, b'q\x86Q\xb8': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toUint256', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'pure', 'type': 'function'}, b'\x01\xa9\xfd\xf3': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toUint256Array', 'outputs': [{'internalType': 'uint256[]', 'name': '', 'type': 'uint256[]'}], 'stateMutability': 'pure', 'type': 'function'}, b'\x8e\xc7c{': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toUint32', 'outputs': [{'internalType': 'uint32', 'name': '', 'type': 'uint32'}], 'stateMutability': 'pure', 'type': 'function'}, b'\x82[{\xfd': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toUint32Array', 'outputs': [{'internalType': 'uint32[]', 'name': '', 'type': 'uint32[]'}], 'stateMutability': 'pure', 'type': 'function'}, b'Gn\x1eH': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toUint64', 'outputs': [{'internalType': 'uint64', 'name': '', 'type': 'uint64'}], 'stateMutability': 'pure', 'type': 'function'}, b'\x18\xb6\xd8I': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toUint64Array', 'outputs': [{'internalType': 'uint64[]', 'name': '', 'type': 'uint64[]'}], 'stateMutability': 'pure', 'type': 'function'}, b'y\x94\x88\x84': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toUint8', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'pure', 'type': 'function'}, b'\xf3(?\xb7': {'inputs': [{'components': [{'components': [{'internalType': 'enum TypeKind', 'name': 'kind', 'type': 'uint8'}, {'internalType': 'bool', 'name': 'isArray', 'type': 'bool'}], 'internalType': 'struct Type', 'name': 'ty', 'type': 'tuple'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'internalType': 'struct Variable', 'name': 'v', 'type': 'tuple'}], 'name': 'toUint8Array', 'outputs': [{'internalType': 'uint8[]', 'name': '', 'type': 'uint8[]'}], 'stateMutability': 'pure', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = "6080806040523460155761221f908161001a8239f35b5f80fdfe60806040526004361015610011575f80fd5b5f5f3560e01c806301a9fdf314611b4657806304f33e3714611a3a5780630e9318b6146119b557806318b6d849146118af578063198c44fc1461176d5780631b8c25c714611716578063269279201461160f57806328924b5614611506578063296a2f41146114975780632f5093131461141657806333571846146113b5578063361b7eb61461134b5780633fb5872b146112cd578063476e1e481461125457806356cd3b68146111cf5780635d0dbfd4146111bc578063713c108f14611142578063718651b81461112757806373dea9ff1461100b5780637994888414610f9e578063825b7bfd14610ea15780638ec7637b14610e29578063938b79b114610d14578063a29eeb7914610cc6578063a59ecfd614610bb6578063a5e1f79214610ab7578063a9cc756b14610975578063ada9f824146108b3578063cd8ceaad1461078d578063e31d23e514610705578063e374b6ac1461060a578063e80f9114146104ec578063ebd42628146103d9578063f3283fb7146102c7578063f7b410741461023b5763fb50451a146101a6575f80fd5b34610238576101bc6101b736611c06565b611ed2565b677fffffffffffffff81138015610226575b6101e0576020906040519060070b8152f35b604051639f9ddabb60e01b815260206004820152601d60248201527f76616c756520646f6573206e6f742066697420696e2027696e743634270000006044820152606490fd5b50677fffffffffffffff1981126101ce565b80fd5b50346102385761024d6101b736611c06565b60016001607f1b03811380156102b6575b6102705760209060405190600f0b8152f35b604051639f9ddabb60e01b815260206004820152601e60248201527f76616c756520646f6573206e6f742066697420696e2027696e743132382700006044820152606490fd5b5060016001607f1b0319811261025e565b5034610238576102de6102d936611c06565b611d05565b9081516103036102ed82611db5565b916102fb6040519384611bca565b808352611db5565b602082019290601f1901368437805b84518110156103915760ff6103278287611dcc565b511161034f578060ff61033c60019388611dcc565b51166103488286611dcc565b5201610312565b604051639f9ddabb60e01b815260206004820152602660248201525f5160206121ca5f395f51905f5260448201526575696e74382760d01b6064820152608490fd5b50925090604051928392602084019060208552518091526040840192915b8181106103bd575050500390f35b825160ff168452859450602093840193909201916001016103af565b50346102385760206103ea36611c06565b6104136040516103f981611b9b565b6005815260018482015261040c83611fcd565b8251611df4565b015180518101906020818184019303126104e4576020810151906001600160401b0382116104e8570181603f820112156104e45760208101519161045683611db5565b916104646040519384611bca565b8383526020830190602080839660051b830101019283116104e057604001905b8282106104d05750505090604051928392602084019060208552518091526040840192915b8181106104b7575050500390f35b82518452859450602093840193909201916001016104a9565b8151815260209182019101610484565b8580fd5b8280fd5b8380fd5b50346102385760206104fd36611c06565b61051f60405161050c81611b9b565b6002815260018482015261040c83611fcd565b015180518101906020818184019303126104e4576020810151906001600160401b0382116104e857019080603f830112156104e45760208201519161056383611db5565b916105716040519384611bca565b8383526020830191602080849660051b830101019182116104e057604001915b8183106105e65750505090604051928392602084019060208552518091526040840192915b8181106105c4575050500390f35b82516001600160a01b03168452859450602093840193909201916001016105b6565b82516001600160a01b038116810361060657815260209283019201610591565b8680fd5b50346102385761061c6102d936611c06565b90815161062b6102ed82611db5565b602082019290601f1901368437805b84518110156106bc5761ffff6106508287611dcc565b5111610679578061ffff61066660019388611dcc565b51166106728286611dcc565b520161063a565b604051639f9ddabb60e01b815260206004820152602760248201525f5160206121ca5f395f51905f5260448201526675696e7431362760c81b6064820152608490fd5b50925090604051928392602084019060208552518091526040840192915b8181106106e8575050500390f35b825161ffff168452859450602093840193909201916001016106da565b503461023857602061071636611c06565b61073760405161072581611b9b565b60078152848482015261040c83611fcd565b01519081518201602083820312610789576020830151916001600160401b0383116102385761078561077185602086818701920101611e81565b604051918291602083526020830190611ce1565b0390f35b5080fd5b5034610238576107a461079f36611c06565b611f30565b9081516107b36102ed82611db5565b602082019290601f1901368437805b845181101561086b57677fffffffffffffff6107de8287611dcc565b5113801561084f575b61080d57806107f860019287611dcc565b5160070b6108068286611dcc565b52016107c2565b604051639f9ddabb60e01b815260206004820152602660248201525f5160206121ca5f395f51905f52604482015265696e7436342760d01b6064820152608490fd5b50677fffffffffffffff196108648287611dcc565b51126107e7565b50925090604051928392602084019060208552518091526040840192915b818110610897575050500390f35b825160070b845285945060209384019390920191600101610889565b5034610971576108c236611c06565b73__$580cbf57661c63d0b788ab76fa58c193a5$__90813b1561097157604051630ad7c7f760e11b81526020600482015281518051919390600883101561095d578461093260205f9681849795859660248701520151151560448501520151606060648401526084830190611ce1565b03915af4801561095257610944575080f35b61095091505f90611bca565b005b6040513d5f823e3d90fd5b634e487b7160e01b5f52602160045260245ffd5b5f80fd5b3461097157602061098536611c06565b6109a760405161099481611b9b565b6007815260018482015261040c83611fcd565b01518051810190602081818401930312610971576020810151906001600160401b03821161097157019080603f83011215610971576020820151906109eb82611db5565b926109f96040519485611bca565b8284526020840190602080839560051b83010101918383116109715760408201905b838210610a8857858760405191829160208301906020845251809152604083019060408160051b85010192915f905b828210610a5957505050500390f35b91936001919395506020610a788192603f198a82030186528851611ce1565b9601920192018594939192610a4a565b81516001600160401b03811161097157602091610aac878480809589010101611e81565b815201910190610a1b565b34610971576020610ac736611c06565b610ae9604051610ad681611b9b565b6003815260018482015261040c83611fcd565b01518051810190602081818401930312610971576020810151906001600160401b03821161097157019080603f8301121561097157602082015190610b2d82611db5565b92610b3b6040519485611bca565b8284526020840190602080839560051b8301010192831161097157604001905b828210610ba6578385604051918291602083019060208452518091526040830191905f5b818110610b8d575050500390f35b8251845285945060209384019390920191600101610b7f565b8151815260209182019101610b5b565b3461097157610bc761079f36611c06565b8051610bd56102ed82611db5565b602082019190601f19013683375f5b8351811015610c8057617fff610bfa8286611dcc565b51138015610c6a575b610c285780610c1460019286611dcc565b51820b610c218285611dcc565b5201610be4565b604051639f9ddabb60e01b815260206004820152602660248201525f5160206121ca5f395f51905f52604482015265696e7431362760d01b6064820152608490fd5b50617fff19610c798286611dcc565b5112610c03565b50604051918291602083019060208452518091526040830191905f5b818110610caa575050500390f35b8251600190810b85528695506020948501949093019201610c9c565b34610971576020610cd636611c06565b610cf7604051610ce581611b9b565b600381525f8482015261040c83611fcd565b015160208180518101031261097157602080910151604051908152f35b3461097157610d2561079f36611c06565b8051610d336102ed82611db5565b602082019190601f19013683375f5b8351811015610de357637fffffff610d5a8286611dcc565b51138015610dcb575b610d895780610d7460019286611dcc565b5160030b610d828285611dcc565b5201610d42565b604051639f9ddabb60e01b815260206004820152602660248201525f5160206121ca5f395f51905f52604482015265696e7433322760d01b6064820152608490fd5b50637fffffff19610ddc8286611dcc565b5112610d63565b50604051918291602083019060208452518091526040830191905f5b818110610e0d575050500390f35b825160030b845285945060209384019390920191600101610dff565b3461097157610e3f610e3a36611c06565b611f0c565b63ffffffff8111610e5b5760209063ffffffff60405191168152f35b604051639f9ddabb60e01b815260206004820152601e60248201527f76616c756520646f6573206e6f742066697420696e202775696e7433322700006044820152606490fd5b3461097157610eb26102d936611c06565b8051610ec06102ed82611db5565b602082019190601f19013683375f5b8351811015610f555763ffffffff610ee78286611dcc565b5111610f12578063ffffffff610eff60019387611dcc565b5116610f0b8285611dcc565b5201610ecf565b604051639f9ddabb60e01b815260206004820152602760248201525f5160206121ca5f395f51905f5260448201526675696e7433322760c81b6064820152608490fd5b50604051918291602083019060208452518091526040830191905f5b818110610f7f575050500390f35b825163ffffffff16845285945060209384019390920191600101610f71565b3461097157610faf610e3a36611c06565b60ff8111610fc55760209060ff60405191168152f35b604051639f9ddabb60e01b815260206004820152601d60248201527f76616c756520646f6573206e6f742066697420696e202775696e7438270000006044820152606490fd5b346109715761101c61079f36611c06565b805161102a6102ed82611db5565b602082019190601f19013683375f5b83518110156110e15760016001607f1b036110548286611dcc565b511380156110c6575b611083578061106e60019286611dcc565b51600f0b61107c8285611dcc565b5201611039565b604051639f9ddabb60e01b815260206004820152602760248201525f5160206121ca5f395f51905f52604482015266696e743132382760c81b6064820152608490fd5b5060016001607f1b03196110da8286611dcc565b511261105d565b50604051918291602083019060208452518091526040830191905f5b81811061110b575050500390f35b8251600f0b8452859450602093840193909201916001016110fd565b3461097157602061113a610e3a36611c06565b604051908152f35b3461097157611153610e3a36611c06565b6001600160801b038111611176576040516001600160801b039091168152602090f35b604051639f9ddabb60e01b815260206004820152601f60248201527f76616c756520646f6573206e6f742066697420696e202775696e7431323827006044820152606490fd5b3461097157602061113a6101b736611c06565b34610971576111e06101b736611c06565b637fffffff81138015611246575b611200576020906040519060030b8152f35b604051639f9ddabb60e01b815260206004820152601d60248201527f76616c756520646f6573206e6f742066697420696e2027696e743332270000006044820152606490fd5b50637fffffff1981126111ee565b3461097157611265610e3a36611c06565b6001600160401b038111611287576020906001600160401b0360405191168152f35b604051639f9ddabb60e01b815260206004820152601e60248201527f76616c756520646f6573206e6f742066697420696e202775696e7436342700006044820152606490fd5b34610971576112de6101b736611c06565b607f81138015611340575b6112fa57602090604051905f0b8152f35b604051639f9ddabb60e01b815260206004820152601c60248201527f76616c756520646f6573206e6f742066697420696e2027696e743827000000006044820152606490fd5b50607f1981126112e9565b3461097157602061135b36611c06565b61137c60405161136a81611b9b565b600681525f8482015261040c83611fcd565b01518051810190602081830312610971576020810151906001600160401b03821161097157602061077192816107859501920101611e81565b346109715760206113c536611c06565b6113e66040516113d481611b9b565b600281525f8482015261040c83611fcd565b015160208180518101031261097157602001516001600160a01b0381169081900361097157602090604051908152f35b34610971576114276101b736611c06565b617fff8113801561148b575b611445576020906040519060010b8152f35b604051639f9ddabb60e01b815260206004820152601d60248201527f76616c756520646f6573206e6f742066697420696e2027696e743136270000006044820152606490fd5b50617fff198112611433565b34610971576114a8610e3a36611c06565b61ffff81116114c05760209061ffff60405191168152f35b604051639f9ddabb60e01b815260206004820152601e60248201527f76616c756520646f6573206e6f742066697420696e202775696e7431362700006044820152606490fd5b3461097157602061151636611c06565b61153860405161152581611b9b565b6001815260018482015261040c83611fcd565b01518051810190602081818401930312610971576020810151906001600160401b03821161097157019080603f830112156109715760208201519061157c82611db5565b9261158a6040519485611bca565b8284526020840190602080839560051b8301010192831161097157604001905b8282106115f7578385604051918291602083019060208452518091526040830191905f5b8181106115dc575050500390f35b825115158452859450602093840193909201916001016115ce565b6020809161160484611ec5565b8152019101906115aa565b34610971576116206102d936611c06565b805161162e6102ed82611db5565b602082019190601f19013683375f5b83518110156116ca576001600160801b036116588286611dcc565b5111611686576001906001600160801b036116738287611dcc565b511661167f8285611dcc565b520161163d565b604051639f9ddabb60e01b815260206004820152602860248201525f5160206121ca5f395f51905f5260448201526775696e743132382760c01b6064820152608490fd5b50604051918291602083019060208452518091526040830191905f5b8181106116f4575050500390f35b82516001600160801b03168452859450602093840193909201916001016116e6565b3461097157602061172636611c06565b61174760405161173581611b9b565b600181525f8482015261040c83611fcd565b0151602081805181010312610971576117636020809201611ec5565b6040519015158152f35b3461097157602061177d36611c06565b61179f60405161178c81611b9b565b6006815260018482015261040c83611fcd565b01518051810190602081818401930312610971576020810151906001600160401b03821161097157019080603f83011215610971576020820151906117e382611db5565b926117f16040519485611bca565b8284526020840190602080839560051b83010101918383116109715760408201905b83821061188057858760405191829160208301906020845251809152604083019060408160051b85010192915f905b82821061185157505050500390f35b919360019193955060206118708192603f198a82030186528851611ce1565b9601920192018594939192611842565b81516001600160401b038111610971576020916118a4878480809589010101611e81565b815201910190611813565b34610971576118c06102d936611c06565b80516118ce6102ed82611db5565b602082019190601f19013683375f5b8351811015611969576001600160401b036118f88286611dcc565b511161192657806001600160401b0361191360019387611dcc565b511661191f8285611dcc565b52016118dd565b604051639f9ddabb60e01b815260206004820152602760248201525f5160206121ca5f395f51905f5260448201526675696e7436342760c81b6064820152608490fd5b50604051918291602083019060208452518091526040830191905f5b818110611993575050500390f35b82516001600160401b0316845285945060209384019390920191600101611985565b346109715736600319016080811261097157604013610971576040516119da81611b9b565b60043560088110156109715781526024358015158103610971576020820152604036604319011261097157604051611a1181611b9b565b604435600881101561097157815260643591821515830361097157610950926020830152611df4565b3461097157611a4b61079f36611c06565b8051611a596102ed82611db5565b602082019190601f19013683375f5b8351811015611b0157607f611a7d8286611dcc565b51138015611aec575b611aab5780611a9760019286611dcc565b515f0b611aa48285611dcc565b5201611a68565b604051639f9ddabb60e01b815260206004820152602560248201525f5160206121ca5f395f51905f52604482015264696e74382760d81b6064820152608490fd5b50607f19611afa8286611dcc565b5112611a86565b50604051918291602083019060208452518091526040830191905f5b818110611b2b575050500390f35b82515f0b845285945060209384019390920191600101611b1d565b3461097157611b576102d936611c06565b6040518091602082016020835281518091526020604084019201905f5b818110611b82575050500390f35b8251845285945060209384019390920191600101611b74565b604081019081106001600160401b03821117611bb657604052565b634e487b7160e01b5f52604160045260245ffd5b90601f801991011681019081106001600160401b03821117611bb657604052565b6001600160401b038111611bb657601f01601f191660200190565b602060031982011261097157600435906001600160401b03821161097157606082820360031901126109715760405191611c3f83611b9b565b806004016040818403126109715760405190611c5a82611b9b565b80359060088210156109715760209183520135801515810361097157602082015283526044810135906001600160401b03821161097157018160238201121561097157600481013590611cac82611beb565b92611cba6040519485611bca565b8284526024828401011161097157815f926024602093018386013783010152602082015290565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b602090611d2a604051611d1781611b9b565b6004815260018482015261040c83611fcd565b01518051810190602081818401930312610971576020810151906001600160401b03821161097157019080603f83011215610971576020820151611d6d81611db5565b92611d7b6040519485611bca565b8184526020808086019360051b8301010192831161097157604001905b828210611da55750505090565b8151815260209182019101611d98565b6001600160401b038111611bb65760051b60200190565b8051821015611de05760209160051b010190565b634e487b7160e01b5f52603260045260245ffd5b908151600881101561095d57815190600882101561095d571480611e6c575b15611e1c575050565b90611e68611e35611e2f611e5694611fee565b92611fee565b60405193849363b02cf71d60e01b8552604060048601526044850190611ce1565b83810360031901602485015290611ce1565b0390fd5b50602082015115156020820151151514611e13565b81601f8201121561097157602081519101611e9b82611beb565b92611ea96040519485611bca565b8284528282011161097157815f926020928386015e8301015290565b5190811515820361097157565b602090611ef6604051611ee481611b9b565b600581525f8482015261040c83611fcd565b0151602081805181010312610971576020015190565b602090611ef6604051611f1e81611b9b565b600481525f8482015261040c83611fcd565b602090611f426040516103f981611b9b565b01518051810190602081818401930312610971576020810151906001600160401b03821161097157019080603f83011215610971576020820151611f8581611db5565b92611f936040519485611bca565b8184526020808086019360051b8301010192831161097157604001905b828210611fbd5750505090565b8151815260209182019101611fb0565b5151600881101561095d5715611fdf57565b6321c4e35760e21b5f5260045ffd5b8051600881101561095d5761200290612065565b90602081015115908115612052575b501561201a5790565b61204f6002602080936040519481869251918291018484015e8101615b5d60f01b838201520301601d19810184520182611bca565b90565b905051600881101561095d57155f612011565b600881101561095d57600181146121a65760028114612180576003811461215a5760048114612134576005811461210f57600681146120ea576007146120c7576040516120b3604082611bca565b60048152636e6f6e6560e01b602082015290565b6040516120d5604082611bca565b6005815264627974657360d81b602082015290565b506040516120f9604082611bca565b6006815265737472696e6760d01b602082015290565b5060405161211e604082611bca565b600681526534b73a191a9b60d11b602082015290565b50604051612143604082611bca565b60078152663ab4b73a191a9b60c91b602082015290565b50604051612169604082611bca565b6007815266313cba32b9999960c91b602082015290565b5060405161218f604082611bca565b60078152666164647265737360c81b602082015290565b506040516121b5604082611bca565b6004815263189bdbdb60e21b60208201529056fe76616c756520696e20617272617920646f6573206e6f742066697420696e2027a26469706673582212200c97d5d8488b07778f13860b856bd3685fc854121aa4b40bac8e96cacd7b8e5564736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, libVariable: Optional[Union[LibVariable, Address]] = None, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, libVariable: Optional[Union[LibVariable, Address]] = None, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> LibVariableHelper:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, libVariable: Optional[Union[LibVariable, Address]] = None, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, libVariable: Optional[Union[LibVariable, Address]] = None, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], libVariable: Optional[Union[LibVariable, Address]] = None, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[LibVariableHelper]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, libVariable: Optional[Union[LibVariable, Address]] = None, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, LibVariableHelper, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[LibVariableHelper]]:
        return cls._deploy(request_type, [], return_tx, LibVariableHelper, from_, value, gas_limit, {b'X\x0c\xbfWf\x1cc\xd0\xb7\x88\xabv\xfaX\xc1\x93\xa5': (libVariable, 'LibVariable')}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls, libVariable: Union[LibVariable, Address]) -> bytes:
        return cls._get_creation_code({b'X\x0c\xbfWf\x1cc\xd0\xb7\x88\xabv\xfaX\xc1\x93\xa5': (libVariable, 'LibVariable')})

    @overload
    def assertExists(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#285)

        Args:
            v: struct Variable
        """
        ...

    @overload
    def assertExists(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#285)

        Args:
            v: struct Variable
        """
        ...

    @overload
    def assertExists(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#285)

        Args:
            v: struct Variable
        """
        ...

    @overload
    def assertExists(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#285)

        Args:
            v: struct Variable
        """
        ...

    def assertExists(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#285)

        Args:
            v: struct Variable
        """
        return self._execute(self.chain, request_type, "ada9f824", [v], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def assertEq(self, t1: Type, t2: Type, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#289)

        Args:
            t1: struct Type
            t2: struct Type
        """
        ...

    @overload
    def assertEq(self, t1: Type, t2: Type, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#289)

        Args:
            t1: struct Type
            t2: struct Type
        """
        ...

    @overload
    def assertEq(self, t1: Type, t2: Type, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#289)

        Args:
            t1: struct Type
            t2: struct Type
        """
        ...

    @overload
    def assertEq(self, t1: Type, t2: Type, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#289)

        Args:
            t1: struct Type
            t2: struct Type
        """
        ...

    def assertEq(self, t1: Type, t2: Type, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#289)

        Args:
            t1: struct Type
            t2: struct Type
        """
        return self._execute(self.chain, request_type, "0e9318b6", [t1, t2], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toBool(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#294)

        Args:
            v: struct Variable
        Returns:
            bool
        """
        ...

    @overload
    def toBool(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#294)

        Args:
            v: struct Variable
        Returns:
            bool
        """
        ...

    @overload
    def toBool(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#294)

        Args:
            v: struct Variable
        Returns:
            bool
        """
        ...

    @overload
    def toBool(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#294)

        Args:
            v: struct Variable
        Returns:
            bool
        """
        ...

    def toBool(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#294)

        Args:
            v: struct Variable
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "1b8c25c7", [v], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toAddress(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#298)

        Args:
            v: struct Variable
        Returns:
            address
        """
        ...

    @overload
    def toAddress(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#298)

        Args:
            v: struct Variable
        Returns:
            address
        """
        ...

    @overload
    def toAddress(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#298)

        Args:
            v: struct Variable
        Returns:
            address
        """
        ...

    @overload
    def toAddress(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#298)

        Args:
            v: struct Variable
        Returns:
            address
        """
        ...

    def toAddress(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#298)

        Args:
            v: struct Variable
        Returns:
            address
        """
        return self._execute(self.chain, request_type, "33571846", [v], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toBytes32(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#302)

        Args:
            v: struct Variable
        Returns:
            bytes32
        """
        ...

    @overload
    def toBytes32(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#302)

        Args:
            v: struct Variable
        Returns:
            bytes32
        """
        ...

    @overload
    def toBytes32(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#302)

        Args:
            v: struct Variable
        Returns:
            bytes32
        """
        ...

    @overload
    def toBytes32(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#302)

        Args:
            v: struct Variable
        Returns:
            bytes32
        """
        ...

    def toBytes32(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#302)

        Args:
            v: struct Variable
        Returns:
            bytes32
        """
        return self._execute(self.chain, request_type, "a29eeb79", [v], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toUint256(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#306)

        Args:
            v: struct Variable
        Returns:
            uint256
        """
        ...

    @overload
    def toUint256(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#306)

        Args:
            v: struct Variable
        Returns:
            uint256
        """
        ...

    @overload
    def toUint256(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#306)

        Args:
            v: struct Variable
        Returns:
            uint256
        """
        ...

    @overload
    def toUint256(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#306)

        Args:
            v: struct Variable
        Returns:
            uint256
        """
        ...

    def toUint256(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#306)

        Args:
            v: struct Variable
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "718651b8", [v], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toInt256(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#310)

        Args:
            v: struct Variable
        Returns:
            int256
        """
        ...

    @overload
    def toInt256(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#310)

        Args:
            v: struct Variable
        Returns:
            int256
        """
        ...

    @overload
    def toInt256(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#310)

        Args:
            v: struct Variable
        Returns:
            int256
        """
        ...

    @overload
    def toInt256(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[int256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#310)

        Args:
            v: struct Variable
        Returns:
            int256
        """
        ...

    def toInt256(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[int256, TransactionAbc[int256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#310)

        Args:
            v: struct Variable
        Returns:
            int256
        """
        return self._execute(self.chain, request_type, "5d0dbfd4", [v], True if request_type == "tx" else False, int256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toString(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#314)

        Args:
            v: struct Variable
        Returns:
            string
        """
        ...

    @overload
    def toString(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#314)

        Args:
            v: struct Variable
        Returns:
            string
        """
        ...

    @overload
    def toString(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#314)

        Args:
            v: struct Variable
        Returns:
            string
        """
        ...

    @overload
    def toString(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#314)

        Args:
            v: struct Variable
        Returns:
            string
        """
        ...

    def toString(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#314)

        Args:
            v: struct Variable
        Returns:
            string
        """
        return self._execute(self.chain, request_type, "361b7eb6", [v], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toBytes(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#318)

        Args:
            v: struct Variable
        Returns:
            bytes
        """
        ...

    @overload
    def toBytes(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#318)

        Args:
            v: struct Variable
        Returns:
            bytes
        """
        ...

    @overload
    def toBytes(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#318)

        Args:
            v: struct Variable
        Returns:
            bytes
        """
        ...

    @overload
    def toBytes(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytearray]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#318)

        Args:
            v: struct Variable
        Returns:
            bytes
        """
        ...

    def toBytes(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, TransactionAbc[bytearray], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#318)

        Args:
            v: struct Variable
        Returns:
            bytes
        """
        return self._execute(self.chain, request_type, "e31d23e5", [v], True if request_type == "tx" else False, bytearray, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toBoolArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#323)

        Args:
            v: struct Variable
        Returns:
            bool[]
        """
        ...

    @overload
    def toBoolArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#323)

        Args:
            v: struct Variable
        Returns:
            bool[]
        """
        ...

    @overload
    def toBoolArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#323)

        Args:
            v: struct Variable
        Returns:
            bool[]
        """
        ...

    @overload
    def toBoolArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[bool]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#323)

        Args:
            v: struct Variable
        Returns:
            bool[]
        """
        ...

    def toBoolArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[bool], TransactionAbc[List[bool]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#323)

        Args:
            v: struct Variable
        Returns:
            bool[]
        """
        return self._execute(self.chain, request_type, "28924b56", [v], True if request_type == "tx" else False, List[bool], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toAddressArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#327)

        Args:
            v: struct Variable
        Returns:
            address[]
        """
        ...

    @overload
    def toAddressArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#327)

        Args:
            v: struct Variable
        Returns:
            address[]
        """
        ...

    @overload
    def toAddressArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#327)

        Args:
            v: struct Variable
        Returns:
            address[]
        """
        ...

    @overload
    def toAddressArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[Address]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#327)

        Args:
            v: struct Variable
        Returns:
            address[]
        """
        ...

    def toAddressArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[Address], TransactionAbc[List[Address]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#327)

        Args:
            v: struct Variable
        Returns:
            address[]
        """
        return self._execute(self.chain, request_type, "e80f9114", [v], True if request_type == "tx" else False, List[Address], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toBytes32Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#331)

        Args:
            v: struct Variable
        Returns:
            bytes32[]
        """
        ...

    @overload
    def toBytes32Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#331)

        Args:
            v: struct Variable
        Returns:
            bytes32[]
        """
        ...

    @overload
    def toBytes32Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#331)

        Args:
            v: struct Variable
        Returns:
            bytes32[]
        """
        ...

    @overload
    def toBytes32Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[bytes32]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#331)

        Args:
            v: struct Variable
        Returns:
            bytes32[]
        """
        ...

    def toBytes32Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[bytes32], TransactionAbc[List[bytes32]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#331)

        Args:
            v: struct Variable
        Returns:
            bytes32[]
        """
        return self._execute(self.chain, request_type, "a5e1f792", [v], True if request_type == "tx" else False, List[bytes32], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toUint256Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#335)

        Args:
            v: struct Variable
        Returns:
            uint256[]
        """
        ...

    @overload
    def toUint256Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#335)

        Args:
            v: struct Variable
        Returns:
            uint256[]
        """
        ...

    @overload
    def toUint256Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#335)

        Args:
            v: struct Variable
        Returns:
            uint256[]
        """
        ...

    @overload
    def toUint256Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[uint256]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#335)

        Args:
            v: struct Variable
        Returns:
            uint256[]
        """
        ...

    def toUint256Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[uint256], TransactionAbc[List[uint256]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#335)

        Args:
            v: struct Variable
        Returns:
            uint256[]
        """
        return self._execute(self.chain, request_type, "01a9fdf3", [v], True if request_type == "tx" else False, List[uint256], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toInt256Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[int256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#339)

        Args:
            v: struct Variable
        Returns:
            int256[]
        """
        ...

    @overload
    def toInt256Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#339)

        Args:
            v: struct Variable
        Returns:
            int256[]
        """
        ...

    @overload
    def toInt256Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#339)

        Args:
            v: struct Variable
        Returns:
            int256[]
        """
        ...

    @overload
    def toInt256Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[int256]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#339)

        Args:
            v: struct Variable
        Returns:
            int256[]
        """
        ...

    def toInt256Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[int256], TransactionAbc[List[int256]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#339)

        Args:
            v: struct Variable
        Returns:
            int256[]
        """
        return self._execute(self.chain, request_type, "ebd42628", [v], True if request_type == "tx" else False, List[int256], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toStringArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[str]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#343)

        Args:
            v: struct Variable
        Returns:
            string[]
        """
        ...

    @overload
    def toStringArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#343)

        Args:
            v: struct Variable
        Returns:
            string[]
        """
        ...

    @overload
    def toStringArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#343)

        Args:
            v: struct Variable
        Returns:
            string[]
        """
        ...

    @overload
    def toStringArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[str]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#343)

        Args:
            v: struct Variable
        Returns:
            string[]
        """
        ...

    def toStringArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[str], TransactionAbc[List[str]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#343)

        Args:
            v: struct Variable
        Returns:
            string[]
        """
        return self._execute(self.chain, request_type, "198c44fc", [v], True if request_type == "tx" else False, List[str], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toBytesArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[bytearray]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#347)

        Args:
            v: struct Variable
        Returns:
            bytes[]
        """
        ...

    @overload
    def toBytesArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#347)

        Args:
            v: struct Variable
        Returns:
            bytes[]
        """
        ...

    @overload
    def toBytesArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#347)

        Args:
            v: struct Variable
        Returns:
            bytes[]
        """
        ...

    @overload
    def toBytesArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[bytearray]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#347)

        Args:
            v: struct Variable
        Returns:
            bytes[]
        """
        ...

    def toBytesArray(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[bytearray], TransactionAbc[List[bytearray]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#347)

        Args:
            v: struct Variable
        Returns:
            bytes[]
        """
        return self._execute(self.chain, request_type, "a9cc756b", [v], True if request_type == "tx" else False, List[bytearray], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toUint128(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint128:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#352)

        Args:
            v: struct Variable
        Returns:
            uint128
        """
        ...

    @overload
    def toUint128(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#352)

        Args:
            v: struct Variable
        Returns:
            uint128
        """
        ...

    @overload
    def toUint128(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#352)

        Args:
            v: struct Variable
        Returns:
            uint128
        """
        ...

    @overload
    def toUint128(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint128]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#352)

        Args:
            v: struct Variable
        Returns:
            uint128
        """
        ...

    def toUint128(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint128, TransactionAbc[uint128], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#352)

        Args:
            v: struct Variable
        Returns:
            uint128
        """
        return self._execute(self.chain, request_type, "713c108f", [v], True if request_type == "tx" else False, uint128, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toUint64(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint64:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#356)

        Args:
            v: struct Variable
        Returns:
            uint64
        """
        ...

    @overload
    def toUint64(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#356)

        Args:
            v: struct Variable
        Returns:
            uint64
        """
        ...

    @overload
    def toUint64(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#356)

        Args:
            v: struct Variable
        Returns:
            uint64
        """
        ...

    @overload
    def toUint64(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint64]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#356)

        Args:
            v: struct Variable
        Returns:
            uint64
        """
        ...

    def toUint64(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint64, TransactionAbc[uint64], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#356)

        Args:
            v: struct Variable
        Returns:
            uint64
        """
        return self._execute(self.chain, request_type, "476e1e48", [v], True if request_type == "tx" else False, uint64, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toUint32(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#360)

        Args:
            v: struct Variable
        Returns:
            uint32
        """
        ...

    @overload
    def toUint32(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#360)

        Args:
            v: struct Variable
        Returns:
            uint32
        """
        ...

    @overload
    def toUint32(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#360)

        Args:
            v: struct Variable
        Returns:
            uint32
        """
        ...

    @overload
    def toUint32(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#360)

        Args:
            v: struct Variable
        Returns:
            uint32
        """
        ...

    def toUint32(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint32, TransactionAbc[uint32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#360)

        Args:
            v: struct Variable
        Returns:
            uint32
        """
        return self._execute(self.chain, request_type, "8ec7637b", [v], True if request_type == "tx" else False, uint32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toUint16(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint16:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#364)

        Args:
            v: struct Variable
        Returns:
            uint16
        """
        ...

    @overload
    def toUint16(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#364)

        Args:
            v: struct Variable
        Returns:
            uint16
        """
        ...

    @overload
    def toUint16(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#364)

        Args:
            v: struct Variable
        Returns:
            uint16
        """
        ...

    @overload
    def toUint16(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint16]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#364)

        Args:
            v: struct Variable
        Returns:
            uint16
        """
        ...

    def toUint16(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint16, TransactionAbc[uint16], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#364)

        Args:
            v: struct Variable
        Returns:
            uint16
        """
        return self._execute(self.chain, request_type, "296a2f41", [v], True if request_type == "tx" else False, uint16, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toUint8(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint8:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#368)

        Args:
            v: struct Variable
        Returns:
            uint8
        """
        ...

    @overload
    def toUint8(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#368)

        Args:
            v: struct Variable
        Returns:
            uint8
        """
        ...

    @overload
    def toUint8(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#368)

        Args:
            v: struct Variable
        Returns:
            uint8
        """
        ...

    @overload
    def toUint8(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint8]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#368)

        Args:
            v: struct Variable
        Returns:
            uint8
        """
        ...

    def toUint8(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint8, TransactionAbc[uint8], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#368)

        Args:
            v: struct Variable
        Returns:
            uint8
        """
        return self._execute(self.chain, request_type, "79948884", [v], True if request_type == "tx" else False, uint8, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toInt128(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int128:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#373)

        Args:
            v: struct Variable
        Returns:
            int128
        """
        ...

    @overload
    def toInt128(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#373)

        Args:
            v: struct Variable
        Returns:
            int128
        """
        ...

    @overload
    def toInt128(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#373)

        Args:
            v: struct Variable
        Returns:
            int128
        """
        ...

    @overload
    def toInt128(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[int128]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#373)

        Args:
            v: struct Variable
        Returns:
            int128
        """
        ...

    def toInt128(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[int128, TransactionAbc[int128], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#373)

        Args:
            v: struct Variable
        Returns:
            int128
        """
        return self._execute(self.chain, request_type, "f7b41074", [v], True if request_type == "tx" else False, int128, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toInt64(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int64:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#377)

        Args:
            v: struct Variable
        Returns:
            int64
        """
        ...

    @overload
    def toInt64(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#377)

        Args:
            v: struct Variable
        Returns:
            int64
        """
        ...

    @overload
    def toInt64(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#377)

        Args:
            v: struct Variable
        Returns:
            int64
        """
        ...

    @overload
    def toInt64(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[int64]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#377)

        Args:
            v: struct Variable
        Returns:
            int64
        """
        ...

    def toInt64(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[int64, TransactionAbc[int64], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#377)

        Args:
            v: struct Variable
        Returns:
            int64
        """
        return self._execute(self.chain, request_type, "fb50451a", [v], True if request_type == "tx" else False, int64, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toInt32(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#381)

        Args:
            v: struct Variable
        Returns:
            int32
        """
        ...

    @overload
    def toInt32(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#381)

        Args:
            v: struct Variable
        Returns:
            int32
        """
        ...

    @overload
    def toInt32(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#381)

        Args:
            v: struct Variable
        Returns:
            int32
        """
        ...

    @overload
    def toInt32(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[int32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#381)

        Args:
            v: struct Variable
        Returns:
            int32
        """
        ...

    def toInt32(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[int32, TransactionAbc[int32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#381)

        Args:
            v: struct Variable
        Returns:
            int32
        """
        return self._execute(self.chain, request_type, "56cd3b68", [v], True if request_type == "tx" else False, int32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toInt16(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int16:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#385)

        Args:
            v: struct Variable
        Returns:
            int16
        """
        ...

    @overload
    def toInt16(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#385)

        Args:
            v: struct Variable
        Returns:
            int16
        """
        ...

    @overload
    def toInt16(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#385)

        Args:
            v: struct Variable
        Returns:
            int16
        """
        ...

    @overload
    def toInt16(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[int16]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#385)

        Args:
            v: struct Variable
        Returns:
            int16
        """
        ...

    def toInt16(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[int16, TransactionAbc[int16], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#385)

        Args:
            v: struct Variable
        Returns:
            int16
        """
        return self._execute(self.chain, request_type, "2f509313", [v], True if request_type == "tx" else False, int16, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toInt8(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int8:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#389)

        Args:
            v: struct Variable
        Returns:
            int8
        """
        ...

    @overload
    def toInt8(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#389)

        Args:
            v: struct Variable
        Returns:
            int8
        """
        ...

    @overload
    def toInt8(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#389)

        Args:
            v: struct Variable
        Returns:
            int8
        """
        ...

    @overload
    def toInt8(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[int8]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#389)

        Args:
            v: struct Variable
        Returns:
            int8
        """
        ...

    def toInt8(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[int8, TransactionAbc[int8], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#389)

        Args:
            v: struct Variable
        Returns:
            int8
        """
        return self._execute(self.chain, request_type, "3fb5872b", [v], True if request_type == "tx" else False, int8, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toUint128Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[uint128]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#394)

        Args:
            v: struct Variable
        Returns:
            uint128[]
        """
        ...

    @overload
    def toUint128Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#394)

        Args:
            v: struct Variable
        Returns:
            uint128[]
        """
        ...

    @overload
    def toUint128Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#394)

        Args:
            v: struct Variable
        Returns:
            uint128[]
        """
        ...

    @overload
    def toUint128Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[uint128]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#394)

        Args:
            v: struct Variable
        Returns:
            uint128[]
        """
        ...

    def toUint128Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[uint128], TransactionAbc[List[uint128]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#394)

        Args:
            v: struct Variable
        Returns:
            uint128[]
        """
        return self._execute(self.chain, request_type, "26927920", [v], True if request_type == "tx" else False, List[uint128], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toUint64Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[uint64]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#398)

        Args:
            v: struct Variable
        Returns:
            uint64[]
        """
        ...

    @overload
    def toUint64Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#398)

        Args:
            v: struct Variable
        Returns:
            uint64[]
        """
        ...

    @overload
    def toUint64Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#398)

        Args:
            v: struct Variable
        Returns:
            uint64[]
        """
        ...

    @overload
    def toUint64Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[uint64]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#398)

        Args:
            v: struct Variable
        Returns:
            uint64[]
        """
        ...

    def toUint64Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[uint64], TransactionAbc[List[uint64]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#398)

        Args:
            v: struct Variable
        Returns:
            uint64[]
        """
        return self._execute(self.chain, request_type, "18b6d849", [v], True if request_type == "tx" else False, List[uint64], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toUint32Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[uint32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#402)

        Args:
            v: struct Variable
        Returns:
            uint32[]
        """
        ...

    @overload
    def toUint32Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#402)

        Args:
            v: struct Variable
        Returns:
            uint32[]
        """
        ...

    @overload
    def toUint32Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#402)

        Args:
            v: struct Variable
        Returns:
            uint32[]
        """
        ...

    @overload
    def toUint32Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[uint32]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#402)

        Args:
            v: struct Variable
        Returns:
            uint32[]
        """
        ...

    def toUint32Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[uint32], TransactionAbc[List[uint32]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#402)

        Args:
            v: struct Variable
        Returns:
            uint32[]
        """
        return self._execute(self.chain, request_type, "825b7bfd", [v], True if request_type == "tx" else False, List[uint32], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toUint16Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[uint16]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#406)

        Args:
            v: struct Variable
        Returns:
            uint16[]
        """
        ...

    @overload
    def toUint16Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#406)

        Args:
            v: struct Variable
        Returns:
            uint16[]
        """
        ...

    @overload
    def toUint16Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#406)

        Args:
            v: struct Variable
        Returns:
            uint16[]
        """
        ...

    @overload
    def toUint16Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[uint16]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#406)

        Args:
            v: struct Variable
        Returns:
            uint16[]
        """
        ...

    def toUint16Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[uint16], TransactionAbc[List[uint16]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#406)

        Args:
            v: struct Variable
        Returns:
            uint16[]
        """
        return self._execute(self.chain, request_type, "e374b6ac", [v], True if request_type == "tx" else False, List[uint16], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toUint8Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[uint8]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#410)

        Args:
            v: struct Variable
        Returns:
            uint8[]
        """
        ...

    @overload
    def toUint8Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#410)

        Args:
            v: struct Variable
        Returns:
            uint8[]
        """
        ...

    @overload
    def toUint8Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#410)

        Args:
            v: struct Variable
        Returns:
            uint8[]
        """
        ...

    @overload
    def toUint8Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[uint8]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#410)

        Args:
            v: struct Variable
        Returns:
            uint8[]
        """
        ...

    def toUint8Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[uint8], TransactionAbc[List[uint8]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#410)

        Args:
            v: struct Variable
        Returns:
            uint8[]
        """
        return self._execute(self.chain, request_type, "f3283fb7", [v], True if request_type == "tx" else False, List[uint8], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toInt128Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[int128]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#415)

        Args:
            v: struct Variable
        Returns:
            int128[]
        """
        ...

    @overload
    def toInt128Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#415)

        Args:
            v: struct Variable
        Returns:
            int128[]
        """
        ...

    @overload
    def toInt128Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#415)

        Args:
            v: struct Variable
        Returns:
            int128[]
        """
        ...

    @overload
    def toInt128Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[int128]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#415)

        Args:
            v: struct Variable
        Returns:
            int128[]
        """
        ...

    def toInt128Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[int128], TransactionAbc[List[int128]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#415)

        Args:
            v: struct Variable
        Returns:
            int128[]
        """
        return self._execute(self.chain, request_type, "73dea9ff", [v], True if request_type == "tx" else False, List[int128], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toInt64Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[int64]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#419)

        Args:
            v: struct Variable
        Returns:
            int64[]
        """
        ...

    @overload
    def toInt64Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#419)

        Args:
            v: struct Variable
        Returns:
            int64[]
        """
        ...

    @overload
    def toInt64Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#419)

        Args:
            v: struct Variable
        Returns:
            int64[]
        """
        ...

    @overload
    def toInt64Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[int64]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#419)

        Args:
            v: struct Variable
        Returns:
            int64[]
        """
        ...

    def toInt64Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[int64], TransactionAbc[List[int64]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#419)

        Args:
            v: struct Variable
        Returns:
            int64[]
        """
        return self._execute(self.chain, request_type, "cd8ceaad", [v], True if request_type == "tx" else False, List[int64], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toInt32Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[int32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#423)

        Args:
            v: struct Variable
        Returns:
            int32[]
        """
        ...

    @overload
    def toInt32Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#423)

        Args:
            v: struct Variable
        Returns:
            int32[]
        """
        ...

    @overload
    def toInt32Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#423)

        Args:
            v: struct Variable
        Returns:
            int32[]
        """
        ...

    @overload
    def toInt32Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[int32]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#423)

        Args:
            v: struct Variable
        Returns:
            int32[]
        """
        ...

    def toInt32Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[int32], TransactionAbc[List[int32]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#423)

        Args:
            v: struct Variable
        Returns:
            int32[]
        """
        return self._execute(self.chain, request_type, "938b79b1", [v], True if request_type == "tx" else False, List[int32], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toInt16Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[int16]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#427)

        Args:
            v: struct Variable
        Returns:
            int16[]
        """
        ...

    @overload
    def toInt16Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#427)

        Args:
            v: struct Variable
        Returns:
            int16[]
        """
        ...

    @overload
    def toInt16Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#427)

        Args:
            v: struct Variable
        Returns:
            int16[]
        """
        ...

    @overload
    def toInt16Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[int16]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#427)

        Args:
            v: struct Variable
        Returns:
            int16[]
        """
        ...

    def toInt16Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[int16], TransactionAbc[List[int16]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#427)

        Args:
            v: struct Variable
        Returns:
            int16[]
        """
        return self._execute(self.chain, request_type, "a59ecfd6", [v], True if request_type == "tx" else False, List[int16], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def toInt8Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[int8]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#431)

        Args:
            v: struct Variable
        Returns:
            int8[]
        """
        ...

    @overload
    def toInt8Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#431)

        Args:
            v: struct Variable
        Returns:
            int8[]
        """
        ...

    @overload
    def toInt8Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#431)

        Args:
            v: struct Variable
        Returns:
            int8[]
        """
        ...

    @overload
    def toInt8Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[int8]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#431)

        Args:
            v: struct Variable
        Returns:
            int8[]
        """
        ...

    def toInt8Array(self, v: Variable, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[int8], TransactionAbc[List[int8]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/LibVariable.t.sol#431)

        Args:
            v: struct Variable
        Returns:
            int8[]
        """
        return self._execute(self.chain, request_type, "04f33e37", [v], True if request_type == "tx" else False, List[int8], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

LibVariableHelper.assertExists.selector = bytes4(b'\xad\xa9\xf8$')
LibVariableHelper.assertEq.selector = bytes4(b'\x0e\x93\x18\xb6')
LibVariableHelper.toBool.selector = bytes4(b'\x1b\x8c%\xc7')
LibVariableHelper.toAddress.selector = bytes4(b'3W\x18F')
LibVariableHelper.toBytes32.selector = bytes4(b'\xa2\x9e\xeby')
LibVariableHelper.toUint256.selector = bytes4(b'q\x86Q\xb8')
LibVariableHelper.toInt256.selector = bytes4(b']\r\xbf\xd4')
LibVariableHelper.toString.selector = bytes4(b'6\x1b~\xb6')
LibVariableHelper.toBytes.selector = bytes4(b'\xe3\x1d#\xe5')
LibVariableHelper.toBoolArray.selector = bytes4(b'(\x92KV')
LibVariableHelper.toAddressArray.selector = bytes4(b'\xe8\x0f\x91\x14')
LibVariableHelper.toBytes32Array.selector = bytes4(b'\xa5\xe1\xf7\x92')
LibVariableHelper.toUint256Array.selector = bytes4(b'\x01\xa9\xfd\xf3')
LibVariableHelper.toInt256Array.selector = bytes4(b'\xeb\xd4&(')
LibVariableHelper.toStringArray.selector = bytes4(b'\x19\x8cD\xfc')
LibVariableHelper.toBytesArray.selector = bytes4(b'\xa9\xccuk')
LibVariableHelper.toUint128.selector = bytes4(b'q<\x10\x8f')
LibVariableHelper.toUint64.selector = bytes4(b'Gn\x1eH')
LibVariableHelper.toUint32.selector = bytes4(b'\x8e\xc7c{')
LibVariableHelper.toUint16.selector = bytes4(b')j/A')
LibVariableHelper.toUint8.selector = bytes4(b'y\x94\x88\x84')
LibVariableHelper.toInt128.selector = bytes4(b'\xf7\xb4\x10t')
LibVariableHelper.toInt64.selector = bytes4(b'\xfbPE\x1a')
LibVariableHelper.toInt32.selector = bytes4(b'V\xcd;h')
LibVariableHelper.toInt16.selector = bytes4(b'/P\x93\x13')
LibVariableHelper.toInt8.selector = bytes4(b'?\xb5\x87+')
LibVariableHelper.toUint128Array.selector = bytes4(b'&\x92y ')
LibVariableHelper.toUint64Array.selector = bytes4(b'\x18\xb6\xd8I')
LibVariableHelper.toUint32Array.selector = bytes4(b'\x82[{\xfd')
LibVariableHelper.toUint16Array.selector = bytes4(b'\xe3t\xb6\xac')
LibVariableHelper.toUint8Array.selector = bytes4(b'\xf3(?\xb7')
LibVariableHelper.toInt128Array.selector = bytes4(b's\xde\xa9\xff')
LibVariableHelper.toInt64Array.selector = bytes4(b'\xcd\x8c\xea\xad')
LibVariableHelper.toInt32Array.selector = bytes4(b'\x93\x8by\xb1')
LibVariableHelper.toInt16Array.selector = bytes4(b'\xa5\x9e\xcf\xd6')
LibVariableHelper.toInt8Array.selector = bytes4(b'\x04\xf3>7')
