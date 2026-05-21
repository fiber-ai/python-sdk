from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.profile_latest_activities_live_fetch_response_200_output_activities_item_activity_type import (
    ProfileLatestActivitiesLiveFetchResponse200OutputActivitiesItemActivityType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileLatestActivitiesLiveFetchResponse200OutputActivitiesItem")


@_attrs_define
class ProfileLatestActivitiesLiveFetchResponse200OutputActivitiesItem:
    """
    Attributes:
        activity_type (ProfileLatestActivitiesLiveFetchResponse200OutputActivitiesItemActivityType): Type of LinkedIn
            activity (post, comment, reaction, share, repost, or other).
        occurred_at (str): Activity timestamp in ISO 8601 format.
        url (None | str | Unset): Best available LinkedIn URL for this activity.
        activity_urn (None | str | Unset): LinkedIn activity URN — a canonical identifier for this activity (for
            example, 'urn:li:activity:7193874239485124608'). Pass this value to the post-comments or post-reactions
            endpoints to fetch comments or reactions on the underlying post.
        content (None | str | Unset): Primary text content for this activity when available.
    """

    activity_type: ProfileLatestActivitiesLiveFetchResponse200OutputActivitiesItemActivityType
    occurred_at: str
    url: None | str | Unset = UNSET
    activity_urn: None | str | Unset = UNSET
    content: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_type = self.activity_type.value

        occurred_at = self.occurred_at

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        activity_urn: None | str | Unset
        if isinstance(self.activity_urn, Unset):
            activity_urn = UNSET
        else:
            activity_urn = self.activity_urn

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activityType": activity_type,
                "occurredAt": occurred_at,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if activity_urn is not UNSET:
            field_dict["activityUrn"] = activity_urn
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activity_type = ProfileLatestActivitiesLiveFetchResponse200OutputActivitiesItemActivityType(
            d.pop("activityType")
        )

        occurred_at = d.pop("occurredAt")

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_activity_urn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        activity_urn = _parse_activity_urn(d.pop("activityUrn", UNSET))

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        profile_latest_activities_live_fetch_response_200_output_activities_item = cls(
            activity_type=activity_type,
            occurred_at=occurred_at,
            url=url,
            activity_urn=activity_urn,
            content=content,
        )

        profile_latest_activities_live_fetch_response_200_output_activities_item.additional_properties = d
        return profile_latest_activities_live_fetch_response_200_output_activities_item

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
