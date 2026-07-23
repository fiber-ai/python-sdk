from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReversePhoneLookupBody")


@_attrs_define
class ReversePhoneLookupBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        phone_number (str): The phone number to look up. Accepts E.164 format (+12125551234) or various national
            formats.
    """

    api_key: str
    phone_number: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        phone_number = self.phone_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "phoneNumber": phone_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        phone_number = d.pop("phoneNumber")

        reverse_phone_lookup_body = cls(
            api_key=api_key,
            phone_number=phone_number,
        )

        reverse_phone_lookup_body.additional_properties = d
        return reverse_phone_lookup_body

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
