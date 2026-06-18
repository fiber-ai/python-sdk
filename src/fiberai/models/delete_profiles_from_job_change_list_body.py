from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteProfilesFromJobChangeListBody")


@_attrs_define
class DeleteProfilesFromJobChangeListBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        profile_ids (list[str]): The IDs of the profiles to remove.
        job_change_list_id (str): The ID of the job change list to remove profiles from.
    """

    api_key: str
    profile_ids: list[str]
    job_change_list_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        profile_ids = self.profile_ids

        job_change_list_id = self.job_change_list_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "profileIds": profile_ids,
                "jobChangeListId": job_change_list_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        profile_ids = cast(list[str], d.pop("profileIds"))

        job_change_list_id = d.pop("jobChangeListId")

        delete_profiles_from_job_change_list_body = cls(
            api_key=api_key,
            profile_ids=profile_ids,
            job_change_list_id=job_change_list_id,
        )

        delete_profiles_from_job_change_list_body.additional_properties = d
        return delete_profiles_from_job_change_list_body

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
