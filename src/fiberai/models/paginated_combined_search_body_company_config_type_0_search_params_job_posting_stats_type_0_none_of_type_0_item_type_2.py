from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.paginated_combined_search_body_company_config_type_0_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2_rule import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2Rule,
)
from ..models.paginated_combined_search_body_company_config_type_0_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2_seniority import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2Seniority,
)

if TYPE_CHECKING:
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2_range_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2_range_type_1 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType1,
    )


T = TypeVar(
    "T", bound="PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2"
)


@_attrs_define
class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2:
    """
    Attributes:
        rule (PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2Rule):
        seniority
            (PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2Seniority):
        range_
            (PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType0 |
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType1):
    """

    rule: PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2Rule
    seniority: (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2Seniority
    )
    range_: (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType0
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType1
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2_range_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType0,  # noqa: PLC0415
        )

        rule = self.rule.value

        seniority = self.seniority.value

        range_: dict[str, Any]
        if isinstance(
            self.range_,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType0,
        ):
            range_ = self.range_.to_dict()
        else:
            range_ = self.range_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule": rule,
                "seniority": seniority,
                "range": range_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2_range_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType0,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2_range_type_1 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType1,  # noqa: PLC0415
        )

        d = dict(src_dict)
        rule = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2Rule(
            d.pop("rule")
        )

        seniority = (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2Seniority(
                d.pop("seniority")
            )
        )

        def _parse_range_(
            data: object,
        ) -> (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType0
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType1
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                range_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType0.from_dict(
                    data
                )

                return range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            range_type_1 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType1.from_dict(
                data
            )

            return range_type_1

        range_ = _parse_range_(d.pop("range"))

        paginated_combined_search_body_company_config_type_0_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2 = cls(
            rule=rule,
            seniority=seniority,
            range_=range_,
        )

        paginated_combined_search_body_company_config_type_0_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2.additional_properties = d
        return paginated_combined_search_body_company_config_type_0_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2

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
