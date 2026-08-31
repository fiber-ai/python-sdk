from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_metro_areas_response_200_output_metro_areas_item_type_1_slug import (
    GetMetroAreasResponse200OutputMetroAreasItemType1Slug,
)
from ..models.get_metro_areas_response_200_output_metro_areas_item_type_1_type import (
    GetMetroAreasResponse200OutputMetroAreasItemType1Type,
)

if TYPE_CHECKING:
    from ..models.get_metro_areas_response_200_output_metro_areas_item_type_1_vertices_item import (
        GetMetroAreasResponse200OutputMetroAreasItemType1VerticesItem,
    )


T = TypeVar("T", bound="GetMetroAreasResponse200OutputMetroAreasItemType1")


@_attrs_define
class GetMetroAreasResponse200OutputMetroAreasItemType1:
    """
    Attributes:
        type_ (GetMetroAreasResponse200OutputMetroAreasItemType1Type):
        slug (GetMetroAreasResponse200OutputMetroAreasItemType1Slug):
        name (str):
        emoji (str):
        country_code (str):
        cities (list[str]):
        synonyms (list[str]):
        vertices (list[GetMetroAreasResponse200OutputMetroAreasItemType1VerticesItem]):
    """

    type_: GetMetroAreasResponse200OutputMetroAreasItemType1Type
    slug: GetMetroAreasResponse200OutputMetroAreasItemType1Slug
    name: str
    emoji: str
    country_code: str
    cities: list[str]
    synonyms: list[str]
    vertices: list[GetMetroAreasResponse200OutputMetroAreasItemType1VerticesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        slug = self.slug.value

        name = self.name

        emoji = self.emoji

        country_code = self.country_code

        cities = self.cities

        synonyms = self.synonyms

        vertices = []
        for vertices_item_data in self.vertices:
            vertices_item = vertices_item_data.to_dict()
            vertices.append(vertices_item)

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
                "vertices": vertices,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_metro_areas_response_200_output_metro_areas_item_type_1_vertices_item import (
            GetMetroAreasResponse200OutputMetroAreasItemType1VerticesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = GetMetroAreasResponse200OutputMetroAreasItemType1Type(d.pop("type"))

        slug = GetMetroAreasResponse200OutputMetroAreasItemType1Slug(d.pop("slug"))

        name = d.pop("name")

        emoji = d.pop("emoji")

        country_code = d.pop("countryCode")

        cities = cast(list[str], d.pop("cities"))

        synonyms = cast(list[str], d.pop("synonyms"))

        vertices = []
        _vertices = d.pop("vertices")
        for vertices_item_data in _vertices:
            vertices_item = GetMetroAreasResponse200OutputMetroAreasItemType1VerticesItem.from_dict(vertices_item_data)

            vertices.append(vertices_item)

        get_metro_areas_response_200_output_metro_areas_item_type_1 = cls(
            type_=type_,
            slug=slug,
            name=name,
            emoji=emoji,
            country_code=country_code,
            cities=cities,
            synonyms=synonyms,
            vertices=vertices,
        )

        get_metro_areas_response_200_output_metro_areas_item_type_1.additional_properties = d
        return get_metro_areas_response_200_output_metro_areas_item_type_1

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
