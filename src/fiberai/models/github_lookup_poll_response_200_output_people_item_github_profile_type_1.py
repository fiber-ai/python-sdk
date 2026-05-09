from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_lookup_poll_response_200_output_people_item_github_profile_type_1_outcome import (
    GithubLookupPollResponse200OutputPeopleItemGithubProfileType1Outcome,
)

T = TypeVar("T", bound="GithubLookupPollResponse200OutputPeopleItemGithubProfileType1")


@_attrs_define
class GithubLookupPollResponse200OutputPeopleItemGithubProfileType1:
    """
    Attributes:
        outcome (GithubLookupPollResponse200OutputPeopleItemGithubProfileType1Outcome):
        message (str): A user-facing explanation of why no profile was found.
    """

    outcome: GithubLookupPollResponse200OutputPeopleItemGithubProfileType1Outcome
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        outcome = self.outcome.value

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "outcome": outcome,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        outcome = GithubLookupPollResponse200OutputPeopleItemGithubProfileType1Outcome(d.pop("outcome"))

        message = d.pop("message")

        github_lookup_poll_response_200_output_people_item_github_profile_type_1 = cls(
            outcome=outcome,
            message=message,
        )

        github_lookup_poll_response_200_output_people_item_github_profile_type_1.additional_properties = d
        return github_lookup_poll_response_200_output_people_item_github_profile_type_1

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
