from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextToCombinedSearchBodyProfileConfig")


@_attrs_define
class TextToCombinedSearchBodyProfileConfig:
    """
    Attributes:
        page_size (float): The number of profiles to return per page.
        exclusion_list_i_ds (list[str] | None | Unset): The IDs of prospect exclusion lists to filter out matching
            people.
        profile_cursor (None | str | Unset):
        get_detailed_education (bool | None | Unset): Whether to include deep details about each educational item, like
            the school's LinkedIn URL, website, location, etc. That'll be put in the detailedEducation array. This slows
            down the API call, so only enable this if you need it. Default: False.
        get_detailed_work_experience (bool | None | Unset): Whether to include deep details about each work experience
            item, like the company's LinkedIn URL, website, location, etc. That'll be put in the detailedWorkExperience
            array. This slows down the API call, so only enable this if you need it. Default: False.
    """

    page_size: float
    exclusion_list_i_ds: list[str] | None | Unset = UNSET
    profile_cursor: None | str | Unset = UNSET
    get_detailed_education: bool | None | Unset = False
    get_detailed_work_experience: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_size = self.page_size

        exclusion_list_i_ds: list[str] | None | Unset
        if isinstance(self.exclusion_list_i_ds, Unset):
            exclusion_list_i_ds = UNSET
        elif isinstance(self.exclusion_list_i_ds, list):
            exclusion_list_i_ds = self.exclusion_list_i_ds

        else:
            exclusion_list_i_ds = self.exclusion_list_i_ds

        profile_cursor: None | str | Unset
        if isinstance(self.profile_cursor, Unset):
            profile_cursor = UNSET
        else:
            profile_cursor = self.profile_cursor

        get_detailed_education: bool | None | Unset
        if isinstance(self.get_detailed_education, Unset):
            get_detailed_education = UNSET
        else:
            get_detailed_education = self.get_detailed_education

        get_detailed_work_experience: bool | None | Unset
        if isinstance(self.get_detailed_work_experience, Unset):
            get_detailed_work_experience = UNSET
        else:
            get_detailed_work_experience = self.get_detailed_work_experience

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pageSize": page_size,
            }
        )
        if exclusion_list_i_ds is not UNSET:
            field_dict["exclusionListIDs"] = exclusion_list_i_ds
        if profile_cursor is not UNSET:
            field_dict["profileCursor"] = profile_cursor
        if get_detailed_education is not UNSET:
            field_dict["getDetailedEducation"] = get_detailed_education
        if get_detailed_work_experience is not UNSET:
            field_dict["getDetailedWorkExperience"] = get_detailed_work_experience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_size = d.pop("pageSize")

        def _parse_exclusion_list_i_ds(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclusion_list_i_ds_type_0 = cast(list[str], data)

                return exclusion_list_i_ds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exclusion_list_i_ds = _parse_exclusion_list_i_ds(d.pop("exclusionListIDs", UNSET))

        def _parse_profile_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_cursor = _parse_profile_cursor(d.pop("profileCursor", UNSET))

        def _parse_get_detailed_education(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        get_detailed_education = _parse_get_detailed_education(d.pop("getDetailedEducation", UNSET))

        def _parse_get_detailed_work_experience(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        get_detailed_work_experience = _parse_get_detailed_work_experience(d.pop("getDetailedWorkExperience", UNSET))

        text_to_combined_search_body_profile_config = cls(
            page_size=page_size,
            exclusion_list_i_ds=exclusion_list_i_ds,
            profile_cursor=profile_cursor,
            get_detailed_education=get_detailed_education,
            get_detailed_work_experience=get_detailed_work_experience,
        )

        text_to_combined_search_body_profile_config.additional_properties = d
        return text_to_combined_search_body_profile_config

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
