from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_saved_search_run_status_response_200_output_run import GetSavedSearchRunStatusResponse200OutputRun





T = TypeVar("T", bound="GetSavedSearchRunStatusResponse200Output")



@_attrs_define
class GetSavedSearchRunStatusResponse200Output:
    """ 
        Attributes:
            run (GetSavedSearchRunStatusResponse200OutputRun): The saved search run details
     """

    run: 'GetSavedSearchRunStatusResponse200OutputRun'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_saved_search_run_status_response_200_output_run import GetSavedSearchRunStatusResponse200OutputRun
        run = self.run.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "run": run,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_saved_search_run_status_response_200_output_run import GetSavedSearchRunStatusResponse200OutputRun
        d = dict(src_dict)
        run = GetSavedSearchRunStatusResponse200OutputRun.from_dict(d.pop("run"))




        get_saved_search_run_status_response_200_output = cls(
            run=run,
        )


        get_saved_search_run_status_response_200_output.additional_properties = d
        return get_saved_search_run_status_response_200_output

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
