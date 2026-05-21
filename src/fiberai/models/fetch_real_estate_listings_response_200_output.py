from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fetch_real_estate_listings_response_200_output_properties_item import (
        FetchRealEstateListingsResponse200OutputPropertiesItem,
    )


T = TypeVar("T", bound="FetchRealEstateListingsResponse200Output")


@_attrs_define
class FetchRealEstateListingsResponse200Output:
    r"""
    Attributes:
        run_id (str): Unique identifier for this search request.
        properties (list[FetchRealEstateListingsResponse200OutputPropertiesItem]): Properties returned for this page.
        total_result_count (int | None | Unset): Total number of matching listings.
        region_name (None | str | Unset): Region name interpreted for this search query.
        next_page_token (None | str | Unset): Token for retrieving the next page. Pass this exact value as
            `nextPageToken` in the next request. Null if no more pages.
        warnings (list[str] | None | Unset): Non-fatal advisories about how this page was served. For example, 'Sort
            \'priceAscending\' is applied from page 2 onwards.' when the requested sort cannot be honored on page 1. Omitted
            or null when there's nothing to flag.
    """

    run_id: str
    properties: list[FetchRealEstateListingsResponse200OutputPropertiesItem]
    total_result_count: int | None | Unset = UNSET
    region_name: None | str | Unset = UNSET
    next_page_token: None | str | Unset = UNSET
    warnings: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        properties = []
        for properties_item_data in self.properties:
            properties_item = properties_item_data.to_dict()
            properties.append(properties_item)

        total_result_count: int | None | Unset
        if isinstance(self.total_result_count, Unset):
            total_result_count = UNSET
        else:
            total_result_count = self.total_result_count

        region_name: None | str | Unset
        if isinstance(self.region_name, Unset):
            region_name = UNSET
        else:
            region_name = self.region_name

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        warnings: list[str] | None | Unset
        if isinstance(self.warnings, Unset):
            warnings = UNSET
        elif isinstance(self.warnings, list):
            warnings = self.warnings

        else:
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runId": run_id,
                "properties": properties,
            }
        )
        if total_result_count is not UNSET:
            field_dict["totalResultCount"] = total_result_count
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fetch_real_estate_listings_response_200_output_properties_item import (
            FetchRealEstateListingsResponse200OutputPropertiesItem,
        )

        d = dict(src_dict)
        run_id = d.pop("runId")

        properties = []
        _properties = d.pop("properties")
        for properties_item_data in _properties:
            properties_item = FetchRealEstateListingsResponse200OutputPropertiesItem.from_dict(properties_item_data)

            properties.append(properties_item)

        def _parse_total_result_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_result_count = _parse_total_result_count(d.pop("totalResultCount", UNSET))

        def _parse_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name = _parse_region_name(d.pop("regionName", UNSET))

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        def _parse_warnings(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = cast(list[str], data)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        warnings = _parse_warnings(d.pop("warnings", UNSET))

        fetch_real_estate_listings_response_200_output = cls(
            run_id=run_id,
            properties=properties,
            total_result_count=total_result_count,
            region_name=region_name,
            next_page_token=next_page_token,
            warnings=warnings,
        )

        fetch_real_estate_listings_response_200_output.additional_properties = d
        return fetch_real_estate_listings_response_200_output

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
