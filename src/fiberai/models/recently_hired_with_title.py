from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecentlyHiredWithTitle")


@_attrs_define
class RecentlyHiredWithTitle:
    """
    Attributes:
        type_ (Literal['recently_hired_with_title']):
        entity_type (Literal['company']):
        title_keywords (list[str]): Title keywords to search for. Fires when the company hires someone whose title
            matches any keyword.
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        min_new_hires (int | None | Unset): Minimum number of new hires to trigger the alert. Omit for 1.
    """

    type_: Literal["recently_hired_with_title"]
    entity_type: Literal["company"]
    title_keywords: list[str]
    lookback_days: int | None | Unset = UNSET
    min_new_hires: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        title_keywords = self.title_keywords

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        min_new_hires: int | None | Unset
        if isinstance(self.min_new_hires, Unset):
            min_new_hires = UNSET
        else:
            min_new_hires = self.min_new_hires

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "entityType": entity_type,
                "titleKeywords": title_keywords,
            }
        )
        if lookback_days is not UNSET:
            field_dict["lookbackDays"] = lookback_days
        if min_new_hires is not UNSET:
            field_dict["minNewHires"] = min_new_hires

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["recently_hired_with_title"], d.pop("type"))
        if type_ != "recently_hired_with_title":
            raise ValueError(f"type must match const 'recently_hired_with_title', got '{type_}'")

        entity_type = cast(Literal["company"], d.pop("entityType"))
        if entity_type != "company":
            raise ValueError(f"entityType must match const 'company', got '{entity_type}'")

        title_keywords = cast(list[str], d.pop("titleKeywords"))

        def _parse_lookback_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        def _parse_min_new_hires(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_new_hires = _parse_min_new_hires(d.pop("minNewHires", UNSET))

        recently_hired_with_title = cls(
            type_=type_,
            entity_type=entity_type,
            title_keywords=title_keywords,
            lookback_days=lookback_days,
            min_new_hires=min_new_hires,
        )

        recently_hired_with_title.additional_properties = d
        return recently_hired_with_title

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
