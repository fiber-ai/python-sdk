from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_media_lookup_batch_polling_response_200_output_status import (
    SocialMediaLookupBatchPollingResponse200OutputStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_media_lookup_batch_polling_response_200_output_overall_stats import (
        SocialMediaLookupBatchPollingResponse200OutputOverallStats,
    )
    from ..models.social_media_lookup_batch_polling_response_200_output_results_item import (
        SocialMediaLookupBatchPollingResponse200OutputResultsItem,
    )


T = TypeVar("T", bound="SocialMediaLookupBatchPollingResponse200Output")


@_attrs_define
class SocialMediaLookupBatchPollingResponse200Output:
    """
    Attributes:
        status (SocialMediaLookupBatchPollingResponse200OutputStatus): Current status of the batch run.
        overall_stats (SocialMediaLookupBatchPollingResponse200OutputOverallStats): Summary statistics for the entire
            batch.
        results (list[SocialMediaLookupBatchPollingResponse200OutputResultsItem]): One entry per person on this page.
        next_page_token (None | str | Unset): Token for the next page of results. Null when there are no more results.
    """

    status: SocialMediaLookupBatchPollingResponse200OutputStatus
    overall_stats: SocialMediaLookupBatchPollingResponse200OutputOverallStats
    results: list[SocialMediaLookupBatchPollingResponse200OutputResultsItem]
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        overall_stats = self.overall_stats.to_dict()

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "overallStats": overall_stats,
                "results": results,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_media_lookup_batch_polling_response_200_output_overall_stats import (
            SocialMediaLookupBatchPollingResponse200OutputOverallStats,  # noqa: PLC0415
        )
        from ..models.social_media_lookup_batch_polling_response_200_output_results_item import (
            SocialMediaLookupBatchPollingResponse200OutputResultsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        status = SocialMediaLookupBatchPollingResponse200OutputStatus(d.pop("status"))

        overall_stats = SocialMediaLookupBatchPollingResponse200OutputOverallStats.from_dict(d.pop("overallStats"))

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = SocialMediaLookupBatchPollingResponse200OutputResultsItem.from_dict(results_item_data)

            results.append(results_item)

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        social_media_lookup_batch_polling_response_200_output = cls(
            status=status,
            overall_stats=overall_stats,
            results=results,
            next_page_token=next_page_token,
        )

        social_media_lookup_batch_polling_response_200_output.additional_properties = d
        return social_media_lookup_batch_polling_response_200_output

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
