from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_lookup_polling_response_200_output_data_item_email_domains_type_0_item import (
        DomainLookupPollingResponse200OutputDataItemEmailDomainsType0Item,
    )


T = TypeVar("T", bound="DomainLookupPollingResponse200OutputDataItem")


@_attrs_define
class DomainLookupPollingResponse200OutputDataItem:
    """
    Attributes:
        company_name (str): The name of the company
        rationale (str): The reasoning why the agent chose the given company
        best_domain (None | str | Unset): The best matching domain of the company. Null if we couldn't find the domain
        email_domains (list[DomainLookupPollingResponse200OutputDataItemEmailDomainsType0Item] | None | Unset): The
            email domains of the company
        all_domains (list[str] | None | Unset): All the found domains of the company
        confidence (int | None | Unset): The confidence score between 0 and 10 denoting the match quality. Higher
            confidence score means the company has more matching parameters.
    """

    company_name: str
    rationale: str
    best_domain: None | str | Unset = UNSET
    email_domains: list[DomainLookupPollingResponse200OutputDataItemEmailDomainsType0Item] | None | Unset = UNSET
    all_domains: list[str] | None | Unset = UNSET
    confidence: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_name = self.company_name

        rationale = self.rationale

        best_domain: None | str | Unset
        if isinstance(self.best_domain, Unset):
            best_domain = UNSET
        else:
            best_domain = self.best_domain

        email_domains: list[dict[str, Any]] | None | Unset
        if isinstance(self.email_domains, Unset):
            email_domains = UNSET
        elif isinstance(self.email_domains, list):
            email_domains = []
            for email_domains_type_0_item_data in self.email_domains:
                email_domains_type_0_item = email_domains_type_0_item_data.to_dict()
                email_domains.append(email_domains_type_0_item)

        else:
            email_domains = self.email_domains

        all_domains: list[str] | None | Unset
        if isinstance(self.all_domains, Unset):
            all_domains = UNSET
        elif isinstance(self.all_domains, list):
            all_domains = self.all_domains

        else:
            all_domains = self.all_domains

        confidence: int | None | Unset
        if isinstance(self.confidence, Unset):
            confidence = UNSET
        else:
            confidence = self.confidence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyName": company_name,
                "rationale": rationale,
            }
        )
        if best_domain is not UNSET:
            field_dict["bestDomain"] = best_domain
        if email_domains is not UNSET:
            field_dict["emailDomains"] = email_domains
        if all_domains is not UNSET:
            field_dict["allDomains"] = all_domains
        if confidence is not UNSET:
            field_dict["confidence"] = confidence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domain_lookup_polling_response_200_output_data_item_email_domains_type_0_item import (
            DomainLookupPollingResponse200OutputDataItemEmailDomainsType0Item,
        )

        d = dict(src_dict)
        company_name = d.pop("companyName")

        rationale = d.pop("rationale")

        def _parse_best_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        best_domain = _parse_best_domain(d.pop("bestDomain", UNSET))

        def _parse_email_domains(
            data: object,
        ) -> list[DomainLookupPollingResponse200OutputDataItemEmailDomainsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                email_domains_type_0 = []
                _email_domains_type_0 = data
                for email_domains_type_0_item_data in _email_domains_type_0:
                    email_domains_type_0_item = (
                        DomainLookupPollingResponse200OutputDataItemEmailDomainsType0Item.from_dict(
                            email_domains_type_0_item_data
                        )
                    )

                    email_domains_type_0.append(email_domains_type_0_item)

                return email_domains_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DomainLookupPollingResponse200OutputDataItemEmailDomainsType0Item] | None | Unset, data)

        email_domains = _parse_email_domains(d.pop("emailDomains", UNSET))

        def _parse_all_domains(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                all_domains_type_0 = cast(list[str], data)

                return all_domains_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        all_domains = _parse_all_domains(d.pop("allDomains", UNSET))

        def _parse_confidence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        confidence = _parse_confidence(d.pop("confidence", UNSET))

        domain_lookup_polling_response_200_output_data_item = cls(
            company_name=company_name,
            rationale=rationale,
            best_domain=best_domain,
            email_domains=email_domains,
            all_domains=all_domains,
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
