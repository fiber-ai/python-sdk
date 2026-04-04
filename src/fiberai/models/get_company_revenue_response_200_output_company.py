from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCompanyRevenueResponse200OutputCompany")


@_attrs_define
class GetCompanyRevenueResponse200OutputCompany:
    """
    Attributes:
        linkedin_url (str): LinkedIn company URL (e.g. 'https://www.linkedin.com/company/anthropic')
        linkedin_org_id (str): LinkedIn organization ID, if known
        name (None | str | Unset): Company display name, if known
        domain (None | str | Unset): Company website domain, if known
    """

    linkedin_url: str
    linkedin_org_id: str
    name: None | str | Unset = UNSET
    domain: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_url = self.linkedin_url

        linkedin_org_id = self.linkedin_org_id

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "linkedinUrl": linkedin_url,
                "linkedinOrgId": linkedin_org_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if domain is not UNSET:
            field_dict["domain"] = domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        linkedin_url = d.pop("linkedinUrl")

        linkedin_org_id = d.pop("linkedinOrgId")

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

        get_company_revenue_response_200_output_company = cls(
            linkedin_url=linkedin_url,
            linkedin_org_id=linkedin_org_id,
            name=name,
            domain=domain,
        )

        get_company_revenue_response_200_output_company.additional_properties = d
        return get_company_revenue_response_200_output_company

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
