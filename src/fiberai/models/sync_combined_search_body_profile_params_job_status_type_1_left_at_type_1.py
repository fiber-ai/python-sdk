from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sync_combined_search_body_profile_params_job_status_type_1_left_at_type_1_strategy import SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1Strategy
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.sync_combined_search_body_profile_params_job_status_type_1_left_at_type_1_window_type_0 import SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType0
  from ..models.sync_combined_search_body_profile_params_job_status_type_1_left_at_type_1_window_type_1 import SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType1
  from ..models.sync_combined_search_body_profile_params_job_status_type_1_left_at_type_1_window_type_2 import SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType2





T = TypeVar("T", bound="SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1")



@_attrs_define
class SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1:
    """ 
        Attributes:
            strategy (SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1Strategy):
            window (Union['SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType0',
                'SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType1',
                'SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType2', None, Unset]):
     """

    strategy: SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1Strategy
    window: Union['SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType0', 'SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType1', 'SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType2', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_combined_search_body_profile_params_job_status_type_1_left_at_type_1_window_type_0 import SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType0
        from ..models.sync_combined_search_body_profile_params_job_status_type_1_left_at_type_1_window_type_1 import SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType1
        from ..models.sync_combined_search_body_profile_params_job_status_type_1_left_at_type_1_window_type_2 import SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType2
        strategy = self.strategy.value

        window: Union[None, Unset, dict[str, Any]]
        if isinstance(self.window, Unset):
            window = UNSET
        elif isinstance(self.window, SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType0):
            window = self.window.to_dict()
        elif isinstance(self.window, SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType1):
            window = self.window.to_dict()
        elif isinstance(self.window, SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType2):
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
        from ..models.sync_combined_search_body_profile_params_job_status_type_1_left_at_type_1_window_type_0 import SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType0
        from ..models.sync_combined_search_body_profile_params_job_status_type_1_left_at_type_1_window_type_1 import SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType1
        from ..models.sync_combined_search_body_profile_params_job_status_type_1_left_at_type_1_window_type_2 import SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType2
        d = dict(src_dict)
        strategy = SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1Strategy(d.pop("strategy"))




        def _parse_window(data: object) -> Union['SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType0', 'SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType1', 'SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType2', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_0 = SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType0.from_dict(data)



                return window_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_1 = SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType1.from_dict(data)



                return window_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_2 = SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType2.from_dict(data)



                return window_type_2
            except: # noqa: E722
                pass
            return cast(Union['SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType0', 'SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType1', 'SyncCombinedSearchBodyProfileParamsJobStatusType1LeftAtType1WindowType2', None, Unset], data)

        window = _parse_window(d.pop("window", UNSET))


        sync_combined_search_body_profile_params_job_status_type_1_left_at_type_1 = cls(
            strategy=strategy,
            window=window,
        )


        sync_combined_search_body_profile_params_job_status_type_1_left_at_type_1.additional_properties = d
        return sync_combined_search_body_profile_params_job_status_type_1_left_at_type_1

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
