from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="CompanyTypeaheadResponse200OutputItem")



@_attrs_define
class CompanyTypeaheadResponse200OutputItem:
    """ 
        Attributes:
            preferred_name (Union[None, Unset, str]):
            names (Union[None, Unset, list[str]]):
            domains (Union[None, Unset, list[str]]):
            linkedin_primary_slug (Union[None, Unset, str]):
            li_org_id (Union[None, Unset, str]):
     """

    preferred_name: Union[None, Unset, str] = UNSET
    names: Union[None, Unset, list[str]] = UNSET
    domains: Union[None, Unset, list[str]] = UNSET
    linkedin_primary_slug: Union[None, Unset, str] = UNSET
    li_org_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        preferred_name: Union[None, Unset, str]
        if isinstance(self.preferred_name, Unset):
            preferred_name = UNSET
        else:
            preferred_name = self.preferred_name

        names: Union[None, Unset, list[str]]
        if isinstance(self.names, Unset):
            names = UNSET
        elif isinstance(self.names, list):
            names = self.names


        else:
            names = self.names

        domains: Union[None, Unset, list[str]]
        if isinstance(self.domains, Unset):
            domains = UNSET
        elif isinstance(self.domains, list):
            domains = self.domains


        else:
            domains = self.domains

        linkedin_primary_slug: Union[None, Unset, str]
        if isinstance(self.linkedin_primary_slug, Unset):
            linkedin_primary_slug = UNSET
        else:
            linkedin_primary_slug = self.linkedin_primary_slug

        li_org_id: Union[None, Unset, str]
        if isinstance(self.li_org_id, Unset):
            li_org_id = UNSET
        else:
            li_org_id = self.li_org_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name
        if names is not UNSET:
            field_dict["names"] = names
        if domains is not UNSET:
            field_dict["domains"] = domains
        if linkedin_primary_slug is not UNSET:
            field_dict["linkedin_primary_slug"] = linkedin_primary_slug
        if li_org_id is not UNSET:
            field_dict["li_org_id"] = li_org_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_preferred_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        preferred_name = _parse_preferred_name(d.pop("preferred_name", UNSET))


        def _parse_names(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                names_type_0 = cast(list[str], data)

                return names_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        names = _parse_names(d.pop("names", UNSET))


        def _parse_domains(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                domains_type_0 = cast(list[str], data)

                return domains_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        domains = _parse_domains(d.pop("domains", UNSET))


        def _parse_linkedin_primary_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        linkedin_primary_slug = _parse_linkedin_primary_slug(d.pop("linkedin_primary_slug", UNSET))


        def _parse_li_org_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        li_org_id = _parse_li_org_id(d.pop("li_org_id", UNSET))


        company_typeahead_response_200_output_item = cls(
            preferred_name=preferred_name,
            names=names,
            domains=domains,
            linkedin_primary_slug=linkedin_primary_slug,
            li_org_id=li_org_id,
        )


        company_typeahead_response_200_output_item.additional_properties = d
        return company_typeahead_response_200_output_item

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
