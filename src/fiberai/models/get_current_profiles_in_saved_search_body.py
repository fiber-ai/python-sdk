from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_current_profiles_in_saved_search_body_statuses_type_0_item import (
    GetCurrentProfilesInSavedSearchBodyStatusesType0Item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCurrentProfilesInSavedSearchBody")


@_attrs_define
class GetCurrentProfilesInSavedSearchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        saved_search_id (str): The ID of the saved search
        statuses (list[GetCurrentProfilesInSavedSearchBodyStatusesType0Item] | None | Unset): The statuses of the
            profiles. This is optional and if not provided, all current profiles will be returned.
        cursor (None | str | Unset): The cursor to start from
        page_size (int | Unset): The number of profiles to return Default: 25.
    """

    api_key: str
    saved_search_id: str
    statuses: list[GetCurrentProfilesInSavedSearchBodyStatusesType0Item] | None | Unset = UNSET
    cursor: None | str | Unset = UNSET
    page_size: int | Unset = 25
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        saved_search_id = self.saved_search_id

        statuses: list[str] | None | Unset
        if isinstance(self.statuses, Unset):
            statuses = UNSET
        elif isinstance(self.statuses, list):
            statuses = []
            for statuses_type_0_item_data in self.statuses:
                statuses_type_0_item = statuses_type_0_item_data.value
                statuses.append(statuses_type_0_item)

        else:
            statuses = self.statuses

        cursor: None | str | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "savedSearchId": saved_search_id,
            }
        )
        if statuses is not UNSET:
            field_dict["statuses"] = statuses
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        saved_search_id = d.pop("savedSearchId")

        def _parse_statuses(data: object) -> list[GetCurrentProfilesInSavedSearchBodyStatusesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                statuses_type_0 = []
                _statuses_type_0 = data
                for statuses_type_0_item_data in _statuses_type_0:
                    statuses_type_0_item = GetCurrentProfilesInSavedSearchBodyStatusesType0Item(
                        statuses_type_0_item_data
                    )

                    statuses_type_0.append(statuses_type_0_item)

                return statuses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GetCurrentProfilesInSavedSearchBodyStatusesType0Item] | None | Unset, data)

        statuses = _parse_statuses(d.pop("statuses", UNSET))

        def _parse_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        page_size = d.pop("pageSize", UNSET)

        get_current_profiles_in_saved_search_body = cls(
            api_key=api_key,
            saved_search_id=saved_search_id,
            statuses=statuses,
            cursor=cursor,
            page_size=page_size,
        )

        get_current_profiles_in_saved_search_body.additional_properties = d
        return get_current_profiles_in_saved_search_body

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
