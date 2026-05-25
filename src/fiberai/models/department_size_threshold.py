from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.department_size_threshold_direction import DepartmentSizeThresholdDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="DepartmentSizeThreshold")


@_attrs_define
class DepartmentSizeThreshold:
    """
    Attributes:
        type_ (Literal['department_size_threshold']):
        entity_type (Literal['company']):
        department (str): Department name to track (e.g. 'Engineering', 'Sales'). Matched against the company's
            organizational structure.
        threshold (int): The employee count threshold to watch for crossing
        direction (DepartmentSizeThresholdDirection): Whether to alert when department size crosses above or below the
            threshold
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
    """

    type_: Literal["department_size_threshold"]
    entity_type: Literal["company"]
    department: str
    threshold: int
    direction: DepartmentSizeThresholdDirection
    lookback_days: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        department = self.department

        threshold = self.threshold

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
                "department": department,
                "threshold": threshold,
                "direction": direction,
            }
        )
        if lookback_days is not UNSET:
            field_dict["lookbackDays"] = lookback_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["department_size_threshold"], d.pop("type"))
        if type_ != "department_size_threshold":
            raise ValueError(f"type must match const 'department_size_threshold', got '{type_}'")

        entity_type = cast(Literal["company"], d.pop("entityType"))
        if entity_type != "company":
            raise ValueError(f"entityType must match const 'company', got '{entity_type}'")

        department = d.pop("department")

        threshold = d.pop("threshold")

        direction = DepartmentSizeThresholdDirection(d.pop("direction"))

        def _parse_lookback_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        department_size_threshold = cls(
            type_=type_,
            entity_type=entity_type,
            department=department,
            threshold=threshold,
            direction=direction,
            lookback_days=lookback_days,
        )

        department_size_threshold.additional_properties = d
        return department_size_threshold

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
