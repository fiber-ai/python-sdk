from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EstimateEnrichmentCostResponse200OutputBreakdownSalesNav")


@_attrs_define
class EstimateEnrichmentCostResponse200OutputBreakdownSalesNav:
    """Sales Navigator enrichment cost

    Attributes:
        credits_ (float):
        is_free (bool):
    """

    credits_: float
    is_free: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credits_ = self.credits_

        is_free = self.is_free

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credits": credits_,
                "isFree": is_free,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credits_ = d.pop("credits")

        is_free = d.pop("isFree")

        estimate_enrichment_cost_response_200_output_breakdown_sales_nav = cls(
            credits_=credits_,
            is_free=is_free,
        )

        estimate_enrichment_cost_response_200_output_breakdown_sales_nav.additional_properties = d
        return estimate_enrichment_cost_response_200_output_breakdown_sales_nav

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
