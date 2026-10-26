from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_user_repo_activity_response_200_output_pull_requests_item_state_type_1 import (
    GithubUserRepoActivityResponse200OutputPullRequestsItemStateType1,
)
from ..models.github_user_repo_activity_response_200_output_pull_requests_item_state_type_2_type_1 import (
    GithubUserRepoActivityResponse200OutputPullRequestsItemStateType2Type1,
)
from ..models.github_user_repo_activity_response_200_output_pull_requests_item_state_type_3_type_1 import (
    GithubUserRepoActivityResponse200OutputPullRequestsItemStateType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubUserRepoActivityResponse200OutputPullRequestsItem")


@_attrs_define
class GithubUserRepoActivityResponse200OutputPullRequestsItem:
    """
    Attributes:
        title (str): Title of the pull request or issue.
        url (str): URL of the pull request or issue.
        state (GithubUserRepoActivityResponse200OutputPullRequestsItemStateType1 |
            GithubUserRepoActivityResponse200OutputPullRequestsItemStateType2Type1 |
            GithubUserRepoActivityResponse200OutputPullRequestsItemStateType3Type1 | None | Unset): Whether the pull request
            or issue is open or closed.
        created_at (None | str | Unset): When it was opened, as an ISO-8601 timestamp.
    """

    title: str
    url: str
    state: (
        GithubUserRepoActivityResponse200OutputPullRequestsItemStateType1
        | GithubUserRepoActivityResponse200OutputPullRequestsItemStateType2Type1
        | GithubUserRepoActivityResponse200OutputPullRequestsItemStateType3Type1
        | None
        | Unset
    ) = UNSET
    created_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        url = self.url

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, GithubUserRepoActivityResponse200OutputPullRequestsItemStateType1):
            state = self.state.value
        elif isinstance(self.state, GithubUserRepoActivityResponse200OutputPullRequestsItemStateType2Type1):
            state = self.state.value
        elif isinstance(self.state, GithubUserRepoActivityResponse200OutputPullRequestsItemStateType3Type1):
            state = self.state.value
        else:
            state = self.state

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "url": url,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        url = d.pop("url")

        def _parse_state(
            data: object,
        ) -> (
            GithubUserRepoActivityResponse200OutputPullRequestsItemStateType1
            | GithubUserRepoActivityResponse200OutputPullRequestsItemStateType2Type1
            | GithubUserRepoActivityResponse200OutputPullRequestsItemStateType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_type_1 = GithubUserRepoActivityResponse200OutputPullRequestsItemStateType1(data)

                return state_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_type_2_type_1 = GithubUserRepoActivityResponse200OutputPullRequestsItemStateType2Type1(data)

                return state_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_type_3_type_1 = GithubUserRepoActivityResponse200OutputPullRequestsItemStateType3Type1(data)

                return state_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GithubUserRepoActivityResponse200OutputPullRequestsItemStateType1
                | GithubUserRepoActivityResponse200OutputPullRequestsItemStateType2Type1
                | GithubUserRepoActivityResponse200OutputPullRequestsItemStateType3Type1
                | None
                | Unset,
                data,
            )

        state = _parse_state(d.pop("state", UNSET))

        def _parse_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        github_user_repo_activity_response_200_output_pull_requests_item = cls(
            title=title,
            url=url,
            state=state,
            created_at=created_at,
        )

        github_user_repo_activity_response_200_output_pull_requests_item.additional_properties = d
        return github_user_repo_activity_response_200_output_pull_requests_item

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
