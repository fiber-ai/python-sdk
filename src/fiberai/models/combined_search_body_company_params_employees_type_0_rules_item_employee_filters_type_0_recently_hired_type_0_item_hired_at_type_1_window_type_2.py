from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.combined_search_body_company_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_1_window_type_2_method import CombinedSearchBodyCompanyParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1WindowType2Method
from ..models.combined_search_body_company_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_1_window_type_2_period import CombinedSearchBodyCompanyParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1WindowType2Period
from ..models.combined_search_body_company_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_1_window_type_2_which import CombinedSearchBodyCompanyParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1WindowType2Which






T = TypeVar("T", bound="CombinedSearchBodyCompanyParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1WindowType2")



@_attrs_define
class CombinedSearchBodyCompanyParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1WindowType2:
    """ 
        Attributes:
            method (CombinedSearchBodyCompanyParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtT
                ype1WindowType2Method):
            which (CombinedSearchBodyCompanyParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtTy
                pe1WindowType2Which):
            period (CombinedSearchBodyCompanyParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtT
                ype1WindowType2Period):
     """

    method: CombinedSearchBodyCompanyParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1WindowType2Method
    which: CombinedSearchBodyCompanyParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1WindowType2Which
    period: CombinedSearchBodyCompanyParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1WindowType2Period
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        which = self.which.value

        period = self.period.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "method": method,
            "which": which,
            "period": period,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = CombinedSearchBodyCompanyParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1WindowType2Method(d.pop("method"))




        which = CombinedSearchBodyCompanyParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1WindowType2Which(d.pop("which"))




        period = CombinedSearchBodyCompanyParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType1WindowType2Period(d.pop("period"))




        combined_search_body_company_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_1_window_type_2 = cls(
            method=method,
            which=which,
            period=period,
        )


        combined_search_body_company_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_1_window_type_2.additional_properties = d
        return combined_search_body_company_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_1_window_type_2

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
