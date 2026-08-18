from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DepartedFromListChange")


@_attrs_define
class DepartedFromListChange:
    """
    Attributes:
        list_id (str): ID of the dynamic tracker list the entity left
        list_name (str): Name of the dynamic tracker list the entity left
        reason (Literal['no_longer_matches']): Why the entity was removed — it no longer matches the list's query
    """

    list_id: str
    list_name: str
    reason: Literal["no_longer_matches"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_id = self.list_id

        list_name = self.list_name

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "listId": list_id,
                "listName": list_name,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        list_id = d.pop("listId")

        list_name = d.pop("listName")

        reason = cast(Literal["no_longer_matches"], d.pop("reason"))
        if reason != "no_longer_matches":
            raise ValueError(f"reason must match const 'no_longer_matches', got '{reason}'")

        departed_from_list_change = cls(
            list_id=list_id,
            list_name=list_name,
            reason=reason,
        )

        departed_from_list_change.additional_properties = d
        return departed_from_list_change

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
