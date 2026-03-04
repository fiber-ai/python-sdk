from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetSavedSearchRunStatusResponse200OutputRunPeopleStats")



@_attrs_define
class GetSavedSearchRunStatusResponse200OutputRunPeopleStats:
    """ The people stats. This includes the number of people joined, departed, stayed, and returned so far.

        Attributes:
            num_people_joined (float): The number of people joined which means people who appeared in the search results for
                the first time
            num_people_departed (float): The number of people departed which means people who appeared in the search results
                previously and then disappeared in the latest search results
            num_people_returned (float): The number of people returned which means people who appeared in the search results
                previously but departed and then appeared again in the latest search results
            num_people_stayed (float): The number of people stayed which means people who appeared in the search results
                previously and then stayed in the latest search results
     """

    num_people_joined: float
    num_people_departed: float
    num_people_returned: float
    num_people_stayed: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        num_people_joined = self.num_people_joined

        num_people_departed = self.num_people_departed

        num_people_returned = self.num_people_returned

        num_people_stayed = self.num_people_stayed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "numPeopleJoined": num_people_joined,
            "numPeopleDeparted": num_people_departed,
            "numPeopleReturned": num_people_returned,
            "numPeopleStayed": num_people_stayed,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        num_people_joined = d.pop("numPeopleJoined")

        num_people_departed = d.pop("numPeopleDeparted")

        num_people_returned = d.pop("numPeopleReturned")

        num_people_stayed = d.pop("numPeopleStayed")

        get_saved_search_run_status_response_200_output_run_people_stats = cls(
            num_people_joined=num_people_joined,
            num_people_departed=num_people_departed,
            num_people_returned=num_people_returned,
            num_people_stayed=num_people_stayed,
        )


        get_saved_search_run_status_response_200_output_run_people_stats.additional_properties = d
        return get_saved_search_run_status_response_200_output_run_people_stats

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
