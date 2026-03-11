from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0_all_of_type_0_item_type_1_range_type_1_type import (
    SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType1RangeType1Type,
)

if TYPE_CHECKING:
    from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0_all_of_type_0_item_type_1_range_type_1_range_in_hundredths import (
        SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType1RangeType1RangeInHundredths,
    )


T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType1RangeType1")


@_attrs_define
class SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType1RangeType1:
    """
    Attributes:
        type_ (SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType1RangeType1Type):
        range_in_hundredths
            (SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType1RangeType1RangeInHundredths):
    """

    type_: SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType1RangeType1Type
    range_in_hundredths: (
        SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType1RangeType1RangeInHundredths
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        range_in_hundredths = self.range_in_hundredths.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "rangeInHundredths": range_in_hundredths,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0_all_of_type_0_item_type_1_range_type_1_range_in_hundredths import (
            SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType1RangeType1RangeInHundredths,
        )

        d = dict(src_dict)
        type_ = SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType1RangeType1Type(d.pop("type"))

        range_in_hundredths = SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType1RangeType1RangeInHundredths.from_dict(
            d.pop("rangeInHundredths")
        )

        sync_combined_search_body_company_params_job_posting_stats_type_0_all_of_type_0_item_type_1_range_type_1 = cls(
            type_=type_,
            range_in_hundredths=range_in_hundredths,
        )

        sync_combined_search_body_company_params_job_posting_stats_type_0_all_of_type_0_item_type_1_range_type_1.additional_properties = d
        return sync_combined_search_body_company_params_job_posting_stats_type_0_all_of_type_0_item_type_1_range_type_1

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
