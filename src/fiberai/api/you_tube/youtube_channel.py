from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.youtube_channel_body import YoutubeChannelBody
from ...models.youtube_channel_response_200 import YoutubeChannelResponse200
from ...models.youtube_channel_response_400 import YoutubeChannelResponse400
from ...models.youtube_channel_response_401 import YoutubeChannelResponse401
from ...models.youtube_channel_response_402 import YoutubeChannelResponse402
from ...models.youtube_channel_response_403 import YoutubeChannelResponse403
from ...models.youtube_channel_response_404 import YoutubeChannelResponse404
from ...models.youtube_channel_response_422 import YoutubeChannelResponse422
from ...models.youtube_channel_response_429 import YoutubeChannelResponse429
from ...models.youtube_channel_response_500 import YoutubeChannelResponse500
from ...models.youtube_channel_response_503 import YoutubeChannelResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: YoutubeChannelBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/youtube/channel",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    YoutubeChannelResponse200
    | YoutubeChannelResponse400
    | YoutubeChannelResponse401
    | YoutubeChannelResponse402
    | YoutubeChannelResponse403
    | YoutubeChannelResponse404
    | YoutubeChannelResponse422
    | YoutubeChannelResponse429
    | YoutubeChannelResponse500
    | YoutubeChannelResponse503
    | None
):
    if response.status_code == 200:
        response_200 = YoutubeChannelResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = YoutubeChannelResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = YoutubeChannelResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = YoutubeChannelResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = YoutubeChannelResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = YoutubeChannelResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = YoutubeChannelResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = YoutubeChannelResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = YoutubeChannelResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = YoutubeChannelResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    YoutubeChannelResponse200
    | YoutubeChannelResponse400
    | YoutubeChannelResponse401
    | YoutubeChannelResponse402
    | YoutubeChannelResponse403
    | YoutubeChannelResponse404
    | YoutubeChannelResponse422
    | YoutubeChannelResponse429
    | YoutubeChannelResponse500
    | YoutubeChannelResponse503
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
    body: YoutubeChannelBody,
) -> Response[
    YoutubeChannelResponse200
    | YoutubeChannelResponse400
    | YoutubeChannelResponse401
    | YoutubeChannelResponse402
    | YoutubeChannelResponse403
    | YoutubeChannelResponse404
    | YoutubeChannelResponse422
    | YoutubeChannelResponse429
    | YoutubeChannelResponse500
    | YoutubeChannelResponse503
]:
    """Fetch YouTube channel info and videos

     Fetches metadata and videos for a YouTube channel. Returns subscriber count, description, video
    count, total views, and a paginated list of videos. Use `nextPageToken` from the response to
    paginate through additional video pages.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YoutubeChannelBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[YoutubeChannelResponse200 | YoutubeChannelResponse400 | YoutubeChannelResponse401 | YoutubeChannelResponse402 | YoutubeChannelResponse403 | YoutubeChannelResponse404 | YoutubeChannelResponse422 | YoutubeChannelResponse429 | YoutubeChannelResponse500 | YoutubeChannelResponse503]
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
    body: YoutubeChannelBody,
) -> (
    YoutubeChannelResponse200
    | YoutubeChannelResponse400
    | YoutubeChannelResponse401
    | YoutubeChannelResponse402
    | YoutubeChannelResponse403
    | YoutubeChannelResponse404
    | YoutubeChannelResponse422
    | YoutubeChannelResponse429
    | YoutubeChannelResponse500
    | YoutubeChannelResponse503
    | None
):
    """Fetch YouTube channel info and videos

     Fetches metadata and videos for a YouTube channel. Returns subscriber count, description, video
    count, total views, and a paginated list of videos. Use `nextPageToken` from the response to
    paginate through additional video pages.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YoutubeChannelBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        YoutubeChannelResponse200 | YoutubeChannelResponse400 | YoutubeChannelResponse401 | YoutubeChannelResponse402 | YoutubeChannelResponse403 | YoutubeChannelResponse404 | YoutubeChannelResponse422 | YoutubeChannelResponse429 | YoutubeChannelResponse500 | YoutubeChannelResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: YoutubeChannelBody,
) -> Response[
    YoutubeChannelResponse200
    | YoutubeChannelResponse400
    | YoutubeChannelResponse401
    | YoutubeChannelResponse402
    | YoutubeChannelResponse403
    | YoutubeChannelResponse404
    | YoutubeChannelResponse422
    | YoutubeChannelResponse429
    | YoutubeChannelResponse500
    | YoutubeChannelResponse503
]:
    """Fetch YouTube channel info and videos

     Fetches metadata and videos for a YouTube channel. Returns subscriber count, description, video
    count, total views, and a paginated list of videos. Use `nextPageToken` from the response to
    paginate through additional video pages.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YoutubeChannelBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[YoutubeChannelResponse200 | YoutubeChannelResponse400 | YoutubeChannelResponse401 | YoutubeChannelResponse402 | YoutubeChannelResponse403 | YoutubeChannelResponse404 | YoutubeChannelResponse422 | YoutubeChannelResponse429 | YoutubeChannelResponse500 | YoutubeChannelResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: YoutubeChannelBody,
) -> (
    YoutubeChannelResponse200
    | YoutubeChannelResponse400
    | YoutubeChannelResponse401
    | YoutubeChannelResponse402
    | YoutubeChannelResponse403
    | YoutubeChannelResponse404
    | YoutubeChannelResponse422
    | YoutubeChannelResponse429
    | YoutubeChannelResponse500
    | YoutubeChannelResponse503
    | None
):
    """Fetch YouTube channel info and videos

     Fetches metadata and videos for a YouTube channel. Returns subscriber count, description, video
    count, total views, and a paginated list of videos. Use `nextPageToken` from the response to
    paginate through additional video pages.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YoutubeChannelBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        YoutubeChannelResponse200 | YoutubeChannelResponse400 | YoutubeChannelResponse401 | YoutubeChannelResponse402 | YoutubeChannelResponse403 | YoutubeChannelResponse404 | YoutubeChannelResponse422 | YoutubeChannelResponse429 | YoutubeChannelResponse500 | YoutubeChannelResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
