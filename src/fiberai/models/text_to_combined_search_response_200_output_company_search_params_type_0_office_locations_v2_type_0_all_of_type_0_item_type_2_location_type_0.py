from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_strategy import TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0Strategy
from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_radius_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType0
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_radius_type_1 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType1
  from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_center import TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0Center





T = TypeVar("T", bound="TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0")



@_attrs_define
class TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0:
    """ 
        Attributes:
            strategy (TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2
                LocationType0Strategy):
            center (TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2Lo
                cationType0Center):
            radius (Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0Item
                Type2LocationType0RadiusType0', 'TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2T
                ype0AllOfType0ItemType2LocationType0RadiusType1']):
     """

    strategy: TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0Strategy
    center: 'TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0Center'
    radius: Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType0', 'TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType1']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_radius_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_radius_type_1 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType1
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_center import TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0Center
        strategy = self.strategy.value

        center = self.center.to_dict()

        radius: dict[str, Any]
        if isinstance(self.radius, TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType0):
            radius = self.radius.to_dict()
        else:
            radius = self.radius.to_dict()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "strategy": strategy,
            "center": center,
            "radius": radius,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_radius_type_0 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType0
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_radius_type_1 import TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType1
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_center import TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0Center
        d = dict(src_dict)
        strategy = TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0Strategy(d.pop("strategy"))




        center = TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0Center.from_dict(d.pop("center"))




        def _parse_radius(data: object) -> Union['TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType0', 'TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType1']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                radius_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType0.from_dict(data)



                return radius_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            radius_type_1 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0OfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType1.from_dict(data)



            return radius_type_1

        radius = _parse_radius(d.pop("radius"))


        text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0 = cls(
            strategy=strategy,
            center=center,
            radius=radius,
        )


        text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0.additional_properties = d
        return text_to_combined_search_response_200_output_company_search_params_type_0_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0

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
