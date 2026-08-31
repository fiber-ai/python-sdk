from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fetch_real_estate_listings_response_200_output_properties_item_base_rent_type_0 import (
        FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0,
    )
    from ..models.fetch_real_estate_listings_response_200_output_properties_item_estimated_monthly_rent_type_0 import (
        FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedMonthlyRentType0,
    )
    from ..models.fetch_real_estate_listings_response_200_output_properties_item_estimated_price_type_0 import (
        FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedPriceType0,
    )
    from ..models.fetch_real_estate_listings_response_200_output_properties_item_facts_and_features_type_0 import (
        FetchRealEstateListingsResponse200OutputPropertiesItemFactsAndFeaturesType0,
    )
    from ..models.fetch_real_estate_listings_response_200_output_properties_item_listing_tags_type_0_item import (
        FetchRealEstateListingsResponse200OutputPropertiesItemListingTagsType0Item,
    )
    from ..models.fetch_real_estate_listings_response_200_output_properties_item_open_house_type_0 import (
        FetchRealEstateListingsResponse200OutputPropertiesItemOpenHouseType0,
    )
    from ..models.fetch_real_estate_listings_response_200_output_properties_item_price_change_amount_type_0 import (
        FetchRealEstateListingsResponse200OutputPropertiesItemPriceChangeAmountType0,
    )
    from ..models.fetch_real_estate_listings_response_200_output_properties_item_price_type_0 import (
        FetchRealEstateListingsResponse200OutputPropertiesItemPriceType0,
    )
    from ..models.fetch_real_estate_listings_response_200_output_properties_item_primary_tag_type_0 import (
        FetchRealEstateListingsResponse200OutputPropertiesItemPrimaryTagType0,
    )
    from ..models.fetch_real_estate_listings_response_200_output_properties_item_rental_units_type_0_item import (
        FetchRealEstateListingsResponse200OutputPropertiesItemRentalUnitsType0Item,
    )
    from ..models.fetch_real_estate_listings_response_200_output_properties_item_tax_assessed_value_type_0 import (
        FetchRealEstateListingsResponse200OutputPropertiesItemTaxAssessedValueType0,
    )


T = TypeVar("T", bound="FetchRealEstateListingsResponse200OutputPropertiesItem")


