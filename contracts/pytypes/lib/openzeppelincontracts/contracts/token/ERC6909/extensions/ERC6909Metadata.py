
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.interfaces.IERC6909 import IERC6909Metadata
from pytypes.lib.openzeppelincontracts.contracts.token.ERC6909.ERC6909 import ERC6909



class ERC6909Metadata(IERC6909Metadata, ERC6909):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#12)
    """
    _abi = {b'X\xa3\xfdZ': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'allowance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'ERC6909InsufficientAllowance', 'type': 'error'}, b'\xb1\xb4\xfe\xc0': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'ERC6909InsufficientBalance', 'type': 'error'}, b'\xccvj\x98': {'inputs': [{'internalType': 'address', 'name': 'approver', 'type': 'address'}], 'name': 'ERC6909InvalidApprover', 'type': 'error'}, b'\xb8\xbb\xd6\x10': {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'ERC6909InvalidReceiver', 'type': 'error'}, b'\xa45 \x80': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'ERC6909InvalidSender', 'type': 'error'}, b'oe\xf4e': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'ERC6909InvalidSpender', 'type': 'error'}, b'\xb3\xfdPq\x83X\x87Vz\x06q\x15\x11!\x89M\xdc\xcc(B\xf1\xd1\x0b\xed\xad\x13\xe0\xd1|\xac\xe9\xa7': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, b'\xc7CXtV\x80\x17\xe6\x13L\x85\x10\x02\xa4\x05\xd73R\x1c\x0fLc\xf9\xf2_:2\xa4\xd5\x95\xb7)': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint8', 'name': 'newDecimals', 'type': 'uint8'}], 'name': 'ERC6909DecimalsUpdated', 'type': 'event'}, b'hFp{\x16\xf5Z6#\xd3\x8b\xf1\x18p\n\xf6=\x07\x84i\x82p\xa5<\xe2\x8b\x11m\xba\xa8\xb7\x94': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'newName', 'type': 'string'}], 'name': 'ERC6909NameUpdated', 'type': 'event'}, b'\x8f\xab\xcb{O\xbd\xde`S\x03\xa73\x9b\xc8\x0f\xb6\x95l\xd0\x1aB\xe9\xcd\xf2\xd1]\x0f/\xdd;\x06\xfa': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'newSymbol', 'type': 'string'}], 'name': 'ERC6909SymbolUpdated', 'type': 'event'}, b'\xce\xb5v\xd9\xf1^N \x0f\xdbP\x96\xd6M]\xfdf~\x16\xde\xf2\x0c\x1e\xef\xd1BV\xd8\xe3\xfa\xa2g': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'OperatorSet', 'type': 'event'}, b'\x1b=~\xdb.\x9c\x0b\x0e|R[ \xaa\xae\xf0\xf5\x94\r.\xd7\x16c\xc7\xd3\x92f\xec\xaf\xacr\x88Y': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'caller', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'indexed': True, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, b'Y\x8a\xf9\xe7': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'Bj\x84\x93': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x00\xfd\xd5\x8e': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'?G\xe6b': {'inputs': [{'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb66<\xf2': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'isOperator', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x00\xad\x80\x0c': {'inputs': [{'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'U\x8ar\x97': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'bool', 'name': 'approved', 'type': 'bool'}], 'name': 'setOperator', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x01\xff\xc9\xa7': {'inputs': [{'internalType': 'bytes4', 'name': 'interfaceId', 'type': 'bytes4'}], 'name': 'supportsInterface', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'NA\xa1\xfb': {'inputs': [{'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\t[\xcd\xb6': {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfe\x99\x04\x9a': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'address', 'name': 'receiver', 'type': 'address'}, {'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":200,"contract":"lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol:ERC6909Metadata","label":"_balances","offset":0,"slot":0,"type":"t_mapping(t_address,t_mapping(t_uint256,t_uint256))"},{"astId":206,"contract":"lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol:ERC6909Metadata","label":"_operatorApprovals","offset":0,"slot":1,"type":"t_mapping(t_address,t_mapping(t_address,t_bool))"},{"astId":214,"contract":"lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol:ERC6909Metadata","label":"_allowances","offset":0,"slot":2,"type":"t_mapping(t_address,t_mapping(t_address,t_mapping(t_uint256,t_uint256)))"},{"astId":846,"contract":"lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol:ERC6909Metadata","label":"_tokenMetadata","offset":0,"slot":3,"type":"t_mapping(t_uint256,t_struct(TokenMetadata)841_storage)"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_mapping(t_address,t_bool)":{"encoding":"mapping","label":"mapping(address => bool)","numberOfBytes":32,"key":"t_address","value":"t_bool"},"t_mapping(t_address,t_mapping(t_address,t_bool))":{"encoding":"mapping","label":"mapping(address => mapping(address => bool))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_address,t_bool)"},"t_mapping(t_address,t_mapping(t_address,t_mapping(t_uint256,t_uint256)))":{"encoding":"mapping","label":"mapping(address => mapping(address => mapping(uint256 => uint256)))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_address,t_mapping(t_uint256,t_uint256))"},"t_mapping(t_address,t_mapping(t_uint256,t_uint256))":{"encoding":"mapping","label":"mapping(address => mapping(uint256 => uint256))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_uint256,t_uint256)"},"t_mapping(t_uint256,t_struct(TokenMetadata)841_storage)":{"encoding":"mapping","label":"mapping(uint256 => struct ERC6909Metadata.TokenMetadata)","numberOfBytes":32,"key":"t_uint256","value":"t_struct(TokenMetadata)841_storage"},"t_mapping(t_uint256,t_uint256)":{"encoding":"mapping","label":"mapping(uint256 => uint256)","numberOfBytes":32,"key":"t_uint256","value":"t_uint256"},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(TokenMetadata)841_storage":{"encoding":"inplace","label":"struct ERC6909Metadata.TokenMetadata","numberOfBytes":96,"members":[{"astId":836,"contract":"lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol:ERC6909Metadata","label":"name","offset":0,"slot":0,"type":"t_string_storage"},{"astId":838,"contract":"lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol:ERC6909Metadata","label":"symbol","offset":0,"slot":1,"type":"t_string_storage"},{"astId":840,"contract":"lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol:ERC6909Metadata","label":"decimals","offset":0,"slot":2,"type":"t_uint8"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32},"t_uint8":{"encoding":"inplace","label":"uint8","numberOfBytes":1}}}
    _creation_code = "6080806040523460155761079d908161001a8239f35b5f80fdfe60806040526004361015610011575f80fd5b5f3560e01c8062ad800c146104b4578062fdd58e1461047157806301ffc9a71461041b578063095bcdb6146104035780633f47e662146103d3578063426a8493146103545780634e41a1fb14610317578063558a72971461025a578063598af9e714610200578063b6363cf2146101a95763fe99049a14610090575f80fd5b346101a55760803660031901126101a5576100a9610508565b6100b161051e565b6001600160a01b0382169160643591604435913385141580610182575b6100e8575b6100dd9450610643565b602060405160018152f35b5f85815260026020908152604080832033845282528083208684529091529020545f198110610118575b506100d3565b8481106101545784906100dd965f52600260205260405f2060018060a01b0333165f5260205260405f20855f526020520360405f20555f610112565b604051632c51fead60e11b815233600482015260248101919091526044810185905260648101849052608490fd5b505f85815260016020908152604080832033845290915290205460ff16156100ce565b5f80fd5b346101a55760403660031901126101a5576101c2610508565b6101ca61051e565b9060018060a01b03165f52600160205260405f209060018060a01b03165f52602052602060ff60405f2054166040519015158152f35b346101a55760603660031901126101a557610219610508565b61022161051e565b6001600160a01b039182165f90815260026020908152604080832094909316825292835281812060443582528352819020549051908152f35b346101a55760403660031901126101a557610273610508565b602435908115158092036101a5573315610304576001600160a01b03169081156102f157335f52600160205260405f20825f5260205260405f2060ff1981541660ff83161790556040519081527fceb576d9f15e4e200fdb5096d64d5dfd667e16def20c1eefd14256d8e3faa26760203392a3602060405160018152f35b636f65f46560e01b5f525f60045260245ffd5b63198ecd5360e31b5f525f60045260245ffd5b346101a55760203660031901126101a5576004355f526003602052610350610344600160405f200161055e565b604051918291826104de565b0390f35b346101a55761036236610534565b90913315610304576001600160a01b03169081156102f157335f52600260205260405f20825f5260205260405f20835f526020528060405f20556040519081527fb3fd5071835887567a0671151121894ddccc2842f1d10bedad13e0d17cace9a760203392a4602060405160018152f35b346101a55760203660031901126101a5576004355f526003602052602060ff600260405f20015416604051908152f35b346101a5576100dd61041436610534565b9133610643565b346101a55760203660031901126101a55760043563ffffffff60e01b81168091036101a557602090630f632fb360e01b8114908115610460575b506040519015158152f35b6301ffc9a760e01b14905082610455565b346101a55760403660031901126101a5576001600160a01b03610492610508565b165f525f60205260405f206024355f52602052602060405f2054604051908152f35b346101a55760203660031901126101a5576004355f52600360205261035061034460405f2061055e565b602060409281835280519182918282860152018484015e5f828201840152601f01601f1916010190565b600435906001600160a01b03821682036101a557565b602435906001600160a01b03821682036101a557565b60609060031901126101a5576004356001600160a01b03811681036101a557906024359060443590565b90604051915f908054908160011c91600181168015610639575b6020841081146106255783875290811561060757506001146105cf575b5050829003601f01601f1916820167ffffffffffffffff8111838210176105bb57604052565b634e487b7160e01b5f52604160045260245ffd5b9091505f5260205f205f905b8282106105f15750602091508301015f80610595565b60018160209254838589010152019101906105db565b9150506020925060ff191682850152151560051b8301015f80610595565b634e487b7160e01b5f52602260045260245ffd5b92607f1692610578565b91926001600160a01b038316918215610754576001600160a01b031692831561074157825f525f60205260405f20855f5260205260405f20549082821061070857508190835f525f60205260405f20865f526020520360405f2055825f525f60205260405f20845f5260205260405f208054918083018093116106f4577f1b3d7edb2e9c0b0e7c525b20aaaef0f5940d2ed71663c7d39266ecafac72885992604092558151903382526020820152a4565b634e487b7160e01b5f52601160045260245ffd5b6040516302c6d3fb60e61b81526001600160a01b0391909116600482015260248101919091526044810182905260648101859052608490fd5b630b8bbd6160e41b5f525f60045260245ffd5b6301486a4160e71b5f525f60045260245ffdfea26469706673582212203c37167a89a6719296200ca655386e8f52898462d497b03a3cadf9943878412864736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC6909Metadata:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC6909Metadata]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC6909Metadata, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC6909Metadata]]:
        return cls._deploy(request_type, [], return_tx, ERC6909Metadata, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class TokenMetadata:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#13)

        Attributes:
            name (str): string
            symbol (str): string
            decimals (uint8): uint8
        """
        original_name = 'TokenMetadata'

        name: str
        symbol: str
        decimals: uint8


    @dataclasses.dataclass
    class ERC6909NameUpdated:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#22)

        Attributes:
            id (uint256): indexed uint256
            newName (str): string
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'newName', 'type': 'string'}], 'name': 'ERC6909NameUpdated', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ERC6909NameUpdated'
        selector = bytes32(b'hFp{\x16\xf5Z6#\xd3\x8b\xf1\x18p\n\xf6=\x07\x84i\x82p\xa5<\xe2\x8b\x11m\xba\xa8\xb7\x94')

        id: uint256
        newName: str


    @dataclasses.dataclass
    class ERC6909SymbolUpdated:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#25)

        Attributes:
            id (uint256): indexed uint256
            newSymbol (str): string
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'newSymbol', 'type': 'string'}], 'name': 'ERC6909SymbolUpdated', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ERC6909SymbolUpdated'
        selector = bytes32(b'\x8f\xab\xcb{O\xbd\xde`S\x03\xa73\x9b\xc8\x0f\xb6\x95l\xd0\x1aB\xe9\xcd\xf2\xd1]\x0f/\xdd;\x06\xfa')

        id: uint256
        newSymbol: str


    @dataclasses.dataclass
    class ERC6909DecimalsUpdated:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#28)

        Attributes:
            id (uint256): indexed uint256
            newDecimals (uint8): uint8
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'id', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint8', 'name': 'newDecimals', 'type': 'uint8'}], 'name': 'ERC6909DecimalsUpdated', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ERC6909DecimalsUpdated'
        selector = bytes32(b'\xc7CXtV\x80\x17\xe6\x13L\x85\x10\x02\xa4\x05\xd73R\x1c\x0fLc\xf9\xf2_:2\xa4\xd5\x95\xb7)')

        id: uint256
        newDecimals: uint8


    @overload
    def name(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#31)

        Args:
            id: uint256
        Returns:
            string
        """
        ...

    @overload
    def name(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#31)

        Args:
            id: uint256
        Returns:
            string
        """
        ...

    @overload
    def name(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#31)

        Args:
            id: uint256
        Returns:
            string
        """
        ...

    @overload
    def name(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#31)

        Args:
            id: uint256
        Returns:
            string
        """
        ...

    def name(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#31)

        Args:
            id: uint256
        Returns:
            string
        """
        return self._execute(self.chain, request_type, "00ad800c", [id], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def symbol(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#36)

        Args:
            id: uint256
        Returns:
            string
        """
        ...

    @overload
    def symbol(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#36)

        Args:
            id: uint256
        Returns:
            string
        """
        ...

    @overload
    def symbol(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#36)

        Args:
            id: uint256
        Returns:
            string
        """
        ...

    @overload
    def symbol(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#36)

        Args:
            id: uint256
        Returns:
            string
        """
        ...

    def symbol(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#36)

        Args:
            id: uint256
        Returns:
            string
        """
        return self._execute(self.chain, request_type, "4e41a1fb", [id], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def decimals(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint8:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#41)

        Args:
            id: uint256
        Returns:
            uint8
        """
        ...

    @overload
    def decimals(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#41)

        Args:
            id: uint256
        Returns:
            uint8
        """
        ...

    @overload
    def decimals(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#41)

        Args:
            id: uint256
        Returns:
            uint8
        """
        ...

    @overload
    def decimals(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint8]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#41)

        Args:
            id: uint256
        Returns:
            uint8
        """
        ...

    def decimals(self, id: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint8, TransactionAbc[uint8], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/token/ERC6909/extensions/ERC6909Metadata.sol#41)

        Args:
            id: uint256
        Returns:
            uint8
        """
        return self._execute(self.chain, request_type, "3f47e662", [id], True if request_type == "tx" else False, uint8, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC6909Metadata.name.selector = bytes4(b'\x00\xad\x80\x0c')
ERC6909Metadata.symbol.selector = bytes4(b'NA\xa1\xfb')
ERC6909Metadata.decimals.selector = bytes4(b'?G\xe6b')
