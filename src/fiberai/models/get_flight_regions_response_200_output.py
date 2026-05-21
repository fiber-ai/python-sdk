from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_flight_regions_response_200_output_regions_item import (
        GetFlightRegionsResponse200OutputRegionsItem,
    )


T = TypeVar("T", bound="GetFlightRegionsResponse200Output")


@_attrs_define
class GetFlightRegionsResponse200Output:
    """
    Attributes:
        regions (list[GetFlightRegionsResponse200OutputRegionsItem]): All supported flight region aliases.
    """

    regions: list[GetFlightRegionsResponse200OutputRegionsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        regions = []
        for regions_item_data in self.regions:
            regions_item = regions_item_data.to_dict()
            regions.append(regions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "regions": regions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_flight_regions_response_200_output_regions_item import (
            GetFlightRegionsResponse200OutputRegionsItem,
        )

        d = dict(src_dict)
        regions = []
        _regions = d.pop("regions")
        for regions_item_data in _regions:
            regions_item = GetFlightRegionsResponse200OutputRegionsItem.from_dict(regions_item_data)

            regions.append(regions_item)

        get_flight_regions_response_200_output = cls(
            regions=regions,
        )

        get_flight_regions_response_200_output.additional_properties = d
        return get_flight_regions_response_200_output

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
