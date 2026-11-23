from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_usage_stats_response_200_output_rows_item_api_key_info_type_0_mode_type_1 import (
    GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType1,
)
from ..models.get_usage_stats_response_200_output_rows_item_api_key_info_type_0_mode_type_2_type_1 import (
    GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType2Type1,
)
from ..models.get_usage_stats_response_200_output_rows_item_api_key_info_type_0_mode_type_3_type_1 import (
    GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0")


@_attrs_define
class GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0:
    """The API key the usage in this row is attributed to. Null when the usage is not attributable to a single API key:
    unattributed dashboard and background usage, or an org-wide `groupBy: "total"` row without an `apiKeyHash` filter.
    Inside the object, `hash` is always present; `name`, `prefix`, and `mode` are null when the key has since been
    deleted.

        Attributes:
            hash_ (str): SHA-256 hash of the API key. Unlike the other fields here, the hash is always present — it is
                recorded when the key is used, so it survives even if the key has since been deleted. Use it as the stable
                identifier when attributing activity to keys, and as the `apiKeyHash` filter value on endpoints that accept one.
            name (None | str | Unset): Name of the API key, as shown on your API keys page. Null when the key has since been
                deleted: the name is looked up from your current key list, and a deleted key is no longer on it — `hash` is the
                only field that still identifies it.
            prefix (None | str | Unset): Non-secret prefix of the API key, for recognizing it at a glance. Null when the key
                has since been deleted, for the same reason as `name`.
            mode (GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType1 |
                GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType2Type1 |
                GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType3Type1 | None | Unset): Whether the key was a live
                or sandbox (`sk_test_...`) key. Null when the key has since been deleted, for the same reason as `name`.
    """

    hash_: str
    name: None | str | Unset = UNSET
    prefix: None | str | Unset = UNSET
    mode: (
        GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType1
        | GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType2Type1
        | GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType3Type1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hash_ = self.hash_

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        prefix: None | str | Unset
        if isinstance(self.prefix, Unset):
            prefix = UNSET
        else:
            prefix = self.prefix

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType1):
            mode = self.mode.value
        elif isinstance(self.mode, GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType2Type1):
            mode = self.mode.value
        elif isinstance(self.mode, GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType3Type1):
            mode = self.mode.value
        else:
            mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hash": hash_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hash_ = d.pop("hash")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prefix = _parse_prefix(d.pop("prefix", UNSET))

        def _parse_mode(
            data: object,
        ) -> (
            GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType1
            | GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType2Type1
            | GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_1 = GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType1(data)

                return mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_2_type_1 = GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType2Type1(data)

                return mode_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_3_type_1 = GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType3Type1(data)

                return mode_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType1
                | GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType2Type1
                | GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType3Type1
                | None
                | Unset,
                data,
            )

        mode = _parse_mode(d.pop("mode", UNSET))

        get_usage_stats_response_200_output_rows_item_api_key_info_type_0 = cls(
            hash_=hash_,
            name=name,
            prefix=prefix,
            mode=mode,
        )

        get_usage_stats_response_200_output_rows_item_api_key_info_type_0.additional_properties = d
        return get_usage_stats_response_200_output_rows_item_api_key_info_type_0

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
