from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.financial_instrument_lookup_response_200_output_quote_type_0_price_change_type_0_direction_type_1 import (
    FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType1,
)
from ..models.financial_instrument_lookup_response_200_output_quote_type_0_price_change_type_0_direction_type_2_type_1 import (
    FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType2Type1,
)
from ..models.financial_instrument_lookup_response_200_output_quote_type_0_price_change_type_0_direction_type_3_type_1 import (
    FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0")


@_attrs_define
class FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0:
    """Magnitude and direction of the most recent price change.

    Attributes:
        percentage (float | None | Unset): Percent change versus the prior session.
        amount (float | None | Unset): Absolute price change versus the prior session.
        direction (FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType1 |
            FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType2Type1 |
            FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType3Type1 | None | Unset): Whether
            the price moved up or down.
        currency (None | str | Unset): Currency the price change amount and percentage are denominated in (e.g. 'USD',
            'GBP').
    """

    percentage: float | None | Unset = UNSET
    amount: float | None | Unset = UNSET
    direction: (
        FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType1
        | FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType2Type1
        | FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType3Type1
        | None
        | Unset
    ) = UNSET
    currency: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        percentage: float | None | Unset
        if isinstance(self.percentage, Unset):
            percentage = UNSET
        else:
            percentage = self.percentage

        amount: float | None | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        direction: None | str | Unset
        if isinstance(self.direction, Unset):
            direction = UNSET
        elif isinstance(
            self.direction, FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType1
        ):
            direction = self.direction.value
        elif isinstance(
            self.direction, FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType2Type1
        ):
            direction = self.direction.value
        elif isinstance(
            self.direction, FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType3Type1
        ):
            direction = self.direction.value
        else:
            direction = self.direction

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if amount is not UNSET:
            field_dict["amount"] = amount
        if direction is not UNSET:
            field_dict["direction"] = direction
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_percentage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        percentage = _parse_percentage(d.pop("percentage", UNSET))

        def _parse_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))

        def _parse_direction(
            data: object,
        ) -> (
            FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType1
            | FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType2Type1
            | FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                direction_type_1 = FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType1(
                    data
                )

                return direction_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                direction_type_2_type_1 = (
                    FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType2Type1(data)
                )

                return direction_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                direction_type_3_type_1 = (
                    FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType3Type1(data)
                )

                return direction_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType1
                | FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType2Type1
                | FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType3Type1
                | None
                | Unset,
                data,
            )

        direction = _parse_direction(d.pop("direction", UNSET))

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        financial_instrument_lookup_response_200_output_quote_type_0_price_change_type_0 = cls(
            percentage=percentage,
            amount=amount,
            direction=direction,
            currency=currency,
        )

        financial_instrument_lookup_response_200_output_quote_type_0_price_change_type_0.additional_properties = d
        return financial_instrument_lookup_response_200_output_quote_type_0_price_change_type_0

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
