from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.financial_instrument_lookup_body_instrument_type_1_type import (
    FinancialInstrumentLookupBodyInstrumentType1Type,
)

T = TypeVar("T", bound="FinancialInstrumentLookupBodyInstrumentType1")


@_attrs_define
class FinancialInstrumentLookupBodyInstrumentType1:
    """
    Attributes:
        type_ (FinancialInstrumentLookupBodyInstrumentType1Type):
        ticker (str): Mutual fund ticker (e.g. `VTSAX`, `FXAIX`). This is for index funds and other mutual funds — NOT
            ETFs. ETFs like `SPY` or `QQQM` should use `stockOrEtf` instead.
    """

    type_: FinancialInstrumentLookupBodyInstrumentType1Type
    ticker: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        ticker = self.ticker

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "ticker": ticker,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = FinancialInstrumentLookupBodyInstrumentType1Type(d.pop("type"))

        ticker = d.pop("ticker")

        financial_instrument_lookup_body_instrument_type_1 = cls(
            type_=type_,
            ticker=ticker,
        )

        financial_instrument_lookup_body_instrument_type_1.additional_properties = d
        return financial_instrument_lookup_body_instrument_type_1

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
