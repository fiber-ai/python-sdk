from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="CombinedSearchBodyProfileParamsExactProfileType0NoneOfType0Item")



@_attrs_define
class CombinedSearchBodyProfileParamsExactProfileType0NoneOfType0Item:
    """ 
        Attributes:
            profile_id (Union[None, Unset, str]):
            primary_slug (Union[None, Unset, str]):
     """

    profile_id: Union[None, Unset, str] = UNSET
    primary_slug: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        profile_id: Union[None, Unset, str]
        if isinstance(self.profile_id, Unset):
            profile_id = UNSET
        else:
            profile_id = self.profile_id

        primary_slug: Union[None, Unset, str]
        if isinstance(self.primary_slug, Unset):
            primary_slug = UNSET
        else:
            primary_slug = self.primary_slug


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if profile_id is not UNSET:
            field_dict["profile_id"] = profile_id
        if primary_slug is not UNSET:
            field_dict["primary_slug"] = primary_slug

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_profile_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        profile_id = _parse_profile_id(d.pop("profile_id", UNSET))


        def _parse_primary_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        primary_slug = _parse_primary_slug(d.pop("primary_slug", UNSET))


        combined_search_body_profile_params_exact_profile_type_0_none_of_type_0_item = cls(
            profile_id=profile_id,
            primary_slug=primary_slug,
        )


        combined_search_body_profile_params_exact_profile_type_0_none_of_type_0_item.additional_properties = d
        return combined_search_body_profile_params_exact_profile_type_0_none_of_type_0_item

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
