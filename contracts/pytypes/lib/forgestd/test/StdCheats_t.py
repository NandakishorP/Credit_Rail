
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.forgestd.src.StdCheats import StdCheats
from pytypes.lib.forgestd.src.Test import Test



class StdCheatsTest(Test):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#10)
    """
    _abi = {b'\x9c\x95U\xb1\xe3\x10.<\xf4\x8fB}y\xcbg\x8f]\x9b\xd1\xed\n\xd5t8\x94a\xe2U\xf9Qp\xed': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'who', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes4', 'name': 'fsig', 'type': 'bytes4'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'keysHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'slot', 'type': 'uint256'}], 'name': 'SlotFound', 'type': 'event'}, b'\x08\x0f\xc4\xa9f \xc4F.p[#\xf3FA?\xe3yk\xb6<o\x8d\x85\x91\xba\xec\x0e#\x15w\xa5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'who', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'slot', 'type': 'uint256'}], 'name': 'WARNING_UninitedSlot', 'type': 'event'}, b'A0O\xac\xd92=u\xb1\x1b\xcd\xd6\t\xcb8\xef\xff\xfd\xb0W\x10\xf7\xca\xf0\xe9\xb1lm\x9dp\x9fP': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log', 'type': 'event'}, b'z\xe7LRt\x14\xae\x13_\xd9pG\xb1)!\xa5\xec9\x11\xb8\x04\x19xU\xd6~%\xc7\xb7^\xe6\xf3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'log_address', 'type': 'event'}, b'\xfb\x10(e\xd5\n\xdd\xdd\xf6\x9d\xa9\xb5\xaa\x1b\xce\xd6l\x80\xcf\x86\x9a\\\x8d\x04q\xa4g\xe1\x8c\xe9\xca\xb1': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_array', 'type': 'event'}, b'\x89\n\x82g\x9bG\x0f+\xd8(\x16\xed\x9b\x16\x1f\x97\xd8\xb9g\xf3\x7f\xa3d|!\xd5\xbf9t\x9e-\xd5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_array', 'type': 'event'}, b'@\xe1\x84\x0fWi\x07=a\xbd\x017-\x9bu\xba\xa9\x84-V)\xa0\xc9\x9f\xf1\x03\xbe\x11x\xa8\xe9\xe2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_array', 'type': 'event'}, b'#\xb6*\xd0XM$\xa7_\x0b\xf3V\x03\x91\xefVY\xecm\xb1&\x9cV\xe1\x1a\xa2A\xd67\xf1\x9b ': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'log_bytes', 'type': 'event'}, b'\xe8\x16\x99\xb8Q\x13\xee\xa1\xc7>\x10X\x8b+\x03^U\x893ic!s\xaf\xd4?\xeb\x19/\xacd\xe3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'log_bytes32', 'type': 'event'}, b'\x0e\xb5\xd5&$\xc8\xd2\x8a\xda\x9f\xc5Z\x8cP.\xd5\xaa?\xbe/\xb6\xe9\x1bq\xb5\xf3v\x88+\x1d/\xb8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256', 'name': '', 'type': 'int256'}], 'name': 'log_int', 'type': 'event'}, b'\x9cN\x85A\xca\x8f\r\xc1\xc4\x13\xf9\x10\x8ff\xd8-<\xec\xb1\xbd\xdb\xceCza\xca\xa3\x17\\L\xc9o': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address', 'name': 'val', 'type': 'address'}], 'name': 'log_named_address', 'type': 'event'}, b'\x00\xaa\xa3\x9c\x9f\xfb_VzE48\x0cspup.\x1f\x7f\x14\x10\x7f\xc9S(\xe3\xb5l\x03%\xfb': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xa7>\xda\tf/F\xdd\xe7)\xbeF\x118_\xf3O\xe6\xc4O\xbb\xc6\xf7\xe1{\x04+Y\xa3D[W': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_named_array', 'type': 'event'}, b";\xcf\xb2\xae.\x8d\x13-\xd1\xfc\xe7\xcf'\x8a\x9a\x19uj\x9f\xce\xab\xe4p\xdf;\xda\xbbK\xc5w\xd1\xbd": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xd2n\x16\xca\xd4T\x87\x05\xe4\xc9\xe2\xd9O\x98\xee\x91\xc2\x89\x08^\xe4%YO\xd5c_\xa2\x96L\xcf\x18': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'val', 'type': 'bytes'}], 'name': 'log_named_bytes', 'type': 'event'}, b'\xaf\xb7\x95\xc9\xc6\x1eO\xe7F\x8c8o\x92]zT)\xec\xad\x9c\x04\x95\xdd\xb8\xd3\x8di\x06\x14\xd3/\x99': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'val', 'type': 'bytes32'}], 'name': 'log_named_bytes32', 'type': 'event'}, b']\xa6\xce\x9dQ\x15\x1b\xa1\x0c\t\xa5Y\xef$\xd5 \xb9\xda\xc5\xc5\xb8\x81\n\xe8CNM\r\x86A\x1a\x95': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_int', 'type': 'event'}, b"\xeb\x8b\xa4<\xedu7B\x19F\xbdC\xe8(\xb8\xb2\xb8B\x89'\xaa\x8f\x80\x1c\x13\xd94\xbf\x11\xac\xa5{": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_uint', 'type': 'event'}, b'/\xe62w\x91t7CxD*\x8e\x97\x8b\xcc\xfb\xdc\xc1\xd6\xb2\xb0\xd8\x1f~\x8e\xb7v\xab"\x86\xf1h': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}], 'name': 'log_named_int', 'type': 'event'}, b'(\x0fDF\xb2\x8a\x13rA}\xdae\x8d0\xb9[)\x92\xb1*\xc9\xc7\xf3xS_)\xa9z\xcf5\x83': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'val', 'type': 'string'}], 'name': 'log_named_string', 'type': 'event'}, b'\xb2\xde/\xbe\x80\x1a\r\xf6\xc0\xcb\xdd\xfdD\x8b\xa3\xc4\x1dH\xa0@\xca5\xc5l\x81\x96\xef\x0f\xca\xe7!\xa8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}], 'name': 'log_named_uint', 'type': 'event'}, b'\x0b.\x13\xff \xac{GA\x98eU\x83\xed\xf7\r\xed\xd2\xc1\xdc\x98\x0e2\x9cO\xbb/\xc0t\x8byk': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log_string', 'type': 'event'}, b',\xab\x97\x90Q\x0f\xd8\xbd\xfb\xd2\x11R\x88\xdb3\xfe\xc6f\x91\xd4v\xef\xc5B|\xfdL\ti0\x17U': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'log_uint', 'type': 'event'}, b"\xe7\x95\x0e\xde\x03\x94\xb9\xf2\xceJZ\x1b\xf5\xa7\xe1\x85$\x11\xf7\xe6f\x1bC\x08\xc9\x13\xc4\xbf\xd1\x10'\xe4": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'logs', 'type': 'event'}, b'\xfav&\xd4': {'inputs': [], 'name': 'IS_TEST', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xces\xc4I': {'inputs': [], 'name': '_revertDeployCodeTo', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'J\xf9g\xd1': {'inputs': [{'internalType': 'string', 'name': 'what', 'type': 'string'}], 'name': 'deployCodeHelper', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb5P\x8a\xa9': {'inputs': [], 'name': 'excludeArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'excludedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe2\x0c\x9fq': {'inputs': [], 'name': 'excludeContracts', 'outputs': [{'internalType': 'address[]', 'name': 'excludedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb0FO\xdc': {'inputs': [], 'name': 'excludeSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'excludedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1e\xd7\x83\x1c': {'inputs': [], 'name': 'excludeSenders', 'outputs': [{'internalType': 'address[]', 'name': 'excludedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbaAO\xa6': {'inputs': [], 'name': 'failed', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\n\x92T\xe4': {'inputs': [], 'name': 'setUp', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'f\xd9\xa9\xa0': {'inputs': [], 'name': 'targetArtifactSelectors', 'outputs': [{'components': [{'internalType': 'string', 'name': 'artifact', 'type': 'string'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzArtifactSelector[]', 'name': 'targetedArtifactSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x85"l\x81': {'inputs': [], 'name': 'targetArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'targetedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'?r\x86\xf4': {'inputs': [], 'name': 'targetContracts', 'outputs': [{'internalType': 'address[]', 'name': 'targetedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'*\xde8\x80': {'inputs': [], 'name': 'targetInterfaces', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'string[]', 'name': 'artifacts', 'type': 'string[]'}], 'internalType': 'struct StdInvariant.FuzzInterface[]', 'name': 'targetedInterfaces_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x91j\x17\xc6': {'inputs': [], 'name': 'targetSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'targetedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'>^<#': {'inputs': [], 'name': 'targetSenders', 'outputs': [{'internalType': 'address[]', 'name': 'targetedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'J\x12\x97\xf8': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'testFuzz_AssumeAddressIsNot', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'u\x1e\xc6\x9d': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'testFuzz_AssumeNotForgeAddress', 'outputs': [], 'stateMutability': 'pure', 'type': 'function'}, b'\x9dbO\xa1': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'testFuzz_AssumeNotPrecompile', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x9b\xac\xb2\xa8': {'inputs': [], 'name': 'test_AssumeNotPayable', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'a&d"': {'inputs': [], 'name': 'test_AssumePayable', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\r+\xf66': {'inputs': [], 'name': 'test_BytesToUint', 'outputs': [], 'stateMutability': 'pure', 'type': 'function'}, b'x\xd5ji': {'inputs': [], 'name': 'test_ChangePrankMsgSender', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'f\xa3\x88\x88': {'inputs': [], 'name': 'test_ChangePrankMsgSenderAndTxOrigin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x05\x8a\xeb>': {'inputs': [], 'name': 'test_Deal', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xbf\xac\x85\xa4': {'inputs': [], 'name': 'test_DealERC1155Token', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf1\x1d\xfb`': {'inputs': [], 'name': 'test_DealERC1155TokenAdjustTotalSupply', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd3\x1d|\x1d': {'inputs': [], 'name': 'test_DealERC721Token', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x97U\x84;': {'inputs': [], 'name': 'test_DealToken', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Y\xff\x1d\x87': {'inputs': [], 'name': 'test_DealTokenAdjustTotalSupply', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\n\xd2\xb4\xc8': {'inputs': [], 'name': 'test_DeployCode', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf90\xb6(': {'inputs': [], 'name': 'test_DeployCodeNoArgs', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'4\x13\x06\xd5': {'inputs': [], 'name': 'test_DeployCodeTo', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xbb\x11\xac\x10': {'inputs': [], 'name': 'test_DeployCodeVal', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'A<\xfc\xb1': {'inputs': [], 'name': 'test_DeployCodeValNoArgs', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'*\xc9\xee\xdb': {'inputs': [], 'name': 'test_DeriveRememberKey', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'D@\xc5E': {'inputs': [], 'name': 'test_DestroyAccount', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x893)\xac': {'inputs': [], 'name': 'test_GasMeteringModifier', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xbf\xc4 \xf1': {'inputs': [], 'name': 'test_Hoax', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xcf\xcd\x8cE': {'inputs': [], 'name': 'test_HoaxDifferentAddresses', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'm\xc2\x87\x8a': {'inputs': [], 'name': 'test_HoaxOrigin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x00\xab\xe4\t': {'inputs': [], 'name': 'test_MakeAccountEquivalence', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x9dD\xb7\x8a': {'inputs': [], 'name': 'test_MakeAddrEquivalence', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xaeB\x82g': {'inputs': [], 'name': 'test_MakeAddrSigning', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xbd\x9f\xb2Y': {'inputs': [], 'name': 'test_ParseJsonTxDetail', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\xae\r\xdb\xc8': {'inputs': [], 'name': 'test_ReadEIP1559Transaction', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\xcf\x99\xd3\xdd': {'inputs': [], 'name': 'test_ReadEIP1559Transactions', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'"\xb4\xdeQ': {'inputs': [], 'name': 'test_ReadReceipt', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\x99\xc8|U': {'inputs': [], 'name': 'test_ReadReceipts', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\xc4\x9e\xb4\xc7': {'inputs': [], 'name': 'test_RevertIf_CannotDeployCodeTo', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'iT\xeeP': {'inputs': [], 'name': 'test_RevertIf_DeployCodeFail', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd9+\x84\xb0': {'inputs': [], 'name': 'test_Rewind', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xc5Kci': {'inputs': [], 'name': 'test_Skip', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x1dN\\\x12': {'inputs': [], 'name': 'test_StartHoax', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'X\xe8%{': {'inputs': [], 'name': 'test_StartHoaxOrigin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":46,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"stdstore","offset":0,"slot":0,"type":"t_struct(StdStorage)8331_storage"},{"astId":209,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_failed","offset":0,"slot":8,"type":"t_bool"},{"astId":2943,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"stdChainsInitialized","offset":1,"slot":8,"type":"t_bool"},{"astId":2964,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"chains","offset":0,"slot":9,"type":"t_mapping(t_string_memory_ptr,t_struct(Chain)2959_storage)"},{"astId":2968,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"defaultRpcUrls","offset":0,"slot":10,"type":"t_mapping(t_string_memory_ptr,t_string_storage)"},{"astId":2972,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"idToAlias","offset":0,"slot":11,"type":"t_mapping(t_uint256,t_string_storage)"},{"astId":2975,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"fallbackToDefaultRpcUrls","offset":0,"slot":12,"type":"t_bool"},{"astId":3931,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"gasMeteringOff","offset":1,"slot":12,"type":"t_bool"},{"astId":6002,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"stdstore","offset":0,"slot":13,"type":"t_struct(StdStorage)8331_storage"},{"astId":6923,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_excludedContracts","offset":0,"slot":21,"type":"t_array(t_address)dyn_storage"},{"astId":6926,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_excludedSenders","offset":0,"slot":22,"type":"t_array(t_address)dyn_storage"},{"astId":6929,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_targetedContracts","offset":0,"slot":23,"type":"t_array(t_address)dyn_storage"},{"astId":6932,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_targetedSenders","offset":0,"slot":24,"type":"t_array(t_address)dyn_storage"},{"astId":6935,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_excludedArtifacts","offset":0,"slot":25,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6938,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_targetedArtifacts","offset":0,"slot":26,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6942,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_targetedArtifactSelectors","offset":0,"slot":27,"type":"t_array(t_struct(FuzzArtifactSelector)6914_storage)dyn_storage"},{"astId":6946,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_excludedSelectors","offset":0,"slot":28,"type":"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage"},{"astId":6950,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_targetedSelectors","offset":0,"slot":29,"type":"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage"},{"astId":6954,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_targetedInterfaces","offset":0,"slot":30,"type":"t_array(t_struct(FuzzInterface)6920_storage)dyn_storage"},{"astId":13223,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"IS_TEST","offset":0,"slot":31,"type":"t_bool"},{"astId":39918,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"test","offset":1,"slot":31,"type":"t_contract(Bar)42206"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_address)dyn_storage":{"encoding":"dynamic_array","label":"address[]","numberOfBytes":32,"base":"t_address"},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_array(t_bytes4)dyn_storage":{"encoding":"dynamic_array","label":"bytes4[]","numberOfBytes":32,"base":"t_bytes4"},"t_array(t_string_storage)dyn_storage":{"encoding":"dynamic_array","label":"string[]","numberOfBytes":32,"base":"t_string_storage"},"t_array(t_struct(FuzzArtifactSelector)6914_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzArtifactSelector[]","numberOfBytes":32,"base":"t_struct(FuzzArtifactSelector)6914_storage"},"t_array(t_struct(FuzzInterface)6920_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzInterface[]","numberOfBytes":32,"base":"t_struct(FuzzInterface)6920_storage"},"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzSelector[]","numberOfBytes":32,"base":"t_struct(FuzzSelector)6908_storage"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_contract(Bar)42206":{"encoding":"inplace","label":"contract Bar","numberOfBytes":20},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))"},"t_mapping(t_bytes32,t_struct(FindData)8306_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)8306_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)8306_storage)"},"t_mapping(t_string_memory_ptr,t_string_storage)":{"encoding":"mapping","label":"mapping(string => string)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_string_storage"},"t_mapping(t_string_memory_ptr,t_struct(Chain)2959_storage)":{"encoding":"mapping","label":"mapping(string => struct StdChains.Chain)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_struct(Chain)2959_storage"},"t_mapping(t_uint256,t_string_storage)":{"encoding":"mapping","label":"mapping(uint256 => string)","numberOfBytes":32,"key":"t_uint256","value":"t_string_storage"},"t_string_memory_ptr":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(Chain)2959_storage":{"encoding":"inplace","label":"struct StdChains.Chain","numberOfBytes":128,"members":[{"astId":2952,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"name","offset":0,"slot":0,"type":"t_string_storage"},{"astId":2954,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"chainId","offset":0,"slot":1,"type":"t_uint256"},{"astId":2956,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"chainAlias","offset":0,"slot":2,"type":"t_string_storage"},{"astId":2958,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"rpcUrl","offset":0,"slot":3,"type":"t_string_storage"}]},"t_struct(FindData)8306_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":8299,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":8301,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":8303,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":8305,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(FuzzArtifactSelector)6914_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzArtifactSelector","numberOfBytes":64,"members":[{"astId":6910,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"artifact","offset":0,"slot":0,"type":"t_string_storage"},{"astId":6913,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(FuzzInterface)6920_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzInterface","numberOfBytes":64,"members":[{"astId":6916,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6919,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"artifacts","offset":0,"slot":1,"type":"t_array(t_string_storage)dyn_storage"}]},"t_struct(FuzzSelector)6908_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzSelector","numberOfBytes":64,"members":[{"astId":6904,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6907,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(StdStorage)8331_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":8315,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))"},{"astId":8318,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":8320,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":8322,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":8324,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":8326,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":8328,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":8330,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60808060405234602f57600160ff19600c541617600c55600160ff19601f541617601f5561cf7c90816100348239f35b5f80fdfe60806040526004361015610011575f80fd5b5f5f3560e01c8062abe409146163ac578063058aeb3e1461631d5780630a9254e4146162b65780630ad2b4c8146161845780630d2bf63614615f245780631d4e5c1214615d245780631ed7831c14615ca657806322b4de5114615a905780632ac9eedb146158885780632ade3880146156c9578063341306d5146151ea5780633e5e3c231461516c5780633f7286f4146150ee578063413cfcb114614fdf5780634440c54514614aa65780634a1297f8146148695780634af967d1146147f657806358e8257b146145c357806359ff1d87146141c15780636126642214613e9657806366a3888814613b2557806366d9a9a0146139fc5780636954ee50146138bf5780636dc2878a14613794578063751ec69d1461370a57806378d56a69146133b457806385226c8114613322578063893329ac146131e7578063916a17c61461313f5780639755843b1461304a57806399c87c5514612e235780639bacb2a814612b545780639d44b78a14612b235780639d624fa114612525578063ae0ddbc814612338578063ae42826714612210578063b0464fdc14612168578063b5508aa9146120cf578063ba414fa6146120aa578063bb11ac1014611f33578063bd9fb25914611b14578063bfac85a414611a00578063bfc420f1146118dc578063c49eb4c71461182a578063c54b636914611688578063ce73c44914611463578063cf99d3dd146111c4578063cfcd8c4514611090578063d31d7c1d14610a9a578063d92b84b0146108cf578063e20c9f7114610841578063f11dfb60146102dd578063f930b628146102905763fa7626d41461026b575f80fd5b3461028d578060031936011261028d57602060ff601f54166040519015158152f35b80fd5b503461028d578060031936011261028d576102da6102bc6102b76102b26166ca565b6178ee565b61731a565b601f546102d49060081c6001600160a01b031661731a565b9061735f565b80f35b503461028d578060031936011261028d57604051610140808201908282106001600160401b0383111761082d5790829161cdc78339039082f080156108205760018060a01b031681806040516020810190627eeac760e11b82523060248201528260448201526044815261035260648261651d565b5190845afa5061036061786c565b6020815191818082019384920101031261067b5751601180546001600160a01b03191683179055600f805463ffffffff191662fdd58e1790556103a23061aa17565b6103ab8361aa17565b6103be69021e19e0c9bab240000061aa93565b8280604051602081019063bd85b03960e01b8252826024820152602481526103e760448261651d565b5190855afa506103f561786c565b805115610701576020815191818082019384920101031261067b5751808269021e19e0c9bab2400000105f146107f2575069021e19e0c9bab23fffff1982019182116106ed5761047b9161044891616b1c565b601180546001600160a01b03191684179055600f805463ffffffff191663bd85b0391790556104768461aa17565b61aa93565b604051627eeac760e11b815230600482015260248101839052602081604481855afa80156106c55783906107be575b6104b4915061718b565b60405163bd85b03960e01b815260048101839052602081602481855afa80156106c557839061078a575b6104e891506171f8565b81806040516020810190627eeac760e11b82523060248201528260448201526044815261051660648261651d565b5190845afa5061052461786c565b6020815191818082019384920101031261067b5751601180546001600160a01b03191683179055600f805463ffffffff191662fdd58e1790556105663061aa17565b61056f8361aa17565b6105788361aa93565b8280604051602081019063bd85b03960e01b8252826024820152602481526105a160448261651d565b5190855afa506105af61786c565b805115610701576020815191818082019384920101031261067b57518082156106d057506105e09161044891616b1c565b604051627eeac760e11b815230600482015260248101839052602081604481855afa9081156106c5578391610692575b5060249161061f602092617134565b6040519283809263bd85b03960e01b82528660048301525afa801561068757829061064f575b6102da915061718b565b506020813d60201161067f575b816106696020938361651d565b8101031261067b576102da9051610645565b5f80fd5b3d915061065c565b6040513d84823e3d90fd5b90506020813d6020116106bd575b816106ad6020938361651d565b8101031261067b57516024610610565b3d91506106a0565b6040513d85823e3d90fd5b918403919050816106ed576105e0916106e8916168f9565b610448565b634e487b7160e01b84526011600452602484fd5b60405162461bcd60e51b815260206004820152605560248201527f537464436865617473206465616c28616464726573732c616464726573732c7560448201527f696e742c75696e742c626f6f6c293a2074617267657420636f6e74726163742060648201527434b9903737ba1022a92198989a9aa9bab838363c9760591b608482015260a490fd5b506020813d6020116107b6575b816107a46020938361651d565b8101031261067b576104e890516104de565b3d9150610797565b506020813d6020116107ea575b816107d86020938361651d565b8101031261067b576104b490516104aa565b3d91506107cb565b91905069021e19e0c9bab2400000039069021e19e0c9bab240000082116106ed5761047b916106e8916168f9565b50604051903d90823e3d90fd5b634e487b7160e01b84526041600452602484fd5b503461028d578060031936011261028d5760405160158054808352908352909160208301917f55f448fdea98c4d29eb340757ef0a66cd03dbb9538908a6a81d96026b71ec475915b8181106108b0576108ac856108a08187038261651d565b6040519182918261641a565b0390f35b82546001600160a01b0316845260209093019260019283019201610889565b503461028d578060031936011261028d575f51602061cf275f395f51905f523b1561028d576040516372eb5f8160e11b81526064600482015281908181602481835f51602061cf275f395f51905f525af1801561068757610a85575b505060405163796b89b960e01b81526020816004815f51602061cf275f395f51905f525afa908115610687578291610a53575b506018198101908111610a3f5781905f51602061cf275f395f51905f523b15610a3c57604051906372eb5f8160e11b825260048201528181602481835f51602061cf275f395f51905f525af1801561068757610a27575b5050604b42036109c25780f35b5f51602061cf275f395f51905f523b1561028d5760405163260a5b1560e21b8152426004820152604b6024820152819081816044815f51602061cf275f395f51905f525afa801561068757610a1657505080f35b81610a209161651d565b61028d5780f35b81610a319161651d565b61028d57805f6109b5565b50fd5b634e487b7160e01b82526011600452602482fd5b90506020813d602011610a7d575b81610a6e6020938361651d565b8101031261067b57515f61095e565b3d9150610a61565b81610a8f9161651d565b61028d57805f61092b565b503461028d578060031936011261028d576040516101a3808201908282106001600160401b0383111761082d5790829161c5278339039082f080156108205760018060a01b0316818060405160208101906331a9108f60e11b82526001602482015260248152610b0b60448261651d565b5190845afa610b1861786c565b9015610fc1578051908380610b35602080850195850101856181f5565b6040516370a0823160e01b602082019081526001600160a01b039092166024808301919091528152610b6860448261651d565b5190865afa50610b7661786c565b6020815191818082019384920101031261067b575190848060405160208101906370a0823160e01b82526002602482015260248152610bb660448261651d565b5190875afa50610bc461786c565b916020835193818082019586920101031261067b579151601180546001600160a01b03191686179055600f805463ffffffff19166370a0823117905581519093610c3493610476939092610c2f926001600160a01b0392610c299201602001906181f5565b1661aa17565b618214565b601180546001600160a01b03191683179055600f805463ffffffff19166370a08231179055610c63600261aa17565b5f198114610fad576001610c77910161aa93565b601180546001600160a01b03191682179055600f805463ffffffff1916636352211e179055610ca6600161aa17565b610cb0600261aa93565b6040516370a0823160e01b815260026004820152602081602481855afa80156106c557839061105c575b610ce49150617265565b6040516370a0823160e01b815260016004820152602081602481855afa80156106c5578390611028575b610d189150617134565b818060405160208101906331a9108f60e11b82526002602482015260248152610d4260448261651d565b5190845afa610d4f61786c565b9015610fc1578051908380610d6c602080850195850101856181f5565b6040516370a0823160e01b602082019081526001600160a01b039092166024808301919091528152610d9f60448261651d565b5190865afa50610dad61786c565b6020815191818082019384920101031261067b575190848060405160208101906370a0823160e01b82526001602482015260248152610ded60448261651d565b5190875afa50610dfb61786c565b916020835193818082019586920101031261067b579151601180546001600160a01b03191686179055600f805463ffffffff19166370a0823117905581519093610e6093610476939092610c2f926001600160a01b0392610c299201602001906181f5565b601180546001600160a01b03191683179055600f805463ffffffff19166370a08231179055610e8f600161aa17565b5f198114610fad576001610ea3910161aa93565b601180546001600160a01b03191682179055600f805463ffffffff1916636352211e179055610ed2600261aa17565b610edc600161aa93565b6040516370a0823160e01b815260016004820152602081602481855afa9081156106c5578391610f7a575b50602491610f16602092617265565b604051928380926370a0823160e01b82528060048301525afa8015610687578290610f46575b6102da9150617265565b506020813d602011610f72575b81610f606020938361651d565b8101031261067b576102da9051610f3c565b3d9150610f53565b90506020813d602011610fa5575b81610f956020938361651d565b8101031261067b57516024610f07565b3d9150610f88565b634e487b7160e01b83526011600452602483fd5b60405162461bcd60e51b815260206004820152603960248201527f537464436865617473206465616c28616464726573732c616464726573732c7560448201527834b73a163137b7b6149d1034b2103737ba1036b4b73a32b21760391b6064820152608490fd5b506020813d602011611054575b816110426020938361651d565b8101031261067b57610d189051610d0e565b3d9150611035565b506020813d602011611088575b816110766020938361651d565b8101031261067b57610ce49051610cda565b3d9150611069565b503461028d578060031936011261028d575f51602061cf275f395f51905f523b1561028d5760405163c88a5e6d60e01b81526105396004820152600160801b602482015281908181604481835f51602061cf275f395f51905f525af18015610687576111af575b50505f51602061cf275f395f51905f523b1561028d576040516323f2866760e11b81526105396004820152611ca3602482015281908181604481835f51602061cf275f395f51905f525af180156106875761119a575b50601f5460081c6001600160a01b0316803b15610a3c57816064916044604051809481936354d9714560e11b83526105396004840152611ca360248401525af1801561068757610a165750f35b816111a49161651d565b61028d57805f61114d565b816111b99161651d565b61028d57805f6110f7565b503461028d578060031936011261028d57604051636c98507360e11b81528180826004815f51602061cf275f395f51905f525afa9182156108205761123692611214918391611449575b50616779565b604051809381926360f9bb1160e01b835260206004840152602483019061645c565b03815f51602061cf275f395f51905f525afa9081156106875791809161128093829161142f575b50604080516385940ef160e01b815260048101829052948592604484019061645c565b6c2e7472616e73616374696f6e7360981b60208483039260031984016024870152600d8152015201815f51602061cf275f395f51905f525afa91821561082057819261140b575b508151820191602081818501940312611403576020810151906001600160401b03821161140757019180603f840112156114035760208301519261130a846167d3565b93611318604051958661651d565b8085526020808087019260051b84010101918383116113ff5760408101915b8383106113cc578651868861134b836167d3565b92611359604051948561651d565b808452611368601f19916167d3565b01825b8181106113b5575050815b81518110156113b1578061139561138f60019385618520565b5161a6c4565b61139f8287618520565b526113aa8186618520565b5001611376565b8280f35b6020906113c0617fda565b8282880101520161136b565b82516001600160401b0381116113fb576020916113f0878480809588010101618017565b815201920191611337565b8680fd5b8480fd5b5080fd5b8280fd5b6114289192503d8084833e611420818361651d565b81019061673f565b905f6112c7565b61144391503d8084833e611420818361651d565b5f61125d565b61145d91503d8085833e611420818361651d565b5f61120e565b503461028d578060031936011261028d576040519061148360608361651d565b602182527f5374644368656174732e742e736f6c3a526576657274696e67436f6e747261636020830152601d60fa1b60408301526114f060209282604051916114cc868461651d565b81835260405180948192638d1cc92560e01b8352886004840152602483019061645c565b03815f51602061cf275f395f51905f525afa9182156106c557918461154f928194869361166a575b5081906040519584879551918291018487015e840190828201888152815193849201905e010184815203601f19810183528261651d565b5f51602061cf275f395f51905f523b1561140357816115909160405180938192635a6b63c160e11b835284600484015260406024840152604483019061645c565b0381835f51602061cf275f395f51905f525af1801561068757908291611655575b5080808080805af16115c161786c565b901561162a5781905f51602061cf275f395f51905f523b15610a3c578161160a9160405180938192635a6b63c160e11b835284600484015260406024840152604483019061645c565b0381835f51602061cf275f395f51905f525af1801561068757610a165750f35b60405162461bcd60e51b8152600481018490526058602482015260a49061165360448201616e44565bfd5b8161165f9161651d565b61028d57805f6115b1565b82919350611681903d8089833e611420818361651d565b9290611518565b503461028d578060031936011261028d575f51602061cf275f395f51905f523b1561028d576040516372eb5f8160e11b81526064600482015281908181602481835f51602061cf275f395f51905f525af1801561068757611815575b505060405163796b89b960e01b81526020816004815f51602061cf275f395f51905f525afa9081156106875782916117e3575b5060198101809111610a3f5781905f51602061cf275f395f51905f523b15610a3c57604051906372eb5f8160e11b825260048201528181602481835f51602061cf275f395f51905f525af18015610687576117ce575b5050607d420361177a5780f35b5f51602061cf275f395f51905f523b1561028d5760405163260a5b1560e21b8152426004820152607d6024820152819081816044815f51602061cf275f395f51905f525afa801561068757610a1657505080f35b816117d89161651d565b61028d57805f61176d565b90506020813d60201161180d575b816117fe6020938361651d565b8101031261067b57515f611717565b3d91506117f1565b8161181f9161651d565b61028d57805f6116e4565b503461028d578060031936011261028d575f51602061cf275f395f51905f523b1561028d5760405163f28dceb360e01b81526020600482015260586024820152819061187860448201616e44565b818160a481835f51602061cf275f395f51905f525af18015610687576118c7575b5050303b1561028d5760405163ce73c44960e01b81528190818160048183305af1801561068757610a165750f35b816118d19161651d565b61028d57805f611899565b503461028d578060031936011261028d575f51602061cf275f395f51905f523b1561028d5760405163c88a5e6d60e01b81526105396004820152600160801b602482015281908181604481835f51602061cf275f395f51905f525af18015610687576119eb575b50505f51602061cf275f395f51905f523b1561028d5760405163ca669fa760e01b8152610539600482015281908181602481835f51602061cf275f395f51905f525af18015610687576119d6575b50601f5460081c6001600160a01b0316803b15610a3c578160649160246040518094819363646ea56d60e01b835261053960048401525af1801561068757610a165750f35b816119e09161651d565b61028d57805f611991565b816119f59161651d565b61028d57805f611943565b503461028d578060031936011261028d57604051610140808201908282106001600160401b0383111761082d5790829161cdc78339039082f0801561082057602060449160018060a01b0316838060405184810190627eeac760e11b82523060248201528287820152868152611a7760648261651d565b5190845afa50611a96611a8861786c565b8380825183010191016168be565b50601180546001600160a01b03191682179055600f805463ffffffff191662fdd58e179055611ac43061aa17565b611acd8461aa17565b611ae069021e19e0c9bab240000061aa93565b60405192838092627eeac760e11b82523060048301528660248301525afa801561068757829061064f576102da915061718b565b503461028d578060031936011261028d57604051636c98507360e11b81528180826004815f51602061cf275f395f51905f525afa91821561082057611b63926112149183916114495750616779565b03815f51602061cf275f395f51905f525afa908115610687578291611f19575b5081611bd381604093845190611b99868361651d565b601382527205ce8e4c2dce6c2c6e8d2dedce6b660ba5ce8f606b1b602083015285516385940ef160e01b815293849283926004840161733a565b03815f51602061cf275f395f51905f525afa908115611f0c578291611ef2575b508051810190602081830312611407576020810151906001600160401b038211611eee576020611c2b9281611c309501920101616c7e565b618167565b82810151909290611c49906001600160a01b0316616fcd565b60a08301516001600160a01b031673e7f1725e7734ce288f8367e1bb143e90bb3f0511198101611e70575b5060208301518151611cde91611c8c6101008361651d565b60c482526323e9918760e01b6020830152600160e01b8483015261133760e01b6060830152600360e51b6080830152600160e11b60a0830152600360e01b60c0830152600160e21b60e08301526177f9565b608083015160038103611e05575b5060c083015160028103611d8e575b506060830151906173b98203611d1a575b826102da60e0860151617134565b5f51602061cf275f395f51905f523b156114075780519163260a5b1560e21b835260048301526173b9602483015282826044815f51602061cf275f395f51905f525afa908115611d855750611d70575b80611d0c565b81611d7a9161651d565b61140357815f611d6a565b513d84823e3d90fd5b5f51602061cf275f395f51905f523b156114075781519063260a5b1560e21b825260048201526002602482015282816044815f51602061cf275f395f51905f525afa8015611df957908391611de4575b50611cfb565b81611dee9161651d565b61140357815f611dde565b505051903d90823e3d90fd5b5f51602061cf275f395f51905f523b156114075781519063260a5b1560e21b825260048201526003602482015282816044815f51602061cf275f395f51905f525afa8015611df957908391611e5b575b50611cec565b81611e659161651d565b61140357815f611e55565b5f51602061cf275f395f51905f523b15611407578151906328a9b0fb60e11b8252600482015273e7f1725e7734ce288f8367e1bb143e90bb3f0512602482015282816044815f51602061cf275f395f51905f525afa8015611df957908391611ed9575b50611c74565b81611ee39161651d565b61140357815f611ed3565b8380fd5b611f0691503d8084833e611420818361651d565b5f611bf3565b50505051903d90823e3d90fd5b611f2d91503d8084833e611420818361651d565b5f611b83565b503461028d578060031936011261028d576020604051611f53828261651d565b828152611f8383611f626166ca565b60405180938192638d1cc92560e01b8352876004840152602483019061645c565b03815f51602061cf275f395f51905f525afa91821561209f578391859361207f575b50611fe290826040519384928180850197805191829101895e8401908282018a8152815193849201905e010186815203601f19810183528261651d565b5190670de0b6b3a7640000f0906001600160a01b0382161561201557508061200f6102bc6102da9361731a565b316170cb565b6084906040519062461bcd60e51b82526004820152603e60248201527f537464436865617473206465706c6f79436f646528737472696e672c6279746560448201527f732c75696e74323536293a204465706c6f796d656e74206661696c65642e00006064820152fd5b611fe2919350612098903d8088833e611420818361651d565b9290611fa5565b6040513d86823e3d90fd5b503461028d578060031936011261028d5760206120c5616b72565b6040519015158152f35b503461028d578060031936011261028d576019546120ec816167d3565b916120fa604051938461651d565b818352601981527f944998273e477b495144fb8794c914197f3ccb46be2900f4698fd0ef743c9695602084015b83831061213c57604051806108ac87826165b6565b60016020819260405161215a816121538189616822565b038261651d565b815201920192019190612127565b503461028d578060031936011261028d57601c54612185816167d3565b91612193604051938461651d565b818352601c81527f0e4562a10381dec21b205ed72637e6b1b523bdd0e4d4d50af5cd23dd4500a211602084015b8383106121d557604051806108ac8782616615565b600260206001926040516121e881616480565b848060a01b0386541681526121fe85870161691a565b838201528152019201920191906121c0565b503461028d578060031936011261028d5761223161222c6166a8565b616eb0565b604051906338d07aa960e21b825260048201527f417f0084d1239e904e5e1c4d803baeec5639aa1e2e2344de049fc5246f88b7a86024820152826060826044815f51602061cf275f395f51905f525afa8015610820578192829083926122e9575b509260809160209460ff604051937f417f0084d1239e904e5e1c4d803baeec5639aa1e2e2344de049fc5246f88b7a8855216868401526040830152606082015282805260015afa15610820576102da908251617059565b93505050506060813d606011612330575b816123076060938361651d565b810103126114075782815160ff8116810361140357602080840151604090940151919390612292565b3d91506122fa565b503461028d578060031936011261028d57604051636c98507360e11b81528180826004815f51602061cf275f395f51905f525afa918215610820576123b2926123879183916114495750616779565b61238f617fda565b50604051809381926360f9bb1160e01b835260206004840152602483019061645c565b03815f51602061cf275f395f51905f525afa90811561068757829161250b575b50816040519163348051d760e11b835281600484015281836024815f51602061cf275f395f51905f525afa9081156106875761245b6001602e6020946124769787916124f1575b506040519586916d2e7472616e73616374696f6e735b60901b828401528051918291018484015e8101605d60f81b838201520301601e1981018552018361651d565b6040516385940ef160e01b815293849283926004840161733a565b03815f51602061cf275f395f51905f525afa9081156106875782916124d7575b508051810190602081830312611407576020810151906001600160401b038211611eee5760206124ce92816124d39501920101618017565b61a6c4565b5080f35b6124eb91503d8084833e611420818361651d565b5f612496565b61250591503d8089833e611420818361651d565b5f612419565b61251f91503d8084833e611420818361651d565b5f6123d2565b503461028d57602036600319011261028d576004356001600160a01b03811680820361140757612553616b29565b9161255c617bd2565b50825115612aac5761256c619dd2565b604051926003815194602081818501978089835e810160098152030190209460405192612598846164e7565b6040516125a981612153818b616822565b84526125eb600188015497602086019889526040516125cf816121538160028601616822565b60408701526125e46040518096819301616822565b038461651d565b6060840192835261267587511515604051907f537464436861696e7320676574436861696e28737472696e67293a204368616960208301526d37103bb4ba341030b634b0b9901160911b6040830152612670600c604e848751808a8484015e81016b11103737ba103337bab7321760a11b83820152030160131981018552018361651d565b617c34565b61267d617bd2565b50825151156126e5575b505050906102da9361269b92505190617c64565b600181109081156126c6575b81156126b4575b5061789b565b610800602160991b011090505f6126ae565b905060098111806126d8575b906126a7565b50602160991b81106126d2565b93919590949260405163975a6ce960e01b81526020600482015288818061270f602482018a61645c565b03815f51602061cf275f395f51905f525afa899181612a90575b50612a7b575061273761786c565b612741865161a716565b96895b87518110156127e45761275781896173b4565b516001600160f81b03198116606160f81b811015806127d6575b156127bf575060f81c601f190160ff81116127ab576001919060f81b6001600160f81b0319168c1a6127a3828c6173b4565b535b01612744565b634e487b7160e01b8c52601160045260248cfd5b60019291508c1a6127d0828c6173b4565b536127a5565b50603d60f91b811115612771565b5091949790929593966128286008602080936040519481869251918291018484015e81016717d49410d7d5549360c21b83820152030160171981018452018261651d565b8960ff600c54165f14612a125761287560405160208189518089835e8101600a8152030190209261288760405194859384936334515cdb60e21b855260406004860152604485019061645c565b83810360031901602485015290616822565b03815f51602061cf275f395f51905f525afa908115612a07578a916129ed575b5081525b604051936f034b73b30b634b210393831903ab936160851b60208601526128ec603086835180878484015e81018d838201520301601f19810187528661651d565b61296760316040519261292a8461291c602082019a630bc4450360e01b8c5260206024840152604483019061645c565b03601f19810186528561651d565b60405195869170034b73b30b634b210393831903ab9361d1607d1b60208401525180918484015e81018d838201520301601f19810185528461651d565b604051926129928461291c602082019363eeaa9e6f60e01b855260206024840152604483019061645c565b8451958660208701209251902082141593846129de575b50505081156129d3575b506129ce5750509161269b916102da94935b91928195612687565b602001fd5b90505151155f6129b3565b519020141591505f80806129a9565b612a0191503d808c833e611420818361651d565b5f6128a7565b6040513d8c823e3d90fd5b60405163f877cb1960e01b8152602060048201529182908190612a3990602483019061645c565b03815f51602061cf275f395f51905f525afa908115612a07578a91612a61575b5081526128ab565b612a7591503d808c833e611420818361651d565b5f612a59565b90919293955061269b94506102da96526129c5565b612aa59192503d808c833e611420818361651d565b905f612729565b60405162461bcd60e51b815260206004820152604360248201527f537464436861696e7320676574436861696e28737472696e67293a204368616960448201527f6e20616c6961732063616e6e6f742062652074686520656d707479207374726960648201526237339760e91b608482015260a490fd5b503461028d578060031936011261028d576102da612b4261222c6166a8565b50612b4e61222c6166a8565b50617059565b503461028d578060031936011261028d576040516106a5808201908282106001600160401b0383111761082d5790829161c6ca8339039082f08015610820576001600160a01b031690813b1561028d5760405162be639d60e51b81525f51602061cf275f395f51905f526004820152818160248183875af1801561068757908291612e0e575b5050813b1561028d5760405162be639d60e51b81526a636f6e736f6c652e6c6f676004820152818160248183875af1801561068757908291612df9575b5050813b1561028d5760405162be639d60e51b8152734e59b44847b379578588920ca78fbf26c0b4956c6004820152818160248183875af1801561068757908291612de4575b50505f51602061cf275f395f51905f523b1561028d57604051633d21120560e21b81528181600481835f51602061cf275f395f51905f525af1801561068757908291612dcf575b5050813b1561028d5760405162be639d60e51b815273d8da6bf26964af9d7eed9e03e53415d37aa960456004820152818160248183875af1801561068757908291612dba575b505060405191605892838101938185106001600160401b0386111761082d578394829161cd6f8339039083f08015610687575f51602061cf275f395f51905f523b15612da157604051633d21120560e21b81528381600481835f51602061cf275f395f51905f525af190811561209f578491612da5575b5050813b15612da15760405162be639d60e51b81526001600160a01b0390911660048201529082908290602490829084905af1801561068757610a165750f35b5050fd5b81612daf9161651d565b612da157825f612d61565b81612dc49161651d565b61028d57805f612cea565b81612dd99161651d565b61028d57805f612ca4565b81612dee9161651d565b61028d57805f612c5d565b81612e039161651d565b61028d57805f612c17565b81612e189161651d565b61028d57805f612bda565b503461028d578060031936011261028d57604051636c98507360e11b81528180826004815f51602061cf275f395f51905f525afa91821561082057612e72926112149183916114495750616779565b03815f51602061cf275f395f51905f525afa90811561068757918091612ebb93829161142f5750604080516385940ef160e01b815260048101829052948592604484019061645c565b682e726563656970747360b81b6020848303926003198401602487015260098152015201815f51602061cf275f395f51905f525afa91821561082057819261302e575b508151820191602081818501940312611403576020810151906001600160401b03821161140757019180603f8401121561140357602083015192612f41846167d3565b93612f4f604051958661651d565b8085526020808087019260051b84010101918383116113ff5760408101915b838310612fff5786518688612f82836167d3565b92612f90604051948561651d565b808452612f9f601f19916167d3565b01825b818110612fe8575050815b81518110156113b15780612fcc612fc660019385618520565b51618220565b612fd68287618520565b52612fe18186618520565b5001612fad565b602090612ff3617460565b82828801015201612fa2565b82516001600160401b0381116113fb576020916130238784808095880101016174c1565b815201920191612f6e565b6130439192503d8084833e611420818361651d565b905f612efe565b503461028d578060031936011261028d576040516101fc808201908282106001600160401b0383111761082d5790829161c32b8339039082f0801561082057602060249160018060a01b03168380604051848101906370a0823160e01b825230878201528681526130bc60448261651d565b5190845afa506130cd611a8861786c565b50601180546001600160a01b03191682179055600f805463ffffffff19166370a082311790556130fc3061aa17565b61310f69021e19e0c9bab240000061aa93565b6040516370a0823160e01b815230600482015292839182905afa801561068757829061064f576102da915061718b565b503461028d578060031936011261028d57601d5461315c816167d3565b9161316a604051938461651d565b818352601d81527f6d4407e7be21f808e6509aa9fa9143369579dd7d760fe20a2c09680fc146134f602084015b8383106131ac57604051806108ac8782616615565b600260206001926040516131bf81616480565b848060a01b0386541681526131d585870161691a565b83820152815201920192019190613197565b503461028d578060031936011261028d5761320c5a613204617ad0565b505a90616b1c565b6132185a613204617af4565b905a5f51602061cf275f395f51905f523b15611eee5760405163d1a5b36f60e01b815284908181600481835f51602061cf275f395f51905f525af180156106875761330d575b505060ff600c5461010061ff0019821617600c5561327a617af4565b5060081c16156132a2575b6102da9261329761329c925a90616b1c565b6168f9565b1061789b565b61ff0019600c5416600c555f51602061cf275f395f51905f523b15611eee5760405163015e6a8760e51b815284908181600481835f51602061cf275f395f51905f525af18015610687576132f8575b5050613285565b816133029161651d565b611eee57835f6132f1565b816133179161651d565b611eee57835f61325e565b503461028d578060031936011261028d57601a5461333f816167d3565b9161334d604051938461651d565b818352601a81527f057c384a7d1c54f3a1b2e5e67b2617b8224fdfd1ea7234eea573a6ff665ff63e602084015b83831061338f57604051806108ac87826165b6565b6001602081926040516133a6816121538189616822565b81520192019201919061337a565b503461028d578060031936011261028d575f51602061cf275f395f51905f523b1561028d576040516303223eab60e11b8152610539600482015281908181602481835f51602061cf275f395f51905f525af18015610687576136f5575b50601f5460081c6001600160a01b0316803b15610a3c5781809160246040518094819363646ea56d60e01b835261053960048401525af18015610687576136e0575b50506134656134606179c8565b6184cc565b5f51602061cf275f395f51905f523b1561028d576040516390c5013b60e01b815281908181600481835f51602061cf275f395f51905f525af18015610687576136cb575b50505f51602061cf275f395f51905f523b1561028d576040516303223eab60e11b815261dead600482015281908181602481835f51602061cf275f395f51905f525af18015610687576136b6575b50601f5460081c6001600160a01b0316803b15610a3c5781809160246040518094819363646ea56d60e01b835261dead60048401525af18015610687576136a1575b50506135466134606179c8565b5f51602061cf275f395f51905f523b1561028d576040516390c5013b60e01b815281908181600481835f51602061cf275f395f51905f525af180156106875761368c575b50505f51602061cf275f395f51905f523b1561028d576040516303223eab60e11b8152610539600482015281908181602481835f51602061cf275f395f51905f525af1801561068757613677575b50601f5460081c6001600160a01b0316803b15610a3c5781809160246040518094819363646ea56d60e01b835261053960048401525af1801561068757613662575b50505f51602061cf275f395f51905f523b1561028d576040516390c5013b60e01b815281908181600481835f51602061cf275f395f51905f525af1801561068757610a165750f35b8161366c9161651d565b61028d57805f61361a565b816136819161651d565b61028d57805f6135d8565b816136969161651d565b61028d57805f61358a565b816136ab9161651d565b61028d57805f613539565b816136c09161651d565b61028d57805f6134f7565b816136d59161651d565b61028d57805f6134a9565b816136ea9161651d565b61028d57805f613453565b816136ff9161651d565b61028d57805f613411565b503461028d57602036600319011261028d576004356001600160a01b0381168082036114075761373c6102da92617a29565b5f51602061cf275f395f51905f52811415908161377e575b8161375f575061789b565b734e59b44847b379578588920ca78fbf26c0b4956c915014155f6126ae565b6a636f6e736f6c652e6c6f678114159150613754565b503461028d578060031936011261028d575f51602061cf275f395f51905f523b1561028d5760405163c88a5e6d60e01b81526105396004820152600160801b602482015281908181604481835f51602061cf275f395f51905f525af18015610687576138aa575b50505f51602061cf275f395f51905f523b1561028d57806040516323f2866760e11b8152610539600482015261053960248201528181604481835f51602061cf275f395f51905f525af1801561068757613895575b50601f5460081c6001600160a01b0316803b15610a3c5781606491602460405180948193635559647760e01b835261053960048401525af1801561068757610a165750f35b8161389f9161651d565b61028d57805f613850565b816138b49161651d565b61028d57805f6137fb565b503461028d578060031936011261028d57806040516138df60608261651d565b603081527f537464436865617473206465706c6f79436f646528737472696e67293a20446560208201526f383637bcb6b2b73a103330b4b632b21760811b60408201525f51602061cf275f395f51905f523b15610a3c578161395d916040518093819263f28dceb360e01b835260206004840152602483019061645c565b0381835f51602061cf275f395f51905f525af18015610687576139e7575b5050303b1561028d57604051634af967d160e01b815260206004820152602160248201527f5374644368656174732e742e736f6c3a526576657274696e67436f6e747261636044820152601d60fa1b60648201528190818160848183305af1801561068757610a165750f35b816139f19161651d565b61028d57805f61397b565b503461028d578060031936011261028d57601b54613a19816167d3565b613a26604051918261651d565b818152601b83526020810191837f3ad8aa4f87544323a9d1e5dd902f40c356527a7955687113db5f9a85ad579dc1845b838310613ae257868587604051928392602084019060208552518091526040840160408260051b8601019392905b828210613a9357505050500390f35b91936001919395506020613ad28192603f198a820301865288519083613ac2835160408452604084019061645c565b9201519084818403910152616579565b9601920192018594939192613a84565b60026020600192604051613af581616480565b604051613b0681612153818a616822565b8152613b1385870161691a565b83820152815201920192019190613a56565b503461028d578060031936011261028d575f51602061cf275f395f51905f523b1561028d576040516308b6ac0f60e31b8152610539600482015261053a602482015281908181604481835f51602061cf275f395f51905f525af1801561068757613e81575b50601f5460081c6001600160a01b0316803b15610a3c576040516354d9714560e11b8152610539600482015261053a60248201529082908290604490829084905af1801561068757613e6c575b5050613be46134606179c8565b5f51602061cf275f395f51905f523b1561028d576040516390c5013b60e01b815281908181600481835f51602061cf275f395f51905f525af1801561068757613e57575b50505f51602061cf275f395f51905f523b1561028d576040516308b6ac0f60e31b815261dead600482015261beef602482015281908181604481835f51602061cf275f395f51905f525af1801561068757613e42575b50601f5460081c6001600160a01b0316803b15610a3c578180916044604051809481936354d9714560e11b835261dead600484015261beef60248401525af1801561068757613e2d575b5050613cd56134606179c8565b5f51602061cf275f395f51905f523b1561028d576040516390c5013b60e01b815281908181600481835f51602061cf275f395f51905f525af1801561068757613e18575b50505f51602061cf275f395f51905f523b1561028d576040516308b6ac0f60e31b8152610539600482015261053a602482015281908181604481835f51602061cf275f395f51905f525af1801561068757613e03575b50601f5460081c6001600160a01b0316803b15610a3c576040516354d9714560e11b8152610539600482015261053a60248201529082908290604490829084905af18015610687576136625750505f51602061cf275f395f51905f523b1561028d576040516390c5013b60e01b815281908181600481835f51602061cf275f395f51905f525af1801561068757610a165750f35b81613e0d9161651d565b61028d57805f613d6f565b81613e229161651d565b61028d57805f613d19565b81613e379161651d565b61028d57805f613cc8565b81613e4c9161651d565b61028d57805f613c7e565b81613e619161651d565b61028d57805f613c28565b81613e769161651d565b61028d57805f613bd7565b81613e8b9161651d565b61028d57805f613b8a565b503461028d578060031936011261028d576040516106a5808201908282106001600160401b0383111761082d5790829161c6ca8339039082f08015610820575f51602061cf275f395f51905f523b1561140357604051633d21120560e21b815282908181600481835f51602061cf275f395f51905f525af18015610687576141ac575b50506001600160a01b031690813b1561028d5760405163de4a5dcd60e01b81525f51602061cf275f395f51905f526004820152818160248183875af1801561068757908291614197575b50505f51602061cf275f395f51905f523b1561028d57604051633d21120560e21b81528181600481835f51602061cf275f395f51905f525af1801561068757908291614182575b5050813b1561028d5760405163de4a5dcd60e01b81526a636f6e736f6c652e6c6f676004820152818160248183875af180156106875790829161416d575b50505f51602061cf275f395f51905f523b1561028d57604051633d21120560e21b81528181600481835f51602061cf275f395f51905f525af1801561068757908291614158575b5050813b1561028d5760405163de4a5dcd60e01b8152734e59b44847b379578588920ca78fbf26c0b4956c6004820152818160248183875af1801561068757908291614143575b5050813b1561028d5760405163de4a5dcd60e01b815273d8da6bf26964af9d7eed9e03e53415d37aa960456004820152818160248183875af180156106875790829161412e575b505060405191605892838101938185106001600160401b0386111761082d578394829161cd6f8339039083f0801561068757813b15612da15760405163de4a5dcd60e01b81526001600160a01b0390911660048201529082908290602490829084905af1801561068757610a165750f35b816141389161651d565b61028d57805f6140bd565b8161414d9161651d565b61028d57805f614076565b816141629161651d565b61028d57805f61402f565b816141779161651d565b61028d57805f613fe8565b8161418c9161651d565b61028d57805f613faa565b816141a19161651d565b61028d57805f613f63565b816141b69161651d565b61140357815f613f19565b503461028d578060031936011261028d576040516101fc808201908282106001600160401b0383111761082d5790829161c32b8339039082f080156108205760018060a01b0316818060405160208101906370a0823160e01b82523060248201526024815261423160448261651d565b5190845afa5061423f61786c565b6020815191818082019384920101031261067b5751601180546001600160a01b03191683179055600f805463ffffffff19166370a082311790556142823061aa17565b61429569021e19e0c9bab240000061aa93565b828060405160208101906318160ddd60e01b8252600481526142b860248261651d565b5190855afa506142c661786c565b6020815191818082019384920101031261067b5751808269021e19e0c9bab2400000105f14614595575069021e19e0c9bab23fffff1982019182116106ed5761433c9161431291616b1c565b601180546001600160a01b03191684179055600f805463ffffffff19166318160ddd17905561aa93565b6040516370a0823160e01b8152306004820152602081602481855afa80156106c5578390614561575b61436f915061718b565b6040516318160ddd60e01b8152602081600481855afa80156106c557839061452d575b61439c91506171f8565b818060405160208101906370a0823160e01b8252306024820152602481526143c560448261651d565b5190845afa506143d361786c565b6020815191818082019384920101031261067b5751601180546001600160a01b03191683179055600f805463ffffffff19166370a082311790556144163061aa17565b61441f8361aa93565b828060405160208101906318160ddd60e01b82526004815261444260248261651d565b5190855afa5061445061786c565b6020815191818082019384920101031261067b5751808215614510575061447a9161431291616b1c565b6040516370a0823160e01b8152306004820152602081602481855afa9081156106c55783916144dd575b506004916144b3602092617134565b6040516318160ddd60e01b815292839182905afa801561068757829061064f576102da915061718b565b90506020813d602011614508575b816144f86020938361651d565b8101031261067b575160046144a4565b3d91506144eb565b918403919050816106ed5761447a91614528916168f9565b614312565b506020813d602011614559575b816145476020938361651d565b8101031261067b5761439c9051614392565b3d915061453a565b506020813d60201161458d575b8161457b6020938361651d565b8101031261067b5761436f9051614365565b3d915061456e565b91905069021e19e0c9bab2400000039069021e19e0c9bab240000082116106ed5761433c91614528916168f9565b503461028d578060031936011261028d575f51602061cf275f395f51905f523b1561028d5760405163c88a5e6d60e01b81526105396004820152600160801b602482015281908181604481835f51602061cf275f395f51905f525af18015610687576147e1575b50505f51602061cf275f395f51905f523b1561028d57806040516308b6ac0f60e31b8152610539600482015261053960248201528181604481835f51602061cf275f395f51905f525af18015610687576147cc575b50601f5460081c6001600160a01b0316803b15610a3c5781606491602460405180948193635559647760e01b835261053960048401525af18015610687576147b7575b50601f5460081c6001600160a01b0316803b15610a3c5781606491602460405180948193635559647760e01b835261053960048401525af18015610687576147a2575b50505f51602061cf275f395f51905f523b1561028d576040516390c5013b60e01b815281908181600481835f51602061cf275f395f51905f525af180156106875761478d575b50601f5460081c6001600160a01b0316803b15610a3c5781809160246040518094819363646ea56d60e01b83523060048401525af1801561068757610a165750f35b816147979161651d565b61028d57805f61474b565b816147ac9161651d565b61028d57805f614705565b816147c19161651d565b61028d57805f6146c2565b816147d69161651d565b61028d57805f61467f565b816147eb9161651d565b61028d57805f61462a565b503461028d57602036600319011261028d576004356001600160401b038111611403573660238201121561140357806004013590826148348361655e565b91614842604051938461651d565b838352366024858301011161140357836124d39460246020930183860137830101526178ee565b503461028d57602036600319011261028d57600435906001600160a01b0382168083036114035760025b60ff81166004811015614a44576005811015614a30578061492757506148b88461a81d565b155f51602061cf275f395f51905f523b15611eee5760405190632631f2b160e11b8252600482015283816024815f51602061cf275f395f51905f525afa801561209f57908491614912575b5050600160ff915b0116614893565b8161491c9161651d565b61140757825f614903565b600181036149a757506149398461a81d565b5f51602061cf275f395f51905f523b15611eee57604051632631f2b160e11b8152901515600482015283816024815f51602061cf275f395f51905f525afa801561209f57908491614992575b5050600160ff915b61490b565b8161499c9161651d565b61140757825f614985565b60028103614a0757505f51602061cf275f395f51905f523b1561140757604051632631f2b160e11b8152821515600482015283816024815f51602061cf275f395f51905f525afa801561209f57908491614992575050600160ff9161490b565b60ff9160019160038103614a20575061498d4687617c64565b60040361498d5761498d86617a29565b634e487b7160e01b84526021600452602484fd5b836102da84614a5481151561789b565b600181108015614a9c575b614a689061789b565b5f51602061cf275f395f51905f52811490811591614a86575061789b565b6a636f6e736f6c652e6c6f6791501415836126ae565b5060098111614a5f565b503461028d578060031936011261028d576040516101a3808201908282106001600160401b0383111761082d5790829161c5278339039082f08015610820576001600160a01b03165f51602061cf275f395f51905f523b15611403578160405163f8e18b5760e01b8152826004820152600a60248201528181604481835f51602061cf275f395f51905f525af1801561068757614fca575b50505f51602061cf275f395f51905f523b15611403578160405163c88a5e6d60e01b8152826004820152606460248201528181604481835f51602061cf275f395f51905f525af1801561068757614fb5575b5050479082813b8015614f53575b50813160648103614ef0575b50604051632d0335ab60e01b8152600481018390526020816024815f51602061cf275f395f51905f525afa8015610687576001600160401b03918391614ed1575b5016600a8103614e6e575b508131604051828152614c0a60208261651d565b5f51602061cf275f395f51905f523b156114075782614c3e9160405180938192635a6b63c160e11b8352886004840161784a565b0381835f51602061cf275f395f51905f525af19081156106c5578391614e59575b50505f51602061cf275f395f51905f523b156114035760405163c88a5e6d60e01b81528360048201528260248201528281604481835f51602061cf275f395f51905f525af19081156106c5578391614e44575b50505f51602061cf275f395f51905f523b1561140357604051631c72346d60e01b8152600481018490528281602481835f51602061cf275f395f51905f525af19081156106c5578391614e2f575b5050614d0d9047906168f9565b5f51602061cf275f395f51905f523b156114035781614d41916040518093819263c88a5e6d60e01b83523060048401616b57565b0381835f51602061cf275f395f51905f525af1801561068757614e1a575b5050803b914760648201809211614e065790614d7a916172c0565b604051632d0335ab60e01b8152600481018290526020816024815f51602061cf275f395f51905f525afa92831561209f57614dcc6001600160401b036102da95614dd1948891614dd7575b5016617134565b617134565b31617134565b614df9915060203d602011614dff575b614df1818361651d565b8101906168da565b5f614dc5565b503d614de7565b634e487b7160e01b85526011600452602485fd5b81614e249161651d565b61140757825f614d5f565b81614e399161651d565b61140357815f614d00565b81614e4e9161651d565b61140357815f614cb2565b81614e639161651d565b61140357815f614c5f565b5f51602061cf275f395f51905f523b15611403576040519063260a5b1560e21b82526004820152600a602482015281816044815f51602061cf275f395f51905f525afa80156106875715614bf65781614ec69161651d565b61140757825f614bf6565b614eea915060203d602011614dff57614df1818361651d565b5f614beb565b5f51602061cf275f395f51905f523b15611403576040519063260a5b1560e21b825260048201526064602482015281816044815f51602061cf275f395f51905f525afa80156106875715614baa5781614f489161651d565b61140757825f614baa565b5f51602061cf275f395f51905f523b156114035760405190636d83fe6960e11b8252600482015281602482015281816044815f51602061cf275f395f51905f525afa80156106875715614b9e5781614faa9161651d565b61140757825f614b9e565b81614fbf9161651d565b61140357815f614b90565b81614fd49161651d565b61140357815f614b3e565b503461028d578060031936011261028d5761501e81614ffc6166ca565b60405180938192638d1cc92560e01b835260206004840152602483019061645c565b03815f51602061cf275f395f51905f525afa9081156106875782916150d4575b50602081519101670de0b6b3a7640000f06001600160a01b0381161561506e578061200f6102bc6102da9361731a565b60405162461bcd60e51b815260206004820152603860248201527f537464436865617473206465706c6f79436f646528737472696e672c75696e74604482015277191a9b149d102232b83637bcb6b2b73a103330b4b632b21760411b6064820152608490fd5b6150e891503d8084833e611420818361651d565b5f61503e565b503461028d578060031936011261028d5760405160178054808352908352909160208301917fc624b66cc0138b8fabc209247f72d758e1cf3343756d543badbf24212bed8c15915b81811061514d576108ac856108a08187038261651d565b82546001600160a01b0316845260209093019260019283019201615136565b503461028d578060031936011261028d5760405160188054808352908352909160208301917fb13d2d76d1f4b7be834882e410b3e3a8afaf69f83600ae24db354391d2378d2e915b8181106151cb576108ac856108a08187038261651d565b82546001600160a01b03168452602090930192600192830192016151b4565b503461028d578060031936011261028d5760409061522f825161520d848261651d565b601081526f6172626974726172794164647265737360801b6020820152616eb0565b509160018060a01b038316906bffffffffffffffffffffffff198460601b169181516152e760208201600681526001858401528560608401526060835261527760808461651d565b86855161528560608261651d565b602f81527f5374644368656174732e742e736f6c3a4d6f636b436f6e74726163745769746860208201526e436f6e7374727563746f724172677360881b87820152865180948192638d1cc92560e01b835260206004840152602483019061645c565b03815f51602061cf275f395f51905f525afa9182156156bf5791602093916153459389926156a3575b5084919287519584879551918291018587015e840190838201908b8252519283915e010187815203601f19810183528261651d565b5f51602061cf275f395f51905f523b156113ff578461537891845180938192635a6b63c160e11b83528a6004840161784a565b0381835f51602061cf275f395f51905f525af180156155995790859161568e575b50808080670de0b6b3a7640000895af1946153b261786c565b95156156665784955f51602061cf275f395f51905f523b1561566257856153ed91855180938192635a6b63c160e11b8352866004840161784a565b0381835f51602061cf275f395f51905f525af1801561565857908691615643575b505061541a90316170cb565b81516303155a6760e21b8152602081600481855afa90811561559957859161560e575b50600681036155a3575b5081516352b6ff2560e11b8152602081600481855afa908115615599578591615554575b5060049161547a60209261789b565b83516362ebc01760e11b815292839182905afa90811561554a578491615507575b506001600160601b031916918083036154b357505050f35b5f51602061cf275f395f51905f523b1561550257815192637c84c69b60e01b84526004840152602483015282826044815f51602061cf275f395f51905f525afa908115611d855750610a165750f35b505050fd5b90506020813d602011615542575b816155226020938361651d565b8101031261550257516001600160601b031981168103615502575f61549b565b3d9150615515565b82513d86823e3d90fd5b90506020813d602011615591575b8161556f6020938361651d565b810103126113ff5760049161547a6155886020936168cd565b9250509161546b565b3d9150615562565b83513d87823e3d90fd5b5f51602061cf275f395f51905f523b156113ff5782519063260a5b1560e21b825260048201526006602482015284816044815f51602061cf275f395f51905f525afa8015615599579085916155f9575b50615447565b816156039161651d565b61550257835f6155f3565b9450506020843d60201161563b575b8161562a6020938361651d565b8101031261067b578493515f61543d565b3d915061561d565b8161564d9161651d565b6113ff57845f61540e565b84513d88823e3d90fd5b8580fd5b825162461bcd60e51b8152602060048201526058602482015260a49061165360448201616e44565b816156989161651d565b611eee57835f615399565b8592506156b9903d808c833e611420818361651d565b91615310565b85513d89823e3d90fd5b503461028d578060031936011261028d57601e546156e6816167d3565b6156f3604051918261651d565b818152601e83526020810191837f50bb669a95c7b50b7e8a6f09454034b2b14cf2b85c730dca9a539ca82cb6e350845b8383106157f75786858760405192839260208401906020855251809152604084019160408260051b8601019392815b83831061575f5786860387f35b919395509193603f198782030183528551906020604082019260018060a01b0381511683520151916040602083015282518091526060820190602060608260051b850101940192855b8281106157cc57505050505060208060019297019301930190928695949293615752565b90919293946020806157ea600193605f19878203018952895161645c565b97019501939291016157a8565b60405161580381616480565b82546001600160a01b0316815260018301805461581f816167d3565b9161582d604051938461651d565b8183528a526020808b20908b9084015b838210615863575050505060019282602092836002950152815201920192019190615723565b60016020819260405161587a81612153818a616822565b81520193019101909161583d565b503461028d578060031936011261028d578061591e60206040516158ad60608261651d565b603b81527f7465737420746573742074657374207465737420746573742074657374207465828201527f73742074657374207465737420746573742074657374206a756e6b0000000000604082015260405180938192636229498b60e01b835260406004840152604483019061645c565b85602483015203815f51602061cf275f395f51905f525afa908115610687578291615a5b575b50604051630884001960e21b815260048101829052602081602481865f51602061cf275f395f51905f525af180156106c5578390615a20575b6159879150616fcd565b7fac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff8081036159b15750f35b5f51602061cf275f395f51905f523b15610a3c576040519063260a5b1560e21b825260048201527fac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80602482015281816044815f51602061cf275f395f51905f525afa801561068757610a165750f35b506020813d602011615a53575b81615a3a6020938361651d565b81010312612da157615a4e61598791616c0d565b61597d565b3d9150615a2d565b9150506020813d602011615a88575b81615a776020938361651d565b8101031261067b578190515f615944565b3d9150615a6a565b503461028d578060031936011261028d57604051636c98507360e11b81528180826004815f51602061cf275f395f51905f525afa91821561082057615ae792615adf9183916114495750616779565b61238f617460565b03815f51602061cf275f395f51905f525afa908115610687578291615c8c575b5060405163348051d760e11b81526005600482015290829081836024815f51602061cf275f395f51905f525afa9081156106875761245b6001602a602094615b8e978791615c72575b50604051958691692e72656365697074735b60b01b828401528051918291018484015e8101605d60f81b838201520301601e1981018552018361651d565b03815f51602061cf275f395f51905f525afa908115610687578291615c58575b508051810190602081830312611407576020810151916001600160401b038311611eee57615bed6101009260206102da9581615bf295019201016174c1565b618220565b015160405190615c046101208361651d565b61010080835262018000698000000000000000000160841b0160208401526001604b1b6040840152606083018590526080830185905260a0830185905260c0830185905260e08301859052828101526177f9565b615c6c91503d8084833e611420818361651d565b5f615bae565b615c8691503d8089833e611420818361651d565b5f615b50565b615ca091503d8084833e611420818361651d565b5f615b07565b503461028d578060031936011261028d5760405160168054808352908352909160208301917fd833147d7dc355ba459fc788f669e58cfaf9dc25ddcd0702e87d69c7b5124289915b818110615d05576108ac856108a08187038261651d565b82546001600160a01b0316845260209093019260019283019201615cee565b503461028d578060031936011261028d575f51602061cf275f395f51905f523b1561028d5760405163c88a5e6d60e01b81526105396004820152600160801b602482015281908181604481835f51602061cf275f395f51905f525af1801561068757615f0f575b50505f51602061cf275f395f51905f523b1561028d576040516303223eab60e11b8152610539600482015281908181602481835f51602061cf275f395f51905f525af1801561068757615efa575b50601f5460081c6001600160a01b0316803b15610a3c578160649160246040518094819363646ea56d60e01b835261053960048401525af1801561068757615ee5575b50601f5460081c6001600160a01b0316803b15610a3c578160649160246040518094819363646ea56d60e01b835261053960048401525af18015610687576147a25750505f51602061cf275f395f51905f523b1561028d576040516390c5013b60e01b815281908181600481835f51602061cf275f395f51905f525af180156106875761478d5750601f5460081c6001600160a01b0316803b15610a3c5781809160246040518094819363646ea56d60e01b83523060048401525af1801561068757610a165750f35b81615eef9161651d565b61028d57805f615e1c565b81615f049161651d565b61028d57805f615dd9565b81615f199161651d565b61028d57805f615d8b565b503461028d578060031936011261028d57806040615f5a8151615f47838261651d565b60018152600360f81b60208201526173e8565b80600303616119575b50615f868151615f73838261651d565b60018152600160f91b60208201526173e8565b806002036160ae575b50615fb68151615f9f838261651d565b600181526001600160f81b031960208201526173e8565b8060ff03616043575b50615fe38151615fcf838261651d565b600281526173b960f01b60208201526173e8565b90816173b903615ff1575050f35b5f51602061cf275f395f51905f523b15612da15780519163260a5b1560e21b83526173b96004840152602483015282826044815f51602061cf275f395f51905f525afa908115611d855750610a165750f35b5f51602061cf275f395f51905f523b15612da15781519063260a5b1560e21b825260ff6004830152602482015282816044815f51602061cf275f395f51905f525afa8015611df957908391616099575b50615fbf565b816160a39161651d565b610a3c57815f616093565b5f51602061cf275f395f51905f523b15612da15781519063260a5b1560e21b825260026004830152602482015282816044815f51602061cf275f395f51905f525afa8015611df957908391616104575b50615f8f565b8161610e9161651d565b610a3c57815f6160fe565b5f51602061cf275f395f51905f523b15612da15781519063260a5b1560e21b825260036004830152602482015282816044815f51602061cf275f395f51905f525afa8015611df95790839161616f575b50615f63565b816161799161651d565b610a3c57815f616169565b503461028d578060031936011261028d5760206040516161a4828261651d565b8281526161b383611f626166ca565b03815f51602061cf275f395f51905f525afa91821561209f5783918593616296575b5061621290826040519384928180850197805191829101895e8401908282018a8152815193849201905e010186815203601f19810183528261651d565b519083f0906001600160a01b0382161561623357506102bc6102da9161731a565b6084906040519062461bcd60e51b82526004820152603660248201527f537464436865617473206465706c6f79436f646528737472696e672c6279746560448201527539949d102232b83637bcb6b2b73a103330b4b632b21760511b6064820152fd5b6162129193506162af903d8088833e611420818361651d565b92906161d5565b503461028d578060031936011261028d576040516101fc808201908282106001600160401b0383111761082d5790829161c32b8339039082f0801561082057601f8054610100600160a81b03191660089290921b610100600160a81b031691909117905580f35b503461067b575f36600319011261067b575f51602061cf275f395f51905f523b1561067b5760405163c88a5e6d60e01b8152306004820152670de0b6b3a764000060248201525f81604481835f51602061cf275f395f51905f525af180156163a15761638e575b506102da476170cb565b61639a91505f9061651d565b5f5f616384565b6040513d5f823e3d90fd5b3461067b575f36600319011261067b576164186163c76166a8565b604051906163d482616480565b5f82526163e760208301915f8352616eb0565b82526001600160a01b0316825261641261640261222c6166a8565b93516001600160a01b0316617059565b516172c0565b005b60206040818301928281528451809452019201905f5b81811061643d5750505090565b82516001600160a01b0316845260209384019390920191600101616430565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b604081019081106001600160401b0382111761649b57604052565b634e487b7160e01b5f52604160045260245ffd5b61010081019081106001600160401b0382111761649b57604052565b6101a081019081106001600160401b0382111761649b57604052565b608081019081106001600160401b0382111761649b57604052565b60e081019081106001600160401b0382111761649b57604052565b90601f801991011681019081106001600160401b0382111761649b57604052565b6040519061654d60608361651d565b565b6040519061654d60808361651d565b6001600160401b03811161649b57601f01601f191660200190565b90602080835192838152019201905f5b8181106165965750505090565b82516001600160e01b031916845260209384019390920191600101616589565b602081016020825282518091526040820191602060408360051b8301019401925f915b8383106165e857505050505090565b9091929394602080616606600193603f19868203018752895161645c565b970193019301919392906165d9565b602081016020825282518091526040820191602060408360051b8301019401925f915b83831061664757505050505090565b909192939460208061667d600193603f198682030187526040838b51878060a01b03815116845201519181858201520190616579565b97019301930191939290616638565b6166955f61655e565b906166a3604051928361651d565b5f8252565b604051906166b760408361651d565b60048252633133333760e01b6020830152565b604051906166d960408361651d565b601382527229ba3221b432b0ba39973a1739b7b61d2130b960691b6020830152565b81601f8201121561067b576020815191016167158261655e565b92616723604051948561651d565b8284528282011161067b57815f926020928386015e8301015290565b9060208282031261067b5781516001600160401b03811161067b5761676492016166fb565b90565b805191908290602001825e015f815290565b9061654d6021602080946040519581879251918291018484015e81017f2f746573742f66697874757265732f62726f6164636173742e6c6f672e6a736f83820152603760f91b60408201520301600181018552018361651d565b6001600160401b03811161649b5760051b60200190565b90600182811c92168015616818575b602083101461680457565b634e487b7160e01b5f52602260045260245ffd5b91607f16916167f9565b5f9291815491616831836167ea565b8083529260018116908115616886575060011461684d57505050565b5f9081526020812093945091925b83831061686c575060209250010190565b60018160209294939454838587010152019101919061685b565b915050602093945060ff929192191683830152151560051b010190565b9061654d6168b79260405193848092616822565b038361651d565b9081602091031261067b575190565b5190811515820361067b57565b9081602091031261067b57516001600160401b038116810361067b5790565b9190820180921161690657565b634e487b7160e01b5f52601160045260245ffd5b90604051918281549182825260208201905f5260205f20925f905b806007830110616a775761654d945491818110616a58575b818110616a39575b818110616a1a575b8181106169fb575b8181106169dc575b8181106169bd575b8181106169a0575b1061698b575b50038361651d565b6001600160e01b03191681526020015f616983565b602083811b6001600160e01b03191685529093019260010161697d565b604083901b6001600160e01b0319168452602090930192600101616975565b606083901b6001600160e01b031916845260209093019260010161696d565b608083901b6001600160e01b0319168452602090930192600101616965565b60a083901b6001600160e01b031916845260209093019260010161695d565b60c083901b6001600160e01b0319168452602090930192600101616955565b60e083901b6001600160e01b031916845260209093019260010161694d565b916008919350610100600191865463ffffffff60e01b8160e01b16825263ffffffff60e01b8160c01b16602083015263ffffffff60e01b8160a01b16604083015263ffffffff60e01b8160801b16606083015263ffffffff60e01b8160601b16608083015263ffffffff60e01b8160401b1660a083015263ffffffff60e01b8160201b1660c083015263ffffffff60e01b1660e0820152019401920185929391616935565b9190820391821161690657565b60405190616b3860408361651d565b601082526f6f7074696d69736d5f7365706f6c696160801b6020830152565b6001600160a01b039091168152602081019190915260400190565b60085460ff1615616b8257600190565b604051630667f9d760e41b81525f51602061cf275f395f51905f5260048201526519985a5b195960d21b60248201526020816044815f51602061cf275f395f51905f525afa9081156163a1575f91616bdb575b50151590565b90506020813d602011616c05575b81616bf66020938361651d565b8101031261067b57515f616bd5565b3d9150616be9565b51906001600160a01b038216820361067b57565b9080601f8301121561067b578151616c38816167d3565b92616c46604051948561651d565b81845260208085019260051b82010192831161067b57602001905b828210616c6e5750505090565b8151815260209182019101616c61565b91906101008382031261067b5760405190616c98826164af565b819380516001600160401b03811161067b57810182601f8201121561067b57805190616cc3826167d3565b91616cd1604051938461651d565b80835260208084019160051b8301019185831161067b5760208101915b838310616dd35750505050835260208101516001600160401b03811161067b5782616d1a9183016166fb565b6020840152616d2b60408201616c0d565b604084015260608101516001600160401b03811161067b5782616d4f9183016166fb565b606084015260808101516001600160401b03811161067b5782616d739183016166fb565b6080840152616d8460a08201616c0d565b60a084015260c08101516001600160401b03811161067b5782616da89183016166fb565b60c084015260e0810151916001600160401b03831161067b5760e092616dce92016166fb565b910152565b82516001600160401b03811161067b578201906040828903601f19011261067b5760405190616e0182616480565b616e0d60208401616c0d565b82526040830151916001600160401b03831161067b57616e358a602080969581960101616c21565b83820152815201920191616cee565b60407731b932b0ba3290393ab73a34b6b290313cba32b1b7b2329760411b917f537464436865617473206465706c6f79436f6465546f28737472696e672c627981527f7465732c75696e743235362c61646472657373293a204661696c656420746f2060208201520152565b906040516020810190616edd602082865180838901875e81015f838201520301601f19810183528261651d565b519020906040519263ffa1864960e01b84528260048501526020846024815f51602061cf275f395f51905f525afa9384156163a1575f94616f91575b50835f51602061cf275f395f51905f523b1561067b57604080516318caf8e360e31b81526001600160a01b0390921660048301526024820152905f9082908190616f6790604483019061645c565b0381835f51602061cf275f395f51905f525af180156163a157616f875750565b5f61654d9161651d565b9093506020813d602011616fc5575b81616fad6020938361651d565b8101031261067b57616fbe90616c0d565b925f616f19565b3d9150616fa0565b6001600160a01b031673f39fd6e51aad88f6f4ce6ab8827279cfffb92265198101616ff6575b50565b5f51602061cf275f395f51905f523b1561067b57604051906328a9b0fb60e11b8252600482015273f39fd6e51aad88f6f4ce6ab8827279cfffb9226660248201525f816044815f51602061cf275f395f51905f525afa80156163a157616f875750565b906001600160a01b0380821690831603617071575050565b5f51602061cf275f395f51905f523b1561067b576040516328a9b0fb60e11b81526001600160a01b039283166004820152911660248201525f816044815f51602061cf275f395f51905f525afa80156163a157616f875750565b670de0b6b3a764000081036170dd5750565b5f51602061cf275f395f51905f523b1561067b576040519063260a5b1560e21b82526004820152670de0b6b3a764000060248201525f816044815f51602061cf275f395f51905f525afa80156163a157616f875750565b8061713c5750565b5f51602061cf275f395f51905f523b1561067b576040519063260a5b1560e21b825260048201525f60248201525f816044815f51602061cf275f395f51905f525afa80156163a157616f875750565b69021e19e0c9bab2400000810361719f5750565b5f51602061cf275f395f51905f523b1561067b576040519063260a5b1560e21b8252600482015269021e19e0c9bab240000060248201525f816044815f51602061cf275f395f51905f525afa80156163a157616f875750565b69043c33c1937564800000810361720c5750565b5f51602061cf275f395f51905f523b1561067b576040519063260a5b1560e21b8252600482015269043c33c193756480000060248201525f816044815f51602061cf275f395f51905f525afa80156163a157616f875750565b600181036172705750565b5f51602061cf275f395f51905f523b1561067b576040519063260a5b1560e21b82526004820152600160248201525f816044815f51602061cf275f395f51905f525afa80156163a157616f875750565b908082036172cc575050565b5f51602061cf275f395f51905f523b1561067b576040519163260a5b1560e21b8352600483015260248201525f816044815f51602061cf275f395f51905f525afa80156163a157616f875750565b90813b5f60405193601f19603f840116850160405282855260208501903c565b90916173516167649360408452604084019061645c565b91602081840391015261645c565b5f51602061cf275f395f51905f523b1561067b5760405163f320d96360e01b8152915f918391829161739591906004840161733a565b03815f51602061cf275f395f51905f525afa80156163a157616f875750565b9081518110156173c5570160200190565b634e487b7160e01b5f52603260045260245ffd5b60ff8111616906576001901b90565b905f805b835182101561745b576173ff82856173b4565b5160f81c908451600184018085116169065761741a91616b1c565b6001600160fd1b0381168103616906576174369060031b6173d9565b9182810292818404149015171561690657600191617453916168f9565b9101906173ec565b925050565b6040519061746d826164cb565b5f610180838281528260208201528260408201528260608201528260808201528260a08201528260c0820152606060e082015260606101008201528261012082015282610140820152826101608201520152565b91906101a08382031261067b57604051906174db826164cb565b81938051835260208101516001600160401b03811161067b57826175009183016166fb565b602084015261751160408201616c0d565b604084015260608101516001600160401b03811161067b57826175359183016166fb565b606084015260808101516001600160401b03811161067b57826175599183016166fb565b608084015261756a60a08201616c0d565b60a084015260c08101516001600160401b03811161067b578261758e9183016166fb565b60c084015260e08101516001600160401b03811161067b57810182601f8201121561067b578051906175bf826167d3565b916175cd604051938461651d565b80835260208084019160051b8301019185831161067b5760208101915b838310617688575050505060e08401526101008101516001600160401b03811161067b578261761a9183016166fb565b6101008401526101208101516001600160401b03811161067b57826176409183016166fb565b6101208401526176536101408201616c0d565b610140840152610160810151610160840152610180810151916001600160401b03831161067b5761018092616dce92016166fb565b82516001600160401b03811161067b57820190610140828903601f19011261067b576040519061014082018281106001600160401b0382111761649b576040526176d460208401616c0d565b82526040830151602083015260608301516001600160401b03811161067b57896020617702928601016166fb565b604083015260808301516001600160401b03811161067b57896020617729928601016166fb565b606083015260a08301516001600160401b03811161067b57896020617750928601016166fb565b608083015261776160c084016168cd565b60a083015260e08301516001600160401b03811161067b5789602061778892860101616c21565b60c083015261010083015160e08301526101208301516001600160401b03811161067b578960206177bb928601016166fb565b610100830152610140830151916001600160401b03831161067b576177e88a6020809695819601016166fb565b6101208201528152019201916175ea565b5f51602061cf275f395f51905f523b1561067b576178385f916173956040519485938493639762463160e01b855260406004860152604485019061645c565b8381036003190160248501529061645c565b6001600160a01b0390911681526040602082018190526167649291019061645c565b3d15617896573d9061787d8261655e565b9161788b604051938461651d565b82523d5f602084013e565b606090565b15806178a45750565b5f51602061cf275f395f51905f523b1561067b57604051630c9fd58160e01b8152901560048201525f816024815f51602061cf275f395f51905f525afa80156163a157616f875750565b5f6179159160405180938192638d1cc92560e01b835260206004840152602483019061645c565b03815f51602061cf275f395f51905f525afa9081156163a1575f916179ae575b506020815191015ff0906001600160a01b0382161561795057565b60405162461bcd60e51b815260206004820152603060248201527f537464436865617473206465706c6f79436f646528737472696e67293a20446560448201526f383637bcb6b2b73a103330b4b632b21760811b6064820152608490fd5b6179c291503d805f833e611420818361651d565b5f617935565b604051906179d760608361651d565b603c82527f652075736520766d2e73746172745072616e6b20696e73746561642e000000006040837f6368616e67655072616e6b20697320646570726563617465642e20506c65617360208201520152565b60018060a01b03165f51602061cf275f395f51905f528114159081617aba575b81617a9b575b505f51602061cf275f395f51905f523b1561067b57604051632631f2b160e11b815290151560048201525f816024815f51602061cf275f395f51905f525afa80156163a157616f875750565b734e59b44847b379578588920ca78fbf26c0b4956c915014155f617a4f565b6a636f6e736f6c652e6c6f678114159150617a49565b5f5f5b6127108110617ae0575090565b90617aed826001926168f9565b9101617ad3565b5f905f51602061cf275f395f51905f523b1561067b5760405163d1a5b36f60e01b81525f81600481835f51602061cf275f395f51905f525af180156163a157617bbd575b50600c549161ff001983166101008117600c5560ff617b55617ad0565b9460081c1615617b63575050565b600c555f51602061cf275f395f51905f523b1561028d5760405163015e6a8760e51b81528181600481835f51602061cf275f395f51905f525af1801561068757617bab575050565b617bb682809261651d565b61028d5750565b617bca9192505f9061651d565b5f905f617b38565b60405190617bdf826164e7565b606080838181525f60208201528160408201520152565b60208091604051928184925191829101835e8101600a81520301902090565b60208091604051928184925191829101835e8101600981520301902090565b15617c3c5750565b60405162461bcd60e51b815260206004820152908190617c6090602483019061645c565b0390fd5b60018060a01b031660018110918215617f91575b5f51602061cf275f395f51905f523b1561067b57604051632631f2b160e11b815292151560048401525f9283816024815f51602061cf275f395f51905f525afa80156163a157617f7c575b50600a81148015617f71575b8015617f65575b15617d4a5750602160991b8110908115617d38575b505f51602061cf275f395f51905f523b1561140357604051632631f2b160e11b8152901515600482015281816024815f51602061cf275f395f51905f525afa801561068757617bab575050565b610800602160991b011090505f617ceb565b61a4b181148015617f59575b15617dbf575060648110908115617db457505f51602061cf275f395f51905f523b1561140357604051632631f2b160e11b8152901515600482015281816024815f51602061cf275f395f51905f525afa801561068757617bab575050565b60689150115f617ceb565b61a86a8114908115617f4d575b50617dd6575b5050565b600160981b81108015617f3d575b5f51602061cf275f395f51905f523b1561140757604051632631f2b160e11b8152901515600482015282816024815f51602061cf275f395f51905f525afa80156106c557908391617f28575b5050600160991b81108015617f18575b5f51602061cf275f395f51905f523b1561140757604051632631f2b160e11b8152901515600482015282816024815f51602061cf275f395f51905f525afa80156106c557908391617f03575b5050600360981b8110908115617ef2575b505f51602061cf275f395f51905f523b1561140357604051632631f2b160e11b8152901515600482015281816024815f51602061cf275f395f51905f525afa80156106875715617dd257617bb682809261651d565b60ff600360981b011090505f617e9d565b81617f0d9161651d565b61140357815f617e8c565b5060ff600160991b018111617e40565b81617f329161651d565b61140357815f617e30565b5060ff600160981b018111617de4565b61a8699150145f617dcc565b5062066eed8114617d56565b5062aa37dc8114617cd6565b506101a48114617ccf565b617f899193505f9061651d565b5f915f617cc3565b60ff82119250617c78565b60405190617fa9826164af565b5f60e08360608152606060208201528260408201528260608201528260808201528260a08201528260c08201520152565b60405190617fe782616502565b606060c0838281525f602082015282604082015282808201525f608082015261800e617f9c565b60a08201520152565b919060e08382031261067b576040519061803082616502565b819380516001600160401b03811161067b57810182601f8201121561067b57805161805a816167d3565b91618068604051938461651d565b81835260208084019260051b8201019185831161067b5760208201905b83821061813a5750505050835261809e60208201616c0d565b602084015260408101516001600160401b03811161067b57826180c29183016166fb565b604084015260608101516001600160401b03811161067b57826180e69183016166fb565b60608401526080810151608084015260a08101516001600160401b03811161067b5782618114918301616c7e565b60a084015260c0810151916001600160401b03831161067b5760c092616dce92016166fb565b81516001600160401b03811161067b5760209161815c898480948801016166fb565b815201910190618085565b61816f617f9c565b50618178617f9c565b906020810151602083015260018060a01b03604082015116604083015260018060a01b0360a08201511660a08301526181b4608082015161a748565b60808301526181c660c082015161a748565b60c08301526181d860e082015161a748565b60e08301526181ea606082015161a748565b606083015251815290565b9081602091031261067b57516001600160a01b038116810361067b5790565b8015616906575f190190565b618228617460565b50618231617460565b81518152610140808301516001600160a01b039081169183019190915260a0808401518216908301526040808401519091169082015260808201516182759061a748565b6080820152618287606083015161a748565b606082015261829960c083015161a748565b60c08201526182ac61012083015161a748565b6101208201526182c061018083015161a748565b6101808201526182d3602083015161a748565b602082015260e0820151928351916182ea836167d3565b926182f8604051948561651d565b808452618307601f19916167d3565b015f5b81811061846a5750505f5b8551811015618445576001906001600160a01b036183338289618520565b5151166183408287618520565b5152602061834e8289618520565b510151602061835d8388618520565b510152618377604061836f838a618520565b51015161a748565b60406183838388618520565b51015260606183928289618520565b51015160606183a18388618520565b5101526183b3608061836f838a618520565b60806183bf8388618520565b51015260c06183ce8289618520565b51015160a06183dd8388618520565b5101526183f061010061836f838a618520565b60c06183fc8388618520565b51015261840f61012061836f838a618520565b60e061841b8388618520565b51015260a061842a8289618520565b510151151561010061843c8388618520565b51015201618315565b50929093506101609160e0840152610100810151610100840152015161016082015290565b604051906101208201918083106001600160401b0384111761649b576020926040525f81525f838201525f60408201526060808201525f6080820152606060a08201525f60c08201525f60e08201525f6101008201528282880101520161830a565b5f8091604051618507816184f9602082019463104c13eb60e21b865260206024840152604483019061645c565b03601f19810183528261651d565b51906a636f6e736f6c652e6c6f675afa50616ff361786c565b80518210156173c55760209160051b010190565b6040519061854360408361651d565b6005825264105b9d9a5b60da1b6020830152565b6040519061856660408361651d565b6015825274687474703a2f2f3132372e302e302e313a3835343560581b6020830152565b6040519061859960408361651d565b6005825264185b9d9a5b60da1b6020830152565b604051906185bc60408361651d565b600782526613585a5b9b995d60ca1b6020830152565b604051906185e160408361651d565b601882527768747470733a2f2f6574682e6c6c616d617270632e636f6d60401b6020830152565b6040519061861760408361651d565b60078252661b585a5b9b995d60ca1b6020830152565b6040519061863c60408361651d565b60078252665365706f6c696160c81b6020830152565b6040519061866160608361651d565b603d82527f39346164316464663834646662386333346436626235646361323030310000006040837f68747470733a2f2f7365706f6c69612e696e667572612e696f2f76332f62393760208201520152565b604051906186c260408361651d565b60078252667365706f6c696160c81b6020830152565b604051906186e760408361651d565b6007825266486f6c65736b7960c81b6020830152565b6040519061870c60608361651d565b6022825261696f60f01b6040837f68747470733a2f2f7270632e686f6c65736b792e65746870616e64616f70732e60208201520152565b6040519061875260408361651d565b6007825266686f6c65736b7960c81b6020830152565b6040519061877760408361651d565b6005825264486f6f646960d81b6020830152565b6040519061879a60408361651d565b602082527f68747470733a2f2f7270632e686f6f64692e65746870616e64616f70732e696f6020830152565b604051906187d560408361651d565b6005825264686f6f646960d81b6020830152565b604051906187f860408361651d565b60088252674f7074696d69736d60c01b6020830152565b6040519061881e60408361651d565b601b82527f68747470733a2f2f6d61696e6e65742e6f7074696d69736d2e696f00000000006020830152565b6040519061885960408361651d565b60088252676f7074696d69736d60c01b6020830152565b6040519061887f60408361651d565b601082526f4f7074696d69736d205365706f6c696160801b6020830152565b604051906188ad60408361651d565b601b82527f68747470733a2f2f7365706f6c69612e6f7074696d69736d2e696f00000000006020830152565b604051906188e860408361651d565b600c82526b417262697472756d204f6e6560a01b6020830152565b6040519061891260408361651d565b601c82527f68747470733a2f2f617262312e617262697472756d2e696f2f727063000000006020830152565b6040519061894d60408361651d565b600c82526b617262697472756d5f6f6e6560a01b6020830152565b6040519061897760408361651d565b6014825273417262697472756d204f6e65205365706f6c696160601b6020830152565b604051906189a960608361651d565b6026825265696f2f72706360d01b6040837f68747470733a2f2f7365706f6c69612d726f6c6c75702e617262697472756d2e60208201520152565b604051906189f360408361651d565b6014825273617262697472756d5f6f6e655f7365706f6c696160601b6020830152565b60405190618a2560408361651d565b600d82526c417262697472756d204e6f766160981b6020830152565b60405190618a5060408361651d565b601c82527f68747470733a2f2f6e6f76612e617262697472756d2e696f2f727063000000006020830152565b60405190618a8b60408361651d565b600d82526c617262697472756d5f6e6f766160981b6020830152565b60405190618ab660408361651d565b60078252662837b63cb3b7b760c91b6020830152565b60405190618adb60408361651d565b601782527668747470733a2f2f706f6c79676f6e2d7270632e636f6d60481b6020830152565b60405190618b1060408361651d565b60078252663837b63cb3b7b760c91b6020830152565b60405190618b3560408361651d565b600c82526b506f6c79676f6e20416d6f7960a01b6020830152565b60405190618b5f60608361651d565b60238252626f677960e81b6040837f68747470733a2f2f7270632d616d6f792e706f6c79676f6e2e746563686e6f6c60208201520152565b60405190618ba660408361651d565b600c82526b706f6c79676f6e5f616d6f7960a01b6020830152565b60405190618bd060408361651d565b60098252684176616c616e63686560b81b6020830152565b60405190618bf760608361651d565b6025825264432f72706360d81b6040837f68747470733a2f2f6170692e617661782e6e6574776f726b2f6578742f62632f60208201520152565b60405190618c4060408361651d565b60098252686176616c616e63686560b81b6020830152565b60405190618c6760408361651d565b600e82526d4176616c616e6368652046756a6960901b6020830152565b60405190618c9360608361651d565b602a825269742f62632f432f72706360b01b6040837f68747470733a2f2f6170692e617661782d746573742e6e6574776f726b2f657860208201520152565b60405190618ce160408361651d565b600e82526d6176616c616e6368655f66756a6960901b6020830152565b60405190618d0d60408361651d565b600f82526e2127211029b6b0b93a1021b430b4b760891b6020830152565b60405190618d3a60608361651d565b60218252606760f81b6040837f68747470733a2f2f6273632d6461746173656564312e62696e616e63652e6f7260208201520152565b60405190618d7f60408361651d565b600f82526e3137312fb9b6b0b93a2fb1b430b4b760891b6020830152565b60405190618dac60408361651d565b60178252761093908814db585c9d0810da185a5b8815195cdd1b995d604a1b6020830152565b60405190618de160608361651d565b602782526617d8da185c195b60ca1b6040837f68747470733a2f2f7270632e616e6b722e636f6d2f6273635f746573746e657460208201520152565b60405190618e2c60408361651d565b6017825276189b9897dcdb585c9d17d8da185a5b97dd195cdd1b995d604a1b6020830152565b60405190618e6160408361651d565b600c82526b23b737b9b4b99021b430b4b760a11b6020830152565b60405190618e8b60408361651d565b601b82527f68747470733a2f2f7270632e676e6f736973636861696e2e636f6d00000000006020830152565b60405190618ec660408361651d565b600c82526b33b737b9b4b9afb1b430b4b760a11b6020830152565b60405190618ef060408361651d565b60088252674d6f6f6e6265616d60c01b6020830152565b60405190618f1660408361651d565b602082527f68747470733a2f2f7270632e6170692e6d6f6f6e6265616d2e6e6574776f726b6020830152565b60405190618f5160408361651d565b60088252676d6f6f6e6265616d60c01b6020830152565b60405190618f7760408361651d565b600982526826b7b7b73934bb32b960b91b6020830152565b60405190618f9e60608361651d565b602a825269616d2e6e6574776f726b60b01b6040837f68747470733a2f2f7270632e6170692e6d6f6f6e72697665722e6d6f6f6e626560208201520152565b60405190618fec60408361651d565b600982526836b7b7b73934bb32b960b91b6020830152565b6040519061901360408361651d565b60088252674d6f6f6e6261736560c01b6020830152565b6040519061903960608361651d565b6024825263776f726b60e01b6040837f68747470733a2f2f7270632e746573746e65742e6d6f6f6e6265616d2e6e657460208201520152565b6040519061908160408361651d565b60088252676d6f6f6e6261736560c01b6020830152565b604051906190a760408361651d565b600c82526b42617365205365706f6c696160a01b6020830152565b604051906190d160408361651d565b601882527768747470733a2f2f7365706f6c69612e626173652e6f726760401b6020830152565b6040519061910760408361651d565b600c82526b626173655f7365706f6c696160a01b6020830152565b6040519061913160408361651d565b60048252634261736560e01b6020830152565b6040519061915360408361651d565b601882527768747470733a2f2f6d61696e6e65742e626173652e6f726760401b6020830152565b6040519061918960408361651d565b60048252636261736560e01b6020830152565b604051906191ab60408361651d565b600d82526c426c617374205365706f6c696160981b6020830152565b604051906191d660408361651d565b601882527768747470733a2f2f7365706f6c69612e626c6173742e696f60401b6020830152565b6040519061920c60408361651d565b600d82526c626c6173745f7365706f6c696160981b6020830152565b6040519061923760408361651d565b6005825264109b185cdd60da1b6020830152565b6040519061925a60408361651d565b601482527368747470733a2f2f7270632e626c6173742e696f60601b6020830152565b6040519061928c60408361651d565b6005825264189b185cdd60da1b6020830152565b604051906192af60408361651d565b600c82526b46616e746f6d204f7065726160a01b6020830152565b604051906192d960408361651d565b601c82527f68747470733a2f2f7270632e616e6b722e636f6d2f66616e746f6d2f000000006020830152565b6040519061931460408361651d565b600c82526b66616e746f6d5f6f7065726160a01b6020830152565b6040519061933e60408361651d565b601482527311985b9d1bdb4813dc195c984815195cdd1b995d60621b6020830152565b6040519061937060608361651d565b60248252636e65742f60e01b6040837f68747470733a2f2f7270632e616e6b722e636f6d2f66616e746f6d5f7465737460208201520152565b604051906193b860408361651d565b601482527319985b9d1bdb57dbdc195c9857dd195cdd1b995d60621b6020830152565b604051906193ea60408361651d565b6007825266119c985e1d185b60ca1b6020830152565b6040519061940f60408361651d565b601482527368747470733a2f2f7270632e667261782e636f6d60601b6020830152565b6040519061944160408361651d565b6007825266199c985e1d185b60ca1b6020830152565b6040519061946660408361651d565b600f82526e119c985e1d185b0815195cdd1b995d608a1b6020830152565b6040519061949360408361651d565b601c82527f68747470733a2f2f7270632e746573746e65742e667261782e636f6d000000006020830152565b604051906194ce60408361651d565b600f82526e199c985e1d185b17dd195cdd1b995d608a1b6020830152565b604051906194fb60408361651d565b601882527710995c9858da185a5b8818905c9d1a5bc815195cdd1b995d60421b6020830152565b6040519061953160408361651d565b602082527f68747470733a2f2f62617274696f2e7270632e62657261636861696e2e636f6d6020830152565b6040519061956c60408361651d565b601882527718995c9858da185a5b97d8985c9d1a5bd7dd195cdd1b995d60421b6020830152565b604051906195a260408361651d565b6005825264466c61726560d81b6020830152565b604051906195c560608361651d565b60298252686578742f432f72706360b81b6040837f68747470733a2f2f666c6172652d6170692e666c6172652e6e6574776f726b2f60208201520152565b6040519061961260408361651d565b6005825264666c61726560d81b6020830152565b6040519061963560408361651d565b600d82526c233630b9329021b7b9ba37b71960991b6020830152565b6040519061966060608361651d565b602b82526a6b2f6578742f432f72706360a81b6040837f68747470733a2f2f636f73746f6e322d6170692e666c6172652e6e6574776f7260208201520152565b604051906196af60408361651d565b600d82526c333630b932afb1b7b9ba37b71960991b6020830152565b604051906196da60408361651d565b60048252634d6f646560e01b6020830152565b604051906196fc60408361651d565b601582527468747470733a2f2f6d6f64652e647270632e6f726760581b6020830152565b6040519061972f60408361651d565b60048252636d6f646560e01b6020830152565b6040519061975160408361651d565b600c82526b4d6f6465205365706f6c696160a01b6020830152565b6040519061977b60408361651d565b601c82527f68747470733a2f2f7365706f6c69612e6d6f64652e6e6574776f726b000000006020830152565b604051906197b660408361651d565b600c82526b6d6f64655f7365706f6c696160a01b6020830152565b604051906197e060408361651d565b60048252635a6f726160e01b6020830152565b6040519061980260408361651d565b601582527468747470733a2f2f7a6f72612e647270632e6f726760581b6020830152565b6040519061983560408361651d565b60048252637a6f726160e01b6020830152565b6040519061985760408361651d565b600c82526b5a6f7261205365706f6c696160a01b6020830152565b6040519061988160408361651d565b601f82527f68747470733a2f2f7365706f6c69612e7270632e7a6f72612e656e65726779006020830152565b604051906198bc60408361651d565b600c82526b7a6f72615f7365706f6c696160a01b6020830152565b604051906198e660408361651d565b60048252635261636560e01b6020830152565b6040519061990860408361651d565b601682527568747470733a2f2f726163656d61696e6e65742e696f60501b6020830152565b6040519061993c60408361651d565b60048252637261636560e01b6020830152565b6040519061995e60408361651d565b600c82526b52616365205365706f6c696160a01b6020830152565b6040519061998860408361651d565b600c82526b726163655f7365706f6c696160a01b6020830152565b604051906199b260408361651d565b600582526413595d185b60da1b6020830152565b604051906199d560408361651d565b601882527768747470733a2f2f6d6574616c6c322e647270632e6f726760401b6020830152565b60405190619a0b60408361651d565b60058252641b595d185b60da1b6020830152565b60405190619a2e60408361651d565b600d82526c4d6574616c205365706f6c696160981b6020830152565b60405190619a5960408361651d565b601f82527f68747470733a2f2f746573746e65742e7270632e6d6574616c6c322e636f6d006020830152565b60405190619a9460408361651d565b600d82526c6d6574616c5f7365706f6c696160981b6020830152565b60405190619abf60408361651d565b600682526542696e61727960d01b6020830152565b60405190619ae360608361651d565b602682526567732e636f6d60d01b6040837f68747470733a2f2f7270632e7a65726f2e74686562696e617279686f6c64696e60208201520152565b60405190619b2d60408361651d565b600682526562696e61727960d01b6020830152565b60405190619b5160408361651d565b600e82526d42696e617279205365706f6c696160901b6020830152565b60405190619b7d60408361651d565b600e82526d62696e6172795f7365706f6c696160901b6020830152565b60405190619ba960408361651d565b60078252664f726465726c7960c81b6020830152565b60405190619bce60408361651d565b601b82527f68747470733a2f2f7270632e6f726465726c792e6e6574776f726b00000000006020830152565b60405190619c0960408361651d565b60078252666f726465726c7960c81b6020830152565b60405190619c2e60408361651d565b600f82526e4f726465726c79205365706f6c696160881b6020830152565b60405190619c5b60408361651d565b601f82527f68747470733a2f2f746573746e65742d7270632e6f726465726c792e6f7267006020830152565b60405190619c9660408361651d565b600f82526e6f726465726c795f7365706f6c696160881b6020830152565b60405190619cc360408361651d565b60088252672ab734b1b430b4b760c11b6020830152565b60405190619ce960408361651d565b601c82527f68747470733a2f2f6d61696e6e65742e756e69636861696e2e6f7267000000006020830152565b60405190619d2460408361651d565b60088252673ab734b1b430b4b760c11b6020830152565b60405190619d4a60408361651d565b601082526f556e69636861696e205365706f6c696160801b6020830152565b60405190619d7860408361651d565b601c82527f68747470733a2f2f7365706f6c69612e756e69636861696e2e6f7267000000006020830152565b60405190619db360408361651d565b601082526f756e69636861696e5f7365706f6c696160801b6020830152565b60088054901c60ff1661654d57619df361010061ff00196008541617600855565b619e2a619dfe61653e565b619e06618534565b8152617a696020820152619e18618557565b6040820152619e2561858a565b61b046565b619e5b619e3561653e565b619e3d6185ad565b815260016020820152619e4e6185d2565b6040820152619e25618608565b619e8e619e6661653e565b619e6e61862d565b815262aa36a76020820152619e81618652565b6040820152619e256186b3565b619ec0619e9961653e565b619ea16186d8565b81526142686020820152619eb36186fd565b6040820152619e25618743565b619ef3619ecb61653e565b619ed3618768565b815262088bb06020820152619ee661878b565b6040820152619e256187c6565b619f24619efe61653e565b619f066187e9565b8152600a6020820152619f1761880f565b6040820152619e2561884a565b619f57619f2f61653e565b619f37618870565b815262aa37dc6020820152619f4a61889e565b6040820152619e25616b29565b619f89619f6261653e565b619f6a6188d9565b815261a4b16020820152619f7c618903565b6040820152619e2561893e565b619fbc619f9461653e565b619f9c618968565b815262066eee6020820152619faf61899a565b6040820152619e256189e4565b619fee619fc761653e565b619fcf618a16565b815261a4ba6020820152619fe1618a41565b6040820152619e25618a7c565b61a01f619ff961653e565b61a001618aa7565b81526089602082015261a012618acc565b6040820152619e25618b01565b61a05261a02a61653e565b61a032618b26565b815262013882602082015261a045618b50565b6040820152619e25618b97565b61a08461a05d61653e565b61a065618bc1565b815261a86a602082015261a077618be8565b6040820152619e25618c31565b61a0b661a08f61653e565b61a097618c58565b815261a869602082015261a0a9618c84565b6040820152619e25618cd2565b61a0e761a0c161653e565b61a0c9618cfe565b81526038602082015261a0da618d2b565b6040820152619e25618d70565b61a11861a0f261653e565b61a0fa618d9d565b81526061602082015261a10b618dd2565b6040820152619e25618e1d565b61a14961a12361653e565b61a12b618e52565b81526064602082015261a13c618e7c565b6040820152619e25618eb7565b61a17b61a15461653e565b61a15c618ee1565b8152610504602082015261a16e618f07565b6040820152619e25618f42565b61a1ad61a18661653e565b61a18e618f68565b8152610505602082015261a1a0618f8f565b6040820152619e25618fdd565b61a1df61a1b861653e565b61a1c0619004565b8152610507602082015261a1d261902a565b6040820152619e25619072565b61a21261a1ea61653e565b61a1f2619098565b815262014a34602082015261a2056190c2565b6040820152619e256190f8565b61a24461a21d61653e565b61a225619122565b8152612105602082015261a237619144565b6040820152619e2561917a565b61a27861a24f61653e565b61a25761919c565b8152630a0c71fd602082015261a26b6191c7565b6040820152619e256191fd565b61a2ab61a28361653e565b61a28b619228565b815262013e31602082015261a29e61924b565b6040820152619e2561927d565b61a2dc61a2b661653e565b61a2be6192a0565b815260fa602082015261a2cf6192ca565b6040820152619e25619305565b61a30e61a2e761653e565b61a2ef61932f565b8152610fa2602082015261a301619361565b6040820152619e256193a9565b61a33f61a31961653e565b61a3216193db565b815260fc602082015261a332619400565b6040820152619e25619432565b61a37161a34a61653e565b61a352619457565b81526109da602082015261a364619484565b6040820152619e256194bf565b61a3a461a37c61653e565b61a3846194ec565b8152620138d4602082015261a397619522565b6040820152619e2561955d565b61a3d561a3af61653e565b61a3b7619593565b8152600e602082015261a3c86195b6565b6040820152619e25619603565b61a40661a3e061653e565b61a3e8619626565b81526072602082015261a3f9619651565b6040820152619e256196a0565b61a43861a41161653e565b61a4196196cb565b815261868b602082015261a42b6196ed565b6040820152619e25619720565b61a46a61a44361653e565b61a44b619742565b8152610397602082015261a45d61976c565b6040820152619e256197a7565b61a49d61a47561653e565b61a47d6197d1565b81526276adf1602082015261a4906197f3565b6040820152619e25619826565b61a4d161a4a861653e565b61a4b0619848565b8152633b9ac9ff602082015261a4c4619872565b6040820152619e256198ad565b61a50361a4dc61653e565b61a4e46198d7565b8152611a95602082015261a4f66198f9565b6040820152619e2561992d565b61a53561a50e61653e565b61a51661994f565b8152611a96602082015261a5286198f9565b6040820152619e25619979565b61a56761a54061653e565b61a5486199a3565b81526106d6602082015261a55a6199c6565b6040820152619e256199fc565b61a59961a57261653e565b61a57a619a1f565b81526106cc602082015261a58c619a4a565b6040820152619e25619a85565b61a5cb61a5a461653e565b61a5ac619ab0565b8152610270602082015261a5be619ad4565b6040820152619e25619b1e565b61a5fd61a5d661653e565b61a5de619b42565b8152610271602082015261a5f0619ad4565b6040820152619e25619b6e565b61a62f61a60861653e565b61a610619b9a565b8152610123602082015261a622619bbf565b6040820152619e25619bfa565b61a66161a63a61653e565b61a642619c1f565b815261116c602082015261a654619c4c565b6040820152619e25619c87565b61a69261a66c61653e565b61a674619cb4565b81526082602082015261a685619cda565b6040820152619e25619d15565b61654d61a69d61653e565b61a6a5619d3b565b8152610515602082015261a6b7619d69565b6040820152619e25619da4565b61a6cc617fda565b5060c061a6d7617fda565b918051835260408101516040840152606081015160608401526080810151608084015261a70760a0820151618167565b60a0840152015160c082015290565b9061a7208261655e565b61a72d604051918261651d565b828152809261a73e601f199161655e565b0190602036910137565b602081511161a7b85780516020036020811161690657602091828061a7aa61a770829561a716565b938260405193849281840199888b9951918291018a5e8401908282015f8152815193849201905e01015f815203601f19810183528261651d565b80510101031261067b575190565b60405162461bcd60e51b815260206004820152603760248201527f537464436865617473205f6279746573546f55696e74286279746573293a20426044820152763cba32b9903632b733ba341032bc31b2b2b2399019991760491b6064820152608490fd5b5f198131101561a98657479080315f51602061cf275f395f51905f523b1561067b5760405163c88a5e6d60e01b8152306004820152600160248201525f92908381604481835f51602061cf275f395f51905f525af180156163a15761a971575b508280808060016001600160a01b0386165af19361a89961786c565b505f51602061cf275f395f51905f523b15611eee578361a8ce916040518093819263c88a5e6d60e01b83523060048401616b57565b0381835f51602061cf275f395f51905f525af1801561209f5790849161a95c575b50505f51602061cf275f395f51905f523b156114075760405163c88a5e6d60e01b81529183918391829161a927919060048401616b57565b0381835f51602061cf275f395f51905f525af180156106875761a94957505090565b61a95482809261651d565b61028d575090565b8161a9669161651d565b61140757825f61a8ef565b61a97e9193505f9061651d565b5f915f61a87d565b60405162461bcd60e51b815260206004820152605e60248201527f537464436865617473205f697350617961626c652861646472657373293a204260448201527f616c616e636520657175616c73206d61782075696e743235362c20736f20697460648201527f2063616e6e6f74207265636569766520616e79206d6f72652066756e64730000608482015260a490fd5b600e54600160401b81101561649b576001810180600e558110156173c557600e5f527fbb7b4a454dc3493923482f07822329ed19e8244eff582cc204f8554c3620c3fd0155565b60209291908391805192839101825e019081520190565b604091949392606082019560018060a01b0316825260208201520152565b601154600f546010545f9493926001600160a01b03169160e01b61aab7600d61b171565b90835f52600d60205260405f209063ffffffff60e01b1690815f5260205260405f20604051602081019061aaf0816184f988888661aa5e565b5190205f5260205260ff600360405f200154161561af14575b835f52600d60205260405f20905f526020526184f961ab3760405f209360405192839160208301958661aa5e565b5190205f5260205260405f20600181015492600282015461ab5881866168f9565b61ae06575b82549060405195630667f9d760e41b87526020878061ab80868a60048401616b57565b03815f51602061cf275f395f51905f525afa9687156163a1575f9761add2575b506001908201610100031b5f1901811b198616915f51602061cf275f395f51905f523b1561067b576040516370ca10bb60e01b8152925f928492839261abef9288901b1790896004850161aa75565b0381835f51602061cf275f395f51905f525af180156163a15761adbd575b5061ac18600d61b231565b91901591821561adb2575b505061ace6575050601180546001600160a01b031916905550600f805463ffffffff19169055600e80545f8255919250600d91908161acc4575b50505f600382015560068101805460ff19169055600701805461ac7f906167ea565b908161ac89575050565b81601f5f931160011461ac9a575055565b8183526020832061acb791601f0160051c8419019060010161af24565b8082528160208120915555565b5f5260205f205f5b82811061acd9575061ac5d565b5f8282015560010161accc565b8492935054905f51602061cf275f395f51905f523b156114075761ad1e60405194859384936370ca10bb60e01b85526004850161aa75565b0381835f51602061cf275f395f51905f525af180156106875761ad9d575b60405162461bcd60e51b815260206004820152603360248201527f73746453746f726167652066696e642853746453746f72616765293a204661696044820152723632b2103a37903bb934ba32903b30b63ab29760691b6064820152608490fd5b61ada882809261651d565b61028d578061ad3c565b141590505f8061ac23565b61adca9196505f9061651d565b5f945f61ac0d565b9096506020813d60201161adfe575b8161adee6020938361651d565b8101031261067b5751958161aba0565b3d915061ade1565b61ae1081866168f9565b6101000361010081116169065761ae26906173d9565b60405163348051d760e11b8152600481018290525f816024815f51602061cf275f395f51905f525afa9182156163a15761aeee606a61aef5946020945f9161aefa575b506040519485917f73746453746f726167652066696e642853746453746f72616765293a20506163828401527f6b656420736c6f742e2057652063616e2774206669742076616c756520677265604084015269030ba32b9103a3430b7160b51b60608401528051918291018484015e81015f838201520301601f19810184528361651d565b8410617c34565b61ab5d565b61af0e91503d805f833e611420818361651d565b5f61ae69565b61af1e600d61b8bd565b5061ab09565b5f5b82811061af3257505050565b5f8282015560010161af26565b91909182516001600160401b03811161649b5761af5c82546167ea565b601f811161b003575b506020601f821160011461afa557819061af969394955f9261af9a575b50508160011b915f199060031b1c19161790565b9055565b015190505f8061af82565b601f19821690835f52805f20915f5b81811061afeb5750958360019596971061afd3575b505050811b019055565b01515f1960f88460031b161c191690555f808061afc9565b9192602060018192868b01518155019401920161afb4565b8181111561af655761b03890835f5260205f2090601f840160051c906020851061b03e575b601f82910160051c03910161af24565b5f61af65565b5f915061b028565b91906040810180519161b05885617bf6565b948351956001600160401b03871161649b5761b07481546167ea565b601f811161b137575b50602096601f811160011461b0d2578061b0b29161b0c4969798995f9161b0c7575b508160011b915f199060031b1c19161790565b90555b61b0bd61668c565b845261b6e1565b52565b90508801515f61b09f565b601f198116825f52885f20905f5b81811061b11f57509061b0c49697989983600194931061b107575b5050811b01905561b0b5565b8901515f1960f88460031b161c191690555f8061b0fb565b888b0151835560209a8b019a6001909301920161b0e0565b8781111561b07d5761b16b90825f5260205f2090601f8a0160051c9060208b1061b03e57601f82910160051c03910161af24565b5f61b07d565b600781019061b18082546167ea565b61b21d57600191500190604051808360208295549384815201905f5260205f20925f5b81811061b20457505061b1b89250038361651d565b81518060051b90808204602014901517156169065761b1d69061a716565b5f5b835181101561b1ff578061b1ee60019286618520565b5160208260051b850101520161b1d8565b509150565b845483526001948501948794506020909301920161b1a3565b506167646121539160405192838092616822565b905f806020600285015460e01b61b281602461b24c8861b171565b6040519485918183019563ffffffff60e01b1686528051918291018484015e810186838201520301601f19810184528361651d565b60048601549151916001600160a01b03165afa600361b29e61786c565b930154600581901b93906001600160fb1b03811603616906575f938151602081115f1461b31d57506020905b5f925b82841061b2dc57505050509190565b9091929560ff60f81b61b2f861b2f289866168f9565b846173b4565b5116908760031b9188830460081489151715616906576001921c17960192919061b2cd565b9061b2ca565b1561b32a57565b60405162461bcd60e51b815260206004820152604d60248201525f51602061cf075f395f51905f5260448201527f617461293a20436861696e20616c6961732063616e6e6f74206265207468652060648201526c32b6b83a3c9039ba3934b7339760991b608482015260a490fd5b1561b39f57565b60405162461bcd60e51b815260206004820152603b60248201525f51602061cf075f395f51905f5260448201527f617461293a20436861696e2049442063616e6e6f7420626520302e00000000006064820152608490fd5b61ac7f81546167ea565b9181519283516001600160401b03811161649b5761b41f82546167ea565b601f811161b6a7575b50602094601f821160011461b6465761b45a9293949582915f9261af9a5750508160011b915f199060031b1c19161790565b81555b602083015160018201556002810160408401518051906001600160401b03821161649b5761b48b83546167ea565b601f811161b60c575b50602090601f831160011461b5a45782606095936003959361b4ca935f9261af9a5750508160011b915f199060031b1c19161790565b90555b019201519182516001600160401b03811161649b5761b4ec82546167ea565b601f811161b56a575b506020601f821160011461b52557819061af969394955f9261af9a5750508160011b915f199060031b1c19161790565b601f19821690835f52805f20915f5b81811061b5525750958360019596971061afd357505050811b019055565b9192602060018192868b01518155019401920161b534565b8181111561b4f55761b59e90835f5260205f2090601f840160051c906020851061b03e57601f82910160051c03910161af24565b5f61b4f5565b90601f19831691845f52815f20925f5b81811061b5f4575092600192859260609896600398961061b5dd575b505050811b01905561b4cd565b01515f1983881b60f8161c191690555f808061b5d0565b9293602060018192878601518155019501930161b5b4565b8281111561b4945761b64090845f5260205f2090601f850160051c906020861061b03e57601f82910160051c03910161af24565b5f61b494565b601f19821695835f52805f20915f5b88811061b68f5750836001959697981061b677575b505050811b01815561b45d565b01515f1960f88460031b161c191690555f808061b66a565b9192602060018192868501518155019401920161b655565b8181111561b4285761b6db90835f5260205f2090601f840160051c906020851061b03e57601f82910160051c03910161af24565b5f61b428565b61b6ed8151151561b323565b602082019161b6fe8351151561b398565b61b706619dd2565b61b72161b71c84515f52600b60205260405f2090565b6168a3565b92835191821592831561b8a3575b50815160405163348051d760e11b81526004810191909152905f8280602481015b03815f51602061cf275f395f51905f525afa801561b89e5761b7d261b8759561267061b80c9361654d9a61b866975f9261b87a575b5061b7f061b7fe9161b7cc60405197889561b7cc60208801602f905f51602061cf075f395f51905f5281526e030ba30949d1021b430b4b71024a21608d1b60208201520190565b90616767565b711030b63932b0b23c903ab9b2b210313c901160711b815260120190565b61111760f11b815260020190565b03601f19810184528361651d565b61b83261b82d600161b81d88617c15565b01545f52600b60205260405f2090565b61b3f7565b805190604084519101519061b84561654f565b9283526020830152856040830152606082015261b86185617c15565b61b401565b515f52600b60205260405f2090565b61af3f565b61b7fe91925061b89661b7f0913d805f833e611420818361651d565b92915061b785565b6163a1565b61b75091935060208601208451602086012014929061b72f565b6004810154600282015460038301546001600160a01b03909216925f929160e01b61b8e78261b171565b9160018060a01b0386165f528060205260405f2063ffffffff60e01b83165f5260205260405f20604051602081019061b925816184f989898661aa5e565b5190205f5260205260ff600360405f2001541661c15c575f51602061cf275f395f51905f523b1561067b5760405163266cf10960e01b81525f81600481835f51602061cf275f395f51905f525af180156163a15761c147575b5061b9888161b231565b90506040516365bc948160e01b815287600482015286816024815f51602061cf275f395f51905f525afa90811561c13c57879161c0d0575b5080518061ba3257608460405162461bcd60e51b815260206004820152604060248201527f73746453746f726167652066696e642853746453746f72616765293a204e6f2060448201527f73746f726167652075736520646574656374656420666f72207461726765742e6064820152fd5b9061ba3f61ba6a92618214565b90602061ba4c8383618520565b51604051630667f9d760e41b81529485918291908e60048401616b57565b03815f51602061cf275f395f51905f525afa92831561c0c557899361c092575b50821561c04e575b61ba9c8282618520565b5160018060a01b0360048701541690604051630667f9d760e41b81526020818061baca858760048401616b57565b03815f51602061cf275f395f51905f525afa90811561c043578c9161c012575b5061baf48861b231565b91909382155f1461c00b575f19905b5f51602061cf275f395f51905f523b1561bff257848f9161bb3860405194859384936370ca10bb60e01b85526004850161aa75565b0381835f51602061cf275f395f51905f525af1801561bf6657908e9161bff6575b505061bb648961b231565b60048b0154909491506001600160a01b03165f51602061cf275f395f51905f523b1561bff257908e9161bbab60405194859384936370ca10bb60e01b85526004850161aa75565b0381835f51602061cf275f395f51905f525af1801561bfe757908d9161bfce575b50508261bfc3575b50501561bfb5578987898b968c9660ff60068b01541661be26575b6001898901610100031b5f1901881b16871c810361be0f57506080600396959361bc8195936184f961bc4d7f9c9555b1e3102e3cf48f427d79cb678f5d9bd1ed0ad574389461e255f95170ed9560405192839160208301958661aa5e565b51902061bc5a8686618520565b519060405192835263ffffffff60e01b8d16602084015260408301526060820152a1618520565b51906040519161bc90836164e7565b8252602080830194855260408084019283526001606085019081526001600160a01b038d165f9081528884528290206001600160e01b03198a168d528352818c20915190969281019061bce8816184f98e8e8661aa5e565b5190208b5260205260408a2092518355516001830155516002820155019051151560ff8019835416911617905560018060a01b0386165f528060205260405f2063ffffffff60e01b8316865260205260408520604051602081019061bd52816184f989898661aa5e565b519020865260205260ff6003604087200154161561bdb25760409560018060a01b03165f52602052845f209063ffffffff60e01b1684526020526184f961bda685852093865192839160208301958661aa5e565b51902082526020522090565b60405162461bcd60e51b815260206004820152602f60248201527f73746453746f726167652066696e642853746453746f72616765293a20536c6f60448201526e3a143994903737ba103337bab7321760891b6064820152608490fd5b9650505050915061ba3f61ba6a915b929192618214565b97509250505061be68935061be3b8383618520565b519460208660018060a01b0360048a0154166040519788928392630667f9d760e41b845260048401616b57565b03815f51602061cf275f395f51905f525afa94851561bfaa578b9561bf77575b5061be93868861c1ac565b95909661bea0818a61c276565b60048b015490939192906001600160a01b03165f51602061cf275f395f51905f523b1561bf7357908f9161bee860405194859384936370ca10bb60e01b85526004850161aa75565b0381835f51602061cf275f395f51905f525af1801561bf6657928f95928f8f95938f979461bf3c575b50508a61bf34575b50979861bbef57509650505050915061ba3f61ba6a9161be1e565b99505f61bf19565b90939650839194975061bf5092955061651d565b61bf6257928a928c928f958f5f61bf11565b8c80fd5b8e604051903d90823e3d90fd5b8f80fd5b9094506020813d821161bfa2575b8161bf926020938361651d565b8101031261067b5751935f61be88565b3d915061bf85565b6040513d8d823e3d90fd5b915061ba3f61ba6a9161be1e565b141590505f8061bbd4565b8161bfd89161651d565b61bfe3578b5f61bbcc565b8b80fd5b6040513d8f823e3d90fd5b8e80fd5b8161c0009161651d565b61bf62578c5f61bb59565b8d9061bb03565b90506020813d821161c03b575b8161c02c6020938361651d565b8101031261067b57515f61baea565b3d915061c01f565b6040513d8e823e3d90fd5b7f080fc4a96620c4462e705b23f346413fe3796bb63c6f8d8591baec0e231577a561c0798383618520565b518b61c08a60405192839283616b57565b0390a161ba92565b9092506020813d821161c0bd575b8161c0ad6020938361651d565b8101031261067b5751915f61ba8a565b3d915061c0a0565b6040513d8b823e3d90fd5b90503d8088833e61c0e1818361651d565b810160408282031261c1385781516001600160401b03811161c134578161c109918401616c21565b916020810151906001600160401b03821161c1305761c129929101616c21565b505f61b9c0565b8980fd5b8880fd5b8780fd5b6040513d89823e3d90fd5b61c1549195505f9061651d565b5f935f61b97e565b919350919360018060a01b03165f5260205260405f209063ffffffff60e01b165f526020526184f961c19d60405f209360405192839160208301958661aa5e565b5190205f5260205260405f2090565b91905f5b610100811061c1c357505090505f905f90565b8060ff0360ff8111616906576004850154600190911b906001600160a01b03165f51602061cf275f395f51905f523b1561067b57835f9161c21860405194859384936370ca10bb60e01b85526004850161aa75565b0381835f51602061cf275f395f51905f525af180156163a15761c266575b5061c2408461b231565b8161c25c575b5061c2535760010161c1b0565b92505060019190565b905015155f61c246565b5f61c2709161651d565b5f61c236565b91905f5b610100811061c28d57505090505f905f90565b60048401546001821b906001600160a01b03165f51602061cf275f395f51905f523b1561067b57835f9161c2d560405194859384936370ca10bb60e01b85526004850161aa75565b0381835f51602061cf275f395f51905f525af180156163a15761c31a575b5061c2fd8461b231565b8161c310575b5061c2535760010161c27a565b905015155f61c303565b5f61c3249161651d565b5f61c2f356fe60808060405269021e19e0c9bab2400000600155305f525f60205269021e19e0c9bab240000060405f20556101c590816100378239f3fe6080806040526004361015610012575f80fd5b5f3560e01c90816318160ddd1461012a5750806355596477146100ff578063646ea56d146100d857806370a08231146100a15763a9b2e28a14610053575f80fd5b604036600319011261009d57610067610144565b6024356001600160a01b0381169081900361009d5761009b91610094906001600160a01b0316331461015a565b321461015a565b005b5f80fd5b3461009d57602036600319011261009d576001600160a01b036100c2610144565b165f525f602052602060405f2054604051908152f35b602036600319011261009d5761009b6001600160a01b036100f7610144565b16331461015a565b602036600319011261009d5761009b6001600160a01b0361011e610144565b1661009481331461015a565b3461009d575f36600319011261009d576020906001548152f35b600435906001600160a01b038216820361009d57565b1561016157565b60405162461bcd60e51b8152602060048201526006602482015265217072616e6b60d01b6044820152606490fdfea2646970667358221220d8b7efabc949b5243edeee5fc571978d12c2761cbdffef438acc5e32d834155b64736f6c63430008210033608060408181527fada5013122d395ba3c54772283fb069b10426056ef8ca54750cb9bb552a59e7d805460016001600160a01b031991821681179092557fcc69885fda6bcc1a4ace058b4a62bf5e179ea78fd58a1ccd71c22cc9b688792f8290557fabbb5caa7dda850e60932de0934eb1f9d0f59695050f761dc64e443e5030a56980543090831681179091557f101e368776582e57ab3d116ffe2517c0a585cd5b23174b01e275c2d8329c3d83805490921681179091555f908152602091909152206002905560d190816100d28239f3fe60808060405260043610156011575f80fd5b5f3560e01c9081636352211e14606c57506370a0823114602f575f80fd5b3460685760203660031901126068576004356001600160a01b038116908190036068575f526001602052602060405f2054604051908152f35b5f80fd5b3460685760203660031901126068576004355f90815260208181526040909120546001600160a01b0316825290f3fea2646970667358221220030a960c495b64223ccb62746a4c0b894bd3e0ac1602bf1a4f0162611ca189ad64736f6c634300082100336080806040523460155761068b908161001a8239f35b5f80fdfe60806040526004361015610011575f80fd5b5f5f3560e01c806317cc73a01461030a57806395b9a383146100ca5763de4a5dcd1461003b575f80fd5b346100b95760203660031901126100b9578061005d61005861038f565b610432565b5f5160206106365f395f51905f523b156100c757604051632631f2b160e11b8152901515600482015281816024815f5160206106365f395f51905f525afa80156100bc576100a85750f35b816100b2916103a5565b6100b95780f35b80fd5b6040513d84823e3d90fd5b50fd5b50346100b95760403660031901126100b9576100e461038f565b6024356001600160a01b038116919082900361030657803b156102815782918280604051602081019063fe575a8760e01b82528460248201526024815261012c6044826103a5565b5190855afa9161013a6103db565b9215928315610264575b505f5160206106365f395f51905f523b1561025f57604051632631f2b160e11b8152921515600484015283836024815f5160206106365f395f51905f525afa918215610254578492610237575b8293506040516020810191630723eb0360e51b83526024820152602481526101ba6044826103a5565b51915afa6101c66103db565b901590811561021c575b505f5160206106365f395f51905f523b156100c757604051632631f2b160e11b8152901515600482015281816024815f5160206106365f395f51905f525afa80156100bc576100a85750f35b61023091506020808251830101910161041a565b155f6101d0565b91909281610244916103a5565b61025057818391610191565b5050fd5b6040513d86823e3d90fd5b505050fd5b6102799193506020808251830101910161041a565b15915f610144565b60405162461bcd60e51b815260206004820152605160248201527f53746443686561747320617373756d654e6f74426c61636b6c6973746564286160448201527f6464726573732c61646472657373293a20546f6b656e2061646472657373206960648201527039903737ba10309031b7b73a3930b1ba1760791b608482015260a490fd5b8280fd5b503461038b57602036600319011261038b5761032761005861038f565b155f5160206106365f395f51905f523b1561038b5760405190632631f2b160e11b825260048201525f816024815f5160206106365f395f51905f525afa801561038057610372575080f35b61037e91505f906103a5565b005b6040513d5f823e3d90fd5b5f80fd5b600435906001600160a01b038216820361038b57565b90601f8019910116810190811067ffffffffffffffff8211176103c757604052565b634e487b7160e01b5f52604160045260245ffd5b3d15610415573d9067ffffffffffffffff82116103c7576040519161040a601f8201601f1916602001846103a5565b82523d5f602084013e565b606090565b9081602091031261038b5751801515810361038b5790565b5f19813110156105a457479080315f5160206106365f395f51905f523b1561038b5760405163c88a5e6d60e01b8152306004820152600160248201525f92908381604481835f5160206106365f395f51905f525af180156103805761058f575b508280808060016001600160a01b0386165af1936104ae6103db565b505f5160206106365f395f51905f523b1561058b5760405163c88a5e6d60e01b815230600482015260248101919091528381604481835f5160206106365f395f51905f525af1801561025457908491610576575b50505f5160206106365f395f51905f523b156103065760405163c88a5e6d60e01b81526001600160a01b0391909116600482015260248101919091528181604481835f5160206106365f395f51905f525af180156100bc5761056357505090565b61056e8280926103a5565b6100b9575090565b81610580916103a5565b61030657825f610502565b8380fd5b61059c9193505f906103a5565b5f915f610492565b60405162461bcd60e51b815260206004820152605e60248201527f537464436865617473205f697350617961626c652861646472657373293a204260448201527f616c616e636520657175616c73206d61782075696e743235362c20736f20697460648201527f2063616e6e6f74207265636569766520616e79206d6f72652066756e64730000608482015260a490fdfe0000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da26469706673582212204fd6b7d9aef6ec582a033ef31a078d753333b5c6736ce20d592a7c098d73249b64736f6c63430008210033608080604052346013576040908160188239f35b5f80fdfe36156008575f80fd5b00fea2646970667358221220f0848357e1138fd6ce5cf47151b43a3c0f4e0f7caf5505b5df99d57a8632f7b464736f6c634300082100336080604081815269021e19e0c9bab24000007fa6eef7e35abe7026729641147f7915573c7e97b47efa546f5f6e3230263bcb49819055305f9081527fad3228b676f7d3cd4284a5443f17f1962b36e491b30a40b2405849e597ba5fb5602052919091205560d1908161006f8239f3fe60808060405260043610156011575f80fd5b5f3560e01c908162fdd58e14605a575063bd85b03914602e575f80fd5b3460565760203660031901126056576004355f526001602052602060405f2054604051908152f35b5f80fd5b3460565760403660031901126056576004356001600160a01b03811691908290036056576020916024355f525f835260405f20905f52825260405f20548152f3fea2646970667358221220e94c6b630765b315bbfe65451892e75eed923d77b697cf9294647ac927515ff764736f6c63430008210033537464436861696e7320736574436861696e28737472696e672c436861696e440000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da26469706673582212200ad9bc8a0f17675e230726e0e5eb43ee0bc52e22d59af76eec5b049750752d2d64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> StdCheatsTest:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[StdCheatsTest]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, StdCheatsTest, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[StdCheatsTest]]:
        return cls._deploy(request_type, [], return_tx, StdCheatsTest, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#15)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#15)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#15)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#15)
        """
        ...

    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#15)
        """
        return self._execute(self.chain, request_type, "0a9254e4", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_Skip(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#19)
        """
        ...

    @overload
    def test_Skip(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#19)
        """
        ...

    @overload
    def test_Skip(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#19)
        """
        ...

    @overload
    def test_Skip(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#19)
        """
        ...

    def test_Skip(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#19)
        """
        return self._execute(self.chain, request_type, "c54b6369", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_Rewind(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#25)
        """
        ...

    @overload
    def test_Rewind(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#25)
        """
        ...

    @overload
    def test_Rewind(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#25)
        """
        ...

    @overload
    def test_Rewind(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#25)
        """
        ...

    def test_Rewind(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#25)
        """
        return self._execute(self.chain, request_type, "d92b84b0", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_Hoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#31)
        """
        ...

    @overload
    def test_Hoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#31)
        """
        ...

    @overload
    def test_Hoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#31)
        """
        ...

    @overload
    def test_Hoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#31)
        """
        ...

    def test_Hoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#31)
        """
        return self._execute(self.chain, request_type, "bfc420f1", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_HoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#36)
        """
        ...

    @overload
    def test_HoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#36)
        """
        ...

    @overload
    def test_HoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#36)
        """
        ...

    @overload
    def test_HoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#36)
        """
        ...

    def test_HoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#36)
        """
        return self._execute(self.chain, request_type, "6dc2878a", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_HoaxDifferentAddresses(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#41)
        """
        ...

    @overload
    def test_HoaxDifferentAddresses(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#41)
        """
        ...

    @overload
    def test_HoaxDifferentAddresses(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#41)
        """
        ...

    @overload
    def test_HoaxDifferentAddresses(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#41)
        """
        ...

    def test_HoaxDifferentAddresses(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#41)
        """
        return self._execute(self.chain, request_type, "cfcd8c45", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StartHoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#46)
        """
        ...

    @overload
    def test_StartHoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#46)
        """
        ...

    @overload
    def test_StartHoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#46)
        """
        ...

    @overload
    def test_StartHoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#46)
        """
        ...

    def test_StartHoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#46)
        """
        return self._execute(self.chain, request_type, "1d4e5c12", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StartHoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#54)
        """
        ...

    @overload
    def test_StartHoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#54)
        """
        ...

    @overload
    def test_StartHoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#54)
        """
        ...

    @overload
    def test_StartHoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#54)
        """
        ...

    def test_StartHoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#54)
        """
        return self._execute(self.chain, request_type, "58e8257b", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_ChangePrankMsgSender(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#62)
        """
        ...

    @overload
    def test_ChangePrankMsgSender(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#62)
        """
        ...

    @overload
    def test_ChangePrankMsgSender(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#62)
        """
        ...

    @overload
    def test_ChangePrankMsgSender(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#62)
        """
        ...

    def test_ChangePrankMsgSender(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#62)
        """
        return self._execute(self.chain, request_type, "78d56a69", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_ChangePrankMsgSenderAndTxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#72)
        """
        ...

    @overload
    def test_ChangePrankMsgSenderAndTxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#72)
        """
        ...

    @overload
    def test_ChangePrankMsgSenderAndTxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#72)
        """
        ...

    @overload
    def test_ChangePrankMsgSenderAndTxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#72)
        """
        ...

    def test_ChangePrankMsgSenderAndTxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#72)
        """
        return self._execute(self.chain, request_type, "66a38888", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_MakeAccountEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#82)
        """
        ...

    @overload
    def test_MakeAccountEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#82)
        """
        ...

    @overload
    def test_MakeAccountEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#82)
        """
        ...

    @overload
    def test_MakeAccountEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#82)
        """
        ...

    def test_MakeAccountEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#82)
        """
        return self._execute(self.chain, request_type, "00abe409", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_MakeAddrEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#89)
        """
        ...

    @overload
    def test_MakeAddrEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#89)
        """
        ...

    @overload
    def test_MakeAddrEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#89)
        """
        ...

    @overload
    def test_MakeAddrEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#89)
        """
        ...

    def test_MakeAddrEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#89)
        """
        return self._execute(self.chain, request_type, "9d44b78a", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_MakeAddrSigning(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#94)
        """
        ...

    @overload
    def test_MakeAddrSigning(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#94)
        """
        ...

    @overload
    def test_MakeAddrSigning(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#94)
        """
        ...

    @overload
    def test_MakeAddrSigning(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#94)
        """
        ...

    def test_MakeAddrSigning(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#94)
        """
        return self._execute(self.chain, request_type, "ae428267", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_Deal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#102)
        """
        ...

    @overload
    def test_Deal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#102)
        """
        ...

    @overload
    def test_Deal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#102)
        """
        ...

    @overload
    def test_Deal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#102)
        """
        ...

    def test_Deal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#102)
        """
        return self._execute(self.chain, request_type, "058aeb3e", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DealToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#107)
        """
        ...

    @overload
    def test_DealToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#107)
        """
        ...

    @overload
    def test_DealToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#107)
        """
        ...

    @overload
    def test_DealToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#107)
        """
        ...

    def test_DealToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#107)
        """
        return self._execute(self.chain, request_type, "9755843b", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DealTokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#114)
        """
        ...

    @overload
    def test_DealTokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#114)
        """
        ...

    @overload
    def test_DealTokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#114)
        """
        ...

    @overload
    def test_DealTokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#114)
        """
        ...

    def test_DealTokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#114)
        """
        return self._execute(self.chain, request_type, "59ff1d87", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DealERC1155Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#125)
        """
        ...

    @overload
    def test_DealERC1155Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#125)
        """
        ...

    @overload
    def test_DealERC1155Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#125)
        """
        ...

    @overload
    def test_DealERC1155Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#125)
        """
        ...

    def test_DealERC1155Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#125)
        """
        return self._execute(self.chain, request_type, "bfac85a4", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DealERC1155TokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#132)
        """
        ...

    @overload
    def test_DealERC1155TokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#132)
        """
        ...

    @overload
    def test_DealERC1155TokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#132)
        """
        ...

    @overload
    def test_DealERC1155TokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#132)
        """
        ...

    def test_DealERC1155TokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#132)
        """
        return self._execute(self.chain, request_type, "f11dfb60", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DealERC721Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#143)
        """
        ...

    @overload
    def test_DealERC721Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#143)
        """
        ...

    @overload
    def test_DealERC721Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#143)
        """
        ...

    @overload
    def test_DealERC721Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#143)
        """
        ...

    def test_DealERC721Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#143)
        """
        return self._execute(self.chain, request_type, "d31d7c1d", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DeployCode(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#154)
        """
        ...

    @overload
    def test_DeployCode(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#154)
        """
        ...

    @overload
    def test_DeployCode(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#154)
        """
        ...

    @overload
    def test_DeployCode(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#154)
        """
        ...

    def test_DeployCode(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#154)
        """
        return self._execute(self.chain, request_type, "0ad2b4c8", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DestroyAccount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#159)
        """
        ...

    @overload
    def test_DestroyAccount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#159)
        """
        ...

    @overload
    def test_DestroyAccount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#159)
        """
        ...

    @overload
    def test_DestroyAccount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#159)
        """
        ...

    def test_DestroyAccount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#159)
        """
        return self._execute(self.chain, request_type, "4440c545", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DeployCodeNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#186)
        """
        ...

    @overload
    def test_DeployCodeNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#186)
        """
        ...

    @overload
    def test_DeployCodeNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#186)
        """
        ...

    @overload
    def test_DeployCodeNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#186)
        """
        ...

    def test_DeployCodeNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#186)
        """
        return self._execute(self.chain, request_type, "f930b628", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DeployCodeVal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#191)
        """
        ...

    @overload
    def test_DeployCodeVal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#191)
        """
        ...

    @overload
    def test_DeployCodeVal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#191)
        """
        ...

    @overload
    def test_DeployCodeVal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#191)
        """
        ...

    def test_DeployCodeVal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#191)
        """
        return self._execute(self.chain, request_type, "bb11ac10", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DeployCodeValNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#197)
        """
        ...

    @overload
    def test_DeployCodeValNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#197)
        """
        ...

    @overload
    def test_DeployCodeValNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#197)
        """
        ...

    @overload
    def test_DeployCodeValNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#197)
        """
        ...

    def test_DeployCodeValNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#197)
        """
        return self._execute(self.chain, request_type, "413cfcb1", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deployCodeHelper(self, what: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#204)

        Args:
            what: string
        """
        ...

    @overload
    def deployCodeHelper(self, what: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#204)

        Args:
            what: string
        """
        ...

    @overload
    def deployCodeHelper(self, what: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#204)

        Args:
            what: string
        """
        ...

    @overload
    def deployCodeHelper(self, what: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#204)

        Args:
            what: string
        """
        ...

    def deployCodeHelper(self, what: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#204)

        Args:
            what: string
        """
        return self._execute(self.chain, request_type, "4af967d1", [what], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_RevertIf_DeployCodeFail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#208)
        """
        ...

    @overload
    def test_RevertIf_DeployCodeFail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#208)
        """
        ...

    @overload
    def test_RevertIf_DeployCodeFail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#208)
        """
        ...

    @overload
    def test_RevertIf_DeployCodeFail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#208)
        """
        ...

    def test_RevertIf_DeployCodeFail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#208)
        """
        return self._execute(self.chain, request_type, "6954ee50", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DeriveRememberKey(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#230)
        """
        ...

    @overload
    def test_DeriveRememberKey(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#230)
        """
        ...

    @overload
    def test_DeriveRememberKey(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#230)
        """
        ...

    @overload
    def test_DeriveRememberKey(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#230)
        """
        ...

    def test_DeriveRememberKey(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#230)
        """
        return self._execute(self.chain, request_type, "2ac9eedb", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_BytesToUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#238)
        """
        ...

    @overload
    def test_BytesToUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#238)
        """
        ...

    @overload
    def test_BytesToUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#238)
        """
        ...

    @overload
    def test_BytesToUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#238)
        """
        ...

    def test_BytesToUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#238)
        """
        return self._execute(self.chain, request_type, "0d2bf636", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_ParseJsonTxDetail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#245)
        """
        ...

    @overload
    def test_ParseJsonTxDetail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#245)
        """
        ...

    @overload
    def test_ParseJsonTxDetail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#245)
        """
        ...

    @overload
    def test_ParseJsonTxDetail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#245)
        """
        ...

    def test_ParseJsonTxDetail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#245)
        """
        return self._execute(self.chain, request_type, "bd9fb259", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_ReadEIP1559Transaction(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#264)
        """
        ...

    @overload
    def test_ReadEIP1559Transaction(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#264)
        """
        ...

    @overload
    def test_ReadEIP1559Transaction(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#264)
        """
        ...

    @overload
    def test_ReadEIP1559Transaction(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#264)
        """
        ...

    def test_ReadEIP1559Transaction(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#264)
        """
        return self._execute(self.chain, request_type, "ae0ddbc8", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_ReadEIP1559Transactions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#272)
        """
        ...

    @overload
    def test_ReadEIP1559Transactions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#272)
        """
        ...

    @overload
    def test_ReadEIP1559Transactions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#272)
        """
        ...

    @overload
    def test_ReadEIP1559Transactions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#272)
        """
        ...

    def test_ReadEIP1559Transactions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#272)
        """
        return self._execute(self.chain, request_type, "cf99d3dd", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_ReadReceipt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#279)
        """
        ...

    @overload
    def test_ReadReceipt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#279)
        """
        ...

    @overload
    def test_ReadReceipt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#279)
        """
        ...

    @overload
    def test_ReadReceipt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#279)
        """
        ...

    def test_ReadReceipt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#279)
        """
        return self._execute(self.chain, request_type, "22b4de51", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_ReadReceipts(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#290)
        """
        ...

    @overload
    def test_ReadReceipts(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#290)
        """
        ...

    @overload
    def test_ReadReceipts(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#290)
        """
        ...

    @overload
    def test_ReadReceipts(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#290)
        """
        ...

    def test_ReadReceipts(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#290)
        """
        return self._execute(self.chain, request_type, "99c87c55", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_GasMeteringModifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#297)
        """
        ...

    @overload
    def test_GasMeteringModifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#297)
        """
        ...

    @overload
    def test_GasMeteringModifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#297)
        """
        ...

    @overload
    def test_GasMeteringModifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#297)
        """
        ...

    def test_GasMeteringModifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#297)
        """
        return self._execute(self.chain, request_type, "893329ac", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_AssumeAddressIsNot(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#337)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeAddressIsNot(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#337)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeAddressIsNot(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#337)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeAddressIsNot(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#337)

        Args:
            addr: address
        """
        ...

    def testFuzz_AssumeAddressIsNot(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#337)

        Args:
            addr: address
        """
        return self._execute(self.chain, request_type, "4a1297f8", [addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_AssumePayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#347)
        """
        ...

    @overload
    def test_AssumePayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#347)
        """
        ...

    @overload
    def test_AssumePayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#347)
        """
        ...

    @overload
    def test_AssumePayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#347)
        """
        ...

    def test_AssumePayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#347)
        """
        return self._execute(self.chain, request_type, "61266422", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_AssumeNotPayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#375)
        """
        ...

    @overload
    def test_AssumeNotPayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#375)
        """
        ...

    @overload
    def test_AssumeNotPayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#375)
        """
        ...

    @overload
    def test_AssumeNotPayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#375)
        """
        ...

    def test_AssumeNotPayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#375)
        """
        return self._execute(self.chain, request_type, "9bacb2a8", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_AssumeNotPrecompile(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#402)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotPrecompile(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#402)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotPrecompile(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#402)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotPrecompile(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#402)

        Args:
            addr: address
        """
        ...

    def testFuzz_AssumeNotPrecompile(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#402)

        Args:
            addr: address
        """
        return self._execute(self.chain, request_type, "9d624fa1", [addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_AssumeNotForgeAddress(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#410)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotForgeAddress(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#410)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotForgeAddress(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#410)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotForgeAddress(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#410)

        Args:
            addr: address
        """
        ...

    def testFuzz_AssumeNotForgeAddress(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#410)

        Args:
            addr: address
        """
        return self._execute(self.chain, request_type, "751ec69d", [addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_RevertIf_CannotDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#418)
        """
        ...

    @overload
    def test_RevertIf_CannotDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#418)
        """
        ...

    @overload
    def test_RevertIf_CannotDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#418)
        """
        ...

    @overload
    def test_RevertIf_CannotDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#418)
        """
        ...

    def test_RevertIf_CannotDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#418)
        """
        return self._execute(self.chain, request_type, "c49eb4c7", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def _revertDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#423)
        """
        ...

    @overload
    def _revertDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#423)
        """
        ...

    @overload
    def _revertDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#423)
        """
        ...

    @overload
    def _revertDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#423)
        """
        ...

    def _revertDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#423)
        """
        return self._execute(self.chain, request_type, "ce73c449", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#427)
        """
        ...

    @overload
    def test_DeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#427)
        """
        ...

    @overload
    def test_DeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#427)
        """
        ...

    @overload
    def test_DeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#427)
        """
        ...

    def test_DeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#427)
        """
        return self._execute(self.chain, request_type, "341306d5", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

StdCheatsTest.setUp.selector = bytes4(b'\n\x92T\xe4')
StdCheatsTest.test_Skip.selector = bytes4(b'\xc5Kci')
StdCheatsTest.test_Rewind.selector = bytes4(b'\xd9+\x84\xb0')
StdCheatsTest.test_Hoax.selector = bytes4(b'\xbf\xc4 \xf1')
StdCheatsTest.test_HoaxOrigin.selector = bytes4(b'm\xc2\x87\x8a')
StdCheatsTest.test_HoaxDifferentAddresses.selector = bytes4(b'\xcf\xcd\x8cE')
StdCheatsTest.test_StartHoax.selector = bytes4(b'\x1dN\\\x12')
StdCheatsTest.test_StartHoaxOrigin.selector = bytes4(b'X\xe8%{')
StdCheatsTest.test_ChangePrankMsgSender.selector = bytes4(b'x\xd5ji')
StdCheatsTest.test_ChangePrankMsgSenderAndTxOrigin.selector = bytes4(b'f\xa3\x88\x88')
StdCheatsTest.test_MakeAccountEquivalence.selector = bytes4(b'\x00\xab\xe4\t')
StdCheatsTest.test_MakeAddrEquivalence.selector = bytes4(b'\x9dD\xb7\x8a')
StdCheatsTest.test_MakeAddrSigning.selector = bytes4(b'\xaeB\x82g')
StdCheatsTest.test_Deal.selector = bytes4(b'\x05\x8a\xeb>')
StdCheatsTest.test_DealToken.selector = bytes4(b'\x97U\x84;')
StdCheatsTest.test_DealTokenAdjustTotalSupply.selector = bytes4(b'Y\xff\x1d\x87')
StdCheatsTest.test_DealERC1155Token.selector = bytes4(b'\xbf\xac\x85\xa4')
StdCheatsTest.test_DealERC1155TokenAdjustTotalSupply.selector = bytes4(b'\xf1\x1d\xfb`')
StdCheatsTest.test_DealERC721Token.selector = bytes4(b'\xd3\x1d|\x1d')
StdCheatsTest.test_DeployCode.selector = bytes4(b'\n\xd2\xb4\xc8')
StdCheatsTest.test_DestroyAccount.selector = bytes4(b'D@\xc5E')
StdCheatsTest.test_DeployCodeNoArgs.selector = bytes4(b'\xf90\xb6(')
StdCheatsTest.test_DeployCodeVal.selector = bytes4(b'\xbb\x11\xac\x10')
StdCheatsTest.test_DeployCodeValNoArgs.selector = bytes4(b'A<\xfc\xb1')
StdCheatsTest.deployCodeHelper.selector = bytes4(b'J\xf9g\xd1')
StdCheatsTest.test_RevertIf_DeployCodeFail.selector = bytes4(b'iT\xeeP')
StdCheatsTest.test_DeriveRememberKey.selector = bytes4(b'*\xc9\xee\xdb')
StdCheatsTest.test_BytesToUint.selector = bytes4(b'\r+\xf66')
StdCheatsTest.test_ParseJsonTxDetail.selector = bytes4(b'\xbd\x9f\xb2Y')
StdCheatsTest.test_ReadEIP1559Transaction.selector = bytes4(b'\xae\r\xdb\xc8')
StdCheatsTest.test_ReadEIP1559Transactions.selector = bytes4(b'\xcf\x99\xd3\xdd')
StdCheatsTest.test_ReadReceipt.selector = bytes4(b'"\xb4\xdeQ')
StdCheatsTest.test_ReadReceipts.selector = bytes4(b'\x99\xc8|U')
StdCheatsTest.test_GasMeteringModifier.selector = bytes4(b'\x893)\xac')
StdCheatsTest.testFuzz_AssumeAddressIsNot.selector = bytes4(b'J\x12\x97\xf8')
StdCheatsTest.test_AssumePayable.selector = bytes4(b'a&d"')
StdCheatsTest.test_AssumeNotPayable.selector = bytes4(b'\x9b\xac\xb2\xa8')
StdCheatsTest.testFuzz_AssumeNotPrecompile.selector = bytes4(b'\x9dbO\xa1')
StdCheatsTest.testFuzz_AssumeNotForgeAddress.selector = bytes4(b'u\x1e\xc6\x9d')
StdCheatsTest.test_RevertIf_CannotDeployCodeTo.selector = bytes4(b'\xc4\x9e\xb4\xc7')
StdCheatsTest._revertDeployCodeTo.selector = bytes4(b'\xces\xc4I')
StdCheatsTest.test_DeployCodeTo.selector = bytes4(b'4\x13\x06\xd5')
class StdCheatsMock(StdCheats):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#446)
    """
    _abi = {b'\x95\xb9\xa3\x83': {'inputs': [{'internalType': 'address', 'name': 'token', 'type': 'address'}, {'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'exposed_assumeNotBlacklisted', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\x17\xccs\xa0': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'exposed_assumeNotPayable', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xdeJ]\xcd': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'exposed_assumePayable', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":3931,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"gasMeteringOff","offset":0,"slot":0,"type":"t_bool"},{"astId":6002,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"stdstore","offset":0,"slot":1,"type":"t_struct(StdStorage)8331_storage"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))"},"t_mapping(t_bytes32,t_struct(FindData)8306_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)8306_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)8306_storage)"},"t_struct(FindData)8306_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":8299,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":8301,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":8303,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":8305,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(StdStorage)8331_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":8315,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))"},{"astId":8318,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":8320,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":8322,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":8324,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":8326,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":8328,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":8330,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "6080806040523460155761068b908161001a8239f35b5f80fdfe60806040526004361015610011575f80fd5b5f5f3560e01c806317cc73a01461030a57806395b9a383146100ca5763de4a5dcd1461003b575f80fd5b346100b95760203660031901126100b9578061005d61005861038f565b610432565b5f5160206106365f395f51905f523b156100c757604051632631f2b160e11b8152901515600482015281816024815f5160206106365f395f51905f525afa80156100bc576100a85750f35b816100b2916103a5565b6100b95780f35b80fd5b6040513d84823e3d90fd5b50fd5b50346100b95760403660031901126100b9576100e461038f565b6024356001600160a01b038116919082900361030657803b156102815782918280604051602081019063fe575a8760e01b82528460248201526024815261012c6044826103a5565b5190855afa9161013a6103db565b9215928315610264575b505f5160206106365f395f51905f523b1561025f57604051632631f2b160e11b8152921515600484015283836024815f5160206106365f395f51905f525afa918215610254578492610237575b8293506040516020810191630723eb0360e51b83526024820152602481526101ba6044826103a5565b51915afa6101c66103db565b901590811561021c575b505f5160206106365f395f51905f523b156100c757604051632631f2b160e11b8152901515600482015281816024815f5160206106365f395f51905f525afa80156100bc576100a85750f35b61023091506020808251830101910161041a565b155f6101d0565b91909281610244916103a5565b61025057818391610191565b5050fd5b6040513d86823e3d90fd5b505050fd5b6102799193506020808251830101910161041a565b15915f610144565b60405162461bcd60e51b815260206004820152605160248201527f53746443686561747320617373756d654e6f74426c61636b6c6973746564286160448201527f6464726573732c61646472657373293a20546f6b656e2061646472657373206960648201527039903737ba10309031b7b73a3930b1ba1760791b608482015260a490fd5b8280fd5b503461038b57602036600319011261038b5761032761005861038f565b155f5160206106365f395f51905f523b1561038b5760405190632631f2b160e11b825260048201525f816024815f5160206106365f395f51905f525afa801561038057610372575080f35b61037e91505f906103a5565b005b6040513d5f823e3d90fd5b5f80fd5b600435906001600160a01b038216820361038b57565b90601f8019910116810190811067ffffffffffffffff8211176103c757604052565b634e487b7160e01b5f52604160045260245ffd5b3d15610415573d9067ffffffffffffffff82116103c7576040519161040a601f8201601f1916602001846103a5565b82523d5f602084013e565b606090565b9081602091031261038b5751801515810361038b5790565b5f19813110156105a457479080315f5160206106365f395f51905f523b1561038b5760405163c88a5e6d60e01b8152306004820152600160248201525f92908381604481835f5160206106365f395f51905f525af180156103805761058f575b508280808060016001600160a01b0386165af1936104ae6103db565b505f5160206106365f395f51905f523b1561058b5760405163c88a5e6d60e01b815230600482015260248101919091528381604481835f5160206106365f395f51905f525af1801561025457908491610576575b50505f5160206106365f395f51905f523b156103065760405163c88a5e6d60e01b81526001600160a01b0391909116600482015260248101919091528181604481835f5160206106365f395f51905f525af180156100bc5761056357505090565b61056e8280926103a5565b6100b9575090565b81610580916103a5565b61030657825f610502565b8380fd5b61059c9193505f906103a5565b5f915f610492565b60405162461bcd60e51b815260206004820152605e60248201527f537464436865617473205f697350617961626c652861646472657373293a204260448201527f616c616e636520657175616c73206d61782075696e743235362c20736f20697460648201527f2063616e6e6f74207265636569766520616e79206d6f72652066756e64730000608482015260a490fdfe0000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da26469706673582212204fd6b7d9aef6ec582a033ef31a078d753333b5c6736ce20d592a7c098d73249b64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> StdCheatsMock:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[StdCheatsMock]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, StdCheatsMock, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[StdCheatsMock]]:
        return cls._deploy(request_type, [], return_tx, StdCheatsMock, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def exposed_assumePayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#447)

        Args:
            addr: address
        """
        ...

    @overload
    def exposed_assumePayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#447)

        Args:
            addr: address
        """
        ...

    @overload
    def exposed_assumePayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#447)

        Args:
            addr: address
        """
        ...

    @overload
    def exposed_assumePayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#447)

        Args:
            addr: address
        """
        ...

    def exposed_assumePayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#447)

        Args:
            addr: address
        """
        return self._execute(self.chain, request_type, "de4a5dcd", [addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def exposed_assumeNotPayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#451)

        Args:
            addr: address
        """
        ...

    @overload
    def exposed_assumeNotPayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#451)

        Args:
            addr: address
        """
        ...

    @overload
    def exposed_assumeNotPayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#451)

        Args:
            addr: address
        """
        ...

    @overload
    def exposed_assumeNotPayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#451)

        Args:
            addr: address
        """
        ...

    def exposed_assumeNotPayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#451)

        Args:
            addr: address
        """
        return self._execute(self.chain, request_type, "17cc73a0", [addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def exposed_assumeNotBlacklisted(self, token: Union[Account, Address], addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#456)

        Args:
            token: address
            addr: address
        """
        ...

    @overload
    def exposed_assumeNotBlacklisted(self, token: Union[Account, Address], addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#456)

        Args:
            token: address
            addr: address
        """
        ...

    @overload
    def exposed_assumeNotBlacklisted(self, token: Union[Account, Address], addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#456)

        Args:
            token: address
            addr: address
        """
        ...

    @overload
    def exposed_assumeNotBlacklisted(self, token: Union[Account, Address], addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#456)

        Args:
            token: address
            addr: address
        """
        ...

    def exposed_assumeNotBlacklisted(self, token: Union[Account, Address], addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#456)

        Args:
            token: address
            addr: address
        """
        return self._execute(self.chain, request_type, "95b9a383", [token, addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

StdCheatsMock.exposed_assumePayable.selector = bytes4(b'\xdeJ]\xcd')
StdCheatsMock.exposed_assumeNotPayable.selector = bytes4(b'\x17\xccs\xa0')
StdCheatsMock.exposed_assumeNotBlacklisted.selector = bytes4(b'\x95\xb9\xa3\x83')
class StdCheatsForkTest(Test):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#461)
    """
    _abi = {b'A0O\xac\xd92=u\xb1\x1b\xcd\xd6\t\xcb8\xef\xff\xfd\xb0W\x10\xf7\xca\xf0\xe9\xb1lm\x9dp\x9fP': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log', 'type': 'event'}, b'z\xe7LRt\x14\xae\x13_\xd9pG\xb1)!\xa5\xec9\x11\xb8\x04\x19xU\xd6~%\xc7\xb7^\xe6\xf3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'log_address', 'type': 'event'}, b'\xfb\x10(e\xd5\n\xdd\xdd\xf6\x9d\xa9\xb5\xaa\x1b\xce\xd6l\x80\xcf\x86\x9a\\\x8d\x04q\xa4g\xe1\x8c\xe9\xca\xb1': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_array', 'type': 'event'}, b'\x89\n\x82g\x9bG\x0f+\xd8(\x16\xed\x9b\x16\x1f\x97\xd8\xb9g\xf3\x7f\xa3d|!\xd5\xbf9t\x9e-\xd5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_array', 'type': 'event'}, b'@\xe1\x84\x0fWi\x07=a\xbd\x017-\x9bu\xba\xa9\x84-V)\xa0\xc9\x9f\xf1\x03\xbe\x11x\xa8\xe9\xe2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_array', 'type': 'event'}, b'#\xb6*\xd0XM$\xa7_\x0b\xf3V\x03\x91\xefVY\xecm\xb1&\x9cV\xe1\x1a\xa2A\xd67\xf1\x9b ': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'log_bytes', 'type': 'event'}, b'\xe8\x16\x99\xb8Q\x13\xee\xa1\xc7>\x10X\x8b+\x03^U\x893ic!s\xaf\xd4?\xeb\x19/\xacd\xe3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'log_bytes32', 'type': 'event'}, b'\x0e\xb5\xd5&$\xc8\xd2\x8a\xda\x9f\xc5Z\x8cP.\xd5\xaa?\xbe/\xb6\xe9\x1bq\xb5\xf3v\x88+\x1d/\xb8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256', 'name': '', 'type': 'int256'}], 'name': 'log_int', 'type': 'event'}, b'\x9cN\x85A\xca\x8f\r\xc1\xc4\x13\xf9\x10\x8ff\xd8-<\xec\xb1\xbd\xdb\xceCza\xca\xa3\x17\\L\xc9o': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address', 'name': 'val', 'type': 'address'}], 'name': 'log_named_address', 'type': 'event'}, b'\x00\xaa\xa3\x9c\x9f\xfb_VzE48\x0cspup.\x1f\x7f\x14\x10\x7f\xc9S(\xe3\xb5l\x03%\xfb': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xa7>\xda\tf/F\xdd\xe7)\xbeF\x118_\xf3O\xe6\xc4O\xbb\xc6\xf7\xe1{\x04+Y\xa3D[W': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_named_array', 'type': 'event'}, b";\xcf\xb2\xae.\x8d\x13-\xd1\xfc\xe7\xcf'\x8a\x9a\x19uj\x9f\xce\xab\xe4p\xdf;\xda\xbbK\xc5w\xd1\xbd": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xd2n\x16\xca\xd4T\x87\x05\xe4\xc9\xe2\xd9O\x98\xee\x91\xc2\x89\x08^\xe4%YO\xd5c_\xa2\x96L\xcf\x18': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'val', 'type': 'bytes'}], 'name': 'log_named_bytes', 'type': 'event'}, b'\xaf\xb7\x95\xc9\xc6\x1eO\xe7F\x8c8o\x92]zT)\xec\xad\x9c\x04\x95\xdd\xb8\xd3\x8di\x06\x14\xd3/\x99': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'val', 'type': 'bytes32'}], 'name': 'log_named_bytes32', 'type': 'event'}, b']\xa6\xce\x9dQ\x15\x1b\xa1\x0c\t\xa5Y\xef$\xd5 \xb9\xda\xc5\xc5\xb8\x81\n\xe8CNM\r\x86A\x1a\x95': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_int', 'type': 'event'}, b"\xeb\x8b\xa4<\xedu7B\x19F\xbdC\xe8(\xb8\xb2\xb8B\x89'\xaa\x8f\x80\x1c\x13\xd94\xbf\x11\xac\xa5{": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_uint', 'type': 'event'}, b'/\xe62w\x91t7CxD*\x8e\x97\x8b\xcc\xfb\xdc\xc1\xd6\xb2\xb0\xd8\x1f~\x8e\xb7v\xab"\x86\xf1h': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}], 'name': 'log_named_int', 'type': 'event'}, b'(\x0fDF\xb2\x8a\x13rA}\xdae\x8d0\xb9[)\x92\xb1*\xc9\xc7\xf3xS_)\xa9z\xcf5\x83': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'val', 'type': 'string'}], 'name': 'log_named_string', 'type': 'event'}, b'\xb2\xde/\xbe\x80\x1a\r\xf6\xc0\xcb\xdd\xfdD\x8b\xa3\xc4\x1dH\xa0@\xca5\xc5l\x81\x96\xef\x0f\xca\xe7!\xa8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}], 'name': 'log_named_uint', 'type': 'event'}, b'\x0b.\x13\xff \xac{GA\x98eU\x83\xed\xf7\r\xed\xd2\xc1\xdc\x98\x0e2\x9cO\xbb/\xc0t\x8byk': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log_string', 'type': 'event'}, b',\xab\x97\x90Q\x0f\xd8\xbd\xfb\xd2\x11R\x88\xdb3\xfe\xc6f\x91\xd4v\xef\xc5B|\xfdL\ti0\x17U': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'log_uint', 'type': 'event'}, b"\xe7\x95\x0e\xde\x03\x94\xb9\xf2\xceJZ\x1b\xf5\xa7\xe1\x85$\x11\xf7\xe6f\x1bC\x08\xc9\x13\xc4\xbf\xd1\x10'\xe4": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'logs', 'type': 'event'}, b'\xfav&\xd4': {'inputs': [], 'name': 'IS_TEST', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x89\xa3\x02q': {'inputs': [], 'name': 'USDC', 'outputs': [{'internalType': 'contract MockUSDC', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc5ND\xeb': {'inputs': [], 'name': 'USDT', 'outputs': [{'internalType': 'contract MockUSDT', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb5P\x8a\xa9': {'inputs': [], 'name': 'excludeArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'excludedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe2\x0c\x9fq': {'inputs': [], 'name': 'excludeContracts', 'outputs': [{'internalType': 'address[]', 'name': 'excludedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb0FO\xdc': {'inputs': [], 'name': 'excludeSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'excludedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1e\xd7\x83\x1c': {'inputs': [], 'name': 'excludeSenders', 'outputs': [{'internalType': 'address[]', 'name': 'excludedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbaAO\xa6': {'inputs': [], 'name': 'failed', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\n\x92T\xe4': {'inputs': [], 'name': 'setUp', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'f\xd9\xa9\xa0': {'inputs': [], 'name': 'targetArtifactSelectors', 'outputs': [{'components': [{'internalType': 'string', 'name': 'artifact', 'type': 'string'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzArtifactSelector[]', 'name': 'targetedArtifactSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x85"l\x81': {'inputs': [], 'name': 'targetArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'targetedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'?r\x86\xf4': {'inputs': [], 'name': 'targetContracts', 'outputs': [{'internalType': 'address[]', 'name': 'targetedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'*\xde8\x80': {'inputs': [], 'name': 'targetInterfaces', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'string[]', 'name': 'artifacts', 'type': 'string[]'}], 'internalType': 'struct StdInvariant.FuzzInterface[]', 'name': 'targetedInterfaces_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x91j\x17\xc6': {'inputs': [], 'name': 'targetSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'targetedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'>^<#': {'inputs': [], 'name': 'targetSenders', 'outputs': [{'internalType': 'address[]', 'name': 'targetedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'W.k\x91': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'testFuzz_AssumeNotBlacklisted_TokenWithoutBlacklist', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\xc8y\xdf\xd7': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'testFuzz_AssumeNotBlacklisted_USDC', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\xf6K\x9d\xc8': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'testFuzz_AssumeNotBlacklisted_USDT', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\xedc\xe2J': {'inputs': [], 'name': 'test_RevertIf_AssumeNoBlacklisted_USDC', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xda\xd8W\xaa': {'inputs': [], 'name': 'test_RevertIf_AssumeNoBlacklisted_USDT', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfd.\x18\x8f': {'inputs': [], 'name': 'test_RevertIf_CannotAssumeNoBlacklisted_EOA', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":46,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"stdstore","offset":0,"slot":0,"type":"t_struct(StdStorage)8331_storage"},{"astId":209,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_failed","offset":0,"slot":8,"type":"t_bool"},{"astId":2943,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"stdChainsInitialized","offset":1,"slot":8,"type":"t_bool"},{"astId":2964,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"chains","offset":0,"slot":9,"type":"t_mapping(t_string_memory_ptr,t_struct(Chain)2959_storage)"},{"astId":2968,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"defaultRpcUrls","offset":0,"slot":10,"type":"t_mapping(t_string_memory_ptr,t_string_storage)"},{"astId":2972,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"idToAlias","offset":0,"slot":11,"type":"t_mapping(t_uint256,t_string_storage)"},{"astId":2975,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"fallbackToDefaultRpcUrls","offset":0,"slot":12,"type":"t_bool"},{"astId":3931,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"gasMeteringOff","offset":1,"slot":12,"type":"t_bool"},{"astId":6002,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"stdstore","offset":0,"slot":13,"type":"t_struct(StdStorage)8331_storage"},{"astId":6923,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_excludedContracts","offset":0,"slot":21,"type":"t_array(t_address)dyn_storage"},{"astId":6926,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_excludedSenders","offset":0,"slot":22,"type":"t_array(t_address)dyn_storage"},{"astId":6929,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_targetedContracts","offset":0,"slot":23,"type":"t_array(t_address)dyn_storage"},{"astId":6932,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_targetedSenders","offset":0,"slot":24,"type":"t_array(t_address)dyn_storage"},{"astId":6935,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_excludedArtifacts","offset":0,"slot":25,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6938,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_targetedArtifacts","offset":0,"slot":26,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6942,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_targetedArtifactSelectors","offset":0,"slot":27,"type":"t_array(t_struct(FuzzArtifactSelector)6914_storage)dyn_storage"},{"astId":6946,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_excludedSelectors","offset":0,"slot":28,"type":"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage"},{"astId":6950,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_targetedSelectors","offset":0,"slot":29,"type":"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage"},{"astId":6954,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_targetedInterfaces","offset":0,"slot":30,"type":"t_array(t_struct(FuzzInterface)6920_storage)dyn_storage"},{"astId":13223,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"IS_TEST","offset":0,"slot":31,"type":"t_bool"},{"astId":41839,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"USDT","offset":1,"slot":31,"type":"t_contract(MockUSDT)42087"},{"astId":41842,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"USDC","offset":0,"slot":32,"type":"t_contract(MockUSDC)42120"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_address)dyn_storage":{"encoding":"dynamic_array","label":"address[]","numberOfBytes":32,"base":"t_address"},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_array(t_bytes4)dyn_storage":{"encoding":"dynamic_array","label":"bytes4[]","numberOfBytes":32,"base":"t_bytes4"},"t_array(t_string_storage)dyn_storage":{"encoding":"dynamic_array","label":"string[]","numberOfBytes":32,"base":"t_string_storage"},"t_array(t_struct(FuzzArtifactSelector)6914_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzArtifactSelector[]","numberOfBytes":32,"base":"t_struct(FuzzArtifactSelector)6914_storage"},"t_array(t_struct(FuzzInterface)6920_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzInterface[]","numberOfBytes":32,"base":"t_struct(FuzzInterface)6920_storage"},"t_array(t_struct(FuzzSelector)6908_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzSelector[]","numberOfBytes":32,"base":"t_struct(FuzzSelector)6908_storage"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_contract(MockUSDC)42120":{"encoding":"inplace","label":"contract MockUSDC","numberOfBytes":20},"t_contract(MockUSDT)42087":{"encoding":"inplace","label":"contract MockUSDT","numberOfBytes":20},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))"},"t_mapping(t_bytes32,t_struct(FindData)8306_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)8306_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)8306_storage)"},"t_mapping(t_string_memory_ptr,t_string_storage)":{"encoding":"mapping","label":"mapping(string => string)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_string_storage"},"t_mapping(t_string_memory_ptr,t_struct(Chain)2959_storage)":{"encoding":"mapping","label":"mapping(string => struct StdChains.Chain)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_struct(Chain)2959_storage"},"t_mapping(t_uint256,t_string_storage)":{"encoding":"mapping","label":"mapping(uint256 => string)","numberOfBytes":32,"key":"t_uint256","value":"t_string_storage"},"t_string_memory_ptr":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(Chain)2959_storage":{"encoding":"inplace","label":"struct StdChains.Chain","numberOfBytes":128,"members":[{"astId":2952,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"name","offset":0,"slot":0,"type":"t_string_storage"},{"astId":2954,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"chainId","offset":0,"slot":1,"type":"t_uint256"},{"astId":2956,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"chainAlias","offset":0,"slot":2,"type":"t_string_storage"},{"astId":2958,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"rpcUrl","offset":0,"slot":3,"type":"t_string_storage"}]},"t_struct(FindData)8306_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":8299,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":8301,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":8303,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":8305,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(FuzzArtifactSelector)6914_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzArtifactSelector","numberOfBytes":64,"members":[{"astId":6910,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"artifact","offset":0,"slot":0,"type":"t_string_storage"},{"astId":6913,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(FuzzInterface)6920_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzInterface","numberOfBytes":64,"members":[{"astId":6916,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6919,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"artifacts","offset":0,"slot":1,"type":"t_array(t_string_storage)dyn_storage"}]},"t_struct(FuzzSelector)6908_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzSelector","numberOfBytes":64,"members":[{"astId":6904,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6907,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(StdStorage)8331_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":8315,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)8306_storage)))"},{"astId":8318,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":8320,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":8322,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":8324,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":8326,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":8328,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":8330,"contract":"lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60808060405234602f57600160ff19600c541617600c55600160ff19601f541617601f556120e190816100348239f35b5f80fdfe6080806040526004361015610012575f80fd5b5f905f3560e01c9081630a9254e414610e33575080631ed7831c14610db55780632ade388014610bfe5780633e5e3c2314610b805780633f7286f414610b02578063572e6b9114610aa957806366d9a9a01461098857806385226c81146108fe57806389a30271146108d7578063916a17c61461082f578063b0464fdc14610787578063b5508aa9146106fd578063ba414fa6146106d8578063c54e44eb146106ab578063c879dfd71461063a578063dad857aa1461053c578063e20c9f71146104ae578063ed63e24a146103b3578063f64b9dc814610308578063fa7626d4146102e55763fd2e188f14610105575f80fd5b34610243578060031936011261024357604051906106a591828101928184106001600160401b038511176102d157829382916119e78339039082f080156102c4576040516001625e79b760e01b0319815260016004820152906020826024815f51602061208c5f395f51905f525afa9182156102b9578392610275575b505f51602061208c5f395f51905f523b156102515760405163f28dceb360e01b815260206004820152605160248201526101be6044820161150b565b838160a481835f51602061208c5f395f51905f525af190811561026a578491610255575b50506001600160a01b031690813b15610251576040516395b9a38360e01b81526001600160a01b03909116600482015260248101839052908290829060449082905afa8015610246576102325750f35b8161023c91611152565b6102435780f35b80fd5b6040513d84823e3d90fd5b5050fd5b8161025f91611152565b61025157825f6101e2565b6040513d86823e3d90fd5b9091506020813d6020116102b1575b8161029160209383611152565b8101031261025157516001600160a01b038116810361025157905f610182565b3d9150610284565b6040513d85823e3d90fd5b50604051903d90823e3d90fd5b634e487b7160e01b83526041600452602483fd5b5034610243578060031936011261024357602060ff601f54166040519015158152f35b5034610243576020366003190112610243576004356001600160a01b0381168082036103af57601f5460081c6001600160a01b0316916020919061034c90846115ae565b602460405180948193630723eb0360e51b835260048301525afa80156102465761037d918391610380575b50611767565b80f35b6103a2915060203d6020116103a8575b61039a8183611152565b8101906114f3565b5f610377565b503d610390565b8280fd5b5034610243578060031936011261024357604051906106a591828101928184106001600160401b038511176102d157829382916119e78339039082f080156102c4575f51602061208c5f395f51905f523b156104ab57604051633d21120560e21b81528281600481835f51602061208c5f395f51905f525af19081156102b9578391610496575b50506020546001600160a01b039182169116813b156102515782906044604051809481936395b9a38360e01b83526004830152731e34a77868e19a6647b1f2f47b51ed72dede95dd60248301525afa8015610246576102325750f35b816104a091611152565b6104ab57815f61043a565b50fd5b503461024357806003193601126102435760405160158054808352908352909160208301917f55f448fdea98c4d29eb340757ef0a66cd03dbb9538908a6a81d96026b71ec475915b81811061051d576105198561050d81870382611152565b60405191829182610fbe565b0390f35b82546001600160a01b03168452602090930192600192830192016104f6565b5034610243578060031936011261024357604051906106a591828101928184106001600160401b038511176102d157829382916119e78339039082f080156102c4575f51602061208c5f395f51905f523b156104ab57604051633d21120560e21b81528281600481835f51602061208c5f395f51905f525af19081156102b9578391610625575b5050601f546001600160a01b039182169160089190911c16813b156102515782906044604051809481936395b9a38360e01b83526004830152738f8a8f4b54a2aac7799d7bc81368ac27b852822a60248301525afa8015610246576102325750f35b8161062f91611152565b6104ab57815f6105c3565b5034610243576020366003190112610243576004356001600160a01b0381168082036103af57602080546001600160a01b03169290919061067b90846115ae565b60246040518094819363fe575a8760e01b835260048301525afa80156102465761037d9183916103805750611767565b5034610243578060031936011261024357601f5460405160089190911c6001600160a01b03168152602090f35b503461024357806003193601126102435760206106f3611458565b6040519015158152f35b503461024357806003193601126102435760195461071a81611173565b916107286040519384611152565b818352601981527f944998273e477b495144fb8794c914197f3ccb46be2900f4698fd0ef743c9695602084015b83831061076a57604051806105198782611061565b6001602081926107798561118a565b815201920192019190610755565b5034610243578060031936011261024357601c546107a481611173565b916107b26040519384611152565b818352601c81527f0e4562a10381dec21b205ed72637e6b1b523bdd0e4d4d50af5cd23dd4500a211602084015b8383106107f4576040518061051987826110c0565b6002602060019260405161080781611137565b848060a01b03865416815261081d858701611256565b838201528152019201920191906107df565b5034610243578060031936011261024357601d5461084c81611173565b9161085a6040519384611152565b818352601d81527f6d4407e7be21f808e6509aa9fa9143369579dd7d760fe20a2c09680fc146134f602084015b83831061089c576040518061051987826110c0565b600260206001926040516108af81611137565b848060a01b0386541681526108c5858701611256565b83820152815201920192019190610887565b5034610243578060031936011261024357602080546040516001600160a01b039091168152f35b5034610243578060031936011261024357601a5461091b81611173565b916109296040519384611152565b818352601a81527f057c384a7d1c54f3a1b2e5e67b2617b8224fdfd1ea7234eea573a6ff665ff63e602084015b83831061096b57604051806105198782611061565b60016020819261097a8561118a565b815201920192019190610956565b5034610243578060031936011261024357601b546109a581611173565b6109b26040519182611152565b818152601b83526020810191837f3ad8aa4f87544323a9d1e5dd902f40c356527a7955687113db5f9a85ad579dc1845b838310610a6e57868587604051928392602084019060208552518091526040840160408260051b8601019392905b828210610a1f57505050500390f35b91936001919395506020610a5e8192603f198a820301865288519083610a4e8351604084526040840190611000565b9201519084818403910152611024565b9601920192018594939192610a10565b60026020600192604051610a8181611137565b610a8a8661118a565b8152610a97858701611256565b838201528152019201920191906109e2565b5034610243576020366003190112610243576004356001600160a01b0381168103610afe5760205461037d9190610aea9082906001600160a01b03166115ae565b601f5460081c6001600160a01b03166115ae565b5080fd5b503461024357806003193601126102435760405160178054808352908352909160208301917fc624b66cc0138b8fabc209247f72d758e1cf3343756d543badbf24212bed8c15915b818110610b61576105198561050d81870382611152565b82546001600160a01b0316845260209093019260019283019201610b4a565b503461024357806003193601126102435760405160188054808352908352909160208301917fb13d2d76d1f4b7be834882e410b3e3a8afaf69f83600ae24db354391d2378d2e915b818110610bdf576105198561050d81870382611152565b82546001600160a01b0316845260209093019260019283019201610bc8565b5034610243578060031936011261024357601e54610c1b81611173565b610c286040519182611152565b818152601e83526020810191837f50bb669a95c7b50b7e8a6f09454034b2b14cf2b85c730dca9a539ca82cb6e350845b838310610d2c5786858760405192839260208401906020855251809152604084019160408260051b8601019392815b838310610c945786860387f35b919395509193603f198782030183528551906020604082019260018060a01b0381511683520151916040602083015282518091526060820190602060608260051b850101940192855b828110610d0157505050505060208060019297019301930190928695949293610c87565b9091929394602080610d1f600193605f198782030189528951611000565b9701950193929101610cdd565b604051610d3881611137565b82546001600160a01b03168152600183018054610d5481611173565b91610d626040519384611152565b8183528a526020808b20908b9084015b838210610d98575050505060019282602092836002950152815201920192019190610c58565b600160208192610da78661118a565b815201930191019091610d72565b503461024357806003193601126102435760405160168054808352908352909160208301917fd833147d7dc355ba459fc788f669e58cfaf9dc25ddcd0702e87d69c7b5124289915b818110610e14576105198561050d81870382611152565b82546001600160a01b0316845260209093019260019283019201610dfd565b905034610fa6575f366003190112610fa6576101118082018281106001600160401b03821117610faa5782916117c5833903905ff08015610f9b57601f8054610100600160a81b03191660089290921b610100600160a81b03169190911790556040516101118082016001600160401b03811183821017610faa5782916118d6833903905ff08015610f9b57602080546001600160a01b0319166001600160a01b03929092169182179055803b15610fa6575f809160446040518094819363680eeb6960e11b8352731e34a77868e19a6647b1f2f47b51ed72dede95dd6004840152600160248401525af18015610f9b57610f88575b50601f54819060081c6001600160a01b0316803b156104ab5781809160446040518094819363680eeb6960e11b8352738f8a8f4b54a2aac7799d7bc81368ac27b852822a6004840152600160248401525af18015610246576102325750f35b610f9491505f90611152565b5f5f610f29565b6040513d5f823e3d90fd5b5f80fd5b634e487b7160e01b5f52604160045260245ffd5b60206040818301928281528451809452019201905f5b818110610fe15750505090565b82516001600160a01b0316845260209384019390920191600101610fd4565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b90602080835192838152019201905f5b8181106110415750505090565b82516001600160e01b031916845260209384019390920191600101611034565b602081016020825282518091526040820191602060408360051b8301019401925f915b83831061109357505050505090565b90919293946020806110b1600193603f198682030187528951611000565b97019301930191939290611084565b602081016020825282518091526040820191602060408360051b8301019401925f915b8383106110f257505050505090565b9091929394602080611128600193603f198682030187526040838b51878060a01b03815116845201519181858201520190611024565b970193019301919392906110e3565b604081019081106001600160401b03821117610faa57604052565b90601f801991011681019081106001600160401b03821117610faa57604052565b6001600160401b038111610faa5760051b60200190565b90604051915f8154908160011c926001831692831561124c575b60208510841461123857848752869390811561121657506001146111d2575b506111d092500383611152565b565b90505f9291925260205f20905f915b8183106111fa5750509060206111d0928201015f6111c3565b60209193508060019154838589010152019101909184926111e1565b9050602092506111d094915060ff191682840152151560051b8201015f6111c3565b634e487b7160e01b5f52602260045260245ffd5b93607f16936111a4565b90604051918281549182825260208201905f5260205f20925f905b8060078301106113b3576111d0945491818110611394575b818110611375575b818110611356575b818110611337575b818110611318575b8181106112f9575b8181106112dc575b106112c7575b500383611152565b6001600160e01b03191681526020015f6112bf565b602083811b6001600160e01b0319168552909301926001016112b9565b604083901b6001600160e01b03191684526020909301926001016112b1565b606083901b6001600160e01b03191684526020909301926001016112a9565b608083901b6001600160e01b03191684526020909301926001016112a1565b60a083901b6001600160e01b0319168452602090930192600101611299565b60c083901b6001600160e01b0319168452602090930192600101611291565b60e083901b6001600160e01b0319168452602090930192600101611289565b916008919350610100600191865463ffffffff60e01b8160e01b16825263ffffffff60e01b8160c01b16602083015263ffffffff60e01b8160a01b16604083015263ffffffff60e01b8160801b16606083015263ffffffff60e01b8160601b16608083015263ffffffff60e01b8160401b1660a083015263ffffffff60e01b8160201b1660c083015263ffffffff60e01b1660e0820152019401920185929391611271565b60085460ff161561146857600190565b604051630667f9d760e41b81525f51602061208c5f395f51905f5260048201526519985a5b195960d21b60248201526020816044815f51602061208c5f395f51905f525afa908115610f9b575f916114c1575b50151590565b90506020813d6020116114eb575b816114dc60209383611152565b81010312610fa657515f6114bb565b3d91506114cf565b90816020910312610fa657518015158103610fa65790565b60407039903737ba10309031b7b73a3930b1ba1760791b917f53746443686561747320617373756d654e6f74426c61636b6c6973746564286181527f6464726573732c61646472657373293a20546f6b656e2061646472657373206960208201520152565b3d156115a9573d906001600160401b038211610faa576040519161159e601f8201601f191660200184611152565b82523d5f602084013e565b606090565b905f90823b1561173c5760405163fe575a8760e01b602082019081526001600160a01b0390921660248083018290528252915f918291906115f0604482611152565b5190865afa6115fd611570565b9015908115611721575b505f51602061208c5f395f51905f523b15610fa657604051632631f2b160e11b815290151560048201525f816024815f51602061208c5f395f51905f525afa8015610f9b5761170c575b50819282916040516020810191630723eb0360e51b835260248201526024815261167c604482611152565b51915afa611688611570565b90159081156116f1575b505f51602061208c5f395f51905f523b15610afe57604051632631f2b160e11b8152901515600482015281816024815f51602061208c5f395f51905f525afa8015610246576116df575050565b6116ea828092611152565b6102435750565b6117059150602080825183010191016114f3565b155f611692565b6117199192505f90611152565b5f905f611651565b6117359150602080825183010191016114f3565b155f611607565b60405162461bcd60e51b8152602060048201526051602482015260a4906117656044820161150b565bfd5b8061176f5750565b5f51602061208c5f395f51905f523b15610fa65760405163a598288560e01b815290151560048201525f816024815f51602061208c5f395f51905f525afa8015610f9b576117ba5750565b5f6111d09161115256fe6080806040523460145760f890816100198239f35b5f80fdfe608060405260043610156010575f80fd5b5f3560e01c8063d01dd6d21460685763e47d606014602c575f80fd5b3460645760203660031901126064576001600160a01b03604960ad565b165f525f602052602060ff60405f2054166040519015158152f35b5f80fd5b346064576040366003190112606457607d60ad565b6024359081151580920360645760018060a01b03165f525f60205260405f209060ff801983541691161790555f80f35b600435906001600160a01b038216820360645756fea2646970667358221220118e76d4cfd39e2dcc255eaf1233d9a49f4458dc08d839e30e29cd60485af7f464736f6c634300082100336080806040523460145760f890816100198239f35b5f80fdfe608060405260043610156010575f80fd5b5f3560e01c8063d01dd6d21460685763fe575a8714602c575f80fd5b3460645760203660031901126064576001600160a01b03604960ad565b165f525f602052602060ff60405f2054166040519015158152f35b5f80fd5b346064576040366003190112606457607d60ad565b6024359081151580920360645760018060a01b03165f525f60205260405f209060ff801983541691161790555f80f35b600435906001600160a01b038216820360645756fea264697066735822122099bfde628fd131c32464f6fccd453233f81519d0a60ac0225f4ea9b7541d5c5f64736f6c634300082100336080806040523460155761068b908161001a8239f35b5f80fdfe60806040526004361015610011575f80fd5b5f5f3560e01c806317cc73a01461030a57806395b9a383146100ca5763de4a5dcd1461003b575f80fd5b346100b95760203660031901126100b9578061005d61005861038f565b610432565b5f5160206106365f395f51905f523b156100c757604051632631f2b160e11b8152901515600482015281816024815f5160206106365f395f51905f525afa80156100bc576100a85750f35b816100b2916103a5565b6100b95780f35b80fd5b6040513d84823e3d90fd5b50fd5b50346100b95760403660031901126100b9576100e461038f565b6024356001600160a01b038116919082900361030657803b156102815782918280604051602081019063fe575a8760e01b82528460248201526024815261012c6044826103a5565b5190855afa9161013a6103db565b9215928315610264575b505f5160206106365f395f51905f523b1561025f57604051632631f2b160e11b8152921515600484015283836024815f5160206106365f395f51905f525afa918215610254578492610237575b8293506040516020810191630723eb0360e51b83526024820152602481526101ba6044826103a5565b51915afa6101c66103db565b901590811561021c575b505f5160206106365f395f51905f523b156100c757604051632631f2b160e11b8152901515600482015281816024815f5160206106365f395f51905f525afa80156100bc576100a85750f35b61023091506020808251830101910161041a565b155f6101d0565b91909281610244916103a5565b61025057818391610191565b5050fd5b6040513d86823e3d90fd5b505050fd5b6102799193506020808251830101910161041a565b15915f610144565b60405162461bcd60e51b815260206004820152605160248201527f53746443686561747320617373756d654e6f74426c61636b6c6973746564286160448201527f6464726573732c61646472657373293a20546f6b656e2061646472657373206960648201527039903737ba10309031b7b73a3930b1ba1760791b608482015260a490fd5b8280fd5b503461038b57602036600319011261038b5761032761005861038f565b155f5160206106365f395f51905f523b1561038b5760405190632631f2b160e11b825260048201525f816024815f5160206106365f395f51905f525afa801561038057610372575080f35b61037e91505f906103a5565b005b6040513d5f823e3d90fd5b5f80fd5b600435906001600160a01b038216820361038b57565b90601f8019910116810190811067ffffffffffffffff8211176103c757604052565b634e487b7160e01b5f52604160045260245ffd5b3d15610415573d9067ffffffffffffffff82116103c7576040519161040a601f8201601f1916602001846103a5565b82523d5f602084013e565b606090565b9081602091031261038b5751801515810361038b5790565b5f19813110156105a457479080315f5160206106365f395f51905f523b1561038b5760405163c88a5e6d60e01b8152306004820152600160248201525f92908381604481835f5160206106365f395f51905f525af180156103805761058f575b508280808060016001600160a01b0386165af1936104ae6103db565b505f5160206106365f395f51905f523b1561058b5760405163c88a5e6d60e01b815230600482015260248101919091528381604481835f5160206106365f395f51905f525af1801561025457908491610576575b50505f5160206106365f395f51905f523b156103065760405163c88a5e6d60e01b81526001600160a01b0391909116600482015260248101919091528181604481835f5160206106365f395f51905f525af180156100bc5761056357505090565b61056e8280926103a5565b6100b9575090565b81610580916103a5565b61030657825f610502565b8380fd5b61059c9193505f906103a5565b5f915f610492565b60405162461bcd60e51b815260206004820152605e60248201527f537464436865617473205f697350617961626c652861646472657373293a204260448201527f616c616e636520657175616c73206d61782075696e743235362c20736f20697460648201527f2063616e6e6f74207265636569766520616e79206d6f72652066756e64730000608482015260a490fdfe0000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da26469706673582212204fd6b7d9aef6ec582a033ef31a078d753333b5c6736ce20d592a7c098d73249b64736f6c634300082100330000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da264697066735822122092c9ad34a58e053f67e89ba01694c1a66bb88a3857caeebec5b57c0731697f6964736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> StdCheatsForkTest:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[StdCheatsForkTest]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, StdCheatsForkTest, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[StdCheatsForkTest]]:
        return cls._deploy(request_type, [], return_tx, StdCheatsForkTest, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> MockUSDT:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#465)

        Returns:
            USDT: contract MockUSDT
        """
        ...

    @overload
    def USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#465)

        Returns:
            USDT: contract MockUSDT
        """
        ...

    @overload
    def USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#465)

        Returns:
            USDT: contract MockUSDT
        """
        ...

    @overload
    def USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[MockUSDT]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#465)

        Returns:
            USDT: contract MockUSDT
        """
        ...

    def USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[MockUSDT, TransactionAbc[MockUSDT], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#465)

        Returns:
            USDT: contract MockUSDT
        """
        return self._execute(self.chain, request_type, "c54e44eb", [], True if request_type == "tx" else False, MockUSDT, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def USDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> MockUSDC:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#466)

        Returns:
            USDC: contract MockUSDC
        """
        ...

    @overload
    def USDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#466)

        Returns:
            USDC: contract MockUSDC
        """
        ...

    @overload
    def USDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#466)

        Returns:
            USDC: contract MockUSDC
        """
        ...

    @overload
    def USDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[MockUSDC]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#466)

        Returns:
            USDC: contract MockUSDC
        """
        ...

    def USDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[MockUSDC, TransactionAbc[MockUSDC], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#466)

        Returns:
            USDC: contract MockUSDC
        """
        return self._execute(self.chain, request_type, "89a30271", [], True if request_type == "tx" else False, MockUSDC, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#468)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#468)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#468)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#468)
        """
        ...

    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#468)
        """
        return self._execute(self.chain, request_type, "0a9254e4", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_RevertIf_CannotAssumeNoBlacklisted_EOA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#476)
        """
        ...

    @overload
    def test_RevertIf_CannotAssumeNoBlacklisted_EOA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#476)
        """
        ...

    @overload
    def test_RevertIf_CannotAssumeNoBlacklisted_EOA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#476)
        """
        ...

    @overload
    def test_RevertIf_CannotAssumeNoBlacklisted_EOA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#476)
        """
        ...

    def test_RevertIf_CannotAssumeNoBlacklisted_EOA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#476)
        """
        return self._execute(self.chain, request_type, "fd2e188f", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_AssumeNotBlacklisted_TokenWithoutBlacklist(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#484)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotBlacklisted_TokenWithoutBlacklist(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#484)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotBlacklisted_TokenWithoutBlacklist(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#484)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotBlacklisted_TokenWithoutBlacklist(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#484)

        Args:
            addr: address
        """
        ...

    def testFuzz_AssumeNotBlacklisted_TokenWithoutBlacklist(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#484)

        Args:
            addr: address
        """
        return self._execute(self.chain, request_type, "572e6b91", [addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_RevertIf_AssumeNoBlacklisted_USDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#490)
        """
        ...

    @overload
    def test_RevertIf_AssumeNoBlacklisted_USDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#490)
        """
        ...

    @overload
    def test_RevertIf_AssumeNoBlacklisted_USDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#490)
        """
        ...

    @overload
    def test_RevertIf_AssumeNoBlacklisted_USDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#490)
        """
        ...

    def test_RevertIf_AssumeNoBlacklisted_USDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#490)
        """
        return self._execute(self.chain, request_type, "ed63e24a", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_AssumeNotBlacklisted_USDC(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#497)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotBlacklisted_USDC(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#497)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotBlacklisted_USDC(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#497)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotBlacklisted_USDC(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#497)

        Args:
            addr: address
        """
        ...

    def testFuzz_AssumeNotBlacklisted_USDC(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#497)

        Args:
            addr: address
        """
        return self._execute(self.chain, request_type, "c879dfd7", [addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_RevertIf_AssumeNoBlacklisted_USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#502)
        """
        ...

    @overload
    def test_RevertIf_AssumeNoBlacklisted_USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#502)
        """
        ...

    @overload
    def test_RevertIf_AssumeNoBlacklisted_USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#502)
        """
        ...

    @overload
    def test_RevertIf_AssumeNoBlacklisted_USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#502)
        """
        ...

    def test_RevertIf_AssumeNoBlacklisted_USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#502)
        """
        return self._execute(self.chain, request_type, "dad857aa", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_AssumeNotBlacklisted_USDT(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#509)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotBlacklisted_USDT(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#509)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotBlacklisted_USDT(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#509)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotBlacklisted_USDT(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#509)

        Args:
            addr: address
        """
        ...

    def testFuzz_AssumeNotBlacklisted_USDT(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#509)

        Args:
            addr: address
        """
        return self._execute(self.chain, request_type, "f64b9dc8", [addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

StdCheatsForkTest.USDT.selector = bytes4(b'\xc5ND\xeb')
StdCheatsForkTest.USDC.selector = bytes4(b'\x89\xa3\x02q')
StdCheatsForkTest.setUp.selector = bytes4(b'\n\x92T\xe4')
StdCheatsForkTest.test_RevertIf_CannotAssumeNoBlacklisted_EOA.selector = bytes4(b'\xfd.\x18\x8f')
StdCheatsForkTest.testFuzz_AssumeNotBlacklisted_TokenWithoutBlacklist.selector = bytes4(b'W.k\x91')
StdCheatsForkTest.test_RevertIf_AssumeNoBlacklisted_USDC.selector = bytes4(b'\xedc\xe2J')
StdCheatsForkTest.testFuzz_AssumeNotBlacklisted_USDC.selector = bytes4(b'\xc8y\xdf\xd7')
StdCheatsForkTest.test_RevertIf_AssumeNoBlacklisted_USDT.selector = bytes4(b'\xda\xd8W\xaa')
StdCheatsForkTest.testFuzz_AssumeNotBlacklisted_USDT.selector = bytes4(b'\xf6K\x9d\xc8')
class USDCLike(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#516)
    """
    _abi = {b'\xfeWZ\x87': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'isBlacklisted', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> USDCLike:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[USDCLike]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, USDCLike, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[USDCLike]]:
        raise Exception("Cannot deploy interface")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an interface")

    @overload
    def isBlacklisted(self, arg1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#517)

        Args:
            arg1: address
        Returns:
            bool
        """
        ...

    @overload
    def isBlacklisted(self, arg1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#517)

        Args:
            arg1: address
        Returns:
            bool
        """
        ...

    @overload
    def isBlacklisted(self, arg1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#517)

        Args:
            arg1: address
        Returns:
            bool
        """
        ...

    @overload
    def isBlacklisted(self, arg1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#517)

        Args:
            arg1: address
        Returns:
            bool
        """
        ...

    def isBlacklisted(self, arg1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#517)

        Args:
            arg1: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "fe575a87", [arg1], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

USDCLike.isBlacklisted.selector = bytes4(b'\xfeWZ\x87')
class USDTLike(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#521)
    """
    _abi = {b'\xe4}``': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'isBlackListed', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> USDTLike:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[USDTLike]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, USDTLike, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[USDTLike]]:
        raise Exception("Cannot deploy interface")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an interface")

    @overload
    def isBlackListed(self, arg1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#522)

        Args:
            arg1: address
        Returns:
            bool
        """
        ...

    @overload
    def isBlackListed(self, arg1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#522)

        Args:
            arg1: address
        Returns:
            bool
        """
        ...

    @overload
    def isBlackListed(self, arg1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#522)

        Args:
            arg1: address
        Returns:
            bool
        """
        ...

    @overload
    def isBlackListed(self, arg1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#522)

        Args:
            arg1: address
        Returns:
            bool
        """
        ...

    def isBlackListed(self, arg1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#522)

        Args:
            arg1: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "e47d6060", [arg1], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

USDTLike.isBlackListed.selector = bytes4(b'\xe4}``')
class MockUSDT(USDTLike):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#525)
    """
    _abi = {b'\xe4}``': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'isBlackListed', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd0\x1d\xd6\xd2': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bool', 'name': 'value', 'type': 'bool'}], 'name': 'setBlacklisted', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":42060,"contract":"lib/forge-std/test/StdCheats.t.sol:MockUSDT","label":"blacklist","offset":0,"slot":0,"type":"t_mapping(t_address,t_bool)"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_mapping(t_address,t_bool)":{"encoding":"mapping","label":"mapping(address => bool)","numberOfBytes":32,"key":"t_address","value":"t_bool"}}}
    _creation_code = "6080806040523460145760f890816100198239f35b5f80fdfe608060405260043610156010575f80fd5b5f3560e01c8063d01dd6d21460685763e47d606014602c575f80fd5b3460645760203660031901126064576001600160a01b03604960ad565b165f525f602052602060ff60405f2054166040519015158152f35b5f80fd5b346064576040366003190112606457607d60ad565b6024359081151580920360645760018060a01b03165f525f60205260405f209060ff801983541691161790555f80f35b600435906001600160a01b038216820360645756fea2646970667358221220118e76d4cfd39e2dcc255eaf1233d9a49f4458dc08d839e30e29cd60485af7f464736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> MockUSDT:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[MockUSDT]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, MockUSDT, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[MockUSDT]]:
        return cls._deploy(request_type, [], return_tx, MockUSDT, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def isBlackListed(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#528)

        Args:
            addr: address
        Returns:
            bool
        """
        ...

    @overload
    def isBlackListed(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#528)

        Args:
            addr: address
        Returns:
            bool
        """
        ...

    @overload
    def isBlackListed(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#528)

        Args:
            addr: address
        Returns:
            bool
        """
        ...

    @overload
    def isBlackListed(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#528)

        Args:
            addr: address
        Returns:
            bool
        """
        ...

    def isBlackListed(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#528)

        Args:
            addr: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "e47d6060", [addr], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setBlacklisted(self, addr: Union[Account, Address], value_: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#532)

        Args:
            addr: address
            value_: bool
        """
        ...

    @overload
    def setBlacklisted(self, addr: Union[Account, Address], value_: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#532)

        Args:
            addr: address
            value_: bool
        """
        ...

    @overload
    def setBlacklisted(self, addr: Union[Account, Address], value_: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#532)

        Args:
            addr: address
            value_: bool
        """
        ...

    @overload
    def setBlacklisted(self, addr: Union[Account, Address], value_: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#532)

        Args:
            addr: address
            value_: bool
        """
        ...

    def setBlacklisted(self, addr: Union[Account, Address], value_: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#532)

        Args:
            addr: address
            value_: bool
        """
        return self._execute(self.chain, request_type, "d01dd6d2", [addr, value_], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

MockUSDT.isBlackListed.selector = bytes4(b'\xe4}``')
MockUSDT.setBlacklisted.selector = bytes4(b'\xd0\x1d\xd6\xd2')
class MockUSDC(USDCLike):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#537)
    """
    _abi = {b'\xfeWZ\x87': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'isBlacklisted', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd0\x1d\xd6\xd2': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bool', 'name': 'value', 'type': 'bool'}], 'name': 'setBlacklisted', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":42093,"contract":"lib/forge-std/test/StdCheats.t.sol:MockUSDC","label":"blacklist","offset":0,"slot":0,"type":"t_mapping(t_address,t_bool)"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_mapping(t_address,t_bool)":{"encoding":"mapping","label":"mapping(address => bool)","numberOfBytes":32,"key":"t_address","value":"t_bool"}}}
    _creation_code = "6080806040523460145760f890816100198239f35b5f80fdfe608060405260043610156010575f80fd5b5f3560e01c8063d01dd6d21460685763fe575a8714602c575f80fd5b3460645760203660031901126064576001600160a01b03604960ad565b165f525f602052602060ff60405f2054166040519015158152f35b5f80fd5b346064576040366003190112606457607d60ad565b6024359081151580920360645760018060a01b03165f525f60205260405f209060ff801983541691161790555f80f35b600435906001600160a01b038216820360645756fea264697066735822122099bfde628fd131c32464f6fccd453233f81519d0a60ac0225f4ea9b7541d5c5f64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> MockUSDC:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[MockUSDC]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, MockUSDC, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[MockUSDC]]:
        return cls._deploy(request_type, [], return_tx, MockUSDC, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def isBlacklisted(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#540)

        Args:
            addr: address
        Returns:
            bool
        """
        ...

    @overload
    def isBlacklisted(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#540)

        Args:
            addr: address
        Returns:
            bool
        """
        ...

    @overload
    def isBlacklisted(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#540)

        Args:
            addr: address
        Returns:
            bool
        """
        ...

    @overload
    def isBlacklisted(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#540)

        Args:
            addr: address
        Returns:
            bool
        """
        ...

    def isBlacklisted(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#540)

        Args:
            addr: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "fe575a87", [addr], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setBlacklisted(self, addr: Union[Account, Address], value_: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#544)

        Args:
            addr: address
            value_: bool
        """
        ...

    @overload
    def setBlacklisted(self, addr: Union[Account, Address], value_: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#544)

        Args:
            addr: address
            value_: bool
        """
        ...

    @overload
    def setBlacklisted(self, addr: Union[Account, Address], value_: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#544)

        Args:
            addr: address
            value_: bool
        """
        ...

    @overload
    def setBlacklisted(self, addr: Union[Account, Address], value_: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#544)

        Args:
            addr: address
            value_: bool
        """
        ...

    def setBlacklisted(self, addr: Union[Account, Address], value_: bool, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#544)

        Args:
            addr: address
            value_: bool
        """
        return self._execute(self.chain, request_type, "d01dd6d2", [addr, value_], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

MockUSDC.isBlacklisted.selector = bytes4(b'\xfeWZ\x87')
MockUSDC.setBlacklisted.selector = bytes4(b'\xd0\x1d\xd6\xd2')
class Bar(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#549)
    """
    _abi = {'constructor': {'inputs': [], 'stateMutability': 'payable', 'type': 'constructor'}, b'p\xa0\x821': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'dn\xa5m': {'inputs': [{'internalType': 'address', 'name': 'expectedSender', 'type': 'address'}], 'name': 'bar', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, b'UYdw': {'inputs': [{'internalType': 'address', 'name': 'expectedSender', 'type': 'address'}], 'name': 'origin', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, b'\xa9\xb2\xe2\x8a': {'inputs': [{'internalType': 'address', 'name': 'expectedSender', 'type': 'address'}, {'internalType': 'address', 'name': 'expectedOrigin', 'type': 'address'}], 'name': 'origin', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, b'\x18\x16\r\xdd': {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":42203,"contract":"lib/forge-std/test/StdCheats.t.sol:Bar","label":"balanceOf","offset":0,"slot":0,"type":"t_mapping(t_address,t_uint256)"},{"astId":42205,"contract":"lib/forge-std/test/StdCheats.t.sol:Bar","label":"totalSupply","offset":0,"slot":1,"type":"t_uint256"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_mapping(t_address,t_uint256)":{"encoding":"mapping","label":"mapping(address => uint256)","numberOfBytes":32,"key":"t_address","value":"t_uint256"},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60808060405269021e19e0c9bab2400000600155305f525f60205269021e19e0c9bab240000060405f20556101c590816100378239f3fe6080806040526004361015610012575f80fd5b5f3560e01c90816318160ddd1461012a5750806355596477146100ff578063646ea56d146100d857806370a08231146100a15763a9b2e28a14610053575f80fd5b604036600319011261009d57610067610144565b6024356001600160a01b0381169081900361009d5761009b91610094906001600160a01b0316331461015a565b321461015a565b005b5f80fd5b3461009d57602036600319011261009d576001600160a01b036100c2610144565b165f525f602052602060405f2054604051908152f35b602036600319011261009d5761009b6001600160a01b036100f7610144565b16331461015a565b602036600319011261009d5761009b6001600160a01b0361011e610144565b1661009481331461015a565b3461009d575f36600319011261009d576020906001548152f35b600435906001600160a01b038216820361009d57565b1561016157565b60405162461bcd60e51b8152602060048201526006602482015265217072616e6b60d01b6044820152606490fdfea2646970667358221220d8b7efabc949b5243edeee5fc571978d12c2761cbdffef438acc5e32d834155b64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#550)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Bar:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#550)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#550)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#550)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Bar]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#550)
        """
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, Bar, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[Bar]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#550)
        """
        return cls._deploy(request_type, [], return_tx, Bar, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def balanceOf(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#572)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def balanceOf(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#572)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def balanceOf(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#572)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def balanceOf(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#572)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    def balanceOf(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#572)

        Args:
            key0: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "70a08231", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#573)

        Returns:
            totalSupply: uint256
        """
        ...

    @overload
    def totalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#573)

        Returns:
            totalSupply: uint256
        """
        ...

    @overload
    def totalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#573)

        Returns:
            totalSupply: uint256
        """
        ...

    @overload
    def totalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#573)

        Returns:
            totalSupply: uint256
        """
        ...

    def totalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#573)

        Returns:
            totalSupply: uint256
        """
        return self._execute(self.chain, request_type, "18160ddd", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def bar(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#557)

        Args:
            expectedSender: address
        """
        ...

    @overload
    def bar(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#557)

        Args:
            expectedSender: address
        """
        ...

    @overload
    def bar(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#557)

        Args:
            expectedSender: address
        """
        ...

    @overload
    def bar(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#557)

        Args:
            expectedSender: address
        """
        ...

    def bar(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#557)

        Args:
            expectedSender: address
        """
        return self._execute(self.chain, request_type, "646ea56d", [expectedSender], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def origin(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#561)

        Args:
            expectedSender: address
        """
        ...

    @overload
    def origin(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#561)

        Args:
            expectedSender: address
        """
        ...

    @overload
    def origin(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#561)

        Args:
            expectedSender: address
        """
        ...

    @overload
    def origin(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#561)

        Args:
            expectedSender: address
        """
        ...

    def origin(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#561)

        Args:
            expectedSender: address
        """
        return self._execute(self.chain, request_type, "55596477", [expectedSender], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def origin_(self, expectedSender: Union[Account, Address], expectedOrigin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#566)

        Args:
            expectedSender: address
            expectedOrigin: address
        """
        ...

    @overload
    def origin_(self, expectedSender: Union[Account, Address], expectedOrigin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#566)

        Args:
            expectedSender: address
            expectedOrigin: address
        """
        ...

    @overload
    def origin_(self, expectedSender: Union[Account, Address], expectedOrigin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#566)

        Args:
            expectedSender: address
            expectedOrigin: address
        """
        ...

    @overload
    def origin_(self, expectedSender: Union[Account, Address], expectedOrigin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#566)

        Args:
            expectedSender: address
            expectedOrigin: address
        """
        ...

    def origin_(self, expectedSender: Union[Account, Address], expectedOrigin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#566)

        Args:
            expectedSender: address
            expectedOrigin: address
        """
        return self._execute(self.chain, request_type, "a9b2e28a", [expectedSender, expectedOrigin], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

Bar.balanceOf.selector = bytes4(b'p\xa0\x821')
Bar.totalSupply.selector = bytes4(b'\x18\x16\r\xdd')
Bar.bar.selector = bytes4(b'dn\xa5m')
Bar.origin.selector = bytes4(b'UYdw')
Bar.origin_.selector = bytes4(b'\xa9\xb2\xe2\x8a')
class BarERC1155(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#576)
    """
    _abi = {'constructor': {'inputs': [], 'stateMutability': 'payable', 'type': 'constructor'}, b'\x00\xfd\xd5\x8e': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbd\x85\xb09': {'inputs': [{'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":42264,"contract":"lib/forge-std/test/StdCheats.t.sol:BarERC1155","label":"_balances","offset":0,"slot":0,"type":"t_mapping(t_uint256,t_mapping(t_address,t_uint256))"},{"astId":42268,"contract":"lib/forge-std/test/StdCheats.t.sol:BarERC1155","label":"_totalSupply","offset":0,"slot":1,"type":"t_mapping(t_uint256,t_uint256)"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_mapping(t_address,t_uint256)":{"encoding":"mapping","label":"mapping(address => uint256)","numberOfBytes":32,"key":"t_address","value":"t_uint256"},"t_mapping(t_uint256,t_mapping(t_address,t_uint256))":{"encoding":"mapping","label":"mapping(uint256 => mapping(address => uint256))","numberOfBytes":32,"key":"t_uint256","value":"t_mapping(t_address,t_uint256)"},"t_mapping(t_uint256,t_uint256)":{"encoding":"mapping","label":"mapping(uint256 => uint256)","numberOfBytes":32,"key":"t_uint256","value":"t_uint256"},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "6080604081815269021e19e0c9bab24000007fa6eef7e35abe7026729641147f7915573c7e97b47efa546f5f6e3230263bcb49819055305f9081527fad3228b676f7d3cd4284a5443f17f1962b36e491b30a40b2405849e597ba5fb5602052919091205560d1908161006f8239f3fe60808060405260043610156011575f80fd5b5f3560e01c908162fdd58e14605a575063bd85b03914602e575f80fd5b3460565760203660031901126056576004355f526001602052602060405f2054604051908152f35b5f80fd5b3460565760403660031901126056576004356001600160a01b03811691908290036056576020916024355f525f835260405f20905f52825260405f20548152f3fea2646970667358221220e94c6b630765b315bbfe65451892e75eed923d77b697cf9294647ac927515ff764736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#577)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> BarERC1155:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#577)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#577)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#577)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[BarERC1155]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#577)
        """
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, BarERC1155, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[BarERC1155]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#577)
        """
        return cls._deploy(request_type, [], return_tx, BarERC1155, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def balanceOf(self, account: Union[Account, Address], id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#583)

        Args:
            account: address
            id: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def balanceOf(self, account: Union[Account, Address], id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#583)

        Args:
            account: address
            id: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def balanceOf(self, account: Union[Account, Address], id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#583)

        Args:
            account: address
            id: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def balanceOf(self, account: Union[Account, Address], id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#583)

        Args:
            account: address
            id: uint256
        Returns:
            uint256
        """
        ...

    def balanceOf(self, account: Union[Account, Address], id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#583)

        Args:
            account: address
            id: uint256
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "00fdd58e", [account, id], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalSupply(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#587)

        Args:
            id: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def totalSupply(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#587)

        Args:
            id: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def totalSupply(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#587)

        Args:
            id: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def totalSupply(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#587)

        Args:
            id: uint256
        Returns:
            uint256
        """
        ...

    def totalSupply(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#587)

        Args:
            id: uint256
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "bd85b039", [id], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

BarERC1155.balanceOf.selector = bytes4(b'\x00\xfd\xd5\x8e')
BarERC1155.totalSupply.selector = bytes4(b'\xbd\x85\xb09')
class BarERC721(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#596)
    """
    _abi = {'constructor': {'inputs': [], 'stateMutability': 'payable', 'type': 'constructor'}, b'p\xa0\x821': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'cR!\x1e': {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'ownerOf', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":42350,"contract":"lib/forge-std/test/StdCheats.t.sol:BarERC721","label":"_owners","offset":0,"slot":0,"type":"t_mapping(t_uint256,t_address)"},{"astId":42354,"contract":"lib/forge-std/test/StdCheats.t.sol:BarERC721","label":"_balances","offset":0,"slot":1,"type":"t_mapping(t_address,t_uint256)"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_mapping(t_address,t_uint256)":{"encoding":"mapping","label":"mapping(address => uint256)","numberOfBytes":32,"key":"t_address","value":"t_uint256"},"t_mapping(t_uint256,t_address)":{"encoding":"mapping","label":"mapping(uint256 => address)","numberOfBytes":32,"key":"t_uint256","value":"t_address"},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "608060408181527fada5013122d395ba3c54772283fb069b10426056ef8ca54750cb9bb552a59e7d805460016001600160a01b031991821681179092557fcc69885fda6bcc1a4ace058b4a62bf5e179ea78fd58a1ccd71c22cc9b688792f8290557fabbb5caa7dda850e60932de0934eb1f9d0f59695050f761dc64e443e5030a56980543090831681179091557f101e368776582e57ab3d116ffe2517c0a585cd5b23174b01e275c2d8329c3d83805490921681179091555f908152602091909152206002905560d190816100d28239f3fe60808060405260043610156011575f80fd5b5f3560e01c9081636352211e14606c57506370a0823114602f575f80fd5b3460685760203660031901126068576004356001600160a01b038116908190036068575f526001602052602060405f2054604051908152f35b5f80fd5b3460685760203660031901126068576004355f90815260208181526040909120546001600160a01b0316825290f3fea2646970667358221220030a960c495b64223ccb62746a4c0b894bd3e0ac1602bf1a4f0162611ca189ad64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#597)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> BarERC721:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#597)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#597)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#597)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[BarERC721]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#597)
        """
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, BarERC721, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[BarERC721]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#597)
        """
        return cls._deploy(request_type, [], return_tx, BarERC721, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def balanceOf(self, owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#606)

        Args:
            owner: address
        Returns:
            uint256
        """
        ...

    @overload
    def balanceOf(self, owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#606)

        Args:
            owner: address
        Returns:
            uint256
        """
        ...

    @overload
    def balanceOf(self, owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#606)

        Args:
            owner: address
        Returns:
            uint256
        """
        ...

    @overload
    def balanceOf(self, owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#606)

        Args:
            owner: address
        Returns:
            uint256
        """
        ...

    def balanceOf(self, owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#606)

        Args:
            owner: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "70a08231", [owner], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def ownerOf(self, tokenId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#610)

        Args:
            tokenId: uint256
        Returns:
            address
        """
        ...

    @overload
    def ownerOf(self, tokenId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#610)

        Args:
            tokenId: uint256
        Returns:
            address
        """
        ...

    @overload
    def ownerOf(self, tokenId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#610)

        Args:
            tokenId: uint256
        Returns:
            address
        """
        ...

    @overload
    def ownerOf(self, tokenId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#610)

        Args:
            tokenId: uint256
        Returns:
            address
        """
        ...

    def ownerOf(self, tokenId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#610)

        Args:
            tokenId: uint256
        Returns:
            address
        """
        return self._execute(self.chain, request_type, "6352211e", [tokenId], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

BarERC721.balanceOf.selector = bytes4(b'p\xa0\x821')
BarERC721.ownerOf.selector = bytes4(b'cR!\x1e')
class RevertingContract(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#619)
    """
    _abi = {'constructor': {'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}}
    _storage_layout = {"storage":[]}
    _creation_code = "5f80fdfe"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#620)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> RevertingContract:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#620)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#620)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#620)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[RevertingContract]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#620)
        """
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, RevertingContract, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[RevertingContract]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#620)
        """
        return cls._deploy(request_type, [], return_tx, RevertingContract, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

class MockContractWithConstructorArgs(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#625)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'uint256', 'name': '_x', 'type': 'uint256'}, {'internalType': 'bool', 'name': '_y', 'type': 'bool'}, {'internalType': 'bytes20', 'name': '_z', 'type': 'bytes20'}], 'stateMutability': 'payable', 'type': 'constructor'}, b'\x0cUi\x9c': {'inputs': [], 'name': 'x', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa5m\xfeJ': {'inputs': [], 'name': 'y', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc5\xd7\x80.': {'inputs': [], 'name': 'z', 'outputs': [{'internalType': 'bytes20', 'name': '', 'type': 'bytes20'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":42367,"contract":"lib/forge-std/test/StdCheats.t.sol:MockContractWithConstructorArgs","label":"y","offset":0,"slot":0,"type":"t_bool"},{"astId":42369,"contract":"lib/forge-std/test/StdCheats.t.sol:MockContractWithConstructorArgs","label":"z","offset":1,"slot":0,"type":"t_bytes20"}],"types":{"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes20":{"encoding":"inplace","label":"bytes20","numberOfBytes":20}}}
    _creation_code = "60a0601f6101ad38819003918201601f19168301916001600160401b0383118484101760a45780849260609460405283398101031260a057805160208201519182151580930360a05760400151906001600160601b03198216820360a0576080525f80546001600160a81b03191660ff939093169290921760589190911c610100600160a81b031617905560405160f490816100b9823960805181609b0152f35b5f80fd5b634e487b7160e01b5f52604160045260245ffdfe60808060405260043610156011575f80fd5b5f3560e01c9081630c55699c14608857508063a56dfe4a1460695763c5d7802e146039575f80fd5b346065575f36600319011260655760206bffffffffffffffffffffffff195f5460581b16604051908152f35b5f80fd5b346065575f366003190112606557602060ff5f54166040519015158152f35b346065575f3660031901126065576020907f00000000000000000000000000000000000000000000000000000000000000008152f3fea264697066735822122099b02dde3c01b00c46a890ae41de7cdd48411a545610030ba715d8aa29104d5e64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, _x: uint256, _y: bool, _z: bytes20, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#630)

        Args:
            _x: uint256
            _y: bool
            _z: bytes20
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _x: uint256, _y: bool, _z: bytes20, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> MockContractWithConstructorArgs:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#630)

        Args:
            _x: uint256
            _y: bool
            _z: bytes20
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _x: uint256, _y: bool, _z: bytes20, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#630)

        Args:
            _x: uint256
            _y: bool
            _z: bytes20
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _x: uint256, _y: bool, _z: bytes20, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#630)

        Args:
            _x: uint256
            _y: bool
            _z: bytes20
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _x: uint256, _y: bool, _z: bytes20, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[MockContractWithConstructorArgs]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#630)

        Args:
            _x: uint256
            _y: bool
            _z: bytes20
        """
        ...

    @classmethod
    def deploy(cls, _x: uint256, _y: bool, _z: bytes20, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, MockContractWithConstructorArgs, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[MockContractWithConstructorArgs]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#630)

        Args:
            _x: uint256
            _y: bool
            _z: bytes20
        """
        return cls._deploy(request_type, [_x, _y, _z], return_tx, MockContractWithConstructorArgs, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def x(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#626)

        Returns:
            x: uint256
        """
        ...

    @overload
    def x(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#626)

        Returns:
            x: uint256
        """
        ...

    @overload
    def x(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#626)

        Returns:
            x: uint256
        """
        ...

    @overload
    def x(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#626)

        Returns:
            x: uint256
        """
        ...

    def x(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#626)

        Returns:
            x: uint256
        """
        return self._execute(self.chain, request_type, "0c55699c", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def y(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#627)

        Returns:
            y: bool
        """
        ...

    @overload
    def y(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#627)

        Returns:
            y: bool
        """
        ...

    @overload
    def y(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#627)

        Returns:
            y: bool
        """
        ...

    @overload
    def y(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#627)

        Returns:
            y: bool
        """
        ...

    def y(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#627)

        Returns:
            y: bool
        """
        return self._execute(self.chain, request_type, "a56dfe4a", [], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def z(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes20:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#628)

        Returns:
            z: bytes20
        """
        ...

    @overload
    def z(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#628)

        Returns:
            z: bytes20
        """
        ...

    @overload
    def z(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#628)

        Returns:
            z: bytes20
        """
        ...

    @overload
    def z(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes20]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#628)

        Returns:
            z: bytes20
        """
        ...

    def z(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes20, TransactionAbc[bytes20], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#628)

        Returns:
            z: bytes20
        """
        return self._execute(self.chain, request_type, "c5d7802e", [], True if request_type == "tx" else False, bytes20, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

MockContractWithConstructorArgs.x.selector = bytes4(b'\x0cUi\x9c')
MockContractWithConstructorArgs.y.selector = bytes4(b'\xa5m\xfeJ')
MockContractWithConstructorArgs.z.selector = bytes4(b'\xc5\xd7\x80.')
class MockContractPayable(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/test/StdCheats.t.sol#637)
    """
    _abi = {'receive': {'stateMutability': 'payable', 'type': 'receive'}}
    _storage_layout = {"storage":[]}
    _creation_code = "608080604052346013576040908160188239f35b5f80fdfe36156008575f80fd5b00fea2646970667358221220f0848357e1138fd6ce5cf47151b43a3c0f4e0f7caf5505b5df99d57a8632f7b464736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> MockContractPayable:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[MockContractPayable]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, MockContractPayable, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[MockContractPayable]]:
        return cls._deploy(request_type, [], return_tx, MockContractPayable, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

