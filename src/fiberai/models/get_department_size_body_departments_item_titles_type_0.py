from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_department_size_body_departments_item_titles_type_0_type import (
    GetDepartmentSizeBodyDepartmentsItemTitlesType0Type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_department_size_body_departments_item_titles_type_0_exclude import (
        GetDepartmentSizeBodyDepartmentsItemTitlesType0Exclude,
    )
    from ..models.get_department_size_body_departments_item_titles_type_0_include import (
        GetDepartmentSizeBodyDepartmentsItemTitlesType0Include,
    )


T = TypeVar("T", bound="GetDepartmentSizeBodyDepartmentsItemTitlesType0")


@_attrs_define
class GetDepartmentSizeBodyDepartmentsItemTitlesType0:
    """
    Attributes:
        type_ (GetDepartmentSizeBodyDepartmentsItemTitlesType0Type): Match employees against a job-title list you
            provide.
        include (GetDepartmentSizeBodyDepartmentsItemTitlesType0Include): Title filter for including employees in this
            department.
        exclude (GetDepartmentSizeBodyDepartmentsItemTitlesType0Exclude | Unset): Optional title filter for excluding
            employees from this department.
    """

    type_: GetDepartmentSizeBodyDepartmentsItemTitlesType0Type
    include: GetDepartmentSizeBodyDepartmentsItemTitlesType0Include
    exclude: GetDepartmentSizeBodyDepartmentsItemTitlesType0Exclude | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        include = self.include.to_dict()

        exclude: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exclude, Unset):
            exclude = self.exclude.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "include": include,
            }
        )
        if exclude is not UNSET:
            field_dict["exclude"] = exclude

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_department_size_body_departments_item_titles_type_0_exclude import (
            GetDepartmentSizeBodyDepartmentsItemTitlesType0Exclude,  # noqa: PLC0415
        )
        from ..models.get_department_size_body_departments_item_titles_type_0_include import (
            GetDepartmentSizeBodyDepartmentsItemTitlesType0Include,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = GetDepartmentSizeBodyDepartmentsItemTitlesType0Type(d.pop("type"))

        include = GetDepartmentSizeBodyDepartmentsItemTitlesType0Include.from_dict(d.pop("include"))

        _exclude = d.pop("exclude", UNSET)
        exclude: GetDepartmentSizeBodyDepartmentsItemTitlesType0Exclude | Unset
        if isinstance(_exclude, Unset):
            exclude = UNSET
        else:
            exclude = GetDepartmentSizeBodyDepartmentsItemTitlesType0Exclude.from_dict(_exclude)

        get_department_size_body_departments_item_titles_type_0 = cls(
            type_=type_,
            include=include,
            exclude=exclude,
        )

        get_department_size_body_departments_item_titles_type_0.additional_properties = d
        return get_department_size_body_departments_item_titles_type_0

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
