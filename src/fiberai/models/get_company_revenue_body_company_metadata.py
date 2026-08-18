from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCompanyRevenueBodyCompanyMetadata")


@_attrs_define
class GetCompanyRevenueBodyCompanyMetadata:
    """
    Attributes:
        name (None | str | Unset): Company display name (optional, helps disambiguate)
        domain (None | str | Unset): Company website domain (e.g. 'openai.com'), optional
        linkedin_url (None | str | Unset): LinkedIn company URL or slug (e.g. 'https://www.linkedin.com/company/openai'
            or 'openai')
        linkedin_org_id (None | str | Unset): LinkedIn numeric organization ID (e.g. '1441'), optional
    """

    name: None | str | Unset = UNSET
    domain: None | str | Unset = UNSET
    linkedin_url: None | str | Unset = UNSET
    linkedin_org_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if domain is not UNSET:
            field_dict["domain"] = domain
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url
        if linkedin_org_id is not UNSET:
            field_dict["linkedinOrgId"] = linkedin_org_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

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

        get_company_revenue_body_company_metadata = cls(
            name=name,
            domain=domain,
            linkedin_url=linkedin_url,
            linkedin_org_id=linkedin_org_id,
        )

        get_company_revenue_body_company_metadata.additional_properties = d
        return get_company_revenue_body_company_metadata

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
