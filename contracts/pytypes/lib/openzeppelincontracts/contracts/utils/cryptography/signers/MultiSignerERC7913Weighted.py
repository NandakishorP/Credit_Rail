
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.utils.cryptography.signers.MultiSignerERC7913 import MultiSignerERC7913



class MultiSignerERC7913Weighted(MultiSignerERC7913):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#48)
    """
    _abi = {b'%\xe1zA': {'inputs': [{'internalType': 'bytes', 'name': 'signer', 'type': 'bytes'}], 'name': 'MultiSignerERC7913AlreadyExists', 'type': 'error'}, b'\x0cA\xddl': {'inputs': [{'internalType': 'bytes', 'name': 'signer', 'type': 'bytes'}], 'name': 'MultiSignerERC7913InvalidSigner', 'type': 'error'}, b'\xb3\xa2\xe4\xcb': {'inputs': [{'internalType': 'bytes', 'name': 'signer', 'type': 'bytes'}], 'name': 'MultiSignerERC7913NonexistentSigner', 'type': 'error'}, b'\x82I\xd7W': {'inputs': [{'internalType': 'uint64', 'name': 'signers', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'threshold', 'type': 'uint64'}], 'name': 'MultiSignerERC7913UnreachableThreshold', 'type': 'error'}, b'\xaa\x16\xddJ': {'inputs': [{'internalType': 'bytes', 'name': 'signer', 'type': 'bytes'}, {'internalType': 'uint64', 'name': 'weight', 'type': 'uint64'}], 'name': 'MultiSignerERC7913WeightedInvalidWeight', 'type': 'error'}, b'p\xb7\x9c\x11': {'inputs': [], 'name': 'MultiSignerERC7913WeightedMismatchedLength', 'type': 'error'}, b'\x8a\xbbT\xbe': {'inputs': [], 'name': 'MultiSignerERC7913ZeroThreshold', 'type': 'error'}, b'm\xfc\xc6P': {'inputs': [{'internalType': 'uint8', 'name': 'bits', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'SafeCastOverflowedUintDowncast', 'type': 'error'}, b'K5\xcaJ\x07\x08\xfa=8&~(\xbd\x94x!Mqf\xd3H?x\xa0\xf3[\x00ir\x19\xd2\xb2': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes', 'name': 'signers', 'type': 'bytes'}], 'name': 'ERC7913SignerAdded', 'type': 'event'}, b'\xca.\xce\x94\xb6`\xc2;\xf1\xa2\xa2\x17\xd3\x83\xd9G\x01\xca\x9e6\x8a\x08)!\xf2\xd73\xd0\x10\xe8U\x05': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes', 'name': 'signers', 'type': 'bytes'}], 'name': 'ERC7913SignerRemoved', 'type': 'event'}, b'#o\xf9M\x1f\x13\xb3[\x0b5\xb2\x85U\xfd\x14}gvxjh\x85\x07$3\xe1\xd9\x81A\xa1\xfa.': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes', 'name': 'signer', 'type': 'bytes'}, {'indexed': False, 'internalType': 'uint64', 'name': 'weight', 'type': 'uint64'}], 'name': 'ERC7913SignerWeightChanged', 'type': 'event'}, b'\xa1\xbc\xba\xd4\xca\x88\xe7H\xde\x7f\x03\x9c\xec\x10P\x95\xba\xe0\x00Hj\xb6S>\xfb3\xa3\x1dy\xbd\xae^': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint64', 'name': 'threshold', 'type': 'uint64'}], 'name': 'ERC7913ThresholdSet', 'type': 'event'}, b'\xb7\x15\xbe\x81': {'inputs': [], 'name': 'getSignerCount', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x95\xfc\xd0A': {'inputs': [{'internalType': 'uint64', 'name': 'start', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'end', 'type': 'uint64'}], 'name': 'getSigners', 'outputs': [{'internalType': 'bytes[]', 'name': '', 'type': 'bytes[]'}], 'stateMutability': 'view', 'type': 'function'}, b'C\xb9\x86e': {'inputs': [{'internalType': 'bytes', 'name': 'signer', 'type': 'bytes'}], 'name': 'isSigner', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'Ya@\xa1': {'inputs': [{'internalType': 'bytes', 'name': 'signer', 'type': 'bytes'}], 'name': 'signerWeight', 'outputs': [{'internalType': 'uint64', 'name': '', 'type': 'uint64'}], 'stateMutability': 'view', 'type': 'function'}, b'B\xcd\xe4\xe8': {'inputs': [], 'name': 'threshold', 'outputs': [{'internalType': 'uint64', 'name': '', 'type': 'uint64'}], 'stateMutability': 'view', 'type': 'function'}, b'\x96\xc8.W': {'inputs': [], 'name': 'totalWeight', 'outputs': [{'internalType': 'uint64', 'name': '', 'type': 'uint64'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":55945,"contract":"lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol:MultiSignerERC7913Weighted","label":"_signers","offset":0,"slot":0,"type":"t_struct(BytesSet)62113_storage"},{"astId":55947,"contract":"lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol:MultiSignerERC7913Weighted","label":"_threshold","offset":0,"slot":2,"type":"t_uint64"},{"astId":56329,"contract":"lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol:MultiSignerERC7913Weighted","label":"_totalExtraWeight","offset":8,"slot":2,"type":"t_uint64"},{"astId":56333,"contract":"lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol:MultiSignerERC7913Weighted","label":"_extraWeights","offset":0,"slot":3,"type":"t_mapping(t_bytes_memory_ptr,t_uint64)"}],"types":{"t_array(t_bytes_storage)dyn_storage":{"encoding":"dynamic_array","label":"bytes[]","numberOfBytes":32,"base":"t_bytes_storage"},"t_bytes_memory_ptr":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_bytes_storage":{"encoding":"bytes","label":"bytes","numberOfBytes":32},"t_mapping(t_bytes_memory_ptr,t_uint256)":{"encoding":"mapping","label":"mapping(bytes => uint256)","numberOfBytes":32,"key":"t_bytes_memory_ptr","value":"t_uint256"},"t_mapping(t_bytes_memory_ptr,t_uint64)":{"encoding":"mapping","label":"mapping(bytes => uint64)","numberOfBytes":32,"key":"t_bytes_memory_ptr","value":"t_uint64"},"t_struct(BytesSet)62113_storage":{"encoding":"inplace","label":"struct EnumerableSet.BytesSet","numberOfBytes":64,"members":[{"astId":62108,"contract":"lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol:MultiSignerERC7913Weighted","label":"_values","offset":0,"slot":0,"type":"t_array(t_bytes_storage)dyn_storage"},{"astId":62112,"contract":"lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol:MultiSignerERC7913Weighted","label":"_positions","offset":0,"slot":1,"type":"t_mapping(t_bytes_memory_ptr,t_uint256)"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32},"t_uint64":{"encoding":"inplace","label":"uint64","numberOfBytes":8}}}
    _creation_code = ""

    @overload
    @classmethod
    def deploy(cls, signers_: List[Union[bytearray, bytes]], weights_: List[uint64], threshold_: uint64, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#71)

        Args:
            signers_: bytes[]
            weights_: uint64[]
            threshold_: uint64
        """
        ...

    @overload
    @classmethod
    def deploy(cls, signers_: List[Union[bytearray, bytes]], weights_: List[uint64], threshold_: uint64, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> MultiSignerERC7913Weighted:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#71)

        Args:
            signers_: bytes[]
            weights_: uint64[]
            threshold_: uint64
        """
        ...

    @overload
    @classmethod
    def deploy(cls, signers_: List[Union[bytearray, bytes]], weights_: List[uint64], threshold_: uint64, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#71)

        Args:
            signers_: bytes[]
            weights_: uint64[]
            threshold_: uint64
        """
        ...

    @overload
    @classmethod
    def deploy(cls, signers_: List[Union[bytearray, bytes]], weights_: List[uint64], threshold_: uint64, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#71)

        Args:
            signers_: bytes[]
            weights_: uint64[]
            threshold_: uint64
        """
        ...

    @overload
    @classmethod
    def deploy(cls, signers_: List[Union[bytearray, bytes]], weights_: List[uint64], threshold_: uint64, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[MultiSignerERC7913Weighted]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#71)

        Args:
            signers_: bytes[]
            weights_: uint64[]
            threshold_: uint64
        """
        ...

    @classmethod
    def deploy(cls, signers_: List[Union[bytearray, bytes]], weights_: List[uint64], threshold_: uint64, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, MultiSignerERC7913Weighted, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[MultiSignerERC7913Weighted]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#71)

        Args:
            signers_: bytes[]
            weights_: uint64[]
            threshold_: uint64
        """
        raise Exception("Cannot deploy abstract contract")

    @classmethod
    def get_creation_code(cls) -> bytes:
        raise Exception("Cannot get creation code of an abstract contract")

    @dataclasses.dataclass
    class MultiSignerERC7913WeightedInvalidWeight(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#66)

        Attributes:
            signer (bytearray): bytes
            weight (uint64): uint64
        """
        _abi = {'inputs': [{'internalType': 'bytes', 'name': 'signer', 'type': 'bytes'}, {'internalType': 'uint64', 'name': 'weight', 'type': 'uint64'}], 'name': 'MultiSignerERC7913WeightedInvalidWeight', 'type': 'error'}
        original_name = 'MultiSignerERC7913WeightedInvalidWeight'
        selector = bytes4(b'\xaa\x16\xddJ')

        signer: bytearray
        weight: uint64


    @dataclasses.dataclass
    class MultiSignerERC7913WeightedMismatchedLength(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#69)
        """
        _abi = {'inputs': [], 'name': 'MultiSignerERC7913WeightedMismatchedLength', 'type': 'error'}
        original_name = 'MultiSignerERC7913WeightedMismatchedLength'
        selector = bytes4(b'p\xb7\x9c\x11')



    @dataclasses.dataclass
    class ERC7913SignerWeightChanged:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#63)

        Attributes:
            signer_hash (bytes): indexed bytes
            weight (uint64): uint64
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes', 'name': 'signer', 'type': 'bytes'}, {'indexed': False, 'internalType': 'uint64', 'name': 'weight', 'type': 'uint64'}], 'name': 'ERC7913SignerWeightChanged', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ERC7913SignerWeightChanged'
        selector = bytes32(b'#o\xf9M\x1f\x13\xb3[\x0b5\xb2\x85U\xfd\x14}gvxjh\x85\x07$3\xe1\xd9\x81A\xa1\xfa.')

        signer_hash: bytes = dataclasses.field(metadata={"original_name": "signer"})
        weight: uint64


    @overload
    def signerWeight(self, signer: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint64:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#77)

        Args:
            signer: bytes
        Returns:
            uint64
        """
        ...

    @overload
    def signerWeight(self, signer: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#77)

        Args:
            signer: bytes
        Returns:
            uint64
        """
        ...

    @overload
    def signerWeight(self, signer: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#77)

        Args:
            signer: bytes
        Returns:
            uint64
        """
        ...

    @overload
    def signerWeight(self, signer: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint64]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#77)

        Args:
            signer: bytes
        Returns:
            uint64
        """
        ...

    def signerWeight(self, signer: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint64, TransactionAbc[uint64], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#77)

        Args:
            signer: bytes
        Returns:
            uint64
        """
        return self._execute(self.chain, request_type, "596140a1", [signer], True if request_type == "tx" else False, uint64, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalWeight(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint64:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#85)

        Returns:
            uint64
        """
        ...

    @overload
    def totalWeight(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#85)

        Returns:
            uint64
        """
        ...

    @overload
    def totalWeight(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#85)

        Returns:
            uint64
        """
        ...

    @overload
    def totalWeight(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint64]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#85)

        Returns:
            uint64
        """
        ...

    def totalWeight(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint64, TransactionAbc[uint64], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol#85)

        Returns:
            uint64
        """
        return self._execute(self.chain, request_type, "96c82e57", [], True if request_type == "tx" else False, uint64, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

MultiSignerERC7913Weighted.signerWeight.selector = bytes4(b'Ya@\xa1')
MultiSignerERC7913Weighted.totalWeight.selector = bytes4(b'\x96\xc8.W')
