from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_to_linkedin_single_response_200_output_debug_timings_type_0_resolver_steps_item_outcome import (
    GithubToLinkedinSingleResponse200OutputDebugTimingsType0ResolverStepsItemOutcome,
)
from ..models.github_to_linkedin_single_response_200_output_debug_timings_type_0_resolver_steps_item_step import (
    GithubToLinkedinSingleResponse200OutputDebugTimingsType0ResolverStepsItemStep,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubToLinkedinSingleResponse200OutputDebugTimingsType0ResolverStepsItem")


@_attrs_define
class GithubToLinkedinSingleResponse200OutputDebugTimingsType0ResolverStepsItem:
    """
    Attributes:
        step (GithubToLinkedinSingleResponse200OutputDebugTimingsType0ResolverStepsItemStep):
        duration_ms (int):
        outcome (GithubToLinkedinSingleResponse200OutputDebugTimingsType0ResolverStepsItemOutcome):
        detail (None | str | Unset):
    """

    step: GithubToLinkedinSingleResponse200OutputDebugTimingsType0ResolverStepsItemStep
    duration_ms: int
    outcome: GithubToLinkedinSingleResponse200OutputDebugTimingsType0ResolverStepsItemOutcome
    detail: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step = self.step.value

        duration_ms = self.duration_ms

        outcome = self.outcome.value

        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step": step,
                "durationMs": duration_ms,
                "outcome": outcome,
            }
        )
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        step = GithubToLinkedinSingleResponse200OutputDebugTimingsType0ResolverStepsItemStep(d.pop("step"))

        duration_ms = d.pop("durationMs")

        outcome = GithubToLinkedinSingleResponse200OutputDebugTimingsType0ResolverStepsItemOutcome(d.pop("outcome"))

        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))

        github_to_linkedin_single_response_200_output_debug_timings_type_0_resolver_steps_item = cls(
            step=step,
            duration_ms=duration_ms,
            outcome=outcome,
            detail=detail,
        )

        github_to_linkedin_single_response_200_output_debug_timings_type_0_resolver_steps_item.additional_properties = d
        return github_to_linkedin_single_response_200_output_debug_timings_type_0_resolver_steps_item

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
