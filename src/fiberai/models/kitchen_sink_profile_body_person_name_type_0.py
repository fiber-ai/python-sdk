from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KitchenSinkProfileBodyPersonNameType0")


@_attrs_define
class KitchenSinkProfileBodyPersonNameType0:
    """
    Attributes:
        value (None | str | Unset):
        loose_match (bool | Unset):  Default: False.
    """

    value: None | str | Unset = UNSET
    loose_match: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        loose_match = self.loose_match

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if loose_match is not UNSET:
            field_dict["looseMatch"] = loose_match

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        loose_match = d.pop("looseMatch", UNSET)

        kitchen_sink_profile_body_person_name_type_0 = cls(
            value=value,
            loose_match=loose_match,
        )

        kitchen_sink_profile_body_person_name_type_0.additional_properties = d
        return kitchen_sink_profile_body_person_name_type_0

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
