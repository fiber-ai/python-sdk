from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.combined_search_body_company_params_office_locations_v2_type_0_all_of_type_0_item_type_2_type import CombinedSearchBodyCompanyParamsOfficeLocationsV2Type0AllOfType0ItemType2Type
from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.combined_search_body_company_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0 import CombinedSearchBodyCompanyParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0





T = TypeVar("T", bound="CombinedSearchBodyCompanyParamsOfficeLocationsV2Type0AllOfType0ItemType2")



@_attrs_define
class CombinedSearchBodyCompanyParamsOfficeLocationsV2Type0AllOfType0ItemType2:
    """ 
        Attributes:
            type_ (CombinedSearchBodyCompanyParamsOfficeLocationsV2Type0AllOfType0ItemType2Type):
            location ('CombinedSearchBodyCompanyParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0'):
     """

    type_: CombinedSearchBodyCompanyParamsOfficeLocationsV2Type0AllOfType0ItemType2Type
    location: 'CombinedSearchBodyCompanyParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.combined_search_body_company_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0 import CombinedSearchBodyCompanyParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0
        type_ = self.type_.value

        location: dict[str, Any]
        if isinstance(self.location, CombinedSearchBodyCompanyParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0):
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
        from ..models.combined_search_body_company_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0 import CombinedSearchBodyCompanyParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0
        d = dict(src_dict)
        type_ = CombinedSearchBodyCompanyParamsOfficeLocationsV2Type0AllOfType0ItemType2Type(d.pop("type"))




        def _parse_location(data: object) -> 'CombinedSearchBodyCompanyParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0':
            if not isinstance(data, dict):
                raise TypeError()
            location_type_0 = CombinedSearchBodyCompanyParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0.from_dict(data)



            return location_type_0

        location = _parse_location(d.pop("location"))


        combined_search_body_company_params_office_locations_v2_type_0_all_of_type_0_item_type_2 = cls(
            type_=type_,
            location=location,
        )


        combined_search_body_company_params_office_locations_v2_type_0_all_of_type_0_item_type_2.additional_properties = d
        return combined_search_body_company_params_office_locations_v2_type_0_all_of_type_0_item_type_2

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
