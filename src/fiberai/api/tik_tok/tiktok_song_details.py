from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tiktok_song_details_body import TiktokSongDetailsBody
from ...models.tiktok_song_details_response_200 import TiktokSongDetailsResponse200
from ...models.tiktok_song_details_response_400 import TiktokSongDetailsResponse400
from ...models.tiktok_song_details_response_401 import TiktokSongDetailsResponse401
from ...models.tiktok_song_details_response_402 import TiktokSongDetailsResponse402
from ...models.tiktok_song_details_response_403 import TiktokSongDetailsResponse403
from ...models.tiktok_song_details_response_404 import TiktokSongDetailsResponse404
from ...models.tiktok_song_details_response_429 import TiktokSongDetailsResponse429
from ...models.tiktok_song_details_response_500 import TiktokSongDetailsResponse500
from ...models.tiktok_song_details_response_503 import TiktokSongDetailsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TiktokSongDetailsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tiktok/song-details",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TiktokSongDetailsResponse200
    | TiktokSongDetailsResponse400
    | TiktokSongDetailsResponse401
    | TiktokSongDetailsResponse402
    | TiktokSongDetailsResponse403
    | TiktokSongDetailsResponse404
    | TiktokSongDetailsResponse429
    | TiktokSongDetailsResponse500
    | TiktokSongDetailsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TiktokSongDetailsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TiktokSongDetailsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TiktokSongDetailsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TiktokSongDetailsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TiktokSongDetailsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TiktokSongDetailsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TiktokSongDetailsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TiktokSongDetailsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TiktokSongDetailsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TiktokSongDetailsResponse200
    | TiktokSongDetailsResponse400
    | TiktokSongDetailsResponse401
    | TiktokSongDetailsResponse402
    | TiktokSongDetailsResponse403
    | TiktokSongDetailsResponse404
    | TiktokSongDetailsResponse429
    | TiktokSongDetailsResponse500
    | TiktokSongDetailsResponse503
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
    body: TiktokSongDetailsBody,
) -> Response[
    TiktokSongDetailsResponse200
    | TiktokSongDetailsResponse400
    | TiktokSongDetailsResponse401
    | TiktokSongDetailsResponse402
    | TiktokSongDetailsResponse403
    | TiktokSongDetailsResponse404
    | TiktokSongDetailsResponse429
    | TiktokSongDetailsResponse500
    | TiktokSongDetailsResponse503
]:
    r"""Fetch TikTok song details

     Fetches details about a TikTok song/sound including title, artist, and usage statistics.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokSongDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokSongDetailsResponse200 | TiktokSongDetailsResponse400 | TiktokSongDetailsResponse401 | TiktokSongDetailsResponse402 | TiktokSongDetailsResponse403 | TiktokSongDetailsResponse404 | TiktokSongDetailsResponse429 | TiktokSongDetailsResponse500 | TiktokSongDetailsResponse503]
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
    body: TiktokSongDetailsBody,
) -> (
    TiktokSongDetailsResponse200
    | TiktokSongDetailsResponse400
    | TiktokSongDetailsResponse401
    | TiktokSongDetailsResponse402
    | TiktokSongDetailsResponse403
    | TiktokSongDetailsResponse404
    | TiktokSongDetailsResponse429
    | TiktokSongDetailsResponse500
    | TiktokSongDetailsResponse503
    | None
):
    r"""Fetch TikTok song details

     Fetches details about a TikTok song/sound including title, artist, and usage statistics.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokSongDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokSongDetailsResponse200 | TiktokSongDetailsResponse400 | TiktokSongDetailsResponse401 | TiktokSongDetailsResponse402 | TiktokSongDetailsResponse403 | TiktokSongDetailsResponse404 | TiktokSongDetailsResponse429 | TiktokSongDetailsResponse500 | TiktokSongDetailsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokSongDetailsBody,
) -> Response[
    TiktokSongDetailsResponse200
    | TiktokSongDetailsResponse400
    | TiktokSongDetailsResponse401
    | TiktokSongDetailsResponse402
    | TiktokSongDetailsResponse403
    | TiktokSongDetailsResponse404
    | TiktokSongDetailsResponse429
    | TiktokSongDetailsResponse500
    | TiktokSongDetailsResponse503
]:
    r"""Fetch TikTok song details

     Fetches details about a TikTok song/sound including title, artist, and usage statistics.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokSongDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokSongDetailsResponse200 | TiktokSongDetailsResponse400 | TiktokSongDetailsResponse401 | TiktokSongDetailsResponse402 | TiktokSongDetailsResponse403 | TiktokSongDetailsResponse404 | TiktokSongDetailsResponse429 | TiktokSongDetailsResponse500 | TiktokSongDetailsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokSongDetailsBody,
) -> (
    TiktokSongDetailsResponse200
    | TiktokSongDetailsResponse400
    | TiktokSongDetailsResponse401
    | TiktokSongDetailsResponse402
    | TiktokSongDetailsResponse403
    | TiktokSongDetailsResponse404
    | TiktokSongDetailsResponse429
    | TiktokSongDetailsResponse500
    | TiktokSongDetailsResponse503
    | None
):
    r"""Fetch TikTok song details

     Fetches details about a TikTok song/sound including title, artist, and usage statistics.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokSongDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokSongDetailsResponse200 | TiktokSongDetailsResponse400 | TiktokSongDetailsResponse401 | TiktokSongDetailsResponse402 | TiktokSongDetailsResponse403 | TiktokSongDetailsResponse404 | TiktokSongDetailsResponse429 | TiktokSongDetailsResponse500 | TiktokSongDetailsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
