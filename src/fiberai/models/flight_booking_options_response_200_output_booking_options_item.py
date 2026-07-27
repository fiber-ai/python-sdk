from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flight_booking_options_response_200_output_booking_options_item_booking_link_type_0 import (
        FlightBookingOptionsResponse200OutputBookingOptionsItemBookingLinkType0,
    )


T = TypeVar("T", bound="FlightBookingOptionsResponse200OutputBookingOptionsItem")


@_attrs_define
class FlightBookingOptionsResponse200OutputBookingOptionsItem:
    """
    Attributes:
        provider_name (str): Name of the airline or booking site selling this ticket (e.g. 'United', 'American').
        airline_logo_urls (list[str]): Logos for the airline(s) or booking site(s) on this option. Multiple entries
            indicate a split booking across providers.
        flight_numbers (list[str]): Flight numbers covered by this option (e.g. 'UA 2175').
        fare_conditions (list[str]): Amenities and fare rules included or excluded (e.g. seat selection policy, change
            rules).
        baggage_details (list[str]): Baggage allowances and fees as display strings (e.g. '1st checked bag: 75', '1 free
            carry-on').
        price (int | None | Unset): Total price in whole currency units.
        fare_type (None | str | Unset): Fare class label (e.g. 'Basic Economy', 'Business').
        is_split_booking (bool | None | Unset): True when this option consists of separately-issued tickets across
            different providers (e.g. booking two separate one-way tickets on different airlines rather than a single
            connection). Split bookings carry higher disruption risk.
        booking_link (FlightBookingOptionsResponse200OutputBookingOptionsItemBookingLinkType0 | None | Unset): Link to
            book this option. When present, both `url` and optionally `postData` are available.
        booking_phone (None | str | Unset): Phone number to book through this provider, in E.164 format (e.g.
            '+18005551212').
        estimated_phone_service_fee (int | None | Unset): Estimated phone booking service fee in whole currency units,
            when phone booking is offered.
    """

    provider_name: str
    airline_logo_urls: list[str]
    flight_numbers: list[str]
    fare_conditions: list[str]
    baggage_details: list[str]
    price: int | None | Unset = UNSET
    fare_type: None | str | Unset = UNSET
    is_split_booking: bool | None | Unset = UNSET
    booking_link: FlightBookingOptionsResponse200OutputBookingOptionsItemBookingLinkType0 | None | Unset = UNSET
    booking_phone: None | str | Unset = UNSET
    estimated_phone_service_fee: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.flight_booking_options_response_200_output_booking_options_item_booking_link_type_0 import (
            FlightBookingOptionsResponse200OutputBookingOptionsItemBookingLinkType0,
        )

        provider_name = self.provider_name

        airline_logo_urls = self.airline_logo_urls

        flight_numbers = self.flight_numbers

        fare_conditions = self.fare_conditions

        baggage_details = self.baggage_details

        price: int | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        fare_type: None | str | Unset
        if isinstance(self.fare_type, Unset):
            fare_type = UNSET
        else:
            fare_type = self.fare_type

        is_split_booking: bool | None | Unset
        if isinstance(self.is_split_booking, Unset):
            is_split_booking = UNSET
        else:
            is_split_booking = self.is_split_booking

        booking_link: dict[str, Any] | None | Unset
        if isinstance(self.booking_link, Unset):
            booking_link = UNSET
        elif isinstance(self.booking_link, FlightBookingOptionsResponse200OutputBookingOptionsItemBookingLinkType0):
            booking_link = self.booking_link.to_dict()
        else:
            booking_link = self.booking_link

        booking_phone: None | str | Unset
        if isinstance(self.booking_phone, Unset):
            booking_phone = UNSET
        else:
            booking_phone = self.booking_phone

        estimated_phone_service_fee: int | None | Unset
        if isinstance(self.estimated_phone_service_fee, Unset):
            estimated_phone_service_fee = UNSET
        else:
            estimated_phone_service_fee = self.estimated_phone_service_fee

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providerName": provider_name,
                "airlineLogoUrls": airline_logo_urls,
                "flightNumbers": flight_numbers,
                "fareConditions": fare_conditions,
                "baggageDetails": baggage_details,
            }
        )
        if price is not UNSET:
            field_dict["price"] = price
        if fare_type is not UNSET:
            field_dict["fareType"] = fare_type
        if is_split_booking is not UNSET:
            field_dict["isSplitBooking"] = is_split_booking
        if booking_link is not UNSET:
            field_dict["bookingLink"] = booking_link
        if booking_phone is not UNSET:
            field_dict["bookingPhone"] = booking_phone
        if estimated_phone_service_fee is not UNSET:
            field_dict["estimatedPhoneServiceFee"] = estimated_phone_service_fee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flight_booking_options_response_200_output_booking_options_item_booking_link_type_0 import (
            FlightBookingOptionsResponse200OutputBookingOptionsItemBookingLinkType0,
        )

        d = dict(src_dict)
        provider_name = d.pop("providerName")

        airline_logo_urls = cast(list[str], d.pop("airlineLogoUrls"))

        flight_numbers = cast(list[str], d.pop("flightNumbers"))

        fare_conditions = cast(list[str], d.pop("fareConditions"))

        baggage_details = cast(list[str], d.pop("baggageDetails"))

        def _parse_price(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_fare_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fare_type = _parse_fare_type(d.pop("fareType", UNSET))

        def _parse_is_split_booking(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_split_booking = _parse_is_split_booking(d.pop("isSplitBooking", UNSET))

        def _parse_booking_link(
            data: object,
        ) -> FlightBookingOptionsResponse200OutputBookingOptionsItemBookingLinkType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                booking_link_type_0 = FlightBookingOptionsResponse200OutputBookingOptionsItemBookingLinkType0.from_dict(
                    data
                )

                return booking_link_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FlightBookingOptionsResponse200OutputBookingOptionsItemBookingLinkType0 | None | Unset, data)

        booking_link = _parse_booking_link(d.pop("bookingLink", UNSET))

        def _parse_booking_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        booking_phone = _parse_booking_phone(d.pop("bookingPhone", UNSET))

        def _parse_estimated_phone_service_fee(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        estimated_phone_service_fee = _parse_estimated_phone_service_fee(d.pop("estimatedPhoneServiceFee", UNSET))

        flight_booking_options_response_200_output_booking_options_item = cls(
            provider_name=provider_name,
            airline_logo_urls=airline_logo_urls,
            flight_numbers=flight_numbers,
            fare_conditions=fare_conditions,
            baggage_details=baggage_details,
            price=price,
            fare_type=fare_type,
            is_split_booking=is_split_booking,
            booking_link=booking_link,
            booking_phone=booking_phone,
            estimated_phone_service_fee=estimated_phone_service_fee,
        )

        flight_booking_options_response_200_output_booking_options_item.additional_properties = d
        return flight_booking_options_response_200_output_booking_options_item

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
