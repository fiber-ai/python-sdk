from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyStockInfoConsensusType0")


@_attrs_define
class GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyStockInfoConsensusType0:
    """
    Attributes:
        ticker (None | str | Unset):
        exchange (None | str | Unset):
    """

    ticker: None | str | Unset = UNSET
    exchange: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker: None | str | Unset
        if isinstance(self.ticker, Unset):
            ticker = UNSET
        else:
            ticker = self.ticker

        exchange: None | str | Unset
        if isinstance(self.exchange, Unset):
            exchange = UNSET
        else:
            exchange = self.exchange

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if exchange is not UNSET:
            field_dict["exchange"] = exchange

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_ticker(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ticker = _parse_ticker(d.pop("ticker", UNSET))

        def _parse_exchange(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exchange = _parse_exchange(d.pop("exchange", UNSET))

        get_saved_search_run_companies_response_200_output_companies_item_company_stock_info_consensus_type_0 = cls(
            ticker=ticker,
            exchange=exchange,
        )

        get_saved_search_run_companies_response_200_output_companies_item_company_stock_info_consensus_type_0.additional_properties = d
        return get_saved_search_run_companies_response_200_output_companies_item_company_stock_info_consensus_type_0

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
