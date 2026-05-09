from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tiktok_popular_hashtags_body import TiktokPopularHashtagsBody
from ...models.tiktok_popular_hashtags_response_200 import TiktokPopularHashtagsResponse200
from ...models.tiktok_popular_hashtags_response_400 import TiktokPopularHashtagsResponse400
from ...models.tiktok_popular_hashtags_response_401 import TiktokPopularHashtagsResponse401
from ...models.tiktok_popular_hashtags_response_402 import TiktokPopularHashtagsResponse402
from ...models.tiktok_popular_hashtags_response_403 import TiktokPopularHashtagsResponse403
from ...models.tiktok_popular_hashtags_response_404 import TiktokPopularHashtagsResponse404
from ...models.tiktok_popular_hashtags_response_429 import TiktokPopularHashtagsResponse429
from ...models.tiktok_popular_hashtags_response_500 import TiktokPopularHashtagsResponse500
from ...models.tiktok_popular_hashtags_response_503 import TiktokPopularHashtagsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TiktokPopularHashtagsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tiktok/popular-hashtags",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TiktokPopularHashtagsResponse200
    | TiktokPopularHashtagsResponse400
    | TiktokPopularHashtagsResponse401
    | TiktokPopularHashtagsResponse402
    | TiktokPopularHashtagsResponse403
    | TiktokPopularHashtagsResponse404
    | TiktokPopularHashtagsResponse429
    | TiktokPopularHashtagsResponse500
    | TiktokPopularHashtagsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TiktokPopularHashtagsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TiktokPopularHashtagsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TiktokPopularHashtagsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TiktokPopularHashtagsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TiktokPopularHashtagsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TiktokPopularHashtagsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TiktokPopularHashtagsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TiktokPopularHashtagsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TiktokPopularHashtagsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TiktokPopularHashtagsResponse200
    | TiktokPopularHashtagsResponse400
    | TiktokPopularHashtagsResponse401
    | TiktokPopularHashtagsResponse402
    | TiktokPopularHashtagsResponse403
    | TiktokPopularHashtagsResponse404
    | TiktokPopularHashtagsResponse429
    | TiktokPopularHashtagsResponse500
    | TiktokPopularHashtagsResponse503
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
    body: TiktokPopularHashtagsBody,
) -> Response[
    TiktokPopularHashtagsResponse200
    | TiktokPopularHashtagsResponse400
    | TiktokPopularHashtagsResponse401
    | TiktokPopularHashtagsResponse402
    | TiktokPopularHashtagsResponse403
    | TiktokPopularHashtagsResponse404
    | TiktokPopularHashtagsResponse429
    | TiktokPopularHashtagsResponse500
    | TiktokPopularHashtagsResponse503
]:
    r"""Fetch popular TikTok hashtags

     Fetches a list of popular TikTok hashtags. Optionally filter by country and time period.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokPopularHashtagsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokPopularHashtagsResponse200 | TiktokPopularHashtagsResponse400 | TiktokPopularHashtagsResponse401 | TiktokPopularHashtagsResponse402 | TiktokPopularHashtagsResponse403 | TiktokPopularHashtagsResponse404 | TiktokPopularHashtagsResponse429 | TiktokPopularHashtagsResponse500 | TiktokPopularHashtagsResponse503]
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
    body: TiktokPopularHashtagsBody,
) -> (
    TiktokPopularHashtagsResponse200
    | TiktokPopularHashtagsResponse400
    | TiktokPopularHashtagsResponse401
    | TiktokPopularHashtagsResponse402
    | TiktokPopularHashtagsResponse403
    | TiktokPopularHashtagsResponse404
    | TiktokPopularHashtagsResponse429
    | TiktokPopularHashtagsResponse500
    | TiktokPopularHashtagsResponse503
    | None
):
    r"""Fetch popular TikTok hashtags

     Fetches a list of popular TikTok hashtags. Optionally filter by country and time period.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokPopularHashtagsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokPopularHashtagsResponse200 | TiktokPopularHashtagsResponse400 | TiktokPopularHashtagsResponse401 | TiktokPopularHashtagsResponse402 | TiktokPopularHashtagsResponse403 | TiktokPopularHashtagsResponse404 | TiktokPopularHashtagsResponse429 | TiktokPopularHashtagsResponse500 | TiktokPopularHashtagsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokPopularHashtagsBody,
) -> Response[
    TiktokPopularHashtagsResponse200
    | TiktokPopularHashtagsResponse400
    | TiktokPopularHashtagsResponse401
    | TiktokPopularHashtagsResponse402
    | TiktokPopularHashtagsResponse403
    | TiktokPopularHashtagsResponse404
    | TiktokPopularHashtagsResponse429
    | TiktokPopularHashtagsResponse500
    | TiktokPopularHashtagsResponse503
]:
    r"""Fetch popular TikTok hashtags

     Fetches a list of popular TikTok hashtags. Optionally filter by country and time period.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokPopularHashtagsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokPopularHashtagsResponse200 | TiktokPopularHashtagsResponse400 | TiktokPopularHashtagsResponse401 | TiktokPopularHashtagsResponse402 | TiktokPopularHashtagsResponse403 | TiktokPopularHashtagsResponse404 | TiktokPopularHashtagsResponse429 | TiktokPopularHashtagsResponse500 | TiktokPopularHashtagsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokPopularHashtagsBody,
) -> (
    TiktokPopularHashtagsResponse200
    | TiktokPopularHashtagsResponse400
    | TiktokPopularHashtagsResponse401
    | TiktokPopularHashtagsResponse402
    | TiktokPopularHashtagsResponse403
    | TiktokPopularHashtagsResponse404
    | TiktokPopularHashtagsResponse429
    | TiktokPopularHashtagsResponse500
    | TiktokPopularHashtagsResponse503
    | None
):
    r"""Fetch popular TikTok hashtags

     Fetches a list of popular TikTok hashtags. Optionally filter by country and time period.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokPopularHashtagsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokPopularHashtagsResponse200 | TiktokPopularHashtagsResponse400 | TiktokPopularHashtagsResponse401 | TiktokPopularHashtagsResponse402 | TiktokPopularHashtagsResponse403 | TiktokPopularHashtagsResponse404 | TiktokPopularHashtagsResponse429 | TiktokPopularHashtagsResponse500 | TiktokPopularHashtagsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
