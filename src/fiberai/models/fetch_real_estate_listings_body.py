from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fetch_real_estate_listings_body_home_types_type_0_item import (
    FetchRealEstateListingsBodyHomeTypesType0Item,
)
from ..models.fetch_real_estate_listings_body_listing_status_type_1 import FetchRealEstateListingsBodyListingStatusType1
from ..models.fetch_real_estate_listings_body_listing_status_type_2_type_1 import (
    FetchRealEstateListingsBodyListingStatusType2Type1,
)
from ..models.fetch_real_estate_listings_body_listing_status_type_3_type_1 import (
    FetchRealEstateListingsBodyListingStatusType3Type1,
)
from ..models.fetch_real_estate_listings_body_sort_by_type_1 import FetchRealEstateListingsBodySortByType1
from ..models.fetch_real_estate_listings_body_sort_by_type_2_type_1 import FetchRealEstateListingsBodySortByType2Type1
from ..models.fetch_real_estate_listings_body_sort_by_type_3_type_1 import FetchRealEstateListingsBodySortByType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fetch_real_estate_listings_body_bathrooms_type_0 import FetchRealEstateListingsBodyBathroomsType0
    from ..models.fetch_real_estate_listings_body_bedrooms_type_0 import FetchRealEstateListingsBodyBedroomsType0
    from ..models.fetch_real_estate_listings_body_features_type_0 import FetchRealEstateListingsBodyFeaturesType0
    from ..models.fetch_real_estate_listings_body_floor_area_sq_ft_type_0 import (
        FetchRealEstateListingsBodyFloorAreaSqFtType0,
    )
    from ..models.fetch_real_estate_listings_body_location_type_0 import FetchRealEstateListingsBodyLocationType0
    from ..models.fetch_real_estate_listings_body_location_type_1 import FetchRealEstateListingsBodyLocationType1
    from ..models.fetch_real_estate_listings_body_lot_area_sq_ft_type_0 import (
        FetchRealEstateListingsBodyLotAreaSqFtType0,
    )
    from ..models.fetch_real_estate_listings_body_parking_spots_type_0 import (
        FetchRealEstateListingsBodyParkingSpotsType0,
    )
    from ..models.fetch_real_estate_listings_body_price_type_0 import FetchRealEstateListingsBodyPriceType0
    from ..models.fetch_real_estate_listings_body_rent_type_0 import FetchRealEstateListingsBodyRentType0
    from ..models.fetch_real_estate_listings_body_year_built_type_0 import FetchRealEstateListingsBodyYearBuiltType0


T = TypeVar("T", bound="FetchRealEstateListingsBody")


