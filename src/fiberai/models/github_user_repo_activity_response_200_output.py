from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_user_repo_activity_response_200_output_unavailable_sections_item import (
    GithubUserRepoActivityResponse200OutputUnavailableSectionsItem,
)

if TYPE_CHECKING:
    from ..models.github_user_repo_activity_response_200_output_commits_item import (
        GithubUserRepoActivityResponse200OutputCommitsItem,
    )
    from ..models.github_user_repo_activity_response_200_output_issues_item import (
        GithubUserRepoActivityResponse200OutputIssuesItem,
    )
    from ..models.github_user_repo_activity_response_200_output_pull_requests_item import (
        GithubUserRepoActivityResponse200OutputPullRequestsItem,
    )


T = TypeVar("T", bound="GithubUserRepoActivityResponse200Output")


@_attrs_define
class GithubUserRepoActivityResponse200Output:
    """
    Attributes:
        commits (list[GithubUserRepoActivityResponse200OutputCommitsItem]): Recent commits by this user in the
            repository.
        pull_requests (list[GithubUserRepoActivityResponse200OutputPullRequestsItem]): Recent pull requests opened by
            this user in the repository.
        issues (list[GithubUserRepoActivityResponse200OutputIssuesItem]): Recent issues opened by this user in the
            repository.
        unavailable_sections (list[GithubUserRepoActivityResponse200OutputUnavailableSectionsItem]): Lists that could
            not be loaded. The other lists are still returned.
    """

    commits: list[GithubUserRepoActivityResponse200OutputCommitsItem]
    pull_requests: list[GithubUserRepoActivityResponse200OutputPullRequestsItem]
    issues: list[GithubUserRepoActivityResponse200OutputIssuesItem]
    unavailable_sections: list[GithubUserRepoActivityResponse200OutputUnavailableSectionsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commits = []
        for commits_item_data in self.commits:
            commits_item = commits_item_data.to_dict()
            commits.append(commits_item)

        pull_requests = []
        for pull_requests_item_data in self.pull_requests:
            pull_requests_item = pull_requests_item_data.to_dict()
            pull_requests.append(pull_requests_item)

        issues = []
        for issues_item_data in self.issues:
            issues_item = issues_item_data.to_dict()
            issues.append(issues_item)

        unavailable_sections = []
        for unavailable_sections_item_data in self.unavailable_sections:
            unavailable_sections_item = unavailable_sections_item_data.value
            unavailable_sections.append(unavailable_sections_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commits": commits,
                "pullRequests": pull_requests,
                "issues": issues,
                "unavailableSections": unavailable_sections,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_user_repo_activity_response_200_output_commits_item import (
            GithubUserRepoActivityResponse200OutputCommitsItem,  # noqa: PLC0415
        )
        from ..models.github_user_repo_activity_response_200_output_issues_item import (
            GithubUserRepoActivityResponse200OutputIssuesItem,  # noqa: PLC0415
        )
        from ..models.github_user_repo_activity_response_200_output_pull_requests_item import (
            GithubUserRepoActivityResponse200OutputPullRequestsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        commits = []
        _commits = d.pop("commits")
        for commits_item_data in _commits:
            commits_item = GithubUserRepoActivityResponse200OutputCommitsItem.from_dict(commits_item_data)

            commits.append(commits_item)

        pull_requests = []
        _pull_requests = d.pop("pullRequests")
        for pull_requests_item_data in _pull_requests:
            pull_requests_item = GithubUserRepoActivityResponse200OutputPullRequestsItem.from_dict(
                pull_requests_item_data
            )

            pull_requests.append(pull_requests_item)

        issues = []
        _issues = d.pop("issues")
        for issues_item_data in _issues:
            issues_item = GithubUserRepoActivityResponse200OutputIssuesItem.from_dict(issues_item_data)

            issues.append(issues_item)

        unavailable_sections = []
        _unavailable_sections = d.pop("unavailableSections")
        for unavailable_sections_item_data in _unavailable_sections:
            unavailable_sections_item = GithubUserRepoActivityResponse200OutputUnavailableSectionsItem(
                unavailable_sections_item_data
            )

            unavailable_sections.append(unavailable_sections_item)

        github_user_repo_activity_response_200_output = cls(
            commits=commits,
            pull_requests=pull_requests,
            issues=issues,
            unavailable_sections=unavailable_sections,
        )

        github_user_repo_activity_response_200_output.additional_properties = d
        return github_user_repo_activity_response_200_output

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
