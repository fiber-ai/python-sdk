from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyPostsLiveFetchResponse200OutputDataItemAuthorType0")


@_attrs_define
class CompanyPostsLiveFetchResponse200OutputDataItemAuthorType0:
    """
    Attributes:
        linkedin_url (None | str | Unset):
        name (None | str | Unset):
        profile_picture (None | str | Unset):
        linkedin_slug (None | str | Unset):
    """

    linkedin_url: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    profile_picture: None | str | Unset = UNSET
    linkedin_slug: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        profile_picture: None | str | Unset
        if isinstance(self.profile_picture, Unset):
            profile_picture = UNSET
        else:
            profile_picture = self.profile_picture

        linkedin_slug: None | str | Unset
        if isinstance(self.linkedin_slug, Unset):
            linkedin_slug = UNSET
        else:
            linkedin_slug = self.linkedin_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url
        if name is not UNSET:
            field_dict["name"] = name
        if profile_picture is not UNSET:
            field_dict["profilePicture"] = profile_picture
        if linkedin_slug is not UNSET:
            field_dict["linkedinSlug"] = linkedin_slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_profile_picture(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_picture = _parse_profile_picture(d.pop("profilePicture", UNSET))

        def _parse_linkedin_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_slug = _parse_linkedin_slug(d.pop("linkedinSlug", UNSET))

        company_posts_live_fetch_response_200_output_data_item_author_type_0 = cls(
            linkedin_url=linkedin_url,
            name=name,
            profile_picture=profile_picture,
            linkedin_slug=linkedin_slug,
        )

        company_posts_live_fetch_response_200_output_data_item_author_type_0.additional_properties = d
        return company_posts_live_fetch_response_200_output_data_item_author_type_0

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
