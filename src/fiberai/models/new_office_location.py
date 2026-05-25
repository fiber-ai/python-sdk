from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewOfficeLocation")


@_attrs_define
class NewOfficeLocation:
    """
    Attributes:
        type_ (Literal['new_office_location']):
        entity_type (Literal['company']):
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        countries (list[str] | None | Unset): Only alert for offices in these countries. Omit for any new office.
        cities (list[str] | None | Unset): Only alert for offices in these cities. Omit for any new office.
    """

    type_: Literal["new_office_location"]
    entity_type: Literal["company"]
    lookback_days: int | None | Unset = UNSET
    countries: list[str] | None | Unset = UNSET
    cities: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        countries: list[str] | None | Unset
        if isinstance(self.countries, Unset):
            countries = UNSET
        elif isinstance(self.countries, list):
            countries = self.countries

        else:
            countries = self.countries

        cities: list[str] | None | Unset
        if isinstance(self.cities, Unset):
            cities = UNSET
        elif isinstance(self.cities, list):
            cities = self.cities

        else:
            cities = self.cities

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
        if countries is not UNSET:
            field_dict["countries"] = countries
        if cities is not UNSET:
            field_dict["cities"] = cities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["new_office_location"], d.pop("type"))
        if type_ != "new_office_location":
            raise ValueError(f"type must match const 'new_office_location', got '{type_}'")

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

        def _parse_countries(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                countries_type_0 = cast(list[str], data)

                return countries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        countries = _parse_countries(d.pop("countries", UNSET))

        def _parse_cities(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cities_type_0 = cast(list[str], data)

                return cities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        cities = _parse_cities(d.pop("cities", UNSET))

        new_office_location = cls(
            type_=type_,
            entity_type=entity_type,
            lookback_days=lookback_days,
            countries=countries,
            cities=cities,
        )

        new_office_location.additional_properties = d
        return new_office_location

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
