from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kitchen_sink_company_response_200_output_data_item_vesting_schedules_type_0_item_years_item_cadence import (
    KitchenSinkCompanyResponse200OutputDataItemVestingSchedulesType0ItemYearsItemCadence,
)

T = TypeVar("T", bound="KitchenSinkCompanyResponse200OutputDataItemVestingSchedulesType0ItemYearsItem")


@_attrs_define
class KitchenSinkCompanyResponse200OutputDataItemVestingSchedulesType0ItemYearsItem:
    """
    Attributes:
        year (int):
        percent_of_grant (float):
        cadence (KitchenSinkCompanyResponse200OutputDataItemVestingSchedulesType0ItemYearsItemCadence):
        vesting_events_per_year (int):
        percent_per_vesting_event (float):
    """

    year: int
    percent_of_grant: float
    cadence: KitchenSinkCompanyResponse200OutputDataItemVestingSchedulesType0ItemYearsItemCadence
    vesting_events_per_year: int
    percent_per_vesting_event: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        year = self.year

        percent_of_grant = self.percent_of_grant

        cadence = self.cadence.value

        vesting_events_per_year = self.vesting_events_per_year

        percent_per_vesting_event = self.percent_per_vesting_event

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "year": year,
                "percent_of_grant": percent_of_grant,
                "cadence": cadence,
                "vesting_events_per_year": vesting_events_per_year,
                "percent_per_vesting_event": percent_per_vesting_event,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        year = d.pop("year")

        percent_of_grant = d.pop("percent_of_grant")

        cadence = KitchenSinkCompanyResponse200OutputDataItemVestingSchedulesType0ItemYearsItemCadence(d.pop("cadence"))

        vesting_events_per_year = d.pop("vesting_events_per_year")

        percent_per_vesting_event = d.pop("percent_per_vesting_event")

        kitchen_sink_company_response_200_output_data_item_vesting_schedules_type_0_item_years_item = cls(
            year=year,
            percent_of_grant=percent_of_grant,
            cadence=cadence,
            vesting_events_per_year=vesting_events_per_year,
            percent_per_vesting_event=percent_per_vesting_event,
        )

        kitchen_sink_company_response_200_output_data_item_vesting_schedules_type_0_item_years_item.additional_properties = d
        return kitchen_sink_company_response_200_output_data_item_vesting_schedules_type_0_item_years_item

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
