from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PollBatchContactEnrichmentBody")



@_attrs_define
class PollBatchContactEnrichmentBody:
    """ 
        Attributes:
            api_key (str): Your Fiber API key
            task_id (str): The task ID from the start endpoint response
            cursor (Union[None, Unset, str]): The cursor from the previous poll response. Omit this if you are polling for
                the first time.
            take (Union[Unset, int]): Number of people to take per batch. Default is 100 Default: 100.
     """

    api_key: str
    task_id: str
    cursor: Union[None, Unset, str] = UNSET
    take: Union[Unset, int] = 100
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        task_id = self.task_id

        cursor: Union[None, Unset, str]
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        take = self.take


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
            "taskId": task_id,
        })
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if take is not UNSET:
            field_dict["take"] = take

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        task_id = d.pop("taskId")

        def _parse_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))


        take = d.pop("take", UNSET)

        poll_batch_contact_enrichment_body = cls(
            api_key=api_key,
            task_id=task_id,
            cursor=cursor,
            take=take,
        )


        poll_batch_contact_enrichment_body.additional_properties = d
        return poll_batch_contact_enrichment_body

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
