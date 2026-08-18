from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_department_size_response_200_output_company import GetDepartmentSizeResponse200OutputCompany
    from ..models.get_department_size_response_200_output_departments_item import (
        GetDepartmentSizeResponse200OutputDepartmentsItem,
    )


T = TypeVar("T", bound="GetDepartmentSizeResponse200Output")


@_attrs_define
class GetDepartmentSizeResponse200Output:
    """
    Attributes:
        company (GetDepartmentSizeResponse200OutputCompany): Company identification details
        headcount (float): Public sources reported total employees at the company (the percentage denominator). Per-
            department counts come from profile matching and may not sum to this value.
        departments (list[GetDepartmentSizeResponse200OutputDepartmentsItem]): One entry per input department, in the
            same order
    """

    company: GetDepartmentSizeResponse200OutputCompany
    headcount: float
    departments: list[GetDepartmentSizeResponse200OutputDepartmentsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company = self.company.to_dict()

        headcount = self.headcount

        departments = []
        for departments_item_data in self.departments:
            departments_item = departments_item_data.to_dict()
            departments.append(departments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company": company,
                "headcount": headcount,
                "departments": departments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_department_size_response_200_output_company import GetDepartmentSizeResponse200OutputCompany
        from ..models.get_department_size_response_200_output_departments_item import (
            GetDepartmentSizeResponse200OutputDepartmentsItem,
        )

        d = dict(src_dict)
        company = GetDepartmentSizeResponse200OutputCompany.from_dict(d.pop("company"))

        headcount = d.pop("headcount")

        departments = []
        _departments = d.pop("departments")
        for departments_item_data in _departments:
            departments_item = GetDepartmentSizeResponse200OutputDepartmentsItem.from_dict(departments_item_data)

            departments.append(departments_item)

        get_department_size_response_200_output = cls(
            company=company,
            headcount=headcount,
            departments=departments,
        )

        get_department_size_response_200_output.additional_properties = d
        return get_department_size_response_200_output

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
