from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.headcount_growth_percent_direction import HeadcountGrowthPercentDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="HeadcountGrowthPercent")


@_attrs_define
class HeadcountGrowthPercent:
    """
    Attributes:
        type_ (Literal['headcount_growth_percent']):
        entity_type (Literal['company']):
        min_percent_change (float): Minimum percent change to trigger (e.g. 20 means 20% growth)
        direction (HeadcountGrowthPercentDirection): Whether to alert on growth, shrinkage, or either
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        is_dummy (bool | Unset): When true, this rule only fires via the fire-dummy endpoint and is skipped during
            normal pipeline runs.
        min_starting_headcount (int | None | Unset): Only alert if the company had at least this many employees before
            the change. Omit for any starting size.
    """

    type_: Literal["headcount_growth_percent"]
    entity_type: Literal["company"]
    min_percent_change: float
    direction: HeadcountGrowthPercentDirection
    lookback_days: int | None | Unset = UNSET
    is_dummy: bool | Unset = UNSET
    min_starting_headcount: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        min_percent_change = self.min_percent_change

        direction = self.direction.value

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        is_dummy = self.is_dummy

        min_starting_headcount: int | None | Unset
        if isinstance(self.min_starting_headcount, Unset):
            min_starting_headcount = UNSET
        else:
            min_starting_headcount = self.min_starting_headcount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "entityType": entity_type,
                "minPercentChange": min_percent_change,
                "direction": direction,
            }
        )
        if lookback_days is not UNSET:
            field_dict["lookbackDays"] = lookback_days
        if is_dummy is not UNSET:
            field_dict["isDummy"] = is_dummy
        if min_starting_headcount is not UNSET:
            field_dict["minStartingHeadcount"] = min_starting_headcount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["headcount_growth_percent"], d.pop("type"))
        if type_ != "headcount_growth_percent":
            raise ValueError(f"type must match const 'headcount_growth_percent', got '{type_}'")

        entity_type = cast(Literal["company"], d.pop("entityType"))
        if entity_type != "company":
            raise ValueError(f"entityType must match const 'company', got '{entity_type}'")

        min_percent_change = d.pop("minPercentChange")

        direction = HeadcountGrowthPercentDirection(d.pop("direction"))

        def _parse_lookback_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        is_dummy = d.pop("isDummy", UNSET)

        def _parse_min_starting_headcount(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_starting_headcount = _parse_min_starting_headcount(d.pop("minStartingHeadcount", UNSET))

        headcount_growth_percent = cls(
            type_=type_,
            entity_type=entity_type,
            min_percent_change=min_percent_change,
            direction=direction,
            lookback_days=lookback_days,
            is_dummy=is_dummy,
            min_starting_headcount=min_starting_headcount,
        )

        headcount_growth_percent.additional_properties = d
        return headcount_growth_percent

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
