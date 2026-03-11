from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0Growth24MType0")


@_attrs_define
class CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0Growth24MType0:
    """
    Attributes:
        percent (float):
        quantity (int):
    """

    percent: float
    quantity: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        percent = self.percent

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "percent": percent,
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        percent = d.pop("percent")

        quantity = d.pop("quantity")

        company_live_enrich_response_200_output_company_historical_headcount_type_0_growth_24m_type_0 = cls(
            percent=percent,
            quantity=quantity,
        )

        company_live_enrich_response_200_output_company_historical_headcount_type_0_growth_24m_type_0.additional_properties = d
        return company_live_enrich_response_200_output_company_historical_headcount_type_0_growth_24m_type_0

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
