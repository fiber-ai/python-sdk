from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemLineItemsType0Item"
)


@_attrs_define
class FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemLineItemsType0Item:
    """A single line item in a financial statement.

    Attributes:
        name (None | str | Unset): Line-item name (e.g. 'Revenue').
        value (float | None | Unset): Reported value for the period.
        change_percentage (float | None | Unset): Percent change versus the comparable prior period.
    """

    name: None | str | Unset = UNSET
    value: float | None | Unset = UNSET
    change_percentage: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        value: float | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        change_percentage: float | None | Unset
        if isinstance(self.change_percentage, Unset):
            change_percentage = UNSET
        else:
            change_percentage = self.change_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value
        if change_percentage is not UNSET:
            field_dict["changePercentage"] = change_percentage

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

        def _parse_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_change_percentage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        change_percentage = _parse_change_percentage(d.pop("changePercentage", UNSET))

        financial_instrument_lookup_response_200_output_financials_type_0_item_periods_type_0_item_line_items_type_0_item = cls(
            name=name,
            value=value,
            change_percentage=change_percentage,
        )

        financial_instrument_lookup_response_200_output_financials_type_0_item_periods_type_0_item_line_items_type_0_item.additional_properties = d
        return financial_instrument_lookup_response_200_output_financials_type_0_item_periods_type_0_item_line_items_type_0_item

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
