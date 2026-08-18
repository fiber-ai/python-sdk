from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetDepartmentSizeResponse200OutputDepartmentsItem")


@_attrs_define
class GetDepartmentSizeResponse200OutputDepartmentsItem:
    """
    Attributes:
        name (str): The department label you supplied
        count (float): Number of current employees matching this department
        percent_of_headcount (float): Department count as a percentage of total company headcount (0–100, rounded to 2
            decimal places). Because departments are counted independently, values across departments need not sum to 100.
            Due to approximation above 40K employees, this can slightly exceed 100.
    """

    name: str
    count: float
    percent_of_headcount: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        count = self.count

        percent_of_headcount = self.percent_of_headcount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "count": count,
                "percentOfHeadcount": percent_of_headcount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        count = d.pop("count")

        percent_of_headcount = d.pop("percentOfHeadcount")

        get_department_size_response_200_output_departments_item = cls(
            name=name,
            count=count,
            percent_of_headcount=percent_of_headcount,
        )

        get_department_size_response_200_output_departments_item.additional_properties = d
        return get_department_size_response_200_output_departments_item

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
