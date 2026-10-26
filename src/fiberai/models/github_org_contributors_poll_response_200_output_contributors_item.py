from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GithubOrgContributorsPollResponse200OutputContributorsItem")


@_attrs_define
class GithubOrgContributorsPollResponse200OutputContributorsItem:
    """
    Attributes:
        username (str): GitHub username.
        profile_url (str): Profile URL, for example 'https://github.com/torvalds'.
        contribution_count (float): Contributions across the repositories that were scanned.
        repo_count (float): How many scanned repositories this person contributed to.
    """

    username: str
    profile_url: str
    contribution_count: float
    repo_count: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        profile_url = self.profile_url

        contribution_count = self.contribution_count

        repo_count = self.repo_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "profileUrl": profile_url,
                "contributionCount": contribution_count,
                "repoCount": repo_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        profile_url = d.pop("profileUrl")

        contribution_count = d.pop("contributionCount")

        repo_count = d.pop("repoCount")

        github_org_contributors_poll_response_200_output_contributors_item = cls(
            username=username,
            profile_url=profile_url,
            contribution_count=contribution_count,
            repo_count=repo_count,
        )

        github_org_contributors_poll_response_200_output_contributors_item.additional_properties = d
        return github_org_contributors_poll_response_200_output_contributors_item

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
