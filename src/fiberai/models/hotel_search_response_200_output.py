from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hotel_search_response_200_output_brands_item import HotelSearchResponse200OutputBrandsItem
    from ..models.hotel_search_response_200_output_properties_item import HotelSearchResponse200OutputPropertiesItem
    from ..models.hotel_search_response_200_output_search_information_type_0 import (
        HotelSearchResponse200OutputSearchInformationType0,
    )


T = TypeVar("T", bound="HotelSearchResponse200Output")


@_attrs_define
class HotelSearchResponse200Output:
    """
    Attributes:
        properties (list[HotelSearchResponse200OutputPropertiesItem]): Matching hotel and vacation rental properties.
        brands (list[HotelSearchResponse200OutputBrandsItem]): Hotel brand groups available for filtering in this
            market. Empty when searching vacation rentals only.
        next_page_token (None | str | Unset): Token to retrieve the next page. Pass as `nextPageToken` in the next
            request. Null if no more pages.
        currency_code (None | str | Unset): ISO 4217 currency code for prices in this response (e.g. 'USD', 'EUR',
            'GBP').
        search_information (HotelSearchResponse200OutputSearchInformationType0 | None | Unset): Summary information
            about the search results.
    """

    properties: list[HotelSearchResponse200OutputPropertiesItem]
    brands: list[HotelSearchResponse200OutputBrandsItem]
    next_page_token: None | str | Unset = UNSET
    currency_code: None | str | Unset = UNSET
    search_information: HotelSearchResponse200OutputSearchInformationType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hotel_search_response_200_output_search_information_type_0 import (
            HotelSearchResponse200OutputSearchInformationType0,
        )

        properties = []
        for properties_item_data in self.properties:
            properties_item = properties_item_data.to_dict()
            properties.append(properties_item)

        brands = []
        for brands_item_data in self.brands:
            brands_item = brands_item_data.to_dict()
            brands.append(brands_item)

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        currency_code: None | str | Unset
        if isinstance(self.currency_code, Unset):
            currency_code = UNSET
        else:
            currency_code = self.currency_code

        search_information: dict[str, Any] | None | Unset
        if isinstance(self.search_information, Unset):
            search_information = UNSET
        elif isinstance(self.search_information, HotelSearchResponse200OutputSearchInformationType0):
            search_information = self.search_information.to_dict()
        else:
            search_information = self.search_information

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "properties": properties,
                "brands": brands,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if search_information is not UNSET:
            field_dict["searchInformation"] = search_information

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hotel_search_response_200_output_brands_item import HotelSearchResponse200OutputBrandsItem
        from ..models.hotel_search_response_200_output_properties_item import HotelSearchResponse200OutputPropertiesItem
        from ..models.hotel_search_response_200_output_search_information_type_0 import (
            HotelSearchResponse200OutputSearchInformationType0,
        )

        d = dict(src_dict)
        properties = []
        _properties = d.pop("properties")
        for properties_item_data in _properties:
            properties_item = HotelSearchResponse200OutputPropertiesItem.from_dict(properties_item_data)

            properties.append(properties_item)

        brands = []
        _brands = d.pop("brands")
        for brands_item_data in _brands:
            brands_item = HotelSearchResponse200OutputBrandsItem.from_dict(brands_item_data)

            brands.append(brands_item)

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        def _parse_currency_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_code = _parse_currency_code(d.pop("currencyCode", UNSET))

        def _parse_search_information(
            data: object,
        ) -> HotelSearchResponse200OutputSearchInformationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                search_information_type_0 = HotelSearchResponse200OutputSearchInformationType0.from_dict(data)

                return search_information_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HotelSearchResponse200OutputSearchInformationType0 | None | Unset, data)

        search_information = _parse_search_information(d.pop("searchInformation", UNSET))

        hotel_search_response_200_output = cls(
            properties=properties,
            brands=brands,
            next_page_token=next_page_token,
            currency_code=currency_code,
            search_information=search_information,
        )

        hotel_search_response_200_output.additional_properties = d
        return hotel_search_response_200_output

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
