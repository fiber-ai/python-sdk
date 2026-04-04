from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="YoutubeChannelResponse200OutputChannel")


@_attrs_define
class YoutubeChannelResponse200OutputChannel:
    """Channel metadata.

    Attributes:
        id (str): YouTube channel ID.
        name (str): Channel display name.
        url (None | str | Unset): URL to the channel page.
        subscriber_count (float | None | Unset): Number of subscribers.
        description (None | str | Unset): Channel description.
        country_code (None | str | Unset): Country associated with the channel (may be a full name or an ISO code).
        video_count (float | None | Unset): Total number of videos on the channel.
        view_count (float | None | Unset): Total view count across all videos.
    """

    id: str
    name: str
    url: None | str | Unset = UNSET
    subscriber_count: float | None | Unset = UNSET
    description: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    video_count: float | None | Unset = UNSET
    view_count: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        subscriber_count: float | None | Unset
        if isinstance(self.subscriber_count, Unset):
            subscriber_count = UNSET
        else:
            subscriber_count = self.subscriber_count

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        video_count: float | None | Unset
        if isinstance(self.video_count, Unset):
            video_count = UNSET
        else:
            video_count = self.video_count

        view_count: float | None | Unset
        if isinstance(self.view_count, Unset):
            view_count = UNSET
        else:
            view_count = self.view_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if subscriber_count is not UNSET:
            field_dict["subscriberCount"] = subscriber_count
        if description is not UNSET:
            field_dict["description"] = description
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if video_count is not UNSET:
            field_dict["videoCount"] = video_count
        if view_count is not UNSET:
            field_dict["viewCount"] = view_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_subscriber_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        subscriber_count = _parse_subscriber_count(d.pop("subscriberCount", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        def _parse_video_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        video_count = _parse_video_count(d.pop("videoCount", UNSET))

        def _parse_view_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        view_count = _parse_view_count(d.pop("viewCount", UNSET))

        youtube_channel_response_200_output_channel = cls(
            id=id,
            name=name,
            url=url,
            subscriber_count=subscriber_count,
            description=description,
            country_code=country_code,
            video_count=video_count,
            view_count=view_count,
        )

        youtube_channel_response_200_output_channel.additional_properties = d
        return youtube_channel_response_200_output_channel

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
