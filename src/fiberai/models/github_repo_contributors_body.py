from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubRepoContributorsBody")


@_attrs_define
class GithubRepoContributorsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        repo_url (str): Repository to list contributors for. Accepts a URL (for example
            'https://github.com/tenstorrent/tt-metal') or 'owner/repo'.
        next_page_token (None | str | Unset): Pagination token from a prior response's `nextPageToken`. Omit (or pass
            null) to fetch the first page. At most the top 500 contributors are available.
    """

    api_key: str
    repo_url: str
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        repo_url = self.repo_url

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "repoUrl": repo_url,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        repo_url = d.pop("repoUrl")

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        github_repo_contributors_body = cls(
            api_key=api_key,
            repo_url=repo_url,
            next_page_token=next_page_token,
        )

        github_repo_contributors_body.additional_properties = d
        return github_repo_contributors_body

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
