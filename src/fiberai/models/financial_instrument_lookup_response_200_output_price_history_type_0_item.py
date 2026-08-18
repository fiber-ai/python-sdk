from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialInstrumentLookupResponse200OutputPriceHistoryType0Item")


@_attrs_define
class FinancialInstrumentLookupResponse200OutputPriceHistoryType0Item:
    """A single point on the price history series.

    Attributes:
        price (float | None | Unset): Price at this point.
        currency (None | str | Unset): Currency of the price.
        at (None | str | Unset): ISO 8601 timestamp of the price point.
        volume (int | None | Unset): Trading volume at this point, when available.
    """

    price: float | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    at: None | str | Unset = UNSET
    volume: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        at: None | str | Unset
        if isinstance(self.at, Unset):
            at = UNSET
        else:
            at = self.at

        volume: int | None | Unset
        if isinstance(self.volume, Unset):
            volume = UNSET
        else:
            volume = self.volume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price is not UNSET:
            field_dict["price"] = price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if at is not UNSET:
            field_dict["at"] = at
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        def _parse_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        at = _parse_at(d.pop("at", UNSET))

        def _parse_volume(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume = _parse_volume(d.pop("volume", UNSET))

        financial_instrument_lookup_response_200_output_price_history_type_0_item = cls(
            price=price,
            currency=currency,
            at=at,
            volume=volume,
        )

        financial_instrument_lookup_response_200_output_price_history_type_0_item.additional_properties = d
        return financial_instrument_lookup_response_200_output_price_history_type_0_item

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
