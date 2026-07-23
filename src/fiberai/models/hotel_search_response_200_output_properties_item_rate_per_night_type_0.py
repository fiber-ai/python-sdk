from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HotelSearchResponse200OutputPropertiesItemRatePerNightType0")


@_attrs_define
class HotelSearchResponse200OutputPropertiesItemRatePerNightType0:
    """Nightly rate summary for one night.

    Attributes:
        currency_code (str): ISO 4217 currency code for the amounts in this rate.
        all_in_cost (int | None | Unset): All-in cost in whole currency units, including taxes and fees. Null when only
            a pre-tax rate is available, in which case only `baseCost` is populated.
        base_cost (int | None | Unset): Base cost before taxes and fees in whole currency units; this is not the final
            amount charged.
    """

    currency_code: str
    all_in_cost: int | None | Unset = UNSET
    base_cost: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_code = self.currency_code

        all_in_cost: int | None | Unset
        if isinstance(self.all_in_cost, Unset):
            all_in_cost = UNSET
        else:
            all_in_cost = self.all_in_cost

        base_cost: int | None | Unset
        if isinstance(self.base_cost, Unset):
            base_cost = UNSET
        else:
            base_cost = self.base_cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currencyCode": currency_code,
            }
        )
        if all_in_cost is not UNSET:
            field_dict["allInCost"] = all_in_cost
        if base_cost is not UNSET:
            field_dict["baseCost"] = base_cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency_code = d.pop("currencyCode")

        def _parse_all_in_cost(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        all_in_cost = _parse_all_in_cost(d.pop("allInCost", UNSET))

        def _parse_base_cost(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        base_cost = _parse_base_cost(d.pop("baseCost", UNSET))

        hotel_search_response_200_output_properties_item_rate_per_night_type_0 = cls(
            currency_code=currency_code,
            all_in_cost=all_in_cost,
            base_cost=base_cost,
        )

        hotel_search_response_200_output_properties_item_rate_per_night_type_0.additional_properties = d
        return hotel_search_response_200_output_properties_item_rate_per_night_type_0

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
