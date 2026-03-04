from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.combined_search_body_company_params_job_postings_v2_type_0_all_of_type_0_item_geo_location_type_0_radius_type_1_unit import CombinedSearchBodyCompanyParamsJobPostingsV2Type0AllOfType0ItemGeoLocationType0RadiusType1Unit






T = TypeVar("T", bound="CombinedSearchBodyCompanyParamsJobPostingsV2Type0AllOfType0ItemGeoLocationType0RadiusType1")



@_attrs_define
class CombinedSearchBodyCompanyParamsJobPostingsV2Type0AllOfType0ItemGeoLocationType0RadiusType1:
    """ 
        Attributes:
            unit (CombinedSearchBodyCompanyParamsJobPostingsV2Type0AllOfType0ItemGeoLocationType0RadiusType1Unit):
            quantity (float):
     """

    unit: CombinedSearchBodyCompanyParamsJobPostingsV2Type0AllOfType0ItemGeoLocationType0RadiusType1Unit
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
        unit = CombinedSearchBodyCompanyParamsJobPostingsV2Type0AllOfType0ItemGeoLocationType0RadiusType1Unit(d.pop("unit"))




        quantity = d.pop("quantity")

        combined_search_body_company_params_job_postings_v2_type_0_all_of_type_0_item_geo_location_type_0_radius_type_1 = cls(
            unit=unit,
            quantity=quantity,
        )


        combined_search_body_company_params_job_postings_v2_type_0_all_of_type_0_item_geo_location_type_0_radius_type_1.additional_properties = d
        return combined_search_body_company_params_job_postings_v2_type_0_all_of_type_0_item_geo_location_type_0_radius_type_1

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
