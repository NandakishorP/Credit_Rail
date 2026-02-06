
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class ConstructorMock(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ConstructorMock.sol#5)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'enum ConstructorMock.RevertType', 'name': 'error', 'type': 'uint8'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\t\xca\xeb\xf3': {'inputs': [], 'name': 'CustomError', 'type': 'error'}}
    _storage_layout = {"storage":[{"astId":3,"contract":"lib/openzeppelin-contracts/contracts/mocks/ConstructorMock.sol:ConstructorMock","label":"foo","offset":0,"slot":0,"type":"t_bool"}],"types":{"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1}}}
    _creation_code = "6080346100ee57601f61014038819003918201601f19168301916001600160401b038311848410176100f2578084926020946040528339810103126100ee575160058110156100ee57600160ff195f5416175f55600181145f14610061575f80fd5b600281036100ae5760405162461bcd60e51b815260206004820152601a60248201527f436f6e7374727563746f724d6f636b3a20726576657274696e670000000000006044820152606490fd5b600381036100c5576309caebf360e01b5f5260045ffd5b6004146100da57604051603990816101078239f35b634e487b7160e01b5f52601260045260245ffd5b5f80fd5b634e487b7160e01b5f52604160045260245ffdfe5f80fdfea26469706673582212205b92fa073bb46aad30b2dbf78bf58579fd7700b36bb7f39ba93c102d827ee72264736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, error: ConstructorMock.RevertType, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ConstructorMock.sol#18)

        Args:
            error: enum ConstructorMock.RevertType
        """
        ...

    @overload
    @classmethod
    def deploy(cls, error: ConstructorMock.RevertType, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ConstructorMock:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ConstructorMock.sol#18)

        Args:
            error: enum ConstructorMock.RevertType
        """
        ...

    @overload
    @classmethod
    def deploy(cls, error: ConstructorMock.RevertType, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ConstructorMock.sol#18)

        Args:
            error: enum ConstructorMock.RevertType
        """
        ...

    @overload
    @classmethod
    def deploy(cls, error: ConstructorMock.RevertType, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ConstructorMock.sol#18)

        Args:
            error: enum ConstructorMock.RevertType
        """
        ...

    @overload
    @classmethod
    def deploy(cls, error: ConstructorMock.RevertType, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ConstructorMock]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ConstructorMock.sol#18)

        Args:
            error: enum ConstructorMock.RevertType
        """
        ...

    @classmethod
    def deploy(cls, error: ConstructorMock.RevertType, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ConstructorMock, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ConstructorMock]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ConstructorMock.sol#18)

        Args:
            error: enum ConstructorMock.RevertType
        """
        return cls._deploy(request_type, [error], return_tx, ConstructorMock, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    class RevertType(IntEnum):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ConstructorMock.sol#8)

        """
        None_ = 0
        RevertWithoutMessage = 1
        RevertWithMessage = 2
        RevertWithCustomError = 3
        Panic = 4


    @dataclasses.dataclass
    class CustomError(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/ConstructorMock.sol#16)
        """
        _abi = {'inputs': [], 'name': 'CustomError', 'type': 'error'}
        original_name = 'CustomError'
        selector = bytes4(b'\t\xca\xeb\xf3')



