from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.text_to_profile_search_params_response_200_output_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_1_strategy import TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1Strategy
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.text_to_profile_search_params_response_200_output_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_1_window_type_2 import TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType2
  from ..models.text_to_profile_search_params_response_200_output_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_1_window_type_1 import TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType1
  from ..models.text_to_profile_search_params_response_200_output_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_1_window_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType0





T = TypeVar("T", bound="TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1")



@_attrs_define
class TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1:
    """ 
        Attributes:
            strategy (TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType
                1Strategy):
            window (Union['TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolA
                tType1WindowType0', 'TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedS
                choolAtType1WindowType1', 'TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFin
                ishedSchoolAtType1WindowType2', None, Unset]):
     """

    strategy: TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1Strategy
    window: Union['TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType0', 'TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType1', 'TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType2', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_profile_search_params_response_200_output_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_1_window_type_2 import TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType2
        from ..models.text_to_profile_search_params_response_200_output_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_1_window_type_1 import TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType1
        from ..models.text_to_profile_search_params_response_200_output_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_1_window_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType0
        strategy = self.strategy.value

        window: Union[None, Unset, dict[str, Any]]
        if isinstance(self.window, Unset):
            window = UNSET
        elif isinstance(self.window, TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType0):
            window = self.window.to_dict()
        elif isinstance(self.window, TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType1):
            window = self.window.to_dict()
        elif isinstance(self.window, TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType2):
            window = self.window.to_dict()
        else:
            window = self.window


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "strategy": strategy,
        })
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_profile_search_params_response_200_output_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_1_window_type_2 import TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType2
        from ..models.text_to_profile_search_params_response_200_output_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_1_window_type_1 import TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType1
        from ..models.text_to_profile_search_params_response_200_output_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_1_window_type_0 import TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType0
        d = dict(src_dict)
        strategy = TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1Strategy(d.pop("strategy"))




        def _parse_window(data: object) -> Union['TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType0', 'TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType1', 'TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType2', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType0.from_dict(data)



                return window_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_1 = TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType1.from_dict(data)



                return window_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_2 = TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType2.from_dict(data)



                return window_type_2
            except: # noqa: E722
                pass
            return cast(Union['TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType0', 'TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType1', 'TextToProfileSearchParamsResponse200OutputSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType2', None, Unset], data)

        window = _parse_window(d.pop("window", UNSET))


        text_to_profile_search_params_response_200_output_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_1 = cls(
            strategy=strategy,
            window=window,
        )


        text_to_profile_search_params_response_200_output_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_1.additional_properties = d
        return text_to_profile_search_params_response_200_output_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_1

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
