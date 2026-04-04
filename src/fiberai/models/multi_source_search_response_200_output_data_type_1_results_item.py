from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiSourceSearchResponse200OutputDataType1ResultsItem")


@_attrs_define
class MultiSourceSearchResponse200OutputDataType1ResultsItem:
    """
    Attributes:
        first_name (None | str | Unset): First name
        last_name (None | str | Unset): Last name
        job_title (None | str | Unset): Job title
        headline (None | str | Unset): LinkedIn headline
        linkedin_url (None | str | Unset): LinkedIn profile URL
        country_code (None | str | Unset): Person's country (ISO alpha-3 code, e.g. USA)
        company_name (None | str | Unset): The person's current company name
        company_domain (None | str | Unset): The person's current company domain
        company_linkedin_url (None | str | Unset): The person's current company LinkedIn URL
        company_city (None | str | Unset): The person's current company city
        company_country_code (None | str | Unset): The person's current company headquarters country (ISO alpha-3 code,
            e.g. USA)
    """

    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    job_title: None | str | Unset = UNSET
    headline: None | str | Unset = UNSET
    linkedin_url: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    company_domain: None | str | Unset = UNSET
    company_linkedin_url: None | str | Unset = UNSET
    company_city: None | str | Unset = UNSET
    company_country_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        job_title: None | str | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        else:
            job_title = self.job_title

        headline: None | str | Unset
        if isinstance(self.headline, Unset):
            headline = UNSET
        else:
            headline = self.headline

        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        company_domain: None | str | Unset
        if isinstance(self.company_domain, Unset):
            company_domain = UNSET
        else:
            company_domain = self.company_domain

        company_linkedin_url: None | str | Unset
        if isinstance(self.company_linkedin_url, Unset):
            company_linkedin_url = UNSET
        else:
            company_linkedin_url = self.company_linkedin_url

        company_city: None | str | Unset
        if isinstance(self.company_city, Unset):
            company_city = UNSET
        else:
            company_city = self.company_city

        company_country_code: None | str | Unset
        if isinstance(self.company_country_code, Unset):
            company_country_code = UNSET
        else:
            company_country_code = self.company_country_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if headline is not UNSET:
            field_dict["headline"] = headline
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if company_domain is not UNSET:
            field_dict["companyDomain"] = company_domain
        if company_linkedin_url is not UNSET:
            field_dict["companyLinkedinUrl"] = company_linkedin_url
        if company_city is not UNSET:
            field_dict["companyCity"] = company_city
        if company_country_code is not UNSET:
            field_dict["companyCountryCode"] = company_country_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("firstName", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("lastName", UNSET))

        def _parse_job_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))

        def _parse_headline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        headline = _parse_headline(d.pop("headline", UNSET))

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))

        def _parse_company_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_domain = _parse_company_domain(d.pop("companyDomain", UNSET))

        def _parse_company_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_linkedin_url = _parse_company_linkedin_url(d.pop("companyLinkedinUrl", UNSET))

        def _parse_company_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_city = _parse_company_city(d.pop("companyCity", UNSET))

        def _parse_company_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_country_code = _parse_company_country_code(d.pop("companyCountryCode", UNSET))

        multi_source_search_response_200_output_data_type_1_results_item = cls(
            first_name=first_name,
            last_name=last_name,
            job_title=job_title,
            headline=headline,
            linkedin_url=linkedin_url,
            country_code=country_code,
            company_name=company_name,
            company_domain=company_domain,
            company_linkedin_url=company_linkedin_url,
            company_city=company_city,
            company_country_code=company_country_code,
        )

        multi_source_search_response_200_output_data_type_1_results_item.additional_properties = d
        return multi_source_search_response_200_output_data_type_1_results_item

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
