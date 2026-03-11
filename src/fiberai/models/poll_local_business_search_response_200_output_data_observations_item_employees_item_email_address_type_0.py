from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemEmailAddressType0")


@_attrs_define
class PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemEmailAddressType0:
    """
    Attributes:
        email_address (str):
        domain (str):
    """

    email_address: str
    domain: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_address = self.email_address

        domain = self.domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emailAddress": email_address,
                "domain": domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email_address = d.pop("emailAddress")

        domain = d.pop("domain")

        poll_local_business_search_response_200_output_data_observations_item_employees_item_email_address_type_0 = cls(
            email_address=email_address,
            domain=domain,
        )

        poll_local_business_search_response_200_output_data_observations_item_employees_item_email_address_type_0.additional_properties = d
        return poll_local_business_search_response_200_output_data_observations_item_employees_item_email_address_type_0

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
