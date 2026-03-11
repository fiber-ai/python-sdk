from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_search_body_search_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1_type import (
    CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Type,
)

if TYPE_CHECKING:
    from ..models.company_search_body_search_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1_change import (
        CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Change,
    )


T = TypeVar("T", bound="CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1")


@_attrs_define
class CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1:
    """
    Attributes:
        type_ (CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Type):
        change (CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Change):
        window_look_back_months (float):
    """

    type_: CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Type
    change: CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Change
    window_look_back_months: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        change = self.change.to_dict()

        window_look_back_months = self.window_look_back_months

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "change": change,
                "windowLookBackMonths": window_look_back_months,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_search_body_search_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1_change import (
            CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Change,
        )

        d = dict(src_dict)
        type_ = CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Type(d.pop("type"))

        change = CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1Change.from_dict(
            d.pop("change")
        )

        window_look_back_months = d.pop("windowLookBackMonths")

        company_search_body_search_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1 = cls(
            type_=type_,
            change=change,
            window_look_back_months=window_look_back_months,
        )

        company_search_body_search_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1.additional_properties = d
        return company_search_body_search_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1

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
