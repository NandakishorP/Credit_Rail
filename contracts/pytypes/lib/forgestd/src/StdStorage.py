
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



@dataclasses.dataclass
class FindData:
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdStorage.sol#6)

    Attributes:
        slot (uint256): uint256
        offsetLeft (uint256): uint256
        offsetRight (uint256): uint256
        found (bool): bool
    """
    original_name = 'FindData'

    slot: uint256
    offsetLeft: uint256
    offsetRight: uint256
    found: bool


@dataclasses.dataclass
class StdStorage:
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdStorage.sol#13)

    Attributes:
        finds (Dict[Address, Dict[bytes4, Dict[bytes32, FindData]]]): mapping(address => mapping(bytes4 => mapping(bytes32 => struct FindData)))
        _keys (List[bytes32]): bytes32[]
        _sig (bytes4): bytes4
        _depth (uint256): uint256
        _target (Address): address
        _set (bytes32): bytes32
        _enable_packed_slots (bool): bool
        _calldata (bytearray): bytes
    """
    original_name = 'StdStorage'

    finds: Dict[Address, Dict[bytes4, Dict[bytes32, FindData]]]
    _keys: List[bytes32]
    _sig: bytes4
    _depth: uint256
    _target: Address
    _set: bytes32
    _enable_packed_slots: bool
    _calldata: bytearray


class stdStorageSafe(Library):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdStorage.sol#24)
    """
    _abi = {b'\x9c\x95U\xb1\xe3\x10.<\xf4\x8fB}y\xcbg\x8f]\x9b\xd1\xed\n\xd5t8\x94a\xe2U\xf9Qp\xed': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'who', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes4', 'name': 'fsig', 'type': 'bytes4'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'keysHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'slot', 'type': 'uint256'}], 'name': 'SlotFound', 'type': 'event'}, b'\x08\x0f\xc4\xa9f \xc4F.p[#\xf3FA?\xe3yk\xb6<o\x8d\x85\x91\xba\xec\x0e#\x15w\xa5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'who', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'slot', 'type': 'uint256'}], 'name': 'WARNING_UninitedSlot', 'type': 'event'}}
    _storage_layout = {"storage":[]}
    _creation_code = "6080806040523460175760399081601c823930815050f35b5f80fdfe5f80fdfea26469706673582212201ccd3ebab8461270d5e5a9fe4ec5f4d650d1debf8d587b19761171c23ebf82cd64736f6c63430008210033"

    _library_id = b'\xb0V\xca\xd5#\x06\xd2\x932Ga1S\xd6A\xe1\xb8'

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> stdStorageSafe:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[stdStorageSafe]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, stdStorageSafe, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[stdStorageSafe]]:
        return cls._deploy(request_type, [], return_tx, stdStorageSafe, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class SlotFound:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdStorage.sol#25)

        Attributes:
            who (Address): address
            fsig (bytes4): bytes4
            keysHash (bytes32): bytes32
            slot (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'who', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes4', 'name': 'fsig', 'type': 'bytes4'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'keysHash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'slot', 'type': 'uint256'}], 'name': 'SlotFound', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'SlotFound'
        selector = bytes32(b'\x9c\x95U\xb1\xe3\x10.<\xf4\x8fB}y\xcbg\x8f]\x9b\xd1\xed\n\xd5t8\x94a\xe2U\xf9Qp\xed')

        who: Address
        fsig: bytes4
        keysHash: bytes32
        slot: uint256


    @dataclasses.dataclass
    class WARNING_UninitedSlot:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdStorage.sol#26)

        Attributes:
            who (Address): address
            slot (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'who', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'slot', 'type': 'uint256'}], 'name': 'WARNING_UninitedSlot', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'WARNING_UninitedSlot'
        selector = bytes32(b'\x08\x0f\xc4\xa9f \xc4F.p[#\xf3FA?\xe3yk\xb6<o\x8d\x85\x91\xba\xec\x0e#\x15w\xa5')

        who: Address
        slot: uint256


class stdStorage(Library):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/forge-std/src/StdStorage.sol#334)
    """
    _abi = {}
    _storage_layout = {"storage":[]}
    _creation_code = "6080806040523460175760399081601c823930815050f35b5f80fdfe5f80fdfea264697066735822122040b648609962b705da15b3ac7022c46da711034a9f04f334e5fcdd8a0501dea864736f6c63430008210033"

    _library_id = b'\x94\xce\xe1g]\xf2\xc6\xc3\x06\x1bW]\xc3\xe5\xdda\xed'

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> stdStorage:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[stdStorage]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, stdStorage, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[stdStorage]]:
        return cls._deploy(request_type, [], return_tx, stdStorage, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

