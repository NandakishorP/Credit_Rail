
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from wake.development.core import Contract, Library, Address, Account, Chain, RequestType
from wake.development.primitive_types import *
from wake.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.src.interfaces.ICreditPolicy import ICreditPolicy



class CreditPolicy(ICreditPolicy):
    """
    [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#10)
    """
    _abi = {'constructor': {'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'\x11\x1es\xbd': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'CreditPolicy__IncompletePolicy', 'type': 'error'}, b'\x1c\x07zg': {'inputs': [], 'name': 'CreditPolicy__InvalidAdmin', 'type': 'error'}, b'\xdbc.@': {'inputs': [], 'name': 'CreditPolicy__InvalidIndustryHash', 'type': 'error'}, b'B\xe5yW': {'inputs': [{'internalType': 'uint256', 'name': 'count', 'type': 'uint256'}], 'name': 'CreditPolicy__InvalidTierCount', 'type': 'error'}, b'b\xf4\xa2\x07': {'inputs': [], 'name': 'CreditPolicy__InvalidVersion', 'type': 'error'}, b'O\x97\xff2': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'CreditPolicy__PolicyFrozen', 'type': 'error'}, b'KR\x88\x8f': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'CreditPolicy__PolicyNotActive', 'type': 'error'}, b'\n\x1fg\x9b': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'CreditPolicy__PolicyNotEditable', 'type': 'error'}, b'\xc5\xc05\xaa': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'CreditPolicy__PolicyVersionExists', 'type': 'error'}, b'y>\x95\xdf': {'inputs': [], 'name': 'CreditPolicy__Unauthorized', 'type': 'error'}, b'\x12\x10\xd3\xec\xd9r\xf2^\x1e"Qb~\xc8?\xb0\x0c\xb0\xe45\xdb\xe0\xc5\xab\xad\xf3*\x9eP\xee\x9f6': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'IndustryExcluded', 'type': 'event'}, b'\xb0g\xf0\x9a\x9e\x7f\xaf4e\xd2W \xc4\xdc\xa9\xd6I\xffX=\x8a\xc9\xa1b\xdc\x1a- Z\xe9\xb3\x8e': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'IndustryIncluded', 'type': 'event'}, b'\x9c\x88\x9e\xdd\xe3\xe1\x84\x91Z\xa8u\x8b\xed\xa1=\x0bT\x8d\xec\xc0\xb5\xa7\x9f;"\xff\xa3\xd9\xd5}\n\xb2': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'LoanTierUpdated', 'type': 'event'}, b'\x809\xca^z\xb2\x80\x89M\xd9\x80\xcer\xff\xf4g-\xe5\x8c\xbeB\x19\xce\xe5\xda`Y\xab\x85\xdb(\x91': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint8', 'name': 'maxTiers', 'type': 'uint8'}], 'name': 'MaxTiersChanged', 'type': 'event'}, b'H\x16U\x97Ped\xc2>8O\xdea\xcf\x1f!e\x91\xbc\xa2\xc8\xa1\xce\x0b\xbb!S\xd4\xc3\xd8\xeb\xc4': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'address', 'name': 'newAdmin', 'type': 'address'}], 'name': 'PolicyAdminChanged', 'type': 'event'}, b'\xdb\xb6\xd3\x14u\xbe\xc9\x84\x9f\xbf5*|5<\xdf\tmn-\x97,\xf7\x8b\xbadJ\x80&\x9d\xd3{': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyAttestationUpdated', 'type': 'event'}, b'|\x8ac\xa0\xb6\xc9\x98\x1e\x93\xea\xaf\x880{\x94\xe7\xa4\x8aYM\x03P\xa6\x05\xad\xf1\xcf\x9f\xcd\x8e\xc5S': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyConcentrationUpdated', 'type': 'event'}, b'\x968\xa3Q\x9a?\xc3\xe7\xd5\xc0\x10\x14\xe1\x07\x17\x1b#\x8d\x1b\xfe\xd1\xc6\xb8[G.\x18&\xa1\xcf\xc6\xd6': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyCovenantsUpdated', 'type': 'event'}, b'\r(\xab-\xec\x81\xaa\xeb\xf8i\x15\xa8e5:D\xc9w\x9f\xa1\xc6\x15\x8ao\xf7H\xdc\x8e\x14\x84(\x85': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyCreated', 'type': 'event'}, b'dO;\xc1\xa6\xec\x9d\x9b\xf2S\xb2\x19I\xe5f\x906\x17\x173\xd6Vj;\xbeT\xf0,\xd4yp\x0b': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyDeactivated', 'type': 'event'}, b"j\xc7\xbb6\x99\x0b\xe2\n\xfe\x8d'w\xe0:\x1c&\x84\xa4X\x9aQME\xa4\xd6\xf7~Sq\xaa\xfd\xa5": {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'bytes32', 'name': 'hash', 'type': 'bytes32'}, {'indexed': False, 'internalType': 'string', 'name': 'uri', 'type': 'string'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyDocumentSet', 'type': 'event'}, b'jP\xb7\x17K\x84DN\xe4\xfc\x85/0\xebMQ\x05\xa8^`\xb1+\x83\x12$\xdcV-\xaa\xbc=\xcd': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyEligibilityUpdated', 'type': 'event'}, b'\x15\xb1\x8a\xed\x16\xee\rwW\x87\xb6YO\xcfUj\xec!~>V\xf0\x81x\x10\x8d~\xcb\xd5\x99\\+': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyFrozen', 'type': 'event'}, b'&\xa7\xb1\xd1\x89/\x9b\x11ZUaz8\xa1\xbb\xf2\x16\xb6l\x17\x03\xee\x89\xce\xbc\\\x83r]\xa2\xf9$': {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'timestamp', 'type': 'uint256'}], 'name': 'PolicyRatiosUpdated', 'type': 'event'}, b'l 4\xca': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'attestation', 'outputs': [{'internalType': 'uint256', 'name': 'maxAttestationAgeDays', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'reAttestationFrequencyDays', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'requiresCPAAttestation', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd9\xe5\xc3]': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'attestationSet', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xf7pq;': {'inputs': [{'internalType': 'address', 'name': 'newAdmin', 'type': 'address'}], 'name': 'changePolicyAdmin', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b"\xd4\x02\xab'": {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'concentration', 'outputs': [{'internalType': 'uint256', 'name': 'maxSingleBorrowerBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxIndustryConcentrationBps', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x90\xff\x8a\xdf': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'concentrationSet', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'(\xf4\xca1': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'covenants', 'outputs': [{'internalType': 'uint256', 'name': 'maxLeverageRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minCoverageRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minLiquidityAmount', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'allowsDividends', 'type': 'bool'}, {'internalType': 'uint256', 'name': 'reportingFrequencyDays', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'cJ\x1c\xd4': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'covenantsSet', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x04\xbd\x12\xbb': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'createPolicy', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x0e\xde\xa5\xb8': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'deActivatePolicy', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'z\x86\x1a\xdb': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'eligibility', 'outputs': [{'internalType': 'uint256', 'name': 'minAnnualRevenue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minTangibleNetWorth', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minBusinessAgeDays', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxDefaultsLast36Months', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'bankruptcyExcluded', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xfe\xcaF\x99': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'eligibilitySet', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'L\xfaz\xf6': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}], 'name': 'excludeIndustry', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa7Z\x04q': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'excludedIndustries', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xfbM\xcb\x8b': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'freezePolicy', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'MOqw': {'inputs': [], 'name': 'getMaxTiers', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, b'jX\xfc0': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'hasAtLeastOneTier', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\x0c5)\xdc': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}], 'name': 'includeIndustry', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xfaOZ\x86': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'industry', 'type': 'bytes32'}], 'name': 'isIndustryExcluded', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbd\x8a\xfaF': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'isPolicyActive', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'L-b\xb7': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'isPolicyFrozen', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'$\xa2\x95"': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'lastUpdated', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'[\xff\xd8\x8f': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'name': 'loanTiers', 'outputs': [{'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'uint256', 'name': 'minRevenue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxRevenue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxDebtToEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxLoanToEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestRateBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'originationFeeBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'termDays', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'active', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'J\tm+': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'policyActive', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'X\xe5\x18\x96': {'inputs': [], 'name': 'policyAdmin', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'J\xe8\xd2\x1a': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'policyCreated', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b';\xf3e\xb1': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'policyDocumentHash', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'k\xdaa\x06': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'policyDocumentURI', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'P7\xf1{': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'policyFrozen', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'w\x1d\xc8j': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'ratios', 'outputs': [{'internalType': 'uint256', 'name': 'maxTotalDebtToEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minInterestCoverageRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minCurrentRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minEBITDAMarginBps', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xb62\xd5|': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'ratiosSet', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'[\x87\xec.': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}, {'components': [{'internalType': 'string', 'name': 'name', 'type': 'string'}, {'internalType': 'uint256', 'name': 'minRevenue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxRevenue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxDebtToEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxLoanToEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'interestRateBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'originationFeeBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'termDays', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'active', 'type': 'bool'}], 'internalType': 'struct CreditPolicy.LoanTier', 'name': 'tier', 'type': 'tuple'}], 'name': 'setLoanTier', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa3\xa1\xda{': {'inputs': [{'internalType': 'uint8', 'name': '_maxTiers', 'type': 'uint8'}], 'name': 'setMaxTiers', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b"9'\xa4\xc3": {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'bytes32', 'name': 'hash', 'type': 'bytes32'}, {'internalType': 'string', 'name': 'uri', 'type': 'string'}], 'name': 'setPolicyDocument', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x8bbK\x10': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'name': 'tierExists', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'Ie\x9c\xdc': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'tierId', 'type': 'uint8'}], 'name': 'tierExistsInPolicy', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, b'\xfe&\xd9e': {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'totalTiers', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, b'f0\xb0\x08': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'components': [{'internalType': 'uint256', 'name': 'maxAttestationAgeDays', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'reAttestationFrequencyDays', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'requiresCPAAttestation', 'type': 'bool'}], 'internalType': 'struct CreditPolicy.AttestationRequirements', 'name': 'data', 'type': 'tuple'}], 'name': 'updateAttestation', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'i\xb6S1': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'components': [{'internalType': 'uint256', 'name': 'maxSingleBorrowerBps', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxIndustryConcentrationBps', 'type': 'uint256'}], 'internalType': 'struct CreditPolicy.ConcentrationLimits', 'name': 'data', 'type': 'tuple'}], 'name': 'updateConcentration', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'l\x11\xa3\x86': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'components': [{'internalType': 'uint256', 'name': 'maxLeverageRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minCoverageRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minLiquidityAmount', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'allowsDividends', 'type': 'bool'}, {'internalType': 'uint256', 'name': 'reportingFrequencyDays', 'type': 'uint256'}], 'internalType': 'struct CreditPolicy.MaintenanceCovenants', 'name': 'data', 'type': 'tuple'}], 'name': 'updateCovenants', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'w\xe4\xd4\xad': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'components': [{'internalType': 'uint256', 'name': 'minAnnualRevenue', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minTangibleNetWorth', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minBusinessAgeDays', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'maxDefaultsLast36Months', 'type': 'uint256'}, {'internalType': 'bool', 'name': 'bankruptcyExcluded', 'type': 'bool'}], 'internalType': 'struct CreditPolicy.EligibilityCriteria', 'name': 'data', 'type': 'tuple'}], 'name': 'updateEligibility', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xa4\xd2F\xfa': {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}, {'components': [{'internalType': 'uint256', 'name': 'maxTotalDebtToEBITDA', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minInterestCoverageRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minCurrentRatio', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'minEBITDAMarginBps', 'type': 'uint256'}], 'internalType': 'struct CreditPolicy.FinancialRatios', 'name': 'data', 'type': 'tuple'}], 'name': 'updateRatios', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _storage_layout = {"storage":[{"astId":39918,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"policyAdmin","offset":0,"slot":0,"type":"t_address"},{"astId":39920,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxTiers","offset":20,"slot":0,"type":"t_uint8"},{"astId":39924,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"policyCreated","offset":0,"slot":1,"type":"t_mapping(t_uint256,t_bool)"},{"astId":39928,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"policyFrozen","offset":0,"slot":2,"type":"t_mapping(t_uint256,t_bool)"},{"astId":39932,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"policyActive","offset":0,"slot":3,"type":"t_mapping(t_uint256,t_bool)"},{"astId":39936,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"lastUpdated","offset":0,"slot":4,"type":"t_mapping(t_uint256,t_uint256)"},{"astId":39954,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"eligibility","offset":0,"slot":5,"type":"t_mapping(t_uint256,t_struct(EligibilityCriteria)39949_storage)"},{"astId":39968,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"ratios","offset":0,"slot":6,"type":"t_mapping(t_uint256,t_struct(FinancialRatios)39963_storage)"},{"astId":39996,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"loanTiers","offset":0,"slot":7,"type":"t_mapping(t_uint256,t_mapping(t_uint8,t_struct(LoanTier)39989_storage))"},{"astId":40000,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"totalTiers","offset":0,"slot":8,"type":"t_mapping(t_uint256,t_uint8)"},{"astId":40006,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"tierExists","offset":0,"slot":9,"type":"t_mapping(t_uint256,t_mapping(t_uint8,t_bool))"},{"astId":40016,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"concentration","offset":0,"slot":10,"type":"t_mapping(t_uint256,t_struct(ConcentrationLimits)40011_storage)"},{"astId":40022,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"excludedIndustries","offset":0,"slot":11,"type":"t_mapping(t_uint256,t_mapping(t_bytes32,t_bool))"},{"astId":40034,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"attestation","offset":0,"slot":12,"type":"t_mapping(t_uint256,t_struct(AttestationRequirements)40029_storage)"},{"astId":40050,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"covenants","offset":0,"slot":13,"type":"t_mapping(t_uint256,t_struct(MaintenanceCovenants)40045_storage)"},{"astId":40054,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"policyDocumentHash","offset":0,"slot":14,"type":"t_mapping(t_uint256,t_bytes32)"},{"astId":40058,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"policyDocumentURI","offset":0,"slot":15,"type":"t_mapping(t_uint256,t_string_storage)"},{"astId":40062,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"eligibilitySet","offset":0,"slot":16,"type":"t_mapping(t_uint256,t_bool)"},{"astId":40066,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"ratiosSet","offset":0,"slot":17,"type":"t_mapping(t_uint256,t_bool)"},{"astId":40070,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"concentrationSet","offset":0,"slot":18,"type":"t_mapping(t_uint256,t_bool)"},{"astId":40074,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"attestationSet","offset":0,"slot":19,"type":"t_mapping(t_uint256,t_bool)"},{"astId":40078,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"covenantsSet","offset":0,"slot":20,"type":"t_mapping(t_uint256,t_bool)"},{"astId":40082,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"hasAtLeastOneTier","offset":0,"slot":21,"type":"t_mapping(t_uint256,t_bool)"}],"types":{"t_address":{"encoding":"inplace","label":"address","numberOfBytes":20},"t_bool":{"encoding":"inplace","label":"bool","numberOfBytes":1},"t_bytes32":{"encoding":"inplace","label":"bytes32","numberOfBytes":32},"t_mapping(t_bytes32,t_bool)":{"encoding":"mapping","label":"mapping(bytes32 => bool)","numberOfBytes":32,"key":"t_bytes32","value":"t_bool"},"t_mapping(t_uint256,t_bool)":{"encoding":"mapping","label":"mapping(uint256 => bool)","numberOfBytes":32,"key":"t_uint256","value":"t_bool"},"t_mapping(t_uint256,t_bytes32)":{"encoding":"mapping","label":"mapping(uint256 => bytes32)","numberOfBytes":32,"key":"t_uint256","value":"t_bytes32"},"t_mapping(t_uint256,t_mapping(t_bytes32,t_bool))":{"encoding":"mapping","label":"mapping(uint256 => mapping(bytes32 => bool))","numberOfBytes":32,"key":"t_uint256","value":"t_mapping(t_bytes32,t_bool)"},"t_mapping(t_uint256,t_mapping(t_uint8,t_bool))":{"encoding":"mapping","label":"mapping(uint256 => mapping(uint8 => bool))","numberOfBytes":32,"key":"t_uint256","value":"t_mapping(t_uint8,t_bool)"},"t_mapping(t_uint256,t_mapping(t_uint8,t_struct(LoanTier)39989_storage))":{"encoding":"mapping","label":"mapping(uint256 => mapping(uint8 => struct CreditPolicy.LoanTier))","numberOfBytes":32,"key":"t_uint256","value":"t_mapping(t_uint8,t_struct(LoanTier)39989_storage)"},"t_mapping(t_uint256,t_string_storage)":{"encoding":"mapping","label":"mapping(uint256 => string)","numberOfBytes":32,"key":"t_uint256","value":"t_string_storage"},"t_mapping(t_uint256,t_struct(AttestationRequirements)40029_storage)":{"encoding":"mapping","label":"mapping(uint256 => struct CreditPolicy.AttestationRequirements)","numberOfBytes":32,"key":"t_uint256","value":"t_struct(AttestationRequirements)40029_storage"},"t_mapping(t_uint256,t_struct(ConcentrationLimits)40011_storage)":{"encoding":"mapping","label":"mapping(uint256 => struct CreditPolicy.ConcentrationLimits)","numberOfBytes":32,"key":"t_uint256","value":"t_struct(ConcentrationLimits)40011_storage"},"t_mapping(t_uint256,t_struct(EligibilityCriteria)39949_storage)":{"encoding":"mapping","label":"mapping(uint256 => struct CreditPolicy.EligibilityCriteria)","numberOfBytes":32,"key":"t_uint256","value":"t_struct(EligibilityCriteria)39949_storage"},"t_mapping(t_uint256,t_struct(FinancialRatios)39963_storage)":{"encoding":"mapping","label":"mapping(uint256 => struct CreditPolicy.FinancialRatios)","numberOfBytes":32,"key":"t_uint256","value":"t_struct(FinancialRatios)39963_storage"},"t_mapping(t_uint256,t_struct(MaintenanceCovenants)40045_storage)":{"encoding":"mapping","label":"mapping(uint256 => struct CreditPolicy.MaintenanceCovenants)","numberOfBytes":32,"key":"t_uint256","value":"t_struct(MaintenanceCovenants)40045_storage"},"t_mapping(t_uint256,t_uint256)":{"encoding":"mapping","label":"mapping(uint256 => uint256)","numberOfBytes":32,"key":"t_uint256","value":"t_uint256"},"t_mapping(t_uint256,t_uint8)":{"encoding":"mapping","label":"mapping(uint256 => uint8)","numberOfBytes":32,"key":"t_uint256","value":"t_uint8"},"t_mapping(t_uint8,t_bool)":{"encoding":"mapping","label":"mapping(uint8 => bool)","numberOfBytes":32,"key":"t_uint8","value":"t_bool"},"t_mapping(t_uint8,t_struct(LoanTier)39989_storage)":{"encoding":"mapping","label":"mapping(uint8 => struct CreditPolicy.LoanTier)","numberOfBytes":32,"key":"t_uint8","value":"t_struct(LoanTier)39989_storage"},"t_string_storage":{"encoding":"bytes","label":"string","numberOfBytes":32},"t_struct(AttestationRequirements)40029_storage":{"encoding":"inplace","label":"struct CreditPolicy.AttestationRequirements","numberOfBytes":96,"members":[{"astId":40024,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxAttestationAgeDays","offset":0,"slot":0,"type":"t_uint256"},{"astId":40026,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"reAttestationFrequencyDays","offset":0,"slot":1,"type":"t_uint256"},{"astId":40028,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"requiresCPAAttestation","offset":0,"slot":2,"type":"t_bool"}]},"t_struct(ConcentrationLimits)40011_storage":{"encoding":"inplace","label":"struct CreditPolicy.ConcentrationLimits","numberOfBytes":64,"members":[{"astId":40008,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxSingleBorrowerBps","offset":0,"slot":0,"type":"t_uint256"},{"astId":40010,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxIndustryConcentrationBps","offset":0,"slot":1,"type":"t_uint256"}]},"t_struct(EligibilityCriteria)39949_storage":{"encoding":"inplace","label":"struct CreditPolicy.EligibilityCriteria","numberOfBytes":192,"members":[{"astId":39938,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minAnnualRevenue","offset":0,"slot":0,"type":"t_uint256"},{"astId":39940,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minEBITDA","offset":0,"slot":1,"type":"t_uint256"},{"astId":39942,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minTangibleNetWorth","offset":0,"slot":2,"type":"t_uint256"},{"astId":39944,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minBusinessAgeDays","offset":0,"slot":3,"type":"t_uint256"},{"astId":39946,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxDefaultsLast36Months","offset":0,"slot":4,"type":"t_uint256"},{"astId":39948,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"bankruptcyExcluded","offset":0,"slot":5,"type":"t_bool"}]},"t_struct(FinancialRatios)39963_storage":{"encoding":"inplace","label":"struct CreditPolicy.FinancialRatios","numberOfBytes":128,"members":[{"astId":39956,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxTotalDebtToEBITDA","offset":0,"slot":0,"type":"t_uint256"},{"astId":39958,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minInterestCoverageRatio","offset":0,"slot":1,"type":"t_uint256"},{"astId":39960,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minCurrentRatio","offset":0,"slot":2,"type":"t_uint256"},{"astId":39962,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minEBITDAMarginBps","offset":0,"slot":3,"type":"t_uint256"}]},"t_struct(LoanTier)39989_storage":{"encoding":"inplace","label":"struct CreditPolicy.LoanTier","numberOfBytes":320,"members":[{"astId":39970,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"name","offset":0,"slot":0,"type":"t_string_storage"},{"astId":39972,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minRevenue","offset":0,"slot":1,"type":"t_uint256"},{"astId":39974,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxRevenue","offset":0,"slot":2,"type":"t_uint256"},{"astId":39976,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minEBITDA","offset":0,"slot":3,"type":"t_uint256"},{"astId":39978,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxDebtToEBITDA","offset":0,"slot":4,"type":"t_uint256"},{"astId":39980,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxLoanToEBITDA","offset":0,"slot":5,"type":"t_uint256"},{"astId":39982,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"interestRateBps","offset":0,"slot":6,"type":"t_uint256"},{"astId":39984,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"originationFeeBps","offset":0,"slot":7,"type":"t_uint256"},{"astId":39986,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"termDays","offset":0,"slot":8,"type":"t_uint256"},{"astId":39988,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"active","offset":0,"slot":9,"type":"t_bool"}]},"t_struct(MaintenanceCovenants)40045_storage":{"encoding":"inplace","label":"struct CreditPolicy.MaintenanceCovenants","numberOfBytes":160,"members":[{"astId":40036,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"maxLeverageRatio","offset":0,"slot":0,"type":"t_uint256"},{"astId":40038,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minCoverageRatio","offset":0,"slot":1,"type":"t_uint256"},{"astId":40040,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"minLiquidityAmount","offset":0,"slot":2,"type":"t_uint256"},{"astId":40042,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"allowsDividends","offset":0,"slot":3,"type":"t_bool"},{"astId":40044,"contract":"src/CreditPolicy.sol:CreditPolicy","label":"reportingFrequencyDays","offset":0,"slot":4,"type":"t_uint256"}]},"t_uint256":{"encoding":"inplace","label":"uint256","numberOfBytes":32},"t_uint8":{"encoding":"inplace","label":"uint8","numberOfBytes":1}}}
    _creation_code = "608080604052346026575f80546001600160a01b031916331790556117c1908161002b8239f35b5f80fdfe60806040526004361015610011575f80fd5b5f3560e01c806304bd12bb1461150d5780630c3529dc1461146e5780630edea5b8146113f857806324a29522146113ce57806328f4ca31146113735780633927a4c31461114c5780633bf365b11461112257806349659cdc146106bb5780634a096d2b146104ea5780634ae8d21a146110f35780634c2d62b714610fec5780634cfa7af61461103d5780634d4f71771461101b5780635037f17b14610fec57806358e5189614610fc55780635b87ec2e14610c995780635bffd88f14610bd7578063634a1cd414610ba85780636630b00814610ad857806369b6533114610a315780636a58fc3014610a025780636bda6106146109c05780636c11a386146108df5780636c2034ca14610899578063771dc86a1461084d57806377e4d4ad146107655780637a861adb146106ff5780638b624b10146106bb57806390ff8adf1461068c578063a3a1da7b146105ff578063a4d246fa14610548578063a75a0471146103d2578063b632d57c14610519578063bd8afa46146104ea578063d402ab27146104b7578063d9e5c35d14610488578063f770713b14610406578063fa4f5a86146103d2578063fb4dcb8b1461023c578063fe26d9651461020f5763feca4699146101dc575f80fd5b3461020b57602036600319011261020b576004355f526010602052602060ff60405f2054166040519015158152f35b5f80fd5b3461020b57602036600319011261020b576004355f526008602052602060ff60405f205416604051908152f35b3461020b57602036600319011261020b5760043561025861170c565b6102618161172e565b805f52600260205260ff60405f2054166103c057805f52600360205260ff60405f205416156103ae57805f52601060205260ff60405f205416158015610397575b8015610380575b8015610369575b8015610352575b801561033b575b61032957805f52600e60205260405f205415610329576040817f15b18aed16ee0d775787b6594fcf556aec217e3e56f08178108d7ecbd5995c2b925f526002602052815f20600160ff19825416179055805f52600460205242825f20558151908152426020820152a1005b63111e73bd60e01b5f5260045260245ffd5b50805f52601560205260ff60405f205416156102be565b50805f52601460205260ff60405f205416156102b7565b50805f52601360205260ff60405f205416156102b0565b50805f52601260205260ff60405f205416156102a9565b50805f52601160205260ff60405f205416156102a2565b634b52888f60e01b5f5260045260245ffd5b6327cbff9960e11b5f5260045260245ffd5b3461020b576103e0366115cf565b905f52600b60205260405f20905f52602052602060ff60405f2054166040519015158152f35b3461020b57602036600319011261020b576004356001600160a01b0381169081900361020b5761043461170c565b8015610479575f80546001600160a01b031916821790556040519081527f48165597506564c23e384fde61cf1f216591bca2c8a1ce0bbb2153d4c3d8ebc490602090a1005b631c077a6760e01b5f5260045ffd5b3461020b57602036600319011261020b576004355f526013602052602060ff60405f2054166040519015158152f35b3461020b57602036600319011261020b576004355f52600a6020526040805f206001815491015482519182526020820152f35b3461020b57602036600319011261020b576004355f526003602052602060ff60405f2054166040519015158152f35b3461020b57602036600319011261020b576004355f526011602052602060ff60405f2054166040519015158152f35b3461020b5760a036600319011261020b57600435608036602319011261020b5760407f26a7b1d1892f9b115a55617a38a1bbf216b66c1703ee89cebc5c83725da2f9249161059461170c565b61059d8161172e565b6105a681611744565b805f526006602052815f206024358155604435600182015560643560028201556003608435910155805f52600460205242825f2055805f526011602052815f20600160ff198254161790558151908152426020820152a1005b3461020b57602036600319011261020b5760043560ff81169081810361020b5761062761170c565b60ff8214610679575f805460ff60a01b191660a09290921b60ff60a01b169190911790556040519081527f8039ca5e7ab280894dd980ce72fff4672de58cbe4219cee5da6059ab85db289190602090a1005b506342e5795760e01b5f5260045260245ffd5b3461020b57602036600319011261020b576004355f526012602052602060ff60405f2054166040519015158152f35b3461020b57604036600319011261020b576106d46115e5565b6004355f52600960205260ff60405f2091165f52602052602060ff60405f2054166040519015158152f35b3461020b57602036600319011261020b576004355f52600560205260c060405f20805490600181015490600281015460038201549060ff6005600485015494015416936040519586526020860152604085015260608401526080830152151560a0820152f35b3461020b5760e036600319011261020b5760043560c036602319011261020b5761078d61170c565b6107968161172e565b61079f81611744565b805f52600560205260405f2090602435825560443560018301556064356002830155608435600383015560a435600483015560c43590811515820361020b5761081c8260057f6a50b7174b84444ee4fc852f30eb4d5105a85e60b12b831224dc562daabc3dcd9560409550019060ff801983541691151516179055565b805f52600460205242825f2055805f526010602052815f20600160ff198254161790558151908152426020820152a1005b3461020b57602036600319011261020b576004355f526006602052608060405f208054906001810154906003600282015491015491604051938452602084015260408301526060820152f35b3461020b57602036600319011261020b576004355f52600c602052606060405f2080549060ff600260018301549201541690604051928352602083015215156040820152f35b3461020b5760c036600319011261020b5760043560a036602319011261020b5761090761170c565b6109108161172e565b61091981611744565b805f52600d60205260405f209060243582556044356001830155606435600283015560843590811515820361020b577f9638a3519a3fc3e7d5c01014e107171b238d1bfed1c6b85b472e1826a1cfc6d6926109878360409450600383019060ff801983541691151516179055565b600460a435910155805f52600460205242825f2055805f526014602052815f20600160ff198254161790558151908152426020820152a1005b3461020b57602036600319011261020b576004355f52600f6020526109fe6109ea60405f2061162d565b6040519182916020835260208301906116e8565b0390f35b3461020b57602036600319011261020b576004355f526015602052602060ff60405f2054166040519015158152f35b3461020b57606036600319011261020b57600435604036602319011261020b5760407f7c8a63a0b6c9981e93eaaf88307b94e7a48a594d0350a605adf1cf9fcd8ec55391610a7d61170c565b610a868161172e565b610a8f81611744565b805f52600a602052815f2060243581556001604435910155805f52600460205242825f2055805f526012602052815f20600160ff198254161790558151908152426020820152a1005b3461020b57608036600319011261020b57600435606036602319011261020b57610b0061170c565b610b098161172e565b610b1281611744565b805f52600c60205260405f20906024358255604435600183015560643590811515820361020b57610b778260027fdbb6d31475bec9849fbf352a7c353cdf096d6e2d972cf78bba644a80269dd37b9560409550019060ff801983541691151516179055565b805f52600460205242825f2055805f526013602052815f20600160ff198254161790558151908152426020820152a1005b3461020b57602036600319011261020b576004355f526014602052602060ff60405f2054166040519015158152f35b3461020b57604036600319011261020b57610bf06115e5565b6004355f52600760205260ff60405f2091165f52602052610c6360405f20610c178161162d565b9060018101549060028101549060038101546004820154600583015460068401549160078501549360ff6009600888015497015416966040519a8b9a6101408c526101408c01906116e8565b9860208b015260408a01526060890152608088015260a087015260c086015260e085015261010084015215156101208301520390f35b3461020b57606036600319011261020b57600435610cb56115e5565b9060443567ffffffffffffffff811161020b578036039061014060031983011261020b57610ce161170c565b610cea8361172e565b610cf383611744565b60ff805f5460a01c16941693841015610fb257825f52600760205260405f20845f5260205260405f20918160040135906022190181121561020b57810160048101359067ffffffffffffffff821161020b57813603602482011361020b57610d5b84546115f5565b601f8111610f61575b505f90601f8311600114610ef2576101249392915f9183610ee4575b50508160011b915f199060031b1c19161783555b6024810135600184015560448101356002840155606481013560038401556084810135600484015560a4810135600584015560c4810135600684015560e4810135600784015561010481013560088401550135801515810361020b576009610e0892019060ff801983541691151516179055565b805f52600960205260405f20825f5260205260405f20600160ff19825416179055805f52600860205260ff60405f205416821015610e9f575b807f9c889edde3e184915aa8758beda13d0b548decc0b5a79f3b22ffa3d9d57d0ab2926060925f52601560205260405f20600160ff19825416179055815f5260046020524260405f20556040519182526020820152426040820152a1005b600182019060ff8211610ed0575f818152600860205260409020805460ff191660ff90931692909217909155610e41565b634e487b7160e01b5f52601160045260245ffd5b016024013590508780610d80565b601f19831691855f5260205f20925f5b818110610f46575091600193918561012497969410610f29575b505050811b018355610d94565b6024910101355f19600384901b60f8161c19169055878080610f1c565b60248484010135855560019094019360209283019201610f02565b82811115610d6457845f5260205f20601f840160051c9060208510610faa575b81601f9101920160051c03905f5b828110610f9d575050610d64565b5f82820155600101610f8f565b5f9150610f81565b836342e5795760e01b5f5260045260245ffd5b3461020b575f36600319011261020b575f546040516001600160a01b039091168152602090f35b3461020b57602036600319011261020b576004355f526002602052602060ff60405f2054166040519015158152f35b3461020b575f36600319011261020b57602060ff5f5460a01c16604051908152f35b3461020b5761104b366115cf565b9061105461170c565b61105d8161172e565b61106681611744565b81156110e4577f1210d3ecd972f25e1e2251627ec83fb00cb0e435dbe0c5abadf32a9e50ee9f3691815f52600b60205260405f20815f5260205260405f20600160ff19825416179055815f5260046020524260405f20556110df6040519283924291846040919493926060820195825260208201520152565b0390a1005b63036d8cb960e61b5f5260045ffd5b3461020b57602036600319011261020b576004355f526001602052602060ff60405f2054166040519015158152f35b3461020b57602036600319011261020b576004355f52600e602052602060405f2054604051908152f35b3461020b57606036600319011261020b5760043560243560443567ffffffffffffffff811161020b573660238201121561020b5780600401359067ffffffffffffffff821161020b57366024838301011161020b576111a961170c565b6111b28461172e565b6111bb84611744565b835f52600e6020528260405f2055835f52600f60205260405f206111df81546115f5565b601f8111611322575b505f601f8411600114611291579260247f6ac7bb36990be20afe8d2777e03a1c2684a4589a514d45a4d6f77e5371aafda5969382938360a0975f91611284575b508460011b905f198660031b1c19161790555b845f5260046020524260405f2055604051968795865260208601526080604086015282608086015201848401375f828201840152426060830152601f01601f19168101030190a1005b849150830101358a611228565b601f19841690825f5260205f20915f5b8181106113075750938593849360249360a0987f6ac7bb36990be20afe8d2777e03a1c2684a4589a514d45a4d6f77e5371aafda59b98106112ec575b5050600184811b01905561123b565b83018401355f19600387901b60f8161c1916905589806112dd565b91926020600181926024878a010135815501940192016112a1565b838111156111e857815f5260205f20601f850160051c906020861061136b575b81601f9101920160051c03905f5b82811061135e5750506111e8565b5f82820155600101611350565b5f9150611342565b3461020b57602036600319011261020b576004355f52600d60205260a060405f208054906001810154906002810154600460ff6003840154169201549260405194855260208501526040840152151560608301526080820152f35b3461020b57602036600319011261020b576004355f526004602052602060405f2054604051908152f35b3461020b57602036600319011261020b577f644f3bc1a6ec9d9bf253b21949e5669036171733d6566a3bbe54f02cd479700b604060043561143761170c565b6114408161172e565b805f526003602052815f2060ff198154169055805f52600460205242825f20558151908152426020820152a1005b3461020b5761147c366115cf565b9061148561170c565b61148e8161172e565b61149781611744565b81156110e4577fb067f09a9e7faf3465d25720c4dca9d649ff583d8ac9a162dc1a2d205ae9b38e91815f52600b60205260405f20815f5260205260405f2060ff198154169055815f5260046020524260405f20556110df6040519283924291846040919493926060820195825260208201520152565b3461020b57602036600319011261020b5760043561152961170c565b80156115c057805f52600160205260ff60405f2054166115ae576040817f0d28ab2dec81aaebf86915a865353a44c9779fa1c6158a6ff748dc8e14842885925f526001602052815f20600160ff19825416179055805f526003602052815f20600160ff19825416179055805f52600460205242825f20558151908152426020820152a1005b6362e01ad560e11b5f5260045260245ffd5b6362f4a20760e01b5f5260045ffd5b604090600319011261020b576004359060243590565b6024359060ff8216820361020b57565b90600182811c92168015611623575b602083101461160f57565b634e487b7160e01b5f52602260045260245ffd5b91607f1691611604565b90604051915f90805490611640826115f5565b80865291600181169081156116ca5750600114611692575b5050829003601f01601f1916820167ffffffffffffffff81118382101761167e57604052565b634e487b7160e01b5f52604160045260245ffd5b9091505f5260205f205f905b8282106116b45750602091508301015f80611658565b600181602092548385890101520191019061169e565b9150506020925060ff191682850152151560051b8301015f80611658565b805180835260209291819084018484015e5f828201840152601f01601f1916010190565b5f546001600160a01b0316330361171f57565b63793e95df60e01b5f5260045ffd5b5f52600160205260ff60405f205416156115c057565b805f52600260205260ff60405f2054168015611774575b6117625750565b630a1f679b60e01b5f5260045260245ffd5b50805f52600360205260ff60405f2054161561175b56fea26469706673582212207cf62a015fb4ef13a4770395702ec6950ba1d2fdc723171d262d2b30800ea51d64736f6c63430008210033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#203)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> CreditPolicy:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#203)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#203)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#203)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[CreditPolicy]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#203)
        """
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, CreditPolicy, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[CreditPolicy]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#203)
        """
        return cls._deploy(request_type, [], return_tx, CreditPolicy, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class EligibilityCriteria:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#72)

        Attributes:
            minAnnualRevenue (uint256): uint256
            minEBITDA (uint256): uint256
            minTangibleNetWorth (uint256): uint256
            minBusinessAgeDays (uint256): uint256
            maxDefaultsLast36Months (uint256): uint256
            bankruptcyExcluded (bool): bool
        """
        original_name = 'EligibilityCriteria'

        minAnnualRevenue: uint256
        minEBITDA: uint256
        minTangibleNetWorth: uint256
        minBusinessAgeDays: uint256
        maxDefaultsLast36Months: uint256
        bankruptcyExcluded: bool


    @dataclasses.dataclass
    class FinancialRatios:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#86)

        Attributes:
            maxTotalDebtToEBITDA (uint256): uint256
            minInterestCoverageRatio (uint256): uint256
            minCurrentRatio (uint256): uint256
            minEBITDAMarginBps (uint256): uint256
        """
        original_name = 'FinancialRatios'

        maxTotalDebtToEBITDA: uint256
        minInterestCoverageRatio: uint256
        minCurrentRatio: uint256
        minEBITDAMarginBps: uint256


    @dataclasses.dataclass
    class LoanTier:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#98)

        Attributes:
            name (str): string
            minRevenue (uint256): uint256
            maxRevenue (uint256): uint256
            minEBITDA (uint256): uint256
            maxDebtToEBITDA (uint256): uint256
            maxLoanToEBITDA (uint256): uint256
            interestRateBps (uint256): uint256
            originationFeeBps (uint256): uint256
            termDays (uint256): uint256
            active (bool): bool
        """
        original_name = 'LoanTier'

        name: str
        minRevenue: uint256
        maxRevenue: uint256
        minEBITDA: uint256
        maxDebtToEBITDA: uint256
        maxLoanToEBITDA: uint256
        interestRateBps: uint256
        originationFeeBps: uint256
        termDays: uint256
        active: bool


    @dataclasses.dataclass
    class ConcentrationLimits:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#118)

        Attributes:
            maxSingleBorrowerBps (uint256): uint256
            maxIndustryConcentrationBps (uint256): uint256
        """
        original_name = 'ConcentrationLimits'

        maxSingleBorrowerBps: uint256
        maxIndustryConcentrationBps: uint256


    @dataclasses.dataclass
    class AttestationRequirements:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#133)

        Attributes:
            maxAttestationAgeDays (uint256): uint256
            reAttestationFrequencyDays (uint256): uint256
            requiresCPAAttestation (bool): bool
        """
        original_name = 'AttestationRequirements'

        maxAttestationAgeDays: uint256
        reAttestationFrequencyDays: uint256
        requiresCPAAttestation: bool


    @dataclasses.dataclass
    class MaintenanceCovenants:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#144)

        Attributes:
            maxLeverageRatio (uint256): uint256
            minCoverageRatio (uint256): uint256
            minLiquidityAmount (uint256): uint256
            allowsDividends (bool): bool
            reportingFrequencyDays (uint256): uint256
        """
        original_name = 'MaintenanceCovenants'

        maxLeverageRatio: uint256
        minCoverageRatio: uint256
        minLiquidityAmount: uint256
        allowsDividends: bool
        reportingFrequencyDays: uint256


    @dataclasses.dataclass
    class CreditPolicy__Unauthorized(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#14)
        """
        _abi = {'inputs': [], 'name': 'CreditPolicy__Unauthorized', 'type': 'error'}
        original_name = 'CreditPolicy__Unauthorized'
        selector = bytes4(b'y>\x95\xdf')



    @dataclasses.dataclass
    class CreditPolicy__PolicyFrozen(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#15)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#16)
        """
        _abi = {'inputs': [], 'name': 'CreditPolicy__InvalidVersion', 'type': 'error'}
        original_name = 'CreditPolicy__InvalidVersion'
        selector = bytes4(b'b\xf4\xa2\x07')



    @dataclasses.dataclass
    class CreditPolicy__PolicyVersionExists(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#17)

        Attributes:
            version (uint256): uint256
        """
        _abi = {'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'CreditPolicy__PolicyVersionExists', 'type': 'error'}
        original_name = 'CreditPolicy__PolicyVersionExists'
        selector = bytes4(b'\xc5\xc05\xaa')

        version: uint256


    @dataclasses.dataclass
    class CreditPolicy__InvalidAdmin(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#18)
        """
        _abi = {'inputs': [], 'name': 'CreditPolicy__InvalidAdmin', 'type': 'error'}
        original_name = 'CreditPolicy__InvalidAdmin'
        selector = bytes4(b'\x1c\x07zg')



    @dataclasses.dataclass
    class CreditPolicy__PolicyNotEditable(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#19)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#20)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#21)
        """
        _abi = {'inputs': [], 'name': 'CreditPolicy__InvalidIndustryHash', 'type': 'error'}
        original_name = 'CreditPolicy__InvalidIndustryHash'
        selector = bytes4(b'\xdbc.@')



    @dataclasses.dataclass
    class CreditPolicy__PolicyNotActive(TransactionRevertedError):
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#22)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#23)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#170)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#171)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#172)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#173)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#174)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#175)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#176)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#177)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#178)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#183)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#184)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#190)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#192)

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
    class PolicyDeactivated:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#198)

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
    def policyAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#58)

        Returns:
            policyAdmin: address
        """
        ...

    @overload
    def policyAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#58)

        Returns:
            policyAdmin: address
        """
        ...

    @overload
    def policyAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#58)

        Returns:
            policyAdmin: address
        """
        ...

    @overload
    def policyAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#58)

        Returns:
            policyAdmin: address
        """
        ...

    def policyAdmin(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#58)

        Returns:
            policyAdmin: address
        """
        return self._execute(self.chain, request_type, "58e51896", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def policyCreated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#64)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def policyCreated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#64)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def policyCreated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#64)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def policyCreated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#64)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    def policyCreated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#64)

        Args:
            key0: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "4ae8d21a", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def policyFrozen(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#65)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def policyFrozen(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#65)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def policyFrozen(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#65)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def policyFrozen(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#65)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    def policyFrozen(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#65)

        Args:
            key0: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "5037f17b", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def policyActive(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#66)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def policyActive(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#66)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def policyActive(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#66)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def policyActive(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#66)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    def policyActive(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#66)

        Args:
            key0: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "4a096d2b", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def lastUpdated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#67)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def lastUpdated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#67)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def lastUpdated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#67)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    @overload
    def lastUpdated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#67)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        ...

    def lastUpdated(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#67)

        Args:
            key0: uint256
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "24a29522", [key0], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def eligibility(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> CreditPolicy.EligibilityCriteria:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#81)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.EligibilityCriteria
        """
        ...

    @overload
    def eligibility(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#81)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.EligibilityCriteria
        """
        ...

    @overload
    def eligibility(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#81)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.EligibilityCriteria
        """
        ...

    @overload
    def eligibility(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[CreditPolicy.EligibilityCriteria]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#81)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.EligibilityCriteria
        """
        ...

    def eligibility(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[CreditPolicy.EligibilityCriteria, TransactionAbc[CreditPolicy.EligibilityCriteria], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#81)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.EligibilityCriteria
        """
        return self._execute(self.chain, request_type, "7a861adb", [key0], True if request_type == "tx" else False, CreditPolicy.EligibilityCriteria, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def ratios(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> CreditPolicy.FinancialRatios:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#93)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.FinancialRatios
        """
        ...

    @overload
    def ratios(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#93)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.FinancialRatios
        """
        ...

    @overload
    def ratios(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#93)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.FinancialRatios
        """
        ...

    @overload
    def ratios(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[CreditPolicy.FinancialRatios]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#93)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.FinancialRatios
        """
        ...

    def ratios(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[CreditPolicy.FinancialRatios, TransactionAbc[CreditPolicy.FinancialRatios], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#93)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.FinancialRatios
        """
        return self._execute(self.chain, request_type, "771dc86a", [key0], True if request_type == "tx" else False, CreditPolicy.FinancialRatios, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def loanTiers(self, key0: uint256, key1: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> CreditPolicy.LoanTier:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#111)

        Args:
            key0: uint256
            key1: uint8
        Returns:
            struct CreditPolicy.LoanTier
        """
        ...

    @overload
    def loanTiers(self, key0: uint256, key1: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#111)

        Args:
            key0: uint256
            key1: uint8
        Returns:
            struct CreditPolicy.LoanTier
        """
        ...

    @overload
    def loanTiers(self, key0: uint256, key1: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#111)

        Args:
            key0: uint256
            key1: uint8
        Returns:
            struct CreditPolicy.LoanTier
        """
        ...

    @overload
    def loanTiers(self, key0: uint256, key1: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[CreditPolicy.LoanTier]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#111)

        Args:
            key0: uint256
            key1: uint8
        Returns:
            struct CreditPolicy.LoanTier
        """
        ...

    def loanTiers(self, key0: uint256, key1: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[CreditPolicy.LoanTier, TransactionAbc[CreditPolicy.LoanTier], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#111)

        Args:
            key0: uint256
            key1: uint8
        Returns:
            struct CreditPolicy.LoanTier
        """
        return self._execute(self.chain, request_type, "5bffd88f", [key0, key1], True if request_type == "tx" else False, CreditPolicy.LoanTier, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def totalTiers(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint8:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#112)

        Args:
            key0: uint256
        Returns:
            uint8
        """
        ...

    @overload
    def totalTiers(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#112)

        Args:
            key0: uint256
        Returns:
            uint8
        """
        ...

    @overload
    def totalTiers(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#112)

        Args:
            key0: uint256
        Returns:
            uint8
        """
        ...

    @overload
    def totalTiers(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint8]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#112)

        Args:
            key0: uint256
        Returns:
            uint8
        """
        ...

    def totalTiers(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint8, TransactionAbc[uint8], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#112)

        Args:
            key0: uint256
        Returns:
            uint8
        """
        return self._execute(self.chain, request_type, "fe26d965", [key0], True if request_type == "tx" else False, uint8, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tierExists(self, key0: uint256, key1: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#113)

        Args:
            key0: uint256
            key1: uint8
        Returns:
            bool
        """
        ...

    @overload
    def tierExists(self, key0: uint256, key1: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#113)

        Args:
            key0: uint256
            key1: uint8
        Returns:
            bool
        """
        ...

    @overload
    def tierExists(self, key0: uint256, key1: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#113)

        Args:
            key0: uint256
            key1: uint8
        Returns:
            bool
        """
        ...

    @overload
    def tierExists(self, key0: uint256, key1: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#113)

        Args:
            key0: uint256
            key1: uint8
        Returns:
            bool
        """
        ...

    def tierExists(self, key0: uint256, key1: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#113)

        Args:
            key0: uint256
            key1: uint8
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "8b624b10", [key0, key1], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def concentration(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> CreditPolicy.ConcentrationLimits:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#123)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.ConcentrationLimits
        """
        ...

    @overload
    def concentration(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#123)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.ConcentrationLimits
        """
        ...

    @overload
    def concentration(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#123)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.ConcentrationLimits
        """
        ...

    @overload
    def concentration(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[CreditPolicy.ConcentrationLimits]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#123)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.ConcentrationLimits
        """
        ...

    def concentration(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[CreditPolicy.ConcentrationLimits, TransactionAbc[CreditPolicy.ConcentrationLimits], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#123)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.ConcentrationLimits
        """
        return self._execute(self.chain, request_type, "d402ab27", [key0], True if request_type == "tx" else False, CreditPolicy.ConcentrationLimits, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def excludedIndustries(self, key0: uint256, key1: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#128)

        Args:
            key0: uint256
            key1: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def excludedIndustries(self, key0: uint256, key1: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#128)

        Args:
            key0: uint256
            key1: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def excludedIndustries(self, key0: uint256, key1: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#128)

        Args:
            key0: uint256
            key1: bytes32
        Returns:
            bool
        """
        ...

    @overload
    def excludedIndustries(self, key0: uint256, key1: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#128)

        Args:
            key0: uint256
            key1: bytes32
        Returns:
            bool
        """
        ...

    def excludedIndustries(self, key0: uint256, key1: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#128)

        Args:
            key0: uint256
            key1: bytes32
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "a75a0471", [key0, key1], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def attestation(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> CreditPolicy.AttestationRequirements:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#139)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.AttestationRequirements
        """
        ...

    @overload
    def attestation(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#139)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.AttestationRequirements
        """
        ...

    @overload
    def attestation(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#139)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.AttestationRequirements
        """
        ...

    @overload
    def attestation(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[CreditPolicy.AttestationRequirements]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#139)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.AttestationRequirements
        """
        ...

    def attestation(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[CreditPolicy.AttestationRequirements, TransactionAbc[CreditPolicy.AttestationRequirements], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#139)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.AttestationRequirements
        """
        return self._execute(self.chain, request_type, "6c2034ca", [key0], True if request_type == "tx" else False, CreditPolicy.AttestationRequirements, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def covenants(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> CreditPolicy.MaintenanceCovenants:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#152)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.MaintenanceCovenants
        """
        ...

    @overload
    def covenants(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#152)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.MaintenanceCovenants
        """
        ...

    @overload
    def covenants(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#152)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.MaintenanceCovenants
        """
        ...

    @overload
    def covenants(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[CreditPolicy.MaintenanceCovenants]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#152)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.MaintenanceCovenants
        """
        ...

    def covenants(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[CreditPolicy.MaintenanceCovenants, TransactionAbc[CreditPolicy.MaintenanceCovenants], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#152)

        Args:
            key0: uint256
        Returns:
            struct CreditPolicy.MaintenanceCovenants
        """
        return self._execute(self.chain, request_type, "28f4ca31", [key0], True if request_type == "tx" else False, CreditPolicy.MaintenanceCovenants, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def policyDocumentHash(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytes32:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#157)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        ...

    @overload
    def policyDocumentHash(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#157)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        ...

    @overload
    def policyDocumentHash(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#157)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        ...

    @overload
    def policyDocumentHash(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bytes32]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#157)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        ...

    def policyDocumentHash(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytes32, TransactionAbc[bytes32], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#157)

        Args:
            key0: uint256
        Returns:
            bytes32
        """
        return self._execute(self.chain, request_type, "3bf365b1", [key0], True if request_type == "tx" else False, bytes32, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def policyDocumentURI(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> str:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#158)

        Args:
            key0: uint256
        Returns:
            string
        """
        ...

    @overload
    def policyDocumentURI(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#158)

        Args:
            key0: uint256
        Returns:
            string
        """
        ...

    @overload
    def policyDocumentURI(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#158)

        Args:
            key0: uint256
        Returns:
            string
        """
        ...

    @overload
    def policyDocumentURI(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[str]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#158)

        Args:
            key0: uint256
        Returns:
            string
        """
        ...

    def policyDocumentURI(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[str, TransactionAbc[str], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#158)

        Args:
            key0: uint256
        Returns:
            string
        """
        return self._execute(self.chain, request_type, "6bda6106", [key0], True if request_type == "tx" else False, str, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def eligibilitySet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#160)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def eligibilitySet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#160)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def eligibilitySet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#160)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def eligibilitySet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#160)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    def eligibilitySet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#160)

        Args:
            key0: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "feca4699", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def ratiosSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#161)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def ratiosSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#161)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def ratiosSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#161)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def ratiosSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#161)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    def ratiosSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#161)

        Args:
            key0: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "b632d57c", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def concentrationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#162)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def concentrationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#162)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def concentrationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#162)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def concentrationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#162)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    def concentrationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#162)

        Args:
            key0: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "90ff8adf", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def attestationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#163)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def attestationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#163)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def attestationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#163)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def attestationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#163)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    def attestationSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#163)

        Args:
            key0: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "d9e5c35d", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def covenantsSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#164)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def covenantsSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#164)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def covenantsSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#164)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def covenantsSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#164)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    def covenantsSet(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#164)

        Args:
            key0: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "634a1cd4", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def hasAtLeastOneTier(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#165)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def hasAtLeastOneTier(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#165)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def hasAtLeastOneTier(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#165)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    @overload
    def hasAtLeastOneTier(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#165)

        Args:
            key0: uint256
        Returns:
            bool
        """
        ...

    def hasAtLeastOneTier(self, key0: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#165)

        Args:
            key0: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "6a58fc30", [key0], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def createPolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#211)

        Args:
            version: uint256
        """
        ...

    @overload
    def createPolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#211)

        Args:
            version: uint256
        """
        ...

    @overload
    def createPolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#211)

        Args:
            version: uint256
        """
        ...

    @overload
    def createPolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#211)

        Args:
            version: uint256
        """
        ...

    def createPolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#211)

        Args:
            version: uint256
        """
        return self._execute(self.chain, request_type, "04bd12bb", [version], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def freezePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#225)

        Args:
            version: uint256
        """
        ...

    @overload
    def freezePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#225)

        Args:
            version: uint256
        """
        ...

    @overload
    def freezePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#225)

        Args:
            version: uint256
        """
        ...

    @overload
    def freezePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#225)

        Args:
            version: uint256
        """
        ...

    def freezePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#225)

        Args:
            version: uint256
        """
        return self._execute(self.chain, request_type, "fb4dcb8b", [version], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def deActivatePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#253)

        Args:
            version: uint256
        """
        ...

    @overload
    def deActivatePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#253)

        Args:
            version: uint256
        """
        ...

    @overload
    def deActivatePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#253)

        Args:
            version: uint256
        """
        ...

    @overload
    def deActivatePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#253)

        Args:
            version: uint256
        """
        ...

    def deActivatePolicy(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#253)

        Args:
            version: uint256
        """
        return self._execute(self.chain, request_type, "0edea5b8", [version], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def updateEligibility(self, version: uint256, data: CreditPolicy.EligibilityCriteria, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#264)

        Args:
            version: uint256
            data: struct CreditPolicy.EligibilityCriteria
        """
        ...

    @overload
    def updateEligibility(self, version: uint256, data: CreditPolicy.EligibilityCriteria, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#264)

        Args:
            version: uint256
            data: struct CreditPolicy.EligibilityCriteria
        """
        ...

    @overload
    def updateEligibility(self, version: uint256, data: CreditPolicy.EligibilityCriteria, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#264)

        Args:
            version: uint256
            data: struct CreditPolicy.EligibilityCriteria
        """
        ...

    @overload
    def updateEligibility(self, version: uint256, data: CreditPolicy.EligibilityCriteria, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#264)

        Args:
            version: uint256
            data: struct CreditPolicy.EligibilityCriteria
        """
        ...

    def updateEligibility(self, version: uint256, data: CreditPolicy.EligibilityCriteria, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#264)

        Args:
            version: uint256
            data: struct CreditPolicy.EligibilityCriteria
        """
        return self._execute(self.chain, request_type, "77e4d4ad", [version, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def updateRatios(self, version: uint256, data: CreditPolicy.FinancialRatios, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#277)

        Args:
            version: uint256
            data: struct CreditPolicy.FinancialRatios
        """
        ...

    @overload
    def updateRatios(self, version: uint256, data: CreditPolicy.FinancialRatios, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#277)

        Args:
            version: uint256
            data: struct CreditPolicy.FinancialRatios
        """
        ...

    @overload
    def updateRatios(self, version: uint256, data: CreditPolicy.FinancialRatios, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#277)

        Args:
            version: uint256
            data: struct CreditPolicy.FinancialRatios
        """
        ...

    @overload
    def updateRatios(self, version: uint256, data: CreditPolicy.FinancialRatios, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#277)

        Args:
            version: uint256
            data: struct CreditPolicy.FinancialRatios
        """
        ...

    def updateRatios(self, version: uint256, data: CreditPolicy.FinancialRatios, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#277)

        Args:
            version: uint256
            data: struct CreditPolicy.FinancialRatios
        """
        return self._execute(self.chain, request_type, "a4d246fa", [version, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def updateConcentration(self, version: uint256, data: CreditPolicy.ConcentrationLimits, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#290)

        Args:
            version: uint256
            data: struct CreditPolicy.ConcentrationLimits
        """
        ...

    @overload
    def updateConcentration(self, version: uint256, data: CreditPolicy.ConcentrationLimits, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#290)

        Args:
            version: uint256
            data: struct CreditPolicy.ConcentrationLimits
        """
        ...

    @overload
    def updateConcentration(self, version: uint256, data: CreditPolicy.ConcentrationLimits, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#290)

        Args:
            version: uint256
            data: struct CreditPolicy.ConcentrationLimits
        """
        ...

    @overload
    def updateConcentration(self, version: uint256, data: CreditPolicy.ConcentrationLimits, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#290)

        Args:
            version: uint256
            data: struct CreditPolicy.ConcentrationLimits
        """
        ...

    def updateConcentration(self, version: uint256, data: CreditPolicy.ConcentrationLimits, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#290)

        Args:
            version: uint256
            data: struct CreditPolicy.ConcentrationLimits
        """
        return self._execute(self.chain, request_type, "69b65331", [version, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def updateAttestation(self, version: uint256, data: CreditPolicy.AttestationRequirements, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#303)

        Args:
            version: uint256
            data: struct CreditPolicy.AttestationRequirements
        """
        ...

    @overload
    def updateAttestation(self, version: uint256, data: CreditPolicy.AttestationRequirements, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#303)

        Args:
            version: uint256
            data: struct CreditPolicy.AttestationRequirements
        """
        ...

    @overload
    def updateAttestation(self, version: uint256, data: CreditPolicy.AttestationRequirements, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#303)

        Args:
            version: uint256
            data: struct CreditPolicy.AttestationRequirements
        """
        ...

    @overload
    def updateAttestation(self, version: uint256, data: CreditPolicy.AttestationRequirements, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#303)

        Args:
            version: uint256
            data: struct CreditPolicy.AttestationRequirements
        """
        ...

    def updateAttestation(self, version: uint256, data: CreditPolicy.AttestationRequirements, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#303)

        Args:
            version: uint256
            data: struct CreditPolicy.AttestationRequirements
        """
        return self._execute(self.chain, request_type, "6630b008", [version, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def updateCovenants(self, version: uint256, data: CreditPolicy.MaintenanceCovenants, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#316)

        Args:
            version: uint256
            data: struct CreditPolicy.MaintenanceCovenants
        """
        ...

    @overload
    def updateCovenants(self, version: uint256, data: CreditPolicy.MaintenanceCovenants, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#316)

        Args:
            version: uint256
            data: struct CreditPolicy.MaintenanceCovenants
        """
        ...

    @overload
    def updateCovenants(self, version: uint256, data: CreditPolicy.MaintenanceCovenants, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#316)

        Args:
            version: uint256
            data: struct CreditPolicy.MaintenanceCovenants
        """
        ...

    @overload
    def updateCovenants(self, version: uint256, data: CreditPolicy.MaintenanceCovenants, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#316)

        Args:
            version: uint256
            data: struct CreditPolicy.MaintenanceCovenants
        """
        ...

    def updateCovenants(self, version: uint256, data: CreditPolicy.MaintenanceCovenants, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#316)

        Args:
            version: uint256
            data: struct CreditPolicy.MaintenanceCovenants
        """
        return self._execute(self.chain, request_type, "6c11a386", [version, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setLoanTier(self, version: uint256, tierId: uint8, tier: CreditPolicy.LoanTier, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#329)

        Args:
            version: uint256
            tierId: uint8
            tier: struct CreditPolicy.LoanTier
        """
        ...

    @overload
    def setLoanTier(self, version: uint256, tierId: uint8, tier: CreditPolicy.LoanTier, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#329)

        Args:
            version: uint256
            tierId: uint8
            tier: struct CreditPolicy.LoanTier
        """
        ...

    @overload
    def setLoanTier(self, version: uint256, tierId: uint8, tier: CreditPolicy.LoanTier, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#329)

        Args:
            version: uint256
            tierId: uint8
            tier: struct CreditPolicy.LoanTier
        """
        ...

    @overload
    def setLoanTier(self, version: uint256, tierId: uint8, tier: CreditPolicy.LoanTier, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#329)

        Args:
            version: uint256
            tierId: uint8
            tier: struct CreditPolicy.LoanTier
        """
        ...

    def setLoanTier(self, version: uint256, tierId: uint8, tier: CreditPolicy.LoanTier, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#329)

        Args:
            version: uint256
            tierId: uint8
            tier: struct CreditPolicy.LoanTier
        """
        return self._execute(self.chain, request_type, "5b87ec2e", [version, tierId, tier], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def excludeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#350)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    @overload
    def excludeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#350)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    @overload
    def excludeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#350)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    @overload
    def excludeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#350)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    def excludeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#350)

        Args:
            version: uint256
            industry: bytes32
        """
        return self._execute(self.chain, request_type, "4cfa7af6", [version, industry], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def includeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#362)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    @overload
    def includeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#362)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    @overload
    def includeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#362)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    @overload
    def includeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#362)

        Args:
            version: uint256
            industry: bytes32
        """
        ...

    def includeIndustry(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#362)

        Args:
            version: uint256
            industry: bytes32
        """
        return self._execute(self.chain, request_type, "0c3529dc", [version, industry], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def setPolicyDocument(self, version: uint256, hash: bytes32, uri: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#377)

        Args:
            version: uint256
            hash: bytes32
            uri: string
        """
        ...

    @overload
    def setPolicyDocument(self, version: uint256, hash: bytes32, uri: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#377)

        Args:
            version: uint256
            hash: bytes32
            uri: string
        """
        ...

    @overload
    def setPolicyDocument(self, version: uint256, hash: bytes32, uri: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#377)

        Args:
            version: uint256
            hash: bytes32
            uri: string
        """
        ...

    @overload
    def setPolicyDocument(self, version: uint256, hash: bytes32, uri: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#377)

        Args:
            version: uint256
            hash: bytes32
            uri: string
        """
        ...

    def setPolicyDocument(self, version: uint256, hash: bytes32, uri: str, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#377)

        Args:
            version: uint256
            hash: bytes32
            uri: string
        """
        return self._execute(self.chain, request_type, "3927a4c3", [version, hash, uri], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def changePolicyAdmin(self, newAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#389)

        Args:
            newAdmin: address
        """
        ...

    @overload
    def changePolicyAdmin(self, newAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#389)

        Args:
            newAdmin: address
        """
        ...

    @overload
    def changePolicyAdmin(self, newAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#389)

        Args:
            newAdmin: address
        """
        ...

    @overload
    def changePolicyAdmin(self, newAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#389)

        Args:
            newAdmin: address
        """
        ...

    def changePolicyAdmin(self, newAdmin: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#389)

        Args:
            newAdmin: address
        """
        return self._execute(self.chain, request_type, "f770713b", [newAdmin], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def isPolicyActive(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#400)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    @overload
    def isPolicyActive(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#400)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    @overload
    def isPolicyActive(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#400)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    @overload
    def isPolicyActive(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#400)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    def isPolicyActive(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#400)

        Args:
            version: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "bd8afa46", [version], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def isPolicyFrozen(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#404)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    @overload
    def isPolicyFrozen(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#404)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    @overload
    def isPolicyFrozen(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#404)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    @overload
    def isPolicyFrozen(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[bool]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#404)

        Args:
            version: uint256
        Returns:
            bool
        """
        ...

    def isPolicyFrozen(self, version: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#404)

        Args:
            version: uint256
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "4c2d62b7", [version], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def tierExistsInPolicy(self, version: uint256, tierId: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#408)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#408)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#408)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#408)

        Args:
            version: uint256
            tierId: uint8
        Returns:
            bool
        """
        ...

    def tierExistsInPolicy(self, version: uint256, tierId: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#408)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#415)

        Args:
            _maxTiers: uint8
        """
        ...

    @overload
    def setMaxTiers(self, _maxTiers: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#415)

        Args:
            _maxTiers: uint8
        """
        ...

    @overload
    def setMaxTiers(self, _maxTiers: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#415)

        Args:
            _maxTiers: uint8
        """
        ...

    @overload
    def setMaxTiers(self, _maxTiers: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#415)

        Args:
            _maxTiers: uint8
        """
        ...

    def setMaxTiers(self, _maxTiers: uint8, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#415)

        Args:
            _maxTiers: uint8
        """
        return self._execute(self.chain, request_type, "a3a1da7b", [_maxTiers], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getMaxTiers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint8:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#423)

        Returns:
            uint8
        """
        ...

    @overload
    def getMaxTiers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#423)

        Returns:
            uint8
        """
        ...

    @overload
    def getMaxTiers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#423)

        Returns:
            uint8
        """
        ...

    @overload
    def getMaxTiers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint8]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#423)

        Returns:
            uint8
        """
        ...

    def getMaxTiers(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint8, TransactionAbc[uint8], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#423)

        Returns:
            uint8
        """
        return self._execute(self.chain, request_type, "4d4f7177", [], True if request_type == "tx" else False, uint8, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def isIndustryExcluded(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bool:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#427)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#427)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#427)

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
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#427)

        Args:
            version: uint256
            industry: bytes32
        Returns:
            bool
        """
        ...

    def isIndustryExcluded(self, version: uint256, industry: bytes32, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bool, TransactionAbc[bool], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/admin/Desktop/credit_rail/contracts/src/CreditPolicy.sol#427)

        Args:
            version: uint256
            industry: bytes32
        Returns:
            bool
        """
        return self._execute(self.chain, request_type, "fa4f5a86", [version, industry], True if request_type == "tx" else False, bool, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

CreditPolicy.policyAdmin.selector = bytes4(b'X\xe5\x18\x96')
CreditPolicy.policyCreated.selector = bytes4(b'J\xe8\xd2\x1a')
CreditPolicy.policyFrozen.selector = bytes4(b'P7\xf1{')
CreditPolicy.policyActive.selector = bytes4(b'J\tm+')
CreditPolicy.lastUpdated.selector = bytes4(b'$\xa2\x95"')
CreditPolicy.eligibility.selector = bytes4(b'z\x86\x1a\xdb')
CreditPolicy.ratios.selector = bytes4(b'w\x1d\xc8j')
CreditPolicy.loanTiers.selector = bytes4(b'[\xff\xd8\x8f')
CreditPolicy.totalTiers.selector = bytes4(b'\xfe&\xd9e')
CreditPolicy.tierExists.selector = bytes4(b'\x8bbK\x10')
CreditPolicy.concentration.selector = bytes4(b"\xd4\x02\xab'")
CreditPolicy.excludedIndustries.selector = bytes4(b'\xa7Z\x04q')
CreditPolicy.attestation.selector = bytes4(b'l 4\xca')
CreditPolicy.covenants.selector = bytes4(b'(\xf4\xca1')
CreditPolicy.policyDocumentHash.selector = bytes4(b';\xf3e\xb1')
CreditPolicy.policyDocumentURI.selector = bytes4(b'k\xdaa\x06')
CreditPolicy.eligibilitySet.selector = bytes4(b'\xfe\xcaF\x99')
CreditPolicy.ratiosSet.selector = bytes4(b'\xb62\xd5|')
CreditPolicy.concentrationSet.selector = bytes4(b'\x90\xff\x8a\xdf')
CreditPolicy.attestationSet.selector = bytes4(b'\xd9\xe5\xc3]')
CreditPolicy.covenantsSet.selector = bytes4(b'cJ\x1c\xd4')
CreditPolicy.hasAtLeastOneTier.selector = bytes4(b'jX\xfc0')
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
CreditPolicy.changePolicyAdmin.selector = bytes4(b'\xf7pq;')
CreditPolicy.isPolicyActive.selector = bytes4(b'\xbd\x8a\xfaF')
CreditPolicy.isPolicyFrozen.selector = bytes4(b'L-b\xb7')
CreditPolicy.tierExistsInPolicy.selector = bytes4(b'Ie\x9c\xdc')
CreditPolicy.setMaxTiers.selector = bytes4(b'\xa3\xa1\xda{')
CreditPolicy.getMaxTiers.selector = bytes4(b'MOqw')
CreditPolicy.isIndustryExcluded.selector = bytes4(b'\xfaOZ\x86')
