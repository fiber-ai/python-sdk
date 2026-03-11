from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanySearchResponse200OutputDataItemAcceleratorsType0ItemFoundersType0Item")


@_attrs_define
class CompanySearchResponse200OutputDataItemAcceleratorsType0ItemFoundersType0Item:
    """
    Attributes:
        full_name (str | Unset):
        bio (str | Unset):
        job_title (str | Unset):
        is_active (bool | Unset):
        email_address (str | Unset):
        facebook_url (str | Unset):
        twitter_handle (str | Unset):
        linkedin_slug (str | Unset):
        github_username (str | Unset):
    """

    full_name: str | Unset = UNSET
    bio: str | Unset = UNSET
    job_title: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    email_address: str | Unset = UNSET
    facebook_url: str | Unset = UNSET
    twitter_handle: str | Unset = UNSET
    linkedin_slug: str | Unset = UNSET
    github_username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_name = self.full_name

        bio = self.bio

        job_title = self.job_title

        is_active = self.is_active

        email_address = self.email_address

        facebook_url = self.facebook_url

        twitter_handle = self.twitter_handle

        linkedin_slug = self.linkedin_slug

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
        full_name = d.pop("full_name", UNSET)

        bio = d.pop("bio", UNSET)

        job_title = d.pop("job_title", UNSET)

        is_active = d.pop("is_active", UNSET)

        email_address = d.pop("email_address", UNSET)

        facebook_url = d.pop("facebook_url", UNSET)

        twitter_handle = d.pop("twitter_handle", UNSET)

        linkedin_slug = d.pop("linkedin_slug", UNSET)

        github_username = d.pop("github_username", UNSET)

        company_search_response_200_output_data_item_accelerators_type_0_item_founders_type_0_item = cls(
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

        company_search_response_200_output_data_item_accelerators_type_0_item_founders_type_0_item.additional_properties = d
        return company_search_response_200_output_data_item_accelerators_type_0_item_founders_type_0_item

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
