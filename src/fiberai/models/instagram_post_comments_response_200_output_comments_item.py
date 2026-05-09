from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instagram_post_comments_response_200_output_comments_item_user_type_0 import (
        InstagramPostCommentsResponse200OutputCommentsItemUserType0,
    )


T = TypeVar("T", bound="InstagramPostCommentsResponse200OutputCommentsItem")


@_attrs_define
class InstagramPostCommentsResponse200OutputCommentsItem:
    """
    Attributes:
        id (str): Unique comment identifier.
        text (None | str | Unset): Comment text.
        published_at (None | str | Unset): ISO 8601 timestamp of when the comment was posted.
        user (InstagramPostCommentsResponse200OutputCommentsItemUserType0 | None | Unset): The user who posted the
            comment.
    """

    id: str
    text: None | str | Unset = UNSET
    published_at: None | str | Unset = UNSET
    user: InstagramPostCommentsResponse200OutputCommentsItemUserType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.instagram_post_comments_response_200_output_comments_item_user_type_0 import (
            InstagramPostCommentsResponse200OutputCommentsItemUserType0,
        )

        id = self.id

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        published_at: None | str | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        else:
            published_at = self.published_at

        user: dict[str, Any] | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, InstagramPostCommentsResponse200OutputCommentsItemUserType0):
            user = self.user.to_dict()
        else:
            user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instagram_post_comments_response_200_output_comments_item_user_type_0 import (
            InstagramPostCommentsResponse200OutputCommentsItemUserType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))

        def _parse_published_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        published_at = _parse_published_at(d.pop("publishedAt", UNSET))

        def _parse_user(data: object) -> InstagramPostCommentsResponse200OutputCommentsItemUserType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_0 = InstagramPostCommentsResponse200OutputCommentsItemUserType0.from_dict(data)

                return user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InstagramPostCommentsResponse200OutputCommentsItemUserType0 | None | Unset, data)

        user = _parse_user(d.pop("user", UNSET))

        instagram_post_comments_response_200_output_comments_item = cls(
            id=id,
            text=text,
            published_at=published_at,
            user=user,
        )

        instagram_post_comments_response_200_output_comments_item.additional_properties = d
        return instagram_post_comments_response_200_output_comments_item

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
