
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.interfaces.IERC7913 import IERC7913SignatureVerifier



class ERC7913WebAuthnVerifier(IERC7913SignatureVerifier):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/verifiers/ERC7913WebAuthnVerifier.sol#23)
    """
    _abi = {b'\x02J\xd3\x18': {'inputs': [{'internalType': 'bytes', 'name': 'key', 'type': 'bytes'}, {'internalType': 'bytes32', 'name': 'hash', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': 'signature', 'type': 'bytes'}], 'name': 'verify', 'outputs': [{'internalType': 'bytes4', 'name': '', 'type': 'bytes4'}], 'stateMutability': 'view', 'type': 'function'}}
    _storage_layout = {"storage":[]}
    _creation_code = "60808060405234601557611231908161001a8239f35b5f80fdfe60806040526004361015610011575f80fd5b5f3560e01c63024ad31814610024575f80fd5b3461047f57606036600319011261047f576004356001600160401b03811161047f576100549036906004016104a2565b906044356001600160401b03811161047f5761007761007d9136906004016104a2565b9061059d565b909283610497575b836100c1575b5050505f146100b157602062495a6360e31b5b6040516001600160e01b03199091168152f35b60206001600160e01b031961009e565b90919250604051926024356020850152602084526100e06040856104ea565b8160201161047f5780359160401161047f57602001359060c08336031261047f576040519260c084018481106001600160401b03821117610483576040528035845260208401906020810135825260408501906040810135825260608601966060820135885260808201356001600160401b03811161047f57820136601f8201121561047f5761017790369060208135910161055a565b916080880192835260a0810135906001600160401b03821161047f570136601f8201121561047f576101b090369060208135910161055a565b60a0880193818552602484515111998a61043d575b5089610343575b50505086610322575b86610301575b866102b4575b866101f5575b5050505050505f808061008b565b602080929394959697505f91519351604051918183925191829101835e8101838152039060025afa156102a9575f6020918151610252848060405180948280830197805191829101895e82019083820152030180845201826104ea565b604051918291518091835e8101838152039060025afa156102a9575f519351905190610281848484848961068a565b9095901561029a5750505050505b5f80808080806101e7565b6102a495506107a6565b61028f565b6040513d5f823e3d90fd5b809650518051602010156102ed5760400151600160fb1b808216149081156102de575b50956101e1565b600160fc1b161590505f6102d7565b634e487b7160e01b5f52603260045260245ffd5b809650518051602010156102ed5760400151600160fa1b90811614956101db565b809650518051602010156102ed5760400151600160f81b90811614956101d5565b519298509061035190610b3d565b906040519061039c6001602d846020808201976c1131b430b63632b733b2911d1160991b89528051918291018484015e8101601160f91b838201520301601e198101855201836104ea565b81518401808511610429578151908180821091180218938480821091180284189060206103c98387610590565b92806103ed6103d78661053f565b956103e560405197886104ea565b80875261053f565b8584019890601f1901368a3703920101855e51905190818114938461041a575b50505050955f80806101cc565b2091201490505f80808061040d565b634e487b7160e01b5f52601160045260245ffd5b90995051601474113a3cb832911d113bb2b130baba34371733b2ba1160591b6affffffffffffffffffffff19602084860101511614910182511116985f6101c5565b5f80fd5b634e487b7160e01b5f52604160045260245ffd5b604081149350610085565b9181601f8401121561047f578235916001600160401b03831161047f576020838186019501011161047f57565b606081019081106001600160401b0382111761048357604052565b90601f801991011681019081106001600160401b0382111761048357604052565b9093929384831161047f57841161047f578101920390565b359060208110610531575090565b5f199060200360031b1b1690565b6001600160401b03811161048357601f01601f191660200190565b9291926105668261053f565b9161057460405193846104ea565b82948184528183011161047f578281602093845f960137010152565b9190820391821161042957565b91908260c08210610682578160801161047f576105c1607f19830160808301610523565b908260a01161047f576105db609f19840160a08301610523565b90601f1984018481116104295782848210918215610678575b505061066f5761062861062161061586858161061b610615828b818b61050b565b90610523565b9661050b565b9385610590565b601f198101908111610429571092831561064f575b50505061064a5760019190565b5f9190565b61065a929350610590565b601f19810190811161042957105f808061063d565b505050505f9190565b109050825f6105f4565b9250505f9190565b909192936106988484610c3b565b158015610795575b156106b15750505050505f90600190565b6020945f9460a094604051948552878501526040840152606083015260808201528280526101005afa15610793575f51156106ee57600190600190565b60205f60a06040517fbb5a52f42f9c9261ed4361f59422a1e30036e7c32b270c8807a419feca6050238152600584820152600160408201527fa71af64de5126a4a4e02b7922d66ce9415ce88a4c9d25514d91082c8725ac95760608201527f5d47723c8fbe580bb369fec9c2665d8e30a435b9932645482e7c9f11e872296b60808201528280526101005afa15610793575f511561078d575f90600190565b5f905f90565bfe5b506107a08186610c9f565b156106a0565b919093926107b48286610c3b565b158015610b2c575b610b2357604051936102006107d181876104ea565b5f5b818110610b0e57505060209261096d5f9360c0936040516107f3816104cf565b8681528688820152866040820152895260405191610810836104cf565b825286820152600160408201528588019081528761095e604051610833816104cf565b7f6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c29681527f4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f589820152600160408201526080830190815261094f6109406108998651610d48565b92604086019384526108ab8151610d48565b9061010087019182526108c18851865190610d85565b96606081019788526108d68951835190610d85565b60a08201526108e88651835190610d85565b8c8201526108f98851835190610d85565b60e082015261090b8951845190610d85565b61012082015261091e8651845190610d85565b6101408201526101606109348951855190610d85565b91015251905190610d85565b6101808d018181529551610d85565b6101a08c015251835190610d85565b6101c08a015251905190610d85565b6101e087015260405190848252848083015284604083015260608201527bffffffff00000000000000004319055258e8617b0c46353d039cdab01960808201527bffffffff00000000000000004319055258e8617b0c46353d039cdaae1960a082015260055afa905f519115610afc579091905f5160206111dc5f395f51905f52838509925f5160206111dc5f395f51905f529109905f905f925f945f915b60808310610a38575050505090610a23929161112a565b505f5160206111dc5f395f51905f5290061490565b86610ada575b8160fe1c600c8260fc1c16176040610a568287610d37565b510151610a72575b5060019060021b9160021b92019190610a0c565b969195909482610ab657505050610a898583610d37565b51519360016040610aa96020610a9f8a88610d37565b5101519886610d37565b5101519695945b90610a5e565b90610acf9291610ac96001989987610d37565b51610ea3565b969195909594610ab0565b9395610aeb9195610af19397610da4565b91610da4565b959194909493610a3e565b634e487b715f5260126020526024601cfd5b602090610b19610d19565b81890152016107d3565b50505050505f90565b50610b378482610c9f565b156107bc565b90815115610c25578151600281901b906001600160fe1b038116036104295760028101809111610429576003900490604051917f4142434445464748494a4b4c4d4e4f505152535455565758595a616263646566601f526106707f6768696a6b6c6d6e6f707172737475767778797a303132333435363738392b2f18603f5260208301938080510160208101908151925f83525b818110610beb575050528083528201602001604052909150565b60036004910197603f8951818160121c165183538181600c1c16516001840153818160061c16516002840153165160038201530196610bd1565b9050604051610c356020826104ea565b5f815290565b908115159182610c88575b5081610c7e575b81610c56575090565b7f7fffffff800000007fffffffffffffffde737d56d38bcf4279dce5617e3192a89150111590565b8015159150610c4d565b5f5160206111dc5f395f51905f521191505f610c46565b600160601b63ffffffff60c01b03197f5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b8183816003600160601b0363ffffffff60c01b031981838009080908600160601b63ffffffff60c01b031983800914600160601b63ffffffff60c01b031992831191909211161690565b60405190610d26826104cf565b5f6040838281528260208201520152565b9060108110156102ed5760051b0190565b610d6890610d54610d19565b508051906040602082015191015191610da4565b9060405192610d76846104cf565b83526020830152604082015290565b610d6891610d91610d19565b5080516040602083015192015192610ea3565b929091600160601b63ffffffff60c01b0319838009600160601b63ffffffff60c01b0319828009600160601b63ffffffff60c01b0319908190819080096003600160601b0363ffffffff60c01b031909600160601b63ffffffff60c01b0319808880096003090894600160601b63ffffffff60c01b031990819083900960040994600160601b63ffffffff60c01b03198087600209600160601b63ffffffff60c01b0319908103908380090895600160601b63ffffffff60c01b031992839081908009600809600160601b63ffffffff60c01b03199081039290918290898203900890090892600160601b63ffffffff60c01b03199182910960020990565b60408101515f958695869591949391929091600160601b63ffffffff60c01b0319828009600160601b63ffffffff60c01b031984800992600160601b63ffffffff60c01b03198086860960208501510991600160601b63ffffffff60c01b031983810381808585098a09089351600160601b63ffffffff60c01b03199086900990600160601b63ffffffff60c01b0319908282039082908b090890811585151694855f14611059575050505050600114610f5e575b50505050565b929650909450919250600160601b63ffffffff60c01b031984800990600160601b63ffffffff60c01b0319908190819080096003600160601b0363ffffffff60c01b031909600160601b63ffffffff60c01b0319808880096003090894600160601b63ffffffff60c01b031990819083900960040994600160601b63ffffffff60c01b03198087600209600160601b63ffffffff60c01b0319908103908380090895600160601b63ffffffff60c01b031992839081908009600809600160601b63ffffffff60c01b03199081039290918290898203900890090892600160601b63ffffffff60c01b031991829109600209905f808080610f58565b939c50919a5097985093969550929350600160601b63ffffffff60c01b03199150849050800991600160601b63ffffffff60c01b03199083900991600160601b63ffffffff60c01b031990840991600160601b63ffffffff60c01b03198082600209600160601b63ffffffff60c01b03199081039085810381868009080897600160601b63ffffffff60c01b031993849109600160601b63ffffffff60c01b031990810392909182908a8203900890090893600160601b63ffffffff60c01b0319928391099009905f808080610f58565b929180156111d15760408051602080825281810181905291810182905260608101929092526bfffffffffffffffffffffffe63ffffffff60c01b03196080830152600160601b63ffffffff60c01b031960a0830152905f9060c09060055afa905f519115610afc57600160601b63ffffffff60c01b031982800993600160601b63ffffffff60c01b03199085900993600160601b63ffffffff60c01b031992839109900990565b505090505f905f9056feffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551a2646970667358221220e2c213d6faccd48f7b4cff338a114ab23c050c1944957705db3c8588b7a7b8de64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC7913WebAuthnVerifier:
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
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC7913WebAuthnVerifier]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC7913WebAuthnVerifier, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC7913WebAuthnVerifier]]:
        return cls._deploy(request_type, [], return_tx, ERC7913WebAuthnVerifier, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def verify(self, key: Union[bytearray, bytes], hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes4:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/verifiers/ERC7913WebAuthnVerifier.sol#25)

        Args:
            key: bytes
            hash: bytes32
            signature: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def verify(self, key: Union[bytearray, bytes], hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/verifiers/ERC7913WebAuthnVerifier.sol#25)

        Args:
            key: bytes
            hash: bytes32
            signature: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def verify(self, key: Union[bytearray, bytes], hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/verifiers/ERC7913WebAuthnVerifier.sol#25)

        Args:
            key: bytes
            hash: bytes32
            signature: bytes
        Returns:
            bytes4
        """
        ...

    @overload
    def verify(self, key: Union[bytearray, bytes], hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes4]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/verifiers/ERC7913WebAuthnVerifier.sol#25)

        Args:
            key: bytes
            hash: bytes32
            signature: bytes
        Returns:
            bytes4
        """
        ...

    def verify(self, key: Union[bytearray, bytes], hash: bytes32, signature: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes4, TransactionAbc[bytes4], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/lib/openzeppelin-contracts/contracts/utils/cryptography/verifiers/ERC7913WebAuthnVerifier.sol#25)

        Args:
            key: bytes
            hash: bytes32
            signature: bytes
        Returns:
            bytes4
        """
        return self._execute(self.chain, request_type, "024ad318", [key, hash, signature], True if request_type == "tx" else False, bytes4, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC7913WebAuthnVerifier.verify.selector = bytes4(b'\x02J\xd3\x18')
