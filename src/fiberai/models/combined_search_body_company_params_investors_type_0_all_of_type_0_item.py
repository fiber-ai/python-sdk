from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CombinedSearchBodyCompanyParamsInvestorsType0AllOfType0Item")


@_attrs_define
class CombinedSearchBodyCompanyParamsInvestorsType0AllOfType0Item:
    """Requires at least one identifier: LinkedIn company ID, LinkedIn URL, or company domain to uniquely identify the
    investor organization.

        Attributes:
            linkedin_company_id (None | str | Unset):
            linkedin_url (None | str | Unset):
            company_domain (None | str | Unset):
    """

    linkedin_company_id: None | str | Unset = UNSET
    linkedin_url: None | str | Unset = UNSET
    company_domain: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_company_id: None | str | Unset
        if isinstance(self.linkedin_company_id, Unset):
            linkedin_company_id = UNSET
        else:
            linkedin_company_id = self.linkedin_company_id

        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        company_domain: None | str | Unset
        if isinstance(self.company_domain, Unset):
            company_domain = UNSET
        else:
            company_domain = self.company_domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if linkedin_company_id is not UNSET:
            field_dict["linkedinCompanyId"] = linkedin_company_id
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url
        if company_domain is not UNSET:
            field_dict["companyDomain"] = company_domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_linkedin_company_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_company_id = _parse_linkedin_company_id(d.pop("linkedinCompanyId", UNSET))

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))

        def _parse_company_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_domain = _parse_company_domain(d.pop("companyDomain", UNSET))

        combined_search_body_company_params_investors_type_0_all_of_type_0_item = cls(
            linkedin_company_id=linkedin_company_id,
            linkedin_url=linkedin_url,
            company_domain=company_domain,
        )

        combined_search_body_company_params_investors_type_0_all_of_type_0_item.additional_properties = d
        return combined_search_body_company_params_investors_type_0_all_of_type_0_item

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
