from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_1_status import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1Status
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_1_left_at_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1LeftAtType0
  from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_1_left_at_type_1 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1LeftAtType1





T = TypeVar("T", bound="TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1")



@_attrs_define
class TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1:
    """ 
        Attributes:
            status (TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1Status):
            left_at (Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1LeftAtType0',
                'TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1LeftAtType1', None, Unset]):
     """

    status: TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1Status
    left_at: Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1LeftAtType0', 'TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1LeftAtType1', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_1_left_at_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1LeftAtType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_1_left_at_type_1 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1LeftAtType1
        status = self.status.value

        left_at: Union[None, Unset, dict[str, Any]]
        if isinstance(self.left_at, Unset):
            left_at = UNSET
        elif isinstance(self.left_at, TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1LeftAtType0):
            left_at = self.left_at.to_dict()
        elif isinstance(self.left_at, TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1LeftAtType1):
            left_at = self.left_at.to_dict()
        else:
            left_at = self.left_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
        })
        if left_at is not UNSET:
            field_dict["leftAt"] = left_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_1_left_at_type_0 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1LeftAtType0
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_1_left_at_type_1 import TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1LeftAtType1
        d = dict(src_dict)
        status = TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1Status(d.pop("status"))




        def _parse_left_at(data: object) -> Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1LeftAtType0', 'TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1LeftAtType1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                left_at_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1LeftAtType0.from_dict(data)



                return left_at_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                left_at_type_1 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1LeftAtType1.from_dict(data)



                return left_at_type_1
            except: # noqa: E722
                pass
            return cast(Union['TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1LeftAtType0', 'TextToCombinedSearchResponse200OutputProfileSearchParamsType0JobStatusType1LeftAtType1', None, Unset], data)

        left_at = _parse_left_at(d.pop("leftAt", UNSET))


        text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_1 = cls(
            status=status,
            left_at=left_at,
        )


        text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_1.additional_properties = d
        return text_to_combined_search_response_200_output_profile_search_params_type_0_job_status_type_1

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
