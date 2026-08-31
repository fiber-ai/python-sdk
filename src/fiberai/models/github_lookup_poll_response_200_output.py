from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_lookup_poll_response_200_output_overall_status import (
    GithubLookupPollResponse200OutputOverallStatus,
)

if TYPE_CHECKING:
    from ..models.github_lookup_poll_response_200_output_counts import GithubLookupPollResponse200OutputCounts
    from ..models.github_lookup_poll_response_200_output_people_item import GithubLookupPollResponse200OutputPeopleItem


T = TypeVar("T", bound="GithubLookupPollResponse200Output")


@_attrs_define
class GithubLookupPollResponse200Output:
    """
    Attributes:
        github_agent_run_id (str): The ID of the GitHub lookup run these results belong to.
        overall_status (GithubLookupPollResponse200OutputOverallStatus): The overall status of the lookup run.
        counts (GithubLookupPollResponse200OutputCounts): Breakdown of lookup progress. All fields sum to the total
            number of people in the run.
        people (list[GithubLookupPollResponse200OutputPeopleItem]): All processed people sorted by outcome (found
            first). Pending people are not included.
    """

    github_agent_run_id: str
    overall_status: GithubLookupPollResponse200OutputOverallStatus
    counts: GithubLookupPollResponse200OutputCounts
    people: list[GithubLookupPollResponse200OutputPeopleItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        github_agent_run_id = self.github_agent_run_id

        overall_status = self.overall_status.value

        counts = self.counts.to_dict()

        people = []
        for people_item_data in self.people:
            people_item = people_item_data.to_dict()
            people.append(people_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "githubAgentRunId": github_agent_run_id,
                "overallStatus": overall_status,
                "counts": counts,
                "people": people,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_lookup_poll_response_200_output_counts import (
            GithubLookupPollResponse200OutputCounts,  # noqa: PLC0415
        )
        from ..models.github_lookup_poll_response_200_output_people_item import (
            GithubLookupPollResponse200OutputPeopleItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        github_agent_run_id = d.pop("githubAgentRunId")

        overall_status = GithubLookupPollResponse200OutputOverallStatus(d.pop("overallStatus"))

        counts = GithubLookupPollResponse200OutputCounts.from_dict(d.pop("counts"))

        people = []
        _people = d.pop("people")
        for people_item_data in _people:
            people_item = GithubLookupPollResponse200OutputPeopleItem.from_dict(people_item_data)

            people.append(people_item)

        github_lookup_poll_response_200_output = cls(
            github_agent_run_id=github_agent_run_id,
            overall_status=overall_status,
            counts=counts,
            people=people,
        )

        github_lookup_poll_response_200_output.additional_properties = d
        return github_lookup_poll_response_200_output

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
