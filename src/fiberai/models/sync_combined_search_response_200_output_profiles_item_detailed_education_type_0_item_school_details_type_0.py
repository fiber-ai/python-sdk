from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="SyncCombinedSearchResponse200OutputProfilesItemDetailedEducationType0ItemSchoolDetailsType0")



@_attrs_define
class SyncCombinedSearchResponse200OutputProfilesItemDetailedEducationType0ItemSchoolDetailsType0:
    """ 
        Attributes:
            linkedin_ids (Union[None, Unset, list[str]]):
            li_org_id (Union[None, Unset, str]):
            linkedin_primary_slug (Union[None, Unset, str]):
            domains (Union[None, Unset, list[str]]):
            preferred_name (Union[None, Unset, str]):
     """

    linkedin_ids: Union[None, Unset, list[str]] = UNSET
    li_org_id: Union[None, Unset, str] = UNSET
    linkedin_primary_slug: Union[None, Unset, str] = UNSET
    domains: Union[None, Unset, list[str]] = UNSET
    preferred_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        linkedin_ids: Union[None, Unset, list[str]]
        if isinstance(self.linkedin_ids, Unset):
            linkedin_ids = UNSET
        elif isinstance(self.linkedin_ids, list):
            linkedin_ids = self.linkedin_ids


        else:
            linkedin_ids = self.linkedin_ids

        li_org_id: Union[None, Unset, str]
        if isinstance(self.li_org_id, Unset):
            li_org_id = UNSET
        else:
            li_org_id = self.li_org_id

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

        preferred_name: Union[None, Unset, str]
        if isinstance(self.preferred_name, Unset):
            preferred_name = UNSET
        else:
            preferred_name = self.preferred_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if linkedin_ids is not UNSET:
            field_dict["linkedin_ids"] = linkedin_ids
        if li_org_id is not UNSET:
            field_dict["li_org_id"] = li_org_id
        if linkedin_primary_slug is not UNSET:
            field_dict["linkedin_primary_slug"] = linkedin_primary_slug
        if domains is not UNSET:
            field_dict["domains"] = domains
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_linkedin_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                linkedin_ids_type_0 = cast(list[str], data)

                return linkedin_ids_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        linkedin_ids = _parse_linkedin_ids(d.pop("linkedin_ids", UNSET))


        def _parse_li_org_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        li_org_id = _parse_li_org_id(d.pop("li_org_id", UNSET))


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


        def _parse_preferred_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        preferred_name = _parse_preferred_name(d.pop("preferred_name", UNSET))


        sync_combined_search_response_200_output_profiles_item_detailed_education_type_0_item_school_details_type_0 = cls(
            linkedin_ids=linkedin_ids,
            li_org_id=li_org_id,
            linkedin_primary_slug=linkedin_primary_slug,
            domains=domains,
            preferred_name=preferred_name,
        )


        sync_combined_search_response_200_output_profiles_item_detailed_education_type_0_item_school_details_type_0.additional_properties = d
        return sync_combined_search_response_200_output_profiles_item_detailed_education_type_0_item_school_details_type_0

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
