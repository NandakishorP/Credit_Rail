
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.utils.structs.EnumerableSet import EnumerableSet



class EnumerableMap(Library):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/EnumerableMap.sol#54)
    """
    _abi = {b'\x16\x9c0\x8f': {'inputs': [{'internalType': 'bytes', 'name': 'key', 'type': 'bytes'}], 'name': 'EnumerableMapNonexistentBytesKey', 'type': 'error'}, b'\x02\xb5f\x86': {'inputs': [{'internalType': 'bytes32', 'name': 'key', 'type': 'bytes32'}], 'name': 'EnumerableMapNonexistentKey', 'type': 'error'}}
    _storage_layout = {"storage":[]}
    _creation_code = "6080806040523460175760399081601c823930815050f35b5f80fdfe5f80fdfea2646970667358221220b4e2f47d2bc0503ce60b2c901209bcc916b79ca8d3a9510e55f3a293e469bb3d64736f6c63430008210033"

    _library_id = b'_\xfc\xe9\xbb\xf9RA\x95.\x85g\xde\xcf\xd2gp`'

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> EnumerableMap:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[EnumerableMap]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, EnumerableMap, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[EnumerableMap]]:
        return cls._deploy(request_type, [], return_tx, EnumerableMap, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class Bytes32ToBytes32Map:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/EnumerableMap.sol#67)

        Attributes:
            _keys (EnumerableSet.Bytes32Set): struct EnumerableSet.Bytes32Set
            _values (Dict[bytes32, bytes32]): mapping(bytes32 => bytes32)
        """
        original_name = 'Bytes32ToBytes32Map'

        _keys: EnumerableSet.Bytes32Set
        _values: Dict[bytes32, bytes32]


    @dataclasses.dataclass
    class UintToUintMap:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/EnumerableMap.sol#196)

        Attributes:
            _inner (EnumerableMap.Bytes32ToBytes32Map): struct EnumerableMap.Bytes32ToBytes32Map
        """
        original_name = 'UintToUintMap'

        _inner: EnumerableMap.Bytes32ToBytes32Map


    @dataclasses.dataclass
    class UintToAddressMap:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/EnumerableMap.sol#319)

        Attributes:
            _inner (EnumerableMap.Bytes32ToBytes32Map): struct EnumerableMap.Bytes32ToBytes32Map
        """
        original_name = 'UintToAddressMap'

        _inner: EnumerableMap.Bytes32ToBytes32Map


    @dataclasses.dataclass
    class UintToBytes32Map:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/EnumerableMap.sol#442)

        Attributes:
            _inner (EnumerableMap.Bytes32ToBytes32Map): struct EnumerableMap.Bytes32ToBytes32Map
        """
        original_name = 'UintToBytes32Map'

        _inner: EnumerableMap.Bytes32ToBytes32Map


    @dataclasses.dataclass
    class AddressToUintMap:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/EnumerableMap.sol#565)

        Attributes:
            _inner (EnumerableMap.Bytes32ToBytes32Map): struct EnumerableMap.Bytes32ToBytes32Map
        """
        original_name = 'AddressToUintMap'

        _inner: EnumerableMap.Bytes32ToBytes32Map


    @dataclasses.dataclass
    class AddressToAddressMap:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/EnumerableMap.sol#688)

        Attributes:
            _inner (EnumerableMap.Bytes32ToBytes32Map): struct EnumerableMap.Bytes32ToBytes32Map
        """
        original_name = 'AddressToAddressMap'

        _inner: EnumerableMap.Bytes32ToBytes32Map


    @dataclasses.dataclass
    class AddressToBytes32Map:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/EnumerableMap.sol#815)

        Attributes:
            _inner (EnumerableMap.Bytes32ToBytes32Map): struct EnumerableMap.Bytes32ToBytes32Map
        """
        original_name = 'AddressToBytes32Map'

        _inner: EnumerableMap.Bytes32ToBytes32Map


    @dataclasses.dataclass
    class Bytes32ToUintMap:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/EnumerableMap.sol#942)

        Attributes:
            _inner (EnumerableMap.Bytes32ToBytes32Map): struct EnumerableMap.Bytes32ToBytes32Map
        """
        original_name = 'Bytes32ToUintMap'

        _inner: EnumerableMap.Bytes32ToBytes32Map


    @dataclasses.dataclass
    class Bytes32ToAddressMap:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/EnumerableMap.sol#1065)

        Attributes:
            _inner (EnumerableMap.Bytes32ToBytes32Map): struct EnumerableMap.Bytes32ToBytes32Map
        """
        original_name = 'Bytes32ToAddressMap'

        _inner: EnumerableMap.Bytes32ToBytes32Map


    @dataclasses.dataclass
    class BytesToBytesMap:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/EnumerableMap.sol#1195)

        Attributes:
            _keys (EnumerableSet.BytesSet): struct EnumerableSet.BytesSet
            _values (Dict[bytearray, bytearray]): mapping(bytes => bytes)
        """
        original_name = 'BytesToBytesMap'

        _keys: EnumerableSet.BytesSet
        _values: Dict[bytearray, bytearray]


    @dataclasses.dataclass
    class EnumerableMapNonexistentKey(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/EnumerableMap.sol#65)

        Attributes:
            key (bytes32): bytes32
        """
        _abi = {'inputs': [{'internalType': 'bytes32', 'name': 'key', 'type': 'bytes32'}], 'name': 'EnumerableMapNonexistentKey', 'type': 'error'}
        original_name = 'EnumerableMapNonexistentKey'
        selector = bytes4(b'\x02\xb5f\x86')

        key: bytes32


    @dataclasses.dataclass
    class EnumerableMapNonexistentBytesKey(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/structs/EnumerableMap.sol#1193)

        Attributes:
            key (bytearray): bytes
        """
        _abi = {'inputs': [{'internalType': 'bytes', 'name': 'key', 'type': 'bytes'}], 'name': 'EnumerableMapNonexistentBytesKey', 'type': 'error'}
        original_name = 'EnumerableMapNonexistentBytesKey'
        selector = bytes4(b'\x16\x9c0\x8f')

        key: bytearray


