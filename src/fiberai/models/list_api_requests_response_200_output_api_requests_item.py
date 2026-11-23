from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_api_requests_response_200_output_api_requests_item_api_key_info_type_0 import (
        ListApiRequestsResponse200OutputApiRequestsItemApiKeyInfoType0,
    )


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
        group_call_id (None | str | Unset): Identifier that ties this request to its billing records — every charge and
            refund recorded for this call carries it. Quote it when reconciling your credit balance against individual
            requests. Null when the call never went through billing (free endpoints, or calls rejected before billing ran).
        credits_charged (float | None | Unset): Credits this request charged, in credits. Null when no billing record
            exists for the call (see `groupCallId`).
        credits_refunded (float | None | Unset): Credits refunded for this request, in credits, when a refund was issued
            against it. Null when no refund was recorded.
        api_key_info (ListApiRequestsResponse200OutputApiRequestsItemApiKeyInfoType0 | None | Unset): The API key that
            made this request. Null only when the request was rejected before authentication completed, so no key was
            involved. Inside the object, `hash` is always present; `name`, `prefix`, and `mode` are null when the key has
            since been deleted.
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
    group_call_id: None | str | Unset = UNSET
    credits_charged: float | None | Unset = UNSET
    credits_refunded: float | None | Unset = UNSET
    api_key_info: ListApiRequestsResponse200OutputApiRequestsItemApiKeyInfoType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_api_requests_response_200_output_api_requests_item_api_key_info_type_0 import (
            ListApiRequestsResponse200OutputApiRequestsItemApiKeyInfoType0,  # noqa: PLC0415
        )

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

        group_call_id: None | str | Unset
        if isinstance(self.group_call_id, Unset):
            group_call_id = UNSET
        else:
            group_call_id = self.group_call_id

        credits_charged: float | None | Unset
        if isinstance(self.credits_charged, Unset):
            credits_charged = UNSET
        else:
            credits_charged = self.credits_charged

        credits_refunded: float | None | Unset
        if isinstance(self.credits_refunded, Unset):
            credits_refunded = UNSET
        else:
            credits_refunded = self.credits_refunded

        api_key_info: dict[str, Any] | None | Unset
        if isinstance(self.api_key_info, Unset):
            api_key_info = UNSET
        elif isinstance(self.api_key_info, ListApiRequestsResponse200OutputApiRequestsItemApiKeyInfoType0):
            api_key_info = self.api_key_info.to_dict()
        else:
            api_key_info = self.api_key_info

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
        if group_call_id is not UNSET:
            field_dict["groupCallId"] = group_call_id
        if credits_charged is not UNSET:
            field_dict["creditsCharged"] = credits_charged
        if credits_refunded is not UNSET:
            field_dict["creditsRefunded"] = credits_refunded
        if api_key_info is not UNSET:
            field_dict["apiKeyInfo"] = api_key_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_api_requests_response_200_output_api_requests_item_api_key_info_type_0 import (
            ListApiRequestsResponse200OutputApiRequestsItemApiKeyInfoType0,  # noqa: PLC0415
        )

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

        def _parse_group_call_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_call_id = _parse_group_call_id(d.pop("groupCallId", UNSET))

        def _parse_credits_charged(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        credits_charged = _parse_credits_charged(d.pop("creditsCharged", UNSET))

        def _parse_credits_refunded(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        credits_refunded = _parse_credits_refunded(d.pop("creditsRefunded", UNSET))

        def _parse_api_key_info(
            data: object,
        ) -> ListApiRequestsResponse200OutputApiRequestsItemApiKeyInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                api_key_info_type_0 = ListApiRequestsResponse200OutputApiRequestsItemApiKeyInfoType0.from_dict(data)

                return api_key_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListApiRequestsResponse200OutputApiRequestsItemApiKeyInfoType0 | None | Unset, data)

        api_key_info = _parse_api_key_info(d.pop("apiKeyInfo", UNSET))

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
            group_call_id=group_call_id,
            credits_charged=credits_charged,
            credits_refunded=credits_refunded,
            api_key_info=api_key_info,
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
