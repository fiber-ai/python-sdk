from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_media_lookup_batch_polling_response_200_output_results_item_candidates_item_platform import (
    SocialMediaLookupBatchPollingResponse200OutputResultsItemCandidatesItemPlatform,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialMediaLookupBatchPollingResponse200OutputResultsItemCandidatesItem")


@_attrs_define
class SocialMediaLookupBatchPollingResponse200OutputResultsItemCandidatesItem:
    """
    Attributes:
        platform (SocialMediaLookupBatchPollingResponse200OutputResultsItemCandidatesItemPlatform): The social media
            platform this candidate is for.
        handle (str): The handle or username on that platform, without any @ prefix (e.g. 'karpathy').
        confidence_out_of_10 (int): Confidence score from 0 to 10. Higher scores indicate a stronger match.
        profile_url (None | str | Unset): Full URL to the profile on that platform (e.g. 'https://x.com/karpathy').
        display_name (None | str | Unset): The display name shown on the profile.
        bio (None | str | Unset): Profile bio or description.
        location (None | str | Unset): Location as displayed on the profile.
        follower_count (int | None | Unset): Number of followers on that platform.
        is_verified (bool | None | Unset): Whether the account is verified on that platform.
        rationale (None | str | Unset): The AI reasoning for why this profile was selected as the best match.
    """

    platform: SocialMediaLookupBatchPollingResponse200OutputResultsItemCandidatesItemPlatform
    handle: str
    confidence_out_of_10: int
    profile_url: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    bio: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    follower_count: int | None | Unset = UNSET
    is_verified: bool | None | Unset = UNSET
    rationale: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform.value

        handle = self.handle

        confidence_out_of_10 = self.confidence_out_of_10

        profile_url: None | str | Unset
        if isinstance(self.profile_url, Unset):
            profile_url = UNSET
        else:
            profile_url = self.profile_url

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

        follower_count: int | None | Unset
        if isinstance(self.follower_count, Unset):
            follower_count = UNSET
        else:
            follower_count = self.follower_count

        is_verified: bool | None | Unset
        if isinstance(self.is_verified, Unset):
            is_verified = UNSET
        else:
            is_verified = self.is_verified

        rationale: None | str | Unset
        if isinstance(self.rationale, Unset):
            rationale = UNSET
        else:
            rationale = self.rationale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "handle": handle,
                "confidenceOutOf10": confidence_out_of_10,
            }
        )
        if profile_url is not UNSET:
            field_dict["profileUrl"] = profile_url
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if bio is not UNSET:
            field_dict["bio"] = bio
        if location is not UNSET:
            field_dict["location"] = location
        if follower_count is not UNSET:
            field_dict["followerCount"] = follower_count
        if is_verified is not UNSET:
            field_dict["isVerified"] = is_verified
        if rationale is not UNSET:
            field_dict["rationale"] = rationale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform = SocialMediaLookupBatchPollingResponse200OutputResultsItemCandidatesItemPlatform(d.pop("platform"))

        handle = d.pop("handle")

        confidence_out_of_10 = d.pop("confidenceOutOf10")

        def _parse_profile_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_url = _parse_profile_url(d.pop("profileUrl", UNSET))

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

        def _parse_follower_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        follower_count = _parse_follower_count(d.pop("followerCount", UNSET))

        def _parse_is_verified(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_verified = _parse_is_verified(d.pop("isVerified", UNSET))

        def _parse_rationale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rationale = _parse_rationale(d.pop("rationale", UNSET))

        social_media_lookup_batch_polling_response_200_output_results_item_candidates_item = cls(
            platform=platform,
            handle=handle,
            confidence_out_of_10=confidence_out_of_10,
            profile_url=profile_url,
            display_name=display_name,
            bio=bio,
            location=location,
            follower_count=follower_count,
            is_verified=is_verified,
            rationale=rationale,
        )

        social_media_lookup_batch_polling_response_200_output_results_item_candidates_item.additional_properties = d
        return social_media_lookup_batch_polling_response_200_output_results_item_candidates_item

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
