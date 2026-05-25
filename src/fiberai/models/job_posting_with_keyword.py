from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_posting_with_keyword_location_types_type_0_item import JobPostingWithKeywordLocationTypesType0Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobPostingWithKeyword")


@_attrs_define
class JobPostingWithKeyword:
    """
    Attributes:
        type_ (Literal['job_posting_with_keyword']):
        entity_type (Literal['company']):
        keywords (list[str]): Alert when a job posting title contains any of these keywords
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        seniority_levels (list[str] | None | Unset): Only alert for these seniority levels. Omit for any level.
        location_types (list[JobPostingWithKeywordLocationTypesType0Item] | None | Unset): Only alert for these location
            types. Omit for any.
    """

    type_: Literal["job_posting_with_keyword"]
    entity_type: Literal["company"]
    keywords: list[str]
    lookback_days: int | None | Unset = UNSET
    seniority_levels: list[str] | None | Unset = UNSET
    location_types: list[JobPostingWithKeywordLocationTypesType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        keywords = self.keywords

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        seniority_levels: list[str] | None | Unset
        if isinstance(self.seniority_levels, Unset):
            seniority_levels = UNSET
        elif isinstance(self.seniority_levels, list):
            seniority_levels = self.seniority_levels

        else:
            seniority_levels = self.seniority_levels

        location_types: list[str] | None | Unset
        if isinstance(self.location_types, Unset):
            location_types = UNSET
        elif isinstance(self.location_types, list):
            location_types = []
            for location_types_type_0_item_data in self.location_types:
                location_types_type_0_item = location_types_type_0_item_data.value
                location_types.append(location_types_type_0_item)

        else:
            location_types = self.location_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "entityType": entity_type,
                "keywords": keywords,
            }
        )
        if lookback_days is not UNSET:
            field_dict["lookbackDays"] = lookback_days
        if seniority_levels is not UNSET:
            field_dict["seniorityLevels"] = seniority_levels
        if location_types is not UNSET:
            field_dict["locationTypes"] = location_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["job_posting_with_keyword"], d.pop("type"))
        if type_ != "job_posting_with_keyword":
            raise ValueError(f"type must match const 'job_posting_with_keyword', got '{type_}'")

        entity_type = cast(Literal["company"], d.pop("entityType"))
        if entity_type != "company":
            raise ValueError(f"entityType must match const 'company', got '{entity_type}'")

        keywords = cast(list[str], d.pop("keywords"))

        def _parse_lookback_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        def _parse_seniority_levels(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                seniority_levels_type_0 = cast(list[str], data)

                return seniority_levels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        seniority_levels = _parse_seniority_levels(d.pop("seniorityLevels", UNSET))

        def _parse_location_types(data: object) -> list[JobPostingWithKeywordLocationTypesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                location_types_type_0 = []
                _location_types_type_0 = data
                for location_types_type_0_item_data in _location_types_type_0:
                    location_types_type_0_item = JobPostingWithKeywordLocationTypesType0Item(
                        location_types_type_0_item_data
                    )

                    location_types_type_0.append(location_types_type_0_item)

                return location_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[JobPostingWithKeywordLocationTypesType0Item] | None | Unset, data)

        location_types = _parse_location_types(d.pop("locationTypes", UNSET))

        job_posting_with_keyword = cls(
            type_=type_,
            entity_type=entity_type,
            keywords=keywords,
            lookback_days=lookback_days,
            seniority_levels=seniority_levels,
            location_types=location_types,
        )

        job_posting_with_keyword.additional_properties = d
        return job_posting_with_keyword

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
