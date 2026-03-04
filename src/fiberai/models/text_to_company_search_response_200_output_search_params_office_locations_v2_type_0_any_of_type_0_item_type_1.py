from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.text_to_company_search_response_200_output_search_params_office_locations_v2_type_0_any_of_type_0_item_type_1_country_or_region_code import TextToCompanySearchResponse200OutputSearchParamsOfficeLocationsV2Type0AnyOfType0ItemType1CountryOrRegionCode
from ..models.text_to_company_search_response_200_output_search_params_office_locations_v2_type_0_any_of_type_0_item_type_1_type import TextToCompanySearchResponse200OutputSearchParamsOfficeLocationsV2Type0AnyOfType0ItemType1Type
from typing import cast

if TYPE_CHECKING:
  from ..models.text_to_company_search_response_200_output_search_params_office_locations_v2_type_0_any_of_type_0_item_type_1_range import TextToCompanySearchResponse200OutputSearchParamsOfficeLocationsV2Type0AnyOfType0ItemType1Range





T = TypeVar("T", bound="TextToCompanySearchResponse200OutputSearchParamsOfficeLocationsV2Type0AnyOfType0ItemType1")



@_attrs_define
class TextToCompanySearchResponse200OutputSearchParamsOfficeLocationsV2Type0AnyOfType0ItemType1:
    """ 
        Attributes:
            type_ (TextToCompanySearchResponse200OutputSearchParamsOfficeLocationsV2Type0AnyOfType0ItemType1Type):
            range_ (TextToCompanySearchResponse200OutputSearchParamsOfficeLocationsV2Type0AnyOfType0ItemType1Range):
            country_or_region_code
                (TextToCompanySearchResponse200OutputSearchParamsOfficeLocationsV2Type0AnyOfType0ItemType1CountryOrRegionCode):
     """

    type_: TextToCompanySearchResponse200OutputSearchParamsOfficeLocationsV2Type0AnyOfType0ItemType1Type
    range_: 'TextToCompanySearchResponse200OutputSearchParamsOfficeLocationsV2Type0AnyOfType0ItemType1Range'
    country_or_region_code: TextToCompanySearchResponse200OutputSearchParamsOfficeLocationsV2Type0AnyOfType0ItemType1CountryOrRegionCode
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_company_search_response_200_output_search_params_office_locations_v2_type_0_any_of_type_0_item_type_1_range import TextToCompanySearchResponse200OutputSearchParamsOfficeLocationsV2Type0AnyOfType0ItemType1Range
        type_ = self.type_.value

        range_ = self.range_.to_dict()

        country_or_region_code = self.country_or_region_code.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "range": range_,
            "countryOrRegionCode": country_or_region_code,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_company_search_response_200_output_search_params_office_locations_v2_type_0_any_of_type_0_item_type_1_range import TextToCompanySearchResponse200OutputSearchParamsOfficeLocationsV2Type0AnyOfType0ItemType1Range
        d = dict(src_dict)
        type_ = TextToCompanySearchResponse200OutputSearchParamsOfficeLocationsV2Type0AnyOfType0ItemType1Type(d.pop("type"))




        range_ = TextToCompanySearchResponse200OutputSearchParamsOfficeLocationsV2Type0AnyOfType0ItemType1Range.from_dict(d.pop("range"))




        country_or_region_code = TextToCompanySearchResponse200OutputSearchParamsOfficeLocationsV2Type0AnyOfType0ItemType1CountryOrRegionCode(d.pop("countryOrRegionCode"))




        text_to_company_search_response_200_output_search_params_office_locations_v2_type_0_any_of_type_0_item_type_1 = cls(
            type_=type_,
            range_=range_,
            country_or_region_code=country_or_region_code,
        )


        text_to_company_search_response_200_output_search_params_office_locations_v2_type_0_any_of_type_0_item_type_1.additional_properties = d
        return text_to_company_search_response_200_output_search_params_office_locations_v2_type_0_any_of_type_0_item_type_1

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
