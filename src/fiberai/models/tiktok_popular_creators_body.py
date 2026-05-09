from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tiktok_popular_creators_body_country_type_1 import TiktokPopularCreatorsBodyCountryType1
from ..models.tiktok_popular_creators_body_country_type_2_type_1 import TiktokPopularCreatorsBodyCountryType2Type1
from ..models.tiktok_popular_creators_body_country_type_3_type_1 import TiktokPopularCreatorsBodyCountryType3Type1
from ..models.tiktok_popular_creators_body_sort_type_1 import TiktokPopularCreatorsBodySortType1
from ..models.tiktok_popular_creators_body_sort_type_2_type_1 import TiktokPopularCreatorsBodySortType2Type1
from ..models.tiktok_popular_creators_body_sort_type_3_type_1 import TiktokPopularCreatorsBodySortType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="TiktokPopularCreatorsBody")


@_attrs_define
class TiktokPopularCreatorsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        country (None | TiktokPopularCreatorsBodyCountryType1 | TiktokPopularCreatorsBodyCountryType2Type1 |
            TiktokPopularCreatorsBodyCountryType3Type1 | Unset): ISO 3166-1 alpha-3 country code to filter by (e.g. 'USA').
            Omit for global results.
        sort (None | TiktokPopularCreatorsBodySortType1 | TiktokPopularCreatorsBodySortType2Type1 |
            TiktokPopularCreatorsBodySortType3Type1 | Unset): Sort results in descending order. Omit for default ranking.
    """

    api_key: str
    country: (
        None
        | TiktokPopularCreatorsBodyCountryType1
        | TiktokPopularCreatorsBodyCountryType2Type1
        | TiktokPopularCreatorsBodyCountryType3Type1
        | Unset
    ) = UNSET
    sort: (
        None
        | TiktokPopularCreatorsBodySortType1
        | TiktokPopularCreatorsBodySortType2Type1
        | TiktokPopularCreatorsBodySortType3Type1
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        elif isinstance(self.country, TiktokPopularCreatorsBodyCountryType1):
            country = self.country.value
        elif isinstance(self.country, TiktokPopularCreatorsBodyCountryType2Type1):
            country = self.country.value
        elif isinstance(self.country, TiktokPopularCreatorsBodyCountryType3Type1):
            country = self.country.value
        else:
            country = self.country

        sort: None | str | Unset
        if isinstance(self.sort, Unset):
            sort = UNSET
        elif isinstance(self.sort, TiktokPopularCreatorsBodySortType1):
            sort = self.sort.value
        elif isinstance(self.sort, TiktokPopularCreatorsBodySortType2Type1):
            sort = self.sort.value
        elif isinstance(self.sort, TiktokPopularCreatorsBodySortType3Type1):
            sort = self.sort.value
        else:
            sort = self.sort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
            }
        )
        if country is not UNSET:
            field_dict["country"] = country
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_country(
            data: object,
        ) -> (
            None
            | TiktokPopularCreatorsBodyCountryType1
            | TiktokPopularCreatorsBodyCountryType2Type1
            | TiktokPopularCreatorsBodyCountryType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_type_1 = TiktokPopularCreatorsBodyCountryType1(data)

                return country_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_type_2_type_1 = TiktokPopularCreatorsBodyCountryType2Type1(data)

                return country_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_type_3_type_1 = TiktokPopularCreatorsBodyCountryType3Type1(data)

                return country_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TiktokPopularCreatorsBodyCountryType1
                | TiktokPopularCreatorsBodyCountryType2Type1
                | TiktokPopularCreatorsBodyCountryType3Type1
                | Unset,
                data,
            )

        country = _parse_country(d.pop("country", UNSET))

        def _parse_sort(
            data: object,
        ) -> (
            None
            | TiktokPopularCreatorsBodySortType1
            | TiktokPopularCreatorsBodySortType2Type1
            | TiktokPopularCreatorsBodySortType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_type_1 = TiktokPopularCreatorsBodySortType1(data)

                return sort_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_type_2_type_1 = TiktokPopularCreatorsBodySortType2Type1(data)

                return sort_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_type_3_type_1 = TiktokPopularCreatorsBodySortType3Type1(data)

                return sort_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TiktokPopularCreatorsBodySortType1
                | TiktokPopularCreatorsBodySortType2Type1
                | TiktokPopularCreatorsBodySortType3Type1
                | Unset,
                data,
            )

        sort = _parse_sort(d.pop("sort", UNSET))

        tiktok_popular_creators_body = cls(
            api_key=api_key,
            country=country,
            sort=sort,
        )

        tiktok_popular_creators_body.additional_properties = d
        return tiktok_popular_creators_body

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
