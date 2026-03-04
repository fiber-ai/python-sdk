from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.kitchen_sink_company_response_200_output_data_item_best_funding_round_type_0_round_type_type_1 import KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType1
from ..models.kitchen_sink_company_response_200_output_data_item_best_funding_round_type_0_round_type_type_2_type_1 import KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType2Type1
from ..models.kitchen_sink_company_response_200_output_data_item_best_funding_round_type_0_round_type_type_3_type_1 import KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType3Type1
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0")



@_attrs_define
class KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0:
    """ 
        Attributes:
            round_type (Union[KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType1,
                KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType2Type1,
                KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType3Type1, None, Unset]):
            announced_on_date (Union[None, Unset, str]):
            raised_amount_usd (Union[None, Unset, float]):
            post_money_valuation_usd (Union[None, Unset, float]):
     """

    round_type: Union[KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType1, KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType2Type1, KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType3Type1, None, Unset] = UNSET
    announced_on_date: Union[None, Unset, str] = UNSET
    raised_amount_usd: Union[None, Unset, float] = UNSET
    post_money_valuation_usd: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        round_type: Union[None, Unset, str]
        if isinstance(self.round_type, Unset):
            round_type = UNSET
        elif isinstance(self.round_type, KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType1):
            round_type = self.round_type.value
        elif isinstance(self.round_type, KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType2Type1):
            round_type = self.round_type.value
        elif isinstance(self.round_type, KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType3Type1):
            round_type = self.round_type.value
        else:
            round_type = self.round_type

        announced_on_date: Union[None, Unset, str]
        if isinstance(self.announced_on_date, Unset):
            announced_on_date = UNSET
        else:
            announced_on_date = self.announced_on_date

        raised_amount_usd: Union[None, Unset, float]
        if isinstance(self.raised_amount_usd, Unset):
            raised_amount_usd = UNSET
        else:
            raised_amount_usd = self.raised_amount_usd

        post_money_valuation_usd: Union[None, Unset, float]
        if isinstance(self.post_money_valuation_usd, Unset):
            post_money_valuation_usd = UNSET
        else:
            post_money_valuation_usd = self.post_money_valuation_usd


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if round_type is not UNSET:
            field_dict["round_type"] = round_type
        if announced_on_date is not UNSET:
            field_dict["announced_on_date"] = announced_on_date
        if raised_amount_usd is not UNSET:
            field_dict["raised_amount_usd"] = raised_amount_usd
        if post_money_valuation_usd is not UNSET:
            field_dict["post_money_valuation_usd"] = post_money_valuation_usd

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_round_type(data: object) -> Union[KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType1, KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType2Type1, KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType3Type1, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                round_type_type_1 = KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType1(data)



                return round_type_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                round_type_type_2_type_1 = KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType2Type1(data)



                return round_type_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                round_type_type_3_type_1 = KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType3Type1(data)



                return round_type_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType1, KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType2Type1, KitchenSinkCompanyResponse200OutputDataItemBestFundingRoundType0RoundTypeType3Type1, None, Unset], data)

        round_type = _parse_round_type(d.pop("round_type", UNSET))


        def _parse_announced_on_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        announced_on_date = _parse_announced_on_date(d.pop("announced_on_date", UNSET))


        def _parse_raised_amount_usd(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        raised_amount_usd = _parse_raised_amount_usd(d.pop("raised_amount_usd", UNSET))


        def _parse_post_money_valuation_usd(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        post_money_valuation_usd = _parse_post_money_valuation_usd(d.pop("post_money_valuation_usd", UNSET))


        kitchen_sink_company_response_200_output_data_item_best_funding_round_type_0 = cls(
            round_type=round_type,
            announced_on_date=announced_on_date,
            raised_amount_usd=raised_amount_usd,
            post_money_valuation_usd=post_money_valuation_usd,
        )


        kitchen_sink_company_response_200_output_data_item_best_funding_round_type_0.additional_properties = d
        return kitchen_sink_company_response_200_output_data_item_best_funding_round_type_0

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
