
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.token.ERC20.IERC20 import IERC20
from pytypes.lib.openzeppelincontracts.contracts.token.ERC20.extensions.IERC20Metadata import IERC20Metadata



class ERC20GetterHelper(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#7)
    """
    _abi = {b'\xe0\x9e\xed"KOQ\xd92\xc9\x80-\x15#ZN=\x83\xe6\xe9\x87F\xfb\xd1vr\xbf\xa0\xc6\x8c\xf2\xa5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'contract IERC20', 'name': 'token', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'allowance', 'type': 'uint256'}], 'name': 'ERC20Allowance', 'type': 'event'}, b'\xfa\x06\x99r\xe8\xd8\xe0\xf3"\x8d\xef\xb4M[|\x9b\xc6\xc3\xf0\x8e\xf9\x8b\xc7\xd6\xa3\x1aZ\xd2\x99:\x97\x95': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'contract IERC20', 'name': 'token', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'account', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'balanceOf', 'type': 'uint256'}], 'name': 'ERC20BalanceOf', 'type': 'event'}, b'\x85\xbc\x87+\x16\xb9\xdb.J\xda7\x05s\xff\xd3\x96`+\xfd\xac\xec\x01\xf72\xf2\xb5\xaboB\xf2D5': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'contract IERC20Metadata', 'name': 'token', 'type': 'address'}, {'indexed': False, 'internalType': 'uint8', 'name': 'decimals', 'type': 'uint8'}], 'name': 'ERC20Decimals', 'type': 'event'}, b'\x04\x85\xcaSu\x88\x9f\x98\xba\xa3\xc2\xb6\xf4\xc5\x01\x7fBD]F\xa8\xea40\x181\xf4\xc0ej\xea\xef': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'contract IERC20Metadata', 'name': 'token', 'type': 'address'}, {'indexed': False, 'internalType': 'string', 'name': 'name', 'type': 'string'}], 'name': 'ERC20Name', 'type': 'event'}, b'&\xe0G\x05\xbb&\xa7\xef\xc4,/\xc2)SZ0\xfa\xa3\xff\xf9\xa0L\xd1^\xd4\xa7)\xc9\xbcM5\xbf': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'contract IERC20Metadata', 'name': 'token', 'type': 'address'}, {'indexed': False, 'internalType': 'string', 'name': 'symbol', 'type': 'string'}], 'name': 'ERC20Symbol', 'type': 'event'}, b'd\x85\xfdI\xc6h\xab1\xaanv\xb8\x18\xc9I/\x82\xe9\xa3r\x7f\x8d\xbd\x1d\xed\x1fzx[,\x98.': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'contract IERC20', 'name': 'token', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'totalSupply', 'type': 'uint256'}], 'name': 'ERC20TotalSupply', 'type': 'event'}, b'\x92}\xa1\x05': {'inputs': [{'internalType': 'contract IERC20', 'name': 'token', 'type': 'address'}, {'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'allowance', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf7\x88\x8a\xec': {'inputs': [{'internalType': 'contract IERC20', 'name': 'token', 'type': 'address'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd4I\xa82': {'inputs': [{'internalType': 'contract IERC20Metadata', 'name': 'token', 'type': 'address'}], 'name': 'decimals', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x01\x98H\x92': {'inputs': [{'internalType': 'contract IERC20Metadata', 'name': 'token', 'type': 'address'}], 'name': 'name', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa8n5v': {'inputs': [{'internalType': 'contract IERC20Metadata', 'name': 'token', 'type': 'address'}], 'name': 'symbol', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xe4\xdc*\xa4': {'inputs': [{'internalType': 'contract IERC20', 'name': 'token', 'type': 'address'}], 'name': 'totalSupply', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = "6080806040523460155761066f908161001a8239f35b5f80fdfe6080806040526004361015610012575f80fd5b5f3560e01c90816301984892146104b257508063927da105146103a3578063a86e3576146102fd578063d449a83214610222578063e4dc2aa4146101585763f7888aec1461005e575f80fd5b3461014157604036600319011261014157610077610528565b61007f61053e565b6040516370a0823160e01b81526001600160a01b03918216600482018190529290911691602082602481865afa91821561014d575f926100f3575b7ffa069972e8d8e0f3228defb44d5b7c9bc6c3f08ef98bc7d6a31a5ad2993a9795606085858560405192835260208301526040820152a1005b9150916020823d602011610145575b8161010f60209383610554565b8101031261014157905190917ffa069972e8d8e0f3228defb44d5b7c9bc6c3f08ef98bc7d6a31a5ad2993a97956100ba565b5f80fd5b3d9150610102565b6040513d5f823e3d90fd5b34610141576020366003190112610141576001600160a01b03610179610528565b166040516318160ddd60e01b8152602081600481855afa90811561014d575f916101d0575b7f6485fd49c668ab31aa6e76b818c9492f82e9a3727f8dbd1ded1f7a785b2c982e6040848482519182526020820152a1005b90506020813d60201161021a575b816101eb60209383610554565b8101031261014157517f6485fd49c668ab31aa6e76b818c9492f82e9a3727f8dbd1ded1f7a785b2c982e61019e565b3d91506101de565b34610141576020366003190112610141576004356001600160a01b038116908190036101415760405163313ce56760e01b8152602081600481855afa90811561014d575f916102a1575b7f85bc872b16b9db2e4ada370573ffd396602bfdacec01f732f2b5ab6f42f2443560408460ff858351928352166020820152a1005b90506020813d6020116102f5575b816102bc60209383610554565b81010312610141575160ff81168103610141577f85bc872b16b9db2e4ada370573ffd396602bfdacec01f732f2b5ab6f42f2443561026c565b3d91506102af565b34610141576020366003190112610141576004356001600160a01b03811690818103610141575f600492604051938480926395d89b4160e01b82525afa90811561014d577f26e04705bb26a7efc42c2fc229535a30faa3fff9a04cd15ed4a729c9bc4d35bf925f9261037f575b5061037a604051928392836105fd565b0390a1005b61039c9192503d805f833e6103948183610554565b81019061058a565b908361036a565b34610141576060366003190112610141576103bc610528565b6103c461053e565b6044356001600160a01b038116929083900361014157604051636eb1769f60e11b81526001600160a01b039283166004820181905260248201859052919092169190602082604481865afa91821561014d575f9261045c575b7fe09eed224b4f51d932c9802d15235a4e3d83e6e98746fbd17672bfa0c68cf2a5608085858886604051938452602084015260408301526060820152a1005b9291506020833d6020116104aa575b8161047860209383610554565b8101031261014157915190917fe09eed224b4f51d932c9802d15235a4e3d83e6e98746fbd17672bfa0c68cf2a561041d565b3d915061046b565b34610141576020366003190112610141576004356001600160a01b03811680820361014157826004815f936306fdde0360e01b82525afa90811561014d577f0485ca5375889f98baa3c2b6f4c5017f42445d46a8ea34301831f4c0656aeaef925f9261037f575061037a604051928392836105fd565b600435906001600160a01b038216820361014157565b602435906001600160a01b038216820361014157565b90601f8019910116810190811067ffffffffffffffff82111761057657604052565b634e487b7160e01b5f52604160045260245ffd5b6020818303126101415780519067ffffffffffffffff8211610141570181601f820112156101415780519067ffffffffffffffff821161057657604051926105dc601f8401601f191660200185610554565b8284526020838301011161014157815f9260208093018386015e8301015290565b6001600160a01b0390911681526040602080830182905283519183018290526060938291018484015e5f828201840152601f01601f191601019056fea2646970667358221220c2c8b4dbe48bb4d6a6c4f3923409fcdd3c9046aa5bb4726060d7edd37669b15564736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC20GetterHelper:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC20GetterHelper]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC20GetterHelper, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC20GetterHelper]]:
        return cls._deploy(request_type, [], return_tx, ERC20GetterHelper, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class ERC20TotalSupply:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#8)

        Attributes:
            token (IERC20): contract IERC20
            totalSupply (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'contract IERC20', 'name': 'token', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'totalSupply', 'type': 'uint256'}], 'name': 'ERC20TotalSupply', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ERC20TotalSupply'
        selector = bytes32(b'd\x85\xfdI\xc6h\xab1\xaanv\xb8\x18\xc9I/\x82\xe9\xa3r\x7f\x8d\xbd\x1d\xed\x1fzx[,\x98.')

        token: IERC20
        totalSupply: uint256


    @dataclasses.dataclass
    class ERC20BalanceOf:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#9)

        Attributes:
            token (IERC20): contract IERC20
            account (Address): address
            balanceOf (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'contract IERC20', 'name': 'token', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'account', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'balanceOf', 'type': 'uint256'}], 'name': 'ERC20BalanceOf', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ERC20BalanceOf'
        selector = bytes32(b'\xfa\x06\x99r\xe8\xd8\xe0\xf3"\x8d\xef\xb4M[|\x9b\xc6\xc3\xf0\x8e\xf9\x8b\xc7\xd6\xa3\x1aZ\xd2\x99:\x97\x95')

        token: IERC20
        account: Address
        balanceOf: uint256


    @dataclasses.dataclass
    class ERC20Allowance:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#10)

        Attributes:
            token (IERC20): contract IERC20
            owner (Address): address
            spender (Address): address
            allowance (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'contract IERC20', 'name': 'token', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': False, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'allowance', 'type': 'uint256'}], 'name': 'ERC20Allowance', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ERC20Allowance'
        selector = bytes32(b'\xe0\x9e\xed"KOQ\xd92\xc9\x80-\x15#ZN=\x83\xe6\xe9\x87F\xfb\xd1vr\xbf\xa0\xc6\x8c\xf2\xa5')

        token: IERC20
        owner: Address
        spender: Address
        allowance: uint256


    @dataclasses.dataclass
    class ERC20Name:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#11)

        Attributes:
            token (IERC20Metadata): contract IERC20Metadata
            name (str): string
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'contract IERC20Metadata', 'name': 'token', 'type': 'address'}, {'indexed': False, 'internalType': 'string', 'name': 'name', 'type': 'string'}], 'name': 'ERC20Name', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ERC20Name'
        selector = bytes32(b'\x04\x85\xcaSu\x88\x9f\x98\xba\xa3\xc2\xb6\xf4\xc5\x01\x7fBD]F\xa8\xea40\x181\xf4\xc0ej\xea\xef')

        token: IERC20Metadata
        name: str


    @dataclasses.dataclass
    class ERC20Symbol:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#12)

        Attributes:
            token (IERC20Metadata): contract IERC20Metadata
            symbol (str): string
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'contract IERC20Metadata', 'name': 'token', 'type': 'address'}, {'indexed': False, 'internalType': 'string', 'name': 'symbol', 'type': 'string'}], 'name': 'ERC20Symbol', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ERC20Symbol'
        selector = bytes32(b'&\xe0G\x05\xbb&\xa7\xef\xc4,/\xc2)SZ0\xfa\xa3\xff\xf9\xa0L\xd1^\xd4\xa7)\xc9\xbcM5\xbf')

        token: IERC20Metadata
        symbol: str


    @dataclasses.dataclass
    class ERC20Decimals:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#13)

        Attributes:
            token (IERC20Metadata): contract IERC20Metadata
            decimals (uint8): uint8
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'contract IERC20Metadata', 'name': 'token', 'type': 'address'}, {'indexed': False, 'internalType': 'uint8', 'name': 'decimals', 'type': 'uint8'}], 'name': 'ERC20Decimals', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ERC20Decimals'
        selector = bytes32(b'\x85\xbc\x87+\x16\xb9\xdb.J\xda7\x05s\xff\xd3\x96`+\xfd\xac\xec\x01\xf72\xf2\xb5\xaboB\xf2D5')

        token: IERC20Metadata
        decimals: uint8


    @overload
    def totalSupply(self, token: IERC20, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#15)

        Args:
            token: contract IERC20
        """
        ...

    @overload
    def totalSupply(self, token: IERC20, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#15)

        Args:
            token: contract IERC20
        """
        ...

    @overload
    def totalSupply(self, token: IERC20, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#15)

        Args:
            token: contract IERC20
        """
        ...

    @overload
    def totalSupply(self, token: IERC20, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#15)

        Args:
            token: contract IERC20
        """
        ...

    def totalSupply(self, token: IERC20, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#15)

        Args:
            token: contract IERC20
        """
        return self._execute(self.chain, request_type, "e4dc2aa4", [token], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def balanceOf(self, token: IERC20, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#19)

        Args:
            token: contract IERC20
            account: address
        """
        ...

    @overload
    def balanceOf(self, token: IERC20, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#19)

        Args:
            token: contract IERC20
            account: address
        """
        ...

    @overload
    def balanceOf(self, token: IERC20, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#19)

        Args:
            token: contract IERC20
            account: address
        """
        ...

    @overload
    def balanceOf(self, token: IERC20, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#19)

        Args:
            token: contract IERC20
            account: address
        """
        ...

    def balanceOf(self, token: IERC20, account: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#19)

        Args:
            token: contract IERC20
            account: address
        """
        return self._execute(self.chain, request_type, "f7888aec", [token, account], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def allowance(self, token: IERC20, owner: Union[Account, Address], spender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#23)

        Args:
            token: contract IERC20
            owner: address
            spender: address
        """
        ...

    @overload
    def allowance(self, token: IERC20, owner: Union[Account, Address], spender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#23)

        Args:
            token: contract IERC20
            owner: address
            spender: address
        """
        ...

    @overload
    def allowance(self, token: IERC20, owner: Union[Account, Address], spender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#23)

        Args:
            token: contract IERC20
            owner: address
            spender: address
        """
        ...

    @overload
    def allowance(self, token: IERC20, owner: Union[Account, Address], spender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#23)

        Args:
            token: contract IERC20
            owner: address
            spender: address
        """
        ...

    def allowance(self, token: IERC20, owner: Union[Account, Address], spender: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#23)

        Args:
            token: contract IERC20
            owner: address
            spender: address
        """
        return self._execute(self.chain, request_type, "927da105", [token, owner, spender], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def name(self, token: IERC20Metadata, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#27)

        Args:
            token: contract IERC20Metadata
        """
        ...

    @overload
    def name(self, token: IERC20Metadata, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#27)

        Args:
            token: contract IERC20Metadata
        """
        ...

    @overload
    def name(self, token: IERC20Metadata, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#27)

        Args:
            token: contract IERC20Metadata
        """
        ...

    @overload
    def name(self, token: IERC20Metadata, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#27)

        Args:
            token: contract IERC20Metadata
        """
        ...

    def name(self, token: IERC20Metadata, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#27)

        Args:
            token: contract IERC20Metadata
        """
        return self._execute(self.chain, request_type, "01984892", [token], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def symbol(self, token: IERC20Metadata, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#31)

        Args:
            token: contract IERC20Metadata
        """
        ...

    @overload
    def symbol(self, token: IERC20Metadata, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#31)

        Args:
            token: contract IERC20Metadata
        """
        ...

    @overload
    def symbol(self, token: IERC20Metadata, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#31)

        Args:
            token: contract IERC20Metadata
        """
        ...

    @overload
    def symbol(self, token: IERC20Metadata, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#31)

        Args:
            token: contract IERC20Metadata
        """
        ...

    def symbol(self, token: IERC20Metadata, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#31)

        Args:
            token: contract IERC20Metadata
        """
        return self._execute(self.chain, request_type, "a86e3576", [token], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def decimals(self, token: IERC20Metadata, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#35)

        Args:
            token: contract IERC20Metadata
        """
        ...

    @overload
    def decimals(self, token: IERC20Metadata, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#35)

        Args:
            token: contract IERC20Metadata
        """
        ...

    @overload
    def decimals(self, token: IERC20Metadata, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#35)

        Args:
            token: contract IERC20Metadata
        """
        ...

    @overload
    def decimals(self, token: IERC20Metadata, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#35)

        Args:
            token: contract IERC20Metadata
        """
        ...

    def decimals(self, token: IERC20Metadata, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/token/ERC20GetterHelper.sol#35)

        Args:
            token: contract IERC20Metadata
        """
        return self._execute(self.chain, request_type, "d449a832", [token], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC20GetterHelper.totalSupply.selector = bytes4(b'\xe4\xdc*\xa4')
ERC20GetterHelper.balanceOf.selector = bytes4(b'\xf7\x88\x8a\xec')
ERC20GetterHelper.allowance.selector = bytes4(b'\x92}\xa1\x05')
ERC20GetterHelper.name.selector = bytes4(b'\x01\x98H\x92')
ERC20GetterHelper.symbol.selector = bytes4(b'\xa8n5v')
ERC20GetterHelper.decimals.selector = bytes4(b'\xd4I\xa82')
