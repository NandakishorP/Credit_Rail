
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.interfaces.IERC6909 import IERC6909ContentURI
from pytypes.lib.openzeppelincontracts.contracts.token.ERC6909.ERC6909 import ERC6909



class ERC6909ContentURI(IERC6909ContentURI, ERC6909):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909ContentURI.sol#12)
    """
    _abi = {b'X\xa3\xfdZ': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'allowance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'ERC6909InsufficientAllowance', 'type': 'error'}, b'\xb1\xb4\xfe\xc0': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'ERC6909InsufficientBalance', 'type': 'error'}, b'\xccvj\x98': {'inputs': [{'internalType': 'address', 'name': 'approver', 'type': 'address'}], 'name': 'ERC6909InvalidApprover', 'type': 'error'}, b'\xb8\xbb\xd6\x10': {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'ERC6909InvalidReceiver', 'type': 'error'}, b'\xa45 \x80': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'ERC6909InvalidSender', 'type': 'error'}, b'oe\xf4e': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'ERC6909InvalidSpender', 'type': 'error'}, b'\xb3\xfdPq\x83X\x87Vz\x06q\x15\x11!\x89M\xdc\xcc(B\xf1\xd1\x0b\xed\xad\x13\xe0\xd1|\xac\xe9\xa7': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, b'\xa5\xd4\t~\xdd\xa6\xd8|\xb92\x9a\xf8?\xb3q.\xf7~\xeb\x13s\x8f\xfeC\xcc5\xa4\xce0Z\xd9b': {'anonymous': False, 'inputs': [], 'name': 'ContractURIUpdated', 'type': 'event'}, b'\xce\xb5v\xd9\xf1^N \x0f\xdbP\x96\xd6M]\xfdf~\x16\xde\xf2\x0c\x1e\xef\xd1BV\xd8\xe3\xfa\xa2g': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'OperatorSet', 'type': 'event'}, b'\x1b=~\xdb.\x9c\x0b\x0e|R[ \xaa\xae\xf0\xf5\x94\r.\xd7\x16c\xc7\xd3\x92f\xec\xaf\xacr\x88Y': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, b'k\xb7\xffp\x86\x19\xba\x06\x10\xcb\xa2\x95\xa5\x85\x92\xe0E\x1d\xee&"\x93\x8c\x87Ufv\x88\xda\xf3R\x9b': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'value', 'type': 'string'}, {'indexed': True, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'URI', 'type': 'event'}, b'Y\x8a\xf9\xe7': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'Bj\x84\x93': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x00\xfd\xd5\x8e': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe8\xa3\xd4\x85': {'inputs': [], 'name': 'contractURI', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb66<\xf2': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'isOperator', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'U\x8ar\x97': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'setOperator', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x01\xff\xc9\xa7': {'inputs': [{'internalType': 'bytes4', 'name': 'interfaceId', 'type': 'bytes4'}], 'name': 'supportsInterface', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc8{V\xdd': {'inputs': [{'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'tokenURI', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\t[\xcd\xb6': {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfe\x99\x04\x9a': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":200,"contract":"lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909ContentURI.sol:ERC6909ContentURI","label":"_balances","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_uint256,t_uint256))"},{"astId":206,"contract":"lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909ContentURI.sol:ERC6909ContentURI","label":"_operatorApprovals","offset":0,"slot":1,"type":"t_mapping(t_address,t_mapping(t_address,t_bool))"},{"astId":214,"contract":"lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909ContentURI.sol:ERC6909ContentURI","label":"_allowances","offset":0,"slot":2,"type":"t_mapping(t_address,t_mapping(t_address,t_mapping(t_uint256,t_uint256)))"},{"astId":836,"contract":"lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909ContentURI.sol:ERC6909ContentURI","label":"_contractURI","offset":0,"slot":3,"type":"t_string_storage"},{"astId":840,"contract":"lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909ContentURI.sol:ERC6909ContentURI","label":"_tokenURIs","offset":0,"slot":4,"type":"t_mapping(t_uint256,t_string_storage)"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_mapping(t_address,t_bool)":{"encoding":"mapping","label":"mapping(address => bool)","numberOfBytes":32,"key":"t_address","value":"t_bool"},"t_mapping(t_address,t_mapping(t_address,t_bool))":{"encoding":"mapping","label":"mapping(address => mapping(address => bool))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_address,t_bool)"},"t_mapping(t_address,t_mapping(t_address,t_mapping(t_uint256,t_uint256)))":{"encoding":"mapping","label":"mapping(address => mapping(address => mapping(uint256 => uint256)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_address,t_mapping(t_uint256,t_uint256))"},"t_mapping(t_address,t_mapping(t_uint256,t_uint256))":{"encoding":"mapping","label":"mapping(address => mapping(uint256 => uint256))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_uint256,t_uint256)"},"t_mapping(t_uint256,t_string_storage)":{"encoding":"mapping","label":"mapping(uint256 => string)","numberOfBytes":32,"key":"t_uint256","value":"t_string_storage"},"t_mapping(t_uint256,t_uint256)":{"encoding":"mapping","label":"mapping(uint256 => uint256)","numberOfBytes":32,"key":"t_uint256","value":"t_uint256"},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60808060405234601557610817908161001a8239f35b5f80fdfe6080806040526004361015610012575f80fd5b5f3560e01c908162fdd58e146105ff5750806301ffc9a7146105a9578063095bcdb614610591578063426a849314610512578063558a729714610455578063598af9e7146103fb578063b6363cf2146103a4578063c87b56dd146102be578063e8a3d485146101a25763fe99049a14610089575f80fd5b3461019e57608036600319011261019e576100a261063d565b6100aa610653565b6001600160a01b038216916064359160443591338514158061017b575b6100e1575b6100d694506106bd565b602060405160018152f35b5f85815260026020908152604080832033845282528083208684529091529020545f198110610111575b506100cc565b84811061014d5784906100d6965f52600260205260405f2060018060a01b0333165f5260205260405f20855f526020520360405f20555f61010b565b604051632c51fead60e11b815233600482015260248101919091526044810185905260648101849052608490fd5b505f85815260016020908152604080832033845290915290205460ff16156100c7565b5f80fd5b3461019e575f36600319011261019e576040515f6003548060011c906001811680156102b4575b6020831081146102a057828552908115610284575060011461022e575b50819003601f01601f191681019067ffffffffffffffff82118183101761021a5761021682918260405282610693565b0390f35b634e487b7160e01b5f52604160045260245ffd5b60035f9081529091507fc2575a0e9e593c00f959f8c92f12db2869c3395a3b0502d05e2516446f71f85b5b82821061026e575060209150820101826101e6565b6001816020925483858801015201910190610259565b90506020925060ff191682840152151560051b820101826101e6565b634e487b7160e01b5f52602260045260245ffd5b91607f16916101c9565b3461019e57602036600319011261019e576004355f52600460205260405f20604051905f908054908160011c9160018116801561039a575b6020841081146102a05783865290811561037c5750600114610344575b5050819003601f01601f191681019067ffffffffffffffff82118183101761021a5761021682918260405282610693565b9091505f5260205f205f905b8282106103665750602091508201018280610313565b6001816020925483858801015201910190610350565b9150506020925060ff191682840152151560051b8201018280610313565b92607f16926102f6565b3461019e57604036600319011261019e576103bd61063d565b6103c5610653565b9060018060a01b03165f52600160205260405f209060018060a01b03165f52602052602060ff60405f2054166040519015158152f35b3461019e57606036600319011261019e5761041461063d565b61041c610653565b6001600160a01b039182165f90815260026020908152604080832094909316825292835281812060443582528352819020549051908152f35b3461019e57604036600319011261019e5761046e61063d565b6024359081151580920361019e5733156104ff576001600160a01b03169081156104ec57335f52600160205260405f20825f5260205260405f2060ff1981541660ff83161790556040519081527fceb576d9f15e4e200fdb5096d64d5dfd667e16def20c1eefd14256d8e3faa26760203392a3602060405160018152f35b636f65f46560e01b5f525f60045260245ffd5b63198ecd5360e31b5f525f60045260245ffd5b3461019e5761052036610669565b909133156104ff576001600160a01b03169081156104ec57335f52600260205260405f20825f5260205260405f20835f526020528060405f20556040519081527fb3fd5071835887567a0671151121894ddccc2842f1d10bedad13e0d17cace9a760203392a4602060405160018152f35b3461019e576100d66105a236610669565b91336106bd565b3461019e57602036600319011261019e5760043563ffffffff60e01b811680910361019e57602090630f632fb360e01b81149081156105ee575b506040519015158152f35b6301ffc9a760e01b149050826105e3565b3461019e57604036600319011261019e576020906001600160a01b0361062361063d565b165f525f825260405f206024355f52825260405f20548152f35b600435906001600160a01b038216820361019e57565b602435906001600160a01b038216820361019e57565b606090600319011261019e576004356001600160a01b038116810361019e57906024359060443590565b602060409281835280519182918282860152018484015e5f828201840152601f01601f1916010190565b91926001600160a01b0383169182156107ce576001600160a01b03169283156107bb57825f525f60205260405f20855f5260205260405f20549082821061078257508190835f525f60205260405f20865f526020520360405f2055825f525f60205260405f20845f5260205260405f2080549180830180931161076e577f1b3d7edb2e9c0b0e7c525b20aaaef0f5940d2ed71663c7d39266ecafac72885992604092558151903382526020820152a4565b634e487b7160e01b5f52601160045260245ffd5b6040516302c6d3fb60e61b81526001600160a01b0391909116600482015260248101919091526044810182905260648101859052608490fd5b630b8bbd6160e41b5f525f60045260245ffd5b6301486a4160e71b5f525f60045260245ffdfea26469706673582212204dcf4ca654c9885450d560906675ec2d09bcc8f697fee2a61e84da65e3d4838964736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC6909ContentURI:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC6909ContentURI]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC6909ContentURI, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC6909ContentURI]]:
        return cls._deploy(request_type, [], return_tx, ERC6909ContentURI, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class ContractURIUpdated:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909ContentURI.sol#17)
        """
        _abi = {'anonymous': False, 'inputs': [], 'name': 'ContractURIUpdated', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ContractURIUpdated'
        selector = bytes32(b'\xa5\xd4\t~\xdd\xa6\xd8|\xb92\x9a\xf8?\xb3q.\xf7~\xeb\x13s\x8f\xfeC\xcc5\xa4\xce0Z\xd9b')



    @dataclasses.dataclass
    class URI:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909ContentURI.sol#20)

        Attributes:
            value (str): string
            id (uint256): indexed uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'string', 'name': 'value', 'type': 'string'}, {'indexed': True, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'URI', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'URI'
        selector = bytes32(b'k\xb7\xffp\x86\x19\xba\x06\x10\xcb\xa2\x95\xa5\x85\x92\xe0E\x1d\xee&"\x93\x8c\x87Ufv\x88\xda\xf3R\x9b')

        value: str
        id: uint256


    @overload
    def contractURI(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909ContentURI.sol#23)

        Returns:
            string
        """
        ...

    @overload
    def contractURI(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909ContentURI.sol#23)

        Returns:
            string
        """
        ...

    @overload
    def contractURI(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909ContentURI.sol#23)

        Returns:
            string
        """
        ...

    @overload
    def contractURI(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909ContentURI.sol#23)

        Returns:
            string
        """
        ...

    def contractURI(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909ContentURI.sol#23)

        Returns:
            string
        """
        return self._execute(self.chain, request_type, "e8a3d485", [], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tokenURI(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909ContentURI.sol#28)

        Args:
            id: uint256
        Returns:
            string
        """
        ...

    @overload
    def tokenURI(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909ContentURI.sol#28)

        Args:
            id: uint256
        Returns:
            string
        """
        ...

    @overload
    def tokenURI(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909ContentURI.sol#28)

        Args:
            id: uint256
        Returns:
            string
        """
        ...

    @overload
    def tokenURI(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909ContentURI.sol#28)

        Args:
            id: uint256
        Returns:
            string
        """
        ...

    def tokenURI(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909ContentURI.sol#28)

        Args:
            id: uint256
        Returns:
            string
        """
        return self._execute(self.chain, request_type, "c87b56dd", [id], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC6909ContentURI.contractURI.selector = bytes4(b'\xe8\xa3\xd4\x85')
ERC6909ContentURI.tokenURI.selector = bytes4(b'\xc8{V\xdd')
