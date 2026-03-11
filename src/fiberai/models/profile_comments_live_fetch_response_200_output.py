from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_comments_live_fetch_response_200_output_comments_type_0_item import (
        ProfileCommentsLiveFetchResponse200OutputCommentsType0Item,
    )


T = TypeVar("T", bound="ProfileCommentsLiveFetchResponse200Output")


@_attrs_define
class ProfileCommentsLiveFetchResponse200Output:
    """
    Attributes:
        comments (list[ProfileCommentsLiveFetchResponse200OutputCommentsType0Item] | None | Unset):
        cursor (None | str | Unset):
    """

    comments: list[ProfileCommentsLiveFetchResponse200OutputCommentsType0Item] | None | Unset = UNSET
    cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments: list[dict[str, Any]] | None | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        elif isinstance(self.comments, list):
            comments = []
            for comments_type_0_item_data in self.comments:
                comments_type_0_item = comments_type_0_item_data.to_dict()
                comments.append(comments_type_0_item)

        else:
            comments = self.comments

        cursor: None | str | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comments is not UNSET:
            field_dict["comments"] = comments
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_comments_live_fetch_response_200_output_comments_type_0_item import (
            ProfileCommentsLiveFetchResponse200OutputCommentsType0Item,
        )

        d = dict(src_dict)

        def _parse_comments(
            data: object,
        ) -> list[ProfileCommentsLiveFetchResponse200OutputCommentsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                comments_type_0 = []
                _comments_type_0 = data
                for comments_type_0_item_data in _comments_type_0:
                    comments_type_0_item = ProfileCommentsLiveFetchResponse200OutputCommentsType0Item.from_dict(
                        comments_type_0_item_data
                    )

                    comments_type_0.append(comments_type_0_item)

                return comments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProfileCommentsLiveFetchResponse200OutputCommentsType0Item] | None | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        def _parse_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        profile_comments_live_fetch_response_200_output = cls(
            comments=comments,
            cursor=cursor,
        )

        profile_comments_live_fetch_response_200_output.additional_properties = d
        return profile_comments_live_fetch_response_200_output

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
