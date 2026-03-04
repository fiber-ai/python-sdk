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
  from ..models.poll_google_maps_results_response_200_output_results_item import PollGoogleMapsResultsResponse200OutputResultsItem





T = TypeVar("T", bound="PollGoogleMapsResultsResponse200Output")



@_attrs_define
class PollGoogleMapsResultsResponse200Output:
    """ 
        Attributes:
            results (list['PollGoogleMapsResultsResponse200OutputResultsItem']): The results of the search
            next_cursor (Union[None, Unset, str]): The cursor to use to get the next page of results. If this is null, then
                there are no more results to fetch
     """

    results: list['PollGoogleMapsResultsResponse200OutputResultsItem']
    next_cursor: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.poll_google_maps_results_response_200_output_results_item import PollGoogleMapsResultsResponse200OutputResultsItem
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)



        next_cursor: Union[None, Unset, str]
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "results": results,
        })
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_google_maps_results_response_200_output_results_item import PollGoogleMapsResultsResponse200OutputResultsItem
        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in (_results):
            results_item = PollGoogleMapsResultsResponse200OutputResultsItem.from_dict(results_item_data)



            results.append(results_item)


        def _parse_next_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))


        poll_google_maps_results_response_200_output = cls(
            results=results,
            next_cursor=next_cursor,
        )


        poll_google_maps_results_response_200_output.additional_properties = d
        return poll_google_maps_results_response_200_output

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
