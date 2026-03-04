from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="DomainLookupTriggerBodyCompanyInfoItem")



@_attrs_define
class DomainLookupTriggerBodyCompanyInfoItem:
    """ 
        Attributes:
            name (str): The name of the company.
            country (Union[None, Unset, str]): The country where the company is based. Provide full country name (e.g.
                United Kingdom) or ISO 3166-1 alpha-3 code (e.g. GBR)
            state (Union[None, Unset, str]): The state where the company is based. Provide full state name (e.g. California)
                or code (e.g. CA).
            city (Union[None, Unset, str]): The city where the company is located.
            address (Union[None, Unset, str]): The street address of the company.
            other_context (Union[None, Unset, str]): Any other disambiguating information or identifiers for the company,
                such as "YC startup" or "Italian airline"
            description (Union[None, Unset, str]): A description of the company, such as what it does or its industry focus.
     """

    name: str
    country: Union[None, Unset, str] = UNSET
    state: Union[None, Unset, str] = UNSET
    city: Union[None, Unset, str] = UNSET
    address: Union[None, Unset, str] = UNSET
    other_context: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        country: Union[None, Unset, str]
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

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

        address: Union[None, Unset, str]
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        other_context: Union[None, Unset, str]
        if isinstance(self.other_context, Unset):
            other_context = UNSET
        else:
            other_context = self.other_context

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if country is not UNSET:
            field_dict["country"] = country
        if state is not UNSET:
            field_dict["state"] = state
        if city is not UNSET:
            field_dict["city"] = city
        if address is not UNSET:
            field_dict["address"] = address
        if other_context is not UNSET:
            field_dict["otherContext"] = other_context
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_country(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        country = _parse_country(d.pop("country", UNSET))


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


        def _parse_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address = _parse_address(d.pop("address", UNSET))


        def _parse_other_context(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        other_context = _parse_other_context(d.pop("otherContext", UNSET))


        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))


        domain_lookup_trigger_body_company_info_item = cls(
            name=name,
            country=country,
            state=state,
            city=city,
            address=address,
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
