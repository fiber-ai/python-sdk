from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_metro_areas_response_200_output_metro_areas_item_type_0 import (
        GetMetroAreasResponse200OutputMetroAreasItemType0,
    )
    from ..models.get_metro_areas_response_200_output_metro_areas_item_type_1 import (
        GetMetroAreasResponse200OutputMetroAreasItemType1,
    )


T = TypeVar("T", bound="GetMetroAreasResponse200Output")


@_attrs_define
class GetMetroAreasResponse200Output:
    """
    Attributes:
        metro_areas (list[GetMetroAreasResponse200OutputMetroAreasItemType0 |
            GetMetroAreasResponse200OutputMetroAreasItemType1]): All available preset metro area regions. Use the slug with
            the preset-region strategy in location-based search endpoints.
    """

    metro_areas: list[
        GetMetroAreasResponse200OutputMetroAreasItemType0 | GetMetroAreasResponse200OutputMetroAreasItemType1
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_metro_areas_response_200_output_metro_areas_item_type_0 import (
            GetMetroAreasResponse200OutputMetroAreasItemType0,  # noqa: PLC0415
        )

        metro_areas = []
        for metro_areas_item_data in self.metro_areas:
            metro_areas_item: dict[str, Any]
            if isinstance(metro_areas_item_data, GetMetroAreasResponse200OutputMetroAreasItemType0):
                metro_areas_item = metro_areas_item_data.to_dict()
            else:
                metro_areas_item = metro_areas_item_data.to_dict()

            metro_areas.append(metro_areas_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metroAreas": metro_areas,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_metro_areas_response_200_output_metro_areas_item_type_0 import (
            GetMetroAreasResponse200OutputMetroAreasItemType0,  # noqa: PLC0415
        )
        from ..models.get_metro_areas_response_200_output_metro_areas_item_type_1 import (
            GetMetroAreasResponse200OutputMetroAreasItemType1,  # noqa: PLC0415
        )

        d = dict(src_dict)
        metro_areas = []
        _metro_areas = d.pop("metroAreas")
        for metro_areas_item_data in _metro_areas:

            def _parse_metro_areas_item(
                data: object,
            ) -> GetMetroAreasResponse200OutputMetroAreasItemType0 | GetMetroAreasResponse200OutputMetroAreasItemType1:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    metro_areas_item_type_0 = GetMetroAreasResponse200OutputMetroAreasItemType0.from_dict(data)

                    return metro_areas_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                metro_areas_item_type_1 = GetMetroAreasResponse200OutputMetroAreasItemType1.from_dict(data)

                return metro_areas_item_type_1

            metro_areas_item = _parse_metro_areas_item(metro_areas_item_data)

            metro_areas.append(metro_areas_item)

        get_metro_areas_response_200_output = cls(
            metro_areas=metro_areas,
        )

        get_metro_areas_response_200_output.additional_properties = d
        return get_metro_areas_response_200_output

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
