from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_4_job_function import CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4JobFunction
from ..models.combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_4_rule import CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4Rule
from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_4_range_type_1 import CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4RangeType1
  from ..models.combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_4_range_type_0 import CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4RangeType0





T = TypeVar("T", bound="CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4")



@_attrs_define
class CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4:
    """ 
        Attributes:
            rule (CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4Rule):
            job_function (CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4JobFunction):
            range_ (Union['CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4RangeType0',
                'CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4RangeType1']):
     """

    rule: CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4Rule
    job_function: CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4JobFunction
    range_: Union['CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4RangeType0', 'CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4RangeType1']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_4_range_type_1 import CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4RangeType1
        from ..models.combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_4_range_type_0 import CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4RangeType0
        rule = self.rule.value

        job_function = self.job_function.value

        range_: dict[str, Any]
        if isinstance(self.range_, CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4RangeType0):
            range_ = self.range_.to_dict()
        else:
            range_ = self.range_.to_dict()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "rule": rule,
            "jobFunction": job_function,
            "range": range_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_4_range_type_1 import CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4RangeType1
        from ..models.combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_4_range_type_0 import CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4RangeType0
        d = dict(src_dict)
        rule = CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4Rule(d.pop("rule"))




        job_function = CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4JobFunction(d.pop("jobFunction"))




        def _parse_range_(data: object) -> Union['CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4RangeType0', 'CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4RangeType1']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                range_type_0 = CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4RangeType0.from_dict(data)



                return range_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            range_type_1 = CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType4RangeType1.from_dict(data)



            return range_type_1

        range_ = _parse_range_(d.pop("range"))


        combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_4 = cls(
            rule=rule,
            job_function=job_function,
            range_=range_,
        )


        combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_4.additional_properties = d
        return combined_search_body_company_params_job_posting_stats_type_0_any_of_type_0_item_type_4

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
