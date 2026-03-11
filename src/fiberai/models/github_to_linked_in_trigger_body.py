from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_to_linked_in_trigger_body_output_type import GithubToLinkedInTriggerBodyOutputType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_to_linked_in_trigger_body_people_item import GithubToLinkedInTriggerBodyPeopleItem


T = TypeVar("T", bound="GithubToLinkedInTriggerBody")


@_attrs_define
class GithubToLinkedInTriggerBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        people (list[GithubToLinkedInTriggerBodyPeopleItem]): List of GitHub usernames to look up. Maximum 1000 people
            can be provided at a time.
        overall_context (None | str | Unset): Descriptor of what your people have in common and who they are. For
            example: "Engineers at Fiber AI" or "YC founders 2021 batch." Helps our agent disambiguate people with similar
            names.
        output_type (GithubToLinkedInTriggerBodyOutputType | Unset): What to extract from GitHub profile. 'linkedin'
            finds LinkedIn profile, 'email' extracts work emails from commits, 'both' returns both. Default:
            GithubToLinkedInTriggerBodyOutputType.LINKEDIN.
    """

    api_key: str
    people: list[GithubToLinkedInTriggerBodyPeopleItem]
    overall_context: None | str | Unset = UNSET
    output_type: GithubToLinkedInTriggerBodyOutputType | Unset = GithubToLinkedInTriggerBodyOutputType.LINKEDIN
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        people = []
        for people_item_data in self.people:
            people_item = people_item_data.to_dict()
            people.append(people_item)

        overall_context: None | str | Unset
        if isinstance(self.overall_context, Unset):
            overall_context = UNSET
        else:
            overall_context = self.overall_context

        output_type: str | Unset = UNSET
        if not isinstance(self.output_type, Unset):
            output_type = self.output_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "people": people,
            }
        )
        if overall_context is not UNSET:
            field_dict["overallContext"] = overall_context
        if output_type is not UNSET:
            field_dict["outputType"] = output_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_to_linked_in_trigger_body_people_item import GithubToLinkedInTriggerBodyPeopleItem

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        people = []
        _people = d.pop("people")
        for people_item_data in _people:
            people_item = GithubToLinkedInTriggerBodyPeopleItem.from_dict(people_item_data)

            people.append(people_item)

        def _parse_overall_context(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overall_context = _parse_overall_context(d.pop("overallContext", UNSET))

        _output_type = d.pop("outputType", UNSET)
        output_type: GithubToLinkedInTriggerBodyOutputType | Unset
        if isinstance(_output_type, Unset):
            output_type = UNSET
        else:
            output_type = GithubToLinkedInTriggerBodyOutputType(_output_type)

        github_to_linked_in_trigger_body = cls(
            api_key=api_key,
            people=people,
            overall_context=overall_context,
            output_type=output_type,
        )

        github_to_linked_in_trigger_body.additional_properties = d
        return github_to_linked_in_trigger_body

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
