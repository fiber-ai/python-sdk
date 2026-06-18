from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateSavedSearchResponse200Output")


@_attrs_define
class UpdateSavedSearchResponse200Output:
    """
    Attributes:
        success (bool): Whether the update was successful.
        id (str): The ID of the saved search.
        name (str): The name of the saved search.
        spawn_frequency_days (int): The frequency of the saved search in days. Minimum is 7 days.
        is_active (bool): Whether the saved search is active.
    """

    success: bool
    id: str
    name: str
    spawn_frequency_days: int
    is_active: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        id = self.id

        name = self.name

        spawn_frequency_days = self.spawn_frequency_days

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "id": id,
                "name": name,
                "spawnFrequencyDays": spawn_frequency_days,
                "isActive": is_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        id = d.pop("id")

        name = d.pop("name")

        spawn_frequency_days = d.pop("spawnFrequencyDays")

        is_active = d.pop("isActive")

        update_saved_search_response_200_output = cls(
            success=success,
            id=id,
            name=name,
            spawn_frequency_days=spawn_frequency_days,
            is_active=is_active,
        )

        update_saved_search_response_200_output.additional_properties = d
        return update_saved_search_response_200_output

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
