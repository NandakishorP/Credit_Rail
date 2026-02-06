
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.proxy.Proxy import Proxy



class BeaconProxy(Proxy):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/beacon/BeaconProxy.sol#23)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'address', 'name': 'beacon', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'stateMutability': 'payable', 'type': 'constructor'}, b'\x99\x96\xb3\x15': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'AddressEmptyCode', 'type': 'error'}, b'd\xce\xd0\xec': {'inputs': [{'internalType': 'address', 'name': 'beacon', 'type': 'address'}], 'name': 'ERC1967InvalidBeacon', 'type': 'error'}, b'L\x9c\x8c\xe3': {'inputs': [{'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'ERC1967InvalidImplementation', 'type': 'error'}, b'\xb3\x98\x97\x9f': {'inputs': [], 'name': 'ERC1967NonPayable', 'type': 'error'}, b'\xd6\xbd\xa2u': {'inputs': [], 'name': 'FailedCall', 'type': 'error'}, b'\x1c\xf3\xb0:l\xf1\x9f\xa2\xba\xbaM\xf1H\xe9\xdc\xab\xed\xea\x7f\x8a\\\x07\x84\x0e ~\\\x08\x9b\xe9]>': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'beacon', 'type': 'address'}], 'name': 'BeaconUpgraded', 'type': 'event'}, 'fallback': {'stateMutability': 'payable', 'type': 'fallback'}}
    _storage_layout = {"storage":[]}
    _creation_code = "60a08060405261045880380380916100178285610271565b833981016040828203126101b45761002e82610294565b602083015190926001600160401b0382116101b4570181601f820112156101b4578051906001600160401b03821161025d5760405192610078601f8401601f191660200185610271565b828452602083830101116101b457815f9260208093018386015e83010152813b1561023c577fa3f0ad74e5423aebfd80d3ef4346578335a9a72aeaee59ff6cb3582b35133d5080546001600160a01b0319166001600160a01b038416908117909155604051635c60da1b60e01b8152909190602081600481865afa9081156101c0575f91610202575b50803b156101e25750817f1cf3b03a6cf19fa2baba4df148e9dcabedea7f8a5c07840e207e5c089be95d3e5f80a28051156101cb57602060049260405193848092635c60da1b60e01b82525afa80156101c0575f90610181575b61016592506102a8565b505b608052604051610123908161033582396080518160180152f35b506020823d6020116101b8575b8161019b60209383610271565b810103126101b4576101af61016592610294565b61015b565b5f80fd5b3d915061018e565b6040513d5f823e3d90fd5b505034156101675763b398979f60e01b5f5260045ffd5b634c9c8ce360e01b5f9081526001600160a01b0391909116600452602490fd5b90506020813d602011610234575b8161021d60209383610271565b810103126101b45761022e90610294565b5f610101565b3d9150610210565b50631933b43b60e21b5f9081526001600160a01b0391909116600452602490fd5b634e487b7160e01b5f52604160045260245ffd5b601f909101601f19168101906001600160401b0382119082101761025d57604052565b51906001600160a01b03821682036101b457565b905f8091602081519101845af48080610321575b156102dc5750506040513d81523d5f602083013e60203d82010160405290565b1561030157639996b31560e01b5f9081526001600160a01b0391909116600452602490fd5b3d15610312576040513d5f823e3d90fd5b63d6bda27560e01b5f5260045ffd5b503d1515806102bc5750813b15156102bc56fe60806040819052635c60da1b60e01b81526020906004817f00000000000000000000000000000000000000000000000000000000000000006001600160a01b03165afa801560a2575f901560d1575060203d602011609c575b601f19601f820116608001906080821067ffffffffffffffff83111760885760849160405260800160ad565b60d1565b634e487b7160e01b5f52604160045260245ffd5b503d6058565b6040513d5f823e3d90fd5b602090607f19011260cd576080516001600160a01b038116810360cd5790565b5f80fd5b5f8091368280378136915af43d5f803e1560e9573d5ff35b3d5ffdfea26469706673582212209a98c63e38da8350cdaec87df443fcc99b0bd3e4291f4e68834a3d4d46149b8164736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, beacon: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/beacon/BeaconProxy.sol#39)

        Args:
            beacon: address
            data: bytes
        """
        ...

    @overload
    @classmethod
    def deploy(cls, beacon: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> BeaconProxy:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/beacon/BeaconProxy.sol#39)

        Args:
            beacon: address
            data: bytes
        """
        ...

    @overload
    @classmethod
    def deploy(cls, beacon: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/beacon/BeaconProxy.sol#39)

        Args:
            beacon: address
            data: bytes
        """
        ...

    @overload
    @classmethod
    def deploy(cls, beacon: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/beacon/BeaconProxy.sol#39)

        Args:
            beacon: address
            data: bytes
        """
        ...

    @overload
    @classmethod
    def deploy(cls, beacon: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[BeaconProxy]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/beacon/BeaconProxy.sol#39)

        Args:
            beacon: address
            data: bytes
        """
        ...

    @classmethod
    def deploy(cls, beacon: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, BeaconProxy, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[BeaconProxy]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/beacon/BeaconProxy.sol#39)

        Args:
            beacon: address
            data: bytes
        """
        return cls._deploy(request_type, [beacon, data], return_tx, BeaconProxy, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

