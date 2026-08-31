from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.youtube_video_details_response_200_output_available_transcript_languages_item import (
        YoutubeVideoDetailsResponse200OutputAvailableTranscriptLanguagesItem,
    )
    from ..models.youtube_video_details_response_200_output_channel_type_0 import (
        YoutubeVideoDetailsResponse200OutputChannelType0,
    )
    from ..models.youtube_video_details_response_200_output_chapters_item import (
        YoutubeVideoDetailsResponse200OutputChaptersItem,
    )
    from ..models.youtube_video_details_response_200_output_key_moments_item import (
        YoutubeVideoDetailsResponse200OutputKeyMomentsItem,
    )
    from ..models.youtube_video_details_response_200_output_published_at_type_0 import (
        YoutubeVideoDetailsResponse200OutputPublishedAtType0,
    )


T = TypeVar("T", bound="YoutubeVideoDetailsResponse200Output")


@_attrs_define
class YoutubeVideoDetailsResponse200Output:
    """
    Attributes:
        id (str): YouTube video ID — the unique identifier found in the URL. For example, in
            'https://www.youtube.com/watch?v=094y1Z2wpJg', the video ID is '094y1Z2wpJg'.
        title (str): Video title.
        chapters (list[YoutubeVideoDetailsResponse200OutputChaptersItem]): Author-defined chapters with timestamps.
            These are manually set by the video creator in the description.
        key_moments (list[YoutubeVideoDetailsResponse200OutputKeyMomentsItem]): Auto-generated key moments identified by
            YouTube's algorithms. These are distinct from author-defined chapters.
        available_transcript_languages (list[YoutubeVideoDetailsResponse200OutputAvailableTranscriptLanguagesItem]):
            Languages for which transcripts are available.
        view_count (float | None | Unset): Number of views.
        like_count (float | None | Unset): Number of likes.
        author (None | str | Unset): Video uploader name.
        category (None | str | Unset): Video category.
        published_at (None | Unset | YoutubeVideoDetailsResponse200OutputPublishedAtType0): Publication date. When
            YouTube only provides approximate time (e.g. '2 years ago'), we estimate the date and set `estimated: true`.
        description (None | str | Unset): Video description.
        thumbnail_url (None | str | Unset): URL of the video thumbnail.
        duration_seconds (float | None | Unset): Video duration in seconds.
        channel (None | Unset | YoutubeVideoDetailsResponse200OutputChannelType0): Channel information.
        comment_count (float | None | Unset): Total number of comments.
    """

    id: str
    title: str
    chapters: list[YoutubeVideoDetailsResponse200OutputChaptersItem]
    key_moments: list[YoutubeVideoDetailsResponse200OutputKeyMomentsItem]
    available_transcript_languages: list[YoutubeVideoDetailsResponse200OutputAvailableTranscriptLanguagesItem]
    view_count: float | None | Unset = UNSET
    like_count: float | None | Unset = UNSET
    author: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    published_at: None | Unset | YoutubeVideoDetailsResponse200OutputPublishedAtType0 = UNSET
    description: None | str | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    duration_seconds: float | None | Unset = UNSET
    channel: None | Unset | YoutubeVideoDetailsResponse200OutputChannelType0 = UNSET
    comment_count: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.youtube_video_details_response_200_output_channel_type_0 import (
            YoutubeVideoDetailsResponse200OutputChannelType0,  # noqa: PLC0415
        )
        from ..models.youtube_video_details_response_200_output_published_at_type_0 import (
            YoutubeVideoDetailsResponse200OutputPublishedAtType0,  # noqa: PLC0415
        )

        id = self.id

        title = self.title

        chapters = []
        for chapters_item_data in self.chapters:
            chapters_item = chapters_item_data.to_dict()
            chapters.append(chapters_item)

        key_moments = []
        for key_moments_item_data in self.key_moments:
            key_moments_item = key_moments_item_data.to_dict()
            key_moments.append(key_moments_item)

        available_transcript_languages = []
        for available_transcript_languages_item_data in self.available_transcript_languages:
            available_transcript_languages_item = available_transcript_languages_item_data.to_dict()
            available_transcript_languages.append(available_transcript_languages_item)

        view_count: float | None | Unset
        if isinstance(self.view_count, Unset):
            view_count = UNSET
        else:
            view_count = self.view_count

        like_count: float | None | Unset
        if isinstance(self.like_count, Unset):
            like_count = UNSET
        else:
            like_count = self.like_count

        author: None | str | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        published_at: dict[str, Any] | None | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        elif isinstance(self.published_at, YoutubeVideoDetailsResponse200OutputPublishedAtType0):
            published_at = self.published_at.to_dict()
        else:
            published_at = self.published_at

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        duration_seconds: float | None | Unset
        if isinstance(self.duration_seconds, Unset):
            duration_seconds = UNSET
        else:
            duration_seconds = self.duration_seconds

        channel: dict[str, Any] | None | Unset
        if isinstance(self.channel, Unset):
            channel = UNSET
        elif isinstance(self.channel, YoutubeVideoDetailsResponse200OutputChannelType0):
            channel = self.channel.to_dict()
        else:
            channel = self.channel

        comment_count: float | None | Unset
        if isinstance(self.comment_count, Unset):
            comment_count = UNSET
        else:
            comment_count = self.comment_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "chapters": chapters,
                "keyMoments": key_moments,
                "availableTranscriptLanguages": available_transcript_languages,
            }
        )
        if view_count is not UNSET:
            field_dict["viewCount"] = view_count
        if like_count is not UNSET:
            field_dict["likeCount"] = like_count
        if author is not UNSET:
            field_dict["author"] = author
        if category is not UNSET:
            field_dict["category"] = category
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at
        if description is not UNSET:
            field_dict["description"] = description
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url
        if duration_seconds is not UNSET:
            field_dict["durationSeconds"] = duration_seconds
        if channel is not UNSET:
            field_dict["channel"] = channel
        if comment_count is not UNSET:
            field_dict["commentCount"] = comment_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.youtube_video_details_response_200_output_available_transcript_languages_item import (
            YoutubeVideoDetailsResponse200OutputAvailableTranscriptLanguagesItem,  # noqa: PLC0415
        )
        from ..models.youtube_video_details_response_200_output_channel_type_0 import (
            YoutubeVideoDetailsResponse200OutputChannelType0,  # noqa: PLC0415
        )
        from ..models.youtube_video_details_response_200_output_chapters_item import (
            YoutubeVideoDetailsResponse200OutputChaptersItem,  # noqa: PLC0415
        )
        from ..models.youtube_video_details_response_200_output_key_moments_item import (
            YoutubeVideoDetailsResponse200OutputKeyMomentsItem,  # noqa: PLC0415
        )
        from ..models.youtube_video_details_response_200_output_published_at_type_0 import (
            YoutubeVideoDetailsResponse200OutputPublishedAtType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        chapters = []
        _chapters = d.pop("chapters")
        for chapters_item_data in _chapters:
            chapters_item = YoutubeVideoDetailsResponse200OutputChaptersItem.from_dict(chapters_item_data)

            chapters.append(chapters_item)

        key_moments = []
        _key_moments = d.pop("keyMoments")
        for key_moments_item_data in _key_moments:
            key_moments_item = YoutubeVideoDetailsResponse200OutputKeyMomentsItem.from_dict(key_moments_item_data)

            key_moments.append(key_moments_item)

        available_transcript_languages = []
        _available_transcript_languages = d.pop("availableTranscriptLanguages")
        for available_transcript_languages_item_data in _available_transcript_languages:
            available_transcript_languages_item = (
                YoutubeVideoDetailsResponse200OutputAvailableTranscriptLanguagesItem.from_dict(
                    available_transcript_languages_item_data
                )
            )

            available_transcript_languages.append(available_transcript_languages_item)

        def _parse_view_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        view_count = _parse_view_count(d.pop("viewCount", UNSET))

        def _parse_like_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        like_count = _parse_like_count(d.pop("likeCount", UNSET))

        def _parse_author(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_published_at(data: object) -> None | Unset | YoutubeVideoDetailsResponse200OutputPublishedAtType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                published_at_type_0 = YoutubeVideoDetailsResponse200OutputPublishedAtType0.from_dict(data)

                return published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | YoutubeVideoDetailsResponse200OutputPublishedAtType0, data)

        published_at = _parse_published_at(d.pop("publishedAt", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))

        def _parse_duration_seconds(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_seconds = _parse_duration_seconds(d.pop("durationSeconds", UNSET))

        def _parse_channel(data: object) -> None | Unset | YoutubeVideoDetailsResponse200OutputChannelType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                channel_type_0 = YoutubeVideoDetailsResponse200OutputChannelType0.from_dict(data)

                return channel_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | YoutubeVideoDetailsResponse200OutputChannelType0, data)

        channel = _parse_channel(d.pop("channel", UNSET))

        def _parse_comment_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        comment_count = _parse_comment_count(d.pop("commentCount", UNSET))

        youtube_video_details_response_200_output = cls(
            id=id,
            title=title,
            chapters=chapters,
            key_moments=key_moments,
            available_transcript_languages=available_transcript_languages,
            view_count=view_count,
            like_count=like_count,
            author=author,
            category=category,
            published_at=published_at,
            description=description,
            thumbnail_url=thumbnail_url,
            duration_seconds=duration_seconds,
            channel=channel,
            comment_count=comment_count,
        )

        youtube_video_details_response_200_output.additional_properties = d
        return youtube_video_details_response_200_output

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
