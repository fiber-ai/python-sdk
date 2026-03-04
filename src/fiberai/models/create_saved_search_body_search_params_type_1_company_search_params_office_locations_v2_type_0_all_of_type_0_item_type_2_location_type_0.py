from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_saved_search_body_search_params_type_1_company_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_strategy import CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0Strategy
from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.create_saved_search_body_search_params_type_1_company_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_center import CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0Center
  from ..models.create_saved_search_body_search_params_type_1_company_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_radius_type_1 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType1
  from ..models.create_saved_search_body_search_params_type_1_company_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_radius_type_0 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType0





T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0")



@_attrs_define
class CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0:
    """ 
        Attributes:
            strategy (CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2Loca
                tionType0Strategy):
            center (CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2Locati
                onType0Center):
            radius (Union['CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType
                2LocationType0RadiusType0', 'CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllO
                fType0ItemType2LocationType0RadiusType1']):
     """

    strategy: CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0Strategy
    center: 'CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0Center'
    radius: Union['CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType0', 'CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType1']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_center import CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0Center
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_radius_type_1 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType1
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_radius_type_0 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType0
        strategy = self.strategy.value

        center = self.center.to_dict()

        radius: dict[str, Any]
        if isinstance(self.radius, CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType0):
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
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_center import CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0Center
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_radius_type_1 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType1
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0_radius_type_0 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType0
        d = dict(src_dict)
        strategy = CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0Strategy(d.pop("strategy"))




        center = CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0Center.from_dict(d.pop("center"))




        def _parse_radius(data: object) -> Union['CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType0', 'CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType1']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                radius_type_0 = CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType0.from_dict(data)



                return radius_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            radius_type_1 = CreateSavedSearchBodySearchParamsType1CompanySearchParamsOfficeLocationsV2Type0AllOfType0ItemType2LocationType0RadiusType1.from_dict(data)



            return radius_type_1

        radius = _parse_radius(d.pop("radius"))


        create_saved_search_body_search_params_type_1_company_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0 = cls(
            strategy=strategy,
            center=center,
            radius=radius,
        )


        create_saved_search_body_search_params_type_1_company_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0.additional_properties = d
        return create_saved_search_body_search_params_type_1_company_search_params_office_locations_v2_type_0_all_of_type_0_item_type_2_location_type_0

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
