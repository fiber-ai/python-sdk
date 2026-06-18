from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemAcceleratorsType0ItemFoundersType0Item"
)


@_attrs_define
class GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemAcceleratorsType0ItemFoundersType0Item:
    """
    Attributes:
        full_name (None | str | Unset):
        bio (None | str | Unset):
        job_title (None | str | Unset):
        is_active (bool | None | Unset):
        email_address (None | str | Unset):
        facebook_url (None | str | Unset):
        twitter_handle (None | str | Unset):
        linkedin_slug (None | str | Unset):
        github_username (None | str | Unset):
    """

    full_name: None | str | Unset = UNSET
    bio: None | str | Unset = UNSET
    job_title: None | str | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    email_address: None | str | Unset = UNSET
    facebook_url: None | str | Unset = UNSET
    twitter_handle: None | str | Unset = UNSET
    linkedin_slug: None | str | Unset = UNSET
    github_username: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        bio: None | str | Unset
        if isinstance(self.bio, Unset):
            bio = UNSET
        else:
            bio = self.bio

        job_title: None | str | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        else:
            job_title = self.job_title

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        email_address: None | str | Unset
        if isinstance(self.email_address, Unset):
            email_address = UNSET
        else:
            email_address = self.email_address

        facebook_url: None | str | Unset
        if isinstance(self.facebook_url, Unset):
            facebook_url = UNSET
        else:
            facebook_url = self.facebook_url

        twitter_handle: None | str | Unset
        if isinstance(self.twitter_handle, Unset):
            twitter_handle = UNSET
        else:
            twitter_handle = self.twitter_handle

        linkedin_slug: None | str | Unset
        if isinstance(self.linkedin_slug, Unset):
            linkedin_slug = UNSET
        else:
            linkedin_slug = self.linkedin_slug

        github_username: None | str | Unset
        if isinstance(self.github_username, Unset):
            github_username = UNSET
        else:
            github_username = self.github_username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if bio is not UNSET:
            field_dict["bio"] = bio
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if email_address is not UNSET:
            field_dict["email_address"] = email_address
        if facebook_url is not UNSET:
            field_dict["facebook_url"] = facebook_url
        if twitter_handle is not UNSET:
            field_dict["twitter_handle"] = twitter_handle
        if linkedin_slug is not UNSET:
            field_dict["linkedin_slug"] = linkedin_slug
        if github_username is not UNSET:
            field_dict["github_username"] = github_username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("full_name", UNSET))

        def _parse_bio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bio = _parse_bio(d.pop("bio", UNSET))

        def _parse_job_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_title = _parse_job_title(d.pop("job_title", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_email_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address = _parse_email_address(d.pop("email_address", UNSET))

        def _parse_facebook_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facebook_url = _parse_facebook_url(d.pop("facebook_url", UNSET))

        def _parse_twitter_handle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        twitter_handle = _parse_twitter_handle(d.pop("twitter_handle", UNSET))

        def _parse_linkedin_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_slug = _parse_linkedin_slug(d.pop("linkedin_slug", UNSET))

        def _parse_github_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        github_username = _parse_github_username(d.pop("github_username", UNSET))

        get_current_companies_in_saved_search_response_200_output_companies_item_accelerators_type_0_item_founders_type_0_item = cls(
            full_name=full_name,
            bio=bio,
            job_title=job_title,
            is_active=is_active,
            email_address=email_address,
            facebook_url=facebook_url,
            twitter_handle=twitter_handle,
            linkedin_slug=linkedin_slug,
            github_username=github_username,
        )

        get_current_companies_in_saved_search_response_200_output_companies_item_accelerators_type_0_item_founders_type_0_item.additional_properties = d
        return get_current_companies_in_saved_search_response_200_output_companies_item_accelerators_type_0_item_founders_type_0_item

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
