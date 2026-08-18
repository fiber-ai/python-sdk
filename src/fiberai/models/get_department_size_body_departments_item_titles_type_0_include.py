from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetDepartmentSizeBodyDepartmentsItemTitlesType0Include")


@_attrs_define
class GetDepartmentSizeBodyDepartmentsItemTitlesType0Include:
    """Title filter for including employees in this department.

    Attributes:
        titles (list[str]): Job-title strings that qualify an employee for this department.
    """

    titles: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        titles = self.titles

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "titles": titles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        titles = cast(list[str], d.pop("titles"))

        get_department_size_body_departments_item_titles_type_0_include = cls(
            titles=titles,
        )

        get_department_size_body_departments_item_titles_type_0_include.additional_properties = d
        return get_department_size_body_departments_item_titles_type_0_include

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
