from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.multi_source_search_body_search_type_0_company_filters_type_0_employee_growth_type_0_item import (
    MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeGrowthType0Item,
)
from ..models.multi_source_search_body_search_type_0_company_filters_type_0_funding_stages_type_0_item import (
    MultiSourceSearchBodySearchType0CompanyFiltersType0FundingStagesType0Item,
)
from ..models.multi_source_search_body_search_type_0_company_filters_type_0_website_traffic_growth_type_0_item import (
    MultiSourceSearchBodySearchType0CompanyFiltersType0WebsiteTrafficGrowthType0Item,
)
from ..models.multi_source_search_body_search_type_0_company_filters_type_0_website_traffic_type_0_item import (
    MultiSourceSearchBodySearchType0CompanyFiltersType0WebsiteTrafficType0Item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multi_source_search_body_search_type_0_company_filters_type_0_employee_count_type_0 import (
        MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeCountType0,
    )
    from ..models.multi_source_search_body_search_type_0_company_filters_type_0_founded_year_type_0 import (
        MultiSourceSearchBodySearchType0CompanyFiltersType0FoundedYearType0,
    )
    from ..models.multi_source_search_body_search_type_0_company_filters_type_0_revenue_type_0 import (
        MultiSourceSearchBodySearchType0CompanyFiltersType0RevenueType0,
    )


T = TypeVar("T", bound="MultiSourceSearchBodySearchType0CompanyFiltersType0")


@_attrs_define
class MultiSourceSearchBodySearchType0CompanyFiltersType0:
    """Optional filters applied on top of the AI-derived company filters (e.g. country, funding stage, employee count,
    etc).

        Attributes:
            country_codes (list[str] | None | Unset): ISO 3166-1 alpha-3 country codes (e.g. USA, GBR).
            min_relevance (float | None | Unset): Minimum relevance score (0.0–1.0). Higher values mean a closer match to
                your query.
            funding_stages (list[MultiSourceSearchBodySearchType0CompanyFiltersType0FundingStagesType0Item] | None | Unset):
                Last funding round stage filter. Acquired, public, closed, and unknown stages are not supported.
            employee_growth (list[MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeGrowthType0Item] | None |
                Unset): Year-over-year employee growth trend. Elements are OR-ed together.
            website_traffic (list[MultiSourceSearchBodySearchType0CompanyFiltersType0WebsiteTrafficType0Item] | None |
                Unset): Monthly website traffic bucket filter. Elements are OR-ed together.
            employee_count (MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeCountType0 | None | Unset): Filter by
                number of employees (inclusive range).
            founded_year (MultiSourceSearchBodySearchType0CompanyFiltersType0FoundedYearType0 | None | Unset): Filter by
                company founding year (inclusive range).
            revenue (MultiSourceSearchBodySearchType0CompanyFiltersType0RevenueType0 | None | Unset): Annual revenue in USD
                (inclusive range).
            is_b2b (bool | None | Unset): If `true`, include only B2B companies. If `false`, exclude B2B companies.
            is_tech (bool | None | Unset): If `true`, include only tech companies. If `false`, exclude tech companies.
            is_saas (bool | None | Unset): If `true`, include only SaaS companies. If `false`, exclude SaaS companies.
            is_startup (bool | None | Unset): If `true`, include only startup-stage companies. If `false`, exclude startups.
            website_traffic_growth (list[MultiSourceSearchBodySearchType0CompanyFiltersType0WebsiteTrafficGrowthType0Item] |
                None | Unset): Year-over-year website traffic growth trend. Elements are OR-ed together.
            has_linkedin_page (bool | None | Unset): If `true`, include only companies with a LinkedIn page. If `false`,
                exclude them.
            has_employees_on_linkedin (bool | None | Unset): If `true`, include only companies that have employees listed on
                LinkedIn. If `false`, exclude them.
            has_public_emails (bool | None | Unset): If `true`, include only companies with public contact emails. If
                `false`, exclude them.
            has_company_phone (bool | None | Unset): If `true`, include only companies with a phone number. If `false`,
                exclude them.
            hiring_is (bool | None | Unset): If `true`, include only companies that are currently hiring. If `false`,
                exclude them.
            is_ai (bool | None | Unset): If `true`, include only AI-related companies. If `false`, exclude them.
    """

    country_codes: list[str] | None | Unset = UNSET
    min_relevance: float | None | Unset = UNSET
    funding_stages: list[MultiSourceSearchBodySearchType0CompanyFiltersType0FundingStagesType0Item] | None | Unset = (
        UNSET
    )
    employee_growth: list[MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeGrowthType0Item] | None | Unset = (
        UNSET
    )
    website_traffic: list[MultiSourceSearchBodySearchType0CompanyFiltersType0WebsiteTrafficType0Item] | None | Unset = (
        UNSET
    )
    employee_count: MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeCountType0 | None | Unset = UNSET
    founded_year: MultiSourceSearchBodySearchType0CompanyFiltersType0FoundedYearType0 | None | Unset = UNSET
    revenue: MultiSourceSearchBodySearchType0CompanyFiltersType0RevenueType0 | None | Unset = UNSET
    is_b2b: bool | None | Unset = UNSET
    is_tech: bool | None | Unset = UNSET
    is_saas: bool | None | Unset = UNSET
    is_startup: bool | None | Unset = UNSET
    website_traffic_growth: (
        list[MultiSourceSearchBodySearchType0CompanyFiltersType0WebsiteTrafficGrowthType0Item] | None | Unset
    ) = UNSET
    has_linkedin_page: bool | None | Unset = UNSET
    has_employees_on_linkedin: bool | None | Unset = UNSET
    has_public_emails: bool | None | Unset = UNSET
    has_company_phone: bool | None | Unset = UNSET
    hiring_is: bool | None | Unset = UNSET
    is_ai: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.multi_source_search_body_search_type_0_company_filters_type_0_employee_count_type_0 import (
            MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeCountType0,
        )
        from ..models.multi_source_search_body_search_type_0_company_filters_type_0_founded_year_type_0 import (
            MultiSourceSearchBodySearchType0CompanyFiltersType0FoundedYearType0,
        )
        from ..models.multi_source_search_body_search_type_0_company_filters_type_0_revenue_type_0 import (
            MultiSourceSearchBodySearchType0CompanyFiltersType0RevenueType0,
        )

        country_codes: list[str] | None | Unset
        if isinstance(self.country_codes, Unset):
            country_codes = UNSET
        elif isinstance(self.country_codes, list):
            country_codes = self.country_codes

        else:
            country_codes = self.country_codes

        min_relevance: float | None | Unset
        if isinstance(self.min_relevance, Unset):
            min_relevance = UNSET
        else:
            min_relevance = self.min_relevance

        funding_stages: list[str] | None | Unset
        if isinstance(self.funding_stages, Unset):
            funding_stages = UNSET
        elif isinstance(self.funding_stages, list):
            funding_stages = []
            for funding_stages_type_0_item_data in self.funding_stages:
                funding_stages_type_0_item = funding_stages_type_0_item_data.value
                funding_stages.append(funding_stages_type_0_item)

        else:
            funding_stages = self.funding_stages

        employee_growth: list[str] | None | Unset
        if isinstance(self.employee_growth, Unset):
            employee_growth = UNSET
        elif isinstance(self.employee_growth, list):
            employee_growth = []
            for employee_growth_type_0_item_data in self.employee_growth:
                employee_growth_type_0_item = employee_growth_type_0_item_data.value
                employee_growth.append(employee_growth_type_0_item)

        else:
            employee_growth = self.employee_growth

        website_traffic: list[str] | None | Unset
        if isinstance(self.website_traffic, Unset):
            website_traffic = UNSET
        elif isinstance(self.website_traffic, list):
            website_traffic = []
            for website_traffic_type_0_item_data in self.website_traffic:
                website_traffic_type_0_item = website_traffic_type_0_item_data.value
                website_traffic.append(website_traffic_type_0_item)

        else:
            website_traffic = self.website_traffic

        employee_count: dict[str, Any] | None | Unset
        if isinstance(self.employee_count, Unset):
            employee_count = UNSET
        elif isinstance(self.employee_count, MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeCountType0):
            employee_count = self.employee_count.to_dict()
        else:
            employee_count = self.employee_count

        founded_year: dict[str, Any] | None | Unset
        if isinstance(self.founded_year, Unset):
            founded_year = UNSET
        elif isinstance(self.founded_year, MultiSourceSearchBodySearchType0CompanyFiltersType0FoundedYearType0):
            founded_year = self.founded_year.to_dict()
        else:
            founded_year = self.founded_year

        revenue: dict[str, Any] | None | Unset
        if isinstance(self.revenue, Unset):
            revenue = UNSET
        elif isinstance(self.revenue, MultiSourceSearchBodySearchType0CompanyFiltersType0RevenueType0):
            revenue = self.revenue.to_dict()
        else:
            revenue = self.revenue

        is_b2b: bool | None | Unset
        if isinstance(self.is_b2b, Unset):
            is_b2b = UNSET
        else:
            is_b2b = self.is_b2b

        is_tech: bool | None | Unset
        if isinstance(self.is_tech, Unset):
            is_tech = UNSET
        else:
            is_tech = self.is_tech

        is_saas: bool | None | Unset
        if isinstance(self.is_saas, Unset):
            is_saas = UNSET
        else:
            is_saas = self.is_saas

        is_startup: bool | None | Unset
        if isinstance(self.is_startup, Unset):
            is_startup = UNSET
        else:
            is_startup = self.is_startup

        website_traffic_growth: list[str] | None | Unset
        if isinstance(self.website_traffic_growth, Unset):
            website_traffic_growth = UNSET
        elif isinstance(self.website_traffic_growth, list):
            website_traffic_growth = []
            for website_traffic_growth_type_0_item_data in self.website_traffic_growth:
                website_traffic_growth_type_0_item = website_traffic_growth_type_0_item_data.value
                website_traffic_growth.append(website_traffic_growth_type_0_item)

        else:
            website_traffic_growth = self.website_traffic_growth

        has_linkedin_page: bool | None | Unset
        if isinstance(self.has_linkedin_page, Unset):
            has_linkedin_page = UNSET
        else:
            has_linkedin_page = self.has_linkedin_page

        has_employees_on_linkedin: bool | None | Unset
        if isinstance(self.has_employees_on_linkedin, Unset):
            has_employees_on_linkedin = UNSET
        else:
            has_employees_on_linkedin = self.has_employees_on_linkedin

        has_public_emails: bool | None | Unset
        if isinstance(self.has_public_emails, Unset):
            has_public_emails = UNSET
        else:
            has_public_emails = self.has_public_emails

        has_company_phone: bool | None | Unset
        if isinstance(self.has_company_phone, Unset):
            has_company_phone = UNSET
        else:
            has_company_phone = self.has_company_phone

        hiring_is: bool | None | Unset
        if isinstance(self.hiring_is, Unset):
            hiring_is = UNSET
        else:
            hiring_is = self.hiring_is

        is_ai: bool | None | Unset
        if isinstance(self.is_ai, Unset):
            is_ai = UNSET
        else:
            is_ai = self.is_ai

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country_codes is not UNSET:
            field_dict["country_codes"] = country_codes
        if min_relevance is not UNSET:
            field_dict["min_relevance"] = min_relevance
        if funding_stages is not UNSET:
            field_dict["funding_stages"] = funding_stages
        if employee_growth is not UNSET:
            field_dict["employee_growth"] = employee_growth
        if website_traffic is not UNSET:
            field_dict["website_traffic"] = website_traffic
        if employee_count is not UNSET:
            field_dict["employee_count"] = employee_count
        if founded_year is not UNSET:
            field_dict["founded_year"] = founded_year
        if revenue is not UNSET:
            field_dict["revenue"] = revenue
        if is_b2b is not UNSET:
            field_dict["is_b2b"] = is_b2b
        if is_tech is not UNSET:
            field_dict["is_tech"] = is_tech
        if is_saas is not UNSET:
            field_dict["is_saas"] = is_saas
        if is_startup is not UNSET:
            field_dict["is_startup"] = is_startup
        if website_traffic_growth is not UNSET:
            field_dict["website_traffic_growth"] = website_traffic_growth
        if has_linkedin_page is not UNSET:
            field_dict["has_linkedin_page"] = has_linkedin_page
        if has_employees_on_linkedin is not UNSET:
            field_dict["has_employees_on_linkedin"] = has_employees_on_linkedin
        if has_public_emails is not UNSET:
            field_dict["has_public_emails"] = has_public_emails
        if has_company_phone is not UNSET:
            field_dict["has_company_phone"] = has_company_phone
        if hiring_is is not UNSET:
            field_dict["hiring_is"] = hiring_is
        if is_ai is not UNSET:
            field_dict["is_ai"] = is_ai

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.multi_source_search_body_search_type_0_company_filters_type_0_employee_count_type_0 import (
            MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeCountType0,
        )
        from ..models.multi_source_search_body_search_type_0_company_filters_type_0_founded_year_type_0 import (
            MultiSourceSearchBodySearchType0CompanyFiltersType0FoundedYearType0,
        )
        from ..models.multi_source_search_body_search_type_0_company_filters_type_0_revenue_type_0 import (
            MultiSourceSearchBodySearchType0CompanyFiltersType0RevenueType0,
        )

        d = dict(src_dict)

        def _parse_country_codes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                country_codes_type_0 = cast(list[str], data)

                return country_codes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        country_codes = _parse_country_codes(d.pop("country_codes", UNSET))

        def _parse_min_relevance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_relevance = _parse_min_relevance(d.pop("min_relevance", UNSET))

        def _parse_funding_stages(
            data: object,
        ) -> list[MultiSourceSearchBodySearchType0CompanyFiltersType0FundingStagesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                funding_stages_type_0 = []
                _funding_stages_type_0 = data
                for funding_stages_type_0_item_data in _funding_stages_type_0:
                    funding_stages_type_0_item = (
                        MultiSourceSearchBodySearchType0CompanyFiltersType0FundingStagesType0Item(
                            funding_stages_type_0_item_data
                        )
                    )

                    funding_stages_type_0.append(funding_stages_type_0_item)

                return funding_stages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[MultiSourceSearchBodySearchType0CompanyFiltersType0FundingStagesType0Item] | None | Unset, data
            )

        funding_stages = _parse_funding_stages(d.pop("funding_stages", UNSET))

        def _parse_employee_growth(
            data: object,
        ) -> list[MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeGrowthType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                employee_growth_type_0 = []
                _employee_growth_type_0 = data
                for employee_growth_type_0_item_data in _employee_growth_type_0:
                    employee_growth_type_0_item = (
                        MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeGrowthType0Item(
                            employee_growth_type_0_item_data
                        )
                    )

                    employee_growth_type_0.append(employee_growth_type_0_item)

                return employee_growth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeGrowthType0Item] | None | Unset, data
            )

        employee_growth = _parse_employee_growth(d.pop("employee_growth", UNSET))

        def _parse_website_traffic(
            data: object,
        ) -> list[MultiSourceSearchBodySearchType0CompanyFiltersType0WebsiteTrafficType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                website_traffic_type_0 = []
                _website_traffic_type_0 = data
                for website_traffic_type_0_item_data in _website_traffic_type_0:
                    website_traffic_type_0_item = (
                        MultiSourceSearchBodySearchType0CompanyFiltersType0WebsiteTrafficType0Item(
                            website_traffic_type_0_item_data
                        )
                    )

                    website_traffic_type_0.append(website_traffic_type_0_item)

                return website_traffic_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[MultiSourceSearchBodySearchType0CompanyFiltersType0WebsiteTrafficType0Item] | None | Unset, data
            )

        website_traffic = _parse_website_traffic(d.pop("website_traffic", UNSET))

        def _parse_employee_count(
            data: object,
        ) -> MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeCountType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employee_count_type_0 = MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeCountType0.from_dict(
                    data
                )

                return employee_count_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MultiSourceSearchBodySearchType0CompanyFiltersType0EmployeeCountType0 | None | Unset, data)

        employee_count = _parse_employee_count(d.pop("employee_count", UNSET))

        def _parse_founded_year(
            data: object,
        ) -> MultiSourceSearchBodySearchType0CompanyFiltersType0FoundedYearType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                founded_year_type_0 = MultiSourceSearchBodySearchType0CompanyFiltersType0FoundedYearType0.from_dict(
                    data
                )

                return founded_year_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MultiSourceSearchBodySearchType0CompanyFiltersType0FoundedYearType0 | None | Unset, data)

        founded_year = _parse_founded_year(d.pop("founded_year", UNSET))

        def _parse_revenue(
            data: object,
        ) -> MultiSourceSearchBodySearchType0CompanyFiltersType0RevenueType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                revenue_type_0 = MultiSourceSearchBodySearchType0CompanyFiltersType0RevenueType0.from_dict(data)

                return revenue_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MultiSourceSearchBodySearchType0CompanyFiltersType0RevenueType0 | None | Unset, data)

        revenue = _parse_revenue(d.pop("revenue", UNSET))

        def _parse_is_b2b(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_b2b = _parse_is_b2b(d.pop("is_b2b", UNSET))

        def _parse_is_tech(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_tech = _parse_is_tech(d.pop("is_tech", UNSET))

        def _parse_is_saas(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_saas = _parse_is_saas(d.pop("is_saas", UNSET))

        def _parse_is_startup(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_startup = _parse_is_startup(d.pop("is_startup", UNSET))

        def _parse_website_traffic_growth(
            data: object,
        ) -> list[MultiSourceSearchBodySearchType0CompanyFiltersType0WebsiteTrafficGrowthType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                website_traffic_growth_type_0 = []
                _website_traffic_growth_type_0 = data
                for website_traffic_growth_type_0_item_data in _website_traffic_growth_type_0:
                    website_traffic_growth_type_0_item = (
                        MultiSourceSearchBodySearchType0CompanyFiltersType0WebsiteTrafficGrowthType0Item(
                            website_traffic_growth_type_0_item_data
                        )
                    )

                    website_traffic_growth_type_0.append(website_traffic_growth_type_0_item)

                return website_traffic_growth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[MultiSourceSearchBodySearchType0CompanyFiltersType0WebsiteTrafficGrowthType0Item] | None | Unset,
                data,
            )

        website_traffic_growth = _parse_website_traffic_growth(d.pop("website_traffic_growth", UNSET))

        def _parse_has_linkedin_page(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_linkedin_page = _parse_has_linkedin_page(d.pop("has_linkedin_page", UNSET))

        def _parse_has_employees_on_linkedin(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_employees_on_linkedin = _parse_has_employees_on_linkedin(d.pop("has_employees_on_linkedin", UNSET))

        def _parse_has_public_emails(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_public_emails = _parse_has_public_emails(d.pop("has_public_emails", UNSET))

        def _parse_has_company_phone(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_company_phone = _parse_has_company_phone(d.pop("has_company_phone", UNSET))

        def _parse_hiring_is(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hiring_is = _parse_hiring_is(d.pop("hiring_is", UNSET))

        def _parse_is_ai(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_ai = _parse_is_ai(d.pop("is_ai", UNSET))

        multi_source_search_body_search_type_0_company_filters_type_0 = cls(
            country_codes=country_codes,
            min_relevance=min_relevance,
            funding_stages=funding_stages,
            employee_growth=employee_growth,
            website_traffic=website_traffic,
            employee_count=employee_count,
            founded_year=founded_year,
            revenue=revenue,
            is_b2b=is_b2b,
            is_tech=is_tech,
            is_saas=is_saas,
            is_startup=is_startup,
            website_traffic_growth=website_traffic_growth,
            has_linkedin_page=has_linkedin_page,
            has_employees_on_linkedin=has_employees_on_linkedin,
            has_public_emails=has_public_emails,
            has_company_phone=has_company_phone,
            hiring_is=hiring_is,
            is_ai=is_ai,
        )

        multi_source_search_body_search_type_0_company_filters_type_0.additional_properties = d
        return multi_source_search_body_search_type_0_company_filters_type_0

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
