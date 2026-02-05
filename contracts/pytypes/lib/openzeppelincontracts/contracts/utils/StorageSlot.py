
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class StorageSlot(Library):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/StorageSlot.sol#34)
    """
    _abi = {}
    _storage_layout = {"storage":[]}
    _creation_code = "6080806040523460175760399081601c823930815050f35b5f80fdfe5f80fdfea2646970667358221220c0befd09b238b61c7a55d23764c4d7fe6f09b62db6e24d7d3d13ca56294e76d864736f6c63430008210033"

    _library_id = b'\x1c\x1a\x85\xc6\n\xffpI\xa0k\xc3\xa8\x1a>\x80\x9b\x9a'

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> StorageSlot:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[StorageSlot]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, StorageSlot, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[StorageSlot]]:
        return cls._deploy(request_type, [], return_tx, StorageSlot, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class AddressSlot:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/StorageSlot.sol#35)

        Attributes:
            value (Address): address
        """
        original_name = 'AddressSlot'

        value: Address


    @dataclasses.dataclass
    class BooleanSlot:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/StorageSlot.sol#39)

        Attributes:
            value (bool): bool
        """
        original_name = 'BooleanSlot'

        value: bool


    @dataclasses.dataclass
    class Bytes32Slot:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/StorageSlot.sol#43)

        Attributes:
            value (bytes32): bytes32
        """
        original_name = 'Bytes32Slot'

        value: bytes32


    @dataclasses.dataclass
    class Uint256Slot:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/StorageSlot.sol#47)

        Attributes:
            value (uint256): uint256
        """
        original_name = 'Uint256Slot'

        value: uint256


    @dataclasses.dataclass
    class Int256Slot:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/StorageSlot.sol#51)

        Attributes:
            value (int256): int256
        """
        original_name = 'Int256Slot'

        value: int256


    @dataclasses.dataclass
    class StringSlot:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/StorageSlot.sol#55)

        Attributes:
            value (str): string
        """
        original_name = 'StringSlot'

        value: str


    @dataclasses.dataclass
    class BytesSlot:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/StorageSlot.sol#59)

        Attributes:
            value (bytearray): bytes
        """
        original_name = 'BytesSlot'

        value: bytearray


