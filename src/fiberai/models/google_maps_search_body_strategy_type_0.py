from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.google_maps_search_body_strategy_type_0_strategy import GoogleMapsSearchBodyStrategyType0Strategy

T = TypeVar("T", bound="GoogleMapsSearchBodyStrategyType0")


@_attrs_define
class GoogleMapsSearchBodyStrategyType0:
    """
    Attributes:
        strategy (GoogleMapsSearchBodyStrategyType0Strategy): Does a broad search across all cities in the United
            States. Not as exhaustive as, for example, a city-specific search.
    """

    strategy: GoogleMapsSearchBodyStrategyType0Strategy
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy = self.strategy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategy": strategy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        strategy = GoogleMapsSearchBodyStrategyType0Strategy(d.pop("strategy"))

        google_maps_search_body_strategy_type_0 = cls(
            strategy=strategy,
        )

        google_maps_search_body_strategy_type_0.additional_properties = d
        return google_maps_search_body_strategy_type_0

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
