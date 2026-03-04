from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.investment_search_response_200_output_investments_item_round_location_country_code_type_1 import InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType1
from ..models.investment_search_response_200_output_investments_item_round_location_country_code_type_2_type_1 import InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType2Type1
from ..models.investment_search_response_200_output_investments_item_round_location_country_code_type_3_type_1 import InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType3Type1
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="InvestmentSearchResponse200OutputInvestmentsItemRoundLocation")



@_attrs_define
class InvestmentSearchResponse200OutputInvestmentsItemRoundLocation:
    """ Location where the funding round occurred

        Attributes:
            country_code (Union[InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType1,
                InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType2Type1,
                InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType3Type1, None, Unset]): Country code
                where the funding round occurred
            state (Union[None, Unset, str]): State where the funding round occurred
            city (Union[None, Unset, str]): City where the funding round occurred
     """

    country_code: Union[InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType1, InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType2Type1, InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType3Type1, None, Unset] = UNSET
    state: Union[None, Unset, str] = UNSET
    city: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        country_code: Union[None, Unset, str]
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        elif isinstance(self.country_code, InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType1):
            country_code = self.country_code.value
        elif isinstance(self.country_code, InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType2Type1):
            country_code = self.country_code.value
        elif isinstance(self.country_code, InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType3Type1):
            country_code = self.country_code.value
        else:
            country_code = self.country_code

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        city: Union[None, Unset, str]
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if state is not UNSET:
            field_dict["state"] = state
        if city is not UNSET:
            field_dict["city"] = city

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_country_code(data: object) -> Union[InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType1, InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType2Type1, InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType3Type1, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_code_type_1 = InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType1(data)



                return country_code_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_code_type_2_type_1 = InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType2Type1(data)



                return country_code_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_code_type_3_type_1 = InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType3Type1(data)



                return country_code_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType1, InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType2Type1, InvestmentSearchResponse200OutputInvestmentsItemRoundLocationCountryCodeType3Type1, None, Unset], data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))


        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))


        def _parse_city(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        city = _parse_city(d.pop("city", UNSET))


        investment_search_response_200_output_investments_item_round_location = cls(
            country_code=country_code,
            state=state,
            city=city,
        )


        investment_search_response_200_output_investments_item_round_location.additional_properties = d
        return investment_search_response_200_output_investments_item_round_location

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
