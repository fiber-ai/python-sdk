from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="DomainLookupPollingResponse200OutputDataItem")



@_attrs_define
class DomainLookupPollingResponse200OutputDataItem:
    """ 
        Attributes:
            company_name (str): The name of the company
            all_domains (list[str]): All the found domains of the company
            rationale (str): The reasoning why the agent chose the given company
            best_domain (Union[None, Unset, str]): The best matching domain of the company. Null if we couldn't find the
                domain
            confidence (Union[None, Unset, int]): The confidence score between 0 and 10 denoting the match quality. Higher
                confidence score means the company has more matching parameters.
     """

    company_name: str
    all_domains: list[str]
    rationale: str
    best_domain: Union[None, Unset, str] = UNSET
    confidence: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        company_name = self.company_name

        all_domains = self.all_domains



        rationale = self.rationale

        best_domain: Union[None, Unset, str]
        if isinstance(self.best_domain, Unset):
            best_domain = UNSET
        else:
            best_domain = self.best_domain

        confidence: Union[None, Unset, int]
        if isinstance(self.confidence, Unset):
            confidence = UNSET
        else:
            confidence = self.confidence


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "companyName": company_name,
            "allDomains": all_domains,
            "rationale": rationale,
        })
        if best_domain is not UNSET:
            field_dict["bestDomain"] = best_domain
        if confidence is not UNSET:
            field_dict["confidence"] = confidence

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_name = d.pop("companyName")

        all_domains = cast(list[str], d.pop("allDomains"))


        rationale = d.pop("rationale")

        def _parse_best_domain(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        best_domain = _parse_best_domain(d.pop("bestDomain", UNSET))


        def _parse_confidence(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        confidence = _parse_confidence(d.pop("confidence", UNSET))


        domain_lookup_polling_response_200_output_data_item = cls(
            company_name=company_name,
            all_domains=all_domains,
            rationale=rationale,
            best_domain=best_domain,
            confidence=confidence,
        )


        domain_lookup_polling_response_200_output_data_item.additional_properties = d
        return domain_lookup_polling_response_200_output_data_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
