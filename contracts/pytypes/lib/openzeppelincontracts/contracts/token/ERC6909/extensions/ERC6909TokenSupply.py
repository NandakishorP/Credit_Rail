
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.interfaces.IERC6909 import IERC6909TokenSupply
from pytypes.lib.openzeppelincontracts.contracts.token.ERC6909.ERC6909 import ERC6909



class ERC6909TokenSupply(IERC6909TokenSupply, ERC6909):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909TokenSupply.sol#13)
    """
    _abi = {b'X\xa3\xfdZ': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'allowance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'ERC6909InsufficientAllowance', 'type': 'error'}, b'\xb1\xb4\xfe\xc0': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'ERC6909InsufficientBalance', 'type': 'error'}, b'\xccvj\x98': {'inputs': [{'internalType': 'address', 'name': 'approver', 'type': 'address'}], 'name': 'ERC6909InvalidApprover', 'type': 'error'}, b'\xb8\xbb\xd6\x10': {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'ERC6909InvalidReceiver', 'type': 'error'}, b'\xa45 \x80': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'ERC6909InvalidSender', 'type': 'error'}, b'oe\xf4e': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'ERC6909InvalidSpender', 'type': 'error'}, b'\xb3\xfdPq\x83X\x87Vz\x06q\x15\x11!\x89M\xdc\xcc(B\xf1\xd1\x0b\xed\xad\x13\xe0\xd1|\xac\xe9\xa7': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, b'\xce\xb5v\xd9\xf1^N \x0f\xdbP\x96\xd6M]\xfdf~\x16\xde\xf2\x0c\x1e\xef\xd1BV\xd8\xe3\xfa\xa2g': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'OperatorSet', 'type': 'event'}, b'\x1b=~\xdb.\x9c\x0b\x0e|R[ \xaa\xae\xf0\xf5\x94\r.\xd7\x16c\xc7\xd3\x92f\xec\xaf\xacr\x88Y': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, b'Y\x8a\xf9\xe7': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'Bj\x84\x93': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x00\xfd\xd5\x8e': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb66<\xf2': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'isOperator', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'U\x8ar\x97': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'setOperator', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x01\xff\xc9\xa7': {'inputs': [{'internalType': 'bytes4', 'name': 'interfaceId', 'type': 'bytes4'}], 'name': 'supportsInterface', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbd\x85\xb09': {'inputs': [{'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\t[\xcd\xb6': {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfe\x99\x04\x9a': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":200,"contract":"lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909TokenSupply.sol:ERC6909TokenSupply","label":"_balances","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_uint256,t_uint256))"},{"astId":206,"contract":"lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909TokenSupply.sol:ERC6909TokenSupply","label":"_operatorApprovals","offset":0,"slot":1,"type":"t_mapping(t_address,t_mapping(t_address,t_bool))"},{"astId":214,"contract":"lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909TokenSupply.sol:ERC6909TokenSupply","label":"_allowances","offset":0,"slot":2,"type":"t_mapping(t_address,t_mapping(t_address,t_mapping(t_uint256,t_uint256)))"},{"astId":838,"contract":"lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909TokenSupply.sol:ERC6909TokenSupply","label":"_totalSupplies","offset":0,"slot":3,"type":"t_mapping(t_uint256,t_uint256)"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_mapping(t_address,t_bool)":{"encoding":"mapping","label":"mapping(address => bool)","numberOfBytes":32,"key":"t_address","value":"t_bool"},"t_mapping(t_address,t_mapping(t_address,t_bool))":{"encoding":"mapping","label":"mapping(address => mapping(address => bool))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_address,t_bool)"},"t_mapping(t_address,t_mapping(t_address,t_mapping(t_uint256,t_uint256)))":{"encoding":"mapping","label":"mapping(address => mapping(address => mapping(uint256 => uint256)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_address,t_mapping(t_uint256,t_uint256))"},"t_mapping(t_address,t_mapping(t_uint256,t_uint256))":{"encoding":"mapping","label":"mapping(address => mapping(uint256 => uint256))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_uint256,t_uint256)"},"t_mapping(t_uint256,t_uint256)":{"encoding":"mapping","label":"mapping(uint256 => uint256)","numberOfBytes":32,"key":"t_uint256","value":"t_uint256"},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "6080806040523460155761060a908161001a8239f35b5f80fdfe6080806040526004361015610012575f80fd5b5f3560e01c908162fdd58e1461041c5750806301ffc9a7146103c6578063095bcdb6146103ae578063426a84931461032f578063558a729714610272578063598af9e714610218578063b6363cf2146101c1578063bd85b039146101975763fe99049a1461007e575f80fd5b346101935760803660031901126101935761009761045a565b61009f610470565b6001600160a01b0382169160643591604435913385141580610170575b6100d6575b6100cb94506104b0565b602060405160018152f35b5f85815260026020908152604080832033845282528083208684529091529020545f198110610106575b506100c1565b8481106101425784906100cb965f52600260205260405f2060018060a01b0333165f5260205260405f20855f526020520360405f20555f610100565b604051632c51fead60e11b815233600482015260248101919091526044810185905260648101849052608490fd5b505f85815260016020908152604080832033845290915290205460ff16156100bc565b5f80fd5b34610193576020366003190112610193576004355f526003602052602060405f2054604051908152f35b34610193576040366003190112610193576101da61045a565b6101e2610470565b9060018060a01b03165f52600160205260405f209060018060a01b03165f52602052602060ff60405f2054166040519015158152f35b346101935760603660031901126101935761023161045a565b610239610470565b6001600160a01b039182165f90815260026020908152604080832094909316825292835281812060443582528352819020549051908152f35b346101935760403660031901126101935761028b61045a565b6024359081151580920361019357331561031c576001600160a01b031690811561030957335f52600160205260405f20825f5260205260405f2060ff1981541660ff83161790556040519081527fceb576d9f15e4e200fdb5096d64d5dfd667e16def20c1eefd14256d8e3faa26760203392a3602060405160018152f35b636f65f46560e01b5f525f60045260245ffd5b63198ecd5360e31b5f525f60045260245ffd5b346101935761033d36610486565b9091331561031c576001600160a01b031690811561030957335f52600260205260405f20825f5260205260405f20835f526020528060405f20556040519081527fb3fd5071835887567a0671151121894ddccc2842f1d10bedad13e0d17cace9a760203392a4602060405160018152f35b34610193576100cb6103bf36610486565b91336104b0565b346101935760203660031901126101935760043563ffffffff60e01b811680910361019357602090630f632fb360e01b811490811561040b575b506040519015158152f35b6301ffc9a760e01b14905082610400565b34610193576040366003190112610193576020906001600160a01b0361044061045a565b165f525f825260405f206024355f52825260405f20548152f35b600435906001600160a01b038216820361019357565b602435906001600160a01b038216820361019357565b6060906003190112610193576004356001600160a01b038116810361019357906024359060443590565b91926001600160a01b0383169182156105c1576001600160a01b03169283156105ae57825f525f60205260405f20855f5260205260405f20549082821061057557508190835f525f60205260405f20865f526020520360405f2055825f525f60205260405f20845f5260205260405f20805491808301809311610561577f1b3d7edb2e9c0b0e7c525b20aaaef0f5940d2ed71663c7d39266ecafac72885992604092558151903382526020820152a4565b634e487b7160e01b5f52601160045260245ffd5b6040516302c6d3fb60e61b81526001600160a01b0391909116600482015260248101919091526044810182905260648101859052608490fd5b630b8bbd6160e41b5f525f60045260245ffd5b6301486a4160e71b5f525f60045260245ffdfea2646970667358221220c014dfe8c4b42d5b9e4f1bbcda2194b054ff88d8e1fd29ac750c0dc762e6abea64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC6909TokenSupply:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC6909TokenSupply]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC6909TokenSupply, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC6909TokenSupply]]:
        return cls._deploy(request_type, [], return_tx, ERC6909TokenSupply, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def totalSupply(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909TokenSupply.sol#17)

        Args:
            id: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def totalSupply(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909TokenSupply.sol#17)

        Args:
            id: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def totalSupply(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909TokenSupply.sol#17)

        Args:
            id: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def totalSupply(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909TokenSupply.sol#17)

        Args:
            id: uint256
        Returns:
            uint256
        """
        ...

    def totalSupply(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909TokenSupply.sol#17)

        Args:
            id: uint256
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "bd85b039", [id], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC6909TokenSupply.totalSupply.selector = bytes4(b'\xbd\x85\xb09')
