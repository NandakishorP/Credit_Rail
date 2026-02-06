
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum



class CompTimelock(Contract):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#29)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'address', 'name': 'admin_', 'type': 'address'}, {'internalType': 'uint256', 'name': 'delay_', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'/\xff\xc0\x91\xa5\x01\xfd\x91\xbf\xbf\xf2qAE\r:\xcb@\xfb\x8em\x83\x82\xb2C\xecz\x81*:\xaf\x87': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'txHash', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'address', 'name': 'target', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'signature', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'indexed': False, 'internalType': 'uint256', 'name': 'eta', 'type': 'uint256'}], 'name': 'CancelTransaction', 'type': 'event'}, b'\xa5`\xe3\x19\x80`\xa2\xf1\x06p\xc1\xec[@0w\xeaj\xe9<\xa8\xde\x1c2\xb4Q\xdc\x1a\x94<\xd6\xe7': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'txHash', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'address', 'name': 'target', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'signature', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'indexed': False, 'internalType': 'uint256', 'name': 'eta', 'type': 'uint256'}], 'name': 'ExecuteTransaction', 'type': 'event'}, b'qa@q\xb8\x8d\xee^\x0b*\xe5x\xa9\xdd{.\xbb\xe9\xae\x83+\xa4\x19\xdc\x02B\xcd\x06Z)\x0bl': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'newAdmin', 'type': 'address'}], 'name': 'NewAdmin', 'type': 'event'}, b'\x94\x8b\x1fjB\xee\x13\x8b~4\x05\x8b\xa8Z7\xf7\x16\xd5_\xf2_\xf0Zv?\x15\xbe\xd6\xa0L\x8d,': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'newDelay', 'type': 'uint256'}], 'name': 'NewDelay', 'type': 'event'}, b'i\xd7\x8e8\xa0\x19\x85\xfb\xb1F)a\x80\x9bK-eS\x1b\xc9;+\x94\x03\x7f34\xb8,\xa4\xa7V': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'newPendingAdmin', 'type': 'address'}], 'name': 'NewPendingAdmin', 'type': 'event'}, b'v\xe2ym\xc3\xa8\x1dW\xb0\xe8PKd\x7f\xeb\xcb\xee\xb5\xf4\xaf\x81\x8e\x16O\x11\xee\xf8\x13\x1ajv?': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'txHash', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'address', 'name': 'target', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'signature', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'indexed': False, 'internalType': 'uint256', 'name': 'eta', 'type': 'uint256'}], 'name': 'QueueTransaction', 'type': 'event'}, b'\xc1\xa2\x87\xe2': {'inputs': [], 'name': 'GRACE_PERIOD', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'}d_\xab': {'inputs': [], 'name': 'MAXIMUM_DELAY', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb1\xb4:\xe5': {'inputs': [], 'name': 'MINIMUM_DELAY', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x0e\x18\xb6\x81': {'inputs': [], 'name': 'acceptAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf8Q\xa4@': {'inputs': [], 'name': 'admin', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'Y\x1f\xcd\xfe': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'internalType': 'string', 'name': 'signature', 'type': 'string'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'internalType': 'uint256', 'name': 'eta', 'type': 'uint256'}], 'name': 'cancelTransaction', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'jB\xb8\xf8': {'inputs': [], 'name': 'delay', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x08%\xf3\x8f': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'internalType': 'string', 'name': 'signature', 'type': 'string'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'internalType': 'uint256', 'name': 'eta', 'type': 'uint256'}], 'name': 'executeTransaction', 'outputs': [{'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'stateMutability': 'payable', 'type': 'function'}, b'&x"G': {'inputs': [], 'name': 'pendingAdmin', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b':f\xf9\x01': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'internalType': 'string', 'name': 'signature', 'type': 'string'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'internalType': 'uint256', 'name': 'eta', 'type': 'uint256'}], 'name': 'queueTransaction', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xf2\xb0e7': {'inputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'queuedTransactions', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xe1w$n': {'inputs': [{'internalType': 'uint256', 'name': 'delay_', 'type': 'uint256'}], 'name': 'setDelay', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'M\xd1\x8b\xf5': {'inputs': [{'internalType': 'address', 'name': 'pendingAdmin_', 'type': 'address'}], 'name': 'setPendingAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, 'receive': {'stateMutability': 'payable', 'type': 'receive'}}
    _storage_layout = {"storage":[{"astId":66,"contract":"lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol:CompTimelock","label":"admin","offset":0,"slot":0,"type":"t_address"},{"astId":68,"contract":"lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol:CompTimelock","label":"pendingAdmin","offset":0,"slot":1,"type":"t_address"},{"astId":70,"contract":"lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol:CompTimelock","label":"delay","offset":0,"slot":2,"type":"t_uint256"},{"astId":74,"contract":"lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol:CompTimelock","label":"queuedTransactions","offset":0,"slot":3,"type":"t_mapping(t_bytes32,t_bool)"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_mapping(t_bytes32,t_bool)":{"encoding":"mapping","label":"mapping(bytes32 => bool)","numberOfBytes":32,"key":"t_bytes32","value":"t_bool"},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "60803461016657601f610e1c38819003918201601f19168301916001600160401b0383118484101761016a5780849260409485528339810103126101665780516001600160a01b03811691908290036101665760200151906202a30082106100fb5762278d008211610090575f80546001600160a01b031916919091179055600255604051610c9d908161017f8239f35b60405162461bcd60e51b815260206004820152603860248201527f54696d656c6f636b3a3a73657444656c61793a2044656c6179206d757374206e60448201527f6f7420657863656564206d6178696d756d2064656c61792e00000000000000006064820152608490fd5b60405162461bcd60e51b815260206004820152603760248201527f54696d656c6f636b3a3a636f6e7374727563746f723a2044656c6179206d757360448201527f7420657863656564206d696e696d756d2064656c61792e0000000000000000006064820152608490fd5b5f80fd5b634e487b7160e01b5f52604160045260245ffdfe6080604052600436101561001a575b3615610018575f80fd5b005b5f3560e01c80630825f38f146107645780630e18b6811461069c57806326782247146106745780633a66f901146104cc5780634dd18bf514610401578063591fcdfe146102fb5780636a42b8f8146102de5780637d645fab146102c1578063b1b43ae5146102a4578063c1a287e214610287578063e177246e14610107578063f2b06537146100d85763f851a4400361000e57346100d4575f3660031901126100d4575f546040516001600160a01b039091168152602090f35b5f80fd5b346100d45760203660031901126100d4576004355f526003602052602060ff60405f2054166040519015158152f35b346100d45760203660031901126100d457600435303303610228576202a30081106101c65762278d00811161016057806002557f948b1f6a42ee138b7e34058ba85a37f716d55ff25ff05a763f15bed6a04c8d2c5f80a2005b60405162461bcd60e51b815260206004820152603860248201527f54696d656c6f636b3a3a73657444656c61793a2044656c6179206d757374206e60448201527737ba1032bc31b2b2b21036b0bc34b6bab6903232b630bc9760411b6064820152608490fd5b60405162461bcd60e51b815260206004820152603460248201527f54696d656c6f636b3a3a73657444656c61793a2044656c6179206d75737420656044820152733c31b2b2b21036b4b734b6bab6903232b630bc9760611b6064820152608490fd5b60405162461bcd60e51b815260206004820152603160248201527f54696d656c6f636b3a3a73657444656c61793a2043616c6c206d75737420636f60448201527036b290333937b6902a34b6b2b637b1b59760791b6064820152608490fd5b346100d4575f3660031901126100d4576020604051621275008152f35b346100d4575f3660031901126100d45760206040516202a3008152f35b346100d4575f3660031901126100d457602060405162278d008152f35b346100d4575f3660031901126100d4576020600254604051908152f35b346100d45761030936610b26565b9190929360018060a01b035f5416330361039c576103977f2fffc091a501fd91bfbff27141450d3acb40fb8e6d8382b243ec7a812a3aaf87938660405161036a8161035c858b8a60208501978b89610bd7565b03601f198101835282610a9e565b51902095865f52600360205260405f2060ff19815416905560405194859460018060a01b03169885610c19565b0390a3005b60405162461bcd60e51b815260206004820152603760248201527f54696d656c6f636b3a3a63616e63656c5472616e73616374696f6e3a2043616c604482015276361036bab9ba1031b7b6b290333937b69030b236b4b71760491b6064820152608490fd5b346100d45760203660031901126100d4576004356001600160a01b038116908190036100d45730330361046657600180546001600160a01b031916821790557f69d78e38a01985fbb1462961809b4b2d65531bc93b2b94037f3334b82ca4a7565f80a2005b60405162461bcd60e51b815260206004820152603860248201527f54696d656c6f636b3a3a73657450656e64696e6741646d696e3a2043616c6c2060448201527736bab9ba1031b7b6b290333937b6902a34b6b2b637b1b59760411b6064820152608490fd5b346100d4576104da36610b26565b5f5492949093926001600160a01b031633036106105760025442018042116105fc57841061057f576020947f76e2796dc3a81d57b0e8504b647febcbeeb5f4af818e164f11eef8131a6a763f91610574604051888101906105438161035c8b8a898d8a89610bd7565b519020968795865f5260038a5260405f20600160ff1982541617905560405194859460018060a01b03169885610c19565b0390a3604051908152f35b60405162461bcd60e51b815260206004820152604960248201527f54696d656c6f636b3a3a71756575655472616e73616374696f6e3a204573746960448201527f6d6174656420657865637574696f6e20626c6f636b206d757374207361746973606482015268333c903232b630bc9760b91b608482015260a490fd5b634e487b7160e01b5f52601160045260245ffd5b60405162461bcd60e51b815260206004820152603660248201527f54696d656c6f636b3a3a71756575655472616e73616374696f6e3a2043616c6c6044820152751036bab9ba1031b7b6b290333937b69030b236b4b71760511b6064820152608490fd5b346100d4575f3660031901126100d4576001546040516001600160a01b039091168152602090f35b346100d4575f3660031901126100d4576001546001600160a01b03811633036106fe575f8054336001600160a01b03199182168117835592166001557f71614071b88dee5e0b2ae578a9dd7b2ebbe9ae832ba419dc0242cd065a290b6c9080a2005b60405162461bcd60e51b815260206004820152603860248201527f54696d656c6f636b3a3a61636365707441646d696e3a2043616c6c206d7573746044820152771031b7b6b290333937b6903832b73234b733a0b236b4b71760411b6064820152608490fd5b61076d36610b26565b5f5491949392916001600160a01b03163303610a3857604051602081019061079d8161035c858a888a8c89610bd7565b51902091825f52600360205260ff60405f205416156109e05781421061097a576212750082018083116105fc57421161092c575f838152600360205260409020805460ff191690558051806108e357505f80875b60208151910187895af1943d156108db573d9561080d87610ad4565b9661081b6040519889610a9e565b87523d5f602089013e5b15610883576108687fa560e3198060a2f10670c1ec5b403077ea6ae93ca8de1c32b451dc1a943cd6e79361087f9860405194859460018060a01b03169885610c19565b0390a3604051918291602083526020830190610bb3565b0390f35b60405162461bcd60e51b815260206004820152603d60248201525f516020610c485f395f51905f5260448201527f616e73616374696f6e20657865637574696f6e2072657665727465642e0000006064820152608490fd5b606095610825565b5f809163ffffffff60e01b9060208501201660405190602082015261092760248260208c8051918291018484015e810185838201520301601f198101835282610a9e565b6107f1565b60405162461bcd60e51b815260206004820152603360248201525f516020610c485f395f51905f5260448201527230b739b0b1ba34b7b71034b99039ba30b6329760691b6064820152608490fd5b60405162461bcd60e51b815260206004820152604560248201525f516020610c485f395f51905f5260448201527f616e73616374696f6e206861736e2774207375727061737365642074696d65206064820152643637b1b59760d91b608482015260a490fd5b60405162461bcd60e51b815260206004820152603d60248201525f516020610c485f395f51905f5260448201527f616e73616374696f6e206861736e2774206265656e207175657565642e0000006064820152608490fd5b60405162461bcd60e51b815260206004820152603860248201527f54696d656c6f636b3a3a657865637574655472616e73616374696f6e3a20436160448201527736361036bab9ba1031b7b6b290333937b69030b236b4b71760411b6064820152608490fd5b90601f8019910116810190811067ffffffffffffffff821117610ac057604052565b634e487b7160e01b5f52604160045260245ffd5b67ffffffffffffffff8111610ac057601f01601f191660200190565b929192610afc82610ad4565b91610b0a6040519384610a9e565b8294818452818301116100d4578281602093845f960137010152565b9060a06003198301126100d4576004356001600160a01b03811681036100d457916024359160443567ffffffffffffffff81116100d457826023820112156100d45782816024610b7b93600401359101610af0565b916064359067ffffffffffffffff82116100d457806023830112156100d457816024610bac93600401359101610af0565b9060843590565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b95949390608093610c1493610c069260018060a01b03168952602089015260a0604089015260a0880190610bb3565b908682036060880152610bb3565b930152565b949392610c39606093610c14938852608060208901526080880190610bb3565b908682036040880152610bb356fe54696d656c6f636b3a3a657865637574655472616e73616374696f6e3a205472a2646970667358221220c7be3899101473b7adf17d1db495b53a8ab64f6b67da4da659781401eeca79a264736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, admin_: Union[Account, Address], delay_: uint256, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#68)

        Args:
            admin_: address
            delay_: uint256
        """
        ...

    @overload
    @classmethod
    def deploy(cls, admin_: Union[Account, Address], delay_: uint256, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> CompTimelock:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#68)

        Args:
            admin_: address
            delay_: uint256
        """
        ...

    @overload
    @classmethod
    def deploy(cls, admin_: Union[Account, Address], delay_: uint256, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#68)

        Args:
            admin_: address
            delay_: uint256
        """
        ...

    @overload
    @classmethod
    def deploy(cls, admin_: Union[Account, Address], delay_: uint256, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#68)

        Args:
            admin_: address
            delay_: uint256
        """
        ...

    @overload
    @classmethod
    def deploy(cls, admin_: Union[Account, Address], delay_: uint256, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[CompTimelock]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#68)

        Args:
            admin_: address
            delay_: uint256
        """
        ...

    @classmethod
    def deploy(cls, admin_: Union[Account, Address], delay_: uint256, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, CompTimelock, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[CompTimelock]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#68)

        Args:
            admin_: address
            delay_: uint256
        """
        return cls._deploy(request_type, [admin_, delay_], return_tx, CompTimelock, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class NewAdmin:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#30)

        Attributes:
            newAdmin (Address): indexed address
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'newAdmin', 'type': 'address'}], 'name': 'NewAdmin', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'NewAdmin'
        selector = bytes32(b'qa@q\xb8\x8d\xee^\x0b*\xe5x\xa9\xdd{.\xbb\xe9\xae\x83+\xa4\x19\xdc\x02B\xcd\x06Z)\x0bl')

        newAdmin: Address


    @dataclasses.dataclass
    class NewPendingAdmin:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#31)

        Attributes:
            newPendingAdmin (Address): indexed address
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'newPendingAdmin', 'type': 'address'}], 'name': 'NewPendingAdmin', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'NewPendingAdmin'
        selector = bytes32(b'i\xd7\x8e8\xa0\x19\x85\xfb\xb1F)a\x80\x9bK-eS\x1b\xc9;+\x94\x03\x7f34\xb8,\xa4\xa7V')

        newPendingAdmin: Address


    @dataclasses.dataclass
    class NewDelay:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#32)

        Attributes:
            newDelay (uint256): indexed uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'uint256', 'name': 'newDelay', 'type': 'uint256'}], 'name': 'NewDelay', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'NewDelay'
        selector = bytes32(b'\x94\x8b\x1fjB\xee\x13\x8b~4\x05\x8b\xa8Z7\xf7\x16\xd5_\xf2_\xf0Zv?\x15\xbe\xd6\xa0L\x8d,')

        newDelay: uint256


    @dataclasses.dataclass
    class CancelTransaction:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#33)

        Attributes:
            txHash (bytes32): indexed bytes32
            target (Address): indexed address
            value (uint256): uint256
            signature (str): string
            data (bytearray): bytes
            eta (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'txHash', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'address', 'name': 'target', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'signature', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'indexed': False, 'internalType': 'uint256', 'name': 'eta', 'type': 'uint256'}], 'name': 'CancelTransaction', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'CancelTransaction'
        selector = bytes32(b'/\xff\xc0\x91\xa5\x01\xfd\x91\xbf\xbf\xf2qAE\r:\xcb@\xfb\x8em\x83\x82\xb2C\xecz\x81*:\xaf\x87')

        txHash: bytes32
        target: Address
        value: uint256
        signature: str
        data: bytearray
        eta: uint256


    @dataclasses.dataclass
    class ExecuteTransaction:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#41)

        Attributes:
            txHash (bytes32): indexed bytes32
            target (Address): indexed address
            value (uint256): uint256
            signature (str): string
            data (bytearray): bytes
            eta (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'txHash', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'address', 'name': 'target', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'signature', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'indexed': False, 'internalType': 'uint256', 'name': 'eta', 'type': 'uint256'}], 'name': 'ExecuteTransaction', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ExecuteTransaction'
        selector = bytes32(b'\xa5`\xe3\x19\x80`\xa2\xf1\x06p\xc1\xec[@0w\xeaj\xe9<\xa8\xde\x1c2\xb4Q\xdc\x1a\x94<\xd6\xe7')

        txHash: bytes32
        target: Address
        value: uint256
        signature: str
        data: bytearray
        eta: uint256


    @dataclasses.dataclass
    class QueueTransaction:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#49)

        Attributes:
            txHash (bytes32): indexed bytes32
            target (Address): indexed address
            value (uint256): uint256
            signature (str): string
            data (bytearray): bytes
            eta (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'txHash', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'address', 'name': 'target', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'indexed': False, 'internalType': 'string', 'name': 'signature', 'type': 'string'}, {'indexed': False, 'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'indexed': False, 'internalType': 'uint256', 'name': 'eta', 'type': 'uint256'}], 'name': 'QueueTransaction', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'QueueTransaction'
        selector = bytes32(b'v\xe2ym\xc3\xa8\x1dW\xb0\xe8PKd\x7f\xeb\xcb\xee\xb5\xf4\xaf\x81\x8e\x16O\x11\xee\xf8\x13\x1ajv?')

        txHash: bytes32
        target: Address
        value: uint256
        signature: str
        data: bytearray
        eta: uint256


    @overload
    def GRACE_PERIOD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#58)

        Returns:
            GRACE_PERIOD: uint256
        """
        ...

    @overload
    def GRACE_PERIOD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#58)

        Returns:
            GRACE_PERIOD: uint256
        """
        ...

    @overload
    def GRACE_PERIOD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#58)

        Returns:
            GRACE_PERIOD: uint256
        """
        ...

    @overload
    def GRACE_PERIOD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#58)

        Returns:
            GRACE_PERIOD: uint256
        """
        ...

    def GRACE_PERIOD(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#58)

        Returns:
            GRACE_PERIOD: uint256
        """
        return self._execute(self.chain, request_type, "c1a287e2", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def MINIMUM_DELAY(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#59)

        Returns:
            MINIMUM_DELAY: uint256
        """
        ...

    @overload
    def MINIMUM_DELAY(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#59)

        Returns:
            MINIMUM_DELAY: uint256
        """
        ...

    @overload
    def MINIMUM_DELAY(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#59)

        Returns:
            MINIMUM_DELAY: uint256
        """
        ...

    @overload
    def MINIMUM_DELAY(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#59)

        Returns:
            MINIMUM_DELAY: uint256
        """
        ...

    def MINIMUM_DELAY(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#59)

        Returns:
            MINIMUM_DELAY: uint256
        """
        return self._execute(self.chain, request_type, "b1b43ae5", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def MAXIMUM_DELAY(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#60)

        Returns:
            MAXIMUM_DELAY: uint256
        """
        ...

    @overload
    def MAXIMUM_DELAY(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#60)

        Returns:
            MAXIMUM_DELAY: uint256
        """
        ...

    @overload
    def MAXIMUM_DELAY(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#60)

        Returns:
            MAXIMUM_DELAY: uint256
        """
        ...

    @overload
    def MAXIMUM_DELAY(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#60)

        Returns:
            MAXIMUM_DELAY: uint256
        """
        ...

    def MAXIMUM_DELAY(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#60)

        Returns:
            MAXIMUM_DELAY: uint256
        """
        return self._execute(self.chain, request_type, "7d645fab", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def admin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#62)

        Returns:
            admin: address
        """
        ...

    @overload
    def admin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#62)

        Returns:
            admin: address
        """
        ...

    @overload
    def admin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#62)

        Returns:
            admin: address
        """
        ...

    @overload
    def admin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#62)

        Returns:
            admin: address
        """
        ...

    def admin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#62)

        Returns:
            admin: address
        """
        return self._execute(self.chain, request_type, "f851a440", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def pendingAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#63)

        Returns:
            pendingAdmin: address
        """
        ...

    @overload
    def pendingAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#63)

        Returns:
            pendingAdmin: address
        """
        ...

    @overload
    def pendingAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#63)

        Returns:
            pendingAdmin: address
        """
        ...

    @overload
    def pendingAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#63)

        Returns:
            pendingAdmin: address
        """
        ...

    def pendingAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#63)

        Returns:
            pendingAdmin: address
        """
        return self._execute(self.chain, request_type, "26782247", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def delay(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#64)

        Returns:
            delay: uint256
        """
        ...

    @overload
    def delay(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#64)

        Returns:
            delay: uint256
        """
        ...

    @overload
    def delay(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#64)

        Returns:
            delay: uint256
        """
        ...

    @overload
    def delay(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#64)

        Returns:
            delay: uint256
        """
        ...

    def delay(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#64)

        Returns:
            delay: uint256
        """
        return self._execute(self.chain, request_type, "6a42b8f8", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def queuedTransactions(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#66)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def queuedTransactions(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#66)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def queuedTransactions(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#66)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def queuedTransactions(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#66)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        ...

    def queuedTransactions(self, key0: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#66)

        Args:
            key0: bytes32
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "f2b06537", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setDelay(self, delay_: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#78)

        Args:
            delay_: uint256
        """
        ...

    @overload
    def setDelay(self, delay_: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#78)

        Args:
            delay_: uint256
        """
        ...

    @overload
    def setDelay(self, delay_: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#78)

        Args:
            delay_: uint256
        """
        ...

    @overload
    def setDelay(self, delay_: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#78)

        Args:
            delay_: uint256
        """
        ...

    def setDelay(self, delay_: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#78)

        Args:
            delay_: uint256
        """
        return self._execute(self.chain, request_type, "e177246e", [delay_], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def acceptAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#87)
        """
        ...

    @overload
    def acceptAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#87)
        """
        ...

    @overload
    def acceptAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#87)
        """
        ...

    @overload
    def acceptAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#87)
        """
        ...

    def acceptAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#87)
        """
        return self._execute(self.chain, request_type, "0e18b681", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setPendingAdmin(self, pendingAdmin_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#95)

        Args:
            pendingAdmin_: address
        """
        ...

    @overload
    def setPendingAdmin(self, pendingAdmin_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#95)

        Args:
            pendingAdmin_: address
        """
        ...

    @overload
    def setPendingAdmin(self, pendingAdmin_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#95)

        Args:
            pendingAdmin_: address
        """
        ...

    @overload
    def setPendingAdmin(self, pendingAdmin_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#95)

        Args:
            pendingAdmin_: address
        """
        ...

    def setPendingAdmin(self, pendingAdmin_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#95)

        Args:
            pendingAdmin_: address
        """
        return self._execute(self.chain, request_type, "4dd18bf5", [pendingAdmin_], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def queueTransaction(self, target: Union[Account, Address], value_: uint256, signature: str, data: Union[bytearray, bytes], eta: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#102)

        Args:
            target: address
            value_: uint256
            signature: string
            data: bytes
            eta: uint256
        Returns:
            bytes32
        """
        ...

    @overload
    def queueTransaction(self, target: Union[Account, Address], value_: uint256, signature: str, data: Union[bytearray, bytes], eta: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#102)

        Args:
            target: address
            value_: uint256
            signature: string
            data: bytes
            eta: uint256
        Returns:
            bytes32
        """
        ...

    @overload
    def queueTransaction(self, target: Union[Account, Address], value_: uint256, signature: str, data: Union[bytearray, bytes], eta: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#102)

        Args:
            target: address
            value_: uint256
            signature: string
            data: bytes
            eta: uint256
        Returns:
            bytes32
        """
        ...

    @overload
    def queueTransaction(self, target: Union[Account, Address], value_: uint256, signature: str, data: Union[bytearray, bytes], eta: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#102)

        Args:
            target: address
            value_: uint256
            signature: string
            data: bytes
            eta: uint256
        Returns:
            bytes32
        """
        ...

    def queueTransaction(self, target: Union[Account, Address], value_: uint256, signature: str, data: Union[bytearray, bytes], eta: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#102)

        Args:
            target: address
            value_: uint256
            signature: string
            data: bytes
            eta: uint256
        Returns:
            bytes32
        """
        return self._execute(self.chain, request_type, "3a66f901", [target, value_, signature, data, eta], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def cancelTransaction(self, target: Union[Account, Address], value_: uint256, signature: str, data: Union[bytearray, bytes], eta: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#122)

        Args:
            target: address
            value_: uint256
            signature: string
            data: bytes
            eta: uint256
        """
        ...

    @overload
    def cancelTransaction(self, target: Union[Account, Address], value_: uint256, signature: str, data: Union[bytearray, bytes], eta: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#122)

        Args:
            target: address
            value_: uint256
            signature: string
            data: bytes
            eta: uint256
        """
        ...

    @overload
    def cancelTransaction(self, target: Union[Account, Address], value_: uint256, signature: str, data: Union[bytearray, bytes], eta: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#122)

        Args:
            target: address
            value_: uint256
            signature: string
            data: bytes
            eta: uint256
        """
        ...

    @overload
    def cancelTransaction(self, target: Union[Account, Address], value_: uint256, signature: str, data: Union[bytearray, bytes], eta: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#122)

        Args:
            target: address
            value_: uint256
            signature: string
            data: bytes
            eta: uint256
        """
        ...

    def cancelTransaction(self, target: Union[Account, Address], value_: uint256, signature: str, data: Union[bytearray, bytes], eta: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#122)

        Args:
            target: address
            value_: uint256
            signature: string
            data: bytes
            eta: uint256
        """
        return self._execute(self.chain, request_type, "591fcdfe", [target, value_, signature, data, eta], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def executeTransaction(self, target: Union[Account, Address], value_: uint256, signature: str, data: Union[bytearray, bytes], eta: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#137)

        Args:
            target: address
            value_: uint256
            signature: string
            data: bytes
            eta: uint256
        Returns:
            bytes
        """
        ...

    @overload
    def executeTransaction(self, target: Union[Account, Address], value_: uint256, signature: str, data: Union[bytearray, bytes], eta: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#137)

        Args:
            target: address
            value_: uint256
            signature: string
            data: bytes
            eta: uint256
        Returns:
            bytes
        """
        ...

    @overload
    def executeTransaction(self, target: Union[Account, Address], value_: uint256, signature: str, data: Union[bytearray, bytes], eta: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#137)

        Args:
            target: address
            value_: uint256
            signature: string
            data: bytes
            eta: uint256
        Returns:
            bytes
        """
        ...

    @overload
    def executeTransaction(self, target: Union[Account, Address], value_: uint256, signature: str, data: Union[bytearray, bytes], eta: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytearray]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#137)

        Args:
            target: address
            value_: uint256
            signature: string
            data: bytes
            eta: uint256
        Returns:
            bytes
        """
        ...

    def executeTransaction(self, target: Union[Account, Address], value_: uint256, signature: str, data: Union[bytearray, bytes], eta: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, TransactionAbc[bytearray], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/mocks/compound/CompTimelock.sol#137)

        Args:
            target: address
            value_: uint256
            signature: string
            data: bytes
            eta: uint256
        Returns:
            bytes
        """
        return self._execute(self.chain, request_type, "0825f38f", [target, value_, signature, data, eta], True if request_type == "tx" else False, bytearray, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

CompTimelock.GRACE_PERIOD.selector = bytes4(b'\xc1\xa2\x87\xe2')
CompTimelock.MINIMUM_DELAY.selector = bytes4(b'\xb1\xb4:\xe5')
CompTimelock.MAXIMUM_DELAY.selector = bytes4(b'}d_\xab')
CompTimelock.admin.selector = bytes4(b'\xf8Q\xa4@')
CompTimelock.pendingAdmin.selector = bytes4(b'&x"G')
CompTimelock.delay.selector = bytes4(b'jB\xb8\xf8')
CompTimelock.queuedTransactions.selector = bytes4(b'\xf2\xb0e7')
CompTimelock.setDelay.selector = bytes4(b'\xe1w$n')
CompTimelock.acceptAdmin.selector = bytes4(b'\x0e\x18\xb6\x81')
CompTimelock.setPendingAdmin.selector = bytes4(b'M\xd1\x8b\xf5')
CompTimelock.queueTransaction.selector = bytes4(b':f\xf9\x01')
CompTimelock.cancelTransaction.selector = bytes4(b'Y\x1f\xcd\xfe')
CompTimelock.executeTransaction.selector = bytes4(b'\x08%\xf3\x8f')
