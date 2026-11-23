from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_tracker_unresolved_identifiers_response_200 import ListTrackerUnresolvedIdentifiersResponse200
from ...models.list_tracker_unresolved_identifiers_response_400 import ListTrackerUnresolvedIdentifiersResponse400
from ...models.list_tracker_unresolved_identifiers_response_401 import ListTrackerUnresolvedIdentifiersResponse401
from ...models.list_tracker_unresolved_identifiers_response_402 import ListTrackerUnresolvedIdentifiersResponse402
from ...models.list_tracker_unresolved_identifiers_response_403 import ListTrackerUnresolvedIdentifiersResponse403
from ...models.list_tracker_unresolved_identifiers_response_404 import ListTrackerUnresolvedIdentifiersResponse404
from ...models.list_tracker_unresolved_identifiers_response_422 import ListTrackerUnresolvedIdentifiersResponse422
from ...models.list_tracker_unresolved_identifiers_response_429 import ListTrackerUnresolvedIdentifiersResponse429
from ...models.list_tracker_unresolved_identifiers_response_500 import ListTrackerUnresolvedIdentifiersResponse500
from ...models.list_tracker_unresolved_identifiers_response_503 import ListTrackerUnresolvedIdentifiersResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    list_id: str,
    *,
    api_key: str,
    cursor: None | str | Unset = UNSET,
    page_size: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["apiKey"] = api_key

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tracker/person-lists/{list_id}/unresolved-identifiers".format(
            list_id=quote(str(list_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListTrackerUnresolvedIdentifiersResponse200
    | ListTrackerUnresolvedIdentifiersResponse400
    | ListTrackerUnresolvedIdentifiersResponse401
    | ListTrackerUnresolvedIdentifiersResponse402
    | ListTrackerUnresolvedIdentifiersResponse403
    | ListTrackerUnresolvedIdentifiersResponse404
    | ListTrackerUnresolvedIdentifiersResponse422
    | ListTrackerUnresolvedIdentifiersResponse429
    | ListTrackerUnresolvedIdentifiersResponse500
    | ListTrackerUnresolvedIdentifiersResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ListTrackerUnresolvedIdentifiersResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListTrackerUnresolvedIdentifiersResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListTrackerUnresolvedIdentifiersResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ListTrackerUnresolvedIdentifiersResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ListTrackerUnresolvedIdentifiersResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListTrackerUnresolvedIdentifiersResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ListTrackerUnresolvedIdentifiersResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ListTrackerUnresolvedIdentifiersResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListTrackerUnresolvedIdentifiersResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListTrackerUnresolvedIdentifiersResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListTrackerUnresolvedIdentifiersResponse200
    | ListTrackerUnresolvedIdentifiersResponse400
    | ListTrackerUnresolvedIdentifiersResponse401
    | ListTrackerUnresolvedIdentifiersResponse402
    | ListTrackerUnresolvedIdentifiersResponse403
    | ListTrackerUnresolvedIdentifiersResponse404
    | ListTrackerUnresolvedIdentifiersResponse422
    | ListTrackerUnresolvedIdentifiersResponse429
    | ListTrackerUnresolvedIdentifiersResponse500
    | ListTrackerUnresolvedIdentifiersResponse503
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
    cursor: None | str | Unset = UNSET,
    page_size: int | Unset = 50,
) -> Response[
    ListTrackerUnresolvedIdentifiersResponse200
    | ListTrackerUnresolvedIdentifiersResponse400
    | ListTrackerUnresolvedIdentifiersResponse401
    | ListTrackerUnresolvedIdentifiersResponse402
    | ListTrackerUnresolvedIdentifiersResponse403
    | ListTrackerUnresolvedIdentifiersResponse404
    | ListTrackerUnresolvedIdentifiersResponse422
    | ListTrackerUnresolvedIdentifiersResponse429
    | ListTrackerUnresolvedIdentifiersResponse500
    | ListTrackerUnresolvedIdentifiersResponse503
]:
    """List unresolved person identifiers

     List the person identifiers on a tracker list that failed to resolve to a profile, plus the number
    of identifiers still being resolved in the background. personCount on the list response only
    reflects identifiers that resolved — use this endpoint to reconcile the identifiers you sent against
    that count.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        cursor (None | str | Unset):
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTrackerUnresolvedIdentifiersResponse200 | ListTrackerUnresolvedIdentifiersResponse400 | ListTrackerUnresolvedIdentifiersResponse401 | ListTrackerUnresolvedIdentifiersResponse402 | ListTrackerUnresolvedIdentifiersResponse403 | ListTrackerUnresolvedIdentifiersResponse404 | ListTrackerUnresolvedIdentifiersResponse422 | ListTrackerUnresolvedIdentifiersResponse429 | ListTrackerUnresolvedIdentifiersResponse500 | ListTrackerUnresolvedIdentifiersResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        api_key=api_key,
        cursor=cursor,
        page_size=page_size,
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
    cursor: None | str | Unset = UNSET,
    page_size: int | Unset = 50,
) -> (
    ListTrackerUnresolvedIdentifiersResponse200
    | ListTrackerUnresolvedIdentifiersResponse400
    | ListTrackerUnresolvedIdentifiersResponse401
    | ListTrackerUnresolvedIdentifiersResponse402
    | ListTrackerUnresolvedIdentifiersResponse403
    | ListTrackerUnresolvedIdentifiersResponse404
    | ListTrackerUnresolvedIdentifiersResponse422
    | ListTrackerUnresolvedIdentifiersResponse429
    | ListTrackerUnresolvedIdentifiersResponse500
    | ListTrackerUnresolvedIdentifiersResponse503
    | None
):
    """List unresolved person identifiers

     List the person identifiers on a tracker list that failed to resolve to a profile, plus the number
    of identifiers still being resolved in the background. personCount on the list response only
    reflects identifiers that resolved — use this endpoint to reconcile the identifiers you sent against
    that count.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        cursor (None | str | Unset):
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTrackerUnresolvedIdentifiersResponse200 | ListTrackerUnresolvedIdentifiersResponse400 | ListTrackerUnresolvedIdentifiersResponse401 | ListTrackerUnresolvedIdentifiersResponse402 | ListTrackerUnresolvedIdentifiersResponse403 | ListTrackerUnresolvedIdentifiersResponse404 | ListTrackerUnresolvedIdentifiersResponse422 | ListTrackerUnresolvedIdentifiersResponse429 | ListTrackerUnresolvedIdentifiersResponse500 | ListTrackerUnresolvedIdentifiersResponse503
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
        api_key=api_key,
        cursor=cursor,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    cursor: None | str | Unset = UNSET,
    page_size: int | Unset = 50,
) -> Response[
    ListTrackerUnresolvedIdentifiersResponse200
    | ListTrackerUnresolvedIdentifiersResponse400
    | ListTrackerUnresolvedIdentifiersResponse401
    | ListTrackerUnresolvedIdentifiersResponse402
    | ListTrackerUnresolvedIdentifiersResponse403
    | ListTrackerUnresolvedIdentifiersResponse404
    | ListTrackerUnresolvedIdentifiersResponse422
    | ListTrackerUnresolvedIdentifiersResponse429
    | ListTrackerUnresolvedIdentifiersResponse500
    | ListTrackerUnresolvedIdentifiersResponse503
]:
    """List unresolved person identifiers

     List the person identifiers on a tracker list that failed to resolve to a profile, plus the number
    of identifiers still being resolved in the background. personCount on the list response only
    reflects identifiers that resolved — use this endpoint to reconcile the identifiers you sent against
    that count.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        cursor (None | str | Unset):
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTrackerUnresolvedIdentifiersResponse200 | ListTrackerUnresolvedIdentifiersResponse400 | ListTrackerUnresolvedIdentifiersResponse401 | ListTrackerUnresolvedIdentifiersResponse402 | ListTrackerUnresolvedIdentifiersResponse403 | ListTrackerUnresolvedIdentifiersResponse404 | ListTrackerUnresolvedIdentifiersResponse422 | ListTrackerUnresolvedIdentifiersResponse429 | ListTrackerUnresolvedIdentifiersResponse500 | ListTrackerUnresolvedIdentifiersResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        api_key=api_key,
        cursor=cursor,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    cursor: None | str | Unset = UNSET,
    page_size: int | Unset = 50,
) -> (
    ListTrackerUnresolvedIdentifiersResponse200
    | ListTrackerUnresolvedIdentifiersResponse400
    | ListTrackerUnresolvedIdentifiersResponse401
    | ListTrackerUnresolvedIdentifiersResponse402
    | ListTrackerUnresolvedIdentifiersResponse403
    | ListTrackerUnresolvedIdentifiersResponse404
    | ListTrackerUnresolvedIdentifiersResponse422
    | ListTrackerUnresolvedIdentifiersResponse429
    | ListTrackerUnresolvedIdentifiersResponse500
    | ListTrackerUnresolvedIdentifiersResponse503
    | None
):
    """List unresolved person identifiers

     List the person identifiers on a tracker list that failed to resolve to a profile, plus the number
    of identifiers still being resolved in the background. personCount on the list response only
    reflects identifiers that resolved — use this endpoint to reconcile the identifiers you sent against
    that count.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        cursor (None | str | Unset):
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTrackerUnresolvedIdentifiersResponse200 | ListTrackerUnresolvedIdentifiersResponse400 | ListTrackerUnresolvedIdentifiersResponse401 | ListTrackerUnresolvedIdentifiersResponse402 | ListTrackerUnresolvedIdentifiersResponse403 | ListTrackerUnresolvedIdentifiersResponse404 | ListTrackerUnresolvedIdentifiersResponse422 | ListTrackerUnresolvedIdentifiersResponse429 | ListTrackerUnresolvedIdentifiersResponse500 | ListTrackerUnresolvedIdentifiersResponse503
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            api_key=api_key,
            cursor=cursor,
            page_size=page_size,
        )
    ).parsed
