from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0_none_of_type_0_item_type_2_location_type_0_radius_type_0_unit import (
    TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0NoneOfType0ItemType2LocationType0RadiusType0Unit,
)

T = TypeVar(
    "T",
    bound="TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0NoneOfType0ItemType2LocationType0RadiusType0",
)


@_attrs_define
class TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0NoneOfType0ItemType2LocationType0RadiusType0:
    """
    Attributes:
        unit (TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0NoneOfType0ItemType2Loc
            ationType0RadiusType0Unit):
        quantity (float):
    """

    unit: TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0NoneOfType0ItemType2LocationType0RadiusType0Unit
    quantity: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unit = self.unit.value

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unit": unit,
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unit = TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0NoneOfType0ItemType2LocationType0RadiusType0Unit(
            d.pop("unit")
        )

        quantity = d.pop("quantity")

        text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0_none_of_type_0_item_type_2_location_type_0_radius_type_0 = cls(
            unit=unit,
            quantity=quantity,
        )

        text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0_none_of_type_0_item_type_2_location_type_0_radius_type_0.additional_properties = d
        return text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0_none_of_type_0_item_type_2_location_type_0_radius_type_0

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
