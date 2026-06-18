from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BlueCollarJobsSearchBody")


@_attrs_define
class BlueCollarJobsSearchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        company_slug (None | str | Unset): Company identifier on the job board. Use the resolve-company endpoint to find
            this from a domain or name.
        query (None | str | Unset): Job title or keyword to search for (e.g. 'warehouse worker', 'forklift operator').
        location (None | str | Unset): US city, state, or region to search within (e.g. 'Philadelphia, PA', 'Texas').
            Only US locations are supported.
        next_page_token (None | str | Unset): Pagination token returned from a previous search. Pass to get the next
            page of results.
    """

    api_key: str
    company_slug: None | str | Unset = UNSET
    query: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        company_slug: None | str | Unset
        if isinstance(self.company_slug, Unset):
            company_slug = UNSET
        else:
            company_slug = self.company_slug

        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
            }
        )
        if company_slug is not UNSET:
            field_dict["companySlug"] = company_slug
        if query is not UNSET:
            field_dict["query"] = query
        if location is not UNSET:
            field_dict["location"] = location
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_company_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_slug = _parse_company_slug(d.pop("companySlug", UNSET))

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        blue_collar_jobs_search_body = cls(
            api_key=api_key,
            company_slug=company_slug,
            query=query,
            location=location,
            next_page_token=next_page_token,
        )

        blue_collar_jobs_search_body.additional_properties = d
        return blue_collar_jobs_search_body

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
