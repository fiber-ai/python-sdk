from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_to_company_search_params_response_200_output_search_params_headquarters_location_type_0_union_all_type_0_item_type_0_strategy import (
    TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0Strategy,
)

if TYPE_CHECKING:
    from ..models.text_to_company_search_params_response_200_output_search_params_headquarters_location_type_0_union_all_type_0_item_type_0_center import (
        TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0Center,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_headquarters_location_type_0_union_all_type_0_item_type_0_radius_type_0 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0RadiusType0,
    )
    from ..models.text_to_company_search_params_response_200_output_search_params_headquarters_location_type_0_union_all_type_0_item_type_0_radius_type_1 import (
        TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0RadiusType1,
    )


T = TypeVar(
    "T", bound="TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0"
)


@_attrs_define
class TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0:
    """
    Attributes:
        strategy
            (TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0Strategy):
        center
            (TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0Center):
        radius (TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0Rad
            iusType0 | TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0
            RadiusType1):
    """

    strategy: (
        TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0Strategy
    )
    center: TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0Center
    radius: (
        TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0RadiusType0
        | TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0RadiusType1
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_company_search_params_response_200_output_search_params_headquarters_location_type_0_union_all_type_0_item_type_0_radius_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0RadiusType0,
        )

        strategy = self.strategy.value

        center = self.center.to_dict()

        radius: dict[str, Any]
        if isinstance(
            self.radius,
            TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0RadiusType0,
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
        from ..models.text_to_company_search_params_response_200_output_search_params_headquarters_location_type_0_union_all_type_0_item_type_0_center import (
            TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0Center,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_headquarters_location_type_0_union_all_type_0_item_type_0_radius_type_0 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0RadiusType0,
        )
        from ..models.text_to_company_search_params_response_200_output_search_params_headquarters_location_type_0_union_all_type_0_item_type_0_radius_type_1 import (
            TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0RadiusType1,
        )

        d = dict(src_dict)
        strategy = TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0Strategy(
            d.pop("strategy")
        )

        center = TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0Center.from_dict(
            d.pop("center")
        )

        def _parse_radius(
            data: object,
        ) -> (
            TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0RadiusType0
            | TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0RadiusType1
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                radius_type_0 = TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0RadiusType0.from_dict(
                    data
                )

                return radius_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            radius_type_1 = TextToCompanySearchParamsResponse200OutputSearchParamsHeadquartersLocationType0UnionAllType0ItemType0RadiusType1.from_dict(
                data
            )

            return radius_type_1

        radius = _parse_radius(d.pop("radius"))

        text_to_company_search_params_response_200_output_search_params_headquarters_location_type_0_union_all_type_0_item_type_0 = cls(
            strategy=strategy,
            center=center,
            radius=radius,
        )

        text_to_company_search_params_response_200_output_search_params_headquarters_location_type_0_union_all_type_0_item_type_0.additional_properties = d
        return text_to_company_search_params_response_200_output_search_params_headquarters_location_type_0_union_all_type_0_item_type_0

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
