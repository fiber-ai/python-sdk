from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BookingSearchResponse200OutputPropertiesItemOriginalPriceType0")


@_attrs_define
class BookingSearchResponse200OutputPropertiesItemOriginalPriceType0:
    """List price before discounts, when a promotion applies.

    Attributes:
        currency_code (str): ISO 4217 currency code for this amount (e.g. 'USD').
        amount (float): Price amount in the specified currency.
    """

    currency_code: str
    amount: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_code = self.currency_code

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currencyCode": currency_code,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency_code = d.pop("currencyCode")

        amount = d.pop("amount")

        booking_search_response_200_output_properties_item_original_price_type_0 = cls(
            currency_code=currency_code,
            amount=amount,
        )

        booking_search_response_200_output_properties_item_original_price_type_0.additional_properties = d
        return booking_search_response_200_output_properties_item_original_price_type_0

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
