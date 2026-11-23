from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lookalikes_single_response_200_output_results_item_match_confidence import (
    LookalikesSingleResponse200OutputResultsItemMatchConfidence,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="LookalikesSingleResponse200OutputResultsItem")


@_attrs_define
class LookalikesSingleResponse200OutputResultsItem:
    """
    Attributes:
        name (str): Company name.
        domain (None | str | Unset): The company's primary domain.
        similarity_score (int | Unset): How closely this company resembles the companies you asked about (1-10; higher
            is more similar).
        opportunity_score (int | Unset): How attractive this company is as a new target for your list (1-10; higher is
            better).
        match_confidence (LookalikesSingleResponse200OutputResultsItemMatchConfidence | Unset): How strong a match this
            company is. 'definite' results are the strongest matches; 'stretch' results are worth a human look.
        rationale (str | Unset): Why this company is a match for the companies you asked about.
    """

    name: str
    domain: None | str | Unset = UNSET
    similarity_score: int | Unset = UNSET
    opportunity_score: int | Unset = UNSET
    match_confidence: LookalikesSingleResponse200OutputResultsItemMatchConfidence | Unset = UNSET
    rationale: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        similarity_score = self.similarity_score

        opportunity_score = self.opportunity_score

        match_confidence: str | Unset = UNSET
        if not isinstance(self.match_confidence, Unset):
            match_confidence = self.match_confidence.value

        rationale = self.rationale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain
        if similarity_score is not UNSET:
            field_dict["similarityScore"] = similarity_score
        if opportunity_score is not UNSET:
            field_dict["opportunityScore"] = opportunity_score
        if match_confidence is not UNSET:
            field_dict["matchConfidence"] = match_confidence
        if rationale is not UNSET:
            field_dict["rationale"] = rationale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        similarity_score = d.pop("similarityScore", UNSET)

        opportunity_score = d.pop("opportunityScore", UNSET)

        _match_confidence = d.pop("matchConfidence", UNSET)
        match_confidence: LookalikesSingleResponse200OutputResultsItemMatchConfidence | Unset
        if isinstance(_match_confidence, Unset):
            match_confidence = UNSET
        else:
            match_confidence = LookalikesSingleResponse200OutputResultsItemMatchConfidence(_match_confidence)

        rationale = d.pop("rationale", UNSET)

        lookalikes_single_response_200_output_results_item = cls(
            name=name,
            domain=domain,
            similarity_score=similarity_score,
            opportunity_score=opportunity_score,
            match_confidence=match_confidence,
            rationale=rationale,
        )

        lookalikes_single_response_200_output_results_item.additional_properties = d
        return lookalikes_single_response_200_output_results_item

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
