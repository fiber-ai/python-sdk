from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GoogleMapsSearchBodyStrategyType1UnionAllItemType0Center")


@_attrs_define
class GoogleMapsSearchBodyStrategyType1UnionAllItemType0Center:
    """
    Attributes:
        latitude (float): The latitude of the point
        longitude (float): The longitude of the point
    """

    latitude: float
    longitude: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "latitude": latitude,
                "longitude": longitude,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        google_maps_search_body_strategy_type_1_union_all_item_type_0_center = cls(
            latitude=latitude,
            longitude=longitude,
        )

        google_maps_search_body_strategy_type_1_union_all_item_type_0_center.additional_properties = d
        return google_maps_search_body_strategy_type_1_union_all_item_type_0_center

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
