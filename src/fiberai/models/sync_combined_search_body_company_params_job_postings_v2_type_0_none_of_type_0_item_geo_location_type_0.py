from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sync_combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0_strategy import SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Strategy
from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.sync_combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0_radius_type_0 import SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType0
  from ..models.sync_combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0_center import SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Center
  from ..models.sync_combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0_radius_type_1 import SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType1





T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0")



@_attrs_define
class SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0:
    """ 
        Attributes:
            strategy (SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Strategy):
            center (SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Center):
            radius (Union['SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType0',
                'SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType1']):
     """

    strategy: SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Strategy
    center: 'SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Center'
    radius: Union['SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType0', 'SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType1']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0_radius_type_0 import SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType0
        from ..models.sync_combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0_center import SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Center
        from ..models.sync_combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0_radius_type_1 import SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType1
        strategy = self.strategy.value

        center = self.center.to_dict()

        radius: dict[str, Any]
        if isinstance(self.radius, SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType0):
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
        from ..models.sync_combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0_radius_type_0 import SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType0
        from ..models.sync_combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0_center import SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Center
        from ..models.sync_combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0_radius_type_1 import SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType1
        d = dict(src_dict)
        strategy = SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Strategy(d.pop("strategy"))




        center = SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Center.from_dict(d.pop("center"))




        def _parse_radius(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType0', 'SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType1']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                radius_type_0 = SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType0.from_dict(data)



                return radius_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            radius_type_1 = SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType1.from_dict(data)



            return radius_type_1

        radius = _parse_radius(d.pop("radius"))


        sync_combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0 = cls(
            strategy=strategy,
            center=center,
            radius=radius,
        )


        sync_combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0.additional_properties = d
        return sync_combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0

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
