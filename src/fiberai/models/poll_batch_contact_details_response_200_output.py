from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.poll_batch_contact_details_response_200_output_overall_stats import (
        PollBatchContactDetailsResponse200OutputOverallStats,
    )
    from ..models.poll_batch_contact_details_response_200_output_page_results_item import (
        PollBatchContactDetailsResponse200OutputPageResultsItem,
    )


T = TypeVar("T", bound="PollBatchContactDetailsResponse200Output")


@_attrs_define
class PollBatchContactDetailsResponse200Output:
    """
    Attributes:
        overall_stats (PollBatchContactDetailsResponse200OutputOverallStats): The overall statistics for the batch
            enrichment task.
        done (bool): Whether the batch task has finished. When true, check the 'failed' field to determine if it
            completed successfully or failed.
        failed (bool): Whether the batch task failed. If true, the task encountered an error and won't be retried. If
            false and done=true, the task completed successfully or was cancelled (check the 'canceled' field). If
            done=false, this field indicates current processing state.
        canceled (bool): Whether the batch task was cancelled. When true, unclaimed profiles were not processed and
            credits were refunded.
        page_results (list[PollBatchContactDetailsResponse200OutputPageResultsItem]): The array of results for each
            person in the current page.
        next_cursor (None | str | Unset): The pagination cursor for the next page of results.
    """

    overall_stats: PollBatchContactDetailsResponse200OutputOverallStats
    done: bool
    failed: bool
    canceled: bool
    page_results: list[PollBatchContactDetailsResponse200OutputPageResultsItem]
    next_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        overall_stats = self.overall_stats.to_dict()

        done = self.done

        failed = self.failed

        canceled = self.canceled

        page_results = []
        for page_results_item_data in self.page_results:
            page_results_item = page_results_item_data.to_dict()
            page_results.append(page_results_item)

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "overallStats": overall_stats,
                "done": done,
                "failed": failed,
                "canceled": canceled,
                "pageResults": page_results,
            }
        )
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_batch_contact_details_response_200_output_overall_stats import (
            PollBatchContactDetailsResponse200OutputOverallStats,
        )
        from ..models.poll_batch_contact_details_response_200_output_page_results_item import (
            PollBatchContactDetailsResponse200OutputPageResultsItem,
        )

        d = dict(src_dict)
        overall_stats = PollBatchContactDetailsResponse200OutputOverallStats.from_dict(d.pop("overallStats"))

        done = d.pop("done")

        failed = d.pop("failed")

        canceled = d.pop("canceled")

        page_results = []
        _page_results = d.pop("pageResults")
        for page_results_item_data in _page_results:
            page_results_item = PollBatchContactDetailsResponse200OutputPageResultsItem.from_dict(
                page_results_item_data
            )

            page_results.append(page_results_item)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        poll_batch_contact_details_response_200_output = cls(
            overall_stats=overall_stats,
            done=done,
            failed=failed,
            canceled=canceled,
            page_results=page_results,
            next_cursor=next_cursor,
        )

        poll_batch_contact_details_response_200_output.additional_properties = d
        return poll_batch_contact_details_response_200_output

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
