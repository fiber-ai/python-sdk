from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0")


@_attrs_define
class ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0:
    """
    Attributes:
        linkedin_url (None | str | Unset):
        profile_picture (None | str | Unset):
        entity_urn (None | str | Unset):
        name (None | str | Unset):
    """

    linkedin_url: None | str | Unset = UNSET
    profile_picture: None | str | Unset = UNSET
    entity_urn: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        profile_picture: None | str | Unset
        if isinstance(self.profile_picture, Unset):
            profile_picture = UNSET
        else:
            profile_picture = self.profile_picture

        entity_urn: None | str | Unset
        if isinstance(self.entity_urn, Unset):
            entity_urn = UNSET
        else:
            entity_urn = self.entity_urn

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url
        if profile_picture is not UNSET:
            field_dict["profilePicture"] = profile_picture
        if entity_urn is not UNSET:
            field_dict["entityUrn"] = entity_urn
        if name is not UNSET:
            field_dict["name"] = name

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

        def _parse_profile_picture(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_picture = _parse_profile_picture(d.pop("profilePicture", UNSET))

        def _parse_entity_urn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_urn = _parse_entity_urn(d.pop("entityUrn", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        profile_comments_live_fetch_response_200_output_comments_type_0_item_commenter_type_0 = cls(
            linkedin_url=linkedin_url,
            profile_picture=profile_picture,
            entity_urn=entity_urn,
            name=name,
        )

        profile_comments_live_fetch_response_200_output_comments_type_0_item_commenter_type_0.additional_properties = d
        return profile_comments_live_fetch_response_200_output_comments_type_0_item_commenter_type_0

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
