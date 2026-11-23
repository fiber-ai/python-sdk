from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTrackerOverviewResponse200OutputEntityLimitsType0People")


@_attrs_define
class GetTrackerOverviewResponse200OutputEntityLimitsType0People:
    """Limit and usage for tracked people.

    Attributes:
        tracked (int): Currently tracked in active lists. Entities in paused lists are not counted until the list is
            resumed.
        limit (int | None | Unset): The most that can be tracked across your active lists. Null when there is no limit.
        remaining (int | None | Unset): How many more can be added before the limit is reached. Null when there is no
            limit.
    """

    tracked: int
    limit: int | None | Unset = UNSET
    remaining: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tracked = self.tracked

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        remaining: int | None | Unset
        if isinstance(self.remaining, Unset):
            remaining = UNSET
        else:
            remaining = self.remaining

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tracked": tracked,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit
        if remaining is not UNSET:
            field_dict["remaining"] = remaining

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tracked = d.pop("tracked")

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        def _parse_remaining(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        remaining = _parse_remaining(d.pop("remaining", UNSET))

        get_tracker_overview_response_200_output_entity_limits_type_0_people = cls(
            tracked=tracked,
            limit=limit,
            remaining=remaining,
        )

        get_tracker_overview_response_200_output_entity_limits_type_0_people.additional_properties = d
        return get_tracker_overview_response_200_output_entity_limits_type_0_people

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
