from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSearchByKeywordsResponse200OutputPostsItemAuthorType0")


@_attrs_define
class PostSearchByKeywordsResponse200OutputPostsItemAuthorType0:
    """
    Attributes:
        type_ (None | str | Unset):
        name (None | str | Unset):
        linkedin_url (None | str | Unset):
        headline (None | str | Unset):
        website (None | str | Unset):
        profile_picture (None | str | Unset):
    """

    type_: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    linkedin_url: None | str | Unset = UNSET
    headline: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    profile_picture: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        headline: None | str | Unset
        if isinstance(self.headline, Unset):
            headline = UNSET
        else:
            headline = self.headline

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        profile_picture: None | str | Unset
        if isinstance(self.profile_picture, Unset):
            profile_picture = UNSET
        else:
            profile_picture = self.profile_picture

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url
        if headline is not UNSET:
            field_dict["headline"] = headline
        if website is not UNSET:
            field_dict["website"] = website
        if profile_picture is not UNSET:
            field_dict["profilePicture"] = profile_picture

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))

        def _parse_headline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        headline = _parse_headline(d.pop("headline", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_profile_picture(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_picture = _parse_profile_picture(d.pop("profilePicture", UNSET))

        post_search_by_keywords_response_200_output_posts_item_author_type_0 = cls(
            type_=type_,
            name=name,
            linkedin_url=linkedin_url,
            headline=headline,
            website=website,
            profile_picture=profile_picture,
        )

        post_search_by_keywords_response_200_output_posts_item_author_type_0.additional_properties = d
        return post_search_by_keywords_response_200_output_posts_item_author_type_0

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
