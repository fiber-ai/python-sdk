from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TechnologyAdded")


@_attrs_define
class TechnologyAdded:
    """
    Attributes:
        type_ (Literal['technology_added']):
        entity_type (Literal['company']):
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        is_dummy (bool | Unset): When true, this rule only fires via the fire-dummy endpoint and is skipped during
            normal pipeline runs.
        technologies (list[str] | None | Unset): Only alert for these technologies. Omit for any new technology.
    """

    type_: Literal["technology_added"]
    entity_type: Literal["company"]
    lookback_days: int | None | Unset = UNSET
    is_dummy: bool | Unset = UNSET
    technologies: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        is_dummy = self.is_dummy

        technologies: list[str] | None | Unset
        if isinstance(self.technologies, Unset):
            technologies = UNSET
        elif isinstance(self.technologies, list):
            technologies = self.technologies

        else:
            technologies = self.technologies

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
        if is_dummy is not UNSET:
            field_dict["isDummy"] = is_dummy
        if technologies is not UNSET:
            field_dict["technologies"] = technologies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["technology_added"], d.pop("type"))
        if type_ != "technology_added":
            raise ValueError(f"type must match const 'technology_added', got '{type_}'")

        entity_type = cast(Literal["company"], d.pop("entityType"))
        if entity_type != "company":
            raise ValueError(f"entityType must match const 'company', got '{entity_type}'")

        def _parse_lookback_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        is_dummy = d.pop("isDummy", UNSET)

        def _parse_technologies(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                technologies_type_0 = cast(list[str], data)

                return technologies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        technologies = _parse_technologies(d.pop("technologies", UNSET))

        technology_added = cls(
            type_=type_,
            entity_type=entity_type,
            lookback_days=lookback_days,
            is_dummy=is_dummy,
            technologies=technologies,
        )

        technology_added.additional_properties = d
        return technology_added

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
