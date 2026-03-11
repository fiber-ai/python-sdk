from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0SnapshotsItem")


@_attrs_define
class CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0SnapshotsItem:
    """
    Attributes:
        date (datetime.date):
        employees (int):
    """

    date: datetime.date
    employees: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        employees = self.employees

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "employees": employees,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = isoparse(d.pop("date")).date()

        employees = d.pop("employees")

        company_live_enrich_response_200_output_company_historical_headcount_type_0_snapshots_item = cls(
            date=date,
            employees=employees,
        )

        company_live_enrich_response_200_output_company_historical_headcount_type_0_snapshots_item.additional_properties = d
        return company_live_enrich_response_200_output_company_historical_headcount_type_0_snapshots_item

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
