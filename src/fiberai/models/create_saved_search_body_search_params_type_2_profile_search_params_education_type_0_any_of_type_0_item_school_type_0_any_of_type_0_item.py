from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationType0AnyOfType0ItemSchoolType0AnyOfType0Item")



@_attrs_define
class CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationType0AnyOfType0ItemSchoolType0AnyOfType0Item:
    """ Requires at least one identifier: LinkedIn school ID, LinkedIn URL, or website domain to uniquely identify the
    school.

        Attributes:
            linkedin_id (Union[None, Unset, str]): The LinkedIn organization ID of the school, like 1646 for Harvard
                University
            linkedin_url (Union[None, Unset, str]): The LinkedIn URL of the school, like
                'https://www.linkedin.com/school/harvard-university/'
            domain (Union[None, Unset, str]): The domain of the school, like 'harvard.edu'
     """

    linkedin_id: Union[None, Unset, str] = UNSET
    linkedin_url: Union[None, Unset, str] = UNSET
    domain: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        linkedin_id: Union[None, Unset, str]
        if isinstance(self.linkedin_id, Unset):
            linkedin_id = UNSET
        else:
            linkedin_id = self.linkedin_id

        linkedin_url: Union[None, Unset, str]
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        domain: Union[None, Unset, str]
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if linkedin_id is not UNSET:
            field_dict["linkedinId"] = linkedin_id
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url
        if domain is not UNSET:
            field_dict["domain"] = domain

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_linkedin_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        linkedin_id = _parse_linkedin_id(d.pop("linkedinId", UNSET))


        def _parse_linkedin_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))


        def _parse_domain(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        domain = _parse_domain(d.pop("domain", UNSET))


        create_saved_search_body_search_params_type_2_profile_search_params_education_type_0_any_of_type_0_item_school_type_0_any_of_type_0_item = cls(
            linkedin_id=linkedin_id,
            linkedin_url=linkedin_url,
            domain=domain,
        )


        create_saved_search_body_search_params_type_2_profile_search_params_education_type_0_any_of_type_0_item_school_type_0_any_of_type_0_item.additional_properties = d
        return create_saved_search_body_search_params_type_2_profile_search_params_education_type_0_any_of_type_0_item_school_type_0_any_of_type_0_item

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
