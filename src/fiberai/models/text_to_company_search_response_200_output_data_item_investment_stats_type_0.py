from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_company_search_response_200_output_data_item_investment_stats_type_0_investments_by_stage_type_0_item import (
        TextToCompanySearchResponse200OutputDataItemInvestmentStatsType0InvestmentsByStageType0Item,
    )


T = TypeVar("T", bound="TextToCompanySearchResponse200OutputDataItemInvestmentStatsType0")


@_attrs_define
class TextToCompanySearchResponse200OutputDataItemInvestmentStatsType0:
    """
    Attributes:
        investments_by_stage
            (list[TextToCompanySearchResponse200OutputDataItemInvestmentStatsType0InvestmentsByStageType0Item] | None |
            Unset):
        lead_investment_rate (float | None | Unset):
        lead_investment_count (float | None | Unset):
        total_investment_count (float | None | Unset):
        last_investment_date (None | str | Unset):
    """

    investments_by_stage: (
        list[TextToCompanySearchResponse200OutputDataItemInvestmentStatsType0InvestmentsByStageType0Item] | None | Unset
    ) = UNSET
    lead_investment_rate: float | None | Unset = UNSET
    lead_investment_count: float | None | Unset = UNSET
    total_investment_count: float | None | Unset = UNSET
    last_investment_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        investments_by_stage: list[dict[str, Any]] | None | Unset
        if isinstance(self.investments_by_stage, Unset):
            investments_by_stage = UNSET
        elif isinstance(self.investments_by_stage, list):
            investments_by_stage = []
            for investments_by_stage_type_0_item_data in self.investments_by_stage:
                investments_by_stage_type_0_item = investments_by_stage_type_0_item_data.to_dict()
                investments_by_stage.append(investments_by_stage_type_0_item)

        else:
            investments_by_stage = self.investments_by_stage

        lead_investment_rate: float | None | Unset
        if isinstance(self.lead_investment_rate, Unset):
            lead_investment_rate = UNSET
        else:
            lead_investment_rate = self.lead_investment_rate

        lead_investment_count: float | None | Unset
        if isinstance(self.lead_investment_count, Unset):
            lead_investment_count = UNSET
        else:
            lead_investment_count = self.lead_investment_count

        total_investment_count: float | None | Unset
        if isinstance(self.total_investment_count, Unset):
            total_investment_count = UNSET
        else:
            total_investment_count = self.total_investment_count

        last_investment_date: None | str | Unset
        if isinstance(self.last_investment_date, Unset):
            last_investment_date = UNSET
        else:
            last_investment_date = self.last_investment_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if investments_by_stage is not UNSET:
            field_dict["investments_by_stage"] = investments_by_stage
        if lead_investment_rate is not UNSET:
            field_dict["lead_investment_rate"] = lead_investment_rate
        if lead_investment_count is not UNSET:
            field_dict["lead_investment_count"] = lead_investment_count
        if total_investment_count is not UNSET:
            field_dict["total_investment_count"] = total_investment_count
        if last_investment_date is not UNSET:
            field_dict["last_investment_date"] = last_investment_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_company_search_response_200_output_data_item_investment_stats_type_0_investments_by_stage_type_0_item import (
            TextToCompanySearchResponse200OutputDataItemInvestmentStatsType0InvestmentsByStageType0Item,
        )

        d = dict(src_dict)

        def _parse_investments_by_stage(
            data: object,
        ) -> (
            list[TextToCompanySearchResponse200OutputDataItemInvestmentStatsType0InvestmentsByStageType0Item]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                investments_by_stage_type_0 = []
                _investments_by_stage_type_0 = data
                for investments_by_stage_type_0_item_data in _investments_by_stage_type_0:
                    investments_by_stage_type_0_item = TextToCompanySearchResponse200OutputDataItemInvestmentStatsType0InvestmentsByStageType0Item.from_dict(
                        investments_by_stage_type_0_item_data
                    )

                    investments_by_stage_type_0.append(investments_by_stage_type_0_item)

                return investments_by_stage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[TextToCompanySearchResponse200OutputDataItemInvestmentStatsType0InvestmentsByStageType0Item]
                | None
                | Unset,
                data,
            )

        investments_by_stage = _parse_investments_by_stage(d.pop("investments_by_stage", UNSET))

        def _parse_lead_investment_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lead_investment_rate = _parse_lead_investment_rate(d.pop("lead_investment_rate", UNSET))

        def _parse_lead_investment_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lead_investment_count = _parse_lead_investment_count(d.pop("lead_investment_count", UNSET))

        def _parse_total_investment_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_investment_count = _parse_total_investment_count(d.pop("total_investment_count", UNSET))

        def _parse_last_investment_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_investment_date = _parse_last_investment_date(d.pop("last_investment_date", UNSET))

        text_to_company_search_response_200_output_data_item_investment_stats_type_0 = cls(
            investments_by_stage=investments_by_stage,
            lead_investment_rate=lead_investment_rate,
            lead_investment_count=lead_investment_count,
            total_investment_count=total_investment_count,
            last_investment_date=last_investment_date,
        )

        text_to_company_search_response_200_output_data_item_investment_stats_type_0.additional_properties = d
        return text_to_company_search_response_200_output_data_item_investment_stats_type_0

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
