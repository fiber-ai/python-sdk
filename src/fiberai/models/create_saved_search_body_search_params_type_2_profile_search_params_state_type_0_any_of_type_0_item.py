from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStateType0AnyOfType0Item")


@_attrs_define
class CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStateType0AnyOfType0Item:
    """
    Attributes:
        state_name (str):
        country_code (None | str | Unset):
    """

    state_name: str
    country_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state_name = self.state_name

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stateName": state_name,
            }
        )
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state_name = d.pop("stateName")

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        create_saved_search_body_search_params_type_2_profile_search_params_state_type_0_any_of_type_0_item = cls(
            state_name=state_name,
            country_code=country_code,
        )

        create_saved_search_body_search_params_type_2_profile_search_params_state_type_0_any_of_type_0_item.additional_properties = d
        return create_saved_search_body_search_params_type_2_profile_search_params_state_type_0_any_of_type_0_item

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
