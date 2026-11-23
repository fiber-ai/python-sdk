from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kitchen_sink_bulk_company_response_200_output_data_item_item_vesting_schedules_type_0_item_cadence import (
    KitchenSinkBulkCompanyResponse200OutputDataItemItemVestingSchedulesType0ItemCadence,
)
from ..models.kitchen_sink_bulk_company_response_200_output_data_item_item_vesting_schedules_type_0_item_shape import (
    KitchenSinkBulkCompanyResponse200OutputDataItemItemVestingSchedulesType0ItemShape,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kitchen_sink_bulk_company_response_200_output_data_item_item_vesting_schedules_type_0_item_years_item import (
        KitchenSinkBulkCompanyResponse200OutputDataItemItemVestingSchedulesType0ItemYearsItem,
    )


T = TypeVar("T", bound="KitchenSinkBulkCompanyResponse200OutputDataItemItemVestingSchedulesType0Item")


@_attrs_define
class KitchenSinkBulkCompanyResponse200OutputDataItemItemVestingSchedulesType0Item:
    """
    Attributes:
        variant (str):
        total_years (int):
        years (list[KitchenSinkBulkCompanyResponse200OutputDataItemItemVestingSchedulesType0ItemYearsItem]):
        shape (KitchenSinkBulkCompanyResponse200OutputDataItemItemVestingSchedulesType0ItemShape):
        cadence (KitchenSinkBulkCompanyResponse200OutputDataItemItemVestingSchedulesType0ItemCadence):
        max_percent_per_year (float):
        min_percent_per_year (float):
        stock_type (None | str | Unset):
        has_one_year_cliff (bool | None | Unset):
        notes (None | str | Unset):
    """

    variant: str
    total_years: int
    years: list[KitchenSinkBulkCompanyResponse200OutputDataItemItemVestingSchedulesType0ItemYearsItem]
    shape: KitchenSinkBulkCompanyResponse200OutputDataItemItemVestingSchedulesType0ItemShape
    cadence: KitchenSinkBulkCompanyResponse200OutputDataItemItemVestingSchedulesType0ItemCadence
    max_percent_per_year: float
    min_percent_per_year: float
    stock_type: None | str | Unset = UNSET
    has_one_year_cliff: bool | None | Unset = UNSET
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variant = self.variant

        total_years = self.total_years

        years = []
        for years_item_data in self.years:
            years_item = years_item_data.to_dict()
            years.append(years_item)

        shape = self.shape.value

        cadence = self.cadence.value

        max_percent_per_year = self.max_percent_per_year

        min_percent_per_year = self.min_percent_per_year

        stock_type: None | str | Unset
        if isinstance(self.stock_type, Unset):
            stock_type = UNSET
        else:
            stock_type = self.stock_type

        has_one_year_cliff: bool | None | Unset
        if isinstance(self.has_one_year_cliff, Unset):
            has_one_year_cliff = UNSET
        else:
            has_one_year_cliff = self.has_one_year_cliff

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "variant": variant,
                "total_years": total_years,
                "years": years,
                "shape": shape,
                "cadence": cadence,
                "max_percent_per_year": max_percent_per_year,
                "min_percent_per_year": min_percent_per_year,
            }
        )
        if stock_type is not UNSET:
            field_dict["stock_type"] = stock_type
        if has_one_year_cliff is not UNSET:
            field_dict["has_one_year_cliff"] = has_one_year_cliff
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kitchen_sink_bulk_company_response_200_output_data_item_item_vesting_schedules_type_0_item_years_item import (
            KitchenSinkBulkCompanyResponse200OutputDataItemItemVestingSchedulesType0ItemYearsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        variant = d.pop("variant")

        total_years = d.pop("total_years")

        years = []
        _years = d.pop("years")
        for years_item_data in _years:
            years_item = (
                KitchenSinkBulkCompanyResponse200OutputDataItemItemVestingSchedulesType0ItemYearsItem.from_dict(
                    years_item_data
                )
            )

            years.append(years_item)

        shape = KitchenSinkBulkCompanyResponse200OutputDataItemItemVestingSchedulesType0ItemShape(d.pop("shape"))

        cadence = KitchenSinkBulkCompanyResponse200OutputDataItemItemVestingSchedulesType0ItemCadence(d.pop("cadence"))

        max_percent_per_year = d.pop("max_percent_per_year")

        min_percent_per_year = d.pop("min_percent_per_year")

        def _parse_stock_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_type = _parse_stock_type(d.pop("stock_type", UNSET))

        def _parse_has_one_year_cliff(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_one_year_cliff = _parse_has_one_year_cliff(d.pop("has_one_year_cliff", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        kitchen_sink_bulk_company_response_200_output_data_item_item_vesting_schedules_type_0_item = cls(
            variant=variant,
            total_years=total_years,
            years=years,
            shape=shape,
            cadence=cadence,
            max_percent_per_year=max_percent_per_year,
            min_percent_per_year=min_percent_per_year,
            stock_type=stock_type,
            has_one_year_cliff=has_one_year_cliff,
            notes=notes,
        )

        kitchen_sink_bulk_company_response_200_output_data_item_item_vesting_schedules_type_0_item.additional_properties = d
        return kitchen_sink_bulk_company_response_200_output_data_item_item_vesting_schedules_type_0_item

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
