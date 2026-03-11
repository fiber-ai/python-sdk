from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="KitchenSinkBulkCompanyResponse200OutputDataItemItemFundingRoundStatsType0IndividualInvestorStatsType0Item",
)


@_attrs_define
class KitchenSinkBulkCompanyResponse200OutputDataItemItemFundingRoundStatsType0IndividualInvestorStatsType0Item:
    """
    Attributes:
        investor_name (None | str | Unset):
        investor_type (None | str | Unset):
        investor_domain (None | str | Unset):
        investment_count (float | None | Unset):
        participated_round_types (list[str] | None | Unset):
    """

    investor_name: None | str | Unset = UNSET
    investor_type: None | str | Unset = UNSET
    investor_domain: None | str | Unset = UNSET
    investment_count: float | None | Unset = UNSET
    participated_round_types: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        investor_name: None | str | Unset
        if isinstance(self.investor_name, Unset):
            investor_name = UNSET
        else:
            investor_name = self.investor_name

        investor_type: None | str | Unset
        if isinstance(self.investor_type, Unset):
            investor_type = UNSET
        else:
            investor_type = self.investor_type

        investor_domain: None | str | Unset
        if isinstance(self.investor_domain, Unset):
            investor_domain = UNSET
        else:
            investor_domain = self.investor_domain

        investment_count: float | None | Unset
        if isinstance(self.investment_count, Unset):
            investment_count = UNSET
        else:
            investment_count = self.investment_count

        participated_round_types: list[str] | None | Unset
        if isinstance(self.participated_round_types, Unset):
            participated_round_types = UNSET
        elif isinstance(self.participated_round_types, list):
            participated_round_types = self.participated_round_types

        else:
            participated_round_types = self.participated_round_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if investor_name is not UNSET:
            field_dict["investor_name"] = investor_name
        if investor_type is not UNSET:
            field_dict["investor_type"] = investor_type
        if investor_domain is not UNSET:
            field_dict["investor_domain"] = investor_domain
        if investment_count is not UNSET:
            field_dict["investment_count"] = investment_count
        if participated_round_types is not UNSET:
            field_dict["participated_round_types"] = participated_round_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_investor_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        investor_name = _parse_investor_name(d.pop("investor_name", UNSET))

        def _parse_investor_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        investor_type = _parse_investor_type(d.pop("investor_type", UNSET))

        def _parse_investor_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        investor_domain = _parse_investor_domain(d.pop("investor_domain", UNSET))

        def _parse_investment_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        investment_count = _parse_investment_count(d.pop("investment_count", UNSET))

        def _parse_participated_round_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                participated_round_types_type_0 = cast(list[str], data)

                return participated_round_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        participated_round_types = _parse_participated_round_types(d.pop("participated_round_types", UNSET))

        kitchen_sink_bulk_company_response_200_output_data_item_item_funding_round_stats_type_0_individual_investor_stats_type_0_item = cls(
            investor_name=investor_name,
            investor_type=investor_type,
            investor_domain=investor_domain,
            investment_count=investment_count,
            participated_round_types=participated_round_types,
        )

        kitchen_sink_bulk_company_response_200_output_data_item_item_funding_round_stats_type_0_individual_investor_stats_type_0_item.additional_properties = d
        return kitchen_sink_bulk_company_response_200_output_data_item_item_funding_round_stats_type_0_individual_investor_stats_type_0_item

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
