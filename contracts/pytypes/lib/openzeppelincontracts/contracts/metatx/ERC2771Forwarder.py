
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.utils.Nonces import Nonces
from pytypes.lib.openzeppelincontracts.contracts.utils.cryptography.EIP712 import EIP712



class ERC2771Forwarder(Nonces, EIP712):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#51)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'string', 'name': 'name', 'type': 'string'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\x94\xee\xf5\x8a': {'inputs': [{'internalType': 'uint48', 'name': 'deadline', 'type': 'uint48'}], 'name': 'ERC2771ForwarderExpiredRequest', 'type': 'error'}, b'\xc8E\xa0V': {'inputs': [{'internalType': 'address', 'name': 'signer', 'type': 'address'}, {'internalType': 'address', 'name': 'from', 'type': 'address'}], 'name': 'ERC2771ForwarderInvalidSigner', 'type': 'error'}, b'pd\x7fy': {'inputs': [{'internalType': 'uint256', 'name': 'requestedValue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'msgValue', 'type': 'uint256'}], 'name': 'ERC2771ForwarderMismatchedValue', 'type': 'error'}, b'\xd2e\x0c\xd1': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'address', 'name': 'forwarder', 'type': 'address'}], 'name': 'ERC2771UntrustfulTarget', 'type': 'error'}, b'\xd6\xbd\xa2u': {'inputs': [], 'name': 'FailedCall', 'type': 'error'}, b'\xcfG\x91\x81': {'inputs': [{'internalType': 'uint256', 'name': 'balance', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'needed', 'type': 'uint256'}], 'name': 'InsufficientBalance', 'type': 'error'}, b'u-\x88\xc0': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'uint256', 'name': 'currentNonce', 'type': 'uint256'}], 'name': 'InvalidAccountNonce', 'type': 'error'}, b'\xb3Q+\x0c': {'inputs': [], 'name': 'InvalidShortString', 'type': 'error'}, b"0Z'\xa9": {'inputs': [{'internalType': 'string', 'name': 'str', 'type': 'string'}], 'name': 'StringTooLong', 'type': 'error'}, b'\nc\x87\xc9\xea6(\xb8\x8ac;\xb4\xf3\xb1Qw\x0fp\x08Q\x17\xa1_\x9b\xf3x|\xdaS\xf1=1': {'anonymous': False, 'inputs': [], 'name': 'EIP712DomainChanged', 'type': 'event'}, b'\x84/\xb2J\x83y5XXz=\xab+\xe7gM\xa4\xa5\x1d\t\xc5T-m\xd3T\xe5\xd0\xeap\x81<': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'signer', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'nonce', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bool', 'name': 'success', 'type': 'bool'}], 'name': 'ExecutedForwardRequest', 'type': 'event'}, b'\x84\xb0\x19n': {'inputs': [], 'name': 'eip712Domain', 'outputs': [{'internalType': 'bytes1', 'name': 'fields', 'type': 'bytes1'}, {'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'string', 'name': 'version', 'type': 'string'}, {'internalType': 'uint256', 'name': 'chainId', 'type': 'uint256'}, {'internalType': 'address', 'name': 'verifyingContract', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'salt', 'type': 'bytes32'}, {'internalType': 'uint256[]', 'name': 'extensions', 'type': 'uint256[]'}], 'stateMutability': 'view', 'type': 'function'}, b'\xdf\x90\\\xaf': {'inputs': [{'components': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'gas', 'type': 'uint256'}, {'internalType': 'uint48', 'name': 'deadline', 'type': 'uint48'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'internalType': 'bytes', 'name': 'signature', 'type': 'bytes'}], 'internalType': 'struct ERC2771Forwarder.ForwardRequestData', 'name': 'request', 'type': 'tuple'}], 'name': 'execute', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, b'\xcc\xf9kJ': {'inputs': [{'components': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'gas', 'type': 'uint256'}, {'internalType': 'uint48', 'name': 'deadline', 'type': 'uint48'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'internalType': 'bytes', 'name': 'signature', 'type': 'bytes'}], 'internalType': 'struct ERC2771Forwarder.ForwardRequestData[]', 'name': 'requests', 'type': 'tuple[]'}, {'internalType': 'address payable', 'name': 'refundReceiver', 'type': 'address'}], 'name': 'executeBatch', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, b'~\xce\xbe\x00': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'nonces', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x19\xd8\xd3\x8c': {'inputs': [{'components': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'gas', 'type': 'uint256'}, {'internalType': 'uint48', 'name': 'deadline', 'type': 'uint48'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}, {'internalType': 'bytes', 'name': 'signature', 'type': 'bytes'}], 'internalType': 'struct ERC2771Forwarder.ForwardRequestData', 'name': 'request', 'type': 'tuple'}], 'name': 'verify', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":44477,"contract":"lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol:ERC2771Forwarder","label":"_nameFallback","offset":0,"slot":0,"type":"t_string_storage"},{"astId":44479,"contract":"lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol:ERC2771Forwarder","label":"_versionFallback","offset":0,"slot":1,"type":"t_string_storage"},{"astId":42054,"contract":"lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol:ERC2771Forwarder","label":"_nonces","offset":0,"slot":2,"type":"t_mapping(t_address,t_uint256)"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_mapping(t_address,t_uint256)":{"encoding":"mapping","label":"mapping(address => uint256)","numberOfBytes":32,"key":"t_address","value":"t_uint256"},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32}}}
    _creation_code = "610160806040523461018957611283803803809161001d82856101a1565b8339810190602081830312610189578051906001600160401b03821161018957019080601f830112156101895781516001600160401b03811161018d5760405192610072601f8301601f1916602001856101a1565b81845260208401926020838301011161018957815f926020809301855e840101526040918251916100a384846101a1565b600183526020830191603160f81b83526100bc816101c4565b610120526100c984610366565b61014052519020918260e05251902080610100524660a05282519060208201927f8b73c3c69bb8fe3d512ecc4cf759cc79239f7b179b0ffacaa9a75d522b39400f84528483015260608201524660808201523060a082015260a0815261013060c0826101a1565b5190206080523060c05251610dd890816104ab823960805181610c3c015260a05181610cf9015260c05181610c06015260e05181610c8b01526101005181610cb101526101205181610492015261014051816104bb0152f35b5f80fd5b634e487b7160e01b5f52604160045260245ffd5b601f909101601f19168101906001600160401b0382119082101761018d57604052565b908151602081105f1461023e575090601f8151116101fe5760208151910151602082106101ef571790565b5f198260200360031b1b161790565b604460209160405192839163305a27a960e01b83528160048401528051918291826024860152018484015e5f828201840152601f01601f19168101030190fd5b6001600160401b03811161018d575f54600181811c9116801561035c575b602082101461034857601f811161030a575b50602092601f82116001146102ab57928192935f926102a0575b50508160011b915f199060031b1c1916175f5560ff90565b015190505f80610288565b601f198216935f8052805f20915f5b8681106102f257508360019596106102da575b505050811b015f5560ff90565b01515f1960f88460031b161c191690555f80806102cd565b919260206001819286850151815501940192016102ba565b8181111561026e575f805260205f20601f80840160051c809201920160051c03905f5b82811061033b57505061026e565b5f8282015560010161032d565b634e487b7160e01b5f52602260045260245ffd5b90607f169061025c565b908151602081105f14610391575090601f8151116101fe5760208151910151602082106101ef571790565b6001600160401b03811161018d57600154600181811c911680156104a0575b602082101461034857601f8111610461575b50602092601f821160011461040057928192935f926103f5575b50508160011b915f199060031b1c19161760015560ff90565b015190505f806103dc565b601f1982169360015f52805f20915f5b8681106104495750836001959610610431575b505050811b0160015560ff90565b01515f1960f88460031b161c191690555f8080610423565b91926020600181928685015181550194019201610410565b818111156103c25760015f5260205f20601f80840160051c809201920160051c03905f5b8281106104935750506103c2565b5f82820155600101610485565b90607f16906103b056fe60806040526004361015610011575f80fd5b5f3560e01c806319d8d38c146105b85780637ecebe001461057257806384b0196e1461047a578063ccf96b4a146102325763df905caf14610050575f80fd5b610059366105fa565b60408101359081340361021b575f9161007182610706565b92919082156101eb5781156101c5578015610197578261018f575b5081610187575b506100b2575b505050156100a357005b63d6bda27560e01b5f5260045ffd5b9091925060018060a01b031690815f5260026020525f8060408120928354936001850190556060860135956100e9602082016106df565b9161010961013c6014602061010160a0870187610903565b9490966106df565b9360405194818692848401998a378201906001600160601b03199060601b16838201520301600b19810184520182610652565b519288f192603f5a9104116101855760407f842fb24a83793558587a3dab2be7674da4a51d09c5542d6dd354e5d0ea70813c9181519081528415156020820152a25f8080610099565bfe5b90505f610093565b91505f61008c565b836101a1876106df565b636422d02b60e11b5f9081526001600160a01b039283166004529116602452604490fd5b65ffffffffffff6101d8608088016106f3565b634a777ac560e11b5f521660045260245ffd5b6101f7602087016106df565b63d2650cd160e01b5f9081526001600160a01b039190911660045230602452604490fd5b506370647f7960e01b5f526004523460245260445ffd5b60403660031901126104765760043567ffffffffffffffff8111610476573660238201121561047657806004013567ffffffffffffffff8111610476576024820191602436918360051b01011161047657602435916001600160a01b0383168084036104765715915f915f935f925b8084106102dc57505050503481036102c65750806102bb57005b6102c491610936565b005b6370647f7960e01b5f526004523460245260445ffd5b909192936102f99060406102f1878588610688565b0135906106be565b93610305818386610688565b5f908461031182610706565b9361043c575b82610434575b508161042c575b50610359575b50501561033d575b6001019291906102a1565b9461035160019160406102f1898689610688565b959050610332565b90915060018060a01b0316805f52600260205260405f208054906001820190555f80606085013594604061038f602083016106df565b61039c60a0840184610903565b6103e1601460206103af889795976106df565b938551948186928484019a8b378201906001600160601b03199060601b16838201520301600b19810184520182610652565b519301359088f192603f5a9104116101855760407f842fb24a83793558587a3dab2be7674da4a51d09c5542d6dd354e5d0ea70813c9181519081528415156020820152a2888061032a565b90508b610324565b91508c61031d565b821561046a578115610457578061031757836101a1866106df565b65ffffffffffff6101d8608087016106f3565b6101f7602086016106df565b5f80fd5b34610476575f366003190112610476576105166104b67f00000000000000000000000000000000000000000000000000000000000000006109d3565b6104df7f0000000000000000000000000000000000000000000000000000000000000000610af9565b6020610524604051926104f28385610652565b5f84525f368137604051958695600f60f81b875260e08588015260e087019061062e565b90858203604087015261062e565b4660608501523060808501525f60a085015283810360c08501528180845192838152019301915f5b82811061055b57505050500390f35b83518552869550938101939281019260010161054c565b34610476576020366003190112610476576004356001600160a01b0381168103610476576001600160a01b03165f90815260026020908152604090912054604051908152f35b346104765760206105d06105cb366105fa565b610706565b5090826105f2575b50816105ea575b506040519015158152f35b9050826105df565b9150836105d8565b6020600319820112610476576004359067ffffffffffffffff82116104765760e09082900360031901126104765760040190565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b90601f8019910116810190811067ffffffffffffffff82111761067457604052565b634e487b7160e01b5f52604160045260245ffd5b91908110156106aa5760051b8101359060de1981360301821215610476570190565b634e487b7160e01b5f52603260045260245ffd5b919082018092116106cb57565b634e487b7160e01b5f52601160045260245ffd5b356001600160a01b03811681036104765790565b3565ffffffffffff811681036104765790565b90610710826106df565b60208301916108346042610723856106df565b9361074a610730886106df565b6001600160a01b03165f9081526002602052604090205490565b94608088019565ffffffffffff610760886106f3565b61077761077060a08d018d610903565b369161098d565b60208151910120926040519460208601967f7f96328b83274ebc7c1cf4f7a3abda602b51a78b7fa1d86a2ce353d75e587cac885260018060a01b0316604087015260018060a01b0316606086015260408c0135608086015260608c013560a086015260c08501521660e083015261010082015261010081526107fb61012082610652565b519020610806610c03565b906040519161190160f01b8352600283015260228201522061082e61077060c0880188610903565b90610bc9565b5060048194929410156108ef575f61084f60209215966106df565b6040518381019063572b6c0560e01b825230602482015260248152610875604482610652565b51915afa903d5f5190836108e3575b50826108d7575b50610895906106f3565b94846108af575b509365ffffffffffff4291161015929190565b9093506001600160a01b03906108c4906106df565b166001600160a01b03831614925f61089c565b1515915061089561088b565b6020111592505f610884565b634e487b7160e01b5f52602160045260245ffd5b903590601e1981360301821215610476570180359067ffffffffffffffff82116104765760200191813603831361047657565b814710610976575f808093819382604051610952602082610652565b526001600160a01b03165af11561096557565b3d156100a3576040513d5f823e3d90fd5b504763cf47918160e01b5f5260045260245260445ffd5b92919267ffffffffffffffff821161067457604051916109b7601f8201601f191660200184610652565b829481845281830111610476578281602093845f960137010152565b60ff8114610a195760ff811690601f8211610a0a57604051916109f7604084610652565b6020808452838101919036833783525290565b632cd44ac360e21b5f5260045ffd5b506040515f5f548060011c9160018216918215610aef575b602084108314610adb578385528492908115610abc5750600114610a5f575b610a5c92500382610652565b90565b505f80805290917f290decd9548b62a8d60345a988386fc84ba6bc95484008f6362f93160ef3e5635b818310610aa0575050906020610a5c92820101610a50565b6020919350806001915483858801015201910190918392610a88565b60209250610a5c94915060ff191682840152151560051b820101610a50565b634e487b7160e01b5f52602260045260245ffd5b92607f1692610a31565b60ff8114610b1d5760ff811690601f8211610a0a57604051916109f7604084610652565b506040515f6001548060011c9160018216918215610bbf575b602084108314610adb578385528492908115610abc5750600114610b6057610a5c92500382610652565b5060015f90815290917fb10e2d527612073b26eecdfd717e6a320cf44b4afac2b0732d9fcbe2b7fa0cf65b818310610ba3575050906020610a5c92820101610a50565b6020919350806001915483858801015201910190918392610b8b565b92607f1692610b36565b8151919060418303610bf957610bf29250602082015190606060408401519301515f1a90610d1f565b9192909190565b50505f9160029190565b307f00000000000000000000000000000000000000000000000000000000000000006001600160a01b03161480610cf6575b15610c5e577f000000000000000000000000000000000000000000000000000000000000000090565b60405160208101907f8b73c3c69bb8fe3d512ecc4cf759cc79239f7b179b0ffacaa9a75d522b39400f82527f000000000000000000000000000000000000000000000000000000000000000060408201527f000000000000000000000000000000000000000000000000000000000000000060608201524660808201523060a082015260a08152610cf060c082610652565b51902090565b507f00000000000000000000000000000000000000000000000000000000000000004614610c35565b91906fa2a8918ca85bafe22016d0b997e4df60600160ff1b038411610d97579160209360809260ff5f9560405194855216868401526040830152606082015282805260015afa15610d8c575f516001600160a01b03811615610d8257905f905f90565b505f906001905f90565b6040513d5f823e3d90fd5b5050505f916003919056fea2646970667358221220b7abaea0067e6b3219da9ef38696627f49c60785265e14e49070ed4d49a4907c64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, name: str, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#101)

        Args:
            name: string
        """
        ...

    @overload
    @classmethod
    def deploy(cls, name: str, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC2771Forwarder:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#101)

        Args:
            name: string
        """
        ...

    @overload
    @classmethod
    def deploy(cls, name: str, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#101)

        Args:
            name: string
        """
        ...

    @overload
    @classmethod
    def deploy(cls, name: str, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#101)

        Args:
            name: string
        """
        ...

    @overload
    @classmethod
    def deploy(cls, name: str, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC2771Forwarder]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#101)

        Args:
            name: string
        """
        ...

    @classmethod
    def deploy(cls, name: str, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC2771Forwarder, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC2771Forwarder]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#101)

        Args:
            name: string
        """
        return cls._deploy(request_type, [name], return_tx, ERC2771Forwarder, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class ForwardRequestData:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#54)

        Attributes:
            from_ (Address): address
            to (Address): address
            value (uint256): uint256
            gas (uint256): uint256
            deadline (uint48): uint48
            data (bytearray): bytes
            signature (bytearray): bytes
        """
        original_name = 'ForwardRequestData'

        from_: Address = dataclasses.field(metadata={"original_name": "from"})
        to: Address
        value: uint256
        gas: uint256
        deadline: uint48
        data: bytearray
        signature: bytearray


    @dataclasses.dataclass
    class ERC2771ForwarderInvalidSigner(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#81)

        Attributes:
            signer (Address): address
            from_ (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'signer', 'type': 'address'}, {'internalType': 'address', 'name': 'from', 'type': 'address'}], 'name': 'ERC2771ForwarderInvalidSigner', 'type': 'error'}
        original_name = 'ERC2771ForwarderInvalidSigner'
        selector = bytes4(b'\xc8E\xa0V')

        signer: Address
        from_: Address = dataclasses.field(metadata={"original_name": "from"})


    @dataclasses.dataclass
    class ERC2771ForwarderMismatchedValue(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#86)

        Attributes:
            requestedValue (uint256): uint256
            msgValue (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'requestedValue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'msgValue', 'type': 'uint256'}], 'name': 'ERC2771ForwarderMismatchedValue', 'type': 'error'}
        original_name = 'ERC2771ForwarderMismatchedValue'
        selector = bytes4(b'pd\x7fy')

        requestedValue: uint256
        msgValue: uint256


    @dataclasses.dataclass
    class ERC2771ForwarderExpiredRequest(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#91)

        Attributes:
            deadline (uint48): uint48
        """
        _abi = {'inputs': [{'internalType': 'uint48', 'name': 'deadline', 'type': 'uint48'}], 'name': 'ERC2771ForwarderExpiredRequest', 'type': 'error'}
        original_name = 'ERC2771ForwarderExpiredRequest'
        selector = bytes4(b'\x94\xee\xf5\x8a')

        deadline: uint48


    @dataclasses.dataclass
    class ERC2771UntrustfulTarget(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#96)

        Attributes:
            target (Address): address
            forwarder (Address): address
        """
        _abi = {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}, {'internalType': 'address', 'name': 'forwarder', 'type': 'address'}], 'name': 'ERC2771UntrustfulTarget', 'type': 'error'}
        original_name = 'ERC2771UntrustfulTarget'
        selector = bytes4(b'\xd2e\x0c\xd1')

        target: Address
        forwarder: Address


    @dataclasses.dataclass
    class ExecutedForwardRequest:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#76)

        Attributes:
            signer (Address): indexed address
            nonce (uint256): uint256
            success (bool): bool
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'signer', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'nonce', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bool', 'name': 'success', 'type': 'bool'}], 'name': 'ExecutedForwardRequest', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'ExecutedForwardRequest'
        selector = bytes32(b'\x84/\xb2J\x83y5XXz=\xab+\xe7gM\xa4\xa5\x1d\t\xc5T-m\xd3T\xe5\xd0\xeap\x81<')

        signer: Address
        nonce: uint256
        success: bool


    @overload
    def verify(self, request: ERC2771Forwarder.ForwardRequestData, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#112)

        Args:
            request: struct ERC2771Forwarder.ForwardRequestData
        Returns:
            bool
        """
        ...

    @overload
    def verify(self, request: ERC2771Forwarder.ForwardRequestData, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#112)

        Args:
            request: struct ERC2771Forwarder.ForwardRequestData
        Returns:
            bool
        """
        ...

    @overload
    def verify(self, request: ERC2771Forwarder.ForwardRequestData, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#112)

        Args:
            request: struct ERC2771Forwarder.ForwardRequestData
        Returns:
            bool
        """
        ...

    @overload
    def verify(self, request: ERC2771Forwarder.ForwardRequestData, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#112)

        Args:
            request: struct ERC2771Forwarder.ForwardRequestData
        Returns:
            bool
        """
        ...

    def verify(self, request: ERC2771Forwarder.ForwardRequestData, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#112)

        Args:
            request: struct ERC2771Forwarder.ForwardRequestData
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "19d8d38c", [request], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def execute(self, request: ERC2771Forwarder.ForwardRequestData, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#127)

        Args:
            request: struct ERC2771Forwarder.ForwardRequestData
        """
        ...

    @overload
    def execute(self, request: ERC2771Forwarder.ForwardRequestData, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#127)

        Args:
            request: struct ERC2771Forwarder.ForwardRequestData
        """
        ...

    @overload
    def execute(self, request: ERC2771Forwarder.ForwardRequestData, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#127)

        Args:
            request: struct ERC2771Forwarder.ForwardRequestData
        """
        ...

    @overload
    def execute(self, request: ERC2771Forwarder.ForwardRequestData, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#127)

        Args:
            request: struct ERC2771Forwarder.ForwardRequestData
        """
        ...

    def execute(self, request: ERC2771Forwarder.ForwardRequestData, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#127)

        Args:
            request: struct ERC2771Forwarder.ForwardRequestData
        """
        return self._execute(self.chain, request_type, "df905caf", [request], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def executeBatch(self, requests: List[ERC2771Forwarder.ForwardRequestData], refundReceiver: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#163)

        Args:
            requests: struct ERC2771Forwarder.ForwardRequestData[]
            refundReceiver: address payable
        """
        ...

    @overload
    def executeBatch(self, requests: List[ERC2771Forwarder.ForwardRequestData], refundReceiver: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#163)

        Args:
            requests: struct ERC2771Forwarder.ForwardRequestData[]
            refundReceiver: address payable
        """
        ...

    @overload
    def executeBatch(self, requests: List[ERC2771Forwarder.ForwardRequestData], refundReceiver: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#163)

        Args:
            requests: struct ERC2771Forwarder.ForwardRequestData[]
            refundReceiver: address payable
        """
        ...

    @overload
    def executeBatch(self, requests: List[ERC2771Forwarder.ForwardRequestData], refundReceiver: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#163)

        Args:
            requests: struct ERC2771Forwarder.ForwardRequestData[]
            refundReceiver: address payable
        """
        ...

    def executeBatch(self, requests: List[ERC2771Forwarder.ForwardRequestData], refundReceiver: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/metatx/ERC2771Forwarder.sol#163)

        Args:
            requests: struct ERC2771Forwarder.ForwardRequestData[]
            refundReceiver: address payable
        """
        return self._execute(self.chain, request_type, "ccf96b4a", [requests, refundReceiver], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC2771Forwarder.verify.selector = bytes4(b'\x19\xd8\xd3\x8c')
ERC2771Forwarder.execute.selector = bytes4(b'\xdf\x90\\\xaf')
ERC2771Forwarder.executeBatch.selector = bytes4(b'\xcc\xf9kJ')
