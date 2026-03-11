from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.google_maps_search_body_strategy_type_1_union_all_item_type_1_region_type import (
    GoogleMapsSearchBodyStrategyType1UnionAllItemType1RegionType,
)

if TYPE_CHECKING:
    from ..models.google_maps_search_body_strategy_type_1_union_all_item_type_1_northwest_corner import (
        GoogleMapsSearchBodyStrategyType1UnionAllItemType1NorthwestCorner,
    )
    from ..models.google_maps_search_body_strategy_type_1_union_all_item_type_1_southeast_corner import (
        GoogleMapsSearchBodyStrategyType1UnionAllItemType1SoutheastCorner,
    )


T = TypeVar("T", bound="GoogleMapsSearchBodyStrategyType1UnionAllItemType1")


@_attrs_define
class GoogleMapsSearchBodyStrategyType1UnionAllItemType1:
    """
    Attributes:
        region_type (GoogleMapsSearchBodyStrategyType1UnionAllItemType1RegionType): Use 'rectangle' to search for places
            in a rectangle
        northwest_corner (GoogleMapsSearchBodyStrategyType1UnionAllItemType1NorthwestCorner): The coordinates of the
            north west corner of the rectangle
        southeast_corner (GoogleMapsSearchBodyStrategyType1UnionAllItemType1SoutheastCorner): The coordinates of the
            south east corner of the rectangle
    """

    region_type: GoogleMapsSearchBodyStrategyType1UnionAllItemType1RegionType
    northwest_corner: GoogleMapsSearchBodyStrategyType1UnionAllItemType1NorthwestCorner
    southeast_corner: GoogleMapsSearchBodyStrategyType1UnionAllItemType1SoutheastCorner
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region_type = self.region_type.value

        northwest_corner = self.northwest_corner.to_dict()

        southeast_corner = self.southeast_corner.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "regionType": region_type,
                "northwestCorner": northwest_corner,
                "southeastCorner": southeast_corner,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.google_maps_search_body_strategy_type_1_union_all_item_type_1_northwest_corner import (
            GoogleMapsSearchBodyStrategyType1UnionAllItemType1NorthwestCorner,
        )
        from ..models.google_maps_search_body_strategy_type_1_union_all_item_type_1_southeast_corner import (
            GoogleMapsSearchBodyStrategyType1UnionAllItemType1SoutheastCorner,
        )

        d = dict(src_dict)
        region_type = GoogleMapsSearchBodyStrategyType1UnionAllItemType1RegionType(d.pop("regionType"))

        northwest_corner = GoogleMapsSearchBodyStrategyType1UnionAllItemType1NorthwestCorner.from_dict(
            d.pop("northwestCorner")
        )

        southeast_corner = GoogleMapsSearchBodyStrategyType1UnionAllItemType1SoutheastCorner.from_dict(
            d.pop("southeastCorner")
        )

        google_maps_search_body_strategy_type_1_union_all_item_type_1 = cls(
            region_type=region_type,
            northwest_corner=northwest_corner,
            southeast_corner=southeast_corner,
        )

        google_maps_search_body_strategy_type_1_union_all_item_type_1.additional_properties = d
        return google_maps_search_body_strategy_type_1_union_all_item_type_1

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
