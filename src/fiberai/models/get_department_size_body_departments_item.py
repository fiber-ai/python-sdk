from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_department_size_body_departments_item_titles_type_0 import (
        GetDepartmentSizeBodyDepartmentsItemTitlesType0,
    )


T = TypeVar("T", bound="GetDepartmentSizeBodyDepartmentsItem")


@_attrs_define
class GetDepartmentSizeBodyDepartmentsItem:
    """
    Attributes:
        name (str): Your label for this department (e.g. 'Engineering').
        titles (GetDepartmentSizeBodyDepartmentsItemTitlesType0): How to decide which employees belong to this
            department.
    """

    name: str
    titles: GetDepartmentSizeBodyDepartmentsItemTitlesType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_department_size_body_departments_item_titles_type_0 import (
            GetDepartmentSizeBodyDepartmentsItemTitlesType0,  # noqa: PLC0415
        )

        name = self.name

        titles: dict[str, Any]
        if isinstance(self.titles, GetDepartmentSizeBodyDepartmentsItemTitlesType0):
            titles = self.titles.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "titles": titles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_department_size_body_departments_item_titles_type_0 import (
            GetDepartmentSizeBodyDepartmentsItemTitlesType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_titles(data: object) -> GetDepartmentSizeBodyDepartmentsItemTitlesType0:
            if not isinstance(data, dict):
                raise TypeError()
            titles_type_0 = GetDepartmentSizeBodyDepartmentsItemTitlesType0.from_dict(data)

            return titles_type_0

        titles = _parse_titles(d.pop("titles"))

        get_department_size_body_departments_item = cls(
            name=name,
            titles=titles,
        )

        get_department_size_body_departments_item.additional_properties = d
        return get_department_size_body_departments_item

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
