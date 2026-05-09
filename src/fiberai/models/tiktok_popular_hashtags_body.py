from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tiktok_popular_hashtags_body_country_type_1 import TiktokPopularHashtagsBodyCountryType1
from ..models.tiktok_popular_hashtags_body_country_type_2_type_1 import TiktokPopularHashtagsBodyCountryType2Type1
from ..models.tiktok_popular_hashtags_body_country_type_3_type_1 import TiktokPopularHashtagsBodyCountryType3Type1
from ..models.tiktok_popular_hashtags_body_period_days_type_0 import TiktokPopularHashtagsBodyPeriodDaysType0
from ..models.tiktok_popular_hashtags_body_period_days_type_1 import TiktokPopularHashtagsBodyPeriodDaysType1
from ..models.tiktok_popular_hashtags_body_period_days_type_2 import TiktokPopularHashtagsBodyPeriodDaysType2
from ..types import UNSET, Unset

T = TypeVar("T", bound="TiktokPopularHashtagsBody")


@_attrs_define
class TiktokPopularHashtagsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        country (None | TiktokPopularHashtagsBodyCountryType1 | TiktokPopularHashtagsBodyCountryType2Type1 |
            TiktokPopularHashtagsBodyCountryType3Type1 | Unset): ISO 3166-1 alpha-3 country code to filter by (e.g. 'USA').
            Omit for global results.
        period_days (None | TiktokPopularHashtagsBodyPeriodDaysType0 | TiktokPopularHashtagsBodyPeriodDaysType1 |
            TiktokPopularHashtagsBodyPeriodDaysType2 | Unset): Time period in days for trending data: 7, 30, or 120. Omit
            for default (7).
    """

    api_key: str
    country: (
        None
        | TiktokPopularHashtagsBodyCountryType1
        | TiktokPopularHashtagsBodyCountryType2Type1
        | TiktokPopularHashtagsBodyCountryType3Type1
        | Unset
    ) = UNSET
    period_days: (
        None
        | TiktokPopularHashtagsBodyPeriodDaysType0
        | TiktokPopularHashtagsBodyPeriodDaysType1
        | TiktokPopularHashtagsBodyPeriodDaysType2
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        elif isinstance(self.country, TiktokPopularHashtagsBodyCountryType1):
            country = self.country.value
        elif isinstance(self.country, TiktokPopularHashtagsBodyCountryType2Type1):
            country = self.country.value
        elif isinstance(self.country, TiktokPopularHashtagsBodyCountryType3Type1):
            country = self.country.value
        else:
            country = self.country

        period_days: int | None | Unset
        if isinstance(self.period_days, Unset):
            period_days = UNSET
        elif isinstance(self.period_days, TiktokPopularHashtagsBodyPeriodDaysType0):
            period_days = self.period_days.value
        elif isinstance(self.period_days, TiktokPopularHashtagsBodyPeriodDaysType1):
            period_days = self.period_days.value
        elif isinstance(self.period_days, TiktokPopularHashtagsBodyPeriodDaysType2):
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
            | TiktokPopularHashtagsBodyCountryType1
            | TiktokPopularHashtagsBodyCountryType2Type1
            | TiktokPopularHashtagsBodyCountryType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_type_1 = TiktokPopularHashtagsBodyCountryType1(data)

                return country_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_type_2_type_1 = TiktokPopularHashtagsBodyCountryType2Type1(data)

                return country_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_type_3_type_1 = TiktokPopularHashtagsBodyCountryType3Type1(data)

                return country_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TiktokPopularHashtagsBodyCountryType1
                | TiktokPopularHashtagsBodyCountryType2Type1
                | TiktokPopularHashtagsBodyCountryType3Type1
                | Unset,
                data,
            )

        country = _parse_country(d.pop("country", UNSET))

        def _parse_period_days(
            data: object,
        ) -> (
            None
            | TiktokPopularHashtagsBodyPeriodDaysType0
            | TiktokPopularHashtagsBodyPeriodDaysType1
            | TiktokPopularHashtagsBodyPeriodDaysType2
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                period_days_type_0 = TiktokPopularHashtagsBodyPeriodDaysType0(data)

                return period_days_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                period_days_type_1 = TiktokPopularHashtagsBodyPeriodDaysType1(data)

                return period_days_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                period_days_type_2 = TiktokPopularHashtagsBodyPeriodDaysType2(data)

                return period_days_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TiktokPopularHashtagsBodyPeriodDaysType0
                | TiktokPopularHashtagsBodyPeriodDaysType1
                | TiktokPopularHashtagsBodyPeriodDaysType2
                | Unset,
                data,
            )

        period_days = _parse_period_days(d.pop("periodDays", UNSET))

        tiktok_popular_hashtags_body = cls(
            api_key=api_key,
            country=country,
            period_days=period_days,
        )

        tiktok_popular_hashtags_body.additional_properties = d
        return tiktok_popular_hashtags_body

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
