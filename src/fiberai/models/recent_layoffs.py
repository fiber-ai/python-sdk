from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecentLayoffs")


@_attrs_define
class RecentLayoffs:
    """
    Attributes:
        type_ (Literal['recent_layoffs']):
        entity_type (Literal['company']):
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        is_dummy (bool | Unset): When true, this rule only fires via the fire-dummy endpoint and is skipped during
            normal pipeline runs.
        min_people_affected (int | None | Unset): Only alert if at least this many people were laid off. Omit for any
            layoff.
        min_percent_affected (float | None | Unset): Only alert if at least this percentage of the workforce was laid
            off. Omit for any layoff.
    """

    type_: Literal["recent_layoffs"]
    entity_type: Literal["company"]
    lookback_days: int | None | Unset = UNSET
    is_dummy: bool | Unset = UNSET
    min_people_affected: int | None | Unset = UNSET
    min_percent_affected: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        is_dummy = self.is_dummy

        min_people_affected: int | None | Unset
        if isinstance(self.min_people_affected, Unset):
            min_people_affected = UNSET
        else:
            min_people_affected = self.min_people_affected

        min_percent_affected: float | None | Unset
        if isinstance(self.min_percent_affected, Unset):
            min_percent_affected = UNSET
        else:
            min_percent_affected = self.min_percent_affected

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
        if is_dummy is not UNSET:
            field_dict["isDummy"] = is_dummy
        if min_people_affected is not UNSET:
            field_dict["minPeopleAffected"] = min_people_affected
        if min_percent_affected is not UNSET:
            field_dict["minPercentAffected"] = min_percent_affected

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["recent_layoffs"], d.pop("type"))
        if type_ != "recent_layoffs":
            raise ValueError(f"type must match const 'recent_layoffs', got '{type_}'")

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

        is_dummy = d.pop("isDummy", UNSET)

        def _parse_min_people_affected(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_people_affected = _parse_min_people_affected(d.pop("minPeopleAffected", UNSET))

        def _parse_min_percent_affected(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_percent_affected = _parse_min_percent_affected(d.pop("minPercentAffected", UNSET))

        recent_layoffs = cls(
            type_=type_,
            entity_type=entity_type,
            lookback_days=lookback_days,
            is_dummy=is_dummy,
            min_people_affected=min_people_affected,
            min_percent_affected=min_percent_affected,
        )

        recent_layoffs.additional_properties = d
        return recent_layoffs

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
