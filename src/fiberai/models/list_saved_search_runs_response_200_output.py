from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.list_saved_search_runs_response_200_output_runs_item import ListSavedSearchRunsResponse200OutputRunsItem





T = TypeVar("T", bound="ListSavedSearchRunsResponse200Output")



@_attrs_define
class ListSavedSearchRunsResponse200Output:
    """ 
        Attributes:
            runs (list['ListSavedSearchRunsResponse200OutputRunsItem']): The runs of the saved search
            next_cursor (Union[None, Unset, str]): The next cursor. You can call this endpoint again with this cursor to get
                the next page of results. If null, there are no more results.
     """

    runs: list['ListSavedSearchRunsResponse200OutputRunsItem']
    next_cursor: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_saved_search_runs_response_200_output_runs_item import ListSavedSearchRunsResponse200OutputRunsItem
        runs = []
        for runs_item_data in self.runs:
            runs_item = runs_item_data.to_dict()
            runs.append(runs_item)



        next_cursor: Union[None, Unset, str]
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "runs": runs,
        })
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_saved_search_runs_response_200_output_runs_item import ListSavedSearchRunsResponse200OutputRunsItem
        d = dict(src_dict)
        runs = []
        _runs = d.pop("runs")
        for runs_item_data in (_runs):
            runs_item = ListSavedSearchRunsResponse200OutputRunsItem.from_dict(runs_item_data)



            runs.append(runs_item)


        def _parse_next_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))


        list_saved_search_runs_response_200_output = cls(
            runs=runs,
            next_cursor=next_cursor,
        )


        list_saved_search_runs_response_200_output.additional_properties = d
        return list_saved_search_runs_response_200_output

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
