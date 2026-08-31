from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tiktok_trending_feed_body import TiktokTrendingFeedBody
from ...models.tiktok_trending_feed_response_200 import TiktokTrendingFeedResponse200
from ...models.tiktok_trending_feed_response_400 import TiktokTrendingFeedResponse400
from ...models.tiktok_trending_feed_response_401 import TiktokTrendingFeedResponse401
from ...models.tiktok_trending_feed_response_402 import TiktokTrendingFeedResponse402
from ...models.tiktok_trending_feed_response_403 import TiktokTrendingFeedResponse403
from ...models.tiktok_trending_feed_response_404 import TiktokTrendingFeedResponse404
from ...models.tiktok_trending_feed_response_422 import TiktokTrendingFeedResponse422
from ...models.tiktok_trending_feed_response_429 import TiktokTrendingFeedResponse429
from ...models.tiktok_trending_feed_response_500 import TiktokTrendingFeedResponse500
from ...models.tiktok_trending_feed_response_503 import TiktokTrendingFeedResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TiktokTrendingFeedBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tiktok/trending-feed",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TiktokTrendingFeedResponse200
    | TiktokTrendingFeedResponse400
    | TiktokTrendingFeedResponse401
    | TiktokTrendingFeedResponse402
    | TiktokTrendingFeedResponse403
    | TiktokTrendingFeedResponse404
    | TiktokTrendingFeedResponse422
    | TiktokTrendingFeedResponse429
    | TiktokTrendingFeedResponse500
    | TiktokTrendingFeedResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TiktokTrendingFeedResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TiktokTrendingFeedResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TiktokTrendingFeedResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TiktokTrendingFeedResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TiktokTrendingFeedResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TiktokTrendingFeedResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = TiktokTrendingFeedResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = TiktokTrendingFeedResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TiktokTrendingFeedResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TiktokTrendingFeedResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TiktokTrendingFeedResponse200
    | TiktokTrendingFeedResponse400
    | TiktokTrendingFeedResponse401
    | TiktokTrendingFeedResponse402
    | TiktokTrendingFeedResponse403
    | TiktokTrendingFeedResponse404
    | TiktokTrendingFeedResponse422
    | TiktokTrendingFeedResponse429
    | TiktokTrendingFeedResponse500
    | TiktokTrendingFeedResponse503
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
    body: TiktokTrendingFeedBody,
) -> Response[
    TiktokTrendingFeedResponse200
    | TiktokTrendingFeedResponse400
    | TiktokTrendingFeedResponse401
    | TiktokTrendingFeedResponse402
    | TiktokTrendingFeedResponse403
    | TiktokTrendingFeedResponse404
    | TiktokTrendingFeedResponse422
    | TiktokTrendingFeedResponse429
    | TiktokTrendingFeedResponse500
    | TiktokTrendingFeedResponse503
]:
    """Fetch TikTok trending feed

     Fetches the current TikTok trending feed. Returns a paginated list of trending videos. Use the
    `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokTrendingFeedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokTrendingFeedResponse200 | TiktokTrendingFeedResponse400 | TiktokTrendingFeedResponse401 | TiktokTrendingFeedResponse402 | TiktokTrendingFeedResponse403 | TiktokTrendingFeedResponse404 | TiktokTrendingFeedResponse422 | TiktokTrendingFeedResponse429 | TiktokTrendingFeedResponse500 | TiktokTrendingFeedResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokTrendingFeedBody,
) -> (
    TiktokTrendingFeedResponse200
    | TiktokTrendingFeedResponse400
    | TiktokTrendingFeedResponse401
    | TiktokTrendingFeedResponse402
    | TiktokTrendingFeedResponse403
    | TiktokTrendingFeedResponse404
    | TiktokTrendingFeedResponse422
    | TiktokTrendingFeedResponse429
    | TiktokTrendingFeedResponse500
    | TiktokTrendingFeedResponse503
    | None
):
    """Fetch TikTok trending feed

     Fetches the current TikTok trending feed. Returns a paginated list of trending videos. Use the
    `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokTrendingFeedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokTrendingFeedResponse200 | TiktokTrendingFeedResponse400 | TiktokTrendingFeedResponse401 | TiktokTrendingFeedResponse402 | TiktokTrendingFeedResponse403 | TiktokTrendingFeedResponse404 | TiktokTrendingFeedResponse422 | TiktokTrendingFeedResponse429 | TiktokTrendingFeedResponse500 | TiktokTrendingFeedResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokTrendingFeedBody,
) -> Response[
    TiktokTrendingFeedResponse200
    | TiktokTrendingFeedResponse400
    | TiktokTrendingFeedResponse401
    | TiktokTrendingFeedResponse402
    | TiktokTrendingFeedResponse403
    | TiktokTrendingFeedResponse404
    | TiktokTrendingFeedResponse422
    | TiktokTrendingFeedResponse429
    | TiktokTrendingFeedResponse500
    | TiktokTrendingFeedResponse503
]:
    """Fetch TikTok trending feed

     Fetches the current TikTok trending feed. Returns a paginated list of trending videos. Use the
    `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokTrendingFeedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokTrendingFeedResponse200 | TiktokTrendingFeedResponse400 | TiktokTrendingFeedResponse401 | TiktokTrendingFeedResponse402 | TiktokTrendingFeedResponse403 | TiktokTrendingFeedResponse404 | TiktokTrendingFeedResponse422 | TiktokTrendingFeedResponse429 | TiktokTrendingFeedResponse500 | TiktokTrendingFeedResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokTrendingFeedBody,
) -> (
    TiktokTrendingFeedResponse200
    | TiktokTrendingFeedResponse400
    | TiktokTrendingFeedResponse401
    | TiktokTrendingFeedResponse402
    | TiktokTrendingFeedResponse403
    | TiktokTrendingFeedResponse404
    | TiktokTrendingFeedResponse422
    | TiktokTrendingFeedResponse429
    | TiktokTrendingFeedResponse500
    | TiktokTrendingFeedResponse503
    | None
):
    """Fetch TikTok trending feed

     Fetches the current TikTok trending feed. Returns a paginated list of trending videos. Use the
    `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokTrendingFeedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokTrendingFeedResponse200 | TiktokTrendingFeedResponse400 | TiktokTrendingFeedResponse401 | TiktokTrendingFeedResponse402 | TiktokTrendingFeedResponse403 | TiktokTrendingFeedResponse404 | TiktokTrendingFeedResponse422 | TiktokTrendingFeedResponse429 | TiktokTrendingFeedResponse500 | TiktokTrendingFeedResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
