from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddTrackerCompaniesBodyCompaniesItem")


@_attrs_define
class AddTrackerCompaniesBodyCompaniesItem:
    """
    Attributes:
        linkedin_url (None | str | Unset): Full LinkedIn company URL.
        linkedin_org_id (None | str | Unset): A company's stable numeric identifier. This is NOT derived from their
            company page URL — retrieve it from a live enrichment lookup. Digits only.
        linkedin_slug (None | str | Unset): The handle in a company page URL — e.g. `microsoft` in
            https://www.linkedin.com/company/microsoft/.
        domain (None | str | Unset): Company website domain (e.g. 'fiber.ai'). Will be resolved to the company profile
            identifier.
    """

    linkedin_url: None | str | Unset = UNSET
    linkedin_org_id: None | str | Unset = UNSET
    linkedin_slug: None | str | Unset = UNSET
    domain: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        linkedin_org_id: None | str | Unset
        if isinstance(self.linkedin_org_id, Unset):
            linkedin_org_id = UNSET
        else:
            linkedin_org_id = self.linkedin_org_id

        linkedin_slug: None | str | Unset
        if isinstance(self.linkedin_slug, Unset):
            linkedin_slug = UNSET
        else:
            linkedin_slug = self.linkedin_slug

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url
        if linkedin_org_id is not UNSET:
            field_dict["linkedinOrgId"] = linkedin_org_id
        if linkedin_slug is not UNSET:
            field_dict["linkedinSlug"] = linkedin_slug
        if domain is not UNSET:
            field_dict["domain"] = domain

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

        def _parse_linkedin_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_org_id = _parse_linkedin_org_id(d.pop("linkedinOrgId", UNSET))

        def _parse_linkedin_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_slug = _parse_linkedin_slug(d.pop("linkedinSlug", UNSET))

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        add_tracker_companies_body_companies_item = cls(
            linkedin_url=linkedin_url,
            linkedin_org_id=linkedin_org_id,
            linkedin_slug=linkedin_slug,
            domain=domain,
        )

        add_tracker_companies_body_companies_item.additional_properties = d
        return add_tracker_companies_body_companies_item

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
