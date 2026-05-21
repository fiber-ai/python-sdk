from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetTrackerOverviewResponse200OutputSummary")


@_attrs_define
class GetTrackerOverviewResponse200OutputSummary:
    """
    Attributes:
        total_company_lists (int): Active, non-archived company tracker lists for the organization.
        total_person_lists (int): Active, non-archived person tracker lists for the organization.
        total_companies_tracked (int): Total active companies across all company lists.
        total_people_tracked (int): Total active people across all person lists.
        total_active_rules (int): Active tracking rules across all lists.
        estimated_daily_credits (float): Amortized daily credit burn across all lists at the current entity counts and
            refresh cadences.
        estimated_monthly_credits (float): Estimated 30-day credit burn at the current entity counts and refresh
            cadences.
    """

    total_company_lists: int
    total_person_lists: int
    total_companies_tracked: int
    total_people_tracked: int
    total_active_rules: int
    estimated_daily_credits: float
    estimated_monthly_credits: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_company_lists = self.total_company_lists

        total_person_lists = self.total_person_lists

        total_companies_tracked = self.total_companies_tracked

        total_people_tracked = self.total_people_tracked

        total_active_rules = self.total_active_rules

        estimated_daily_credits = self.estimated_daily_credits

        estimated_monthly_credits = self.estimated_monthly_credits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalCompanyLists": total_company_lists,
                "totalPersonLists": total_person_lists,
                "totalCompaniesTracked": total_companies_tracked,
                "totalPeopleTracked": total_people_tracked,
                "totalActiveRules": total_active_rules,
                "estimatedDailyCredits": estimated_daily_credits,
                "estimatedMonthlyCredits": estimated_monthly_credits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_company_lists = d.pop("totalCompanyLists")

        total_person_lists = d.pop("totalPersonLists")

        total_companies_tracked = d.pop("totalCompaniesTracked")

        total_people_tracked = d.pop("totalPeopleTracked")

        total_active_rules = d.pop("totalActiveRules")

        estimated_daily_credits = d.pop("estimatedDailyCredits")

        estimated_monthly_credits = d.pop("estimatedMonthlyCredits")

        get_tracker_overview_response_200_output_summary = cls(
            total_company_lists=total_company_lists,
            total_person_lists=total_person_lists,
            total_companies_tracked=total_companies_tracked,
            total_people_tracked=total_people_tracked,
            total_active_rules=total_active_rules,
            estimated_daily_credits=estimated_daily_credits,
            estimated_monthly_credits=estimated_monthly_credits,
        )

        get_tracker_overview_response_200_output_summary.additional_properties = d
        return get_tracker_overview_response_200_output_summary

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
