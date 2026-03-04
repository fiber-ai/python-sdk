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
  from ..models.get_saved_search_run_profiles_response_200_output_profiles_item import GetSavedSearchRunProfilesResponse200OutputProfilesItem





T = TypeVar("T", bound="GetSavedSearchRunProfilesResponse200Output")



@_attrs_define
class GetSavedSearchRunProfilesResponse200Output:
    """ 
        Attributes:
            profiles (list['GetSavedSearchRunProfilesResponse200OutputProfilesItem']): The profiles found for the saved
                search run
            next_cursor (Union[None, Unset, str]): The next cursor
     """

    profiles: list['GetSavedSearchRunProfilesResponse200OutputProfilesItem']
    next_cursor: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_saved_search_run_profiles_response_200_output_profiles_item import GetSavedSearchRunProfilesResponse200OutputProfilesItem
        profiles = []
        for profiles_item_data in self.profiles:
            profiles_item = profiles_item_data.to_dict()
            profiles.append(profiles_item)



        next_cursor: Union[None, Unset, str]
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "profiles": profiles,
        })
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_saved_search_run_profiles_response_200_output_profiles_item import GetSavedSearchRunProfilesResponse200OutputProfilesItem
        d = dict(src_dict)
        profiles = []
        _profiles = d.pop("profiles")
        for profiles_item_data in (_profiles):
            profiles_item = GetSavedSearchRunProfilesResponse200OutputProfilesItem.from_dict(profiles_item_data)



            profiles.append(profiles_item)


        def _parse_next_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))


        get_saved_search_run_profiles_response_200_output = cls(
            profiles=profiles,
            next_cursor=next_cursor,
        )


        get_saved_search_run_profiles_response_200_output.additional_properties = d
        return get_saved_search_run_profiles_response_200_output

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
