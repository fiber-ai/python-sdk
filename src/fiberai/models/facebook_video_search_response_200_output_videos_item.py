from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.facebook_video_search_response_200_output_videos_item_author_type_0 import (
        FacebookVideoSearchResponse200OutputVideosItemAuthorType0,
    )


T = TypeVar("T", bound="FacebookVideoSearchResponse200OutputVideosItem")


@_attrs_define
class FacebookVideoSearchResponse200OutputVideosItem:
    """
    Attributes:
        id (str): Unique video ID.
        url (None | str | Unset): URL of the video or Reel.
        title (None | str | Unset): Video title.
        author (FacebookVideoSearchResponse200OutputVideosItemAuthorType0 | None | Unset): Author of the video.
        view_count (float | None | Unset): Number of views.
    """

    id: str
    url: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    author: FacebookVideoSearchResponse200OutputVideosItemAuthorType0 | None | Unset = UNSET
    view_count: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.facebook_video_search_response_200_output_videos_item_author_type_0 import (
            FacebookVideoSearchResponse200OutputVideosItemAuthorType0,  # noqa: PLC0415
        )

        id = self.id

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        author: dict[str, Any] | None | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        elif isinstance(self.author, FacebookVideoSearchResponse200OutputVideosItemAuthorType0):
            author = self.author.to_dict()
        else:
            author = self.author

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
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if title is not UNSET:
            field_dict["title"] = title
        if author is not UNSET:
            field_dict["author"] = author
        if view_count is not UNSET:
            field_dict["viewCount"] = view_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.facebook_video_search_response_200_output_videos_item_author_type_0 import (
            FacebookVideoSearchResponse200OutputVideosItemAuthorType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_author(data: object) -> FacebookVideoSearchResponse200OutputVideosItemAuthorType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_type_0 = FacebookVideoSearchResponse200OutputVideosItemAuthorType0.from_dict(data)

                return author_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FacebookVideoSearchResponse200OutputVideosItemAuthorType0 | None | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        def _parse_view_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        view_count = _parse_view_count(d.pop("viewCount", UNSET))

        facebook_video_search_response_200_output_videos_item = cls(
            id=id,
            url=url,
            title=title,
            author=author,
            view_count=view_count,
        )

        facebook_video_search_response_200_output_videos_item.additional_properties = d
        return facebook_video_search_response_200_output_videos_item

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
