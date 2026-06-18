from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSavedSearchRunProfilesResponse200OutputProfilesItemProfileCoursesType0Item")


@_attrs_define
class GetSavedSearchRunProfilesResponse200OutputProfilesItemProfileCoursesType0Item:
    """
    Attributes:
        title (None | str | Unset):
        course_number (None | str | Unset):
        association (None | Unset):
    """

    title: None | str | Unset = UNSET
    course_number: None | str | Unset = UNSET
    association: None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        course_number: None | str | Unset
        if isinstance(self.course_number, Unset):
            course_number = UNSET
        else:
            course_number = self.course_number

        association = self.association

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if course_number is not UNSET:
            field_dict["course_number"] = course_number
        if association is not UNSET:
            field_dict["association"] = association

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_course_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        course_number = _parse_course_number(d.pop("course_number", UNSET))

        association = d.pop("association", UNSET)

        get_saved_search_run_profiles_response_200_output_profiles_item_profile_courses_type_0_item = cls(
            title=title,
            course_number=course_number,
            association=association,
        )

        get_saved_search_run_profiles_response_200_output_profiles_item_profile_courses_type_0_item.additional_properties = d
        return get_saved_search_run_profiles_response_200_output_profiles_item_profile_courses_type_0_item

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
