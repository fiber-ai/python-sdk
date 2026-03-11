from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KitchenSinkProfileBodyProfileLocationType0")


@_attrs_define
class KitchenSinkProfileBodyProfileLocationType0:
    """
    Attributes:
        country_code (None | str | Unset):
        state_name (None | str | Unset):
        locality (None | str | Unset):
    """

    country_code: None | str | Unset = UNSET
    state_name: None | str | Unset = UNSET
    locality: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        state_name: None | str | Unset
        if isinstance(self.state_name, Unset):
            state_name = UNSET
        else:
            state_name = self.state_name

        locality: None | str | Unset
        if isinstance(self.locality, Unset):
            locality = UNSET
        else:
            locality = self.locality

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if state_name is not UNSET:
            field_dict["stateName"] = state_name
        if locality is not UNSET:
            field_dict["locality"] = locality

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        def _parse_state_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state_name = _parse_state_name(d.pop("stateName", UNSET))

        def _parse_locality(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locality = _parse_locality(d.pop("locality", UNSET))

        kitchen_sink_profile_body_profile_location_type_0 = cls(
            country_code=country_code,
            state_name=state_name,
            locality=locality,
        )

        kitchen_sink_profile_body_profile_location_type_0.additional_properties = d
        return kitchen_sink_profile_body_profile_location_type_0

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
