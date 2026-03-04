from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sync_combined_search_body_company_params_employee_trends_type_0_obeys_none_type_0_item_count_criteria_type_2_type import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType2Type
from typing import cast

if TYPE_CHECKING:
  from ..models.sync_combined_search_body_company_params_employee_trends_type_0_obeys_none_type_0_item_count_criteria_type_2_range import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType2Range





T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType2")



@_attrs_define
class SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType2:
    """ 
        Attributes:
            type_ (SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType2Type):
            range_ (SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType2Range):
     """

    type_: SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType2Type
    range_: 'SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType2Range'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_combined_search_body_company_params_employee_trends_type_0_obeys_none_type_0_item_count_criteria_type_2_range import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType2Range
        type_ = self.type_.value

        range_ = self.range_.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "range": range_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_combined_search_body_company_params_employee_trends_type_0_obeys_none_type_0_item_count_criteria_type_2_range import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType2Range
        d = dict(src_dict)
        type_ = SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType2Type(d.pop("type"))




        range_ = SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType2Range.from_dict(d.pop("range"))




        sync_combined_search_body_company_params_employee_trends_type_0_obeys_none_type_0_item_count_criteria_type_2 = cls(
            type_=type_,
            range_=range_,
        )


        sync_combined_search_body_company_params_employee_trends_type_0_obeys_none_type_0_item_count_criteria_type_2.additional_properties = d
        return sync_combined_search_body_company_params_employee_trends_type_0_obeys_none_type_0_item_count_criteria_type_2

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
