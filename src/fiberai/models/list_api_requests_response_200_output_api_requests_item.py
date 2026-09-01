from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListApiRequestsResponse200OutputApiRequestsItem")


@_attrs_define
class ListApiRequestsResponse200OutputApiRequestsItem:
    """
    Attributes:
        id (str): Unique id of this logged request. Quote it in support requests to identify a specific call.
        organization_id (str): Your organization's id.
        created_at (datetime.datetime): When the request was received, as an ISO 8601 timestamp.
        method (str): HTTP method, e.g. "POST".
        route_path (str): The route template that handled the request, e.g. "/v1/person/search"
        status_code (int): HTTP status code returned to you.
        duration_ms (int | None | Unset): How long the request took to process, in milliseconds, measured from receipt
            to just before the response was written.
        error_code (None | str | Unset): Correlation code included in the response body when a request fails. Quote it
            in support requests.
        request (Any | Unset): The input you sent with this call.
    """

    id: str
    organization_id: str
    created_at: datetime.datetime
    method: str
    route_path: str
    status_code: int
    duration_ms: int | None | Unset = UNSET
    error_code: None | str | Unset = UNSET
    request: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        organization_id = self.organization_id

        created_at = self.created_at.isoformat()

        method = self.method

        route_path = self.route_path

        status_code = self.status_code

        duration_ms: int | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        error_code: None | str | Unset
        if isinstance(self.error_code, Unset):
            error_code = UNSET
        else:
            error_code = self.error_code

        request = self.request

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "organizationId": organization_id,
                "createdAt": created_at,
                "method": method,
                "routePath": route_path,
                "statusCode": status_code,
            }
        )
        if duration_ms is not UNSET:
            field_dict["durationMs"] = duration_ms
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if request is not UNSET:
            field_dict["request"] = request

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        organization_id = d.pop("organizationId")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        method = d.pop("method")

        route_path = d.pop("routePath")

        status_code = d.pop("statusCode")

        def _parse_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("durationMs", UNSET))

        def _parse_error_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_code = _parse_error_code(d.pop("errorCode", UNSET))

        request = d.pop("request", UNSET)

        list_api_requests_response_200_output_api_requests_item = cls(
            id=id,
            organization_id=organization_id,
            created_at=created_at,
            method=method,
            route_path=route_path,
            status_code=status_code,
            duration_ms=duration_ms,
            error_code=error_code,
            request=request,
        )

        list_api_requests_response_200_output_api_requests_item.additional_properties = d
        return list_api_requests_response_200_output_api_requests_item

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
