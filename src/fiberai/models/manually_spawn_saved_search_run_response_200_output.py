from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ManuallySpawnSavedSearchRunResponse200Output")


@_attrs_define
class ManuallySpawnSavedSearchRunResponse200Output:
    """
    Attributes:
        id (str): The ID of the saved search run
        started_at (str): The date and time the saved search run started
    """

    id: str
    started_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        started_at = self.started_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "startedAt": started_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        started_at = d.pop("startedAt")

        manually_spawn_saved_search_run_response_200_output = cls(
            id=id,
            started_at=started_at,
        )

        manually_spawn_saved_search_run_response_200_output.additional_properties = d
        return manually_spawn_saved_search_run_response_200_output

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
