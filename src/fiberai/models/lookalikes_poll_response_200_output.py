from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lookalikes_poll_response_200_output_status import LookalikesPollResponse200OutputStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lookalikes_poll_response_200_output_buckets_item import LookalikesPollResponse200OutputBucketsItem
    from ..models.lookalikes_poll_response_200_output_progress import LookalikesPollResponse200OutputProgress


T = TypeVar("T", bound="LookalikesPollResponse200Output")


@_attrs_define
class LookalikesPollResponse200Output:
    """
    Attributes:
        status (LookalikesPollResponse200OutputStatus): Current state of the run.
        progress (LookalikesPollResponse200OutputProgress): Per-phase progress. Poll until status is 'done' or 'failed'.
        unresolved_domains (list[str]): Inputs that did not contribute to the results, exactly as you submitted them —
            either not matched to a company, or rejected as invalid or as a personal-email domain.
        buckets (list[LookalikesPollResponse200OutputBucketsItem]): Company groupings. Each grouping's graded findings
            appear when the run completes.
        overall_summary (None | str | Unset): Short summary of the themes across your input companies.
        error_message (None | str | Unset): Present when the run failed.
    """

    status: LookalikesPollResponse200OutputStatus
    progress: LookalikesPollResponse200OutputProgress
    unresolved_domains: list[str]
    buckets: list[LookalikesPollResponse200OutputBucketsItem]
    overall_summary: None | str | Unset = UNSET
    error_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        progress = self.progress.to_dict()

        unresolved_domains = self.unresolved_domains

        buckets = []
        for buckets_item_data in self.buckets:
            buckets_item = buckets_item_data.to_dict()
            buckets.append(buckets_item)

        overall_summary: None | str | Unset
        if isinstance(self.overall_summary, Unset):
            overall_summary = UNSET
        else:
            overall_summary = self.overall_summary

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "progress": progress,
                "unresolvedDomains": unresolved_domains,
                "buckets": buckets,
            }
        )
        if overall_summary is not UNSET:
            field_dict["overallSummary"] = overall_summary
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookalikes_poll_response_200_output_buckets_item import LookalikesPollResponse200OutputBucketsItem  # noqa: PLC0415
        from ..models.lookalikes_poll_response_200_output_progress import LookalikesPollResponse200OutputProgress  # noqa: PLC0415

        d = dict(src_dict)
        status = LookalikesPollResponse200OutputStatus(d.pop("status"))

        progress = LookalikesPollResponse200OutputProgress.from_dict(d.pop("progress"))

        unresolved_domains = cast(list[str], d.pop("unresolvedDomains"))

        buckets = []
        _buckets = d.pop("buckets")
        for buckets_item_data in _buckets:
            buckets_item = LookalikesPollResponse200OutputBucketsItem.from_dict(buckets_item_data)

            buckets.append(buckets_item)

        def _parse_overall_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overall_summary = _parse_overall_summary(d.pop("overallSummary", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        lookalikes_poll_response_200_output = cls(
            status=status,
            progress=progress,
            unresolved_domains=unresolved_domains,
            buckets=buckets,
            overall_summary=overall_summary,
            error_message=error_message,
        )

        lookalikes_poll_response_200_output.additional_properties = d
        return lookalikes_poll_response_200_output

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
