from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainLookupTriggerBodyCompanyInfoItem")


@_attrs_define
class DomainLookupTriggerBodyCompanyInfoItem:
    """
    Attributes:
        name (str): The name of the company.
        domain (None | str | Unset): The domain of the company if already known (e.g. 'example.com'). If provided and
            findEmailDomains is true, the agent will skip domain search and only find email domains. Else if not provided,
            the agent will search for the domain.
        country (None | str | Unset): The country where the company is based. Provide full country name (e.g. United
            Kingdom) or ISO 3166-1 alpha-3 code (e.g. GBR)
        state (None | str | Unset): The state where the company is based. Provide full state name (e.g. California) or
            code (e.g. CA).
        city (None | str | Unset): The city where the company is located.
        address (None | str | Unset): The street address of the company.
        find_email_domains (bool | Unset): Whether to find the email domains of the company. Default: False.
        other_context (None | str | Unset): Any other disambiguating information or identifiers for the company, such as
            "YC startup" or "Italian airline"
        description (None | str | Unset): A description of the company, such as what it does or its industry focus.
    """

    name: str
    domain: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    find_email_domains: bool | Unset = False
    other_context: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

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

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        find_email_domains = self.find_email_domains

        other_context: None | str | Unset
        if isinstance(self.other_context, Unset):
            other_context = UNSET
        else:
            other_context = self.other_context

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain
        if country is not UNSET:
            field_dict["country"] = country
        if state is not UNSET:
            field_dict["state"] = state
        if city is not UNSET:
            field_dict["city"] = city
        if address is not UNSET:
            field_dict["address"] = address
        if find_email_domains is not UNSET:
            field_dict["findEmailDomains"] = find_email_domains
        if other_context is not UNSET:
            field_dict["otherContext"] = other_context
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

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

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        find_email_domains = d.pop("findEmailDomains", UNSET)

        def _parse_other_context(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_context = _parse_other_context(d.pop("otherContext", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        domain_lookup_trigger_body_company_info_item = cls(
            name=name,
            domain=domain,
            country=country,
            state=state,
            city=city,
            address=address,
            find_email_domains=find_email_domains,
            other_context=other_context,
            description=description,
        )

        domain_lookup_trigger_body_company_info_item.additional_properties = d
        return domain_lookup_trigger_body_company_info_item

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
