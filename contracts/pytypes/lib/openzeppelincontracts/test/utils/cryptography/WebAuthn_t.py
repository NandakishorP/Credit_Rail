
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.forgestd.src.Test import Test
from pytypes.lib.openzeppelincontracts.contracts.utils.cryptography.WebAuthn import WebAuthn



class WebAuthnTest(Test):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#11)
    """
    _abi = {b'A0O\xac\xd92=u\xb1\x1b\xcd\xd6\t\xcb8\xef\xff\xfd\xb0W\x10\xf7\xca\xf0\xe9\xb1lm\x9dp\x9fP': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log', 'type': 'event'}, b'z\xe7LRt\x14\xae\x13_\xd9pG\xb1)!\xa5\xec9\x11\xb8\x04\x19xU\xd6~%\xc7\xb7^\xe6\xf3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'log_address', 'type': 'event'}, b'\xfb\x10(e\xd5\n\xdd\xdd\xf6\x9d\xa9\xb5\xaa\x1b\xce\xd6l\x80\xcf\x86\x9a\\\x8d\x04q\xa4g\xe1\x8c\xe9\xca\xb1': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_array', 'type': 'event'}, b'\x89\n\x82g\x9bG\x0f+\xd8(\x16\xed\x9b\x16\x1f\x97\xd8\xb9g\xf3\x7f\xa3d|!\xd5\xbf9t\x9e-\xd5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_array', 'type': 'event'}, b'@\xe1\x84\x0fWi\x07=a\xbd\x017-\x9bu\xba\xa9\x84-V)\xa0\xc9\x9f\xf1\x03\xbe\x11x\xa8\xe9\xe2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_array', 'type': 'event'}, b'#\xb6*\xd0XM$\xa7_\x0b\xf3V\x03\x91\xefVY\xecm\xb1&\x9cV\xe1\x1a\xa2A\xd67\xf1\x9b ': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'log_bytes', 'type': 'event'}, b'\xe8\x16\x99\xb8Q\x13\xee\xa1\xc7>\x10X\x8b+\x03^U\x893ic!s\xaf\xd4?\xeb\x19/\xacd\xe3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'log_bytes32', 'type': 'event'}, b'\x0e\xb5\xd5&$\xc8\xd2\x8a\xda\x9f\xc5Z\x8cP.\xd5\xaa?\xbe/\xb6\xe9\x1bq\xb5\xf3v\x88+\x1d/\xb8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256', 'name': '', 'type': 'int256'}], 'name': 'log_int', 'type': 'event'}, b'\x9cN\x85A\xca\x8f\r\xc1\xc4\x13\xf9\x10\x8ff\xd8-<\xec\xb1\xbd\xdb\xceCza\xca\xa3\x17\\L\xc9o': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address', 'name': 'val', 'type': 'address'}], 'name': 'log_named_address', 'type': 'event'}, b'\x00\xaa\xa3\x9c\x9f\xfb_VzE48\x0cspup.\x1f\x7f\x14\x10\x7f\xc9S(\xe3\xb5l\x03%\xfb': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xa7>\xda\tf/F\xdd\xe7)\xbeF\x118_\xf3O\xe6\xc4O\xbb\xc6\xf7\xe1{\x04+Y\xa3D[W': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_named_array', 'type': 'event'}, b";\xcf\xb2\xae.\x8d\x13-\xd1\xfc\xe7\xcf'\x8a\x9a\x19uj\x9f\xce\xab\xe4p\xdf;\xda\xbbK\xc5w\xd1\xbd": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xd2n\x16\xca\xd4T\x87\x05\xe4\xc9\xe2\xd9O\x98\xee\x91\xc2\x89\x08^\xe4%YO\xd5c_\xa2\x96L\xcf\x18': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'val', 'type': 'bytes'}], 'name': 'log_named_bytes', 'type': 'event'}, b'\xaf\xb7\x95\xc9\xc6\x1eO\xe7F\x8c8o\x92]zT)\xec\xad\x9c\x04\x95\xdd\xb8\xd3\x8di\x06\x14\xd3/\x99': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'val', 'type': 'bytes32'}], 'name': 'log_named_bytes32', 'type': 'event'}, b']\xa6\xce\x9dQ\x15\x1b\xa1\x0c\t\xa5Y\xef$\xd5 \xb9\xda\xc5\xc5\xb8\x81\n\xe8CNM\r\x86A\x1a\x95': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_int', 'type': 'event'}, b"\xeb\x8b\xa4<\xedu7B\x19F\xbdC\xe8(\xb8\xb2\xb8B\x89'\xaa\x8f\x80\x1c\x13\xd94\xbf\x11\xac\xa5{": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_uint', 'type': 'event'}, b'/\xe62w\x91t7CxD*\x8e\x97\x8b\xcc\xfb\xdc\xc1\xd6\xb2\xb0\xd8\x1f~\x8e\xb7v\xab"\x86\xf1h': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}], 'name': 'log_named_int', 'type': 'event'}, b'(\x0fDF\xb2\x8a\x13rA}\xdae\x8d0\xb9[)\x92\xb1*\xc9\xc7\xf3xS_)\xa9z\xcf5\x83': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'val', 'type': 'string'}], 'name': 'log_named_string', 'type': 'event'}, b'\xb2\xde/\xbe\x80\x1a\r\xf6\xc0\xcb\xdd\xfdD\x8b\xa3\xc4\x1dH\xa0@\xca5\xc5l\x81\x96\xef\x0f\xca\xe7!\xa8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}], 'name': 'log_named_uint', 'type': 'event'}, b'\x0b.\x13\xff \xac{GA\x98eU\x83\xed\xf7\r\xed\xd2\xc1\xdc\x98\x0e2\x9cO\xbb/\xc0t\x8byk': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log_string', 'type': 'event'}, b',\xab\x97\x90Q\x0f\xd8\xbd\xfb\xd2\x11R\x88\xdb3\xfe\xc6f\x91\xd4v\xef\xc5B|\xfdL\ti0\x17U': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'log_uint', 'type': 'event'}, b"\xe7\x95\x0e\xde\x03\x94\xb9\xf2\xceJZ\x1b\xf5\xa7\xe1\x85$\x11\xf7\xe6f\x1bC\x08\xc9\x13\xc4\xbf\xd1\x10'\xe4": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'logs', 'type': 'event'}, b'\xfav&\xd4': {'inputs': [], 'name': 'IS_TEST', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb5P\x8a\xa9': {'inputs': [], 'name': 'excludeArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'excludedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe2\x0c\x9fq': {'inputs': [], 'name': 'excludeContracts', 'outputs': [{'internalType': 'address[]', 'name': 'excludedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb0FO\xdc': {'inputs': [], 'name': 'excludeSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'excludedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1e\xd7\x83\x1c': {'inputs': [], 'name': 'excludeSenders', 'outputs': [{'internalType': 'address[]', 'name': 'excludedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbaAO\xa6': {'inputs': [], 'name': 'failed', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'f\xd9\xa9\xa0': {'inputs': [], 'name': 'targetArtifactSelectors', 'outputs': [{'components': [{'internalType': 'string', 'name': 'artifact', 'type': 'string'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzArtifactSelector[]', 'name': 'targetedArtifactSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x85"l\x81': {'inputs': [], 'name': 'targetArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'targetedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'?r\x86\xf4': {'inputs': [], 'name': 'targetContracts', 'outputs': [{'internalType': 'address[]', 'name': 'targetedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'*\xde8\x80': {'inputs': [], 'name': 'targetInterfaces', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'string[]', 'name': 'artifacts', 'type': 'string[]'}], 'internalType': 'struct StdInvariant.FuzzInterface[]', 'name': 'targetedInterfaces_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x91j\x17\xc6': {'inputs': [], 'name': 'targetSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'targetedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'>^<#': {'inputs': [], 'name': 'targetSenders', 'outputs': [{'internalType': 'address[]', 'name': 'targetedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b' $m~': {'inputs': [], 'name': 'testTryDecodeAuthInvalid', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\x7f:\xa4\x92': {'inputs': [{'internalType': 'bytes32', 'name': 'r', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 's', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'challengeIndex', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'typeIndex', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'authenticatorData', 'type': 'bytes'}, {'internalType': 'string', 'name': 'clientDataJSON', 'type': 'string'}], 'name': 'testTryDecodeAuthValid', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\xe6\xaa\xd3|': {'inputs': [{'internalType': 'bytes', 'name': 'challenge', 'type': 'bytes'}, {'internalType': 'uint256', 'name': 'seed', 'type': 'uint256'}], 'name': 'testVerify', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\x18\x05\x80\xc7': {'inputs': [{'internalType': 'bytes', 'name': 'challenge', 'type': 'bytes'}, {'internalType': 'uint256', 'name': 'seed', 'type': 'uint256'}], 'name': 'testVerifyFlagsBEBS', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\xd4\x8a\xac\xc7': {'inputs': [{'internalType': 'bytes', 'name': 'challenge', 'type': 'bytes'}, {'internalType': 'uint256', 'name': 'seed', 'type': 'uint256'}], 'name': 'testVerifyFlagsUP', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'=!q\x8b': {'inputs': [{'internalType': 'bytes', 'name': 'challenge', 'type': 'bytes'}, {'internalType': 'uint256', 'name': 'seed', 'type': 'uint256'}], 'name': 'testVerifyFlagsUV', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\x14\x9fe\xca': {'inputs': [{'internalType': 'bytes', 'name': 'challenge', 'type': 'bytes'}, {'internalType': 'uint256', 'name': 'seed', 'type': 'uint256'}], 'name': 'testVerifyInvalidChallenge', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'=\xe3\x15$': {'inputs': [{'internalType': 'bytes', 'name': 'challenge', 'type': 'bytes'}, {'internalType': 'uint256', 'name': 'seed', 'type': 'uint256'}], 'name': 'testVerifyInvalidType', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'A\xda\xe3\x0c': {'inputs': [{'internalType': 'bytes', 'name': 'encoded', 'type': 'bytes'}], 'name': 'tryDecodeAuth', 'outputs': [{'internalType': 'bool', 'name': 'success', 'type': 'bool'}, {'components': [{'internalType': 'bytes32', 'name': 'r', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 's', 'type': 'bytes32'}, {'internalType': 'uint256', 'name': 'challengeIndex', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'typeIndex', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'authenticatorData', 'type': 'bytes'}, {'internalType': 'string', 'name': 'clientDataJSON', 'type': 'string'}], 'internalType': 'struct WebAuthn.WebAuthnAuth', 'name': 'auth', 'type': 'tuple'}], 'stateMutability': 'pure', 'type': 'function'}, b'\x14-\x1a\x11': {'inputs': [{'internalType': 'bytes', 'name': 'encoded', 'type': 'bytes'}], 'name': 'tryDecodeAuthDrop', 'outputs': [{'internalType': 'bool', 'name': 'success', 'type': 'bool'}], 'stateMutability': 'pure', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":46,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"stdstore","offset":0,"slot":0,"type":"t_struct(StdStorage)8331_storage"},{"astId":209,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"_failed","offset":0,"slot":8,"type":"t_bool"},{"astId":2943,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"stdChainsInitialized","offset":1,"slot":8,"type":"t_bool"},{"astId":2964,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"chains","offset":0,"slot":9,"type":"t_mapping(t_string_memory_ptr,t_struct(Chain)2959_storage)"},{"astId":2968,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"defaultRpcUrls","offset":0,"slot":10,"type":"t_mapping(t_string_memory_ptr,t_string_storage)"},{"astId":2972,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"idToAlias","offset":0,"slot":11,"type":"t_mapping(t_uint256,t_string_storage)"},{"astId":2975,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"fallbackToDefaultRpcUrls","offset":0,"slot":12,"type":"t_bool"},{"astId":3931,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"gasMeteringOff","offset":1,"slot":12,"type":"t_bool"},{"astId":6002,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"stdstore","offset":0,"slot":13,"type":"t_struct(StdStorage)8331_storage"},{"astId":6923,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"_excludedContracts","offset":0,"slot":21,"type":"t_array(t_address)dyn_storage"},{"astId":6926,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"_excludedSenders","offset":0,"slot":22,"type":"t_array(t_address)dyn_storage"},{"astId":6929,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"_targetedContracts","offset":0,"slot":23,"type":"t_array(t_address)dyn_storage"},{"astId":6932,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"_targetedSenders","offset":0,"slot":24,"type":"t_array(t_address)dyn_storage"},{"astId":6935,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"_excludedArtifacts","offset":0,"slot":25,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6938,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"_targetedArtifacts","offset":0,"slot":26,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6942,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"_targetedArtifactSelectors","offset":0,"slot":27,"type":"t_array(t_struct(FuzzArtifactSelector)6914_storage)dyn_storage"},{"astId":6946,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"_excludedSelectors","offset":0,"slot":28,"type":"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage"},{"astId":6950,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"_targetedSelectors","offset":0,"slot":29,"type":"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage"},{"astId":6954,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"_targetedInterfaces","offset":0,"slot":30,"type":"t_array(t_struct(FuzzInterface)6920_storage)dyn_storage"},{"astId":13223,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"IS_TEST","offset":0,"slot":31,"type":"t_bool"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_address)dyn_storage":{"encoding":"dynamic_array","label":"address[]","numberOfBytes":32,"base":"t_address"},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_array(t_bytes4)dyn_storage":{"encoding":"dynamic_array","label":"bytes4[]","numberOfBytes":32,"base":"t_bytes4"},"t_array(t_string_storage)dyn_storage":{"encoding":"dynamic_array","label":"string[]","numberOfBytes":32,"base":"t_string_storage"},"t_array(t_struct(FuzzArtifactSelector)6914_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzArtifactSelector[]","numberOfBytes":32,"base":"t_struct(FuzzArtifactSelector)6914_storage"},"t_array(t_struct(FuzzInterface)6920_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzInterface[]","numberOfBytes":32,"base":"t_struct(FuzzInterface)6920_storage"},"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzSelector[]","numberOfBytes":32,"base":"t_struct(FuzzSelector)6908_storage"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))"},"t_mapping(t_bytes32,t_struct(FindData)8306_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)8306_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)8306_storage)"},"t_mapping(t_string_memory_ptr,t_string_storage)":{"encoding":"mapping","label":"mapping(string => string)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_string_storage"},"t_mapping(t_string_memory_ptr,t_struct(Chain)2959_storage)":{"encoding":"mapping","label":"mapping(string => struct StdChains.Chain)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_struct(Chain)2959_storage"},"t_mapping(t_uint256,t_string_storage)":{"encoding":"mapping","label":"mapping(uint256 => string)","numberOfBytes":32,"key":"t_uint256","value":"t_string_storage"},"t_string_memory_ptr":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(Chain)2959_storage":{"encoding":"inplace","label":"struct StdChains.Chain","numberOfBytes":128,"members":[{"astId":2952,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"name","offset":0,"slot":0,"type":"t_string_storage"},{"astId":2954,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"chainId","offset":0,"slot":1,"type":"t_uint256"},{"astId":2956,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"chainAlias","offset":0,"slot":2,"type":"t_string_storage"},{"astId":2958,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"rpcUrl","offset":0,"slot":3,"type":"t_string_storage"}]},"t_struct(FindData)8306_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":8299,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":8301,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":8303,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":8305,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(FuzzArtifactSelector)6914_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzArtifactSelector","numberOfBytes":64,"members":[{"astId":6910,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"artifact","offset":0,"slot":0,"type":"t_string_storage"},{"astId":6913,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(FuzzInterface)6920_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzInterface","numberOfBytes":64,"members":[{"astId":6916,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6919,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"artifacts","offset":0,"slot":1,"type":"t_array(t_string_storage)dyn_storage"}]},"t_struct(FuzzSelector)6908_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzSelector","numberOfBytes":64,"members":[{"astId":6904,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6907,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(StdStorage)8331_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":8315,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))"},{"astId":8318,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":8320,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":8322,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":8324,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":8326,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":8328,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":8330,"contract":"lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol:WebAuthnTest","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60808060405234602f57600160ff19600c541617600c55600160ff19601f541617601f5561351490816100348239f35b5f80fdfe60806040526004361015610011575f80fd5b5f5f3560e01c8063142d1a11146114b9578063149f65ca14611464578063180580c7146113ca5780631ed7831c1461134d57806320246d7e14610d725780632ade388014610c065780633d21718b14610b925780633de3152414610afa5780633e5e3c2314610a7d5780633f7286f414610a0057806341dae30c1461096e57806366d9a9a01461084a5780637f3aa492146104e657806385226c8114610454578063916a17c6146103ac578063b0464fdc14610304578063b5508aa914610272578063ba414fa61461024d578063d48aacc7146101fd578063e20c9f711461016f578063e6aad37c146101315763fa7626d41461010c575f80fd5b3461012e578060031936011261012e57602060ff601f54166040519015158152f35b80fd5b503461012e5761016c6101676101463661161b565b9061014f611d3c565b9061016161015c82612750565b611d64565b92611de4565b61263b565b80f35b503461012e578060031936011261012e5760405160158054808352908352909160208301917f55f448fdea98c4d29eb340757ef0a66cd03dbb9538908a6a81d96026b71ec475915b8181106101de576101da856101ce8187038261158b565b6040519182918261164c565b0390f35b82546001600160a01b03168452602090930192600192830192016101b7565b503461012e5761016c6102486102123661161b565b9060405190856020830152600160fa1b60408301528560418301526025825261023c60458361158b565b61016161015c82612750565b6125de565b503461012e578060031936011261012e576020610268611b37565b6040519015158152f35b503461012e578060031936011261012e5760195461028f8161181c565b9161029d604051938461158b565b818352601981527f944998273e477b495144fb8794c914197f3ccb46be2900f4698fd0ef743c9695602084015b8383106102e757604051602080825281906101da908201886116b2565b6001602081926102f685611833565b8152019201920191906102ca565b503461012e578060031936011261012e57601c546103218161181c565b9161032f604051938461158b565b818352601c81527f0e4562a10381dec21b205ed72637e6b1b523bdd0e4d4d50af5cd23dd4500a211602084015b83831061037157604051806101da8782611798565b6002602060019260405161038481611526565b848060a01b03865416815261039a8587016118ff565b8382015281520192019201919061035c565b503461012e578060031936011261012e57601d546103c98161181c565b916103d7604051938461158b565b818352601d81527f6d4407e7be21f808e6509aa9fa9143369579dd7d760fe20a2c09680fc146134f602084015b83831061041957604051806101da8782611798565b6002602060019260405161042c81611526565b848060a01b0386541681526104428587016118ff565b83820152815201920192019190610404565b503461012e578060031936011261012e57601a546104718161181c565b9161047f604051938461158b565b818352601a81527f057c384a7d1c54f3a1b2e5e67b2617b8224fdfd1ea7234eea573a6ff665ff63e602084015b8383106104c957604051602080825281906101da908201886116b2565b6001602081926104d885611833565b8152019201920191906104ac565b50346107415760c036600319011261074157602435906004356044356064356084356001600160401b038111610741576105249036906004016115fd565b9160a435956001600160401b0387116107415736602388011215610741576105596105d39736906024816004013591016115c7565b945f60405182602082015283604082015284606082015285608082015260c060a08201526105b1816105a361059160e083018b61168e565b828103601f190160c08401528b61168e565b03601f19810183528261158b565b604051809a8192631076b8c360e21b835260206004840152602483019061168e565b0381305afa978815610736575f905f99610745575b5061061d926106096106279695936106026106139461263b565b8b5161268e565b60208a015161268e565b60408801516126e8565b60608601516126e8565b60808401515f51602061345f5f395f51905f523b156107415761066b5f9161067d6040519485938493639762463160e01b855260406004860152604485019061168e565b8381036003190160248501529061168e565b03815f51602061345f5f395f51905f525afa80156107365761071f575b5060a0829301515f51602061345f5f395f51905f523b1561071b5761066b83916106e0604051948593849363f320d96360e01b855260406004860152604485019061168e565b03815f51602061345f5f395f51905f525afa8015610710576106ff5750f35b816107099161158b565b61012e5780f35b6040513d84823e3d90fd5b5050fd5b60a09392505f61072e9161158b565b5f919261069a565b6040513d5f823e3d90fd5b5f80fd5b9298505092913d805f843e61075a818461158b565b820191604081840312610741576107708161180f565b906020810151906001600160401b03821161074157019860c08a850312610741576040519961079e8b611555565b80518b52602081015160208c0152604081015160408c0152606081015160608c015260808101516001600160401b03811161074157810185601f8201121561074157858160206107f093519101611b01565b60808c015260a0810151906001600160401b038211610741570184601f820112156107415761062796610602610613948d60a061083961061d9a87602061060999519101611b01565b9101529450509395965050926105e8565b34610741575f36600319011261074157601b546108668161181c565b90610874604051928361158b565b808252601b5f9081526020830191907f3ad8aa4f87544323a9d1e5dd902f40c356527a7955687113db5f9a85ad579dc1835b83831061093357848660405191829160208301906020845251809152604083019060408160051b85010192915f905b8282106108e457505050500390f35b919360019193955060206109238192603f198a820301865288519083610913835160408452604084019061168e565b920151908481840391015261175b565b96019201920185949391926108d5565b6002602060019260405161094681611526565b61094f86611833565b815261095c8587016118ff565b838201528152019201920191906108a6565b346107415761098561097f366114d7565b90611c27565b906101da6040519283921515835260406020840152803560408401526020810135606084015260408101356080840152606081013560a08401526109ee6109e36109d2608084018461170a565b60c08088015261010087019161173b565b9160a081019061170a565b848303603f190160e08601529061173b565b34610741575f36600319011261074157604051601780548083525f91825260208301917fc624b66cc0138b8fabc209247f72d758e1cf3343756d543badbf24212bed8c1591905b818110610a5e576101da856101ce8187038261158b565b82546001600160a01b0316845260209093019260019283019201610a47565b34610741575f36600319011261074157604051601880548083525f91825260208301917fb13d2d76d1f4b7be834882e410b3e3a8afaf69f83600ae24db354391d2378d2e91905b818110610adb576101da856101ce8187038261158b565b82546001600160a01b0316845260209093019260019283019201610ac4565b3461074157610b906102486020610b103661161b565b90610b19611d14565b91610b8b60026047610b2a85612750565b6040519788917f7b2274797065223a22776562617574686e2e637265617465222c226368616c6c828401526632b733b2911d1160c91b60408401528051918291018484015e810161227d60f01b838201520301601d1981018752018561158b565b611de4565b005b3461074157610b90610167610ba63661161b565b90610bc9610167610bb5611d3c565b610bc161015c85612750565b908486611de4565b610beb610248610bd7611d3c565b610be361015c85612750565b908486612270565b610bf3611d14565b90610c0061015c82612750565b92612270565b34610741575f36600319011261074157601e54610c228161181c565b90610c30604051928361158b565b808252601e5f9081526020830191907f50bb669a95c7b50b7e8a6f09454034b2b14cf2b85c730dca9a539ca82cb6e350835b838310610ce757848660405191829160208301906020845251809152604083019060408160051b85010192915f905b828210610ca057505050500390f35b91936001919395506020610cd78192603f198a82030186526040838a51878060a01b038151168452015191818582015201906116b2565b9601920192018594939192610c91565b604051610cf381611526565b82546001600160a01b03168152600183018054610d0f8161181c565b91610d1d604051938461158b565b81835260208301905f5260205f20905f905b838210610d55575050505060019282602092836002950152815201920192019190610c62565b600160208192610d6486611833565b815201930191019091610d2f565b34610741575f36600319011261074157610ded60206040515f5160206134bf5f395f51905f52828201525f51602061343f5f395f51905f526040820152601160608201526001608082015260808152610dcc60a08261158b565b6040518093819263142d1a1160e01b8352846004840152602483019061168e565b0381305afa8015610736575f90611312575b610e0991506125de565b610e6060206040515f5160206134bf5f395f51905f52828201525f51602061343f5f395f51905f526040820152601160608201526001608082015260c060a08201525f60c082015260c08152610dcc60e08261158b565b0381305afa8015610736575f906112d7575b610e7c91506125de565b610ed260206040515f5160206134bf5f395f51905f52828201525f51602061343f5f395f51905f52604082015260116060820152600160808201525f60a082015260c08082015260c08152610dcc60e08261158b565b0381305afa8015610736575f9061129c575b610eee91506125de565b610f4c60206040515f5160206134bf5f395f51905f52828201525f51602061343f5f395f51905f526040820152601160608201526001608082015260c060a082015260c0808201525f60e082015260e08152610dcc6101008261158b565b0381305afa8015610736575f90611261575b610f68915061263b565b610fcf60206040515f5160206134bf5f395f51905f52828201525f51602061343f5f395f51905f526040820152601160608201526001608082015260c060a082015260e060c08201528160e08201525f6101008201526101008152610dcc6101208261158b565b0381305afa8015610736575f90611226575b610feb915061263b565b61105360206040515f5160206134bf5f395f51905f52828201525f51602061343f5f395f51905f526040820152601160608201526001608082015260c060a082015260e060c0820152602160e08201525f6101008201526101008152610dcc6101208261158b565b0381305afa8015610736575f906111eb575b61106f91506125de565b6110d660206040515f5160206134bf5f395f51905f52828201525f51602061343f5f395f51905f526040820152601160608201526001608082015260c060a082015260e060c08201525f60e08201525f6101008201526101008152610dcc6101208261158b565b0381305afa8015610736575f906111b0575b6110f2915061263b565b61115a60206040515f5160206134bf5f395f51905f52828201525f51602061343f5f395f51905f526040820152601160608201526001608082015260c060a082015260e060c08201525f60e082015260016101008201526101008152610dcc6101208261158b565b0381305afa8015610736575f90611175575b610b90906125de565b506020813d6020116111a8575b8161118f6020938361158b565b81010312610741576111a3610b909161180f565b61116c565b3d9150611182565b506020813d6020116111e3575b816111ca6020938361158b565b81010312610741576111de6110f29161180f565b6110e8565b3d91506111bd565b506020813d60201161121e575b816112056020938361158b565b810103126107415761121961106f9161180f565b611065565b3d91506111f8565b506020813d602011611259575b816112406020938361158b565b8101031261074157611254610feb9161180f565b610fe1565b3d9150611233565b506020813d602011611294575b8161127b6020938361158b565b810103126107415761128f610f689161180f565b610f5e565b3d915061126e565b506020813d6020116112cf575b816112b66020938361158b565b81010312610741576112ca610eee9161180f565b610ee4565b3d91506112a9565b506020813d60201161130a575b816112f16020938361158b565b8101031261074157611305610e7c9161180f565b610e72565b3d91506112e4565b506020813d602011611345575b8161132c6020938361158b565b8101031261074157611340610e099161180f565b610dff565b3d915061131f565b34610741575f36600319011261074157604051601680548083525f91825260208301917fd833147d7dc355ba459fc788f669e58cfaf9dc25ddcd0702e87d69c7b512428991905b8181106113ab576101da856101ce8187038261158b565b82546001600160a01b0316845260209093019260019283019201611394565b3461074157610b906101676113de3661161b565b9061140d6102486040515f6020820152601560f81b60408201525f604182015260258152610bb560458261158b565b61143b6101676040515f6020820152600d60f81b60408201525f604182015260258152610bb560458261158b565b604051905f6020830152601d60f81b60408301525f60418301526025825261023c60458361158b565b3461074157610b906102486114783661161b565b90611481611d14565b9061016161015c60405161149660408261158b565b6011815270696e76616c69645f6368616c6c656e676560781b6020820152612750565b346107415760206114cc61097f366114d7565b506040519015158152f35b906020600319830112610741576004356001600160401b0381116107415782602382011215610741578060040135926001600160401b0384116107415760248483010111610741576024019190565b604081019081106001600160401b0382111761154157604052565b634e487b7160e01b5f52604160045260245ffd5b60c081019081106001600160401b0382111761154157604052565b606081019081106001600160401b0382111761154157604052565b90601f801991011681019081106001600160401b0382111761154157604052565b6001600160401b03811161154157601f01601f191660200190565b9291926115d3826115ac565b916115e1604051938461158b565b829481845281830111610741578281602093845f960137010152565b9080601f8301121561074157816020611618933591016115c7565b90565b604060031982011261074157600435906001600160401b03821161074157611645916004016115fd565b9060243590565b60206040818301928281528451809452019201905f5b81811061166f5750505090565b82516001600160a01b0316845260209384019390920191600101611662565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b9080602083519182815201916020808360051b8301019401925f915b8383106116dd57505050505090565b90919293946020806116fb600193601f19868203018752895161168e565b970193019301919392906116ce565b9035601e19823603018112156107415701602081359101916001600160401b03821161074157813603831361074157565b908060209392818452848401375f828201840152601f01601f1916010190565b90602080835192838152019201905f5b8181106117785750505090565b82516001600160e01b03191684526020938401939092019160010161176b565b602081016020825282518091526040820191602060408360051b8301019401925f915b8383106117ca57505050505090565b9091929394602080611800600193603f198682030187526040838b51878060a01b0381511684520151918185820152019061175b565b970193019301919392906117bb565b5190811515820361074157565b6001600160401b0381116115415760051b60200190565b90604051915f8154908160011c92600183169283156118f5575b6020851084146118e15784875286939081156118bf575060011461187b575b506118799250038361158b565b565b90505f9291925260205f20905f915b8183106118a3575050906020611879928201015f61186c565b602091935080600191548385890101520191019091849261188a565b90506020925061187994915060ff191682840152151560051b8201015f61186c565b634e487b7160e01b5f52602260045260245ffd5b93607f169361184d565b90604051918281549182825260208201905f5260205f20925f905b806007830110611a5c57611879945491818110611a3d575b818110611a1e575b8181106119ff575b8181106119e0575b8181106119c1575b8181106119a2575b818110611985575b10611970575b50038361158b565b6001600160e01b03191681526020015f611968565b602083811b6001600160e01b031916855290930192600101611962565b604083901b6001600160e01b031916845260209093019260010161195a565b606083901b6001600160e01b0319168452602090930192600101611952565b608083901b6001600160e01b031916845260209093019260010161194a565b60a083901b6001600160e01b0319168452602090930192600101611942565b60c083901b6001600160e01b031916845260209093019260010161193a565b60e083901b6001600160e01b0319168452602090930192600101611932565b916008919350610100600191865463ffffffff60e01b8160e01b16825263ffffffff60e01b8160c01b16602083015263ffffffff60e01b8160a01b16604083015263ffffffff60e01b8160801b16606083015263ffffffff60e01b8160601b16608083015263ffffffff60e01b8160401b1660a083015263ffffffff60e01b8160201b1660c083015263ffffffff60e01b1660e082015201940192018592939161191a565b929192611b0d826115ac565b91611b1b604051938461158b565b829481845281830111610741578281602093845f96015e010152565b60085460ff1615611b4757600190565b604051630667f9d760e41b81525f51602061345f5f395f51905f5260048201526519985a5b195960d21b60248201526020816044815f51602061345f5f395f51905f525afa908115610736575f91611ba0575b50151590565b90506020813d602011611bca575b81611bbb6020938361158b565b8101031261074157515f611b9a565b3d9150611bae565b90939293848311610741578411610741578101920390565b359060208110611bf8575090565b5f199060200360031b1b1690565b91908203918211611c1357565b634e487b7160e01b5f52601160045260245ffd5b91908260c08210611d0c578160801161074157611c4b607f19830160808301611bea565b908260a01161074157611c65609f19840160a08301611bea565b90601f198401848111611c135782848210918215611d02575b5050611cf957611cb2611cab611c9f868581611ca5611c9f828b818b611bd2565b90611bea565b96611bd2565b9385611c06565b601f198101908111611c135710928315611cd9575b505050611cd45760019190565b5f9190565b611ce4929350611c06565b601f198101908111611c1357105f8080611cc7565b505050505f9190565b109050825f611c7e565b9250505f9190565b6040515f6020820152600560f81b60408201525f60418201526025815261161860458261158b565b6040515f6020820152600160f81b60408201525f60418201526025815261161860458261158b565b90611879600260446020946040519586917f7b2274797065223a22776562617574686e2e676574222c226368616c6c656e67828401526332911d1160e11b60408401528051918291018484015e810161227d60f01b838201520301601d1981018552018361158b565b60209291908391805192839101825e019081520190565b611df1909392919361284e565b916040905f808351611e03858261158b565b600c81526b109bdd5b99081c995cdd5b1d60a21b60208201528451611e5881611e446020820194632d839cb360e21b8652896024840152606483019061168e565b8a604483015203601f19810183528261158b565b51906a636f6e736f6c652e6c6f675afa508151636229ca4f60e11b8152600481018590529180836024815f51602061345f5f395f51905f525afa938415612063575f935f95612239575b5060205f835180865180858901835e8101838152039060025afa156120635760205f80518451611eda816105a3868201948886611dcd565b8551918291518091835e8101838152039060025afa15612063575f5182519663020c846d60e61b88526004880152602487015281866044815f51602061345f5f395f51905f525afa92831561222f575f965f946121f9575b505f51602061349f5f395f51905f52848103908111611c1357835197611f5789611555565b8852602088019481808210911802188452601783880152600160608801526080870190828252602460a0890193828552511198896121c2575b896120e2575b5050876120c2575b876120b9575b8761206d575b87611fba575b5050505050505090565b60208092939495969798505f915193518551918183925191829101835e8101838152039060025afa15612063575f6020916105a3612002835186519283918783019586611dcd565b8451918291518091835e8101838152039060025afa1561205a57505f51935190519061203184848484896129eb565b9095901561204b5750505050505b5f808080808080611fb0565b6120559550612b07565b61203f565b513d5f823e3d90fd5b50513d5f823e3d90fd5b809750518051602010156120a557820151600160fb1b80821614908115612096575b5096611faa565b600160fc1b161590505f61208f565b634e487b7160e01b5f52603260045260245ffd5b60019750611fa4565b809750518051602010156120a557820151600160f81b9081161496611f9e565b6120ee91929950612750565b83516121366001602d836020808201966c1131b430b63632b733b2911d1160991b88528051918291018484015e8101601160f91b838201520301601e1981018452018261158b565b6121408151612742565b83519081808210911802189283601710846017180284189060206121648387611c06565b9280612187612172866115ac565b9561217f8c51978861158b565b8087526115ac565b8584019890601f1901368a3703920101855e5190519081811493846121b3575b50505050965f80611f96565b2091201490505f8080806121a7565b985074113a3cb832911d113bb2b130baba34371733b2ba1160591b6001600160581b03196021830151161460158251111698611f90565b965092508186813d8111612228575b612212818361158b565b810103126107415760208651960151925f611f32565b503d612208565b82513d5f823e3d90fd5b82809296508195503d8311612269575b612253818361158b565b810103126107415760208351930151935f611ea2565b503d612249565b61227d909392919361284e565b916040905f80835161228f858261158b565b600c81526b109bdd5b99081c995cdd5b1d60a21b602082015284516122d081611e446020820194632d839cb360e21b8652896024840152606483019061168e565b51906a636f6e736f6c652e6c6f675afa508151636229ca4f60e11b8152600481018590529180836024815f51602061345f5f395f51905f525afa938415612063575f935f956125a7575b5060205f835180865180858901835e8101838152039060025afa156120635760205f80518451612352816105a3868201948886611dcd565b8551918291518091835e8101838152039060025afa15612063575f5182519663020c846d60e61b88526004880152602487015281866044815f51602061345f5f395f51905f525afa92831561222f575f965f94612571575b505f51602061349f5f395f51905f52848103908111611c13578351976123cf89611555565b8852602088019481808210911802188452601783880152600160608801526080870190828252602460a08901938285525111988961253a575b8961246f575b50508761244f575b8761242f578761206d5787611fba575050505050505090565b965086518051602010156120a557820151600160fa1b9081161496611fa4565b809750518051602010156120a557820151600160f81b9081161496612416565b61247b91929950612750565b83516124c36001602d836020808201966c1131b430b63632b733b2911d1160991b88528051918291018484015e8101601160f91b838201520301601e1981018452018261158b565b6124cd8151612742565b83519081808210911802189283601710846017180284189060206124f18387611c06565b92806124ff612172866115ac565b8584019890601f1901368a3703920101855e51905190818114938461252b575b50505050965f8061240e565b2091201490505f80808061251f565b985074113a3cb832911d113bb2b130baba34371733b2ba1160591b6001600160581b03196021830151161460158251111698612408565b965092508186813d81116125a0575b61258a818361158b565b810103126107415760208651960151925f6123aa565b503d612580565b82809296508195503d83116125d7575b6125c1818361158b565b810103126107415760208351930151935f61231a565b503d6125b7565b806125e65750565b5f51602061345f5f395f51905f523b156107415760405163a598288560e01b815290151560048201525f816024815f51602061345f5f395f51905f525afa8015610736576126315750565b5f6118799161158b565b15806126445750565b5f51602061345f5f395f51905f523b1561074157604051630c9fd58160e01b8152901560048201525f816024815f51602061345f5f395f51905f525afa8015610736576126315750565b9080820361269a575050565b5f51602061345f5f395f51905f523b156107415760405191637c84c69b60e01b8352600483015260248201525f816044815f51602061345f5f395f51905f525afa8015610736576126315750565b908082036126f4575050565b5f51602061345f5f395f51905f523b15610741576040519163260a5b1560e21b8352600483015260248201525f816044815f51602061345f5f395f51905f525afa8015610736576126315750565b6017019081601711611c1357565b90815115612838578151600281901b906001600160fe1b03811603611c135760028101809111611c13576003900490604051917f4142434445464748494a4b4c4d4e4f505152535455565758595a616263646566601f526106707f6768696a6b6c6d6e6f707172737475767778797a303132333435363738392b2f18603f5260208301938080510160208101908151925f83525b8181106127fe575050528083528201602001604052909150565b60036004910197603f8951818160121c165183538181600c1c16516001840153818160061c165160028401531651600382015301966127e4565b905060405161284860208261158b565b5f815290565b905f91600181108015806129d4575b6129cf576003821115806129ac575b61299a5760031982101580612983575b61293e575f51602061347f5f395f51905f528211156128f357509091507bffffffff00000000000000004319055258e8617b0c46353d039cdab08101908111611c13575f51602061347f5f395f51905f52908190069081156128ee57508060010180600111611c13578111611c135790565b905090565b6128fa5750565b90915060010360018111611c13575f51602061347f5f395f51905f52908190068015612937578103908111611c135760018101809111611c135790565b5050600190565b50909150196f4319055258e8617b0c46353d039cdaaf63ffffffff60c01b0119036f4319055258e8617b0c46353d039cdaaf63ffffffff60c01b01198111611c135790565b5081195f51602061347f5f395f51905f521161287c565b5090915060010180600111611c135790565b50816f4319055258e8617b0c46353d039cdaaf63ffffffff60c01b01191161286c565b509150565b505f51602061347f5f395f51905f5282111561285d565b909192936129f98484612e9e565b158015612af6575b15612a125750505050505f90600190565b6020945f9460a094604051948552878501526040840152606083015260808201528280526101005afa15612af4575f5115612a4f57600190600190565b60205f60a06040517fbb5a52f42f9c9261ed4361f59422a1e30036e7c32b270c8807a419feca6050238152600584820152600160408201527fa71af64de5126a4a4e02b7922d66ce9415ce88a4c9d25514d91082c8725ac95760608201527f5d47723c8fbe580bb369fec9c2665d8e30a435b9932645482e7c9f11e872296b60808201528280526101005afa15612af4575f5115612aee575f90600190565b5f905f90565bfe5b50612b018186612f02565b15612a01565b91909392612b158286612e9e565b158015612e8d575b612e845760405193610200612b32818761158b565b5f5b818110612e6f575050602092612cce5f9360c093604051612b5481611570565b8681528688820152866040820152895260405191612b7183611570565b8252868201526001604082015285880190815287612cbf604051612b9481611570565b7f6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c29681527f4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5898201526001604082015260808301908152612cb0612ca1612bfa8651612fab565b9260408601938452612c0c8151612fab565b906101008701918252612c228851865190612fe8565b9660608101978852612c378951835190612fe8565b60a0820152612c498651835190612fe8565b8c820152612c5a8851835190612fe8565b60e0820152612c6c8951845190612fe8565b610120820152612c7f8651845190612fe8565b610140820152610160612c958951855190612fe8565b91015251905190612fe8565b6101808d018181529551612fe8565b6101a08c015251835190612fe8565b6101c08a015251905190612fe8565b6101e087015260405190848252848083015284604083015260608201527bffffffff00000000000000004319055258e8617b0c46353d039cdab01960808201527bffffffff00000000000000004319055258e8617b0c46353d039cdaae1960a082015260055afa905f519115612e5d579091905f51602061349f5f395f51905f52838509925f51602061349f5f395f51905f529109905f905f925f945f915b60808310612d99575050505090612d84929161338d565b505f51602061349f5f395f51905f5290061490565b86612e3b575b8160fe1c600c8260fc1c16176040612db78287612f9a565b510151612dd3575b5060019060021b9160021b92019190612d6d565b969195909482612e1757505050612dea8583612f9a565b51519360016040612e0a6020612e008a88612f9a565b5101519886612f9a565b5101519695945b90612dbf565b90612e309291612e2a6001989987612f9a565b51613106565b969195909594612e11565b9395612e4c9195612e529397613007565b91613007565b959194909493612d9f565b634e487b715f5260126020526024601cfd5b602090612e7a612f7c565b8189015201612b34565b50505050505f90565b50612e988482612f02565b15612b1d565b908115159182612eeb575b5081612ee1575b81612eb9575090565b7f7fffffff800000007fffffffffffffffde737d56d38bcf4279dce5617e3192a89150111590565b8015159150612eb0565b5f51602061349f5f395f51905f521191505f612ea9565b600160601b63ffffffff60c01b03197f5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b8183816003600160601b0363ffffffff60c01b031981838009080908600160601b63ffffffff60c01b031983800914600160601b63ffffffff60c01b031992831191909211161690565b60405190612f8982611570565b5f6040838281528260208201520152565b9060108110156120a55760051b0190565b612fcb90612fb7612f7c565b508051906040602082015191015191613007565b9060405192612fd984611570565b83526020830152604082015290565b612fcb91612ff4612f7c565b5080516040602083015192015192613106565b929091600160601b63ffffffff60c01b0319838009600160601b63ffffffff60c01b0319828009600160601b63ffffffff60c01b0319908190819080096003600160601b0363ffffffff60c01b031909600160601b63ffffffff60c01b0319808880096003090894600160601b63ffffffff60c01b031990819083900960040994600160601b63ffffffff60c01b03198087600209600160601b63ffffffff60c01b0319908103908380090895600160601b63ffffffff60c01b031992839081908009600809600160601b63ffffffff60c01b03199081039290918290898203900890090892600160601b63ffffffff60c01b03199182910960020990565b60408101515f958695869591949391929091600160601b63ffffffff60c01b0319828009600160601b63ffffffff60c01b031984800992600160601b63ffffffff60c01b03198086860960208501510991600160601b63ffffffff60c01b031983810381808585098a09089351600160601b63ffffffff60c01b03199086900990600160601b63ffffffff60c01b0319908282039082908b090890811585151694855f146132bc5750505050506001146131c1575b50505050565b929650909450919250600160601b63ffffffff60c01b031984800990600160601b63ffffffff60c01b0319908190819080096003600160601b0363ffffffff60c01b031909600160601b63ffffffff60c01b0319808880096003090894600160601b63ffffffff60c01b031990819083900960040994600160601b63ffffffff60c01b03198087600209600160601b63ffffffff60c01b0319908103908380090895600160601b63ffffffff60c01b031992839081908009600809600160601b63ffffffff60c01b03199081039290918290898203900890090892600160601b63ffffffff60c01b031991829109600209905f8080806131bb565b939c50919a5097985093969550929350600160601b63ffffffff60c01b03199150849050800991600160601b63ffffffff60c01b03199083900991600160601b63ffffffff60c01b031990840991600160601b63ffffffff60c01b03198082600209600160601b63ffffffff60c01b03199081039085810381868009080897600160601b63ffffffff60c01b031993849109600160601b63ffffffff60c01b031990810392909182908a8203900890090893600160601b63ffffffff60c01b0319928391099009905f8080806131bb565b929180156134345760408051602080825281810181905291810182905260608101929092526bfffffffffffffffffffffffe63ffffffff60c01b03196080830152600160601b63ffffffff60c01b031960a0830152905f9060c09060055afa905f519115612e5d57600160601b63ffffffff60c01b031982800993600160601b63ffffffff60c01b03199085900993600160601b63ffffffff60c01b031992839109900990565b505090505f905f9056fe60a73bfb121a98fb6b52dfb29eb0defd76b60065b8cf07902baf28c167d24daf0000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12dffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632550ffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551414f72a4d550cad29f17d9d99a4af64b3776ec5538cd440cef0f03fef2e9e010a2646970667358221220301f908b7cae3fb12ba39343bf8c1f134f2bd2ed0bb4a03c4cebc6bec4a515fa64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> WebAuthnTest:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[WebAuthnTest]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, WebAuthnTest, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[WebAuthnTest]]:
        return cls._deploy(request_type, [], return_tx, WebAuthnTest, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def testVerify(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#13)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    @overload
    def testVerify(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#13)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    @overload
    def testVerify(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#13)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    @overload
    def testVerify(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#13)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    def testVerify(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#13)

        Args:
            challenge: bytes
            seed: uint256
        """
        return self._execute(self.chain, request_type, "e6aad37c", [challenge, seed], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testVerifyInvalidType(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#26)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    @overload
    def testVerifyInvalidType(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#26)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    @overload
    def testVerifyInvalidType(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#26)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    @overload
    def testVerifyInvalidType(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#26)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    def testVerifyInvalidType(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#26)

        Args:
            challenge: bytes
            seed: uint256
        """
        return self._execute(self.chain, request_type, "3de31524", [challenge, seed], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testVerifyInvalidChallenge(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#40)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    @overload
    def testVerifyInvalidChallenge(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#40)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    @overload
    def testVerifyInvalidChallenge(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#40)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    @overload
    def testVerifyInvalidChallenge(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#40)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    def testVerifyInvalidChallenge(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#40)

        Args:
            challenge: bytes
            seed: uint256
        """
        return self._execute(self.chain, request_type, "149f65ca", [challenge, seed], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testVerifyFlagsUP(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#53)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    @overload
    def testVerifyFlagsUP(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#53)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    @overload
    def testVerifyFlagsUP(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#53)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    @overload
    def testVerifyFlagsUP(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#53)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    def testVerifyFlagsUP(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#53)

        Args:
            challenge: bytes
            seed: uint256
        """
        return self._execute(self.chain, request_type, "d48aacc7", [challenge, seed], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testVerifyFlagsUV(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#67)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    @overload
    def testVerifyFlagsUV(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#67)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    @overload
    def testVerifyFlagsUV(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#67)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    @overload
    def testVerifyFlagsUV(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#67)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    def testVerifyFlagsUV(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#67)

        Args:
            challenge: bytes
            seed: uint256
        """
        return self._execute(self.chain, request_type, "3d21718b", [challenge, seed], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testVerifyFlagsBEBS(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#101)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    @overload
    def testVerifyFlagsBEBS(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#101)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    @overload
    def testVerifyFlagsBEBS(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#101)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    @overload
    def testVerifyFlagsBEBS(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#101)

        Args:
            challenge: bytes
            seed: uint256
        """
        ...

    def testVerifyFlagsBEBS(self, challenge: Union[bytearray, bytes], seed: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#101)

        Args:
            challenge: bytes
            seed: uint256
        """
        return self._execute(self.chain, request_type, "180580c7", [challenge, seed], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testTryDecodeAuthValid(self, r: bytes32, s: bytes32, challengeIndex: uint256, typeIndex: uint256, authenticatorData: Union[bytearray, bytes], clientDataJSON: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#176)

        Args:
            r: bytes32
            s: bytes32
            challengeIndex: uint256
            typeIndex: uint256
            authenticatorData: bytes
            clientDataJSON: string
        """
        ...

    @overload
    def testTryDecodeAuthValid(self, r: bytes32, s: bytes32, challengeIndex: uint256, typeIndex: uint256, authenticatorData: Union[bytearray, bytes], clientDataJSON: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#176)

        Args:
            r: bytes32
            s: bytes32
            challengeIndex: uint256
            typeIndex: uint256
            authenticatorData: bytes
            clientDataJSON: string
        """
        ...

    @overload
    def testTryDecodeAuthValid(self, r: bytes32, s: bytes32, challengeIndex: uint256, typeIndex: uint256, authenticatorData: Union[bytearray, bytes], clientDataJSON: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#176)

        Args:
            r: bytes32
            s: bytes32
            challengeIndex: uint256
            typeIndex: uint256
            authenticatorData: bytes
            clientDataJSON: string
        """
        ...

    @overload
    def testTryDecodeAuthValid(self, r: bytes32, s: bytes32, challengeIndex: uint256, typeIndex: uint256, authenticatorData: Union[bytearray, bytes], clientDataJSON: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#176)

        Args:
            r: bytes32
            s: bytes32
            challengeIndex: uint256
            typeIndex: uint256
            authenticatorData: bytes
            clientDataJSON: string
        """
        ...

    def testTryDecodeAuthValid(self, r: bytes32, s: bytes32, challengeIndex: uint256, typeIndex: uint256, authenticatorData: Union[bytearray, bytes], clientDataJSON: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#176)

        Args:
            r: bytes32
            s: bytes32
            challengeIndex: uint256
            typeIndex: uint256
            authenticatorData: bytes
            clientDataJSON: string
        """
        return self._execute(self.chain, request_type, "7f3aa492", [r, s, challengeIndex, typeIndex, authenticatorData, clientDataJSON], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testTryDecodeAuthInvalid(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#196)
        """
        ...

    @overload
    def testTryDecodeAuthInvalid(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#196)
        """
        ...

    @overload
    def testTryDecodeAuthInvalid(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#196)
        """
        ...

    @overload
    def testTryDecodeAuthInvalid(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#196)
        """
        ...

    def testTryDecodeAuthInvalid(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#196)
        """
        return self._execute(self.chain, request_type, "20246d7e", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tryDecodeAuth(self, encoded: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[bool, WebAuthn.WebAuthnAuth]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#279)

        Args:
            encoded: bytes
        Returns:
            success: bool
            auth: struct WebAuthn.WebAuthnAuth
        """
        ...

    @overload
    def tryDecodeAuth(self, encoded: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#279)

        Args:
            encoded: bytes
        Returns:
            success: bool
            auth: struct WebAuthn.WebAuthnAuth
        """
        ...

    @overload
    def tryDecodeAuth(self, encoded: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#279)

        Args:
            encoded: bytes
        Returns:
            success: bool
            auth: struct WebAuthn.WebAuthnAuth
        """
        ...

    @overload
    def tryDecodeAuth(self, encoded: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[bool, WebAuthn.WebAuthnAuth]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#279)

        Args:
            encoded: bytes
        Returns:
            success: bool
            auth: struct WebAuthn.WebAuthnAuth
        """
        ...

    def tryDecodeAuth(self, encoded: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[bool, WebAuthn.WebAuthnAuth], TransactionAbc[Tuple[bool, WebAuthn.WebAuthnAuth]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#279)

        Args:
            encoded: bytes
        Returns:
            success: bool
            auth: struct WebAuthn.WebAuthnAuth
        """
        return self._execute(self.chain, request_type, "41dae30c", [encoded], True if request_type == "tx" else False, Tuple[bool, WebAuthn.WebAuthnAuth], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tryDecodeAuthDrop(self, encoded: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#285)

        Args:
            encoded: bytes
        Returns:
            success: bool
        """
        ...

    @overload
    def tryDecodeAuthDrop(self, encoded: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#285)

        Args:
            encoded: bytes
        Returns:
            success: bool
        """
        ...

    @overload
    def tryDecodeAuthDrop(self, encoded: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#285)

        Args:
            encoded: bytes
        Returns:
            success: bool
        """
        ...

    @overload
    def tryDecodeAuthDrop(self, encoded: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#285)

        Args:
            encoded: bytes
        Returns:
            success: bool
        """
        ...

    def tryDecodeAuthDrop(self, encoded: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/test/utils/cryptography/WebAuthn.t.sol#285)

        Args:
            encoded: bytes
        Returns:
            success: bool
        """
        return self._execute(self.chain, request_type, "142d1a11", [encoded], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

WebAuthnTest.testVerify.selector = bytes4(b'\xe6\xaa\xd3|')
WebAuthnTest.testVerifyInvalidType.selector = bytes4(b'=\xe3\x15$')
WebAuthnTest.testVerifyInvalidChallenge.selector = bytes4(b'\x14\x9fe\xca')
WebAuthnTest.testVerifyFlagsUP.selector = bytes4(b'\xd4\x8a\xac\xc7')
WebAuthnTest.testVerifyFlagsUV.selector = bytes4(b'=!q\x8b')
WebAuthnTest.testVerifyFlagsBEBS.selector = bytes4(b'\x18\x05\x80\xc7')
WebAuthnTest.testTryDecodeAuthValid.selector = bytes4(b'\x7f:\xa4\x92')
WebAuthnTest.testTryDecodeAuthInvalid.selector = bytes4(b' $m~')
WebAuthnTest.tryDecodeAuth.selector = bytes4(b'A\xda\xe3\x0c')
WebAuthnTest.tryDecodeAuthDrop.selector = bytes4(b'\x14-\x1a\x11')
