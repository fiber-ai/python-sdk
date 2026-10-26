from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubRepoSearchResponse200OutputReposItem")


@_attrs_define
class GithubRepoSearchResponse200OutputReposItem:
    """
    Attributes:
        full_name (str): Repository name, including the owner.
        repo_url (str): Repository URL.
        star_count (float): Number of stars.
        fork_count (float): Number of forks.
        topics (list[str]): Repository topics.
        description (None | str | Unset): Repository description.
        language (None | str | Unset): Primary language.
        last_pushed_at (None | str | Unset): When the repository was last pushed, as an ISO-8601 timestamp.
    """

    full_name: str
    repo_url: str
    star_count: float
    fork_count: float
    topics: list[str]
    description: None | str | Unset = UNSET
    language: None | str | Unset = UNSET
    last_pushed_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_name = self.full_name

        repo_url = self.repo_url

        star_count = self.star_count

        fork_count = self.fork_count

        topics = self.topics

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        last_pushed_at: None | str | Unset
        if isinstance(self.last_pushed_at, Unset):
            last_pushed_at = UNSET
        else:
            last_pushed_at = self.last_pushed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fullName": full_name,
                "repoUrl": repo_url,
                "starCount": star_count,
                "forkCount": fork_count,
                "topics": topics,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if language is not UNSET:
            field_dict["language"] = language
        if last_pushed_at is not UNSET:
            field_dict["lastPushedAt"] = last_pushed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        full_name = d.pop("fullName")

        repo_url = d.pop("repoUrl")

        star_count = d.pop("starCount")

        fork_count = d.pop("forkCount")

        topics = cast(list[str], d.pop("topics"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_last_pushed_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_pushed_at = _parse_last_pushed_at(d.pop("lastPushedAt", UNSET))

        github_repo_search_response_200_output_repos_item = cls(
            full_name=full_name,
            repo_url=repo_url,
            star_count=star_count,
            fork_count=fork_count,
            topics=topics,
            description=description,
            language=language,
            last_pushed_at=last_pushed_at,
        )

        github_repo_search_response_200_output_repos_item.additional_properties = d
        return github_repo_search_response_200_output_repos_item

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
