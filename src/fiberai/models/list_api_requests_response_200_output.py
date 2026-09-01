from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_api_requests_response_200_output_api_requests_item import (
        ListApiRequestsResponse200OutputApiRequestsItem,
    )


T = TypeVar("T", bound="ListApiRequestsResponse200Output")


@_attrs_define
class ListApiRequestsResponse200Output:
    """
    Attributes:
        api_requests (list[ListApiRequestsResponse200OutputApiRequestsItem]): Your past API requests, newest first.
        has_more (bool): Whether there are more results to fetch.
        retention_days (int): How many days of request history are retained. Requests older than this have been purged
            and cannot be returned.
        next_cursor (None | str | Unset): The pagination cursor for the next page of results. Null if there are no more
            results.
    """

    api_requests: list[ListApiRequestsResponse200OutputApiRequestsItem]
    has_more: bool
    retention_days: int
    next_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_requests = []
        for api_requests_item_data in self.api_requests:
            api_requests_item = api_requests_item_data.to_dict()
            api_requests.append(api_requests_item)

        has_more = self.has_more

        retention_days = self.retention_days

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiRequests": api_requests,
                "hasMore": has_more,
                "retentionDays": retention_days,
            }
        )
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_api_requests_response_200_output_api_requests_item import (
            ListApiRequestsResponse200OutputApiRequestsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        api_requests = []
        _api_requests = d.pop("apiRequests")
        for api_requests_item_data in _api_requests:
            api_requests_item = ListApiRequestsResponse200OutputApiRequestsItem.from_dict(api_requests_item_data)

            api_requests.append(api_requests_item)

        has_more = d.pop("hasMore")

        retention_days = d.pop("retentionDays")

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        list_api_requests_response_200_output = cls(
            api_requests=api_requests,
            has_more=has_more,
            retention_days=retention_days,
            next_cursor=next_cursor,
        )

        list_api_requests_response_200_output.additional_properties = d
        return list_api_requests_response_200_output

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
