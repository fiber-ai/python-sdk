from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetScoutingReportResponse200OutputReportMilestonesItem")


@_attrs_define
class GetScoutingReportResponse200OutputReportMilestonesItem:
    """
    Attributes:
        type_ (str):
        description (str):
        date (None | str | Unset):
    """

    type_: str
    description: str
    date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        description = self.description

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "description": description,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        description = d.pop("description")

        def _parse_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        get_scouting_report_response_200_output_report_milestones_item = cls(
            type_=type_,
            description=description,
            date=date,
        )

        get_scouting_report_response_200_output_report_milestones_item.additional_properties = d
        return get_scouting_report_response_200_output_report_milestones_item

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
