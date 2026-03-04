from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.text_to_company_search_params_response_200_output_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_type import TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0AllOfType0ItemType2Type
from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.text_to_company_search_params_response_200_output_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0 import TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0





T = TypeVar("T", bound="TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0AllOfType0ItemType2")



@_attrs_define
class TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0AllOfType0ItemType2:
    """ 
        Attributes:
            type_ (TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0AllOfType0ItemType2Type):
            location ('TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0AllOfType0ItemType2Locati
                onType0'):
     """

    type_: TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0AllOfType0ItemType2Type
    location: 'TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_company_search_params_response_200_output_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0 import TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0
        type_ = self.type_.value

        location: dict[str, Any]
        if isinstance(self.location, TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0):
            location = self.location.to_dict()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "location": location,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_company_search_params_response_200_output_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0 import TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0
        d = dict(src_dict)
        type_ = TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0AllOfType0ItemType2Type(d.pop("type"))




        def _parse_location(data: object) -> 'TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0':
            if not isinstance(data, dict):
                raise TypeError()
            location_type_0 = TextToCompanySearchParamsResponse200OutputSearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0.from_dict(data)



            return location_type_0

        location = _parse_location(d.pop("location"))


        text_to_company_search_params_response_200_output_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2 = cls(
            type_=type_,
            location=location,
        )


        text_to_company_search_params_response_200_output_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2.additional_properties = d
        return text_to_company_search_params_response_200_output_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2

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
