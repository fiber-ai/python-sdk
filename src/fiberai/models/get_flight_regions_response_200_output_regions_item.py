from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetFlightRegionsResponse200OutputRegionsItem")


@_attrs_define
class GetFlightRegionsResponse200OutputRegionsItem:
    """A flight region alias covering one metropolitan area's airports.

    Attributes:
        api_code (str): Alias to use as `departureAirports` / `arrivalAirports` to target this entire metro (e.g.
            'X-NYC').
        name (str): Human-readable metro name (e.g. 'New York City').
        airport_iata_codes (list[str]): IATA codes covered by this metro alias (e.g. 'JFK', 'LGA', 'EWR').
        freebase_id (str): Stable identifier for this metro. Also accepted as `departureAirports` / `arrivalAirports`.
    """

    api_code: str
    name: str
    airport_iata_codes: list[str]
    freebase_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_code = self.api_code

        name = self.name

        airport_iata_codes = self.airport_iata_codes

        freebase_id = self.freebase_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiCode": api_code,
                "name": name,
                "airportIataCodes": airport_iata_codes,
                "freebaseId": freebase_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_code = d.pop("apiCode")

        name = d.pop("name")

        airport_iata_codes = cast(list[str], d.pop("airportIataCodes"))

        freebase_id = d.pop("freebaseId")

        get_flight_regions_response_200_output_regions_item = cls(
            api_code=api_code,
            name=name,
            airport_iata_codes=airport_iata_codes,
            freebase_id=freebase_id,
        )

        get_flight_regions_response_200_output_regions_item.additional_properties = d
        return get_flight_regions_response_200_output_regions_item

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
