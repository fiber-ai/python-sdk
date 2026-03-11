from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.company_live_enrich_response_200_output_company_historical_headcount_type_0_growth import (
        CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0Growth,
    )
    from ..models.company_live_enrich_response_200_output_company_historical_headcount_type_0_snapshots_item import (
        CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0SnapshotsItem,
    )


T = TypeVar("T", bound="CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0")


@_attrs_define
class CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0:
    """
    Attributes:
        latest_snapshot_date (datetime.date):
        snapshots (list[CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0SnapshotsItem]):
        growth (CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0Growth):
    """

    latest_snapshot_date: datetime.date
    snapshots: list[CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0SnapshotsItem]
    growth: CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0Growth
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latest_snapshot_date = self.latest_snapshot_date.isoformat()

        snapshots = []
        for snapshots_item_data in self.snapshots:
            snapshots_item = snapshots_item_data.to_dict()
            snapshots.append(snapshots_item)

        growth = self.growth.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "latest_snapshot_date": latest_snapshot_date,
                "snapshots": snapshots,
                "growth": growth,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_live_enrich_response_200_output_company_historical_headcount_type_0_growth import (
            CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0Growth,
        )
        from ..models.company_live_enrich_response_200_output_company_historical_headcount_type_0_snapshots_item import (
            CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0SnapshotsItem,
        )

        d = dict(src_dict)
        latest_snapshot_date = isoparse(d.pop("latest_snapshot_date")).date()

        snapshots = []
        _snapshots = d.pop("snapshots")
        for snapshots_item_data in _snapshots:
            snapshots_item = CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0SnapshotsItem.from_dict(
                snapshots_item_data
            )

            snapshots.append(snapshots_item)

        growth = CompanyLiveEnrichResponse200OutputCompanyHistoricalHeadcountType0Growth.from_dict(d.pop("growth"))

        company_live_enrich_response_200_output_company_historical_headcount_type_0 = cls(
            latest_snapshot_date=latest_snapshot_date,
            snapshots=snapshots,
            growth=growth,
        )

        company_live_enrich_response_200_output_company_historical_headcount_type_0.additional_properties = d
        return company_live_enrich_response_200_output_company_historical_headcount_type_0

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
