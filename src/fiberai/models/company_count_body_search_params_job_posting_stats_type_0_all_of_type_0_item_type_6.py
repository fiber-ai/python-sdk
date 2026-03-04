from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.company_count_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_6_industry import CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6Industry
from ..models.company_count_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_6_rule import CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6Rule
from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.company_count_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_6_range_type_1 import CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6RangeType1
  from ..models.company_count_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_6_range_type_0 import CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6RangeType0





T = TypeVar("T", bound="CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6")



@_attrs_define
class CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6:
    """ 
        Attributes:
            rule (CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6Rule):
            industry (CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6Industry):
            range_ (Union['CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6RangeType0',
                'CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6RangeType1']):
     """

    rule: CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6Rule
    industry: CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6Industry
    range_: Union['CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6RangeType0', 'CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6RangeType1']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.company_count_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_6_range_type_1 import CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6RangeType1
        from ..models.company_count_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_6_range_type_0 import CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6RangeType0
        rule = self.rule.value

        industry = self.industry.value

        range_: dict[str, Any]
        if isinstance(self.range_, CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6RangeType0):
            range_ = self.range_.to_dict()
        else:
            range_ = self.range_.to_dict()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "rule": rule,
            "industry": industry,
            "range": range_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_count_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_6_range_type_1 import CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6RangeType1
        from ..models.company_count_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_6_range_type_0 import CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6RangeType0
        d = dict(src_dict)
        rule = CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6Rule(d.pop("rule"))




        industry = CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6Industry(d.pop("industry"))




        def _parse_range_(data: object) -> Union['CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6RangeType0', 'CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6RangeType1']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                range_type_0 = CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6RangeType0.from_dict(data)



                return range_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            range_type_1 = CompanyCountBodySearchParamsJobPostingStatsType0AllOfType0ItemType6RangeType1.from_dict(data)



            return range_type_1

        range_ = _parse_range_(d.pop("range"))


        company_count_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_6 = cls(
            rule=rule,
            industry=industry,
            range_=range_,
        )


        company_count_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_6.additional_properties = d
        return company_count_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_6

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
