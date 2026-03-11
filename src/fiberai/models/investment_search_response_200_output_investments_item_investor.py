from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.investment_search_response_200_output_investments_item_investor_type_type_1 import (
    InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType1,
)
from ..models.investment_search_response_200_output_investments_item_investor_type_type_2_type_1 import (
    InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType2Type1,
)
from ..models.investment_search_response_200_output_investments_item_investor_type_type_3_type_1 import (
    InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvestmentSearchResponse200OutputInvestmentsItemInvestor")


@_attrs_define
class InvestmentSearchResponse200OutputInvestmentsItemInvestor:
    """Investor information

    Attributes:
        is_lead_investor (bool): Whether the investor was a lead investor
        name (None | str | Unset): Investor name
        type_ (InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType1 |
            InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType2Type1 |
            InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType3Type1 | None | Unset): Investor type: 'person'
            or 'organization'
        linkedin_url (None | str | Unset): Full LinkedIn URL for the investor. Examples:
            'https://www.linkedin.com/in/johndoe/' for person or 'https://www.linkedin.com/company/sequoia-capital/' for
            organization. You can also use organization ID (e.g., 'https://www.linkedin.com/company/123456789/')
    """

    is_lead_investor: bool
    name: None | str | Unset = UNSET
    type_: (
        InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType1
        | InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType2Type1
        | InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType3Type1
        | None
        | Unset
    ) = UNSET
    linkedin_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_lead_investor = self.is_lead_investor

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType1):
            type_ = self.type_.value
        elif isinstance(self.type_, InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType2Type1):
            type_ = self.type_.value
        elif isinstance(self.type_, InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType3Type1):
            type_ = self.type_.value
        else:
            type_ = self.type_

        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isLeadInvestor": is_lead_investor,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_lead_investor = d.pop("isLeadInvestor")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_type_(
            data: object,
        ) -> (
            InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType1
            | InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType2Type1
            | InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType3Type1
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
                type_type_1 = InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType1(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2_type_1 = InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType2Type1(data)

                return type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_3_type_1 = InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType3Type1(data)

                return type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType1
                | InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType2Type1
                | InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType3Type1
                | None
                | Unset,
                data,
            )

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))

        investment_search_response_200_output_investments_item_investor = cls(
            is_lead_investor=is_lead_investor,
            name=name,
            type_=type_,
            linkedin_url=linkedin_url,
        )

        investment_search_response_200_output_investments_item_investor.additional_properties = d
        return investment_search_response_200_output_investments_item_investor

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
