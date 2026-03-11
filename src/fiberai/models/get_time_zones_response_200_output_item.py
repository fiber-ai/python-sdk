from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTimeZonesResponse200OutputItem")


@_attrs_define
class GetTimeZonesResponse200OutputItem:
    """
    Attributes:
        time_zone_name (str): The IANA timezone identifier (e.g., 'America/New_York')
        min_utc_offset_minutes (int): The minimum (most negative) offset from UTC at any point in the year, in minutes.
            Time zones that observe Daylight Savings will always have a max offset that's 60 greater than their min offset.
        max_utc_offset_minutes (int): The maximum (most positive) offset from UTC at any point in the year, in minutes.
            Time zones that observe Daylight Savings will always have a max offset that's 60 greater than their min offset.
        main_cities (list[str]): Major cities in this timezone
        alternative_name (str): Alternative/common name for the timezone
        sub_zones (list[str]): Related timezone variants that share geographic proximity or similar time offset
            behaviors (e.g., Mountain Time zones in British Columbia: 'America/Creston', 'America/Dawson_Creek',
            'America/Fort_Nelson')
        current_utc_offset_minutes (int): Current UTC offset in minutes
        current_local_time (str): Current time in this timezone, formatted as an ISO 8601 string.
        abbreviation (str): Current timezone abbreviation (e.g., 'EST', 'PDT')
        display_name (str): Human-friendly display name
        is_daylight_saving (bool): Whether the time zone is currently in Daylight Savings time.
        continent_code (None | str | Unset): Continent code (e.g., 'NA' for North America)
        continent_name (None | str | Unset): Continent name (e.g., 'North America')
        country_name (None | str | Unset): Country name (e.g., 'United States')
        country_code_alpha_2 (None | str | Unset): ISO country code (e.g., 'US'). This is a 2 letter code.
    """

    time_zone_name: str
    min_utc_offset_minutes: int
    max_utc_offset_minutes: int
    main_cities: list[str]
    alternative_name: str
    sub_zones: list[str]
    current_utc_offset_minutes: int
    current_local_time: str
    abbreviation: str
    display_name: str
    is_daylight_saving: bool
    continent_code: None | str | Unset = UNSET
    continent_name: None | str | Unset = UNSET
    country_name: None | str | Unset = UNSET
    country_code_alpha_2: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_zone_name = self.time_zone_name

        min_utc_offset_minutes = self.min_utc_offset_minutes

        max_utc_offset_minutes = self.max_utc_offset_minutes

        main_cities = self.main_cities

        alternative_name = self.alternative_name

        sub_zones = self.sub_zones

        current_utc_offset_minutes = self.current_utc_offset_minutes

        current_local_time = self.current_local_time

        abbreviation = self.abbreviation

        display_name = self.display_name

        is_daylight_saving = self.is_daylight_saving

        continent_code: None | str | Unset
        if isinstance(self.continent_code, Unset):
            continent_code = UNSET
        else:
            continent_code = self.continent_code

        continent_name: None | str | Unset
        if isinstance(self.continent_name, Unset):
            continent_name = UNSET
        else:
            continent_name = self.continent_name

        country_name: None | str | Unset
        if isinstance(self.country_name, Unset):
            country_name = UNSET
        else:
            country_name = self.country_name

        country_code_alpha_2: None | str | Unset
        if isinstance(self.country_code_alpha_2, Unset):
            country_code_alpha_2 = UNSET
        else:
            country_code_alpha_2 = self.country_code_alpha_2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timeZoneName": time_zone_name,
                "minUtcOffsetMinutes": min_utc_offset_minutes,
                "maxUtcOffsetMinutes": max_utc_offset_minutes,
                "mainCities": main_cities,
                "alternativeName": alternative_name,
                "subZones": sub_zones,
                "currentUtcOffsetMinutes": current_utc_offset_minutes,
                "currentLocalTime": current_local_time,
                "abbreviation": abbreviation,
                "displayName": display_name,
                "isDaylightSaving": is_daylight_saving,
            }
        )
        if continent_code is not UNSET:
            field_dict["continentCode"] = continent_code
        if continent_name is not UNSET:
            field_dict["continentName"] = continent_name
        if country_name is not UNSET:
            field_dict["countryName"] = country_name
        if country_code_alpha_2 is not UNSET:
            field_dict["countryCodeAlpha2"] = country_code_alpha_2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time_zone_name = d.pop("timeZoneName")

        min_utc_offset_minutes = d.pop("minUtcOffsetMinutes")

        max_utc_offset_minutes = d.pop("maxUtcOffsetMinutes")

        main_cities = cast(list[str], d.pop("mainCities"))

        alternative_name = d.pop("alternativeName")

        sub_zones = cast(list[str], d.pop("subZones"))

        current_utc_offset_minutes = d.pop("currentUtcOffsetMinutes")

        current_local_time = d.pop("currentLocalTime")

        abbreviation = d.pop("abbreviation")

        display_name = d.pop("displayName")

        is_daylight_saving = d.pop("isDaylightSaving")

        def _parse_continent_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        continent_code = _parse_continent_code(d.pop("continentCode", UNSET))

        def _parse_continent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        continent_name = _parse_continent_name(d.pop("continentName", UNSET))

        def _parse_country_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_name = _parse_country_name(d.pop("countryName", UNSET))

        def _parse_country_code_alpha_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code_alpha_2 = _parse_country_code_alpha_2(d.pop("countryCodeAlpha2", UNSET))

        get_time_zones_response_200_output_item = cls(
            time_zone_name=time_zone_name,
            min_utc_offset_minutes=min_utc_offset_minutes,
            max_utc_offset_minutes=max_utc_offset_minutes,
            main_cities=main_cities,
            alternative_name=alternative_name,
            sub_zones=sub_zones,
            current_utc_offset_minutes=current_utc_offset_minutes,
            current_local_time=current_local_time,
            abbreviation=abbreviation,
            display_name=display_name,
            is_daylight_saving=is_daylight_saving,
            continent_code=continent_code,
            continent_name=continent_name,
            country_name=country_name,
            country_code_alpha_2=country_code_alpha_2,
        )

        get_time_zones_response_200_output_item.additional_properties = d
        return get_time_zones_response_200_output_item

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
