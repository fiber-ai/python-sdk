from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_latest_activities_live_fetch_response_200_output_activities_item import (
        ProfileLatestActivitiesLiveFetchResponse200OutputActivitiesItem,
    )


T = TypeVar("T", bound="ProfileLatestActivitiesLiveFetchResponse200Output")


@_attrs_define
class ProfileLatestActivitiesLiveFetchResponse200Output:
    """
    Attributes:
        activities (list[ProfileLatestActivitiesLiveFetchResponse200OutputActivitiesItem]): Up to 30 recent LinkedIn
            activities, ordered from newest to oldest.
        last_activity_at (None | str | Unset): Timestamp of the most recent public LinkedIn activity (post, comment,
            reaction, share, or repost) in ISO 8601 format, or null when no activity is available. This is not a 'last
            login' or 'last seen online' value.
    """

    activities: list[ProfileLatestActivitiesLiveFetchResponse200OutputActivitiesItem]
    last_activity_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activities = []
        for activities_item_data in self.activities:
            activities_item = activities_item_data.to_dict()
            activities.append(activities_item)

        last_activity_at: None | str | Unset
        if isinstance(self.last_activity_at, Unset):
            last_activity_at = UNSET
        else:
            last_activity_at = self.last_activity_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activities": activities,
            }
        )
        if last_activity_at is not UNSET:
            field_dict["lastActivityAt"] = last_activity_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_latest_activities_live_fetch_response_200_output_activities_item import (
            ProfileLatestActivitiesLiveFetchResponse200OutputActivitiesItem,
        )

        d = dict(src_dict)
        activities = []
        _activities = d.pop("activities")
        for activities_item_data in _activities:
            activities_item = ProfileLatestActivitiesLiveFetchResponse200OutputActivitiesItem.from_dict(
                activities_item_data
            )

            activities.append(activities_item)

        def _parse_last_activity_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_activity_at = _parse_last_activity_at(d.pop("lastActivityAt", UNSET))

        profile_latest_activities_live_fetch_response_200_output = cls(
            activities=activities,
            last_activity_at=last_activity_at,
        )

        profile_latest_activities_live_fetch_response_200_output.additional_properties = d
        return profile_latest_activities_live_fetch_response_200_output

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
