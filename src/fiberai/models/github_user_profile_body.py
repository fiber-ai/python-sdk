from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GithubUserProfileBody")


@_attrs_define
class GithubUserProfileBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        profile_url (str): User to look up. Accepts a profile URL (for example 'https://github.com/torvalds') or a
            username. Organization and bot accounts are not returned.
    """

    api_key: str
    profile_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        profile_url = self.profile_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "profileUrl": profile_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        profile_url = d.pop("profileUrl")

        github_user_profile_body = cls(
            api_key=api_key,
            profile_url=profile_url,
        )

        github_user_profile_body.additional_properties = d
        return github_user_profile_body

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
