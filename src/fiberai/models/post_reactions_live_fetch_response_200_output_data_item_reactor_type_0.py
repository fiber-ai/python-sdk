from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostReactionsLiveFetchResponse200OutputDataItemReactorType0")



@_attrs_define
class PostReactionsLiveFetchResponse200OutputDataItemReactorType0:
    """ 
        Attributes:
            user_id (Union[None, Unset, float]):
            entity_urn (Union[None, Unset, str]):
            profile_picture (Union[None, Unset, str]):
            name (Union[None, Unset, str]):
            headline (Union[None, Unset, str]):
     """

    user_id: Union[None, Unset, float] = UNSET
    entity_urn: Union[None, Unset, str] = UNSET
    profile_picture: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    headline: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        user_id: Union[None, Unset, float]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        entity_urn: Union[None, Unset, str]
        if isinstance(self.entity_urn, Unset):
            entity_urn = UNSET
        else:
            entity_urn = self.entity_urn

        profile_picture: Union[None, Unset, str]
        if isinstance(self.profile_picture, Unset):
            profile_picture = UNSET
        else:
            profile_picture = self.profile_picture

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        headline: Union[None, Unset, str]
        if isinstance(self.headline, Unset):
            headline = UNSET
        else:
            headline = self.headline


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if entity_urn is not UNSET:
            field_dict["entityUrn"] = entity_urn
        if profile_picture is not UNSET:
            field_dict["profilePicture"] = profile_picture
        if name is not UNSET:
            field_dict["name"] = name
        if headline is not UNSET:
            field_dict["headline"] = headline

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_user_id(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        user_id = _parse_user_id(d.pop("userId", UNSET))


        def _parse_entity_urn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        entity_urn = _parse_entity_urn(d.pop("entityUrn", UNSET))


        def _parse_profile_picture(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        profile_picture = _parse_profile_picture(d.pop("profilePicture", UNSET))


        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_headline(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        headline = _parse_headline(d.pop("headline", UNSET))


        post_reactions_live_fetch_response_200_output_data_item_reactor_type_0 = cls(
            user_id=user_id,
            entity_urn=entity_urn,
            profile_picture=profile_picture,
            name=name,
            headline=headline,
        )


        post_reactions_live_fetch_response_200_output_data_item_reactor_type_0.additional_properties = d
        return post_reactions_live_fetch_response_200_output_data_item_reactor_type_0

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
