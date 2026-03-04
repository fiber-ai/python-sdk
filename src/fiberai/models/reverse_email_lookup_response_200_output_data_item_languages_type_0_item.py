from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="ReverseEmailLookupResponse200OutputDataItemLanguagesType0Item")



@_attrs_define
class ReverseEmailLookupResponse200OutputDataItemLanguagesType0Item:
    """ 
        Attributes:
            name (Union[None, Unset, str]):
            proficiency_id (Union[None, Unset, str]):
            proficiency_name (Union[None, Unset, str]):
     """

    name: Union[None, Unset, str] = UNSET
    proficiency_id: Union[None, Unset, str] = UNSET
    proficiency_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        proficiency_id: Union[None, Unset, str]
        if isinstance(self.proficiency_id, Unset):
            proficiency_id = UNSET
        else:
            proficiency_id = self.proficiency_id

        proficiency_name: Union[None, Unset, str]
        if isinstance(self.proficiency_name, Unset):
            proficiency_name = UNSET
        else:
            proficiency_name = self.proficiency_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if proficiency_id is not UNSET:
            field_dict["proficiency_id"] = proficiency_id
        if proficiency_name is not UNSET:
            field_dict["proficiency_name"] = proficiency_name

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


        def _parse_proficiency_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        proficiency_id = _parse_proficiency_id(d.pop("proficiency_id", UNSET))


        def _parse_proficiency_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        proficiency_name = _parse_proficiency_name(d.pop("proficiency_name", UNSET))


        reverse_email_lookup_response_200_output_data_item_languages_type_0_item = cls(
            name=name,
            proficiency_id=proficiency_id,
            proficiency_name=proficiency_name,
        )


        reverse_email_lookup_response_200_output_data_item_languages_type_0_item.additional_properties = d
        return reverse_email_lookup_response_200_output_data_item_languages_type_0_item

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
