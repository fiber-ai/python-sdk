from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multi_source_search_body_search_type_0_people_filters_type_0_job_titles_type_0 import (
        MultiSourceSearchBodySearchType0PeopleFiltersType0JobTitlesType0,
    )


T = TypeVar("T", bound="MultiSourceSearchBodySearchType0PeopleFiltersType0")


@_attrs_define
class MultiSourceSearchBodySearchType0PeopleFiltersType0:
    """Optional filters applied on top of the AI-derived people filters (e.g. job titles, country, max people per company).
    Only used when the query resolves to a people search.

        Attributes:
            country_codes (list[str] | None | Unset): ISO 3166-1 alpha-3 country codes (e.g. USA, GBR).
            min_relevance (float | None | Unset): Minimum relevance score (0.0–1.0). Higher values mean a closer job-title
                match.
            job_titles (MultiSourceSearchBodySearchType0PeopleFiltersType0JobTitlesType0 | None | Unset):
            max_people_per_company (int | None | Unset): Maximum number of people to return per matched company.
            company_linkedin_ids (list[str] | None | Unset): Restrict results to people from these companies. Provide the
                numeric LinkedIn company IDs returned by Fiber's company search endpoints.
    """

    country_codes: list[str] | None | Unset = UNSET
    min_relevance: float | None | Unset = UNSET
    job_titles: MultiSourceSearchBodySearchType0PeopleFiltersType0JobTitlesType0 | None | Unset = UNSET
    max_people_per_company: int | None | Unset = UNSET
    company_linkedin_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.multi_source_search_body_search_type_0_people_filters_type_0_job_titles_type_0 import (
            MultiSourceSearchBodySearchType0PeopleFiltersType0JobTitlesType0,
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

        job_titles: dict[str, Any] | None | Unset
        if isinstance(self.job_titles, Unset):
            job_titles = UNSET
        elif isinstance(self.job_titles, MultiSourceSearchBodySearchType0PeopleFiltersType0JobTitlesType0):
            job_titles = self.job_titles.to_dict()
        else:
            job_titles = self.job_titles

        max_people_per_company: int | None | Unset
        if isinstance(self.max_people_per_company, Unset):
            max_people_per_company = UNSET
        else:
            max_people_per_company = self.max_people_per_company

        company_linkedin_ids: list[str] | None | Unset
        if isinstance(self.company_linkedin_ids, Unset):
            company_linkedin_ids = UNSET
        elif isinstance(self.company_linkedin_ids, list):
            company_linkedin_ids = self.company_linkedin_ids

        else:
            company_linkedin_ids = self.company_linkedin_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country_codes is not UNSET:
            field_dict["country_codes"] = country_codes
        if min_relevance is not UNSET:
            field_dict["min_relevance"] = min_relevance
        if job_titles is not UNSET:
            field_dict["job_titles"] = job_titles
        if max_people_per_company is not UNSET:
            field_dict["max_people_per_company"] = max_people_per_company
        if company_linkedin_ids is not UNSET:
            field_dict["company_linkedin_ids"] = company_linkedin_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.multi_source_search_body_search_type_0_people_filters_type_0_job_titles_type_0 import (
            MultiSourceSearchBodySearchType0PeopleFiltersType0JobTitlesType0,
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

        def _parse_job_titles(
            data: object,
        ) -> MultiSourceSearchBodySearchType0PeopleFiltersType0JobTitlesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_titles_type_0 = MultiSourceSearchBodySearchType0PeopleFiltersType0JobTitlesType0.from_dict(data)

                return job_titles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MultiSourceSearchBodySearchType0PeopleFiltersType0JobTitlesType0 | None | Unset, data)

        job_titles = _parse_job_titles(d.pop("job_titles", UNSET))

        def _parse_max_people_per_company(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_people_per_company = _parse_max_people_per_company(d.pop("max_people_per_company", UNSET))

        def _parse_company_linkedin_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                company_linkedin_ids_type_0 = cast(list[str], data)

                return company_linkedin_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        company_linkedin_ids = _parse_company_linkedin_ids(d.pop("company_linkedin_ids", UNSET))

        multi_source_search_body_search_type_0_people_filters_type_0 = cls(
            country_codes=country_codes,
            min_relevance=min_relevance,
            job_titles=job_titles,
            max_people_per_company=max_people_per_company,
            company_linkedin_ids=company_linkedin_ids,
        )

        multi_source_search_body_search_type_0_people_filters_type_0.additional_properties = d
        return multi_source_search_body_search_type_0_people_filters_type_0

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
