from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.location_typeahead_response_200_output_data_item import LocationTypeaheadResponse200OutputDataItem
    from ..models.location_typeahead_response_200_output_preset_regions_item_type_0 import (
        LocationTypeaheadResponse200OutputPresetRegionsItemType0,
    )
    from ..models.location_typeahead_response_200_output_preset_regions_item_type_1 import (
        LocationTypeaheadResponse200OutputPresetRegionsItemType1,
    )


T = TypeVar("T", bound="LocationTypeaheadResponse200Output")


@_attrs_define
class LocationTypeaheadResponse200Output:
    """
    Attributes:
        data (list[LocationTypeaheadResponse200OutputDataItem]):
        preset_regions (list[LocationTypeaheadResponse200OutputPresetRegionsItemType0 |
            LocationTypeaheadResponse200OutputPresetRegionsItemType1]): Preset metro area regions matching the query. Each
            includes a slug usable with the preset-region strategy in location-based search endpoints, plus geometry and
            major cities for display.
    """

    data: list[LocationTypeaheadResponse200OutputDataItem]
    preset_regions: list[
        LocationTypeaheadResponse200OutputPresetRegionsItemType0
        | LocationTypeaheadResponse200OutputPresetRegionsItemType1
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.location_typeahead_response_200_output_preset_regions_item_type_0 import (
            LocationTypeaheadResponse200OutputPresetRegionsItemType0,
        )

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        preset_regions = []
        for preset_regions_item_data in self.preset_regions:
            preset_regions_item: dict[str, Any]
            if isinstance(preset_regions_item_data, LocationTypeaheadResponse200OutputPresetRegionsItemType0):
                preset_regions_item = preset_regions_item_data.to_dict()
            else:
                preset_regions_item = preset_regions_item_data.to_dict()

            preset_regions.append(preset_regions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "presetRegions": preset_regions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_typeahead_response_200_output_data_item import LocationTypeaheadResponse200OutputDataItem
        from ..models.location_typeahead_response_200_output_preset_regions_item_type_0 import (
            LocationTypeaheadResponse200OutputPresetRegionsItemType0,
        )
        from ..models.location_typeahead_response_200_output_preset_regions_item_type_1 import (
            LocationTypeaheadResponse200OutputPresetRegionsItemType1,
        )

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = LocationTypeaheadResponse200OutputDataItem.from_dict(data_item_data)

            data.append(data_item)

        preset_regions = []
        _preset_regions = d.pop("presetRegions")
        for preset_regions_item_data in _preset_regions:

            def _parse_preset_regions_item(
                data: object,
            ) -> (
                LocationTypeaheadResponse200OutputPresetRegionsItemType0
                | LocationTypeaheadResponse200OutputPresetRegionsItemType1
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    preset_regions_item_type_0 = LocationTypeaheadResponse200OutputPresetRegionsItemType0.from_dict(
                        data
                    )

                    return preset_regions_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                preset_regions_item_type_1 = LocationTypeaheadResponse200OutputPresetRegionsItemType1.from_dict(data)

                return preset_regions_item_type_1

            preset_regions_item = _parse_preset_regions_item(preset_regions_item_data)

            preset_regions.append(preset_regions_item)

        location_typeahead_response_200_output = cls(
            data=data,
            preset_regions=preset_regions,
        )

        location_typeahead_response_200_output.additional_properties = d
        return location_typeahead_response_200_output

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
