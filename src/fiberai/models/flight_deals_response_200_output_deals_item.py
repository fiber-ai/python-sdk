from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flight_deals_response_200_output_deals_item_destination import (
        FlightDealsResponse200OutputDealsItemDestination,
    )


T = TypeVar("T", bound="FlightDealsResponse200OutputDealsItem")


@_attrs_define
class FlightDealsResponse200OutputDealsItem:
    """
    Attributes:
        destination (FlightDealsResponse200OutputDealsItemDestination):
        price (int): Deal price in whole currency units.
        departure_iata_code (None | str | Unset): IATA code of the airport this deal departs from. When
            `departureAirports` covers a metro, this is the specific airport the deal uses.
        outbound_date (None | str | Unset): Outbound date of the cheapest itinerary (YYYY-MM-DD).
        return_date (None | str | Unset): Return date of the cheapest itinerary (YYYY-MM-DD).
        trip_length_days (int | None | Unset): Length of the trip in whole days.
        typical_price (int | None | Unset): Typical price for a similar trip in whole currency units.
        savings_amount (int | None | Unset): Amount cheaper than the typical price, in whole currency units.
        savings_percentage (int | None | Unset): Percent cheaper than the typical price, from 0 to 100.
        stop_count (int | None | Unset): Number of stops on the outbound itinerary.
        duration_minutes (int | None | Unset): Total outbound flight duration in minutes.
        airline_name (None | str | Unset): Airline operating the itinerary. Null when the itinerary has no single
            operating airline.
        airline_code (None | str | Unset): IATA airline designator (e.g. 'UA').
        booking_url (None | str | Unset): URL to view and book this itinerary.
    """

    destination: FlightDealsResponse200OutputDealsItemDestination
    price: int
    departure_iata_code: None | str | Unset = UNSET
    outbound_date: None | str | Unset = UNSET
    return_date: None | str | Unset = UNSET
    trip_length_days: int | None | Unset = UNSET
    typical_price: int | None | Unset = UNSET
    savings_amount: int | None | Unset = UNSET
    savings_percentage: int | None | Unset = UNSET
    stop_count: int | None | Unset = UNSET
    duration_minutes: int | None | Unset = UNSET
    airline_name: None | str | Unset = UNSET
    airline_code: None | str | Unset = UNSET
    booking_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination = self.destination.to_dict()

        price = self.price

        departure_iata_code: None | str | Unset
        if isinstance(self.departure_iata_code, Unset):
            departure_iata_code = UNSET
        else:
            departure_iata_code = self.departure_iata_code

        outbound_date: None | str | Unset
        if isinstance(self.outbound_date, Unset):
            outbound_date = UNSET
        else:
            outbound_date = self.outbound_date

        return_date: None | str | Unset
        if isinstance(self.return_date, Unset):
            return_date = UNSET
        else:
            return_date = self.return_date

        trip_length_days: int | None | Unset
        if isinstance(self.trip_length_days, Unset):
            trip_length_days = UNSET
        else:
            trip_length_days = self.trip_length_days

        typical_price: int | None | Unset
        if isinstance(self.typical_price, Unset):
            typical_price = UNSET
        else:
            typical_price = self.typical_price

        savings_amount: int | None | Unset
        if isinstance(self.savings_amount, Unset):
            savings_amount = UNSET
        else:
            savings_amount = self.savings_amount

        savings_percentage: int | None | Unset
        if isinstance(self.savings_percentage, Unset):
            savings_percentage = UNSET
        else:
            savings_percentage = self.savings_percentage

        stop_count: int | None | Unset
        if isinstance(self.stop_count, Unset):
            stop_count = UNSET
        else:
            stop_count = self.stop_count

        duration_minutes: int | None | Unset
        if isinstance(self.duration_minutes, Unset):
            duration_minutes = UNSET
        else:
            duration_minutes = self.duration_minutes

        airline_name: None | str | Unset
        if isinstance(self.airline_name, Unset):
            airline_name = UNSET
        else:
            airline_name = self.airline_name

        airline_code: None | str | Unset
        if isinstance(self.airline_code, Unset):
            airline_code = UNSET
        else:
            airline_code = self.airline_code

        booking_url: None | str | Unset
        if isinstance(self.booking_url, Unset):
            booking_url = UNSET
        else:
            booking_url = self.booking_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destination": destination,
                "price": price,
            }
        )
        if departure_iata_code is not UNSET:
            field_dict["departureIataCode"] = departure_iata_code
        if outbound_date is not UNSET:
            field_dict["outboundDate"] = outbound_date
        if return_date is not UNSET:
            field_dict["returnDate"] = return_date
        if trip_length_days is not UNSET:
            field_dict["tripLengthDays"] = trip_length_days
        if typical_price is not UNSET:
            field_dict["typicalPrice"] = typical_price
        if savings_amount is not UNSET:
            field_dict["savingsAmount"] = savings_amount
        if savings_percentage is not UNSET:
            field_dict["savingsPercentage"] = savings_percentage
        if stop_count is not UNSET:
            field_dict["stopCount"] = stop_count
        if duration_minutes is not UNSET:
            field_dict["durationMinutes"] = duration_minutes
        if airline_name is not UNSET:
            field_dict["airlineName"] = airline_name
        if airline_code is not UNSET:
            field_dict["airlineCode"] = airline_code
        if booking_url is not UNSET:
            field_dict["bookingUrl"] = booking_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flight_deals_response_200_output_deals_item_destination import (
            FlightDealsResponse200OutputDealsItemDestination,  # noqa: PLC0415
        )

        d = dict(src_dict)
        destination = FlightDealsResponse200OutputDealsItemDestination.from_dict(d.pop("destination"))

        price = d.pop("price")

        def _parse_departure_iata_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        departure_iata_code = _parse_departure_iata_code(d.pop("departureIataCode", UNSET))

        def _parse_outbound_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outbound_date = _parse_outbound_date(d.pop("outboundDate", UNSET))

        def _parse_return_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        return_date = _parse_return_date(d.pop("returnDate", UNSET))

        def _parse_trip_length_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        trip_length_days = _parse_trip_length_days(d.pop("tripLengthDays", UNSET))

        def _parse_typical_price(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        typical_price = _parse_typical_price(d.pop("typicalPrice", UNSET))

        def _parse_savings_amount(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        savings_amount = _parse_savings_amount(d.pop("savingsAmount", UNSET))

        def _parse_savings_percentage(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        savings_percentage = _parse_savings_percentage(d.pop("savingsPercentage", UNSET))

        def _parse_stop_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        stop_count = _parse_stop_count(d.pop("stopCount", UNSET))

        def _parse_duration_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_minutes = _parse_duration_minutes(d.pop("durationMinutes", UNSET))

        def _parse_airline_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        airline_name = _parse_airline_name(d.pop("airlineName", UNSET))

        def _parse_airline_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        airline_code = _parse_airline_code(d.pop("airlineCode", UNSET))

        def _parse_booking_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        booking_url = _parse_booking_url(d.pop("bookingUrl", UNSET))

        flight_deals_response_200_output_deals_item = cls(
            destination=destination,
            price=price,
            departure_iata_code=departure_iata_code,
            outbound_date=outbound_date,
            return_date=return_date,
            trip_length_days=trip_length_days,
            typical_price=typical_price,
            savings_amount=savings_amount,
            savings_percentage=savings_percentage,
            stop_count=stop_count,
            duration_minutes=duration_minutes,
            airline_name=airline_name,
            airline_code=airline_code,
            booking_url=booking_url,
        )

        flight_deals_response_200_output_deals_item.additional_properties = d
        return flight_deals_response_200_output_deals_item

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
