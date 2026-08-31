from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.multi_source_search_body_search_type_0_request import MultiSourceSearchBodySearchType0Request
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multi_source_search_body_search_type_0_company_filters_type_0 import (
        MultiSourceSearchBodySearchType0CompanyFiltersType0,
    )
    from ..models.multi_source_search_body_search_type_0_people_filters_type_0 import (
        MultiSourceSearchBodySearchType0PeopleFiltersType0,
    )


T = TypeVar("T", bound="MultiSourceSearchBodySearchType0")


@_attrs_define
class MultiSourceSearchBodySearchType0:
    """
    Attributes:
        request (MultiSourceSearchBodySearchType0Request): Use "initial" for the first page of a new search. Provide
            query, pageSize, and any filters.
        query (str): Natural language search query, e.g. "pizza shops in NYC" or "Series A SaaS founders in London". The
            API infers whether to return companies or people.
        page_size (int | Unset): Number of results per page (default 10, max 1000). This value is locked for the entire
            pagination session. Default: 10.
        company_filters (MultiSourceSearchBodySearchType0CompanyFiltersType0 | None | Unset): Optional filters applied
            on top of the AI-derived company filters (e.g. country, funding stage, employee count, etc).
        people_filters (MultiSourceSearchBodySearchType0PeopleFiltersType0 | None | Unset): Optional filters applied on
            top of the AI-derived people filters (e.g. job titles, country, max people per company). Only used when the
            query resolves to a people search.
    """

    request: MultiSourceSearchBodySearchType0Request
    query: str
    page_size: int | Unset = 10
    company_filters: MultiSourceSearchBodySearchType0CompanyFiltersType0 | None | Unset = UNSET
    people_filters: MultiSourceSearchBodySearchType0PeopleFiltersType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.multi_source_search_body_search_type_0_company_filters_type_0 import (
            MultiSourceSearchBodySearchType0CompanyFiltersType0,  # noqa: PLC0415
        )
        from ..models.multi_source_search_body_search_type_0_people_filters_type_0 import (
            MultiSourceSearchBodySearchType0PeopleFiltersType0,  # noqa: PLC0415
        )

        request = self.request.value

        query = self.query

        page_size = self.page_size

        company_filters: dict[str, Any] | None | Unset
        if isinstance(self.company_filters, Unset):
            company_filters = UNSET
        elif isinstance(self.company_filters, MultiSourceSearchBodySearchType0CompanyFiltersType0):
            company_filters = self.company_filters.to_dict()
        else:
            company_filters = self.company_filters

        people_filters: dict[str, Any] | None | Unset
        if isinstance(self.people_filters, Unset):
            people_filters = UNSET
        elif isinstance(self.people_filters, MultiSourceSearchBodySearchType0PeopleFiltersType0):
            people_filters = self.people_filters.to_dict()
        else:
            people_filters = self.people_filters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "request": request,
                "query": query,
            }
        )
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if company_filters is not UNSET:
            field_dict["companyFilters"] = company_filters
        if people_filters is not UNSET:
            field_dict["peopleFilters"] = people_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.multi_source_search_body_search_type_0_company_filters_type_0 import (
            MultiSourceSearchBodySearchType0CompanyFiltersType0,  # noqa: PLC0415
        )
        from ..models.multi_source_search_body_search_type_0_people_filters_type_0 import (
            MultiSourceSearchBodySearchType0PeopleFiltersType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        request = MultiSourceSearchBodySearchType0Request(d.pop("request"))

        query = d.pop("query")

        page_size = d.pop("pageSize", UNSET)

        def _parse_company_filters(data: object) -> MultiSourceSearchBodySearchType0CompanyFiltersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_filters_type_0 = MultiSourceSearchBodySearchType0CompanyFiltersType0.from_dict(data)

                return company_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MultiSourceSearchBodySearchType0CompanyFiltersType0 | None | Unset, data)

        company_filters = _parse_company_filters(d.pop("companyFilters", UNSET))

        def _parse_people_filters(data: object) -> MultiSourceSearchBodySearchType0PeopleFiltersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                people_filters_type_0 = MultiSourceSearchBodySearchType0PeopleFiltersType0.from_dict(data)

                return people_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MultiSourceSearchBodySearchType0PeopleFiltersType0 | None | Unset, data)

        people_filters = _parse_people_filters(d.pop("peopleFilters", UNSET))

        multi_source_search_body_search_type_0 = cls(
            request=request,
            query=query,
            page_size=page_size,
            company_filters=company_filters,
            people_filters=people_filters,
        )

        multi_source_search_body_search_type_0.additional_properties = d
        return multi_source_search_body_search_type_0

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
