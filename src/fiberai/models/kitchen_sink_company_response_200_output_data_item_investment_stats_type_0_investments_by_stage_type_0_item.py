from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="KitchenSinkCompanyResponse200OutputDataItemInvestmentStatsType0InvestmentsByStageType0Item")



@_attrs_define
class KitchenSinkCompanyResponse200OutputDataItemInvestmentStatsType0InvestmentsByStageType0Item:
    """ 
        Attributes:
            stage (Union[None, Unset, str]):
            lead_rate (Union[None, Unset, float]):
            lead_count (Union[None, Unset, float]):
            total_count (Union[None, Unset, float]):
            share_of_portfolio (Union[None, Unset, float]):
            last_investment_date (Union[None, Unset, str]):
     """

    stage: Union[None, Unset, str] = UNSET
    lead_rate: Union[None, Unset, float] = UNSET
    lead_count: Union[None, Unset, float] = UNSET
    total_count: Union[None, Unset, float] = UNSET
    share_of_portfolio: Union[None, Unset, float] = UNSET
    last_investment_date: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        stage: Union[None, Unset, str]
        if isinstance(self.stage, Unset):
            stage = UNSET
        else:
            stage = self.stage

        lead_rate: Union[None, Unset, float]
        if isinstance(self.lead_rate, Unset):
            lead_rate = UNSET
        else:
            lead_rate = self.lead_rate

        lead_count: Union[None, Unset, float]
        if isinstance(self.lead_count, Unset):
            lead_count = UNSET
        else:
            lead_count = self.lead_count

        total_count: Union[None, Unset, float]
        if isinstance(self.total_count, Unset):
            total_count = UNSET
        else:
            total_count = self.total_count

        share_of_portfolio: Union[None, Unset, float]
        if isinstance(self.share_of_portfolio, Unset):
            share_of_portfolio = UNSET
        else:
            share_of_portfolio = self.share_of_portfolio

        last_investment_date: Union[None, Unset, str]
        if isinstance(self.last_investment_date, Unset):
            last_investment_date = UNSET
        else:
            last_investment_date = self.last_investment_date


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
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
        def _parse_stage(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        stage = _parse_stage(d.pop("stage", UNSET))


        def _parse_lead_rate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lead_rate = _parse_lead_rate(d.pop("lead_rate", UNSET))


        def _parse_lead_count(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lead_count = _parse_lead_count(d.pop("lead_count", UNSET))


        def _parse_total_count(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total_count = _parse_total_count(d.pop("total_count", UNSET))


        def _parse_share_of_portfolio(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        share_of_portfolio = _parse_share_of_portfolio(d.pop("share_of_portfolio", UNSET))


        def _parse_last_investment_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_investment_date = _parse_last_investment_date(d.pop("last_investment_date", UNSET))


        kitchen_sink_company_response_200_output_data_item_investment_stats_type_0_investments_by_stage_type_0_item = cls(
            stage=stage,
            lead_rate=lead_rate,
            lead_count=lead_count,
            total_count=total_count,
            share_of_portfolio=share_of_portfolio,
            last_investment_date=last_investment_date,
        )


        kitchen_sink_company_response_200_output_data_item_investment_stats_type_0_investments_by_stage_type_0_item.additional_properties = d
        return kitchen_sink_company_response_200_output_data_item_investment_stats_type_0_investments_by_stage_type_0_item

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
