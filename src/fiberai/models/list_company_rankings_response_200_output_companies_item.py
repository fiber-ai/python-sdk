from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListCompanyRankingsResponse200OutputCompaniesItem")


@_attrs_define
class ListCompanyRankingsResponse200OutputCompaniesItem:
    """
    Attributes:
        name (str): Company name as published on the list.
        rank (int): Position on the list for this edition (1 = top ranked).
        domain (None | str | Unset): Primary company domain, e.g. 'example.com'.
        ticker (None | str | Unset): Stock ticker symbol (e.g. 'AAPL'), when the company is publicly traded.
        headquarters (None | str | Unset): Where the company is based. The exact format varies by list.
        country_code (None | str | Unset): ISO 3166-1 alpha-3 country code of the headquarters country (e.g. 'USA').
        revenue_usd (float | None | Unset): Annual revenue in US dollars.
        profits_usd (float | None | Unset): Annual profits in US dollars.
        market_cap_usd (float | None | Unset): Market capitalization in US dollars.
        employee_count (float | None | Unset): Number of employees.
    """

    name: str
    rank: int
    domain: None | str | Unset = UNSET
    ticker: None | str | Unset = UNSET
    headquarters: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    revenue_usd: float | None | Unset = UNSET
    profits_usd: float | None | Unset = UNSET
    market_cap_usd: float | None | Unset = UNSET
    employee_count: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        rank = self.rank

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        ticker: None | str | Unset
        if isinstance(self.ticker, Unset):
            ticker = UNSET
        else:
            ticker = self.ticker

        headquarters: None | str | Unset
        if isinstance(self.headquarters, Unset):
            headquarters = UNSET
        else:
            headquarters = self.headquarters

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        revenue_usd: float | None | Unset
        if isinstance(self.revenue_usd, Unset):
            revenue_usd = UNSET
        else:
            revenue_usd = self.revenue_usd

        profits_usd: float | None | Unset
        if isinstance(self.profits_usd, Unset):
            profits_usd = UNSET
        else:
            profits_usd = self.profits_usd

        market_cap_usd: float | None | Unset
        if isinstance(self.market_cap_usd, Unset):
            market_cap_usd = UNSET
        else:
            market_cap_usd = self.market_cap_usd

        employee_count: float | None | Unset
        if isinstance(self.employee_count, Unset):
            employee_count = UNSET
        else:
            employee_count = self.employee_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "rank": rank,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if headquarters is not UNSET:
            field_dict["headquarters"] = headquarters
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if revenue_usd is not UNSET:
            field_dict["revenueUsd"] = revenue_usd
        if profits_usd is not UNSET:
            field_dict["profitsUsd"] = profits_usd
        if market_cap_usd is not UNSET:
            field_dict["marketCapUsd"] = market_cap_usd
        if employee_count is not UNSET:
            field_dict["employeeCount"] = employee_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        rank = d.pop("rank")

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        def _parse_ticker(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ticker = _parse_ticker(d.pop("ticker", UNSET))

        def _parse_headquarters(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        headquarters = _parse_headquarters(d.pop("headquarters", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        def _parse_revenue_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        revenue_usd = _parse_revenue_usd(d.pop("revenueUsd", UNSET))

        def _parse_profits_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        profits_usd = _parse_profits_usd(d.pop("profitsUsd", UNSET))

        def _parse_market_cap_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        market_cap_usd = _parse_market_cap_usd(d.pop("marketCapUsd", UNSET))

        def _parse_employee_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        employee_count = _parse_employee_count(d.pop("employeeCount", UNSET))

        list_company_rankings_response_200_output_companies_item = cls(
            name=name,
            rank=rank,
            domain=domain,
            ticker=ticker,
            headquarters=headquarters,
            country_code=country_code,
            revenue_usd=revenue_usd,
            profits_usd=profits_usd,
            market_cap_usd=market_cap_usd,
            employee_count=employee_count,
        )

        list_company_rankings_response_200_output_companies_item.additional_properties = d
        return list_company_rankings_response_200_output_companies_item

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
