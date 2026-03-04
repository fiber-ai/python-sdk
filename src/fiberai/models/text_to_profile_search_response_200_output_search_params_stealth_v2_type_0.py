from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.text_to_profile_search_response_200_output_search_params_stealth_v2_type_0_status import TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0Status
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.text_to_profile_search_response_200_output_search_params_stealth_v2_type_0_entered_stealth_at_type_1 import TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0EnteredStealthAtType1
  from ..models.text_to_profile_search_response_200_output_search_params_stealth_v2_type_0_entered_stealth_at_type_0 import TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0EnteredStealthAtType0





T = TypeVar("T", bound="TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0")



@_attrs_define
class TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0:
    """ 
        Attributes:
            status (TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0Status):
            entered_stealth_at (Union['TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0EnteredStealthAtType0',
                'TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0EnteredStealthAtType1', None, Unset]):
     """

    status: TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0Status
    entered_stealth_at: Union['TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0EnteredStealthAtType0', 'TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0EnteredStealthAtType1', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_profile_search_response_200_output_search_params_stealth_v2_type_0_entered_stealth_at_type_1 import TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0EnteredStealthAtType1
        from ..models.text_to_profile_search_response_200_output_search_params_stealth_v2_type_0_entered_stealth_at_type_0 import TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0EnteredStealthAtType0
        status = self.status.value

        entered_stealth_at: Union[None, Unset, dict[str, Any]]
        if isinstance(self.entered_stealth_at, Unset):
            entered_stealth_at = UNSET
        elif isinstance(self.entered_stealth_at, TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0EnteredStealthAtType0):
            entered_stealth_at = self.entered_stealth_at.to_dict()
        elif isinstance(self.entered_stealth_at, TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0EnteredStealthAtType1):
            entered_stealth_at = self.entered_stealth_at.to_dict()
        else:
            entered_stealth_at = self.entered_stealth_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
        })
        if entered_stealth_at is not UNSET:
            field_dict["enteredStealthAt"] = entered_stealth_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_profile_search_response_200_output_search_params_stealth_v2_type_0_entered_stealth_at_type_1 import TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0EnteredStealthAtType1
        from ..models.text_to_profile_search_response_200_output_search_params_stealth_v2_type_0_entered_stealth_at_type_0 import TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0EnteredStealthAtType0
        d = dict(src_dict)
        status = TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0Status(d.pop("status"))




        def _parse_entered_stealth_at(data: object) -> Union['TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0EnteredStealthAtType0', 'TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0EnteredStealthAtType1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entered_stealth_at_type_0 = TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0EnteredStealthAtType0.from_dict(data)



                return entered_stealth_at_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entered_stealth_at_type_1 = TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0EnteredStealthAtType1.from_dict(data)



                return entered_stealth_at_type_1
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0EnteredStealthAtType0', 'TextToProfileSearchResponse200OutputSearchParamsStealthV2Type0EnteredStealthAtType1', None, Unset], data)

        entered_stealth_at = _parse_entered_stealth_at(d.pop("enteredStealthAt", UNSET))


        text_to_profile_search_response_200_output_search_params_stealth_v2_type_0 = cls(
            status=status,
            entered_stealth_at=entered_stealth_at,
        )


        text_to_profile_search_response_200_output_search_params_stealth_v2_type_0.additional_properties = d
        return text_to_profile_search_response_200_output_search_params_stealth_v2_type_0

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
