from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlightSearchResponse200OutputBestFlightsItemSegmentsItemArrivalAirport")


@_attrs_define
class FlightSearchResponse200OutputBestFlightsItemSegmentsItemArrivalAirport:
    """Arrival airport.

    Attributes:
        iata_code (None | str | Unset): 3-letter IATA airport code (e.g. 'JFK', 'LAX', 'LHR').
        name (None | str | Unset): Airport display name.
        local_date_time (None | str | Unset): Local departure or arrival datetime without timezone offset (format: YYYY-
            MM-DDTHH:mm:ss).
    """

    iata_code: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    local_date_time: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        iata_code: None | str | Unset
        if isinstance(self.iata_code, Unset):
            iata_code = UNSET
        else:
            iata_code = self.iata_code

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        local_date_time: None | str | Unset
        if isinstance(self.local_date_time, Unset):
            local_date_time = UNSET
        else:
            local_date_time = self.local_date_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if iata_code is not UNSET:
            field_dict["iataCode"] = iata_code
        if name is not UNSET:
            field_dict["name"] = name
        if local_date_time is not UNSET:
            field_dict["localDateTime"] = local_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_iata_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        iata_code = _parse_iata_code(d.pop("iataCode", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_local_date_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        local_date_time = _parse_local_date_time(d.pop("localDateTime", UNSET))

        flight_search_response_200_output_best_flights_item_segments_item_arrival_airport = cls(
            iata_code=iata_code,
            name=name,
            local_date_time=local_date_time,
        )

        flight_search_response_200_output_best_flights_item_segments_item_arrival_airport.additional_properties = d
        return flight_search_response_200_output_best_flights_item_segments_item_arrival_airport

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
