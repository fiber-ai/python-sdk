from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubOrgContributorsPollResponse200OutputProgress")


@_attrs_define
class GithubOrgContributorsPollResponse200OutputProgress:
    """
    Attributes:
        scanned_repo_count (float): Repositories whose contributors were collected.
        failed_repo_count (float): Repositories that could not be scanned.
        total_repo_count (float | None | Unset): Public non-fork repositories selected for this scan.
    """

    scanned_repo_count: float
    failed_repo_count: float
    total_repo_count: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scanned_repo_count = self.scanned_repo_count

        failed_repo_count = self.failed_repo_count

        total_repo_count: float | None | Unset
        if isinstance(self.total_repo_count, Unset):
            total_repo_count = UNSET
        else:
            total_repo_count = self.total_repo_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scannedRepoCount": scanned_repo_count,
                "failedRepoCount": failed_repo_count,
            }
        )
        if total_repo_count is not UNSET:
            field_dict["totalRepoCount"] = total_repo_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scanned_repo_count = d.pop("scannedRepoCount")

        failed_repo_count = d.pop("failedRepoCount")

        def _parse_total_repo_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_repo_count = _parse_total_repo_count(d.pop("totalRepoCount", UNSET))

        github_org_contributors_poll_response_200_output_progress = cls(
            scanned_repo_count=scanned_repo_count,
            failed_repo_count=failed_repo_count,
            total_repo_count=total_repo_count,
        )

        github_org_contributors_poll_response_200_output_progress.additional_properties = d
        return github_org_contributors_poll_response_200_output_progress

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
