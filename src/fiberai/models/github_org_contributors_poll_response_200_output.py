from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_org_contributors_poll_response_200_output_status import (
    GithubOrgContributorsPollResponse200OutputStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_org_contributors_poll_response_200_output_contributors_item import (
        GithubOrgContributorsPollResponse200OutputContributorsItem,
    )
    from ..models.github_org_contributors_poll_response_200_output_progress import (
        GithubOrgContributorsPollResponse200OutputProgress,
    )
    from ..models.github_org_contributors_poll_response_200_output_skipped_repos_item import (
        GithubOrgContributorsPollResponse200OutputSkippedReposItem,
    )


T = TypeVar("T", bound="GithubOrgContributorsPollResponse200Output")


@_attrs_define
class GithubOrgContributorsPollResponse200Output:
    """
    Attributes:
        status (GithubOrgContributorsPollResponse200OutputStatus): NOT_STARTED or STARTED while the scan is running.
            DONE when it finished. FAILED when it stopped before finishing.
        progress (GithubOrgContributorsPollResponse200OutputProgress):
        contributors (list[GithubOrgContributorsPollResponse200OutputContributorsItem]): People who contributed to the
            scanned repositories, highest contribution count first. Empty until the scan finishes. Up to 100 per page. Bot
            accounts are omitted.
        skipped_repos (list[GithubOrgContributorsPollResponse200OutputSkippedReposItem]): Repositories that were
            selected but could not be scanned.
        next_page_token (None | str | Unset): Token to retrieve the next page. Pass as `nextPageToken` in the next
            request. Null if no more pages.
    """

    status: GithubOrgContributorsPollResponse200OutputStatus
    progress: GithubOrgContributorsPollResponse200OutputProgress
    contributors: list[GithubOrgContributorsPollResponse200OutputContributorsItem]
    skipped_repos: list[GithubOrgContributorsPollResponse200OutputSkippedReposItem]
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        progress = self.progress.to_dict()

        contributors = []
        for contributors_item_data in self.contributors:
            contributors_item = contributors_item_data.to_dict()
            contributors.append(contributors_item)

        skipped_repos = []
        for skipped_repos_item_data in self.skipped_repos:
            skipped_repos_item = skipped_repos_item_data.to_dict()
            skipped_repos.append(skipped_repos_item)

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "progress": progress,
                "contributors": contributors,
                "skippedRepos": skipped_repos,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_org_contributors_poll_response_200_output_contributors_item import (
            GithubOrgContributorsPollResponse200OutputContributorsItem,  # noqa: PLC0415
        )
        from ..models.github_org_contributors_poll_response_200_output_progress import (
            GithubOrgContributorsPollResponse200OutputProgress,  # noqa: PLC0415
        )
        from ..models.github_org_contributors_poll_response_200_output_skipped_repos_item import (
            GithubOrgContributorsPollResponse200OutputSkippedReposItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        status = GithubOrgContributorsPollResponse200OutputStatus(d.pop("status"))

        progress = GithubOrgContributorsPollResponse200OutputProgress.from_dict(d.pop("progress"))

        contributors = []
        _contributors = d.pop("contributors")
        for contributors_item_data in _contributors:
            contributors_item = GithubOrgContributorsPollResponse200OutputContributorsItem.from_dict(
                contributors_item_data
            )

            contributors.append(contributors_item)

        skipped_repos = []
        _skipped_repos = d.pop("skippedRepos")
        for skipped_repos_item_data in _skipped_repos:
            skipped_repos_item = GithubOrgContributorsPollResponse200OutputSkippedReposItem.from_dict(
                skipped_repos_item_data
            )

            skipped_repos.append(skipped_repos_item)

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        github_org_contributors_poll_response_200_output = cls(
            status=status,
            progress=progress,
            contributors=contributors,
            skipped_repos=skipped_repos,
            next_page_token=next_page_token,
        )

        github_org_contributors_poll_response_200_output.additional_properties = d
        return github_org_contributors_poll_response_200_output

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
