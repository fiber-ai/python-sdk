from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_any_of_type_0_item_type_5_location_type import CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5LocationType
from ..models.create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_any_of_type_0_item_type_5_rule import CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5Rule
from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_any_of_type_0_item_type_5_range_type_0 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5RangeType0
  from ..models.create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_any_of_type_0_item_type_5_range_type_1 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5RangeType1





T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5")



@_attrs_define
class CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5:
    """ 
        Attributes:
            rule (CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5Rule):
            location_type
                (CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5LocationType):
            range_ (Union['CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5R
                angeType0',
                'CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5RangeType1']):
     """

    rule: CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5Rule
    location_type: CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5LocationType
    range_: Union['CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5RangeType0', 'CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5RangeType1']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_any_of_type_0_item_type_5_range_type_0 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5RangeType0
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_any_of_type_0_item_type_5_range_type_1 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5RangeType1
        rule = self.rule.value

        location_type = self.location_type.value

        range_: dict[str, Any]
        if isinstance(self.range_, CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5RangeType0):
            range_ = self.range_.to_dict()
        else:
            range_ = self.range_.to_dict()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "rule": rule,
            "locationType": location_type,
            "range": range_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_any_of_type_0_item_type_5_range_type_0 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5RangeType0
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_any_of_type_0_item_type_5_range_type_1 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5RangeType1
        d = dict(src_dict)
        rule = CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5Rule(d.pop("rule"))




        location_type = CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5LocationType(d.pop("locationType"))




        def _parse_range_(data: object) -> Union['CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5RangeType0', 'CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5RangeType1']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                range_type_0 = CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5RangeType0.from_dict(data)



                return range_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            range_type_1 = CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingStatsType0AnyOfType0ItemType5RangeType1.from_dict(data)



            return range_type_1

        range_ = _parse_range_(d.pop("range"))


        create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_any_of_type_0_item_type_5 = cls(
            rule=rule,
            location_type=location_type,
            range_=range_,
        )


        create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_any_of_type_0_item_type_5.additional_properties = d
        return create_saved_search_body_search_params_type_1_company_search_params_job_posting_stats_type_0_any_of_type_0_item_type_5

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
