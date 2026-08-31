from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_tracker_signals_filter import ListTrackerSignalsFilter
from ...models.list_tracker_signals_response_200 import ListTrackerSignalsResponse200
from ...models.list_tracker_signals_response_400 import ListTrackerSignalsResponse400
from ...models.list_tracker_signals_response_401 import ListTrackerSignalsResponse401
from ...models.list_tracker_signals_response_402 import ListTrackerSignalsResponse402
from ...models.list_tracker_signals_response_403 import ListTrackerSignalsResponse403
from ...models.list_tracker_signals_response_404 import ListTrackerSignalsResponse404
from ...models.list_tracker_signals_response_422 import ListTrackerSignalsResponse422
from ...models.list_tracker_signals_response_429 import ListTrackerSignalsResponse429
from ...models.list_tracker_signals_response_500 import ListTrackerSignalsResponse500
from ...models.list_tracker_signals_response_503 import ListTrackerSignalsResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    list_id: str,
    *,
    api_key: str,
    since: None | str | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    page_size: int | Unset = 50,
    filter_: ListTrackerSignalsFilter | Unset = ListTrackerSignalsFilter.REAL,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["apiKey"] = api_key

    json_since: None | str | Unset
    if isinstance(since, Unset):
        json_since = UNSET
    else:
        json_since = since
    params["since"] = json_since

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    params["pageSize"] = page_size

    json_filter_: str | Unset = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_.value

    params["filter"] = json_filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tracker/signals/{list_id}".format(
            list_id=quote(str(list_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListTrackerSignalsResponse200
    | ListTrackerSignalsResponse400
    | ListTrackerSignalsResponse401
    | ListTrackerSignalsResponse402
    | ListTrackerSignalsResponse403
    | ListTrackerSignalsResponse404
    | ListTrackerSignalsResponse422
    | ListTrackerSignalsResponse429
    | ListTrackerSignalsResponse500
    | ListTrackerSignalsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ListTrackerSignalsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListTrackerSignalsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListTrackerSignalsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ListTrackerSignalsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ListTrackerSignalsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListTrackerSignalsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ListTrackerSignalsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ListTrackerSignalsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListTrackerSignalsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListTrackerSignalsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListTrackerSignalsResponse200
    | ListTrackerSignalsResponse400
    | ListTrackerSignalsResponse401
    | ListTrackerSignalsResponse402
    | ListTrackerSignalsResponse403
    | ListTrackerSignalsResponse404
    | ListTrackerSignalsResponse422
    | ListTrackerSignalsResponse429
    | ListTrackerSignalsResponse500
    | ListTrackerSignalsResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    since: None | str | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    page_size: int | Unset = 50,
    filter_: ListTrackerSignalsFilter | Unset = ListTrackerSignalsFilter.REAL,
) -> Response[
    ListTrackerSignalsResponse200
    | ListTrackerSignalsResponse400
    | ListTrackerSignalsResponse401
    | ListTrackerSignalsResponse402
    | ListTrackerSignalsResponse403
    | ListTrackerSignalsResponse404
    | ListTrackerSignalsResponse422
    | ListTrackerSignalsResponse429
    | ListTrackerSignalsResponse500
    | ListTrackerSignalsResponse503
]:
    """List signals

     Retrieve signals for a tracker list. Each signal represents a detected change that matched one of
    your tracking rules (e.g., a person changed jobs, a company raised funding). Use the `filter` query
    parameter to control which signals are returned: 'real' (default) for production signals only,
    'dummy' for test signals generated via the fire-dummy endpoint, or 'all' for both. Pass
    `filter=dummy` to validate your integration by consuming test signals through the same polling flow
    you use in production.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        since (None | str | Unset):
        cursor (None | str | Unset):
        page_size (int | Unset):  Default: 50.
        filter_ (ListTrackerSignalsFilter | Unset):  Default: ListTrackerSignalsFilter.REAL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTrackerSignalsResponse200 | ListTrackerSignalsResponse400 | ListTrackerSignalsResponse401 | ListTrackerSignalsResponse402 | ListTrackerSignalsResponse403 | ListTrackerSignalsResponse404 | ListTrackerSignalsResponse422 | ListTrackerSignalsResponse429 | ListTrackerSignalsResponse500 | ListTrackerSignalsResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        api_key=api_key,
        since=since,
        cursor=cursor,
        page_size=page_size,
        filter_=filter_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    since: None | str | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    page_size: int | Unset = 50,
    filter_: ListTrackerSignalsFilter | Unset = ListTrackerSignalsFilter.REAL,
) -> (
    ListTrackerSignalsResponse200
    | ListTrackerSignalsResponse400
    | ListTrackerSignalsResponse401
    | ListTrackerSignalsResponse402
    | ListTrackerSignalsResponse403
    | ListTrackerSignalsResponse404
    | ListTrackerSignalsResponse422
    | ListTrackerSignalsResponse429
    | ListTrackerSignalsResponse500
    | ListTrackerSignalsResponse503
    | None
):
    """List signals

     Retrieve signals for a tracker list. Each signal represents a detected change that matched one of
    your tracking rules (e.g., a person changed jobs, a company raised funding). Use the `filter` query
    parameter to control which signals are returned: 'real' (default) for production signals only,
    'dummy' for test signals generated via the fire-dummy endpoint, or 'all' for both. Pass
    `filter=dummy` to validate your integration by consuming test signals through the same polling flow
    you use in production.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        since (None | str | Unset):
        cursor (None | str | Unset):
        page_size (int | Unset):  Default: 50.
        filter_ (ListTrackerSignalsFilter | Unset):  Default: ListTrackerSignalsFilter.REAL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTrackerSignalsResponse200 | ListTrackerSignalsResponse400 | ListTrackerSignalsResponse401 | ListTrackerSignalsResponse402 | ListTrackerSignalsResponse403 | ListTrackerSignalsResponse404 | ListTrackerSignalsResponse422 | ListTrackerSignalsResponse429 | ListTrackerSignalsResponse500 | ListTrackerSignalsResponse503
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
        api_key=api_key,
        since=since,
        cursor=cursor,
        page_size=page_size,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    since: None | str | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    page_size: int | Unset = 50,
    filter_: ListTrackerSignalsFilter | Unset = ListTrackerSignalsFilter.REAL,
) -> Response[
    ListTrackerSignalsResponse200
    | ListTrackerSignalsResponse400
    | ListTrackerSignalsResponse401
    | ListTrackerSignalsResponse402
    | ListTrackerSignalsResponse403
    | ListTrackerSignalsResponse404
    | ListTrackerSignalsResponse422
    | ListTrackerSignalsResponse429
    | ListTrackerSignalsResponse500
    | ListTrackerSignalsResponse503
]:
    """List signals

     Retrieve signals for a tracker list. Each signal represents a detected change that matched one of
    your tracking rules (e.g., a person changed jobs, a company raised funding). Use the `filter` query
    parameter to control which signals are returned: 'real' (default) for production signals only,
    'dummy' for test signals generated via the fire-dummy endpoint, or 'all' for both. Pass
    `filter=dummy` to validate your integration by consuming test signals through the same polling flow
    you use in production.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        since (None | str | Unset):
        cursor (None | str | Unset):
        page_size (int | Unset):  Default: 50.
        filter_ (ListTrackerSignalsFilter | Unset):  Default: ListTrackerSignalsFilter.REAL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTrackerSignalsResponse200 | ListTrackerSignalsResponse400 | ListTrackerSignalsResponse401 | ListTrackerSignalsResponse402 | ListTrackerSignalsResponse403 | ListTrackerSignalsResponse404 | ListTrackerSignalsResponse422 | ListTrackerSignalsResponse429 | ListTrackerSignalsResponse500 | ListTrackerSignalsResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        api_key=api_key,
        since=since,
        cursor=cursor,
        page_size=page_size,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    since: None | str | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    page_size: int | Unset = 50,
    filter_: ListTrackerSignalsFilter | Unset = ListTrackerSignalsFilter.REAL,
) -> (
    ListTrackerSignalsResponse200
    | ListTrackerSignalsResponse400
    | ListTrackerSignalsResponse401
    | ListTrackerSignalsResponse402
    | ListTrackerSignalsResponse403
    | ListTrackerSignalsResponse404
    | ListTrackerSignalsResponse422
    | ListTrackerSignalsResponse429
    | ListTrackerSignalsResponse500
    | ListTrackerSignalsResponse503
    | None
):
    """List signals

     Retrieve signals for a tracker list. Each signal represents a detected change that matched one of
    your tracking rules (e.g., a person changed jobs, a company raised funding). Use the `filter` query
    parameter to control which signals are returned: 'real' (default) for production signals only,
    'dummy' for test signals generated via the fire-dummy endpoint, or 'all' for both. Pass
    `filter=dummy` to validate your integration by consuming test signals through the same polling flow
    you use in production.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        since (None | str | Unset):
        cursor (None | str | Unset):
        page_size (int | Unset):  Default: 50.
        filter_ (ListTrackerSignalsFilter | Unset):  Default: ListTrackerSignalsFilter.REAL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTrackerSignalsResponse200 | ListTrackerSignalsResponse400 | ListTrackerSignalsResponse401 | ListTrackerSignalsResponse402 | ListTrackerSignalsResponse403 | ListTrackerSignalsResponse404 | ListTrackerSignalsResponse422 | ListTrackerSignalsResponse429 | ListTrackerSignalsResponse500 | ListTrackerSignalsResponse503
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            api_key=api_key,
            since=since,
            cursor=cursor,
            page_size=page_size,
            filter_=filter_,
        )
    ).parsed
