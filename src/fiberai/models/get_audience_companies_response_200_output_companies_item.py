from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAudienceCompaniesResponse200OutputCompaniesItem")


@_attrs_define
class GetAudienceCompaniesResponse200OutputCompaniesItem:
    """
    Attributes:
        company_id (str): Unique ID of the company
        name (None | str | Unset): Company name
        linkedin_url (None | str | Unset): LinkedIn URL
        domain (None | str | Unset): Company domain
        industry (None | str | Unset): Industry
        headcount (float | None | Unset): Employee count
    """

    company_id: str
    name: None | str | Unset = UNSET
    linkedin_url: None | str | Unset = UNSET
    domain: None | str | Unset = UNSET
    industry: None | str | Unset = UNSET
    headcount: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        industry: None | str | Unset
        if isinstance(self.industry, Unset):
            industry = UNSET
        else:
            industry = self.industry

        headcount: float | None | Unset
        if isinstance(self.headcount, Unset):
            headcount = UNSET
        else:
            headcount = self.headcount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyId": company_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url
        if domain is not UNSET:
            field_dict["domain"] = domain
        if industry is not UNSET:
            field_dict["industry"] = industry
        if headcount is not UNSET:
            field_dict["headcount"] = headcount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("companyId")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        def _parse_industry(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        industry = _parse_industry(d.pop("industry", UNSET))

        def _parse_headcount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        headcount = _parse_headcount(d.pop("headcount", UNSET))

        get_audience_companies_response_200_output_companies_item = cls(
            company_id=company_id,
            name=name,
            linkedin_url=linkedin_url,
            domain=domain,
            industry=industry,
            headcount=headcount,
        )

        get_audience_companies_response_200_output_companies_item.additional_properties = d
        return get_audience_companies_response_200_output_companies_item

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
