from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.person_title_changed_to_seniority_type_0_item import PersonTitleChangedToSeniorityType0Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonTitleChanged")


@_attrs_define
class PersonTitleChanged:
    """
    Attributes:
        type_ (Literal['person_title_changed']):
        entity_type (Literal['person']):
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        is_dummy (bool | Unset): When true, this rule only fires via the fire-dummy endpoint and is skipped during
            normal pipeline runs.
        title_keywords (list[str] | None | Unset): Only alert if new title contains one of these keywords. Omit for any
            title change.
        to_seniority (list[PersonTitleChangedToSeniorityType0Item] | None | Unset): Only alert if the new position's
            seniority level matches one of these. Omit for any seniority.
    """

    type_: Literal["person_title_changed"]
    entity_type: Literal["person"]
    lookback_days: int | None | Unset = UNSET
    is_dummy: bool | Unset = UNSET
    title_keywords: list[str] | None | Unset = UNSET
    to_seniority: list[PersonTitleChangedToSeniorityType0Item] | None | Unset = UNSET
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

        title_keywords: list[str] | None | Unset
        if isinstance(self.title_keywords, Unset):
            title_keywords = UNSET
        elif isinstance(self.title_keywords, list):
            title_keywords = self.title_keywords

        else:
            title_keywords = self.title_keywords

        to_seniority: list[str] | None | Unset
        if isinstance(self.to_seniority, Unset):
            to_seniority = UNSET
        elif isinstance(self.to_seniority, list):
            to_seniority = []
            for to_seniority_type_0_item_data in self.to_seniority:
                to_seniority_type_0_item = to_seniority_type_0_item_data.value
                to_seniority.append(to_seniority_type_0_item)

        else:
            to_seniority = self.to_seniority

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
        if title_keywords is not UNSET:
            field_dict["titleKeywords"] = title_keywords
        if to_seniority is not UNSET:
            field_dict["toSeniority"] = to_seniority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["person_title_changed"], d.pop("type"))
        if type_ != "person_title_changed":
            raise ValueError(f"type must match const 'person_title_changed', got '{type_}'")

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

        is_dummy = d.pop("isDummy", UNSET)

        def _parse_title_keywords(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                title_keywords_type_0 = cast(list[str], data)

                return title_keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        title_keywords = _parse_title_keywords(d.pop("titleKeywords", UNSET))

        def _parse_to_seniority(data: object) -> list[PersonTitleChangedToSeniorityType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                to_seniority_type_0 = []
                _to_seniority_type_0 = data
                for to_seniority_type_0_item_data in _to_seniority_type_0:
                    to_seniority_type_0_item = PersonTitleChangedToSeniorityType0Item(to_seniority_type_0_item_data)

                    to_seniority_type_0.append(to_seniority_type_0_item)

                return to_seniority_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PersonTitleChangedToSeniorityType0Item] | None | Unset, data)

        to_seniority = _parse_to_seniority(d.pop("toSeniority", UNSET))

        person_title_changed = cls(
            type_=type_,
            entity_type=entity_type,
            lookback_days=lookback_days,
            is_dummy=is_dummy,
            title_keywords=title_keywords,
            to_seniority=to_seniority,
        )

        person_title_changed.additional_properties = d
        return person_title_changed

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
