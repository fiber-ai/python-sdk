from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_li_locations_type_0_item_location_type_0 import (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiLocationsType0ItemLocationType0,
    )


T = TypeVar("T", bound="GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiLocationsType0Item")


@_attrs_define
class GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiLocationsType0Item:
    """
    Attributes:
        address (None | str | Unset):
        is_primary (bool | None | Unset):
        location (GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiLocationsType0ItemLocationType0 |
            None | Unset):
    """

    address: None | str | Unset = UNSET
    is_primary: bool | None | Unset = UNSET
    location: (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiLocationsType0ItemLocationType0 | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_li_locations_type_0_item_location_type_0 import (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiLocationsType0ItemLocationType0,
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
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiLocationsType0ItemLocationType0,
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
        from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_li_locations_type_0_item_location_type_0 import (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiLocationsType0ItemLocationType0,
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
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiLocationsType0ItemLocationType0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiLocationsType0ItemLocationType0.from_dict(
                    data
                )

                return location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyLiLocationsType0ItemLocationType0
                | None
                | Unset,
                data,
            )

        location = _parse_location(d.pop("location", UNSET))

        get_saved_search_run_companies_response_200_output_companies_item_company_li_locations_type_0_item = cls(
            address=address,
            is_primary=is_primary,
            location=location,
        )

        get_saved_search_run_companies_response_200_output_companies_item_company_li_locations_type_0_item.additional_properties = d
        return get_saved_search_run_companies_response_200_output_companies_item_company_li_locations_type_0_item

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
