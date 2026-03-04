from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_2_rule import CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2Rule
from ..models.company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_2_seniority import CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2Seniority
from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_2_range_type_1 import CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2RangeType1
  from ..models.company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_2_range_type_0 import CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2RangeType0





T = TypeVar("T", bound="CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2")



@_attrs_define
class CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2:
    """ 
        Attributes:
            rule (CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2Rule):
            seniority (CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2Seniority):
            range_ (Union['CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2RangeType0',
                'CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2RangeType1']):
     """

    rule: CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2Rule
    seniority: CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2Seniority
    range_: Union['CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2RangeType0', 'CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2RangeType1']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_2_range_type_1 import CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2RangeType1
        from ..models.company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_2_range_type_0 import CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2RangeType0
        rule = self.rule.value

        seniority = self.seniority.value

        range_: dict[str, Any]
        if isinstance(self.range_, CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2RangeType0):
            range_ = self.range_.to_dict()
        else:
            range_ = self.range_.to_dict()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "rule": rule,
            "seniority": seniority,
            "range": range_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_2_range_type_1 import CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2RangeType1
        from ..models.company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_2_range_type_0 import CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2RangeType0
        d = dict(src_dict)
        rule = CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2Rule(d.pop("rule"))




        seniority = CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2Seniority(d.pop("seniority"))




        def _parse_range_(data: object) -> Union['CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2RangeType0', 'CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2RangeType1']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                range_type_0 = CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2RangeType0.from_dict(data)



                return range_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            range_type_1 = CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType2RangeType1.from_dict(data)



            return range_type_1

        range_ = _parse_range_(d.pop("range"))


        company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_2 = cls(
            rule=rule,
            seniority=seniority,
            range_=range_,
        )


        company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_2.additional_properties = d
        return company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_2

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
