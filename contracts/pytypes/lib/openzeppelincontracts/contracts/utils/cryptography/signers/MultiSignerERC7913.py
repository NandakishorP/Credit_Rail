
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.utils.cryptography.signers.AbstractSigner import AbstractSigner



class MultiSignerERC7913(AbstractSigner):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#45)
    """
    _abi = {b'%\xe1zA': {'inputs': [{'internalType': 'bytes', 'name': 'signer', 'type': 'bytes'}], 'name': 'MultiSignerERC7913AlreadyExists', 'type': 'error'}, b'\x0cA\xddl': {'inputs': [{'internalType': 'bytes', 'name': 'signer', 'type': 'bytes'}], 'name': 'MultiSignerERC7913InvalidSigner', 'type': 'error'}, b'\xb3\xa2\xe4\xcb': {'inputs': [{'internalType': 'bytes', 'name': 'signer', 'type': 'bytes'}], 'name': 'MultiSignerERC7913NonexistentSigner', 'type': 'error'}, b'\x82I\xd7W': {'inputs': [{'internalType': 'uint64', 'name': 'signers', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'threshold', 'type': 'uint64'}], 'name': 'MultiSignerERC7913UnreachableThreshold', 'type': 'error'}, b'\x8a\xbbT\xbe': {'inputs': [], 'name': 'MultiSignerERC7913ZeroThreshold', 'type': 'error'}, b'K5\xcaJ\x07\x08\xfa=8&~(\xbd\x94x!Mqf\xd3H?x\xa0\xf3[\x00ir\x19\xd2\xb2': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes', 'name': 'signers', 'type': 'bytes'}], 'name': 'ERC7913SignerAdded', 'type': 'event'}, b'\xca.\xce\x94\xb6`\xc2;\xf1\xa2\xa2\x17\xd3\x83\xd9G\x01\xca\x9e6\x8a\x08)!\xf2\xd73\xd0\x10\xe8U\x05': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes', 'name': 'signers', 'type': 'bytes'}], 'name': 'ERC7913SignerRemoved', 'type': 'event'}, b'\xa1\xbc\xba\xd4\xca\x88\xe7H\xde\x7f\x03\x9c\xec\x10P\x95\xba\xe0\x00Hj\xb6S>\xfb3\xa3\x1dy\xbd\xae^': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint64', 'name': 'threshold', 'type': 'uint64'}], 'name': 'ERC7913ThresholdSet', 'type': 'event'}, b'\xb7\x15\xbe\x81': {'inputs': [], 'name': 'getSignerCount', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x95\xfc\xd0A': {'inputs': [{'internalType': 'uint64', 'name': 'start', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'end', 'type': 'uint64'}], 'name': 'getSigners', 'outputs': [{'internalType': 'bytes[]', 'name': '', 'type': 'bytes[]'}], 'stateMutability': 'view', 'type': 'function'}, b'C\xb9\x86e': {'inputs': [{'internalType': 'bytes', 'name': 'signer', 'type': 'bytes'}], 'name': 'isSigner', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'B\xcd\xe4\xe8': {'inputs': [], 'name': 'threshold', 'outputs': [{'internalType': 'uint64', 'name': '', 'type': 'uint64'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":55945,"contract":"lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol:MultiSignerERC7913","label":"_signers","offset":0,"slot":0,"type":"t_struct(BytesSet)62113_storage"},{"astId":55947,"contract":"lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol:MultiSignerERC7913","label":"_threshold","offset":0,"slot":2,"type":"t_uint64"}],"types":{"t_array(t_bytes_storage)dyn_storage":{"encoding":"dynamic_array","label":"bytes[]","numberOfBytes":32,"base":"t_bytes_storage"},"t_bytes_memory_ptr":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_mapping(t_bytes_memory_ptr,t_uint256)":{"encoding":"mapping","label":"mapping(bytes => uint256)","numberOfBytes":32,"key":"t_bytes_memory_ptr","value":"t_uint256"},"t_struct(BytesSet)62113_storage":{"encoding":"inplace","label":"struct EnumerableSet.BytesSet","numberOfBytes":64,"members":[{"astId":62108,"contract":"lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol:MultiSignerERC7913","label":"_values","offset":0,"slot":0,"type":"t_array(t_bytes_storage)dyn_storage"},{"astId":62112,"contract":"lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol:MultiSignerERC7913","label":"_positions","offset":0,"slot":1,"type":"t_mapping(t_bytes_memory_ptr,t_uint256)"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32},"t_uint64":{"encoding":"inplace","label":"uint64","numberOfBytes":8}}}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, signers_: List[Union[bytearray, bytes]], threshold_: uint64, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#76)

        Args:
            signers_: bytes[]
            threshold_: uint64
        """
        ...

    @overload
    @classmethod
    def deploy(cls, signers_: List[Union[bytearray, bytes]], threshold_: uint64, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> MultiSignerERC7913:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#76)

        Args:
            signers_: bytes[]
            threshold_: uint64
        """
        ...

    @overload
    @classmethod
    def deploy(cls, signers_: List[Union[bytearray, bytes]], threshold_: uint64, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#76)

        Args:
            signers_: bytes[]
            threshold_: uint64
        """
        ...

    @overload
    @classmethod
    def deploy(cls, signers_: List[Union[bytearray, bytes]], threshold_: uint64, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#76)

        Args:
            signers_: bytes[]
            threshold_: uint64
        """
        ...

    @overload
    @classmethod
    def deploy(cls, signers_: List[Union[bytearray, bytes]], threshold_: uint64, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[MultiSignerERC7913]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#76)

        Args:
            signers_: bytes[]
            threshold_: uint64
        """
        ...

    @classmethod
    def deploy(cls, signers_: List[Union[bytearray, bytes]], threshold_: uint64, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, MultiSignerERC7913, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[MultiSignerERC7913]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#76)

        Args:
            signers_: bytes[]
            threshold_: uint64
        """
        raise Exception("Cannot deploy abstract contract")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an abstract contract")

    @dataclasses.dataclass
    class MultiSignerERC7913AlreadyExists(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#62)

        Attributes:
            signer (bytearray): bytes
        """
        _abi = {'inputs': [{'internalType': 'bytes', 'name': 'signer', 'type': 'bytes'}], 'name': 'MultiSignerERC7913AlreadyExists', 'type': 'error'}
        original_name = 'MultiSignerERC7913AlreadyExists'
        selector = bytes4(b'%\xe1zA')

        signer: bytearray


    @dataclasses.dataclass
    class MultiSignerERC7913NonexistentSigner(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#65)

        Attributes:
            signer (bytearray): bytes
        """
        _abi = {'inputs': [{'internalType': 'bytes', 'name': 'signer', 'type': 'bytes'}], 'name': 'MultiSignerERC7913NonexistentSigner', 'type': 'error'}
        original_name = 'MultiSignerERC7913NonexistentSigner'
        selector = bytes4(b'\xb3\xa2\xe4\xcb')

        signer: bytearray


    @dataclasses.dataclass
    class MultiSignerERC7913InvalidSigner(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#68)

        Attributes:
            signer (bytearray): bytes
        """
        _abi = {'inputs': [{'internalType': 'bytes', 'name': 'signer', 'type': 'bytes'}], 'name': 'MultiSignerERC7913InvalidSigner', 'type': 'error'}
        original_name = 'MultiSignerERC7913InvalidSigner'
        selector = bytes4(b'\x0cA\xddl')

        signer: bytearray


    @dataclasses.dataclass
    class MultiSignerERC7913ZeroThreshold(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#71)
        """
        _abi = {'inputs': [], 'name': 'MultiSignerERC7913ZeroThreshold', 'type': 'error'}
        original_name = 'MultiSignerERC7913ZeroThreshold'
        selector = bytes4(b'\x8a\xbbT\xbe')



    @dataclasses.dataclass
    class MultiSignerERC7913UnreachableThreshold(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#74)

        Attributes:
            signers (uint64): uint64
            threshold (uint64): uint64
        """
        _abi = {'inputs': [{'internalType': 'uint64', 'name': 'signers', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'threshold', 'type': 'uint64'}], 'name': 'MultiSignerERC7913UnreachableThreshold', 'type': 'error'}
        original_name = 'MultiSignerERC7913UnreachableThreshold'
        selector = bytes4(b'\x82I\xd7W')

        signers: uint64
        threshold: uint64


    @dataclasses.dataclass
    class ERC7913SignerAdded:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#53)

        Attributes:
            signers_hash (bytes): indexed bytes
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes', 'name': 'signers', 'type': 'bytes'}], 'name': 'ERC7913SignerAdded', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ERC7913SignerAdded'
        selector = bytes32(b'K5\xcaJ\x07\x08\xfa=8&~(\xbd\x94x!Mqf\xd3H?x\xa0\xf3[\x00ir\x19\xd2\xb2')

        signers_hash: bytes = dataclasses.field(metadata={"original_name": "signers"})


    @dataclasses.dataclass
    class ERC7913SignerRemoved:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#56)

        Attributes:
            signers_hash (bytes): indexed bytes
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes', 'name': 'signers', 'type': 'bytes'}], 'name': 'ERC7913SignerRemoved', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ERC7913SignerRemoved'
        selector = bytes32(b'\xca.\xce\x94\xb6`\xc2;\xf1\xa2\xa2\x17\xd3\x83\xd9G\x01\xca\x9e6\x8a\x08)!\xf2\xd73\xd0\x10\xe8U\x05')

        signers_hash: bytes = dataclasses.field(metadata={"original_name": "signers"})


    @dataclasses.dataclass
    class ERC7913ThresholdSet:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#59)

        Attributes:
            threshold (uint64): uint64
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint64', 'name': 'threshold', 'type': 'uint64'}], 'name': 'ERC7913ThresholdSet', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ERC7913ThresholdSet'
        selector = bytes32(b'\xa1\xbc\xba\xd4\xca\x88\xe7H\xde\x7f\x03\x9c\xec\x10P\x95\xba\xe0\x00Hj\xb6S>\xfb3\xa3\x1dy\xbd\xae^')

        threshold: uint64


    @overload
    def getSigners(self, start: uint64, end: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> List[bytearray]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#90)

        Args:
            start: uint64
            end: uint64
        Returns:
            bytes[]
        """
        ...

    @overload
    def getSigners(self, start: uint64, end: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#90)

        Args:
            start: uint64
            end: uint64
        Returns:
            bytes[]
        """
        ...

    @overload
    def getSigners(self, start: uint64, end: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#90)

        Args:
            start: uint64
            end: uint64
        Returns:
            bytes[]
        """
        ...

    @overload
    def getSigners(self, start: uint64, end: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[List[bytearray]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#90)

        Args:
            start: uint64
            end: uint64
        Returns:
            bytes[]
        """
        ...

    def getSigners(self, start: uint64, end: uint64, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[List[bytearray], TransactionAbc[List[bytearray]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#90)

        Args:
            start: uint64
            end: uint64
        Returns:
            bytes[]
        """
        return self._execute(self.chain, request_type, "95fcd041", [start, end], True if request_type == "tx" else False, List[bytearray], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getSignerCount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#95)

        Returns:
            uint256
        """
        ...

    @overload
    def getSignerCount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#95)

        Returns:
            uint256
        """
        ...

    @overload
    def getSignerCount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#95)

        Returns:
            uint256
        """
        ...

    @overload
    def getSignerCount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#95)

        Returns:
            uint256
        """
        ...

    def getSignerCount(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#95)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "b715be81", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def isSigner(self, signer: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#100)

        Args:
            signer: bytes
        Returns:
            bool
        """
        ...

    @overload
    def isSigner(self, signer: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#100)

        Args:
            signer: bytes
        Returns:
            bool
        """
        ...

    @overload
    def isSigner(self, signer: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#100)

        Args:
            signer: bytes
        Returns:
            bool
        """
        ...

    @overload
    def isSigner(self, signer: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#100)

        Args:
            signer: bytes
        Returns:
            bool
        """
        ...

    def isSigner(self, signer: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#100)

        Args:
            signer: bytes
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "43b98665", [signer], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def threshold(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint64:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#105)

        Returns:
            uint64
        """
        ...

    @overload
    def threshold(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#105)

        Returns:
            uint64
        """
        ...

    @overload
    def threshold(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#105)

        Returns:
            uint64
        """
        ...

    @overload
    def threshold(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint64]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#105)

        Returns:
            uint64
        """
        ...

    def threshold(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint64, TransactionAbc[uint64], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913.sol#105)

        Returns:
            uint64
        """
        return self._execute(self.chain, request_type, "42cde4e8", [], True if request_type == "tx" else False, uint64, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

MultiSignerERC7913.getSigners.selector = bytes4(b'\x95\xfc\xd0A')
MultiSignerERC7913.getSignerCount.selector = bytes4(b'\xb7\x15\xbe\x81')
MultiSignerERC7913.isSigner.selector = bytes4(b'C\xb9\x86e')
MultiSignerERC7913.threshold.selector = bytes4(b'B\xcd\xe4\xe8')
