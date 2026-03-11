from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.github_lookup_trigger_body_people_item_type_0 import GithubLookupTriggerBodyPeopleItemType0
    from ..models.github_lookup_trigger_body_people_item_type_1 import GithubLookupTriggerBodyPeopleItemType1
    from ..models.github_lookup_trigger_body_people_item_type_2 import GithubLookupTriggerBodyPeopleItemType2


T = TypeVar("T", bound="GithubLookupTriggerBody")


@_attrs_define
class GithubLookupTriggerBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        overall_context (str): Descriptor of what your people have in common and who they are. For example: "Engineers
            at Fiber AI" or "YC founders 2021 batch." Helps our agent disambiguate people with similar names.
        people (list[GithubLookupTriggerBodyPeopleItemType0 | GithubLookupTriggerBodyPeopleItemType1 |
            GithubLookupTriggerBodyPeopleItemType2]): List of people to look up. Maximum 2000 people can be provided at a
            time.
    """

    api_key: str
    overall_context: str
    people: list[
        GithubLookupTriggerBodyPeopleItemType0
        | GithubLookupTriggerBodyPeopleItemType1
        | GithubLookupTriggerBodyPeopleItemType2
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.github_lookup_trigger_body_people_item_type_0 import GithubLookupTriggerBodyPeopleItemType0
        from ..models.github_lookup_trigger_body_people_item_type_1 import GithubLookupTriggerBodyPeopleItemType1

        api_key = self.api_key

        overall_context = self.overall_context

        people = []
        for people_item_data in self.people:
            people_item: dict[str, Any]
            if isinstance(people_item_data, GithubLookupTriggerBodyPeopleItemType0):
                people_item = people_item_data.to_dict()
            elif isinstance(people_item_data, GithubLookupTriggerBodyPeopleItemType1):
                people_item = people_item_data.to_dict()
            else:
                people_item = people_item_data.to_dict()

            people.append(people_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "overallContext": overall_context,
                "people": people,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_lookup_trigger_body_people_item_type_0 import GithubLookupTriggerBodyPeopleItemType0
        from ..models.github_lookup_trigger_body_people_item_type_1 import GithubLookupTriggerBodyPeopleItemType1
        from ..models.github_lookup_trigger_body_people_item_type_2 import GithubLookupTriggerBodyPeopleItemType2

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        overall_context = d.pop("overallContext")

        people = []
        _people = d.pop("people")
        for people_item_data in _people:

            def _parse_people_item(
                data: object,
            ) -> (
                GithubLookupTriggerBodyPeopleItemType0
                | GithubLookupTriggerBodyPeopleItemType1
                | GithubLookupTriggerBodyPeopleItemType2
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    people_item_type_0 = GithubLookupTriggerBodyPeopleItemType0.from_dict(data)

                    return people_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    people_item_type_1 = GithubLookupTriggerBodyPeopleItemType1.from_dict(data)

                    return people_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                people_item_type_2 = GithubLookupTriggerBodyPeopleItemType2.from_dict(data)

                return people_item_type_2

            people_item = _parse_people_item(people_item_data)

            people.append(people_item)

        github_lookup_trigger_body = cls(
            api_key=api_key,
            overall_context=overall_context,
            people=people,
        )

        github_lookup_trigger_body.additional_properties = d
        return github_lookup_trigger_body

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
