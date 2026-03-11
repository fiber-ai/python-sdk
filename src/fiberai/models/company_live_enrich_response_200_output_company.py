from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_live_enrich_response_200_output_company_historical_headcount_type_0 import (
        CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0,
    )
    from ..models.company_live_enrich_response_200_output_company_industries_type_0_item import (
        CompanyLiveEnrichResponse200OutputCompanyIndustriesType0Item,
    )
    from ..models.company_live_enrich_response_200_output_company_inferred_location_type_0 import (
        CompanyLiveEnrichResponse200OutputCompanyInferredLocationType0,
    )
    from ..models.company_live_enrich_response_200_output_company_locations_stats_type_0 import (
        CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0,
    )
    from ..models.company_live_enrich_response_200_output_company_locations_type_0_item import (
        CompanyLiveEnrichResponse200OutputCompanyLocationsType0Item,
    )


T = TypeVar("T", bound="CompanyLiveEnrichResponse200OutputCompany")


@_attrs_define
class CompanyLiveEnrichResponse200OutputCompany:
    """The company that was found and enriched else a 404 HTTP code is returned

    Attributes:
        slug (str):
        headline (None | str | Unset):
        description (None | str | Unset):
        employee_count (float | None | Unset):
        follower_count (float | None | Unset):
        founded_year (float | None | Unset):
        industries (list[CompanyLiveEnrichResponse200OutputCompanyIndustriesType0Item] | None | Unset):
        inferred_location (CompanyLiveEnrichResponse200OutputCompanyInferredLocationType0 | None | Unset):
        linkedin_url (None | str | Unset):
        locations (list[CompanyLiveEnrichResponse200OutputCompanyLocationsType0Item] | None | Unset):
        naics_codes (list[str] | None | Unset):
        name (None | str | Unset):
        org_id (None | str | Unset):
        specialties (list[str] | None | Unset):
        ticker (None | str | Unset):
        type_ (None | str | Unset):
        domain (None | str | Unset):
        website (None | str | Unset):
        est_employee_count_lower_bound (float | None | Unset):
        est_employee_count_upper_bound (float | None | Unset):
        standardized_industries (list[str] | None | Unset):
        locations_stats (CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0 | None | Unset):
        logo_url (None | str | Unset):
        historical_headcount (CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0 | None | Unset):
        revenue_usd_lower_bound (None | str | Unset):
        revenue_usd_upper_bound (None | str | Unset):
    """

    slug: str
    headline: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    employee_count: float | None | Unset = UNSET
    follower_count: float | None | Unset = UNSET
    founded_year: float | None | Unset = UNSET
    industries: list[CompanyLiveEnrichResponse200OutputCompanyIndustriesType0Item] | None | Unset = UNSET
    inferred_location: CompanyLiveEnrichResponse200OutputCompanyInferredLocationType0 | None | Unset = UNSET
    linkedin_url: None | str | Unset = UNSET
    locations: list[CompanyLiveEnrichResponse200OutputCompanyLocationsType0Item] | None | Unset = UNSET
    naics_codes: list[str] | None | Unset = UNSET
    name: None | str | Unset = UNSET
    org_id: None | str | Unset = UNSET
    specialties: list[str] | None | Unset = UNSET
    ticker: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    domain: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    est_employee_count_lower_bound: float | None | Unset = UNSET
    est_employee_count_upper_bound: float | None | Unset = UNSET
    standardized_industries: list[str] | None | Unset = UNSET
    locations_stats: CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0 | None | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    historical_headcount: CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0 | None | Unset = UNSET
    revenue_usd_lower_bound: None | str | Unset = UNSET
    revenue_usd_upper_bound: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_live_enrich_response_200_output_company_historical_headcount_type_0 import (
            CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0,
        )
        from ..models.company_live_enrich_response_200_output_company_inferred_location_type_0 import (
            CompanyLiveEnrichResponse200OutputCompanyInferredLocationType0,
        )
        from ..models.company_live_enrich_response_200_output_company_locations_stats_type_0 import (
            CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0,
        )

        slug = self.slug

        headline: None | str | Unset
        if isinstance(self.headline, Unset):
            headline = UNSET
        else:
            headline = self.headline

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        employee_count: float | None | Unset
        if isinstance(self.employee_count, Unset):
            employee_count = UNSET
        else:
            employee_count = self.employee_count

        follower_count: float | None | Unset
        if isinstance(self.follower_count, Unset):
            follower_count = UNSET
        else:
            follower_count = self.follower_count

        founded_year: float | None | Unset
        if isinstance(self.founded_year, Unset):
            founded_year = UNSET
        else:
            founded_year = self.founded_year

        industries: list[dict[str, Any]] | None | Unset
        if isinstance(self.industries, Unset):
            industries = UNSET
        elif isinstance(self.industries, list):
            industries = []
            for industries_type_0_item_data in self.industries:
                industries_type_0_item = industries_type_0_item_data.to_dict()
                industries.append(industries_type_0_item)

        else:
            industries = self.industries

        inferred_location: dict[str, Any] | None | Unset
        if isinstance(self.inferred_location, Unset):
            inferred_location = UNSET
        elif isinstance(self.inferred_location, CompanyLiveEnrichResponse200OutputCompanyInferredLocationType0):
            inferred_location = self.inferred_location.to_dict()
        else:
            inferred_location = self.inferred_location

        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        locations: list[dict[str, Any]] | None | Unset
        if isinstance(self.locations, Unset):
            locations = UNSET
        elif isinstance(self.locations, list):
            locations = []
            for locations_type_0_item_data in self.locations:
                locations_type_0_item = locations_type_0_item_data.to_dict()
                locations.append(locations_type_0_item)

        else:
            locations = self.locations

        naics_codes: list[str] | None | Unset
        if isinstance(self.naics_codes, Unset):
            naics_codes = UNSET
        elif isinstance(self.naics_codes, list):
            naics_codes = self.naics_codes

        else:
            naics_codes = self.naics_codes

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        else:
            org_id = self.org_id

        specialties: list[str] | None | Unset
        if isinstance(self.specialties, Unset):
            specialties = UNSET
        elif isinstance(self.specialties, list):
            specialties = self.specialties

        else:
            specialties = self.specialties

        ticker: None | str | Unset
        if isinstance(self.ticker, Unset):
            ticker = UNSET
        else:
            ticker = self.ticker

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        est_employee_count_lower_bound: float | None | Unset
        if isinstance(self.est_employee_count_lower_bound, Unset):
            est_employee_count_lower_bound = UNSET
        else:
            est_employee_count_lower_bound = self.est_employee_count_lower_bound

        est_employee_count_upper_bound: float | None | Unset
        if isinstance(self.est_employee_count_upper_bound, Unset):
            est_employee_count_upper_bound = UNSET
        else:
            est_employee_count_upper_bound = self.est_employee_count_upper_bound

        standardized_industries: list[str] | None | Unset
        if isinstance(self.standardized_industries, Unset):
            standardized_industries = UNSET
        elif isinstance(self.standardized_industries, list):
            standardized_industries = self.standardized_industries

        else:
            standardized_industries = self.standardized_industries

        locations_stats: dict[str, Any] | None | Unset
        if isinstance(self.locations_stats, Unset):
            locations_stats = UNSET
        elif isinstance(self.locations_stats, CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0):
            locations_stats = self.locations_stats.to_dict()
        else:
            locations_stats = self.locations_stats

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        historical_headcount: dict[str, Any] | None | Unset
        if isinstance(self.historical_headcount, Unset):
            historical_headcount = UNSET
        elif isinstance(self.historical_headcount, CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0):
            historical_headcount = self.historical_headcount.to_dict()
        else:
            historical_headcount = self.historical_headcount

        revenue_usd_lower_bound: None | str | Unset
        if isinstance(self.revenue_usd_lower_bound, Unset):
            revenue_usd_lower_bound = UNSET
        else:
            revenue_usd_lower_bound = self.revenue_usd_lower_bound

        revenue_usd_upper_bound: None | str | Unset
        if isinstance(self.revenue_usd_upper_bound, Unset):
            revenue_usd_upper_bound = UNSET
        else:
            revenue_usd_upper_bound = self.revenue_usd_upper_bound

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
            }
        )
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
        if historical_headcount is not UNSET:
            field_dict["historical_headcount"] = historical_headcount
        if revenue_usd_lower_bound is not UNSET:
            field_dict["revenue_usd_lower_bound"] = revenue_usd_lower_bound
        if revenue_usd_upper_bound is not UNSET:
            field_dict["revenue_usd_upper_bound"] = revenue_usd_upper_bound

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_live_enrich_response_200_output_company_historical_headcount_type_0 import (
            CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0,
        )
        from ..models.company_live_enrich_response_200_output_company_industries_type_0_item import (
            CompanyLiveEnrichResponse200OutputCompanyIndustriesType0Item,
        )
        from ..models.company_live_enrich_response_200_output_company_inferred_location_type_0 import (
            CompanyLiveEnrichResponse200OutputCompanyInferredLocationType0,
        )
        from ..models.company_live_enrich_response_200_output_company_locations_stats_type_0 import (
            CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0,
        )
        from ..models.company_live_enrich_response_200_output_company_locations_type_0_item import (
            CompanyLiveEnrichResponse200OutputCompanyLocationsType0Item,
        )

        d = dict(src_dict)
        slug = d.pop("slug")

        def _parse_headline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        headline = _parse_headline(d.pop("headline", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_employee_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        employee_count = _parse_employee_count(d.pop("employee_count", UNSET))

        def _parse_follower_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        follower_count = _parse_follower_count(d.pop("follower_count", UNSET))

        def _parse_founded_year(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        founded_year = _parse_founded_year(d.pop("founded_year", UNSET))

        def _parse_industries(
            data: object,
        ) -> list[CompanyLiveEnrichResponse200OutputCompanyIndustriesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                industries_type_0 = []
                _industries_type_0 = data
                for industries_type_0_item_data in _industries_type_0:
                    industries_type_0_item = CompanyLiveEnrichResponse200OutputCompanyIndustriesType0Item.from_dict(
                        industries_type_0_item_data
                    )

                    industries_type_0.append(industries_type_0_item)

                return industries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanyLiveEnrichResponse200OutputCompanyIndustriesType0Item] | None | Unset, data)

        industries = _parse_industries(d.pop("industries", UNSET))

        def _parse_inferred_location(
            data: object,
        ) -> CompanyLiveEnrichResponse200OutputCompanyInferredLocationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                inferred_location_type_0 = CompanyLiveEnrichResponse200OutputCompanyInferredLocationType0.from_dict(
                    data
                )

                return inferred_location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyLiveEnrichResponse200OutputCompanyInferredLocationType0 | None | Unset, data)

        inferred_location = _parse_inferred_location(d.pop("inferred_location", UNSET))

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedin_url", UNSET))

        def _parse_locations(
            data: object,
        ) -> list[CompanyLiveEnrichResponse200OutputCompanyLocationsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                locations_type_0 = []
                _locations_type_0 = data
                for locations_type_0_item_data in _locations_type_0:
                    locations_type_0_item = CompanyLiveEnrichResponse200OutputCompanyLocationsType0Item.from_dict(
                        locations_type_0_item_data
                    )

                    locations_type_0.append(locations_type_0_item)

                return locations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanyLiveEnrichResponse200OutputCompanyLocationsType0Item] | None | Unset, data)

        locations = _parse_locations(d.pop("locations", UNSET))

        def _parse_naics_codes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                naics_codes_type_0 = cast(list[str], data)

                return naics_codes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        naics_codes = _parse_naics_codes(d.pop("naics_codes", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org_id = _parse_org_id(d.pop("org_id", UNSET))

        def _parse_specialties(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                specialties_type_0 = cast(list[str], data)

                return specialties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        specialties = _parse_specialties(d.pop("specialties", UNSET))

        def _parse_ticker(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ticker = _parse_ticker(d.pop("ticker", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_est_employee_count_lower_bound(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_employee_count_lower_bound = _parse_est_employee_count_lower_bound(
            d.pop("est_employee_count_lower_bound", UNSET)
        )

        def _parse_est_employee_count_upper_bound(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_employee_count_upper_bound = _parse_est_employee_count_upper_bound(
            d.pop("est_employee_count_upper_bound", UNSET)
        )

        def _parse_standardized_industries(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                standardized_industries_type_0 = cast(list[str], data)

                return standardized_industries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        standardized_industries = _parse_standardized_industries(d.pop("standardized_industries", UNSET))

        def _parse_locations_stats(
            data: object,
        ) -> CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                locations_stats_type_0 = CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0.from_dict(data)

                return locations_stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyLiveEnrichResponse200OutputCompanyLocationsStatsType0 | None | Unset, data)

        locations_stats = _parse_locations_stats(d.pop("locations_stats", UNSET))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        def _parse_historical_headcount(
            data: object,
        ) -> CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                historical_headcount_type_0 = (
                    CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0.from_dict(data)
                )

                return historical_headcount_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0 | None | Unset, data)

        historical_headcount = _parse_historical_headcount(d.pop("historical_headcount", UNSET))

        def _parse_revenue_usd_lower_bound(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        revenue_usd_lower_bound = _parse_revenue_usd_lower_bound(d.pop("revenue_usd_lower_bound", UNSET))

        def _parse_revenue_usd_upper_bound(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

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
            historical_headcount=historical_headcount,
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
