from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hotel_property_response_200_output_property import HotelPropertyResponse200OutputProperty


T = TypeVar("T", bound="HotelPropertyResponse200Output")


@_attrs_define
class HotelPropertyResponse200Output:
    """
    Attributes:
        property_ (HotelPropertyResponse200OutputProperty): Full property details including offers and amenities.
        currency_code (None | str | Unset): ISO 4217 currency code for prices in this response (e.g. 'USD', 'EUR',
            'GBP').
    """

    property_: HotelPropertyResponse200OutputProperty
    currency_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        property_ = self.property_.to_dict()

        currency_code: None | str | Unset
        if isinstance(self.currency_code, Unset):
            currency_code = UNSET
        else:
            currency_code = self.currency_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "property": property_,
            }
        )
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hotel_property_response_200_output_property import HotelPropertyResponse200OutputProperty

        d = dict(src_dict)
        property_ = HotelPropertyResponse200OutputProperty.from_dict(d.pop("property"))

        def _parse_currency_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_code = _parse_currency_code(d.pop("currencyCode", UNSET))

        hotel_property_response_200_output = cls(
            property_=property_,
            currency_code=currency_code,
        )

        hotel_property_response_200_output.additional_properties = d
        return hotel_property_response_200_output

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
