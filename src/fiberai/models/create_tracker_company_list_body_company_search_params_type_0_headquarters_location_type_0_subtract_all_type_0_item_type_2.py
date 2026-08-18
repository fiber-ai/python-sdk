from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_tracker_company_list_body_company_search_params_type_0_headquarters_location_type_0_subtract_all_type_0_item_type_2_strategy import (
    CreateTrackerCompanyListBodyCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType2Strategy,
)

if TYPE_CHECKING:
    from ..models.create_tracker_company_list_body_company_search_params_type_0_headquarters_location_type_0_subtract_all_type_0_item_type_2_vertices_item import (
        CreateTrackerCompanyListBodyCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType2VerticesItem,
    )


T = TypeVar(
    "T", bound="CreateTrackerCompanyListBodyCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType2"
)


@_attrs_define
class CreateTrackerCompanyListBodyCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType2:
    """
    Attributes:
        strategy (CreateTrackerCompanyListBodyCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType2
            Strategy):
        vertices (list[CreateTrackerCompanyListBodyCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0Item
            Type2VerticesItem]):
    """

    strategy: (
        CreateTrackerCompanyListBodyCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType2Strategy
    )
    vertices: list[
        CreateTrackerCompanyListBodyCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType2VerticesItem
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
        from ..models.create_tracker_company_list_body_company_search_params_type_0_headquarters_location_type_0_subtract_all_type_0_item_type_2_vertices_item import (
            CreateTrackerCompanyListBodyCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType2VerticesItem,
        )

        d = dict(src_dict)
        strategy = CreateTrackerCompanyListBodyCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType2Strategy(
            d.pop("strategy")
        )

        vertices = []
        _vertices = d.pop("vertices")
        for vertices_item_data in _vertices:
            vertices_item = CreateTrackerCompanyListBodyCompanySearchParamsType0HeadquartersLocationType0SubtractAllType0ItemType2VerticesItem.from_dict(
                vertices_item_data
            )

            vertices.append(vertices_item)

        create_tracker_company_list_body_company_search_params_type_0_headquarters_location_type_0_subtract_all_type_0_item_type_2 = cls(
            strategy=strategy,
            vertices=vertices,
        )

        create_tracker_company_list_body_company_search_params_type_0_headquarters_location_type_0_subtract_all_type_0_item_type_2.additional_properties = d
        return create_tracker_company_list_body_company_search_params_type_0_headquarters_location_type_0_subtract_all_type_0_item_type_2

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
