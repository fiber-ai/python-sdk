from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PollLocalBusinessSearchResponse200OutputDataObservationsItemBusinessEmailsItem")


@_attrs_define
class PollLocalBusinessSearchResponse200OutputDataObservationsItemBusinessEmailsItem:
    """
    Attributes:
        email_address (str):
        domain (None | str | Unset):
    """

    email_address: str
    domain: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_address = self.email_address

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emailAddress": email_address,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email_address = d.pop("emailAddress")

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        poll_local_business_search_response_200_output_data_observations_item_business_emails_item = cls(
            email_address=email_address,
            domain=domain,
        )

        poll_local_business_search_response_200_output_data_observations_item_business_emails_item.additional_properties = d
        return poll_local_business_search_response_200_output_data_observations_item_business_emails_item

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
