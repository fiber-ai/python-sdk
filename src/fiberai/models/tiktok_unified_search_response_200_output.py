from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tiktok_unified_search_response_200_output_users_item import (
        TiktokUnifiedSearchResponse200OutputUsersItem,
    )
    from ..models.tiktok_unified_search_response_200_output_videos_item import (
        TiktokUnifiedSearchResponse200OutputVideosItem,
    )


T = TypeVar("T", bound="TiktokUnifiedSearchResponse200Output")


@_attrs_define
class TiktokUnifiedSearchResponse200Output:
    """
    Attributes:
        videos (list[TiktokUnifiedSearchResponse200OutputVideosItem]): List of videos from the unified search results,
            for this page.
        users (list[TiktokUnifiedSearchResponse200OutputUsersItem]): List of users from the unified search results, for
            this page.
        next_page_token (None | str | Unset): Token to retrieve the next page. Pass as `nextPageToken` in the next
            request. Null if there are no more pages.
    """

    videos: list[TiktokUnifiedSearchResponse200OutputVideosItem]
    users: list[TiktokUnifiedSearchResponse200OutputUsersItem]
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        videos = []
        for videos_item_data in self.videos:
            videos_item = videos_item_data.to_dict()
            videos.append(videos_item)

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

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
                "users": users,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiktok_unified_search_response_200_output_users_item import (
            TiktokUnifiedSearchResponse200OutputUsersItem,  # noqa: PLC0415
        )
        from ..models.tiktok_unified_search_response_200_output_videos_item import (
            TiktokUnifiedSearchResponse200OutputVideosItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        videos = []
        _videos = d.pop("videos")
        for videos_item_data in _videos:
            videos_item = TiktokUnifiedSearchResponse200OutputVideosItem.from_dict(videos_item_data)

            videos.append(videos_item)

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = TiktokUnifiedSearchResponse200OutputUsersItem.from_dict(users_item_data)

            users.append(users_item)

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        tiktok_unified_search_response_200_output = cls(
            videos=videos,
            users=users,
            next_page_token=next_page_token,
        )

        tiktok_unified_search_response_200_output.additional_properties = d
        return tiktok_unified_search_response_200_output

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
