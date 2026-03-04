from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.reverse_email_lookup_response_200_output_data_item import ReverseEmailLookupResponse200OutputDataItem





T = TypeVar("T", bound="ReverseEmailLookupResponse200Output")



@_attrs_define
class ReverseEmailLookupResponse200Output:
    """ 
        Attributes:
            data (list['ReverseEmailLookupResponse200OutputDataItem']): Array of people found
     """

    data: list['ReverseEmailLookupResponse200OutputDataItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reverse_email_lookup_response_200_output_data_item import ReverseEmailLookupResponse200OutputDataItem
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reverse_email_lookup_response_200_output_data_item import ReverseEmailLookupResponse200OutputDataItem
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = ReverseEmailLookupResponse200OutputDataItem.from_dict(data_item_data)



            data.append(data_item)


        reverse_email_lookup_response_200_output = cls(
            data=data,
        )


        reverse_email_lookup_response_200_output.additional_properties = d
        return reverse_email_lookup_response_200_output

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
