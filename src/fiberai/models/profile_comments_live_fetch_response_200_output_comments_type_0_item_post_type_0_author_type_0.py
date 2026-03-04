from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0AuthorType0")



@_attrs_define
class ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0AuthorType0:
    """ 
        Attributes:
            name (Union[None, Unset, str]):
            linkedin_url (Union[None, Unset, str]):
            entity_urn (Union[None, Unset, str]):
     """

    name: Union[None, Unset, str] = UNSET
    linkedin_url: Union[None, Unset, str] = UNSET
    entity_urn: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        linkedin_url: Union[None, Unset, str]
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        entity_urn: Union[None, Unset, str]
        if isinstance(self.entity_urn, Unset):
            entity_urn = UNSET
        else:
            entity_urn = self.entity_urn


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url
        if entity_urn is not UNSET:
            field_dict["entityUrn"] = entity_urn

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_linkedin_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))


        def _parse_entity_urn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        entity_urn = _parse_entity_urn(d.pop("entityUrn", UNSET))


        profile_comments_live_fetch_response_200_output_comments_type_0_item_post_type_0_author_type_0 = cls(
            name=name,
            linkedin_url=linkedin_url,
            entity_urn=entity_urn,
        )


        profile_comments_live_fetch_response_200_output_comments_type_0_item_post_type_0_author_type_0.additional_properties = d
        return profile_comments_live_fetch_response_200_output_comments_type_0_item_post_type_0_author_type_0

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
