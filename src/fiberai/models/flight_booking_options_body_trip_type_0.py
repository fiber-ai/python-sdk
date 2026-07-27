from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flight_booking_options_body_trip_type_0_flight_type import FlightBookingOptionsBodyTripType0FlightType

T = TypeVar("T", bound="FlightBookingOptionsBodyTripType0")


@_attrs_define
class FlightBookingOptionsBodyTripType0:
    """
    Attributes:
        flight_type (FlightBookingOptionsBodyTripType0FlightType):
        departure_airports (str): Airport(s) to search. Accepts a 3-letter IATA airport code (e.g. 'JFK'), a comma-
            separated IATA list to search multiple airports (e.g. 'JFK,LGA,EWR'), an X- metro alias that covers every
            airport in a metro area (e.g. 'X-NYC' — call GET /v1/enums/flight-regions for the full list), or a Freebase ID
            for a city or metro (e.g. '/m/02_286'). Case-insensitive except Freebase IDs.
        arrival_airports (str): Airport(s) to search. Accepts a 3-letter IATA airport code (e.g. 'JFK'), a comma-
            separated IATA list to search multiple airports (e.g. 'JFK,LGA,EWR'), an X- metro alias that covers every
            airport in a metro area (e.g. 'X-NYC' — call GET /v1/enums/flight-regions for the full list), or a Freebase ID
            for a city or metro (e.g. '/m/02_286'). Case-insensitive except Freebase IDs.
        outbound_date (str): ISO date in YYYY-MM-DD format (e.g. '2026-06-10').
    """

    flight_type: FlightBookingOptionsBodyTripType0FlightType
    departure_airports: str
    arrival_airports: str
    outbound_date: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flight_type = self.flight_type.value

        departure_airports = self.departure_airports

        arrival_airports = self.arrival_airports

        outbound_date = self.outbound_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "flightType": flight_type,
                "departureAirports": departure_airports,
                "arrivalAirports": arrival_airports,
                "outboundDate": outbound_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        flight_type = FlightBookingOptionsBodyTripType0FlightType(d.pop("flightType"))

        departure_airports = d.pop("departureAirports")

        arrival_airports = d.pop("arrivalAirports")

        outbound_date = d.pop("outboundDate")

        flight_booking_options_body_trip_type_0 = cls(
            flight_type=flight_type,
            departure_airports=departure_airports,
            arrival_airports=arrival_airports,
            outbound_date=outbound_date,
        )

        flight_booking_options_body_trip_type_0.additional_properties = d
        return flight_booking_options_body_trip_type_0

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
