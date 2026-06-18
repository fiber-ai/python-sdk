from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.youtube_video_details_body import YoutubeVideoDetailsBody
from ...models.youtube_video_details_response_200 import YoutubeVideoDetailsResponse200
from ...models.youtube_video_details_response_400 import YoutubeVideoDetailsResponse400
from ...models.youtube_video_details_response_401 import YoutubeVideoDetailsResponse401
from ...models.youtube_video_details_response_402 import YoutubeVideoDetailsResponse402
from ...models.youtube_video_details_response_403 import YoutubeVideoDetailsResponse403
from ...models.youtube_video_details_response_404 import YoutubeVideoDetailsResponse404
from ...models.youtube_video_details_response_422 import YoutubeVideoDetailsResponse422
from ...models.youtube_video_details_response_429 import YoutubeVideoDetailsResponse429
from ...models.youtube_video_details_response_500 import YoutubeVideoDetailsResponse500
from ...models.youtube_video_details_response_503 import YoutubeVideoDetailsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: YoutubeVideoDetailsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/youtube/video-details",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    YoutubeVideoDetailsResponse200
    | YoutubeVideoDetailsResponse400
    | YoutubeVideoDetailsResponse401
    | YoutubeVideoDetailsResponse402
    | YoutubeVideoDetailsResponse403
    | YoutubeVideoDetailsResponse404
    | YoutubeVideoDetailsResponse422
    | YoutubeVideoDetailsResponse429
    | YoutubeVideoDetailsResponse500
    | YoutubeVideoDetailsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = YoutubeVideoDetailsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = YoutubeVideoDetailsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = YoutubeVideoDetailsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = YoutubeVideoDetailsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = YoutubeVideoDetailsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = YoutubeVideoDetailsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = YoutubeVideoDetailsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = YoutubeVideoDetailsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = YoutubeVideoDetailsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = YoutubeVideoDetailsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    YoutubeVideoDetailsResponse200
    | YoutubeVideoDetailsResponse400
    | YoutubeVideoDetailsResponse401
    | YoutubeVideoDetailsResponse402
    | YoutubeVideoDetailsResponse403
    | YoutubeVideoDetailsResponse404
    | YoutubeVideoDetailsResponse422
    | YoutubeVideoDetailsResponse429
    | YoutubeVideoDetailsResponse500
    | YoutubeVideoDetailsResponse503
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
    body: YoutubeVideoDetailsBody,
) -> Response[
    YoutubeVideoDetailsResponse200
    | YoutubeVideoDetailsResponse400
    | YoutubeVideoDetailsResponse401
    | YoutubeVideoDetailsResponse402
    | YoutubeVideoDetailsResponse403
    | YoutubeVideoDetailsResponse404
    | YoutubeVideoDetailsResponse422
    | YoutubeVideoDetailsResponse429
    | YoutubeVideoDetailsResponse500
    | YoutubeVideoDetailsResponse503
]:
    r"""Fetch YouTube video details

     Fetches detailed metadata for a YouTube video including title, view count, like count, channel
    information, chapters, key moments, and available transcript languages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (YoutubeVideoDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[YoutubeVideoDetailsResponse200 | YoutubeVideoDetailsResponse400 | YoutubeVideoDetailsResponse401 | YoutubeVideoDetailsResponse402 | YoutubeVideoDetailsResponse403 | YoutubeVideoDetailsResponse404 | YoutubeVideoDetailsResponse422 | YoutubeVideoDetailsResponse429 | YoutubeVideoDetailsResponse500 | YoutubeVideoDetailsResponse503]
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
    body: YoutubeVideoDetailsBody,
) -> (
    YoutubeVideoDetailsResponse200
    | YoutubeVideoDetailsResponse400
    | YoutubeVideoDetailsResponse401
    | YoutubeVideoDetailsResponse402
    | YoutubeVideoDetailsResponse403
    | YoutubeVideoDetailsResponse404
    | YoutubeVideoDetailsResponse422
    | YoutubeVideoDetailsResponse429
    | YoutubeVideoDetailsResponse500
    | YoutubeVideoDetailsResponse503
    | None
):
    r"""Fetch YouTube video details

     Fetches detailed metadata for a YouTube video including title, view count, like count, channel
    information, chapters, key moments, and available transcript languages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (YoutubeVideoDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        YoutubeVideoDetailsResponse200 | YoutubeVideoDetailsResponse400 | YoutubeVideoDetailsResponse401 | YoutubeVideoDetailsResponse402 | YoutubeVideoDetailsResponse403 | YoutubeVideoDetailsResponse404 | YoutubeVideoDetailsResponse422 | YoutubeVideoDetailsResponse429 | YoutubeVideoDetailsResponse500 | YoutubeVideoDetailsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: YoutubeVideoDetailsBody,
) -> Response[
    YoutubeVideoDetailsResponse200
    | YoutubeVideoDetailsResponse400
    | YoutubeVideoDetailsResponse401
    | YoutubeVideoDetailsResponse402
    | YoutubeVideoDetailsResponse403
    | YoutubeVideoDetailsResponse404
    | YoutubeVideoDetailsResponse422
    | YoutubeVideoDetailsResponse429
    | YoutubeVideoDetailsResponse500
    | YoutubeVideoDetailsResponse503
]:
    r"""Fetch YouTube video details

     Fetches detailed metadata for a YouTube video including title, view count, like count, channel
    information, chapters, key moments, and available transcript languages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (YoutubeVideoDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[YoutubeVideoDetailsResponse200 | YoutubeVideoDetailsResponse400 | YoutubeVideoDetailsResponse401 | YoutubeVideoDetailsResponse402 | YoutubeVideoDetailsResponse403 | YoutubeVideoDetailsResponse404 | YoutubeVideoDetailsResponse422 | YoutubeVideoDetailsResponse429 | YoutubeVideoDetailsResponse500 | YoutubeVideoDetailsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: YoutubeVideoDetailsBody,
) -> (
    YoutubeVideoDetailsResponse200
    | YoutubeVideoDetailsResponse400
    | YoutubeVideoDetailsResponse401
    | YoutubeVideoDetailsResponse402
    | YoutubeVideoDetailsResponse403
    | YoutubeVideoDetailsResponse404
    | YoutubeVideoDetailsResponse422
    | YoutubeVideoDetailsResponse429
    | YoutubeVideoDetailsResponse500
    | YoutubeVideoDetailsResponse503
    | None
):
    r"""Fetch YouTube video details

     Fetches detailed metadata for a YouTube video including title, view count, like count, channel
    information, chapters, key moments, and available transcript languages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (YoutubeVideoDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        YoutubeVideoDetailsResponse200 | YoutubeVideoDetailsResponse400 | YoutubeVideoDetailsResponse401 | YoutubeVideoDetailsResponse402 | YoutubeVideoDetailsResponse403 | YoutubeVideoDetailsResponse404 | YoutubeVideoDetailsResponse422 | YoutubeVideoDetailsResponse429 | YoutubeVideoDetailsResponse500 | YoutubeVideoDetailsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
