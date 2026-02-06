
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.proxy.Proxy import Proxy



class ERC1967Proxy(Proxy):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/ERC1967/ERC1967Proxy.sol#15)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'address', 'name': 'implementation', 'type': 'address'}, {'internalType': 'bytes', 'name': '_data', 'type': 'bytes'}], 'stateMutability': 'payable', 'type': 'constructor'}, b'\x99\x96\xb3\x15': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'AddressEmptyCode', 'type': 'error'}, b'L\x9c\x8c\xe3': {'inputs': [{'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'ERC1967InvalidImplementation', 'type': 'error'}, b'\xb3\x98\x97\x9f': {'inputs': [], 'name': 'ERC1967NonPayable', 'type': 'error'}, b'\xd6\xbd\xa2u': {'inputs': [], 'name': 'FailedCall', 'type': 'error'}, b'\xbc|\xd7Z \xee\'\xfd\x9a\xde\xba\xb3 A\xf7U!M\xbck\xff\xa9\x0c\xc0"[9\xda.\\-;': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'Upgraded', 'type': 'event'}, 'fallback': {'stateMutability': 'payable', 'type': 'fallback'}}
    _storage_layout = {"storage":[]}
    _creation_code = "608060405261028c8038038061001481610158565b9283398101604082820312610140578151916001600160a01b03831690818403610140576020810151906001600160401b038211610140570182601f82011215610140578051906001600160401b0382116101445761007c601f8301601f1916602001610158565b938285526020838301011161014057815f9260208093018387015e84010152823b1561012e577f360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc80546001600160a01b031916821790557fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b5f80a2805115610117576101079161017d565b505b6040516082908161020a8239f35b505034156101095763b398979f60e01b5f5260045ffd5b634c9c8ce360e01b5f5260045260245ffd5b5f80fd5b634e487b7160e01b5f52604160045260245ffd5b6040519190601f01601f191682016001600160401b0381118382101761014457604052565b905f8091602081519101845af480806101f6575b156101b15750506040513d81523d5f602083013e60203d82010160405290565b156101d657639996b31560e01b5f9081526001600160a01b0391909116600452602490fd5b3d156101e7576040513d5f823e3d90fd5b63d6bda27560e01b5f5260045ffd5b503d1515806101915750813b151561019156fe60806040527f360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc545f9081906001600160a01b0316368280378136915af43d5f803e156048573d5ff35b3d5ffdfea2646970667358221220841260dce6872ae9f1c28b38fbc6c278de41eabca9db74dbe18598484bfe469f64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, implementation: Union[Account, Address], _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/ERC1967/ERC1967Proxy.sol#26)

        Args:
            implementation: address
            _data: bytes
        """
        ...

    @overload
    @classmethod
    def deploy(cls, implementation: Union[Account, Address], _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC1967Proxy:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/ERC1967/ERC1967Proxy.sol#26)

        Args:
            implementation: address
            _data: bytes
        """
        ...

    @overload
    @classmethod
    def deploy(cls, implementation: Union[Account, Address], _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/ERC1967/ERC1967Proxy.sol#26)

        Args:
            implementation: address
            _data: bytes
        """
        ...

    @overload
    @classmethod
    def deploy(cls, implementation: Union[Account, Address], _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/ERC1967/ERC1967Proxy.sol#26)

        Args:
            implementation: address
            _data: bytes
        """
        ...

    @overload
    @classmethod
    def deploy(cls, implementation: Union[Account, Address], _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC1967Proxy]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/ERC1967/ERC1967Proxy.sol#26)

        Args:
            implementation: address
            _data: bytes
        """
        ...

    @classmethod
    def deploy(cls, implementation: Union[Account, Address], _data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC1967Proxy, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC1967Proxy]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/proxy/ERC1967/ERC1967Proxy.sol#26)

        Args:
            implementation: address
            _data: bytes
        """
        return cls._deploy(request_type, [implementation, _data], return_tx, ERC1967Proxy, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

