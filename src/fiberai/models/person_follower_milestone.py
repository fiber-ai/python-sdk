from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.person_follower_milestone_direction import PersonFollowerMilestoneDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonFollowerMilestone")


@_attrs_define
class PersonFollowerMilestone:
    """
    Attributes:
        type_ (Literal['person_follower_milestone']):
        entity_type (Literal['person']):
        threshold (int): Follower count to watch for crossing
        direction (PersonFollowerMilestoneDirection): Whether to alert when crossing above or below the threshold
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
    """

    type_: Literal["person_follower_milestone"]
    entity_type: Literal["person"]
    threshold: int
    direction: PersonFollowerMilestoneDirection
    lookback_days: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

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
        type_ = cast(Literal["person_follower_milestone"], d.pop("type"))
        if type_ != "person_follower_milestone":
            raise ValueError(f"type must match const 'person_follower_milestone', got '{type_}'")

        entity_type = cast(Literal["person"], d.pop("entityType"))
        if entity_type != "person":
            raise ValueError(f"entityType must match const 'person', got '{entity_type}'")

        threshold = d.pop("threshold")

        direction = PersonFollowerMilestoneDirection(d.pop("direction"))

        def _parse_lookback_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        person_follower_milestone = cls(
            type_=type_,
            entity_type=entity_type,
            threshold=threshold,
            direction=direction,
            lookback_days=lookback_days,
        )

        person_follower_milestone.additional_properties = d
        return person_follower_milestone

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
