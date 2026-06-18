from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SocialMediaLookupBatchTriggerResponse200Output")


@_attrs_define
class SocialMediaLookupBatchTriggerResponse200Output:
    """
    Attributes:
        run_id (str): The ID of this batch run. Provide to the batch polling endpoint to get results.
        num_people_enqueued (int): Number of people enqueued for lookup after deduplication.
        num_duplicates_skipped (int): Number of duplicate people skipped (same LinkedIn profile submitted multiple
            times).
    """

    run_id: str
    num_people_enqueued: int
    num_duplicates_skipped: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        num_people_enqueued = self.num_people_enqueued

        num_duplicates_skipped = self.num_duplicates_skipped

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runId": run_id,
                "numPeopleEnqueued": num_people_enqueued,
                "numDuplicatesSkipped": num_duplicates_skipped,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("runId")

        num_people_enqueued = d.pop("numPeopleEnqueued")

        num_duplicates_skipped = d.pop("numDuplicatesSkipped")

        social_media_lookup_batch_trigger_response_200_output = cls(
            run_id=run_id,
            num_people_enqueued=num_people_enqueued,
            num_duplicates_skipped=num_duplicates_skipped,
        )

        social_media_lookup_batch_trigger_response_200_output.additional_properties = d
        return social_media_lookup_batch_trigger_response_200_output

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
