from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlightBookingOptionsResponse200OutputBookingOptionsItemBookingLinkType0")


@_attrs_define
class FlightBookingOptionsResponse200OutputBookingOptionsItemBookingLinkType0:
    """Link to book this option. When present, both `url` and optionally `postData` are available.

    Attributes:
        url (str): URL to begin booking this option.
        post_data (None | str | Unset): Form-encoded body to POST to `url` to start the booking flow, when a POST
            request is required.
    """

    url: str
    post_data: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        post_data: None | str | Unset
        if isinstance(self.post_data, Unset):
            post_data = UNSET
        else:
            post_data = self.post_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if post_data is not UNSET:
            field_dict["postData"] = post_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        def _parse_post_data(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_data = _parse_post_data(d.pop("postData", UNSET))

        flight_booking_options_response_200_output_booking_options_item_booking_link_type_0 = cls(
            url=url,
            post_data=post_data,
        )

        flight_booking_options_response_200_output_booking_options_item_booking_link_type_0.additional_properties = d
        return flight_booking_options_response_200_output_booking_options_item_booking_link_type_0

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
