from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TwitterProfileResponse200Output")


@_attrs_define
class TwitterProfileResponse200Output:
    """
    Attributes:
        id (None | str | Unset): Numeric user ID.
        handle (None | str | Unset): Twitter/X handle (without '@').
        display_name (None | str | Unset): Display name.
        bio (None | str | Unset): Profile bio / description.
        location (None | str | Unset): Location as entered on profile.
        profile_image_url (None | str | Unset): URL of the profile picture.
        banner_image_url (None | str | Unset): URL of the profile banner image.
        follower_count (float | None | Unset): Number of followers.
        following_count (float | None | Unset): Number of accounts followed.
        tweet_count (float | None | Unset): Total number of tweets / posts.
        is_verified (bool | None | Unset): Legacy verified status.
        is_blue_verified (bool | None | Unset): Twitter Blue / X Premium verified status.
        created_at (None | str | Unset): When the account was created.
        external_url (None | str | Unset): External URL linked in the profile.
    """

    id: None | str | Unset = UNSET
    handle: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    bio: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    profile_image_url: None | str | Unset = UNSET
    banner_image_url: None | str | Unset = UNSET
    follower_count: float | None | Unset = UNSET
    following_count: float | None | Unset = UNSET
    tweet_count: float | None | Unset = UNSET
    is_verified: bool | None | Unset = UNSET
    is_blue_verified: bool | None | Unset = UNSET
    created_at: None | str | Unset = UNSET
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

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        profile_image_url: None | str | Unset
        if isinstance(self.profile_image_url, Unset):
            profile_image_url = UNSET
        else:
            profile_image_url = self.profile_image_url

        banner_image_url: None | str | Unset
        if isinstance(self.banner_image_url, Unset):
            banner_image_url = UNSET
        else:
            banner_image_url = self.banner_image_url

        follower_count: float | None | Unset
        if isinstance(self.follower_count, Unset):
            follower_count = UNSET
        else:
            follower_count = self.follower_count

        following_count: float | None | Unset
        if isinstance(self.following_count, Unset):
            following_count = UNSET
        else:
            following_count = self.following_count

        tweet_count: float | None | Unset
        if isinstance(self.tweet_count, Unset):
            tweet_count = UNSET
        else:
            tweet_count = self.tweet_count

        is_verified: bool | None | Unset
        if isinstance(self.is_verified, Unset):
            is_verified = UNSET
        else:
            is_verified = self.is_verified

        is_blue_verified: bool | None | Unset
        if isinstance(self.is_blue_verified, Unset):
            is_blue_verified = UNSET
        else:
            is_blue_verified = self.is_blue_verified

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

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
        if location is not UNSET:
            field_dict["location"] = location
        if profile_image_url is not UNSET:
            field_dict["profileImageUrl"] = profile_image_url
        if banner_image_url is not UNSET:
            field_dict["bannerImageUrl"] = banner_image_url
        if follower_count is not UNSET:
            field_dict["followerCount"] = follower_count
        if following_count is not UNSET:
            field_dict["followingCount"] = following_count
        if tweet_count is not UNSET:
            field_dict["tweetCount"] = tweet_count
        if is_verified is not UNSET:
            field_dict["isVerified"] = is_verified
        if is_blue_verified is not UNSET:
            field_dict["isBlueVerified"] = is_blue_verified
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
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

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_profile_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_image_url = _parse_profile_image_url(d.pop("profileImageUrl", UNSET))

        def _parse_banner_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        banner_image_url = _parse_banner_image_url(d.pop("bannerImageUrl", UNSET))

        def _parse_follower_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        follower_count = _parse_follower_count(d.pop("followerCount", UNSET))

        def _parse_following_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        following_count = _parse_following_count(d.pop("followingCount", UNSET))

        def _parse_tweet_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tweet_count = _parse_tweet_count(d.pop("tweetCount", UNSET))

        def _parse_is_verified(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_verified = _parse_is_verified(d.pop("isVerified", UNSET))

        def _parse_is_blue_verified(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_blue_verified = _parse_is_blue_verified(d.pop("isBlueVerified", UNSET))

        def _parse_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        def _parse_external_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_url = _parse_external_url(d.pop("externalUrl", UNSET))

        twitter_profile_response_200_output = cls(
            id=id,
            handle=handle,
            display_name=display_name,
            bio=bio,
            location=location,
            profile_image_url=profile_image_url,
            banner_image_url=banner_image_url,
            follower_count=follower_count,
            following_count=following_count,
            tweet_count=tweet_count,
            is_verified=is_verified,
            is_blue_verified=is_blue_verified,
            created_at=created_at,
            external_url=external_url,
        )

        twitter_profile_response_200_output.additional_properties = d
        return twitter_profile_response_200_output

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
