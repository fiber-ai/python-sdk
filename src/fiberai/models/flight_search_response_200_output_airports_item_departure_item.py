from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlightSearchResponse200OutputAirportsItemDepartureItem")


@_attrs_define
class FlightSearchResponse200OutputAirportsItemDepartureItem:
    """
    Attributes:
        iata_code (None | str | Unset): IATA airport code (e.g. 'JFK'). When the search targeted a metro area via an X-
            alias or Freebase ID input, this will be a Freebase ID (e.g. '/m/02_286') representing the metro rather than a
            single airport.
        name (None | str | Unset): Airport name.
        city (None | str | Unset): City name.
        country_code (None | str | Unset): ISO 3166-1 alpha-3 country code (e.g. 'USA', 'GBR').
    """

    iata_code: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
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

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if iata_code is not UNSET:
            field_dict["iataCode"] = iata_code
        if name is not UNSET:
            field_dict["name"] = name
        if city is not UNSET:
            field_dict["city"] = city
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code

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

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        flight_search_response_200_output_airports_item_departure_item = cls(
            iata_code=iata_code,
            name=name,
            city=city,
            country_code=country_code,
        )

        flight_search_response_200_output_airports_item_departure_item.additional_properties = d
        return flight_search_response_200_output_airports_item_departure_item

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
