from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KitchenSinkBulkProfileResponse200OutputDataItemItemLanguagesType0Item")


@_attrs_define
class KitchenSinkBulkProfileResponse200OutputDataItemItemLanguagesType0Item:
    """
    Attributes:
        name (None | str | Unset):
        proficiency_id (None | str | Unset):
        proficiency_name (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    proficiency_id: None | str | Unset = UNSET
    proficiency_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        proficiency_id: None | str | Unset
        if isinstance(self.proficiency_id, Unset):
            proficiency_id = UNSET
        else:
            proficiency_id = self.proficiency_id

        proficiency_name: None | str | Unset
        if isinstance(self.proficiency_name, Unset):
            proficiency_name = UNSET
        else:
            proficiency_name = self.proficiency_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if proficiency_id is not UNSET:
            field_dict["proficiency_id"] = proficiency_id
        if proficiency_name is not UNSET:
            field_dict["proficiency_name"] = proficiency_name

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

        def _parse_proficiency_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proficiency_id = _parse_proficiency_id(d.pop("proficiency_id", UNSET))

        def _parse_proficiency_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proficiency_name = _parse_proficiency_name(d.pop("proficiency_name", UNSET))

        kitchen_sink_bulk_profile_response_200_output_data_item_item_languages_type_0_item = cls(
            name=name,
            proficiency_id=proficiency_id,
            proficiency_name=proficiency_name,
        )

        kitchen_sink_bulk_profile_response_200_output_data_item_item_languages_type_0_item.additional_properties = d
        return kitchen_sink_bulk_profile_response_200_output_data_item_item_languages_type_0_item

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
