from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tracker_overview_response_200 import GetTrackerOverviewResponse200
from ...models.get_tracker_overview_response_400 import GetTrackerOverviewResponse400
from ...models.get_tracker_overview_response_401 import GetTrackerOverviewResponse401
from ...models.get_tracker_overview_response_402 import GetTrackerOverviewResponse402
from ...models.get_tracker_overview_response_403 import GetTrackerOverviewResponse403
from ...models.get_tracker_overview_response_404 import GetTrackerOverviewResponse404
from ...models.get_tracker_overview_response_429 import GetTrackerOverviewResponse429
from ...models.get_tracker_overview_response_500 import GetTrackerOverviewResponse500
from ...models.get_tracker_overview_response_503 import GetTrackerOverviewResponse503
from ...types import UNSET, Response


def _get_kwargs(
    *,
    api_key: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["apiKey"] = api_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tracker/overview",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetTrackerOverviewResponse200
    | GetTrackerOverviewResponse400
    | GetTrackerOverviewResponse401
    | GetTrackerOverviewResponse402
    | GetTrackerOverviewResponse403
    | GetTrackerOverviewResponse404
    | GetTrackerOverviewResponse429
    | GetTrackerOverviewResponse500
    | GetTrackerOverviewResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetTrackerOverviewResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetTrackerOverviewResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetTrackerOverviewResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetTrackerOverviewResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetTrackerOverviewResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetTrackerOverviewResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetTrackerOverviewResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetTrackerOverviewResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetTrackerOverviewResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetTrackerOverviewResponse200
    | GetTrackerOverviewResponse400
    | GetTrackerOverviewResponse401
    | GetTrackerOverviewResponse402
    | GetTrackerOverviewResponse403
    | GetTrackerOverviewResponse404
    | GetTrackerOverviewResponse429
    | GetTrackerOverviewResponse500
    | GetTrackerOverviewResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> Response[
    GetTrackerOverviewResponse200
    | GetTrackerOverviewResponse400
    | GetTrackerOverviewResponse401
    | GetTrackerOverviewResponse402
    | GetTrackerOverviewResponse403
    | GetTrackerOverviewResponse404
    | GetTrackerOverviewResponse429
    | GetTrackerOverviewResponse500
    | GetTrackerOverviewResponse503
]:
    r"""Get tracker overview

     Returns a single-call summary of all of your tracker lists, the rules attached to each, and a
    forecast of upcoming refreshes with the credits each refresh will cost. Useful for monitoring credit
    burn and seeing what's being tracked at a glance.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTrackerOverviewResponse200 | GetTrackerOverviewResponse400 | GetTrackerOverviewResponse401 | GetTrackerOverviewResponse402 | GetTrackerOverviewResponse403 | GetTrackerOverviewResponse404 | GetTrackerOverviewResponse429 | GetTrackerOverviewResponse500 | GetTrackerOverviewResponse503]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> (
    GetTrackerOverviewResponse200
    | GetTrackerOverviewResponse400
    | GetTrackerOverviewResponse401
    | GetTrackerOverviewResponse402
    | GetTrackerOverviewResponse403
    | GetTrackerOverviewResponse404
    | GetTrackerOverviewResponse429
    | GetTrackerOverviewResponse500
    | GetTrackerOverviewResponse503
    | None
):
    r"""Get tracker overview

     Returns a single-call summary of all of your tracker lists, the rules attached to each, and a
    forecast of upcoming refreshes with the credits each refresh will cost. Useful for monitoring credit
    burn and seeing what's being tracked at a glance.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTrackerOverviewResponse200 | GetTrackerOverviewResponse400 | GetTrackerOverviewResponse401 | GetTrackerOverviewResponse402 | GetTrackerOverviewResponse403 | GetTrackerOverviewResponse404 | GetTrackerOverviewResponse429 | GetTrackerOverviewResponse500 | GetTrackerOverviewResponse503
    """

    return sync_detailed(
        client=client,
        api_key=api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> Response[
    GetTrackerOverviewResponse200
    | GetTrackerOverviewResponse400
    | GetTrackerOverviewResponse401
    | GetTrackerOverviewResponse402
    | GetTrackerOverviewResponse403
    | GetTrackerOverviewResponse404
    | GetTrackerOverviewResponse429
    | GetTrackerOverviewResponse500
    | GetTrackerOverviewResponse503
]:
    r"""Get tracker overview

     Returns a single-call summary of all of your tracker lists, the rules attached to each, and a
    forecast of upcoming refreshes with the credits each refresh will cost. Useful for monitoring credit
    burn and seeing what's being tracked at a glance.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTrackerOverviewResponse200 | GetTrackerOverviewResponse400 | GetTrackerOverviewResponse401 | GetTrackerOverviewResponse402 | GetTrackerOverviewResponse403 | GetTrackerOverviewResponse404 | GetTrackerOverviewResponse429 | GetTrackerOverviewResponse500 | GetTrackerOverviewResponse503]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> (
    GetTrackerOverviewResponse200
    | GetTrackerOverviewResponse400
    | GetTrackerOverviewResponse401
    | GetTrackerOverviewResponse402
    | GetTrackerOverviewResponse403
    | GetTrackerOverviewResponse404
    | GetTrackerOverviewResponse429
    | GetTrackerOverviewResponse500
    | GetTrackerOverviewResponse503
    | None
):
    r"""Get tracker overview

     Returns a single-call summary of all of your tracker lists, the rules attached to each, and a
    forecast of upcoming refreshes with the credits each refresh will cost. Useful for monitoring credit
    burn and seeing what's being tracked at a glance.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTrackerOverviewResponse200 | GetTrackerOverviewResponse400 | GetTrackerOverviewResponse401 | GetTrackerOverviewResponse402 | GetTrackerOverviewResponse403 | GetTrackerOverviewResponse404 | GetTrackerOverviewResponse429 | GetTrackerOverviewResponse500 | GetTrackerOverviewResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
        )
    ).parsed
