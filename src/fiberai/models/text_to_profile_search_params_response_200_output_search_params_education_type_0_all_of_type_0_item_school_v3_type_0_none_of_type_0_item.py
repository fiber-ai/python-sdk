from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.text_to_profile_search_params_response_200_output_search_params_education_type_0_all_of_type_0_item_school_v3_type_0_none_of_type_0_item_source_type_1 import TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType1
from ..models.text_to_profile_search_params_response_200_output_search_params_education_type_0_all_of_type_0_item_school_v3_type_0_none_of_type_0_item_source_type_2_type_1 import TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType2Type1
from ..models.text_to_profile_search_params_response_200_output_search_params_education_type_0_all_of_type_0_item_school_v3_type_0_none_of_type_0_item_source_type_3_type_1 import TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType3Type1
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0Item")



@_attrs_define
class TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0Item:
    """ 
        Attributes:
            li_org_id (str):
            linkedin_id (Union[None, Unset, str]):
            preferred_name (Union[None, Unset, str]):
            names (Union[None, Unset, list[str]]):
            linkedin_primary_slug (Union[None, Unset, str]):
            domains (Union[None, Unset, list[str]]):
            logo_url (Union[None, Unset, str]):
            source (Union[None, TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Ty
                pe0NoneOfType0ItemSourceType1, TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0Ite
                mSchoolV3Type0NoneOfType0ItemSourceType2Type1, TextToProfileSearchParamsResponse200OutputSearchParamsEducationTy
                pe0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType3Type1, Unset]):
     """

    li_org_id: str
    linkedin_id: Union[None, Unset, str] = UNSET
    preferred_name: Union[None, Unset, str] = UNSET
    names: Union[None, Unset, list[str]] = UNSET
    linkedin_primary_slug: Union[None, Unset, str] = UNSET
    domains: Union[None, Unset, list[str]] = UNSET
    logo_url: Union[None, Unset, str] = UNSET
    source: Union[None, TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType1, TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType2Type1, TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType3Type1, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        li_org_id = self.li_org_id

        linkedin_id: Union[None, Unset, str]
        if isinstance(self.linkedin_id, Unset):
            linkedin_id = UNSET
        else:
            linkedin_id = self.linkedin_id

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

        linkedin_primary_slug: Union[None, Unset, str]
        if isinstance(self.linkedin_primary_slug, Unset):
            linkedin_primary_slug = UNSET
        else:
            linkedin_primary_slug = self.linkedin_primary_slug

        domains: Union[None, Unset, list[str]]
        if isinstance(self.domains, Unset):
            domains = UNSET
        elif isinstance(self.domains, list):
            domains = self.domains


        else:
            domains = self.domains

        logo_url: Union[None, Unset, str]
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        source: Union[None, Unset, str]
        if isinstance(self.source, Unset):
            source = UNSET
        elif isinstance(self.source, TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType1):
            source = self.source.value
        elif isinstance(self.source, TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType2Type1):
            source = self.source.value
        elif isinstance(self.source, TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType3Type1):
            source = self.source.value
        else:
            source = self.source


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "li_org_id": li_org_id,
        })
        if linkedin_id is not UNSET:
            field_dict["linkedin_id"] = linkedin_id
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name
        if names is not UNSET:
            field_dict["names"] = names
        if linkedin_primary_slug is not UNSET:
            field_dict["linkedin_primary_slug"] = linkedin_primary_slug
        if domains is not UNSET:
            field_dict["domains"] = domains
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        li_org_id = d.pop("li_org_id")

        def _parse_linkedin_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        linkedin_id = _parse_linkedin_id(d.pop("linkedin_id", UNSET))


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


        def _parse_linkedin_primary_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        linkedin_primary_slug = _parse_linkedin_primary_slug(d.pop("linkedin_primary_slug", UNSET))


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


        def _parse_logo_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))


        def _parse_source(data: object) -> Union[None, TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType1, TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType2Type1, TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType3Type1, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_type_1 = TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType1(data)



                return source_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_type_2_type_1 = TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType2Type1(data)



                return source_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_type_3_type_1 = TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType3Type1(data)



                return source_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[None, TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType1, TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType2Type1, TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AllOfType0ItemSchoolV3Type0NoneOfType0ItemSourceType3Type1, Unset], data)

        source = _parse_source(d.pop("source", UNSET))


        text_to_profile_search_params_response_200_output_search_params_education_type_0_all_of_type_0_item_school_v3_type_0_none_of_type_0_item = cls(
            li_org_id=li_org_id,
            linkedin_id=linkedin_id,
            preferred_name=preferred_name,
            names=names,
            linkedin_primary_slug=linkedin_primary_slug,
            domains=domains,
            logo_url=logo_url,
            source=source,
        )


        text_to_profile_search_params_response_200_output_search_params_education_type_0_all_of_type_0_item_school_v3_type_0_none_of_type_0_item.additional_properties = d
        return text_to_profile_search_params_response_200_output_search_params_education_type_0_all_of_type_0_item_school_v3_type_0_none_of_type_0_item

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
