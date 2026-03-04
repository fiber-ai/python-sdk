from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0Range")



@_attrs_define
class TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0Range:
    """ 
        Attributes:
            lower_bound (float):
            upper_bound (float):
     """

    lower_bound: float
    upper_bound: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        lower_bound = self.lower_bound

        upper_bound = self.upper_bound


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "lowerBound": lower_bound,
            "upperBound": upper_bound,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lower_bound = d.pop("lowerBound")

        upper_bound = d.pop("upperBound")

        text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_stealth_duration_type_0_range = cls(
            lower_bound=lower_bound,
            upper_bound=upper_bound,
        )


        text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_stealth_duration_type_0_range.additional_properties = d
        return text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_stealth_duration_type_0_range

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
