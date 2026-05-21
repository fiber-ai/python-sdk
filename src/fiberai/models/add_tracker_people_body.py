from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.add_tracker_people_body_people_item import AddTrackerPeopleBodyPeopleItem


T = TypeVar("T", bound="AddTrackerPeopleBody")


@_attrs_define
class AddTrackerPeopleBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        people (list[AddTrackerPeopleBodyPeopleItem]): People to add. At least one identifier required per person.
    """

    api_key: str
    people: list[AddTrackerPeopleBodyPeopleItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        people = []
        for people_item_data in self.people:
            people_item = people_item_data.to_dict()
            people.append(people_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "people": people,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_tracker_people_body_people_item import AddTrackerPeopleBodyPeopleItem

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        people = []
        _people = d.pop("people")
        for people_item_data in _people:
            people_item = AddTrackerPeopleBodyPeopleItem.from_dict(people_item_data)

            people.append(people_item)

        add_tracker_people_body = cls(
            api_key=api_key,
            people=people,
        )

        add_tracker_people_body.additional_properties = d
        return add_tracker_people_body

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
