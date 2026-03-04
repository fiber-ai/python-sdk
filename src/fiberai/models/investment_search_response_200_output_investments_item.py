from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.investment_search_response_200_output_investments_item_round_type_type_1 import InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType1
from ..models.investment_search_response_200_output_investments_item_round_type_type_2_type_1 import InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType2Type1
from ..models.investment_search_response_200_output_investments_item_round_type_type_3_type_1 import InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType3Type1
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.investment_search_response_200_output_investments_item_round_location import InvestmentSearchResponse200OutputInvestmentsItemRoundLocation
  from ..models.investment_search_response_200_output_investments_item_investor import InvestmentSearchResponse200OutputInvestmentsItemInvestor
  from ..models.investment_search_response_200_output_investments_item_company import InvestmentSearchResponse200OutputInvestmentsItemCompany





T = TypeVar("T", bound="InvestmentSearchResponse200OutputInvestmentsItem")



@_attrs_define
class InvestmentSearchResponse200OutputInvestmentsItem:
    """ 
        Attributes:
            company (InvestmentSearchResponse200OutputInvestmentsItemCompany): Company information
            investor (InvestmentSearchResponse200OutputInvestmentsItemInvestor): Investor information
            round_location (InvestmentSearchResponse200OutputInvestmentsItemRoundLocation): Location where the funding round
                occurred
            round_type (Union[InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType1,
                InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType2Type1,
                InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType3Type1, None, Unset]): Type of funding round (e.g.,
                series_a, seed)
            round_date (Union[None, Unset, str]): Date of the funding round
            raised_amount_usd (Union[None, Unset, int]): Amount raised in USD
            post_money_valuation_usd (Union[None, Unset, int]): Post-money valuation in USD
            investor_count (Union[None, Unset, int]): Total number of investors in this funding round
     """

    company: 'InvestmentSearchResponse200OutputInvestmentsItemCompany'
    investor: 'InvestmentSearchResponse200OutputInvestmentsItemInvestor'
    round_location: 'InvestmentSearchResponse200OutputInvestmentsItemRoundLocation'
    round_type: Union[InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType1, InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType2Type1, InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType3Type1, None, Unset] = UNSET
    round_date: Union[None, Unset, str] = UNSET
    raised_amount_usd: Union[None, Unset, int] = UNSET
    post_money_valuation_usd: Union[None, Unset, int] = UNSET
    investor_count: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.investment_search_response_200_output_investments_item_round_location import InvestmentSearchResponse200OutputInvestmentsItemRoundLocation
        from ..models.investment_search_response_200_output_investments_item_investor import InvestmentSearchResponse200OutputInvestmentsItemInvestor
        from ..models.investment_search_response_200_output_investments_item_company import InvestmentSearchResponse200OutputInvestmentsItemCompany
        company = self.company.to_dict()

        investor = self.investor.to_dict()

        round_location = self.round_location.to_dict()

        round_type: Union[None, Unset, str]
        if isinstance(self.round_type, Unset):
            round_type = UNSET
        elif isinstance(self.round_type, InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType1):
            round_type = self.round_type.value
        elif isinstance(self.round_type, InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType2Type1):
            round_type = self.round_type.value
        elif isinstance(self.round_type, InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType3Type1):
            round_type = self.round_type.value
        else:
            round_type = self.round_type

        round_date: Union[None, Unset, str]
        if isinstance(self.round_date, Unset):
            round_date = UNSET
        else:
            round_date = self.round_date

        raised_amount_usd: Union[None, Unset, int]
        if isinstance(self.raised_amount_usd, Unset):
            raised_amount_usd = UNSET
        else:
            raised_amount_usd = self.raised_amount_usd

        post_money_valuation_usd: Union[None, Unset, int]
        if isinstance(self.post_money_valuation_usd, Unset):
            post_money_valuation_usd = UNSET
        else:
            post_money_valuation_usd = self.post_money_valuation_usd

        investor_count: Union[None, Unset, int]
        if isinstance(self.investor_count, Unset):
            investor_count = UNSET
        else:
            investor_count = self.investor_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "company": company,
            "investor": investor,
            "roundLocation": round_location,
        })
        if round_type is not UNSET:
            field_dict["roundType"] = round_type
        if round_date is not UNSET:
            field_dict["roundDate"] = round_date
        if raised_amount_usd is not UNSET:
            field_dict["raisedAmountUSD"] = raised_amount_usd
        if post_money_valuation_usd is not UNSET:
            field_dict["postMoneyValuationUSD"] = post_money_valuation_usd
        if investor_count is not UNSET:
            field_dict["investorCount"] = investor_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investment_search_response_200_output_investments_item_round_location import InvestmentSearchResponse200OutputInvestmentsItemRoundLocation
        from ..models.investment_search_response_200_output_investments_item_investor import InvestmentSearchResponse200OutputInvestmentsItemInvestor
        from ..models.investment_search_response_200_output_investments_item_company import InvestmentSearchResponse200OutputInvestmentsItemCompany
        d = dict(src_dict)
        company = InvestmentSearchResponse200OutputInvestmentsItemCompany.from_dict(d.pop("company"))




        investor = InvestmentSearchResponse200OutputInvestmentsItemInvestor.from_dict(d.pop("investor"))




        round_location = InvestmentSearchResponse200OutputInvestmentsItemRoundLocation.from_dict(d.pop("roundLocation"))




        def _parse_round_type(data: object) -> Union[InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType1, InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType2Type1, InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType3Type1, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                round_type_type_1 = InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType1(data)



                return round_type_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                round_type_type_2_type_1 = InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType2Type1(data)



                return round_type_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                round_type_type_3_type_1 = InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType3Type1(data)



                return round_type_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType1, InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType2Type1, InvestmentSearchResponse200OutputInvestmentsItemRoundTypeType3Type1, None, Unset], data)

        round_type = _parse_round_type(d.pop("roundType", UNSET))


        def _parse_round_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        round_date = _parse_round_date(d.pop("roundDate", UNSET))


        def _parse_raised_amount_usd(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        raised_amount_usd = _parse_raised_amount_usd(d.pop("raisedAmountUSD", UNSET))


        def _parse_post_money_valuation_usd(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        post_money_valuation_usd = _parse_post_money_valuation_usd(d.pop("postMoneyValuationUSD", UNSET))


        def _parse_investor_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        investor_count = _parse_investor_count(d.pop("investorCount", UNSET))


        investment_search_response_200_output_investments_item = cls(
            company=company,
            investor=investor,
            round_location=round_location,
            round_type=round_type,
            round_date=round_date,
            raised_amount_usd=raised_amount_usd,
            post_money_valuation_usd=post_money_valuation_usd,
            investor_count=investor_count,
        )


        investment_search_response_200_output_investments_item.additional_properties = d
        return investment_search_response_200_output_investments_item

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
