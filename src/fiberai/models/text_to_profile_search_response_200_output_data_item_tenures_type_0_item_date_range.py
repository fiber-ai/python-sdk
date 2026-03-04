from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="TextToProfileSearchResponse200OutputDataItemTenuresType0ItemDateRange")



@_attrs_define
class TextToProfileSearchResponse200OutputDataItemTenuresType0ItemDateRange:
    """ 
        Attributes:
            gte (Union[None, Unset, str]):
            lte (Union[None, Unset, str]):
     """

    gte: Union[None, Unset, str] = UNSET
    lte: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        gte: Union[None, Unset, str]
        if isinstance(self.gte, Unset):
            gte = UNSET
        else:
            gte = self.gte

        lte: Union[None, Unset, str]
        if isinstance(self.lte, Unset):
            lte = UNSET
        else:
            lte = self.lte


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if gte is not UNSET:
            field_dict["gte"] = gte
        if lte is not UNSET:
            field_dict["lte"] = lte

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_gte(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        gte = _parse_gte(d.pop("gte", UNSET))


        def _parse_lte(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        lte = _parse_lte(d.pop("lte", UNSET))


        text_to_profile_search_response_200_output_data_item_tenures_type_0_item_date_range = cls(
            gte=gte,
            lte=lte,
        )


        text_to_profile_search_response_200_output_data_item_tenures_type_0_item_date_range.additional_properties = d
        return text_to_profile_search_response_200_output_data_item_tenures_type_0_item_date_range

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
