from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.financial_instrument_lookup_body_instrument_type_0_index import (
    FinancialInstrumentLookupBodyInstrumentType0Index,
)
from ..models.financial_instrument_lookup_body_instrument_type_0_type import (
    FinancialInstrumentLookupBodyInstrumentType0Type,
)

T = TypeVar("T", bound="FinancialInstrumentLookupBodyInstrumentType0")


@_attrs_define
class FinancialInstrumentLookupBodyInstrumentType0:
    """
    Attributes:
        type_ (FinancialInstrumentLookupBodyInstrumentType0Type):
        index (FinancialInstrumentLookupBodyInstrumentType0Index): Named market index preset.
    """

    type_: FinancialInstrumentLookupBodyInstrumentType0Type
    index: FinancialInstrumentLookupBodyInstrumentType0Index
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        index = self.index.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "index": index,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = FinancialInstrumentLookupBodyInstrumentType0Type(d.pop("type"))

        index = FinancialInstrumentLookupBodyInstrumentType0Index(d.pop("index"))

        financial_instrument_lookup_body_instrument_type_0 = cls(
            type_=type_,
            index=index,
        )

        financial_instrument_lookup_body_instrument_type_0.additional_properties = d
        return financial_instrument_lookup_body_instrument_type_0

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
