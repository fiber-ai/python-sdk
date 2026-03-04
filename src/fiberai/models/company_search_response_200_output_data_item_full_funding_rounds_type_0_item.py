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
  from ..models.company_search_response_200_output_data_item_full_funding_rounds_type_0_item_investors_type_0_item import CompanySearchResponse200OutputDataItemFullFundingRoundsType0ItemInvestorsType0Item





T = TypeVar("T", bound="CompanySearchResponse200OutputDataItemFullFundingRoundsType0Item")



@_attrs_define
class CompanySearchResponse200OutputDataItemFullFundingRoundsType0Item:
    """ 
        Attributes:
            investors (Union[None, Unset,
                list['CompanySearchResponse200OutputDataItemFullFundingRoundsType0ItemInvestorsType0Item']]):
            round_city (Union[None, Unset, str]):
            round_date (Union[None, Unset, str]):
            round_type (Union[None, Unset, str]):
            round_state (Union[None, Unset, str]):
            investor_count (Union[None, Unset, float]):
            round_raised_usd (Union[None, Unset, float]):
            round_country_code (Union[None, Unset, str]):
            round_valuation_usd (Union[None, Unset, float]):
     """

    investors: Union[None, Unset, list['CompanySearchResponse200OutputDataItemFullFundingRoundsType0ItemInvestorsType0Item']] = UNSET
    round_city: Union[None, Unset, str] = UNSET
    round_date: Union[None, Unset, str] = UNSET
    round_type: Union[None, Unset, str] = UNSET
    round_state: Union[None, Unset, str] = UNSET
    investor_count: Union[None, Unset, float] = UNSET
    round_raised_usd: Union[None, Unset, float] = UNSET
    round_country_code: Union[None, Unset, str] = UNSET
    round_valuation_usd: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.company_search_response_200_output_data_item_full_funding_rounds_type_0_item_investors_type_0_item import CompanySearchResponse200OutputDataItemFullFundingRoundsType0ItemInvestorsType0Item
        investors: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.investors, Unset):
            investors = UNSET
        elif isinstance(self.investors, list):
            investors = []
            for investors_type_0_item_data in self.investors:
                investors_type_0_item = investors_type_0_item_data.to_dict()
                investors.append(investors_type_0_item)


        else:
            investors = self.investors

        round_city: Union[None, Unset, str]
        if isinstance(self.round_city, Unset):
            round_city = UNSET
        else:
            round_city = self.round_city

        round_date: Union[None, Unset, str]
        if isinstance(self.round_date, Unset):
            round_date = UNSET
        else:
            round_date = self.round_date

        round_type: Union[None, Unset, str]
        if isinstance(self.round_type, Unset):
            round_type = UNSET
        else:
            round_type = self.round_type

        round_state: Union[None, Unset, str]
        if isinstance(self.round_state, Unset):
            round_state = UNSET
        else:
            round_state = self.round_state

        investor_count: Union[None, Unset, float]
        if isinstance(self.investor_count, Unset):
            investor_count = UNSET
        else:
            investor_count = self.investor_count

        round_raised_usd: Union[None, Unset, float]
        if isinstance(self.round_raised_usd, Unset):
            round_raised_usd = UNSET
        else:
            round_raised_usd = self.round_raised_usd

        round_country_code: Union[None, Unset, str]
        if isinstance(self.round_country_code, Unset):
            round_country_code = UNSET
        else:
            round_country_code = self.round_country_code

        round_valuation_usd: Union[None, Unset, float]
        if isinstance(self.round_valuation_usd, Unset):
            round_valuation_usd = UNSET
        else:
            round_valuation_usd = self.round_valuation_usd


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if investors is not UNSET:
            field_dict["investors"] = investors
        if round_city is not UNSET:
            field_dict["round_city"] = round_city
        if round_date is not UNSET:
            field_dict["round_date"] = round_date
        if round_type is not UNSET:
            field_dict["round_type"] = round_type
        if round_state is not UNSET:
            field_dict["round_state"] = round_state
        if investor_count is not UNSET:
            field_dict["investor_count"] = investor_count
        if round_raised_usd is not UNSET:
            field_dict["round_raised_usd"] = round_raised_usd
        if round_country_code is not UNSET:
            field_dict["round_country_code"] = round_country_code
        if round_valuation_usd is not UNSET:
            field_dict["round_valuation_usd"] = round_valuation_usd

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_search_response_200_output_data_item_full_funding_rounds_type_0_item_investors_type_0_item import CompanySearchResponse200OutputDataItemFullFundingRoundsType0ItemInvestorsType0Item
        d = dict(src_dict)
        def _parse_investors(data: object) -> Union[None, Unset, list['CompanySearchResponse200OutputDataItemFullFundingRoundsType0ItemInvestorsType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                investors_type_0 = []
                _investors_type_0 = data
                for investors_type_0_item_data in (_investors_type_0):
                    investors_type_0_item = CompanySearchResponse200OutputDataItemFullFundingRoundsType0ItemInvestorsType0Item.from_dict(investors_type_0_item_data)



                    investors_type_0.append(investors_type_0_item)

                return investors_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['CompanySearchResponse200OutputDataItemFullFundingRoundsType0ItemInvestorsType0Item']], data)

        investors = _parse_investors(d.pop("investors", UNSET))


        def _parse_round_city(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        round_city = _parse_round_city(d.pop("round_city", UNSET))


        def _parse_round_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        round_date = _parse_round_date(d.pop("round_date", UNSET))


        def _parse_round_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        round_type = _parse_round_type(d.pop("round_type", UNSET))


        def _parse_round_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        round_state = _parse_round_state(d.pop("round_state", UNSET))


        def _parse_investor_count(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        investor_count = _parse_investor_count(d.pop("investor_count", UNSET))


        def _parse_round_raised_usd(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        round_raised_usd = _parse_round_raised_usd(d.pop("round_raised_usd", UNSET))


        def _parse_round_country_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        round_country_code = _parse_round_country_code(d.pop("round_country_code", UNSET))


        def _parse_round_valuation_usd(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        round_valuation_usd = _parse_round_valuation_usd(d.pop("round_valuation_usd", UNSET))


        company_search_response_200_output_data_item_full_funding_rounds_type_0_item = cls(
            investors=investors,
            round_city=round_city,
            round_date=round_date,
            round_type=round_type,
            round_state=round_state,
            investor_count=investor_count,
            round_raised_usd=round_raised_usd,
            round_country_code=round_country_code,
            round_valuation_usd=round_valuation_usd,
        )


        company_search_response_200_output_data_item_full_funding_rounds_type_0_item.additional_properties = d
        return company_search_response_200_output_data_item_full_funding_rounds_type_0_item

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
