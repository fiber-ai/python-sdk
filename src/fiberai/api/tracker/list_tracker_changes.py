import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_tracker_changes_response_200 import ListTrackerChangesResponse200
from ...models.list_tracker_changes_response_400 import ListTrackerChangesResponse400
from ...models.list_tracker_changes_response_401 import ListTrackerChangesResponse401
from ...models.list_tracker_changes_response_402 import ListTrackerChangesResponse402
from ...models.list_tracker_changes_response_403 import ListTrackerChangesResponse403
from ...models.list_tracker_changes_response_404 import ListTrackerChangesResponse404
from ...models.list_tracker_changes_response_429 import ListTrackerChangesResponse429
from ...models.list_tracker_changes_response_500 import ListTrackerChangesResponse500
from ...models.list_tracker_changes_response_503 import ListTrackerChangesResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    list_id: str,
    *,
    api_key: str,
    since: datetime.datetime | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["apiKey"] = api_key

    json_since: None | str | Unset
    if isinstance(since, Unset):
        json_since = UNSET
    elif isinstance(since, datetime.datetime):
        json_since = since.isoformat()
    else:
        json_since = since
    params["since"] = json_since

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tracker/changes/{list_id}".format(
            list_id=quote(str(list_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListTrackerChangesResponse200
    | ListTrackerChangesResponse400
    | ListTrackerChangesResponse401
    | ListTrackerChangesResponse402
    | ListTrackerChangesResponse403
    | ListTrackerChangesResponse404
    | ListTrackerChangesResponse429
    | ListTrackerChangesResponse500
    | ListTrackerChangesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ListTrackerChangesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListTrackerChangesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListTrackerChangesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ListTrackerChangesResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ListTrackerChangesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListTrackerChangesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ListTrackerChangesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListTrackerChangesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListTrackerChangesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListTrackerChangesResponse200
    | ListTrackerChangesResponse400
    | ListTrackerChangesResponse401
    | ListTrackerChangesResponse402
    | ListTrackerChangesResponse403
    | ListTrackerChangesResponse404
    | ListTrackerChangesResponse429
    | ListTrackerChangesResponse500
    | ListTrackerChangesResponse503
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
    since: datetime.datetime | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[
    ListTrackerChangesResponse200
    | ListTrackerChangesResponse400
    | ListTrackerChangesResponse401
    | ListTrackerChangesResponse402
    | ListTrackerChangesResponse403
    | ListTrackerChangesResponse404
    | ListTrackerChangesResponse429
    | ListTrackerChangesResponse500
    | ListTrackerChangesResponse503
]:
    r"""List tracker changes

     List detected changes for a tracker list. All returned signals matched a tracking rule.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        since (datetime.datetime | None | Unset):
        cursor (None | str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTrackerChangesResponse200 | ListTrackerChangesResponse400 | ListTrackerChangesResponse401 | ListTrackerChangesResponse402 | ListTrackerChangesResponse403 | ListTrackerChangesResponse404 | ListTrackerChangesResponse429 | ListTrackerChangesResponse500 | ListTrackerChangesResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        api_key=api_key,
        since=since,
        cursor=cursor,
        limit=limit,
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
    since: datetime.datetime | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> (
    ListTrackerChangesResponse200
    | ListTrackerChangesResponse400
    | ListTrackerChangesResponse401
    | ListTrackerChangesResponse402
    | ListTrackerChangesResponse403
    | ListTrackerChangesResponse404
    | ListTrackerChangesResponse429
    | ListTrackerChangesResponse500
    | ListTrackerChangesResponse503
    | None
):
    r"""List tracker changes

     List detected changes for a tracker list. All returned signals matched a tracking rule.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        since (datetime.datetime | None | Unset):
        cursor (None | str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTrackerChangesResponse200 | ListTrackerChangesResponse400 | ListTrackerChangesResponse401 | ListTrackerChangesResponse402 | ListTrackerChangesResponse403 | ListTrackerChangesResponse404 | ListTrackerChangesResponse429 | ListTrackerChangesResponse500 | ListTrackerChangesResponse503
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
        api_key=api_key,
        since=since,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    since: datetime.datetime | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[
    ListTrackerChangesResponse200
    | ListTrackerChangesResponse400
    | ListTrackerChangesResponse401
    | ListTrackerChangesResponse402
    | ListTrackerChangesResponse403
    | ListTrackerChangesResponse404
    | ListTrackerChangesResponse429
    | ListTrackerChangesResponse500
    | ListTrackerChangesResponse503
]:
    r"""List tracker changes

     List detected changes for a tracker list. All returned signals matched a tracking rule.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        since (datetime.datetime | None | Unset):
        cursor (None | str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTrackerChangesResponse200 | ListTrackerChangesResponse400 | ListTrackerChangesResponse401 | ListTrackerChangesResponse402 | ListTrackerChangesResponse403 | ListTrackerChangesResponse404 | ListTrackerChangesResponse429 | ListTrackerChangesResponse500 | ListTrackerChangesResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        api_key=api_key,
        since=since,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    since: datetime.datetime | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> (
    ListTrackerChangesResponse200
    | ListTrackerChangesResponse400
    | ListTrackerChangesResponse401
    | ListTrackerChangesResponse402
    | ListTrackerChangesResponse403
    | ListTrackerChangesResponse404
    | ListTrackerChangesResponse429
    | ListTrackerChangesResponse500
    | ListTrackerChangesResponse503
    | None
):
    r"""List tracker changes

     List detected changes for a tracker list. All returned signals matched a tracking rule.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        since (datetime.datetime | None | Unset):
        cursor (None | str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTrackerChangesResponse200 | ListTrackerChangesResponse400 | ListTrackerChangesResponse401 | ListTrackerChangesResponse402 | ListTrackerChangesResponse403 | ListTrackerChangesResponse404 | ListTrackerChangesResponse429 | ListTrackerChangesResponse500 | ListTrackerChangesResponse503
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            api_key=api_key,
            since=since,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
