
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class StdAssertions(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#7)
    """
    _abi = {b'A0O\xac\xd92=u\xb1\x1b\xcd\xd6\t\xcb8\xef\xff\xfd\xb0W\x10\xf7\xca\xf0\xe9\xb1lm\x9dp\x9fP': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log', 'type': 'event'}, b'z\xe7LRt\x14\xae\x13_\xd9pG\xb1)!\xa5\xec9\x11\xb8\x04\x19xU\xd6~%\xc7\xb7^\xe6\xf3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'log_address', 'type': 'event'}, b'\xfb\x10(e\xd5\n\xdd\xdd\xf6\x9d\xa9\xb5\xaa\x1b\xce\xd6l\x80\xcf\x86\x9a\\\x8d\x04q\xa4g\xe1\x8c\xe9\xca\xb1': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_array', 'type': 'event'}, b'\x89\n\x82g\x9bG\x0f+\xd8(\x16\xed\x9b\x16\x1f\x97\xd8\xb9g\xf3\x7f\xa3d|!\xd5\xbf9t\x9e-\xd5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_array', 'type': 'event'}, b'@\xe1\x84\x0fWi\x07=a\xbd\x017-\x9bu\xba\xa9\x84-V)\xa0\xc9\x9f\xf1\x03\xbe\x11x\xa8\xe9\xe2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_array', 'type': 'event'}, b'#\xb6*\xd0XM$\xa7_\x0b\xf3V\x03\x91\xefVY\xecm\xb1&\x9cV\xe1\x1a\xa2A\xd67\xf1\x9b ': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'log_bytes', 'type': 'event'}, b'\xe8\x16\x99\xb8Q\x13\xee\xa1\xc7>\x10X\x8b+\x03^U\x893ic!s\xaf\xd4?\xeb\x19/\xacd\xe3': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'log_bytes32', 'type': 'event'}, b'\x0e\xb5\xd5&$\xc8\xd2\x8a\xda\x9f\xc5Z\x8cP.\xd5\xaa?\xbe/\xb6\xe9\x1bq\xb5\xf3v\x88+\x1d/\xb8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256', 'name': '', 'type': 'int256'}], 'name': 'log_int', 'type': 'event'}, b'\x9cN\x85A\xca\x8f\r\xc1\xc4\x13\xf9\x10\x8ff\xd8-<\xec\xb1\xbd\xdb\xceCza\xca\xa3\x17\\L\xc9o': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address', 'name': 'val', 'type': 'address'}], 'name': 'log_named_address', 'type': 'event'}, b'\x00\xaa\xa3\x9c\x9f\xfb_VzE48\x0cspup.\x1f\x7f\x14\x10\x7f\xc9S(\xe3\xb5l\x03%\xfb': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xa7>\xda\tf/F\xdd\xe7)\xbeF\x118_\xf3O\xe6\xc4O\xbb\xc6\xf7\xe1{\x04+Y\xa3D[W': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_named_array', 'type': 'event'}, b";\xcf\xb2\xae.\x8d\x13-\xd1\xfc\xe7\xcf'\x8a\x9a\x19uj\x9f\xce\xab\xe4p\xdf;\xda\xbbK\xc5w\xd1\xbd": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_named_array', 'type': 'event'}, b'\xd2n\x16\xca\xd4T\x87\x05\xe4\xc9\xe2\xd9O\x98\xee\x91\xc2\x89\x08^\xe4%YO\xd5c_\xa2\x96L\xcf\x18': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'val', 'type': 'bytes'}], 'name': 'log_named_bytes', 'type': 'event'}, b'\xaf\xb7\x95\xc9\xc6\x1eO\xe7F\x8c8o\x92]zT)\xec\xad\x9c\x04\x95\xdd\xb8\xd3\x8di\x06\x14\xd3/\x99': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'val', 'type': 'bytes32'}], 'name': 'log_named_bytes32', 'type': 'event'}, b']\xa6\xce\x9dQ\x15\x1b\xa1\x0c\t\xa5Y\xef$\xd5 \xb9\xda\xc5\xc5\xb8\x81\n\xe8CNM\r\x86A\x1a\x95': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_int', 'type': 'event'}, b"\xeb\x8b\xa4<\xedu7B\x19F\xbdC\xe8(\xb8\xb2\xb8B\x89'\xaa\x8f\x80\x1c\x13\xd94\xbf\x11\xac\xa5{": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_uint', 'type': 'event'}, b'/\xe62w\x91t7CxD*\x8e\x97\x8b\xcc\xfb\xdc\xc1\xd6\xb2\xb0\xd8\x1f~\x8e\xb7v\xab"\x86\xf1h': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}], 'name': 'log_named_int', 'type': 'event'}, b'(\x0fDF\xb2\x8a\x13rA}\xdae\x8d0\xb9[)\x92\xb1*\xc9\xc7\xf3xS_)\xa9z\xcf5\x83': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'val', 'type': 'string'}], 'name': 'log_named_string', 'type': 'event'}, b'\xb2\xde/\xbe\x80\x1a\r\xf6\xc0\xcb\xdd\xfdD\x8b\xa3\xc4\x1dH\xa0@\xca5\xc5l\x81\x96\xef\x0f\xca\xe7!\xa8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}], 'name': 'log_named_uint', 'type': 'event'}, b'\x0b.\x13\xff \xac{GA\x98eU\x83\xed\xf7\r\xed\xd2\xc1\xdc\x98\x0e2\x9cO\xbb/\xc0t\x8byk': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log_string', 'type': 'event'}, b',\xab\x97\x90Q\x0f\xd8\xbd\xfb\xd2\x11R\x88\xdb3\xfe\xc6f\x91\xd4v\xef\xc5B|\xfdL\ti0\x17U': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'log_uint', 'type': 'event'}, b"\xe7\x95\x0e\xde\x03\x94\xb9\xf2\xceJZ\x1b\xf5\xa7\xe1\x85$\x11\xf7\xe6f\x1bC\x08\xc9\x13\xc4\xbf\xd1\x10'\xe4": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'logs', 'type': 'event'}, b'\xbaAO\xa6': {'inputs': [], 'name': 'failed', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":209,"contract":"lib/forge-std/src/StdAssertions.sol:StdAssertions","label":"_failed","offset":0,"slot":0,"type":"t_bool"}],"types":{"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1}}}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> StdAssertions:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[StdAssertions]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, StdAssertions, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[StdAssertions]]:
        raise Exception("Cannot deploy abstract contract")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an abstract contract")

    @dataclasses.dataclass
    class log:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#10)

        Attributes:
            param1 (str): string
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log'
        selector = bytes32(b'A0O\xac\xd92=u\xb1\x1b\xcd\xd6\t\xcb8\xef\xff\xfd\xb0W\x10\xf7\xca\xf0\xe9\xb1lm\x9dp\x9fP')

        param1: str = dataclasses.field(metadata={"original_name": ""})


    @dataclasses.dataclass
    class logs:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#11)

        Attributes:
            param1 (bytearray): bytes
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'logs', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'logs'
        selector = bytes32(b"\xe7\x95\x0e\xde\x03\x94\xb9\xf2\xceJZ\x1b\xf5\xa7\xe1\x85$\x11\xf7\xe6f\x1bC\x08\xc9\x13\xc4\xbf\xd1\x10'\xe4")

        param1: bytearray = dataclasses.field(metadata={"original_name": ""})


    @dataclasses.dataclass
    class log_address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#13)

        Attributes:
            param1 (Address): address
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'log_address', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_address'
        selector = bytes32(b'z\xe7LRt\x14\xae\x13_\xd9pG\xb1)!\xa5\xec9\x11\xb8\x04\x19xU\xd6~%\xc7\xb7^\xe6\xf3')

        param1: Address = dataclasses.field(metadata={"original_name": ""})


    @dataclasses.dataclass
    class log_bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#14)

        Attributes:
            param1 (bytes32): bytes32
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'log_bytes32', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_bytes32'
        selector = bytes32(b'\xe8\x16\x99\xb8Q\x13\xee\xa1\xc7>\x10X\x8b+\x03^U\x893ic!s\xaf\xd4?\xeb\x19/\xacd\xe3')

        param1: bytes32 = dataclasses.field(metadata={"original_name": ""})


    @dataclasses.dataclass
    class log_int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#15)

        Attributes:
            param1 (int256): int256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256', 'name': '', 'type': 'int256'}], 'name': 'log_int', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_int'
        selector = bytes32(b'\x0e\xb5\xd5&$\xc8\xd2\x8a\xda\x9f\xc5Z\x8cP.\xd5\xaa?\xbe/\xb6\xe9\x1bq\xb5\xf3v\x88+\x1d/\xb8')

        param1: int256 = dataclasses.field(metadata={"original_name": ""})


    @dataclasses.dataclass
    class log_uint:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#16)

        Attributes:
            param1 (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'log_uint', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_uint'
        selector = bytes32(b',\xab\x97\x90Q\x0f\xd8\xbd\xfb\xd2\x11R\x88\xdb3\xfe\xc6f\x91\xd4v\xef\xc5B|\xfdL\ti0\x17U')

        param1: uint256 = dataclasses.field(metadata={"original_name": ""})


    @dataclasses.dataclass
    class log_bytes:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#17)

        Attributes:
            param1 (bytearray): bytes
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'log_bytes', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_bytes'
        selector = bytes32(b'#\xb6*\xd0XM$\xa7_\x0b\xf3V\x03\x91\xefVY\xecm\xb1&\x9cV\xe1\x1a\xa2A\xd67\xf1\x9b ')

        param1: bytearray = dataclasses.field(metadata={"original_name": ""})


    @dataclasses.dataclass
    class log_string:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#18)

        Attributes:
            param1 (str): string
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': '', 'type': 'string'}], 'name': 'log_string', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_string'
        selector = bytes32(b'\x0b.\x13\xff \xac{GA\x98eU\x83\xed\xf7\r\xed\xd2\xc1\xdc\x98\x0e2\x9cO\xbb/\xc0t\x8byk')

        param1: str = dataclasses.field(metadata={"original_name": ""})


    @dataclasses.dataclass
    class log_named_address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#20)

        Attributes:
            key (str): string
            val (Address): address
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address', 'name': 'val', 'type': 'address'}], 'name': 'log_named_address', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_named_address'
        selector = bytes32(b'\x9cN\x85A\xca\x8f\r\xc1\xc4\x13\xf9\x10\x8ff\xd8-<\xec\xb1\xbd\xdb\xceCza\xca\xa3\x17\\L\xc9o')

        key: str
        val: Address


    @dataclasses.dataclass
    class log_named_bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#21)

        Attributes:
            key (str): string
            val (bytes32): bytes32
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'val', 'type': 'bytes32'}], 'name': 'log_named_bytes32', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_named_bytes32'
        selector = bytes32(b'\xaf\xb7\x95\xc9\xc6\x1eO\xe7F\x8c8o\x92]zT)\xec\xad\x9c\x04\x95\xdd\xb8\xd3\x8di\x06\x14\xd3/\x99')

        key: str
        val: bytes32


    @dataclasses.dataclass
    class log_named_decimal_int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#22)

        Attributes:
            key (str): string
            val (int256): int256
            decimals (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_int', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_named_decimal_int'
        selector = bytes32(b']\xa6\xce\x9dQ\x15\x1b\xa1\x0c\t\xa5Y\xef$\xd5 \xb9\xda\xc5\xc5\xb8\x81\n\xe8CNM\r\x86A\x1a\x95')

        key: str
        val: int256
        decimals: uint256


    @dataclasses.dataclass
    class log_named_decimal_uint:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#23)

        Attributes:
            key (str): string
            val (uint256): uint256
            decimals (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'decimals', 'type': 'uint256'}], 'name': 'log_named_decimal_uint', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_named_decimal_uint'
        selector = bytes32(b"\xeb\x8b\xa4<\xedu7B\x19F\xbdC\xe8(\xb8\xb2\xb8B\x89'\xaa\x8f\x80\x1c\x13\xd94\xbf\x11\xac\xa5{")

        key: str
        val: uint256
        decimals: uint256


    @dataclasses.dataclass
    class log_named_int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#24)

        Attributes:
            key (str): string
            val (int256): int256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256', 'name': 'val', 'type': 'int256'}], 'name': 'log_named_int', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_named_int'
        selector = bytes32(b'/\xe62w\x91t7CxD*\x8e\x97\x8b\xcc\xfb\xdc\xc1\xd6\xb2\xb0\xd8\x1f~\x8e\xb7v\xab"\x86\xf1h')

        key: str
        val: int256


    @dataclasses.dataclass
    class log_named_uint:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#25)

        Attributes:
            key (str): string
            val (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'val', 'type': 'uint256'}], 'name': 'log_named_uint', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_named_uint'
        selector = bytes32(b'\xb2\xde/\xbe\x80\x1a\r\xf6\xc0\xcb\xdd\xfdD\x8b\xa3\xc4\x1dH\xa0@\xca5\xc5l\x81\x96\xef\x0f\xca\xe7!\xa8')

        key: str
        val: uint256


    @dataclasses.dataclass
    class log_named_bytes:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#26)

        Attributes:
            key (str): string
            val (bytearray): bytes
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'val', 'type': 'bytes'}], 'name': 'log_named_bytes', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_named_bytes'
        selector = bytes32(b'\xd2n\x16\xca\xd4T\x87\x05\xe4\xc9\xe2\xd9O\x98\xee\x91\xc2\x89\x08^\xe4%YO\xd5c_\xa2\x96L\xcf\x18')

        key: str
        val: bytearray


    @dataclasses.dataclass
    class log_named_string:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#27)

        Attributes:
            key (str): string
            val (str): string
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'string', 'name': 'val', 'type': 'string'}], 'name': 'log_named_string', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_named_string'
        selector = bytes32(b'(\x0fDF\xb2\x8a\x13rA}\xdae\x8d0\xb9[)\x92\xb1*\xc9\xc7\xf3xS_)\xa9z\xcf5\x83')

        key: str
        val: str


    @dataclasses.dataclass
    class log_array:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#29)

        Attributes:
            val (List[uint256]): uint256[]
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_array', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_array'
        selector = bytes32(b'\xfb\x10(e\xd5\n\xdd\xdd\xf6\x9d\xa9\xb5\xaa\x1b\xce\xd6l\x80\xcf\x86\x9a\\\x8d\x04q\xa4g\xe1\x8c\xe9\xca\xb1')

        val: List[uint256]


    @dataclasses.dataclass
    class log_array_:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#30)

        Attributes:
            val (List[int256]): int256[]
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_array', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_array'
        selector = bytes32(b'\x89\n\x82g\x9bG\x0f+\xd8(\x16\xed\x9b\x16\x1f\x97\xd8\xb9g\xf3\x7f\xa3d|!\xd5\xbf9t\x9e-\xd5')

        val: List[int256]


    @dataclasses.dataclass
    class log_array__:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#31)

        Attributes:
            val (List[Address]): address[]
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_array', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_array'
        selector = bytes32(b'@\xe1\x84\x0fWi\x07=a\xbd\x017-\x9bu\xba\xa9\x84-V)\xa0\xc9\x9f\xf1\x03\xbe\x11x\xa8\xe9\xe2')

        val: List[Address]


    @dataclasses.dataclass
    class log_named_array:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#32)

        Attributes:
            key (str): string
            val (List[uint256]): uint256[]
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'val', 'type': 'uint256[]'}], 'name': 'log_named_array', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_named_array'
        selector = bytes32(b'\x00\xaa\xa3\x9c\x9f\xfb_VzE48\x0cspup.\x1f\x7f\x14\x10\x7f\xc9S(\xe3\xb5l\x03%\xfb')

        key: str
        val: List[uint256]


    @dataclasses.dataclass
    class log_named_array_:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#33)

        Attributes:
            key (str): string
            val (List[int256]): int256[]
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'int256[]', 'name': 'val', 'type': 'int256[]'}], 'name': 'log_named_array', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_named_array'
        selector = bytes32(b'\xa7>\xda\tf/F\xdd\xe7)\xbeF\x118_\xf3O\xe6\xc4O\xbb\xc6\xf7\xe1{\x04+Y\xa3D[W')

        key: str
        val: List[int256]


    @dataclasses.dataclass
    class log_named_array__:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#34)

        Attributes:
            key (str): string
            val (List[Address]): address[]
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'key', 'type': 'string'}, {'indexed': False, 'internalType': 'address[]', 'name': 'val', 'type': 'address[]'}], 'name': 'log_named_array', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'log_named_array'
        selector = bytes32(b";\xcf\xb2\xae.\x8d\x13-\xd1\xfc\xe7\xcf'\x8a\x9a\x19uj\x9f\xce\xab\xe4p\xdf;\xda\xbbK\xc5w\xd1\xbd")

        key: str
        val: List[Address]


    @overload
    def failed(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#40)

        Returns:
            bool
        """
        ...

    @overload
    def failed(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#40)

        Returns:
            bool
        """
        ...

    @overload
    def failed(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#40)

        Returns:
            bool
        """
        ...

    @overload
    def failed(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#40)

        Returns:
            bool
        """
        ...

    def failed(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdAssertions.sol#40)

        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "ba414fa6", [], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

StdAssertions.failed.selector = bytes4(b'\xbaAO\xa6')
