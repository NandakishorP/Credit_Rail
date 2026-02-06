
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.interfaces.IERC2981 import IERC2981
from pytypes.lib.openzeppelincontracts.contracts.utils.introspection.ERC165 import ERC165



class ERC2981(ERC165, IERC2981):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol#22)
    """
    _abi = {b'oH=\t': {'inputs': [{'internalType': 'uint256', 'name': 'numerator', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'denominator', 'type': 'uint256'}], 'name': 'ERC2981InvalidDefaultRoyalty', 'type': 'error'}, b'\xb6\xd9\x90\n': {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'ERC2981InvalidDefaultRoyaltyReceiver', 'type': 'error'}, b'\xdf\xd1\xfc\x1b': {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'numerator', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'denominator', 'type': 'uint256'}], 'name': 'ERC2981InvalidTokenRoyalty', 'type': 'error'}, b'\x96\x9f\x08R': {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'ERC2981InvalidTokenRoyaltyReceiver', 'type': 'error'}, b'*U Z': {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'salePrice', 'type': 'uint256'}], 'name': 'royaltyInfo', 'outputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x01\xff\xc9\xa7': {'inputs': [{'internalType': 'bytes4', 'name': 'interfaceId', 'type': 'bytes4'}], 'name': 'supportsInterface', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":1404,"contract":"lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol:ERC2981","label":"_defaultRoyaltyInfo","offset":0,"slot":0,"type":"t_struct(RoyaltyInfo)1401_storage"},{"astId":1409,"contract":"lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol:ERC2981","label":"_tokenRoyaltyInfo","offset":0,"slot":1,"type":"t_mapping(t_uint256,t_struct(RoyaltyInfo)1401_storage)"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_mapping(t_uint256,t_struct(RoyaltyInfo)1401_storage)":{"encoding":"mapping","label":"mapping(uint256 => struct ERC2981.RoyaltyInfo)","numberOfBytes":32,"key":"t_uint256","value":"t_struct(RoyaltyInfo)1401_storage"},"t_struct(RoyaltyInfo)1401_storage":{"encoding":"inplace","label":"struct ERC2981.RoyaltyInfo","numberOfBytes":32,"members":[{"astId":1398,"contract":"lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol:ERC2981","label":"receiver","offset":0,"slot":0,"type":"t_address"},{"astId":1400,"contract":"lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol:ERC2981","label":"royaltyFraction","offset":20,"slot":0,"type":"t_uint96"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32},"t_uint96":{"encoding":"inplace","label":"uint96","numberOfBytes":12}}}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC2981:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC2981]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC2981, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC2981]]:
        raise Exception("Cannot deploy abstract contract")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an abstract contract")

    @dataclasses.dataclass
    class RoyaltyInfo:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol#23)

        Attributes:
            receiver (Address): address
            royaltyFraction (uint96): uint96
        """
        original_name = 'RoyaltyInfo'

        receiver: Address
        royaltyFraction: uint96


    @dataclasses.dataclass
    class ERC2981InvalidDefaultRoyalty(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol#34)

        Attributes:
            numerator (uint256): uint256
            denominator (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'numerator', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'denominator', 'type': 'uint256'}], 'name': 'ERC2981InvalidDefaultRoyalty', 'type': 'error'}
        original_name = 'ERC2981InvalidDefaultRoyalty'
        selector = bytes4(b'oH=\t')

        numerator: uint256
        denominator: uint256


    @dataclasses.dataclass
    class ERC2981InvalidDefaultRoyaltyReceiver(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol#39)

        Attributes:
            receiver (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'ERC2981InvalidDefaultRoyaltyReceiver', 'type': 'error'}
        original_name = 'ERC2981InvalidDefaultRoyaltyReceiver'
        selector = bytes4(b'\xb6\xd9\x90\n')

        receiver: Address


    @dataclasses.dataclass
    class ERC2981InvalidTokenRoyalty(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol#44)

        Attributes:
            tokenId (uint256): uint256
            numerator (uint256): uint256
            denominator (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'numerator', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'denominator', 'type': 'uint256'}], 'name': 'ERC2981InvalidTokenRoyalty', 'type': 'error'}
        original_name = 'ERC2981InvalidTokenRoyalty'
        selector = bytes4(b'\xdf\xd1\xfc\x1b')

        tokenId: uint256
        numerator: uint256
        denominator: uint256


    @dataclasses.dataclass
    class ERC2981InvalidTokenRoyaltyReceiver(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol#49)

        Attributes:
            tokenId (uint256): uint256
            receiver (Address): address
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'ERC2981InvalidTokenRoyaltyReceiver', 'type': 'error'}
        original_name = 'ERC2981InvalidTokenRoyaltyReceiver'
        selector = bytes4(b'\x96\x9f\x08R')

        tokenId: uint256
        receiver: Address


    @overload
    def supportsInterface(self, interfaceId: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol#52)

        Args:
            interfaceId: bytes4
        Returns:
            bool
        """
        ...

    @overload
    def supportsInterface(self, interfaceId: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol#52)

        Args:
            interfaceId: bytes4
        Returns:
            bool
        """
        ...

    @overload
    def supportsInterface(self, interfaceId: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol#52)

        Args:
            interfaceId: bytes4
        Returns:
            bool
        """
        ...

    @overload
    def supportsInterface(self, interfaceId: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol#52)

        Args:
            interfaceId: bytes4
        Returns:
            bool
        """
        ...

    def supportsInterface(self, interfaceId: bytes4, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol#52)

        Args:
            interfaceId: bytes4
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "01ffc9a7", [interfaceId], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def royaltyInfo(self, tokenId: uint256, salePrice: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Address, uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol#57)

        Args:
            tokenId: uint256
            salePrice: uint256
        Returns:
            receiver: address
            amount: uint256
        """
        ...

    @overload
    def royaltyInfo(self, tokenId: uint256, salePrice: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol#57)

        Args:
            tokenId: uint256
            salePrice: uint256
        Returns:
            receiver: address
            amount: uint256
        """
        ...

    @overload
    def royaltyInfo(self, tokenId: uint256, salePrice: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol#57)

        Args:
            tokenId: uint256
            salePrice: uint256
        Returns:
            receiver: address
            amount: uint256
        """
        ...

    @overload
    def royaltyInfo(self, tokenId: uint256, salePrice: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[Address, uint256]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol#57)

        Args:
            tokenId: uint256
            salePrice: uint256
        Returns:
            receiver: address
            amount: uint256
        """
        ...

    def royaltyInfo(self, tokenId: uint256, salePrice: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[Address, uint256], TransactionAbc[Tuple[Address, uint256]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/common/ERC2981.sol#57)

        Args:
            tokenId: uint256
            salePrice: uint256
        Returns:
            receiver: address
            amount: uint256
        """
        return self._execute(self.chain, request_type, "2a55205a", [tokenId, salePrice], True if request_type == "tx" else False, Tuple[Address, uint256], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC2981.supportsInterface.selector = bytes4(b'\x01\xff\xc9\xa7')
ERC2981.royaltyInfo.selector = bytes4(b'*U Z')
