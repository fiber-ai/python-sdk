from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.investor_search_response_200_output_investors_item_investments_by_stage_type_0_item_stage_type_1 import (
    InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType1,
)
from ..models.investor_search_response_200_output_investors_item_investments_by_stage_type_0_item_stage_type_2_type_1 import (
    InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType2Type1,
)
from ..models.investor_search_response_200_output_investors_item_investments_by_stage_type_0_item_stage_type_3_type_1 import (
    InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0Item")


@_attrs_define
class InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0Item:
    """
    Attributes:
        total_count (int): Total investments at this stage
        lead_count (int): Lead investments at this stage
        lead_rate (float): Lead rate at this stage (0.0 - 1.0)
        share_of_portfolio (float): Share of total investments accounted for by this stage (0.0 - 1.0)
        stage (InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType1 |
            InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType2Type1 |
            InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType3Type1 | None | Unset): Funding
            stage (e.g., seed, series_a)
        last_investment_date (None | str | Unset): Date of most recent investment at this stage
    """

    total_count: int
    lead_count: int
    lead_rate: float
    share_of_portfolio: float
    stage: (
        InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType1
        | InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType2Type1
        | InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType3Type1
        | None
        | Unset
    ) = UNSET
    last_investment_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        lead_count = self.lead_count

        lead_rate = self.lead_rate

        share_of_portfolio = self.share_of_portfolio

        stage: None | str | Unset
        if isinstance(self.stage, Unset):
            stage = UNSET
        elif isinstance(self.stage, InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType1):
            stage = self.stage.value
        elif isinstance(
            self.stage, InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType2Type1
        ):
            stage = self.stage.value
        elif isinstance(
            self.stage, InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType3Type1
        ):
            stage = self.stage.value
        else:
            stage = self.stage

        last_investment_date: None | str | Unset
        if isinstance(self.last_investment_date, Unset):
            last_investment_date = UNSET
        else:
            last_investment_date = self.last_investment_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalCount": total_count,
                "leadCount": lead_count,
                "leadRate": lead_rate,
                "shareOfPortfolio": share_of_portfolio,
            }
        )
        if stage is not UNSET:
            field_dict["stage"] = stage
        if last_investment_date is not UNSET:
            field_dict["lastInvestmentDate"] = last_investment_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_count = d.pop("totalCount")

        lead_count = d.pop("leadCount")

        lead_rate = d.pop("leadRate")

        share_of_portfolio = d.pop("shareOfPortfolio")

        def _parse_stage(
            data: object,
        ) -> (
            InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType1
            | InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType2Type1
            | InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                stage_type_1 = InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType1(data)

                return stage_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                stage_type_2_type_1 = (
                    InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType2Type1(data)
                )

                return stage_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                stage_type_3_type_1 = (
                    InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType3Type1(data)
                )

                return stage_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType1
                | InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType2Type1
                | InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0ItemStageType3Type1
                | None
                | Unset,
                data,
            )

        stage = _parse_stage(d.pop("stage", UNSET))

        def _parse_last_investment_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_investment_date = _parse_last_investment_date(d.pop("lastInvestmentDate", UNSET))

        investor_search_response_200_output_investors_item_investments_by_stage_type_0_item = cls(
            total_count=total_count,
            lead_count=lead_count,
            lead_rate=lead_rate,
            share_of_portfolio=share_of_portfolio,
            stage=stage,
            last_investment_date=last_investment_date,
        )

        investor_search_response_200_output_investors_item_investments_by_stage_type_0_item.additional_properties = d
        return investor_search_response_200_output_investors_item_investments_by_stage_type_0_item

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
