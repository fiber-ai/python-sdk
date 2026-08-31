from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_search_body_search_params_headquarters_location_type_0_subtract_all_type_0_item_type_2_strategy import (
    CompanySearchBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType2Strategy,
)

if TYPE_CHECKING:
    from ..models.company_search_body_search_params_headquarters_location_type_0_subtract_all_type_0_item_type_2_vertices_item import (
        CompanySearchBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType2VerticesItem,
    )


T = TypeVar("T", bound="CompanySearchBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType2")


@_attrs_define
class CompanySearchBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType2:
    """
    Attributes:
        strategy (CompanySearchBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType2Strategy):
        vertices (list[CompanySearchBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType2VerticesItem]):
    """

    strategy: CompanySearchBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType2Strategy
    vertices: list[CompanySearchBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType2VerticesItem]
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
        from ..models.company_search_body_search_params_headquarters_location_type_0_subtract_all_type_0_item_type_2_vertices_item import (
            CompanySearchBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType2VerticesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        strategy = CompanySearchBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType2Strategy(
            d.pop("strategy")
        )

        vertices = []
        _vertices = d.pop("vertices")
        for vertices_item_data in _vertices:
            vertices_item = (
                CompanySearchBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType2VerticesItem.from_dict(
                    vertices_item_data
                )
            )

            vertices.append(vertices_item)

        company_search_body_search_params_headquarters_location_type_0_subtract_all_type_0_item_type_2 = cls(
            strategy=strategy,
            vertices=vertices,
        )

        company_search_body_search_params_headquarters_location_type_0_subtract_all_type_0_item_type_2.additional_properties = d
        return company_search_body_search_params_headquarters_location_type_0_subtract_all_type_0_item_type_2

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
