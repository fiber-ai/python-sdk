from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.remove_tracker_people_body_people_item import RemoveTrackerPeopleBodyPeopleItem


T = TypeVar("T", bound="RemoveTrackerPeopleBody")


@_attrs_define
class RemoveTrackerPeopleBody:
    """
    Attributes:
        people (list[RemoveTrackerPeopleBodyPeopleItem]): People to remove. Uses the same identifier format as add-
            people.
    """

    people: list[RemoveTrackerPeopleBodyPeopleItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        people = []
        for people_item_data in self.people:
            people_item = people_item_data.to_dict()
            people.append(people_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "people": people,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.remove_tracker_people_body_people_item import RemoveTrackerPeopleBodyPeopleItem  # noqa: PLC0415

        d = dict(src_dict)
        people = []
        _people = d.pop("people")
        for people_item_data in _people:
            people_item = RemoveTrackerPeopleBodyPeopleItem.from_dict(people_item_data)

            people.append(people_item)

        remove_tracker_people_body = cls(
            people=people,
        )

        remove_tracker_people_body.additional_properties = d
        return remove_tracker_people_body

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