@_attrs_define
class FetchRealEstateListingsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        location (FetchRealEstateListingsBodyLocationType0 | FetchRealEstateListingsBodyLocationType1): Location input
            for listing search. Use `raw` for user-provided text and `structured` for exact city/state precision.
        next_page_token (None | str | Unset): Pagination token from a previous response. Omit for the first page.
        sort_by (FetchRealEstateListingsBodySortByType1 | FetchRealEstateListingsBodySortByType2Type1 |
            FetchRealEstateListingsBodySortByType3Type1 | None | Unset): Sort order for search results.
        listing_status (FetchRealEstateListingsBodyListingStatusType1 |
            FetchRealEstateListingsBodyListingStatusType2Type1 | FetchRealEstateListingsBodyListingStatusType3Type1 | None |
            Unset): Listing category to search.
        home_types (list[FetchRealEstateListingsBodyHomeTypesType0Item] | None | Unset): Property types to include.
        price (FetchRealEstateListingsBodyPriceType0 | None | Unset): Price range filter for sale and sold listings.
            Values must use the local market currency for the location (for example, CAD for Canada and USD for the United
            States).
        rent (FetchRealEstateListingsBodyRentType0 | None | Unset): Monthly rent range filter for rental listings.
            Values must use the local market currency for the location (for example, CAD for Canada and USD for the United
            States).
        bedrooms (FetchRealEstateListingsBodyBedroomsType0 | None | Unset): Bedroom count filter. Use `min` to set the
            lower bound.
        bathrooms (FetchRealEstateListingsBodyBathroomsType0 | None | Unset): Bathroom count filter. Use `min` to set
            the lower bound.
        floor_area_sq_ft (FetchRealEstateListingsBodyFloorAreaSqFtType0 | None | Unset): Interior living-area range in
            square feet.
        lot_area_sq_ft (FetchRealEstateListingsBodyLotAreaSqFtType0 | None | Unset): Lot-size range in square feet.
        year_built (FetchRealEstateListingsBodyYearBuiltType0 | None | Unset): Year-built range.
        parking_spots (FetchRealEstateListingsBodyParkingSpotsType0 | None | Unset): Parking spots filter.
        keywords (None | str | Unset): Additional keyword terms to match in listing text. For broader matching, separate
            terms with commas (for example: 'pool,garage').
        features (FetchRealEstateListingsBodyFeaturesType0 | None | Unset): Optional property feature filters.
    """

    api_key: str
    location: FetchRealEstateListingsBodyLocationType0 | FetchRealEstateListingsBodyLocationType1
    next_page_token: None | str | Unset = UNSET
    sort_by: (
        FetchRealEstateListingsBodySortByType1
        | FetchRealEstateListingsBodySortByType2Type1
        | FetchRealEstateListingsBodySortByType3Type1
        | None
        | Unset
    ) = UNSET
    listing_status: (
        FetchRealEstateListingsBodyListingStatusType1
        | FetchRealEstateListingsBodyListingStatusType2Type1
        | FetchRealEstateListingsBodyListingStatusType3Type1
        | None
        | Unset
    ) = UNSET
    home_types: list[FetchRealEstateListingsBodyHomeTypesType0Item] | None | Unset = UNSET
    price: FetchRealEstateListingsBodyPriceType0 | None | Unset = UNSET
    rent: FetchRealEstateListingsBodyRentType0 | None | Unset = UNSET
    bedrooms: FetchRealEstateListingsBodyBedroomsType0 | None | Unset = UNSET
    bathrooms: FetchRealEstateListingsBodyBathroomsType0 | None | Unset = UNSET
    floor_area_sq_ft: FetchRealEstateListingsBodyFloorAreaSqFtType0 | None | Unset = UNSET
    lot_area_sq_ft: FetchRealEstateListingsBodyLotAreaSqFtType0 | None | Unset = UNSET
    year_built: FetchRealEstateListingsBodyYearBuiltType0 | None | Unset = UNSET
    parking_spots: FetchRealEstateListingsBodyParkingSpotsType0 | None | Unset = UNSET
    keywords: None | str | Unset = UNSET
    features: FetchRealEstateListingsBodyFeaturesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.fetch_real_estate_listings_body_bathrooms_type_0 import FetchRealEstateListingsBodyBathroomsType0
        from ..models.fetch_real_estate_listings_body_bedrooms_type_0 import FetchRealEstateListingsBodyBedroomsType0
        from ..models.fetch_real_estate_listings_body_features_type_0 import FetchRealEstateListingsBodyFeaturesType0
        from ..models.fetch_real_estate_listings_body_floor_area_sq_ft_type_0 import (
            FetchRealEstateListingsBodyFloorAreaSqFtType0,
        )
        from ..models.fetch_real_estate_listings_body_location_type_0 import FetchRealEstateListingsBodyLocationType0
        from ..models.fetch_real_estate_listings_body_lot_area_sq_ft_type_0 import (
            FetchRealEstateListingsBodyLotAreaSqFtType0,
        )
        from ..models.fetch_real_estate_listings_body_parking_spots_type_0 import (
            FetchRealEstateListingsBodyParkingSpotsType0,
        )
        from ..models.fetch_real_estate_listings_body_price_type_0 import FetchRealEstateListingsBodyPriceType0
        from ..models.fetch_real_estate_listings_body_rent_type_0 import FetchRealEstateListingsBodyRentType0
        from ..models.fetch_real_estate_listings_body_year_built_type_0 import FetchRealEstateListingsBodyYearBuiltType0

        api_key = self.api_key

        location: dict[str, Any]
        if isinstance(self.location, FetchRealEstateListingsBodyLocationType0):
            location = self.location.to_dict()
        else:
            location = self.location.to_dict()

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        sort_by: None | str | Unset
        if isinstance(self.sort_by, Unset):
            sort_by = UNSET
        elif isinstance(self.sort_by, FetchRealEstateListingsBodySortByType1):
            sort_by = self.sort_by.value
        elif isinstance(self.sort_by, FetchRealEstateListingsBodySortByType2Type1):
            sort_by = self.sort_by.value
        elif isinstance(self.sort_by, FetchRealEstateListingsBodySortByType3Type1):
            sort_by = self.sort_by.value
        else:
            sort_by = self.sort_by

        listing_status: None | str | Unset
        if isinstance(self.listing_status, Unset):
            listing_status = UNSET
        elif isinstance(self.listing_status, FetchRealEstateListingsBodyListingStatusType1):
            listing_status = self.listing_status.value
        elif isinstance(self.listing_status, FetchRealEstateListingsBodyListingStatusType2Type1):
            listing_status = self.listing_status.value
        elif isinstance(self.listing_status, FetchRealEstateListingsBodyListingStatusType3Type1):
            listing_status = self.listing_status.value
        else:
            listing_status = self.listing_status

        home_types: list[str] | None | Unset
        if isinstance(self.home_types, Unset):
            home_types = UNSET
        elif isinstance(self.home_types, list):
            home_types = []
            for home_types_type_0_item_data in self.home_types:
                home_types_type_0_item = home_types_type_0_item_data.value
                home_types.append(home_types_type_0_item)

        else:
            home_types = self.home_types

        price: dict[str, Any] | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        elif isinstance(self.price, FetchRealEstateListingsBodyPriceType0):
            price = self.price.to_dict()
        else:
            price = self.price

        rent: dict[str, Any] | None | Unset
        if isinstance(self.rent, Unset):
            rent = UNSET
        elif isinstance(self.rent, FetchRealEstateListingsBodyRentType0):
            rent = self.rent.to_dict()
        else:
            rent = self.rent

        bedrooms: dict[str, Any] | None | Unset
        if isinstance(self.bedrooms, Unset):
            bedrooms = UNSET
        elif isinstance(self.bedrooms, FetchRealEstateListingsBodyBedroomsType0):
            bedrooms = self.bedrooms.to_dict()
        else:
            bedrooms = self.bedrooms

        bathrooms: dict[str, Any] | None | Unset
        if isinstance(self.bathrooms, Unset):
            bathrooms = UNSET
        elif isinstance(self.bathrooms, FetchRealEstateListingsBodyBathroomsType0):
            bathrooms = self.bathrooms.to_dict()
        else:
            bathrooms = self.bathrooms

        floor_area_sq_ft: dict[str, Any] | None | Unset
        if isinstance(self.floor_area_sq_ft, Unset):
            floor_area_sq_ft = UNSET
        elif isinstance(self.floor_area_sq_ft, FetchRealEstateListingsBodyFloorAreaSqFtType0):
            floor_area_sq_ft = self.floor_area_sq_ft.to_dict()
        else:
            floor_area_sq_ft = self.floor_area_sq_ft

        lot_area_sq_ft: dict[str, Any] | None | Unset
        if isinstance(self.lot_area_sq_ft, Unset):
            lot_area_sq_ft = UNSET
        elif isinstance(self.lot_area_sq_ft, FetchRealEstateListingsBodyLotAreaSqFtType0):
            lot_area_sq_ft = self.lot_area_sq_ft.to_dict()
        else:
            lot_area_sq_ft = self.lot_area_sq_ft

        year_built: dict[str, Any] | None | Unset
        if isinstance(self.year_built, Unset):
            year_built = UNSET
        elif isinstance(self.year_built, FetchRealEstateListingsBodyYearBuiltType0):
            year_built = self.year_built.to_dict()
        else:
            year_built = self.year_built

        parking_spots: dict[str, Any] | None | Unset
        if isinstance(self.parking_spots, Unset):
            parking_spots = UNSET
        elif isinstance(self.parking_spots, FetchRealEstateListingsBodyParkingSpotsType0):
            parking_spots = self.parking_spots.to_dict()
        else:
            parking_spots = self.parking_spots

        keywords: None | str | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        else:
            keywords = self.keywords

        features: dict[str, Any] | None | Unset
        if isinstance(self.features, Unset):
            features = UNSET
        elif isinstance(self.features, FetchRealEstateListingsBodyFeaturesType0):
            features = self.features.to_dict()
        else:
            features = self.features

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "location": location,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if sort_by is not UNSET:
            field_dict["sortBy"] = sort_by
        if listing_status is not UNSET:
            field_dict["listingStatus"] = listing_status
        if home_types is not UNSET:
            field_dict["homeTypes"] = home_types
        if price is not UNSET:
            field_dict["price"] = price
        if rent is not UNSET:
            field_dict["rent"] = rent
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if bathrooms is not UNSET:
            field_dict["bathrooms"] = bathrooms
        if floor_area_sq_ft is not UNSET:
            field_dict["floorAreaSqFt"] = floor_area_sq_ft
        if lot_area_sq_ft is not UNSET:
            field_dict["lotAreaSqFt"] = lot_area_sq_ft
        if year_built is not UNSET:
            field_dict["yearBuilt"] = year_built
        if parking_spots is not UNSET:
            field_dict["parkingSpots"] = parking_spots
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if features is not UNSET:
            field_dict["features"] = features

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fetch_real_estate_listings_body_bathrooms_type_0 import FetchRealEstateListingsBodyBathroomsType0
        from ..models.fetch_real_estate_listings_body_bedrooms_type_0 import FetchRealEstateListingsBodyBedroomsType0
        from ..models.fetch_real_estate_listings_body_features_type_0 import FetchRealEstateListingsBodyFeaturesType0
        from ..models.fetch_real_estate_listings_body_floor_area_sq_ft_type_0 import (
            FetchRealEstateListingsBodyFloorAreaSqFtType0,
        )
        from ..models.fetch_real_estate_listings_body_location_type_0 import FetchRealEstateListingsBodyLocationType0
        from ..models.fetch_real_estate_listings_body_location_type_1 import FetchRealEstateListingsBodyLocationType1
        from ..models.fetch_real_estate_listings_body_lot_area_sq_ft_type_0 import (
            FetchRealEstateListingsBodyLotAreaSqFtType0,
        )
        from ..models.fetch_real_estate_listings_body_parking_spots_type_0 import (
            FetchRealEstateListingsBodyParkingSpotsType0,
        )
        from ..models.fetch_real_estate_listings_body_price_type_0 import FetchRealEstateListingsBodyPriceType0
        from ..models.fetch_real_estate_listings_body_rent_type_0 import FetchRealEstateListingsBodyRentType0
        from ..models.fetch_real_estate_listings_body_year_built_type_0 import FetchRealEstateListingsBodyYearBuiltType0

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_location(
            data: object,
        ) -> FetchRealEstateListingsBodyLocationType0 | FetchRealEstateListingsBodyLocationType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = FetchRealEstateListingsBodyLocationType0.from_dict(data)

                return location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            location_type_1 = FetchRealEstateListingsBodyLocationType1.from_dict(data)

            return location_type_1

        location = _parse_location(d.pop("location"))

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        def _parse_sort_by(
            data: object,
        ) -> (
            FetchRealEstateListingsBodySortByType1
            | FetchRealEstateListingsBodySortByType2Type1
            | FetchRealEstateListingsBodySortByType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_by_type_1 = FetchRealEstateListingsBodySortByType1(data)

                return sort_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_by_type_2_type_1 = FetchRealEstateListingsBodySortByType2Type1(data)

                return sort_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_by_type_3_type_1 = FetchRealEstateListingsBodySortByType3Type1(data)

                return sort_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FetchRealEstateListingsBodySortByType1
                | FetchRealEstateListingsBodySortByType2Type1
                | FetchRealEstateListingsBodySortByType3Type1
                | None
                | Unset,
                data,
            )

        sort_by = _parse_sort_by(d.pop("sortBy", UNSET))

        def _parse_listing_status(
            data: object,
        ) -> (
            FetchRealEstateListingsBodyListingStatusType1
            | FetchRealEstateListingsBodyListingStatusType2Type1
            | FetchRealEstateListingsBodyListingStatusType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                listing_status_type_1 = FetchRealEstateListingsBodyListingStatusType1(data)

                return listing_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                listing_status_type_2_type_1 = FetchRealEstateListingsBodyListingStatusType2Type1(data)

                return listing_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                listing_status_type_3_type_1 = FetchRealEstateListingsBodyListingStatusType3Type1(data)

                return listing_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FetchRealEstateListingsBodyListingStatusType1
                | FetchRealEstateListingsBodyListingStatusType2Type1
                | FetchRealEstateListingsBodyListingStatusType3Type1
                | None
                | Unset,
                data,
            )

        listing_status = _parse_listing_status(d.pop("listingStatus", UNSET))

        def _parse_home_types(data: object) -> list[FetchRealEstateListingsBodyHomeTypesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                home_types_type_0 = []
                _home_types_type_0 = data
                for home_types_type_0_item_data in _home_types_type_0:
                    home_types_type_0_item = FetchRealEstateListingsBodyHomeTypesType0Item(home_types_type_0_item_data)

                    home_types_type_0.append(home_types_type_0_item)

                return home_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FetchRealEstateListingsBodyHomeTypesType0Item] | None | Unset, data)

        home_types = _parse_home_types(d.pop("homeTypes", UNSET))

        def _parse_price(data: object) -> FetchRealEstateListingsBodyPriceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                price_type_0 = FetchRealEstateListingsBodyPriceType0.from_dict(data)

                return price_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FetchRealEstateListingsBodyPriceType0 | None | Unset, data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_rent(data: object) -> FetchRealEstateListingsBodyRentType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rent_type_0 = FetchRealEstateListingsBodyRentType0.from_dict(data)

                return rent_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FetchRealEstateListingsBodyRentType0 | None | Unset, data)

        rent = _parse_rent(d.pop("rent", UNSET))

        def _parse_bedrooms(data: object) -> FetchRealEstateListingsBodyBedroomsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bedrooms_type_0 = FetchRealEstateListingsBodyBedroomsType0.from_dict(data)

                return bedrooms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FetchRealEstateListingsBodyBedroomsType0 | None | Unset, data)

        bedrooms = _parse_bedrooms(d.pop("bedrooms", UNSET))

        def _parse_bathrooms(data: object) -> FetchRealEstateListingsBodyBathroomsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bathrooms_type_0 = FetchRealEstateListingsBodyBathroomsType0.from_dict(data)

                return bathrooms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FetchRealEstateListingsBodyBathroomsType0 | None | Unset, data)

        bathrooms = _parse_bathrooms(d.pop("bathrooms", UNSET))

        def _parse_floor_area_sq_ft(data: object) -> FetchRealEstateListingsBodyFloorAreaSqFtType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                floor_area_sq_ft_type_0 = FetchRealEstateListingsBodyFloorAreaSqFtType0.from_dict(data)

                return floor_area_sq_ft_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FetchRealEstateListingsBodyFloorAreaSqFtType0 | None | Unset, data)

        floor_area_sq_ft = _parse_floor_area_sq_ft(d.pop("floorAreaSqFt", UNSET))

        def _parse_lot_area_sq_ft(data: object) -> FetchRealEstateListingsBodyLotAreaSqFtType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                lot_area_sq_ft_type_0 = FetchRealEstateListingsBodyLotAreaSqFtType0.from_dict(data)

                return lot_area_sq_ft_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FetchRealEstateListingsBodyLotAreaSqFtType0 | None | Unset, data)

        lot_area_sq_ft = _parse_lot_area_sq_ft(d.pop("lotAreaSqFt", UNSET))

        def _parse_year_built(data: object) -> FetchRealEstateListingsBodyYearBuiltType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                year_built_type_0 = FetchRealEstateListingsBodyYearBuiltType0.from_dict(data)

                return year_built_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FetchRealEstateListingsBodyYearBuiltType0 | None | Unset, data)

        year_built = _parse_year_built(d.pop("yearBuilt", UNSET))

        def _parse_parking_spots(data: object) -> FetchRealEstateListingsBodyParkingSpotsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parking_spots_type_0 = FetchRealEstateListingsBodyParkingSpotsType0.from_dict(data)

                return parking_spots_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FetchRealEstateListingsBodyParkingSpotsType0 | None | Unset, data)

        parking_spots = _parse_parking_spots(d.pop("parkingSpots", UNSET))

        def _parse_keywords(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_features(data: object) -> FetchRealEstateListingsBodyFeaturesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                features_type_0 = FetchRealEstateListingsBodyFeaturesType0.from_dict(data)

                return features_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FetchRealEstateListingsBodyFeaturesType0 | None | Unset, data)

        features = _parse_features(d.pop("features", UNSET))

        fetch_real_estate_listings_body = cls(
            api_key=api_key,
            location=location,
            next_page_token=next_page_token,
            sort_by=sort_by,
            listing_status=listing_status,
            home_types=home_types,
            price=price,
            rent=rent,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            floor_area_sq_ft=floor_area_sq_ft,
            lot_area_sq_ft=lot_area_sq_ft,
            year_built=year_built,
            parking_spots=parking_spots,
            keywords=keywords,
            features=features,
        )

        fetch_real_estate_listings_body.additional_properties = d
        return fetch_real_estate_listings_body

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
