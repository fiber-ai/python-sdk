from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LookalikesPollResponse200OutputProgress")


@_attrs_define
class LookalikesPollResponse200OutputProgress:
    """Per-phase progress. Poll until status is 'done' or 'failed'.

    Attributes:
        companies_resolved (int): Input companies matched so far.
        companies_total (int): Input companies provided.
        buckets_found (int): Company groupings identified.
        candidates_found (int): Candidates selected for grading across all groupings.
        reviews_completed (int): Candidates graded so far, out of candidatesFound.
    """

    companies_resolved: int
    companies_total: int
    buckets_found: int
    candidates_found: int
    reviews_completed: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        companies_resolved = self.companies_resolved

        companies_total = self.companies_total

        buckets_found = self.buckets_found

        candidates_found = self.candidates_found

        reviews_completed = self.reviews_completed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companiesResolved": companies_resolved,
                "companiesTotal": companies_total,
                "bucketsFound": buckets_found,
                "candidatesFound": candidates_found,
                "reviewsCompleted": reviews_completed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        companies_resolved = d.pop("companiesResolved")

        companies_total = d.pop("companiesTotal")

        buckets_found = d.pop("bucketsFound")

        candidates_found = d.pop("candidatesFound")

        reviews_completed = d.pop("reviewsCompleted")

        lookalikes_poll_response_200_output_progress = cls(
            companies_resolved=companies_resolved,
            companies_total=companies_total,
            buckets_found=buckets_found,
            candidates_found=candidates_found,
            reviews_completed=reviews_completed,
        )

        lookalikes_poll_response_200_output_progress.additional_properties = d
        return lookalikes_poll_response_200_output_progress

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
