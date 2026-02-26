
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.lib.openzeppelincontracts.contracts.proxy.utils.Initializable import Initializable
from pytypes.lib.openzeppelincontracts.contracts.proxy.utils.UUPSUpgradeable import UUPSUpgradeable
from pytypes.lib.openzeppelincontractsupgradeable.contracts.access.AccessControlUpgradeable import AccessControlUpgradeable
from pytypes.src.interfaces.ICreditPolicy import ICreditPolicy



class CreditPolicy(UUPSUpgradeable, AccessControlUpgradeable, Initializable, ICreditPolicy):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#30)
    """
    _abi = {'constructor': {'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'f\x97\xb22': {'inputs': [], 'name': 'AccessControlBadConfirmation', 'type': 'error'}, b'\xe2Q}?': {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}, {'internalType': 'bytes32', 'name': 'neededRole', 'type': 'bytes32'}], 'name': 'AccessControlUnauthorizedAccount', 'type': 'error'}, b'\x99\x96\xb3\x15': {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'AddressEmptyCode', 'type': 'error'}, b'\x11\x1es\xbd': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'CreditPolicy__IncompletePolicy', 'type': 'error'}, b'\xdbc.@': {'inputs': [], 'name': 'CreditPolicy__InvalidIndustryHash', 'type': 'error'}, b'B\xe5yW': {'inputs': [{'internalType': 'uint256', 'name': 'count', 'type': 'uint256'}], 'name': 'CreditPolicy__InvalidTierCount', 'type': 'error'}, b'b\xf4\xa2\x07': {'inputs': [], 'name': 'CreditPolicy__InvalidVersion', 'type': 'error'}, b'O\x97\xff2': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'CreditPolicy__PolicyFrozen', 'type': 'error'}, b'KR\x88\x8f': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'CreditPolicy__PolicyNotActive', 'type': 'error'}, b'\n\x1fg\x9b': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'CreditPolicy__PolicyNotEditable', 'type': 'error'}, b'\xc5\xc05\xaa': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'CreditPolicy__PolicyVersionExists', 'type': 'error'}, b'L\x9c\x8c\xe3': {'inputs': [{'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'ERC1967InvalidImplementation', 'type': 'error'}, b'\xb3\x98\x97\x9f': {'inputs': [], 'name': 'ERC1967NonPayable', 'type': 'error'}, b'\xd6\xbd\xa2u': {'inputs': [], 'name': 'FailedCall', 'type': 'error'}, b'\xf9.\xe8\xa9': {'inputs': [], 'name': 'InvalidInitialization', 'type': 'error'}, b'\xd7\xe6\xbc\xf8': {'inputs': [], 'name': 'NotInitializing', 'type': 'error'}, b'\xe0|\x8d\xba': {'inputs': [], 'name': 'UUPSUnauthorizedCallContext', 'type': 'error'}, b'\xaa\x1dI\xa4': {'inputs': [{'internalType': 'bytes32', 'name': 'slot', 'type': 'bytes32'}], 'name': 'UUPSUnsupportedProxiableUUID', 'type': 'error'}, b'\x12\x10\xd3\xec\xd9r\xf2^\x1e"Qb~\xc8?\xb0\x0c\xb0\xe45\xdb\xe0\xc5\xab\xad\xf3*\x9eP\xee\x9f6': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'IndustryExcluded', 'type': 'event'}, b'\xb0g\xf0\x9a\x9e\x7f\xaf4e\xd2W \xc4\xdc\xa9\xd6I\xffX=\x8a\xc9\xa1b\xdc\x1a- Z\xe9\xb3\x8e': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'IndustryIncluded', 'type': 'event'}, b'\xc7\xf5\x05\xb2\xf3q\xae!u\xeeI\x13\xf4I\x9e\x1f&3\xa7\xb5\x93c!\xee\xd1\xcd\xae\xb6\x11Q\x81\xd2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint64', 'name': 'version', 'type': 'uint64'}], 'name': 'Initialized', 'type': 'event'}, b'\x9c\x88\x9e\xdd\xe3\xe1\x84\x91Z\xa8u\x8b\xed\xa1=\x0bT\x8d\xec\xc0\xb5\xa7\x9f;"\xff\xa3\xd9\xd5}\n\xb2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanTierUpdated', 'type': 'event'}, b'\x809\xca^z\xb2\x80\x89M\xd9\x80\xcer\xff\xf4g-\xe5\x8c\xbeB\x19\xce\xe5\xda`Y\xab\x85\xdb(\x91': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint8', 'name': 'maxTiers', 'type': 'uint8'}], 'name': 'MaxTiersChanged', 'type': 'event'}, b'H\x16U\x97Ped\xc2>8O\xdea\xcf\x1f!e\x91\xbc\xa2\xc8\xa1\xce\x0b\xbb!S\xd4\xc3\xd8\xeb\xc4': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'newAdmin', 'type': 'address'}], 'name': 'PolicyAdminChanged', 'type': 'event'}, b'\xdb\xb6\xd3\x14u\xbe\xc9\x84\x9f\xbf5*|5<\xdf\tmn-\x97,\xf7\x8b\xbadJ\x80&\x9d\xd3{': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyAttestationUpdated', 'type': 'event'}, b'|\x8ac\xa0\xb6\xc9\x98\x1e\x93\xea\xaf\x880{\x94\xe7\xa4\x8aYM\x03P\xa6\x05\xad\xf1\xcf\x9f\xcd\x8e\xc5S': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyConcentrationUpdated', 'type': 'event'}, b'\x968\xa3Q\x9a?\xc3\xe7\xd5\xc0\x10\x14\xe1\x07\x17\x1b#\x8d\x1b\xfe\xd1\xc6\xb8[G.\x18&\xa1\xcf\xc6\xd6': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyCovenantsUpdated', 'type': 'event'}, b'\r(\xab-\xec\x81\xaa\xeb\xf8i\x15\xa8e5:D\xc9w\x9f\xa1\xc6\x15\x8ao\xf7H\xdc\x8e\x14\x84(\x85': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyCreated', 'type': 'event'}, b'dO;\xc1\xa6\xec\x9d\x9b\xf2S\xb2\x19I\xe5f\x906\x17\x173\xd6Vj;\xbeT\xf0,\xd4yp\x0b': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyDeactivated', 'type': 'event'}, b"j\xc7\xbb6\x99\x0b\xe2\n\xfe\x8d'w\xe0:\x1c&\x84\xa4X\x9aQME\xa4\xd6\xf7~Sq\xaa\xfd\xa5": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'hash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'string', 'name': 'uri', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyDocumentSet', 'type': 'event'}, b'jP\xb7\x17K\x84DN\xe4\xfc\x85/0\xebMQ\x05\xa8^`\xb1+\x83\x12$\xdcV-\xaa\xbc=\xcd': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyEligibilityUpdated', 'type': 'event'}, b'\x15\xb1\x8a\xed\x16\xee\rwW\x87\xb6YO\xcfUj\xec!~>V\xf0\x81x\x10\x8d~\xcb\xd5\x99\\+': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyFrozen', 'type': 'event'}, b'&\xa7\xb1\xd1\x89/\x9b\x11ZUaz8\xa1\xbb\xf2\x16\xb6l\x17\x03\xee\x89\xce\xbc\\\x83r]\xa2\xf9$': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyRatiosUpdated', 'type': 'event'}, b'\x83Ff\x14\x80\xd5\xcf\x14\x06\xcd\x88\x15#X_\x80\xca\n\xe4\x7f\xbc#\x12\x9a7\x13R\x94\x17_\xb8\xf4': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'hash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyScopeHashSet', 'type': 'event'}, b'\xbdy\xb8o\xfe\n\xb8\xe8waQQB\x17\xcd|\xac\xd5,\x90\x9ffG\\:\xf4N\x12\x9f\x0b\x00\xff': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'role', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'bytes32', 'name': 'previousAdminRole', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'bytes32', 'name': 'newAdminRole', 'type': 'bytes32'}], 'name': 'RoleAdminChanged', 'type': 'event'}, b"/\x87\x88\x11~~\xff\x1d\x82\xe9&\xecyI\x01\xd1|x\x02JP'\t@0E@\xa73eo\r": {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'role', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'address', 'name': 'account', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'RoleGranted', 'type': 'event'}, b'\xf69\x1f\\2\xd9\xc6\x9d*G\xeag\x0bD)t\xb595\xd1\xed\xc7\xfdd\xeb!\xe0G\xa89\x17\x1b': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'bytes32', 'name': 'role', 'type': 'bytes32'}, {'indexed': True, 'internalType': 'address', 'name': 'account', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}], 'name': 'RoleRevoked', 'type': 'event'}, b'\xbc|\xd7Z \xee\'\xfd\x9a\xde\xba\xb3 A\xf7U!M\xbck\xff\xa9\x0c\xc0"[9\xda.\\-;': {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'implementation', 'type': 'address'}], 'name': 'Upgraded', 'type': 'event'}, b'\xa2\x17\xfd\xdf': {'inputs': [], 'name': 'DEFAULT_ADMIN_ROLE', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\x0e\x95\xf2\xb9': {'inputs': [], 'name': 'INDUSTRY_ADMIN_ROLE', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa1v \xc1': {'inputs': [], 'name': 'POLICY_ADMIN_ROLE', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xea\x95\x8f\xf9': {'inputs': [], 'name': 'POLICY_EDITOR_ROLE', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xad<\xb1\xcc': {'inputs': [], 'name': 'UPGRADE_INTERFACE_VERSION', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'l 4\xca': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'attestation', 'outputs': [{'internalType': 'uint256', 'name': 'maxAttestationAgeDays', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'reAttestationFrequencyDays', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'requiresCPAAttestation', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd9\xe5\xc3]': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'attestationSet', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xf7pq;': {'inputs': [{'internalType': 'address', 'name': 'newAdmin', 'type': 'address'}], 'name': 'changePolicyAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b"\xd4\x02\xab'": {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'concentration', 'outputs': [{'internalType': 'uint256', 'name': 'maxSingleBorrowerBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxIndustryConcentrationBps', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x90\xff\x8a\xdf': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'concentrationSet', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'(\xf4\xca1': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'covenants', 'outputs': [{'internalType': 'uint256', 'name': 'maxLeverageRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minCoverageRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minLiquidityAmount', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'allowsDividends', 'type': 'bool'}, {'internalType': 'uint256', 'name': 'reportingFrequencyDays', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'cJ\x1c\xd4': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'covenantsSet', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x04\xbd\x12\xbb': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'createPolicy', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x0e\xde\xa5\xb8': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'deActivatePolicy', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'z\x86\x1a\xdb': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'eligibility', 'outputs': [{'internalType': 'uint256', 'name': 'minAnnualRevenue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minTangibleNetWorth', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minBusinessAgeDays', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxDefaultsLast36Months', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'bankruptcyExcluded', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xfe\xcaF\x99': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'eligibilitySet', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'L\xfaz\xf6': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}], 'name': 'excludeIndustry', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfbM\xcb\x8b': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'freezePolicy', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'MOqw': {'inputs': [], 'name': 'getMaxTiers', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, b'$\x8a\x9c\xa3': {'inputs': [{'internalType': 'bytes32', 'name': 'role', 'type': 'bytes32'}], 'name': 'getRoleAdmin', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'//\xf1]': {'inputs': [{'internalType': 'bytes32', 'name': 'role', 'type': 'bytes32'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'grantRole', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'jX\xfc0': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'hasAtLeastOneTier', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x91\xd1HT': {'inputs': [{'internalType': 'bytes32', 'name': 'role', 'type': 'bytes32'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'hasRole', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x0c5)\xdc': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}], 'name': 'includeIndustry', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xc4\xd6m\xe8': {'inputs': [{'internalType': 'address', 'name': 'initialAdmin', 'type': 'address'}], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfaOZ\x86': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}], 'name': 'isIndustryExcluded', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbd\x8a\xfaF': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'isPolicyActive', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'L-b\xb7': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'isPolicyFrozen', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'$\xa2\x95"': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'lastUpdated', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'[\xff\xd8\x8f': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'name': 'loanTiers', 'outputs': [{'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'uint256', 'name': 'minRevenue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxRevenue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxDebtToEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxLoanToEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestRateBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'originationFeeBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'termDays', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'active', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'J\xe8\xd2\x1a': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'policyCreated', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b';\xf3e\xb1': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'policyDocumentHash', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'k\xdaa\x06': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'policyDocumentURI', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x80U\xc5\xa9': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'policyScopeHash', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'R\xd1\x90-': {'inputs': [], 'name': 'proxiableUUID', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'w\x1d\xc8j': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'ratios', 'outputs': [{'internalType': 'uint256', 'name': 'maxTotalDebtToEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minInterestCoverageRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minCurrentRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minEBITDAMarginBps', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb62\xd5|': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'ratiosSet', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'6V\x8a\xbe': {'inputs': [{'internalType': 'bytes32', 'name': 'role', 'type': 'bytes32'}, {'internalType': 'address', 'name': 'callerConfirmation', 'type': 'address'}], 'name': 'renounceRole', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd5Gt\x1f': {'inputs': [{'internalType': 'bytes32', 'name': 'role', 'type': 'bytes32'}, {'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'revokeRole', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'[\x87\xec.': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}, {'components': [{'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'uint256', 'name': 'minRevenue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxRevenue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxDebtToEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxLoanToEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestRateBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'originationFeeBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'termDays', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'active', 'type': 'bool'}], 'internalType': 'struct ICreditPolicy.LoanTier', 'name': 'tier', 'type': 'tuple'}], 'name': 'setLoanTier', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa3\xa1\xda{': {'inputs': [{'internalType': 'uint8', 'name': '_maxTiers', 'type': 'uint8'}], 'name': 'setMaxTiers', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b"9'\xa4\xc3": {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'hash', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'uri', 'type': 'string'}], 'name': 'setPolicyDocument', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'2\xabcP': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'hash', 'type': 'bytes32'}], 'name': 'setPolicyScopeHash', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x01\xff\xc9\xa7': {'inputs': [{'internalType': 'bytes4', 'name': 'interfaceId', 'type': 'bytes4'}], 'name': 'supportsInterface', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'Ie\x9c\xdc': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}], 'name': 'tierExistsInPolicy', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xfe&\xd9e': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'totalTiers', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, b'f0\xb0\x08': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'components': [{'internalType': 'uint256', 'name': 'maxAttestationAgeDays', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'reAttestationFrequencyDays', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'requiresCPAAttestation', 'type': 'bool'}], 'internalType': 'struct ICreditPolicy.AttestationRequirements', 'name': 'data', 'type': 'tuple'}], 'name': 'updateAttestation', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'i\xb6S1': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'components': [{'internalType': 'uint256', 'name': 'maxSingleBorrowerBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxIndustryConcentrationBps', 'type': 'uint256'}], 'internalType': 'struct ICreditPolicy.ConcentrationLimits', 'name': 'data', 'type': 'tuple'}], 'name': 'updateConcentration', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'l\x11\xa3\x86': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'components': [{'internalType': 'uint256', 'name': 'maxLeverageRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minCoverageRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minLiquidityAmount', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'allowsDividends', 'type': 'bool'}, {'internalType': 'uint256', 'name': 'reportingFrequencyDays', 'type': 'uint256'}], 'internalType': 'struct ICreditPolicy.MaintenanceCovenants', 'name': 'data', 'type': 'tuple'}], 'name': 'updateCovenants', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'w\xe4\xd4\xad': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'components': [{'internalType': 'uint256', 'name': 'minAnnualRevenue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minTangibleNetWorth', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minBusinessAgeDays', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxDefaultsLast36Months', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'bankruptcyExcluded', 'type': 'bool'}], 'internalType': 'struct ICreditPolicy.EligibilityCriteria', 'name': 'data', 'type': 'tuple'}], 'name': 'updateEligibility', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa4\xd2F\xfa': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'components': [{'internalType': 'uint256', 'name': 'maxTotalDebtToEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minInterestCoverageRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minCurrentRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minEBITDAMarginBps', 'type': 'uint256'}], 'internalType': 'struct ICreditPolicy.FinancialRatios', 'name': 'data', 'type': 'tuple'}], 'name': 'updateRatios', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'O\x1e\xf2\x86': {'inputs': [{'internalType': 'address', 'name': 'newImplementation', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'upgradeToAndCall', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":7664,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxTiers","offset":0,"slot":0,"type":"t_uint8"},{"astId":7668,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"policyCreated","offset":0,"slot":1,"type":"t_mapping(t_uint256,t_bool)"},{"astId":7672,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"policyFrozen","offset":0,"slot":2,"type":"t_mapping(t_uint256,t_bool)"},{"astId":7676,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"policyActive","offset":0,"slot":3,"type":"t_mapping(t_uint256,t_bool)"},{"astId":7680,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"lastUpdated","offset":0,"slot":4,"type":"t_mapping(t_uint256,t_uint256)"},{"astId":7685,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"eligibility","offset":0,"slot":5,"type":"t_mapping(t_uint256,t_struct(EligibilityCriteria)14257_storage)"},{"astId":7690,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"ratios","offset":0,"slot":6,"type":"t_mapping(t_uint256,t_struct(FinancialRatios)14266_storage)"},{"astId":7697,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"loanTiers","offset":0,"slot":7,"type":"t_mapping(t_uint256,t_mapping(t_uint8,t_struct(LoanTier)14287_storage))"},{"astId":7701,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"totalTiers","offset":0,"slot":8,"type":"t_mapping(t_uint256,t_uint8)"},{"astId":7707,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"tierExists","offset":0,"slot":9,"type":"t_mapping(t_uint256,t_mapping(t_uint8,t_bool))"},{"astId":7712,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"concentration","offset":0,"slot":10,"type":"t_mapping(t_uint256,t_struct(ConcentrationLimits)14292_storage)"},{"astId":7718,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"excludedIndustries","offset":0,"slot":11,"type":"t_mapping(t_uint256,t_mapping(t_bytes32,t_bool))"},{"astId":7723,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"attestation","offset":0,"slot":12,"type":"t_mapping(t_uint256,t_struct(AttestationRequirements)14299_storage)"},{"astId":7728,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"covenants","offset":0,"slot":13,"type":"t_mapping(t_uint256,t_struct(MaintenanceCovenants)14310_storage)"},{"astId":7732,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"policyDocumentHash","offset":0,"slot":14,"type":"t_mapping(t_uint256,t_bytes32)"},{"astId":7736,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"policyDocumentURI","offset":0,"slot":15,"type":"t_mapping(t_uint256,t_string_storage)"},{"astId":7740,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"policyScopeHash","offset":0,"slot":16,"type":"t_mapping(t_uint256,t_bytes32)"},{"astId":7744,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"eligibilitySet","offset":0,"slot":17,"type":"t_mapping(t_uint256,t_bool)"},{"astId":7748,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"ratiosSet","offset":0,"slot":18,"type":"t_mapping(t_uint256,t_bool)"},{"astId":7752,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"concentrationSet","offset":0,"slot":19,"type":"t_mapping(t_uint256,t_bool)"},{"astId":7756,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"attestationSet","offset":0,"slot":20,"type":"t_mapping(t_uint256,t_bool)"},{"astId":7760,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"covenantsSet","offset":0,"slot":21,"type":"t_mapping(t_uint256,t_bool)"},{"astId":7764,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"hasAtLeastOneTier","offset":0,"slot":22,"type":"t_mapping(t_uint256,t_bool)"},{"astId":8735,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"__gap","offset":0,"slot":23,"type":"t_array(t_uint256)50_storage"}],"types":{"t_array(t_uint256)50_storage":{"encoding":"inplace","label":"uint256[50]","numberOfBytes":1600,"base":"t_uint256"},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_mapping(t_bytes32,t_bool)":{"encoding":"mapping","label":"mapping(bytes32 => bool)","numberOfBytes":32,"key":"t_bytes32","value":"t_bool"},"t_mapping(t_uint256,t_bool)":{"encoding":"mapping","label":"mapping(uint256 => bool)","numberOfBytes":32,"key":"t_uint256","value":"t_bool"},"t_mapping(t_uint256,t_bytes32)":{"encoding":"mapping","label":"mapping(uint256 => bytes32)","numberOfBytes":32,"key":"t_uint256","value":"t_bytes32"},"t_mapping(t_uint256,t_mapping(t_bytes32,t_bool))":{"encoding":"mapping","label":"mapping(uint256 => mapping(bytes32 => bool))","numberOfBytes":32,"key":"t_uint256","value":"t_mapping(t_bytes32,t_bool)"},"t_mapping(t_uint256,t_mapping(t_uint8,t_bool))":{"encoding":"mapping","label":"mapping(uint256 => mapping(uint8 => bool))","numberOfBytes":32,"key":"t_uint256","value":"t_mapping(t_uint8,t_bool)"},"t_mapping(t_uint256,t_mapping(t_uint8,t_struct(LoanTier)14287_storage))":{"encoding":"mapping","label":"mapping(uint256 => mapping(uint8 => struct ICreditPolicy.LoanTier))","numberOfBytes":32,"key":"t_uint256","value":"t_mapping(t_uint8,t_struct(LoanTier)14287_storage)"},"t_mapping(t_uint256,t_string_storage)":{"encoding":"mapping","label":"mapping(uint256 => string)","numberOfBytes":32,"key":"t_uint256","value":"t_string_storage"},"t_mapping(t_uint256,t_struct(AttestationRequirements)14299_storage)":{"encoding":"mapping","label":"mapping(uint256 => struct ICreditPolicy.AttestationRequirements)","numberOfBytes":32,"key":"t_uint256","value":"t_struct(AttestationRequirements)14299_storage"},"t_mapping(t_uint256,t_struct(ConcentrationLimits)14292_storage)":{"encoding":"mapping","label":"mapping(uint256 => struct ICreditPolicy.ConcentrationLimits)","numberOfBytes":32,"key":"t_uint256","value":"t_struct(ConcentrationLimits)14292_storage"},"t_mapping(t_uint256,t_struct(EligibilityCriteria)14257_storage)":{"encoding":"mapping","label":"mapping(uint256 => struct ICreditPolicy.EligibilityCriteria)","numberOfBytes":32,"key":"t_uint256","value":"t_struct(EligibilityCriteria)14257_storage"},"t_mapping(t_uint256,t_struct(FinancialRatios)14266_storage)":{"encoding":"mapping","label":"mapping(uint256 => struct ICreditPolicy.FinancialRatios)","numberOfBytes":32,"key":"t_uint256","value":"t_struct(FinancialRatios)14266_storage"},"t_mapping(t_uint256,t_struct(MaintenanceCovenants)14310_storage)":{"encoding":"mapping","label":"mapping(uint256 => struct ICreditPolicy.MaintenanceCovenants)","numberOfBytes":32,"key":"t_uint256","value":"t_struct(MaintenanceCovenants)14310_storage"},"t_mapping(t_uint256,t_uint256)":{"encoding":"mapping","label":"mapping(uint256 => uint256)","numberOfBytes":32,"key":"t_uint256","value":"t_uint256"},"t_mapping(t_uint256,t_uint8)":{"encoding":"mapping","label":"mapping(uint256 => uint8)","numberOfBytes":32,"key":"t_uint256","value":"t_uint8"},"t_mapping(t_uint8,t_bool)":{"encoding":"mapping","label":"mapping(uint8 => bool)","numberOfBytes":32,"key":"t_uint8","value":"t_bool"},"t_mapping(t_uint8,t_struct(LoanTier)14287_storage)":{"encoding":"mapping","label":"mapping(uint8 => struct ICreditPolicy.LoanTier)","numberOfBytes":32,"key":"t_uint8","value":"t_struct(LoanTier)14287_storage"},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(AttestationRequirements)14299_storage":{"encoding":"inplace","label":"struct ICreditPolicy.AttestationRequirements","numberOfBytes":96,"members":[{"astId":14294,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxAttestationAgeDays","offset":0,"slot":0,"type":"t_uint256"},{"astId":14296,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"reAttestationFrequencyDays","offset":0,"slot":1,"type":"t_uint256"},{"astId":14298,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"requiresCPAAttestation","offset":0,"slot":2,"type":"t_bool"}]},"t_struct(ConcentrationLimits)14292_storage":{"encoding":"inplace","label":"struct ICreditPolicy.ConcentrationLimits","numberOfBytes":64,"members":[{"astId":14289,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxSingleBorrowerBps","offset":0,"slot":0,"type":"t_uint256"},{"astId":14291,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxIndustryConcentrationBps","offset":0,"slot":1,"type":"t_uint256"}]},"t_struct(EligibilityCriteria)14257_storage":{"encoding":"inplace","label":"struct ICreditPolicy.EligibilityCriteria","numberOfBytes":192,"members":[{"astId":14246,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minAnnualRevenue","offset":0,"slot":0,"type":"t_uint256"},{"astId":14248,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minEBITDA","offset":0,"slot":1,"type":"t_uint256"},{"astId":14250,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minTangibleNetWorth","offset":0,"slot":2,"type":"t_uint256"},{"astId":14252,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minBusinessAgeDays","offset":0,"slot":3,"type":"t_uint256"},{"astId":14254,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxDefaultsLast36Months","offset":0,"slot":4,"type":"t_uint256"},{"astId":14256,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"bankruptcyExcluded","offset":0,"slot":5,"type":"t_bool"}]},"t_struct(FinancialRatios)14266_storage":{"encoding":"inplace","label":"struct ICreditPolicy.FinancialRatios","numberOfBytes":128,"members":[{"astId":14259,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxTotalDebtToEBITDA","offset":0,"slot":0,"type":"t_uint256"},{"astId":14261,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minInterestCoverageRatio","offset":0,"slot":1,"type":"t_uint256"},{"astId":14263,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minCurrentRatio","offset":0,"slot":2,"type":"t_uint256"},{"astId":14265,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minEBITDAMarginBps","offset":0,"slot":3,"type":"t_uint256"}]},"t_struct(LoanTier)14287_storage":{"encoding":"inplace","label":"struct ICreditPolicy.LoanTier","numberOfBytes":320,"members":[{"astId":14268,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"name","offset":0,"slot":0,"type":"t_string_storage"},{"astId":14270,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minRevenue","offset":0,"slot":1,"type":"t_uint256"},{"astId":14272,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxRevenue","offset":0,"slot":2,"type":"t_uint256"},{"astId":14274,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minEBITDA","offset":0,"slot":3,"type":"t_uint256"},{"astId":14276,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxDebtToEBITDA","offset":0,"slot":4,"type":"t_uint256"},{"astId":14278,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxLoanToEBITDA","offset":0,"slot":5,"type":"t_uint256"},{"astId":14280,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"interestRateBps","offset":0,"slot":6,"type":"t_uint256"},{"astId":14282,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"originationFeeBps","offset":0,"slot":7,"type":"t_uint256"},{"astId":14284,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"termDays","offset":0,"slot":8,"type":"t_uint256"},{"astId":14286,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"active","offset":0,"slot":9,"type":"t_bool"}]},"t_struct(MaintenanceCovenants)14310_storage":{"encoding":"inplace","label":"struct ICreditPolicy.MaintenanceCovenants","numberOfBytes":160,"members":[{"astId":14301,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxLeverageRatio","offset":0,"slot":0,"type":"t_uint256"},{"astId":14303,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minCoverageRatio","offset":0,"slot":1,"type":"t_uint256"},{"astId":14305,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minLiquidityAmount","offset":0,"slot":2,"type":"t_uint256"},{"astId":14307,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"allowsDividends","offset":0,"slot":3,"type":"t_bool"},{"astId":14309,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"reportingFrequencyDays","offset":0,"slot":4,"type":"t_uint256"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32},"t_uint8":{"encoding":"inplace","label":"uint8","numberOfBytes":1}}}
    _creation_code = "60a080604052346100c257306080525f5160206127185f395f51905f525460ff8160401c166100b3576002600160401b03196001600160401b03821601610060575b60405161265190816100c7823960805181818161139d01526114770152f35b6001600160401b0319166001600160401b039081175f5160206127185f395f51905f525581527fc7f505b2f371ae2175ee4913f4499e1f2633a7b5936321eed1cdaeb6115181d290602090a15f80610041565b63f92ee8a960e01b5f5260045ffd5b5f80fdfe6080806040526004361015610012575f80fd5b5f3560e01c90816301ffc9a714611d725750806304bd12bb14611cb05780630c3529dc14611c115780630e95f2b914611bea5780630edea5b814611b74578063248a9ca314611b4e57806324a2952214611b2457806328f4ca3114611ac95780632f2ff15d14611a9857806332ab635014611a1157806336568abe146119cd5780633927a4c3146117a85780633bf365b11461177e57806349659cdc1461173a5780634ae8d21a1461170b5780634c2d62b7146116dc5780634cfa7af6146116265780634d4f7177146116075780634f1ef286146113f157806352d1902d1461138b5780635b87ec2e146110645780635bffd88f14610fa2578063634a1cd414610f735780636630b00814610ea357806369b6533114610dfc5780636a58fc3014610dcd5780636bda610614610d8f5780636c11a38614610cae5780636c2034ca14610c68578063771dc86a14610c1c57806377e4d4ad14610b345780637a861adb14610ace5780638055c5a914610aa457806390ff8adf14610a7557806391d1485414610a20578063a17620c1146109f9578063a217fddf146109df578063a3a1da7b14610967578063a4d246fa146108b0578063ad3cb1cc14610865578063b632d57c14610836578063bd8afa4614610807578063c4d66de814610687578063d402ab2714610654578063d547741f1461061c578063d9e5c35d146105ed578063ea958ff9146105c6578063f770713b14610494578063fa4f5a8614610460578063fb4dcb8b146102b8578063fe26d9651461028b5763feca469914610258575f80fd5b34610287576020366003190112610287576004355f526011602052602060ff60405f2054166040519015158152f35b5f80fd5b34610287576020366003190112610287576004355f526008602052602060ff60405f205416604051908152f35b34610287576020366003190112610287576004356102d4611f52565b6102dd816120af565b805f52600260205260ff60405f20541661044e57805f52600360205260ff60405f2054161561043c57805f52601160205260ff60405f205416158015610425575b801561040e575b80156103f7575b80156103e0575b80156103c9575b6103b757805f52600e60205260405f2054156103b757805f52601060205260405f2054156103b7576040817f15b18aed16ee0d775787b6594fcf556aec217e3e56f08178108d7ecbd5995c2b925f526002602052815f20600160ff19825416179055805f52600460205242825f20558151908152426020820152a1005b63111e73bd60e01b5f5260045260245ffd5b50805f52601660205260ff60405f2054161561033a565b50805f52601560205260ff60405f20541615610333565b50805f52601460205260ff60405f2054161561032c565b50805f52601360205260ff60405f20541615610325565b50805f52601260205260ff60405f2054161561031e565b634b52888f60e01b5f5260045260245ffd5b6327cbff9960e11b5f5260045260245ffd5b346102875761046e36611dc5565b905f52600b60205260405f20905f52602052602060ff60405f2054166040519015158152f35b34610287576020366003190112610287577f48165597506564c23e384fde61cf1f216591bca2c8a1ce0bbb2153d4c3d8ebc460206104d0611df1565b6104d861202d565b5f80525f5160206125bc5f395f51905f5282526104fb600160405f200154612069565b6105048161210c565b505f51602061255c5f395f51905f525f525f5160206125bc5f395f51905f528252610535600160405f200154612069565b61053e81612182565b505f5160206125fc5f395f51905f525f525f5160206125bc5f395f51905f52825261056f600160405f200154612069565b61057881612202565b505f51602061257c5f395f51905f525f525f5160206125bc5f395f51905f5282526105a9600160405f200154612069565b6105b281612282565b506040516001600160a01b039091168152a1005b34610287575f3660031901126102875760206040515f5160206125fc5f395f51905f528152f35b34610287576020366003190112610287576004355f526014602052602060ff60405f2054166040519015158152f35b346102875760403660031901126102875761065260043561063b611ddb565b9061064d61064882611f34565b612069565b612393565b005b34610287576020366003190112610287576004355f52600a6020526040805f206001815491015482519182526020820152f35b34610287576020366003190112610287576106a0611df1565b5f5160206125dc5f395f51905f52549060ff8260401c1615916001600160401b038116801590816107ff575b60011490816107f5575b1590816107ec575b506107dd5767ffffffffffffffff1981166001175f5160206125dc5f395f51905f5255826107b1575b5060ff5f5160206125dc5f395f51905f525460401c16156107a2578061072f6107499261210c565b5061073981612182565b5061074381612202565b50612282565b5061075057005b60ff60401b195f5160206125dc5f395f51905f5254165f5160206125dc5f395f51905f52557fc7f505b2f371ae2175ee4913f4499e1f2633a7b5936321eed1cdaeb6115181d2602060405160018152a1005b631afcd79f60e31b5f5260045ffd5b68ffffffffffffffffff191668010000000000000001175f5160206125dc5f395f51905f525582610707565b63f92ee8a960e01b5f5260045ffd5b905015846106de565b303b1591506106d6565b8491506106cc565b34610287576020366003190112610287576004355f526003602052602060ff60405f2054166040519015158152f35b34610287576020366003190112610287576004355f526012602052602060ff60405f2054166040519015158152f35b34610287575f366003190112610287576108ac604051610886604082611e17565b60058152640352e302e360dc1b6020820152604051918291602083526020830190611f10565b0390f35b346102875760a03660031901126102875760043560803660231901126102875760407f26a7b1d1892f9b115a55617a38a1bbf216b66c1703ee89cebc5c83725da2f924916108fc611fe4565b610905816120af565b61090e816120c5565b805f526006602052815f206024358155604435600182015560643560028201556003608435910155805f52600460205242825f2055805f526012602052815f20600160ff198254161790558151908152426020820152a1005b346102875760203660031901126102875760043560ff81168091036102875761098e611f52565b60ff81146109cd576020817f8039ca5e7ab280894dd980ce72fff4672de58cbe4219cee5da6059ab85db28919260ff195f5416175f55604051908152a1005b6342e5795760e01b5f5260045260245ffd5b34610287575f3660031901126102875760206040515f8152f35b34610287575f3660031901126102875760206040515f51602061255c5f395f51905f528152f35b3461028757604036600319011261028757610a39611ddb565b6004355f525f5160206125bc5f395f51905f5260205260405f209060018060a01b03165f52602052602060ff60405f2054166040519015158152f35b34610287576020366003190112610287576004355f526013602052602060ff60405f2054166040519015158152f35b34610287576020366003190112610287576004355f526010602052602060405f2054604051908152f35b34610287576020366003190112610287576004355f52600560205260c060405f20805490600181015490600281015460038201549060ff6005600485015494015416936040519586526020860152604085015260608401526080830152151560a0820152f35b346102875760e03660031901126102875760043560c036602319011261028757610b5c611fe4565b610b65816120af565b610b6e816120c5565b805f52600560205260405f2090602435825560443560018301556064356002830155608435600383015560a435600483015560c43590811515820361028757610beb8260057f6a50b7174b84444ee4fc852f30eb4d5105a85e60b12b831224dc562daabc3dcd9560409550019060ff801983541691151516179055565b805f52600460205242825f2055805f526011602052815f20600160ff198254161790558151908152426020820152a1005b34610287576020366003190112610287576004355f526006602052608060405f208054906001810154906003600282015491015491604051938452602084015260408301526060820152f35b34610287576020366003190112610287576004355f52600c602052606060405f2080549060ff600260018301549201541690604051928352602083015215156040820152f35b346102875760c03660031901126102875760043560a036602319011261028757610cd6611fe4565b610cdf816120af565b610ce8816120c5565b805f52600d60205260405f2090602435825560443560018301556064356002830155608435908115158203610287577f9638a3519a3fc3e7d5c01014e107171b238d1bfed1c6b85b472e1826a1cfc6d692610d568360409450600383019060ff801983541691151516179055565b600460a435910155805f52600460205242825f2055805f526015602052815f20600160ff198254161790558151908152426020820152a1005b34610287576020366003190112610287576004355f52600f6020526108ac610db960405f20611e70565b604051918291602083526020830190611f10565b34610287576020366003190112610287576004355f526016602052602060ff60405f2054166040519015158152f35b346102875760603660031901126102875760043560403660231901126102875760407f7c8a63a0b6c9981e93eaaf88307b94e7a48a594d0350a605adf1cf9fcd8ec55391610e48611fe4565b610e51816120af565b610e5a816120c5565b805f52600a602052815f2060243581556001604435910155805f52600460205242825f2055805f526013602052815f20600160ff198254161790558151908152426020820152a1005b3461028757608036600319011261028757600435606036602319011261028757610ecb611fe4565b610ed4816120af565b610edd816120c5565b805f52600c60205260405f20906024358255604435600183015560643590811515820361028757610f428260027fdbb6d31475bec9849fbf352a7c353cdf096d6e2d972cf78bba644a80269dd37b9560409550019060ff801983541691151516179055565b805f52600460205242825f2055805f526014602052815f20600160ff198254161790558151908152426020820152a1005b34610287576020366003190112610287576004355f526015602052602060ff60405f2054166040519015158152f35b3461028757604036600319011261028757610fbb611e07565b6004355f52600760205260ff60405f2091165f5260205261102e60405f20610fe281611e70565b9060018101549060028101549060038101546004820154600583015460068401549160078501549360ff6009600888015497015416966040519a8b9a6101408c526101408c0190611f10565b9860208b015260408a01526060890152608088015260a087015260c086015260e085015261010084015215156101208301520390f35b3461028757606036600319011261028757600435611080611e07565b906044356001600160401b0381116102875780360390610140600319830112610287576110ab611fe4565b6110b4836120af565b6110bd836120c5565b60ff805f541694169384101561137857825f52600760205260405f20845f5260205260405f2091816004013590602219018112156102875781016004810135906001600160401b038211610287578136036024820113610287576111218454611e38565b601f8111611327575b505f90601f83116001146112b8576101249392915f91836112aa575b50508160011b915f199060031b1c19161783555b6024810135600184015560448101356002840155606481013560038401556084810135600484015560a4810135600584015560c4810135600684015560e481013560078401556101048101356008840155013580151581036102875760096111ce92019060ff801983541691151516179055565b805f52600960205260405f20825f5260205260405f20600160ff19825416179055805f52600860205260ff60405f205416821015611265575b807f9c889edde3e184915aa8758beda13d0b548decc0b5a79f3b22ffa3d9d57d0ab2926060925f52601660205260405f20600160ff19825416179055815f5260046020524260405f20556040519182526020820152426040820152a1005b600182019060ff8211611296575f818152600860205260409020805460ff191660ff90931692909217909155611207565b634e487b7160e01b5f52601160045260245ffd5b016024013590508780611146565b601f19831691855f5260205f20925f5b81811061130c5750916001939185610124979694106112ef575b505050811b01835561115a565b6024910101355f19600384901b60f8161c191690558780806112e2565b602484840101358555600190940193602092830192016112c8565b8281111561112a57845f5260205f20601f840160051c9060208510611370575b81601f9101920160051c03905f5b82811061136357505061112a565b5f82820155600101611355565b5f9150611347565b836342e5795760e01b5f5260045260245ffd5b34610287575f366003190112610287577f00000000000000000000000000000000000000000000000000000000000000006001600160a01b031630036113e25760206040515f51602061253c5f395f51905f528152f35b63703e46dd60e11b5f5260045ffd5b604036600319011261028757611405611df1565b602435906001600160401b03821161028757366023830112156102875781600401356001600160401b0381116115f3576040519261144d601f8301601f191660200185611e17565b818452366024838301011161028757815f9260246020930183870137840101526001600160a01b037f0000000000000000000000000000000000000000000000000000000000000000163081149081156115d1575b506113e2576114af61202d565b6040516352d1902d60e01b81526001600160a01b0382169290602081600481875afa5f918161159d575b506114f15783634c9c8ce360e01b5f5260045260245ffd5b805f51602061253c5f395f51905f5285920361158b5750823b15611579575f51602061253c5f395f51905f5280546001600160a01b031916821790557fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b5f80a2805115611561576106529161242f565b50503461156a57005b63b398979f60e01b5f5260045ffd5b634c9c8ce360e01b5f5260045260245ffd5b632a87526960e21b5f5260045260245ffd5b9091506020813d6020116115c9575b816115b960209383611e17565b81010312610287575190856114d9565b3d91506115ac565b5f51602061253c5f395f51905f52546001600160a01b031614159050836114a2565b634e487b7160e01b5f52604160045260245ffd5b34610287575f36600319011261028757602060ff5f5416604051908152f35b346102875761163436611dc5565b9061163d611f9b565b611646816120af565b61164f816120c5565b81156116cd577f1210d3ecd972f25e1e2251627ec83fb00cb0e435dbe0c5abadf32a9e50ee9f3691815f52600b60205260405f20815f5260205260405f20600160ff19825416179055815f5260046020524260405f20556116c86040519283924291846040919493926060820195825260208201520152565b0390a1005b63036d8cb960e61b5f5260045ffd5b34610287576020366003190112610287576004355f526002602052602060ff60405f2054166040519015158152f35b34610287576020366003190112610287576004355f526001602052602060ff60405f2054166040519015158152f35b3461028757604036600319011261028757611753611e07565b6004355f52600960205260ff60405f2091165f52602052602060ff60405f2054166040519015158152f35b34610287576020366003190112610287576004355f52600e602052602060405f2054604051908152f35b34610287576060366003190112610287576004356024356044356001600160401b0381116102875736602382011215610287578060040135906001600160401b03821161028757366024838301011161028757611803611fe4565b61180c846120af565b611815846120c5565b835f52600e6020528260405f2055835f52600f60205260405f206118398154611e38565b601f811161197c575b505f601f84116001146118eb579260247f6ac7bb36990be20afe8d2777e03a1c2684a4589a514d45a4d6f77e5371aafda5969382938360a0975f916118de575b508460011b905f198660031b1c19161790555b845f5260046020524260405f2055604051968795865260208601526080604086015282608086015201848401375f828201840152426060830152601f01601f19168101030190a1005b849150830101358a611882565b601f19841690825f5260205f20915f5b8181106119615750938593849360249360a0987f6ac7bb36990be20afe8d2777e03a1c2684a4589a514d45a4d6f77e5371aafda59b9810611946575b5050600184811b019055611895565b83018401355f19600387901b60f8161c191690558980611937565b91926020600181926024878a010135815501940192016118fb565b8381111561184257815f5260205f20601f850160051c90602086106119c5575b81601f9101920160051c03905f5b8281106119b8575050611842565b5f828201556001016119aa565b5f915061199c565b34610287576040366003190112610287576119e6611ddb565b336001600160a01b03821603611a025761065290600435612393565b63334bd91960e11b5f5260045ffd5b34610287577f8346661480d5cf1406cd881523585f80ca0ae47fbc23129a37135294175fb8f4611a4036611dc5565b611a48611f52565b611a51826120af565b611a5a826120c5565b815f5260106020528060405f2055815f5260046020524260405f20556116c86040519283924291846040919493926060820195825260208201520152565b3461028757604036600319011261028757610652600435611ab7611ddb565b90611ac461064882611f34565b612302565b34610287576020366003190112610287576004355f52600d60205260a060405f208054906001810154906002810154600460ff6003840154169201549260405194855260208501526040840152151560608301526080820152f35b34610287576020366003190112610287576004355f526004602052602060405f2054604051908152f35b34610287576020366003190112610287576020611b6c600435611f34565b604051908152f35b34610287576020366003190112610287577f644f3bc1a6ec9d9bf253b21949e5669036171733d6566a3bbe54f02cd479700b6040600435611bb3611f52565b611bbc816120af565b805f526003602052815f2060ff198154169055805f52600460205242825f20558151908152426020820152a1005b34610287575f3660031901126102875760206040515f51602061257c5f395f51905f528152f35b3461028757611c1f36611dc5565b90611c28611f9b565b611c31816120af565b611c3a816120c5565b81156116cd577fb067f09a9e7faf3465d25720c4dca9d649ff583d8ac9a162dc1a2d205ae9b38e91815f52600b60205260405f20815f5260205260405f2060ff198154169055815f5260046020524260405f20556116c86040519283924291846040919493926060820195825260208201520152565b3461028757602036600319011261028757600435611ccc611f52565b8015611d6357805f52600160205260ff60405f205416611d51576040817f0d28ab2dec81aaebf86915a865353a44c9779fa1c6158a6ff748dc8e14842885925f526001602052815f20600160ff19825416179055805f526003602052815f20600160ff19825416179055805f52600460205242825f20558151908152426020820152a1005b6362e01ad560e11b5f5260045260245ffd5b6362f4a20760e01b5f5260045ffd5b34610287576020366003190112610287576004359063ffffffff60e01b821680920361028757602091637965db0b60e01b8114908115611db4575b5015158152f35b6301ffc9a760e01b14905083611dad565b6040906003190112610287576004359060243590565b602435906001600160a01b038216820361028757565b600435906001600160a01b038216820361028757565b6024359060ff8216820361028757565b90601f801991011681019081106001600160401b038211176115f357604052565b90600182811c92168015611e66575b6020831014611e5257565b634e487b7160e01b5f52602260045260245ffd5b91607f1691611e47565b9060405191825f825492611e8384611e38565b8084529360018116908115611eee5750600114611eaa575b50611ea892500383611e17565b565b90505f9291925260205f20905f915b818310611ed2575050906020611ea8928201015f611e9b565b6020919350806001915483858901015201910190918492611eb9565b905060209250611ea894915060ff191682840152151560051b8201015f611e9b565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b5f525f5160206125bc5f395f51905f52602052600160405f20015490565b335f9081525f5160206124fc5f395f51905f52602052604090205460ff1615611f7757565b63e2517d3f60e01b5f52336004525f51602061255c5f395f51905f5260245260445ffd5b335f9081525f51602061259c5f395f51905f52602052604090205460ff1615611fc057565b63e2517d3f60e01b5f52336004525f51602061257c5f395f51905f5260245260445ffd5b335f9081525f5160206124dc5f395f51905f52602052604090205460ff161561200957565b63e2517d3f60e01b5f52336004525f5160206125fc5f395f51905f5260245260445ffd5b335f9081525f51602061251c5f395f51905f52602052604090205460ff161561205257565b63e2517d3f60e01b5f52336004525f60245260445ffd5b5f8181525f5160206125bc5f395f51905f526020908152604080832033845290915290205460ff16156120995750565b63e2517d3f60e01b5f523360045260245260445ffd5b5f52600160205260ff60405f20541615611d6357565b805f52600260205260ff60405f20541680156120f5575b6120e35750565b630a1f679b60e01b5f5260045260245ffd5b50805f52600360205260ff60405f205416156120dc565b6001600160a01b0381165f9081525f51602061251c5f395f51905f52602052604090205460ff1661217d576001600160a01b03165f8181525f51602061251c5f395f51905f5260205260408120805460ff191660011790553391905f5160206124bc5f395f51905f528180a4600190565b505f90565b6001600160a01b0381165f9081525f5160206124fc5f395f51905f52602052604090205460ff1661217d576001600160a01b03165f8181525f5160206124fc5f395f51905f5260205260408120805460ff191660011790553391905f51602061255c5f395f51905f52905f5160206124bc5f395f51905f529080a4600190565b6001600160a01b0381165f9081525f5160206124dc5f395f51905f52602052604090205460ff1661217d576001600160a01b03165f8181525f5160206124dc5f395f51905f5260205260408120805460ff191660011790553391905f5160206125fc5f395f51905f52905f5160206124bc5f395f51905f529080a4600190565b6001600160a01b0381165f9081525f51602061259c5f395f51905f52602052604090205460ff1661217d576001600160a01b03165f8181525f51602061259c5f395f51905f5260205260408120805460ff191660011790553391905f51602061257c5f395f51905f52905f5160206124bc5f395f51905f529080a4600190565b5f8181525f5160206125bc5f395f51905f52602090815260408083206001600160a01b038616845290915290205460ff1661238d575f8181525f5160206125bc5f395f51905f52602090815260408083206001600160a01b0395909516808452949091528120805460ff19166001179055339291905f5160206124bc5f395f51905f529080a4600190565b50505f90565b5f8181525f5160206125bc5f395f51905f52602090815260408083206001600160a01b038616845290915290205460ff161561238d575f8181525f5160206125bc5f395f51905f52602090815260408083206001600160a01b0395909516808452949091528120805460ff19169055339291907ff6391f5c32d9c69d2a47ea670b442974b53935d1edc7fd64eb21e047a839171b9080a4600190565b905f8091602081519101845af480806124a8575b156124635750506040513d81523d5f602083013e60203d82010160405290565b1561248857639996b31560e01b5f9081526001600160a01b0391909116600452602490fd5b3d15612499576040513d5f823e3d90fd5b63d6bda27560e01b5f5260045ffd5b503d1515806124435750813b151561244356fe2f8788117e7eff1d82e926ec794901d17c78024a50270940304540a733656f0db900ec6e85ad2eab059132e6d8587c01ac74807d8b041b8b05598c858ec1cb7e1985cb0f3cc11741fc8ea799b7e0248e9a0bbb059ba5ca2c3d971ef69ec8b54fb7db2dd08fcb62d0c9e08c51941cae53c267786a0b75803fb7960902fc8ef97d360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbcace7350211ab645c1937904136ede4855ac3aa1eabb4970e1a51a335d2e19920c259057028a99cb230dc6a3e535a4ec065f3521928facd896e5d9d66d0f6a78da0fcda49636701225b191e2c5b05a62fc040c7e99c3f6056d439636dbc8ea5f602dd7bc7dec4dceedda775e58dd541e08a116c6c53815c0bd028192f7b626800f0c57e16840df040f15088dc2f81fe391c3923bec73e23a9662efc9c229c6a007c6da3b867cb597f11dcc7880abe9bbf4278b5acf688e7d4765b4ff32999975fa2646970667358221220beab94a4f98a32e9909ccec5dfdb02e824e16e79d5568055f4d94098fd9d29f764736f6c63430008210033f0c57e16840df040f15088dc2f81fe391c3923bec73e23a9662efc9c229c6a00"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#198)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> CreditPolicy:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#198)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#198)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#198)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[CreditPolicy]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#198)
        """
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, CreditPolicy, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[CreditPolicy]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#198)
        """
        return cls._deploy(request_type, [], return_tx, CreditPolicy, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class CreditPolicy__PolicyFrozen(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#39)

        Attributes:
            version (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'CreditPolicy__PolicyFrozen', 'type': 'error'}
        original_name = 'CreditPolicy__PolicyFrozen'
        selector = bytes4(b'O\x97\xff2')

        version: uint256


    @dataclasses.dataclass
    class CreditPolicy__InvalidVersion(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#40)
        """
        _abi = {'inputs': [], 'name': 'CreditPolicy__InvalidVersion', 'type': 'error'}
        original_name = 'CreditPolicy__InvalidVersion'
        selector = bytes4(b'b\xf4\xa2\x07')



    @dataclasses.dataclass
    class CreditPolicy__PolicyVersionExists(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#41)

        Attributes:
            version (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'CreditPolicy__PolicyVersionExists', 'type': 'error'}
        original_name = 'CreditPolicy__PolicyVersionExists'
        selector = bytes4(b'\xc5\xc05\xaa')

        version: uint256


    @dataclasses.dataclass
    class CreditPolicy__PolicyNotEditable(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#42)

        Attributes:
            version (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'CreditPolicy__PolicyNotEditable', 'type': 'error'}
        original_name = 'CreditPolicy__PolicyNotEditable'
        selector = bytes4(b'\n\x1fg\x9b')

        version: uint256


    @dataclasses.dataclass
    class CreditPolicy__IncompletePolicy(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#43)

        Attributes:
            version (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'CreditPolicy__IncompletePolicy', 'type': 'error'}
        original_name = 'CreditPolicy__IncompletePolicy'
        selector = bytes4(b'\x11\x1es\xbd')

        version: uint256


    @dataclasses.dataclass
    class CreditPolicy__InvalidIndustryHash(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#44)
        """
        _abi = {'inputs': [], 'name': 'CreditPolicy__InvalidIndustryHash', 'type': 'error'}
        original_name = 'CreditPolicy__InvalidIndustryHash'
        selector = bytes4(b'\xdbc.@')



    @dataclasses.dataclass
    class CreditPolicy__PolicyNotActive(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#45)

        Attributes:
            version (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'CreditPolicy__PolicyNotActive', 'type': 'error'}
        original_name = 'CreditPolicy__PolicyNotActive'
        selector = bytes4(b'KR\x88\x8f')

        version: uint256


    @dataclasses.dataclass
    class CreditPolicy__InvalidTierCount(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#46)

        Attributes:
            count (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'count', 'type': 'uint256'}], 'name': 'CreditPolicy__InvalidTierCount', 'type': 'error'}
        original_name = 'CreditPolicy__InvalidTierCount'
        selector = bytes4(b'B\xe5yW')

        count: uint256


    @dataclasses.dataclass
    class PolicyCreated:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#162)

        Attributes:
            version (uint256): uint256
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyCreated', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'PolicyCreated'
        selector = bytes32(b'\r(\xab-\xec\x81\xaa\xeb\xf8i\x15\xa8e5:D\xc9w\x9f\xa1\xc6\x15\x8ao\xf7H\xdc\x8e\x14\x84(\x85')

        version: uint256
        timestamp: uint256


    @dataclasses.dataclass
    class PolicyFrozen:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#163)

        Attributes:
            version (uint256): uint256
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyFrozen', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'PolicyFrozen'
        selector = bytes32(b'\x15\xb1\x8a\xed\x16\xee\rwW\x87\xb6YO\xcfUj\xec!~>V\xf0\x81x\x10\x8d~\xcb\xd5\x99\\+')

        version: uint256
        timestamp: uint256


    @dataclasses.dataclass
    class PolicyEligibilityUpdated:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#164)

        Attributes:
            version (uint256): uint256
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyEligibilityUpdated', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'PolicyEligibilityUpdated'
        selector = bytes32(b'jP\xb7\x17K\x84DN\xe4\xfc\x85/0\xebMQ\x05\xa8^`\xb1+\x83\x12$\xdcV-\xaa\xbc=\xcd')

        version: uint256
        timestamp: uint256


    @dataclasses.dataclass
    class PolicyRatiosUpdated:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#165)

        Attributes:
            version (uint256): uint256
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyRatiosUpdated', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'PolicyRatiosUpdated'
        selector = bytes32(b'&\xa7\xb1\xd1\x89/\x9b\x11ZUaz8\xa1\xbb\xf2\x16\xb6l\x17\x03\xee\x89\xce\xbc\\\x83r]\xa2\xf9$')

        version: uint256
        timestamp: uint256


    @dataclasses.dataclass
    class PolicyConcentrationUpdated:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#166)

        Attributes:
            version (uint256): uint256
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyConcentrationUpdated', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'PolicyConcentrationUpdated'
        selector = bytes32(b'|\x8ac\xa0\xb6\xc9\x98\x1e\x93\xea\xaf\x880{\x94\xe7\xa4\x8aYM\x03P\xa6\x05\xad\xf1\xcf\x9f\xcd\x8e\xc5S')

        version: uint256
        timestamp: uint256


    @dataclasses.dataclass
    class PolicyAttestationUpdated:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#167)

        Attributes:
            version (uint256): uint256
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyAttestationUpdated', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'PolicyAttestationUpdated'
        selector = bytes32(b'\xdb\xb6\xd3\x14u\xbe\xc9\x84\x9f\xbf5*|5<\xdf\tmn-\x97,\xf7\x8b\xbadJ\x80&\x9d\xd3{')

        version: uint256
        timestamp: uint256


    @dataclasses.dataclass
    class PolicyCovenantsUpdated:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#168)

        Attributes:
            version (uint256): uint256
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyCovenantsUpdated', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'PolicyCovenantsUpdated'
        selector = bytes32(b'\x968\xa3Q\x9a?\xc3\xe7\xd5\xc0\x10\x14\xe1\x07\x17\x1b#\x8d\x1b\xfe\xd1\xc6\xb8[G.\x18&\xa1\xcf\xc6\xd6')

        version: uint256
        timestamp: uint256


    @dataclasses.dataclass
    class LoanTierUpdated:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#169)

        Attributes:
            version (uint256): uint256
            tierId (uint8): uint8
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanTierUpdated', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'LoanTierUpdated'
        selector = bytes32(b'\x9c\x88\x9e\xdd\xe3\xe1\x84\x91Z\xa8u\x8b\xed\xa1=\x0bT\x8d\xec\xc0\xb5\xa7\x9f;"\xff\xa3\xd9\xd5}\n\xb2')

        version: uint256
        tierId: uint8
        timestamp: uint256


    @dataclasses.dataclass
    class IndustryExcluded:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#170)

        Attributes:
            version (uint256): uint256
            industry (bytes32): bytes32
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'IndustryExcluded', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'IndustryExcluded'
        selector = bytes32(b'\x12\x10\xd3\xec\xd9r\xf2^\x1e"Qb~\xc8?\xb0\x0c\xb0\xe45\xdb\xe0\xc5\xab\xad\xf3*\x9eP\xee\x9f6')

        version: uint256
        industry: bytes32
        timestamp: uint256


    @dataclasses.dataclass
    class MaxTiersChanged:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#175)

        Attributes:
            maxTiers (uint8): uint8
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint8', 'name': 'maxTiers', 'type': 'uint8'}], 'name': 'MaxTiersChanged', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'MaxTiersChanged'
        selector = bytes32(b'\x809\xca^z\xb2\x80\x89M\xd9\x80\xcer\xff\xf4g-\xe5\x8c\xbeB\x19\xce\xe5\xda`Y\xab\x85\xdb(\x91')

        maxTiers: uint8


    @dataclasses.dataclass
    class IndustryIncluded:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#176)

        Attributes:
            version (uint256): uint256
            industry (bytes32): bytes32
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'IndustryIncluded', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'IndustryIncluded'
        selector = bytes32(b'\xb0g\xf0\x9a\x9e\x7f\xaf4e\xd2W \xc4\xdc\xa9\xd6I\xffX=\x8a\xc9\xa1b\xdc\x1a- Z\xe9\xb3\x8e')

        version: uint256
        industry: bytes32
        timestamp: uint256


    @dataclasses.dataclass
    class PolicyAdminChanged:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#182)

        Attributes:
            newAdmin (Address): address
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'newAdmin', 'type': 'address'}], 'name': 'PolicyAdminChanged', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'PolicyAdminChanged'
        selector = bytes32(b'H\x16U\x97Ped\xc2>8O\xdea\xcf\x1f!e\x91\xbc\xa2\xc8\xa1\xce\x0b\xbb!S\xd4\xc3\xd8\xeb\xc4')

        newAdmin: Address


    @dataclasses.dataclass
    class PolicyDocumentSet:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#184)

        Attributes:
            version (uint256): uint256
            hash (bytes32): bytes32
            uri (str): string
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'hash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'string', 'name': 'uri', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyDocumentSet', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'PolicyDocumentSet'
        selector = bytes32(b"j\xc7\xbb6\x99\x0b\xe2\n\xfe\x8d'w\xe0:\x1c&\x84\xa4X\x9aQME\xa4\xd6\xf7~Sq\xaa\xfd\xa5")

        version: uint256
        hash: bytes32
        uri: str
        timestamp: uint256


    @dataclasses.dataclass
    class PolicyScopeHashSet:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#190)

        Attributes:
            version (uint256): uint256
            hash (bytes32): bytes32
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'hash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyScopeHashSet', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'PolicyScopeHashSet'
        selector = bytes32(b'\x83Ff\x14\x80\xd5\xcf\x14\x06\xcd\x88\x15#X_\x80\xca\n\xe4\x7f\xbc#\x12\x9a7\x13R\x94\x17_\xb8\xf4')

        version: uint256
        hash: bytes32
        timestamp: uint256


    @dataclasses.dataclass
    class PolicyDeactivated:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#191)

        Attributes:
            version (uint256): uint256
            timestamp (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyDeactivated', 'type': 'event'}
        origin: Account = dataclasses.field(init=False, compare=False, repr=False)
        original_name = 'PolicyDeactivated'
        selector = bytes32(b'dO;\xc1\xa6\xec\x9d\x9b\xf2S\xb2\x19I\xe5f\x906\x17\x173\xd6Vj;\xbeT\xf0,\xd4yp\x0b')

        version: uint256
        timestamp: uint256


    @overload
    def POLICY_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#52)

        Returns:
            POLICY_ADMIN_ROLE: bytes32
        """
        ...

    @overload
    def POLICY_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#52)

        Returns:
            POLICY_ADMIN_ROLE: bytes32
        """
        ...

    @overload
    def POLICY_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#52)

        Returns:
            POLICY_ADMIN_ROLE: bytes32
        """
        ...

    @overload
    def POLICY_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#52)

        Returns:
            POLICY_ADMIN_ROLE: bytes32
        """
        ...

    def POLICY_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#52)

        Returns:
            POLICY_ADMIN_ROLE: bytes32
        """
        return self._execute(self.chain, request_type, "a17620c1", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def POLICY_EDITOR_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#53)

        Returns:
            POLICY_EDITOR_ROLE: bytes32
        """
        ...

    @overload
    def POLICY_EDITOR_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#53)

        Returns:
            POLICY_EDITOR_ROLE: bytes32
        """
        ...

    @overload
    def POLICY_EDITOR_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#53)

        Returns:
            POLICY_EDITOR_ROLE: bytes32
        """
        ...

    @overload
    def POLICY_EDITOR_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#53)

        Returns:
            POLICY_EDITOR_ROLE: bytes32
        """
        ...

    def POLICY_EDITOR_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#53)

        Returns:
            POLICY_EDITOR_ROLE: bytes32
        """
        return self._execute(self.chain, request_type, "ea958ff9", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def INDUSTRY_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#55)

        Returns:
            INDUSTRY_ADMIN_ROLE: bytes32
        """
        ...

    @overload
    def INDUSTRY_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#55)

        Returns:
            INDUSTRY_ADMIN_ROLE: bytes32
        """
        ...

    @overload
    def INDUSTRY_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#55)

        Returns:
            INDUSTRY_ADMIN_ROLE: bytes32
        """
        ...

    @overload
    def INDUSTRY_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#55)

        Returns:
            INDUSTRY_ADMIN_ROLE: bytes32
        """
        ...

    def INDUSTRY_ADMIN_ROLE(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#55)

        Returns:
            INDUSTRY_ADMIN_ROLE: bytes32
        """
        return self._execute(self.chain, request_type, "0e95f2b9", [], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def policyCreated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#89)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def policyCreated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#89)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def policyCreated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#89)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def policyCreated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#89)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    def policyCreated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#89)

        Args:
            key0: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "4ae8d21a", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def lastUpdated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#92)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def lastUpdated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#92)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def lastUpdated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#92)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def lastUpdated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#92)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    def lastUpdated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#92)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "24a29522", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def eligibility(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ICreditPolicy.EligibilityCriteria:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#99)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.EligibilityCriteria
        """
        ...

    @overload
    def eligibility(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#99)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.EligibilityCriteria
        """
        ...

    @overload
    def eligibility(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#99)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.EligibilityCriteria
        """
        ...

    @overload
    def eligibility(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ICreditPolicy.EligibilityCriteria]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#99)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.EligibilityCriteria
        """
        ...

    def eligibility(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[ICreditPolicy.EligibilityCriteria, TransactionAbc[ICreditPolicy.EligibilityCriteria], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#99)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.EligibilityCriteria
        """
        return self._execute(self.chain, request_type, "7a861adb", [key0], True if request_type == "tx" else False, ICreditPolicy.EligibilityCriteria, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def ratios(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ICreditPolicy.FinancialRatios:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#106)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.FinancialRatios
        """
        ...

    @overload
    def ratios(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#106)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.FinancialRatios
        """
        ...

    @overload
    def ratios(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#106)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.FinancialRatios
        """
        ...

    @overload
    def ratios(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ICreditPolicy.FinancialRatios]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#106)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.FinancialRatios
        """
        ...

    def ratios(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[ICreditPolicy.FinancialRatios, TransactionAbc[ICreditPolicy.FinancialRatios], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#106)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.FinancialRatios
        """
        return self._execute(self.chain, request_type, "771dc86a", [key0], True if request_type == "tx" else False, ICreditPolicy.FinancialRatios, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def loanTiers(self, key0: uint256, key1: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ICreditPolicy.LoanTier:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#113)

        Args:
            key0: uint256
            key1: uint8
        Returns:
            struct ICreditPolicy.LoanTier
        """
        ...

    @overload
    def loanTiers(self, key0: uint256, key1: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#113)

        Args:
            key0: uint256
            key1: uint8
        Returns:
            struct ICreditPolicy.LoanTier
        """
        ...

    @overload
    def loanTiers(self, key0: uint256, key1: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#113)

        Args:
            key0: uint256
            key1: uint8
        Returns:
            struct ICreditPolicy.LoanTier
        """
        ...

    @overload
    def loanTiers(self, key0: uint256, key1: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ICreditPolicy.LoanTier]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#113)

        Args:
            key0: uint256
            key1: uint8
        Returns:
            struct ICreditPolicy.LoanTier
        """
        ...

    def loanTiers(self, key0: uint256, key1: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[ICreditPolicy.LoanTier, TransactionAbc[ICreditPolicy.LoanTier], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#113)

        Args:
            key0: uint256
            key1: uint8
        Returns:
            struct ICreditPolicy.LoanTier
        """
        return self._execute(self.chain, request_type, "5bffd88f", [key0, key1], True if request_type == "tx" else False, ICreditPolicy.LoanTier, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalTiers(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint8:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#114)

        Args:
            key0: uint256
        Returns:
            uint8
        """
        ...

    @overload
    def totalTiers(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#114)

        Args:
            key0: uint256
        Returns:
            uint8
        """
        ...

    @overload
    def totalTiers(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#114)

        Args:
            key0: uint256
        Returns:
            uint8
        """
        ...

    @overload
    def totalTiers(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint8]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#114)

        Args:
            key0: uint256
        Returns:
            uint8
        """
        ...

    def totalTiers(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint8, TransactionAbc[uint8], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#114)

        Args:
            key0: uint256
        Returns:
            uint8
        """
        return self._execute(self.chain, request_type, "fe26d965", [key0], True if request_type == "tx" else False, uint8, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def concentration(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ICreditPolicy.ConcentrationLimits:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#122)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.ConcentrationLimits
        """
        ...

    @overload
    def concentration(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#122)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.ConcentrationLimits
        """
        ...

    @overload
    def concentration(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#122)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.ConcentrationLimits
        """
        ...

    @overload
    def concentration(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ICreditPolicy.ConcentrationLimits]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#122)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.ConcentrationLimits
        """
        ...

    def concentration(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[ICreditPolicy.ConcentrationLimits, TransactionAbc[ICreditPolicy.ConcentrationLimits], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#122)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.ConcentrationLimits
        """
        return self._execute(self.chain, request_type, "d402ab27", [key0], True if request_type == "tx" else False, ICreditPolicy.ConcentrationLimits, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def attestation(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ICreditPolicy.AttestationRequirements:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#134)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.AttestationRequirements
        """
        ...

    @overload
    def attestation(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#134)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.AttestationRequirements
        """
        ...

    @overload
    def attestation(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#134)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.AttestationRequirements
        """
        ...

    @overload
    def attestation(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ICreditPolicy.AttestationRequirements]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#134)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.AttestationRequirements
        """
        ...

    def attestation(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[ICreditPolicy.AttestationRequirements, TransactionAbc[ICreditPolicy.AttestationRequirements], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#134)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.AttestationRequirements
        """
        return self._execute(self.chain, request_type, "6c2034ca", [key0], True if request_type == "tx" else False, ICreditPolicy.AttestationRequirements, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def covenants(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ICreditPolicy.MaintenanceCovenants:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#141)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.MaintenanceCovenants
        """
        ...

    @overload
    def covenants(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#141)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.MaintenanceCovenants
        """
        ...

    @overload
    def covenants(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#141)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.MaintenanceCovenants
        """
        ...

    @overload
    def covenants(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ICreditPolicy.MaintenanceCovenants]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#141)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.MaintenanceCovenants
        """
        ...

    def covenants(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[ICreditPolicy.MaintenanceCovenants, TransactionAbc[ICreditPolicy.MaintenanceCovenants], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#141)

        Args:
            key0: uint256
        Returns:
            struct ICreditPolicy.MaintenanceCovenants
        """
        return self._execute(self.chain, request_type, "28f4ca31", [key0], True if request_type == "tx" else False, ICreditPolicy.MaintenanceCovenants, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def policyDocumentHash(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#146)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        ...

    @overload
    def policyDocumentHash(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#146)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        ...

    @overload
    def policyDocumentHash(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#146)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        ...

    @overload
    def policyDocumentHash(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#146)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        ...

    def policyDocumentHash(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#146)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        return self._execute(self.chain, request_type, "3bf365b1", [key0], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def policyDocumentURI(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#147)

        Args:
            key0: uint256
        Returns:
            string
        """
        ...

    @overload
    def policyDocumentURI(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#147)

        Args:
            key0: uint256
        Returns:
            string
        """
        ...

    @overload
    def policyDocumentURI(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#147)

        Args:
            key0: uint256
        Returns:
            string
        """
        ...

    @overload
    def policyDocumentURI(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#147)

        Args:
            key0: uint256
        Returns:
            string
        """
        ...

    def policyDocumentURI(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#147)

        Args:
            key0: uint256
        Returns:
            string
        """
        return self._execute(self.chain, request_type, "6bda6106", [key0], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def policyScopeHash(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#150)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        ...

    @overload
    def policyScopeHash(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#150)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        ...

    @overload
    def policyScopeHash(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#150)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        ...

    @overload
    def policyScopeHash(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#150)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        ...

    def policyScopeHash(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#150)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        return self._execute(self.chain, request_type, "8055c5a9", [key0], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def eligibilitySet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#152)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def eligibilitySet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#152)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def eligibilitySet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#152)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def eligibilitySet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#152)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    def eligibilitySet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#152)

        Args:
            key0: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "feca4699", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def ratiosSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#153)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def ratiosSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#153)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def ratiosSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#153)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def ratiosSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#153)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    def ratiosSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#153)

        Args:
            key0: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "b632d57c", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def concentrationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#154)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def concentrationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#154)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def concentrationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#154)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def concentrationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#154)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    def concentrationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#154)

        Args:
            key0: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "90ff8adf", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def attestationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#155)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def attestationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#155)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def attestationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#155)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def attestationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#155)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    def attestationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#155)

        Args:
            key0: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "d9e5c35d", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def covenantsSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#156)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def covenantsSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#156)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def covenantsSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#156)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def covenantsSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#156)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    def covenantsSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#156)

        Args:
            key0: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "634a1cd4", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def hasAtLeastOneTier(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#157)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def hasAtLeastOneTier(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#157)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def hasAtLeastOneTier(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#157)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def hasAtLeastOneTier(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#157)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    def hasAtLeastOneTier(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#157)

        Args:
            key0: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "6a58fc30", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def initialize(self, initialAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#206)

        Args:
            initialAdmin: address
        """
        ...

    @overload
    def initialize(self, initialAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#206)

        Args:
            initialAdmin: address
        """
        ...

    @overload
    def initialize(self, initialAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#206)

        Args:
            initialAdmin: address
        """
        ...

    @overload
    def initialize(self, initialAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#206)

        Args:
            initialAdmin: address
        """
        ...

    def initialize(self, initialAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#206)

        Args:
            initialAdmin: address
        """
        return self._execute(self.chain, request_type, "c4d66de8", [initialAdmin], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def createPolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#227)

        Args:
            version: uint256
        """
        ...

    @overload
    def createPolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#227)

        Args:
            version: uint256
        """
        ...

    @overload
    def createPolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#227)

        Args:
            version: uint256
        """
        ...

    @overload
    def createPolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#227)

        Args:
            version: uint256
        """
        ...

    def createPolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#227)

        Args:
            version: uint256
        """
        return self._execute(self.chain, request_type, "04bd12bb", [version], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def freezePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#249)

        Args:
            version: uint256
        """
        ...

    @overload
    def freezePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#249)

        Args:
            version: uint256
        """
        ...

    @overload
    def freezePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#249)

        Args:
            version: uint256
        """
        ...

    @overload
    def freezePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#249)

        Args:
            version: uint256
        """
        ...

    def freezePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#249)

        Args:
            version: uint256
        """
        return self._execute(self.chain, request_type, "fb4dcb8b", [version], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deActivatePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#284)

        Args:
            version: uint256
        """
        ...

    @overload
    def deActivatePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#284)

        Args:
            version: uint256
        """
        ...

    @overload
    def deActivatePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#284)

        Args:
            version: uint256
        """
        ...

    @overload
    def deActivatePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#284)

        Args:
            version: uint256
        """
        ...

    def deActivatePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#284)

        Args:
            version: uint256
        """
        return self._execute(self.chain, request_type, "0edea5b8", [version], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def updateEligibility(self, version: uint256, data: ICreditPolicy.EligibilityCriteria, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#300)

        Args:
            version: uint256
            data: struct ICreditPolicy.EligibilityCriteria
        """
        ...

    @overload
    def updateEligibility(self, version: uint256, data: ICreditPolicy.EligibilityCriteria, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#300)

        Args:
            version: uint256
            data: struct ICreditPolicy.EligibilityCriteria
        """
        ...

    @overload
    def updateEligibility(self, version: uint256, data: ICreditPolicy.EligibilityCriteria, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#300)

        Args:
            version: uint256
            data: struct ICreditPolicy.EligibilityCriteria
        """
        ...

    @overload
    def updateEligibility(self, version: uint256, data: ICreditPolicy.EligibilityCriteria, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#300)

        Args:
            version: uint256
            data: struct ICreditPolicy.EligibilityCriteria
        """
        ...

    def updateEligibility(self, version: uint256, data: ICreditPolicy.EligibilityCriteria, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#300)

        Args:
            version: uint256
            data: struct ICreditPolicy.EligibilityCriteria
        """
        return self._execute(self.chain, request_type, "77e4d4ad", [version, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def updateRatios(self, version: uint256, data: ICreditPolicy.FinancialRatios, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#322)

        Args:
            version: uint256
            data: struct ICreditPolicy.FinancialRatios
        """
        ...

    @overload
    def updateRatios(self, version: uint256, data: ICreditPolicy.FinancialRatios, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#322)

        Args:
            version: uint256
            data: struct ICreditPolicy.FinancialRatios
        """
        ...

    @overload
    def updateRatios(self, version: uint256, data: ICreditPolicy.FinancialRatios, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#322)

        Args:
            version: uint256
            data: struct ICreditPolicy.FinancialRatios
        """
        ...

    @overload
    def updateRatios(self, version: uint256, data: ICreditPolicy.FinancialRatios, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#322)

        Args:
            version: uint256
            data: struct ICreditPolicy.FinancialRatios
        """
        ...

    def updateRatios(self, version: uint256, data: ICreditPolicy.FinancialRatios, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#322)

        Args:
            version: uint256
            data: struct ICreditPolicy.FinancialRatios
        """
        return self._execute(self.chain, request_type, "a4d246fa", [version, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def updateConcentration(self, version: uint256, data: ICreditPolicy.ConcentrationLimits, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#344)

        Args:
            version: uint256
            data: struct ICreditPolicy.ConcentrationLimits
        """
        ...

    @overload
    def updateConcentration(self, version: uint256, data: ICreditPolicy.ConcentrationLimits, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#344)

        Args:
            version: uint256
            data: struct ICreditPolicy.ConcentrationLimits
        """
        ...

    @overload
    def updateConcentration(self, version: uint256, data: ICreditPolicy.ConcentrationLimits, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#344)

        Args:
            version: uint256
            data: struct ICreditPolicy.ConcentrationLimits
        """
        ...

    @overload
    def updateConcentration(self, version: uint256, data: ICreditPolicy.ConcentrationLimits, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#344)

        Args:
            version: uint256
            data: struct ICreditPolicy.ConcentrationLimits
        """
        ...

    def updateConcentration(self, version: uint256, data: ICreditPolicy.ConcentrationLimits, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#344)

        Args:
            version: uint256
            data: struct ICreditPolicy.ConcentrationLimits
        """
        return self._execute(self.chain, request_type, "69b65331", [version, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def updateAttestation(self, version: uint256, data: ICreditPolicy.AttestationRequirements, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#366)

        Args:
            version: uint256
            data: struct ICreditPolicy.AttestationRequirements
        """
        ...

    @overload
    def updateAttestation(self, version: uint256, data: ICreditPolicy.AttestationRequirements, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#366)

        Args:
            version: uint256
            data: struct ICreditPolicy.AttestationRequirements
        """
        ...

    @overload
    def updateAttestation(self, version: uint256, data: ICreditPolicy.AttestationRequirements, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#366)

        Args:
            version: uint256
            data: struct ICreditPolicy.AttestationRequirements
        """
        ...

    @overload
    def updateAttestation(self, version: uint256, data: ICreditPolicy.AttestationRequirements, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#366)

        Args:
            version: uint256
            data: struct ICreditPolicy.AttestationRequirements
        """
        ...

    def updateAttestation(self, version: uint256, data: ICreditPolicy.AttestationRequirements, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#366)

        Args:
            version: uint256
            data: struct ICreditPolicy.AttestationRequirements
        """
        return self._execute(self.chain, request_type, "6630b008", [version, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def updateCovenants(self, version: uint256, data: ICreditPolicy.MaintenanceCovenants, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#388)

        Args:
            version: uint256
            data: struct ICreditPolicy.MaintenanceCovenants
        """
        ...

    @overload
    def updateCovenants(self, version: uint256, data: ICreditPolicy.MaintenanceCovenants, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#388)

        Args:
            version: uint256
            data: struct ICreditPolicy.MaintenanceCovenants
        """
        ...

    @overload
    def updateCovenants(self, version: uint256, data: ICreditPolicy.MaintenanceCovenants, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#388)

        Args:
            version: uint256
            data: struct ICreditPolicy.MaintenanceCovenants
        """
        ...

    @overload
    def updateCovenants(self, version: uint256, data: ICreditPolicy.MaintenanceCovenants, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#388)

        Args:
            version: uint256
            data: struct ICreditPolicy.MaintenanceCovenants
        """
        ...

    def updateCovenants(self, version: uint256, data: ICreditPolicy.MaintenanceCovenants, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#388)

        Args:
            version: uint256
            data: struct ICreditPolicy.MaintenanceCovenants
        """
        return self._execute(self.chain, request_type, "6c11a386", [version, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setLoanTier(self, version: uint256, tierId: uint8, tier: ICreditPolicy.LoanTier, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#414)

        Args:
            version: uint256
            tierId: uint8
            tier: struct ICreditPolicy.LoanTier
        """
        ...

    @overload
    def setLoanTier(self, version: uint256, tierId: uint8, tier: ICreditPolicy.LoanTier, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#414)

        Args:
            version: uint256
            tierId: uint8
            tier: struct ICreditPolicy.LoanTier
        """
        ...

    @overload
    def setLoanTier(self, version: uint256, tierId: uint8, tier: ICreditPolicy.LoanTier, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#414)

        Args:
            version: uint256
            tierId: uint8
            tier: struct ICreditPolicy.LoanTier
        """
        ...

    @overload
    def setLoanTier(self, version: uint256, tierId: uint8, tier: ICreditPolicy.LoanTier, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#414)

        Args:
            version: uint256
            tierId: uint8
            tier: struct ICreditPolicy.LoanTier
        """
        ...

    def setLoanTier(self, version: uint256, tierId: uint8, tier: ICreditPolicy.LoanTier, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#414)

        Args:
            version: uint256
            tierId: uint8
            tier: struct ICreditPolicy.LoanTier
        """
        return self._execute(self.chain, request_type, "5b87ec2e", [version, tierId, tier], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def excludeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#444)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    @overload
    def excludeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#444)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    @overload
    def excludeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#444)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    @overload
    def excludeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#444)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    def excludeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#444)

        Args:
            version: uint256
            industry: bytes32
        """
        return self._execute(self.chain, request_type, "4cfa7af6", [version, industry], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def includeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#464)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    @overload
    def includeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#464)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    @overload
    def includeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#464)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    @overload
    def includeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#464)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    def includeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#464)

        Args:
            version: uint256
            industry: bytes32
        """
        return self._execute(self.chain, request_type, "0c3529dc", [version, industry], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setPolicyDocument(self, version: uint256, hash: bytes32, uri: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#491)

        Args:
            version: uint256
            hash: bytes32
            uri: string
        """
        ...

    @overload
    def setPolicyDocument(self, version: uint256, hash: bytes32, uri: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#491)

        Args:
            version: uint256
            hash: bytes32
            uri: string
        """
        ...

    @overload
    def setPolicyDocument(self, version: uint256, hash: bytes32, uri: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#491)

        Args:
            version: uint256
            hash: bytes32
            uri: string
        """
        ...

    @overload
    def setPolicyDocument(self, version: uint256, hash: bytes32, uri: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#491)

        Args:
            version: uint256
            hash: bytes32
            uri: string
        """
        ...

    def setPolicyDocument(self, version: uint256, hash: bytes32, uri: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#491)

        Args:
            version: uint256
            hash: bytes32
            uri: string
        """
        return self._execute(self.chain, request_type, "3927a4c3", [version, hash, uri], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setPolicyScopeHash(self, version: uint256, hash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#515)

        Args:
            version: uint256
            hash: bytes32
        """
        ...

    @overload
    def setPolicyScopeHash(self, version: uint256, hash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#515)

        Args:
            version: uint256
            hash: bytes32
        """
        ...

    @overload
    def setPolicyScopeHash(self, version: uint256, hash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#515)

        Args:
            version: uint256
            hash: bytes32
        """
        ...

    @overload
    def setPolicyScopeHash(self, version: uint256, hash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#515)

        Args:
            version: uint256
            hash: bytes32
        """
        ...

    def setPolicyScopeHash(self, version: uint256, hash: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#515)

        Args:
            version: uint256
            hash: bytes32
        """
        return self._execute(self.chain, request_type, "32ab6350", [version, hash], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def changePolicyAdmin(self, newAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#533)

        Args:
            newAdmin: address
        """
        ...

    @overload
    def changePolicyAdmin(self, newAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#533)

        Args:
            newAdmin: address
        """
        ...

    @overload
    def changePolicyAdmin(self, newAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#533)

        Args:
            newAdmin: address
        """
        ...

    @overload
    def changePolicyAdmin(self, newAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#533)

        Args:
            newAdmin: address
        """
        ...

    def changePolicyAdmin(self, newAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#533)

        Args:
            newAdmin: address
        """
        return self._execute(self.chain, request_type, "f770713b", [newAdmin], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def isPolicyActive(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#551)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    @overload
    def isPolicyActive(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#551)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    @overload
    def isPolicyActive(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#551)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    @overload
    def isPolicyActive(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#551)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    def isPolicyActive(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#551)

        Args:
            version: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "bd8afa46", [version], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def isPolicyFrozen(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#558)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    @overload
    def isPolicyFrozen(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#558)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    @overload
    def isPolicyFrozen(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#558)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    @overload
    def isPolicyFrozen(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#558)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    def isPolicyFrozen(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#558)

        Args:
            version: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "4c2d62b7", [version], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tierExistsInPolicy(self, version: uint256, tierId: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#566)

        Args:
            version: uint256
            tierId: uint8
        Returns:
            bool
        """
        ...

    @overload
    def tierExistsInPolicy(self, version: uint256, tierId: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#566)

        Args:
            version: uint256
            tierId: uint8
        Returns:
            bool
        """
        ...

    @overload
    def tierExistsInPolicy(self, version: uint256, tierId: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#566)

        Args:
            version: uint256
            tierId: uint8
        Returns:
            bool
        """
        ...

    @overload
    def tierExistsInPolicy(self, version: uint256, tierId: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#566)

        Args:
            version: uint256
            tierId: uint8
        Returns:
            bool
        """
        ...

    def tierExistsInPolicy(self, version: uint256, tierId: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#566)

        Args:
            version: uint256
            tierId: uint8
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "49659cdc", [version, tierId], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setMaxTiers(self, _maxTiers: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#575)

        Args:
            _maxTiers: uint8
        """
        ...

    @overload
    def setMaxTiers(self, _maxTiers: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#575)

        Args:
            _maxTiers: uint8
        """
        ...

    @overload
    def setMaxTiers(self, _maxTiers: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#575)

        Args:
            _maxTiers: uint8
        """
        ...

    @overload
    def setMaxTiers(self, _maxTiers: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#575)

        Args:
            _maxTiers: uint8
        """
        ...

    def setMaxTiers(self, _maxTiers: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#575)

        Args:
            _maxTiers: uint8
        """
        return self._execute(self.chain, request_type, "a3a1da7b", [_maxTiers], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getMaxTiers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint8:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#584)

        Returns:
            uint8
        """
        ...

    @overload
    def getMaxTiers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#584)

        Returns:
            uint8
        """
        ...

    @overload
    def getMaxTiers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#584)

        Returns:
            uint8
        """
        ...

    @overload
    def getMaxTiers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint8]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#584)

        Returns:
            uint8
        """
        ...

    def getMaxTiers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint8, TransactionAbc[uint8], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#584)

        Returns:
            uint8
        """
        return self._execute(self.chain, request_type, "4d4f7177", [], True if request_type == "tx" else False, uint8, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def isIndustryExcluded(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#592)

        Args:
            version: uint256
            industry: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def isIndustryExcluded(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#592)

        Args:
            version: uint256
            industry: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def isIndustryExcluded(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#592)

        Args:
            version: uint256
            industry: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def isIndustryExcluded(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#592)

        Args:
            version: uint256
            industry: bytes32
        Returns:
            bool
        """
        ...

    def isIndustryExcluded(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#592)

        Args:
            version: uint256
            industry: bytes32
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "fa4f5a86", [version, industry], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

CreditPolicy.POLICY_ADMIN_ROLE.selector = bytes4(b'\xa1v \xc1')
CreditPolicy.POLICY_EDITOR_ROLE.selector = bytes4(b'\xea\x95\x8f\xf9')
CreditPolicy.INDUSTRY_ADMIN_ROLE.selector = bytes4(b'\x0e\x95\xf2\xb9')
CreditPolicy.policyCreated.selector = bytes4(b'J\xe8\xd2\x1a')
CreditPolicy.lastUpdated.selector = bytes4(b'$\xa2\x95"')
CreditPolicy.eligibility.selector = bytes4(b'z\x86\x1a\xdb')
CreditPolicy.ratios.selector = bytes4(b'w\x1d\xc8j')
CreditPolicy.loanTiers.selector = bytes4(b'[\xff\xd8\x8f')
CreditPolicy.totalTiers.selector = bytes4(b'\xfe&\xd9e')
CreditPolicy.concentration.selector = bytes4(b"\xd4\x02\xab'")
CreditPolicy.attestation.selector = bytes4(b'l 4\xca')
CreditPolicy.covenants.selector = bytes4(b'(\xf4\xca1')
CreditPolicy.policyDocumentHash.selector = bytes4(b';\xf3e\xb1')
CreditPolicy.policyDocumentURI.selector = bytes4(b'k\xdaa\x06')
CreditPolicy.policyScopeHash.selector = bytes4(b'\x80U\xc5\xa9')
CreditPolicy.eligibilitySet.selector = bytes4(b'\xfe\xcaF\x99')
CreditPolicy.ratiosSet.selector = bytes4(b'\xb62\xd5|')
CreditPolicy.concentrationSet.selector = bytes4(b'\x90\xff\x8a\xdf')
CreditPolicy.attestationSet.selector = bytes4(b'\xd9\xe5\xc3]')
CreditPolicy.covenantsSet.selector = bytes4(b'cJ\x1c\xd4')
CreditPolicy.hasAtLeastOneTier.selector = bytes4(b'jX\xfc0')
CreditPolicy.initialize.selector = bytes4(b'\xc4\xd6m\xe8')
CreditPolicy.createPolicy.selector = bytes4(b'\x04\xbd\x12\xbb')
CreditPolicy.freezePolicy.selector = bytes4(b'\xfbM\xcb\x8b')
CreditPolicy.deActivatePolicy.selector = bytes4(b'\x0e\xde\xa5\xb8')
CreditPolicy.updateEligibility.selector = bytes4(b'w\xe4\xd4\xad')
CreditPolicy.updateRatios.selector = bytes4(b'\xa4\xd2F\xfa')
CreditPolicy.updateConcentration.selector = bytes4(b'i\xb6S1')
CreditPolicy.updateAttestation.selector = bytes4(b'f0\xb0\x08')
CreditPolicy.updateCovenants.selector = bytes4(b'l\x11\xa3\x86')
CreditPolicy.setLoanTier.selector = bytes4(b'[\x87\xec.')
CreditPolicy.excludeIndustry.selector = bytes4(b'L\xfaz\xf6')
CreditPolicy.includeIndustry.selector = bytes4(b'\x0c5)\xdc')
CreditPolicy.setPolicyDocument.selector = bytes4(b"9'\xa4\xc3")
CreditPolicy.setPolicyScopeHash.selector = bytes4(b'2\xabcP')
CreditPolicy.changePolicyAdmin.selector = bytes4(b'\xf7pq;')
CreditPolicy.isPolicyActive.selector = bytes4(b'\xbd\x8a\xfaF')
CreditPolicy.isPolicyFrozen.selector = bytes4(b'L-b\xb7')
CreditPolicy.tierExistsInPolicy.selector = bytes4(b'Ie\x9c\xdc')
CreditPolicy.setMaxTiers.selector = bytes4(b'\xa3\xa1\xda{')
CreditPolicy.getMaxTiers.selector = bytes4(b'MOqw')
CreditPolicy.isIndustryExcluded.selector = bytes4(b'\xfaOZ\x86')
