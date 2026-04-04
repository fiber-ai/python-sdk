from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetScoutingReportResponse200OutputReportCompanyProfileType0")


@_attrs_define
class GetScoutingReportResponse200OutputReportCompanyProfileType0:
    """
    Attributes:
        name (None | str):
        headline (None | str):
        description (None | str):
        logo_url (None | str):
        website (None | str):
        linkedin_url (None | str):
        follower_count (float | None):
        employee_count (float | None):
        founded_year (float | None):
        street_address (None | str):
        locality (None | str):
        country_name (None | str):
        state_code (None | str):
        industries (list[str] | None):
        specialties (list[str] | None):
        twitter_handle (None | str):
        facebook_url (None | str):
        wellfound_slug (None | str):
    """

    name: None | str
    headline: None | str
    description: None | str
    logo_url: None | str
    website: None | str
    linkedin_url: None | str
    follower_count: float | None
    employee_count: float | None
    founded_year: float | None
    street_address: None | str
    locality: None | str
    country_name: None | str
    state_code: None | str
    industries: list[str] | None
    specialties: list[str] | None
    twitter_handle: None | str
    facebook_url: None | str
    wellfound_slug: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str
        name = self.name

        headline: None | str
        headline = self.headline

        description: None | str
        description = self.description

        logo_url: None | str
        logo_url = self.logo_url

        website: None | str
        website = self.website

        linkedin_url: None | str
        linkedin_url = self.linkedin_url

        follower_count: float | None
        follower_count = self.follower_count

        employee_count: float | None
        employee_count = self.employee_count

        founded_year: float | None
        founded_year = self.founded_year

        street_address: None | str
        street_address = self.street_address

        locality: None | str
        locality = self.locality

        country_name: None | str
        country_name = self.country_name

        state_code: None | str
        state_code = self.state_code

        industries: list[str] | None
        if isinstance(self.industries, list):
            industries = self.industries

        else:
            industries = self.industries

        specialties: list[str] | None
        if isinstance(self.specialties, list):
            specialties = self.specialties

        else:
            specialties = self.specialties

        twitter_handle: None | str
        twitter_handle = self.twitter_handle

        facebook_url: None | str
        facebook_url = self.facebook_url

        wellfound_slug: None | str
        wellfound_slug = self.wellfound_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "headline": headline,
                "description": description,
                "logoUrl": logo_url,
                "website": website,
                "linkedinUrl": linkedin_url,
                "followerCount": follower_count,
                "employeeCount": employee_count,
                "foundedYear": founded_year,
                "streetAddress": street_address,
                "locality": locality,
                "countryName": country_name,
                "stateCode": state_code,
                "industries": industries,
                "specialties": specialties,
                "twitterHandle": twitter_handle,
                "facebookUrl": facebook_url,
                "wellfoundSlug": wellfound_slug,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_headline(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        headline = _parse_headline(d.pop("headline"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_logo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo_url = _parse_logo_url(d.pop("logoUrl"))

        def _parse_website(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        website = _parse_website(d.pop("website"))

        def _parse_linkedin_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl"))

        def _parse_follower_count(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        follower_count = _parse_follower_count(d.pop("followerCount"))

        def _parse_employee_count(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        employee_count = _parse_employee_count(d.pop("employeeCount"))

        def _parse_founded_year(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        founded_year = _parse_founded_year(d.pop("foundedYear"))

        def _parse_street_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        street_address = _parse_street_address(d.pop("streetAddress"))

        def _parse_locality(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        locality = _parse_locality(d.pop("locality"))

        def _parse_country_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country_name = _parse_country_name(d.pop("countryName"))

        def _parse_state_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state_code = _parse_state_code(d.pop("stateCode"))

        def _parse_industries(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                industries_type_0 = cast(list[str], data)

                return industries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        industries = _parse_industries(d.pop("industries"))

        def _parse_specialties(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                specialties_type_0 = cast(list[str], data)

                return specialties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        specialties = _parse_specialties(d.pop("specialties"))

        def _parse_twitter_handle(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        twitter_handle = _parse_twitter_handle(d.pop("twitterHandle"))

        def _parse_facebook_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        facebook_url = _parse_facebook_url(d.pop("facebookUrl"))

        def _parse_wellfound_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        wellfound_slug = _parse_wellfound_slug(d.pop("wellfoundSlug"))

        get_scouting_report_response_200_output_report_company_profile_type_0 = cls(
            name=name,
            headline=headline,
            description=description,
            logo_url=logo_url,
            website=website,
            linkedin_url=linkedin_url,
            follower_count=follower_count,
            employee_count=employee_count,
            founded_year=founded_year,
            street_address=street_address,
            locality=locality,
            country_name=country_name,
            state_code=state_code,
            industries=industries,
            specialties=specialties,
            twitter_handle=twitter_handle,
            facebook_url=facebook_url,
            wellfound_slug=wellfound_slug,
        )

        get_scouting_report_response_200_output_report_company_profile_type_0.additional_properties = d
        return get_scouting_report_response_200_output_report_company_profile_type_0

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
