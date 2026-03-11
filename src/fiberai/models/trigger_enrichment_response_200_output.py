from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trigger_enrichment_response_200_output_status import TriggerEnrichmentResponse200OutputStatus

T = TypeVar("T", bound="TriggerEnrichmentResponse200Output")


@_attrs_define
class TriggerEnrichmentResponse200Output:
    """
    Attributes:
        enrichment_id (str): Unique ID of the enrichment run
        status (TriggerEnrichmentResponse200OutputStatus): Initial status of the enrichment run
        estimated_credits (float): Estimated credits that will be charged for this enrichment
    """

    enrichment_id: str
    status: TriggerEnrichmentResponse200OutputStatus
    estimated_credits: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enrichment_id = self.enrichment_id

        status = self.status.value

        estimated_credits = self.estimated_credits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enrichmentId": enrichment_id,
                "status": status,
                "estimatedCredits": estimated_credits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enrichment_id = d.pop("enrichmentId")

        status = TriggerEnrichmentResponse200OutputStatus(d.pop("status"))

        estimated_credits = d.pop("estimatedCredits")

        trigger_enrichment_response_200_output = cls(
            enrichment_id=enrichment_id,
            status=status,
            estimated_credits=estimated_credits,
        )

        trigger_enrichment_response_200_output.additional_properties = d
        return trigger_enrichment_response_200_output

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
