from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestmentStatsType0InvestmentsByStageType0Item",
)


@_attrs_define
class GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemInvestmentStatsType0InvestmentsByStageType0Item:
    """
    Attributes:
        stage (None | str | Unset):
        lead_rate (float | None | Unset):
        lead_count (float | None | Unset):
        total_count (float | None | Unset):
        share_of_portfolio (float | None | Unset):
        last_investment_date (None | str | Unset):
    """

    stage: None | str | Unset = UNSET
    lead_rate: float | None | Unset = UNSET
    lead_count: float | None | Unset = UNSET
    total_count: float | None | Unset = UNSET
    share_of_portfolio: float | None | Unset = UNSET
    last_investment_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage: None | str | Unset
        if isinstance(self.stage, Unset):
            stage = UNSET
        else:
            stage = self.stage

        lead_rate: float | None | Unset
        if isinstance(self.lead_rate, Unset):
            lead_rate = UNSET
        else:
            lead_rate = self.lead_rate

        lead_count: float | None | Unset
        if isinstance(self.lead_count, Unset):
            lead_count = UNSET
        else:
            lead_count = self.lead_count

        total_count: float | None | Unset
        if isinstance(self.total_count, Unset):
            total_count = UNSET
        else:
            total_count = self.total_count

        share_of_portfolio: float | None | Unset
        if isinstance(self.share_of_portfolio, Unset):
            share_of_portfolio = UNSET
        else:
            share_of_portfolio = self.share_of_portfolio

        last_investment_date: None | str | Unset
        if isinstance(self.last_investment_date, Unset):
            last_investment_date = UNSET
        else:
            last_investment_date = self.last_investment_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stage is not UNSET:
            field_dict["stage"] = stage
        if lead_rate is not UNSET:
            field_dict["lead_rate"] = lead_rate
        if lead_count is not UNSET:
            field_dict["lead_count"] = lead_count
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if share_of_portfolio is not UNSET:
            field_dict["share_of_portfolio"] = share_of_portfolio
        if last_investment_date is not UNSET:
            field_dict["last_investment_date"] = last_investment_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_stage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stage = _parse_stage(d.pop("stage", UNSET))

        def _parse_lead_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lead_rate = _parse_lead_rate(d.pop("lead_rate", UNSET))

        def _parse_lead_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lead_count = _parse_lead_count(d.pop("lead_count", UNSET))

        def _parse_total_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_count = _parse_total_count(d.pop("total_count", UNSET))

        def _parse_share_of_portfolio(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        share_of_portfolio = _parse_share_of_portfolio(d.pop("share_of_portfolio", UNSET))

        def _parse_last_investment_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_investment_date = _parse_last_investment_date(d.pop("last_investment_date", UNSET))

        get_current_companies_in_saved_search_response_200_output_companies_item_investment_stats_type_0_investments_by_stage_type_0_item = cls(
            stage=stage,
            lead_rate=lead_rate,
            lead_count=lead_count,
            total_count=total_count,
            share_of_portfolio=share_of_portfolio,
            last_investment_date=last_investment_date,
        )

        get_current_companies_in_saved_search_response_200_output_companies_item_investment_stats_type_0_investments_by_stage_type_0_item.additional_properties = d
        return get_current_companies_in_saved_search_response_200_output_companies_item_investment_stats_type_0_investments_by_stage_type_0_item

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
