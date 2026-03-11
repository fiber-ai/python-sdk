from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubToLinkedInTriggerBodyPeopleItem")


@_attrs_define
class GithubToLinkedInTriggerBodyPeopleItem:
    """
    Attributes:
        github_username (str):
        customer_provided_id (None | str | Unset):
    """

    github_username: str
    customer_provided_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        github_username = self.github_username

        customer_provided_id: None | str | Unset
        if isinstance(self.customer_provided_id, Unset):
            customer_provided_id = UNSET
        else:
            customer_provided_id = self.customer_provided_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "githubUsername": github_username,
            }
        )
        if customer_provided_id is not UNSET:
            field_dict["customerProvidedId"] = customer_provided_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        github_username = d.pop("githubUsername")

        def _parse_customer_provided_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_provided_id = _parse_customer_provided_id(d.pop("customerProvidedId", UNSET))

        github_to_linked_in_trigger_body_people_item = cls(
            github_username=github_username,
            customer_provided_id=customer_provided_id,
        )

        github_to_linked_in_trigger_body_people_item.additional_properties = d
        return github_to_linked_in_trigger_body_people_item

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
