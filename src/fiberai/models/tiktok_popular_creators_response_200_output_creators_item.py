from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TiktokPopularCreatorsResponse200OutputCreatorsItem")


@_attrs_define
class TiktokPopularCreatorsResponse200OutputCreatorsItem:
    """
    Attributes:
        handle (None | str | Unset): TikTok handle (without '@').
        display_name (None | str | Unset): Display name.
        follower_count (float | None | Unset): Number of followers.
        profile_image_url (None | str | Unset): URL of the profile picture.
        total_like_count (float | None | Unset): Total number of likes received across all videos.
    """

    handle: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    follower_count: float | None | Unset = UNSET
    profile_image_url: None | str | Unset = UNSET
    total_like_count: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        total_like_count: float | None | Unset
        if isinstance(self.total_like_count, Unset):
            total_like_count = UNSET
        else:
            total_like_count = self.total_like_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if handle is not UNSET:
            field_dict["handle"] = handle
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if follower_count is not UNSET:
            field_dict["followerCount"] = follower_count
        if profile_image_url is not UNSET:
            field_dict["profileImageUrl"] = profile_image_url
        if total_like_count is not UNSET:
            field_dict["totalLikeCount"] = total_like_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_total_like_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_like_count = _parse_total_like_count(d.pop("totalLikeCount", UNSET))

        tiktok_popular_creators_response_200_output_creators_item = cls(
            handle=handle,
            display_name=display_name,
            follower_count=follower_count,
            profile_image_url=profile_image_url,
            total_like_count=total_like_count,
        )

        tiktok_popular_creators_response_200_output_creators_item.additional_properties = d
        return tiktok_popular_creators_response_200_output_creators_item

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
