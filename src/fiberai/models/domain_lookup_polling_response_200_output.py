from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.domain_lookup_polling_response_200_output_status import DomainLookupPollingResponse200OutputStatus
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.domain_lookup_polling_response_200_output_data_item import DomainLookupPollingResponse200OutputDataItem





T = TypeVar("T", bound="DomainLookupPollingResponse200Output")



@_attrs_define
class DomainLookupPollingResponse200Output:
    """ 
        Attributes:
            status (DomainLookupPollingResponse200OutputStatus):
            data (list['DomainLookupPollingResponse200OutputDataItem']): The list of companies found along with their
                rationale and confidence scores
            has_more (bool): Whether there are more results to fetch
            next_cursor (Union[None, Unset, str]): The cursor to the next page of results. Provide this to the polling
                endpoint to get the next page of results - null if there are no more results.
     """

    status: DomainLookupPollingResponse200OutputStatus
    data: list['DomainLookupPollingResponse200OutputDataItem']
    has_more: bool
    next_cursor: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.domain_lookup_polling_response_200_output_data_item import DomainLookupPollingResponse200OutputDataItem
        status = self.status.value

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        has_more = self.has_more

        next_cursor: Union[None, Unset, str]
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "data": data,
            "hasMore": has_more,
        })
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domain_lookup_polling_response_200_output_data_item import DomainLookupPollingResponse200OutputDataItem
        d = dict(src_dict)
        status = DomainLookupPollingResponse200OutputStatus(d.pop("status"))




        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = DomainLookupPollingResponse200OutputDataItem.from_dict(data_item_data)



            data.append(data_item)


        has_more = d.pop("hasMore")

        def _parse_next_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))


        domain_lookup_polling_response_200_output = cls(
            status=status,
            data=data,
            has_more=has_more,
            next_cursor=next_cursor,
        )


        domain_lookup_polling_response_200_output.additional_properties = d
        return domain_lookup_polling_response_200_output

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
