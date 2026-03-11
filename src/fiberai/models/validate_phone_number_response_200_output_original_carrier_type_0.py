from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidatePhoneNumberResponse200OutputOriginalCarrierType0")


@_attrs_define
class ValidatePhoneNumberResponse200OutputOriginalCarrierType0:
    """Information about the original carrier that issued the number

    Attributes:
        name (None | str | Unset):
        network_type (None | str | Unset):
        country (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    network_type: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        network_type: None | str | Unset
        if isinstance(self.network_type, Unset):
            network_type = UNSET
        else:
            network_type = self.network_type

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if network_type is not UNSET:
            field_dict["networkType"] = network_type
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_network_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        network_type = _parse_network_type(d.pop("networkType", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        validate_phone_number_response_200_output_original_carrier_type_0 = cls(
            name=name,
            network_type=network_type,
            country=country,
        )

        validate_phone_number_response_200_output_original_carrier_type_0.additional_properties = d
        return validate_phone_number_response_200_output_original_carrier_type_0

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
