from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_rate_limits_response_200 import GetRateLimitsResponse200
from ...models.get_rate_limits_response_400 import GetRateLimitsResponse400
from ...models.get_rate_limits_response_401 import GetRateLimitsResponse401
from ...models.get_rate_limits_response_402 import GetRateLimitsResponse402
from ...models.get_rate_limits_response_403 import GetRateLimitsResponse403
from ...models.get_rate_limits_response_404 import GetRateLimitsResponse404
from ...models.get_rate_limits_response_422 import GetRateLimitsResponse422
from ...models.get_rate_limits_response_429 import GetRateLimitsResponse429
from ...models.get_rate_limits_response_500 import GetRateLimitsResponse500
from ...models.get_rate_limits_response_503 import GetRateLimitsResponse503
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
        "url": "/v1/rate-limits",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetRateLimitsResponse200
    | GetRateLimitsResponse400
    | GetRateLimitsResponse401
    | GetRateLimitsResponse402
    | GetRateLimitsResponse403
    | GetRateLimitsResponse404
    | GetRateLimitsResponse422
    | GetRateLimitsResponse429
    | GetRateLimitsResponse500
    | GetRateLimitsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetRateLimitsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetRateLimitsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetRateLimitsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetRateLimitsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetRateLimitsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetRateLimitsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetRateLimitsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetRateLimitsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetRateLimitsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetRateLimitsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetRateLimitsResponse200
    | GetRateLimitsResponse400
    | GetRateLimitsResponse401
    | GetRateLimitsResponse402
    | GetRateLimitsResponse403
    | GetRateLimitsResponse404
    | GetRateLimitsResponse422
    | GetRateLimitsResponse429
    | GetRateLimitsResponse500
    | GetRateLimitsResponse503
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
    GetRateLimitsResponse200
    | GetRateLimitsResponse400
    | GetRateLimitsResponse401
    | GetRateLimitsResponse402
    | GetRateLimitsResponse403
    | GetRateLimitsResponse404
    | GetRateLimitsResponse422
    | GetRateLimitsResponse429
    | GetRateLimitsResponse500
    | GetRateLimitsResponse503
]:
    """Get organization rate limits

     Returns the effective rate limits for all API endpoints for your organization. If your organization
    has custom rate limits on any endpoint, those are reflected here.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRateLimitsResponse200 | GetRateLimitsResponse400 | GetRateLimitsResponse401 | GetRateLimitsResponse402 | GetRateLimitsResponse403 | GetRateLimitsResponse404 | GetRateLimitsResponse422 | GetRateLimitsResponse429 | GetRateLimitsResponse500 | GetRateLimitsResponse503]
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
    GetRateLimitsResponse200
    | GetRateLimitsResponse400
    | GetRateLimitsResponse401
    | GetRateLimitsResponse402
    | GetRateLimitsResponse403
    | GetRateLimitsResponse404
    | GetRateLimitsResponse422
    | GetRateLimitsResponse429
    | GetRateLimitsResponse500
    | GetRateLimitsResponse503
    | None
):
    """Get organization rate limits

     Returns the effective rate limits for all API endpoints for your organization. If your organization
    has custom rate limits on any endpoint, those are reflected here.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRateLimitsResponse200 | GetRateLimitsResponse400 | GetRateLimitsResponse401 | GetRateLimitsResponse402 | GetRateLimitsResponse403 | GetRateLimitsResponse404 | GetRateLimitsResponse422 | GetRateLimitsResponse429 | GetRateLimitsResponse500 | GetRateLimitsResponse503
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
    GetRateLimitsResponse200
    | GetRateLimitsResponse400
    | GetRateLimitsResponse401
    | GetRateLimitsResponse402
    | GetRateLimitsResponse403
    | GetRateLimitsResponse404
    | GetRateLimitsResponse422
    | GetRateLimitsResponse429
    | GetRateLimitsResponse500
    | GetRateLimitsResponse503
]:
    """Get organization rate limits

     Returns the effective rate limits for all API endpoints for your organization. If your organization
    has custom rate limits on any endpoint, those are reflected here.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRateLimitsResponse200 | GetRateLimitsResponse400 | GetRateLimitsResponse401 | GetRateLimitsResponse402 | GetRateLimitsResponse403 | GetRateLimitsResponse404 | GetRateLimitsResponse422 | GetRateLimitsResponse429 | GetRateLimitsResponse500 | GetRateLimitsResponse503]
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
    GetRateLimitsResponse200
    | GetRateLimitsResponse400
    | GetRateLimitsResponse401
    | GetRateLimitsResponse402
    | GetRateLimitsResponse403
    | GetRateLimitsResponse404
    | GetRateLimitsResponse422
    | GetRateLimitsResponse429
    | GetRateLimitsResponse500
    | GetRateLimitsResponse503
    | None
):
    """Get organization rate limits

     Returns the effective rate limits for all API endpoints for your organization. If your organization
    has custom rate limits on any endpoint, those are reflected here.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRateLimitsResponse200 | GetRateLimitsResponse400 | GetRateLimitsResponse401 | GetRateLimitsResponse402 | GetRateLimitsResponse403 | GetRateLimitsResponse404 | GetRateLimitsResponse422 | GetRateLimitsResponse429 | GetRateLimitsResponse500 | GetRateLimitsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
        )
    ).parsed
