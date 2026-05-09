from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstagramPostCommentsResponse200OutputCommentsItemUserType0")


@_attrs_define
class InstagramPostCommentsResponse200OutputCommentsItemUserType0:
    """The user who posted the comment.

    Attributes:
        id (str): Unique user identifier.
        handle (None | str | Unset): Instagram handle (without '@').
        display_name (None | str | Unset): Display name.
        profile_image_url (None | str | Unset): URL of the profile picture.
        is_verified (bool | None | Unset): Whether the account is verified.
    """

    id: str
    handle: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    profile_image_url: None | str | Unset = UNSET
    is_verified: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        handle: None | str | Unset
        if isinstance(self.handle, Unset):
            handle = UNSET
        else:
            handle = self.handle

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        profile_image_url: None | str | Unset
        if isinstance(self.profile_image_url, Unset):
            profile_image_url = UNSET
        else:
            profile_image_url = self.profile_image_url

        is_verified: bool | None | Unset
        if isinstance(self.is_verified, Unset):
            is_verified = UNSET
        else:
            is_verified = self.is_verified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if handle is not UNSET:
            field_dict["handle"] = handle
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if profile_image_url is not UNSET:
            field_dict["profileImageUrl"] = profile_image_url
        if is_verified is not UNSET:
            field_dict["isVerified"] = is_verified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_handle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        handle = _parse_handle(d.pop("handle", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        def _parse_profile_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_image_url = _parse_profile_image_url(d.pop("profileImageUrl", UNSET))

        def _parse_is_verified(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_verified = _parse_is_verified(d.pop("isVerified", UNSET))

        instagram_post_comments_response_200_output_comments_item_user_type_0 = cls(
            id=id,
            handle=handle,
            display_name=display_name,
            profile_image_url=profile_image_url,
            is_verified=is_verified,
        )

        instagram_post_comments_response_200_output_comments_item_user_type_0.additional_properties = d
        return instagram_post_comments_response_200_output_comments_item_user_type_0

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
