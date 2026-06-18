from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2_rule import (
    CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2Rule,
)
from ..models.create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2_seniority import (
    CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2Seniority,
)

if TYPE_CHECKING:
    from ..models.create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2_range_type_0 import (
        CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType0,
    )
    from ..models.create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2_range_type_1 import (
        CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType1,
    )


T = TypeVar(
    "T", bound="CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2"
)


@_attrs_define
class CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2:
    """
    Attributes:
        rule (CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2Rule):
        seniority
            (CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2Seniority):
        range_
            (CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType0 |
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType1):
    """

    rule: CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2Rule
    seniority: (
        CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2Seniority
    )
    range_: (
        CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType0
        | CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType1
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2_range_type_0 import (
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType0,
        )

        rule = self.rule.value

        seniority = self.seniority.value

        range_: dict[str, Any]
        if isinstance(
            self.range_,
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType0,
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
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2_range_type_0 import (
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType0,
        )
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2_range_type_1 import (
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType1,
        )

        d = dict(src_dict)
        rule = CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2Rule(
            d.pop("rule")
        )

        seniority = (
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2Seniority(
                d.pop("seniority")
            )
        )

        def _parse_range_(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType0
            | CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType1
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                range_type_0 = CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType0.from_dict(
                    data
                )

                return range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            range_type_1 = CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0NoneOfType0ItemType2RangeType1.from_dict(
                data
            )

            return range_type_1

        range_ = _parse_range_(d.pop("range"))

        create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2 = cls(
            rule=rule,
            seniority=seniority,
            range_=range_,
        )

        create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2.additional_properties = d
        return create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_none_of_type_0_item_type_2

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
