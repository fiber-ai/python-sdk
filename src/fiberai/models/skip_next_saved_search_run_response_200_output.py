from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SkipNextSavedSearchRunResponse200Output")


@_attrs_define
class SkipNextSavedSearchRunResponse200Output:
    """
    Attributes:
        id (str): The saved search ID
        skip_until (str): The date until which auto-runs are suppressed. After this date passes, the saved search
            resumes its normal schedule.
    """

    id: str
    skip_until: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        skip_until = self.skip_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "skipUntil": skip_until,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        skip_until = d.pop("skipUntil")

        skip_next_saved_search_run_response_200_output = cls(
            id=id,
            skip_until=skip_until,
        )

        skip_next_saved_search_run_response_200_output.additional_properties = d
        return skip_next_saved_search_run_response_200_output

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
