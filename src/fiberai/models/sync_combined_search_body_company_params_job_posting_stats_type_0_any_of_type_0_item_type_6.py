from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_6_industry import (
    SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6Industry,
)
from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_6_rule import (
    SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6Rule,
)

if TYPE_CHECKING:
    from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_6_range_type_0 import (
        SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6RangeType0,
    )
    from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_6_range_type_1 import (
        SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6RangeType1,
    )


T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6")


@_attrs_define
class SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6:
    """
    Attributes:
        rule (SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6Rule):
        industry (SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6Industry):
        range_ (SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6RangeType0 |
            SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6RangeType1):
    """

    rule: SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6Rule
    industry: SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6Industry
    range_: (
        SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6RangeType0
        | SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6RangeType1
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_6_range_type_0 import (
            SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6RangeType0,
        )

        rule = self.rule.value

        industry = self.industry.value

        range_: dict[str, Any]
        if isinstance(
            self.range_, SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6RangeType0
        ):
            range_ = self.range_.to_dict()
        else:
            range_ = self.range_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule": rule,
                "industry": industry,
                "range": range_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_6_range_type_0 import (
            SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6RangeType0,
        )
        from ..models.sync_combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_6_range_type_1 import (
            SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6RangeType1,
        )

        d = dict(src_dict)
        rule = SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6Rule(d.pop("rule"))

        industry = SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6Industry(d.pop("industry"))

        def _parse_range_(
            data: object,
        ) -> (
            SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6RangeType0
            | SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6RangeType1
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                range_type_0 = (
                    SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6RangeType0.from_dict(data)
                )

                return range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            range_type_1 = (
                SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType6RangeType1.from_dict(data)
            )

            return range_type_1

        range_ = _parse_range_(d.pop("range"))

        sync_combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_6 = cls(
            rule=rule,
            industry=industry,
            range_=range_,
        )

        sync_combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_6.additional_properties = d
        return sync_combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_6

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
