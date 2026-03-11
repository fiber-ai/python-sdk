from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0_strategy import (
    CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Strategy,
)

if TYPE_CHECKING:
    from ..models.combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0_center import (
        CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Center,
    )
    from ..models.combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0_radius_type_0 import (
        CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType0,
    )
    from ..models.combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0_radius_type_1 import (
        CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType1,
    )


T = TypeVar("T", bound="CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0")


@_attrs_define
class CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0:
    """
    Attributes:
        strategy (CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Strategy):
        center (CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Center):
        radius (CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType0 |
            CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType1):
    """

    strategy: CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Strategy
    center: CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Center
    radius: (
        CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType0
        | CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType1
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0_radius_type_0 import (
            CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType0,
        )

        strategy = self.strategy.value

        center = self.center.to_dict()

        radius: dict[str, Any]
        if isinstance(
            self.radius, CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType0
        ):
            radius = self.radius.to_dict()
        else:
            radius = self.radius.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategy": strategy,
                "center": center,
                "radius": radius,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0_center import (
            CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Center,
        )
        from ..models.combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0_radius_type_0 import (
            CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType0,
        )
        from ..models.combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0_radius_type_1 import (
            CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType1,
        )

        d = dict(src_dict)
        strategy = CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Strategy(
            d.pop("strategy")
        )

        center = CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0Center.from_dict(
            d.pop("center")
        )

        def _parse_radius(
            data: object,
        ) -> (
            CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType0
            | CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType1
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                radius_type_0 = CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType0.from_dict(
                    data
                )

                return radius_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            radius_type_1 = (
                CombinedSearchBodyCompanyParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType0RadiusType1.from_dict(
                    data
                )
            )

            return radius_type_1

        radius = _parse_radius(d.pop("radius"))

        combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0 = cls(
            strategy=strategy,
            center=center,
            radius=radius,
        )

        combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0.additional_properties = d
        return combined_search_body_company_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_0

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
