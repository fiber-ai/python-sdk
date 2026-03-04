from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1_type import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Type
from typing import cast

if TYPE_CHECKING:
  from ..models.sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1_change import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Change





T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1")



@_attrs_define
class SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1:
    """ 
        Attributes:
            type_ (SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Type):
            change (SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Change):
            window_look_back_months (float):
     """

    type_: SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Type
    change: 'SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Change'
    window_look_back_months: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1_change import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Change
        type_ = self.type_.value

        change = self.change.to_dict()

        window_look_back_months = self.window_look_back_months


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "change": change,
            "windowLookBackMonths": window_look_back_months,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1_change import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Change
        d = dict(src_dict)
        type_ = SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Type(d.pop("type"))




        change = SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Change.from_dict(d.pop("change"))




        window_look_back_months = d.pop("windowLookBackMonths")

        sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1 = cls(
            type_=type_,
            change=change,
            window_look_back_months=window_look_back_months,
        )


        sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1.additional_properties = d
        return sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1

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
