from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="TextToCompanySearchBody")



@_attrs_define
class TextToCompanySearchBody:
    """ 
        Attributes:
            api_key (str): Your Fiber API key
            query (str):
            page_size (Union[Unset, int]): The number of companies to return, if you need to get more results, you can
                paginate. Default: 25.
            cursor (Union[None, Unset, str]): A pagination cursor returned from a previous search response. Use this to
                fetch the next page of results.
     """

    api_key: str
    query: str
    page_size: Union[Unset, int] = 25
    cursor: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        query = self.query

        page_size = self.page_size

        cursor: Union[None, Unset, str]
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
            "query": query,
        })
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        query = d.pop("query")

        page_size = d.pop("pageSize", UNSET)

        def _parse_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))


        text_to_company_search_body = cls(
            api_key=api_key,
            query=query,
            page_size=page_size,
            cursor=cursor,
        )


        text_to_company_search_body.additional_properties = d
        return text_to_company_search_body

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
