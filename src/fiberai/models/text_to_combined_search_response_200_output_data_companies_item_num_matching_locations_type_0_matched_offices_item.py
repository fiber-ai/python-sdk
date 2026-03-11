from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_combined_search_response_200_output_data_companies_item_num_matching_locations_type_0_matched_offices_item_location_type_0 import (
        TextToCombinedSearchResponse200OutputDataCompaniesItemNumMatchingLocationsType0MatchedOfficesItemLocationType0,
    )


T = TypeVar(
    "T", bound="TextToCombinedSearchResponse200OutputDataCompaniesItemNumMatchingLocationsType0MatchedOfficesItem"
)


@_attrs_define
class TextToCombinedSearchResponse200OutputDataCompaniesItemNumMatchingLocationsType0MatchedOfficesItem:
    """
    Attributes:
        address (None | str | Unset):
        is_primary (bool | None | Unset):
        location (None |
            TextToCombinedSearchResponse200OutputDataCompaniesItemNumMatchingLocationsType0MatchedOfficesItemLocationType0 |
            Unset):
    """

    address: None | str | Unset = UNSET
    is_primary: bool | None | Unset = UNSET
    location: (
        None
        | TextToCombinedSearchResponse200OutputDataCompaniesItemNumMatchingLocationsType0MatchedOfficesItemLocationType0
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_response_200_output_data_companies_item_num_matching_locations_type_0_matched_offices_item_location_type_0 import (
            TextToCombinedSearchResponse200OutputDataCompaniesItemNumMatchingLocationsType0MatchedOfficesItemLocationType0,
        )

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        is_primary: bool | None | Unset
        if isinstance(self.is_primary, Unset):
            is_primary = UNSET
        else:
            is_primary = self.is_primary

        location: dict[str, Any] | None | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(
            self.location,
            TextToCombinedSearchResponse200OutputDataCompaniesItemNumMatchingLocationsType0MatchedOfficesItemLocationType0,
        ):
            location = self.location.to_dict()
        else:
            location = self.location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if is_primary is not UNSET:
            field_dict["is_primary"] = is_primary
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_combined_search_response_200_output_data_companies_item_num_matching_locations_type_0_matched_offices_item_location_type_0 import (
            TextToCombinedSearchResponse200OutputDataCompaniesItemNumMatchingLocationsType0MatchedOfficesItemLocationType0,
        )

        d = dict(src_dict)

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_is_primary(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_primary = _parse_is_primary(d.pop("is_primary", UNSET))

        def _parse_location(
            data: object,
        ) -> (
            None
            | TextToCombinedSearchResponse200OutputDataCompaniesItemNumMatchingLocationsType0MatchedOfficesItemLocationType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = TextToCombinedSearchResponse200OutputDataCompaniesItemNumMatchingLocationsType0MatchedOfficesItemLocationType0.from_dict(
                    data
                )

                return location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchResponse200OutputDataCompaniesItemNumMatchingLocationsType0MatchedOfficesItemLocationType0
                | Unset,
                data,
            )

        location = _parse_location(d.pop("location", UNSET))

        text_to_combined_search_response_200_output_data_companies_item_num_matching_locations_type_0_matched_offices_item = cls(
            address=address,
            is_primary=is_primary,
            location=location,
        )

        text_to_combined_search_response_200_output_data_companies_item_num_matching_locations_type_0_matched_offices_item.additional_properties = d
        return text_to_combined_search_response_200_output_data_companies_item_num_matching_locations_type_0_matched_offices_item

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
