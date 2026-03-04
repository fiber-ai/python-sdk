from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_title_v3_type_0_any_of_type_0_item_type_2_type import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobTitleV3Type0AnyOfType0ItemType2Type
from typing import cast






T = TypeVar("T", bound="TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobTitleV3Type0AnyOfType0ItemType2")



@_attrs_define
class TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobTitleV3Type0AnyOfType0ItemType2:
    """ 
        Attributes:
            type_ (TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobTitleV3Type0AnyOfType0ItemType2Type):
            keyword_arrays (list[list[str]]):
     """

    type_: TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobTitleV3Type0AnyOfType0ItemType2Type
    keyword_arrays: list[list[str]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        keyword_arrays = []
        for keyword_arrays_item_data in self.keyword_arrays:
            keyword_arrays_item = keyword_arrays_item_data


            keyword_arrays.append(keyword_arrays_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "keywordArrays": keyword_arrays,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobTitleV3Type0AnyOfType0ItemType2Type(d.pop("type"))




        keyword_arrays = []
        _keyword_arrays = d.pop("keywordArrays")
        for keyword_arrays_item_data in (_keyword_arrays):
            keyword_arrays_item = cast(list[str], keyword_arrays_item_data)

            keyword_arrays.append(keyword_arrays_item)


        text_to_combined_search_response_200_output_profile_search_params_type_0_job_title_v3_type_0_any_of_type_0_item_type_2 = cls(
            type_=type_,
            keyword_arrays=keyword_arrays,
        )


        text_to_combined_search_response_200_output_profile_search_params_type_0_job_title_v3_type_0_any_of_type_0_item_type_2.additional_properties = d
        return text_to_combined_search_response_200_output_profile_search_params_type_0_job_title_v3_type_0_any_of_type_0_item_type_2

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
