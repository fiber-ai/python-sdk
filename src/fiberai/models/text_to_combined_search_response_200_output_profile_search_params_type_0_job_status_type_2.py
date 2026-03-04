from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_2_status import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType2Status






T = TypeVar("T", bound="TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType2")



@_attrs_define
class TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType2:
    """ 
        Attributes:
            status (TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType2Status):
     """

    status: TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType2Status
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        status = self.status.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType2Status(d.pop("status"))




        text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_2 = cls(
            status=status,
        )


        text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_2.additional_properties = d
        return text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_2

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
