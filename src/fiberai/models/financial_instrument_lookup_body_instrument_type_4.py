from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.financial_instrument_lookup_body_instrument_type_4_type import (
    FinancialInstrumentLookupBodyInstrumentType4Type,
)

T = TypeVar("T", bound="FinancialInstrumentLookupBodyInstrumentType4")


@_attrs_define
class FinancialInstrumentLookupBodyInstrumentType4:
    """
    Attributes:
        type_ (FinancialInstrumentLookupBodyInstrumentType4Type):
        symbol (str): Fully-qualified symbol using Google Finance's format. You are responsible for the correct syntax.
            Examples: `AAPL:NASDAQ` (stock), `SPY:NYSEARCA` (ETF), `VTSAX:MUTF` (mutual fund), `EUR-USD` (currency pair),
            `BTC-USD` (crypto), `NIFTY_50:INDEXNSE` (index).
    """

    type_: FinancialInstrumentLookupBodyInstrumentType4Type
    symbol: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        symbol = self.symbol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "symbol": symbol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = FinancialInstrumentLookupBodyInstrumentType4Type(d.pop("type"))

        symbol = d.pop("symbol")

        financial_instrument_lookup_body_instrument_type_4 = cls(
            type_=type_,
            symbol=symbol,
        )

        financial_instrument_lookup_body_instrument_type_4.additional_properties = d
        return financial_instrument_lookup_body_instrument_type_4

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
