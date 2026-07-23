from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HotelSearchResponse200OutputPropertiesItemImagesItem")


@_attrs_define
class HotelSearchResponse200OutputPropertiesItemImagesItem:
    """
    Attributes:
        thumbnail_url (None | str | Unset): Thumbnail image URL.
        original_url (None | str | Unset): Full-size image URL.
    """

    thumbnail_url: None | str | Unset = UNSET
    original_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        original_url: None | str | Unset
        if isinstance(self.original_url, Unset):
            original_url = UNSET
        else:
            original_url = self.original_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url
        if original_url is not UNSET:
            field_dict["originalUrl"] = original_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))

        def _parse_original_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        original_url = _parse_original_url(d.pop("originalUrl", UNSET))

        hotel_search_response_200_output_properties_item_images_item = cls(
            thumbnail_url=thumbnail_url,
            original_url=original_url,
        )

        hotel_search_response_200_output_properties_item_images_item.additional_properties = d
        return hotel_search_response_200_output_properties_item_images_item

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
