from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlightDealsResponse200OutputDealsItemDestination")


@_attrs_define
class FlightDealsResponse200OutputDealsItemDestination:
    """
    Attributes:
        name (str): Destination city or place name.
        freebase_id (str): Stable location identifier (Freebase ID) for this destination, beginning with '/m/' or '/g/'
            (e.g. '/m/0_vn7'). Pass as `departureAirports` or `arrivalAirports` in POST /v1/flights/search. Always present
            on returned deals.
        country_code (None | str | Unset): ISO 3166-1 alpha-3 country code (e.g. 'USA', 'GBR').
        iata_code (None | str | Unset): IATA code of the destination airport (e.g. 'TYS').
        tagline (None | str | Unset): Short highlight of the destination.
        description (None | str | Unset): Longer destination description.
        thumbnail_url (None | str | Unset): Thumbnail image URL for the destination.
    """

    name: str
    freebase_id: str
    country_code: None | str | Unset = UNSET
    iata_code: None | str | Unset = UNSET
    tagline: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        freebase_id = self.freebase_id

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        iata_code: None | str | Unset
        if isinstance(self.iata_code, Unset):
            iata_code = UNSET
        else:
            iata_code = self.iata_code

        tagline: None | str | Unset
        if isinstance(self.tagline, Unset):
            tagline = UNSET
        else:
            tagline = self.tagline

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "freebaseId": freebase_id,
            }
        )
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if iata_code is not UNSET:
            field_dict["iataCode"] = iata_code
        if tagline is not UNSET:
            field_dict["tagline"] = tagline
        if description is not UNSET:
            field_dict["description"] = description
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        freebase_id = d.pop("freebaseId")

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        def _parse_iata_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        iata_code = _parse_iata_code(d.pop("iataCode", UNSET))

        def _parse_tagline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tagline = _parse_tagline(d.pop("tagline", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))

        flight_deals_response_200_output_deals_item_destination = cls(
            name=name,
            freebase_id=freebase_id,
            country_code=country_code,
            iata_code=iata_code,
            tagline=tagline,
            description=description,
            thumbnail_url=thumbnail_url,
        )

        flight_deals_response_200_output_deals_item_destination.additional_properties = d
        return flight_deals_response_200_output_deals_item_destination

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
