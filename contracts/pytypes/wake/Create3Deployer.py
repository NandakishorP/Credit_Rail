
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class Create3Deployer(Contract):
    """
    [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/Create3Deployer.sol#6)
    """
    _abi = {b'S\xdeT\xb9': {'inputs': [], 'name': 'ErrorCreatingContract', 'type': 'error'}, b'\xbb\xd2\xfe\x87': {'inputs': [], 'name': 'ErrorCreatingProxy', 'type': 'error'}, b'\xcdC\xef\xa1': {'inputs': [], 'name': 'TargetAlreadyExists', 'type': 'error'}, b'\x7f\xdeV\xda': {'inputs': [{'internalType': 'bytes32', 'name': '_salt', 'type': 'bytes32'}], 'name': 'computeAddress', 'outputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xcd\xcbv\n': {'inputs': [{'internalType': 'bytes32', 'name': '_salt', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': '_creationCode', 'type': 'bytes'}], 'name': 'deploy', 'outputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x99\x95BR': {'inputs': [{'internalType': 'bytes32', 'name': '_salt', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': '_creationCode', 'type': 'bytes'}, {'internalType': 'uint256', 'name': '_value', 'type': 'uint256'}], 'name': 'deployWithValue', 'outputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = "608080604052346015576103b1908161001a8239f35b5f80fdfe60806040526004361015610011575f80fd5b5f3560e01c80637fde56da14610119578063999542521461003f5763cdcb760a1461003a575f80fd5b6101e6565b346101155760603660031901126101155760043560243567ffffffffffffffff8111610115576100739036906004016101a0565b61007b61031e565b9161008581610261565b92833b610106576020815191015ff56001600160a01b038116156100f757815f92916020849351920190604435905af16100bd61034c565b501580156100ee575b6100df576040516001600160a01b039091168152602090f35b6353de54b960e01b5f5260045ffd5b50803b156100c6565b63bbd2fe8760e01b5f5260045ffd5b63cd43efa160e01b5f5260045ffd5b5f80fd5b34610115576020366003190112610115576020610137600435610261565b6040516001600160a01b039091168152f35b634e487b7160e01b5f52604160045260245ffd5b90601f8019910116810190811067ffffffffffffffff82111761017f57604052565b610149565b67ffffffffffffffff811161017f57601f01601f191660200190565b81601f82011215610115578035906101b782610184565b926101c5604051948561015d565b8284526020838301011161011557815f926020809301838601378301015290565b346101155760403660031901126101155760043560243567ffffffffffffffff81116101155761021a9036906004016101a0565b61022261031e565b9161022c81610261565b92833b610106576020815191015ff56001600160a01b038116156100f757815f92918360208194519301915af16100bd61034c565b61030f61031b91604051602081019160ff60f81b83523060601b602183015260358201527f21c35dbe1b344a2488cf3321d6ce542f8e9f305544ff09e4993a62319a497c1f6055820152605581526102ba60758261015d565b5190206040516135a560f21b6020820190815260609290921b6bffffffffffffffffffffffff19166022820152600160f81b60368201526017815261030060378261015d565b5190206001600160a01b031690565b6001600160a01b031690565b90565b6040519061032d60408361015d565b601082526f67363d3d37363d34f03d5260086018f360801b6020830152565b3d15610376573d9061035d82610184565b9161036b604051938461015d565b82523d5f602084013e565b60609056fea26469706673582212200e6d8e1354d2c92703cd43be206117d029b3d47de2908e5b2a765eabe480514a64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Create3Deployer:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Create3Deployer]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, Create3Deployer, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[Create3Deployer]]:
        return cls._deploy(request_type, [], return_tx, Create3Deployer, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def deploy_(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/Create3Deployer.sol#7)

        Args:
            _salt: bytes32
            _creationCode: bytes
        Returns:
            addr: address
        """
        ...

    @overload
    def deploy_(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/Create3Deployer.sol#7)

        Args:
            _salt: bytes32
            _creationCode: bytes
        Returns:
            addr: address
        """
        ...

    @overload
    def deploy_(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/Create3Deployer.sol#7)

        Args:
            _salt: bytes32
            _creationCode: bytes
        Returns:
            addr: address
        """
        ...

    @overload
    def deploy_(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/Create3Deployer.sol#7)

        Args:
            _salt: bytes32
            _creationCode: bytes
        Returns:
            addr: address
        """
        ...

    def deploy_(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/Create3Deployer.sol#7)

        Args:
            _salt: bytes32
            _creationCode: bytes
        Returns:
            addr: address
        """
        return self._execute(self.chain, request_type, "cdcb760a", [_salt, _creationCode], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deployWithValue(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], _value: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/Create3Deployer.sol#11)

        Args:
            _salt: bytes32
            _creationCode: bytes
            _value: uint256
        Returns:
            addr: address
        """
        ...

    @overload
    def deployWithValue(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], _value: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/Create3Deployer.sol#11)

        Args:
            _salt: bytes32
            _creationCode: bytes
            _value: uint256
        Returns:
            addr: address
        """
        ...

    @overload
    def deployWithValue(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], _value: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/Create3Deployer.sol#11)

        Args:
            _salt: bytes32
            _creationCode: bytes
            _value: uint256
        Returns:
            addr: address
        """
        ...

    @overload
    def deployWithValue(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], _value: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/Create3Deployer.sol#11)

        Args:
            _salt: bytes32
            _creationCode: bytes
            _value: uint256
        Returns:
            addr: address
        """
        ...

    def deployWithValue(self, _salt: bytes32, _creationCode: Union[bytearray, bytes], _value: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/Create3Deployer.sol#11)

        Args:
            _salt: bytes32
            _creationCode: bytes
            _value: uint256
        Returns:
            addr: address
        """
        return self._execute(self.chain, request_type, "99954252", [_salt, _creationCode, _value], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def computeAddress(self, _salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/Create3Deployer.sol#15)

        Args:
            _salt: bytes32
        Returns:
            addr: address
        """
        ...

    @overload
    def computeAddress(self, _salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/Create3Deployer.sol#15)

        Args:
            _salt: bytes32
        Returns:
            addr: address
        """
        ...

    @overload
    def computeAddress(self, _salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/Create3Deployer.sol#15)

        Args:
            _salt: bytes32
        Returns:
            addr: address
        """
        ...

    @overload
    def computeAddress(self, _salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/Create3Deployer.sol#15)

        Args:
            _salt: bytes32
        Returns:
            addr: address
        """
        ...

    def computeAddress(self, _salt: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///opt/homebrew/lib/python3.13/site-packages/contracts/wake/Create3Deployer.sol#15)

        Args:
            _salt: bytes32
        Returns:
            addr: address
        """
        return self._execute(self.chain, request_type, "7fde56da", [_salt], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

Create3Deployer.deploy_.selector = bytes4(b'\xcd\xcbv\n')
Create3Deployer.deployWithValue.selector = bytes4(b'\x99\x95BR')
Create3Deployer.computeAddress.selector = bytes4(b'\x7f\xdeV\xda')
