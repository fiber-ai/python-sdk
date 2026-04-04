from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.youtube_channel_response_200_output_channel import YoutubeChannelResponse200OutputChannel
    from ..models.youtube_channel_response_200_output_videos_item import YoutubeChannelResponse200OutputVideosItem


T = TypeVar("T", bound="YoutubeChannelResponse200Output")


@_attrs_define
class YoutubeChannelResponse200Output:
    """
    Attributes:
        channel (YoutubeChannelResponse200OutputChannel): Channel metadata.
        videos (list[YoutubeChannelResponse200OutputVideosItem]): Videos on this page.
        next_page_token (None | str | Unset): Token to retrieve the next page of channel videos. Pass this as
            `nextPageToken` in the next request. Null if there are no more pages.
    """

    channel: YoutubeChannelResponse200OutputChannel
    videos: list[YoutubeChannelResponse200OutputVideosItem]
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel.to_dict()

        videos = []
        for videos_item_data in self.videos:
            videos_item = videos_item_data.to_dict()
            videos.append(videos_item)

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel": channel,
                "videos": videos,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.youtube_channel_response_200_output_channel import YoutubeChannelResponse200OutputChannel
        from ..models.youtube_channel_response_200_output_videos_item import YoutubeChannelResponse200OutputVideosItem

        d = dict(src_dict)
        channel = YoutubeChannelResponse200OutputChannel.from_dict(d.pop("channel"))

        videos = []
        _videos = d.pop("videos")
        for videos_item_data in _videos:
            videos_item = YoutubeChannelResponse200OutputVideosItem.from_dict(videos_item_data)

            videos.append(videos_item)

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        youtube_channel_response_200_output = cls(
            channel=channel,
            videos=videos,
            next_page_token=next_page_token,
        )

        youtube_channel_response_200_output.additional_properties = d
        return youtube_channel_response_200_output

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
