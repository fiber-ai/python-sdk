from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.numeric_delta_change_direction import NumericDeltaChangeDirection

T = TypeVar("T", bound="NumericDeltaChange")


@_attrs_define
class NumericDeltaChange:
    """
    Attributes:
        kind (Literal['numeric']):
        previous (float | None): Previous value
        current (float | None): Current value
        direction (NumericDeltaChangeDirection): Direction of change
        absolute_change (float): Absolute numeric change
        percent_change (float | None): Percent change, null if previous was zero or null
    """

    kind: Literal["numeric"]
    previous: float | None
    current: float | None
    direction: NumericDeltaChangeDirection
    absolute_change: float
    percent_change: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        previous: float | None
        previous = self.previous

        current: float | None
        current = self.current

        direction = self.direction.value

        absolute_change = self.absolute_change

        percent_change: float | None
        percent_change = self.percent_change

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "previous": previous,
                "current": current,
                "direction": direction,
                "absoluteChange": absolute_change,
                "percentChange": percent_change,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = cast(Literal["numeric"], d.pop("kind"))
        if kind != "numeric":
            raise ValueError(f"kind must match const 'numeric', got '{kind}'")

        def _parse_previous(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        previous = _parse_previous(d.pop("previous"))

        def _parse_current(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        current = _parse_current(d.pop("current"))

        direction = NumericDeltaChangeDirection(d.pop("direction"))

        absolute_change = d.pop("absoluteChange")

        def _parse_percent_change(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        percent_change = _parse_percent_change(d.pop("percentChange"))

        numeric_delta_change = cls(
            kind=kind,
            previous=previous,
            current=current,
            direction=direction,
            absolute_change=absolute_change,
            percent_change=percent_change,
        )

        numeric_delta_change.additional_properties = d
        return numeric_delta_change

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
