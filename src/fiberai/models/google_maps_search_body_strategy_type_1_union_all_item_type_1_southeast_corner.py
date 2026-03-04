from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GoogleMapsSearchBodyStrategyType1UnionAllItemType1SoutheastCorner")



@_attrs_define
class GoogleMapsSearchBodyStrategyType1UnionAllItemType1SoutheastCorner:
    """ The coordinates of the south east corner of the rectangle

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
        field_dict.update({
            "latitude": latitude,
            "longitude": longitude,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        google_maps_search_body_strategy_type_1_union_all_item_type_1_southeast_corner = cls(
            latitude=latitude,
            longitude=longitude,
        )


        google_maps_search_body_strategy_type_1_union_all_item_type_1_southeast_corner.additional_properties = d
        return google_maps_search_body_strategy_type_1_union_all_item_type_1_southeast_corner

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
