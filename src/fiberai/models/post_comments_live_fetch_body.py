from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostCommentsLiveFetchBody")


@_attrs_define
class PostCommentsLiveFetchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        content_id (str): You can get LinkedIn posts from the Profile or Company Posts endpoints. (e.g.,
            'urn:li:activity:7123456789012345678' or 'urn:li:ugcPost:7391650829398675456')
        cursor (None | str | Unset): Pagination cursor for fetching additional pages of posts
        include_tagged_users (bool | None | Unset): When true, also returns the LinkedIn users @-mentioned (tagged)
            inside each comment. This might be slower so only enable it if needed. Default: False.
    """

    api_key: str
    content_id: str
    cursor: None | str | Unset = UNSET
    include_tagged_users: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        content_id = self.content_id

        cursor: None | str | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        include_tagged_users: bool | None | Unset
        if isinstance(self.include_tagged_users, Unset):
            include_tagged_users = UNSET
        else:
            include_tagged_users = self.include_tagged_users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "contentId": content_id,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if include_tagged_users is not UNSET:
            field_dict["includeTaggedUsers"] = include_tagged_users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        content_id = d.pop("contentId")

        def _parse_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        def _parse_include_tagged_users(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_tagged_users = _parse_include_tagged_users(d.pop("includeTaggedUsers", UNSET))

        post_comments_live_fetch_body = cls(
            api_key=api_key,
            content_id=content_id,
            cursor=cursor,
            include_tagged_users=include_tagged_users,
        )

        post_comments_live_fetch_body.additional_properties = d
        return post_comments_live_fetch_body

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
