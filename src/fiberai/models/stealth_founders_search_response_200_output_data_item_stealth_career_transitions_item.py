from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.stealth_founders_search_response_200_output_data_item_stealth_career_transitions_item_added_current_experiences_item import (
        StealthFoundersSearchResponse200OutputDataItemStealthCareerTransitionsItemAddedCurrentExperiencesItem,
    )
    from ..models.stealth_founders_search_response_200_output_data_item_stealth_career_transitions_item_removed_current_experiences_item import (
        StealthFoundersSearchResponse200OutputDataItemStealthCareerTransitionsItemRemovedCurrentExperiencesItem,
    )


T = TypeVar("T", bound="StealthFoundersSearchResponse200OutputDataItemStealthCareerTransitionsItem")


@_attrs_define
class StealthFoundersSearchResponse200OutputDataItemStealthCareerTransitionsItem:
    """
    Attributes:
        before_snapshot_date (str): Older snapshot timestamp in this transition.
        after_snapshot_date (str): Newer snapshot timestamp in this transition.
        added_current_experiences
            (list[StealthFoundersSearchResponse200OutputDataItemStealthCareerTransitionsItemAddedCurrentExperiencesItem]):
            Current experiences that appeared in the newer snapshot and were absent in the older snapshot.
        removed_current_experiences
            (list[StealthFoundersSearchResponse200OutputDataItemStealthCareerTransitionsItemRemovedCurrentExperiencesItem]):
            Current experiences that existed in the older snapshot and disappeared in the newer snapshot.
        stealth_state_changed (bool): Whether the person switched stealth state between the two snapshots.
    """

    before_snapshot_date: str
    after_snapshot_date: str
    added_current_experiences: list[
        StealthFoundersSearchResponse200OutputDataItemStealthCareerTransitionsItemAddedCurrentExperiencesItem
    ]
    removed_current_experiences: list[
        StealthFoundersSearchResponse200OutputDataItemStealthCareerTransitionsItemRemovedCurrentExperiencesItem
    ]
    stealth_state_changed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        before_snapshot_date = self.before_snapshot_date

        after_snapshot_date = self.after_snapshot_date

        added_current_experiences = []
        for added_current_experiences_item_data in self.added_current_experiences:
            added_current_experiences_item = added_current_experiences_item_data.to_dict()
            added_current_experiences.append(added_current_experiences_item)

        removed_current_experiences = []
        for removed_current_experiences_item_data in self.removed_current_experiences:
            removed_current_experiences_item = removed_current_experiences_item_data.to_dict()
            removed_current_experiences.append(removed_current_experiences_item)

        stealth_state_changed = self.stealth_state_changed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "beforeSnapshotDate": before_snapshot_date,
                "afterSnapshotDate": after_snapshot_date,
                "addedCurrentExperiences": added_current_experiences,
                "removedCurrentExperiences": removed_current_experiences,
                "stealthStateChanged": stealth_state_changed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stealth_founders_search_response_200_output_data_item_stealth_career_transitions_item_added_current_experiences_item import (
            StealthFoundersSearchResponse200OutputDataItemStealthCareerTransitionsItemAddedCurrentExperiencesItem,  # noqa: PLC0415
        )
        from ..models.stealth_founders_search_response_200_output_data_item_stealth_career_transitions_item_removed_current_experiences_item import (
            StealthFoundersSearchResponse200OutputDataItemStealthCareerTransitionsItemRemovedCurrentExperiencesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        before_snapshot_date = d.pop("beforeSnapshotDate")

        after_snapshot_date = d.pop("afterSnapshotDate")

        added_current_experiences = []
        _added_current_experiences = d.pop("addedCurrentExperiences")
        for added_current_experiences_item_data in _added_current_experiences:
            added_current_experiences_item = StealthFoundersSearchResponse200OutputDataItemStealthCareerTransitionsItemAddedCurrentExperiencesItem.from_dict(
                added_current_experiences_item_data
            )

            added_current_experiences.append(added_current_experiences_item)

        removed_current_experiences = []
        _removed_current_experiences = d.pop("removedCurrentExperiences")
        for removed_current_experiences_item_data in _removed_current_experiences:
            removed_current_experiences_item = StealthFoundersSearchResponse200OutputDataItemStealthCareerTransitionsItemRemovedCurrentExperiencesItem.from_dict(
                removed_current_experiences_item_data
            )

            removed_current_experiences.append(removed_current_experiences_item)

        stealth_state_changed = d.pop("stealthStateChanged")

        stealth_founders_search_response_200_output_data_item_stealth_career_transitions_item = cls(
            before_snapshot_date=before_snapshot_date,
            after_snapshot_date=after_snapshot_date,
            added_current_experiences=added_current_experiences,
            removed_current_experiences=removed_current_experiences,
            stealth_state_changed=stealth_state_changed,
        )

        stealth_founders_search_response_200_output_data_item_stealth_career_transitions_item.additional_properties = d
        return stealth_founders_search_response_200_output_data_item_stealth_career_transitions_item

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
