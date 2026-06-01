from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.kitchen_sink_company_response_200_output_data_item_historical_headcount_type_0_growth import (
        KitchenSinkCompanyResponse200OutputDataItemHistoricalHeadcountType0Growth,
    )
    from ..models.kitchen_sink_company_response_200_output_data_item_historical_headcount_type_0_snapshots_item import (
        KitchenSinkCompanyResponse200OutputDataItemHistoricalHeadcountType0SnapshotsItem,
    )


T = TypeVar("T", bound="KitchenSinkCompanyResponse200OutputDataItemHistoricalHeadcountType0")


@_attrs_define
class KitchenSinkCompanyResponse200OutputDataItemHistoricalHeadcountType0:
    """
    Attributes:
        latest_snapshot_date (datetime.date):
        snapshots (list[KitchenSinkCompanyResponse200OutputDataItemHistoricalHeadcountType0SnapshotsItem]):
        growth (KitchenSinkCompanyResponse200OutputDataItemHistoricalHeadcountType0Growth):
    """

    latest_snapshot_date: datetime.date
    snapshots: list[KitchenSinkCompanyResponse200OutputDataItemHistoricalHeadcountType0SnapshotsItem]
    growth: KitchenSinkCompanyResponse200OutputDataItemHistoricalHeadcountType0Growth
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
        from ..models.kitchen_sink_company_response_200_output_data_item_historical_headcount_type_0_growth import (
            KitchenSinkCompanyResponse200OutputDataItemHistoricalHeadcountType0Growth,
        )
        from ..models.kitchen_sink_company_response_200_output_data_item_historical_headcount_type_0_snapshots_item import (
            KitchenSinkCompanyResponse200OutputDataItemHistoricalHeadcountType0SnapshotsItem,
        )

        d = dict(src_dict)
        latest_snapshot_date = datetime.date.fromisoformat(d.pop("latest_snapshot_date"))

        snapshots = []
        _snapshots = d.pop("snapshots")
        for snapshots_item_data in _snapshots:
            snapshots_item = KitchenSinkCompanyResponse200OutputDataItemHistoricalHeadcountType0SnapshotsItem.from_dict(
                snapshots_item_data
            )

            snapshots.append(snapshots_item)

        growth = KitchenSinkCompanyResponse200OutputDataItemHistoricalHeadcountType0Growth.from_dict(d.pop("growth"))

        kitchen_sink_company_response_200_output_data_item_historical_headcount_type_0 = cls(
            latest_snapshot_date=latest_snapshot_date,
            snapshots=snapshots,
            growth=growth,
        )

        kitchen_sink_company_response_200_output_data_item_historical_headcount_type_0.additional_properties = d
        return kitchen_sink_company_response_200_output_data_item_historical_headcount_type_0

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
