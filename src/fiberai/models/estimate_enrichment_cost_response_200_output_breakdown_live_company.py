from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EstimateEnrichmentCostResponse200OutputBreakdownLiveCompany")


@_attrs_define
class EstimateEnrichmentCostResponse200OutputBreakdownLiveCompany:
    """Company live enrichment cost

    Attributes:
        credits_ (float):
        discounted (bool):
    """

    credits_: float
    discounted: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credits_ = self.credits_

        discounted = self.discounted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credits": credits_,
                "discounted": discounted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credits_ = d.pop("credits")

        discounted = d.pop("discounted")

        estimate_enrichment_cost_response_200_output_breakdown_live_company = cls(
            credits_=credits_,
            discounted=discounted,
        )

        estimate_enrichment_cost_response_200_output_breakdown_live_company.additional_properties = d
        return estimate_enrichment_cost_response_200_output_breakdown_live_company

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
