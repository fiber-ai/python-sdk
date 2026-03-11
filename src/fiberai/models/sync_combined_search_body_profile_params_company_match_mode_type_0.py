from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_combined_search_body_profile_params_company_match_mode_type_0_mode import (
    SyncCombinedSearchBodyProfileParamsCompanyMatchModeType0Mode,
)

T = TypeVar("T", bound="SyncCombinedSearchBodyProfileParamsCompanyMatchModeType0")


@_attrs_define
class SyncCombinedSearchBodyProfileParamsCompanyMatchModeType0:
    """
    Attributes:
        mode (SyncCombinedSearchBodyProfileParamsCompanyMatchModeType0Mode):
    """

    mode: SyncCombinedSearchBodyProfileParamsCompanyMatchModeType0Mode
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = SyncCombinedSearchBodyProfileParamsCompanyMatchModeType0Mode(d.pop("mode"))

        sync_combined_search_body_profile_params_company_match_mode_type_0 = cls(
            mode=mode,
        )

        sync_combined_search_body_profile_params_company_match_mode_type_0.additional_properties = d
        return sync_combined_search_body_profile_params_company_match_mode_type_0

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
