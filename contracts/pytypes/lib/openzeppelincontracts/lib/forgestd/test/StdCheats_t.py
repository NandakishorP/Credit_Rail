
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.lib.forgestd.src.StdCheats import StdCheats
from pytypes.lib.openzeppelincontracts.lib.forgestd.src.Test import Test



class StdCheatsTest(Test):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#10)
    """
    _abi = {b'\x9c\x95U\xb1\xe3\x10.<\xf4\x8fB}y\xcbg\x8f]\x9b\xd1\xed\n\xd5t8\x94a\xe2U\xf9Qp\xed': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'who', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes4', 'name': 'fsig', 'type': 'bytes4'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'keysHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'slot', 'type': 'uint256'}], 'name': 'SlotFound', 'type': 'event'}, b'\x08\x0f\xc4\xa9f \xc4F.p[#\xf3FA?\xe3yk\xb6<o\x8d\x85\x91\xba\xec\x0e#\x15w\xa5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'who', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'slot', 'type': 'uint256'}], 'name': 'WARNING_UninitedSlot', 'type': 'event'}, b'A0O\xac\xd92=u\xb1\x1b\xcd\xd6\t\xcb8\xef\xff\xfd\xb0W\x10\xf7\xca\xf0\xe9\xb1lm\x9dp\x9fP': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log', 'type': 'event'}, b'z\xe7LRt\x14\xae\x13_\xd9pG\xb1)!\xa5\xec9\x11\xb8\x04\x19xU\xd6~%\xc7\xb7^\xe6\xf3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'log_address', 'type': 'event'}, b'\xfb\x10(e\xd5\n\xdd\xdd\xf6\x9d\xa9\xb5\xaa\x1b\xce\xd6l\x80\xcf\x86\x9a\\\x8d\x04q\xa4g\xe1\x8c\xe9\xca\xb1': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_array', 'type': 'event'}, b'\x89\n\x82g\x9bG\x0f+\xd8(\x16\xed\x9b\x16\x1f\x97\xd8\xb9g\xf3\x7f\xa3d|!\xd5\xbf9t\x9e-\xd5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_array', 'type': 'event'}, b'@\xe1\x84\x0fWi\x07=a\xbd\x017-\x9bu\xba\xa9\x84-V)\xa0\xc9\x9f\xf1\x03\xbe\x11x\xa8\xe9\xe2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_array', 'type': 'event'}, b'#\xb6*\xd0XM$\xa7_\x0b\xf3V\x03\x91\xefVY\xecm\xb1&\x9cV\xe1\x1a\xa2A\xd67\xf1\x9b ': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'log_bytes', 'type': 'event'}, b'\xe8\x16\x99\xb8Q\x13\xee\xa1\xc7>\x10X\x8b+\x03^U\x893ic!s\xaf\xd4?\xeb\x19/\xacd\xe3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'log_bytes32', 'type': 'event'}, b'\x0e\xb5\xd5&$\xc8\xd2\x8a\xda\x9f\xc5Z\x8cP.\xd5\xaa?\xbe/\xb6\xe9\x1bq\xb5\xf3v\x88+\x1d/\xb8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256', 'name': '', 'type': 'int256'}], 'name': 'log_int', 'type': 'event'}, b'\x9cN\x85A\xca\x8f\r\xc1\xc4\x13\xf9\x10\x8ff\xd8-<\xec\xb1\xbd\xdb\xceCza\xca\xa3\x17\\L\xc9o': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address', 'name': 'val', 'type': 'address'}], 'name': 'log_named_address', 'type': 'event'}, b'\x00\xaa\xa3\x9c\x9f\xfb_VzE48\x0cspup.\x1f\x7f\x14\x10\x7f\xc9S(\xe3\xb5l\x03%\xfb': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xa7>\xda\tf/F\xdd\xe7)\xbeF\x118_\xf3O\xe6\xc4O\xbb\xc6\xf7\xe1{\x04+Y\xa3D[W': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_named_array', 'type': 'event'}, b";\xcf\xb2\xae.\x8d\x13-\xd1\xfc\xe7\xcf'\x8a\x9a\x19uj\x9f\xce\xab\xe4p\xdf;\xda\xbbK\xc5w\xd1\xbd": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xd2n\x16\xca\xd4T\x87\x05\xe4\xc9\xe2\xd9O\x98\xee\x91\xc2\x89\x08^\xe4%YO\xd5c_\xa2\x96L\xcf\x18': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'val', 'type': 'bytes'}], 'name': 'log_named_bytes', 'type': 'event'}, b'\xaf\xb7\x95\xc9\xc6\x1eO\xe7F\x8c8o\x92]zT)\xec\xad\x9c\x04\x95\xdd\xb8\xd3\x8di\x06\x14\xd3/\x99': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'val', 'type': 'bytes32'}], 'name': 'log_named_bytes32', 'type': 'event'}, b']\xa6\xce\x9dQ\x15\x1b\xa1\x0c\t\xa5Y\xef$\xd5 \xb9\xda\xc5\xc5\xb8\x81\n\xe8CNM\r\x86A\x1a\x95': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_int', 'type': 'event'}, b"\xeb\x8b\xa4<\xedu7B\x19F\xbdC\xe8(\xb8\xb2\xb8B\x89'\xaa\x8f\x80\x1c\x13\xd94\xbf\x11\xac\xa5{": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_uint', 'type': 'event'}, b'/\xe62w\x91t7CxD*\x8e\x97\x8b\xcc\xfb\xdc\xc1\xd6\xb2\xb0\xd8\x1f~\x8e\xb7v\xab"\x86\xf1h': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}], 'name': 'log_named_int', 'type': 'event'}, b'(\x0fDF\xb2\x8a\x13rA}\xdae\x8d0\xb9[)\x92\xb1*\xc9\xc7\xf3xS_)\xa9z\xcf5\x83': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'val', 'type': 'string'}], 'name': 'log_named_string', 'type': 'event'}, b'\xb2\xde/\xbe\x80\x1a\r\xf6\xc0\xcb\xdd\xfdD\x8b\xa3\xc4\x1dH\xa0@\xca5\xc5l\x81\x96\xef\x0f\xca\xe7!\xa8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}], 'name': 'log_named_uint', 'type': 'event'}, b'\x0b.\x13\xff \xac{GA\x98eU\x83\xed\xf7\r\xed\xd2\xc1\xdc\x98\x0e2\x9cO\xbb/\xc0t\x8byk': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log_string', 'type': 'event'}, b',\xab\x97\x90Q\x0f\xd8\xbd\xfb\xd2\x11R\x88\xdb3\xfe\xc6f\x91\xd4v\xef\xc5B|\xfdL\ti0\x17U': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'log_uint', 'type': 'event'}, b"\xe7\x95\x0e\xde\x03\x94\xb9\xf2\xceJZ\x1b\xf5\xa7\xe1\x85$\x11\xf7\xe6f\x1bC\x08\xc9\x13\xc4\xbf\xd1\x10'\xe4": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'logs', 'type': 'event'}, b'\xfav&\xd4': {'inputs': [], 'name': 'IS_TEST', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xces\xc4I': {'inputs': [], 'name': '_revertDeployCodeTo', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'J\xf9g\xd1': {'inputs': [{'internalType': 'string', 'name': 'what', 'type': 'string'}], 'name': 'deployCodeHelper', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xb5P\x8a\xa9': {'inputs': [], 'name': 'excludeArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'excludedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe2\x0c\x9fq': {'inputs': [], 'name': 'excludeContracts', 'outputs': [{'internalType': 'address[]', 'name': 'excludedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb0FO\xdc': {'inputs': [], 'name': 'excludeSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'excludedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1e\xd7\x83\x1c': {'inputs': [], 'name': 'excludeSenders', 'outputs': [{'internalType': 'address[]', 'name': 'excludedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbaAO\xa6': {'inputs': [], 'name': 'failed', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\n\x92T\xe4': {'inputs': [], 'name': 'setUp', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'f\xd9\xa9\xa0': {'inputs': [], 'name': 'targetArtifactSelectors', 'outputs': [{'components': [{'internalType': 'string', 'name': 'artifact', 'type': 'string'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzArtifactSelector[]', 'name': 'targetedArtifactSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x85"l\x81': {'inputs': [], 'name': 'targetArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'targetedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'?r\x86\xf4': {'inputs': [], 'name': 'targetContracts', 'outputs': [{'internalType': 'address[]', 'name': 'targetedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'*\xde8\x80': {'inputs': [], 'name': 'targetInterfaces', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'string[]', 'name': 'artifacts', 'type': 'string[]'}], 'internalType': 'struct StdInvariant.FuzzInterface[]', 'name': 'targetedInterfaces_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x91j\x17\xc6': {'inputs': [], 'name': 'targetSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'targetedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'>^<#': {'inputs': [], 'name': 'targetSenders', 'outputs': [{'internalType': 'address[]', 'name': 'targetedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'J\x12\x97\xf8': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'testFuzz_AssumeAddressIsNot', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'u\x1e\xc6\x9d': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'testFuzz_AssumeNotForgeAddress', 'outputs': [], 'stateMutability': 'pure', 'type': 'function'}, b'\x9dbO\xa1': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'testFuzz_AssumeNotPrecompile', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x9b\xac\xb2\xa8': {'inputs': [], 'name': 'test_AssumeNotPayable', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'a&d"': {'inputs': [], 'name': 'test_AssumePayable', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\r+\xf66': {'inputs': [], 'name': 'test_BytesToUint', 'outputs': [], 'stateMutability': 'pure', 'type': 'function'}, b'x\xd5ji': {'inputs': [], 'name': 'test_ChangePrankMsgSender', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'f\xa3\x88\x88': {'inputs': [], 'name': 'test_ChangePrankMsgSenderAndTxOrigin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x05\x8a\xeb>': {'inputs': [], 'name': 'test_Deal', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xbf\xac\x85\xa4': {'inputs': [], 'name': 'test_DealERC1155Token', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf1\x1d\xfb`': {'inputs': [], 'name': 'test_DealERC1155TokenAdjustTotalSupply', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd3\x1d|\x1d': {'inputs': [], 'name': 'test_DealERC721Token', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x97U\x84;': {'inputs': [], 'name': 'test_DealToken', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Y\xff\x1d\x87': {'inputs': [], 'name': 'test_DealTokenAdjustTotalSupply', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\n\xd2\xb4\xc8': {'inputs': [], 'name': 'test_DeployCode', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf90\xb6(': {'inputs': [], 'name': 'test_DeployCodeNoArgs', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'4\x13\x06\xd5': {'inputs': [], 'name': 'test_DeployCodeTo', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xbb\x11\xac\x10': {'inputs': [], 'name': 'test_DeployCodeVal', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'A<\xfc\xb1': {'inputs': [], 'name': 'test_DeployCodeValNoArgs', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'*\xc9\xee\xdb': {'inputs': [], 'name': 'test_DeriveRememberKey', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'D@\xc5E': {'inputs': [], 'name': 'test_DestroyAccount', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x893)\xac': {'inputs': [], 'name': 'test_GasMeteringModifier', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xbf\xc4 \xf1': {'inputs': [], 'name': 'test_Hoax', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xcf\xcd\x8cE': {'inputs': [], 'name': 'test_HoaxDifferentAddresses', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'm\xc2\x87\x8a': {'inputs': [], 'name': 'test_HoaxOrigin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x00\xab\xe4\t': {'inputs': [], 'name': 'test_MakeAccountEquivalence', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x9dD\xb7\x8a': {'inputs': [], 'name': 'test_MakeAddrEquivalence', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xaeB\x82g': {'inputs': [], 'name': 'test_MakeAddrSigning', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xbd\x9f\xb2Y': {'inputs': [], 'name': 'test_ParseJsonTxDetail', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\xae\r\xdb\xc8': {'inputs': [], 'name': 'test_ReadEIP1559Transaction', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\xcf\x99\xd3\xdd': {'inputs': [], 'name': 'test_ReadEIP1559Transactions', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'"\xb4\xdeQ': {'inputs': [], 'name': 'test_ReadReceipt', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\x99\xc8|U': {'inputs': [], 'name': 'test_ReadReceipts', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\xc4\x9e\xb4\xc7': {'inputs': [], 'name': 'test_RevertIf_CannotDeployCodeTo', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'iT\xeeP': {'inputs': [], 'name': 'test_RevertIf_DeployCodeFail', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd9+\x84\xb0': {'inputs': [], 'name': 'test_Rewind', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xc5Kci': {'inputs': [], 'name': 'test_Skip', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x1dN\\\x12': {'inputs': [], 'name': 'test_StartHoax', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'X\xe8%{': {'inputs': [], 'name': 'test_StartHoaxOrigin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":61,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"stdstore","offset":0,"slot":0,"type":"t_struct(StdStorage)8017_storage"},{"astId":218,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_failed","offset":0,"slot":8,"type":"t_bool"},{"astId":2719,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"stdChainsInitialized","offset":1,"slot":8,"type":"t_bool"},{"astId":2740,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"chains","offset":0,"slot":9,"type":"t_mapping(t_string_memory_ptr,t_struct(Chain)2735_storage)"},{"astId":2744,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"defaultRpcUrls","offset":0,"slot":10,"type":"t_mapping(t_string_memory_ptr,t_string_storage)"},{"astId":2748,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"idToAlias","offset":0,"slot":11,"type":"t_mapping(t_uint256,t_string_storage)"},{"astId":2751,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"fallbackToDefaultRpcUrls","offset":0,"slot":12,"type":"t_bool"},{"astId":3680,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"gasMeteringOff","offset":1,"slot":12,"type":"t_bool"},{"astId":5747,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"stdstore","offset":0,"slot":13,"type":"t_struct(StdStorage)8017_storage"},{"astId":6623,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_excludedContracts","offset":0,"slot":21,"type":"t_array(t_address)dyn_storage"},{"astId":6626,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_excludedSenders","offset":0,"slot":22,"type":"t_array(t_address)dyn_storage"},{"astId":6629,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_targetedContracts","offset":0,"slot":23,"type":"t_array(t_address)dyn_storage"},{"astId":6632,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_targetedSenders","offset":0,"slot":24,"type":"t_array(t_address)dyn_storage"},{"astId":6635,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_excludedArtifacts","offset":0,"slot":25,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6638,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_targetedArtifacts","offset":0,"slot":26,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6642,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_targetedArtifactSelectors","offset":0,"slot":27,"type":"t_array(t_struct(FuzzArtifactSelector)6614_storage)dyn_storage"},{"astId":6646,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_excludedSelectors","offset":0,"slot":28,"type":"t_array(t_struct(FuzzSelector)6608_storage)dyn_storage"},{"astId":6650,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_targetedSelectors","offset":0,"slot":29,"type":"t_array(t_struct(FuzzSelector)6608_storage)dyn_storage"},{"astId":6654,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_targetedInterfaces","offset":0,"slot":30,"type":"t_array(t_struct(FuzzInterface)6620_storage)dyn_storage"},{"astId":12907,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"IS_TEST","offset":0,"slot":31,"type":"t_bool"},{"astId":39159,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"test","offset":1,"slot":31,"type":"t_contract(Bar)41358"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_address)dyn_storage":{"encoding":"dynamic_array","label":"address[]","numberOfBytes":32,"base":"t_address"},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_array(t_bytes4)dyn_storage":{"encoding":"dynamic_array","label":"bytes4[]","numberOfBytes":32,"base":"t_bytes4"},"t_array(t_string_storage)dyn_storage":{"encoding":"dynamic_array","label":"string[]","numberOfBytes":32,"base":"t_string_storage"},"t_array(t_struct(FuzzArtifactSelector)6614_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzArtifactSelector[]","numberOfBytes":32,"base":"t_struct(FuzzArtifactSelector)6614_storage"},"t_array(t_struct(FuzzInterface)6620_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzInterface[]","numberOfBytes":32,"base":"t_struct(FuzzInterface)6620_storage"},"t_array(t_struct(FuzzSelector)6608_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzSelector[]","numberOfBytes":32,"base":"t_struct(FuzzSelector)6608_storage"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_contract(Bar)41358":{"encoding":"inplace","label":"contract Bar","numberOfBytes":20},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage))"},"t_mapping(t_bytes32,t_struct(FindData)7992_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)7992_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)7992_storage)"},"t_mapping(t_string_memory_ptr,t_string_storage)":{"encoding":"mapping","label":"mapping(string => string)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_string_storage"},"t_mapping(t_string_memory_ptr,t_struct(Chain)2735_storage)":{"encoding":"mapping","label":"mapping(string => struct StdChains.Chain)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_struct(Chain)2735_storage"},"t_mapping(t_uint256,t_string_storage)":{"encoding":"mapping","label":"mapping(uint256 => string)","numberOfBytes":32,"key":"t_uint256","value":"t_string_storage"},"t_string_memory_ptr":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(Chain)2735_storage":{"encoding":"inplace","label":"struct StdChains.Chain","numberOfBytes":128,"members":[{"astId":2728,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"name","offset":0,"slot":0,"type":"t_string_storage"},{"astId":2730,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"chainId","offset":0,"slot":1,"type":"t_uint256"},{"astId":2732,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"chainAlias","offset":0,"slot":2,"type":"t_string_storage"},{"astId":2734,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"rpcUrl","offset":0,"slot":3,"type":"t_string_storage"}]},"t_struct(FindData)7992_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":7985,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":7987,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":7989,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":7991,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(FuzzArtifactSelector)6614_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzArtifactSelector","numberOfBytes":64,"members":[{"astId":6610,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"artifact","offset":0,"slot":0,"type":"t_string_storage"},{"astId":6613,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(FuzzInterface)6620_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzInterface","numberOfBytes":64,"members":[{"astId":6616,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6619,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"artifacts","offset":0,"slot":1,"type":"t_array(t_string_storage)dyn_storage"}]},"t_struct(FuzzSelector)6608_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzSelector","numberOfBytes":64,"members":[{"astId":6604,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6607,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(StdStorage)8017_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":8001,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage)))"},{"astId":8004,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":8006,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":8008,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":8010,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":8012,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":8014,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":8016,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsTest","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60808060405234602f57600160ff19600c541617600c55600160ff19601f541617601f5561cc4b90816100348239f35b5f80fdfe60806040526004361015610011575f80fd5b5f5f3560e01c8062abe409146163d4578063058aeb3e146163455780630a9254e4146162de5780630ad2b4c8146161ac5780630d2bf63614615f835780631d4e5c1214615d835780631ed7831c14615d0557806322b4de5114615aef5780632ac9eedb146159115780632ade388014615752578063341306d51461528c5780633e5e3c231461520e5780633f7286f414615190578063413cfcb1146150815780634440c54514614b615780634a1297f8146149245780634af967d1146148b157806358e8257b1461467e57806359ff1d871461427c5780636126642214613f5157806366a3888814613bf657806366d9a9a014613acd5780636954ee50146139905780636dc2878a14613865578063751ec69d146137db57806378d56a691461334c57806385226c81146132ba578063893329ac1461317f578063916a17c6146130d75780639755843b14612fe257806399c87c5514612dbb5780639bacb2a814612aec5780639d44b78a14612abb5780639d624fa1146124bd578063ae0ddbc8146122d0578063ae428267146121a8578063b0464fdc14612100578063b5508aa914612067578063ba414fa614612042578063bb11ac1014611ecb578063bd9fb25914611afa578063bfac85a4146119e6578063bfc420f1146118c2578063c49eb4c714611810578063c54b63691461167b578063ce73c44914611456578063cf99d3dd146111b7578063cfcd8c4514611083578063d31d7c1d14610a8d578063d92b84b0146108cf578063e20c9f7114610841578063f11dfb60146102dd578063f930b628146102905763fa7626d41461026b575f80fd5b3461028d578060031936011261028d57602060ff601f54166040519015158152f35b80fd5b503461028d578060031936011261028d576102da6102bc6102b76102b26166f2565b617880565b6172b4565b601f546102d49060081c6001600160a01b03166172b4565b906172f9565b80f35b503461028d578060031936011261028d57604051610140808201908282106001600160401b0383111761082d5790829161ca968339039082f080156108205760018060a01b031681806040516020810190627eeac760e11b825230602482015282604482015260448152610352606482616545565b5190845afa50610360617806565b6020815191818082019384920101031261067b5751601180546001600160a01b03191683179055600f805463ffffffff191662fdd58e1790556103a23061a6e5565b6103ab8361a6e5565b6103be69021e19e0c9bab240000061a761565b8280604051602081019063bd85b03960e01b8252826024820152602481526103e7604482616545565b5190855afa506103f5617806565b805115610701576020815191818082019384920101031261067b5751808269021e19e0c9bab2400000105f146107f2575069021e19e0c9bab23fffff1982019182116106ed5761047b9161044891616b44565b601180546001600160a01b03191684179055600f805463ffffffff191663bd85b0391790556104768461a6e5565b61a761565b604051627eeac760e11b815230600482015260248101839052602081604481855afa80156106c55783906107be575b6104b49150617163565b60405163bd85b03960e01b815260048101839052602081602481855afa80156106c557839061078a575b6104e891506171bc565b81806040516020810190627eeac760e11b825230602482015282604482015260448152610516606482616545565b5190845afa50610524617806565b6020815191818082019384920101031261067b5751601180546001600160a01b03191683179055600f805463ffffffff191662fdd58e1790556105663061a6e5565b61056f8361a6e5565b6105788361a761565b8280604051602081019063bd85b03960e01b8252826024820152602481526105a1604482616545565b5190855afa506105af617806565b805115610701576020815191818082019384920101031261067b57518082156106d057506105e09161044891616b44565b604051627eeac760e11b815230600482015260248101839052602081604481855afa9081156106c5578391610692575b5060249161061f602092617114565b6040519283809263bd85b03960e01b82528660048301525afa801561068757829061064f575b6102da9150617163565b506020813d60201161067f575b8161066960209383616545565b8101031261067b576102da9051610645565b5f80fd5b3d915061065c565b6040513d84823e3d90fd5b90506020813d6020116106bd575b816106ad60209383616545565b8101031261067b57516024610610565b3d91506106a0565b6040513d85823e3d90fd5b918403919050816106ed576105e0916106e891616921565b610448565b634e487b7160e01b84526011600452602484fd5b60405162461bcd60e51b815260206004820152605560248201527f537464436865617473206465616c28616464726573732c616464726573732c7560448201527f696e742c75696e742c626f6f6c293a2074617267657420636f6e74726163742060648201527434b9903737ba1022a92198989a9aa9bab838363c9760591b608482015260a490fd5b506020813d6020116107b6575b816107a460209383616545565b8101031261067b576104e890516104de565b3d9150610797565b506020813d6020116107ea575b816107d860209383616545565b8101031261067b576104b490516104aa565b3d91506107cb565b91905069021e19e0c9bab2400000039069021e19e0c9bab240000082116106ed5761047b916106e891616921565b50604051903d90823e3d90fd5b634e487b7160e01b84526041600452602484fd5b503461028d578060031936011261028d5760405160158054808352908352909160208301917f55f448fdea98c4d29eb340757ef0a66cd03dbb9538908a6a81d96026b71ec475915b8181106108b0576108ac856108a081870382616545565b60405191829182616442565b0390f35b82546001600160a01b0316845260209093019260019283019201610889565b503461028d578060031936011261028d575f51602061cbf65f395f51905f523b1561028d576040516372eb5f8160e11b81526064600482015281908181602481835f51602061cbf65f395f51905f525af1801561068757610a78575b505060405163796b89b960e01b81526020816004815f51602061cbf65f395f51905f525afa908115610687578291610a46575b506018198101908111610a325781905f51602061cbf65f395f51905f523b15610a2f57604051906372eb5f8160e11b825260048201528181602481835f51602061cbf65f395f51905f525af1801561068757610a1a575b50505f51602061cbf65f395f51905f523b1561028d5760405163260a5b1560e21b8152426004820152604b6024820152819081816044815f51602061cbf65f395f51905f525afa801561068757610a095750f35b81610a1391616545565b61028d5780f35b81610a2491616545565b61028d57805f6109b5565b50fd5b634e487b7160e01b82526011600452602482fd5b90506020813d602011610a70575b81610a6160209383616545565b8101031261067b57515f61095e565b3d9150610a54565b81610a8291616545565b61028d57805f61092b565b503461028d578060031936011261028d576040516101a3808201908282106001600160401b0383111761082d5790829161c1f68339039082f080156108205760018060a01b0316818060405160208101906331a9108f60e11b82526001602482015260248152610afe604482616545565b5190845afa610b0b617806565b9015610fb4578051908380610b2860208085019585010185618113565b6040516370a0823160e01b602082019081526001600160a01b039092166024808301919091528152610b5b604482616545565b5190865afa50610b69617806565b6020815191818082019384920101031261067b575190848060405160208101906370a0823160e01b82526002602482015260248152610ba9604482616545565b5190875afa50610bb7617806565b916020835193818082019586920101031261067b579151601180546001600160a01b03191686179055600f805463ffffffff19166370a0823117905581519093610c2793610476939092610c22926001600160a01b0392610c1c920160200190618113565b1661a6e5565b618132565b601180546001600160a01b03191683179055600f805463ffffffff19166370a08231179055610c56600261a6e5565b5f198114610fa0576001610c6a910161a761565b601180546001600160a01b03191682179055600f805463ffffffff1916636352211e179055610c99600161a6e5565b610ca3600261a761565b6040516370a0823160e01b815260026004820152602081602481855afa80156106c557839061104f575b610cd79150617215565b6040516370a0823160e01b815260016004820152602081602481855afa80156106c557839061101b575b610d0b9150617114565b818060405160208101906331a9108f60e11b82526002602482015260248152610d35604482616545565b5190845afa610d42617806565b9015610fb4578051908380610d5f60208085019585010185618113565b6040516370a0823160e01b602082019081526001600160a01b039092166024808301919091528152610d92604482616545565b5190865afa50610da0617806565b6020815191818082019384920101031261067b575190848060405160208101906370a0823160e01b82526001602482015260248152610de0604482616545565b5190875afa50610dee617806565b916020835193818082019586920101031261067b579151601180546001600160a01b03191686179055600f805463ffffffff19166370a0823117905581519093610e5393610476939092610c22926001600160a01b0392610c1c920160200190618113565b601180546001600160a01b03191683179055600f805463ffffffff19166370a08231179055610e82600161a6e5565b5f198114610fa0576001610e96910161a761565b601180546001600160a01b03191682179055600f805463ffffffff1916636352211e179055610ec5600261a6e5565b610ecf600161a761565b6040516370a0823160e01b815260016004820152602081602481855afa9081156106c5578391610f6d575b50602491610f09602092617215565b604051928380926370a0823160e01b82528060048301525afa8015610687578290610f39575b6102da9150617215565b506020813d602011610f65575b81610f5360209383616545565b8101031261067b576102da9051610f2f565b3d9150610f46565b90506020813d602011610f98575b81610f8860209383616545565b8101031261067b57516024610efa565b3d9150610f7b565b634e487b7160e01b83526011600452602483fd5b60405162461bcd60e51b815260206004820152603960248201527f537464436865617473206465616c28616464726573732c616464726573732c7560448201527834b73a163137b7b6149d1034b2103737ba1036b4b73a32b21760391b6064820152608490fd5b506020813d602011611047575b8161103560209383616545565b8101031261067b57610d0b9051610d01565b3d9150611028565b506020813d60201161107b575b8161106960209383616545565b8101031261067b57610cd79051610ccd565b3d915061105c565b503461028d578060031936011261028d575f51602061cbf65f395f51905f523b1561028d5760405163c88a5e6d60e01b81526105396004820152600160801b602482015281908181604481835f51602061cbf65f395f51905f525af18015610687576111a2575b50505f51602061cbf65f395f51905f523b1561028d576040516323f2866760e11b81526105396004820152611ca3602482015281908181604481835f51602061cbf65f395f51905f525af180156106875761118d575b50601f5460081c6001600160a01b0316803b15610a2f57816064916044604051809481936354d9714560e11b83526105396004840152611ca360248401525af1801561068757610a095750f35b8161119791616545565b61028d57805f611140565b816111ac91616545565b61028d57805f6110ea565b503461028d578060031936011261028d57604051636c98507360e11b81528180826004815f51602061cbf65f395f51905f525afa918215610820576112299261120791839161143c575b506167a1565b604051809381926360f9bb1160e01b8352602060048401526024830190616484565b03815f51602061cbf65f395f51905f525afa90811561068757918091611273938291611422575b50604080516385940ef160e01b8152600481018290529485926044840190616484565b6c2e7472616e73616374696f6e7360981b60208483039260031984016024870152600d8152015201815f51602061cbf65f395f51905f525afa9182156108205781926113fe575b5081518201916020818185019403126113f6576020810151906001600160401b0382116113fa57019180603f840112156113f6576020830151926112fd846167fb565b9361130b6040519586616545565b8085526020808087019260051b84010101918383116113f25760408101915b8383106113bf578651868861133e836167fb565b9261134c6040519485616545565b80845261135b601f19916167fb565b01825b8181106113a8575050815b81518110156113a45780611388611382600193856183ea565b5161a392565b61139282876183ea565b5261139d81866183ea565b5001611369565b8280f35b6020906113b3617ef8565b8282880101520161135e565b82516001600160401b0381116113ee576020916113e3878480809588010101617f35565b81520192019161132a565b8680fd5b8480fd5b5080fd5b8280fd5b61141b9192503d8084833e6114138183616545565b810190616767565b905f6112ba565b61143691503d8084833e6114138183616545565b5f611250565b61145091503d8085833e6114138183616545565b5f611201565b503461028d578060031936011261028d5760405190611476606083616545565b602182527f5374644368656174732e742e736f6c3a526576657274696e67436f6e747261636020830152601d60fa1b60408301526114e360209282604051916114bf8684616545565b81835260405180948192638d1cc92560e01b83528860048401526024830190616484565b03815f51602061cbf65f395f51905f525afa9182156106c5579184611542928194869361165d575b5081906040519584879551918291018487015e840190828201888152815193849201905e010184815203601f198101835282616545565b5f51602061cbf65f395f51905f523b156113f657816115839160405180938192635a6b63c160e11b8352846004840152604060248401526044830190616484565b0381835f51602061cbf65f395f51905f525af1801561068757908291611648575b5080808080805af16115b4617806565b901561161d5781905f51602061cbf65f395f51905f523b15610a2f57816115fd9160405180938192635a6b63c160e11b8352846004840152604060248401526044830190616484565b0381835f51602061cbf65f395f51905f525af1801561068757610a095750f35b60405162461bcd60e51b8152600481018490526058602482015260a49061164660448201616e6c565bfd5b8161165291616545565b61028d57805f6115a4565b82919350611674903d8089833e6114138183616545565b929061150b565b503461028d578060031936011261028d575f51602061cbf65f395f51905f523b1561028d576040516372eb5f8160e11b81526064600482015281908181602481835f51602061cbf65f395f51905f525af18015610687576117fb575b505060405163796b89b960e01b81526020816004815f51602061cbf65f395f51905f525afa9081156106875782916117c9575b5060198101809111610a325781905f51602061cbf65f395f51905f523b15610a2f57604051906372eb5f8160e11b825260048201528181602481835f51602061cbf65f395f51905f525af18015610687576117b4575b50505f51602061cbf65f395f51905f523b1561028d5760405163260a5b1560e21b8152426004820152607d6024820152819081816044815f51602061cbf65f395f51905f525afa801561068757610a095750f35b816117be91616545565b61028d57805f611760565b90506020813d6020116117f3575b816117e460209383616545565b8101031261067b57515f61170a565b3d91506117d7565b8161180591616545565b61028d57805f6116d7565b503461028d578060031936011261028d575f51602061cbf65f395f51905f523b1561028d5760405163f28dceb360e01b81526020600482015260586024820152819061185e60448201616e6c565b818160a481835f51602061cbf65f395f51905f525af18015610687576118ad575b5050303b1561028d5760405163ce73c44960e01b81528190818160048183305af1801561068757610a095750f35b816118b791616545565b61028d57805f61187f565b503461028d578060031936011261028d575f51602061cbf65f395f51905f523b1561028d5760405163c88a5e6d60e01b81526105396004820152600160801b602482015281908181604481835f51602061cbf65f395f51905f525af18015610687576119d1575b50505f51602061cbf65f395f51905f523b1561028d5760405163ca669fa760e01b8152610539600482015281908181602481835f51602061cbf65f395f51905f525af18015610687576119bc575b50601f5460081c6001600160a01b0316803b15610a2f578160649160246040518094819363646ea56d60e01b835261053960048401525af1801561068757610a095750f35b816119c691616545565b61028d57805f611977565b816119db91616545565b61028d57805f611929565b503461028d578060031936011261028d57604051610140808201908282106001600160401b0383111761082d5790829161ca968339039082f0801561082057602060449160018060a01b0316838060405184810190627eeac760e11b82523060248201528287820152868152611a5d606482616545565b5190845afa50611a7c611a6e617806565b8380825183010191016168e6565b50601180546001600160a01b03191682179055600f805463ffffffff191662fdd58e179055611aaa3061a6e5565b611ab38461a6e5565b611ac669021e19e0c9bab240000061a761565b60405192838092627eeac760e11b82523060048301528660248301525afa801561068757829061064f576102da9150617163565b503461028d578060031936011261028d57604051636c98507360e11b81528180826004815f51602061cbf65f395f51905f525afa91821561082057611b499261120791839161143c57506167a1565b03815f51602061cbf65f395f51905f525afa908115610687578291611eb1575b5081611bb981604093845190611b7f8683616545565b601382527205ce8e4c2dce6c2c6e8d2dedce6b660ba5ce8f606b1b602083015285516385940ef160e01b81529384928392600484016172d4565b03815f51602061cbf65f395f51905f525afa908115611ea4578291611e8a575b5080518101906020818303126113fa576020810151906001600160401b038211611e86576020611c119281611c169501920101616ca6565b618085565b82810151909290611c2f906001600160a01b0316616ff5565b60a08301516001600160a01b03165f51602061cbf65f395f51905f523b156113fa578151906328a9b0fb60e11b8252600482015273e7f1725e7734ce288f8367e1bb143e90bb3f0512602482015282816044815f51602061cbf65f395f51905f525afa8015611e5057908391611e71575b505060208301518151611d0b91611cb961010083616545565b60c482526323e9918760e01b6020830152600160e01b8483015261133760e01b6060830152600360e51b6080830152600160e11b60a0830152600360e01b60c0830152600160e21b60e0830152617793565b60808301515f51602061cbf65f395f51905f523b156113fa5781519063260a5b1560e21b825260048201526003602482015282816044815f51602061cbf65f395f51905f525afa8015611e5057908391611e5c575b505060c08301515f51602061cbf65f395f51905f523b156113fa5781519063260a5b1560e21b825260048201526002602482015282816044815f51602061cbf65f395f51905f525afa8015611e5057908391611e3b575b50506060830151905f51602061cbf65f395f51905f523b156113fa5780519163260a5b1560e21b835260048301526173b9602483015282826044815f51602061cbf65f395f51905f525afa908115611e325750611e1d575b506102da60e0830151617114565b81611e2791616545565b6113f657815f611e0f565b513d84823e3d90fd5b81611e4591616545565b6113f657815f611db7565b505051903d90823e3d90fd5b81611e6691616545565b6113f657815f611d60565b81611e7b91616545565b6113f657815f611ca0565b8380fd5b611e9e91503d8084833e6114138183616545565b5f611bd9565b50505051903d90823e3d90fd5b611ec591503d8084833e6114138183616545565b5f611b69565b503461028d578060031936011261028d576020604051611eeb8282616545565b828152611f1b83611efa6166f2565b60405180938192638d1cc92560e01b83528760048401526024830190616484565b03815f51602061cbf65f395f51905f525afa9182156120375783918593612017575b50611f7a90826040519384928180850197805191829101895e8401908282018a8152815193849201905e010186815203601f198101835282616545565b5190670de0b6b3a7640000f0906001600160a01b03821615611fad575080611fa76102bc6102da936172b4565b316170bd565b6084906040519062461bcd60e51b82526004820152603e60248201527f537464436865617473206465706c6f79436f646528737472696e672c6279746560448201527f732c75696e74323536293a204465706c6f796d656e74206661696c65642e00006064820152fd5b611f7a919350612030903d8088833e6114138183616545565b9290611f3d565b6040513d86823e3d90fd5b503461028d578060031936011261028d57602061205d616b9a565b6040519015158152f35b503461028d578060031936011261028d57601954612084816167fb565b916120926040519384616545565b818352601981527f944998273e477b495144fb8794c914197f3ccb46be2900f4698fd0ef743c9695602084015b8383106120d457604051806108ac87826165de565b6001602081926040516120f2816120eb818961684a565b0382616545565b8152019201920191906120bf565b503461028d578060031936011261028d57601c5461211d816167fb565b9161212b6040519384616545565b818352601c81527f0e4562a10381dec21b205ed72637e6b1b523bdd0e4d4d50af5cd23dd4500a211602084015b83831061216d57604051806108ac878261663d565b60026020600192604051612180816164a8565b848060a01b038654168152612196858701616942565b83820152815201920192019190612158565b503461028d578060031936011261028d576121c96121c46166d0565b616ed8565b604051906338d07aa960e21b825260048201527f417f0084d1239e904e5e1c4d803baeec5639aa1e2e2344de049fc5246f88b7a86024820152826060826044815f51602061cbf65f395f51905f525afa801561082057819282908392612281575b509260809160209460ff604051937f417f0084d1239e904e5e1c4d803baeec5639aa1e2e2344de049fc5246f88b7a8855216868401526040830152606082015282805260015afa15610820576102da908251617062565b93505050506060813d6060116122c8575b8161229f60609383616545565b810103126113fa5782815160ff811681036113f65760208084015160409094015191939061222a565b3d9150612292565b503461028d578060031936011261028d57604051636c98507360e11b81528180826004815f51602061cbf65f395f51905f525afa9182156108205761234a9261231f91839161143c57506167a1565b612327617ef8565b50604051809381926360f9bb1160e01b8352602060048401526024830190616484565b03815f51602061cbf65f395f51905f525afa9081156106875782916124a3575b50816040519163348051d760e11b835281600484015281836024815f51602061cbf65f395f51905f525afa908115610687576123f36001602e60209461240e978791612489575b506040519586916d2e7472616e73616374696f6e735b60901b828401528051918291018484015e8101605d60f81b838201520301601e19810185520183616545565b6040516385940ef160e01b81529384928392600484016172d4565b03815f51602061cbf65f395f51905f525afa90811561068757829161246f575b5080518101906020818303126113fa576020810151906001600160401b038211611e86576020612466928161246b9501920101617f35565b61a392565b5080f35b61248391503d8084833e6114138183616545565b5f61242e565b61249d91503d8089833e6114138183616545565b5f6123b1565b6124b791503d8084833e6114138183616545565b5f61236a565b503461028d57602036600319011261028d576004356001600160a01b0381168082036113fa576124eb616b51565b916124f4617b03565b50825115612a4457612504619b36565b604051926003815194602081818501978089835e8101600981520301902094604051926125308461650f565b604051612541816120eb818b61684a565b845261258360018801549760208601988952604051612567816120eb816002860161684a565b604087015261257c604051809681930161684a565b0384616545565b6060840192835261260d87511515604051907f537464436861696e7320676574436861696e28737472696e67293a204368616960208301526d37103bb4ba341030b634b0b9901160911b6040830152612608600c604e848751808a8484015e81016b11103737ba103337bab7321760a11b838201520301601319810185520183616545565b617b65565b612615617b03565b508251511561267d575b505050906102da9361263392505190617b95565b6001811090811561265e575b811561264c575b50617835565b610800602160991b011090505f612646565b90506009811180612670575b9061263f565b50602160991b811061266a565b93919590949260405163975a6ce960e01b8152602060048201528881806126a7602482018a616484565b03815f51602061cbf65f395f51905f525afa899181612a28575b50612a1357506126cf617806565b6126d9865161a3e4565b96895b875181101561277c576126ef818961734e565b516001600160f81b03198116606160f81b8110158061276e575b15612757575060f81c601f190160ff8111612743576001919060f81b6001600160f81b0319168c1a61273b828c61734e565b535b016126dc565b634e487b7160e01b8c52601160045260248cfd5b60019291508c1a612768828c61734e565b5361273d565b50603d60f91b811115612709565b5091949790929593966127c06008602080936040519481869251918291018484015e81016717d49410d7d5549360c21b838201520301601719810184520182616545565b8960ff600c54165f146129aa5761280d60405160208189518089835e8101600a8152030190209261281f60405194859384936334515cdb60e21b8552604060048601526044850190616484565b8381036003190160248501529061684a565b03815f51602061cbf65f395f51905f525afa90811561299f578a91612985575b5081525b604051936f034b73b30b634b210393831903ab936160851b6020860152612884603086835180878484015e81018d838201520301601f198101875286616545565b6128ff6031604051926128c2846128b4602082019a630bc4450360e01b8c52602060248401526044830190616484565b03601f198101865285616545565b60405195869170034b73b30b634b210393831903ab9361d1607d1b60208401525180918484015e81018d838201520301601f198101855284616545565b6040519261292a846128b4602082019363eeaa9e6f60e01b8552602060248401526044830190616484565b845195866020870120925190208214159384612976575b505050811561296b575b5061296657505091612633916102da94935b9192819561261f565b602001fd5b90505151155f61294b565b519020141591505f8080612941565b61299991503d808c833e6114138183616545565b5f61283f565b6040513d8c823e3d90fd5b60405163f877cb1960e01b81526020600482015291829081906129d1906024830190616484565b03815f51602061cbf65f395f51905f525afa90811561299f578a916129f9575b508152612843565b612a0d91503d808c833e6114138183616545565b5f6129f1565b90919293955061263394506102da965261295d565b612a3d9192503d808c833e6114138183616545565b905f6126c1565b60405162461bcd60e51b815260206004820152604360248201527f537464436861696e7320676574436861696e28737472696e67293a204368616960448201527f6e20616c6961732063616e6e6f742062652074686520656d707479207374726960648201526237339760e91b608482015260a490fd5b503461028d578060031936011261028d576102da612ada6121c46166d0565b50612ae66121c46166d0565b50617062565b503461028d578060031936011261028d576040516106a5808201908282106001600160401b0383111761082d5790829161c3998339039082f08015610820576001600160a01b031690813b1561028d5760405162be639d60e51b81525f51602061cbf65f395f51905f526004820152818160248183875af1801561068757908291612da6575b5050813b1561028d5760405162be639d60e51b81526a636f6e736f6c652e6c6f676004820152818160248183875af1801561068757908291612d91575b5050813b1561028d5760405162be639d60e51b8152734e59b44847b379578588920ca78fbf26c0b4956c6004820152818160248183875af1801561068757908291612d7c575b50505f51602061cbf65f395f51905f523b1561028d57604051633d21120560e21b81528181600481835f51602061cbf65f395f51905f525af1801561068757908291612d67575b5050813b1561028d5760405162be639d60e51b815273d8da6bf26964af9d7eed9e03e53415d37aa960456004820152818160248183875af1801561068757908291612d52575b505060405191605892838101938185106001600160401b0386111761082d578394829161ca3e8339039083f08015610687575f51602061cbf65f395f51905f523b15612d3957604051633d21120560e21b81528381600481835f51602061cbf65f395f51905f525af1908115612037578491612d3d575b5050813b15612d395760405162be639d60e51b81526001600160a01b0390911660048201529082908290602490829084905af1801561068757610a095750f35b5050fd5b81612d4791616545565b612d3957825f612cf9565b81612d5c91616545565b61028d57805f612c82565b81612d7191616545565b61028d57805f612c3c565b81612d8691616545565b61028d57805f612bf5565b81612d9b91616545565b61028d57805f612baf565b81612db091616545565b61028d57805f612b72565b503461028d578060031936011261028d57604051636c98507360e11b81528180826004815f51602061cbf65f395f51905f525afa91821561082057612e0a9261120791839161143c57506167a1565b03815f51602061cbf65f395f51905f525afa90811561068757918091612e539382916114225750604080516385940ef160e01b8152600481018290529485926044840190616484565b682e726563656970747360b81b6020848303926003198401602487015260098152015201815f51602061cbf65f395f51905f525afa918215610820578192612fc6575b5081518201916020818185019403126113f6576020810151906001600160401b0382116113fa57019180603f840112156113f657602083015192612ed9846167fb565b93612ee76040519586616545565b8085526020808087019260051b84010101918383116113f25760408101915b838310612f975786518688612f1a836167fb565b92612f286040519485616545565b808452612f37601f19916167fb565b01825b818110612f80575050815b81518110156113a45780612f64612f5e600193856183ea565b5161813e565b612f6e82876183ea565b52612f7981866183ea565b5001612f45565b602090612f8b6173fa565b82828801015201612f3a565b82516001600160401b0381116113ee57602091612fbb87848080958801010161745b565b815201920191612f06565b612fdb9192503d8084833e6114138183616545565b905f612e96565b503461028d578060031936011261028d576040516101fc808201908282106001600160401b0383111761082d5790829161bffa8339039082f0801561082057602060249160018060a01b03168380604051848101906370a0823160e01b82523087820152868152613054604482616545565b5190845afa50613065611a6e617806565b50601180546001600160a01b03191682179055600f805463ffffffff19166370a082311790556130943061a6e5565b6130a769021e19e0c9bab240000061a761565b6040516370a0823160e01b815230600482015292839182905afa801561068757829061064f576102da9150617163565b503461028d578060031936011261028d57601d546130f4816167fb565b916131026040519384616545565b818352601d81527f6d4407e7be21f808e6509aa9fa9143369579dd7d760fe20a2c09680fc146134f602084015b83831061314457604051806108ac878261663d565b60026020600192604051613157816164a8565b848060a01b03865416815261316d858701616942565b8382015281520192019201919061312f565b503461028d578060031936011261028d576131a45a61319c617a01565b505a90616b44565b6131b05a61319c617a25565b905a5f51602061cbf65f395f51905f523b15611e865760405163d1a5b36f60e01b815284908181600481835f51602061cbf65f395f51905f525af18015610687576132a5575b505060ff600c5461010061ff0019821617600c55613212617a25565b5060081c161561323a575b6102da9261322f613234925a90616b44565b616921565b10617835565b61ff0019600c5416600c555f51602061cbf65f395f51905f523b15611e865760405163015e6a8760e51b815284908181600481835f51602061cbf65f395f51905f525af1801561068757613290575b505061321d565b8161329a91616545565b611e8657835f613289565b816132af91616545565b611e8657835f6131f6565b503461028d578060031936011261028d57601a546132d7816167fb565b916132e56040519384616545565b818352601a81527f057c384a7d1c54f3a1b2e5e67b2617b8224fdfd1ea7234eea573a6ff665ff63e602084015b83831061332757604051806108ac87826165de565b60016020819260405161333e816120eb818961684a565b815201920192019190613312565b503461028d578060031936011261028d575f51602061cbf65f395f51905f523b1561028d576040516303223eab60e11b8152610539600482015281908181602481835f51602061cbf65f395f51905f525af18015610687576137c6575b50601f5460081c6001600160a01b0316803b15610a2f5781809160246040518094819363646ea56d60e01b835261053960048401525af18015610687576137b1575b505080806040516133fd606082616545565b603c81527f6368616e67655072616e6b20697320646570726563617465642e20506c65617360208201527f652075736520766d2e73746172745072616e6b20696e73746561642e00000000604082015260405161348581613477602082019463104c13eb60e21b8652602060248401526044830190616484565b03601f198101835282616545565b51906a636f6e736f6c652e6c6f675afa5061349e617806565b505f51602061cbf65f395f51905f523b1561028d576040516390c5013b60e01b815281908181600481835f51602061cbf65f395f51905f525af180156106875761379c575b50505f51602061cbf65f395f51905f523b1561028d576040516303223eab60e11b815261dead600482015281908181602481835f51602061cbf65f395f51905f525af1801561068757613787575b50601f5460081c6001600160a01b0316803b15610a2f5781809160246040518094819363646ea56d60e01b835261dead60048401525af1801561068757613772575b5080604051613583606082616545565b603c81527f6368616e67655072616e6b20697320646570726563617465642e20506c65617360208201527f652075736520766d2e73746172745072616e6b20696e73746561642e0000000060408201526040516135fd81613477602082019463104c13eb60e21b8652602060248401526044830190616484565b51906a636f6e736f6c652e6c6f675afa50613616617806565b505f51602061cbf65f395f51905f523b1561028d576040516390c5013b60e01b815281908181600481835f51602061cbf65f395f51905f525af180156106875761375d575b50505f51602061cbf65f395f51905f523b1561028d576040516303223eab60e11b8152610539600482015281908181602481835f51602061cbf65f395f51905f525af1801561068757613748575b50601f5460081c6001600160a01b0316803b15610a2f5781809160246040518094819363646ea56d60e01b835261053960048401525af1801561068757613733575b50505f51602061cbf65f395f51905f523b1561028d576040516390c5013b60e01b815281908181600481835f51602061cbf65f395f51905f525af1801561068757610a095750f35b8161373d91616545565b61028d57805f6136eb565b8161375291616545565b61028d57805f6136a9565b8161376791616545565b61028d57805f61365b565b8161377c91616545565b61028d57805f613573565b8161379191616545565b61028d57805f613531565b816137a691616545565b61028d57805f6134e3565b816137bb91616545565b61028d57805f6133eb565b816137d091616545565b61028d57805f6133a9565b503461028d57602036600319011261028d576004356001600160a01b0381168082036113fa5761380d6102da9261795a565b5f51602061cbf65f395f51905f52811415908161384f575b816138305750617835565b734e59b44847b379578588920ca78fbf26c0b4956c915014155f612646565b6a636f6e736f6c652e6c6f678114159150613825565b503461028d578060031936011261028d575f51602061cbf65f395f51905f523b1561028d5760405163c88a5e6d60e01b81526105396004820152600160801b602482015281908181604481835f51602061cbf65f395f51905f525af180156106875761397b575b50505f51602061cbf65f395f51905f523b1561028d57806040516323f2866760e11b8152610539600482015261053960248201528181604481835f51602061cbf65f395f51905f525af1801561068757613966575b50601f5460081c6001600160a01b0316803b15610a2f5781606491602460405180948193635559647760e01b835261053960048401525af1801561068757610a095750f35b8161397091616545565b61028d57805f613921565b8161398591616545565b61028d57805f6138cc565b503461028d578060031936011261028d57806040516139b0606082616545565b603081527f537464436865617473206465706c6f79436f646528737472696e67293a20446560208201526f383637bcb6b2b73a103330b4b632b21760811b60408201525f51602061cbf65f395f51905f523b15610a2f5781613a2e916040518093819263f28dceb360e01b8352602060048401526024830190616484565b0381835f51602061cbf65f395f51905f525af1801561068757613ab8575b5050303b1561028d57604051634af967d160e01b815260206004820152602160248201527f5374644368656174732e742e736f6c3a526576657274696e67436f6e747261636044820152601d60fa1b60648201528190818160848183305af1801561068757610a095750f35b81613ac291616545565b61028d57805f613a4c565b503461028d578060031936011261028d57601b54613aea816167fb565b613af76040519182616545565b818152601b83526020810191837f3ad8aa4f87544323a9d1e5dd902f40c356527a7955687113db5f9a85ad579dc1845b838310613bb357868587604051928392602084019060208552518091526040840160408260051b8601019392905b828210613b6457505050500390f35b91936001919395506020613ba38192603f198a820301865288519083613b938351604084526040840190616484565b92015190848184039101526165a1565b9601920192018594939192613b55565b60026020600192604051613bc6816164a8565b604051613bd7816120eb818a61684a565b8152613be4858701616942565b83820152815201920192019190613b27565b503461028d578060031936011261028d575f51602061cbf65f395f51905f523b1561028d576040516308b6ac0f60e31b8152610539600482015261053a602482015281908181604481835f51602061cbf65f395f51905f525af1801561068757613f3c575b50601f5460081c6001600160a01b0316803b15610a2f576040516354d9714560e11b8152610539600482015261053a60248201529082908290604490829084905af1801561068757613f27575b50505f51602061cbf65f395f51905f523b1561028d576040516390c5013b60e01b815281908181600481835f51602061cbf65f395f51905f525af1801561068757613f12575b50505f51602061cbf65f395f51905f523b1561028d576040516308b6ac0f60e31b815261dead600482015261beef602482015281908181604481835f51602061cbf65f395f51905f525af1801561068757613efd575b50601f5460081c6001600160a01b0316803b15610a2f578180916044604051809481936354d9714560e11b835261dead600484015261beef60248401525af1801561068757613ee8575b50505f51602061cbf65f395f51905f523b1561028d576040516390c5013b60e01b815281908181600481835f51602061cbf65f395f51905f525af1801561068757613ed3575b50505f51602061cbf65f395f51905f523b1561028d576040516308b6ac0f60e31b8152610539600482015261053a602482015281908181604481835f51602061cbf65f395f51905f525af1801561068757613ebe575b50601f5460081c6001600160a01b0316803b15610a2f576040516354d9714560e11b8152610539600482015261053a60248201529082908290604490829084905af18015610687576137335750505f51602061cbf65f395f51905f523b1561028d576040516390c5013b60e01b815281908181600481835f51602061cbf65f395f51905f525af1801561068757610a095750f35b81613ec891616545565b61028d57805f613e2a565b81613edd91616545565b61028d57805f613dd4565b81613ef291616545565b61028d57805f613d8e565b81613f0791616545565b61028d57805f613d44565b81613f1c91616545565b61028d57805f613cee565b81613f3191616545565b61028d57805f613ca8565b81613f4691616545565b61028d57805f613c5b565b503461028d578060031936011261028d576040516106a5808201908282106001600160401b0383111761082d5790829161c3998339039082f08015610820575f51602061cbf65f395f51905f523b156113f657604051633d21120560e21b815282908181600481835f51602061cbf65f395f51905f525af1801561068757614267575b50506001600160a01b031690813b1561028d5760405163de4a5dcd60e01b81525f51602061cbf65f395f51905f526004820152818160248183875af1801561068757908291614252575b50505f51602061cbf65f395f51905f523b1561028d57604051633d21120560e21b81528181600481835f51602061cbf65f395f51905f525af180156106875790829161423d575b5050813b1561028d5760405163de4a5dcd60e01b81526a636f6e736f6c652e6c6f676004820152818160248183875af1801561068757908291614228575b50505f51602061cbf65f395f51905f523b1561028d57604051633d21120560e21b81528181600481835f51602061cbf65f395f51905f525af1801561068757908291614213575b5050813b1561028d5760405163de4a5dcd60e01b8152734e59b44847b379578588920ca78fbf26c0b4956c6004820152818160248183875af18015610687579082916141fe575b5050813b1561028d5760405163de4a5dcd60e01b815273d8da6bf26964af9d7eed9e03e53415d37aa960456004820152818160248183875af18015610687579082916141e9575b505060405191605892838101938185106001600160401b0386111761082d578394829161ca3e8339039083f0801561068757813b15612d395760405163de4a5dcd60e01b81526001600160a01b0390911660048201529082908290602490829084905af1801561068757610a095750f35b816141f391616545565b61028d57805f614178565b8161420891616545565b61028d57805f614131565b8161421d91616545565b61028d57805f6140ea565b8161423291616545565b61028d57805f6140a3565b8161424791616545565b61028d57805f614065565b8161425c91616545565b61028d57805f61401e565b8161427191616545565b6113f657815f613fd4565b503461028d578060031936011261028d576040516101fc808201908282106001600160401b0383111761082d5790829161bffa8339039082f080156108205760018060a01b0316818060405160208101906370a0823160e01b8252306024820152602481526142ec604482616545565b5190845afa506142fa617806565b6020815191818082019384920101031261067b5751601180546001600160a01b03191683179055600f805463ffffffff19166370a0823117905561433d3061a6e5565b61435069021e19e0c9bab240000061a761565b828060405160208101906318160ddd60e01b825260048152614373602482616545565b5190855afa50614381617806565b6020815191818082019384920101031261067b5751808269021e19e0c9bab2400000105f14614650575069021e19e0c9bab23fffff1982019182116106ed576143f7916143cd91616b44565b601180546001600160a01b03191684179055600f805463ffffffff19166318160ddd17905561a761565b6040516370a0823160e01b8152306004820152602081602481855afa80156106c557839061461c575b61442a9150617163565b6040516318160ddd60e01b8152602081600481855afa80156106c55783906145e8575b61445791506171bc565b818060405160208101906370a0823160e01b825230602482015260248152614480604482616545565b5190845afa5061448e617806565b6020815191818082019384920101031261067b5751601180546001600160a01b03191683179055600f805463ffffffff19166370a082311790556144d13061a6e5565b6144da8361a761565b828060405160208101906318160ddd60e01b8252600481526144fd602482616545565b5190855afa5061450b617806565b6020815191818082019384920101031261067b57518082156145cb5750614535916143cd91616b44565b6040516370a0823160e01b8152306004820152602081602481855afa9081156106c5578391614598575b5060049161456e602092617114565b6040516318160ddd60e01b815292839182905afa801561068757829061064f576102da9150617163565b90506020813d6020116145c3575b816145b360209383616545565b8101031261067b5751600461455f565b3d91506145a6565b918403919050816106ed57614535916145e391616921565b6143cd565b506020813d602011614614575b8161460260209383616545565b8101031261067b57614457905161444d565b3d91506145f5565b506020813d602011614648575b8161463660209383616545565b8101031261067b5761442a9051614420565b3d9150614629565b91905069021e19e0c9bab2400000039069021e19e0c9bab240000082116106ed576143f7916145e391616921565b503461028d578060031936011261028d575f51602061cbf65f395f51905f523b1561028d5760405163c88a5e6d60e01b81526105396004820152600160801b602482015281908181604481835f51602061cbf65f395f51905f525af180156106875761489c575b50505f51602061cbf65f395f51905f523b1561028d57806040516308b6ac0f60e31b8152610539600482015261053960248201528181604481835f51602061cbf65f395f51905f525af1801561068757614887575b50601f5460081c6001600160a01b0316803b15610a2f5781606491602460405180948193635559647760e01b835261053960048401525af1801561068757614872575b50601f5460081c6001600160a01b0316803b15610a2f5781606491602460405180948193635559647760e01b835261053960048401525af180156106875761485d575b50505f51602061cbf65f395f51905f523b1561028d576040516390c5013b60e01b815281908181600481835f51602061cbf65f395f51905f525af1801561068757614848575b50601f5460081c6001600160a01b0316803b15610a2f5781809160246040518094819363646ea56d60e01b83523060048401525af1801561068757610a095750f35b8161485291616545565b61028d57805f614806565b8161486791616545565b61028d57805f6147c0565b8161487c91616545565b61028d57805f61477d565b8161489191616545565b61028d57805f61473a565b816148a691616545565b61028d57805f6146e5565b503461028d57602036600319011261028d576004356001600160401b0381116113f657366023820112156113f657806004013590826148ef83616586565b916148fd6040519384616545565b83835236602485830101116113f6578361246b946024602093018386013783010152617880565b503461028d57602036600319011261028d57600435906001600160a01b0382168083036113f65760025b60ff81166004811015614aff576005811015614aeb57806149e257506149738461a4eb565b155f51602061cbf65f395f51905f523b15611e865760405190632631f2b160e11b8252600482015283816024815f51602061cbf65f395f51905f525afa8015612037579084916149cd575b5050600160ff915b011661494e565b816149d791616545565b6113fa57825f6149be565b60018103614a6257506149f48461a4eb565b5f51602061cbf65f395f51905f523b15611e8657604051632631f2b160e11b8152901515600482015283816024815f51602061cbf65f395f51905f525afa801561203757908491614a4d575b5050600160ff915b6149c6565b81614a5791616545565b6113fa57825f614a40565b60028103614ac257505f51602061cbf65f395f51905f523b156113fa57604051632631f2b160e11b8152821515600482015283816024815f51602061cbf65f395f51905f525afa801561203757908491614a4d575050600160ff916149c6565b60ff9160019160038103614adb5750614a484687617b95565b600403614a4857614a488661795a565b634e487b7160e01b84526021600452602484fd5b836102da84614b0f811515617835565b600181108015614b57575b614b2390617835565b5f51602061cbf65f395f51905f52811490811591614b415750617835565b6a636f6e736f6c652e6c6f679150141583612646565b5060098111614b1a565b503461028d578060031936011261028d576040516101a3808201908282106001600160401b0383111761082d5790829161c1f68339039082f08015610820576001600160a01b03165f51602061cbf65f395f51905f523b156113f6578160405163f8e18b5760e01b8152826004820152600a60248201528181604481835f51602061cbf65f395f51905f525af180156106875761506c575b50505f51602061cbf65f395f51905f523b156113f6578160405163c88a5e6d60e01b8152826004820152606460248201528181604481835f51602061cbf65f395f51905f525af1801561068757615057575b5050479082813b5f51602061cbf65f395f51905f523b156113f65760405190636d83fe6960e11b8252600482015281602482015281816044815f51602061cbf65f395f51905f525afa801561068757615042575b5081315f51602061cbf65f395f51905f523b156113f6576040519063260a5b1560e21b825260048201526064602482015281816044815f51602061cbf65f395f51905f525afa80156106875761502d575b50604051632d0335ab60e01b8152600481018390526020816024815f51602061cbf65f395f51905f525afa90811561068757829161500e575b505f51602061cbf65f395f51905f523b156113f6576001600160401b036040519163260a5b1560e21b8352166004820152600a602482015281816044815f51602061cbf65f395f51905f525afa801561068757614ff9575b508131604051828152614d95602082616545565b5f51602061cbf65f395f51905f523b156113fa5782614dc99160405180938192635a6b63c160e11b835288600484016177e4565b0381835f51602061cbf65f395f51905f525af19081156106c5578391614fe4575b50505f51602061cbf65f395f51905f523b156113f65760405163c88a5e6d60e01b81528360048201528260248201528281604481835f51602061cbf65f395f51905f525af19081156106c5578391614fcf575b50505f51602061cbf65f395f51905f523b156113f657604051631c72346d60e01b8152600481018490528281602481835f51602061cbf65f395f51905f525af19081156106c5578391614fba575b5050614e98904790616921565b5f51602061cbf65f395f51905f523b156113f65781614ecc916040518093819263c88a5e6d60e01b83523060048401616b7f565b0381835f51602061cbf65f395f51905f525af1801561068757614fa5575b5050803b914760648201809211614f915790614f0591617265565b604051632d0335ab60e01b8152600481018290526020816024815f51602061cbf65f395f51905f525afa92831561203757614f576001600160401b036102da95614f5c948891614f62575b5016617114565b617114565b31617114565b614f84915060203d602011614f8a575b614f7c8183616545565b810190616902565b5f614f50565b503d614f72565b634e487b7160e01b85526011600452602485fd5b81614faf91616545565b6113fa57825f614eea565b81614fc491616545565b6113f657815f614e8b565b81614fd991616545565b6113f657815f614e3d565b81614fee91616545565b6113f657815f614dea565b8161500391616545565b6113fa57825f614d81565b615027915060203d602011614f8a57614f7c8183616545565b5f614d29565b8161503791616545565b6113fa57825f614cf0565b8161504c91616545565b6113fa57825f614c9f565b8161506191616545565b6113f657815f614c4b565b8161507691616545565b6113f657815f614bf9565b503461028d578060031936011261028d576150c08161509e6166f2565b60405180938192638d1cc92560e01b8352602060048401526024830190616484565b03815f51602061cbf65f395f51905f525afa908115610687578291615176575b50602081519101670de0b6b3a7640000f06001600160a01b038116156151105780611fa76102bc6102da936172b4565b60405162461bcd60e51b815260206004820152603860248201527f537464436865617473206465706c6f79436f646528737472696e672c75696e74604482015277191a9b149d102232b83637bcb6b2b73a103330b4b632b21760411b6064820152608490fd5b61518a91503d8084833e6114138183616545565b5f6150e0565b503461028d578060031936011261028d5760405160178054808352908352909160208301917fc624b66cc0138b8fabc209247f72d758e1cf3343756d543badbf24212bed8c15915b8181106151ef576108ac856108a081870382616545565b82546001600160a01b03168452602090930192600192830192016151d8565b503461028d578060031936011261028d5760405160188054808352908352909160208301917fb13d2d76d1f4b7be834882e410b3e3a8afaf69f83600ae24db354391d2378d2e915b81811061526d576108ac856108a081870382616545565b82546001600160a01b0316845260209093019260019283019201615256565b503461028d578060031936011261028d576040906152d182516152af8482616545565b601081526f6172626974726172794164647265737360801b6020820152616ed8565b509160018060a01b038316906bffffffffffffffffffffffff198460601b168151615388602082016006815260018584015283606084015260608352615318608084616545565b868551615326606082616545565b602f81527f5374644368656174732e742e736f6c3a4d6f636b436f6e74726163745769746860208201526e436f6e7374727563746f724172677360881b87820152865180948192638d1cc92560e01b8352602060048401526024830190616484565b03815f51602061cbf65f395f51905f525afa9182156157485791602093916153e693899261572c575b5084919287519584879551918291018587015e840190838201908b8252519283915e010187815203601f198101835282616545565b5f51602061cbf65f395f51905f523b156113f2578461541991845180938192635a6b63c160e11b83528a600484016177e4565b0381835f51602061cbf65f395f51905f525af1801561567857908591615717575b50808080670de0b6b3a7640000895af194615453617806565b95156156ef5784955f51602061cbf65f395f51905f523b156156eb578561548e91855180938192635a6b63c160e11b835286600484016177e4565b0381835f51602061cbf65f395f51905f525af180156156e1579086916156cc575b50506154bb90316170bd565b81516303155a6760e21b8152602081600481875afa908115615678578591615697575b505f51602061cbf65f395f51905f523b156113f25782519063260a5b1560e21b825260048201526006602482015284816044815f51602061cbf65f395f51905f525afa801561567857908591615682575b505081516352b6ff2560e11b8152602081600481875afa908115615678578591615633575b50600493615563602092617835565b83516362ebc01760e11b815294859182905afa9283156156295784936155e4575b505f51602061cbf65f395f51905f523b156155df578151637c84c69b60e01b81526001600160601b03199093166004840152602483015282826044815f51602061cbf65f395f51905f525afa908115611e325750610a095750f35b505050fd5b9092506020813d602011615621575b8161560060209383616545565b810103126155df57516001600160601b0319811681036155df57915f615584565b3d91506155f3565b82513d86823e3d90fd5b90506020813d602011615670575b8161564e60209383616545565b810103126113f2576004936155636156676020936168f5565b92505093615554565b3d9150615641565b83513d87823e3d90fd5b8161568c91616545565b6155df57835f61552f565b9450506020843d6020116156c4575b816156b360209383616545565b8101031261067b578493515f6154de565b3d91506156a6565b816156d691616545565b6113f257845f6154af565b84513d88823e3d90fd5b8580fd5b825162461bcd60e51b8152602060048201526058602482015260a49061164660448201616e6c565b8161572191616545565b611e8657835f61543a565b859250615742903d808c833e6114138183616545565b916153b1565b85513d89823e3d90fd5b503461028d578060031936011261028d57601e5461576f816167fb565b61577c6040519182616545565b818152601e83526020810191837f50bb669a95c7b50b7e8a6f09454034b2b14cf2b85c730dca9a539ca82cb6e350845b8383106158805786858760405192839260208401906020855251809152604084019160408260051b8601019392815b8383106157e85786860387f35b919395509193603f198782030183528551906020604082019260018060a01b0381511683520151916040602083015282518091526060820190602060608260051b850101940192855b828110615855575050505050602080600192970193019301909286959492936157db565b9091929394602080615873600193605f198782030189528951616484565b9701950193929101615831565b60405161588c816164a8565b82546001600160a01b031681526001830180546158a8816167fb565b916158b66040519384616545565b8183528a526020808b20908b9084015b8382106158ec5750505050600192826020928360029501528152019201920191906157ac565b600160208192604051615903816120eb818a61684a565b8152019301910190916158c6565b503461028d578060031936011261028d57806159a76020604051615936606082616545565b603b81527f7465737420746573742074657374207465737420746573742074657374207465828201527f73742074657374207465737420746573742074657374206a756e6b0000000000604082015260405180938192636229498b60e01b8352604060048401526044830190616484565b85602483015203815f51602061cbf65f395f51905f525afa908115610687578291615aba575b50604051630884001960e21b815260048101829052602081602481865f51602061cbf65f395f51905f525af180156106c5578390615a7f575b615a109150616ff5565b5f51602061cbf65f395f51905f523b15610a2f576040519063260a5b1560e21b825260048201527fac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80602482015281816044815f51602061cbf65f395f51905f525afa801561068757610a095750f35b506020813d602011615ab2575b81615a9960209383616545565b81010312612d3957615aad615a1091616c35565b615a06565b3d9150615a8c565b9150506020813d602011615ae7575b81615ad660209383616545565b8101031261067b578190515f6159cd565b3d9150615ac9565b503461028d578060031936011261028d57604051636c98507360e11b81528180826004815f51602061cbf65f395f51905f525afa91821561082057615b4692615b3e91839161143c57506167a1565b6123276173fa565b03815f51602061cbf65f395f51905f525afa908115610687578291615ceb575b5060405163348051d760e11b81526005600482015290829081836024815f51602061cbf65f395f51905f525afa908115610687576123f36001602a602094615bed978791615cd1575b50604051958691692e72656365697074735b60b01b828401528051918291018484015e8101605d60f81b838201520301601e19810185520183616545565b03815f51602061cbf65f395f51905f525afa908115610687578291615cb7575b5080518101906020818303126113fa576020810151916001600160401b038311611e8657615c4c6101009260206102da9581615c51950192010161745b565b61813e565b015160405190615c6361012083616545565b61010080835262018000698000000000000000000160841b0160208401526001604b1b6040840152606083018590526080830185905260a0830185905260c0830185905260e0830185905282810152617793565b615ccb91503d8084833e6114138183616545565b5f615c0d565b615ce591503d8089833e6114138183616545565b5f615baf565b615cff91503d8084833e6114138183616545565b5f615b66565b503461028d578060031936011261028d5760405160168054808352908352909160208301917fd833147d7dc355ba459fc788f669e58cfaf9dc25ddcd0702e87d69c7b5124289915b818110615d64576108ac856108a081870382616545565b82546001600160a01b0316845260209093019260019283019201615d4d565b503461028d578060031936011261028d575f51602061cbf65f395f51905f523b1561028d5760405163c88a5e6d60e01b81526105396004820152600160801b602482015281908181604481835f51602061cbf65f395f51905f525af1801561068757615f6e575b50505f51602061cbf65f395f51905f523b1561028d576040516303223eab60e11b8152610539600482015281908181602481835f51602061cbf65f395f51905f525af1801561068757615f59575b50601f5460081c6001600160a01b0316803b15610a2f578160649160246040518094819363646ea56d60e01b835261053960048401525af1801561068757615f44575b50601f5460081c6001600160a01b0316803b15610a2f578160649160246040518094819363646ea56d60e01b835261053960048401525af180156106875761485d5750505f51602061cbf65f395f51905f523b1561028d576040516390c5013b60e01b815281908181600481835f51602061cbf65f395f51905f525af18015610687576148485750601f5460081c6001600160a01b0316803b15610a2f5781809160246040518094819363646ea56d60e01b83523060048401525af1801561068757610a095750f35b81615f4e91616545565b61028d57805f615e7b565b81615f6391616545565b61028d57805f615e38565b81615f7891616545565b61028d57805f615dea565b503461028d578060031936011261028d57806040615fb98151615fa68382616545565b60018152600360f81b6020820152617382565b5f51602061cbf65f395f51905f523b15612d395781519063260a5b1560e21b825260036004830152602482015282816044815f51602061cbf65f395f51905f525afa8015611e5057908391616197575b505061602d815161601a8382616545565b60018152600160f91b6020820152617382565b5f51602061cbf65f395f51905f523b15612d395781519063260a5b1560e21b825260026004830152602482015282816044815f51602061cbf65f395f51905f525afa8015611e5057908391616182575b50506160a5815161608e8382616545565b600181526001600160f81b03196020820152617382565b5f51602061cbf65f395f51905f523b15612d395781519063260a5b1560e21b825260ff6004830152602482015282816044815f51602061cbf65f395f51905f525afa8015611e505790839161616d575b505061611a81516161068382616545565b600281526173b960f01b6020820152617382565b905f51602061cbf65f395f51905f523b15612d395780519163260a5b1560e21b83526173b96004840152602483015282826044815f51602061cbf65f395f51905f525afa908115611e325750610a095750f35b8161617791616545565b610a2f57815f6160f5565b8161618c91616545565b610a2f57815f61607d565b816161a191616545565b610a2f57815f616009565b503461028d578060031936011261028d5760206040516161cc8282616545565b8281526161db83611efa6166f2565b03815f51602061cbf65f395f51905f525afa91821561203757839185936162be575b5061623a90826040519384928180850197805191829101895e8401908282018a8152815193849201905e010186815203601f198101835282616545565b519083f0906001600160a01b0382161561625b57506102bc6102da916172b4565b6084906040519062461bcd60e51b82526004820152603660248201527f537464436865617473206465706c6f79436f646528737472696e672c6279746560448201527539949d102232b83637bcb6b2b73a103330b4b632b21760511b6064820152fd5b61623a9193506162d7903d8088833e6114138183616545565b92906161fd565b503461028d578060031936011261028d576040516101fc808201908282106001600160401b0383111761082d5790829161bffa8339039082f0801561082057601f8054610100600160a81b03191660089290921b610100600160a81b031691909117905580f35b503461067b575f36600319011261067b575f51602061cbf65f395f51905f523b1561067b5760405163c88a5e6d60e01b8152306004820152670de0b6b3a764000060248201525f81604481835f51602061cbf65f395f51905f525af180156163c9576163b6575b506102da476170bd565b6163c291505f90616545565b5f5f6163ac565b6040513d5f823e3d90fd5b3461067b575f36600319011261067b576164406163ef6166d0565b604051906163fc826164a8565b5f825261640f60208301915f8352616ed8565b82526001600160a01b0316825261643a61642a6121c46166d0565b93516001600160a01b0316617062565b51617265565b005b60206040818301928281528451809452019201905f5b8181106164655750505090565b82516001600160a01b0316845260209384019390920191600101616458565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b604081019081106001600160401b038211176164c357604052565b634e487b7160e01b5f52604160045260245ffd5b61010081019081106001600160401b038211176164c357604052565b6101a081019081106001600160401b038211176164c357604052565b608081019081106001600160401b038211176164c357604052565b60e081019081106001600160401b038211176164c357604052565b90601f801991011681019081106001600160401b038211176164c357604052565b60405190616575606083616545565b565b60405190616575608083616545565b6001600160401b0381116164c357601f01601f191660200190565b90602080835192838152019201905f5b8181106165be5750505090565b82516001600160e01b0319168452602093840193909201916001016165b1565b602081016020825282518091526040820191602060408360051b8301019401925f915b83831061661057505050505090565b909192939460208061662e600193603f198682030187528951616484565b97019301930191939290616601565b602081016020825282518091526040820191602060408360051b8301019401925f915b83831061666f57505050505090565b90919293946020806166a5600193603f198682030187526040838b51878060a01b038151168452015191818582015201906165a1565b97019301930191939290616660565b6166bd5f616586565b906166cb6040519283616545565b5f8252565b604051906166df604083616545565b60048252633133333760e01b6020830152565b60405190616701604083616545565b601382527229ba3221b432b0ba39973a1739b7b61d2130b960691b6020830152565b81601f8201121561067b5760208151910161673d82616586565b9261674b6040519485616545565b8284528282011161067b57815f926020928386015e8301015290565b9060208282031261067b5781516001600160401b03811161067b5761678c9201616723565b90565b805191908290602001825e015f815290565b906165756021602080946040519581879251918291018484015e81017f2f746573742f66697874757265732f62726f6164636173742e6c6f672e6a736f83820152603760f91b604082015203016001810185520183616545565b6001600160401b0381116164c35760051b60200190565b90600182811c92168015616840575b602083101461682c57565b634e487b7160e01b5f52602260045260245ffd5b91607f1691616821565b5f929181549161685983616812565b80835292600181169081156168ae575060011461687557505050565b5f9081526020812093945091925b838310616894575060209250010190565b600181602092949394548385870101520191019190616883565b915050602093945060ff929192191683830152151560051b010190565b906165756168df926040519384809261684a565b0383616545565b9081602091031261067b575190565b5190811515820361067b57565b9081602091031261067b57516001600160401b038116810361067b5790565b9190820180921161692e57565b634e487b7160e01b5f52601160045260245ffd5b90604051918281549182825260208201905f5260205f20925f905b806007830110616a9f57616575945491818110616a80575b818110616a61575b818110616a42575b818110616a23575b818110616a04575b8181106169e5575b8181106169c8575b106169b3575b500383616545565b6001600160e01b03191681526020015f6169ab565b602083811b6001600160e01b0319168552909301926001016169a5565b604083901b6001600160e01b031916845260209093019260010161699d565b606083901b6001600160e01b0319168452602090930192600101616995565b608083901b6001600160e01b031916845260209093019260010161698d565b60a083901b6001600160e01b0319168452602090930192600101616985565b60c083901b6001600160e01b031916845260209093019260010161697d565b60e083901b6001600160e01b0319168452602090930192600101616975565b916008919350610100600191865463ffffffff60e01b8160e01b16825263ffffffff60e01b8160c01b16602083015263ffffffff60e01b8160a01b16604083015263ffffffff60e01b8160801b16606083015263ffffffff60e01b8160601b16608083015263ffffffff60e01b8160401b1660a083015263ffffffff60e01b8160201b1660c083015263ffffffff60e01b1660e082015201940192018592939161695d565b9190820391821161692e57565b60405190616b60604083616545565b601082526f6f7074696d69736d5f7365706f6c696160801b6020830152565b6001600160a01b039091168152602081019190915260400190565b60085460ff168015616ba95790565b50604051630667f9d760e41b81525f51602061cbf65f395f51905f5260048201526519985a5b195960d21b60248201526020816044815f51602061cbf65f395f51905f525afa9081156163c9575f91616c03575b50151590565b90506020813d602011616c2d575b81616c1e60209383616545565b8101031261067b57515f616bfd565b3d9150616c11565b51906001600160a01b038216820361067b57565b9080601f8301121561067b578151616c60816167fb565b92616c6e6040519485616545565b81845260208085019260051b82010192831161067b57602001905b828210616c965750505090565b8151815260209182019101616c89565b91906101008382031261067b5760405190616cc0826164d7565b819380516001600160401b03811161067b57810182601f8201121561067b57805190616ceb826167fb565b91616cf96040519384616545565b80835260208084019160051b8301019185831161067b5760208101915b838310616dfb5750505050835260208101516001600160401b03811161067b5782616d42918301616723565b6020840152616d5360408201616c35565b604084015260608101516001600160401b03811161067b5782616d77918301616723565b606084015260808101516001600160401b03811161067b5782616d9b918301616723565b6080840152616dac60a08201616c35565b60a084015260c08101516001600160401b03811161067b5782616dd0918301616723565b60c084015260e0810151916001600160401b03831161067b5760e092616df69201616723565b910152565b82516001600160401b03811161067b578201906040828903601f19011261067b5760405190616e29826164a8565b616e3560208401616c35565b82526040830151916001600160401b03831161067b57616e5d8a602080969581960101616c49565b83820152815201920191616d16565b60407731b932b0ba3290393ab73a34b6b290313cba32b1b7b2329760411b917f537464436865617473206465706c6f79436f6465546f28737472696e672c627981527f7465732c75696e743235362c61646472657373293a204661696c656420746f2060208201520152565b906040516020810190616f05602082865180838901875e81015f838201520301601f198101835282616545565b519020906040519263ffa1864960e01b84528260048501526020846024815f51602061cbf65f395f51905f525afa9384156163c9575f94616fb9575b50835f51602061cbf65f395f51905f523b1561067b57604080516318caf8e360e31b81526001600160a01b0390921660048301526024820152905f9082908190616f8f906044830190616484565b0381835f51602061cbf65f395f51905f525af180156163c957616faf5750565b5f61657591616545565b9093506020813d602011616fed575b81616fd560209383616545565b8101031261067b57616fe690616c35565b925f616f41565b3d9150616fc8565b5f51602061cbf65f395f51905f523b1561067b576040516328a9b0fb60e11b81526001600160a01b03909116600482015273f39fd6e51aad88f6f4ce6ab8827279cfffb9226660248201525f816044815f51602061cbf65f395f51905f525afa80156163c957616faf5750565b905f51602061cbf65f395f51905f523b1561067b576040516328a9b0fb60e11b81526001600160a01b039283166004820152911660248201525f816044815f51602061cbf65f395f51905f525afa80156163c957616faf5750565b5f51602061cbf65f395f51905f523b1561067b576040519063260a5b1560e21b82526004820152670de0b6b3a764000060248201525f816044815f51602061cbf65f395f51905f525afa80156163c957616faf5750565b5f51602061cbf65f395f51905f523b1561067b576040519063260a5b1560e21b825260048201525f60248201525f816044815f51602061cbf65f395f51905f525afa80156163c957616faf5750565b5f51602061cbf65f395f51905f523b1561067b576040519063260a5b1560e21b8252600482015269021e19e0c9bab240000060248201525f816044815f51602061cbf65f395f51905f525afa80156163c957616faf5750565b5f51602061cbf65f395f51905f523b1561067b576040519063260a5b1560e21b8252600482015269043c33c193756480000060248201525f816044815f51602061cbf65f395f51905f525afa80156163c957616faf5750565b5f51602061cbf65f395f51905f523b1561067b576040519063260a5b1560e21b82526004820152600160248201525f816044815f51602061cbf65f395f51905f525afa80156163c957616faf5750565b905f51602061cbf65f395f51905f523b1561067b576040519163260a5b1560e21b8352600483015260248201525f816044815f51602061cbf65f395f51905f525afa80156163c957616faf5750565b90813b5f60405193601f19603f840116850160405282855260208501903c565b90916172eb61678c93604084526040840190616484565b916020818403910152616484565b5f51602061cbf65f395f51905f523b1561067b5760405163f320d96360e01b8152915f918391829161732f9190600484016172d4565b03815f51602061cbf65f395f51905f525afa80156163c957616faf5750565b90815181101561735f570160200190565b634e487b7160e01b5f52603260045260245ffd5b60ff811161692e576001901b90565b905f805b83518210156173f557617399828561734e565b5160f81c9084516001840180851161692e576173b491616b44565b6001600160fd1b038116810361692e576173d09060031b617373565b9182810292818404149015171561692e576001916173ed91616921565b910190617386565b925050565b60405190617407826164f3565b5f610180838281528260208201528260408201528260608201528260808201528260a08201528260c0820152606060e082015260606101008201528261012082015282610140820152826101608201520152565b91906101a08382031261067b5760405190617475826164f3565b81938051835260208101516001600160401b03811161067b578261749a918301616723565b60208401526174ab60408201616c35565b604084015260608101516001600160401b03811161067b57826174cf918301616723565b606084015260808101516001600160401b03811161067b57826174f3918301616723565b608084015261750460a08201616c35565b60a084015260c08101516001600160401b03811161067b5782617528918301616723565b60c084015260e08101516001600160401b03811161067b57810182601f8201121561067b57805190617559826167fb565b916175676040519384616545565b80835260208084019160051b8301019185831161067b5760208101915b838310617622575050505060e08401526101008101516001600160401b03811161067b57826175b4918301616723565b6101008401526101208101516001600160401b03811161067b57826175da918301616723565b6101208401526175ed6101408201616c35565b610140840152610160810151610160840152610180810151916001600160401b03831161067b5761018092616df69201616723565b82516001600160401b03811161067b57820190610140828903601f19011261067b576040519061014082018281106001600160401b038211176164c35760405261766e60208401616c35565b82526040830151602083015260608301516001600160401b03811161067b5789602061769c92860101616723565b604083015260808301516001600160401b03811161067b578960206176c392860101616723565b606083015260a08301516001600160401b03811161067b578960206176ea92860101616723565b60808301526176fb60c084016168f5565b60a083015260e08301516001600160401b03811161067b5789602061772292860101616c49565b60c083015261010083015160e08301526101208301516001600160401b03811161067b5789602061775592860101616723565b610100830152610140830151916001600160401b03831161067b576177828a602080969581960101616723565b610120820152815201920191617584565b5f51602061cbf65f395f51905f523b1561067b576177d25f9161732f6040519485938493639762463160e01b8552604060048601526044850190616484565b83810360031901602485015290616484565b6001600160a01b03909116815260406020820181905261678c92910190616484565b3d15617830573d9061781782616586565b916178256040519384616545565b82523d5f602084013e565b606090565b5f51602061cbf65f395f51905f523b1561067b57604051630c9fd58160e01b815290151560048201525f816024815f51602061cbf65f395f51905f525afa80156163c957616faf5750565b5f6178a79160405180938192638d1cc92560e01b8352602060048401526024830190616484565b03815f51602061cbf65f395f51905f525afa9081156163c9575f91617940575b506020815191015ff0906001600160a01b038216156178e257565b60405162461bcd60e51b815260206004820152603060248201527f537464436865617473206465706c6f79436f646528737472696e67293a20446560448201526f383637bcb6b2b73a103330b4b632b21760811b6064820152608490fd5b61795491503d805f833e6114138183616545565b5f6178c7565b60018060a01b03165f51602061cbf65f395f51905f5281141590816179eb575b816179cc575b505f51602061cbf65f395f51905f523b1561067b57604051632631f2b160e11b815290151560048201525f816024815f51602061cbf65f395f51905f525afa80156163c957616faf5750565b734e59b44847b379578588920ca78fbf26c0b4956c915014155f617980565b6a636f6e736f6c652e6c6f67811415915061797a565b5f5f5b6127108110617a11575090565b90617a1e82600192616921565b9101617a04565b5f905f51602061cbf65f395f51905f523b1561067b5760405163d1a5b36f60e01b81525f81600481835f51602061cbf65f395f51905f525af180156163c957617aee575b50600c549161ff001983166101008117600c5560ff617a86617a01565b9460081c1615617a94575050565b600c555f51602061cbf65f395f51905f523b1561028d5760405163015e6a8760e51b81528181600481835f51602061cbf65f395f51905f525af1801561068757617adc575050565b617ae7828092616545565b61028d5750565b617afb9192505f90616545565b5f905f617a69565b60405190617b108261650f565b606080838181525f60208201528160408201520152565b60208091604051928184925191829101835e8101600a81520301902090565b60208091604051928184925191829101835e8101600981520301902090565b15617b6d5750565b60405162461bcd60e51b815260206004820152908190617b91906024830190616484565b0390fd5b60018060a01b031660018110918215617eaf575b5f51602061cbf65f395f51905f523b1561067b57604051632631f2b160e11b815292151560048401525f9283816024815f51602061cbf65f395f51905f525afa80156163c957617e9a575b50600a81148015617e8f575b15617c745750602160991b8110908115617c62575b505f51602061cbf65f395f51905f523b156113f657604051632631f2b160e11b8152901515600482015281816024815f51602061cbf65f395f51905f525afa801561068757617adc575050565b610800602160991b011090505f617c15565b61a4b181148015617e83575b15617ce9575060648110908115617cde57505f51602061cbf65f395f51905f523b156113f657604051632631f2b160e11b8152901515600482015281816024815f51602061cbf65f395f51905f525afa801561068757617adc575050565b60689150115f617c15565b61a86a8114908115617e77575b50617d00575b5050565b600160981b81108015617e67575b5f51602061cbf65f395f51905f523b156113fa57604051632631f2b160e11b8152901515600482015282816024815f51602061cbf65f395f51905f525afa80156106c557908391617e52575b5050600160991b81108015617e42575b5f51602061cbf65f395f51905f523b156113fa57604051632631f2b160e11b8152901515600482015282816024815f51602061cbf65f395f51905f525afa80156106c557908391617e2d575b5050600360981b8110908115617e1c575b505f51602061cbf65f395f51905f523b156113f657604051632631f2b160e11b8152901515600482015281816024815f51602061cbf65f395f51905f525afa80156106875715617cfc57617ae7828092616545565b60ff600360981b011090505f617dc7565b81617e3791616545565b6113f657815f617db6565b5060ff600160991b018111617d6a565b81617e5c91616545565b6113f657815f617d5a565b5060ff600160981b018111617d0e565b61a8699150145f617cf6565b5062066eed8114617c80565b506101a48114617c00565b617ea79193505f90616545565b5f915f617bf4565b60ff82119250617ba9565b60405190617ec7826164d7565b5f60e08360608152606060208201528260408201528260608201528260808201528260a08201528260c08201520152565b60405190617f058261652a565b606060c0838281525f602082015282604082015282808201525f6080820152617f2c617eba565b60a08201520152565b919060e08382031261067b5760405190617f4e8261652a565b819380516001600160401b03811161067b57810182601f8201121561067b578051617f78816167fb565b91617f866040519384616545565b81835260208084019260051b8201019185831161067b5760208201905b83821061805857505050508352617fbc60208201616c35565b602084015260408101516001600160401b03811161067b5782617fe0918301616723565b604084015260608101516001600160401b03811161067b5782618004918301616723565b60608401526080810151608084015260a08101516001600160401b03811161067b5782618032918301616ca6565b60a084015260c0810151916001600160401b03831161067b5760c092616df69201616723565b81516001600160401b03811161067b5760209161807a89848094880101616723565b815201910190617fa3565b61808d617eba565b50618096617eba565b906020810151602083015260018060a01b03604082015116604083015260018060a01b0360a08201511660a08301526180d2608082015161a416565b60808301526180e460c082015161a416565b60c08301526180f660e082015161a416565b60e0830152618108606082015161a416565b606083015251815290565b9081602091031261067b57516001600160a01b038116810361067b5790565b801561692e575f190190565b6181466173fa565b5061814f6173fa565b81518152610140808301516001600160a01b039081169183019190915260a0808401518216908301526040808401519091169082015260808201516181939061a416565b60808201526181a5606083015161a416565b60608201526181b760c083015161a416565b60c08201526181ca61012083015161a416565b6101208201526181de61018083015161a416565b6101808201526181f1602083015161a416565b602082015260e082015192835191618208836167fb565b926182166040519485616545565b808452618225601f19916167fb565b015f5b8181106183885750505f5b8551811015618363576001906001600160a01b0361825182896183ea565b51511661825e82876183ea565b5152602061826c82896183ea565b510151602061827b83886183ea565b510152618295604061828d838a6183ea565b51015161a416565b60406182a183886183ea565b51015260606182b082896183ea565b51015160606182bf83886183ea565b5101526182d1608061828d838a6183ea565b60806182dd83886183ea565b51015260c06182ec82896183ea565b51015160a06182fb83886183ea565b51015261830e61010061828d838a6183ea565b60c061831a83886183ea565b51015261832d61012061828d838a6183ea565b60e061833983886183ea565b51015260a061834882896183ea565b510151151561010061835a83886183ea565b51015201618233565b50929093506101609160e0840152610100810151610100840152015161016082015290565b604051906101208201918083106001600160401b038411176164c3576020926040525f81525f838201525f60408201526060808201525f6080820152606060a08201525f60c08201525f60e08201525f61010082015282828801015201618228565b805182101561735f5760209160051b010190565b6040519061840d604083616545565b6005825264105b9d9a5b60da1b6020830152565b60405190618430604083616545565b6015825274687474703a2f2f3132372e302e302e313a3835343560581b6020830152565b60405190618463604083616545565b6005825264185b9d9a5b60da1b6020830152565b60405190618486604083616545565b600782526613585a5b9b995d60ca1b6020830152565b604051906184ab608083616545565b604582526406d504472560dc1b6060837f68747470733a2f2f6574682d6d61696e6e65742e616c6368656d796170692e6960208201527f6f2f76322f70776335726d4a6872646f61534566696d6f4b456d73764f6a4b5360408201520152565b6040519061851a604083616545565b60078252661b585a5b9b995d60ca1b6020830152565b6040519061853f604083616545565b60078252665365706f6c696160c81b6020830152565b60405190618564606083616545565b603d82527f39346164316464663834646662386333346436626235646361323030310000006040837f68747470733a2f2f7365706f6c69612e696e667572612e696f2f76332f62393760208201520152565b604051906185c5604083616545565b60078252667365706f6c696160c81b6020830152565b604051906185ea604083616545565b6007825266486f6c65736b7960c81b6020830152565b6040519061860f606083616545565b6022825261696f60f01b6040837f68747470733a2f2f7270632e686f6c65736b792e65746870616e64616f70732e60208201520152565b60405190618655604083616545565b6007825266686f6c65736b7960c81b6020830152565b6040519061867a604083616545565b60088252674f7074696d69736d60c01b6020830152565b604051906186a0604083616545565b601b82527f68747470733a2f2f6d61696e6e65742e6f7074696d69736d2e696f00000000006020830152565b604051906186db604083616545565b60088252676f7074696d69736d60c01b6020830152565b60405190618701604083616545565b601082526f4f7074696d69736d205365706f6c696160801b6020830152565b6040519061872f604083616545565b601b82527f68747470733a2f2f7365706f6c69612e6f7074696d69736d2e696f00000000006020830152565b6040519061876a604083616545565b600c82526b417262697472756d204f6e6560a01b6020830152565b60405190618794604083616545565b601c82527f68747470733a2f2f617262312e617262697472756d2e696f2f727063000000006020830152565b604051906187cf604083616545565b600c82526b617262697472756d5f6f6e6560a01b6020830152565b604051906187f9604083616545565b6014825273417262697472756d204f6e65205365706f6c696160601b6020830152565b6040519061882b606083616545565b6026825265696f2f72706360d01b6040837f68747470733a2f2f7365706f6c69612d726f6c6c75702e617262697472756d2e60208201520152565b60405190618875604083616545565b6014825273617262697472756d5f6f6e655f7365706f6c696160601b6020830152565b604051906188a7604083616545565b600d82526c417262697472756d204e6f766160981b6020830152565b604051906188d2604083616545565b601c82527f68747470733a2f2f6e6f76612e617262697472756d2e696f2f727063000000006020830152565b6040519061890d604083616545565b600d82526c617262697472756d5f6e6f766160981b6020830152565b60405190618938604083616545565b60078252662837b63cb3b7b760c91b6020830152565b6040519061895d604083616545565b601782527668747470733a2f2f706f6c79676f6e2d7270632e636f6d60481b6020830152565b60405190618992604083616545565b60078252663837b63cb3b7b760c91b6020830152565b604051906189b7604083616545565b600c82526b506f6c79676f6e20416d6f7960a01b6020830152565b604051906189e1606083616545565b60238252626f677960e81b6040837f68747470733a2f2f7270632d616d6f792e706f6c79676f6e2e746563686e6f6c60208201520152565b60405190618a28604083616545565b600c82526b706f6c79676f6e5f616d6f7960a01b6020830152565b60405190618a52604083616545565b60098252684176616c616e63686560b81b6020830152565b60405190618a79606083616545565b6025825264432f72706360d81b6040837f68747470733a2f2f6170692e617661782e6e6574776f726b2f6578742f62632f60208201520152565b60405190618ac2604083616545565b60098252686176616c616e63686560b81b6020830152565b60405190618ae9604083616545565b600e82526d4176616c616e6368652046756a6960901b6020830152565b60405190618b15606083616545565b602a825269742f62632f432f72706360b01b6040837f68747470733a2f2f6170692e617661782d746573742e6e6574776f726b2f657860208201520152565b60405190618b63604083616545565b600e82526d6176616c616e6368655f66756a6960901b6020830152565b60405190618b8f604083616545565b600f82526e2127211029b6b0b93a1021b430b4b760891b6020830152565b60405190618bbc606083616545565b60218252606760f81b6040837f68747470733a2f2f6273632d6461746173656564312e62696e616e63652e6f7260208201520152565b60405190618c01604083616545565b600f82526e3137312fb9b6b0b93a2fb1b430b4b760891b6020830152565b60405190618c2e604083616545565b60178252761093908814db585c9d0810da185a5b8815195cdd1b995d604a1b6020830152565b60405190618c63606083616545565b602782526617d8da185c195b60ca1b6040837f68747470733a2f2f7270632e616e6b722e636f6d2f6273635f746573746e657460208201520152565b60405190618cae604083616545565b6017825276189b9897dcdb585c9d17d8da185a5b97dd195cdd1b995d604a1b6020830152565b60405190618ce3604083616545565b600c82526b23b737b9b4b99021b430b4b760a11b6020830152565b60405190618d0d604083616545565b601b82527f68747470733a2f2f7270632e676e6f736973636861696e2e636f6d00000000006020830152565b60405190618d48604083616545565b600c82526b33b737b9b4b9afb1b430b4b760a11b6020830152565b60405190618d72604083616545565b60088252674d6f6f6e6265616d60c01b6020830152565b60405190618d98604083616545565b602082527f68747470733a2f2f7270632e6170692e6d6f6f6e6265616d2e6e6574776f726b6020830152565b60405190618dd3604083616545565b60088252676d6f6f6e6265616d60c01b6020830152565b60405190618df9604083616545565b600982526826b7b7b73934bb32b960b91b6020830152565b60405190618e20606083616545565b602a825269616d2e6e6574776f726b60b01b6040837f68747470733a2f2f7270632e6170692e6d6f6f6e72697665722e6d6f6f6e626560208201520152565b60405190618e6e604083616545565b600982526836b7b7b73934bb32b960b91b6020830152565b60405190618e95604083616545565b60088252674d6f6f6e6261736560c01b6020830152565b60405190618ebb606083616545565b6024825263776f726b60e01b6040837f68747470733a2f2f7270632e746573746e65742e6d6f6f6e6265616d2e6e657460208201520152565b60405190618f03604083616545565b60088252676d6f6f6e6261736560c01b6020830152565b60405190618f29604083616545565b600c82526b42617365205365706f6c696160a01b6020830152565b60405190618f53604083616545565b601882527768747470733a2f2f7365706f6c69612e626173652e6f726760401b6020830152565b60405190618f89604083616545565b600c82526b626173655f7365706f6c696160a01b6020830152565b60405190618fb3604083616545565b60048252634261736560e01b6020830152565b60405190618fd5604083616545565b601882527768747470733a2f2f6d61696e6e65742e626173652e6f726760401b6020830152565b6040519061900b604083616545565b60048252636261736560e01b6020830152565b6040519061902d604083616545565b600d82526c426c617374205365706f6c696160981b6020830152565b60405190619058604083616545565b601882527768747470733a2f2f7365706f6c69612e626c6173742e696f60401b6020830152565b6040519061908e604083616545565b600d82526c626c6173745f7365706f6c696160981b6020830152565b604051906190b9604083616545565b6005825264109b185cdd60da1b6020830152565b604051906190dc604083616545565b601482527368747470733a2f2f7270632e626c6173742e696f60601b6020830152565b6040519061910e604083616545565b6005825264189b185cdd60da1b6020830152565b60405190619131604083616545565b600c82526b46616e746f6d204f7065726160a01b6020830152565b6040519061915b604083616545565b601c82527f68747470733a2f2f7270632e616e6b722e636f6d2f66616e746f6d2f000000006020830152565b60405190619196604083616545565b600c82526b66616e746f6d5f6f7065726160a01b6020830152565b604051906191c0604083616545565b601482527311985b9d1bdb4813dc195c984815195cdd1b995d60621b6020830152565b604051906191f2606083616545565b60248252636e65742f60e01b6040837f68747470733a2f2f7270632e616e6b722e636f6d2f66616e746f6d5f7465737460208201520152565b6040519061923a604083616545565b601482527319985b9d1bdb57dbdc195c9857dd195cdd1b995d60621b6020830152565b6040519061926c604083616545565b6007825266119c985e1d185b60ca1b6020830152565b60405190619291604083616545565b601482527368747470733a2f2f7270632e667261782e636f6d60601b6020830152565b604051906192c3604083616545565b6007825266199c985e1d185b60ca1b6020830152565b604051906192e8604083616545565b600f82526e119c985e1d185b0815195cdd1b995d608a1b6020830152565b60405190619315604083616545565b601c82527f68747470733a2f2f7270632e746573746e65742e667261782e636f6d000000006020830152565b60405190619350604083616545565b600f82526e199c985e1d185b17dd195cdd1b995d608a1b6020830152565b6040519061937d604083616545565b601882527710995c9858da185a5b8818905c9d1a5bc815195cdd1b995d60421b6020830152565b604051906193b3604083616545565b602082527f68747470733a2f2f62617274696f2e7270632e62657261636861696e2e636f6d6020830152565b604051906193ee604083616545565b601882527718995c9858da185a5b97d8985c9d1a5bd7dd195cdd1b995d60421b6020830152565b60405190619424604083616545565b6005825264466c61726560d81b6020830152565b60405190619447606083616545565b60298252686578742f432f72706360b81b6040837f68747470733a2f2f666c6172652d6170692e666c6172652e6e6574776f726b2f60208201520152565b60405190619494604083616545565b6005825264666c61726560d81b6020830152565b604051906194b7604083616545565b600d82526c233630b9329021b7b9ba37b71960991b6020830152565b604051906194e2606083616545565b602b82526a6b2f6578742f432f72706360a81b6040837f68747470733a2f2f636f73746f6e322d6170692e666c6172652e6e6574776f7260208201520152565b60405190619531604083616545565b600d82526c333630b932afb1b7b9ba37b71960991b6020830152565b6040519061955c604083616545565b60048252634d6f646560e01b6020830152565b6040519061957e604083616545565b601582527468747470733a2f2f6d6f64652e647270632e6f726760581b6020830152565b604051906195b1604083616545565b60048252636d6f646560e01b6020830152565b604051906195d3604083616545565b600c82526b4d6f6465205365706f6c696160a01b6020830152565b604051906195fd604083616545565b601c82527f68747470733a2f2f7365706f6c69612e6d6f64652e6e6574776f726b000000006020830152565b60405190619638604083616545565b600c82526b6d6f64655f7365706f6c696160a01b6020830152565b60405190619662604083616545565b60048252635a6f726160e01b6020830152565b60405190619684604083616545565b601582527468747470733a2f2f7a6f72612e647270632e6f726760581b6020830152565b604051906196b7604083616545565b60048252637a6f726160e01b6020830152565b604051906196d9604083616545565b600c82526b5a6f7261205365706f6c696160a01b6020830152565b60405190619703604083616545565b601f82527f68747470733a2f2f7365706f6c69612e7270632e7a6f72612e656e65726779006020830152565b6040519061973e604083616545565b600c82526b7a6f72615f7365706f6c696160a01b6020830152565b60405190619768604083616545565b60048252635261636560e01b6020830152565b6040519061978a604083616545565b601682527568747470733a2f2f726163656d61696e6e65742e696f60501b6020830152565b604051906197be604083616545565b60048252637261636560e01b6020830152565b604051906197e0604083616545565b600c82526b52616365205365706f6c696160a01b6020830152565b6040519061980a604083616545565b600c82526b726163655f7365706f6c696160a01b6020830152565b60405190619834604083616545565b600582526413595d185b60da1b6020830152565b60405190619857604083616545565b601882527768747470733a2f2f6d6574616c6c322e647270632e6f726760401b6020830152565b6040519061988d604083616545565b60058252641b595d185b60da1b6020830152565b604051906198b0604083616545565b600d82526c4d6574616c205365706f6c696160981b6020830152565b604051906198db604083616545565b601f82527f68747470733a2f2f746573746e65742e7270632e6d6574616c6c322e636f6d006020830152565b60405190619916604083616545565b600d82526c6d6574616c5f7365706f6c696160981b6020830152565b60405190619941604083616545565b600682526542696e61727960d01b6020830152565b60405190619965606083616545565b602682526567732e636f6d60d01b6040837f68747470733a2f2f7270632e7a65726f2e74686562696e617279686f6c64696e60208201520152565b604051906199af604083616545565b600682526562696e61727960d01b6020830152565b604051906199d3604083616545565b600e82526d42696e617279205365706f6c696160901b6020830152565b604051906199ff604083616545565b600e82526d62696e6172795f7365706f6c696160901b6020830152565b60405190619a2b604083616545565b60078252664f726465726c7960c81b6020830152565b60405190619a50604083616545565b601b82527f68747470733a2f2f7270632e6f726465726c792e6e6574776f726b00000000006020830152565b60405190619a8b604083616545565b60078252666f726465726c7960c81b6020830152565b60405190619ab0604083616545565b600f82526e4f726465726c79205365706f6c696160881b6020830152565b60405190619add604083616545565b601f82527f68747470733a2f2f746573746e65742d7270632e6f726465726c792e6f7267006020830152565b60405190619b18604083616545565b600f82526e6f726465726c795f7365706f6c696160881b6020830152565b60088054901c60ff1661657557619b5761010061ff00196008541617600855565b619b8e619b62616566565b619b6a6183fe565b8152617a696020820152619b7c618421565b6040820152619b89618454565b61ad14565b619bbf619b99616566565b619ba1618477565b815260016020820152619bb261849c565b6040820152619b8961850b565b619bf2619bca616566565b619bd2618530565b815262aa36a76020820152619be5618555565b6040820152619b896185b6565b619c24619bfd616566565b619c056185db565b81526142686020820152619c17618600565b6040820152619b89618646565b619c55619c2f616566565b619c3761866b565b8152600a6020820152619c48618691565b6040820152619b896186cc565b619c88619c60616566565b619c686186f2565b815262aa37dc6020820152619c7b618720565b6040820152619b89616b51565b619cba619c93616566565b619c9b61875b565b815261a4b16020820152619cad618785565b6040820152619b896187c0565b619ced619cc5616566565b619ccd6187ea565b815262066eee6020820152619ce061881c565b6040820152619b89618866565b619d1f619cf8616566565b619d00618898565b815261a4ba6020820152619d126188c3565b6040820152619b896188fe565b619d50619d2a616566565b619d32618929565b815260896020820152619d4361894e565b6040820152619b89618983565b619d83619d5b616566565b619d636189a8565b8152620138826020820152619d766189d2565b6040820152619b89618a19565b619db5619d8e616566565b619d96618a43565b815261a86a6020820152619da8618a6a565b6040820152619b89618ab3565b619de7619dc0616566565b619dc8618ada565b815261a8696020820152619dda618b06565b6040820152619b89618b54565b619e18619df2616566565b619dfa618b80565b815260386020820152619e0b618bad565b6040820152619b89618bf2565b619e49619e23616566565b619e2b618c1f565b815260616020820152619e3c618c54565b6040820152619b89618c9f565b619e7a619e54616566565b619e5c618cd4565b815260646020820152619e6d618cfe565b6040820152619b89618d39565b619eac619e85616566565b619e8d618d63565b81526105046020820152619e9f618d89565b6040820152619b89618dc4565b619ede619eb7616566565b619ebf618dea565b81526105056020820152619ed1618e11565b6040820152619b89618e5f565b619f10619ee9616566565b619ef1618e86565b81526105076020820152619f03618eac565b6040820152619b89618ef4565b619f43619f1b616566565b619f23618f1a565b815262014a346020820152619f36618f44565b6040820152619b89618f7a565b619f75619f4e616566565b619f56618fa4565b81526121056020820152619f68618fc6565b6040820152619b89618ffc565b619fa9619f80616566565b619f8861901e565b8152630a0c71fd6020820152619f9c619049565b6040820152619b8961907f565b619fdc619fb4616566565b619fbc6190aa565b815262013e316020820152619fcf6190cd565b6040820152619b896190ff565b61a00d619fe7616566565b619fef619122565b815260fa602082015261a00061914c565b6040820152619b89619187565b61a03f61a018616566565b61a0206191b1565b8152610fa2602082015261a0326191e3565b6040820152619b8961922b565b61a07061a04a616566565b61a05261925d565b815260fc602082015261a063619282565b6040820152619b896192b4565b61a0a261a07b616566565b61a0836192d9565b81526109da602082015261a095619306565b6040820152619b89619341565b61a0d561a0ad616566565b61a0b561936e565b8152620138d4602082015261a0c86193a4565b6040820152619b896193df565b61a10661a0e0616566565b61a0e8619415565b8152600e602082015261a0f9619438565b6040820152619b89619485565b61a13761a111616566565b61a1196194a8565b81526072602082015261a12a6194d3565b6040820152619b89619522565b61a16961a142616566565b61a14a61954d565b815261868b602082015261a15c61956f565b6040820152619b896195a2565b61a19b61a174616566565b61a17c6195c4565b8152610397602082015261a18e6195ee565b6040820152619b89619629565b61a1ce61a1a6616566565b61a1ae619653565b81526276adf1602082015261a1c1619675565b6040820152619b896196a8565b61a20261a1d9616566565b61a1e16196ca565b8152633b9ac9ff602082015261a1f56196f4565b6040820152619b8961972f565b61a23461a20d616566565b61a215619759565b8152611a95602082015261a22761977b565b6040820152619b896197af565b61a26661a23f616566565b61a2476197d1565b8152611a96602082015261a25961977b565b6040820152619b896197fb565b61a29861a271616566565b61a279619825565b81526106d6602082015261a28b619848565b6040820152619b8961987e565b61a2ca61a2a3616566565b61a2ab6198a1565b81526106cc602082015261a2bd6198cc565b6040820152619b89619907565b61a2fc61a2d5616566565b61a2dd619932565b8152610270602082015261a2ef619956565b6040820152619b896199a0565b61a32e61a307616566565b61a30f6199c4565b8152610271602082015261a321619956565b6040820152619b896199f0565b61a36061a339616566565b61a341619a1c565b8152610123602082015261a353619a41565b6040820152619b89619a7c565b61657561a36b616566565b61a373619aa1565b815261116c602082015261a385619ace565b6040820152619b89619b09565b61a39a617ef8565b5060c061a3a5617ef8565b918051835260408101516040840152606081015160608401526080810151608084015261a3d560a0820151618085565b60a0840152015160c082015290565b9061a3ee82616586565b61a3fb6040519182616545565b828152809261a40c601f1991616586565b0190602036910137565b602081511161a4865780516020036020811161692e57602091828061a47861a43e829561a3e4565b938260405193849281840199888b9951918291018a5e8401908282015f8152815193849201905e01015f815203601f198101835282616545565b80510101031261067b575190565b60405162461bcd60e51b815260206004820152603760248201527f537464436865617473205f6279746573546f55696e74286279746573293a20426044820152763cba32b9903632b733ba341032bc31b2b2b2399019991760491b6064820152608490fd5b5f198131101561a65457479080315f51602061cbf65f395f51905f523b1561067b5760405163c88a5e6d60e01b8152306004820152600160248201525f92908381604481835f51602061cbf65f395f51905f525af180156163c95761a63f575b508280808060016001600160a01b0386165af19361a567617806565b505f51602061cbf65f395f51905f523b15611e86578361a59c916040518093819263c88a5e6d60e01b83523060048401616b7f565b0381835f51602061cbf65f395f51905f525af180156120375790849161a62a575b50505f51602061cbf65f395f51905f523b156113fa5760405163c88a5e6d60e01b81529183918391829161a5f5919060048401616b7f565b0381835f51602061cbf65f395f51905f525af180156106875761a61757505090565b61a622828092616545565b61028d575090565b8161a63491616545565b6113fa57825f61a5bd565b61a64c9193505f90616545565b5f915f61a54b565b60405162461bcd60e51b815260206004820152605e60248201527f537464436865617473205f697350617961626c652861646472657373293a204260448201527f616c616e636520657175616c73206d61782075696e743235362c20736f20697460648201527f2063616e6e6f74207265636569766520616e79206d6f72652066756e64730000608482015260a490fd5b600e54600160401b8110156164c3576001810180600e5581101561735f57600e5f527fbb7b4a454dc3493923482f07822329ed19e8244eff582cc204f8554c3620c3fd0155565b60209291908391805192839101825e019081520190565b604091949392606082019560018060a01b0316825260208201520152565b601154600f546010545f9493926001600160a01b03169160e01b61a785600d61ae3f565b90835f52600d60205260405f209063ffffffff60e01b1690815f5260205260405f20604051602081019061a7be8161347788888661a72c565b5190205f5260205260ff600360405f200154161561abe2575b835f52600d60205260405f20905f5260205261347761a80560405f209360405192839160208301958661a72c565b5190205f5260205260405f20600181015492600282015461a8268186616921565b61aad4575b82549060405195630667f9d760e41b87526020878061a84e868a60048401616b7f565b03815f51602061cbf65f395f51905f525afa9687156163c9575f9761aaa0575b506001908201610100031b5f1901811b198616915f51602061cbf65f395f51905f523b1561067b576040516370ca10bb60e01b8152925f928492839261a8bd9288901b1790896004850161a743565b0381835f51602061cbf65f395f51905f525af180156163c95761aa8b575b5061a8e6600d61aeff565b91901591821561aa80575b505061a9b4575050601180546001600160a01b031916905550600f805463ffffffff19169055600e80545f8255919250600d91908161a992575b50505f600382015560068101805460ff19169055600701805461a94d90616812565b908161a957575050565b81601f5f931160011461a968575055565b8183526020832061a98591601f0160051c8419019060010161abf2565b8082528160208120915555565b5f5260205f205f5b82811061a9a7575061a92b565b5f8282015560010161a99a565b8492935054905f51602061cbf65f395f51905f523b156113fa5761a9ec60405194859384936370ca10bb60e01b85526004850161a743565b0381835f51602061cbf65f395f51905f525af180156106875761aa6b575b60405162461bcd60e51b815260206004820152603360248201527f73746453746f726167652066696e642853746453746f72616765293a204661696044820152723632b2103a37903bb934ba32903b30b63ab29760691b6064820152608490fd5b61aa76828092616545565b61028d578061aa0a565b141590505f8061a8f1565b61aa989196505f90616545565b5f945f61a8db565b9096506020813d60201161aacc575b8161aabc60209383616545565b8101031261067b5751958161a86e565b3d915061aaaf565b61aade8186616921565b61010003610100811161692e5761aaf490617373565b60405163348051d760e11b8152600481018290525f816024815f51602061cbf65f395f51905f525afa9182156163c95761abbc606a61abc3946020945f9161abc8575b506040519485917f73746453746f726167652066696e642853746453746f72616765293a20506163828401527f6b656420736c6f742e2057652063616e2774206669742076616c756520677265604084015269030ba32b9103a3430b7160b51b60608401528051918291018484015e81015f838201520301601f198101845283616545565b8410617b65565b61a82b565b61abdc91503d805f833e6114138183616545565b5f61ab37565b61abec600d61b58b565b5061a7d7565b5f5b82811061ac0057505050565b5f8282015560010161abf4565b91909182516001600160401b0381116164c35761ac2a8254616812565b601f811161acd1575b506020601f821160011461ac7357819061ac649394955f9261ac68575b50508160011b915f199060031b1c19161790565b9055565b015190505f8061ac50565b601f19821690835f52805f20915f5b81811061acb95750958360019596971061aca1575b505050811b019055565b01515f1960f88460031b161c191690555f808061ac97565b9192602060018192868b01518155019401920161ac82565b8181111561ac335761ad0690835f5260205f2090601f840160051c906020851061ad0c575b601f82910160051c03910161abf2565b5f61ac33565b5f915061acf6565b91906040810180519161ad2685617b27565b948351956001600160401b0387116164c35761ad428154616812565b601f811161ae05575b50602096601f811160011461ada0578061ad809161ad92969798995f9161ad95575b508160011b915f199060031b1c19161790565b90555b61ad8b6166b4565b845261b3af565b52565b90508801515f61ad6d565b601f198116825f52885f20905f5b81811061aded57509061ad929697989983600194931061add5575b5050811b01905561ad83565b8901515f1960f88460031b161c191690555f8061adc9565b888b0151835560209a8b019a6001909301920161adae565b8781111561ad4b5761ae3990825f5260205f2090601f8a0160051c9060208b1061ad0c57601f82910160051c03910161abf2565b5f61ad4b565b600781019061ae4e8254616812565b61aeeb57600191500190604051808360208295549384815201905f5260205f20925f5b81811061aed257505061ae8692500383616545565b81518060051b908082046020149015171561692e5761aea49061a3e4565b5f5b835181101561aecd578061aebc600192866183ea565b5160208260051b850101520161aea6565b509150565b845483526001948501948794506020909301920161ae71565b5061678c6120eb916040519283809261684a565b905f806020600285015460e01b61af4f602461af1a8861ae3f565b6040519485918183019563ffffffff60e01b1686528051918291018484015e810186838201520301601f198101845283616545565b60048601549151916001600160a01b03165afa600361af6c617806565b930154600581901b93906001600160fb1b0381160361692e575f938151602081115f1461afeb57506020905b5f925b82841061afaa57505050509190565b9091929560ff60f81b61afc661afc08986616921565b8461734e565b5116908760031b918883046008148915171561692e576001921c17960192919061af9b565b9061af98565b1561aff857565b60405162461bcd60e51b815260206004820152604d60248201525f51602061cbd65f395f51905f5260448201527f617461293a20436861696e20616c6961732063616e6e6f74206265207468652060648201526c32b6b83a3c9039ba3934b7339760991b608482015260a490fd5b1561b06d57565b60405162461bcd60e51b815260206004820152603b60248201525f51602061cbd65f395f51905f5260448201527f617461293a20436861696e2049442063616e6e6f7420626520302e00000000006064820152608490fd5b61a94d8154616812565b9181519283516001600160401b0381116164c35761b0ed8254616812565b601f811161b375575b50602094601f821160011461b3145761b1289293949582915f9261ac685750508160011b915f199060031b1c19161790565b81555b602083015160018201556002810160408401518051906001600160401b0382116164c35761b1598354616812565b601f811161b2da575b50602090601f831160011461b2725782606095936003959361b198935f9261ac685750508160011b915f199060031b1c19161790565b90555b019201519182516001600160401b0381116164c35761b1ba8254616812565b601f811161b238575b506020601f821160011461b1f357819061ac649394955f9261ac685750508160011b915f199060031b1c19161790565b601f19821690835f52805f20915f5b81811061b2205750958360019596971061aca157505050811b019055565b9192602060018192868b01518155019401920161b202565b8181111561b1c35761b26c90835f5260205f2090601f840160051c906020851061ad0c57601f82910160051c03910161abf2565b5f61b1c3565b90601f19831691845f52815f20925f5b81811061b2c2575092600192859260609896600398961061b2ab575b505050811b01905561b19b565b01515f1983881b60f8161c191690555f808061b29e565b9293602060018192878601518155019501930161b282565b8281111561b1625761b30e90845f5260205f2090601f850160051c906020861061ad0c57601f82910160051c03910161abf2565b5f61b162565b601f19821695835f52805f20915f5b88811061b35d5750836001959697981061b345575b505050811b01815561b12b565b01515f1960f88460031b161c191690555f808061b338565b9192602060018192868501518155019401920161b323565b8181111561b0f65761b3a990835f5260205f2090601f840160051c906020851061ad0c57601f82910160051c03910161abf2565b5f61b0f6565b61b3bb8151151561aff1565b602082019161b3cc8351151561b066565b61b3d4619b36565b61b3ef61b3ea84515f52600b60205260405f2090565b6168cb565b92835191821592831561b571575b50815160405163348051d760e11b81526004810191909152905f8280602481015b03815f51602061cbf65f395f51905f525afa801561b56c5761b4a061b5439561260861b4da936165759a61b534975f9261b548575b5061b4be61b4cc9161b49a60405197889561b49a60208801602f905f51602061cbd65f395f51905f5281526e030ba30949d1021b430b4b71024a21608d1b60208201520190565b9061678f565b711030b63932b0b23c903ab9b2b210313c901160711b815260120190565b61111760f11b815260020190565b03601f198101845283616545565b61b50061b4fb600161b4eb88617b46565b01545f52600b60205260405f2090565b61b0c5565b805190604084519101519061b513616577565b9283526020830152856040830152606082015261b52f85617b46565b61b0cf565b515f52600b60205260405f2090565b61ac0d565b61b4cc91925061b56461b4be913d805f833e6114138183616545565b92915061b453565b6163c9565b61b41e91935060208601208451602086012014929061b3fd565b6004810154600282015460038301546001600160a01b03909216925f929160e01b61b5b58261ae3f565b9160018060a01b0386165f528060205260405f2063ffffffff60e01b83165f5260205260405f20604051602081019061b5f38161347789898661a72c565b5190205f5260205260ff600360405f2001541661be2b575f51602061cbf65f395f51905f523b1561067b5760405163266cf10960e01b81525f81600481835f51602061cbf65f395f51905f525af180156163c95761be16575b5061b6568161aeff565b90506040516365bc948160e01b81528760048201528681602481835f51602061cbf65f395f51905f525af190811561be0b57879161bd9f575b5080518061b70157608460405162461bcd60e51b815260206004820152604060248201527f73746453746f726167652066696e642853746453746f72616765293a204e6f2060448201527f73746f726167652075736520646574656374656420666f72207461726765742e6064820152fd5b9061b70e61b73992618132565b90602061b71b83836183ea565b51604051630667f9d760e41b81529485918291908e60048401616b7f565b03815f51602061cbf65f395f51905f525afa92831561bd9457899361bd61575b50821561bd1d575b61b76b82826183ea565b5160018060a01b0360048701541690604051630667f9d760e41b81526020818061b799858760048401616b7f565b03815f51602061cbf65f395f51905f525afa90811561bd12578c9161bce1575b5061b7c38861aeff565b91909382155f1461bcda575f19905b5f51602061cbf65f395f51905f523b1561bcc157848f9161b80760405194859384936370ca10bb60e01b85526004850161a743565b0381835f51602061cbf65f395f51905f525af1801561bc3557908e9161bcc5575b505061b8338961aeff565b60048b0154909491506001600160a01b03165f51602061cbf65f395f51905f523b1561bcc157908e9161b87a60405194859384936370ca10bb60e01b85526004850161a743565b0381835f51602061cbf65f395f51905f525af1801561bcb657908d9161bc9d575b50508261bc92575b50501561bc84578987898b968c9660ff60068b01541661baf5575b6001898901610100031b5f1901881b16871c810361bade57506080600396959361b950959361347761b91c7f9c9555b1e3102e3cf48f427d79cb678f5d9bd1ed0ad574389461e255f95170ed9560405192839160208301958661a72c565b51902061b92986866183ea565b519060405192835263ffffffff60e01b8d16602084015260408301526060820152a16183ea565b51906040519161b95f8361650f565b8252602080830194855260408084019283526001606085019081526001600160a01b038d165f9081528884528290206001600160e01b03198a168d528352818c20915190969281019061b9b7816134778e8e8661a72c565b5190208b5260205260408a2092518355516001830155516002820155019051151560ff8019835416911617905560018060a01b0386165f528060205260405f2063ffffffff60e01b8316865260205260408520604051602081019061ba218161347789898661a72c565b519020865260205260ff6003604087200154161561ba815760409560018060a01b03165f52602052845f209063ffffffff60e01b16845260205261347761ba7585852093865192839160208301958661a72c565b51902082526020522090565b60405162461bcd60e51b815260206004820152602f60248201527f73746453746f726167652066696e642853746453746f72616765293a20536c6f60448201526e3a143994903737ba103337bab7321760891b6064820152608490fd5b9650505050915061b70e61b739915b929192618132565b97509250505061bb37935061bb0a83836183ea565b519460208660018060a01b0360048a0154166040519788928392630667f9d760e41b845260048401616b7f565b03815f51602061cbf65f395f51905f525afa94851561bc79578b9561bc46575b5061bb62868861be7b565b95909661bb6f818a61bf45565b60048b015490939192906001600160a01b03165f51602061cbf65f395f51905f523b1561bc4257908f9161bbb760405194859384936370ca10bb60e01b85526004850161a743565b0381835f51602061cbf65f395f51905f525af1801561bc3557928f95928f8f95938f979461bc0b575b50508a61bc03575b50979861b8be57509650505050915061b70e61b7399161baed565b99505f61bbe8565b90939650839194975061bc1f929550616545565b61bc3157928a928c928f958f5f61bbe0565b8c80fd5b8e604051903d90823e3d90fd5b8f80fd5b9094506020813d821161bc71575b8161bc6160209383616545565b8101031261067b5751935f61bb57565b3d915061bc54565b6040513d8d823e3d90fd5b915061b70e61b7399161baed565b141590505f8061b8a3565b8161bca791616545565b61bcb2578b5f61b89b565b8b80fd5b6040513d8f823e3d90fd5b8e80fd5b8161bccf91616545565b61bc31578c5f61b828565b8d9061b7d2565b90506020813d821161bd0a575b8161bcfb60209383616545565b8101031261067b57515f61b7b9565b3d915061bcee565b6040513d8e823e3d90fd5b7f080fc4a96620c4462e705b23f346413fe3796bb63c6f8d8591baec0e231577a561bd4883836183ea565b518b61bd5960405192839283616b7f565b0390a161b761565b9092506020813d821161bd8c575b8161bd7c60209383616545565b8101031261067b5751915f61b759565b3d915061bd6f565b6040513d8b823e3d90fd5b90503d8088833e61bdb08183616545565b810160408282031261be075781516001600160401b03811161be03578161bdd8918401616c49565b916020810151906001600160401b03821161bdff5761bdf8929101616c49565b505f61b68f565b8980fd5b8880fd5b8780fd5b6040513d89823e3d90fd5b61be239195505f90616545565b5f935f61b64c565b919350919360018060a01b03165f5260205260405f209063ffffffff60e01b165f5260205261347761be6c60405f209360405192839160208301958661a72c565b5190205f5260205260405f2090565b91905f5b610100811061be9257505090505f905f90565b8060ff0360ff811161692e576004850154600190911b906001600160a01b03165f51602061cbf65f395f51905f523b1561067b57835f9161bee760405194859384936370ca10bb60e01b85526004850161a743565b0381835f51602061cbf65f395f51905f525af180156163c95761bf35575b5061bf0f8461aeff565b8161bf2b575b5061bf225760010161be7f565b92505060019190565b905015155f61bf15565b5f61bf3f91616545565b5f61bf05565b91905f5b610100811061bf5c57505090505f905f90565b60048401546001821b906001600160a01b03165f51602061cbf65f395f51905f523b1561067b57835f9161bfa460405194859384936370ca10bb60e01b85526004850161a743565b0381835f51602061cbf65f395f51905f525af180156163c95761bfe9575b5061bfcc8461aeff565b8161bfdf575b5061bf225760010161bf49565b905015155f61bfd2565b5f61bff391616545565b5f61bfc256fe60808060405269021e19e0c9bab2400000600155305f525f60205269021e19e0c9bab240000060405f20556101c590816100378239f3fe6080806040526004361015610012575f80fd5b5f3560e01c90816318160ddd1461012a5750806355596477146100ff578063646ea56d146100d857806370a08231146100a15763a9b2e28a14610053575f80fd5b604036600319011261009d57610067610144565b6024356001600160a01b0381169081900361009d5761009b91610094906001600160a01b0316331461015a565b321461015a565b005b5f80fd5b3461009d57602036600319011261009d576001600160a01b036100c2610144565b165f525f602052602060405f2054604051908152f35b602036600319011261009d5761009b6001600160a01b036100f7610144565b16331461015a565b602036600319011261009d5761009b6001600160a01b0361011e610144565b1661009481331461015a565b3461009d575f36600319011261009d576020906001548152f35b600435906001600160a01b038216820361009d57565b1561016157565b60405162461bcd60e51b8152602060048201526006602482015265217072616e6b60d01b6044820152606490fdfea2646970667358221220affb8f4fbb2b160005623b992a1e0a18587f4ec495909425624e93cfee9fa67d64736f6c63430008210033608060408181527fada5013122d395ba3c54772283fb069b10426056ef8ca54750cb9bb552a59e7d805460016001600160a01b031991821681179092557fcc69885fda6bcc1a4ace058b4a62bf5e179ea78fd58a1ccd71c22cc9b688792f8290557fabbb5caa7dda850e60932de0934eb1f9d0f59695050f761dc64e443e5030a56980543090831681179091557f101e368776582e57ab3d116ffe2517c0a585cd5b23174b01e275c2d8329c3d83805490921681179091555f908152602091909152206002905560d190816100d28239f3fe60808060405260043610156011575f80fd5b5f3560e01c9081636352211e14606c57506370a0823114602f575f80fd5b3460685760203660031901126068576004356001600160a01b038116908190036068575f526001602052602060405f2054604051908152f35b5f80fd5b3460685760203660031901126068576004355f90815260208181526040909120546001600160a01b0316825290f3fea2646970667358221220a0864b3879de6022a5f20540cf998ab8986a8bc06a6843df5278bd94e197d52664736f6c634300082100336080806040523460155761068b908161001a8239f35b5f80fdfe60806040526004361015610011575f80fd5b5f5f3560e01c806317cc73a01461030a57806395b9a383146100ca5763de4a5dcd1461003b575f80fd5b346100b95760203660031901126100b9578061005d61005861038f565b610432565b5f5160206106365f395f51905f523b156100c757604051632631f2b160e11b8152901515600482015281816024815f5160206106365f395f51905f525afa80156100bc576100a85750f35b816100b2916103a5565b6100b95780f35b80fd5b6040513d84823e3d90fd5b50fd5b50346100b95760403660031901126100b9576100e461038f565b6024356001600160a01b038116919082900361030657803b156102815782918280604051602081019063fe575a8760e01b82528460248201526024815261012c6044826103a5565b5190855afa9161013a6103db565b9215928315610264575b505f5160206106365f395f51905f523b1561025f57604051632631f2b160e11b8152921515600484015283836024815f5160206106365f395f51905f525afa918215610254578492610237575b8293506040516020810191630723eb0360e51b83526024820152602481526101ba6044826103a5565b51915afa6101c66103db565b901590811561021c575b505f5160206106365f395f51905f523b156100c757604051632631f2b160e11b8152901515600482015281816024815f5160206106365f395f51905f525afa80156100bc576100a85750f35b61023091506020808251830101910161041a565b155f6101d0565b91909281610244916103a5565b61025057818391610191565b5050fd5b6040513d86823e3d90fd5b505050fd5b6102799193506020808251830101910161041a565b15915f610144565b60405162461bcd60e51b815260206004820152605160248201527f53746443686561747320617373756d654e6f74426c61636b6c6973746564286160448201527f6464726573732c61646472657373293a20546f6b656e2061646472657373206960648201527039903737ba10309031b7b73a3930b1ba1760791b608482015260a490fd5b8280fd5b503461038b57602036600319011261038b5761032761005861038f565b155f5160206106365f395f51905f523b1561038b5760405190632631f2b160e11b825260048201525f816024815f5160206106365f395f51905f525afa801561038057610372575080f35b61037e91505f906103a5565b005b6040513d5f823e3d90fd5b5f80fd5b600435906001600160a01b038216820361038b57565b90601f8019910116810190811067ffffffffffffffff8211176103c757604052565b634e487b7160e01b5f52604160045260245ffd5b3d15610415573d9067ffffffffffffffff82116103c7576040519161040a601f8201601f1916602001846103a5565b82523d5f602084013e565b606090565b9081602091031261038b5751801515810361038b5790565b5f19813110156105a457479080315f5160206106365f395f51905f523b1561038b5760405163c88a5e6d60e01b8152306004820152600160248201525f92908381604481835f5160206106365f395f51905f525af180156103805761058f575b508280808060016001600160a01b0386165af1936104ae6103db565b505f5160206106365f395f51905f523b1561058b5760405163c88a5e6d60e01b815230600482015260248101919091528381604481835f5160206106365f395f51905f525af1801561025457908491610576575b50505f5160206106365f395f51905f523b156103065760405163c88a5e6d60e01b81526001600160a01b0391909116600482015260248101919091528181604481835f5160206106365f395f51905f525af180156100bc5761056357505090565b61056e8280926103a5565b6100b9575090565b81610580916103a5565b61030657825f610502565b8380fd5b61059c9193505f906103a5565b5f915f610492565b60405162461bcd60e51b815260206004820152605e60248201527f537464436865617473205f697350617961626c652861646472657373293a204260448201527f616c616e636520657175616c73206d61782075696e743235362c20736f20697460648201527f2063616e6e6f74207265636569766520616e79206d6f72652066756e64730000608482015260a490fdfe0000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da26469706673582212202286ba7b490a6ed2e21d62dd805d42d34d93a83baf9cb48a48a393a8d131e33064736f6c63430008210033608080604052346013576040908160188239f35b5f80fdfe36156008575f80fd5b00fea26469706673582212200d1a601e552da1591def0754c7f68b0886f1b9e8f0d55f77c7dece0deda0ad6764736f6c634300082100336080604081815269021e19e0c9bab24000007fa6eef7e35abe7026729641147f7915573c7e97b47efa546f5f6e3230263bcb49819055305f9081527fad3228b676f7d3cd4284a5443f17f1962b36e491b30a40b2405849e597ba5fb5602052919091205560d1908161006f8239f3fe60808060405260043610156011575f80fd5b5f3560e01c908162fdd58e14605a575063bd85b03914602e575f80fd5b3460565760203660031901126056576004355f526001602052602060405f2054604051908152f35b5f80fd5b3460565760403660031901126056576004356001600160a01b03811691908290036056576020916024355f525f835260405f20905f52825260405f20548152f3fea2646970667358221220b651e70a21708bba240ce38abbfa6134f514ef28cd4f59a0015ad0a80ea9d7ac64736f6c63430008210033537464436861696e7320736574436861696e28737472696e672c436861696e440000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da2646970667358221220be4b5ebfef57063d56400715a7852325f1999095b7e2180d8143ec9986049c1d64736f6c63430008210033"

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#15)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#15)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#15)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#15)
        """
        ...

    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#15)
        """
        return self._execute(self.chain, request_type, "0a9254e4", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_Skip(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#19)
        """
        ...

    @overload
    def test_Skip(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#19)
        """
        ...

    @overload
    def test_Skip(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#19)
        """
        ...

    @overload
    def test_Skip(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#19)
        """
        ...

    def test_Skip(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#19)
        """
        return self._execute(self.chain, request_type, "c54b6369", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_Rewind(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#25)
        """
        ...

    @overload
    def test_Rewind(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#25)
        """
        ...

    @overload
    def test_Rewind(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#25)
        """
        ...

    @overload
    def test_Rewind(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#25)
        """
        ...

    def test_Rewind(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#25)
        """
        return self._execute(self.chain, request_type, "d92b84b0", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_Hoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#31)
        """
        ...

    @overload
    def test_Hoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#31)
        """
        ...

    @overload
    def test_Hoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#31)
        """
        ...

    @overload
    def test_Hoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#31)
        """
        ...

    def test_Hoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#31)
        """
        return self._execute(self.chain, request_type, "bfc420f1", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_HoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#36)
        """
        ...

    @overload
    def test_HoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#36)
        """
        ...

    @overload
    def test_HoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#36)
        """
        ...

    @overload
    def test_HoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#36)
        """
        ...

    def test_HoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#36)
        """
        return self._execute(self.chain, request_type, "6dc2878a", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_HoaxDifferentAddresses(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#41)
        """
        ...

    @overload
    def test_HoaxDifferentAddresses(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#41)
        """
        ...

    @overload
    def test_HoaxDifferentAddresses(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#41)
        """
        ...

    @overload
    def test_HoaxDifferentAddresses(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#41)
        """
        ...

    def test_HoaxDifferentAddresses(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#41)
        """
        return self._execute(self.chain, request_type, "cfcd8c45", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StartHoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#46)
        """
        ...

    @overload
    def test_StartHoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#46)
        """
        ...

    @overload
    def test_StartHoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#46)
        """
        ...

    @overload
    def test_StartHoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#46)
        """
        ...

    def test_StartHoax(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#46)
        """
        return self._execute(self.chain, request_type, "1d4e5c12", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_StartHoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#54)
        """
        ...

    @overload
    def test_StartHoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#54)
        """
        ...

    @overload
    def test_StartHoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#54)
        """
        ...

    @overload
    def test_StartHoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#54)
        """
        ...

    def test_StartHoaxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#54)
        """
        return self._execute(self.chain, request_type, "58e8257b", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_ChangePrankMsgSender(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#62)
        """
        ...

    @overload
    def test_ChangePrankMsgSender(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#62)
        """
        ...

    @overload
    def test_ChangePrankMsgSender(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#62)
        """
        ...

    @overload
    def test_ChangePrankMsgSender(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#62)
        """
        ...

    def test_ChangePrankMsgSender(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#62)
        """
        return self._execute(self.chain, request_type, "78d56a69", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_ChangePrankMsgSenderAndTxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#72)
        """
        ...

    @overload
    def test_ChangePrankMsgSenderAndTxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#72)
        """
        ...

    @overload
    def test_ChangePrankMsgSenderAndTxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#72)
        """
        ...

    @overload
    def test_ChangePrankMsgSenderAndTxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#72)
        """
        ...

    def test_ChangePrankMsgSenderAndTxOrigin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#72)
        """
        return self._execute(self.chain, request_type, "66a38888", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_MakeAccountEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#82)
        """
        ...

    @overload
    def test_MakeAccountEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#82)
        """
        ...

    @overload
    def test_MakeAccountEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#82)
        """
        ...

    @overload
    def test_MakeAccountEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#82)
        """
        ...

    def test_MakeAccountEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#82)
        """
        return self._execute(self.chain, request_type, "00abe409", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_MakeAddrEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#89)
        """
        ...

    @overload
    def test_MakeAddrEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#89)
        """
        ...

    @overload
    def test_MakeAddrEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#89)
        """
        ...

    @overload
    def test_MakeAddrEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#89)
        """
        ...

    def test_MakeAddrEquivalence(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#89)
        """
        return self._execute(self.chain, request_type, "9d44b78a", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_MakeAddrSigning(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#94)
        """
        ...

    @overload
    def test_MakeAddrSigning(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#94)
        """
        ...

    @overload
    def test_MakeAddrSigning(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#94)
        """
        ...

    @overload
    def test_MakeAddrSigning(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#94)
        """
        ...

    def test_MakeAddrSigning(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#94)
        """
        return self._execute(self.chain, request_type, "ae428267", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_Deal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#102)
        """
        ...

    @overload
    def test_Deal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#102)
        """
        ...

    @overload
    def test_Deal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#102)
        """
        ...

    @overload
    def test_Deal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#102)
        """
        ...

    def test_Deal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#102)
        """
        return self._execute(self.chain, request_type, "058aeb3e", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DealToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#107)
        """
        ...

    @overload
    def test_DealToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#107)
        """
        ...

    @overload
    def test_DealToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#107)
        """
        ...

    @overload
    def test_DealToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#107)
        """
        ...

    def test_DealToken(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#107)
        """
        return self._execute(self.chain, request_type, "9755843b", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DealTokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#114)
        """
        ...

    @overload
    def test_DealTokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#114)
        """
        ...

    @overload
    def test_DealTokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#114)
        """
        ...

    @overload
    def test_DealTokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#114)
        """
        ...

    def test_DealTokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#114)
        """
        return self._execute(self.chain, request_type, "59ff1d87", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DealERC1155Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#125)
        """
        ...

    @overload
    def test_DealERC1155Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#125)
        """
        ...

    @overload
    def test_DealERC1155Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#125)
        """
        ...

    @overload
    def test_DealERC1155Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#125)
        """
        ...

    def test_DealERC1155Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#125)
        """
        return self._execute(self.chain, request_type, "bfac85a4", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DealERC1155TokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#132)
        """
        ...

    @overload
    def test_DealERC1155TokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#132)
        """
        ...

    @overload
    def test_DealERC1155TokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#132)
        """
        ...

    @overload
    def test_DealERC1155TokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#132)
        """
        ...

    def test_DealERC1155TokenAdjustTotalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#132)
        """
        return self._execute(self.chain, request_type, "f11dfb60", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DealERC721Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#143)
        """
        ...

    @overload
    def test_DealERC721Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#143)
        """
        ...

    @overload
    def test_DealERC721Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#143)
        """
        ...

    @overload
    def test_DealERC721Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#143)
        """
        ...

    def test_DealERC721Token(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#143)
        """
        return self._execute(self.chain, request_type, "d31d7c1d", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DeployCode(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#154)
        """
        ...

    @overload
    def test_DeployCode(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#154)
        """
        ...

    @overload
    def test_DeployCode(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#154)
        """
        ...

    @overload
    def test_DeployCode(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#154)
        """
        ...

    def test_DeployCode(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#154)
        """
        return self._execute(self.chain, request_type, "0ad2b4c8", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DestroyAccount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#159)
        """
        ...

    @overload
    def test_DestroyAccount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#159)
        """
        ...

    @overload
    def test_DestroyAccount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#159)
        """
        ...

    @overload
    def test_DestroyAccount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#159)
        """
        ...

    def test_DestroyAccount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#159)
        """
        return self._execute(self.chain, request_type, "4440c545", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DeployCodeNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#186)
        """
        ...

    @overload
    def test_DeployCodeNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#186)
        """
        ...

    @overload
    def test_DeployCodeNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#186)
        """
        ...

    @overload
    def test_DeployCodeNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#186)
        """
        ...

    def test_DeployCodeNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#186)
        """
        return self._execute(self.chain, request_type, "f930b628", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DeployCodeVal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#191)
        """
        ...

    @overload
    def test_DeployCodeVal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#191)
        """
        ...

    @overload
    def test_DeployCodeVal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#191)
        """
        ...

    @overload
    def test_DeployCodeVal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#191)
        """
        ...

    def test_DeployCodeVal(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#191)
        """
        return self._execute(self.chain, request_type, "bb11ac10", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DeployCodeValNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#197)
        """
        ...

    @overload
    def test_DeployCodeValNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#197)
        """
        ...

    @overload
    def test_DeployCodeValNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#197)
        """
        ...

    @overload
    def test_DeployCodeValNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#197)
        """
        ...

    def test_DeployCodeValNoArgs(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#197)
        """
        return self._execute(self.chain, request_type, "413cfcb1", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deployCodeHelper(self, what: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#204)

        Args:
            what: string
        """
        ...

    @overload
    def deployCodeHelper(self, what: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#204)

        Args:
            what: string
        """
        ...

    @overload
    def deployCodeHelper(self, what: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#204)

        Args:
            what: string
        """
        ...

    @overload
    def deployCodeHelper(self, what: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#204)

        Args:
            what: string
        """
        ...

    def deployCodeHelper(self, what: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#204)

        Args:
            what: string
        """
        return self._execute(self.chain, request_type, "4af967d1", [what], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_RevertIf_DeployCodeFail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#208)
        """
        ...

    @overload
    def test_RevertIf_DeployCodeFail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#208)
        """
        ...

    @overload
    def test_RevertIf_DeployCodeFail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#208)
        """
        ...

    @overload
    def test_RevertIf_DeployCodeFail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#208)
        """
        ...

    def test_RevertIf_DeployCodeFail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#208)
        """
        return self._execute(self.chain, request_type, "6954ee50", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DeriveRememberKey(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#230)
        """
        ...

    @overload
    def test_DeriveRememberKey(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#230)
        """
        ...

    @overload
    def test_DeriveRememberKey(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#230)
        """
        ...

    @overload
    def test_DeriveRememberKey(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#230)
        """
        ...

    def test_DeriveRememberKey(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#230)
        """
        return self._execute(self.chain, request_type, "2ac9eedb", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_BytesToUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#238)
        """
        ...

    @overload
    def test_BytesToUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#238)
        """
        ...

    @overload
    def test_BytesToUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#238)
        """
        ...

    @overload
    def test_BytesToUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#238)
        """
        ...

    def test_BytesToUint(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#238)
        """
        return self._execute(self.chain, request_type, "0d2bf636", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_ParseJsonTxDetail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#245)
        """
        ...

    @overload
    def test_ParseJsonTxDetail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#245)
        """
        ...

    @overload
    def test_ParseJsonTxDetail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#245)
        """
        ...

    @overload
    def test_ParseJsonTxDetail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#245)
        """
        ...

    def test_ParseJsonTxDetail(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#245)
        """
        return self._execute(self.chain, request_type, "bd9fb259", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_ReadEIP1559Transaction(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#264)
        """
        ...

    @overload
    def test_ReadEIP1559Transaction(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#264)
        """
        ...

    @overload
    def test_ReadEIP1559Transaction(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#264)
        """
        ...

    @overload
    def test_ReadEIP1559Transaction(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#264)
        """
        ...

    def test_ReadEIP1559Transaction(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#264)
        """
        return self._execute(self.chain, request_type, "ae0ddbc8", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_ReadEIP1559Transactions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#272)
        """
        ...

    @overload
    def test_ReadEIP1559Transactions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#272)
        """
        ...

    @overload
    def test_ReadEIP1559Transactions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#272)
        """
        ...

    @overload
    def test_ReadEIP1559Transactions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#272)
        """
        ...

    def test_ReadEIP1559Transactions(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#272)
        """
        return self._execute(self.chain, request_type, "cf99d3dd", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_ReadReceipt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#279)
        """
        ...

    @overload
    def test_ReadReceipt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#279)
        """
        ...

    @overload
    def test_ReadReceipt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#279)
        """
        ...

    @overload
    def test_ReadReceipt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#279)
        """
        ...

    def test_ReadReceipt(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#279)
        """
        return self._execute(self.chain, request_type, "22b4de51", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_ReadReceipts(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#290)
        """
        ...

    @overload
    def test_ReadReceipts(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#290)
        """
        ...

    @overload
    def test_ReadReceipts(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#290)
        """
        ...

    @overload
    def test_ReadReceipts(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#290)
        """
        ...

    def test_ReadReceipts(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#290)
        """
        return self._execute(self.chain, request_type, "99c87c55", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_GasMeteringModifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#297)
        """
        ...

    @overload
    def test_GasMeteringModifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#297)
        """
        ...

    @overload
    def test_GasMeteringModifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#297)
        """
        ...

    @overload
    def test_GasMeteringModifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#297)
        """
        ...

    def test_GasMeteringModifier(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#297)
        """
        return self._execute(self.chain, request_type, "893329ac", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_AssumeAddressIsNot(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#337)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeAddressIsNot(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#337)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeAddressIsNot(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#337)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeAddressIsNot(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#337)

        Args:
            addr: address
        """
        ...

    def testFuzz_AssumeAddressIsNot(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#337)

        Args:
            addr: address
        """
        return self._execute(self.chain, request_type, "4a1297f8", [addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_AssumePayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#347)
        """
        ...

    @overload
    def test_AssumePayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#347)
        """
        ...

    @overload
    def test_AssumePayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#347)
        """
        ...

    @overload
    def test_AssumePayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#347)
        """
        ...

    def test_AssumePayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#347)
        """
        return self._execute(self.chain, request_type, "61266422", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_AssumeNotPayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#375)
        """
        ...

    @overload
    def test_AssumeNotPayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#375)
        """
        ...

    @overload
    def test_AssumeNotPayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#375)
        """
        ...

    @overload
    def test_AssumeNotPayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#375)
        """
        ...

    def test_AssumeNotPayable(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#375)
        """
        return self._execute(self.chain, request_type, "9bacb2a8", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_AssumeNotPrecompile(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#402)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotPrecompile(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#402)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotPrecompile(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#402)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotPrecompile(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#402)

        Args:
            addr: address
        """
        ...

    def testFuzz_AssumeNotPrecompile(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#402)

        Args:
            addr: address
        """
        return self._execute(self.chain, request_type, "9d624fa1", [addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_AssumeNotForgeAddress(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#410)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotForgeAddress(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#410)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotForgeAddress(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#410)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotForgeAddress(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#410)

        Args:
            addr: address
        """
        ...

    def testFuzz_AssumeNotForgeAddress(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#410)

        Args:
            addr: address
        """
        return self._execute(self.chain, request_type, "751ec69d", [addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_RevertIf_CannotDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#418)
        """
        ...

    @overload
    def test_RevertIf_CannotDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#418)
        """
        ...

    @overload
    def test_RevertIf_CannotDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#418)
        """
        ...

    @overload
    def test_RevertIf_CannotDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#418)
        """
        ...

    def test_RevertIf_CannotDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#418)
        """
        return self._execute(self.chain, request_type, "c49eb4c7", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def _revertDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#423)
        """
        ...

    @overload
    def _revertDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#423)
        """
        ...

    @overload
    def _revertDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#423)
        """
        ...

    @overload
    def _revertDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#423)
        """
        ...

    def _revertDeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#423)
        """
        return self._execute(self.chain, request_type, "ce73c449", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_DeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#427)
        """
        ...

    @overload
    def test_DeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#427)
        """
        ...

    @overload
    def test_DeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#427)
        """
        ...

    @overload
    def test_DeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#427)
        """
        ...

    def test_DeployCodeTo(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#427)
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
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#446)
    """
    _abi = {b'\x95\xb9\xa3\x83': {'inputs': [{'internalType': 'address', 'name': 'token', 'type': 'address'}, {'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'exposed_assumeNotBlacklisted', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\x17\xccs\xa0': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'exposed_assumeNotPayable', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xdeJ]\xcd': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'exposed_assumePayable', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":3680,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"gasMeteringOff","offset":0,"slot":0,"type":"t_bool"},{"astId":5747,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"stdstore","offset":0,"slot":1,"type":"t_struct(StdStorage)8017_storage"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage))"},"t_mapping(t_bytes32,t_struct(FindData)7992_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)7992_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)7992_storage)"},"t_struct(FindData)7992_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":7985,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":7987,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":7989,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":7991,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(StdStorage)8017_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":8001,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage)))"},{"astId":8004,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":8006,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":8008,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":8010,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":8012,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":8014,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":8016,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsMock","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "6080806040523460155761068b908161001a8239f35b5f80fdfe60806040526004361015610011575f80fd5b5f5f3560e01c806317cc73a01461030a57806395b9a383146100ca5763de4a5dcd1461003b575f80fd5b346100b95760203660031901126100b9578061005d61005861038f565b610432565b5f5160206106365f395f51905f523b156100c757604051632631f2b160e11b8152901515600482015281816024815f5160206106365f395f51905f525afa80156100bc576100a85750f35b816100b2916103a5565b6100b95780f35b80fd5b6040513d84823e3d90fd5b50fd5b50346100b95760403660031901126100b9576100e461038f565b6024356001600160a01b038116919082900361030657803b156102815782918280604051602081019063fe575a8760e01b82528460248201526024815261012c6044826103a5565b5190855afa9161013a6103db565b9215928315610264575b505f5160206106365f395f51905f523b1561025f57604051632631f2b160e11b8152921515600484015283836024815f5160206106365f395f51905f525afa918215610254578492610237575b8293506040516020810191630723eb0360e51b83526024820152602481526101ba6044826103a5565b51915afa6101c66103db565b901590811561021c575b505f5160206106365f395f51905f523b156100c757604051632631f2b160e11b8152901515600482015281816024815f5160206106365f395f51905f525afa80156100bc576100a85750f35b61023091506020808251830101910161041a565b155f6101d0565b91909281610244916103a5565b61025057818391610191565b5050fd5b6040513d86823e3d90fd5b505050fd5b6102799193506020808251830101910161041a565b15915f610144565b60405162461bcd60e51b815260206004820152605160248201527f53746443686561747320617373756d654e6f74426c61636b6c6973746564286160448201527f6464726573732c61646472657373293a20546f6b656e2061646472657373206960648201527039903737ba10309031b7b73a3930b1ba1760791b608482015260a490fd5b8280fd5b503461038b57602036600319011261038b5761032761005861038f565b155f5160206106365f395f51905f523b1561038b5760405190632631f2b160e11b825260048201525f816024815f5160206106365f395f51905f525afa801561038057610372575080f35b61037e91505f906103a5565b005b6040513d5f823e3d90fd5b5f80fd5b600435906001600160a01b038216820361038b57565b90601f8019910116810190811067ffffffffffffffff8211176103c757604052565b634e487b7160e01b5f52604160045260245ffd5b3d15610415573d9067ffffffffffffffff82116103c7576040519161040a601f8201601f1916602001846103a5565b82523d5f602084013e565b606090565b9081602091031261038b5751801515810361038b5790565b5f19813110156105a457479080315f5160206106365f395f51905f523b1561038b5760405163c88a5e6d60e01b8152306004820152600160248201525f92908381604481835f5160206106365f395f51905f525af180156103805761058f575b508280808060016001600160a01b0386165af1936104ae6103db565b505f5160206106365f395f51905f523b1561058b5760405163c88a5e6d60e01b815230600482015260248101919091528381604481835f5160206106365f395f51905f525af1801561025457908491610576575b50505f5160206106365f395f51905f523b156103065760405163c88a5e6d60e01b81526001600160a01b0391909116600482015260248101919091528181604481835f5160206106365f395f51905f525af180156100bc5761056357505090565b61056e8280926103a5565b6100b9575090565b81610580916103a5565b61030657825f610502565b8380fd5b61059c9193505f906103a5565b5f915f610492565b60405162461bcd60e51b815260206004820152605e60248201527f537464436865617473205f697350617961626c652861646472657373293a204260448201527f616c616e636520657175616c73206d61782075696e743235362c20736f20697460648201527f2063616e6e6f74207265636569766520616e79206d6f72652066756e64730000608482015260a490fdfe0000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da26469706673582212202286ba7b490a6ed2e21d62dd805d42d34d93a83baf9cb48a48a393a8d131e33064736f6c63430008210033"

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#447)

        Args:
            addr: address
        """
        ...

    @overload
    def exposed_assumePayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#447)

        Args:
            addr: address
        """
        ...

    @overload
    def exposed_assumePayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#447)

        Args:
            addr: address
        """
        ...

    @overload
    def exposed_assumePayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#447)

        Args:
            addr: address
        """
        ...

    def exposed_assumePayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#447)

        Args:
            addr: address
        """
        return self._execute(self.chain, request_type, "de4a5dcd", [addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def exposed_assumeNotPayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#451)

        Args:
            addr: address
        """
        ...

    @overload
    def exposed_assumeNotPayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#451)

        Args:
            addr: address
        """
        ...

    @overload
    def exposed_assumeNotPayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#451)

        Args:
            addr: address
        """
        ...

    @overload
    def exposed_assumeNotPayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#451)

        Args:
            addr: address
        """
        ...

    def exposed_assumeNotPayable(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#451)

        Args:
            addr: address
        """
        return self._execute(self.chain, request_type, "17cc73a0", [addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def exposed_assumeNotBlacklisted(self, token: Union[Account, Address], addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#456)

        Args:
            token: address
            addr: address
        """
        ...

    @overload
    def exposed_assumeNotBlacklisted(self, token: Union[Account, Address], addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#456)

        Args:
            token: address
            addr: address
        """
        ...

    @overload
    def exposed_assumeNotBlacklisted(self, token: Union[Account, Address], addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#456)

        Args:
            token: address
            addr: address
        """
        ...

    @overload
    def exposed_assumeNotBlacklisted(self, token: Union[Account, Address], addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#456)

        Args:
            token: address
            addr: address
        """
        ...

    def exposed_assumeNotBlacklisted(self, token: Union[Account, Address], addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#456)

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
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#461)
    """
    _abi = {b'\x9c\x95U\xb1\xe3\x10.<\xf4\x8fB}y\xcbg\x8f]\x9b\xd1\xed\n\xd5t8\x94a\xe2U\xf9Qp\xed': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'who', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes4', 'name': 'fsig', 'type': 'bytes4'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'keysHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'slot', 'type': 'uint256'}], 'name': 'SlotFound', 'type': 'event'}, b'\x08\x0f\xc4\xa9f \xc4F.p[#\xf3FA?\xe3yk\xb6<o\x8d\x85\x91\xba\xec\x0e#\x15w\xa5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'who', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'slot', 'type': 'uint256'}], 'name': 'WARNING_UninitedSlot', 'type': 'event'}, b'A0O\xac\xd92=u\xb1\x1b\xcd\xd6\t\xcb8\xef\xff\xfd\xb0W\x10\xf7\xca\xf0\xe9\xb1lm\x9dp\x9fP': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log', 'type': 'event'}, b'z\xe7LRt\x14\xae\x13_\xd9pG\xb1)!\xa5\xec9\x11\xb8\x04\x19xU\xd6~%\xc7\xb7^\xe6\xf3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'log_address', 'type': 'event'}, b'\xfb\x10(e\xd5\n\xdd\xdd\xf6\x9d\xa9\xb5\xaa\x1b\xce\xd6l\x80\xcf\x86\x9a\\\x8d\x04q\xa4g\xe1\x8c\xe9\xca\xb1': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_array', 'type': 'event'}, b'\x89\n\x82g\x9bG\x0f+\xd8(\x16\xed\x9b\x16\x1f\x97\xd8\xb9g\xf3\x7f\xa3d|!\xd5\xbf9t\x9e-\xd5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_array', 'type': 'event'}, b'@\xe1\x84\x0fWi\x07=a\xbd\x017-\x9bu\xba\xa9\x84-V)\xa0\xc9\x9f\xf1\x03\xbe\x11x\xa8\xe9\xe2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_array', 'type': 'event'}, b'#\xb6*\xd0XM$\xa7_\x0b\xf3V\x03\x91\xefVY\xecm\xb1&\x9cV\xe1\x1a\xa2A\xd67\xf1\x9b ': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'log_bytes', 'type': 'event'}, b'\xe8\x16\x99\xb8Q\x13\xee\xa1\xc7>\x10X\x8b+\x03^U\x893ic!s\xaf\xd4?\xeb\x19/\xacd\xe3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'log_bytes32', 'type': 'event'}, b'\x0e\xb5\xd5&$\xc8\xd2\x8a\xda\x9f\xc5Z\x8cP.\xd5\xaa?\xbe/\xb6\xe9\x1bq\xb5\xf3v\x88+\x1d/\xb8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256', 'name': '', 'type': 'int256'}], 'name': 'log_int', 'type': 'event'}, b'\x9cN\x85A\xca\x8f\r\xc1\xc4\x13\xf9\x10\x8ff\xd8-<\xec\xb1\xbd\xdb\xceCza\xca\xa3\x17\\L\xc9o': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address', 'name': 'val', 'type': 'address'}], 'name': 'log_named_address', 'type': 'event'}, b'\x00\xaa\xa3\x9c\x9f\xfb_VzE48\x0cspup.\x1f\x7f\x14\x10\x7f\xc9S(\xe3\xb5l\x03%\xfb': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xa7>\xda\tf/F\xdd\xe7)\xbeF\x118_\xf3O\xe6\xc4O\xbb\xc6\xf7\xe1{\x04+Y\xa3D[W': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_named_array', 'type': 'event'}, b";\xcf\xb2\xae.\x8d\x13-\xd1\xfc\xe7\xcf'\x8a\x9a\x19uj\x9f\xce\xab\xe4p\xdf;\xda\xbbK\xc5w\xd1\xbd": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xd2n\x16\xca\xd4T\x87\x05\xe4\xc9\xe2\xd9O\x98\xee\x91\xc2\x89\x08^\xe4%YO\xd5c_\xa2\x96L\xcf\x18': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'val', 'type': 'bytes'}], 'name': 'log_named_bytes', 'type': 'event'}, b'\xaf\xb7\x95\xc9\xc6\x1eO\xe7F\x8c8o\x92]zT)\xec\xad\x9c\x04\x95\xdd\xb8\xd3\x8di\x06\x14\xd3/\x99': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'val', 'type': 'bytes32'}], 'name': 'log_named_bytes32', 'type': 'event'}, b']\xa6\xce\x9dQ\x15\x1b\xa1\x0c\t\xa5Y\xef$\xd5 \xb9\xda\xc5\xc5\xb8\x81\n\xe8CNM\r\x86A\x1a\x95': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_int', 'type': 'event'}, b"\xeb\x8b\xa4<\xedu7B\x19F\xbdC\xe8(\xb8\xb2\xb8B\x89'\xaa\x8f\x80\x1c\x13\xd94\xbf\x11\xac\xa5{": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_uint', 'type': 'event'}, b'/\xe62w\x91t7CxD*\x8e\x97\x8b\xcc\xfb\xdc\xc1\xd6\xb2\xb0\xd8\x1f~\x8e\xb7v\xab"\x86\xf1h': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}], 'name': 'log_named_int', 'type': 'event'}, b'(\x0fDF\xb2\x8a\x13rA}\xdae\x8d0\xb9[)\x92\xb1*\xc9\xc7\xf3xS_)\xa9z\xcf5\x83': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'val', 'type': 'string'}], 'name': 'log_named_string', 'type': 'event'}, b'\xb2\xde/\xbe\x80\x1a\r\xf6\xc0\xcb\xdd\xfdD\x8b\xa3\xc4\x1dH\xa0@\xca5\xc5l\x81\x96\xef\x0f\xca\xe7!\xa8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}], 'name': 'log_named_uint', 'type': 'event'}, b'\x0b.\x13\xff \xac{GA\x98eU\x83\xed\xf7\r\xed\xd2\xc1\xdc\x98\x0e2\x9cO\xbb/\xc0t\x8byk': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log_string', 'type': 'event'}, b',\xab\x97\x90Q\x0f\xd8\xbd\xfb\xd2\x11R\x88\xdb3\xfe\xc6f\x91\xd4v\xef\xc5B|\xfdL\ti0\x17U': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'log_uint', 'type': 'event'}, b"\xe7\x95\x0e\xde\x03\x94\xb9\xf2\xceJZ\x1b\xf5\xa7\xe1\x85$\x11\xf7\xe6f\x1bC\x08\xc9\x13\xc4\xbf\xd1\x10'\xe4": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'logs', 'type': 'event'}, b'\xfav&\xd4': {'inputs': [], 'name': 'IS_TEST', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb5P\x8a\xa9': {'inputs': [], 'name': 'excludeArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'excludedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe2\x0c\x9fq': {'inputs': [], 'name': 'excludeContracts', 'outputs': [{'internalType': 'address[]', 'name': 'excludedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb0FO\xdc': {'inputs': [], 'name': 'excludeSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'excludedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x1e\xd7\x83\x1c': {'inputs': [], 'name': 'excludeSenders', 'outputs': [{'internalType': 'address[]', 'name': 'excludedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbaAO\xa6': {'inputs': [], 'name': 'failed', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\n\x92T\xe4': {'inputs': [], 'name': 'setUp', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'f\xd9\xa9\xa0': {'inputs': [], 'name': 'targetArtifactSelectors', 'outputs': [{'components': [{'internalType': 'string', 'name': 'artifact', 'type': 'string'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzArtifactSelector[]', 'name': 'targetedArtifactSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x85"l\x81': {'inputs': [], 'name': 'targetArtifacts', 'outputs': [{'internalType': 'string[]', 'name': 'targetedArtifacts_', 'type': 'string[]'}], 'stateMutability': 'view', 'type': 'function'}, b'?r\x86\xf4': {'inputs': [], 'name': 'targetContracts', 'outputs': [{'internalType': 'address[]', 'name': 'targetedContracts_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'*\xde8\x80': {'inputs': [], 'name': 'targetInterfaces', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'string[]', 'name': 'artifacts', 'type': 'string[]'}], 'internalType': 'struct StdInvariant.FuzzInterface[]', 'name': 'targetedInterfaces_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\x91j\x17\xc6': {'inputs': [], 'name': 'targetSelectors', 'outputs': [{'components': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}, {'internalType': 'bytes4[]', 'name': 'selectors', 'type': 'bytes4[]'}], 'internalType': 'struct StdInvariant.FuzzSelector[]', 'name': 'targetedSelectors_', 'type': 'tuple[]'}], 'stateMutability': 'view', 'type': 'function'}, b'>^<#': {'inputs': [], 'name': 'targetSenders', 'outputs': [{'internalType': 'address[]', 'name': 'targetedSenders_', 'type': 'address[]'}], 'stateMutability': 'view', 'type': 'function'}, b'W.k\x91': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'testFuzz_AssumeNotBlacklisted_TokenWithoutBlacklist', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\xc8y\xdf\xd7': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'testFuzz_AssumeNotBlacklisted_USDC', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\xf6K\x9d\xc8': {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'testFuzz_AssumeNotBlacklisted_USDT', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, b'\xedc\xe2J': {'inputs': [], 'name': 'test_RevertIf_AssumeNoBlacklisted_USDC', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xda\xd8W\xaa': {'inputs': [], 'name': 'test_RevertIf_AssumeNoBlacklisted_USDT', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfd.\x18\x8f': {'inputs': [], 'name': 'test_RevertIf_CannotAssumeNoBlacklisted_EOA', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'*\x14\xa6\xaa': {'inputs': [], 'name': 'test_dealUSDC', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":61,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"stdstore","offset":0,"slot":0,"type":"t_struct(StdStorage)8017_storage"},{"astId":218,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_failed","offset":0,"slot":8,"type":"t_bool"},{"astId":2719,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"stdChainsInitialized","offset":1,"slot":8,"type":"t_bool"},{"astId":2740,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"chains","offset":0,"slot":9,"type":"t_mapping(t_string_memory_ptr,t_struct(Chain)2735_storage)"},{"astId":2744,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"defaultRpcUrls","offset":0,"slot":10,"type":"t_mapping(t_string_memory_ptr,t_string_storage)"},{"astId":2748,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"idToAlias","offset":0,"slot":11,"type":"t_mapping(t_uint256,t_string_storage)"},{"astId":2751,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"fallbackToDefaultRpcUrls","offset":0,"slot":12,"type":"t_bool"},{"astId":3680,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"gasMeteringOff","offset":1,"slot":12,"type":"t_bool"},{"astId":5747,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"stdstore","offset":0,"slot":13,"type":"t_struct(StdStorage)8017_storage"},{"astId":6623,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_excludedContracts","offset":0,"slot":21,"type":"t_array(t_address)dyn_storage"},{"astId":6626,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_excludedSenders","offset":0,"slot":22,"type":"t_array(t_address)dyn_storage"},{"astId":6629,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_targetedContracts","offset":0,"slot":23,"type":"t_array(t_address)dyn_storage"},{"astId":6632,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_targetedSenders","offset":0,"slot":24,"type":"t_array(t_address)dyn_storage"},{"astId":6635,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_excludedArtifacts","offset":0,"slot":25,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6638,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_targetedArtifacts","offset":0,"slot":26,"type":"t_array(t_string_storage)dyn_storage"},{"astId":6642,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_targetedArtifactSelectors","offset":0,"slot":27,"type":"t_array(t_struct(FuzzArtifactSelector)6614_storage)dyn_storage"},{"astId":6646,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_excludedSelectors","offset":0,"slot":28,"type":"t_array(t_struct(FuzzSelector)6608_storage)dyn_storage"},{"astId":6650,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_targetedSelectors","offset":0,"slot":29,"type":"t_array(t_struct(FuzzSelector)6608_storage)dyn_storage"},{"astId":6654,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_targetedInterfaces","offset":0,"slot":30,"type":"t_array(t_struct(FuzzInterface)6620_storage)dyn_storage"},{"astId":12907,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"IS_TEST","offset":0,"slot":31,"type":"t_bool"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_array(t_address)dyn_storage":{"encoding":"dynamic_array","label":"address[]","numberOfBytes":32,"base":"t_address"},"t_array(t_bytes32)dyn_storage":{"encoding":"dynamic_array","label":"bytes32[]","numberOfBytes":32,"base":"t_bytes32"},"t_array(t_bytes4)dyn_storage":{"encoding":"dynamic_array","label":"bytes4[]","numberOfBytes":32,"base":"t_bytes4"},"t_array(t_string_storage)dyn_storage":{"encoding":"dynamic_array","label":"string[]","numberOfBytes":32,"base":"t_string_storage"},"t_array(t_struct(FuzzArtifactSelector)6614_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzArtifactSelector[]","numberOfBytes":32,"base":"t_struct(FuzzArtifactSelector)6614_storage"},"t_array(t_struct(FuzzInterface)6620_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzInterface[]","numberOfBytes":32,"base":"t_struct(FuzzInterface)6620_storage"},"t_array(t_struct(FuzzSelector)6608_storage)dyn_storage":{"encoding":"dynamic_array","label":"struct StdInvariant.FuzzSelector[]","numberOfBytes":32,"base":"t_struct(FuzzSelector)6608_storage"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_bytes4":{"encoding":"inplace","label":"bytes4","numberOfBytes":4},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage)))":{"encoding":"mapping","label":"mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage))"},"t_mapping(t_bytes32,t_struct(FindData)7992_storage)":{"encoding":"mapping","label":"mapping(bytes32 => struct FindData)","numberOfBytes":32,"key":"t_bytes32","value":"t_struct(FindData)7992_storage"},"t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage))":{"encoding":"mapping","label":"mapping(bytes4 => mapping(bytes32 => struct FindData))","numberOfBytes":32,"key":"t_bytes4","value":"t_mapping(t_bytes32,t_struct(FindData)7992_storage)"},"t_mapping(t_string_memory_ptr,t_string_storage)":{"encoding":"mapping","label":"mapping(string => string)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_string_storage"},"t_mapping(t_string_memory_ptr,t_struct(Chain)2735_storage)":{"encoding":"mapping","label":"mapping(string => struct StdChains.Chain)","numberOfBytes":32,"key":"t_string_memory_ptr","value":"t_struct(Chain)2735_storage"},"t_mapping(t_uint256,t_string_storage)":{"encoding":"mapping","label":"mapping(uint256 => string)","numberOfBytes":32,"key":"t_uint256","value":"t_string_storage"},"t_string_memory_ptr":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(Chain)2735_storage":{"encoding":"inplace","label":"struct StdChains.Chain","numberOfBytes":128,"members":[{"astId":2728,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"name","offset":0,"slot":0,"type":"t_string_storage"},{"astId":2730,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"chainId","offset":0,"slot":1,"type":"t_uint256"},{"astId":2732,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"chainAlias","offset":0,"slot":2,"type":"t_string_storage"},{"astId":2734,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"rpcUrl","offset":0,"slot":3,"type":"t_string_storage"}]},"t_struct(FindData)7992_storage":{"encoding":"inplace","label":"struct FindData","numberOfBytes":128,"members":[{"astId":7985,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"slot","offset":0,"slot":0,"type":"t_uint256"},{"astId":7987,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"offsetLeft","offset":0,"slot":1,"type":"t_uint256"},{"astId":7989,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"offsetRight","offset":0,"slot":2,"type":"t_uint256"},{"astId":7991,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"found","offset":0,"slot":3,"type":"t_bool"}]},"t_struct(FuzzArtifactSelector)6614_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzArtifactSelector","numberOfBytes":64,"members":[{"astId":6610,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"artifact","offset":0,"slot":0,"type":"t_string_storage"},{"astId":6613,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(FuzzInterface)6620_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzInterface","numberOfBytes":64,"members":[{"astId":6616,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6619,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"artifacts","offset":0,"slot":1,"type":"t_array(t_string_storage)dyn_storage"}]},"t_struct(FuzzSelector)6608_storage":{"encoding":"inplace","label":"struct StdInvariant.FuzzSelector","numberOfBytes":64,"members":[{"astId":6604,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"addr","offset":0,"slot":0,"type":"t_address"},{"astId":6607,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"selectors","offset":0,"slot":1,"type":"t_array(t_bytes4)dyn_storage"}]},"t_struct(StdStorage)8017_storage":{"encoding":"inplace","label":"struct StdStorage","numberOfBytes":256,"members":[{"astId":8001,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"finds","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_bytes4,t_mapping(t_bytes32,t_struct(FindData)7992_storage)))"},{"astId":8004,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_keys","offset":0,"slot":1,"type":"t_array(t_bytes32)dyn_storage"},{"astId":8006,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_sig","offset":0,"slot":2,"type":"t_bytes4"},{"astId":8008,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_depth","offset":0,"slot":3,"type":"t_uint256"},{"astId":8010,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_target","offset":0,"slot":4,"type":"t_address"},{"astId":8012,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_set","offset":0,"slot":5,"type":"t_bytes32"},{"astId":8014,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_enable_packed_slots","offset":0,"slot":6,"type":"t_bool"},{"astId":8016,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:StdCheatsForkTest","label":"_calldata","offset":0,"slot":7,"type":"t_bytes_storage"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60808060405234602f57600160ff19600c541617600c55600160ff19601f541617601f5561380090816100348239f35b5f80fdfe6080806040526004361015610012575f80fd5b5f905f3560e01c9081630a9254e414611c79575080631ed7831c14611bfc5780632a14a6aa146112de5780632ade38801461111f5780633e5e3c23146110a15780633f7286f414611023578063572e6b9114610df257806366d9a9a014610cc957806385226c8114610c37578063916a17c614610b8f578063b0464fdc14610ae7578063b5508aa914610a4e578063ba414fa614610a29578063c879dfd71461081d578063dad857aa14610717578063e20c9f7114610689578063ed63e24a14610587578063f64b9dc8146102fd578063fa7626d4146102da5763fd2e188f146100fa575f80fd5b34610238578060031936011261023857604051906106a591828101928184106001600160401b038511176102c657829382916130e68339039082f080156102b9576040516001625e79b760e01b0319815260016004820152906020826024815f51602061378b5f395f51905f525afa9182156102ae57839261026a575b505f51602061378b5f395f51905f523b156102465760405163f28dceb360e01b815260206004820152605160248201526101b360448201612266565b838160a481835f51602061378b5f395f51905f525af190811561025f57849161024a575b50506001600160a01b031690813b15610246576040516395b9a38360e01b81526001600160a01b03909116600482015260248101839052908290829060449082905afa801561023b576102275750f35b8161023191611eaf565b6102385780f35b80fd5b6040513d84823e3d90fd5b5050fd5b8161025491611eaf565b61024657825f6101d7565b6040513d86823e3d90fd5b9091506020813d6020116102a6575b8161028660209383611eaf565b8101031261024657516001600160a01b038116810361024657905f610177565b3d9150610279565b6040513d85823e3d90fd5b50604051903d90823e3d90fd5b634e487b7160e01b83526041600452602483fd5b5034610238578060031936011261023857602060ff601f54166040519015158152f35b5034610238576020366003190112610238576004356001600160a01b0381169081900361050d5773dac17f958d2ee523a2206206994597c13d831ec73b1561055c57818080604051602081019063fe575a8760e01b825285602482015260248152610369604482611eaf565b519073dac17f958d2ee523a2206206994597c13d831ec75afa61038a6122e6565b9015908115610541575b505f51602061378b5f395f51905f523b1561050d57604051632631f2b160e11b8152901515600482015281816024815f51602061378b5f395f51905f525afa801561023b5761052c575b5080806040516020810190630723eb0360e51b825285602482015260248152610408604482611eaf565b519073dac17f958d2ee523a2206206994597c13d831ec75afa6104296122e6565b9015908115610511575b505f51602061378b5f395f51905f523b1561050d57604051632631f2b160e11b8152901515600482015281816024815f51602061378b5f395f51905f525afa801561023b576104f8575b505060405190630723eb0360e51b8252600482015260208160248173dac17f958d2ee523a2206206994597c13d831ec75afa801561023b576104c69183916104c9575b50612315565b80f35b6104eb915060203d6020116104f1575b6104e38183611eaf565b81019061224e565b5f6104c0565b503d6104d9565b8161050291611eaf565b61050d57815f61047d565b5080fd5b61052591506020808251830101910161224e565b155f610433565b8161053691611eaf565b61050d57815f6103de565b61055591506020808251830101910161224e565b155f610394565b60405162461bcd60e51b8152602060048201526051602482015260a49061058560448201612266565bfd5b5034610238578060031936011261023857604051906106a591828101928184106001600160401b038511176102c657829382916130e68339039082f080156102b9575f51602061378b5f395f51905f523b1561067157604051633d21120560e21b81528281600481835f51602061378b5f395f51905f525af19081156102ae578391610674575b50506001600160a01b0316803b156106715781604491604051928380926395b9a38360e01b82525f5160206137ab5f395f51905f526004830152731e34a77868e19a6647b1f2f47b51ed72dede95dd60248301525afa801561023b576102275750f35b50fd5b8161067e91611eaf565b61067157815f61060e565b503461023857806003193601126102385760405160158054808352908352909160208301917f55f448fdea98c4d29eb340757ef0a66cd03dbb9538908a6a81d96026b71ec475915b8181106106f8576106f4856106e881870382611eaf565b60405191829182611d07565b0390f35b82546001600160a01b03168452602090930192600192830192016106d1565b5034610238578060031936011261023857604051906106a591828101928184106001600160401b038511176102c657829382916130e68339039082f080156102b9575f51602061378b5f395f51905f523b1561067157604051633d21120560e21b81528281600481835f51602061378b5f395f51905f525af19081156102ae578391610808575b50506001600160a01b0316803b156106715781604491604051928380926395b9a38360e01b825273dac17f958d2ee523a2206206994597c13d831ec76004830152738f8a8f4b54a2aac7799d7bc81368ac27b852822a60248301525afa801561023b576102275750f35b8161081291611eaf565b61067157815f61079e565b5034610238576020366003190112610238576004356001600160a01b0381169081900361050d575f5160206137ab5f395f51905f523b1561055c57818080604051602081019063fe575a8760e01b825285602482015260248152610882604482611eaf565b51905f5160206137ab5f395f51905f525afa61089c6122e6565b9015908115610a0e575b505f51602061378b5f395f51905f523b1561050d57604051632631f2b160e11b8152901515600482015281816024815f51602061378b5f395f51905f525afa801561023b576109f9575b5080806040516020810190630723eb0360e51b82528560248201526024815261091a604482611eaf565b51905f5160206137ab5f395f51905f525afa6109346122e6565b90159081156109de575b505f51602061378b5f395f51905f523b1561050d57604051632631f2b160e11b8152901515600482015281816024815f51602061378b5f395f51905f525afa801561023b576109c9575b50506040519063fe575a8760e01b825260048201526020816024815f5160206137ab5f395f51905f525afa801561023b576104c69183916104c95750612315565b816109d391611eaf565b61050d57815f610988565b6109f291506020808251830101910161224e565b155f61093e565b81610a0391611eaf565b61050d57815f6108f0565b610a2291506020808251830101910161224e565b155f6108a6565b50346102385780600319360112610238576020610a446121b3565b6040519015158152f35b5034610238578060031936011261023857601954610a6b81611edf565b91610a796040519384611eaf565b818352601981527f944998273e477b495144fb8794c914197f3ccb46be2900f4698fd0ef743c9695602084015b838310610abb57604051806106f48782611daa565b600160208192604051610ad981610ad28189611f2e565b0382611eaf565b815201920192019190610aa6565b5034610238578060031936011261023857601c54610b0481611edf565b91610b126040519384611eaf565b818352601c81527f0e4562a10381dec21b205ed72637e6b1b523bdd0e4d4d50af5cd23dd4500a211602084015b838310610b5457604051806106f48782611e09565b60026020600192604051610b6781611e80565b848060a01b038654168152610b7d858701611faf565b83820152815201920192019190610b3f565b5034610238578060031936011261023857601d54610bac81611edf565b91610bba6040519384611eaf565b818352601d81527f6d4407e7be21f808e6509aa9fa9143369579dd7d760fe20a2c09680fc146134f602084015b838310610bfc57604051806106f48782611e09565b60026020600192604051610c0f81611e80565b848060a01b038654168152610c25858701611faf565b83820152815201920192019190610be7565b5034610238578060031936011261023857601a54610c5481611edf565b91610c626040519384611eaf565b818352601a81527f057c384a7d1c54f3a1b2e5e67b2617b8224fdfd1ea7234eea573a6ff665ff63e602084015b838310610ca457604051806106f48782611daa565b600160208192604051610cbb81610ad28189611f2e565b815201920192019190610c8f565b5034610238578060031936011261023857601b54610ce681611edf565b610cf36040519182611eaf565b818152601b83526020810191837f3ad8aa4f87544323a9d1e5dd902f40c356527a7955687113db5f9a85ad579dc1845b838310610daf57868587604051928392602084019060208552518091526040840160408260051b8601019392905b828210610d6057505050500390f35b91936001919395506020610d9f8192603f198a820301865288519083610d8f8351604084526040840190611d49565b9201519084818403910152611d6d565b9601920192018594939192610d51565b60026020600192604051610dc281611e80565b604051610dd381610ad2818a611f2e565b8152610de0858701611faf565b83820152815201920192019190610d23565b5034610238576020366003190112610238576004356001600160a01b0381169081900361050d577395ad61b0a150d79219dcf64e1e6cc01f0b64c4ce3b1561055c5781908180604051602081019063fe575a8760e01b825284602482015260248152610e5f604482611eaf565b51907395ad61b0a150d79219dcf64e1e6cc01f0b64c4ce5afa610e806122e6565b9015908115611008575b505f51602061378b5f395f51905f523b1561024657604051632631f2b160e11b8152901515600482015282816024815f51602061378b5f395f51905f525afa9081156102ae578391610ff3575b5080916040516020810191630723eb0360e51b8352602482015260248152610f00604482611eaf565b51907395ad61b0a150d79219dcf64e1e6cc01f0b64c4ce5afa610f216122e6565b9015908115610fd8575b505f51602061378b5f395f51905f523b1561067157604051632631f2b160e11b8152901515600482015281816024815f51602061378b5f395f51905f525afa801561023b57610fc3575b50505f51602061378b5f395f51905f523b1561023857604051630c9fd58160e01b815260016004820152819081816024815f51602061378b5f395f51905f525afa801561023b576102275750f35b81610fcd91611eaf565b61023857805f610f75565b610fec91506020808251830101910161224e565b155f610f2b565b81610ffd91611eaf565b61067157815f610ed7565b61101c91506020808251830101910161224e565b155f610e8a565b503461023857806003193601126102385760405160178054808352908352909160208301917fc624b66cc0138b8fabc209247f72d758e1cf3343756d543badbf24212bed8c15915b818110611082576106f4856106e881870382611eaf565b82546001600160a01b031684526020909301926001928301920161106b565b503461023857806003193601126102385760405160188054808352908352909160208301917fb13d2d76d1f4b7be834882e410b3e3a8afaf69f83600ae24db354391d2378d2e915b818110611100576106f4856106e881870382611eaf565b82546001600160a01b03168452602090930192600192830192016110e9565b5034610238578060031936011261023857601e5461113c81611edf565b6111496040519182611eaf565b818152601e83526020810191837f50bb669a95c7b50b7e8a6f09454034b2b14cf2b85c730dca9a539ca82cb6e350845b83831061124d5786858760405192839260208401906020855251809152604084019160408260051b8601019392815b8383106111b55786860387f35b919395509193603f198782030183528551906020604082019260018060a01b0381511683520151916040602083015282518091526060820190602060608260051b850101940192855b828110611222575050505050602080600192970193019301909286959492936111a8565b9091929394602080611240600193605f198782030189528951611d49565b97019501939291016111fe565b60405161125981611e80565b82546001600160a01b0316815260018301805461127581611edf565b916112836040519384611eaf565b8183528a526020808b20908b9084015b8382106112b9575050505060019282602092836002950152815201920192019190611179565b6001602081926040516112d081610ad2818a611f2e565b815201930191019091611293565b5034611763575f366003190112611763575f51602061378b5f395f51905f523b156117635760405163d9bbf3a160e01b81526301262d6f60048201525f81602481835f51602061378b5f395f51905f525af18015611bf157611bde575b50808060405160208101906370a0823160e01b825230602482015260248152611365604482611eaf565b51905f5160206137ab5f395f51905f525afa506113926113836122e6565b60208082518301019101611ed0565b50601180546001600160a01b0319165f5160206137ab5f395f51905f52179055600f805463ffffffff19166370a08231179055600e54600160401b811015611bca576001810180600e55811015611bb657600e8252602082200130905560018060a01b036011541690600f5460e01b6010549061140d6123c0565b6001600160a01b0385165f908152600d60205260409020909163ffffffff60e01b169081855260205260408420604051602081019061145f8161145188888661238b565b03601f198101835282611eaf565b519020855260205260ff60036040862001541615611ba8575b6001600160a01b0385165f908152600d602052604090209084526020526114516114b1604085209360405192839160208301958661238b565b5190208252602052604081209160018301549060028401546114d3818461236a565b6119e8575b8454604051630667f9d760e41b81526001600160a01b038416600482015260248101829052939091906020856044815f51602061378b5f395f51905f525afa9485156119dd5786956119a9575b506001908201610100031b5f1901811b198416915f51602061378b5f395f51905f523b156119a5576040516370ca10bb60e01b815292869284928392611578926305f5e100901b179087600485016123a2565b0381835f51602061378b5f395f51905f525af1801561025f57908491611990575b505082806020600f5460e01b6115e960246115b4600d61249d565b6040519485918183019563ffffffff60e01b1686528051918291018484015e810186838201520301601f198101845283611eaf565b6011549151916001600160a01b03165afa936116036122e6565b601054600581901b96906001600160fb1b0381160361197c5785968695965085928051602081115f14611971575060209198509695965b87985b828a106118fe57508795949392159291505081156118ef575b5061182357601180546001600160a01b0319169055600f805463ffffffff19169055600e8054908490558390806117e0575b508060105560ff19601354166013556116a2601454611ef6565b8061176f575b506040516370a0823160e01b815230600482015281906020816024815f5160206137ab5f395f51905f525afa90811561023b578291611736575b505f51602061378b5f395f51905f523b15610671576040519063260a5b1560e21b825260048201526305f5e100602482015281816044815f51602061378b5f395f51905f525afa801561023b576102275750f35b9150506020813d602011611767575b8161175260209383611eaf565b8101031261176357819051836116e2565b5f80fd5b3d9150611745565b601f81116001146117865750806014555b816116a8565b60148252601f0160051c5f19017fce6d7b5282bd9a3661ae061feed1dbda4e52ab073b1f9285be6e155d9c38d4ed5f5b8281106117d3575050506014815280602081208160145555611780565b5f828201556001016117b6565b600e82527fbb7b4a454dc3493923482f07822329ed19e8244eff582cc204f8554c3620c3fd825b828110611815575050611688565b600190848184015501611807565b54905f51602061378b5f395f51905f523b156118eb5761185760405194859384936370ca10bb60e01b8552600485016123a2565b0381835f51602061378b5f395f51905f525af1801561023b576118d6575b60405162461bcd60e51b815260206004820152603360248201527f73746453746f726167652066696e642853746453746f72616765293a204661696044820152723632b2103a37903bb934ba32903b30b63ab29760691b6064820152608490fd5b6118e1828092611eaf565b6102385780611875565b8280fd5b6305f5e1009150141586611656565b61190b8a829b969b61236a565b825181101561195d578201602001516001600160f81b031916600386901b86156008888304141715611949576001969096019a951c9094179361163d565b634e487b7160e01b8b52601160045260248bfd5b634e487b7160e01b8a52603260045260248afd5b91985096959661163a565b634e487b7160e01b86526011600452602486fd5b8161199a91611eaf565b6118eb57825f611599565b8580fd5b9094506020813d6020116119d5575b816119c560209383611eaf565b8101031261176357519381611525565b3d91506119b8565b6040513d88823e3d90fd5b6119f2818461236a565b610100036101008111611b945760ff8111611b94576001901b60405163348051d760e11b815281600482015285816024815f51602061378b5f395f51905f525afa9081156119dd578691611b08575b5090611acf606a6020936040519485917f73746453746f726167652066696e642853746453746f72616765293a20506163828401527f6b656420736c6f742e2057652063616e2774206669742076616c756520677265604084015269030ba32b9103a3430b7160b51b60608401528051918291018484015e810189838201520301601f198101845283611eaf565b6305f5e1001015611ae057506114d8565b60405162461bcd60e51b815260206004820152908190611b04906024830190611d49565b0390fd5b90503d8087833e611b198183611eaf565b810190602081830312611b90578051906001600160401b038211611b8c570181601f82011215611b9057805190611b4f826122cb565b92611b5d6040519485611eaf565b82845260208383010111611b8c5760209392888584611acf9582606a96018386015e8301015292935050611a41565b8780fd5b8680fd5b634e487b7160e01b85526011600452602485fd5b611bb06126c7565b50611478565b634e487b7160e01b82526032600452602482fd5b634e487b7160e01b82526041600452602482fd5b611bea91505f90611eaf565b5f5f61133b565b6040513d5f823e3d90fd5b34611763575f36600319011261176357604051601680548083525f91825260208301917fd833147d7dc355ba459fc788f669e58cfaf9dc25ddcd0702e87d69c7b512428991905b818110611c5a576106f4856106e881870382611eaf565b82546001600160a01b0316845260209093019260019283019201611c43565b34611763575f366003190112611763576371ee464d60e01b81526040600482015260076044820152661b585a5b9b995d60ca1b606482015262faaf6460248201526020816084815f5f51602061378b5f395f51905f525af18015611bf157611cdd57005b611cfe9060203d602011611d00575b611cf68183611eaf565b810190611ed0565b005b503d611cec565b60206040818301928281528451809452019201905f5b818110611d2a5750505090565b82516001600160a01b0316845260209384019390920191600101611d1d565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b90602080835192838152019201905f5b818110611d8a5750505090565b82516001600160e01b031916845260209384019390920191600101611d7d565b602081016020825282518091526040820191602060408360051b8301019401925f915b838310611ddc57505050505090565b9091929394602080611dfa600193603f198682030187528951611d49565b97019301930191939290611dcd565b602081016020825282518091526040820191602060408360051b8301019401925f915b838310611e3b57505050505090565b9091929394602080611e71600193603f198682030187526040838b51878060a01b03815116845201519181858201520190611d6d565b97019301930191939290611e2c565b604081019081106001600160401b03821117611e9b57604052565b634e487b7160e01b5f52604160045260245ffd5b90601f801991011681019081106001600160401b03821117611e9b57604052565b90816020910312611763575190565b6001600160401b038111611e9b5760051b60200190565b90600182811c92168015611f24575b6020831014611f1057565b634e487b7160e01b5f52602260045260245ffd5b91607f1691611f05565b5f9291815491611f3d83611ef6565b8083529260018116908115611f925750600114611f5957505050565b5f9081526020812093945091925b838310611f78575060209250010190565b600181602092949394548385870101520191019190611f67565b915050602093945060ff929192191683830152151560051b010190565b90604051918281549182825260208201905f5260205f20925f905b80600783011061210e576120209454918181106120ef575b8181106120d0575b8181106120b1575b818110612092575b818110612073575b818110612054575b818110612037575b10612022575b500383611eaf565b565b6001600160e01b03191681526020015f612018565b602083811b6001600160e01b031916855290930192600101612012565b604083901b6001600160e01b031916845260209093019260010161200a565b606083901b6001600160e01b0319168452602090930192600101612002565b608083901b6001600160e01b0319168452602090930192600101611ffa565b60a083901b6001600160e01b0319168452602090930192600101611ff2565b60c083901b6001600160e01b0319168452602090930192600101611fea565b60e083901b6001600160e01b0319168452602090930192600101611fe2565b916008919350610100600191865463ffffffff60e01b8160e01b16825263ffffffff60e01b8160c01b16602083015263ffffffff60e01b8160a01b16604083015263ffffffff60e01b8160801b16606083015263ffffffff60e01b8160601b16608083015263ffffffff60e01b8160401b1660a083015263ffffffff60e01b8160201b1660c083015263ffffffff60e01b1660e0820152019401920185929391611fca565b60085460ff1680156121c25790565b50604051630667f9d760e41b81525f51602061378b5f395f51905f5260048201526519985a5b195960d21b60248201526020816044815f51602061378b5f395f51905f525afa908115611bf1575f9161221c575b50151590565b90506020813d602011612246575b8161223760209383611eaf565b8101031261176357515f612216565b3d915061222a565b90816020910312611763575180151581036117635790565b60407039903737ba10309031b7b73a3930b1ba1760791b917f53746443686561747320617373756d654e6f74426c61636b6c6973746564286181527f6464726573732c61646472657373293a20546f6b656e2061646472657373206960208201520152565b6001600160401b038111611e9b57601f01601f191660200190565b3d15612310573d906122f7826122cb565b916123056040519384611eaf565b82523d5f602084013e565b606090565b5f51602061378b5f395f51905f523b156117635760405163a598288560e01b815290151560048201525f816024815f51602061378b5f395f51905f525afa8015611bf1576123605750565b5f61202091611eaf565b9190820180921161237757565b634e487b7160e01b5f52601160045260245ffd5b60209291908391805192839101825e019081520190565b604091949392606082019560018060a01b0316825260208201520152565b6123cb601454611ef6565b612488576040519081826020600e549283815201600e5f5260205f20925f5b81811061246f5750506123ff92500383611eaf565b81518060051b90808204602014901517156123775761241d816122cb565b9061242b6040519283611eaf565b80825261243a601f19916122cb565b013660208301375f5b835181101561246a578061245960019286612656565b5160208260051b8501015201612443565b509150565b84548352600194850194879450602090930192016123ea565b60405161249a81610ad2816014611f2e565b90565b60078101906124ac8254611ef6565b61256857600191500190604051808360208295549384815201905f5260205f20925f5b81811061254f5750506124e492500383611eaf565b81518060051b908082046020149015171561237757612502816122cb565b906125106040519283611eaf565b80825261251f601f19916122cb565b013660208301375f5b835181101561246a578061253e60019286612656565b5160208260051b8501015201612528565b84548352600194850194879450602090930192016124cf565b5061249a610ad29160405192838092611f2e565b905f806020600285015460e01b61259760246115b48861249d565b60048601549151916001600160a01b03165afa60036125b46122e6565b930154600581901b906001600160fb1b03811603612377575f938051602081115f1461265057506020905b5f925b8284106125f157505050509190565b909192956125ff878361236a565b835181101561263c57830160200151600388901b91906001600160f81b031916881560088a8504141715612377576001921c1796019291906125e2565b634e487b7160e01b5f52603260045260245ffd5b906125df565b805182101561263c5760209160051b010190565b9080601f8301121561176357815161268181611edf565b9261268f6040519485611eaf565b81845260208085019260051b82010192831161176357602001905b8282106126b75750505090565b81518152602091820191016126aa565b601154600f546010546001600160a01b03909216915f9160e01b6126eb600d61249d565b90845f52600d60205260405f209063ffffffff60e01b1690815f5260205260405f2060405160208101906127248161145188888661238b565b5190205f5260205260ff600360405f20015416612f26575f51602061378b5f395f51905f523b156117635760405163266cf10960e01b81525f81600481835f51602061378b5f395f51905f525af18015611bf157612f11575b50612788600d61257c565b90506040516365bc948160e01b81528660048201528581602481835f51602061378b5f395f51905f525af19081156119dd578691612ead575b5080518061283357608460405162461bcd60e51b815260206004820152604060248201527f73746453746f726167652066696e642853746453746f72616765293a204e6f2060448201527f73746f726167652075736520646574656374656420666f72207461726765742e6064820152fd5b8015612e99579061287f915f190190602061284e8383612656565b51604051630667f9d760e41b81526001600160a01b038c166004820152602481019190915293849081906044820190565b03815f51602061378b5f395f51905f525afa928315612e8e578893612e5b575b508215612e1c575b6128b18282612656565b51601154604051630667f9d760e41b81526001600160a01b03909116600482018190526024820183905291906020816044815f51602061378b5f395f51905f525afa908115612e11578b91612de0575b5061290c600d61257c565b91909382155f14612dd9575f19905b5f51602061378b5f395f51905f523b15612dc057848e9161295060405194859384936370ca10bb60e01b8552600485016123a2565b0381835f51602061378b5f395f51905f525af18015612d3d57908d91612dc4575b505061297d600d61257c565b601154909491506001600160a01b03165f51602061378b5f395f51905f523b15612dc057908d916129c260405194859384936370ca10bb60e01b8552600485016123a2565b0381835f51602061378b5f395f51905f525af18015612db557908c91612d9c575b505082612d91575b505015612d8a578793889360ff60135416612c17575b6001868601610100031b5f1901851b16841c8103612c0e575090612a87917f9c9555b1e3102e3cf48f427d79cb678f5d9bd1ed0ad574389461e255f95170ed60808b89611451612a5c8d60405192839160208301958661238b565b519020612a698686612656565b51906040519283528a602084015260408301526060820152a1612656565b519060405191608083018381106001600160401b03821117612bfa5790600393929160405282526020820193845260408201908152606082019360018552898952600d60205260408920868a52602052604089206040516020810190612af2816114518d8d8661238b565b5190208a526020526040892092518355516001830155516002820155019051151560ff80198354169116179055848452600d60205260408420818552602052604084206040516020810190612b4c8161145188888661238b565b519020855260205260ff60036040862001541615612b9d576040948452600d602052848420908452602052611451612b9185852093865192839160208301958661238b565b51902082526020522090565b60405162461bcd60e51b815260206004820152602f60248201527f73746453746f726167652066696e642853746453746f72616765293a20536c6f60448201526e3a143994903737ba103337bab7321760891b6064820152608490fd5b634e487b7160e01b89526041600452602489fd5b93509150612833565b9450612c629350612c288383612656565b51601154604051630667f9d760e41b81526001600160a01b0390911660048201526024810182905290959094602090869081906044820190565b03815f51602061378b5f395f51905f525afa948515612d7f578a95612d4c575b50612c8e86600d612f67565b959096612c9c81600d613031565b60115490939192906001600160a01b03165f51602061378b5f395f51905f523b15612d4857908e91612ce260405194859384936370ca10bb60e01b8552600485016123a2565b0381835f51602061378b5f395f51905f525af18015612d3d57908d91612d24575b505087612d1c575b509495612a01575093509150612833565b96505f612d0b565b81612d2e91611eaf565b612d39578b5f612d03565b8b80fd5b6040513d8f823e3d90fd5b8e80fd5b9094506020813d8211612d77575b81612d6760209383611eaf565b810103126117635751935f612c82565b3d9150612d5a565b6040513d8c823e3d90fd5b9150612833565b141590505f806129eb565b81612da691611eaf565b612db1578a5f6129e3565b8a80fd5b6040513d8e823e3d90fd5b8d80fd5b81612dce91611eaf565b612d39578b5f612971565b8c9061291b565b90506020813d8211612e09575b81612dfa60209383611eaf565b8101031261176357515f612901565b3d9150612ded565b6040513d8d823e3d90fd5b7f080fc4a96620c4462e705b23f346413fe3796bb63c6f8d8591baec0e231577a56040612e498484612656565b518151908c82526020820152a16128a7565b9092506020813d8211612e86575b81612e7660209383611eaf565b810103126117635751915f61289f565b3d9150612e69565b6040513d8a823e3d90fd5b634e487b7160e01b87526011600452602487fd5b90503d8087833e612ebe8183611eaf565b8101604082820312611b905781516001600160401b038111611b8c5781612ee691840161266a565b916020810151906001600160401b038211612f0d57612f0692910161266a565b505f6127c1565b8880fd5b612f1e9194505f90611eaf565b5f925f61277d565b91939092505f52600d60205260405f20905f52602052611451612f5860405f209360405192839160208301958661238b565b5190205f5260205260405f2090565b91905f5b6101008110612f7e57505090505f905f90565b8060ff0360ff8111612377576004850154600190911b906001600160a01b03165f51602061378b5f395f51905f523b1561176357835f91612fd360405194859384936370ca10bb60e01b8552600485016123a2565b0381835f51602061378b5f395f51905f525af18015611bf157613021575b50612ffb8461257c565b81613017575b5061300e57600101612f6b565b92505060019190565b905015155f613001565b5f61302b91611eaf565b5f612ff1565b91905f5b610100811061304857505090505f905f90565b60048401546001821b906001600160a01b03165f51602061378b5f395f51905f523b1561176357835f9161309060405194859384936370ca10bb60e01b8552600485016123a2565b0381835f51602061378b5f395f51905f525af18015611bf1576130d5575b506130b88461257c565b816130cb575b5061300e57600101613035565b905015155f6130be565b5f6130df91611eaf565b5f6130ae56fe6080806040523460155761068b908161001a8239f35b5f80fdfe60806040526004361015610011575f80fd5b5f5f3560e01c806317cc73a01461030a57806395b9a383146100ca5763de4a5dcd1461003b575f80fd5b346100b95760203660031901126100b9578061005d61005861038f565b610432565b5f5160206106365f395f51905f523b156100c757604051632631f2b160e11b8152901515600482015281816024815f5160206106365f395f51905f525afa80156100bc576100a85750f35b816100b2916103a5565b6100b95780f35b80fd5b6040513d84823e3d90fd5b50fd5b50346100b95760403660031901126100b9576100e461038f565b6024356001600160a01b038116919082900361030657803b156102815782918280604051602081019063fe575a8760e01b82528460248201526024815261012c6044826103a5565b5190855afa9161013a6103db565b9215928315610264575b505f5160206106365f395f51905f523b1561025f57604051632631f2b160e11b8152921515600484015283836024815f5160206106365f395f51905f525afa918215610254578492610237575b8293506040516020810191630723eb0360e51b83526024820152602481526101ba6044826103a5565b51915afa6101c66103db565b901590811561021c575b505f5160206106365f395f51905f523b156100c757604051632631f2b160e11b8152901515600482015281816024815f5160206106365f395f51905f525afa80156100bc576100a85750f35b61023091506020808251830101910161041a565b155f6101d0565b91909281610244916103a5565b61025057818391610191565b5050fd5b6040513d86823e3d90fd5b505050fd5b6102799193506020808251830101910161041a565b15915f610144565b60405162461bcd60e51b815260206004820152605160248201527f53746443686561747320617373756d654e6f74426c61636b6c6973746564286160448201527f6464726573732c61646472657373293a20546f6b656e2061646472657373206960648201527039903737ba10309031b7b73a3930b1ba1760791b608482015260a490fd5b8280fd5b503461038b57602036600319011261038b5761032761005861038f565b155f5160206106365f395f51905f523b1561038b5760405190632631f2b160e11b825260048201525f816024815f5160206106365f395f51905f525afa801561038057610372575080f35b61037e91505f906103a5565b005b6040513d5f823e3d90fd5b5f80fd5b600435906001600160a01b038216820361038b57565b90601f8019910116810190811067ffffffffffffffff8211176103c757604052565b634e487b7160e01b5f52604160045260245ffd5b3d15610415573d9067ffffffffffffffff82116103c7576040519161040a601f8201601f1916602001846103a5565b82523d5f602084013e565b606090565b9081602091031261038b5751801515810361038b5790565b5f19813110156105a457479080315f5160206106365f395f51905f523b1561038b5760405163c88a5e6d60e01b8152306004820152600160248201525f92908381604481835f5160206106365f395f51905f525af180156103805761058f575b508280808060016001600160a01b0386165af1936104ae6103db565b505f5160206106365f395f51905f523b1561058b5760405163c88a5e6d60e01b815230600482015260248101919091528381604481835f5160206106365f395f51905f525af1801561025457908491610576575b50505f5160206106365f395f51905f523b156103065760405163c88a5e6d60e01b81526001600160a01b0391909116600482015260248101919091528181604481835f5160206106365f395f51905f525af180156100bc5761056357505090565b61056e8280926103a5565b6100b9575090565b81610580916103a5565b61030657825f610502565b8380fd5b61059c9193505f906103a5565b5f915f610492565b60405162461bcd60e51b815260206004820152605e60248201527f537464436865617473205f697350617961626c652861646472657373293a204260448201527f616c616e636520657175616c73206d61782075696e743235362c20736f20697460648201527f2063616e6e6f74207265636569766520616e79206d6f72652066756e64730000608482015260a490fdfe0000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12da26469706673582212202286ba7b490a6ed2e21d62dd805d42d34d93a83baf9cb48a48a393a8d131e33064736f6c634300082100330000000000000000000000007109709ecfa91a80626ff3989d68f67f5b1dd12d000000000000000000000000a0b86991c6218b36c1d19d4a2e9eb0ce3606eb48a2646970667358221220fd5b51076ebf911b1298d2c84b6d63a43e498e544c67572cd1956c00290c3aa964736f6c63430008210033"

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
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#468)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#468)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#468)
        """
        ...

    @overload
    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#468)
        """
        ...

    def setUp(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#468)
        """
        return self._execute(self.chain, request_type, "0a9254e4", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_RevertIf_CannotAssumeNoBlacklisted_EOA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#473)
        """
        ...

    @overload
    def test_RevertIf_CannotAssumeNoBlacklisted_EOA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#473)
        """
        ...

    @overload
    def test_RevertIf_CannotAssumeNoBlacklisted_EOA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#473)
        """
        ...

    @overload
    def test_RevertIf_CannotAssumeNoBlacklisted_EOA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#473)
        """
        ...

    def test_RevertIf_CannotAssumeNoBlacklisted_EOA(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#473)
        """
        return self._execute(self.chain, request_type, "fd2e188f", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_AssumeNotBlacklisted_TokenWithoutBlacklist(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#481)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotBlacklisted_TokenWithoutBlacklist(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#481)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotBlacklisted_TokenWithoutBlacklist(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#481)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotBlacklisted_TokenWithoutBlacklist(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#481)

        Args:
            addr: address
        """
        ...

    def testFuzz_AssumeNotBlacklisted_TokenWithoutBlacklist(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#481)

        Args:
            addr: address
        """
        return self._execute(self.chain, request_type, "572e6b91", [addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_RevertIf_AssumeNoBlacklisted_USDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#486)
        """
        ...

    @overload
    def test_RevertIf_AssumeNoBlacklisted_USDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#486)
        """
        ...

    @overload
    def test_RevertIf_AssumeNoBlacklisted_USDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#486)
        """
        ...

    @overload
    def test_RevertIf_AssumeNoBlacklisted_USDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#486)
        """
        ...

    def test_RevertIf_AssumeNoBlacklisted_USDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#486)
        """
        return self._execute(self.chain, request_type, "ed63e24a", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_AssumeNotBlacklisted_USDC(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#493)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotBlacklisted_USDC(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#493)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotBlacklisted_USDC(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#493)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotBlacklisted_USDC(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#493)

        Args:
            addr: address
        """
        ...

    def testFuzz_AssumeNotBlacklisted_USDC(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#493)

        Args:
            addr: address
        """
        return self._execute(self.chain, request_type, "c879dfd7", [addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_RevertIf_AssumeNoBlacklisted_USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#498)
        """
        ...

    @overload
    def test_RevertIf_AssumeNoBlacklisted_USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#498)
        """
        ...

    @overload
    def test_RevertIf_AssumeNoBlacklisted_USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#498)
        """
        ...

    @overload
    def test_RevertIf_AssumeNoBlacklisted_USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#498)
        """
        ...

    def test_RevertIf_AssumeNoBlacklisted_USDT(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#498)
        """
        return self._execute(self.chain, request_type, "dad857aa", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def testFuzz_AssumeNotBlacklisted_USDT(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#505)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotBlacklisted_USDT(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#505)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotBlacklisted_USDT(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#505)

        Args:
            addr: address
        """
        ...

    @overload
    def testFuzz_AssumeNotBlacklisted_USDT(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#505)

        Args:
            addr: address
        """
        ...

    def testFuzz_AssumeNotBlacklisted_USDT(self, addr: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#505)

        Args:
            addr: address
        """
        return self._execute(self.chain, request_type, "f64b9dc8", [addr], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def test_dealUSDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#510)
        """
        ...

    @overload
    def test_dealUSDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#510)
        """
        ...

    @overload
    def test_dealUSDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#510)
        """
        ...

    @overload
    def test_dealUSDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#510)
        """
        ...

    def test_dealUSDC(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#510)
        """
        return self._execute(self.chain, request_type, "2a14a6aa", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

StdCheatsForkTest.setUp.selector = bytes4(b'\n\x92T\xe4')
StdCheatsForkTest.test_RevertIf_CannotAssumeNoBlacklisted_EOA.selector = bytes4(b'\xfd.\x18\x8f')
StdCheatsForkTest.testFuzz_AssumeNotBlacklisted_TokenWithoutBlacklist.selector = bytes4(b'W.k\x91')
StdCheatsForkTest.test_RevertIf_AssumeNoBlacklisted_USDC.selector = bytes4(b'\xedc\xe2J')
StdCheatsForkTest.testFuzz_AssumeNotBlacklisted_USDC.selector = bytes4(b'\xc8y\xdf\xd7')
StdCheatsForkTest.test_RevertIf_AssumeNoBlacklisted_USDT.selector = bytes4(b'\xda\xd8W\xaa')
StdCheatsForkTest.testFuzz_AssumeNotBlacklisted_USDT.selector = bytes4(b'\xf6K\x9d\xc8')
StdCheatsForkTest.test_dealUSDC.selector = bytes4(b'*\x14\xa6\xaa')
class Bar(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#520)
    """
    _abi = {'constructor': {'inputs': [], 'stateMutability': 'payable', 'type': 'constructor'}, b'p\xa0\x821': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'dn\xa5m': {'inputs': [{'internalType': 'address', 'name': 'expectedSender', 'type': 'address'}], 'name': 'bar', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, b'UYdw': {'inputs': [{'internalType': 'address', 'name': 'expectedSender', 'type': 'address'}], 'name': 'origin', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, b'\xa9\xb2\xe2\x8a': {'inputs': [{'internalType': 'address', 'name': 'expectedSender', 'type': 'address'}, {'internalType': 'address', 'name': 'expectedOrigin', 'type': 'address'}], 'name': 'origin', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, b'\x18\x16\r\xdd': {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":41355,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:Bar","label":"balanceOf","offset":0,"slot":0,"type":"t_mapping(t_address,t_uint256)"},{"astId":41357,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:Bar","label":"totalSupply","offset":0,"slot":1,"type":"t_uint256"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_mapping(t_address,t_uint256)":{"encoding":"mapping","label":"mapping(address => uint256)","numberOfBytes":32,"key":"t_address","value":"t_uint256"},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60808060405269021e19e0c9bab2400000600155305f525f60205269021e19e0c9bab240000060405f20556101c590816100378239f3fe6080806040526004361015610012575f80fd5b5f3560e01c90816318160ddd1461012a5750806355596477146100ff578063646ea56d146100d857806370a08231146100a15763a9b2e28a14610053575f80fd5b604036600319011261009d57610067610144565b6024356001600160a01b0381169081900361009d5761009b91610094906001600160a01b0316331461015a565b321461015a565b005b5f80fd5b3461009d57602036600319011261009d576001600160a01b036100c2610144565b165f525f602052602060405f2054604051908152f35b602036600319011261009d5761009b6001600160a01b036100f7610144565b16331461015a565b602036600319011261009d5761009b6001600160a01b0361011e610144565b1661009481331461015a565b3461009d575f36600319011261009d576020906001548152f35b600435906001600160a01b038216820361009d57565b1561016157565b60405162461bcd60e51b8152602060048201526006602482015265217072616e6b60d01b6044820152606490fdfea2646970667358221220affb8f4fbb2b160005623b992a1e0a18587f4ec495909425624e93cfee9fa67d64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#521)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Bar:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#521)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#521)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#521)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Bar]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#521)
        """
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, Bar, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[Bar]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#521)
        """
        return cls._deploy(request_type, [], return_tx, Bar, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def balanceOf(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#543)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def balanceOf(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#543)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def balanceOf(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#543)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    @overload
    def balanceOf(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#543)

        Args:
            key0: address
        Returns:
            uint256
        """
        ...

    def balanceOf(self, key0: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#543)

        Args:
            key0: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "70a08231", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#544)

        Returns:
            totalSupply: uint256
        """
        ...

    @overload
    def totalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#544)

        Returns:
            totalSupply: uint256
        """
        ...

    @overload
    def totalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#544)

        Returns:
            totalSupply: uint256
        """
        ...

    @overload
    def totalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#544)

        Returns:
            totalSupply: uint256
        """
        ...

    def totalSupply(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#544)

        Returns:
            totalSupply: uint256
        """
        return self._execute(self.chain, request_type, "18160ddd", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def bar(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#528)

        Args:
            expectedSender: address
        """
        ...

    @overload
    def bar(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#528)

        Args:
            expectedSender: address
        """
        ...

    @overload
    def bar(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#528)

        Args:
            expectedSender: address
        """
        ...

    @overload
    def bar(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#528)

        Args:
            expectedSender: address
        """
        ...

    def bar(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#528)

        Args:
            expectedSender: address
        """
        return self._execute(self.chain, request_type, "646ea56d", [expectedSender], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def origin(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#532)

        Args:
            expectedSender: address
        """
        ...

    @overload
    def origin(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#532)

        Args:
            expectedSender: address
        """
        ...

    @overload
    def origin(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#532)

        Args:
            expectedSender: address
        """
        ...

    @overload
    def origin(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#532)

        Args:
            expectedSender: address
        """
        ...

    def origin(self, expectedSender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#532)

        Args:
            expectedSender: address
        """
        return self._execute(self.chain, request_type, "55596477", [expectedSender], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def origin_(self, expectedSender: Union[Account, Address], expectedOrigin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#537)

        Args:
            expectedSender: address
            expectedOrigin: address
        """
        ...

    @overload
    def origin_(self, expectedSender: Union[Account, Address], expectedOrigin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#537)

        Args:
            expectedSender: address
            expectedOrigin: address
        """
        ...

    @overload
    def origin_(self, expectedSender: Union[Account, Address], expectedOrigin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#537)

        Args:
            expectedSender: address
            expectedOrigin: address
        """
        ...

    @overload
    def origin_(self, expectedSender: Union[Account, Address], expectedOrigin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#537)

        Args:
            expectedSender: address
            expectedOrigin: address
        """
        ...

    def origin_(self, expectedSender: Union[Account, Address], expectedOrigin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#537)

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
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#547)
    """
    _abi = {'constructor': {'inputs': [], 'stateMutability': 'payable', 'type': 'constructor'}, b'\x00\xfd\xd5\x8e': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbd\x85\xb09': {'inputs': [{'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":41416,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:BarERC1155","label":"_balances","offset":0,"slot":0,"type":"t_mapping(t_uint256,t_mapping(t_address,t_uint256))"},{"astId":41420,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:BarERC1155","label":"_totalSupply","offset":0,"slot":1,"type":"t_mapping(t_uint256,t_uint256)"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_mapping(t_address,t_uint256)":{"encoding":"mapping","label":"mapping(address => uint256)","numberOfBytes":32,"key":"t_address","value":"t_uint256"},"t_mapping(t_uint256,t_mapping(t_address,t_uint256))":{"encoding":"mapping","label":"mapping(uint256 => mapping(address => uint256))","numberOfBytes":32,"key":"t_uint256","value":"t_mapping(t_address,t_uint256)"},"t_mapping(t_uint256,t_uint256)":{"encoding":"mapping","label":"mapping(uint256 => uint256)","numberOfBytes":32,"key":"t_uint256","value":"t_uint256"},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "6080604081815269021e19e0c9bab24000007fa6eef7e35abe7026729641147f7915573c7e97b47efa546f5f6e3230263bcb49819055305f9081527fad3228b676f7d3cd4284a5443f17f1962b36e491b30a40b2405849e597ba5fb5602052919091205560d1908161006f8239f3fe60808060405260043610156011575f80fd5b5f3560e01c908162fdd58e14605a575063bd85b03914602e575f80fd5b3460565760203660031901126056576004355f526001602052602060405f2054604051908152f35b5f80fd5b3460565760403660031901126056576004356001600160a01b03811691908290036056576020916024355f525f835260405f20905f52825260405f20548152f3fea2646970667358221220b651e70a21708bba240ce38abbfa6134f514ef28cd4f59a0015ad0a80ea9d7ac64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#548)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> BarERC1155:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#548)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#548)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#548)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[BarERC1155]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#548)
        """
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, BarERC1155, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[BarERC1155]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#548)
        """
        return cls._deploy(request_type, [], return_tx, BarERC1155, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def balanceOf(self, account: Union[Account, Address], id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#554)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#554)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#554)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#554)

        Args:
            account: address
            id: uint256
        Returns:
            uint256
        """
        ...

    def balanceOf(self, account: Union[Account, Address], id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#554)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#558)

        Args:
            id: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def totalSupply(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#558)

        Args:
            id: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def totalSupply(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#558)

        Args:
            id: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def totalSupply(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#558)

        Args:
            id: uint256
        Returns:
            uint256
        """
        ...

    def totalSupply(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#558)

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
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#567)
    """
    _abi = {'constructor': {'inputs': [], 'stateMutability': 'payable', 'type': 'constructor'}, b'p\xa0\x821': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'cR!\x1e': {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}], 'name': 'ownerOf', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":41502,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:BarERC721","label":"_owners","offset":0,"slot":0,"type":"t_mapping(t_uint256,t_address)"},{"astId":41506,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:BarERC721","label":"_balances","offset":0,"slot":1,"type":"t_mapping(t_address,t_uint256)"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_mapping(t_address,t_uint256)":{"encoding":"mapping","label":"mapping(address => uint256)","numberOfBytes":32,"key":"t_address","value":"t_uint256"},"t_mapping(t_uint256,t_address)":{"encoding":"mapping","label":"mapping(uint256 => address)","numberOfBytes":32,"key":"t_uint256","value":"t_address"},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "608060408181527fada5013122d395ba3c54772283fb069b10426056ef8ca54750cb9bb552a59e7d805460016001600160a01b031991821681179092557fcc69885fda6bcc1a4ace058b4a62bf5e179ea78fd58a1ccd71c22cc9b688792f8290557fabbb5caa7dda850e60932de0934eb1f9d0f59695050f761dc64e443e5030a56980543090831681179091557f101e368776582e57ab3d116ffe2517c0a585cd5b23174b01e275c2d8329c3d83805490921681179091555f908152602091909152206002905560d190816100d28239f3fe60808060405260043610156011575f80fd5b5f3560e01c9081636352211e14606c57506370a0823114602f575f80fd5b3460685760203660031901126068576004356001600160a01b038116908190036068575f526001602052602060405f2054604051908152f35b5f80fd5b3460685760203660031901126068576004355f90815260208181526040909120546001600160a01b0316825290f3fea2646970667358221220a0864b3879de6022a5f20540cf998ab8986a8bc06a6843df5278bd94e197d52664736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#568)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> BarERC721:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#568)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#568)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#568)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[BarERC721]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#568)
        """
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, BarERC721, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[BarERC721]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#568)
        """
        return cls._deploy(request_type, [], return_tx, BarERC721, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def balanceOf(self, owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#577)

        Args:
            owner: address
        Returns:
            uint256
        """
        ...

    @overload
    def balanceOf(self, owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#577)

        Args:
            owner: address
        Returns:
            uint256
        """
        ...

    @overload
    def balanceOf(self, owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#577)

        Args:
            owner: address
        Returns:
            uint256
        """
        ...

    @overload
    def balanceOf(self, owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#577)

        Args:
            owner: address
        Returns:
            uint256
        """
        ...

    def balanceOf(self, owner: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#577)

        Args:
            owner: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "70a08231", [owner], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def ownerOf(self, tokenId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#581)

        Args:
            tokenId: uint256
        Returns:
            address
        """
        ...

    @overload
    def ownerOf(self, tokenId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#581)

        Args:
            tokenId: uint256
        Returns:
            address
        """
        ...

    @overload
    def ownerOf(self, tokenId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#581)

        Args:
            tokenId: uint256
        Returns:
            address
        """
        ...

    @overload
    def ownerOf(self, tokenId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#581)

        Args:
            tokenId: uint256
        Returns:
            address
        """
        ...

    def ownerOf(self, tokenId: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#581)

        Args:
            tokenId: uint256
        Returns:
            address
        """
        return self._execute(self.chain, request_type, "6352211e", [tokenId], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

BarERC721.balanceOf.selector = bytes4(b'p\xa0\x821')
BarERC721.ownerOf.selector = bytes4(b'cR!\x1e')
class USDCLike(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#590)
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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#591)

        Args:
            arg1: address
        Returns:
            bool
        """
        ...

    @overload
    def isBlacklisted(self, arg1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#591)

        Args:
            arg1: address
        Returns:
            bool
        """
        ...

    @overload
    def isBlacklisted(self, arg1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#591)

        Args:
            arg1: address
        Returns:
            bool
        """
        ...

    @overload
    def isBlacklisted(self, arg1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#591)

        Args:
            arg1: address
        Returns:
            bool
        """
        ...

    def isBlacklisted(self, arg1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#591)

        Args:
            arg1: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "fe575a87", [arg1], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

USDCLike.isBlacklisted.selector = bytes4(b'\xfeWZ\x87')
class USDTLike(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#594)
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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#595)

        Args:
            arg1: address
        Returns:
            bool
        """
        ...

    @overload
    def isBlackListed(self, arg1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#595)

        Args:
            arg1: address
        Returns:
            bool
        """
        ...

    @overload
    def isBlackListed(self, arg1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#595)

        Args:
            arg1: address
        Returns:
            bool
        """
        ...

    @overload
    def isBlackListed(self, arg1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#595)

        Args:
            arg1: address
        Returns:
            bool
        """
        ...

    def isBlackListed(self, arg1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#595)

        Args:
            arg1: address
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "e47d6060", [arg1], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

USDTLike.isBlackListed.selector = bytes4(b'\xe4}``')
class RevertingContract(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#598)
    """
    _abi = {'constructor': {'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}}
    _storage_layout = {"storage":[]}
    _creation_code = "5f80fdfe"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#599)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> RevertingContract:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#599)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#599)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#599)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[RevertingContract]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#599)
        """
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, RevertingContract, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[RevertingContract]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#599)
        """
        return cls._deploy(request_type, [], return_tx, RevertingContract, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

class MockContractWithConstructorArgs(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#604)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'uint256', 'name': '_x', 'type': 'uint256'}, {'internalType': 'bool', 'name': '_y', 'type': 'bool'}, {'internalType': 'bytes20', 'name': '_z', 'type': 'bytes20'}], 'stateMutability': 'payable', 'type': 'constructor'}, b'\x0cUi\x9c': {'inputs': [], 'name': 'x', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa5m\xfeJ': {'inputs': [], 'name': 'y', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc5\xd7\x80.': {'inputs': [], 'name': 'z', 'outputs': [{'internalType': 'bytes20', 'name': '', 'type': 'bytes20'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":41535,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:MockContractWithConstructorArgs","label":"y","offset":0,"slot":0,"type":"t_bool"},{"astId":41537,"contract":"lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol:MockContractWithConstructorArgs","label":"z","offset":1,"slot":0,"type":"t_bytes20"}],"types":{"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes20":{"encoding":"inplace","label":"bytes20","numberOfBytes":20}}}
    _creation_code = "60a0601f6101ad38819003918201601f19168301916001600160401b0383118484101760a45780849260609460405283398101031260a057805160208201519182151580930360a05760400151906001600160601b03198216820360a0576080525f80546001600160a81b03191660ff939093169290921760589190911c610100600160a81b031617905560405160f490816100b9823960805181609b0152f35b5f80fd5b634e487b7160e01b5f52604160045260245ffdfe60808060405260043610156011575f80fd5b5f3560e01c9081630c55699c14608857508063a56dfe4a1460695763c5d7802e146039575f80fd5b346065575f36600319011260655760206bffffffffffffffffffffffff195f5460581b16604051908152f35b5f80fd5b346065575f366003190112606557602060ff5f54166040519015158152f35b346065575f3660031901126065576020907f00000000000000000000000000000000000000000000000000000000000000008152f3fea26469706673582212203b528f4195c05a4459257fedcd2219f8a612be68bbfe565c9705536aec58e39164736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, _x: uint256, _y: bool, _z: bytes20, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#609)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#609)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#609)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#609)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#609)

        Args:
            _x: uint256
            _y: bool
            _z: bytes20
        """
        ...

    @classmethod
    def deploy(cls, _x: uint256, _y: bool, _z: bytes20, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, MockContractWithConstructorArgs, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[MockContractWithConstructorArgs]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#609)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#605)

        Returns:
            x: uint256
        """
        ...

    @overload
    def x(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#605)

        Returns:
            x: uint256
        """
        ...

    @overload
    def x(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#605)

        Returns:
            x: uint256
        """
        ...

    @overload
    def x(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#605)

        Returns:
            x: uint256
        """
        ...

    def x(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#605)

        Returns:
            x: uint256
        """
        return self._execute(self.chain, request_type, "0c55699c", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def y(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#606)

        Returns:
            y: bool
        """
        ...

    @overload
    def y(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#606)

        Returns:
            y: bool
        """
        ...

    @overload
    def y(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#606)

        Returns:
            y: bool
        """
        ...

    @overload
    def y(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#606)

        Returns:
            y: bool
        """
        ...

    def y(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#606)

        Returns:
            y: bool
        """
        return self._execute(self.chain, request_type, "a56dfe4a", [], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def z(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes20:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#607)

        Returns:
            z: bytes20
        """
        ...

    @overload
    def z(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#607)

        Returns:
            z: bytes20
        """
        ...

    @overload
    def z(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#607)

        Returns:
            z: bytes20
        """
        ...

    @overload
    def z(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes20]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#607)

        Returns:
            z: bytes20
        """
        ...

    def z(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes20, TransactionAbc[bytes20], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#607)

        Returns:
            z: bytes20
        """
        return self._execute(self.chain, request_type, "c5d7802e", [], True if request_type == "tx" else False, bytes20, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

MockContractWithConstructorArgs.x.selector = bytes4(b'\x0cUi\x9c')
MockContractWithConstructorArgs.y.selector = bytes4(b'\xa5m\xfeJ')
MockContractWithConstructorArgs.z.selector = bytes4(b'\xc5\xd7\x80.')
class MockContractPayable(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/lib/forge-std/test/StdCheats.t.sol#616)
    """
    _abi = {'receive': {'stateMutability': 'payable', 'type': 'receive'}}
    _storage_layout = {"storage":[]}
    _creation_code = "608080604052346013576040908160188239f35b5f80fdfe36156008575f80fd5b00fea26469706673582212200d1a601e552da1591def0754c7f68b0886f1b9e8f0d55f77c7dece0deda0ad6764736f6c63430008210033"

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

