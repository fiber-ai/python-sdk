from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiSourceSearchResponse200OutputDataType0ResultsItem")


@_attrs_define
class MultiSourceSearchResponse200OutputDataType0ResultsItem:
    """
    Attributes:
        name (None | str | Unset): Company name
        domain (None | str | Unset): Company domain
        website_url (None | str | Unset): Company website URL
        linkedin_url (None | str | Unset): LinkedIn company page URL using the numeric company ID (e.g.
            https://linkedin.com/company/1234). Null if unavailable.
        industry (None | str | Unset): Primary industry. The value comes from the data provider and may vary in format.
        employee_count (int | None | Unset): Estimated employee count
        city (None | str | Unset): Company city
        country_code (None | str | Unset): Company country (ISO alpha-3 code, e.g. USA)
        founded_year (int | None | Unset): Year the company was founded
        description (None | str | Unset): Company description
    """

    name: None | str | Unset = UNSET
    domain: None | str | Unset = UNSET
    website_url: None | str | Unset = UNSET
    linkedin_url: None | str | Unset = UNSET
    industry: None | str | Unset = UNSET
    employee_count: int | None | Unset = UNSET
    city: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    founded_year: int | None | Unset = UNSET
    description: None | str | Unset = UNSET
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

        website_url: None | str | Unset
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        industry: None | str | Unset
        if isinstance(self.industry, Unset):
            industry = UNSET
        else:
            industry = self.industry

        employee_count: int | None | Unset
        if isinstance(self.employee_count, Unset):
            employee_count = UNSET
        else:
            employee_count = self.employee_count

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        founded_year: int | None | Unset
        if isinstance(self.founded_year, Unset):
            founded_year = UNSET
        else:
            founded_year = self.founded_year

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if domain is not UNSET:
            field_dict["domain"] = domain
        if website_url is not UNSET:
            field_dict["websiteUrl"] = website_url
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url
        if industry is not UNSET:
            field_dict["industry"] = industry
        if employee_count is not UNSET:
            field_dict["employeeCount"] = employee_count
        if city is not UNSET:
            field_dict["city"] = city
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if founded_year is not UNSET:
            field_dict["foundedYear"] = founded_year
        if description is not UNSET:
            field_dict["description"] = description

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

        def _parse_website_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_url = _parse_website_url(d.pop("websiteUrl", UNSET))

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))

        def _parse_industry(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        industry = _parse_industry(d.pop("industry", UNSET))

        def _parse_employee_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        employee_count = _parse_employee_count(d.pop("employeeCount", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        def _parse_founded_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        founded_year = _parse_founded_year(d.pop("foundedYear", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        multi_source_search_response_200_output_data_type_0_results_item = cls(
            name=name,
            domain=domain,
            website_url=website_url,
            linkedin_url=linkedin_url,
            industry=industry,
            employee_count=employee_count,
            city=city,
            country_code=country_code,
            founded_year=founded_year,
            description=description,
        )

        multi_source_search_response_200_output_data_type_0_results_item.additional_properties = d
        return multi_source_search_response_200_output_data_type_0_results_item

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
