from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0_all_of_type_0_item_type_3_employment_type import (
    SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3EmploymentType,
)
from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0_all_of_type_0_item_type_3_rule import (
    SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3Rule,
)

if TYPE_CHECKING:
    from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0_all_of_type_0_item_type_3_range_type_0 import (
        SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3RangeType0,
    )
    from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0_all_of_type_0_item_type_3_range_type_1 import (
        SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3RangeType1,
    )


T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3")


@_attrs_define
class SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3:
    """
    Attributes:
        rule (SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3Rule):
        employment_type (SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3EmploymentType):
        range_ (SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3RangeType0 |
            SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3RangeType1):
    """

    rule: SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3Rule
    employment_type: SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3EmploymentType
    range_: (
        SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3RangeType0
        | SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3RangeType1
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0_all_of_type_0_item_type_3_range_type_0 import (
            SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3RangeType0,
        )

        rule = self.rule.value

        employment_type = self.employment_type.value

        range_: dict[str, Any]
        if isinstance(
            self.range_, SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3RangeType0
        ):
            range_ = self.range_.to_dict()
        else:
            range_ = self.range_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule": rule,
                "employmentType": employment_type,
                "range": range_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0_all_of_type_0_item_type_3_range_type_0 import (
            SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3RangeType0,
        )
        from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0_all_of_type_0_item_type_3_range_type_1 import (
            SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3RangeType1,
        )

        d = dict(src_dict)
        rule = SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3Rule(d.pop("rule"))

        employment_type = SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3EmploymentType(
            d.pop("employmentType")
        )

        def _parse_range_(
            data: object,
        ) -> (
            SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3RangeType0
            | SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3RangeType1
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                range_type_0 = (
                    SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3RangeType0.from_dict(data)
                )

                return range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            range_type_1 = (
                SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType3RangeType1.from_dict(data)
            )

            return range_type_1

        range_ = _parse_range_(d.pop("range"))

        sync_combined_search_body_company_params_job_posting_stats_type_0_all_of_type_0_item_type_3 = cls(
            rule=rule,
            employment_type=employment_type,
            range_=range_,
        )

        sync_combined_search_body_company_params_job_posting_stats_type_0_all_of_type_0_item_type_3.additional_properties = d
        return sync_combined_search_body_company_params_job_posting_stats_type_0_all_of_type_0_item_type_3

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
