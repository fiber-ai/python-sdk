from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonLocationChanged")


@_attrs_define
class PersonLocationChanged:
    """
    Attributes:
        type_ (Literal['person_location_changed']):
        entity_type (Literal['person']):
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        is_dummy (bool | Unset): When true, this rule only fires via the fire-dummy endpoint and is skipped during
            normal pipeline runs.
        to_countries (list[str] | None | Unset): ISO 3166-1 alpha-3 country codes (e.g. 'USA', 'GBR', 'DEU'). Only alert
            if moved to one of these countries. Omit for any relocation.
        from_countries (list[str] | None | Unset): Only alert if they moved FROM one of these countries. Omit for any.
        regions (list[str] | None | Unset): Region codes (e.g. 'X-EMEA', 'X-APAC'). Only alert if destination country is
            in one of these regions. Omit for any.
    """

    type_: Literal["person_location_changed"]
    entity_type: Literal["person"]
    lookback_days: int | None | Unset = UNSET
    is_dummy: bool | Unset = UNSET
    to_countries: list[str] | None | Unset = UNSET
    from_countries: list[str] | None | Unset = UNSET
    regions: list[str] | None | Unset = UNSET
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

        to_countries: list[str] | None | Unset
        if isinstance(self.to_countries, Unset):
            to_countries = UNSET
        elif isinstance(self.to_countries, list):
            to_countries = self.to_countries

        else:
            to_countries = self.to_countries

        from_countries: list[str] | None | Unset
        if isinstance(self.from_countries, Unset):
            from_countries = UNSET
        elif isinstance(self.from_countries, list):
            from_countries = self.from_countries

        else:
            from_countries = self.from_countries

        regions: list[str] | None | Unset
        if isinstance(self.regions, Unset):
            regions = UNSET
        elif isinstance(self.regions, list):
            regions = self.regions

        else:
            regions = self.regions

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
        if to_countries is not UNSET:
            field_dict["toCountries"] = to_countries
        if from_countries is not UNSET:
            field_dict["fromCountries"] = from_countries
        if regions is not UNSET:
            field_dict["regions"] = regions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["person_location_changed"], d.pop("type"))
        if type_ != "person_location_changed":
            raise ValueError(f"type must match const 'person_location_changed', got '{type_}'")

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

        def _parse_to_countries(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                to_countries_type_0 = cast(list[str], data)

                return to_countries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        to_countries = _parse_to_countries(d.pop("toCountries", UNSET))

        def _parse_from_countries(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                from_countries_type_0 = cast(list[str], data)

                return from_countries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        from_countries = _parse_from_countries(d.pop("fromCountries", UNSET))

        def _parse_regions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                regions_type_0 = cast(list[str], data)

                return regions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        regions = _parse_regions(d.pop("regions", UNSET))

        person_location_changed = cls(
            type_=type_,
            entity_type=entity_type,
            lookback_days=lookback_days,
            is_dummy=is_dummy,
            to_countries=to_countries,
            from_countries=from_countries,
            regions=regions,
        )

        person_location_changed.additional_properties = d
        return person_location_changed

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
