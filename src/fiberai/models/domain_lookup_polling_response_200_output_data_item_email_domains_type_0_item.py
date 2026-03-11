from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainLookupPollingResponse200OutputDataItemEmailDomainsType0Item")


@_attrs_define
class DomainLookupPollingResponse200OutputDataItemEmailDomainsType0Item:
    """
    Attributes:
        email_domain (None | str | Unset): The email domain found for the company, non personal email domains only
        confidence (float | None | Unset): The confidence of the email domain found, 1-10, 10 is most confident
        rationale (None | str | Unset): The rationale for the email domain found
    """

    email_domain: None | str | Unset = UNSET
    confidence: float | None | Unset = UNSET
    rationale: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_domain: None | str | Unset
        if isinstance(self.email_domain, Unset):
            email_domain = UNSET
        else:
            email_domain = self.email_domain

        confidence: float | None | Unset
        if isinstance(self.confidence, Unset):
            confidence = UNSET
        else:
            confidence = self.confidence

        rationale: None | str | Unset
        if isinstance(self.rationale, Unset):
            rationale = UNSET
        else:
            rationale = self.rationale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email_domain is not UNSET:
            field_dict["emailDomain"] = email_domain
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if rationale is not UNSET:
            field_dict["rationale"] = rationale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_email_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_domain = _parse_email_domain(d.pop("emailDomain", UNSET))

        def _parse_confidence(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        confidence = _parse_confidence(d.pop("confidence", UNSET))

        def _parse_rationale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rationale = _parse_rationale(d.pop("rationale", UNSET))

        domain_lookup_polling_response_200_output_data_item_email_domains_type_0_item = cls(
            email_domain=email_domain,
            confidence=confidence,
            rationale=rationale,
        )

        domain_lookup_polling_response_200_output_data_item_email_domains_type_0_item.additional_properties = d
        return domain_lookup_polling_response_200_output_data_item_email_domains_type_0_item

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
