from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TwitterHandleToLinkedinUrlResponse200OutputXProfileType0")


@_attrs_define
class TwitterHandleToLinkedinUrlResponse200OutputXProfileType0:
    """Public snapshot of the X profile that was used for matching (null if the X profile could not be fetched).

    Attributes:
        handle (str): The X handle, echoed from the fetched profile.
        display_name (None | str | Unset): Display name shown on the X profile. Null if the profile has no display name
            set.
        bio (None | str | Unset): Profile bio text. Null if the profile has no bio.
        location (None | str | Unset): Location as displayed on the X profile (free-form, not normalized). Null if the
            user did not set a location.
        external_url (None | str | Unset): External URL linked from the X profile (often a personal site or company
            link). Null if the profile has no external URL.
    """

    handle: str
    display_name: None | str | Unset = UNSET
    bio: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    external_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        handle = self.handle

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        bio: None | str | Unset
        if isinstance(self.bio, Unset):
            bio = UNSET
        else:
            bio = self.bio

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        external_url: None | str | Unset
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "handle": handle,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if bio is not UNSET:
            field_dict["bio"] = bio
        if location is not UNSET:
            field_dict["location"] = location
        if external_url is not UNSET:
            field_dict["externalUrl"] = external_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        handle = d.pop("handle")

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        def _parse_bio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bio = _parse_bio(d.pop("bio", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_external_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_url = _parse_external_url(d.pop("externalUrl", UNSET))

        twitter_handle_to_linkedin_url_response_200_output_x_profile_type_0 = cls(
            handle=handle,
            display_name=display_name,
            bio=bio,
            location=location,
            external_url=external_url,
        )

        twitter_handle_to_linkedin_url_response_200_output_x_profile_type_0.additional_properties = d
        return twitter_handle_to_linkedin_url_response_200_output_x_profile_type_0

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
