from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_repo_contributors_response_200_output_contributors_item import (
        GithubRepoContributorsResponse200OutputContributorsItem,
    )


T = TypeVar("T", bound="GithubRepoContributorsResponse200Output")


@_attrs_define
class GithubRepoContributorsResponse200Output:
    """
    Attributes:
        contributors (list[GithubRepoContributorsResponse200OutputContributorsItem]): Contributors for this page, up to
            100. Only the top 500 contributors of a repository are available. Bot accounts are omitted.
        next_page_token (None | str | Unset): Token to retrieve the next page. Pass as `nextPageToken` in the next
            request. Null if no more pages.
    """

    contributors: list[GithubRepoContributorsResponse200OutputContributorsItem]
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contributors = []
        for contributors_item_data in self.contributors:
            contributors_item = contributors_item_data.to_dict()
            contributors.append(contributors_item)

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contributors": contributors,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_repo_contributors_response_200_output_contributors_item import (
            GithubRepoContributorsResponse200OutputContributorsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        contributors = []
        _contributors = d.pop("contributors")
        for contributors_item_data in _contributors:
            contributors_item = GithubRepoContributorsResponse200OutputContributorsItem.from_dict(
                contributors_item_data
            )

            contributors.append(contributors_item)

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        github_repo_contributors_response_200_output = cls(
            contributors=contributors,
            next_page_token=next_page_token,
        )

        github_repo_contributors_response_200_output.additional_properties = d
        return github_repo_contributors_response_200_output

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
