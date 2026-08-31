from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_all_job_change_lists_response_200_output_job_changes_lists_item import (
        ListAllJobChangeListsResponse200OutputJobChangesListsItem,
    )


T = TypeVar("T", bound="ListAllJobChangeListsResponse200Output")


@_attrs_define
class ListAllJobChangeListsResponse200Output:
    """
    Attributes:
        job_changes_lists (list[ListAllJobChangeListsResponse200OutputJobChangesListsItem]):
        total_count (float): Total number of job changes lists.
        next_cursor (None | str | Unset): The pagination cursor for the next page. Null if there are no more results.
    """

    job_changes_lists: list[ListAllJobChangeListsResponse200OutputJobChangesListsItem]
    total_count: float
    next_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_changes_lists = []
        for job_changes_lists_item_data in self.job_changes_lists:
            job_changes_lists_item = job_changes_lists_item_data.to_dict()
            job_changes_lists.append(job_changes_lists_item)

        total_count = self.total_count

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobChangesLists": job_changes_lists,
                "totalCount": total_count,
            }
        )
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_all_job_change_lists_response_200_output_job_changes_lists_item import (
            ListAllJobChangeListsResponse200OutputJobChangesListsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        job_changes_lists = []
        _job_changes_lists = d.pop("jobChangesLists")
        for job_changes_lists_item_data in _job_changes_lists:
            job_changes_lists_item = ListAllJobChangeListsResponse200OutputJobChangesListsItem.from_dict(
                job_changes_lists_item_data
            )

            job_changes_lists.append(job_changes_lists_item)

        total_count = d.pop("totalCount")

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        list_all_job_change_lists_response_200_output = cls(
            job_changes_lists=job_changes_lists,
            total_count=total_count,
            next_cursor=next_cursor,
        )

        list_all_job_change_lists_response_200_output.additional_properties = d
        return list_all_job_change_lists_response_200_output

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
