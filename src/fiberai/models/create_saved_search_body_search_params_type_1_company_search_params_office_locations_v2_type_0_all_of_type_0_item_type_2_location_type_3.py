from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_saved_search_body_search_params_type_1_company_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_3_region import (
    CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType3Region,
)
from ..models.create_saved_search_body_search_params_type_1_company_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_3_strategy import (
    CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType3Strategy,
)

T = TypeVar(
    "T",
    bound="CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType3",
)


@_attrs_define
class CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType3:
    """
    Attributes:
        strategy (CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2Loca
            tionType3Strategy):
        region (CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2Locati
            onType3Region):
    """

    strategy: CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType3Strategy
    region: CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType3Region
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy = self.strategy.value

        region = self.region.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategy": strategy,
                "region": region,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        strategy = CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType3Strategy(
            d.pop("strategy")
        )

        region = CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType3Region(
            d.pop("region")
        )

        create_saved_search_body_search_params_type_1_company_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_3 = cls(
            strategy=strategy,
            region=region,
        )

        create_saved_search_body_search_params_type_1_company_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_3.additional_properties = d
        return create_saved_search_body_search_params_type_1_company_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_3

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
