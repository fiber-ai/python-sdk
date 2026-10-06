from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RescheduleTrackerCompanyListBody")


@_attrs_define
class RescheduleTrackerCompanyListBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        next_refresh_date (str): The date (YYYY-MM-DD, UTC) on which the next scheduled refresh should run. Must be
            tomorrow (UTC) or later, and at most 360 days ahead. To refresh a list immediately, use the refresh endpoint
            instead. Subsequent refreshes continue at the list's regular interval, counted from this run.
    """

    api_key: str
    next_refresh_date: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        next_refresh_date = self.next_refresh_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "nextRefreshDate": next_refresh_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        next_refresh_date = d.pop("nextRefreshDate")

        reschedule_tracker_company_list_body = cls(
            api_key=api_key,
            next_refresh_date=next_refresh_date,
        )

        reschedule_tracker_company_list_body.additional_properties = d
        return reschedule_tracker_company_list_body

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
