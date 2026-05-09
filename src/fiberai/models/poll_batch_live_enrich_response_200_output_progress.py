from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PollBatchLiveEnrichResponse200OutputProgress")


@_attrs_define
class PollBatchLiveEnrichResponse200OutputProgress:
    """
    Attributes:
        total (int): Total unique identifiers in the batch (excluding duplicates skipped at submission)
        completed (int): Number successfully enriched
        not_found (int): Number of identifiers not found on LinkedIn
        failed (int): Number that failed due to enrichment errors
        malformed (int): Number of identifiers that could not be parsed from your input
        pending (int): Number still waiting or in progress
    """

    total: int
    completed: int
    not_found: int
    failed: int
    malformed: int
    pending: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        completed = self.completed

        not_found = self.not_found

        failed = self.failed

        malformed = self.malformed

        pending = self.pending

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "completed": completed,
                "notFound": not_found,
                "failed": failed,
                "malformed": malformed,
                "pending": pending,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        completed = d.pop("completed")

        not_found = d.pop("notFound")

        failed = d.pop("failed")

        malformed = d.pop("malformed")

        pending = d.pop("pending")

        poll_batch_live_enrich_response_200_output_progress = cls(
            total=total,
            completed=completed,
            not_found=not_found,
            failed=failed,
            malformed=malformed,
            pending=pending,
        )

        poll_batch_live_enrich_response_200_output_progress.additional_properties = d
        return poll_batch_live_enrich_response_200_output_progress

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
