from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetNaicsCodesResponse200OutputNaicsCodesItem")



@_attrs_define
class GetNaicsCodesResponse200OutputNaicsCodesItem:
    """ 
        Attributes:
            code (str): The NAICS code identifier (2017 version)
            title (str): The title/description of the NAICS code
     """

    code: str
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        title = self.title


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
            "title": title,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        title = d.pop("title")

        get_naics_codes_response_200_output_naics_codes_item = cls(
            code=code,
            title=title,
        )


        get_naics_codes_response_200_output_naics_codes_item.additional_properties = d
        return get_naics_codes_response_200_output_naics_codes_item

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
