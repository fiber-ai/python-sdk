from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeopleSearchBodyCurrentCompaniesType0Item")


@_attrs_define
class PeopleSearchBodyCurrentCompaniesType0Item:
    """
    Attributes:
        domain (None | str | Unset): Company domain, like 'google.com'. Don't include 'https://', path fragments like
            '/about', or URL query parameters. If provided, we will not strip them out. This may be useful if your company
            page is like `instagram.com/google`.
        linkedin_slug_or_url (None | str | Unset): The company's linkedin slug or URL
        name (None | str | Unset): The company's name as present in LinkedIn. This would do partial matches as well, eg.
            `Fiber AI` matches with `Fiber AI (YC S23)`. Try not to rely on this field as it will simply be doing a loose
            name match. We recommend that you use the domain or LI slug if available.
        linkedin_org_id (None | str | Unset): The company's LinkedIn Organization ID, eg. 1441 for google
    """

    domain: None | str | Unset = UNSET
    linkedin_slug_or_url: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    linkedin_org_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        linkedin_slug_or_url: None | str | Unset
        if isinstance(self.linkedin_slug_or_url, Unset):
            linkedin_slug_or_url = UNSET
        else:
            linkedin_slug_or_url = self.linkedin_slug_or_url

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        linkedin_org_id: None | str | Unset
        if isinstance(self.linkedin_org_id, Unset):
            linkedin_org_id = UNSET
        else:
            linkedin_org_id = self.linkedin_org_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain is not UNSET:
            field_dict["domain"] = domain
        if linkedin_slug_or_url is not UNSET:
            field_dict["linkedinSlugOrURL"] = linkedin_slug_or_url
        if name is not UNSET:
            field_dict["name"] = name
        if linkedin_org_id is not UNSET:
            field_dict["linkedinOrgID"] = linkedin_org_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        def _parse_linkedin_slug_or_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_slug_or_url = _parse_linkedin_slug_or_url(d.pop("linkedinSlugOrURL", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_linkedin_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_org_id = _parse_linkedin_org_id(d.pop("linkedinOrgID", UNSET))

        people_search_body_current_companies_type_0_item = cls(
            domain=domain,
            linkedin_slug_or_url=linkedin_slug_or_url,
            name=name,
            linkedin_org_id=linkedin_org_id,
        )

        people_search_body_current_companies_type_0_item.additional_properties = d
        return people_search_body_current_companies_type_0_item

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
