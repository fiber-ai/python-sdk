from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="YelpPlaceResponse200OutputPlaceServicesItem")


@_attrs_define
class YelpPlaceResponse200OutputPlaceServicesItem:
    """
    Attributes:
        name (str): Service or feature name (e.g. 'Takes reservations').
        is_active (bool): True when the business currently offers this service.
    """

    name: str
    is_active: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "isActive": is_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        is_active = d.pop("isActive")

        yelp_place_response_200_output_place_services_item = cls(
            name=name,
            is_active=is_active,
        )

        yelp_place_response_200_output_place_services_item.additional_properties = d
        return yelp_place_response_200_output_place_services_item

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
