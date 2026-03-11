from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.estimate_enrichment_cost_response_200_output_breakdown import (
        EstimateEnrichmentCostResponse200OutputBreakdown,
    )
    from ..models.estimate_enrichment_cost_response_200_output_time_estimate import (
        EstimateEnrichmentCostResponse200OutputTimeEstimate,
    )


T = TypeVar("T", bound="EstimateEnrichmentCostResponse200Output")


@_attrs_define
class EstimateEnrichmentCostResponse200Output:
    """
    Attributes:
        total_credits (float): Total estimated credits required
        breakdown (EstimateEnrichmentCostResponse200OutputBreakdown): Detailed cost breakdown by operation type
        time_estimate (EstimateEnrichmentCostResponse200OutputTimeEstimate): Estimated time to complete enrichment
    """

    total_credits: float
    breakdown: EstimateEnrichmentCostResponse200OutputBreakdown
    time_estimate: EstimateEnrichmentCostResponse200OutputTimeEstimate
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_credits = self.total_credits

        breakdown = self.breakdown.to_dict()

        time_estimate = self.time_estimate.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalCredits": total_credits,
                "breakdown": breakdown,
                "timeEstimate": time_estimate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.estimate_enrichment_cost_response_200_output_breakdown import (
            EstimateEnrichmentCostResponse200OutputBreakdown,
        )
        from ..models.estimate_enrichment_cost_response_200_output_time_estimate import (
            EstimateEnrichmentCostResponse200OutputTimeEstimate,
        )

        d = dict(src_dict)
        total_credits = d.pop("totalCredits")

        breakdown = EstimateEnrichmentCostResponse200OutputBreakdown.from_dict(d.pop("breakdown"))

        time_estimate = EstimateEnrichmentCostResponse200OutputTimeEstimate.from_dict(d.pop("timeEstimate"))

        estimate_enrichment_cost_response_200_output = cls(
            total_credits=total_credits,
            breakdown=breakdown,
            time_estimate=time_estimate,
        )

        estimate_enrichment_cost_response_200_output.additional_properties = d
        return estimate_enrichment_cost_response_200_output

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
