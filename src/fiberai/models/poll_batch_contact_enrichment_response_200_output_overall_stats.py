from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PollBatchContactEnrichmentResponse200OutputOverallStats")


@_attrs_define
class PollBatchContactEnrichmentResponse200OutputOverallStats:
    """Overall statistics for the batch enrichment task

    Attributes:
        total_people_to_fetch (int): Total number of people in this bulk task
        num_completed (int): Number of people for which contact reveal process has been completed.
        num_remaining (int): Number of people remaining to be processed
        num_rejected (int): Number of people for which contact reveal process has been rejected either due to invalid
            input or person not found
        num_duplicates (int): Number of duplicates found in the input
    """

    total_people_to_fetch: int
    num_completed: int
    num_remaining: int
    num_rejected: int
    num_duplicates: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_people_to_fetch = self.total_people_to_fetch

        num_completed = self.num_completed

        num_remaining = self.num_remaining

        num_rejected = self.num_rejected

        num_duplicates = self.num_duplicates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalPeopleToFetch": total_people_to_fetch,
                "numCompleted": num_completed,
                "numRemaining": num_remaining,
                "numRejected": num_rejected,
                "numDuplicates": num_duplicates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_people_to_fetch = d.pop("totalPeopleToFetch")

        num_completed = d.pop("numCompleted")

        num_remaining = d.pop("numRemaining")

        num_rejected = d.pop("numRejected")

        num_duplicates = d.pop("numDuplicates")

        poll_batch_contact_enrichment_response_200_output_overall_stats = cls(
            total_people_to_fetch=total_people_to_fetch,
            num_completed=num_completed,
            num_remaining=num_remaining,
            num_rejected=num_rejected,
            num_duplicates=num_duplicates,
        )

        poll_batch_contact_enrichment_response_200_output_overall_stats.additional_properties = d
        return poll_batch_contact_enrichment_response_200_output_overall_stats

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
