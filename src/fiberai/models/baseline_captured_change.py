from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BaselineCapturedChange")


@_attrs_define
class BaselineCapturedChange:
    """
    Attributes:
        list_id (str): ID of the tracker list the entity belongs to
        list_name (str): Name of the tracker list the entity belongs to
        baselined_at (datetime.datetime): When the entity's first snapshot was stored. Monitoring compares against this
            snapshot from here on.
    """

    list_id: str
    list_name: str
    baselined_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_id = self.list_id

        list_name = self.list_name

        baselined_at = self.baselined_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "listId": list_id,
                "listName": list_name,
                "baselinedAt": baselined_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        list_id = d.pop("listId")

        list_name = d.pop("listName")

        baselined_at = datetime.datetime.fromisoformat(d.pop("baselinedAt"))

        baseline_captured_change = cls(
            list_id=list_id,
            list_name=list_name,
            baselined_at=baselined_at,
        )

        baseline_captured_change.additional_properties = d
        return baseline_captured_change

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
