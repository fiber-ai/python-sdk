from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="StartBatchContactEnrichmentResponse200Output")



@_attrs_define
class StartBatchContactEnrichmentResponse200Output:
    """ 
        Attributes:
            task_id (str): Task ID. Use this to poll for results using the poll endpoint.
            num_people_enqueued (int): Total number of people queued for enrichment
            num_duplicates_skipped (Union[None, Unset, int]): Total number of duplicate people found in your input list.
                These people are skipped, and you aren't charged for them. The number of duplicates and the number of people
                queued should sum up to the length of your original input.
     """

    task_id: str
    num_people_enqueued: int
    num_duplicates_skipped: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        num_people_enqueued = self.num_people_enqueued

        num_duplicates_skipped: Union[None, Unset, int]
        if isinstance(self.num_duplicates_skipped, Unset):
            num_duplicates_skipped = UNSET
        else:
            num_duplicates_skipped = self.num_duplicates_skipped


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "taskId": task_id,
            "numPeopleEnqueued": num_people_enqueued,
        })
        if num_duplicates_skipped is not UNSET:
            field_dict["numDuplicatesSkipped"] = num_duplicates_skipped

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_id = d.pop("taskId")

        num_people_enqueued = d.pop("numPeopleEnqueued")

        def _parse_num_duplicates_skipped(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        num_duplicates_skipped = _parse_num_duplicates_skipped(d.pop("numDuplicatesSkipped", UNSET))


        start_batch_contact_enrichment_response_200_output = cls(
            task_id=task_id,
            num_people_enqueued=num_people_enqueued,
            num_duplicates_skipped=num_duplicates_skipped,
        )


        start_batch_contact_enrichment_response_200_output.additional_properties = d
        return start_batch_contact_enrichment_response_200_output

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
