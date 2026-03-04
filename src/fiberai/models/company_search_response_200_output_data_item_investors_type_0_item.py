from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="CompanySearchResponse200OutputDataItemInvestorsType0Item")



@_attrs_define
class CompanySearchResponse200OutputDataItemInvestorsType0Item:
    """ 
        Attributes:
            logo_url (Union[None, Unset, str]):
            entity_type (Union[None, Unset, str]):
            investor_name (Union[None, Unset, str]):
            linkedin_slug (Union[None, Unset, str]):
            investor_types (Union[None, Unset, list[str]]):
     """

    logo_url: Union[None, Unset, str] = UNSET
    entity_type: Union[None, Unset, str] = UNSET
    investor_name: Union[None, Unset, str] = UNSET
    linkedin_slug: Union[None, Unset, str] = UNSET
    investor_types: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        logo_url: Union[None, Unset, str]
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        entity_type: Union[None, Unset, str]
        if isinstance(self.entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = self.entity_type

        investor_name: Union[None, Unset, str]
        if isinstance(self.investor_name, Unset):
            investor_name = UNSET
        else:
            investor_name = self.investor_name

        linkedin_slug: Union[None, Unset, str]
        if isinstance(self.linkedin_slug, Unset):
            linkedin_slug = UNSET
        else:
            linkedin_slug = self.linkedin_slug

        investor_types: Union[None, Unset, list[str]]
        if isinstance(self.investor_types, Unset):
            investor_types = UNSET
        elif isinstance(self.investor_types, list):
            investor_types = self.investor_types


        else:
            investor_types = self.investor_types


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if investor_name is not UNSET:
            field_dict["investor_name"] = investor_name
        if linkedin_slug is not UNSET:
            field_dict["linkedin_slug"] = linkedin_slug
        if investor_types is not UNSET:
            field_dict["investor_types"] = investor_types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_logo_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))


        def _parse_entity_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        entity_type = _parse_entity_type(d.pop("entity_type", UNSET))


        def _parse_investor_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        investor_name = _parse_investor_name(d.pop("investor_name", UNSET))


        def _parse_linkedin_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        linkedin_slug = _parse_linkedin_slug(d.pop("linkedin_slug", UNSET))


        def _parse_investor_types(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                investor_types_type_0 = cast(list[str], data)

                return investor_types_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        investor_types = _parse_investor_types(d.pop("investor_types", UNSET))


        company_search_response_200_output_data_item_investors_type_0_item = cls(
            logo_url=logo_url,
            entity_type=entity_type,
            investor_name=investor_name,
            linkedin_slug=linkedin_slug,
            investor_types=investor_types,
        )


        company_search_response_200_output_data_item_investors_type_0_item.additional_properties = d
        return company_search_response_200_output_data_item_investors_type_0_item

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
