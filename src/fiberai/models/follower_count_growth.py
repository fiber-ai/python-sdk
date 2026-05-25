from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FollowerCountGrowth")


@_attrs_define
class FollowerCountGrowth:
    """
    Attributes:
        type_ (Literal['follower_count_growth']):
        entity_type (Literal['company']):
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        min_absolute_growth (int | None | Unset): Minimum absolute follower increase to trigger. Omit or set to 0 for
            any increase.
        min_percent_growth (float | None | Unset): Minimum percent follower increase to trigger. Omit for any increase.
    """

    type_: Literal["follower_count_growth"]
    entity_type: Literal["company"]
    lookback_days: int | None | Unset = UNSET
    min_absolute_growth: int | None | Unset = UNSET
    min_percent_growth: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        min_absolute_growth: int | None | Unset
        if isinstance(self.min_absolute_growth, Unset):
            min_absolute_growth = UNSET
        else:
            min_absolute_growth = self.min_absolute_growth

        min_percent_growth: float | None | Unset
        if isinstance(self.min_percent_growth, Unset):
            min_percent_growth = UNSET
        else:
            min_percent_growth = self.min_percent_growth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "entityType": entity_type,
            }
        )
        if lookback_days is not UNSET:
            field_dict["lookbackDays"] = lookback_days
        if min_absolute_growth is not UNSET:
            field_dict["minAbsoluteGrowth"] = min_absolute_growth
        if min_percent_growth is not UNSET:
            field_dict["minPercentGrowth"] = min_percent_growth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["follower_count_growth"], d.pop("type"))
        if type_ != "follower_count_growth":
            raise ValueError(f"type must match const 'follower_count_growth', got '{type_}'")

        entity_type = cast(Literal["company"], d.pop("entityType"))
        if entity_type != "company":
            raise ValueError(f"entityType must match const 'company', got '{entity_type}'")

        def _parse_lookback_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        def _parse_min_absolute_growth(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_absolute_growth = _parse_min_absolute_growth(d.pop("minAbsoluteGrowth", UNSET))

        def _parse_min_percent_growth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_percent_growth = _parse_min_percent_growth(d.pop("minPercentGrowth", UNSET))

        follower_count_growth = cls(
            type_=type_,
            entity_type=entity_type,
            lookback_days=lookback_days,
            min_absolute_growth=min_absolute_growth,
            min_percent_growth=min_percent_growth,
        )

        follower_count_growth.additional_properties = d
        return follower_count_growth

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
