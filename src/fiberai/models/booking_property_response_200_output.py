from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.booking_property_response_200_output_property import BookingPropertyResponse200OutputProperty


T = TypeVar("T", bound="BookingPropertyResponse200Output")


@_attrs_define
class BookingPropertyResponse200Output:
    """
    Attributes:
        property_ (BookingPropertyResponse200OutputProperty): Full property details including amenities, photos, and
            house rules.
    """

    property_: BookingPropertyResponse200OutputProperty
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        property_ = self.property_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "property": property_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_property_response_200_output_property import BookingPropertyResponse200OutputProperty  # noqa: PLC0415

        d = dict(src_dict)
        property_ = BookingPropertyResponse200OutputProperty.from_dict(d.pop("property"))

        booking_property_response_200_output = cls(
            property_=property_,
        )

        booking_property_response_200_output.additional_properties = d
        return booking_property_response_200_output

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
