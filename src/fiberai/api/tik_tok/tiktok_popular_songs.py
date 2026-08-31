from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tiktok_popular_songs_body import TiktokPopularSongsBody
from ...models.tiktok_popular_songs_response_200 import TiktokPopularSongsResponse200
from ...models.tiktok_popular_songs_response_400 import TiktokPopularSongsResponse400
from ...models.tiktok_popular_songs_response_401 import TiktokPopularSongsResponse401
from ...models.tiktok_popular_songs_response_402 import TiktokPopularSongsResponse402
from ...models.tiktok_popular_songs_response_403 import TiktokPopularSongsResponse403
from ...models.tiktok_popular_songs_response_404 import TiktokPopularSongsResponse404
from ...models.tiktok_popular_songs_response_422 import TiktokPopularSongsResponse422
from ...models.tiktok_popular_songs_response_429 import TiktokPopularSongsResponse429
from ...models.tiktok_popular_songs_response_500 import TiktokPopularSongsResponse500
from ...models.tiktok_popular_songs_response_503 import TiktokPopularSongsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TiktokPopularSongsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tiktok/popular-songs",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TiktokPopularSongsResponse200
    | TiktokPopularSongsResponse400
    | TiktokPopularSongsResponse401
    | TiktokPopularSongsResponse402
    | TiktokPopularSongsResponse403
    | TiktokPopularSongsResponse404
    | TiktokPopularSongsResponse422
    | TiktokPopularSongsResponse429
    | TiktokPopularSongsResponse500
    | TiktokPopularSongsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TiktokPopularSongsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TiktokPopularSongsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TiktokPopularSongsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TiktokPopularSongsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TiktokPopularSongsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TiktokPopularSongsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = TiktokPopularSongsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = TiktokPopularSongsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TiktokPopularSongsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TiktokPopularSongsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TiktokPopularSongsResponse200
    | TiktokPopularSongsResponse400
    | TiktokPopularSongsResponse401
    | TiktokPopularSongsResponse402
    | TiktokPopularSongsResponse403
    | TiktokPopularSongsResponse404
    | TiktokPopularSongsResponse422
    | TiktokPopularSongsResponse429
    | TiktokPopularSongsResponse500
    | TiktokPopularSongsResponse503
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
    body: TiktokPopularSongsBody,
) -> Response[
    TiktokPopularSongsResponse200
    | TiktokPopularSongsResponse400
    | TiktokPopularSongsResponse401
    | TiktokPopularSongsResponse402
    | TiktokPopularSongsResponse403
    | TiktokPopularSongsResponse404
    | TiktokPopularSongsResponse422
    | TiktokPopularSongsResponse429
    | TiktokPopularSongsResponse500
    | TiktokPopularSongsResponse503
]:
    """Fetch popular TikTok songs

     Fetches a list of currently popular songs/sounds on TikTok.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokPopularSongsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokPopularSongsResponse200 | TiktokPopularSongsResponse400 | TiktokPopularSongsResponse401 | TiktokPopularSongsResponse402 | TiktokPopularSongsResponse403 | TiktokPopularSongsResponse404 | TiktokPopularSongsResponse422 | TiktokPopularSongsResponse429 | TiktokPopularSongsResponse500 | TiktokPopularSongsResponse503]
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
    body: TiktokPopularSongsBody,
) -> (
    TiktokPopularSongsResponse200
    | TiktokPopularSongsResponse400
    | TiktokPopularSongsResponse401
    | TiktokPopularSongsResponse402
    | TiktokPopularSongsResponse403
    | TiktokPopularSongsResponse404
    | TiktokPopularSongsResponse422
    | TiktokPopularSongsResponse429
    | TiktokPopularSongsResponse500
    | TiktokPopularSongsResponse503
    | None
):
    """Fetch popular TikTok songs

     Fetches a list of currently popular songs/sounds on TikTok.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokPopularSongsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokPopularSongsResponse200 | TiktokPopularSongsResponse400 | TiktokPopularSongsResponse401 | TiktokPopularSongsResponse402 | TiktokPopularSongsResponse403 | TiktokPopularSongsResponse404 | TiktokPopularSongsResponse422 | TiktokPopularSongsResponse429 | TiktokPopularSongsResponse500 | TiktokPopularSongsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokPopularSongsBody,
) -> Response[
    TiktokPopularSongsResponse200
    | TiktokPopularSongsResponse400
    | TiktokPopularSongsResponse401
    | TiktokPopularSongsResponse402
    | TiktokPopularSongsResponse403
    | TiktokPopularSongsResponse404
    | TiktokPopularSongsResponse422
    | TiktokPopularSongsResponse429
    | TiktokPopularSongsResponse500
    | TiktokPopularSongsResponse503
]:
    """Fetch popular TikTok songs

     Fetches a list of currently popular songs/sounds on TikTok.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokPopularSongsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokPopularSongsResponse200 | TiktokPopularSongsResponse400 | TiktokPopularSongsResponse401 | TiktokPopularSongsResponse402 | TiktokPopularSongsResponse403 | TiktokPopularSongsResponse404 | TiktokPopularSongsResponse422 | TiktokPopularSongsResponse429 | TiktokPopularSongsResponse500 | TiktokPopularSongsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokPopularSongsBody,
) -> (
    TiktokPopularSongsResponse200
    | TiktokPopularSongsResponse400
    | TiktokPopularSongsResponse401
    | TiktokPopularSongsResponse402
    | TiktokPopularSongsResponse403
    | TiktokPopularSongsResponse404
    | TiktokPopularSongsResponse422
    | TiktokPopularSongsResponse429
    | TiktokPopularSongsResponse500
    | TiktokPopularSongsResponse503
    | None
):
    """Fetch popular TikTok songs

     Fetches a list of currently popular songs/sounds on TikTok.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokPopularSongsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokPopularSongsResponse200 | TiktokPopularSongsResponse400 | TiktokPopularSongsResponse401 | TiktokPopularSongsResponse402 | TiktokPopularSongsResponse403 | TiktokPopularSongsResponse404 | TiktokPopularSongsResponse422 | TiktokPopularSongsResponse429 | TiktokPopularSongsResponse500 | TiktokPopularSongsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
