from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.start_local_business_search_body_data_item_type_1_source import StartLocalBusinessSearchBodyDataItemType1Source
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="StartLocalBusinessSearchBodyDataItemType1")



@_attrs_define
class StartLocalBusinessSearchBodyDataItemType1:
    """ 
        Attributes:
            source (StartLocalBusinessSearchBodyDataItemType1Source):
            place_id (Union[None, Unset, str]): Google Maps place ID of the business like ChIJFeu5p7alIIYRQIdohzciYLI. Only
                recommended if you previously did a google maps search on Fiber UI before with this place id
     """

    source: StartLocalBusinessSearchBodyDataItemType1Source
    place_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        source = self.source.value

        place_id: Union[None, Unset, str]
        if isinstance(self.place_id, Unset):
            place_id = UNSET
        else:
            place_id = self.place_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "source": source,
        })
        if place_id is not UNSET:
            field_dict["placeId"] = place_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = StartLocalBusinessSearchBodyDataItemType1Source(d.pop("source"))




        def _parse_place_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        place_id = _parse_place_id(d.pop("placeId", UNSET))


        start_local_business_search_body_data_item_type_1 = cls(
            source=source,
            place_id=place_id,
        )


        start_local_business_search_body_data_item_type_1.additional_properties = d
        return start_local_business_search_body_data_item_type_1

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
