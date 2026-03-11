from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GithubToLinkedInTriggerResponse200Output")


@_attrs_define
class GithubToLinkedInTriggerResponse200Output:
    """
    Attributes:
        github_agent_run_id (str): The ID of the GitHub to LinkedIn lookup run. Provide this to the polling endpoint to
            get actual results back.
    """

    github_agent_run_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        github_agent_run_id = self.github_agent_run_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "githubAgentRunId": github_agent_run_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        github_agent_run_id = d.pop("githubAgentRunId")

        github_to_linked_in_trigger_response_200_output = cls(
            github_agent_run_id=github_agent_run_id,
        )

        github_to_linked_in_trigger_response_200_output.additional_properties = d
        return github_to_linked_in_trigger_response_200_output

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
