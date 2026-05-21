from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CompanyCountBodySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType1VerticesItem")


@_attrs_define
class CompanyCountBodySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType1VerticesItem:
    """
    Attributes:
        latitude (float):
        longitude (float):
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

        company_count_body_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_1_vertices_item = cls(
            latitude=latitude,
            longitude=longitude,
        )

        company_count_body_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_1_vertices_item.additional_properties = d
        return company_count_body_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_1_vertices_item

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
