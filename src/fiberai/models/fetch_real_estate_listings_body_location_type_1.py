from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fetch_real_estate_listings_body_location_type_1_type import FetchRealEstateListingsBodyLocationType1Type

T = TypeVar("T", bound="FetchRealEstateListingsBodyLocationType1")


@_attrs_define
class FetchRealEstateListingsBodyLocationType1:
    """
    Attributes:
        type_ (FetchRealEstateListingsBodyLocationType1Type):
        city (str): City name (e.g., 'Toronto', 'Trois-Rivières').
        state_code (str): Two-letter US state code or Canadian province code (e.g., 'NY', 'CA', 'QC', 'ON').
    """

    type_: FetchRealEstateListingsBodyLocationType1Type
    city: str
    state_code: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        city = self.city

        state_code = self.state_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "city": city,
                "stateCode": state_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = FetchRealEstateListingsBodyLocationType1Type(d.pop("type"))

        city = d.pop("city")

        state_code = d.pop("stateCode")

        fetch_real_estate_listings_body_location_type_1 = cls(
            type_=type_,
            city=city,
            state_code=state_code,
        )

        fetch_real_estate_listings_body_location_type_1.additional_properties = d
        return fetch_real_estate_listings_body_location_type_1

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
