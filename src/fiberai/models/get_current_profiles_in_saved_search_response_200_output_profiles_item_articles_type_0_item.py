from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="GetCurrentProfilesInSavedSearchResponse200OutputProfilesItemArticlesType0Item")



@_attrs_define
class GetCurrentProfilesInSavedSearchResponse200OutputProfilesItemArticlesType0Item:
    """ 
        Attributes:
            id (Union[None, Unset, str]):
            title (Union[None, Unset, str]):
            date_published (Union[None, Unset, str]):
     """

    id: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    date_published: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        date_published: Union[None, Unset, str]
        if isinstance(self.date_published, Unset):
            date_published = UNSET
        else:
            date_published = self.date_published


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if date_published is not UNSET:
            field_dict["date_published"] = date_published

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_date_published(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        date_published = _parse_date_published(d.pop("date_published", UNSET))


        get_current_profiles_in_saved_search_response_200_output_profiles_item_articles_type_0_item = cls(
            id=id,
            title=title,
            date_published=date_published,
        )


        get_current_profiles_in_saved_search_response_200_output_profiles_item_articles_type_0_item.additional_properties = d
        return get_current_profiles_in_saved_search_response_200_output_profiles_item_articles_type_0_item

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
