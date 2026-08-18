from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LayoffEventChange")


@_attrs_define
class LayoffEventChange:
    """
    Attributes:
        date (None | str | Unset): ISO date of the layoff event
        num_laid_off (float | None | Unset): Number of employees laid off
        percent_laid_off (float | None | Unset): Percentage of workforce laid off
        source (None | str | Unset): Source URL for the layoff report
    """

    date: None | str | Unset = UNSET
    num_laid_off: float | None | Unset = UNSET
    percent_laid_off: float | None | Unset = UNSET
    source: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        num_laid_off: float | None | Unset
        if isinstance(self.num_laid_off, Unset):
            num_laid_off = UNSET
        else:
            num_laid_off = self.num_laid_off

        percent_laid_off: float | None | Unset
        if isinstance(self.percent_laid_off, Unset):
            percent_laid_off = UNSET
        else:
            percent_laid_off = self.percent_laid_off

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if num_laid_off is not UNSET:
            field_dict["numLaidOff"] = num_laid_off
        if percent_laid_off is not UNSET:
            field_dict["percentLaidOff"] = percent_laid_off
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_num_laid_off(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        num_laid_off = _parse_num_laid_off(d.pop("numLaidOff", UNSET))

        def _parse_percent_laid_off(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        percent_laid_off = _parse_percent_laid_off(d.pop("percentLaidOff", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        layoff_event_change = cls(
            date=date,
            num_laid_off=num_laid_off,
            percent_laid_off=percent_laid_off,
            source=source,
        )

        layoff_event_change.additional_properties = d
        return layoff_event_change

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
