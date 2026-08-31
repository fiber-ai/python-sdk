from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flight_search_response_200_output_other_flights_item_segments_item_arrival_airport import (
        FlightSearchResponse200OutputOtherFlightsItemSegmentsItemArrivalAirport,
    )
    from ..models.flight_search_response_200_output_other_flights_item_segments_item_departure_airport import (
        FlightSearchResponse200OutputOtherFlightsItemSegmentsItemDepartureAirport,
    )


T = TypeVar("T", bound="FlightSearchResponse200OutputOtherFlightsItemSegmentsItem")


@_attrs_define
class FlightSearchResponse200OutputOtherFlightsItemSegmentsItem:
    """
    Attributes:
        departure_airport (FlightSearchResponse200OutputOtherFlightsItemSegmentsItemDepartureAirport): Departure
            airport.
        arrival_airport (FlightSearchResponse200OutputOtherFlightsItemSegmentsItemArrivalAirport): Arrival airport.
        duration_minutes (int | None | Unset): Segment duration in minutes.
        airline_name (None | str | Unset): Operating airline name.
        airline_logo_url (None | str | Unset): Operating airline logo URL.
        travel_class (None | str | Unset): Cabin class as labeled in the search results (e.g. 'Economy', 'Premium
            Economy', 'Business', 'First').
        flight_number (None | str | Unset): Flight number including airline code (e.g. 'UA 2175', 'DL 1384').
        aircraft_model (None | str | Unset): Aircraft model.
        legroom (None | str | Unset): Legroom distance as reported by the airline (e.g. '32 in').
        is_overnight (bool | None | Unset): True when this segment is overnight.
        is_often_delayed (bool | None | Unset): True when this segment is frequently delayed.
        carbon_emission_kg (float | None | Unset): Estimated carbon emissions in kilograms.
    """

    departure_airport: FlightSearchResponse200OutputOtherFlightsItemSegmentsItemDepartureAirport
    arrival_airport: FlightSearchResponse200OutputOtherFlightsItemSegmentsItemArrivalAirport
    duration_minutes: int | None | Unset = UNSET
    airline_name: None | str | Unset = UNSET
    airline_logo_url: None | str | Unset = UNSET
    travel_class: None | str | Unset = UNSET
    flight_number: None | str | Unset = UNSET
    aircraft_model: None | str | Unset = UNSET
    legroom: None | str | Unset = UNSET
    is_overnight: bool | None | Unset = UNSET
    is_often_delayed: bool | None | Unset = UNSET
    carbon_emission_kg: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        departure_airport = self.departure_airport.to_dict()

        arrival_airport = self.arrival_airport.to_dict()

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

        airline_logo_url: None | str | Unset
        if isinstance(self.airline_logo_url, Unset):
            airline_logo_url = UNSET
        else:
            airline_logo_url = self.airline_logo_url

        travel_class: None | str | Unset
        if isinstance(self.travel_class, Unset):
            travel_class = UNSET
        else:
            travel_class = self.travel_class

        flight_number: None | str | Unset
        if isinstance(self.flight_number, Unset):
            flight_number = UNSET
        else:
            flight_number = self.flight_number

        aircraft_model: None | str | Unset
        if isinstance(self.aircraft_model, Unset):
            aircraft_model = UNSET
        else:
            aircraft_model = self.aircraft_model

        legroom: None | str | Unset
        if isinstance(self.legroom, Unset):
            legroom = UNSET
        else:
            legroom = self.legroom

        is_overnight: bool | None | Unset
        if isinstance(self.is_overnight, Unset):
            is_overnight = UNSET
        else:
            is_overnight = self.is_overnight

        is_often_delayed: bool | None | Unset
        if isinstance(self.is_often_delayed, Unset):
            is_often_delayed = UNSET
        else:
            is_often_delayed = self.is_often_delayed

        carbon_emission_kg: float | None | Unset
        if isinstance(self.carbon_emission_kg, Unset):
            carbon_emission_kg = UNSET
        else:
            carbon_emission_kg = self.carbon_emission_kg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "departureAirport": departure_airport,
                "arrivalAirport": arrival_airport,
            }
        )
        if duration_minutes is not UNSET:
            field_dict["durationMinutes"] = duration_minutes
        if airline_name is not UNSET:
            field_dict["airlineName"] = airline_name
        if airline_logo_url is not UNSET:
            field_dict["airlineLogoUrl"] = airline_logo_url
        if travel_class is not UNSET:
            field_dict["travelClass"] = travel_class
        if flight_number is not UNSET:
            field_dict["flightNumber"] = flight_number
        if aircraft_model is not UNSET:
            field_dict["aircraftModel"] = aircraft_model
        if legroom is not UNSET:
            field_dict["legroom"] = legroom
        if is_overnight is not UNSET:
            field_dict["isOvernight"] = is_overnight
        if is_often_delayed is not UNSET:
            field_dict["isOftenDelayed"] = is_often_delayed
        if carbon_emission_kg is not UNSET:
            field_dict["carbonEmissionKg"] = carbon_emission_kg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flight_search_response_200_output_other_flights_item_segments_item_arrival_airport import (
            FlightSearchResponse200OutputOtherFlightsItemSegmentsItemArrivalAirport,  # noqa: PLC0415
        )
        from ..models.flight_search_response_200_output_other_flights_item_segments_item_departure_airport import (
            FlightSearchResponse200OutputOtherFlightsItemSegmentsItemDepartureAirport,  # noqa: PLC0415
        )

        d = dict(src_dict)
        departure_airport = FlightSearchResponse200OutputOtherFlightsItemSegmentsItemDepartureAirport.from_dict(
            d.pop("departureAirport")
        )

        arrival_airport = FlightSearchResponse200OutputOtherFlightsItemSegmentsItemArrivalAirport.from_dict(
            d.pop("arrivalAirport")
        )

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

        def _parse_airline_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        airline_logo_url = _parse_airline_logo_url(d.pop("airlineLogoUrl", UNSET))

        def _parse_travel_class(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        travel_class = _parse_travel_class(d.pop("travelClass", UNSET))

        def _parse_flight_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flight_number = _parse_flight_number(d.pop("flightNumber", UNSET))

        def _parse_aircraft_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aircraft_model = _parse_aircraft_model(d.pop("aircraftModel", UNSET))

        def _parse_legroom(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legroom = _parse_legroom(d.pop("legroom", UNSET))

        def _parse_is_overnight(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_overnight = _parse_is_overnight(d.pop("isOvernight", UNSET))

        def _parse_is_often_delayed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_often_delayed = _parse_is_often_delayed(d.pop("isOftenDelayed", UNSET))

        def _parse_carbon_emission_kg(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        carbon_emission_kg = _parse_carbon_emission_kg(d.pop("carbonEmissionKg", UNSET))

        flight_search_response_200_output_other_flights_item_segments_item = cls(
            departure_airport=departure_airport,
            arrival_airport=arrival_airport,
            duration_minutes=duration_minutes,
            airline_name=airline_name,
            airline_logo_url=airline_logo_url,
            travel_class=travel_class,
            flight_number=flight_number,
            aircraft_model=aircraft_model,
            legroom=legroom,
            is_overnight=is_overnight,
            is_often_delayed=is_often_delayed,
            carbon_emission_kg=carbon_emission_kg,
        )

        flight_search_response_200_output_other_flights_item_segments_item.additional_properties = d
        return flight_search_response_200_output_other_flights_item_segments_item

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
