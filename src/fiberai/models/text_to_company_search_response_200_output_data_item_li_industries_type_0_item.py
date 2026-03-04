from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="TextToCompanySearchResponse200OutputDataItemLiIndustriesType0Item")



@_attrs_define
class TextToCompanySearchResponse200OutputDataItemLiIndustriesType0Item:
    """ 
        Attributes:
            id (str):
            name (str):
            primary (Union[None, Unset, bool]):
     """

    id: str
    name: str
    primary: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        primary: Union[None, Unset, bool]
        if isinstance(self.primary, Unset):
            primary = UNSET
        else:
            primary = self.primary


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
        })
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_primary(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        primary = _parse_primary(d.pop("primary", UNSET))


        text_to_company_search_response_200_output_data_item_li_industries_type_0_item = cls(
            id=id,
            name=name,
            primary=primary,
        )


        text_to_company_search_response_200_output_data_item_li_industries_type_0_item.additional_properties = d
        return text_to_company_search_response_200_output_data_item_li_industries_type_0_item

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
