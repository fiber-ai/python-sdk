from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lookalikes_poll_response_200_output_buckets_item_findings_item_match_confidence import (
    LookalikesPollResponse200OutputBucketsItemFindingsItemMatchConfidence,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="LookalikesPollResponse200OutputBucketsItemFindingsItem")


@_attrs_define
class LookalikesPollResponse200OutputBucketsItemFindingsItem:
    """
    Attributes:
        name (str): Company name.
        similarity_score (int): How closely this company resembles the bucket's companies (1-10; higher is more
            similar).
        opportunity_score (int): How attractive this company is as a new target for your list (1-10; higher is better).
        match_confidence (LookalikesPollResponse200OutputBucketsItemFindingsItemMatchConfidence): How strong a match
            this company is. 'definite' results are the strongest matches; 'stretch' results are worth a human look.
        rationale (str): Why this company was selected, referencing the patterns in your input list.
        domain (None | str | Unset): The company's primary domain.
    """

    name: str
    similarity_score: int
    opportunity_score: int
    match_confidence: LookalikesPollResponse200OutputBucketsItemFindingsItemMatchConfidence
    rationale: str
    domain: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        similarity_score = self.similarity_score

        opportunity_score = self.opportunity_score

        match_confidence = self.match_confidence.value

        rationale = self.rationale

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "similarityScore": similarity_score,
                "opportunityScore": opportunity_score,
                "matchConfidence": match_confidence,
                "rationale": rationale,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        similarity_score = d.pop("similarityScore")

        opportunity_score = d.pop("opportunityScore")

        match_confidence = LookalikesPollResponse200OutputBucketsItemFindingsItemMatchConfidence(
            d.pop("matchConfidence")
        )

        rationale = d.pop("rationale")

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        lookalikes_poll_response_200_output_buckets_item_findings_item = cls(
            name=name,
            similarity_score=similarity_score,
            opportunity_score=opportunity_score,
            match_confidence=match_confidence,
            rationale=rationale,
            domain=domain,
        )

        lookalikes_poll_response_200_output_buckets_item_findings_item.additional_properties = d
        return lookalikes_poll_response_200_output_buckets_item_findings_item

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
