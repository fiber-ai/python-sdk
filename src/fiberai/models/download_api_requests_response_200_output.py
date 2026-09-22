from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.download_api_requests_response_200_output_api_requests_item import (
        DownloadApiRequestsResponse200OutputApiRequestsItem,
    )


T = TypeVar("T", bound="DownloadApiRequestsResponse200Output")


@_attrs_define
class DownloadApiRequestsResponse200Output:
    """
    Attributes:
        api_requests (list[DownloadApiRequestsResponse200OutputApiRequestsItem]): Your past API requests, newest first.
        truncated (bool): True when more than 5000 matching requests exist. Narrow `from`/`to` and retry.
        retention_days (int): How many days of request history are retained. Requests older than this have been purged
            and cannot be returned.
    """

    api_requests: list[DownloadApiRequestsResponse200OutputApiRequestsItem]
    truncated: bool
    retention_days: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_requests = []
        for api_requests_item_data in self.api_requests:
            api_requests_item = api_requests_item_data.to_dict()
            api_requests.append(api_requests_item)

        truncated = self.truncated

        retention_days = self.retention_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiRequests": api_requests,
                "truncated": truncated,
                "retentionDays": retention_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.download_api_requests_response_200_output_api_requests_item import (
            DownloadApiRequestsResponse200OutputApiRequestsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        api_requests = []
        _api_requests = d.pop("apiRequests")
        for api_requests_item_data in _api_requests:
            api_requests_item = DownloadApiRequestsResponse200OutputApiRequestsItem.from_dict(api_requests_item_data)

            api_requests.append(api_requests_item)

        truncated = d.pop("truncated")

        retention_days = d.pop("retentionDays")

        download_api_requests_response_200_output = cls(
            api_requests=api_requests,
            truncated=truncated,
            retention_days=retention_days,
        )

        download_api_requests_response_200_output.additional_properties = d
        return download_api_requests_response_200_output

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
