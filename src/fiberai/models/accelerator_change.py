from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AcceleratorChange")


@_attrs_define
class AcceleratorChange:
    """
    Attributes:
        accelerator_name (str): Name of the accelerator the company joined (e.g. "Y Combinator")
        batch (None | str | Unset): Batch or cohort the company went through, as labeled by the accelerator. Null when
            the accelerator does not publish one.
        year (int | None | Unset): Year of the batch. Null when unknown.
    """

    accelerator_name: str
    batch: None | str | Unset = UNSET
    year: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accelerator_name = self.accelerator_name

        batch: None | str | Unset
        if isinstance(self.batch, Unset):
            batch = UNSET
        else:
            batch = self.batch

        year: int | None | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acceleratorName": accelerator_name,
            }
        )
        if batch is not UNSET:
            field_dict["batch"] = batch
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accelerator_name = d.pop("acceleratorName")

        def _parse_batch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch = _parse_batch(d.pop("batch", UNSET))

        def _parse_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        year = _parse_year(d.pop("year", UNSET))

        accelerator_change = cls(
            accelerator_name=accelerator_name,
            batch=batch,
            year=year,
        )

        accelerator_change.additional_properties = d
        return accelerator_change

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
