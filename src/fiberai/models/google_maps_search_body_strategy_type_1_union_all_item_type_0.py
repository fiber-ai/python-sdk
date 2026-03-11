from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.google_maps_search_body_strategy_type_1_union_all_item_type_0_region_type import (
    GoogleMapsSearchBodyStrategyType1UnionAllItemType0RegionType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_maps_search_body_strategy_type_1_union_all_item_type_0_center import (
        GoogleMapsSearchBodyStrategyType1UnionAllItemType0Center,
    )


T = TypeVar("T", bound="GoogleMapsSearchBodyStrategyType1UnionAllItemType0")


@_attrs_define
class GoogleMapsSearchBodyStrategyType1UnionAllItemType0:
    """
    Attributes:
        region_type (GoogleMapsSearchBodyStrategyType1UnionAllItemType0RegionType): Use 'circle' to search for places in
            a circle
        center (GoogleMapsSearchBodyStrategyType1UnionAllItemType0Center):
        radius_miles (float | Unset): The radius of the circle in miles Default: 25.0.
    """

    region_type: GoogleMapsSearchBodyStrategyType1UnionAllItemType0RegionType
    center: GoogleMapsSearchBodyStrategyType1UnionAllItemType0Center
    radius_miles: float | Unset = 25.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region_type = self.region_type.value

        center = self.center.to_dict()

        radius_miles = self.radius_miles

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "regionType": region_type,
                "center": center,
            }
        )
        if radius_miles is not UNSET:
            field_dict["radiusMiles"] = radius_miles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.google_maps_search_body_strategy_type_1_union_all_item_type_0_center import (
            GoogleMapsSearchBodyStrategyType1UnionAllItemType0Center,
        )

        d = dict(src_dict)
        region_type = GoogleMapsSearchBodyStrategyType1UnionAllItemType0RegionType(d.pop("regionType"))

        center = GoogleMapsSearchBodyStrategyType1UnionAllItemType0Center.from_dict(d.pop("center"))

        radius_miles = d.pop("radiusMiles", UNSET)

        google_maps_search_body_strategy_type_1_union_all_item_type_0 = cls(
            region_type=region_type,
            center=center,
            radius_miles=radius_miles,
        )

        google_maps_search_body_strategy_type_1_union_all_item_type_0.additional_properties = d
        return google_maps_search_body_strategy_type_1_union_all_item_type_0

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
