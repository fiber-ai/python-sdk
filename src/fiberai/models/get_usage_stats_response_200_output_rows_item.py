from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_usage_stats_response_200_output_rows_item_api_key_info_type_0 import (
        GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0,
    )


T = TypeVar("T", bound="GetUsageStatsResponse200OutputRowsItem")


@_attrs_define
class GetUsageStatsResponse200OutputRowsItem:
    """
    Attributes:
        credits_charged (float): Credits charged to your balance by the calls in this bucket.
        credits_refunded (float): Credits refunded back to your balance within this bucket.
        request_count (int): Number of distinct API calls recorded in this bucket.
        bucket_start (None | str | Unset): Start of the time bucket (ISO 8601, UTC). Null when granularity is 'all',
            which returns a single unbucketed row.
        api_key_info (GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0 | None | Unset): The API key the usage in
            this row is attributed to. Null when the usage is not attributable to a single API key: unattributed dashboard
            and background usage, or an org-wide `groupBy: "total"` row without an `apiKeyHash` filter. Inside the object,
            `hash` is always present; `name`, `prefix`, and `mode` are null when the key has since been deleted.
    """

    credits_charged: float
    credits_refunded: float
    request_count: int
    bucket_start: None | str | Unset = UNSET
    api_key_info: GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_usage_stats_response_200_output_rows_item_api_key_info_type_0 import (
            GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0,  # noqa: PLC0415
        )

        credits_charged = self.credits_charged

        credits_refunded = self.credits_refunded

        request_count = self.request_count

        bucket_start: None | str | Unset
        if isinstance(self.bucket_start, Unset):
            bucket_start = UNSET
        else:
            bucket_start = self.bucket_start

        api_key_info: dict[str, Any] | None | Unset
        if isinstance(self.api_key_info, Unset):
            api_key_info = UNSET
        elif isinstance(self.api_key_info, GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0):
            api_key_info = self.api_key_info.to_dict()
        else:
            api_key_info = self.api_key_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creditsCharged": credits_charged,
                "creditsRefunded": credits_refunded,
                "requestCount": request_count,
            }
        )
        if bucket_start is not UNSET:
            field_dict["bucketStart"] = bucket_start
        if api_key_info is not UNSET:
            field_dict["apiKeyInfo"] = api_key_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_usage_stats_response_200_output_rows_item_api_key_info_type_0 import (
            GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        credits_charged = d.pop("creditsCharged")

        credits_refunded = d.pop("creditsRefunded")

        request_count = d.pop("requestCount")

        def _parse_bucket_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bucket_start = _parse_bucket_start(d.pop("bucketStart", UNSET))

        def _parse_api_key_info(data: object) -> GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                api_key_info_type_0 = GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0.from_dict(data)

                return api_key_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0 | None | Unset, data)

        api_key_info = _parse_api_key_info(d.pop("apiKeyInfo", UNSET))

        get_usage_stats_response_200_output_rows_item = cls(
            credits_charged=credits_charged,
            credits_refunded=credits_refunded,
            request_count=request_count,
            bucket_start=bucket_start,
            api_key_info=api_key_info,
        )

        get_usage_stats_response_200_output_rows_item.additional_properties = d
        return get_usage_stats_response_200_output_rows_item

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
