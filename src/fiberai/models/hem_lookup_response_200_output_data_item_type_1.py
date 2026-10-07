from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hem_lookup_response_200_output_data_item_type_1_status import (
    HemLookupResponse200OutputDataItemType1Status,
)

T = TypeVar("T", bound="HemLookupResponse200OutputDataItemType1")


@_attrs_define
class HemLookupResponse200OutputDataItemType1:
    """
    Attributes:
        status (HemLookupResponse200OutputDataItemType1Status): `not_found` — the hash was not found in our contact
            database. `rejected` — the input was not a usable hash at all.
        hashed_email (str): The input exactly as you supplied it, for correlation.
        message (str): Human-readable explanation. Neither status is billed.
    """

    status: HemLookupResponse200OutputDataItemType1Status
    hashed_email: str
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        hashed_email = self.hashed_email

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "hashedEmail": hashed_email,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = HemLookupResponse200OutputDataItemType1Status(d.pop("status"))

        hashed_email = d.pop("hashedEmail")

        message = d.pop("message")

        hem_lookup_response_200_output_data_item_type_1 = cls(
            status=status,
            hashed_email=hashed_email,
            message=message,
        )

        hem_lookup_response_200_output_data_item_type_1.additional_properties = d
        return hem_lookup_response_200_output_data_item_type_1

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
