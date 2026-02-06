
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.token.ERC721.IERC721Receiver import IERC721Receiver



class ERC721ReceiverMock(IERC721Receiver):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC721ReceiverMock.sol#7)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'bytes4', 'name': 'retval', 'type': 'bytes4'}, {'internalType': 'enum ERC721ReceiverMock.RevertType', 'name': 'error', 'type': 'uint8'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'fC[\xc0': {'inputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'name': 'CustomError', 'type': 'error'}, b'(\xfan\x16E\x8f\x9c$\xaaY\xdd\xd4\x08RdW0\x06\xdb\xe3\x03\x04\x83xs\xc7\xde\xaf\xc7\x02\xb08': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'indexed': False, 'internalType': 'uint256', 'name': 'gas', 'type': 'uint256'}], 'name': 'Received', 'type': 'event'}, b'\x15\x0bz\x02': {'inputs': [{'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'onERC721Received', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = "60c03461008c57601f61036738819003918201601f19168301916001600160401b0383118484101761009057808492604094855283398101031261008c578051906001600160e01b03198216820361008c576020015190600582101561008c5760805260a0526040516102c290816100a58239608051818181610176015261021c015260a0518160df0152f35b5f80fd5b634e487b7160e01b5f52604160045260245ffdfe6080806040526004361015610012575f80fd5b5f3560e01c63150b7a0214610025575f80fd5b34610274576080366003190112610274576004356001600160a01b0381169190829003610274576024356001600160a01b0381169190829003610274576064359267ffffffffffffffff8411610274573660238501121561027457836004013567ffffffffffffffff811161027857601f8101601f19908116603f0116830167ffffffffffffffff811184821017610278576040528083526020830194366024838301011161027457815f926024602093018837840101527f000000000000000000000000000000000000000000000000000000000000000060058110156102605760018103610113575f80fd5b600281036101605760405162461bcd60e51b815260206004820152601d60248201527f45524337323152656365697665724d6f636b3a20726576657274696e670000006044820152606490fd5b600381036101a7576301990d6f60e61b5f9081527f00000000000000000000000000000000000000000000000000000000000000006001600160e01b031916600452602490fd5b60041461024c577f28fa6e16458f9c24aa59ddd4085264573006dbe30304837873c7deafc702b0389360c0925a9060405195869485526020850152604435604085015260a060608501525180928160a08601528585015e5f8383018501526080830152601f01601f19168101030190a16040517f00000000000000000000000000000000000000000000000000000000000000006001600160e01b0319168152602090f35b634e487b7160e01b5f52601260045260245ffd5b634e487b7160e01b5f52602160045260245ffd5b5f80fd5b634e487b7160e01b5f52604160045260245ffdfea2646970667358221220ebf69b6716a943dac94cf9cc99c24e2425649ddc63620fc3e43d8df72942e17264736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, retval: bytes4, error: ERC721ReceiverMock.RevertType, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC721ReceiverMock.sol#22)

        Args:
            retval: bytes4
            error: enum ERC721ReceiverMock.RevertType
        """
        ...

    @overload
    @classmethod
    def deploy(cls, retval: bytes4, error: ERC721ReceiverMock.RevertType, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC721ReceiverMock:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC721ReceiverMock.sol#22)

        Args:
            retval: bytes4
            error: enum ERC721ReceiverMock.RevertType
        """
        ...

    @overload
    @classmethod
    def deploy(cls, retval: bytes4, error: ERC721ReceiverMock.RevertType, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC721ReceiverMock.sol#22)

        Args:
            retval: bytes4
            error: enum ERC721ReceiverMock.RevertType
        """
        ...

    @overload
    @classmethod
    def deploy(cls, retval: bytes4, error: ERC721ReceiverMock.RevertType, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC721ReceiverMock.sol#22)

        Args:
            retval: bytes4
            error: enum ERC721ReceiverMock.RevertType
        """
        ...

    @overload
    @classmethod
    def deploy(cls, retval: bytes4, error: ERC721ReceiverMock.RevertType, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC721ReceiverMock]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC721ReceiverMock.sol#22)

        Args:
            retval: bytes4
            error: enum ERC721ReceiverMock.RevertType
        """
        ...

    @classmethod
    def deploy(cls, retval: bytes4, error: ERC721ReceiverMock.RevertType, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC721ReceiverMock, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC721ReceiverMock]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC721ReceiverMock.sol#22)

        Args:
            retval: bytes4
            error: enum ERC721ReceiverMock.RevertType
        """
        return cls._deploy(request_type, [retval, error], return_tx, ERC721ReceiverMock, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    class RevertType(IntEnum):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC721ReceiverMock.sol#8)

        """
        None_ = 0
        RevertWithoutMessage = 1
        RevertWithMessage = 2
        RevertWithCustomError = 3
        Panic = 4


    @dataclasses.dataclass
    class CustomError(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC721ReceiverMock.sol#20)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC721ReceiverMock.sol#19)

        Attributes:
            operator (Address): address
            from_ (Address): address
            tokenId (uint256): uint256
            data (bytearray): bytes
            gas (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'operator', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'tokenId', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'indexed': False, 'internalType': 'uint256', 'name': 'gas', 'type': 'uint256'}], 'name': 'Received', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'Received'
        selector = bytes32(b'(\xfan\x16E\x8f\x9c$\xaaY\xdd\xd4\x08RdW0\x06\xdb\xe3\x03\x04\x83xs\xc7\xde\xaf\xc7\x02\xb08')

        operator: Address
        from_: Address = dataclasses.field(metadata={"original_name": "from"})
        tokenId: uint256
        data: bytearray
        gas: uint256


    @overload
    def onERC721Received(self, operator: Union[Account, Address], from__: Union[Account, Address], tokenId: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes4:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC721ReceiverMock.sol#27)

        Args:
            operator: address
            from__: address
            tokenId: uint256
            data: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def onERC721Received(self, operator: Union[Account, Address], from__: Union[Account, Address], tokenId: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC721ReceiverMock.sol#27)

        Args:
            operator: address
            from__: address
            tokenId: uint256
            data: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def onERC721Received(self, operator: Union[Account, Address], from__: Union[Account, Address], tokenId: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC721ReceiverMock.sol#27)

        Args:
            operator: address
            from__: address
            tokenId: uint256
            data: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def onERC721Received(self, operator: Union[Account, Address], from__: Union[Account, Address], tokenId: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes4]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC721ReceiverMock.sol#27)

        Args:
            operator: address
            from__: address
            tokenId: uint256
            data: bytes
        Returns:
            bytes4
        """
        ...

    def onERC721Received(self, operator: Union[Account, Address], from__: Union[Account, Address], tokenId: uint256, data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes4, TransactionAbc[bytes4], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC721ReceiverMock.sol#27)

        Args:
            operator: address
            from__: address
            tokenId: uint256
            data: bytes
        Returns:
            bytes4
        """
        return self._execute(self.chain, request_type, "150b7a02", [operator, from__, tokenId, data], True if request_type == "tx" else False, bytes4, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC721ReceiverMock.onERC721Received.selector = bytes4(b'\x15\x0bz\x02')
