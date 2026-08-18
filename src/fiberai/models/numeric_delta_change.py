from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.numeric_delta_change_direction import NumericDeltaChangeDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="NumericDeltaChange")


@_attrs_define
class NumericDeltaChange:
    """
    Attributes:
        kind (Literal['numeric']):
        direction (NumericDeltaChangeDirection): Direction of change
        absolute_change (float): Absolute numeric change
        previous (float | None | Unset): Previous value
        current (float | None | Unset): Current value
        percent_change (float | None | Unset): Percent change, null if previous was zero or null
    """

    kind: Literal["numeric"]
    direction: NumericDeltaChangeDirection
    absolute_change: float
    previous: float | None | Unset = UNSET
    current: float | None | Unset = UNSET
    percent_change: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        direction = self.direction.value

        absolute_change = self.absolute_change

        previous: float | None | Unset
        if isinstance(self.previous, Unset):
            previous = UNSET
        else:
            previous = self.previous

        current: float | None | Unset
        if isinstance(self.current, Unset):
            current = UNSET
        else:
            current = self.current

        percent_change: float | None | Unset
        if isinstance(self.percent_change, Unset):
            percent_change = UNSET
        else:
            percent_change = self.percent_change

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "direction": direction,
                "absoluteChange": absolute_change,
            }
        )
        if previous is not UNSET:
            field_dict["previous"] = previous
        if current is not UNSET:
            field_dict["current"] = current
        if percent_change is not UNSET:
            field_dict["percentChange"] = percent_change

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = cast(Literal["numeric"], d.pop("kind"))
        if kind != "numeric":
            raise ValueError(f"kind must match const 'numeric', got '{kind}'")

        direction = NumericDeltaChangeDirection(d.pop("direction"))

        absolute_change = d.pop("absoluteChange")

        def _parse_previous(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        previous = _parse_previous(d.pop("previous", UNSET))

        def _parse_current(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        current = _parse_current(d.pop("current", UNSET))

        def _parse_percent_change(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        percent_change = _parse_percent_change(d.pop("percentChange", UNSET))

        numeric_delta_change = cls(
            kind=kind,
            direction=direction,
            absolute_change=absolute_change,
            previous=previous,
            current=current,
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
