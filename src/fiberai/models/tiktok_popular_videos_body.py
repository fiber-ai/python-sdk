from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tiktok_popular_videos_body_country_type_1 import TiktokPopularVideosBodyCountryType1
from ..models.tiktok_popular_videos_body_country_type_2_type_1 import TiktokPopularVideosBodyCountryType2Type1
from ..models.tiktok_popular_videos_body_country_type_3_type_1 import TiktokPopularVideosBodyCountryType3Type1
from ..models.tiktok_popular_videos_body_period_days_type_0 import TiktokPopularVideosBodyPeriodDaysType0
from ..models.tiktok_popular_videos_body_period_days_type_1 import TiktokPopularVideosBodyPeriodDaysType1
from ..types import UNSET, Unset

T = TypeVar("T", bound="TiktokPopularVideosBody")


@_attrs_define
class TiktokPopularVideosBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        country (None | TiktokPopularVideosBodyCountryType1 | TiktokPopularVideosBodyCountryType2Type1 |
            TiktokPopularVideosBodyCountryType3Type1 | Unset): ISO 3166-1 alpha-3 country code to filter by (e.g. 'USA').
            Omit for global results.
        period_days (None | TiktokPopularVideosBodyPeriodDaysType0 | TiktokPopularVideosBodyPeriodDaysType1 | Unset):
            Time period in days for trending data: 7 or 30. Omit for default (7).
    """

    api_key: str
    country: (
        None
        | TiktokPopularVideosBodyCountryType1
        | TiktokPopularVideosBodyCountryType2Type1
        | TiktokPopularVideosBodyCountryType3Type1
        | Unset
    ) = UNSET
    period_days: None | TiktokPopularVideosBodyPeriodDaysType0 | TiktokPopularVideosBodyPeriodDaysType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        elif isinstance(self.country, TiktokPopularVideosBodyCountryType1):
            country = self.country.value
        elif isinstance(self.country, TiktokPopularVideosBodyCountryType2Type1):
            country = self.country.value
        elif isinstance(self.country, TiktokPopularVideosBodyCountryType3Type1):
            country = self.country.value
        else:
            country = self.country

        period_days: int | None | Unset
        if isinstance(self.period_days, Unset):
            period_days = UNSET
        elif isinstance(self.period_days, TiktokPopularVideosBodyPeriodDaysType0):
            period_days = self.period_days.value
        elif isinstance(self.period_days, TiktokPopularVideosBodyPeriodDaysType1):
            period_days = self.period_days.value
        else:
            period_days = self.period_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
            }
        )
        if country is not UNSET:
            field_dict["country"] = country
        if period_days is not UNSET:
            field_dict["periodDays"] = period_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_country(
            data: object,
        ) -> (
            None
            | TiktokPopularVideosBodyCountryType1
            | TiktokPopularVideosBodyCountryType2Type1
            | TiktokPopularVideosBodyCountryType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_type_1 = TiktokPopularVideosBodyCountryType1(data)

                return country_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_type_2_type_1 = TiktokPopularVideosBodyCountryType2Type1(data)

                return country_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_type_3_type_1 = TiktokPopularVideosBodyCountryType3Type1(data)

                return country_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TiktokPopularVideosBodyCountryType1
                | TiktokPopularVideosBodyCountryType2Type1
                | TiktokPopularVideosBodyCountryType3Type1
                | Unset,
                data,
            )

        country = _parse_country(d.pop("country", UNSET))

        def _parse_period_days(
            data: object,
        ) -> None | TiktokPopularVideosBodyPeriodDaysType0 | TiktokPopularVideosBodyPeriodDaysType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                period_days_type_0 = TiktokPopularVideosBodyPeriodDaysType0(data)

                return period_days_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                period_days_type_1 = TiktokPopularVideosBodyPeriodDaysType1(data)

                return period_days_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TiktokPopularVideosBodyPeriodDaysType0 | TiktokPopularVideosBodyPeriodDaysType1 | Unset, data
            )

        period_days = _parse_period_days(d.pop("periodDays", UNSET))

        tiktok_popular_videos_body = cls(
            api_key=api_key,
            country=country,
            period_days=period_days,
        )

        tiktok_popular_videos_body.additional_properties = d
        return tiktok_popular_videos_body

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
