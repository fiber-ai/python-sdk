from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.investment_search_response_200_output_investments_item_company_country_code_type_1 import (
    InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType1,
)
from ..models.investment_search_response_200_output_investments_item_company_country_code_type_2_type_1 import (
    InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType2Type1,
)
from ..models.investment_search_response_200_output_investments_item_company_country_code_type_3_type_1 import (
    InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvestmentSearchResponse200OutputInvestmentsItemCompany")


@_attrs_define
class InvestmentSearchResponse200OutputInvestmentsItemCompany:
    """Company information

    Attributes:
        name (None | str | Unset): Company name
        domain (None | str | Unset): Company domain
        linkedin_url (None | str | Unset): Full LinkedIn URL for the company. Examples:
            'https://www.linkedin.com/company/fiber-ai/' or 'https://www.linkedin.com/company/123456789/' (using
            organization ID)
        linkedin_id (None | str | Unset): LinkedIn organization ID
        country_code (InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType1 |
            InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType2Type1 |
            InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType3Type1 | None | Unset): Company country
            code
        state (None | str | Unset): Company state
        city (None | str | Unset): Company city
    """

    name: None | str | Unset = UNSET
    domain: None | str | Unset = UNSET
    linkedin_url: None | str | Unset = UNSET
    linkedin_id: None | str | Unset = UNSET
    country_code: (
        InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType1
        | InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType2Type1
        | InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType3Type1
        | None
        | Unset
    ) = UNSET
    state: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        linkedin_id: None | str | Unset
        if isinstance(self.linkedin_id, Unset):
            linkedin_id = UNSET
        else:
            linkedin_id = self.linkedin_id

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        elif isinstance(self.country_code, InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType1):
            country_code = self.country_code.value
        elif isinstance(
            self.country_code, InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType2Type1
        ):
            country_code = self.country_code.value
        elif isinstance(
            self.country_code, InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType3Type1
        ):
            country_code = self.country_code.value
        else:
            country_code = self.country_code

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if domain is not UNSET:
            field_dict["domain"] = domain
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url
        if linkedin_id is not UNSET:
            field_dict["linkedinId"] = linkedin_id
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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))

        def _parse_linkedin_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_id = _parse_linkedin_id(d.pop("linkedinId", UNSET))

        def _parse_country_code(
            data: object,
        ) -> (
            InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType1
            | InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType2Type1
            | InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType3Type1
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
                country_code_type_1 = InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType1(data)

                return country_code_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_code_type_2_type_1 = (
                    InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType2Type1(data)
                )

                return country_code_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_code_type_3_type_1 = (
                    InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType3Type1(data)
                )

                return country_code_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType1
                | InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType2Type1
                | InvestmentSearchResponse200OutputInvestmentsItemCompanyCountryCodeType3Type1
                | None
                | Unset,
                data,
            )

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        investment_search_response_200_output_investments_item_company = cls(
            name=name,
            domain=domain,
            linkedin_url=linkedin_url,
            linkedin_id=linkedin_id,
            country_code=country_code,
            state=state,
            city=city,
        )

        investment_search_response_200_output_investments_item_company.additional_properties = d
        return investment_search_response_200_output_investments_item_company

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
