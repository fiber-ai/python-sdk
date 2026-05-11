from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlightSearchBodyConnectingAirportsType0")


@_attrs_define
class FlightSearchBodyConnectingAirportsType0:
    """Filter by connecting airports. By default all connecting airports are allowed. We recommend not passing this unless
    you have a good reason — it significantly reduces the number of results returned.

        Attributes:
            include (list[str] | None | Unset): Only allow itineraries connecting through at least one of these IATA
                airports (e.g. 'DFW', 'SFO'). Nonstop flights and itineraries that don't match are filtered out. Narrow
                allowlists may return zero results. Case-insensitive.
            exclude (list[str] | None | Unset): Drop itineraries connecting through any of these IATA airports (e.g. 'ORD',
                'ATL'). Case-insensitive.
    """

    include: list[str] | None | Unset = UNSET
    exclude: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include: list[str] | None | Unset
        if isinstance(self.include, Unset):
            include = UNSET
        elif isinstance(self.include, list):
            include = self.include

        else:
            include = self.include

        exclude: list[str] | None | Unset
        if isinstance(self.exclude, Unset):
            exclude = UNSET
        elif isinstance(self.exclude, list):
            exclude = self.exclude

        else:
            exclude = self.exclude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include is not UNSET:
            field_dict["include"] = include
        if exclude is not UNSET:
            field_dict["exclude"] = exclude

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_include(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                include_type_0 = cast(list[str], data)

                return include_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        include = _parse_include(d.pop("include", UNSET))

        def _parse_exclude(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclude_type_0 = cast(list[str], data)

                return exclude_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exclude = _parse_exclude(d.pop("exclude", UNSET))

        flight_search_body_connecting_airports_type_0 = cls(
            include=include,
            exclude=exclude,
        )

        flight_search_body_connecting_airports_type_0.additional_properties = d
        return flight_search_body_connecting_airports_type_0

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
