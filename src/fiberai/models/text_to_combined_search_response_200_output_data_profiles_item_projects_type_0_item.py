from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextToCombinedSearchResponse200OutputDataProfilesItemProjectsType0Item")


@_attrs_define
class TextToCombinedSearchResponse200OutputDataProfilesItemProjectsType0Item:
    """
    Attributes:
        project_id (None | str | Unset):
        project_title (None | str | Unset):
        project_url (None | str | Unset):
        project_summary (None | str | Unset):
        is_current (bool | None | Unset):
        start_date (None | str | Unset):
        end_date (None | str | Unset):
    """

    project_id: None | str | Unset = UNSET
    project_title: None | str | Unset = UNSET
    project_url: None | str | Unset = UNSET
    project_summary: None | str | Unset = UNSET
    is_current: bool | None | Unset = UNSET
    start_date: None | str | Unset = UNSET
    end_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        project_title: None | str | Unset
        if isinstance(self.project_title, Unset):
            project_title = UNSET
        else:
            project_title = self.project_title

        project_url: None | str | Unset
        if isinstance(self.project_url, Unset):
            project_url = UNSET
        else:
            project_url = self.project_url

        project_summary: None | str | Unset
        if isinstance(self.project_summary, Unset):
            project_summary = UNSET
        else:
            project_summary = self.project_summary

        is_current: bool | None | Unset
        if isinstance(self.is_current, Unset):
            is_current = UNSET
        else:
            is_current = self.is_current

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if project_title is not UNSET:
            field_dict["project_title"] = project_title
        if project_url is not UNSET:
            field_dict["project_url"] = project_url
        if project_summary is not UNSET:
            field_dict["project_summary"] = project_summary
        if is_current is not UNSET:
            field_dict["is_current"] = is_current
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_project_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_title = _parse_project_title(d.pop("project_title", UNSET))

        def _parse_project_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_url = _parse_project_url(d.pop("project_url", UNSET))

        def _parse_project_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_summary = _parse_project_summary(d.pop("project_summary", UNSET))

        def _parse_is_current(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_current = _parse_is_current(d.pop("is_current", UNSET))

        def _parse_start_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        text_to_combined_search_response_200_output_data_profiles_item_projects_type_0_item = cls(
            project_id=project_id,
            project_title=project_title,
            project_url=project_url,
            project_summary=project_summary,
            is_current=is_current,
            start_date=start_date,
            end_date=end_date,
        )

        text_to_combined_search_response_200_output_data_profiles_item_projects_type_0_item.additional_properties = d
        return text_to_combined_search_response_200_output_data_profiles_item_projects_type_0_item

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
