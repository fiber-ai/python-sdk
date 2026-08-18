from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialInstrumentLookupResponse200OutputInstrumentType0")


@_attrs_define
class FinancialInstrumentLookupResponse200OutputInstrumentType0:
    """Core identity of the looked-up instrument.

    Attributes:
        name (None | str | Unset): Display name of the instrument (e.g. 'Alphabet Inc Class A').
        ticker (None | str | Unset): Ticker symbol without the exchange (e.g. 'GOOGL').
        exchange (None | str | Unset): Exchange code (e.g. 'NASDAQ').
        currency (None | str | Unset): Currency the quote is denominated in — fiat (e.g. 'USD', 'GBP') or crypto (e.g.
            'BTC', 'USDC'). Minor-unit exchanges such as London in pence are converted to the major unit so every price
            matches this code.
    """

    name: None | str | Unset = UNSET
    ticker: None | str | Unset = UNSET
    exchange: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if exchange is not UNSET:
            field_dict["exchange"] = exchange
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

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

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        financial_instrument_lookup_response_200_output_instrument_type_0 = cls(
            name=name,
            ticker=ticker,
            exchange=exchange,
            currency=currency,
        )

        financial_instrument_lookup_response_200_output_instrument_type_0.additional_properties = d
        return financial_instrument_lookup_response_200_output_instrument_type_0

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
