from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlightSearchBodyLayoverDurationType0")


@_attrs_define
class FlightSearchBodyLayoverDurationType0:
    """Constrain layover duration. Omit to allow any layover length.

    Attributes:
        min_minutes (int | None | Unset): Minimum layover duration in minutes. Omit for no minimum.
        max_minutes (int | None | Unset): Maximum layover duration in minutes. Omit for no maximum.
    """

    min_minutes: int | None | Unset = UNSET
    max_minutes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_minutes: int | None | Unset
        if isinstance(self.min_minutes, Unset):
            min_minutes = UNSET
        else:
            min_minutes = self.min_minutes

        max_minutes: int | None | Unset
        if isinstance(self.max_minutes, Unset):
            max_minutes = UNSET
        else:
            max_minutes = self.max_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_minutes is not UNSET:
            field_dict["minMinutes"] = min_minutes
        if max_minutes is not UNSET:
            field_dict["maxMinutes"] = max_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_min_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_minutes = _parse_min_minutes(d.pop("minMinutes", UNSET))

        def _parse_max_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_minutes = _parse_max_minutes(d.pop("maxMinutes", UNSET))

        flight_search_body_layover_duration_type_0 = cls(
            min_minutes=min_minutes,
            max_minutes=max_minutes,
        )

        flight_search_body_layover_duration_type_0.additional_properties = d
        return flight_search_body_layover_duration_type_0

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
