from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.financial_instrument_lookup_body_instrument_type_2_type import (
    FinancialInstrumentLookupBodyInstrumentType2Type,
)

T = TypeVar("T", bound="FinancialInstrumentLookupBodyInstrumentType2")


@_attrs_define
class FinancialInstrumentLookupBodyInstrumentType2:
    """
    Attributes:
        type_ (FinancialInstrumentLookupBodyInstrumentType2Type):
        ticker (str): Ticker symbol for a stock or ETF (e.g. `AAPL`, `QQQM`, `BARC`).
        exchange (str): Exchange code (e.g. `NASDAQ`, `NYSE`, `NYSEARCA`, `LON`, `TYO`).
    """

    type_: FinancialInstrumentLookupBodyInstrumentType2Type
    ticker: str
    exchange: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        ticker = self.ticker

        exchange = self.exchange

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "ticker": ticker,
                "exchange": exchange,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = FinancialInstrumentLookupBodyInstrumentType2Type(d.pop("type"))

        ticker = d.pop("ticker")

        exchange = d.pop("exchange")

        financial_instrument_lookup_body_instrument_type_2 = cls(
            type_=type_,
            ticker=ticker,
            exchange=exchange,
        )

        financial_instrument_lookup_body_instrument_type_2.additional_properties = d
        return financial_instrument_lookup_body_instrument_type_2

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
