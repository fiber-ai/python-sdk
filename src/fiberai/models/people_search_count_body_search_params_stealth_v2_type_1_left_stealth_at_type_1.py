from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.people_search_count_body_search_params_stealth_v2_type_1_left_stealth_at_type_1_strategy import PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1Strategy
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.people_search_count_body_search_params_stealth_v2_type_1_left_stealth_at_type_1_window_type_1 import PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType1
  from ..models.people_search_count_body_search_params_stealth_v2_type_1_left_stealth_at_type_1_window_type_0 import PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType0
  from ..models.people_search_count_body_search_params_stealth_v2_type_1_left_stealth_at_type_1_window_type_2 import PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType2





T = TypeVar("T", bound="PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1")



@_attrs_define
class PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1:
    """ 
        Attributes:
            strategy (PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1Strategy):
            window (Union['PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType0',
                'PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType1',
                'PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType2', None, Unset]):
     """

    strategy: PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1Strategy
    window: Union['PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType0', 'PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType1', 'PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType2', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.people_search_count_body_search_params_stealth_v2_type_1_left_stealth_at_type_1_window_type_1 import PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType1
        from ..models.people_search_count_body_search_params_stealth_v2_type_1_left_stealth_at_type_1_window_type_0 import PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType0
        from ..models.people_search_count_body_search_params_stealth_v2_type_1_left_stealth_at_type_1_window_type_2 import PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType2
        strategy = self.strategy.value

        window: Union[None, Unset, dict[str, Any]]
        if isinstance(self.window, Unset):
            window = UNSET
        elif isinstance(self.window, PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType0):
            window = self.window.to_dict()
        elif isinstance(self.window, PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType1):
            window = self.window.to_dict()
        elif isinstance(self.window, PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType2):
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
        from ..models.people_search_count_body_search_params_stealth_v2_type_1_left_stealth_at_type_1_window_type_1 import PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType1
        from ..models.people_search_count_body_search_params_stealth_v2_type_1_left_stealth_at_type_1_window_type_0 import PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType0
        from ..models.people_search_count_body_search_params_stealth_v2_type_1_left_stealth_at_type_1_window_type_2 import PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType2
        d = dict(src_dict)
        strategy = PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1Strategy(d.pop("strategy"))




        def _parse_window(data: object) -> Union['PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType0', 'PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType1', 'PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType2', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_0 = PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType0.from_dict(data)



                return window_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_1 = PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType1.from_dict(data)



                return window_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_2 = PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType2.from_dict(data)



                return window_type_2
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType0', 'PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType1', 'PeopleSearchCountBodySearchParamsStealthV2Type1LeftStealthAtType1WindowType2', None, Unset], data)

        window = _parse_window(d.pop("window", UNSET))


        people_search_count_body_search_params_stealth_v2_type_1_left_stealth_at_type_1 = cls(
            strategy=strategy,
            window=window,
        )


        people_search_count_body_search_params_stealth_v2_type_1_left_stealth_at_type_1.additional_properties = d
        return people_search_count_body_search_params_stealth_v2_type_1_left_stealth_at_type_1

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
