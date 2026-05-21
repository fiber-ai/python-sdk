from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_search_body_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_2_region import (
    CompanySearchBodySearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2Region,
)
from ..models.company_search_body_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_2_strategy import (
    CompanySearchBodySearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2Strategy,
)

T = TypeVar("T", bound="CompanySearchBodySearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2")


@_attrs_define
class CompanySearchBodySearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2:
    """
    Attributes:
        strategy (CompanySearchBodySearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2Strategy):
        region (CompanySearchBodySearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2Region):
    """

    strategy: CompanySearchBodySearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2Strategy
    region: CompanySearchBodySearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2Region
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
        strategy = CompanySearchBodySearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2Strategy(
            d.pop("strategy")
        )

        region = CompanySearchBodySearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2Region(
            d.pop("region")
        )

        company_search_body_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_2 = cls(
            strategy=strategy,
            region=region,
        )

        company_search_body_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_2.additional_properties = d
        return company_search_body_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_2

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
