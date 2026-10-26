from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubOrgContributorsBody")


@_attrs_define
class GithubOrgContributorsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        org_url (str): Organization to scan. Accepts a URL (for example 'https://github.com/tenstorrent' or
            'https://github.com/orgs/tenstorrent') or a login.
        max_repos (int | None | Unset): How many public repositories to scan, most recently pushed first. Defaults to
            100. Forks are skipped and do not count toward this limit.
    """

    api_key: str
    org_url: str
    max_repos: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        org_url = self.org_url

        max_repos: int | None | Unset
        if isinstance(self.max_repos, Unset):
            max_repos = UNSET
        else:
            max_repos = self.max_repos

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "orgUrl": org_url,
            }
        )
        if max_repos is not UNSET:
            field_dict["maxRepos"] = max_repos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        org_url = d.pop("orgUrl")

        def _parse_max_repos(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_repos = _parse_max_repos(d.pop("maxRepos", UNSET))

        github_org_contributors_body = cls(
            api_key=api_key,
            org_url=org_url,
            max_repos=max_repos,
        )

        github_org_contributors_body.additional_properties = d
        return github_org_contributors_body

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
