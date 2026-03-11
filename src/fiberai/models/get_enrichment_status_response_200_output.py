from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_enrichment_status_response_200_output_current_stage import (
    GetEnrichmentStatusResponse200OutputCurrentStage,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetEnrichmentStatusResponse200Output")


@_attrs_define
class GetEnrichmentStatusResponse200Output:
    """
    Attributes:
        enrichment_id (str): Unique ID of the enrichment run
        current_stage (GetEnrichmentStatusResponse200OutputCurrentStage): Current stage of the enrichment process
        progress_percent (float): Progress percentage (0-100)
        steps_completed (list[str]): List of completed step names
        steps_remaining (list[str]): List of remaining step names
        created_at (str): When the enrichment was created
        current_step (None | str | Unset): Name of the current step being executed
        completed_at (None | str | Unset): When the enrichment completed
    """

    enrichment_id: str
    current_stage: GetEnrichmentStatusResponse200OutputCurrentStage
    progress_percent: float
    steps_completed: list[str]
    steps_remaining: list[str]
    created_at: str
    current_step: None | str | Unset = UNSET
    completed_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enrichment_id = self.enrichment_id

        current_stage = self.current_stage.value

        progress_percent = self.progress_percent

        steps_completed = self.steps_completed

        steps_remaining = self.steps_remaining

        created_at = self.created_at

        current_step: None | str | Unset
        if isinstance(self.current_step, Unset):
            current_step = UNSET
        else:
            current_step = self.current_step

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = self.completed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enrichmentId": enrichment_id,
                "currentStage": current_stage,
                "progressPercent": progress_percent,
                "stepsCompleted": steps_completed,
                "stepsRemaining": steps_remaining,
                "createdAt": created_at,
            }
        )
        if current_step is not UNSET:
            field_dict["currentStep"] = current_step
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enrichment_id = d.pop("enrichmentId")

        current_stage = GetEnrichmentStatusResponse200OutputCurrentStage(d.pop("currentStage"))

        progress_percent = d.pop("progressPercent")

        steps_completed = cast(list[str], d.pop("stepsCompleted"))

        steps_remaining = cast(list[str], d.pop("stepsRemaining"))

        created_at = d.pop("createdAt")

        def _parse_current_step(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_step = _parse_current_step(d.pop("currentStep", UNSET))

        def _parse_completed_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))

        get_enrichment_status_response_200_output = cls(
            enrichment_id=enrichment_id,
            current_stage=current_stage,
            progress_percent=progress_percent,
            steps_completed=steps_completed,
            steps_remaining=steps_remaining,
            created_at=created_at,
            current_step=current_step,
            completed_at=completed_at,
        )

        get_enrichment_status_response_200_output.additional_properties = d
        return get_enrichment_status_response_200_output

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
