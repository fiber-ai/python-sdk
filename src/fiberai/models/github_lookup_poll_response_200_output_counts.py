from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GithubLookupPollResponse200OutputCounts")


@_attrs_define
class GithubLookupPollResponse200OutputCounts:
    """Breakdown of lookup progress. All fields sum to the total number of people in the run.

    Attributes:
        total (int): Total number of people submitted in this run.
        found (int): Number of people for whom a GitHub profile was found.
        not_found (int): Number of people for whom no GitHub profile could be found after searching.
        invalid_input (int): Number of people whose input could not be resolved (e.g. unresolvable LinkedIn URL,
            insufficient information).
        failed (int): Number of people whose lookup failed due to a system error.
        pending (int): Number of people still waiting to be processed.
    """

    total: int
    found: int
    not_found: int
    invalid_input: int
    failed: int
    pending: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        found = self.found

        not_found = self.not_found

        invalid_input = self.invalid_input

        failed = self.failed

        pending = self.pending

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "found": found,
                "notFound": not_found,
                "invalidInput": invalid_input,
                "failed": failed,
                "pending": pending,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        found = d.pop("found")

        not_found = d.pop("notFound")

        invalid_input = d.pop("invalidInput")

        failed = d.pop("failed")

        pending = d.pop("pending")

        github_lookup_poll_response_200_output_counts = cls(
            total=total,
            found=found,
            not_found=not_found,
            invalid_input=invalid_input,
            failed=failed,
            pending=pending,
        )

        github_lookup_poll_response_200_output_counts.additional_properties = d
        return github_lookup_poll_response_200_output_counts

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
