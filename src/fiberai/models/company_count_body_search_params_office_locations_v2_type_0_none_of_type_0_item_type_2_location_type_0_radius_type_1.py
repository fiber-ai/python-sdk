from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.company_count_body_search_params_office_locations_v2_type_0_none_of_type_0_item_type_2_location_type_0_radius_type_1_unit import CompanyCountBodySearchParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType0RadiusType1Unit






T = TypeVar("T", bound="CompanyCountBodySearchParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType0RadiusType1")



@_attrs_define
class CompanyCountBodySearchParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType0RadiusType1:
    """ 
        Attributes:
            unit (CompanyCountBodySearchParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType0RadiusType1Unit):
            quantity (float):
     """

    unit: CompanyCountBodySearchParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType0RadiusType1Unit
    quantity: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        unit = self.unit.value

        quantity = self.quantity


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "unit": unit,
            "quantity": quantity,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unit = CompanyCountBodySearchParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType0RadiusType1Unit(d.pop("unit"))




        quantity = d.pop("quantity")

        company_count_body_search_params_office_locations_v2_type_0_none_of_type_0_item_type_2_location_type_0_radius_type_1 = cls(
            unit=unit,
            quantity=quantity,
        )


        company_count_body_search_params_office_locations_v2_type_0_none_of_type_0_item_type_2_location_type_0_radius_type_1.additional_properties = d
        return company_count_body_search_params_office_locations_v2_type_0_none_of_type_0_item_type_2_location_type_0_radius_type_1

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
