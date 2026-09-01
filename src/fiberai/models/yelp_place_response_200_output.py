from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.yelp_place_response_200_output_place import YelpPlaceResponse200OutputPlace


T = TypeVar("T", bound="YelpPlaceResponse200Output")


@_attrs_define
class YelpPlaceResponse200Output:
    """
    Attributes:
        place (YelpPlaceResponse200OutputPlace): Detailed information about the Yelp business.
    """

    place: YelpPlaceResponse200OutputPlace
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        place = self.place.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "place": place,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.yelp_place_response_200_output_place import YelpPlaceResponse200OutputPlace  # noqa: PLC0415

        d = dict(src_dict)
        place = YelpPlaceResponse200OutputPlace.from_dict(d.pop("place"))

        yelp_place_response_200_output = cls(
            place=place,
        )

        yelp_place_response_200_output.additional_properties = d
        return yelp_place_response_200_output

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
