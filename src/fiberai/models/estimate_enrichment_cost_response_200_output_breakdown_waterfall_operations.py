from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EstimateEnrichmentCostResponse200OutputBreakdownWaterfallOperations")


@_attrs_define
class EstimateEnrichmentCostResponse200OutputBreakdownWaterfallOperations:
    """
    Attributes:
        work_email (float):
        personal_email (float):
        phone (float):
    """

    work_email: float
    personal_email: float
    phone: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        work_email = self.work_email

        personal_email = self.personal_email

        phone = self.phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workEmail": work_email,
                "personalEmail": personal_email,
                "phone": phone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        work_email = d.pop("workEmail")

        personal_email = d.pop("personalEmail")

        phone = d.pop("phone")

        estimate_enrichment_cost_response_200_output_breakdown_waterfall_operations = cls(
            work_email=work_email,
            personal_email=personal_email,
            phone=phone,
        )

        estimate_enrichment_cost_response_200_output_breakdown_waterfall_operations.additional_properties = d
        return estimate_enrichment_cost_response_200_output_breakdown_waterfall_operations

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
