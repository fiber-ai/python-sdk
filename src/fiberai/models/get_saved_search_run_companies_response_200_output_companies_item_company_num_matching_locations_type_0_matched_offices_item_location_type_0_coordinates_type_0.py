from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyNumMatchingLocationsType0MatchedOfficesItemLocationType0CoordinatesType0",
)


@_attrs_define
class GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyNumMatchingLocationsType0MatchedOfficesItemLocationType0CoordinatesType0:
    """
    Attributes:
        lat (float):
        lon (float):
    """

    lat: float
    lon: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lat = self.lat

        lon = self.lon

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lat": lat,
                "lon": lon,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lat = d.pop("lat")

        lon = d.pop("lon")

        get_saved_search_run_companies_response_200_output_companies_item_company_num_matching_locations_type_0_matched_offices_item_location_type_0_coordinates_type_0 = cls(
            lat=lat,
            lon=lon,
        )

        get_saved_search_run_companies_response_200_output_companies_item_company_num_matching_locations_type_0_matched_offices_item_location_type_0_coordinates_type_0.additional_properties = d
        return get_saved_search_run_companies_response_200_output_companies_item_company_num_matching_locations_type_0_matched_offices_item_location_type_0_coordinates_type_0

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
