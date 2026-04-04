from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.add_profiles_to_list_body_profiles_item import AddProfilesToListBodyProfilesItem


T = TypeVar("T", bound="AddProfilesToListBody")


@_attrs_define
class AddProfilesToListBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        job_change_list_id (str): The job change list id.
        profiles (list[AddProfilesToListBodyProfilesItem]):
    """

    api_key: str
    job_change_list_id: str
    profiles: list[AddProfilesToListBodyProfilesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        job_change_list_id = self.job_change_list_id

        profiles = []
        for profiles_item_data in self.profiles:
            profiles_item = profiles_item_data.to_dict()
            profiles.append(profiles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "jobChangeListId": job_change_list_id,
                "profiles": profiles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_profiles_to_list_body_profiles_item import AddProfilesToListBodyProfilesItem

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        job_change_list_id = d.pop("jobChangeListId")

        profiles = []
        _profiles = d.pop("profiles")
        for profiles_item_data in _profiles:
            profiles_item = AddProfilesToListBodyProfilesItem.from_dict(profiles_item_data)

            profiles.append(profiles_item)

        add_profiles_to_list_body = cls(
            api_key=api_key,
            job_change_list_id=job_change_list_id,
            profiles=profiles,
        )

        add_profiles_to_list_body.additional_properties = d
        return add_profiles_to_list_body

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
