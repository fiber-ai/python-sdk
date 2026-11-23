from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FacebookProfileReelsResponse200OutputReelsItem")


@_attrs_define
class FacebookProfileReelsResponse200OutputReelsItem:
    """
    Attributes:
        id (str): Unique Reel ID.
        url (None | str | Unset): URL of the Reel.
        text (None | str | Unset): Reel description or caption.
        play_count (float | None | Unset): Number of plays.
    """

    id: str
    url: None | str | Unset = UNSET
    text: None | str | Unset = UNSET
    play_count: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        play_count: float | None | Unset
        if isinstance(self.play_count, Unset):
            play_count = UNSET
        else:
            play_count = self.play_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if text is not UNSET:
            field_dict["text"] = text
        if play_count is not UNSET:
            field_dict["playCount"] = play_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))

        def _parse_play_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        play_count = _parse_play_count(d.pop("playCount", UNSET))

        facebook_profile_reels_response_200_output_reels_item = cls(
            id=id,
            url=url,
            text=text,
            play_count=play_count,
        )

        facebook_profile_reels_response_200_output_reels_item.additional_properties = d
        return facebook_profile_reels_response_200_output_reels_item

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
