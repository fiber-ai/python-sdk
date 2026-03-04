from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.start_local_business_search_body_data_item_type_0_source import StartLocalBusinessSearchBodyDataItemType0Source
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="StartLocalBusinessSearchBodyDataItemType0")



@_attrs_define
class StartLocalBusinessSearchBodyDataItemType0:
    """ 
        Attributes:
            source (StartLocalBusinessSearchBodyDataItemType0Source):
            company_name (str): Business name
            domain (Union[None, Unset, str]): Domain of the business
            context (Union[None, Unset, str]): Context of the business like its industry, etc.
            city (Union[None, Unset, str]): City of the business
            state (Union[None, Unset, str]): State of the business
            state_code (Union[None, Unset, str]): State code of the business
            country_name (Union[None, Unset, str]): Country name of the business
            country_3_letter_code (Union[None, Unset, str]): Country 3 letter code of the business
            address (Union[None, Unset, str]): Address of the business
     """

    source: StartLocalBusinessSearchBodyDataItemType0Source
    company_name: str
    domain: Union[None, Unset, str] = UNSET
    context: Union[None, Unset, str] = UNSET
    city: Union[None, Unset, str] = UNSET
    state: Union[None, Unset, str] = UNSET
    state_code: Union[None, Unset, str] = UNSET
    country_name: Union[None, Unset, str] = UNSET
    country_3_letter_code: Union[None, Unset, str] = UNSET
    address: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        source = self.source.value

        company_name = self.company_name

        domain: Union[None, Unset, str]
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        context: Union[None, Unset, str]
        if isinstance(self.context, Unset):
            context = UNSET
        else:
            context = self.context

        city: Union[None, Unset, str]
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        state_code: Union[None, Unset, str]
        if isinstance(self.state_code, Unset):
            state_code = UNSET
        else:
            state_code = self.state_code

        country_name: Union[None, Unset, str]
        if isinstance(self.country_name, Unset):
            country_name = UNSET
        else:
            country_name = self.country_name

        country_3_letter_code: Union[None, Unset, str]
        if isinstance(self.country_3_letter_code, Unset):
            country_3_letter_code = UNSET
        else:
            country_3_letter_code = self.country_3_letter_code

        address: Union[None, Unset, str]
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "source": source,
            "companyName": company_name,
        })
        if domain is not UNSET:
            field_dict["domain"] = domain
        if context is not UNSET:
            field_dict["context"] = context
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if state_code is not UNSET:
            field_dict["stateCode"] = state_code
        if country_name is not UNSET:
            field_dict["countryName"] = country_name
        if country_3_letter_code is not UNSET:
            field_dict["country3LetterCode"] = country_3_letter_code
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = StartLocalBusinessSearchBodyDataItemType0Source(d.pop("source"))




        company_name = d.pop("companyName")

        def _parse_domain(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        domain = _parse_domain(d.pop("domain", UNSET))


        def _parse_context(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        context = _parse_context(d.pop("context", UNSET))


        def _parse_city(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        city = _parse_city(d.pop("city", UNSET))


        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))


        def _parse_state_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state_code = _parse_state_code(d.pop("stateCode", UNSET))


        def _parse_country_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        country_name = _parse_country_name(d.pop("countryName", UNSET))


        def _parse_country_3_letter_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        country_3_letter_code = _parse_country_3_letter_code(d.pop("country3LetterCode", UNSET))


        def _parse_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address = _parse_address(d.pop("address", UNSET))


        start_local_business_search_body_data_item_type_0 = cls(
            source=source,
            company_name=company_name,
            domain=domain,
            context=context,
            city=city,
            state=state,
            state_code=state_code,
            country_name=country_name,
            country_3_letter_code=country_3_letter_code,
            address=address,
        )


        start_local_business_search_body_data_item_type_0.additional_properties = d
        return start_local_business_search_body_data_item_type_0

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
