from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.start_batch_live_enrich_response_200_output_type import StartBatchLiveEnrichResponse200OutputType

T = TypeVar("T", bound="StartBatchLiveEnrichResponse200Output")


@_attrs_define
class StartBatchLiveEnrichResponse200Output:
    """
    Attributes:
        task_id (str): Use this ID to poll for progress via the poll endpoint.
        type_ (StartBatchLiveEnrichResponse200OutputType):
        num_identifiers_enqueued (int): Number of unique identifiers queued for enrichment
        num_duplicates_skipped (int): Number of duplicate identifiers skipped.
        num_malformed (int): Number of identifiers that could not be parsed. numIdentifiersEnqueued +
            numDuplicatesSkipped + numMalformed = length of your input.
    """

    task_id: str
    type_: StartBatchLiveEnrichResponse200OutputType
    num_identifiers_enqueued: int
    num_duplicates_skipped: int
    num_malformed: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        type_ = self.type_.value

        num_identifiers_enqueued = self.num_identifiers_enqueued

        num_duplicates_skipped = self.num_duplicates_skipped

        num_malformed = self.num_malformed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "taskId": task_id,
                "type": type_,
                "numIdentifiersEnqueued": num_identifiers_enqueued,
                "numDuplicatesSkipped": num_duplicates_skipped,
                "numMalformed": num_malformed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_id = d.pop("taskId")

        type_ = StartBatchLiveEnrichResponse200OutputType(d.pop("type"))

        num_identifiers_enqueued = d.pop("numIdentifiersEnqueued")

        num_duplicates_skipped = d.pop("numDuplicatesSkipped")

        num_malformed = d.pop("numMalformed")

        start_batch_live_enrich_response_200_output = cls(
            task_id=task_id,
            type_=type_,
            num_identifiers_enqueued=num_identifiers_enqueued,
            num_duplicates_skipped=num_duplicates_skipped,
            num_malformed=num_malformed,
        )

        start_batch_live_enrich_response_200_output.additional_properties = d
        return start_batch_live_enrich_response_200_output

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
