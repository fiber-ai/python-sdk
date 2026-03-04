from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.company_live_enrich_response_200_output_company_industries_type_0_item import CompanyLiveEnrichResponse200OutputCompanyIndustriesType0Item
  from ..models.company_live_enrich_response_200_output_company_locations_type_0_item import CompanyLiveEnrichResponse200OutputCompanyLocationsType0Item
  from ..models.company_live_enrich_response_200_output_company_locations_stats_type_0 import CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0
  from ..models.company_live_enrich_response_200_output_company_inferred_location_type_0 import CompanyLiveEnrichResponse200OutputCompanyInferredLocationType0





T = TypeVar("T", bound="CompanyLiveEnrichResponse200OutputCompany")



@_attrs_define
class CompanyLiveEnrichResponse200OutputCompany:
    """ The company that was found and enriched else a 404 HTTP code is returned

        Attributes:
            slug (str):
            headline (Union[None, Unset, str]):
            description (Union[None, Unset, str]):
            employee_count (Union[None, Unset, float]):
            follower_count (Union[None, Unset, float]):
            founded_year (Union[None, Unset, float]):
            industries (Union[None, Unset, list['CompanyLiveEnrichResponse200OutputCompanyIndustriesType0Item']]):
            inferred_location (Union['CompanyLiveEnrichResponse200OutputCompanyInferredLocationType0', None, Unset]):
            linkedin_url (Union[None, Unset, str]):
            locations (Union[None, Unset, list['CompanyLiveEnrichResponse200OutputCompanyLocationsType0Item']]):
            naics_codes (Union[None, Unset, list[str]]):
            name (Union[None, Unset, str]):
            org_id (Union[None, Unset, str]):
            specialties (Union[None, Unset, list[str]]):
            ticker (Union[None, Unset, str]):
            type_ (Union[None, Unset, str]):
            domain (Union[None, Unset, str]):
            website (Union[None, Unset, str]):
            est_employee_count_lower_bound (Union[None, Unset, float]):
            est_employee_count_upper_bound (Union[None, Unset, float]):
            standardized_industries (Union[None, Unset, list[str]]):
            locations_stats (Union['CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0', None, Unset]):
            logo_url (Union[None, Unset, str]):
            revenue_usd_lower_bound (Union[None, Unset, str]):
            revenue_usd_upper_bound (Union[None, Unset, str]):
     """

    slug: str
    headline: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    employee_count: Union[None, Unset, float] = UNSET
    follower_count: Union[None, Unset, float] = UNSET
    founded_year: Union[None, Unset, float] = UNSET
    industries: Union[None, Unset, list['CompanyLiveEnrichResponse200OutputCompanyIndustriesType0Item']] = UNSET
    inferred_location: Union['CompanyLiveEnrichResponse200OutputCompanyInferredLocationType0', None, Unset] = UNSET
    linkedin_url: Union[None, Unset, str] = UNSET
    locations: Union[None, Unset, list['CompanyLiveEnrichResponse200OutputCompanyLocationsType0Item']] = UNSET
    naics_codes: Union[None, Unset, list[str]] = UNSET
    name: Union[None, Unset, str] = UNSET
    org_id: Union[None, Unset, str] = UNSET
    specialties: Union[None, Unset, list[str]] = UNSET
    ticker: Union[None, Unset, str] = UNSET
    type_: Union[None, Unset, str] = UNSET
    domain: Union[None, Unset, str] = UNSET
    website: Union[None, Unset, str] = UNSET
    est_employee_count_lower_bound: Union[None, Unset, float] = UNSET
    est_employee_count_upper_bound: Union[None, Unset, float] = UNSET
    standardized_industries: Union[None, Unset, list[str]] = UNSET
    locations_stats: Union['CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0', None, Unset] = UNSET
    logo_url: Union[None, Unset, str] = UNSET
    revenue_usd_lower_bound: Union[None, Unset, str] = UNSET
    revenue_usd_upper_bound: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.company_live_enrich_response_200_output_company_industries_type_0_item import CompanyLiveEnrichResponse200OutputCompanyIndustriesType0Item
        from ..models.company_live_enrich_response_200_output_company_locations_type_0_item import CompanyLiveEnrichResponse200OutputCompanyLocationsType0Item
        from ..models.company_live_enrich_response_200_output_company_locations_stats_type_0 import CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0
        from ..models.company_live_enrich_response_200_output_company_inferred_location_type_0 import CompanyLiveEnrichResponse200OutputCompanyInferredLocationType0
        slug = self.slug

        headline: Union[None, Unset, str]
        if isinstance(self.headline, Unset):
            headline = UNSET
        else:
            headline = self.headline

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        employee_count: Union[None, Unset, float]
        if isinstance(self.employee_count, Unset):
            employee_count = UNSET
        else:
            employee_count = self.employee_count

        follower_count: Union[None, Unset, float]
        if isinstance(self.follower_count, Unset):
            follower_count = UNSET
        else:
            follower_count = self.follower_count

        founded_year: Union[None, Unset, float]
        if isinstance(self.founded_year, Unset):
            founded_year = UNSET
        else:
            founded_year = self.founded_year

        industries: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.industries, Unset):
            industries = UNSET
        elif isinstance(self.industries, list):
            industries = []
            for industries_type_0_item_data in self.industries:
                industries_type_0_item = industries_type_0_item_data.to_dict()
                industries.append(industries_type_0_item)


        else:
            industries = self.industries

        inferred_location: Union[None, Unset, dict[str, Any]]
        if isinstance(self.inferred_location, Unset):
            inferred_location = UNSET
        elif isinstance(self.inferred_location, CompanyLiveEnrichResponse200OutputCompanyInferredLocationType0):
            inferred_location = self.inferred_location.to_dict()
        else:
            inferred_location = self.inferred_location

        linkedin_url: Union[None, Unset, str]
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        locations: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.locations, Unset):
            locations = UNSET
        elif isinstance(self.locations, list):
            locations = []
            for locations_type_0_item_data in self.locations:
                locations_type_0_item = locations_type_0_item_data.to_dict()
                locations.append(locations_type_0_item)


        else:
            locations = self.locations

        naics_codes: Union[None, Unset, list[str]]
        if isinstance(self.naics_codes, Unset):
            naics_codes = UNSET
        elif isinstance(self.naics_codes, list):
            naics_codes = self.naics_codes


        else:
            naics_codes = self.naics_codes

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        org_id: Union[None, Unset, str]
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        else:
            org_id = self.org_id

        specialties: Union[None, Unset, list[str]]
        if isinstance(self.specialties, Unset):
            specialties = UNSET
        elif isinstance(self.specialties, list):
            specialties = self.specialties


        else:
            specialties = self.specialties

        ticker: Union[None, Unset, str]
        if isinstance(self.ticker, Unset):
            ticker = UNSET
        else:
            ticker = self.ticker

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        domain: Union[None, Unset, str]
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        website: Union[None, Unset, str]
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        est_employee_count_lower_bound: Union[None, Unset, float]
        if isinstance(self.est_employee_count_lower_bound, Unset):
            est_employee_count_lower_bound = UNSET
        else:
            est_employee_count_lower_bound = self.est_employee_count_lower_bound

        est_employee_count_upper_bound: Union[None, Unset, float]
        if isinstance(self.est_employee_count_upper_bound, Unset):
            est_employee_count_upper_bound = UNSET
        else:
            est_employee_count_upper_bound = self.est_employee_count_upper_bound

        standardized_industries: Union[None, Unset, list[str]]
        if isinstance(self.standardized_industries, Unset):
            standardized_industries = UNSET
        elif isinstance(self.standardized_industries, list):
            standardized_industries = self.standardized_industries


        else:
            standardized_industries = self.standardized_industries

        locations_stats: Union[None, Unset, dict[str, Any]]
        if isinstance(self.locations_stats, Unset):
            locations_stats = UNSET
        elif isinstance(self.locations_stats, CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0):
            locations_stats = self.locations_stats.to_dict()
        else:
            locations_stats = self.locations_stats

        logo_url: Union[None, Unset, str]
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        revenue_usd_lower_bound: Union[None, Unset, str]
        if isinstance(self.revenue_usd_lower_bound, Unset):
            revenue_usd_lower_bound = UNSET
        else:
            revenue_usd_lower_bound = self.revenue_usd_lower_bound

        revenue_usd_upper_bound: Union[None, Unset, str]
        if isinstance(self.revenue_usd_upper_bound, Unset):
            revenue_usd_upper_bound = UNSET
        else:
            revenue_usd_upper_bound = self.revenue_usd_upper_bound


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "slug": slug,
        })
        if headline is not UNSET:
            field_dict["headline"] = headline
        if description is not UNSET:
            field_dict["description"] = description
        if employee_count is not UNSET:
            field_dict["employee_count"] = employee_count
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count
        if founded_year is not UNSET:
            field_dict["founded_year"] = founded_year
        if industries is not UNSET:
            field_dict["industries"] = industries
        if inferred_location is not UNSET:
            field_dict["inferred_location"] = inferred_location
        if linkedin_url is not UNSET:
            field_dict["linkedin_url"] = linkedin_url
        if locations is not UNSET:
            field_dict["locations"] = locations
        if naics_codes is not UNSET:
            field_dict["naics_codes"] = naics_codes
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if specialties is not UNSET:
            field_dict["specialties"] = specialties
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if type_ is not UNSET:
            field_dict["type"] = type_
        if domain is not UNSET:
            field_dict["domain"] = domain
        if website is not UNSET:
            field_dict["website"] = website
        if est_employee_count_lower_bound is not UNSET:
            field_dict["est_employee_count_lower_bound"] = est_employee_count_lower_bound
        if est_employee_count_upper_bound is not UNSET:
            field_dict["est_employee_count_upper_bound"] = est_employee_count_upper_bound
        if standardized_industries is not UNSET:
            field_dict["standardized_industries"] = standardized_industries
        if locations_stats is not UNSET:
            field_dict["locations_stats"] = locations_stats
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if revenue_usd_lower_bound is not UNSET:
            field_dict["revenue_usd_lower_bound"] = revenue_usd_lower_bound
        if revenue_usd_upper_bound is not UNSET:
            field_dict["revenue_usd_upper_bound"] = revenue_usd_upper_bound

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_live_enrich_response_200_output_company_industries_type_0_item import CompanyLiveEnrichResponse200OutputCompanyIndustriesType0Item
        from ..models.company_live_enrich_response_200_output_company_locations_type_0_item import CompanyLiveEnrichResponse200OutputCompanyLocationsType0Item
        from ..models.company_live_enrich_response_200_output_company_locations_stats_type_0 import CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0
        from ..models.company_live_enrich_response_200_output_company_inferred_location_type_0 import CompanyLiveEnrichResponse200OutputCompanyInferredLocationType0
        d = dict(src_dict)
        slug = d.pop("slug")

        def _parse_headline(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        headline = _parse_headline(d.pop("headline", UNSET))


        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_employee_count(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        employee_count = _parse_employee_count(d.pop("employee_count", UNSET))


        def _parse_follower_count(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        follower_count = _parse_follower_count(d.pop("follower_count", UNSET))


        def _parse_founded_year(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        founded_year = _parse_founded_year(d.pop("founded_year", UNSET))


        def _parse_industries(data: object) -> Union[None, Unset, list['CompanyLiveEnrichResponse200OutputCompanyIndustriesType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                industries_type_0 = []
                _industries_type_0 = data
                for industries_type_0_item_data in (_industries_type_0):
                    industries_type_0_item = CompanyLiveEnrichResponse200OutputCompanyIndustriesType0Item.from_dict(industries_type_0_item_data)



                    industries_type_0.append(industries_type_0_item)

                return industries_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['CompanyLiveEnrichResponse200OutputCompanyIndustriesType0Item']], data)

        industries = _parse_industries(d.pop("industries", UNSET))


        def _parse_inferred_location(data: object) -> Union['CompanyLiveEnrichResponse200OutputCompanyInferredLocationType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                inferred_location_type_0 = CompanyLiveEnrichResponse200OutputCompanyInferredLocationType0.from_dict(data)



                return inferred_location_type_0
            except: # noqa: E722
                pass
            return cast(Union['CompanyLiveEnrichResponse200OutputCompanyInferredLocationType0', None, Unset], data)

        inferred_location = _parse_inferred_location(d.pop("inferred_location", UNSET))


        def _parse_linkedin_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedin_url", UNSET))


        def _parse_locations(data: object) -> Union[None, Unset, list['CompanyLiveEnrichResponse200OutputCompanyLocationsType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                locations_type_0 = []
                _locations_type_0 = data
                for locations_type_0_item_data in (_locations_type_0):
                    locations_type_0_item = CompanyLiveEnrichResponse200OutputCompanyLocationsType0Item.from_dict(locations_type_0_item_data)



                    locations_type_0.append(locations_type_0_item)

                return locations_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['CompanyLiveEnrichResponse200OutputCompanyLocationsType0Item']], data)

        locations = _parse_locations(d.pop("locations", UNSET))


        def _parse_naics_codes(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                naics_codes_type_0 = cast(list[str], data)

                return naics_codes_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        naics_codes = _parse_naics_codes(d.pop("naics_codes", UNSET))


        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_org_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        org_id = _parse_org_id(d.pop("org_id", UNSET))


        def _parse_specialties(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                specialties_type_0 = cast(list[str], data)

                return specialties_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        specialties = _parse_specialties(d.pop("specialties", UNSET))


        def _parse_ticker(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ticker = _parse_ticker(d.pop("ticker", UNSET))


        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_domain(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        domain = _parse_domain(d.pop("domain", UNSET))


        def _parse_website(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        website = _parse_website(d.pop("website", UNSET))


        def _parse_est_employee_count_lower_bound(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        est_employee_count_lower_bound = _parse_est_employee_count_lower_bound(d.pop("est_employee_count_lower_bound", UNSET))


        def _parse_est_employee_count_upper_bound(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        est_employee_count_upper_bound = _parse_est_employee_count_upper_bound(d.pop("est_employee_count_upper_bound", UNSET))


        def _parse_standardized_industries(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                standardized_industries_type_0 = cast(list[str], data)

                return standardized_industries_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        standardized_industries = _parse_standardized_industries(d.pop("standardized_industries", UNSET))


        def _parse_locations_stats(data: object) -> Union['CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                locations_stats_type_0 = CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0.from_dict(data)



                return locations_stats_type_0
            except: # noqa: E722
                pass
            return cast(Union['CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0', None, Unset], data)

        locations_stats = _parse_locations_stats(d.pop("locations_stats", UNSET))


        def _parse_logo_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))


        def _parse_revenue_usd_lower_bound(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        revenue_usd_lower_bound = _parse_revenue_usd_lower_bound(d.pop("revenue_usd_lower_bound", UNSET))


        def _parse_revenue_usd_upper_bound(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        revenue_usd_upper_bound = _parse_revenue_usd_upper_bound(d.pop("revenue_usd_upper_bound", UNSET))


        company_live_enrich_response_200_output_company = cls(
            slug=slug,
            headline=headline,
            description=description,
            employee_count=employee_count,
            follower_count=follower_count,
            founded_year=founded_year,
            industries=industries,
            inferred_location=inferred_location,
            linkedin_url=linkedin_url,
            locations=locations,
            naics_codes=naics_codes,
            name=name,
            org_id=org_id,
            specialties=specialties,
            ticker=ticker,
            type_=type_,
            domain=domain,
            website=website,
            est_employee_count_lower_bound=est_employee_count_lower_bound,
            est_employee_count_upper_bound=est_employee_count_upper_bound,
            standardized_industries=standardized_industries,
            locations_stats=locations_stats,
            logo_url=logo_url,
            revenue_usd_lower_bound=revenue_usd_lower_bound,
            revenue_usd_upper_bound=revenue_usd_upper_bound,
        )


        company_live_enrich_response_200_output_company.additional_properties = d
        return company_live_enrich_response_200_output_company

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
