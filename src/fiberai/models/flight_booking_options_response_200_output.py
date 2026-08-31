from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flight_booking_options_response_200_output_booking_options_item import (
        FlightBookingOptionsResponse200OutputBookingOptionsItem,
    )


T = TypeVar("T", bound="FlightBookingOptionsResponse200Output")


@_attrs_define
class FlightBookingOptionsResponse200Output:
    """
    Attributes:
        booking_options (list[FlightBookingOptionsResponse200OutputBookingOptionsItem]): Purchasing options for the
            selected itinerary, each representing a specific provider × fare type combination (e.g. United Economy). Ordered
            best first. Empty when the itinerary is no longer bookable.
        currency_code (None | str | Unset): ISO 4217 currency code for prices in this response (e.g. 'USD', 'EUR',
            'GBP').
    """

    booking_options: list[FlightBookingOptionsResponse200OutputBookingOptionsItem]
    currency_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        booking_options = []
        for booking_options_item_data in self.booking_options:
            booking_options_item = booking_options_item_data.to_dict()
            booking_options.append(booking_options_item)

        currency_code: None | str | Unset
        if isinstance(self.currency_code, Unset):
            currency_code = UNSET
        else:
            currency_code = self.currency_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bookingOptions": booking_options,
            }
        )
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flight_booking_options_response_200_output_booking_options_item import (
            FlightBookingOptionsResponse200OutputBookingOptionsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        booking_options = []
        _booking_options = d.pop("bookingOptions")
        for booking_options_item_data in _booking_options:
            booking_options_item = FlightBookingOptionsResponse200OutputBookingOptionsItem.from_dict(
                booking_options_item_data
            )

            booking_options.append(booking_options_item)

        def _parse_currency_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_code = _parse_currency_code(d.pop("currencyCode", UNSET))

        flight_booking_options_response_200_output = cls(
            booking_options=booking_options,
            currency_code=currency_code,
        )

        flight_booking_options_response_200_output.additional_properties = d
        return flight_booking_options_response_200_output

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
