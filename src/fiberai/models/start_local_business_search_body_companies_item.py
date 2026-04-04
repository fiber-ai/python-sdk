from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartLocalBusinessSearchBodyCompaniesItem")


@_attrs_define
class StartLocalBusinessSearchBodyCompaniesItem:
    """
    Attributes:
        company_name (str): The name of the company to search for.
        company_website (None | str | Unset): The website URL of the company.
        company_city (None | str | Unset): The city where the company is located.
        company_state (None | str | Unset): The state where the company is located.
        company_country_name (None | str | Unset): The country of the company.
        company_country_code (None | str | Unset): The ISO 3166-1 alpha-2 country code.
        company_address (None | str | Unset): The address of the company.
        context (None | str | Unset): Additional context about the company. Helps distinguish between companies with
            similar names.
    """

    company_name: str
    company_website: None | str | Unset = UNSET
    company_city: None | str | Unset = UNSET
    company_state: None | str | Unset = UNSET
    company_country_name: None | str | Unset = UNSET
    company_country_code: None | str | Unset = UNSET
    company_address: None | str | Unset = UNSET
    context: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_name = self.company_name

        company_website: None | str | Unset
        if isinstance(self.company_website, Unset):
            company_website = UNSET
        else:
            company_website = self.company_website

        company_city: None | str | Unset
        if isinstance(self.company_city, Unset):
            company_city = UNSET
        else:
            company_city = self.company_city

        company_state: None | str | Unset
        if isinstance(self.company_state, Unset):
            company_state = UNSET
        else:
            company_state = self.company_state

        company_country_name: None | str | Unset
        if isinstance(self.company_country_name, Unset):
            company_country_name = UNSET
        else:
            company_country_name = self.company_country_name

        company_country_code: None | str | Unset
        if isinstance(self.company_country_code, Unset):
            company_country_code = UNSET
        else:
            company_country_code = self.company_country_code

        company_address: None | str | Unset
        if isinstance(self.company_address, Unset):
            company_address = UNSET
        else:
            company_address = self.company_address

        context: None | str | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        else:
            context = self.context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyName": company_name,
            }
        )
        if company_website is not UNSET:
            field_dict["companyWebsite"] = company_website
        if company_city is not UNSET:
            field_dict["companyCity"] = company_city
        if company_state is not UNSET:
            field_dict["companyState"] = company_state
        if company_country_name is not UNSET:
            field_dict["companyCountryName"] = company_country_name
        if company_country_code is not UNSET:
            field_dict["companyCountryCode"] = company_country_code
        if company_address is not UNSET:
            field_dict["companyAddress"] = company_address
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_name = d.pop("companyName")

        def _parse_company_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_website = _parse_company_website(d.pop("companyWebsite", UNSET))

        def _parse_company_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_city = _parse_company_city(d.pop("companyCity", UNSET))

        def _parse_company_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_state = _parse_company_state(d.pop("companyState", UNSET))

        def _parse_company_country_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_country_name = _parse_company_country_name(d.pop("companyCountryName", UNSET))

        def _parse_company_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_country_code = _parse_company_country_code(d.pop("companyCountryCode", UNSET))

        def _parse_company_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_address = _parse_company_address(d.pop("companyAddress", UNSET))

        def _parse_context(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        start_local_business_search_body_companies_item = cls(
            company_name=company_name,
            company_website=company_website,
            company_city=company_city,
            company_state=company_state,
            company_country_name=company_country_name,
            company_country_code=company_country_code,
            company_address=company_address,
            context=context,
        )

        start_local_business_search_body_companies_item.additional_properties = d
        return start_local_business_search_body_companies_item

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
