from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.poll_batch_contact_enrichment_response_200_output_overall_stats import PollBatchContactEnrichmentResponse200OutputOverallStats
  from ..models.poll_batch_contact_enrichment_response_200_output_page_results_item import PollBatchContactEnrichmentResponse200OutputPageResultsItem





T = TypeVar("T", bound="PollBatchContactEnrichmentResponse200Output")



@_attrs_define
class PollBatchContactEnrichmentResponse200Output:
    """ 
        Attributes:
            overall_stats (PollBatchContactEnrichmentResponse200OutputOverallStats): Overall statistics for the batch
                enrichment task
            done (bool): True when ALL people have been processed (completed or failed)
            page_results (list['PollBatchContactEnrichmentResponse200OutputPageResultsItem']): Array of results for each
                person in the current page. You need to keep paginating using the cursor to get more results.
            next_cursor (Union[None, Unset, str]): Next cursor to use for pagination. Use this to get the next page of
                results.
     """

    overall_stats: 'PollBatchContactEnrichmentResponse200OutputOverallStats'
    done: bool
    page_results: list['PollBatchContactEnrichmentResponse200OutputPageResultsItem']
    next_cursor: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.poll_batch_contact_enrichment_response_200_output_overall_stats import PollBatchContactEnrichmentResponse200OutputOverallStats
        from ..models.poll_batch_contact_enrichment_response_200_output_page_results_item import PollBatchContactEnrichmentResponse200OutputPageResultsItem
        overall_stats = self.overall_stats.to_dict()

        done = self.done

        page_results = []
        for page_results_item_data in self.page_results:
            page_results_item = page_results_item_data.to_dict()
            page_results.append(page_results_item)



        next_cursor: Union[None, Unset, str]
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "overallStats": overall_stats,
            "done": done,
            "pageResults": page_results,
        })
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_batch_contact_enrichment_response_200_output_overall_stats import PollBatchContactEnrichmentResponse200OutputOverallStats
        from ..models.poll_batch_contact_enrichment_response_200_output_page_results_item import PollBatchContactEnrichmentResponse200OutputPageResultsItem
        d = dict(src_dict)
        overall_stats = PollBatchContactEnrichmentResponse200OutputOverallStats.from_dict(d.pop("overallStats"))




        done = d.pop("done")

        page_results = []
        _page_results = d.pop("pageResults")
        for page_results_item_data in (_page_results):
            page_results_item = PollBatchContactEnrichmentResponse200OutputPageResultsItem.from_dict(page_results_item_data)



            page_results.append(page_results_item)


        def _parse_next_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))


        poll_batch_contact_enrichment_response_200_output = cls(
            overall_stats=overall_stats,
            done=done,
            page_results=page_results,
            next_cursor=next_cursor,
        )


        poll_batch_contact_enrichment_response_200_output.additional_properties = d
        return poll_batch_contact_enrichment_response_200_output

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
