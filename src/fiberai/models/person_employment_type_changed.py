from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonEmploymentTypeChanged")


@_attrs_define
class PersonEmploymentTypeChanged:
    """
    Attributes:
        type_ (Literal['person_employment_type_changed']):
        entity_type (Literal['person']):
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        to_types (list[str] | None | Unset): Only alert if new employment type is one of these (e.g. 'Contract', 'Part-
            time'). Omit for any change.
    """

    type_: Literal["person_employment_type_changed"]
    entity_type: Literal["person"]
    lookback_days: int | None | Unset = UNSET
    to_types: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        to_types: list[str] | None | Unset
        if isinstance(self.to_types, Unset):
            to_types = UNSET
        elif isinstance(self.to_types, list):
            to_types = self.to_types

        else:
            to_types = self.to_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "entityType": entity_type,
            }
        )
        if lookback_days is not UNSET:
            field_dict["lookbackDays"] = lookback_days
        if to_types is not UNSET:
            field_dict["toTypes"] = to_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["person_employment_type_changed"], d.pop("type"))
        if type_ != "person_employment_type_changed":
            raise ValueError(f"type must match const 'person_employment_type_changed', got '{type_}'")

        entity_type = cast(Literal["person"], d.pop("entityType"))
        if entity_type != "person":
            raise ValueError(f"entityType must match const 'person', got '{entity_type}'")

        def _parse_lookback_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        def _parse_to_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                to_types_type_0 = cast(list[str], data)

                return to_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        to_types = _parse_to_types(d.pop("toTypes", UNSET))

        person_employment_type_changed = cls(
            type_=type_,
            entity_type=entity_type,
            lookback_days=lookback_days,
            to_types=to_types,
        )

        person_employment_type_changed.additional_properties = d
        return person_employment_type_changed

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
