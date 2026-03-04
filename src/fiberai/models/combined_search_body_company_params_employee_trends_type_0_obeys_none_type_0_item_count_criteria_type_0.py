from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.combined_search_body_company_params_employee_trends_type_0_obeys_none_type_0_item_count_criteria_type_0_type import CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType0Type
from typing import cast

if TYPE_CHECKING:
  from ..models.combined_search_body_company_params_employee_trends_type_0_obeys_none_type_0_item_count_criteria_type_0_change import CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType0Change





T = TypeVar("T", bound="CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType0")



@_attrs_define
class CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType0:
    """ 
        Attributes:
            type_ (CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType0Type):
            change (CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType0Change):
            window_look_back_months (float):
     """

    type_: CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType0Type
    change: 'CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType0Change'
    window_look_back_months: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.combined_search_body_company_params_employee_trends_type_0_obeys_none_type_0_item_count_criteria_type_0_change import CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType0Change
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
        from ..models.combined_search_body_company_params_employee_trends_type_0_obeys_none_type_0_item_count_criteria_type_0_change import CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType0Change
        d = dict(src_dict)
        type_ = CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType0Type(d.pop("type"))




        change = CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysNoneType0ItemCountCriteriaType0Change.from_dict(d.pop("change"))




        window_look_back_months = d.pop("windowLookBackMonths")

        combined_search_body_company_params_employee_trends_type_0_obeys_none_type_0_item_count_criteria_type_0 = cls(
            type_=type_,
            change=change,
            window_look_back_months=window_look_back_months,
        )


        combined_search_body_company_params_employee_trends_type_0_obeys_none_type_0_item_count_criteria_type_0.additional_properties = d
        return combined_search_body_company_params_employee_trends_type_0_obeys_none_type_0_item_count_criteria_type_0

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
