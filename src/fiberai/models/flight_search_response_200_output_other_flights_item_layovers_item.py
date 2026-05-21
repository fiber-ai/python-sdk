from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlightSearchResponse200OutputOtherFlightsItemLayoversItem")


@_attrs_define
class FlightSearchResponse200OutputOtherFlightsItemLayoversItem:
    """
    Attributes:
        iata_code (None | str | Unset): 3-letter IATA code of the layover airport (e.g. 'DFW', 'ORD').
        airport_name (None | str | Unset): Layover airport name.
        duration_minutes (int | None | Unset): Layover duration in minutes.
        is_overnight (bool | None | Unset): True when layover spans overnight.
    """

    iata_code: None | str | Unset = UNSET
    airport_name: None | str | Unset = UNSET
    duration_minutes: int | None | Unset = UNSET
    is_overnight: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        iata_code: None | str | Unset
        if isinstance(self.iata_code, Unset):
            iata_code = UNSET
        else:
            iata_code = self.iata_code

        airport_name: None | str | Unset
        if isinstance(self.airport_name, Unset):
            airport_name = UNSET
        else:
            airport_name = self.airport_name

        duration_minutes: int | None | Unset
        if isinstance(self.duration_minutes, Unset):
            duration_minutes = UNSET
        else:
            duration_minutes = self.duration_minutes

        is_overnight: bool | None | Unset
        if isinstance(self.is_overnight, Unset):
            is_overnight = UNSET
        else:
            is_overnight = self.is_overnight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if iata_code is not UNSET:
            field_dict["iataCode"] = iata_code
        if airport_name is not UNSET:
            field_dict["airportName"] = airport_name
        if duration_minutes is not UNSET:
            field_dict["durationMinutes"] = duration_minutes
        if is_overnight is not UNSET:
            field_dict["isOvernight"] = is_overnight

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

        def _parse_airport_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        airport_name = _parse_airport_name(d.pop("airportName", UNSET))

        def _parse_duration_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_minutes = _parse_duration_minutes(d.pop("durationMinutes", UNSET))

        def _parse_is_overnight(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_overnight = _parse_is_overnight(d.pop("isOvernight", UNSET))

        flight_search_response_200_output_other_flights_item_layovers_item = cls(
            iata_code=iata_code,
            airport_name=airport_name,
            duration_minutes=duration_minutes,
            is_overnight=is_overnight,
        )

        flight_search_response_200_output_other_flights_item_layovers_item.additional_properties = d
        return flight_search_response_200_output_other_flights_item_layovers_item

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
