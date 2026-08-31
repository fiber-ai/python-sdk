from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.combined_search_count_body_company_params_office_locations_v2_type_0_none_of_type_0_item_type_2_location_type_2_strategy import (
    CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType2Strategy,
)

if TYPE_CHECKING:
    from ..models.combined_search_count_body_company_params_office_locations_v2_type_0_none_of_type_0_item_type_2_location_type_2_vertices_item import (
        CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType2VerticesItem,
    )


T = TypeVar("T", bound="CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType2")


@_attrs_define
class CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType2:
    """
    Attributes:
        strategy (CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType2Strategy):
        vertices
            (list[CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType2VerticesItem]):
    """

    strategy: CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType2Strategy
    vertices: list[
        CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType2VerticesItem
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy = self.strategy.value

        vertices = []
        for vertices_item_data in self.vertices:
            vertices_item = vertices_item_data.to_dict()
            vertices.append(vertices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategy": strategy,
                "vertices": vertices,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.combined_search_count_body_company_params_office_locations_v2_type_0_none_of_type_0_item_type_2_location_type_2_vertices_item import (
            CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType2VerticesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        strategy = CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType2Strategy(
            d.pop("strategy")
        )

        vertices = []
        _vertices = d.pop("vertices")
        for vertices_item_data in _vertices:
            vertices_item = CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType2LocationType2VerticesItem.from_dict(
                vertices_item_data
            )

            vertices.append(vertices_item)

        combined_search_count_body_company_params_office_locations_v2_type_0_none_of_type_0_item_type_2_location_type_2 = cls(
            strategy=strategy,
            vertices=vertices,
        )

        combined_search_count_body_company_params_office_locations_v2_type_0_none_of_type_0_item_type_2_location_type_2.additional_properties = d
        return combined_search_count_body_company_params_office_locations_v2_type_0_none_of_type_0_item_type_2_location_type_2

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
