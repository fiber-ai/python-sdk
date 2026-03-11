from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyPostsLiveFetchResponse200OutputDataItemResharedPostType0VideoType0")


@_attrs_define
class CompanyPostsLiveFetchResponse200OutputDataItemResharedPostType0VideoType0:
    """
    Attributes:
        video_url (None | str | Unset):
        thumbnail_url (None | str | Unset):
    """

    video_url: None | str | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        video_url: None | str | Unset
        if isinstance(self.video_url, Unset):
            video_url = UNSET
        else:
            video_url = self.video_url

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if video_url is not UNSET:
            field_dict["videoUrl"] = video_url
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_video_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        video_url = _parse_video_url(d.pop("videoUrl", UNSET))

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))

        company_posts_live_fetch_response_200_output_data_item_reshared_post_type_0_video_type_0 = cls(
            video_url=video_url,
            thumbnail_url=thumbnail_url,
        )

        company_posts_live_fetch_response_200_output_data_item_reshared_post_type_0_video_type_0.additional_properties = d
        return company_posts_live_fetch_response_200_output_data_item_reshared_post_type_0_video_type_0

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
