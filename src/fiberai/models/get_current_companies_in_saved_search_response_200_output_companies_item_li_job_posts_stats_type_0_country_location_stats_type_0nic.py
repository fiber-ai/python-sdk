from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0CountryLocationStatsType0NIC",
)


@_attrs_define
class GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0CountryLocationStatsType0NIC:
    """
    Attributes:
        count (float):
        fraction (float):
    """

    count: float
    fraction: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        fraction = self.fraction

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "fraction": fraction,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        fraction = d.pop("fraction")

        get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_country_location_stats_type_0nic = cls(
            count=count,
            fraction=fraction,
        )

        get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_country_location_stats_type_0nic.additional_properties = d
        return get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_country_location_stats_type_0nic

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
