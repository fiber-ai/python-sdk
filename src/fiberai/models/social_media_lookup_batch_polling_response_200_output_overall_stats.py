from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SocialMediaLookupBatchPollingResponse200OutputOverallStats")


@_attrs_define
class SocialMediaLookupBatchPollingResponse200OutputOverallStats:
    """Summary statistics for the entire batch.

    Attributes:
        total_people (int): Total number of people in this batch.
        num_completed (int): Number of people whose lookup has completed (success or no-match).
        num_failed (int): Number of people whose lookup failed (insufficient info, error).
        num_remaining (int): Number of people still being processed.
    """

    total_people: int
    num_completed: int
    num_failed: int
    num_remaining: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_people = self.total_people

        num_completed = self.num_completed

        num_failed = self.num_failed

        num_remaining = self.num_remaining

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalPeople": total_people,
                "numCompleted": num_completed,
                "numFailed": num_failed,
                "numRemaining": num_remaining,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_people = d.pop("totalPeople")

        num_completed = d.pop("numCompleted")

        num_failed = d.pop("numFailed")

        num_remaining = d.pop("numRemaining")

        social_media_lookup_batch_polling_response_200_output_overall_stats = cls(
            total_people=total_people,
            num_completed=num_completed,
            num_failed=num_failed,
            num_remaining=num_remaining,
        )

        social_media_lookup_batch_polling_response_200_output_overall_stats.additional_properties = d
        return social_media_lookup_batch_polling_response_200_output_overall_stats

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
