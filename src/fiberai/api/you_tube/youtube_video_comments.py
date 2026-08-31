from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.youtube_video_comments_body import YoutubeVideoCommentsBody
from ...models.youtube_video_comments_response_200 import YoutubeVideoCommentsResponse200
from ...models.youtube_video_comments_response_400 import YoutubeVideoCommentsResponse400
from ...models.youtube_video_comments_response_401 import YoutubeVideoCommentsResponse401
from ...models.youtube_video_comments_response_402 import YoutubeVideoCommentsResponse402
from ...models.youtube_video_comments_response_403 import YoutubeVideoCommentsResponse403
from ...models.youtube_video_comments_response_404 import YoutubeVideoCommentsResponse404
from ...models.youtube_video_comments_response_422 import YoutubeVideoCommentsResponse422
from ...models.youtube_video_comments_response_429 import YoutubeVideoCommentsResponse429
from ...models.youtube_video_comments_response_500 import YoutubeVideoCommentsResponse500
from ...models.youtube_video_comments_response_503 import YoutubeVideoCommentsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: YoutubeVideoCommentsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/youtube/video-comments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    YoutubeVideoCommentsResponse200
    | YoutubeVideoCommentsResponse400
    | YoutubeVideoCommentsResponse401
    | YoutubeVideoCommentsResponse402
    | YoutubeVideoCommentsResponse403
    | YoutubeVideoCommentsResponse404
    | YoutubeVideoCommentsResponse422
    | YoutubeVideoCommentsResponse429
    | YoutubeVideoCommentsResponse500
    | YoutubeVideoCommentsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = YoutubeVideoCommentsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = YoutubeVideoCommentsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = YoutubeVideoCommentsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = YoutubeVideoCommentsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = YoutubeVideoCommentsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = YoutubeVideoCommentsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = YoutubeVideoCommentsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = YoutubeVideoCommentsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = YoutubeVideoCommentsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = YoutubeVideoCommentsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    YoutubeVideoCommentsResponse200
    | YoutubeVideoCommentsResponse400
    | YoutubeVideoCommentsResponse401
    | YoutubeVideoCommentsResponse402
    | YoutubeVideoCommentsResponse403
    | YoutubeVideoCommentsResponse404
    | YoutubeVideoCommentsResponse422
    | YoutubeVideoCommentsResponse429
    | YoutubeVideoCommentsResponse500
    | YoutubeVideoCommentsResponse503
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
    body: YoutubeVideoCommentsBody,
) -> Response[
    YoutubeVideoCommentsResponse200
    | YoutubeVideoCommentsResponse400
    | YoutubeVideoCommentsResponse401
    | YoutubeVideoCommentsResponse402
    | YoutubeVideoCommentsResponse403
    | YoutubeVideoCommentsResponse404
    | YoutubeVideoCommentsResponse422
    | YoutubeVideoCommentsResponse429
    | YoutubeVideoCommentsResponse500
    | YoutubeVideoCommentsResponse503
]:
    """Fetch YouTube video comments

     Fetches a page of comments for a YouTube video. Returns comment text, author, like count, and reply
    count. Use `nextPageToken` from the response to paginate through additional pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YoutubeVideoCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[YoutubeVideoCommentsResponse200 | YoutubeVideoCommentsResponse400 | YoutubeVideoCommentsResponse401 | YoutubeVideoCommentsResponse402 | YoutubeVideoCommentsResponse403 | YoutubeVideoCommentsResponse404 | YoutubeVideoCommentsResponse422 | YoutubeVideoCommentsResponse429 | YoutubeVideoCommentsResponse500 | YoutubeVideoCommentsResponse503]
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
    body: YoutubeVideoCommentsBody,
) -> (
    YoutubeVideoCommentsResponse200
    | YoutubeVideoCommentsResponse400
    | YoutubeVideoCommentsResponse401
    | YoutubeVideoCommentsResponse402
    | YoutubeVideoCommentsResponse403
    | YoutubeVideoCommentsResponse404
    | YoutubeVideoCommentsResponse422
    | YoutubeVideoCommentsResponse429
    | YoutubeVideoCommentsResponse500
    | YoutubeVideoCommentsResponse503
    | None
):
    """Fetch YouTube video comments

     Fetches a page of comments for a YouTube video. Returns comment text, author, like count, and reply
    count. Use `nextPageToken` from the response to paginate through additional pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YoutubeVideoCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        YoutubeVideoCommentsResponse200 | YoutubeVideoCommentsResponse400 | YoutubeVideoCommentsResponse401 | YoutubeVideoCommentsResponse402 | YoutubeVideoCommentsResponse403 | YoutubeVideoCommentsResponse404 | YoutubeVideoCommentsResponse422 | YoutubeVideoCommentsResponse429 | YoutubeVideoCommentsResponse500 | YoutubeVideoCommentsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: YoutubeVideoCommentsBody,
) -> Response[
    YoutubeVideoCommentsResponse200
    | YoutubeVideoCommentsResponse400
    | YoutubeVideoCommentsResponse401
    | YoutubeVideoCommentsResponse402
    | YoutubeVideoCommentsResponse403
    | YoutubeVideoCommentsResponse404
    | YoutubeVideoCommentsResponse422
    | YoutubeVideoCommentsResponse429
    | YoutubeVideoCommentsResponse500
    | YoutubeVideoCommentsResponse503
]:
    """Fetch YouTube video comments

     Fetches a page of comments for a YouTube video. Returns comment text, author, like count, and reply
    count. Use `nextPageToken` from the response to paginate through additional pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YoutubeVideoCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[YoutubeVideoCommentsResponse200 | YoutubeVideoCommentsResponse400 | YoutubeVideoCommentsResponse401 | YoutubeVideoCommentsResponse402 | YoutubeVideoCommentsResponse403 | YoutubeVideoCommentsResponse404 | YoutubeVideoCommentsResponse422 | YoutubeVideoCommentsResponse429 | YoutubeVideoCommentsResponse500 | YoutubeVideoCommentsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: YoutubeVideoCommentsBody,
) -> (
    YoutubeVideoCommentsResponse200
    | YoutubeVideoCommentsResponse400
    | YoutubeVideoCommentsResponse401
    | YoutubeVideoCommentsResponse402
    | YoutubeVideoCommentsResponse403
    | YoutubeVideoCommentsResponse404
    | YoutubeVideoCommentsResponse422
    | YoutubeVideoCommentsResponse429
    | YoutubeVideoCommentsResponse500
    | YoutubeVideoCommentsResponse503
    | None
):
    """Fetch YouTube video comments

     Fetches a page of comments for a YouTube video. Returns comment text, author, like count, and reply
    count. Use `nextPageToken` from the response to paginate through additional pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YoutubeVideoCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        YoutubeVideoCommentsResponse200 | YoutubeVideoCommentsResponse400 | YoutubeVideoCommentsResponse401 | YoutubeVideoCommentsResponse402 | YoutubeVideoCommentsResponse403 | YoutubeVideoCommentsResponse404 | YoutubeVideoCommentsResponse422 | YoutubeVideoCommentsResponse429 | YoutubeVideoCommentsResponse500 | YoutubeVideoCommentsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
