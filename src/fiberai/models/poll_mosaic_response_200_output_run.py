from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.poll_mosaic_response_200_output_run_status import PollMosaicResponse200OutputRunStatus

if TYPE_CHECKING:
    from ..models.poll_mosaic_response_200_output_run_stats_type_0 import PollMosaicResponse200OutputRunStatsType0


T = TypeVar("T", bound="PollMosaicResponse200OutputRun")


@_attrs_define
class PollMosaicResponse200OutputRun:
    """Current Mosaic run state. When status is done, outputCsvUrl and reportUrl are temporary download links.

    Attributes:
        run_id (str):
        status (PollMosaicResponse200OutputRunStatus):
        row_count (int | None): Rows detected in the input file.
        processed_row_count (int | None): Rows enriched and written to the output CSV (<= rowCount when maxRows or the
            free-trial cap applies).
        is_free_trial_run (bool):
        stats (None | PollMosaicResponse200OutputRunStatsType0):
        output_csv_url (None | str):
        report_url (None | str):
    """

    run_id: str
    status: PollMosaicResponse200OutputRunStatus
    row_count: int | None
    processed_row_count: int | None
    is_free_trial_run: bool
    stats: None | PollMosaicResponse200OutputRunStatsType0
    output_csv_url: None | str
    report_url: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.poll_mosaic_response_200_output_run_stats_type_0 import PollMosaicResponse200OutputRunStatsType0

        run_id = self.run_id

        status = self.status.value

        row_count: int | None
        row_count = self.row_count

        processed_row_count: int | None
        processed_row_count = self.processed_row_count

        is_free_trial_run = self.is_free_trial_run

        stats: dict[str, Any] | None
        if isinstance(self.stats, PollMosaicResponse200OutputRunStatsType0):
            stats = self.stats.to_dict()
        else:
            stats = self.stats

        output_csv_url: None | str
        output_csv_url = self.output_csv_url

        report_url: None | str
        report_url = self.report_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runId": run_id,
                "status": status,
                "rowCount": row_count,
                "processedRowCount": processed_row_count,
                "isFreeTrialRun": is_free_trial_run,
                "stats": stats,
                "outputCsvUrl": output_csv_url,
                "reportUrl": report_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_mosaic_response_200_output_run_stats_type_0 import PollMosaicResponse200OutputRunStatsType0

        d = dict(src_dict)
        run_id = d.pop("runId")

        status = PollMosaicResponse200OutputRunStatus(d.pop("status"))

        def _parse_row_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        row_count = _parse_row_count(d.pop("rowCount"))

        def _parse_processed_row_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        processed_row_count = _parse_processed_row_count(d.pop("processedRowCount"))

        is_free_trial_run = d.pop("isFreeTrialRun")

        def _parse_stats(data: object) -> None | PollMosaicResponse200OutputRunStatsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stats_type_0 = PollMosaicResponse200OutputRunStatsType0.from_dict(data)

                return stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PollMosaicResponse200OutputRunStatsType0, data)

        stats = _parse_stats(d.pop("stats"))

        def _parse_output_csv_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        output_csv_url = _parse_output_csv_url(d.pop("outputCsvUrl"))

        def _parse_report_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        report_url = _parse_report_url(d.pop("reportUrl"))

        poll_mosaic_response_200_output_run = cls(
            run_id=run_id,
            status=status,
            row_count=row_count,
            processed_row_count=processed_row_count,
            is_free_trial_run=is_free_trial_run,
            stats=stats,
            output_csv_url=output_csv_url,
            report_url=report_url,
        )

        poll_mosaic_response_200_output_run.additional_properties = d
        return poll_mosaic_response_200_output_run

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
