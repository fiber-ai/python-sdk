from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfilePostsLiveFetchBody")


@_attrs_define
class ProfilePostsLiveFetchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        identifier (str): Identifier can be a profile's LinkedIn slug (e.g. 'williamhgates' from
            <linkedin.com/in/williamhgates>), a Sales Navigator URN (e.g. 'ACwAAA.....'), or a full LinkedIn URL (e.g.
            'https://www.linkedin.com/in/williamhgates/')
        cursor (None | str | Unset): Pagination cursor for fetching additional pages of posts
    """

    api_key: str
    identifier: str
    cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        identifier = self.identifier

        cursor: None | str | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "identifier": identifier,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        identifier = d.pop("identifier")

        def _parse_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        profile_posts_live_fetch_body = cls(
            api_key=api_key,
            identifier=identifier,
            cursor=cursor,
        )

        profile_posts_live_fetch_body.additional_properties = d
        return profile_posts_live_fetch_body

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
