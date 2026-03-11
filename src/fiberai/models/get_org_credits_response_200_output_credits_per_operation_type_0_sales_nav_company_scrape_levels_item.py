from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOrgCreditsResponse200OutputCreditsPerOperationType0SalesNavCompanyScrapeLevelsItem")


@_attrs_define
class GetOrgCreditsResponse200OutputCreditsPerOperationType0SalesNavCompanyScrapeLevelsItem:
    """
    Attributes:
        centi_credit_cost (float):
        limit (float | None | Unset):
    """

    centi_credit_cost: float
    limit: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        centi_credit_cost = self.centi_credit_cost

        limit: float | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "centiCreditCost": centi_credit_cost,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        centi_credit_cost = d.pop("centiCreditCost")

        def _parse_limit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        get_org_credits_response_200_output_credits_per_operation_type_0_sales_nav_company_scrape_levels_item = cls(
            centi_credit_cost=centi_credit_cost,
            limit=limit,
        )

        get_org_credits_response_200_output_credits_per_operation_type_0_sales_nav_company_scrape_levels_item.additional_properties = d
        return get_org_credits_response_200_output_credits_per_operation_type_0_sales_nav_company_scrape_levels_item

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