@_attrs_define
class FetchRealEstateListingsResponse200OutputPropertiesItem:
    """
    Attributes:
        listing_id (str): Unique listing identifier.
        price (FetchRealEstateListingsResponse200OutputPropertiesItemPriceType0 | None | Unset): Price represented in
            both USD and local listing currency.
        position (int | None | Unset): Result position on this page.
        address (None | str | Unset): Full property address.
        street (None | str | Unset): Street address.
        city (None | str | Unset): City name.
        state (None | str | Unset): State or province code.
        postal_code (None | str | Unset): Postal or ZIP code.
        unit_number (None | str | Unset): Unit or apartment number, when the listing is part of a multi-unit building.
        bedroom_count (int | None | Unset): Number of bedrooms.
        bathroom_count (float | None | Unset): Number of bathrooms.
        estimated_price (FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedPriceType0 | None | Unset):
            Estimated property value in USD and local currency.
        estimated_monthly_rent (FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedMonthlyRentType0 | None |
            Unset): Estimated monthly rent in USD and local currency.
        price_change_amount (FetchRealEstateListingsResponse200OutputPropertiesItemPriceChangeAmountType0 | None |
            Unset): Latest absolute price change in USD and local currency.
        price_reduction_note (None | str | Unset): Formatted price-reduction note.
        tax_assessed_value (FetchRealEstateListingsResponse200OutputPropertiesItemTaxAssessedValueType0 | None | Unset):
            Tax-assessed property value in USD and local currency.
        floor_area_sq_ft (int | None | Unset): Living area in square feet.
        lot_area_sq_ft (float | None | Unset): Lot size in square feet.
        home_type (None | str | Unset): Property type label.
        listing_lifecycle_status (None | str | Unset): Listing lifecycle status.
        listing_status_label (None | str | Unset): Human-readable listing status label.
        listing_type (None | str | Unset): Listing type.
        date_sold (None | str | Unset): Sold date.
        date_price_changed (None | str | Unset): Latest price-change date.
        new_construction_type (None | str | Unset): New-construction type.
        time_on_market_days (int | None | Unset): Number of days this listing has been on market.
        url (None | str | Unset): Listing URL.
        thumbnail_url (None | str | Unset): Listing thumbnail URL.
        image_urls (list[str] | None | Unset): Listing image URLs.
        street_view_url (None | str | Unset): Street-view URL.
        has_3_d_model (bool | None | Unset): Whether a 3D model is available.
        broker_name (None | str | Unset): Listing broker name.
        builder_name (None | str | Unset): Builder name.
        is_showcase_listing (bool | None | Unset): Whether the listing is marked as showcase.
        is_featured_listing (bool | None | Unset): Whether the listing is marked as featured.
        primary_tag (FetchRealEstateListingsResponse200OutputPropertiesItemPrimaryTagType0 | None | Unset): Primary
            listing tag.
        listing_tags (list[FetchRealEstateListingsResponse200OutputPropertiesItemListingTagsType0Item] | None | Unset):
            Additional listing tags.
        contact_phone (None | str | Unset): Listing contact phone number.
        open_house (FetchRealEstateListingsResponse200OutputPropertiesItemOpenHouseType0 | None | Unset): Open-house
            details.
        building_name (None | str | Unset): Building name.
        rental_units (list[FetchRealEstateListingsResponse200OutputPropertiesItemRentalUnitsType0Item] | None | Unset):
            Individual rental units available in a multi-unit building.
        availability_count (int | None | Unset): Count of available units.
        base_rent (FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0 | None | Unset): Base-rent range
            in USD and local currency.
        availability_date (None | str | Unset): Availability date.
        is_instant_tour_enabled (bool | None | Unset): Whether instant tour is enabled.
        facts_and_features (FetchRealEstateListingsResponse200OutputPropertiesItemFactsAndFeaturesType0 | None | Unset):
            Additional facts and features.
        country_code (None | str | Unset): ISO 3166-1 alpha-3 country code (for example: 'CAN').
        latitude (float | None | Unset): Latitude coordinate.
        longitude (float | None | Unset): Longitude coordinate.
    """

    listing_id: str
    price: FetchRealEstateListingsResponse200OutputPropertiesItemPriceType0 | None | Unset = UNSET
    position: int | None | Unset = UNSET
    address: None | str | Unset = UNSET
    street: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    postal_code: None | str | Unset = UNSET
    unit_number: None | str | Unset = UNSET
    bedroom_count: int | None | Unset = UNSET
    bathroom_count: float | None | Unset = UNSET
    estimated_price: FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedPriceType0 | None | Unset = UNSET
    estimated_monthly_rent: (
        FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedMonthlyRentType0 | None | Unset
    ) = UNSET
    price_change_amount: FetchRealEstateListingsResponse200OutputPropertiesItemPriceChangeAmountType0 | None | Unset = (
        UNSET
    )
    price_reduction_note: None | str | Unset = UNSET
    tax_assessed_value: FetchRealEstateListingsResponse200OutputPropertiesItemTaxAssessedValueType0 | None | Unset = (
        UNSET
    )
    floor_area_sq_ft: int | None | Unset = UNSET
    lot_area_sq_ft: float | None | Unset = UNSET
    home_type: None | str | Unset = UNSET
    listing_lifecycle_status: None | str | Unset = UNSET
    listing_status_label: None | str | Unset = UNSET
    listing_type: None | str | Unset = UNSET
    date_sold: None | str | Unset = UNSET
    date_price_changed: None | str | Unset = UNSET
    new_construction_type: None | str | Unset = UNSET
    time_on_market_days: int | None | Unset = UNSET
    url: None | str | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    image_urls: list[str] | None | Unset = UNSET
    street_view_url: None | str | Unset = UNSET
    has_3_d_model: bool | None | Unset = UNSET
    broker_name: None | str | Unset = UNSET
    builder_name: None | str | Unset = UNSET
    is_showcase_listing: bool | None | Unset = UNSET
    is_featured_listing: bool | None | Unset = UNSET
    primary_tag: FetchRealEstateListingsResponse200OutputPropertiesItemPrimaryTagType0 | None | Unset = UNSET
    listing_tags: list[FetchRealEstateListingsResponse200OutputPropertiesItemListingTagsType0Item] | None | Unset = (
        UNSET
    )
    contact_phone: None | str | Unset = UNSET
    open_house: FetchRealEstateListingsResponse200OutputPropertiesItemOpenHouseType0 | None | Unset = UNSET
    building_name: None | str | Unset = UNSET
    rental_units: list[FetchRealEstateListingsResponse200OutputPropertiesItemRentalUnitsType0Item] | None | Unset = (
        UNSET
    )
    availability_count: int | None | Unset = UNSET
    base_rent: FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0 | None | Unset = UNSET
    availability_date: None | str | Unset = UNSET
    is_instant_tour_enabled: bool | None | Unset = UNSET
    facts_and_features: FetchRealEstateListingsResponse200OutputPropertiesItemFactsAndFeaturesType0 | None | Unset = (
        UNSET
    )
    country_code: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_base_rent_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_estimated_monthly_rent_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedMonthlyRentType0,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_estimated_price_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedPriceType0,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_facts_and_features_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemFactsAndFeaturesType0,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_open_house_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemOpenHouseType0,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_price_change_amount_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemPriceChangeAmountType0,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_price_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemPriceType0,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_primary_tag_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemPrimaryTagType0,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_tax_assessed_value_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemTaxAssessedValueType0,  # noqa: PLC0415
        )

        listing_id = self.listing_id

        price: dict[str, Any] | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        elif isinstance(self.price, FetchRealEstateListingsResponse200OutputPropertiesItemPriceType0):
            price = self.price.to_dict()
        else:
            price = self.price

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        street: None | str | Unset
        if isinstance(self.street, Unset):
            street = UNSET
        else:
            street = self.street

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        postal_code: None | str | Unset
        if isinstance(self.postal_code, Unset):
            postal_code = UNSET
        else:
            postal_code = self.postal_code

        unit_number: None | str | Unset
        if isinstance(self.unit_number, Unset):
            unit_number = UNSET
        else:
            unit_number = self.unit_number

        bedroom_count: int | None | Unset
        if isinstance(self.bedroom_count, Unset):
            bedroom_count = UNSET
        else:
            bedroom_count = self.bedroom_count

        bathroom_count: float | None | Unset
        if isinstance(self.bathroom_count, Unset):
            bathroom_count = UNSET
        else:
            bathroom_count = self.bathroom_count

        estimated_price: dict[str, Any] | None | Unset
        if isinstance(self.estimated_price, Unset):
            estimated_price = UNSET
        elif isinstance(
            self.estimated_price, FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedPriceType0
        ):
            estimated_price = self.estimated_price.to_dict()
        else:
            estimated_price = self.estimated_price

        estimated_monthly_rent: dict[str, Any] | None | Unset
        if isinstance(self.estimated_monthly_rent, Unset):
            estimated_monthly_rent = UNSET
        elif isinstance(
            self.estimated_monthly_rent, FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedMonthlyRentType0
        ):
            estimated_monthly_rent = self.estimated_monthly_rent.to_dict()
        else:
            estimated_monthly_rent = self.estimated_monthly_rent

        price_change_amount: dict[str, Any] | None | Unset
        if isinstance(self.price_change_amount, Unset):
            price_change_amount = UNSET
        elif isinstance(
            self.price_change_amount, FetchRealEstateListingsResponse200OutputPropertiesItemPriceChangeAmountType0
        ):
            price_change_amount = self.price_change_amount.to_dict()
        else:
            price_change_amount = self.price_change_amount

        price_reduction_note: None | str | Unset
        if isinstance(self.price_reduction_note, Unset):
            price_reduction_note = UNSET
        else:
            price_reduction_note = self.price_reduction_note

        tax_assessed_value: dict[str, Any] | None | Unset
        if isinstance(self.tax_assessed_value, Unset):
            tax_assessed_value = UNSET
        elif isinstance(
            self.tax_assessed_value, FetchRealEstateListingsResponse200OutputPropertiesItemTaxAssessedValueType0
        ):
            tax_assessed_value = self.tax_assessed_value.to_dict()
        else:
            tax_assessed_value = self.tax_assessed_value

        floor_area_sq_ft: int | None | Unset
        if isinstance(self.floor_area_sq_ft, Unset):
            floor_area_sq_ft = UNSET
        else:
            floor_area_sq_ft = self.floor_area_sq_ft

        lot_area_sq_ft: float | None | Unset
        if isinstance(self.lot_area_sq_ft, Unset):
            lot_area_sq_ft = UNSET
        else:
            lot_area_sq_ft = self.lot_area_sq_ft

        home_type: None | str | Unset
        if isinstance(self.home_type, Unset):
            home_type = UNSET
        else:
            home_type = self.home_type

        listing_lifecycle_status: None | str | Unset
        if isinstance(self.listing_lifecycle_status, Unset):
            listing_lifecycle_status = UNSET
        else:
            listing_lifecycle_status = self.listing_lifecycle_status

        listing_status_label: None | str | Unset
        if isinstance(self.listing_status_label, Unset):
            listing_status_label = UNSET
        else:
            listing_status_label = self.listing_status_label

        listing_type: None | str | Unset
        if isinstance(self.listing_type, Unset):
            listing_type = UNSET
        else:
            listing_type = self.listing_type

        date_sold: None | str | Unset
        if isinstance(self.date_sold, Unset):
            date_sold = UNSET
        else:
            date_sold = self.date_sold

        date_price_changed: None | str | Unset
        if isinstance(self.date_price_changed, Unset):
            date_price_changed = UNSET
        else:
            date_price_changed = self.date_price_changed

        new_construction_type: None | str | Unset
        if isinstance(self.new_construction_type, Unset):
            new_construction_type = UNSET
        else:
            new_construction_type = self.new_construction_type

        time_on_market_days: int | None | Unset
        if isinstance(self.time_on_market_days, Unset):
            time_on_market_days = UNSET
        else:
            time_on_market_days = self.time_on_market_days

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        image_urls: list[str] | None | Unset
        if isinstance(self.image_urls, Unset):
            image_urls = UNSET
        elif isinstance(self.image_urls, list):
            image_urls = self.image_urls

        else:
            image_urls = self.image_urls

        street_view_url: None | str | Unset
        if isinstance(self.street_view_url, Unset):
            street_view_url = UNSET
        else:
            street_view_url = self.street_view_url

        has_3_d_model: bool | None | Unset
        if isinstance(self.has_3_d_model, Unset):
            has_3_d_model = UNSET
        else:
            has_3_d_model = self.has_3_d_model

        broker_name: None | str | Unset
        if isinstance(self.broker_name, Unset):
            broker_name = UNSET
        else:
            broker_name = self.broker_name

        builder_name: None | str | Unset
        if isinstance(self.builder_name, Unset):
            builder_name = UNSET
        else:
            builder_name = self.builder_name

        is_showcase_listing: bool | None | Unset
        if isinstance(self.is_showcase_listing, Unset):
            is_showcase_listing = UNSET
        else:
            is_showcase_listing = self.is_showcase_listing

        is_featured_listing: bool | None | Unset
        if isinstance(self.is_featured_listing, Unset):
            is_featured_listing = UNSET
        else:
            is_featured_listing = self.is_featured_listing

        primary_tag: dict[str, Any] | None | Unset
        if isinstance(self.primary_tag, Unset):
            primary_tag = UNSET
        elif isinstance(self.primary_tag, FetchRealEstateListingsResponse200OutputPropertiesItemPrimaryTagType0):
            primary_tag = self.primary_tag.to_dict()
        else:
            primary_tag = self.primary_tag

        listing_tags: list[dict[str, Any]] | None | Unset
        if isinstance(self.listing_tags, Unset):
            listing_tags = UNSET
        elif isinstance(self.listing_tags, list):
            listing_tags = []
            for listing_tags_type_0_item_data in self.listing_tags:
                listing_tags_type_0_item = listing_tags_type_0_item_data.to_dict()
                listing_tags.append(listing_tags_type_0_item)

        else:
            listing_tags = self.listing_tags

        contact_phone: None | str | Unset
        if isinstance(self.contact_phone, Unset):
            contact_phone = UNSET
        else:
            contact_phone = self.contact_phone

        open_house: dict[str, Any] | None | Unset
        if isinstance(self.open_house, Unset):
            open_house = UNSET
        elif isinstance(self.open_house, FetchRealEstateListingsResponse200OutputPropertiesItemOpenHouseType0):
            open_house = self.open_house.to_dict()
        else:
            open_house = self.open_house

        building_name: None | str | Unset
        if isinstance(self.building_name, Unset):
            building_name = UNSET
        else:
            building_name = self.building_name

        rental_units: list[dict[str, Any]] | None | Unset
        if isinstance(self.rental_units, Unset):
            rental_units = UNSET
        elif isinstance(self.rental_units, list):
            rental_units = []
            for rental_units_type_0_item_data in self.rental_units:
                rental_units_type_0_item = rental_units_type_0_item_data.to_dict()
                rental_units.append(rental_units_type_0_item)

        else:
            rental_units = self.rental_units

        availability_count: int | None | Unset
        if isinstance(self.availability_count, Unset):
            availability_count = UNSET
        else:
            availability_count = self.availability_count

        base_rent: dict[str, Any] | None | Unset
        if isinstance(self.base_rent, Unset):
            base_rent = UNSET
        elif isinstance(self.base_rent, FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0):
            base_rent = self.base_rent.to_dict()
        else:
            base_rent = self.base_rent

        availability_date: None | str | Unset
        if isinstance(self.availability_date, Unset):
            availability_date = UNSET
        else:
            availability_date = self.availability_date

        is_instant_tour_enabled: bool | None | Unset
        if isinstance(self.is_instant_tour_enabled, Unset):
            is_instant_tour_enabled = UNSET
        else:
            is_instant_tour_enabled = self.is_instant_tour_enabled

        facts_and_features: dict[str, Any] | None | Unset
        if isinstance(self.facts_and_features, Unset):
            facts_and_features = UNSET
        elif isinstance(
            self.facts_and_features, FetchRealEstateListingsResponse200OutputPropertiesItemFactsAndFeaturesType0
        ):
            facts_and_features = self.facts_and_features.to_dict()
        else:
            facts_and_features = self.facts_and_features

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "listingId": listing_id,
            }
        )
        if price is not UNSET:
            field_dict["price"] = price
        if position is not UNSET:
            field_dict["position"] = position
        if address is not UNSET:
            field_dict["address"] = address
        if street is not UNSET:
            field_dict["street"] = street
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if unit_number is not UNSET:
            field_dict["unitNumber"] = unit_number
        if bedroom_count is not UNSET:
            field_dict["bedroomCount"] = bedroom_count
        if bathroom_count is not UNSET:
            field_dict["bathroomCount"] = bathroom_count
        if estimated_price is not UNSET:
            field_dict["estimatedPrice"] = estimated_price
        if estimated_monthly_rent is not UNSET:
            field_dict["estimatedMonthlyRent"] = estimated_monthly_rent
        if price_change_amount is not UNSET:
            field_dict["priceChangeAmount"] = price_change_amount
        if price_reduction_note is not UNSET:
            field_dict["priceReductionNote"] = price_reduction_note
        if tax_assessed_value is not UNSET:
            field_dict["taxAssessedValue"] = tax_assessed_value
        if floor_area_sq_ft is not UNSET:
            field_dict["floorAreaSqFt"] = floor_area_sq_ft
        if lot_area_sq_ft is not UNSET:
            field_dict["lotAreaSqFt"] = lot_area_sq_ft
        if home_type is not UNSET:
            field_dict["homeType"] = home_type
        if listing_lifecycle_status is not UNSET:
            field_dict["listingLifecycleStatus"] = listing_lifecycle_status
        if listing_status_label is not UNSET:
            field_dict["listingStatusLabel"] = listing_status_label
        if listing_type is not UNSET:
            field_dict["listingType"] = listing_type
        if date_sold is not UNSET:
            field_dict["dateSold"] = date_sold
        if date_price_changed is not UNSET:
            field_dict["datePriceChanged"] = date_price_changed
        if new_construction_type is not UNSET:
            field_dict["newConstructionType"] = new_construction_type
        if time_on_market_days is not UNSET:
            field_dict["timeOnMarketDays"] = time_on_market_days
        if url is not UNSET:
            field_dict["url"] = url
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url
        if image_urls is not UNSET:
            field_dict["imageUrls"] = image_urls
        if street_view_url is not UNSET:
            field_dict["streetViewUrl"] = street_view_url
        if has_3_d_model is not UNSET:
            field_dict["has3dModel"] = has_3_d_model
        if broker_name is not UNSET:
            field_dict["brokerName"] = broker_name
        if builder_name is not UNSET:
            field_dict["builderName"] = builder_name
        if is_showcase_listing is not UNSET:
            field_dict["isShowcaseListing"] = is_showcase_listing
        if is_featured_listing is not UNSET:
            field_dict["isFeaturedListing"] = is_featured_listing
        if primary_tag is not UNSET:
            field_dict["primaryTag"] = primary_tag
        if listing_tags is not UNSET:
            field_dict["listingTags"] = listing_tags
        if contact_phone is not UNSET:
            field_dict["contactPhone"] = contact_phone
        if open_house is not UNSET:
            field_dict["openHouse"] = open_house
        if building_name is not UNSET:
            field_dict["buildingName"] = building_name
        if rental_units is not UNSET:
            field_dict["rentalUnits"] = rental_units
        if availability_count is not UNSET:
            field_dict["availabilityCount"] = availability_count
        if base_rent is not UNSET:
            field_dict["baseRent"] = base_rent
        if availability_date is not UNSET:
            field_dict["availabilityDate"] = availability_date
        if is_instant_tour_enabled is not UNSET:
            field_dict["isInstantTourEnabled"] = is_instant_tour_enabled
        if facts_and_features is not UNSET:
            field_dict["factsAndFeatures"] = facts_and_features
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_base_rent_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_estimated_monthly_rent_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedMonthlyRentType0,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_estimated_price_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedPriceType0,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_facts_and_features_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemFactsAndFeaturesType0,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_listing_tags_type_0_item import (
            FetchRealEstateListingsResponse200OutputPropertiesItemListingTagsType0Item,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_open_house_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemOpenHouseType0,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_price_change_amount_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemPriceChangeAmountType0,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_price_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemPriceType0,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_primary_tag_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemPrimaryTagType0,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_rental_units_type_0_item import (
            FetchRealEstateListingsResponse200OutputPropertiesItemRentalUnitsType0Item,  # noqa: PLC0415
        )
        from ..models.fetch_real_estate_listings_response_200_output_properties_item_tax_assessed_value_type_0 import (
            FetchRealEstateListingsResponse200OutputPropertiesItemTaxAssessedValueType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        listing_id = d.pop("listingId")

        def _parse_price(
            data: object,
        ) -> FetchRealEstateListingsResponse200OutputPropertiesItemPriceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                price_type_0 = FetchRealEstateListingsResponse200OutputPropertiesItemPriceType0.from_dict(data)

                return price_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FetchRealEstateListingsResponse200OutputPropertiesItemPriceType0 | None | Unset, data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_street(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street = _parse_street(d.pop("street", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_postal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_code = _parse_postal_code(d.pop("postalCode", UNSET))

        def _parse_unit_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_number = _parse_unit_number(d.pop("unitNumber", UNSET))

        def _parse_bedroom_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bedroom_count = _parse_bedroom_count(d.pop("bedroomCount", UNSET))

        def _parse_bathroom_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        bathroom_count = _parse_bathroom_count(d.pop("bathroomCount", UNSET))

        def _parse_estimated_price(
            data: object,
        ) -> FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedPriceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                estimated_price_type_0 = (
                    FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedPriceType0.from_dict(data)
                )

                return estimated_price_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedPriceType0 | None | Unset, data)

        estimated_price = _parse_estimated_price(d.pop("estimatedPrice", UNSET))

        def _parse_estimated_monthly_rent(
            data: object,
        ) -> FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedMonthlyRentType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                estimated_monthly_rent_type_0 = (
                    FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedMonthlyRentType0.from_dict(data)
                )

                return estimated_monthly_rent_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FetchRealEstateListingsResponse200OutputPropertiesItemEstimatedMonthlyRentType0 | None | Unset, data
            )

        estimated_monthly_rent = _parse_estimated_monthly_rent(d.pop("estimatedMonthlyRent", UNSET))

        def _parse_price_change_amount(
            data: object,
        ) -> FetchRealEstateListingsResponse200OutputPropertiesItemPriceChangeAmountType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                price_change_amount_type_0 = (
                    FetchRealEstateListingsResponse200OutputPropertiesItemPriceChangeAmountType0.from_dict(data)
                )

                return price_change_amount_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FetchRealEstateListingsResponse200OutputPropertiesItemPriceChangeAmountType0 | None | Unset, data
            )

        price_change_amount = _parse_price_change_amount(d.pop("priceChangeAmount", UNSET))

        def _parse_price_reduction_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price_reduction_note = _parse_price_reduction_note(d.pop("priceReductionNote", UNSET))

        def _parse_tax_assessed_value(
            data: object,
        ) -> FetchRealEstateListingsResponse200OutputPropertiesItemTaxAssessedValueType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tax_assessed_value_type_0 = (
                    FetchRealEstateListingsResponse200OutputPropertiesItemTaxAssessedValueType0.from_dict(data)
                )

                return tax_assessed_value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FetchRealEstateListingsResponse200OutputPropertiesItemTaxAssessedValueType0 | None | Unset, data
            )

        tax_assessed_value = _parse_tax_assessed_value(d.pop("taxAssessedValue", UNSET))

        def _parse_floor_area_sq_ft(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        floor_area_sq_ft = _parse_floor_area_sq_ft(d.pop("floorAreaSqFt", UNSET))

        def _parse_lot_area_sq_ft(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lot_area_sq_ft = _parse_lot_area_sq_ft(d.pop("lotAreaSqFt", UNSET))

        def _parse_home_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        home_type = _parse_home_type(d.pop("homeType", UNSET))

        def _parse_listing_lifecycle_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_lifecycle_status = _parse_listing_lifecycle_status(d.pop("listingLifecycleStatus", UNSET))

        def _parse_listing_status_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_status_label = _parse_listing_status_label(d.pop("listingStatusLabel", UNSET))

        def _parse_listing_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_type = _parse_listing_type(d.pop("listingType", UNSET))

        def _parse_date_sold(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_sold = _parse_date_sold(d.pop("dateSold", UNSET))

        def _parse_date_price_changed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_price_changed = _parse_date_price_changed(d.pop("datePriceChanged", UNSET))

        def _parse_new_construction_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_construction_type = _parse_new_construction_type(d.pop("newConstructionType", UNSET))

        def _parse_time_on_market_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_on_market_days = _parse_time_on_market_days(d.pop("timeOnMarketDays", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))

        def _parse_image_urls(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_urls_type_0 = cast(list[str], data)

                return image_urls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        image_urls = _parse_image_urls(d.pop("imageUrls", UNSET))

        def _parse_street_view_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_view_url = _parse_street_view_url(d.pop("streetViewUrl", UNSET))

        def _parse_has_3_d_model(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_3_d_model = _parse_has_3_d_model(d.pop("has3dModel", UNSET))

        def _parse_broker_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        broker_name = _parse_broker_name(d.pop("brokerName", UNSET))

        def _parse_builder_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        builder_name = _parse_builder_name(d.pop("builderName", UNSET))

        def _parse_is_showcase_listing(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_showcase_listing = _parse_is_showcase_listing(d.pop("isShowcaseListing", UNSET))

        def _parse_is_featured_listing(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_featured_listing = _parse_is_featured_listing(d.pop("isFeaturedListing", UNSET))

        def _parse_primary_tag(
            data: object,
        ) -> FetchRealEstateListingsResponse200OutputPropertiesItemPrimaryTagType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                primary_tag_type_0 = FetchRealEstateListingsResponse200OutputPropertiesItemPrimaryTagType0.from_dict(
                    data
                )

                return primary_tag_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FetchRealEstateListingsResponse200OutputPropertiesItemPrimaryTagType0 | None | Unset, data)

        primary_tag = _parse_primary_tag(d.pop("primaryTag", UNSET))

        def _parse_listing_tags(
            data: object,
        ) -> list[FetchRealEstateListingsResponse200OutputPropertiesItemListingTagsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                listing_tags_type_0 = []
                _listing_tags_type_0 = data
                for listing_tags_type_0_item_data in _listing_tags_type_0:
                    listing_tags_type_0_item = (
                        FetchRealEstateListingsResponse200OutputPropertiesItemListingTagsType0Item.from_dict(
                            listing_tags_type_0_item_data
                        )
                    )

                    listing_tags_type_0.append(listing_tags_type_0_item)

                return listing_tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[FetchRealEstateListingsResponse200OutputPropertiesItemListingTagsType0Item] | None | Unset, data
            )

        listing_tags = _parse_listing_tags(d.pop("listingTags", UNSET))

        def _parse_contact_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_phone = _parse_contact_phone(d.pop("contactPhone", UNSET))

        def _parse_open_house(
            data: object,
        ) -> FetchRealEstateListingsResponse200OutputPropertiesItemOpenHouseType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                open_house_type_0 = FetchRealEstateListingsResponse200OutputPropertiesItemOpenHouseType0.from_dict(data)

                return open_house_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FetchRealEstateListingsResponse200OutputPropertiesItemOpenHouseType0 | None | Unset, data)

        open_house = _parse_open_house(d.pop("openHouse", UNSET))

        def _parse_building_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_name = _parse_building_name(d.pop("buildingName", UNSET))

        def _parse_rental_units(
            data: object,
        ) -> list[FetchRealEstateListingsResponse200OutputPropertiesItemRentalUnitsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rental_units_type_0 = []
                _rental_units_type_0 = data
                for rental_units_type_0_item_data in _rental_units_type_0:
                    rental_units_type_0_item = (
                        FetchRealEstateListingsResponse200OutputPropertiesItemRentalUnitsType0Item.from_dict(
                            rental_units_type_0_item_data
                        )
                    )

                    rental_units_type_0.append(rental_units_type_0_item)

                return rental_units_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[FetchRealEstateListingsResponse200OutputPropertiesItemRentalUnitsType0Item] | None | Unset, data
            )

        rental_units = _parse_rental_units(d.pop("rentalUnits", UNSET))

        def _parse_availability_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        availability_count = _parse_availability_count(d.pop("availabilityCount", UNSET))

        def _parse_base_rent(
            data: object,
        ) -> FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                base_rent_type_0 = FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0.from_dict(data)

                return base_rent_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FetchRealEstateListingsResponse200OutputPropertiesItemBaseRentType0 | None | Unset, data)

        base_rent = _parse_base_rent(d.pop("baseRent", UNSET))

        def _parse_availability_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        availability_date = _parse_availability_date(d.pop("availabilityDate", UNSET))

        def _parse_is_instant_tour_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_instant_tour_enabled = _parse_is_instant_tour_enabled(d.pop("isInstantTourEnabled", UNSET))

        def _parse_facts_and_features(
            data: object,
        ) -> FetchRealEstateListingsResponse200OutputPropertiesItemFactsAndFeaturesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                facts_and_features_type_0 = (
                    FetchRealEstateListingsResponse200OutputPropertiesItemFactsAndFeaturesType0.from_dict(data)
                )

                return facts_and_features_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FetchRealEstateListingsResponse200OutputPropertiesItemFactsAndFeaturesType0 | None | Unset, data
            )

        facts_and_features = _parse_facts_and_features(d.pop("factsAndFeatures", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        fetch_real_estate_listings_response_200_output_properties_item = cls(
            listing_id=listing_id,
            price=price,
            position=position,
            address=address,
            street=street,
            city=city,
            state=state,
            postal_code=postal_code,
            unit_number=unit_number,
            bedroom_count=bedroom_count,
            bathroom_count=bathroom_count,
            estimated_price=estimated_price,
            estimated_monthly_rent=estimated_monthly_rent,
            price_change_amount=price_change_amount,
            price_reduction_note=price_reduction_note,
            tax_assessed_value=tax_assessed_value,
            floor_area_sq_ft=floor_area_sq_ft,
            lot_area_sq_ft=lot_area_sq_ft,
            home_type=home_type,
            listing_lifecycle_status=listing_lifecycle_status,
            listing_status_label=listing_status_label,
            listing_type=listing_type,
            date_sold=date_sold,
            date_price_changed=date_price_changed,
            new_construction_type=new_construction_type,
            time_on_market_days=time_on_market_days,
            url=url,
            thumbnail_url=thumbnail_url,
            image_urls=image_urls,
            street_view_url=street_view_url,
            has_3_d_model=has_3_d_model,
            broker_name=broker_name,
            builder_name=builder_name,
            is_showcase_listing=is_showcase_listing,
            is_featured_listing=is_featured_listing,
            primary_tag=primary_tag,
            listing_tags=listing_tags,
            contact_phone=contact_phone,
            open_house=open_house,
            building_name=building_name,
            rental_units=rental_units,
            availability_count=availability_count,
            base_rent=base_rent,
            availability_date=availability_date,
            is_instant_tour_enabled=is_instant_tour_enabled,
            facts_and_features=facts_and_features,
            country_code=country_code,
            latitude=latitude,
            longitude=longitude,
        )

        fetch_real_estate_listings_response_200_output_properties_item.additional_properties = d
        return fetch_real_estate_listings_response_200_output_properties_item

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
