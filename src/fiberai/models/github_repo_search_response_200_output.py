from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_repo_search_response_200_output_repos_item import GithubRepoSearchResponse200OutputReposItem


T = TypeVar("T", bound="GithubRepoSearchResponse200Output")


@_attrs_define
class GithubRepoSearchResponse200Output:
    """
    Attributes:
        repos (list[GithubRepoSearchResponse200OutputReposItem]): Repositories for this page, up to 100. At most 1,000
            results are available.
        total_count (float): Total matches reported for the query. Only the first 1,000 can be paged through.
        next_page_token (None | str | Unset): Token to retrieve the next page. Pass as `nextPageToken` in the next
            request. Null if no more pages.
    """

    repos: list[GithubRepoSearchResponse200OutputReposItem]
    total_count: float
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repos = []
        for repos_item_data in self.repos:
            repos_item = repos_item_data.to_dict()
            repos.append(repos_item)

        total_count = self.total_count

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repos": repos,
                "totalCount": total_count,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_repo_search_response_200_output_repos_item import (
            GithubRepoSearchResponse200OutputReposItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        repos = []
        _repos = d.pop("repos")
        for repos_item_data in _repos:
            repos_item = GithubRepoSearchResponse200OutputReposItem.from_dict(repos_item_data)

            repos.append(repos_item)

        total_count = d.pop("totalCount")

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        github_repo_search_response_200_output = cls(
            repos=repos,
            total_count=total_count,
            next_page_token=next_page_token,
        )

        github_repo_search_response_200_output.additional_properties = d
        return github_repo_search_response_200_output

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
