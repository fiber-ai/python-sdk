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
  from ..models.post_comments_live_fetch_response_200_output_data_item import PostCommentsLiveFetchResponse200OutputDataItem





T = TypeVar("T", bound="PostCommentsLiveFetchResponse200Output")



@_attrs_define
class PostCommentsLiveFetchResponse200Output:
    """ 
        Attributes:
            data (list['PostCommentsLiveFetchResponse200OutputDataItem']):
            cursor (Union[None, Unset, str]):
     """

    data: list['PostCommentsLiveFetchResponse200OutputDataItem']
    cursor: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_comments_live_fetch_response_200_output_data_item import PostCommentsLiveFetchResponse200OutputDataItem
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        cursor: Union[None, Unset, str]
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data": data,
        })
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_comments_live_fetch_response_200_output_data_item import PostCommentsLiveFetchResponse200OutputDataItem
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = PostCommentsLiveFetchResponse200OutputDataItem.from_dict(data_item_data)



            data.append(data_item)


        def _parse_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))


        post_comments_live_fetch_response_200_output = cls(
            data=data,
            cursor=cursor,
        )


        post_comments_live_fetch_response_200_output.additional_properties = d
        return post_comments_live_fetch_response_200_output

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
