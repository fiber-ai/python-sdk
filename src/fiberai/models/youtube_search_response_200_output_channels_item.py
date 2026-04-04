from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="YoutubeSearchResponse200OutputChannelsItem")


@_attrs_define
class YoutubeSearchResponse200OutputChannelsItem:
    """
    Attributes:
        name (str): Channel display name.
        id (None | str | Unset): YouTube channel ID.
        url (None | str | Unset): URL to the channel page.
        handle (None | str | Unset): Channel handle (e.g. '@veritasium').
        subscriber_count (float | None | Unset): Number of subscribers.
        description (None | str | Unset): Channel description snippet.
        verified (bool | None | Unset): Whether the channel is verified.
        thumbnail_url (None | str | Unset): URL of the channel thumbnail.
    """

    name: str
    id: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    handle: None | str | Unset = UNSET
    subscriber_count: float | None | Unset = UNSET
    description: None | str | Unset = UNSET
    verified: bool | None | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        handle: None | str | Unset
        if isinstance(self.handle, Unset):
            handle = UNSET
        else:
            handle = self.handle

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

        verified: bool | None | Unset
        if isinstance(self.verified, Unset):
            verified = UNSET
        else:
            verified = self.verified

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if handle is not UNSET:
            field_dict["handle"] = handle
        if subscriber_count is not UNSET:
            field_dict["subscriberCount"] = subscriber_count
        if description is not UNSET:
            field_dict["description"] = description
        if verified is not UNSET:
            field_dict["verified"] = verified
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_handle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        handle = _parse_handle(d.pop("handle", UNSET))

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

        def _parse_verified(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        verified = _parse_verified(d.pop("verified", UNSET))

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))

        youtube_search_response_200_output_channels_item = cls(
            name=name,
            id=id,
            url=url,
            handle=handle,
            subscriber_count=subscriber_count,
            description=description,
            verified=verified,
            thumbnail_url=thumbnail_url,
        )

        youtube_search_response_200_output_channels_item.additional_properties = d
        return youtube_search_response_200_output_channels_item

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
