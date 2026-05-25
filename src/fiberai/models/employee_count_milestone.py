from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.employee_count_milestone_direction import EmployeeCountMilestoneDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployeeCountMilestone")


@_attrs_define
class EmployeeCountMilestone:
    """
    Attributes:
        type_ (Literal['employee_count_milestone']):
        entity_type (Literal['company']):
        milestone (int): Employee count milestone to watch (e.g. 100, 500, 1000)
        direction (EmployeeCountMilestoneDirection): Whether to alert when crossing above or below the milestone
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
    """

    type_: Literal["employee_count_milestone"]
    entity_type: Literal["company"]
    milestone: int
    direction: EmployeeCountMilestoneDirection
    lookback_days: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        milestone = self.milestone

        direction = self.direction.value

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "entityType": entity_type,
                "milestone": milestone,
                "direction": direction,
            }
        )
        if lookback_days is not UNSET:
            field_dict["lookbackDays"] = lookback_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["employee_count_milestone"], d.pop("type"))
        if type_ != "employee_count_milestone":
            raise ValueError(f"type must match const 'employee_count_milestone', got '{type_}'")

        entity_type = cast(Literal["company"], d.pop("entityType"))
        if entity_type != "company":
            raise ValueError(f"entityType must match const 'company', got '{entity_type}'")

        milestone = d.pop("milestone")

        direction = EmployeeCountMilestoneDirection(d.pop("direction"))

        def _parse_lookback_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        employee_count_milestone = cls(
            type_=type_,
            entity_type=entity_type,
            milestone=milestone,
            direction=direction,
            lookback_days=lookback_days,
        )

        employee_count_milestone.additional_properties = d
        return employee_count_milestone

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
