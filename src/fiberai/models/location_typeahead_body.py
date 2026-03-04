from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="LocationTypeaheadBody")



@_attrs_define
class LocationTypeaheadBody:
    """ 
        Attributes:
            api_key (str): Your Fiber API key
            query (str): Search query for location. It can be a city name or ZIP/postal code. Can be the complete name ('New
                York') or a prefix ('san fr'). Intentionally doesn't support neighborhoods, street addresses, states, or
                countries.
     """

    api_key: str
    query: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        query = self.query


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
            "query": query,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        query = d.pop("query")

        location_typeahead_body = cls(
            api_key=api_key,
            query=query,
        )


        location_typeahead_body.additional_properties = d
        return location_typeahead_body

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
