from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubUserRepoActivityBody")


@_attrs_define
class GithubUserRepoActivityBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        profile_url (str): User whose activity to return. Accepts a profile URL or a username.
        repo_url (str): Repository to look in. Accepts a repository URL or 'owner/repo'.
        limit (int | None | Unset): How many commits, pull requests, and issues to return for each list. Defaults to 10.
            Maximum 30.
    """

    api_key: str
    profile_url: str
    repo_url: str
    limit: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        profile_url = self.profile_url

        repo_url = self.repo_url

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "profileUrl": profile_url,
                "repoUrl": repo_url,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        profile_url = d.pop("profileUrl")

        repo_url = d.pop("repoUrl")

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        github_user_repo_activity_body = cls(
            api_key=api_key,
            profile_url=profile_url,
            repo_url=repo_url,
            limit=limit,
        )

        github_user_repo_activity_body.additional_properties = d
        return github_user_repo_activity_body

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
