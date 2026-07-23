from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonExperienceChange")


@_attrs_define
class PersonExperienceChange:
    """
    Attributes:
        linkedin_company_id (None | str): LinkedIn company ID
        company_name (None | str): Company name
        company_linkedin_url (None | str): Company LinkedIn URL
        title (None | str): Job title
        is_current (bool): Whether this is a current position
        start_date (None | str): ISO start date
        end_date (None | str): ISO end date
        location (None | str): Position location
        employment_type (None | str): Employment type
        seniority (None | str): Seniority level
        linkedin_company_slug (None | str | Unset): LinkedIn company vanity slug
        company_domains (list[str] | None | Unset): Known company domains
    """

    linkedin_company_id: None | str
    company_name: None | str
    company_linkedin_url: None | str
    title: None | str
    is_current: bool
    start_date: None | str
    end_date: None | str
    location: None | str
    employment_type: None | str
    seniority: None | str
    linkedin_company_slug: None | str | Unset = UNSET
    company_domains: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_company_id: None | str
        linkedin_company_id = self.linkedin_company_id

        company_name: None | str
        company_name = self.company_name

        company_linkedin_url: None | str
        company_linkedin_url = self.company_linkedin_url

        title: None | str
        title = self.title

        is_current = self.is_current

        start_date: None | str
        start_date = self.start_date

        end_date: None | str
        end_date = self.end_date

        location: None | str
        location = self.location

        employment_type: None | str
        employment_type = self.employment_type

        seniority: None | str
        seniority = self.seniority

        linkedin_company_slug: None | str | Unset
        if isinstance(self.linkedin_company_slug, Unset):
            linkedin_company_slug = UNSET
        else:
            linkedin_company_slug = self.linkedin_company_slug

        company_domains: list[str] | None | Unset
        if isinstance(self.company_domains, Unset):
            company_domains = UNSET
        elif isinstance(self.company_domains, list):
            company_domains = self.company_domains

        else:
            company_domains = self.company_domains

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "linkedinCompanyId": linkedin_company_id,
                "companyName": company_name,
                "companyLinkedinUrl": company_linkedin_url,
                "title": title,
                "isCurrent": is_current,
                "startDate": start_date,
                "endDate": end_date,
                "location": location,
                "employmentType": employment_type,
                "seniority": seniority,
            }
        )
        if linkedin_company_slug is not UNSET:
            field_dict["linkedinCompanySlug"] = linkedin_company_slug
        if company_domains is not UNSET:
            field_dict["companyDomains"] = company_domains

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_linkedin_company_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linkedin_company_id = _parse_linkedin_company_id(d.pop("linkedinCompanyId"))

        def _parse_company_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        company_name = _parse_company_name(d.pop("companyName"))

        def _parse_company_linkedin_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        company_linkedin_url = _parse_company_linkedin_url(d.pop("companyLinkedinUrl"))

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        is_current = d.pop("isCurrent")

        def _parse_start_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        start_date = _parse_start_date(d.pop("startDate"))

        def _parse_end_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        end_date = _parse_end_date(d.pop("endDate"))

        def _parse_location(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        location = _parse_location(d.pop("location"))

        def _parse_employment_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        employment_type = _parse_employment_type(d.pop("employmentType"))

        def _parse_seniority(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        seniority = _parse_seniority(d.pop("seniority"))

        def _parse_linkedin_company_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_company_slug = _parse_linkedin_company_slug(d.pop("linkedinCompanySlug", UNSET))

        def _parse_company_domains(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                company_domains_type_0 = cast(list[str], data)

                return company_domains_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        company_domains = _parse_company_domains(d.pop("companyDomains", UNSET))

        person_experience_change = cls(
            linkedin_company_id=linkedin_company_id,
            company_name=company_name,
            company_linkedin_url=company_linkedin_url,
            title=title,
            is_current=is_current,
            start_date=start_date,
            end_date=end_date,
            location=location,
            employment_type=employment_type,
            seniority=seniority,
            linkedin_company_slug=linkedin_company_slug,
            company_domains=company_domains,
        )

        person_experience_change.additional_properties = d
        return person_experience_change

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
