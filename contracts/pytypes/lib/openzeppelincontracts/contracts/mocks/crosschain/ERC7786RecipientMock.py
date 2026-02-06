
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.crosschain.ERC7786Recipient import ERC7786Recipient



class ERC7786RecipientMock(ERC7786Recipient):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/crosschain/ERC7786RecipientMock.sol#7)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'address', 'name': 'gateway_', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'R\xbc0Q': {'inputs': [{'internalType': 'address', 'name': 'gateway', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'receiveId', 'type': 'bytes32'}], 'name': 'ERC7786RecipientMessageAlreadyProcessed', 'type': 'error'}, b'\xcd\xde\xa77': {'inputs': [{'internalType': 'address', 'name': 'gateway', 'type': 'address'}, {'internalType': 'bytes', 'name': 'sender', 'type': 'bytes'}], 'name': 'ERC7786RecipientUnauthorizedGateway', 'type': 'error'}, b'd\x81(N\x17\xcb^(\x0c\xd7\x9e\xdd{C\xc0\xbe\xa1\xc6\x93\x98M\xee[\x1d\x91\x99W\x98\x84\xfa\rN': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'gateway', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'receiveId', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'bytes', 'name': 'sender', 'type': 'bytes'}, {'indexed': False, 'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'MessageReceived', 'type': 'event'}, b'$2\xef&': {'inputs': [{'internalType': 'bytes32', 'name': 'receiveId', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'sender', 'type': 'bytes'}, {'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}], 'name': 'receiveMessage', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'payable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":17,"contract":"lib/openzeppelin-contracts/contracts/mocks/crosschain/ERC7786RecipientMock.sol:ERC7786RecipientMock","label":"_received","offset":0,"slot":0,"type":"t_mapping(t_address,t_struct(BitMap)256_storage)"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_mapping(t_address,t_struct(BitMap)256_storage)":{"encoding":"mapping","label":"mapping(address => struct BitMaps.BitMap)","numberOfBytes":32,"key":"t_address","value":"t_struct(BitMap)256_storage"},"t_mapping(t_uint256,t_uint256)":{"encoding":"mapping","label":"mapping(uint256 => uint256)","numberOfBytes":32,"key":"t_uint256","value":"t_uint256"},"t_struct(BitMap)256_storage":{"encoding":"inplace","label":"struct BitMaps.BitMap","numberOfBytes":32,"members":[{"astId":255,"contract":"lib/openzeppelin-contracts/contracts/mocks/crosschain/ERC7786RecipientMock.sol:ERC7786RecipientMock","label":"_data","offset":0,"slot":0,"type":"t_mapping(t_uint256,t_uint256)"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60a034606557601f6102ad38819003918201601f19168301916001600160401b03831184841017606957808492602094604052833981010312606557516001600160a01b038116810360655760805260405161022f908161007e823960805181607e0152f35b5f80fd5b634e487b7160e01b5f52604160045260245ffdfe6080806040526004361015610012575f80fd5b5f3560e01c632432ef2614610025575f80fd5b60603660031901126101a7576004359060243567ffffffffffffffff81116101a7576100559036906004016101ab565b919060443567ffffffffffffffff81116101a7576100779036906004016101ab565b90929091907f00000000000000000000000000000000000000000000000000000000000000006001600160a01b0316330361017c5750335f525f60205260405f208560081c600160ff88161b91815f526020528160405f205416610165577f6481284e17cb5e280cd79edd7b43c0bea1c693984dee5b1d9199579884fa0d4e96949261014a949261013c92335f525f60205260405f20905f5260205260405f20908154179055604051968796338852602088015260a0604088015260a08701916101d9565b9184830360608601526101d9565b3460808301520390a1604051631219779360e11b8152602090f35b866352bc305160e01b5f523360045260245260445ffd5b6101a381928663cddea73760e01b84523360048501526040602485015260448401916101d9565b0390fd5b5f80fd5b9181601f840112156101a75782359167ffffffffffffffff83116101a757602083818601950101116101a757565b908060209392818452848401375f828201840152601f01601f191601019056fea2646970667358221220dee9e4e9f39612a62ef96225cd932a00ecfde337cd3127c151f87dae06bab16764736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, gateway_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/crosschain/ERC7786RecipientMock.sol#12)

        Args:
            gateway_: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, gateway_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC7786RecipientMock:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/crosschain/ERC7786RecipientMock.sol#12)

        Args:
            gateway_: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, gateway_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/crosschain/ERC7786RecipientMock.sol#12)

        Args:
            gateway_: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, gateway_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/crosschain/ERC7786RecipientMock.sol#12)

        Args:
            gateway_: address
        """
        ...

    @overload
    @classmethod
    def deploy(cls, gateway_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC7786RecipientMock]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/crosschain/ERC7786RecipientMock.sol#12)

        Args:
            gateway_: address
        """
        ...

    @classmethod
    def deploy(cls, gateway_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC7786RecipientMock, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC7786RecipientMock]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/crosschain/ERC7786RecipientMock.sol#12)

        Args:
            gateway_: address
        """
        return cls._deploy(request_type, [gateway_], return_tx, ERC7786RecipientMock, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class MessageReceived:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/crosschain/ERC7786RecipientMock.sol#10)

        Attributes:
            gateway (Address): address
            receiveId (bytes32): bytes32
            sender (bytearray): bytes
            payload (bytearray): bytes
            value (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'gateway', 'type': 'address'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'receiveId', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'bytes', 'name': 'sender', 'type': 'bytes'}, {'indexed': False, 'internalType': 'bytes', 'name': 'payload', 'type': 'bytes'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'MessageReceived', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'MessageReceived'
        selector = bytes32(b'd\x81(N\x17\xcb^(\x0c\xd7\x9e\xdd{C\xc0\xbe\xa1\xc6\x93\x98M\xee[\x1d\x91\x99W\x98\x84\xfa\rN')

        gateway: Address
        receiveId: bytes32
        sender: bytearray
        payload: bytearray
        value: uint256


