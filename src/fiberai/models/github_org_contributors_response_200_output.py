from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GithubOrgContributorsResponse200Output")


@_attrs_define
class GithubOrgContributorsResponse200Output:
    """
    Attributes:
        run_id (str): Identifier to pass when polling for this scan.
        repos_selected (float): Public non-fork repositories selected for this scan. This is the billed quantity.
    """

    run_id: str
    repos_selected: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        repos_selected = self.repos_selected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runId": run_id,
                "reposSelected": repos_selected,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("runId")

        repos_selected = d.pop("reposSelected")

        github_org_contributors_response_200_output = cls(
            run_id=run_id,
            repos_selected=repos_selected,
        )

        github_org_contributors_response_200_output.additional_properties = d
        return github_org_contributors_response_200_output

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
