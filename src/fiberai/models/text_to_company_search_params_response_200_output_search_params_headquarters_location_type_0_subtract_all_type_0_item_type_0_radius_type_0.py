from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.text_to_company_search_params_response_200_output_search_params_headquarters_location_type_0_subtract_all_type_0_item_type_0_radius_type_0_unit import TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0SubtractAllType0ItemType0RadiusType0Unit






T = TypeVar("T", bound="TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0SubtractAllType0ItemType0RadiusType0")



@_attrs_define
class TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0SubtractAllType0ItemType0RadiusType0:
    """ 
        Attributes:
            unit (TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0SubtractAllType0ItemType0Ra
                diusType0Unit):
            quantity (float):
     """

    unit: TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0SubtractAllType0ItemType0RadiusType0Unit
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
        unit = TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0SubtractAllType0ItemType0RadiusType0Unit(d.pop("unit"))




        quantity = d.pop("quantity")

        text_to_company_search_params_response_200_output_search_params_headquarters_location_type_0_subtract_all_type_0_item_type_0_radius_type_0 = cls(
            unit=unit,
            quantity=quantity,
        )


        text_to_company_search_params_response_200_output_search_params_headquarters_location_type_0_subtract_all_type_0_item_type_0_radius_type_0.additional_properties = d
        return text_to_company_search_params_response_200_output_search_params_headquarters_location_type_0_subtract_all_type_0_item_type_0_radius_type_0

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
