from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.financial_instrument_lookup_response_200_output_quote_type_0_price_change_type_0 import (
        FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0,
    )


T = TypeVar("T", bound="FinancialInstrumentLookupResponse200OutputQuoteType0")


@_attrs_define
class FinancialInstrumentLookupResponse200OutputQuoteType0:
    """Latest regular-session quote.

    Attributes:
        price (float | None | Unset): Latest traded price as a number.
        currency (None | str | Unset): Currency the price is denominated in — fiat (e.g. 'USD', 'GBP') or crypto (e.g.
            'BTC', 'USDC').
        price_change (FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0 | None | Unset): Magnitude
            and direction of the most recent price change.
        quoted_at (None | str | Unset): ISO 8601 timestamp of when the quote was observed.
    """

    price: float | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    price_change: FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0 | None | Unset = UNSET
    quoted_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.financial_instrument_lookup_response_200_output_quote_type_0_price_change_type_0 import (
            FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0,
        )

        price: float | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        price_change: dict[str, Any] | None | Unset
        if isinstance(self.price_change, Unset):
            price_change = UNSET
        elif isinstance(self.price_change, FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0):
            price_change = self.price_change.to_dict()
        else:
            price_change = self.price_change

        quoted_at: None | str | Unset
        if isinstance(self.quoted_at, Unset):
            quoted_at = UNSET
        else:
            quoted_at = self.quoted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price is not UNSET:
            field_dict["price"] = price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if price_change is not UNSET:
            field_dict["priceChange"] = price_change
        if quoted_at is not UNSET:
            field_dict["quotedAt"] = quoted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.financial_instrument_lookup_response_200_output_quote_type_0_price_change_type_0 import (
            FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0,
        )

        d = dict(src_dict)

        def _parse_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_price_change(
            data: object,
        ) -> FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                price_change_type_0 = FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0.from_dict(
                    data
                )

                return price_change_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0 | None | Unset, data)

        price_change = _parse_price_change(d.pop("priceChange", UNSET))

        def _parse_quoted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quoted_at = _parse_quoted_at(d.pop("quotedAt", UNSET))

        financial_instrument_lookup_response_200_output_quote_type_0 = cls(
            price=price,
            currency=currency,
            price_change=price_change,
            quoted_at=quoted_at,
        )

        financial_instrument_lookup_response_200_output_quote_type_0.additional_properties = d
        return financial_instrument_lookup_response_200_output_quote_type_0

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
