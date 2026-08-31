from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fetch_real_estate_listings_response_200_output_properties_item_rental_units_type_0_item_price_type_0 import (
        FetchRealEstateListingsResponse200OutputPropertiesItemRentalUnitsType0ItemPriceType0,
    )


T = TypeVar("T", bound="FetchRealEstateListingsResponse200OutputPropertiesItemRentalUnitsType0Item")


@_attrs_define
class FetchRealEstateListingsResponse200OutputPropertiesItemRentalUnitsType0Item:
    """
    Attributes:
        price (FetchRealEstateListingsResponse200OutputPropertiesItemRentalUnitsType0ItemPriceType0 | None | Unset):
            Unit asking price in USD and local currency.
        bedroom_count (int | None | Unset): Number of bedrooms in the unit. 0 indicates a studio.
        is_room_for_rent (bool | None | Unset): Whether the unit is a single room for rent.
    """

    price: FetchRealEstateListingsResponse200OutputPropertiesItemRentalUnitsType0ItemPriceType0 | None | Unset = UNSET
    bedroom_count: int | None | Unset = UNSET
    is_room_for_rent: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_rental_units_type_0_item_price_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemRentalUnitsType0ItemPriceType0,  # noqa: PLC0415
        )

        price: dict[str, Any] | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        elif isinstance(
            self.price, FetchRealEstateListingsResponse200OutputPropertiesItemRentalUnitsType0ItemPriceType0
        ):
            price = self.price.to_dict()
        else:
            price = self.price

        bedroom_count: int | None | Unset
        if isinstance(self.bedroom_count, Unset):
            bedroom_count = UNSET
        else:
            bedroom_count = self.bedroom_count

        is_room_for_rent: bool | None | Unset
        if isinstance(self.is_room_for_rent, Unset):
            is_room_for_rent = UNSET
        else:
            is_room_for_rent = self.is_room_for_rent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price is not UNSET:
            field_dict["price"] = price
        if bedroom_count is not UNSET:
            field_dict["bedroomCount"] = bedroom_count
        if is_room_for_rent is not UNSET:
            field_dict["isRoomForRent"] = is_room_for_rent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_rental_units_type_0_item_price_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemRentalUnitsType0ItemPriceType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_price(
            data: object,
        ) -> FetchRealEstateListingsResponse200OutputPropertiesItemRentalUnitsType0ItemPriceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                price_type_0 = (
                    FetchRealEstateListingsResponse200OutputPropertiesItemRentalUnitsType0ItemPriceType0.from_dict(data)
                )

                return price_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FetchRealEstateListingsResponse200OutputPropertiesItemRentalUnitsType0ItemPriceType0 | None | Unset,
                data,
            )

        price = _parse_price(d.pop("price", UNSET))

        def _parse_bedroom_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bedroom_count = _parse_bedroom_count(d.pop("bedroomCount", UNSET))

        def _parse_is_room_for_rent(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_room_for_rent = _parse_is_room_for_rent(d.pop("isRoomForRent", UNSET))

        fetch_real_estate_listings_response_200_output_properties_item_rental_units_type_0_item = cls(
            price=price,
            bedroom_count=bedroom_count,
            is_room_for_rent=is_room_for_rent,
        )

        fetch_real_estate_listings_response_200_output_properties_item_rental_units_type_0_item.additional_properties = d
        return fetch_real_estate_listings_response_200_output_properties_item_rental_units_type_0_item

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
