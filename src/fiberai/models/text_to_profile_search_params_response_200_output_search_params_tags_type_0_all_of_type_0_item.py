from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_to_profile_search_params_response_200_output_search_params_tags_type_0_all_of_type_0_item_slug import (
    TextToProfileSearchParamsResponse200OutputSearchParamsTagsType0AllOfType0ItemSlug,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TextToProfileSearchParamsResponse200OutputSearchParamsTagsType0AllOfType0Item")


@_attrs_define
class TextToProfileSearchParamsResponse200OutputSearchParamsTagsType0AllOfType0Item:
    """
    Attributes:
        slug (TextToProfileSearchParamsResponse200OutputSearchParamsTagsType0AllOfType0ItemSlug):
        name (str):
        emoji (str):
        description (None | str | Unset):
    """

    slug: TextToProfileSearchParamsResponse200OutputSearchParamsTagsType0AllOfType0ItemSlug
    name: str
    emoji: str
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug.value

        name = self.name

        emoji = self.emoji

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "name": name,
                "emoji": emoji,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = TextToProfileSearchParamsResponse200OutputSearchParamsTagsType0AllOfType0ItemSlug(d.pop("slug"))

        name = d.pop("name")

        emoji = d.pop("emoji")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        text_to_profile_search_params_response_200_output_search_params_tags_type_0_all_of_type_0_item = cls(
            slug=slug,
            name=name,
            emoji=emoji,
            description=description,
        )

        text_to_profile_search_params_response_200_output_search_params_tags_type_0_all_of_type_0_item.additional_properties = d
        return text_to_profile_search_params_response_200_output_search_params_tags_type_0_all_of_type_0_item

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
