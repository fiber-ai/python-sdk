from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TiktokProfileResponse200Output")


@_attrs_define
class TiktokProfileResponse200Output:
    """
    Attributes:
        id (None | str | Unset): Unique user identifier.
        handle (None | str | Unset): TikTok handle (without '@').
        display_name (None | str | Unset): Display name.
        bio (None | str | Unset): Profile bio.
        follower_count (float | None | Unset): Number of followers.
        profile_image_url (None | str | Unset): URL of the profile picture.
        is_verified (bool | None | Unset): Whether the account is verified.
        following_count (float | None | Unset): Number of accounts followed.
        video_count (float | None | Unset): Total number of videos posted.
        total_like_count (float | None | Unset): Total number of likes received across all videos.
        is_private (bool | None | Unset): Whether the account is private.
        external_url (None | str | Unset): Website URL from the profile (the 'link in bio').
    """

    id: None | str | Unset = UNSET
    handle: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    bio: None | str | Unset = UNSET
    follower_count: float | None | Unset = UNSET
    profile_image_url: None | str | Unset = UNSET
    is_verified: bool | None | Unset = UNSET
    following_count: float | None | Unset = UNSET
    video_count: float | None | Unset = UNSET
    total_like_count: float | None | Unset = UNSET
    is_private: bool | None | Unset = UNSET
    external_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
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

        bio: None | str | Unset
        if isinstance(self.bio, Unset):
            bio = UNSET
        else:
            bio = self.bio

        follower_count: float | None | Unset
        if isinstance(self.follower_count, Unset):
            follower_count = UNSET
        else:
            follower_count = self.follower_count

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

        following_count: float | None | Unset
        if isinstance(self.following_count, Unset):
            following_count = UNSET
        else:
            following_count = self.following_count

        video_count: float | None | Unset
        if isinstance(self.video_count, Unset):
            video_count = UNSET
        else:
            video_count = self.video_count

        total_like_count: float | None | Unset
        if isinstance(self.total_like_count, Unset):
            total_like_count = UNSET
        else:
            total_like_count = self.total_like_count

        is_private: bool | None | Unset
        if isinstance(self.is_private, Unset):
            is_private = UNSET
        else:
            is_private = self.is_private

        external_url: None | str | Unset
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if handle is not UNSET:
            field_dict["handle"] = handle
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if bio is not UNSET:
            field_dict["bio"] = bio
        if follower_count is not UNSET:
            field_dict["followerCount"] = follower_count
        if profile_image_url is not UNSET:
            field_dict["profileImageUrl"] = profile_image_url
        if is_verified is not UNSET:
            field_dict["isVerified"] = is_verified
        if following_count is not UNSET:
            field_dict["followingCount"] = following_count
        if video_count is not UNSET:
            field_dict["videoCount"] = video_count
        if total_like_count is not UNSET:
            field_dict["totalLikeCount"] = total_like_count
        if is_private is not UNSET:
            field_dict["isPrivate"] = is_private
        if external_url is not UNSET:
            field_dict["externalUrl"] = external_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

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

        def _parse_bio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bio = _parse_bio(d.pop("bio", UNSET))

        def _parse_follower_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        follower_count = _parse_follower_count(d.pop("followerCount", UNSET))

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

        def _parse_following_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        following_count = _parse_following_count(d.pop("followingCount", UNSET))

        def _parse_video_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        video_count = _parse_video_count(d.pop("videoCount", UNSET))

        def _parse_total_like_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_like_count = _parse_total_like_count(d.pop("totalLikeCount", UNSET))

        def _parse_is_private(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_private = _parse_is_private(d.pop("isPrivate", UNSET))

        def _parse_external_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_url = _parse_external_url(d.pop("externalUrl", UNSET))

        tiktok_profile_response_200_output = cls(
            id=id,
            handle=handle,
            display_name=display_name,
            bio=bio,
            follower_count=follower_count,
            profile_image_url=profile_image_url,
            is_verified=is_verified,
            following_count=following_count,
            video_count=video_count,
            total_like_count=total_like_count,
            is_private=is_private,
            external_url=external_url,
        )

        tiktok_profile_response_200_output.additional_properties = d
        return tiktok_profile_response_200_output

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
