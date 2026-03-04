from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_3_employment_type import CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3EmploymentType
from ..models.company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_3_rule import CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3Rule
from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_3_range_type_1 import CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3RangeType1
  from ..models.company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_3_range_type_0 import CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3RangeType0





T = TypeVar("T", bound="CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3")



@_attrs_define
class CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3:
    """ 
        Attributes:
            rule (CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3Rule):
            employment_type (CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3EmploymentType):
            range_ (Union['CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3RangeType0',
                'CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3RangeType1']):
     """

    rule: CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3Rule
    employment_type: CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3EmploymentType
    range_: Union['CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3RangeType0', 'CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3RangeType1']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_3_range_type_1 import CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3RangeType1
        from ..models.company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_3_range_type_0 import CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3RangeType0
        rule = self.rule.value

        employment_type = self.employment_type.value

        range_: dict[str, Any]
        if isinstance(self.range_, CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3RangeType0):
            range_ = self.range_.to_dict()
        else:
            range_ = self.range_.to_dict()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "rule": rule,
            "employmentType": employment_type,
            "range": range_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_3_range_type_1 import CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3RangeType1
        from ..models.company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_3_range_type_0 import CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3RangeType0
        d = dict(src_dict)
        rule = CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3Rule(d.pop("rule"))




        employment_type = CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3EmploymentType(d.pop("employmentType"))




        def _parse_range_(data: object) -> Union['CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3RangeType0', 'CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3RangeType1']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                range_type_0 = CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3RangeType0.from_dict(data)



                return range_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            range_type_1 = CompanySearchBodySearchParamsJobPostingStatsType0AllOfType0ItemType3RangeType1.from_dict(data)



            return range_type_1

        range_ = _parse_range_(d.pop("range"))


        company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_3 = cls(
            rule=rule,
            employment_type=employment_type,
            range_=range_,
        )


        company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_3.additional_properties = d
        return company_search_body_search_params_job_posting_stats_type_0_all_of_type_0_item_type_3

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
