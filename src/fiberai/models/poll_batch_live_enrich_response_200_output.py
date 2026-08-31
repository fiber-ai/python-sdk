from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.poll_batch_live_enrich_response_200_output_status import PollBatchLiveEnrichResponse200OutputStatus
from ..models.poll_batch_live_enrich_response_200_output_type import PollBatchLiveEnrichResponse200OutputType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.poll_batch_live_enrich_response_200_output_progress import (
        PollBatchLiveEnrichResponse200OutputProgress,
    )
    from ..models.poll_batch_live_enrich_response_200_output_results_item import (
        PollBatchLiveEnrichResponse200OutputResultsItem,
    )


T = TypeVar("T", bound="PollBatchLiveEnrichResponse200Output")


@_attrs_define
class PollBatchLiveEnrichResponse200Output:
    """
    Attributes:
        status (PollBatchLiveEnrichResponse200OutputStatus): Current status of the batch job
        type_ (PollBatchLiveEnrichResponse200OutputType):
        progress (PollBatchLiveEnrichResponse200OutputProgress):
        results (list[PollBatchLiveEnrichResponse200OutputResultsItem]): Paginated enrichment results for
            completed/failed items.
        next_cursor (None | str | Unset): Pagination cursor for the next page. Null when no more results.
        completed_at (datetime.datetime | None | Unset): ISO timestamp of when the batch completed, if done
    """

    status: PollBatchLiveEnrichResponse200OutputStatus
    type_: PollBatchLiveEnrichResponse200OutputType
    progress: PollBatchLiveEnrichResponse200OutputProgress
    results: list[PollBatchLiveEnrichResponse200OutputResultsItem]
    next_cursor: None | str | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        type_ = self.type_.value

        progress = self.progress.to_dict()

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "type": type_,
                "progress": progress,
                "results": results,
            }
        )
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_batch_live_enrich_response_200_output_progress import (
            PollBatchLiveEnrichResponse200OutputProgress,  # noqa: PLC0415
        )
        from ..models.poll_batch_live_enrich_response_200_output_results_item import (
            PollBatchLiveEnrichResponse200OutputResultsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        status = PollBatchLiveEnrichResponse200OutputStatus(d.pop("status"))

        type_ = PollBatchLiveEnrichResponse200OutputType(d.pop("type"))

        progress = PollBatchLiveEnrichResponse200OutputProgress.from_dict(d.pop("progress"))

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = PollBatchLiveEnrichResponse200OutputResultsItem.from_dict(results_item_data)

            results.append(results_item)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))

        poll_batch_live_enrich_response_200_output = cls(
            status=status,
            type_=type_,
            progress=progress,
            results=results,
            next_cursor=next_cursor,
            completed_at=completed_at,
        )

        poll_batch_live_enrich_response_200_output.additional_properties = d
        return poll_batch_live_enrich_response_200_output

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
