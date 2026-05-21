from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flight_search_response_200_output_other_flights_item_flight_type_type_1 import (
    FlightSearchResponse200OutputOtherFlightsItemFlightTypeType1,
)
from ..models.flight_search_response_200_output_other_flights_item_flight_type_type_2_type_1 import (
    FlightSearchResponse200OutputOtherFlightsItemFlightTypeType2Type1,
)
from ..models.flight_search_response_200_output_other_flights_item_flight_type_type_3_type_1 import (
    FlightSearchResponse200OutputOtherFlightsItemFlightTypeType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flight_search_response_200_output_other_flights_item_carbon_emissions_type_0 import (
        FlightSearchResponse200OutputOtherFlightsItemCarbonEmissionsType0,
    )
    from ..models.flight_search_response_200_output_other_flights_item_layovers_item import (
        FlightSearchResponse200OutputOtherFlightsItemLayoversItem,
    )
    from ..models.flight_search_response_200_output_other_flights_item_segments_item import (
        FlightSearchResponse200OutputOtherFlightsItemSegmentsItem,
    )


T = TypeVar("T", bound="FlightSearchResponse200OutputOtherFlightsItem")


@_attrs_define
class FlightSearchResponse200OutputOtherFlightsItem:
    """
    Attributes:
        segments (list[FlightSearchResponse200OutputOtherFlightsItemSegmentsItem]): Flight segments for this itinerary.
        layovers (list[FlightSearchResponse200OutputOtherFlightsItemLayoversItem]): Layovers for this itinerary.
        total_duration_minutes (int | None | Unset): Total itinerary duration in minutes.
        price (int | None | Unset): Total itinerary price in whole currency units.
        booking_token (None | str | Unset): Opaque booking token. Pass this in follow-up requests to retrieve booking
            options for this itinerary.
        flight_type (FlightSearchResponse200OutputOtherFlightsItemFlightTypeType1 |
            FlightSearchResponse200OutputOtherFlightsItemFlightTypeType2Type1 |
            FlightSearchResponse200OutputOtherFlightsItemFlightTypeType3Type1 | None | Unset): Trip type for this itinerary.
        main_airline_logo_url (None | str | Unset): Logo URL for the primary airline on this itinerary. For multi-
            airline itineraries this may be a generic multi-carrier logo.
        carbon_emissions (FlightSearchResponse200OutputOtherFlightsItemCarbonEmissionsType0 | None | Unset): Carbon
            emissions summary for this itinerary.
        also_sold_by (list[str] | None | Unset): Full names of other airlines that also sell this itinerary (e.g.
            'United', 'Korean Air').
        operating_carrier (None | str | Unset): Full name of the airline operating the aircraft and crew, when it
            differs from the marketing airline (e.g. 'Envoy Air' operating on behalf of American Airlines).
    """

    segments: list[FlightSearchResponse200OutputOtherFlightsItemSegmentsItem]
    layovers: list[FlightSearchResponse200OutputOtherFlightsItemLayoversItem]
    total_duration_minutes: int | None | Unset = UNSET
    price: int | None | Unset = UNSET
    booking_token: None | str | Unset = UNSET
    flight_type: (
        FlightSearchResponse200OutputOtherFlightsItemFlightTypeType1
        | FlightSearchResponse200OutputOtherFlightsItemFlightTypeType2Type1
        | FlightSearchResponse200OutputOtherFlightsItemFlightTypeType3Type1
        | None
        | Unset
    ) = UNSET
    main_airline_logo_url: None | str | Unset = UNSET
    carbon_emissions: FlightSearchResponse200OutputOtherFlightsItemCarbonEmissionsType0 | None | Unset = UNSET
    also_sold_by: list[str] | None | Unset = UNSET
    operating_carrier: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.flight_search_response_200_output_other_flights_item_carbon_emissions_type_0 import (
            FlightSearchResponse200OutputOtherFlightsItemCarbonEmissionsType0,
        )

        segments = []
        for segments_item_data in self.segments:
            segments_item = segments_item_data.to_dict()
            segments.append(segments_item)

        layovers = []
        for layovers_item_data in self.layovers:
            layovers_item = layovers_item_data.to_dict()
            layovers.append(layovers_item)

        total_duration_minutes: int | None | Unset
        if isinstance(self.total_duration_minutes, Unset):
            total_duration_minutes = UNSET
        else:
            total_duration_minutes = self.total_duration_minutes

        price: int | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        booking_token: None | str | Unset
        if isinstance(self.booking_token, Unset):
            booking_token = UNSET
        else:
            booking_token = self.booking_token

        flight_type: None | str | Unset
        if isinstance(self.flight_type, Unset):
            flight_type = UNSET
        elif isinstance(self.flight_type, FlightSearchResponse200OutputOtherFlightsItemFlightTypeType1):
            flight_type = self.flight_type.value
        elif isinstance(self.flight_type, FlightSearchResponse200OutputOtherFlightsItemFlightTypeType2Type1):
            flight_type = self.flight_type.value
        elif isinstance(self.flight_type, FlightSearchResponse200OutputOtherFlightsItemFlightTypeType3Type1):
            flight_type = self.flight_type.value
        else:
            flight_type = self.flight_type

        main_airline_logo_url: None | str | Unset
        if isinstance(self.main_airline_logo_url, Unset):
            main_airline_logo_url = UNSET
        else:
            main_airline_logo_url = self.main_airline_logo_url

        carbon_emissions: dict[str, Any] | None | Unset
        if isinstance(self.carbon_emissions, Unset):
            carbon_emissions = UNSET
        elif isinstance(self.carbon_emissions, FlightSearchResponse200OutputOtherFlightsItemCarbonEmissionsType0):
            carbon_emissions = self.carbon_emissions.to_dict()
        else:
            carbon_emissions = self.carbon_emissions

        also_sold_by: list[str] | None | Unset
        if isinstance(self.also_sold_by, Unset):
            also_sold_by = UNSET
        elif isinstance(self.also_sold_by, list):
            also_sold_by = self.also_sold_by

        else:
            also_sold_by = self.also_sold_by

        operating_carrier: None | str | Unset
        if isinstance(self.operating_carrier, Unset):
            operating_carrier = UNSET
        else:
            operating_carrier = self.operating_carrier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "segments": segments,
                "layovers": layovers,
            }
        )
        if total_duration_minutes is not UNSET:
            field_dict["totalDurationMinutes"] = total_duration_minutes
        if price is not UNSET:
            field_dict["price"] = price
        if booking_token is not UNSET:
            field_dict["bookingToken"] = booking_token
        if flight_type is not UNSET:
            field_dict["flightType"] = flight_type
        if main_airline_logo_url is not UNSET:
            field_dict["mainAirlineLogoUrl"] = main_airline_logo_url
        if carbon_emissions is not UNSET:
            field_dict["carbonEmissions"] = carbon_emissions
        if also_sold_by is not UNSET:
            field_dict["alsoSoldBy"] = also_sold_by
        if operating_carrier is not UNSET:
            field_dict["operatingCarrier"] = operating_carrier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flight_search_response_200_output_other_flights_item_carbon_emissions_type_0 import (
            FlightSearchResponse200OutputOtherFlightsItemCarbonEmissionsType0,
        )
        from ..models.flight_search_response_200_output_other_flights_item_layovers_item import (
            FlightSearchResponse200OutputOtherFlightsItemLayoversItem,
        )
        from ..models.flight_search_response_200_output_other_flights_item_segments_item import (
            FlightSearchResponse200OutputOtherFlightsItemSegmentsItem,
        )

        d = dict(src_dict)
        segments = []
        _segments = d.pop("segments")
        for segments_item_data in _segments:
            segments_item = FlightSearchResponse200OutputOtherFlightsItemSegmentsItem.from_dict(segments_item_data)

            segments.append(segments_item)

        layovers = []
        _layovers = d.pop("layovers")
        for layovers_item_data in _layovers:
            layovers_item = FlightSearchResponse200OutputOtherFlightsItemLayoversItem.from_dict(layovers_item_data)

            layovers.append(layovers_item)

        def _parse_total_duration_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_duration_minutes = _parse_total_duration_minutes(d.pop("totalDurationMinutes", UNSET))

        def _parse_price(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_booking_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        booking_token = _parse_booking_token(d.pop("bookingToken", UNSET))

        def _parse_flight_type(
            data: object,
        ) -> (
            FlightSearchResponse200OutputOtherFlightsItemFlightTypeType1
            | FlightSearchResponse200OutputOtherFlightsItemFlightTypeType2Type1
            | FlightSearchResponse200OutputOtherFlightsItemFlightTypeType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                flight_type_type_1 = FlightSearchResponse200OutputOtherFlightsItemFlightTypeType1(data)

                return flight_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                flight_type_type_2_type_1 = FlightSearchResponse200OutputOtherFlightsItemFlightTypeType2Type1(data)

                return flight_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                flight_type_type_3_type_1 = FlightSearchResponse200OutputOtherFlightsItemFlightTypeType3Type1(data)

                return flight_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FlightSearchResponse200OutputOtherFlightsItemFlightTypeType1
                | FlightSearchResponse200OutputOtherFlightsItemFlightTypeType2Type1
                | FlightSearchResponse200OutputOtherFlightsItemFlightTypeType3Type1
                | None
                | Unset,
                data,
            )

        flight_type = _parse_flight_type(d.pop("flightType", UNSET))

        def _parse_main_airline_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        main_airline_logo_url = _parse_main_airline_logo_url(d.pop("mainAirlineLogoUrl", UNSET))

        def _parse_carbon_emissions(
            data: object,
        ) -> FlightSearchResponse200OutputOtherFlightsItemCarbonEmissionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                carbon_emissions_type_0 = FlightSearchResponse200OutputOtherFlightsItemCarbonEmissionsType0.from_dict(
                    data
                )

                return carbon_emissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FlightSearchResponse200OutputOtherFlightsItemCarbonEmissionsType0 | None | Unset, data)

        carbon_emissions = _parse_carbon_emissions(d.pop("carbonEmissions", UNSET))

        def _parse_also_sold_by(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                also_sold_by_type_0 = cast(list[str], data)

                return also_sold_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        also_sold_by = _parse_also_sold_by(d.pop("alsoSoldBy", UNSET))

        def _parse_operating_carrier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operating_carrier = _parse_operating_carrier(d.pop("operatingCarrier", UNSET))

        flight_search_response_200_output_other_flights_item = cls(
            segments=segments,
            layovers=layovers,
            total_duration_minutes=total_duration_minutes,
            price=price,
            booking_token=booking_token,
            flight_type=flight_type,
            main_airline_logo_url=main_airline_logo_url,
            carbon_emissions=carbon_emissions,
            also_sold_by=also_sold_by,
            operating_carrier=operating_carrier,
        )

        flight_search_response_200_output_other_flights_item.additional_properties = d
        return flight_search_response_200_output_other_flights_item

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
