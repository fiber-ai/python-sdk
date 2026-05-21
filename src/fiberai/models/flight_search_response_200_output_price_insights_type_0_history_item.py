from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlightSearchResponse200OutputPriceInsightsType0HistoryItem")


@_attrs_define
class FlightSearchResponse200OutputPriceInsightsType0HistoryItem:
    """
    Attributes:
        price (int): Observed price in whole currency units.
        snapshot_date (None | str | Unset): Date this price was observed (e.g. '2024-09-19').
    """

    price: int
    snapshot_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price = self.price

        snapshot_date: None | str | Unset
        if isinstance(self.snapshot_date, Unset):
            snapshot_date = UNSET
        else:
            snapshot_date = self.snapshot_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "price": price,
            }
        )
        if snapshot_date is not UNSET:
            field_dict["snapshotDate"] = snapshot_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price = d.pop("price")

        def _parse_snapshot_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        snapshot_date = _parse_snapshot_date(d.pop("snapshotDate", UNSET))

        flight_search_response_200_output_price_insights_type_0_history_item = cls(
            price=price,
            snapshot_date=snapshot_date,
        )

        flight_search_response_200_output_price_insights_type_0_history_item.additional_properties = d
        return flight_search_response_200_output_price_insights_type_0_history_item

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
