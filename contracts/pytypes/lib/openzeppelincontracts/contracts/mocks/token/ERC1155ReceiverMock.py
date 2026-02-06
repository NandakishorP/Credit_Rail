
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.token.ERC1155.IERC1155Receiver import IERC1155Receiver
from pytypes.lib.openzeppelincontracts.contracts.utils.introspection.ERC165 import ERC165



class ERC1155ReceiverMock(IERC1155Receiver, ERC165):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#8)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'bytes4', 'name': 'recRetval', 'type': 'bytes4'}, {'internalType': 'bytes4', 'name': 'batRetval', 'type': 'bytes4'}, {'internalType': 'enum ERC1155ReceiverMock.RevertType', 'name': 'error', 'type': 'uint8'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'fC[\xc0': {'inputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'name': 'CustomError', 'type': 'error'}, b'\x0b\xca\xd9"K\xa3;WN\x9c\x85)\x8d\xe2\xf4KL\x80\x01Z!\xaa]\xf4t\x89dD\x90\x98c\xd8': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'ids', 'type': 'uint256[]'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'indexed': False, 'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'indexed': False, 'internalType': 'uint256', 'name': 'gas', 'type': 'uint256'}], 'name': 'BatchReceived', 'type': 'event'}, b' \xdf\xa9\xf7\x90`\xc8\xc4\xd7\xfe\x89,\x97\xc7\x1b\xcfn;c\xd1\xdc\xf6o\xeaz\xef\xc0!\x16(\xcf)': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'indexed': False, 'internalType': 'uint256', 'name': 'gas', 'type': 'uint256'}], 'name': 'Received', 'type': 'event'}, b'\xbc\x19|\x81': {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'uint256[]', 'name': 'ids', 'type': 'uint256[]'}, {'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'onERC1155BatchReceived', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf2:na': {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'onERC1155Received', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x01\xff\xc9\xa7': {'inputs': [{'internalType': 'bytes4', 'name': 'interfaceId', 'type': 'bytes4'}], 'name': 'supportsInterface', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = "60e0346100aa57601f61066e38819003918201601f19168301916001600160401b038311848410176100ae578084926060946040528339810103126100aa57610047816100c2565b906040610056602083016100c2565b9101519160058310156100aa5760805260a05260c05260405161059690816100d8823960805181818161012c015281816101d7015261036c015260a0518161042b015260c051818181608301526102bd0152f35b5f80fd5b634e487b7160e01b5f52604160045260245ffd5b51906001600160e01b0319821682036100aa5756fe6080806040526004361015610012575f80fd5b5f3560e01c90816301ffc9a71461045b57508063bc197c81146102335763f23a6e611461003d575f80fd5b3461022f5760a036600319011261022f57610056610491565b61005e6104a7565b60843567ffffffffffffffff811161022f5761007e9036906004016104ee565b9290927f0000000000000000000000000000000000000000000000000000000000000000600581101561021b57600181036100b7575f80fd5b600281036101165760405162461bcd60e51b815260206004820152602960248201527f4552433131353552656365697665724d6f636b3a20726576657274696e67206f6044820152686e207265636569766560b81b6064820152608490fd5b6003810361015d576301990d6f60e61b5f9081527f00000000000000000000000000000000000000000000000000000000000000006001600160e01b031916600452602490fd5b600414610207576101c97f20dfa9f79060c8c4d7fe892c97c71bcf6e3b63d1dcf66fea7aefc0211628cf29945a9260405195869560018060a01b0316865260018060a01b031660208601526044356040860152606435606086015260c0608086015260c0850191610540565b9060a08301520390a16040517f00000000000000000000000000000000000000000000000000000000000000006001600160e01b0319168152602090f35b634e487b7160e01b5f52601260045260245ffd5b634e487b7160e01b5f52602160045260245ffd5b5f80fd5b3461022f5760a036600319011261022f5761024c610491565b6102546104a7565b60443567ffffffffffffffff811161022f576102749036906004016104bd565b60649391933567ffffffffffffffff811161022f576102979036906004016104bd565b909460843567ffffffffffffffff811161022f576102b99036906004016104ee565b90917f0000000000000000000000000000000000000000000000000000000000000000600581101561021b57600181036102f1575f80fd5b600281036103565760405162461bcd60e51b815260206004820152602f60248201527f4552433131353552656365697665724d6f636b3a20726576657274696e67206f60448201526e6e206261746368207265636569766560881b6064820152608490fd5b6003810361039d576301990d6f60e61b5f9081527f00000000000000000000000000000000000000000000000000000000000000006001600160e01b031916600452602490fd5b600414610207577f0bcad9224ba33b574e9c85298de2f44b4c80015a21aa5df474896444909863d89761041d9461040161040f935a986040519b8c9b60018060a01b03168c5260018060a01b031660208c015260c060408c015260c08b019161051c565b9188830360608a015261051c565b918583036080870152610540565b9060a08301520390a16040517f00000000000000000000000000000000000000000000000000000000000000006001600160e01b0319168152602090f35b3461022f57602036600319011261022f576004359063ffffffff60e01b821680920361022f576020916301ffc9a760e01b148152f35b600435906001600160a01b038216820361022f57565b602435906001600160a01b038216820361022f57565b9181601f8401121561022f5782359167ffffffffffffffff831161022f576020808501948460051b01011161022f57565b9181601f8401121561022f5782359167ffffffffffffffff831161022f576020838186019501011161022f57565b81835290916001600160fb1b03831161022f5760209260051b809284830137010190565b908060209392818452848401375f828201840152601f01601f191601019056fea2646970667358221220823673650484174e61eb587521eda8972de5bdd31e87e0e37544c7fcd3cebc9164736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, recRetval: bytes4, batRetval: bytes4, error: ERC1155ReceiverMock.RevertType, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#25)

        Args:
            recRetval: bytes4
            batRetval: bytes4
            error: enum ERC1155ReceiverMock.RevertType
        """
        ...

    @overload
    @classmethod
    def deploy(cls, recRetval: bytes4, batRetval: bytes4, error: ERC1155ReceiverMock.RevertType, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC1155ReceiverMock:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#25)

        Args:
            recRetval: bytes4
            batRetval: bytes4
            error: enum ERC1155ReceiverMock.RevertType
        """
        ...

    @overload
    @classmethod
    def deploy(cls, recRetval: bytes4, batRetval: bytes4, error: ERC1155ReceiverMock.RevertType, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#25)

        Args:
            recRetval: bytes4
            batRetval: bytes4
            error: enum ERC1155ReceiverMock.RevertType
        """
        ...

    @overload
    @classmethod
    def deploy(cls, recRetval: bytes4, batRetval: bytes4, error: ERC1155ReceiverMock.RevertType, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#25)

        Args:
            recRetval: bytes4
            batRetval: bytes4
            error: enum ERC1155ReceiverMock.RevertType
        """
        ...

    @overload
    @classmethod
    def deploy(cls, recRetval: bytes4, batRetval: bytes4, error: ERC1155ReceiverMock.RevertType, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC1155ReceiverMock]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#25)

        Args:
            recRetval: bytes4
            batRetval: bytes4
            error: enum ERC1155ReceiverMock.RevertType
        """
        ...

    @classmethod
    def deploy(cls, recRetval: bytes4, batRetval: bytes4, error: ERC1155ReceiverMock.RevertType, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC1155ReceiverMock, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC1155ReceiverMock]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#25)

        Args:
            recRetval: bytes4
            batRetval: bytes4
            error: enum ERC1155ReceiverMock.RevertType
        """
        return cls._deploy(request_type, [recRetval, batRetval, error], return_tx, ERC1155ReceiverMock, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    class RevertType(IntEnum):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#9)

        """
        None_ = 0
        RevertWithoutMessage = 1
        RevertWithMessage = 2
        RevertWithCustomError = 3
        Panic = 4


    @dataclasses.dataclass
    class CustomError(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#23)

        Attributes:
            param1 (bytes4): bytes4
        """
        _abi = {'inputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'name': 'CustomError', 'type': 'error'}
        original_name = 'CustomError'
        selector = bytes4(b'fC[\xc0')

        param1: bytes4 = dataclasses.field(metadata={"original_name": ""})


    @dataclasses.dataclass
    class Received:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#21)

        Attributes:
            operator (Address): address
            from_ (Address): address
            id (uint256): uint256
            value (uint256): uint256
            data (bytearray): bytes
            gas (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'indexed': False, 'internalType': 'uint256', 'name': 'gas', 'type': 'uint256'}], 'name': 'Received', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'Received'
        selector = bytes32(b' \xdf\xa9\xf7\x90`\xc8\xc4\xd7\xfe\x89,\x97\xc7\x1b\xcfn;c\xd1\xdc\xf6o\xeaz\xef\xc0!\x16(\xcf)')

        operator: Address
        from_: Address = dataclasses.field(metadata={"original_name": "from"})
        id: uint256
        value: uint256
        data: bytearray
        gas: uint256


    @dataclasses.dataclass
    class BatchReceived:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#22)

        Attributes:
            operator (Address): address
            from_ (Address): address
            ids (List[uint256]): uint256[]
            values (List[uint256]): uint256[]
            data (bytearray): bytes
            gas (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'ids', 'type': 'uint256[]'}, {'indexed': False, 'internalType': 'uint256[]', 'name': 'values', 'type': 'uint256[]'}, {'indexed': False, 'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'indexed': False, 'internalType': 'uint256', 'name': 'gas', 'type': 'uint256'}], 'name': 'BatchReceived', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'BatchReceived'
        selector = bytes32(b'\x0b\xca\xd9"K\xa3;WN\x9c\x85)\x8d\xe2\xf4KL\x80\x01Z!\xaa]\xf4t\x89dD\x90\x98c\xd8')

        operator: Address
        from_: Address = dataclasses.field(metadata={"original_name": "from"})
        ids: List[uint256]
        values: List[uint256]
        data: bytearray
        gas: uint256


    @overload
    def onERC1155Received(self, operator: Union[Account, Address], from__: Union[Account, Address], id: uint256, value_: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes4:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#31)

        Args:
            operator: address
            from__: address
            id: uint256
            value_: uint256
            data: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def onERC1155Received(self, operator: Union[Account, Address], from__: Union[Account, Address], id: uint256, value_: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#31)

        Args:
            operator: address
            from__: address
            id: uint256
            value_: uint256
            data: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def onERC1155Received(self, operator: Union[Account, Address], from__: Union[Account, Address], id: uint256, value_: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#31)

        Args:
            operator: address
            from__: address
            id: uint256
            value_: uint256
            data: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def onERC1155Received(self, operator: Union[Account, Address], from__: Union[Account, Address], id: uint256, value_: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes4]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#31)

        Args:
            operator: address
            from__: address
            id: uint256
            value_: uint256
            data: bytes
        Returns:
            bytes4
        """
        ...

    def onERC1155Received(self, operator: Union[Account, Address], from__: Union[Account, Address], id: uint256, value_: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes4, TransactionAbc[bytes4], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#31)

        Args:
            operator: address
            from__: address
            id: uint256
            value_: uint256
            data: bytes
        Returns:
            bytes4
        """
        return self._execute(self.chain, request_type, "f23a6e61", [operator, from__, id, value_, data], True if request_type == "tx" else False, bytes4, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def onERC1155BatchReceived(self, operator: Union[Account, Address], from__: Union[Account, Address], ids: List[uint256], values: List[uint256], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes4:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#53)

        Args:
            operator: address
            from__: address
            ids: uint256[]
            values: uint256[]
            data: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def onERC1155BatchReceived(self, operator: Union[Account, Address], from__: Union[Account, Address], ids: List[uint256], values: List[uint256], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#53)

        Args:
            operator: address
            from__: address
            ids: uint256[]
            values: uint256[]
            data: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def onERC1155BatchReceived(self, operator: Union[Account, Address], from__: Union[Account, Address], ids: List[uint256], values: List[uint256], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#53)

        Args:
            operator: address
            from__: address
            ids: uint256[]
            values: uint256[]
            data: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def onERC1155BatchReceived(self, operator: Union[Account, Address], from__: Union[Account, Address], ids: List[uint256], values: List[uint256], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes4]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#53)

        Args:
            operator: address
            from__: address
            ids: uint256[]
            values: uint256[]
            data: bytes
        Returns:
            bytes4
        """
        ...

    def onERC1155BatchReceived(self, operator: Union[Account, Address], from__: Union[Account, Address], ids: List[uint256], values: List[uint256], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes4, TransactionAbc[bytes4], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC1155ReceiverMock.sol#53)

        Args:
            operator: address
            from__: address
            ids: uint256[]
            values: uint256[]
            data: bytes
        Returns:
            bytes4
        """
        return self._execute(self.chain, request_type, "bc197c81", [operator, from__, ids, values, data], True if request_type == "tx" else False, bytes4, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC1155ReceiverMock.onERC1155Received.selector = bytes4(b'\xf2:na')
ERC1155ReceiverMock.onERC1155BatchReceived.selector = bytes4(b'\xbc\x19|\x81')
