from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_search_body_search_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_1_strategy import (
    CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1Strategy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_search_body_search_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_1_radius_type_0 import (
        CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1RadiusType0,
    )
    from ..models.company_search_body_search_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_1_radius_type_1 import (
        CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1RadiusType1,
    )


T = TypeVar("T", bound="CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1")


@_attrs_define
class CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1:
    """
    Attributes:
        strategy (CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1Strategy):
        city (str):
        radius (CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1RadiusType0 |
            CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1RadiusType1):
        country_code (None | str | Unset):
    """

    strategy: CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1Strategy
    city: str
    radius: (
        CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1RadiusType0
        | CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1RadiusType1
    )
    country_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_search_body_search_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_1_radius_type_0 import (
            CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1RadiusType0,
        )

        strategy = self.strategy.value

        city = self.city

        radius: dict[str, Any]
        if isinstance(
            self.radius, CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1RadiusType0
        ):
            radius = self.radius.to_dict()
        else:
            radius = self.radius.to_dict()

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategy": strategy,
                "city": city,
                "radius": radius,
            }
        )
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_search_body_search_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_1_radius_type_0 import (
            CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1RadiusType0,
        )
        from ..models.company_search_body_search_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_1_radius_type_1 import (
            CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1RadiusType1,
        )

        d = dict(src_dict)
        strategy = CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1Strategy(
            d.pop("strategy")
        )

        city = d.pop("city")

        def _parse_radius(
            data: object,
        ) -> (
            CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1RadiusType0
            | CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1RadiusType1
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                radius_type_0 = (
                    CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1RadiusType0.from_dict(
                        data
                    )
                )

                return radius_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            radius_type_1 = (
                CompanySearchBodySearchParamsJobPostingsV2Type0NoneOfType0ItemGeoLocationType1RadiusType1.from_dict(
                    data
                )
            )

            return radius_type_1

        radius = _parse_radius(d.pop("radius"))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        company_search_body_search_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_1 = cls(
            strategy=strategy,
            city=city,
            radius=radius,
            country_code=country_code,
        )

        company_search_body_search_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_1.additional_properties = d
        return company_search_body_search_params_job_postings_v2_type_0_none_of_type_0_item_geo_location_type_1

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
