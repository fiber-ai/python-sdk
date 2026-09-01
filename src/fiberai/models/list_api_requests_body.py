from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListApiRequestsBody")


@_attrs_define
class ListApiRequestsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        from_ (datetime.datetime | None | Unset): Only return requests received at or after this ISO 8601 timestamp.
            Logs are retained for 7 days, so earlier timestamps simply return nothing.
        to (datetime.datetime | None | Unset): Only return requests received strictly before this ISO 8601 timestamp.
        route_path (None | str | Unset): Only return requests to this exact route template, e.g. "/v1/person/search".
        method (None | str | Unset): Only return requests using this HTTP method, e.g. "POST".
        status_code (int | None | Unset): Only return requests that returned this exact status code.
        error_code (None | str | Unset): Only return the request carrying this error correlation code.
        cursor (None | str | Unset): The cursor from where to start fetching the next page of results. Provide the
            `nextCursor` from the previous response to continue from there. Keep the same filters as the call that produced
            the cursor — reusing a cursor while changing filters silently skips rows.
        page_size (int | Unset): The number of results to fetch per page. Default: 25.
    """

    api_key: str
    from_: datetime.datetime | None | Unset = UNSET
    to: datetime.datetime | None | Unset = UNSET
    route_path: None | str | Unset = UNSET
    method: None | str | Unset = UNSET
    status_code: int | None | Unset = UNSET
    error_code: None | str | Unset = UNSET
    cursor: None | str | Unset = UNSET
    page_size: int | Unset = 25
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        from_: None | str | Unset
        if isinstance(self.from_, Unset):
            from_ = UNSET
        elif isinstance(self.from_, datetime.datetime):
            from_ = self.from_.isoformat()
        else:
            from_ = self.from_

        to: None | str | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        elif isinstance(self.to, datetime.datetime):
            to = self.to.isoformat()
        else:
            to = self.to

        route_path: None | str | Unset
        if isinstance(self.route_path, Unset):
            route_path = UNSET
        else:
            route_path = self.route_path

        method: None | str | Unset
        if isinstance(self.method, Unset):
            method = UNSET
        else:
            method = self.method

        status_code: int | None | Unset
        if isinstance(self.status_code, Unset):
            status_code = UNSET
        else:
            status_code = self.status_code

        error_code: None | str | Unset
        if isinstance(self.error_code, Unset):
            error_code = UNSET
        else:
            error_code = self.error_code

        cursor: None | str | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
            }
        )
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if route_path is not UNSET:
            field_dict["routePath"] = route_path
        if method is not UNSET:
            field_dict["method"] = method
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_from_(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_type_0 = datetime.datetime.fromisoformat(data)

                return from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        from_ = _parse_from_(d.pop("from", UNSET))

        def _parse_to(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                to_type_0 = datetime.datetime.fromisoformat(data)

                return to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        to = _parse_to(d.pop("to", UNSET))

        def _parse_route_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        route_path = _parse_route_path(d.pop("routePath", UNSET))

        def _parse_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        method = _parse_method(d.pop("method", UNSET))

        def _parse_status_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        status_code = _parse_status_code(d.pop("statusCode", UNSET))

        def _parse_error_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_code = _parse_error_code(d.pop("errorCode", UNSET))

        def _parse_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        page_size = d.pop("pageSize", UNSET)

        list_api_requests_body = cls(
            api_key=api_key,
            from_=from_,
            to=to,
            route_path=route_path,
            method=method,
            status_code=status_code,
            error_code=error_code,
            cursor=cursor,
            page_size=page_size,
        )

        list_api_requests_body.additional_properties = d
        return list_api_requests_body

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
