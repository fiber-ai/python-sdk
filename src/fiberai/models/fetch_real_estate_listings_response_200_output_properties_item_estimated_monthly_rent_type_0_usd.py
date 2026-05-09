from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedMonthlyRentType0Usd")


@_attrs_define
class FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedMonthlyRentType0Usd:
    """Listing price converted to USD when conversion data is available.

    Attributes:
        currency (None | str | Unset): ISO 4217 currency code for the listing price.
        amount (float | None | Unset): Numeric listing price amount.
    """

    currency: None | str | Unset = UNSET
    amount: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        amount: float | None | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))

        fetch_real_estate_listings_response_200_output_properties_item_estimated_monthly_rent_type_0_usd = cls(
            currency=currency,
            amount=amount,
        )

        fetch_real_estate_listings_response_200_output_properties_item_estimated_monthly_rent_type_0_usd.additional_properties = d
        return fetch_real_estate_listings_response_200_output_properties_item_estimated_monthly_rent_type_0_usd

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
