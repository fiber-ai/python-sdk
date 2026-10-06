from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BookingPropertyBody")


@_attrs_define
class BookingPropertyBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        property_url (str): Full Booking.com property URL (e.g. 'https://www.booking.com/hotel/hr/sumratin-
            dubrovnik.html'). Obtain it from a result returned by POST /v1/booking/search — pass the `propertyUrl`, not the
            `propertyId`.
        language_code (None | str | Unset): Language for property names, descriptions, and labels. Pass a BCP-47
            language tag such as 'en', 'en-US', 'fr', 'de', or 'es'. Omit for English.
    """

    api_key: str
    property_url: str
    language_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        property_url = self.property_url

        language_code: None | str | Unset
        if isinstance(self.language_code, Unset):
            language_code = UNSET
        else:
            language_code = self.language_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "propertyUrl": property_url,
            }
        )
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        property_url = d.pop("propertyUrl")

        def _parse_language_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language_code = _parse_language_code(d.pop("languageCode", UNSET))

        booking_property_body = cls(
            api_key=api_key,
            property_url=property_url,
            language_code=language_code,
        )

        booking_property_body.additional_properties = d
        return booking_property_body

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
