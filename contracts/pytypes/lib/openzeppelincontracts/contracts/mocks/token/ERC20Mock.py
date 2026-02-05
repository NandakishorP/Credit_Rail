
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.token.ERC20.ERC20 import ERC20



class ERC20Mock(ERC20):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol#6)
    """
    _abi = {'constructor': {'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\xfb\x8fA\xb2': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'allowance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}], 'name': 'ERC20InsufficientAllowance', 'type': 'error'}, b'\xe4P\xd3\x8c': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}], 'name': 'ERC20InsufficientBalance', 'type': 'error'}, b'\xe6\x02\xdf\x05': {'inputs': [{'internalType': 'address', 'name': 'approver', 'type': 'address'}], 'name': 'ERC20InvalidApprover', 'type': 'error'}, b'\xecD/\x05': {'inputs': [{'internalType': 'address', 'name': 'receiver', 'type': 'address'}], 'name': 'ERC20InvalidReceiver', 'type': 'error'}, b'\x96\xc6\xfd\x1e': {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'ERC20InvalidSender', 'type': 'error'}, b'\x94(\rb': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'ERC20InvalidSpender', 'type': 'error'}, b'\x8c[\xe1\xe5\xeb\xec}[\xd1OqB}\x1e\x84\xf3\xdd\x03\x14\xc0\xf7\xb2)\x1e[ \n\xc8\xc7\xc3\xb9%': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, b'\xdd\xf2R\xad\x1b\xe2\xc8\x9bi\xc2\xb0h\xfc7\x8d\xaa\x95+\xa7\xf1c\xc4\xa1\x16(\xf5ZM\xf5#\xb3\xef': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, b'\xddb\xed>': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\t^\xa7\xb3': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'p\xa0\x821': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x9d\xc2\x9f\xac': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'burn', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'1<\xe5g': {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, b'@\xc1\x0f\x19': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'mint', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x06\xfd\xde\x03': {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x95\xd8\x9bA': {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x18\x16\r\xdd': {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa9\x05\x9c\xbb': {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'#\xb8r\xdd': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":40244,"contract":"lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol:ERC20Mock","label":"_balances","offset":0,"slot":0,"type":"t_mapping(t_address,t_uint256)"},{"astId":40250,"contract":"lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol:ERC20Mock","label":"_allowances","offset":0,"slot":1,"type":"t_mapping(t_address,t_mapping(t_address,t_uint256))"},{"astId":40252,"contract":"lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol:ERC20Mock","label":"_totalSupply","offset":0,"slot":2,"type":"t_uint256"},{"astId":40254,"contract":"lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol:ERC20Mock","label":"_name","offset":0,"slot":3,"type":"t_string_storage"},{"astId":40256,"contract":"lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol:ERC20Mock","label":"_symbol","offset":0,"slot":4,"type":"t_string_storage"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_mapping(t_address,t_mapping(t_address,t_uint256))":{"encoding":"mapping","label":"mapping(address => mapping(address => uint256))","numberOfBytes":32,"key":"t_address","value":"t_mapping(t_address,t_uint256)"},"t_mapping(t_address,t_uint256)":{"encoding":"mapping","label":"mapping(address => uint256)","numberOfBytes":32,"key":"t_address","value":"t_uint256"},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60806040523461032957604080519081016001600160401b03811182821017610231576040908152600982526845524332304d6f636b60b81b602083015280519081016001600160401b038111828210176102315760405260048152634532304d60e01b602082015281516001600160401b03811161023157600354600181811c9116801561031f575b602082101461021357601f81116102b1575b50602092601f821160011461025057928192935f92610245575b50508160011b915f199060031b1c1916176003555b80516001600160401b03811161023157600454600181811c91168015610227575b602082101461021357601f81116101a5575b50602091601f8211600114610145579181925f9261013a575b50508160011b915f199060031b1c1916176004555b604051610731908161032e8239f35b015190505f80610116565b601f1982169260045f52805f20915f5b85811061018d57508360019510610175575b505050811b0160045561012b565b01515f1960f88460031b161c191690555f8080610167565b91926020600181928685015181550194019201610155565b818111156100fd5760045f52601f820160051c7f8a35acfbc15ff81a39ae7d344fd709f28e8600b4aa8c65c6b64bfe7fe36bd19b6020841061020b575b81601f9101920160051c03905f5b8281106101fe5750506100fd565b5f828201556001016101f0565b5f91506101e2565b634e487b7160e01b5f52602260045260245ffd5b90607f16906100eb565b634e487b7160e01b5f52604160045260245ffd5b015190505f806100b5565b601f1982169360035f52805f20915f5b8681106102995750836001959610610281575b505050811b016003556100ca565b01515f1960f88460031b161c191690555f8080610273565b91926020600181928685015181550194019201610260565b8181111561009b5760035f52601f820160051c7fc2575a0e9e593c00f959f8c92f12db2869c3395a3b0502d05e2516446f71f85b60208410610317575b81601f9101920160051c03905f5b82811061030a57505061009b565b5f828201556001016102fc565b5f91506102ee565b90607f1690610089565b5f80fdfe6080806040526004361015610012575f80fd5b5f3560e01c90816306fdde031461053157508063095ea7b3146104af57806318160ddd1461049257806323b872dd146103b3578063313ce5671461039857806340c10f191461030957806370a08231146102d257806395d89b41146101b65780639dc29fac1461011a578063a9059cbb146100e95763dd62ed3e14610095575f80fd5b346100e55760403660031901126100e5576100ae61062b565b6100b6610641565b6001600160a01b039182165f908152600160209081526040808320949093168252928352819020549051908152f35b5f80fd5b346100e55760403660031901126100e55761010f61010561062b565b6024359033610657565b602060405160018152f35b346100e55760403660031901126100e55761013361062b565b602435906001600160a01b031680156101a357805f525f60205260405f205482811061018a576020835f945f5160206106dc5f395f51905f52938587528684520360408620558060025403600255604051908152a3005b9063391434e360e21b5f5260045260245260445260645ffd5b634b637e8f60e11b5f525f60045260245ffd5b346100e5575f3660031901126100e5576040515f6004548060011c906001811680156102c8575b6020831081146102b4578285529081156102985750600114610242575b50819003601f01601f191681019067ffffffffffffffff82118183101761022e5761022a82918260405282610601565b0390f35b634e487b7160e01b5f52604160045260245ffd5b60045f9081529091507f8a35acfbc15ff81a39ae7d344fd709f28e8600b4aa8c65c6b64bfe7fe36bd19b5b828210610282575060209150820101826101fa565b600181602092548385880101520191019061026d565b90506020925060ff191682840152151560051b820101826101fa565b634e487b7160e01b5f52602260045260245ffd5b91607f16916101dd565b346100e55760203660031901126100e5576001600160a01b036102f361062b565b165f525f602052602060405f2054604051908152f35b346100e55760403660031901126100e55761032261062b565b6001600160a01b0316602435811561038557600254908082018092116103715760205f5160206106dc5f395f51905f52915f9360025584845283825260408420818154019055604051908152a3005b634e487b7160e01b5f52601160045260245ffd5b63ec442f0560e01b5f525f60045260245ffd5b346100e5575f3660031901126100e557602060405160128152f35b346100e55760603660031901126100e5576103cc61062b565b6103d4610641565b6001600160a01b0382165f818152600160209081526040808320338452909152902054909260443592915f198110610412575b5061010f9350610657565b8381106104775784156104645733156104515761010f945f52600160205260405f2060018060a01b0333165f526020528360405f209103905584610407565b634a1406b160e11b5f525f60045260245ffd5b63e602df0560e01b5f525f60045260245ffd5b8390637dc7a0d960e11b5f523360045260245260445260645ffd5b346100e5575f3660031901126100e5576020600254604051908152f35b346100e55760403660031901126100e5576104c861062b565b602435903315610464576001600160a01b031690811561045157335f52600160205260405f20825f526020528060405f20556040519081527f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b92560203392a3602060405160018152f35b346100e5575f3660031901126100e5575f6003548060011c906001811680156105f7575b6020831081146102b45782855290811561029857506001146105a15750819003601f01601f191681019067ffffffffffffffff82118183101761022e5761022a82918260405282610601565b60035f9081529091507fc2575a0e9e593c00f959f8c92f12db2869c3395a3b0502d05e2516446f71f85b5b8282106105e1575060209150820101826101fa565b60018160209254838588010152019101906105cc565b91607f1691610555565b602060409281835280519182918282860152018484015e5f828201840152601f01601f1916010190565b600435906001600160a01b03821682036100e557565b602435906001600160a01b03821682036100e557565b6001600160a01b03169081156101a3576001600160a01b031691821561038557815f525f60205260405f20548181106106c257815f5160206106dc5f395f51905f5292602092855f525f84520360405f2055845f525f825260405f20818154019055604051908152a3565b8263391434e360e21b5f5260045260245260445260645ffdfeddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3efa26469706673582212200818327cac74ef319a519aee20f7af169fd2da078a2fa5a704d995b7c953506264736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol#7)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC20Mock:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol#7)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol#7)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol#7)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC20Mock]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol#7)
        """
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC20Mock, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC20Mock]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol#7)
        """
        return cls._deploy(request_type, [], return_tx, ERC20Mock, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def mint(self, account: Union[Account, Address], amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol#9)

        Args:
            account: address
            amount: uint256
        """
        ...

    @overload
    def mint(self, account: Union[Account, Address], amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol#9)

        Args:
            account: address
            amount: uint256
        """
        ...

    @overload
    def mint(self, account: Union[Account, Address], amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol#9)

        Args:
            account: address
            amount: uint256
        """
        ...

    @overload
    def mint(self, account: Union[Account, Address], amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol#9)

        Args:
            account: address
            amount: uint256
        """
        ...

    def mint(self, account: Union[Account, Address], amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol#9)

        Args:
            account: address
            amount: uint256
        """
        return self._execute(self.chain, request_type, "40c10f19", [account, amount], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def burn(self, account: Union[Account, Address], amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol#13)

        Args:
            account: address
            amount: uint256
        """
        ...

    @overload
    def burn(self, account: Union[Account, Address], amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol#13)

        Args:
            account: address
            amount: uint256
        """
        ...

    @overload
    def burn(self, account: Union[Account, Address], amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol#13)

        Args:
            account: address
            amount: uint256
        """
        ...

    @overload
    def burn(self, account: Union[Account, Address], amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol#13)

        Args:
            account: address
            amount: uint256
        """
        ...

    def burn(self, account: Union[Account, Address], amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20Mock.sol#13)

        Args:
            account: address
            amount: uint256
        """
        return self._execute(self.chain, request_type, "9dc29fac", [account, amount], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC20Mock.mint.selector = bytes4(b'@\xc1\x0f\x19')
ERC20Mock.burn.selector = bytes4(b'\x9d\xc2\x9f\xac')
