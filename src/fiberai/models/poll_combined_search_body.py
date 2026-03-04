from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.poll_combined_search_body_entity_type import PollCombinedSearchBodyEntityType
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PollCombinedSearchBody")



@_attrs_define
class PollCombinedSearchBody:
    """ 
        Attributes:
            api_key (str): Your Fiber API key
            entity_type (PollCombinedSearchBodyEntityType): Whether you want to find the companies or profiles that your
                search returned. Profiles returned works on the companies that are saved with given search criteria
            search_id (str): The search id returned by the combined search endpoint
            cursor (Union[None, Unset, str]): An optional cursor to start the pagination from
            page_size (Union[Unset, int]): The number of items to return on this page Default: 25.
     """

    api_key: str
    entity_type: PollCombinedSearchBodyEntityType
    search_id: str
    cursor: Union[None, Unset, str] = UNSET
    page_size: Union[Unset, int] = 25
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        entity_type = self.entity_type.value

        search_id = self.search_id

        cursor: Union[None, Unset, str]
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        page_size = self.page_size


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
            "entityType": entity_type,
            "searchId": search_id,
        })
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        entity_type = PollCombinedSearchBodyEntityType(d.pop("entityType"))




        search_id = d.pop("searchId")

        def _parse_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))


        page_size = d.pop("pageSize", UNSET)

        poll_combined_search_body = cls(
            api_key=api_key,
            entity_type=entity_type,
            search_id=search_id,
            cursor=cursor,
            page_size=page_size,
        )


        poll_combined_search_body.additional_properties = d
        return poll_combined_search_body

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
