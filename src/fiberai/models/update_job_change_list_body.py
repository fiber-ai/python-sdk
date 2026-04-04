from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateJobChangeListBody")


@_attrs_define
class UpdateJobChangeListBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        job_change_list_id (str): The ID of the job change list.
        new_name (None | str | Unset): The name of the job change list.
        is_active (bool | None | Unset): Make the list active or in-active.
    """

    api_key: str
    job_change_list_id: str
    new_name: None | str | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        job_change_list_id = self.job_change_list_id

        new_name: None | str | Unset
        if isinstance(self.new_name, Unset):
            new_name = UNSET
        else:
            new_name = self.new_name

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "jobChangeListId": job_change_list_id,
            }
        )
        if new_name is not UNSET:
            field_dict["newName"] = new_name
        if is_active is not UNSET:
            field_dict["isActive"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        job_change_list_id = d.pop("jobChangeListId")

        def _parse_new_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_name = _parse_new_name(d.pop("newName", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("isActive", UNSET))

        update_job_change_list_body = cls(
            api_key=api_key,
            job_change_list_id=job_change_list_id,
            new_name=new_name,
            is_active=is_active,
        )

        update_job_change_list_body.additional_properties = d
        return update_job_change_list_body

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
