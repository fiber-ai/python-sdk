from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_org_contributors_poll_response_200_output_skipped_repos_item_reason import (
    GithubOrgContributorsPollResponse200OutputSkippedReposItemReason,
)

T = TypeVar("T", bound="GithubOrgContributorsPollResponse200OutputSkippedReposItem")


@_attrs_define
class GithubOrgContributorsPollResponse200OutputSkippedReposItem:
    """
    Attributes:
        repo_url (str): Repository URL.
        reason (GithubOrgContributorsPollResponse200OutputSkippedReposItemReason): Why this repository was not included:
            too_large (too many contributors for GitHub to list), not_found (the repository is gone), or scan_failed (GitHub
            could not be reached).
    """

    repo_url: str
    reason: GithubOrgContributorsPollResponse200OutputSkippedReposItemReason
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repo_url = self.repo_url

        reason = self.reason.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repoUrl": repo_url,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repo_url = d.pop("repoUrl")

        reason = GithubOrgContributorsPollResponse200OutputSkippedReposItemReason(d.pop("reason"))

        github_org_contributors_poll_response_200_output_skipped_repos_item = cls(
            repo_url=repo_url,
            reason=reason,
        )

        github_org_contributors_poll_response_200_output_skipped_repos_item.additional_properties = d
        return github_org_contributors_poll_response_200_output_skipped_repos_item

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
