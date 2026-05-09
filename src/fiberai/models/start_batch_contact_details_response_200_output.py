from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartBatchContactDetailsResponse200Output")


@_attrs_define
class StartBatchContactDetailsResponse200Output:
    """
    Attributes:
        task_id (str): The task ID. Use this to poll for results.
        num_people_enqueued (int): The total number of people queued for enrichment.
        num_duplicates_skipped (int | None | Unset): The number of duplicate people found in the input list. Duplicates
            are skipped and not charged.
    """

    task_id: str
    num_people_enqueued: int
    num_duplicates_skipped: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        num_people_enqueued = self.num_people_enqueued

        num_duplicates_skipped: int | None | Unset
        if isinstance(self.num_duplicates_skipped, Unset):
            num_duplicates_skipped = UNSET
        else:
            num_duplicates_skipped = self.num_duplicates_skipped

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "taskId": task_id,
                "numPeopleEnqueued": num_people_enqueued,
            }
        )
        if num_duplicates_skipped is not UNSET:
            field_dict["numDuplicatesSkipped"] = num_duplicates_skipped

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_id = d.pop("taskId")

        num_people_enqueued = d.pop("numPeopleEnqueued")

        def _parse_num_duplicates_skipped(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_duplicates_skipped = _parse_num_duplicates_skipped(d.pop("numDuplicatesSkipped", UNSET))

        start_batch_contact_details_response_200_output = cls(
            task_id=task_id,
            num_people_enqueued=num_people_enqueued,
            num_duplicates_skipped=num_duplicates_skipped,
        )

        start_batch_contact_details_response_200_output.additional_properties = d
        return start_batch_contact_details_response_200_output

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
