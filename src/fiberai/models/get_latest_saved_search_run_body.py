from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetLatestSavedSearchRunBody")



@_attrs_define
class GetLatestSavedSearchRunBody:
    """ 
        Attributes:
            api_key (str): Your Fiber API key
            saved_search_id (str): The ID of the saved search
     """

    api_key: str
    saved_search_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        saved_search_id = self.saved_search_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
            "savedSearchId": saved_search_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        saved_search_id = d.pop("savedSearchId")

        get_latest_saved_search_run_body = cls(
            api_key=api_key,
            saved_search_id=saved_search_id,
        )


        get_latest_saved_search_run_body.additional_properties = d
        return get_latest_saved_search_run_body

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
