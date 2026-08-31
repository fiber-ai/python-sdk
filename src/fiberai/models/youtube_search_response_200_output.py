from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.youtube_search_response_200_output_channels_item import YoutubeSearchResponse200OutputChannelsItem
    from ..models.youtube_search_response_200_output_shorts_item import YoutubeSearchResponse200OutputShortsItem
    from ..models.youtube_search_response_200_output_videos_item import YoutubeSearchResponse200OutputVideosItem


T = TypeVar("T", bound="YoutubeSearchResponse200Output")


@_attrs_define
class YoutubeSearchResponse200Output:
    """
    Attributes:
        videos (list[YoutubeSearchResponse200OutputVideosItem]): List of video search results.
        shorts (list[YoutubeSearchResponse200OutputShortsItem]): List of YouTube Shorts matching the query.
        channels (list[YoutubeSearchResponse200OutputChannelsItem]): List of channel results matching the query.
        next_page_token (None | str | Unset): Token to retrieve the next page of search results. Pass this as
            `nextPageToken` in the next request. Null if there are no more pages.
    """

    videos: list[YoutubeSearchResponse200OutputVideosItem]
    shorts: list[YoutubeSearchResponse200OutputShortsItem]
    channels: list[YoutubeSearchResponse200OutputChannelsItem]
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        videos = []
        for videos_item_data in self.videos:
            videos_item = videos_item_data.to_dict()
            videos.append(videos_item)

        shorts = []
        for shorts_item_data in self.shorts:
            shorts_item = shorts_item_data.to_dict()
            shorts.append(shorts_item)

        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()
            channels.append(channels_item)

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "videos": videos,
                "shorts": shorts,
                "channels": channels,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.youtube_search_response_200_output_channels_item import (
            YoutubeSearchResponse200OutputChannelsItem,  # noqa: PLC0415
        )
        from ..models.youtube_search_response_200_output_shorts_item import (
            YoutubeSearchResponse200OutputShortsItem,  # noqa: PLC0415
        )
        from ..models.youtube_search_response_200_output_videos_item import (
            YoutubeSearchResponse200OutputVideosItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        videos = []
        _videos = d.pop("videos")
        for videos_item_data in _videos:
            videos_item = YoutubeSearchResponse200OutputVideosItem.from_dict(videos_item_data)

            videos.append(videos_item)

        shorts = []
        _shorts = d.pop("shorts")
        for shorts_item_data in _shorts:
            shorts_item = YoutubeSearchResponse200OutputShortsItem.from_dict(shorts_item_data)

            shorts.append(shorts_item)

        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = YoutubeSearchResponse200OutputChannelsItem.from_dict(channels_item_data)

            channels.append(channels_item)

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        youtube_search_response_200_output = cls(
            videos=videos,
            shorts=shorts,
            channels=channels,
            next_page_token=next_page_token,
        )

        youtube_search_response_200_output.additional_properties = d
        return youtube_search_response_200_output

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
