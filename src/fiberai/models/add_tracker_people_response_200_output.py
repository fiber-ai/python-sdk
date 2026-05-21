from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.add_tracker_people_response_200_output_invalid_people_item import (
        AddTrackerPeopleResponse200OutputInvalidPeopleItem,
    )


T = TypeVar("T", bound="AddTrackerPeopleResponse200Output")


@_attrs_define
class AddTrackerPeopleResponse200Output:
    """
    Attributes:
        added (int): Number of people successfully added
        skipped (int): Number skipped (duplicates or invalid)
        invalid_people (list[AddTrackerPeopleResponse200OutputInvalidPeopleItem]): Details on any people that could not
            be added
    """

    added: int
    skipped: int
    invalid_people: list[AddTrackerPeopleResponse200OutputInvalidPeopleItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added = self.added

        skipped = self.skipped

        invalid_people = []
        for invalid_people_item_data in self.invalid_people:
            invalid_people_item = invalid_people_item_data.to_dict()
            invalid_people.append(invalid_people_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "added": added,
                "skipped": skipped,
                "invalidPeople": invalid_people,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_tracker_people_response_200_output_invalid_people_item import (
            AddTrackerPeopleResponse200OutputInvalidPeopleItem,
        )

        d = dict(src_dict)
        added = d.pop("added")

        skipped = d.pop("skipped")

        invalid_people = []
        _invalid_people = d.pop("invalidPeople")
        for invalid_people_item_data in _invalid_people:
            invalid_people_item = AddTrackerPeopleResponse200OutputInvalidPeopleItem.from_dict(invalid_people_item_data)

            invalid_people.append(invalid_people_item)

        add_tracker_people_response_200_output = cls(
            added=added,
            skipped=skipped,
            invalid_people=invalid_people,
        )

        add_tracker_people_response_200_output.additional_properties = d
        return add_tracker_people_response_200_output

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
