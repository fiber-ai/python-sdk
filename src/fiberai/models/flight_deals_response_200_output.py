from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.flight_deals_response_200_output_deals_item import FlightDealsResponse200OutputDealsItem


T = TypeVar("T", bound="FlightDealsResponse200Output")


@_attrs_define
class FlightDealsResponse200Output:
    """
    Attributes:
        deals (list[FlightDealsResponse200OutputDealsItem]): Cheap round-trip deals from the departure location, ranked
            by savings versus the typical price. Empty when none match the request.
        currency_code (str): ISO 4217 currency code for prices in this response (e.g. 'USD', 'EUR', 'GBP').
    """

    deals: list[FlightDealsResponse200OutputDealsItem]
    currency_code: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deals = []
        for deals_item_data in self.deals:
            deals_item = deals_item_data.to_dict()
            deals.append(deals_item)

        currency_code = self.currency_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deals": deals,
                "currencyCode": currency_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flight_deals_response_200_output_deals_item import (
            FlightDealsResponse200OutputDealsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        deals = []
        _deals = d.pop("deals")
        for deals_item_data in _deals:
            deals_item = FlightDealsResponse200OutputDealsItem.from_dict(deals_item_data)

            deals.append(deals_item)

        currency_code = d.pop("currencyCode")

        flight_deals_response_200_output = cls(
            deals=deals,
            currency_code=currency_code,
        )

        flight_deals_response_200_output.additional_properties = d
        return flight_deals_response_200_output

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
