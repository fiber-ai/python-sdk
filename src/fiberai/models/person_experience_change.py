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
        is_current (bool): Whether this is a current position
        linkedin_company_id (None | str | Unset): LinkedIn company ID
        company_name (None | str | Unset): Company name
        company_linkedin_url (None | str | Unset): Company LinkedIn URL
        linkedin_company_slug (None | str | Unset): LinkedIn company vanity slug
        company_domains (list[str] | None | Unset): Known company domains
        title (None | str | Unset): Job title
        start_date (None | str | Unset): ISO start date
        end_date (None | str | Unset): ISO end date
        location (None | str | Unset): Position location
        employment_type (None | str | Unset): Employment type
        seniority (None | str | Unset): Seniority level
    """

    is_current: bool
    linkedin_company_id: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    company_linkedin_url: None | str | Unset = UNSET
    linkedin_company_slug: None | str | Unset = UNSET
    company_domains: list[str] | None | Unset = UNSET
    title: None | str | Unset = UNSET
    start_date: None | str | Unset = UNSET
    end_date: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    employment_type: None | str | Unset = UNSET
    seniority: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_current = self.is_current

        linkedin_company_id: None | str | Unset
        if isinstance(self.linkedin_company_id, Unset):
            linkedin_company_id = UNSET
        else:
            linkedin_company_id = self.linkedin_company_id

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        company_linkedin_url: None | str | Unset
        if isinstance(self.company_linkedin_url, Unset):
            company_linkedin_url = UNSET
        else:
            company_linkedin_url = self.company_linkedin_url

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

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        employment_type: None | str | Unset
        if isinstance(self.employment_type, Unset):
            employment_type = UNSET
        else:
            employment_type = self.employment_type

        seniority: None | str | Unset
        if isinstance(self.seniority, Unset):
            seniority = UNSET
        else:
            seniority = self.seniority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isCurrent": is_current,
            }
        )
        if linkedin_company_id is not UNSET:
            field_dict["linkedinCompanyId"] = linkedin_company_id
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if company_linkedin_url is not UNSET:
            field_dict["companyLinkedinUrl"] = company_linkedin_url
        if linkedin_company_slug is not UNSET:
            field_dict["linkedinCompanySlug"] = linkedin_company_slug
        if company_domains is not UNSET:
            field_dict["companyDomains"] = company_domains
        if title is not UNSET:
            field_dict["title"] = title
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if location is not UNSET:
            field_dict["location"] = location
        if employment_type is not UNSET:
            field_dict["employmentType"] = employment_type
        if seniority is not UNSET:
            field_dict["seniority"] = seniority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_current = d.pop("isCurrent")

        def _parse_linkedin_company_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_company_id = _parse_linkedin_company_id(d.pop("linkedinCompanyId", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))

        def _parse_company_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_linkedin_url = _parse_company_linkedin_url(d.pop("companyLinkedinUrl", UNSET))

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

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_start_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_date = _parse_start_date(d.pop("startDate", UNSET))

        def _parse_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_employment_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employment_type = _parse_employment_type(d.pop("employmentType", UNSET))

        def _parse_seniority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        seniority = _parse_seniority(d.pop("seniority", UNSET))

        person_experience_change = cls(
            is_current=is_current,
            linkedin_company_id=linkedin_company_id,
            company_name=company_name,
            company_linkedin_url=company_linkedin_url,
            linkedin_company_slug=linkedin_company_slug,
            company_domains=company_domains,
            title=title,
            start_date=start_date,
            end_date=end_date,
            location=location,
            employment_type=employment_type,
            seniority=seniority,
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
