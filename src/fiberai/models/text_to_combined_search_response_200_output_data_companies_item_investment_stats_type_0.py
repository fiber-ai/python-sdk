from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.text_to_combined_search_response_200_output_data_companies_item_investment_stats_type_0_investments_by_stage_type_0_item import TextToCombinedSearchResponse200OutputDataCompaniesItemInvestmentStatsType0InvestmentsByStageType0Item





T = TypeVar("T", bound="TextToCombinedSearchResponse200OutputDataCompaniesItemInvestmentStatsType0")



@_attrs_define
class TextToCombinedSearchResponse200OutputDataCompaniesItemInvestmentStatsType0:
    """ 
        Attributes:
            investments_by_stage (Union[None, Unset,
                list['TextToCombinedSearchResponse200OutputDataCompaniesItemInvestmentStatsType0InvestmentsByStageType0Item']]):
            lead_investment_rate (Union[None, Unset, float]):
            lead_investment_count (Union[None, Unset, float]):
            total_investment_count (Union[None, Unset, float]):
            last_investment_date (Union[None, Unset, str]):
     """

    investments_by_stage: Union[None, Unset, list['TextToCombinedSearchResponse200OutputDataCompaniesItemInvestmentStatsType0InvestmentsByStageType0Item']] = UNSET
    lead_investment_rate: Union[None, Unset, float] = UNSET
    lead_investment_count: Union[None, Unset, float] = UNSET
    total_investment_count: Union[None, Unset, float] = UNSET
    last_investment_date: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_response_200_output_data_companies_item_investment_stats_type_0_investments_by_stage_type_0_item import TextToCombinedSearchResponse200OutputDataCompaniesItemInvestmentStatsType0InvestmentsByStageType0Item
        investments_by_stage: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.investments_by_stage, Unset):
            investments_by_stage = UNSET
        elif isinstance(self.investments_by_stage, list):
            investments_by_stage = []
            for investments_by_stage_type_0_item_data in self.investments_by_stage:
                investments_by_stage_type_0_item = investments_by_stage_type_0_item_data.to_dict()
                investments_by_stage.append(investments_by_stage_type_0_item)


        else:
            investments_by_stage = self.investments_by_stage

        lead_investment_rate: Union[None, Unset, float]
        if isinstance(self.lead_investment_rate, Unset):
            lead_investment_rate = UNSET
        else:
            lead_investment_rate = self.lead_investment_rate

        lead_investment_count: Union[None, Unset, float]
        if isinstance(self.lead_investment_count, Unset):
            lead_investment_count = UNSET
        else:
            lead_investment_count = self.lead_investment_count

        total_investment_count: Union[None, Unset, float]
        if isinstance(self.total_investment_count, Unset):
            total_investment_count = UNSET
        else:
            total_investment_count = self.total_investment_count

        last_investment_date: Union[None, Unset, str]
        if isinstance(self.last_investment_date, Unset):
            last_investment_date = UNSET
        else:
            last_investment_date = self.last_investment_date


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
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
        from ..models.text_to_combined_search_response_200_output_data_companies_item_investment_stats_type_0_investments_by_stage_type_0_item import TextToCombinedSearchResponse200OutputDataCompaniesItemInvestmentStatsType0InvestmentsByStageType0Item
        d = dict(src_dict)
        def _parse_investments_by_stage(data: object) -> Union[None, Unset, list['TextToCombinedSearchResponse200OutputDataCompaniesItemInvestmentStatsType0InvestmentsByStageType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                investments_by_stage_type_0 = []
                _investments_by_stage_type_0 = data
                for investments_by_stage_type_0_item_data in (_investments_by_stage_type_0):
                    investments_by_stage_type_0_item = TextToCombinedSearchResponse200OutputDataCompaniesItemInvestmentStatsType0InvestmentsByStageType0Item.from_dict(investments_by_stage_type_0_item_data)



                    investments_by_stage_type_0.append(investments_by_stage_type_0_item)

                return investments_by_stage_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['TextToCombinedSearchResponse200OutputDataCompaniesItemInvestmentStatsType0InvestmentsByStageType0Item']], data)

        investments_by_stage = _parse_investments_by_stage(d.pop("investments_by_stage", UNSET))


        def _parse_lead_investment_rate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lead_investment_rate = _parse_lead_investment_rate(d.pop("lead_investment_rate", UNSET))


        def _parse_lead_investment_count(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lead_investment_count = _parse_lead_investment_count(d.pop("lead_investment_count", UNSET))


        def _parse_total_investment_count(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total_investment_count = _parse_total_investment_count(d.pop("total_investment_count", UNSET))


        def _parse_last_investment_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_investment_date = _parse_last_investment_date(d.pop("last_investment_date", UNSET))


        text_to_combined_search_response_200_output_data_companies_item_investment_stats_type_0 = cls(
            investments_by_stage=investments_by_stage,
            lead_investment_rate=lead_investment_rate,
            lead_investment_count=lead_investment_count,
            total_investment_count=total_investment_count,
            last_investment_date=last_investment_date,
        )


        text_to_combined_search_response_200_output_data_companies_item_investment_stats_type_0.additional_properties = d
        return text_to_combined_search_response_200_output_data_companies_item_investment_stats_type_0

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
