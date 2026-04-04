from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.twitter_user_followers_response_200_output_users_item import (
        TwitterUserFollowersResponse200OutputUsersItem,
    )


T = TypeVar("T", bound="TwitterUserFollowersResponse200Output")


@_attrs_define
class TwitterUserFollowersResponse200Output:
    """
    Attributes:
        users (list[TwitterUserFollowersResponse200OutputUsersItem]): List of followers for this page.
        next_cursor (None | str | Unset): Cursor to retrieve the next page of followers. Pass as `cursor` in the next
            request. Null if there are no more pages.
    """

    users: list[TwitterUserFollowersResponse200OutputUsersItem]
    next_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "users": users,
            }
        )
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.twitter_user_followers_response_200_output_users_item import (
            TwitterUserFollowersResponse200OutputUsersItem,
        )

        d = dict(src_dict)
        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = TwitterUserFollowersResponse200OutputUsersItem.from_dict(users_item_data)

            users.append(users_item)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        twitter_user_followers_response_200_output = cls(
            users=users,
            next_cursor=next_cursor,
        )

        twitter_user_followers_response_200_output.additional_properties = d
        return twitter_user_followers_response_200_output

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
