from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LayoffEventChange")


@_attrs_define
class LayoffEventChange:
    """
    Attributes:
        date (None | str): ISO date of the layoff event
        num_laid_off (float | None): Number of employees laid off
        percent_laid_off (float | None): Percentage of workforce laid off
        source (None | str): Source URL for the layoff report
    """

    date: None | str
    num_laid_off: float | None
    percent_laid_off: float | None
    source: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: None | str
        date = self.date

        num_laid_off: float | None
        num_laid_off = self.num_laid_off

        percent_laid_off: float | None
        percent_laid_off = self.percent_laid_off

        source: None | str
        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "numLaidOff": num_laid_off,
                "percentLaidOff": percent_laid_off,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        date = _parse_date(d.pop("date"))

        def _parse_num_laid_off(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        num_laid_off = _parse_num_laid_off(d.pop("numLaidOff"))

        def _parse_percent_laid_off(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        percent_laid_off = _parse_percent_laid_off(d.pop("percentLaidOff"))

        def _parse_source(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source = _parse_source(d.pop("source"))

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
