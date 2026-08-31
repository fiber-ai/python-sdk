from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.flight_search_response_200_output_airports_item_arrival_item import (
        FlightSearchResponse200OutputAirportsItemArrivalItem,
    )
    from ..models.flight_search_response_200_output_airports_item_departure_item import (
        FlightSearchResponse200OutputAirportsItemDepartureItem,
    )


T = TypeVar("T", bound="FlightSearchResponse200OutputAirportsItem")


@_attrs_define
class FlightSearchResponse200OutputAirportsItem:
    """
    Attributes:
        departure (list[FlightSearchResponse200OutputAirportsItemDepartureItem]): Departure airport options matched for
            this query.
        arrival (list[FlightSearchResponse200OutputAirportsItemArrivalItem]): Arrival airport options matched for this
            query.
    """

    departure: list[FlightSearchResponse200OutputAirportsItemDepartureItem]
    arrival: list[FlightSearchResponse200OutputAirportsItemArrivalItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        departure = []
        for departure_item_data in self.departure:
            departure_item = departure_item_data.to_dict()
            departure.append(departure_item)

        arrival = []
        for arrival_item_data in self.arrival:
            arrival_item = arrival_item_data.to_dict()
            arrival.append(arrival_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "departure": departure,
                "arrival": arrival,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flight_search_response_200_output_airports_item_arrival_item import (
            FlightSearchResponse200OutputAirportsItemArrivalItem,  # noqa: PLC0415
        )
        from ..models.flight_search_response_200_output_airports_item_departure_item import (
            FlightSearchResponse200OutputAirportsItemDepartureItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        departure = []
        _departure = d.pop("departure")
        for departure_item_data in _departure:
            departure_item = FlightSearchResponse200OutputAirportsItemDepartureItem.from_dict(departure_item_data)

            departure.append(departure_item)

        arrival = []
        _arrival = d.pop("arrival")
        for arrival_item_data in _arrival:
            arrival_item = FlightSearchResponse200OutputAirportsItemArrivalItem.from_dict(arrival_item_data)

            arrival.append(arrival_item)

        flight_search_response_200_output_airports_item = cls(
            departure=departure,
            arrival=arrival,
        )

        flight_search_response_200_output_airports_item.additional_properties = d
        return flight_search_response_200_output_airports_item

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
