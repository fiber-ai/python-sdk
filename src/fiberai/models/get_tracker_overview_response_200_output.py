from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_tracker_overview_response_200_output_company_lists_item import (
        GetTrackerOverviewResponse200OutputCompanyListsItem,
    )
    from ..models.get_tracker_overview_response_200_output_person_lists_item import (
        GetTrackerOverviewResponse200OutputPersonListsItem,
    )
    from ..models.get_tracker_overview_response_200_output_summary import GetTrackerOverviewResponse200OutputSummary
    from ..models.get_tracker_overview_response_200_output_upcoming_refreshes_item import (
        GetTrackerOverviewResponse200OutputUpcomingRefreshesItem,
    )


T = TypeVar("T", bound="GetTrackerOverviewResponse200Output")


@_attrs_define
class GetTrackerOverviewResponse200Output:
    """
    Attributes:
        summary (GetTrackerOverviewResponse200OutputSummary):
        company_lists (list[GetTrackerOverviewResponse200OutputCompanyListsItem]): All active, non-archived company
            tracker lists with rules and refresh estimates.
        person_lists (list[GetTrackerOverviewResponse200OutputPersonListsItem]): All active, non-archived person tracker
            lists with rules and refresh estimates.
        upcoming_refreshes (list[GetTrackerOverviewResponse200OutputUpcomingRefreshesItem]): Next refreshes across all
            lists, sorted earliest first. Use this to forecast upcoming charges.
    """

    summary: GetTrackerOverviewResponse200OutputSummary
    company_lists: list[GetTrackerOverviewResponse200OutputCompanyListsItem]
    person_lists: list[GetTrackerOverviewResponse200OutputPersonListsItem]
    upcoming_refreshes: list[GetTrackerOverviewResponse200OutputUpcomingRefreshesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary.to_dict()

        company_lists = []
        for company_lists_item_data in self.company_lists:
            company_lists_item = company_lists_item_data.to_dict()
            company_lists.append(company_lists_item)

        person_lists = []
        for person_lists_item_data in self.person_lists:
            person_lists_item = person_lists_item_data.to_dict()
            person_lists.append(person_lists_item)

        upcoming_refreshes = []
        for upcoming_refreshes_item_data in self.upcoming_refreshes:
            upcoming_refreshes_item = upcoming_refreshes_item_data.to_dict()
            upcoming_refreshes.append(upcoming_refreshes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "summary": summary,
                "companyLists": company_lists,
                "personLists": person_lists,
                "upcomingRefreshes": upcoming_refreshes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_tracker_overview_response_200_output_company_lists_item import (
            GetTrackerOverviewResponse200OutputCompanyListsItem,
        )
        from ..models.get_tracker_overview_response_200_output_person_lists_item import (
            GetTrackerOverviewResponse200OutputPersonListsItem,
        )
        from ..models.get_tracker_overview_response_200_output_summary import GetTrackerOverviewResponse200OutputSummary
        from ..models.get_tracker_overview_response_200_output_upcoming_refreshes_item import (
            GetTrackerOverviewResponse200OutputUpcomingRefreshesItem,
        )

        d = dict(src_dict)
        summary = GetTrackerOverviewResponse200OutputSummary.from_dict(d.pop("summary"))

        company_lists = []
        _company_lists = d.pop("companyLists")
        for company_lists_item_data in _company_lists:
            company_lists_item = GetTrackerOverviewResponse200OutputCompanyListsItem.from_dict(company_lists_item_data)

            company_lists.append(company_lists_item)

        person_lists = []
        _person_lists = d.pop("personLists")
        for person_lists_item_data in _person_lists:
            person_lists_item = GetTrackerOverviewResponse200OutputPersonListsItem.from_dict(person_lists_item_data)

            person_lists.append(person_lists_item)

        upcoming_refreshes = []
        _upcoming_refreshes = d.pop("upcomingRefreshes")
        for upcoming_refreshes_item_data in _upcoming_refreshes:
            upcoming_refreshes_item = GetTrackerOverviewResponse200OutputUpcomingRefreshesItem.from_dict(
                upcoming_refreshes_item_data
            )

            upcoming_refreshes.append(upcoming_refreshes_item)

        get_tracker_overview_response_200_output = cls(
            summary=summary,
            company_lists=company_lists,
            person_lists=person_lists,
            upcoming_refreshes=upcoming_refreshes,
        )

        get_tracker_overview_response_200_output.additional_properties = d
        return get_tracker_overview_response_200_output

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
