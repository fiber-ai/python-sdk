from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_headquarters_location_type_0_subtract_all_type_0_item_type_1_strategy import (
    TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType1Strategy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_headquarters_location_type_0_subtract_all_type_0_item_type_1_radius_type_0 import (
        TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType1RadiusType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_headquarters_location_type_0_subtract_all_type_0_item_type_1_radius_type_1 import (
        TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType1RadiusType1,
    )


T = TypeVar(
    "T",
    bound="TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType1",
)


@_attrs_define
class TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType1:
    """
    Attributes:
        strategy (TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAll
            Type0ItemType1Strategy):
        city (str):
        radius (TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAllTy
            pe0ItemType1RadiusType0 | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocation
            Type0SubtractAllType0ItemType1RadiusType1):
        country_code (None | str | Unset):
    """

    strategy: TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType1Strategy
    city: str
    radius: (
        TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType1RadiusType0
        | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType1RadiusType1
    )
    country_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_headquarters_location_type_0_subtract_all_type_0_item_type_1_radius_type_0 import (
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType1RadiusType0,
        )

        strategy = self.strategy.value

        city = self.city

        radius: dict[str, Any]
        if isinstance(
            self.radius,
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType1RadiusType0,
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
        from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_headquarters_location_type_0_subtract_all_type_0_item_type_1_radius_type_0 import (
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType1RadiusType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_headquarters_location_type_0_subtract_all_type_0_item_type_1_radius_type_1 import (
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType1RadiusType1,
        )

        d = dict(src_dict)
        strategy = TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType1Strategy(
            d.pop("strategy")
        )

        city = d.pop("city")

        def _parse_radius(
            data: object,
        ) -> (
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType1RadiusType0
            | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType1RadiusType1
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                radius_type_0 = TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType1RadiusType0.from_dict(
                    data
                )

                return radius_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            radius_type_1 = TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType1RadiusType1.from_dict(
                data
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

        text_to_combined_search_param_response_200_output_company_search_params_type_0_headquarters_location_type_0_subtract_all_type_0_item_type_1 = cls(
            strategy=strategy,
            city=city,
            radius=radius,
            country_code=country_code,
        )

        text_to_combined_search_param_response_200_output_company_search_params_type_0_headquarters_location_type_0_subtract_all_type_0_item_type_1.additional_properties = d
        return text_to_combined_search_param_response_200_output_company_search_params_type_0_headquarters_location_type_0_subtract_all_type_0_item_type_1

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
