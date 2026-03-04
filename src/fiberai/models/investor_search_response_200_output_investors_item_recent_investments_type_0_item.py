from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.investor_search_response_200_output_investors_item_recent_investments_type_0_item_round_type_type_1 import InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType1
from ..models.investor_search_response_200_output_investors_item_recent_investments_type_0_item_round_type_type_2_type_1 import InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType2Type1
from ..models.investor_search_response_200_output_investors_item_recent_investments_type_0_item_round_type_type_3_type_1 import InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType3Type1
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0Item")



@_attrs_define
class InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0Item:
    """ 
        Attributes:
            was_lead_investor (bool): Whether the investor was lead investor
            org_linkedin_slug (Union[None, Unset, str]): LinkedIn slug for the organization invested in (in long format,
                e.g., 'company/companyname')
            org_name (Union[None, Unset, str]): Name of the organization invested in
            org_domain (Union[None, Unset, str]): Domain of the organization
            round_type (Union[InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType1,
                InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType2Type1,
                InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType3Type1, None, Unset]): Type
                of funding round (e.g., series_a, seed)
            round_date (Union[None, Unset, str]): Date of the funding round
            round_raised_usd (Union[None, Unset, int]): Amount raised in USD
     """

    was_lead_investor: bool
    org_linkedin_slug: Union[None, Unset, str] = UNSET
    org_name: Union[None, Unset, str] = UNSET
    org_domain: Union[None, Unset, str] = UNSET
    round_type: Union[InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType1, InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType2Type1, InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType3Type1, None, Unset] = UNSET
    round_date: Union[None, Unset, str] = UNSET
    round_raised_usd: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        was_lead_investor = self.was_lead_investor

        org_linkedin_slug: Union[None, Unset, str]
        if isinstance(self.org_linkedin_slug, Unset):
            org_linkedin_slug = UNSET
        else:
            org_linkedin_slug = self.org_linkedin_slug

        org_name: Union[None, Unset, str]
        if isinstance(self.org_name, Unset):
            org_name = UNSET
        else:
            org_name = self.org_name

        org_domain: Union[None, Unset, str]
        if isinstance(self.org_domain, Unset):
            org_domain = UNSET
        else:
            org_domain = self.org_domain

        round_type: Union[None, Unset, str]
        if isinstance(self.round_type, Unset):
            round_type = UNSET
        elif isinstance(self.round_type, InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType1):
            round_type = self.round_type.value
        elif isinstance(self.round_type, InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType2Type1):
            round_type = self.round_type.value
        elif isinstance(self.round_type, InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType3Type1):
            round_type = self.round_type.value
        else:
            round_type = self.round_type

        round_date: Union[None, Unset, str]
        if isinstance(self.round_date, Unset):
            round_date = UNSET
        else:
            round_date = self.round_date

        round_raised_usd: Union[None, Unset, int]
        if isinstance(self.round_raised_usd, Unset):
            round_raised_usd = UNSET
        else:
            round_raised_usd = self.round_raised_usd


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "wasLeadInvestor": was_lead_investor,
        })
        if org_linkedin_slug is not UNSET:
            field_dict["orgLinkedinSlug"] = org_linkedin_slug
        if org_name is not UNSET:
            field_dict["orgName"] = org_name
        if org_domain is not UNSET:
            field_dict["orgDomain"] = org_domain
        if round_type is not UNSET:
            field_dict["roundType"] = round_type
        if round_date is not UNSET:
            field_dict["roundDate"] = round_date
        if round_raised_usd is not UNSET:
            field_dict["roundRaisedUSD"] = round_raised_usd

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        was_lead_investor = d.pop("wasLeadInvestor")

        def _parse_org_linkedin_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        org_linkedin_slug = _parse_org_linkedin_slug(d.pop("orgLinkedinSlug", UNSET))


        def _parse_org_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        org_name = _parse_org_name(d.pop("orgName", UNSET))


        def _parse_org_domain(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        org_domain = _parse_org_domain(d.pop("orgDomain", UNSET))


        def _parse_round_type(data: object) -> Union[InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType1, InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType2Type1, InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType3Type1, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                round_type_type_1 = InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType1(data)



                return round_type_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                round_type_type_2_type_1 = InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType2Type1(data)



                return round_type_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                round_type_type_3_type_1 = InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType3Type1(data)



                return round_type_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType1, InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType2Type1, InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0ItemRoundTypeType3Type1, None, Unset], data)

        round_type = _parse_round_type(d.pop("roundType", UNSET))


        def _parse_round_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        round_date = _parse_round_date(d.pop("roundDate", UNSET))


        def _parse_round_raised_usd(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        round_raised_usd = _parse_round_raised_usd(d.pop("roundRaisedUSD", UNSET))


        investor_search_response_200_output_investors_item_recent_investments_type_0_item = cls(
            was_lead_investor=was_lead_investor,
            org_linkedin_slug=org_linkedin_slug,
            org_name=org_name,
            org_domain=org_domain,
            round_type=round_type,
            round_date=round_date,
            round_raised_usd=round_raised_usd,
        )


        investor_search_response_200_output_investors_item_recent_investments_type_0_item.additional_properties = d
        return investor_search_response_200_output_investors_item_recent_investments_type_0_item

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
