from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hotel_property_response_200_output_property_offers_item_rate_per_night_type_0 import (
        HotelPropertyResponse200OutputPropertyOffersItemRatePerNightType0,
    )
    from ..models.hotel_property_response_200_output_property_offers_item_total_rate_type_0 import (
        HotelPropertyResponse200OutputPropertyOffersItemTotalRateType0,
    )


T = TypeVar("T", bound="HotelPropertyResponse200OutputPropertyOffersItem")


@_attrs_define
class HotelPropertyResponse200OutputPropertyOffersItem:
    """
    Attributes:
        source_name (None | str | Unset): Booking source name.
        logo_url (None | str | Unset): Booking source logo URL.
        url (None | str | Unset): Booking URL.
        is_official (bool | None | Unset): True when this is the property's official booking channel.
        rate_per_night (HotelPropertyResponse200OutputPropertyOffersItemRatePerNightType0 | None | Unset): Nightly rate
            from this source.
        total_rate (HotelPropertyResponse200OutputPropertyOffersItemTotalRateType0 | None | Unset): Total rate for the
            entire requested stay from this source. The all-in amount includes taxes and fees when supplied; otherwise
            `baseCost` is provided.
    """

    source_name: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    is_official: bool | None | Unset = UNSET
    rate_per_night: HotelPropertyResponse200OutputPropertyOffersItemRatePerNightType0 | None | Unset = UNSET
    total_rate: HotelPropertyResponse200OutputPropertyOffersItemTotalRateType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hotel_property_response_200_output_property_offers_item_rate_per_night_type_0 import (
            HotelPropertyResponse200OutputPropertyOffersItemRatePerNightType0,
        )
        from ..models.hotel_property_response_200_output_property_offers_item_total_rate_type_0 import (
            HotelPropertyResponse200OutputPropertyOffersItemTotalRateType0,
        )

        source_name: None | str | Unset
        if isinstance(self.source_name, Unset):
            source_name = UNSET
        else:
            source_name = self.source_name

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        is_official: bool | None | Unset
        if isinstance(self.is_official, Unset):
            is_official = UNSET
        else:
            is_official = self.is_official

        rate_per_night: dict[str, Any] | None | Unset
        if isinstance(self.rate_per_night, Unset):
            rate_per_night = UNSET
        elif isinstance(self.rate_per_night, HotelPropertyResponse200OutputPropertyOffersItemRatePerNightType0):
            rate_per_night = self.rate_per_night.to_dict()
        else:
            rate_per_night = self.rate_per_night

        total_rate: dict[str, Any] | None | Unset
        if isinstance(self.total_rate, Unset):
            total_rate = UNSET
        elif isinstance(self.total_rate, HotelPropertyResponse200OutputPropertyOffersItemTotalRateType0):
            total_rate = self.total_rate.to_dict()
        else:
            total_rate = self.total_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_name is not UNSET:
            field_dict["sourceName"] = source_name
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if url is not UNSET:
            field_dict["url"] = url
        if is_official is not UNSET:
            field_dict["isOfficial"] = is_official
        if rate_per_night is not UNSET:
            field_dict["ratePerNight"] = rate_per_night
        if total_rate is not UNSET:
            field_dict["totalRate"] = total_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hotel_property_response_200_output_property_offers_item_rate_per_night_type_0 import (
            HotelPropertyResponse200OutputPropertyOffersItemRatePerNightType0,
        )
        from ..models.hotel_property_response_200_output_property_offers_item_total_rate_type_0 import (
            HotelPropertyResponse200OutputPropertyOffersItemTotalRateType0,
        )

        d = dict(src_dict)

        def _parse_source_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_name = _parse_source_name(d.pop("sourceName", UNSET))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logoUrl", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_is_official(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_official = _parse_is_official(d.pop("isOfficial", UNSET))

        def _parse_rate_per_night(
            data: object,
        ) -> HotelPropertyResponse200OutputPropertyOffersItemRatePerNightType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rate_per_night_type_0 = HotelPropertyResponse200OutputPropertyOffersItemRatePerNightType0.from_dict(
                    data
                )

                return rate_per_night_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HotelPropertyResponse200OutputPropertyOffersItemRatePerNightType0 | None | Unset, data)

        rate_per_night = _parse_rate_per_night(d.pop("ratePerNight", UNSET))

        def _parse_total_rate(
            data: object,
        ) -> HotelPropertyResponse200OutputPropertyOffersItemTotalRateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                total_rate_type_0 = HotelPropertyResponse200OutputPropertyOffersItemTotalRateType0.from_dict(data)

                return total_rate_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HotelPropertyResponse200OutputPropertyOffersItemTotalRateType0 | None | Unset, data)

        total_rate = _parse_total_rate(d.pop("totalRate", UNSET))

        hotel_property_response_200_output_property_offers_item = cls(
            source_name=source_name,
            logo_url=logo_url,
            url=url,
            is_official=is_official,
            rate_per_night=rate_per_night,
            total_rate=total_rate,
        )

        hotel_property_response_200_output_property_offers_item.additional_properties = d
        return hotel_property_response_200_output_property_offers_item

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
