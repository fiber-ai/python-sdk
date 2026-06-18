from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.person_tag_gained_tags_item import PersonTagGainedTagsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonTagGained")


@_attrs_define
class PersonTagGained:
    """
    Attributes:
        type_ (Literal['person_tag_gained']):
        entity_type (Literal['person']):
        tags (list[PersonTagGainedTagsItem]): Alert when the person gains any of these system-assigned tags.
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        is_dummy (bool | Unset): When true, this rule only fires via the fire-dummy endpoint and is skipped during
            normal pipeline runs.
    """

    type_: Literal["person_tag_gained"]
    entity_type: Literal["person"]
    tags: list[PersonTagGainedTagsItem]
    lookback_days: int | None | Unset = UNSET
    is_dummy: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.value
            tags.append(tags_item)

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        is_dummy = self.is_dummy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "entityType": entity_type,
                "tags": tags,
            }
        )
        if lookback_days is not UNSET:
            field_dict["lookbackDays"] = lookback_days
        if is_dummy is not UNSET:
            field_dict["isDummy"] = is_dummy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["person_tag_gained"], d.pop("type"))
        if type_ != "person_tag_gained":
            raise ValueError(f"type must match const 'person_tag_gained', got '{type_}'")

        entity_type = cast(Literal["person"], d.pop("entityType"))
        if entity_type != "person":
            raise ValueError(f"entityType must match const 'person', got '{entity_type}'")

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = PersonTagGainedTagsItem(tags_item_data)

            tags.append(tags_item)

        def _parse_lookback_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        is_dummy = d.pop("isDummy", UNSET)

        person_tag_gained = cls(
            type_=type_,
            entity_type=entity_type,
            tags=tags,
            lookback_days=lookback_days,
            is_dummy=is_dummy,
        )

        person_tag_gained.additional_properties = d
        return person_tag_gained

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
