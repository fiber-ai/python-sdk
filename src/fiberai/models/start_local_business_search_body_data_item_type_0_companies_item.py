from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartLocalBusinessSearchBodyDataItemType0CompaniesItem")


@_attrs_define
class StartLocalBusinessSearchBodyDataItemType0CompaniesItem:
    """
    Attributes:
        company_name (str): The name of the company to search for
        company_domain (None | str | Unset): The domain of the company
        company_city (None | str | Unset): The city where the company is located
        company_state (None | str | Unset): The state where the company is located
        company_country_name (None | str | Unset): The country of the company
        company_country_code (None | str | Unset): The ISO 3166-1 alpha-2 code of the company
        company_address (None | str | Unset): The address of the company
        context (None | str | Unset): The general context of the company. Helps agent to distinguish between companies
            with similar names. You can provide any additional information that helps agent to search for the company
            better.
        find_owner_contact_info (bool | Unset): Whether to search for owner/founder contact information. Defaults to
            false. Default: False.
    """

    company_name: str
    company_domain: None | str | Unset = UNSET
    company_city: None | str | Unset = UNSET
    company_state: None | str | Unset = UNSET
    company_country_name: None | str | Unset = UNSET
    company_country_code: None | str | Unset = UNSET
    company_address: None | str | Unset = UNSET
    context: None | str | Unset = UNSET
    find_owner_contact_info: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_name = self.company_name

        company_domain: None | str | Unset
        if isinstance(self.company_domain, Unset):
            company_domain = UNSET
        else:
            company_domain = self.company_domain

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

        find_owner_contact_info = self.find_owner_contact_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyName": company_name,
            }
        )
        if company_domain is not UNSET:
            field_dict["companyDomain"] = company_domain
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
        if find_owner_contact_info is not UNSET:
            field_dict["findOwnerContactInfo"] = find_owner_contact_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_name = d.pop("companyName")

        def _parse_company_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_domain = _parse_company_domain(d.pop("companyDomain", UNSET))

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

        find_owner_contact_info = d.pop("findOwnerContactInfo", UNSET)

        start_local_business_search_body_data_item_type_0_companies_item = cls(
            company_name=company_name,
            company_domain=company_domain,
            company_city=company_city,
            company_state=company_state,
            company_country_name=company_country_name,
            company_country_code=company_country_code,
            company_address=company_address,
            context=context,
            find_owner_contact_info=find_owner_contact_info,
        )

        start_local_business_search_body_data_item_type_0_companies_item.additional_properties = d
        return start_local_business_search_body_data_item_type_0_companies_item

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
