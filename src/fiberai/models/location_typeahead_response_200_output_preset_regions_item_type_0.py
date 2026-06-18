from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.location_typeahead_response_200_output_preset_regions_item_type_0_slug import (
    LocationTypeaheadResponse200OutputPresetRegionsItemType0Slug,
)
from ..models.location_typeahead_response_200_output_preset_regions_item_type_0_type import (
    LocationTypeaheadResponse200OutputPresetRegionsItemType0Type,
)

T = TypeVar("T", bound="LocationTypeaheadResponse200OutputPresetRegionsItemType0")


@_attrs_define
class LocationTypeaheadResponse200OutputPresetRegionsItemType0:
    """
    Attributes:
        type_ (LocationTypeaheadResponse200OutputPresetRegionsItemType0Type):
        slug (LocationTypeaheadResponse200OutputPresetRegionsItemType0Slug):
        name (str):
        emoji (str):
        country_code (str):
        cities (list[str]):
        synonyms (list[str]):
        latitude (float):
        longitude (float):
        radius_miles (float):
    """

    type_: LocationTypeaheadResponse200OutputPresetRegionsItemType0Type
    slug: LocationTypeaheadResponse200OutputPresetRegionsItemType0Slug
    name: str
    emoji: str
    country_code: str
    cities: list[str]
    synonyms: list[str]
    latitude: float
    longitude: float
    radius_miles: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        slug = self.slug.value

        name = self.name

        emoji = self.emoji

        country_code = self.country_code

        cities = self.cities

        synonyms = self.synonyms

        latitude = self.latitude

        longitude = self.longitude

        radius_miles = self.radius_miles

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "slug": slug,
                "name": name,
                "emoji": emoji,
                "countryCode": country_code,
                "cities": cities,
                "synonyms": synonyms,
                "latitude": latitude,
                "longitude": longitude,
                "radiusMiles": radius_miles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = LocationTypeaheadResponse200OutputPresetRegionsItemType0Type(d.pop("type"))

        slug = LocationTypeaheadResponse200OutputPresetRegionsItemType0Slug(d.pop("slug"))

        name = d.pop("name")

        emoji = d.pop("emoji")

        country_code = d.pop("countryCode")

        cities = cast(list[str], d.pop("cities"))

        synonyms = cast(list[str], d.pop("synonyms"))

        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        radius_miles = d.pop("radiusMiles")

        location_typeahead_response_200_output_preset_regions_item_type_0 = cls(
            type_=type_,
            slug=slug,
            name=name,
            emoji=emoji,
            country_code=country_code,
            cities=cities,
            synonyms=synonyms,
            latitude=latitude,
            longitude=longitude,
            radius_miles=radius_miles,
        )

        location_typeahead_response_200_output_preset_regions_item_type_0.additional_properties = d
        return location_typeahead_response_200_output_preset_regions_item_type_0

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
