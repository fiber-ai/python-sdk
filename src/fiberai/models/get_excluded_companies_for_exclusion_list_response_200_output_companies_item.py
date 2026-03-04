from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetExcludedCompaniesForExclusionListResponse200OutputCompaniesItem")



@_attrs_define
class GetExcludedCompaniesForExclusionListResponse200OutputCompaniesItem:
    """ 
        Attributes:
            id (str): ID of the excluded company
            domain (Union[None, str]): Domain of the excluded company
            linked_in_url (Union[None, str]): LinkedIn URL of the excluded company
            name (Union[None, str]): Name of the excluded company
     """

    id: str
    domain: Union[None, str]
    linked_in_url: Union[None, str]
    name: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        domain: Union[None, str]
        domain = self.domain

        linked_in_url: Union[None, str]
        linked_in_url = self.linked_in_url

        name: Union[None, str]
        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "domain": domain,
            "linkedInUrl": linked_in_url,
            "name": name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_domain(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        domain = _parse_domain(d.pop("domain"))


        def _parse_linked_in_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        linked_in_url = _parse_linked_in_url(d.pop("linkedInUrl"))


        def _parse_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        name = _parse_name(d.pop("name"))


        get_excluded_companies_for_exclusion_list_response_200_output_companies_item = cls(
            id=id,
            domain=domain,
            linked_in_url=linked_in_url,
            name=name,
        )


        get_excluded_companies_for_exclusion_list_response_200_output_companies_item.additional_properties = d
        return get_excluded_companies_for_exclusion_list_response_200_output_companies_item

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
