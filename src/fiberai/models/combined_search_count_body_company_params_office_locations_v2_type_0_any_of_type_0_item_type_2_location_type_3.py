from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_3_region import (
    CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3Region,
)
from ..models.combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_3_strategy import (
    CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3Strategy,
)

T = TypeVar("T", bound="CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3")


@_attrs_define
class CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3:
    """
    Attributes:
        strategy (CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3Strategy):
        region (CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3Region):
    """

    strategy: CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3Strategy
    region: CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3Region
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
        strategy = CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3Strategy(
            d.pop("strategy")
        )

        region = CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3Region(
            d.pop("region")
        )

        combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_3 = cls(
            strategy=strategy,
            region=region,
        )

        combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_3.additional_properties = d
        return combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_3

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
