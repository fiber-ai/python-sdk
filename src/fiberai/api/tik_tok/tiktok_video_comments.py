from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tiktok_video_comments_body import TiktokVideoCommentsBody
from ...models.tiktok_video_comments_response_200 import TiktokVideoCommentsResponse200
from ...models.tiktok_video_comments_response_400 import TiktokVideoCommentsResponse400
from ...models.tiktok_video_comments_response_401 import TiktokVideoCommentsResponse401
from ...models.tiktok_video_comments_response_402 import TiktokVideoCommentsResponse402
from ...models.tiktok_video_comments_response_403 import TiktokVideoCommentsResponse403
from ...models.tiktok_video_comments_response_404 import TiktokVideoCommentsResponse404
from ...models.tiktok_video_comments_response_422 import TiktokVideoCommentsResponse422
from ...models.tiktok_video_comments_response_429 import TiktokVideoCommentsResponse429
from ...models.tiktok_video_comments_response_500 import TiktokVideoCommentsResponse500
from ...models.tiktok_video_comments_response_503 import TiktokVideoCommentsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TiktokVideoCommentsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tiktok/video-comments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TiktokVideoCommentsResponse200
    | TiktokVideoCommentsResponse400
    | TiktokVideoCommentsResponse401
    | TiktokVideoCommentsResponse402
    | TiktokVideoCommentsResponse403
    | TiktokVideoCommentsResponse404
    | TiktokVideoCommentsResponse422
    | TiktokVideoCommentsResponse429
    | TiktokVideoCommentsResponse500
    | TiktokVideoCommentsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TiktokVideoCommentsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TiktokVideoCommentsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TiktokVideoCommentsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TiktokVideoCommentsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TiktokVideoCommentsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TiktokVideoCommentsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = TiktokVideoCommentsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = TiktokVideoCommentsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TiktokVideoCommentsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TiktokVideoCommentsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TiktokVideoCommentsResponse200
    | TiktokVideoCommentsResponse400
    | TiktokVideoCommentsResponse401
    | TiktokVideoCommentsResponse402
    | TiktokVideoCommentsResponse403
    | TiktokVideoCommentsResponse404
    | TiktokVideoCommentsResponse422
    | TiktokVideoCommentsResponse429
    | TiktokVideoCommentsResponse500
    | TiktokVideoCommentsResponse503
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
    body: TiktokVideoCommentsBody,
) -> Response[
    TiktokVideoCommentsResponse200
    | TiktokVideoCommentsResponse400
    | TiktokVideoCommentsResponse401
    | TiktokVideoCommentsResponse402
    | TiktokVideoCommentsResponse403
    | TiktokVideoCommentsResponse404
    | TiktokVideoCommentsResponse422
    | TiktokVideoCommentsResponse429
    | TiktokVideoCommentsResponse500
    | TiktokVideoCommentsResponse503
]:
    """Fetch TikTok video comments

     Fetches comments for a TikTok video. Returns a paginated list of comments. Use the `nextPageToken`
    field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokVideoCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokVideoCommentsResponse200 | TiktokVideoCommentsResponse400 | TiktokVideoCommentsResponse401 | TiktokVideoCommentsResponse402 | TiktokVideoCommentsResponse403 | TiktokVideoCommentsResponse404 | TiktokVideoCommentsResponse422 | TiktokVideoCommentsResponse429 | TiktokVideoCommentsResponse500 | TiktokVideoCommentsResponse503]
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
    body: TiktokVideoCommentsBody,
) -> (
    TiktokVideoCommentsResponse200
    | TiktokVideoCommentsResponse400
    | TiktokVideoCommentsResponse401
    | TiktokVideoCommentsResponse402
    | TiktokVideoCommentsResponse403
    | TiktokVideoCommentsResponse404
    | TiktokVideoCommentsResponse422
    | TiktokVideoCommentsResponse429
    | TiktokVideoCommentsResponse500
    | TiktokVideoCommentsResponse503
    | None
):
    """Fetch TikTok video comments

     Fetches comments for a TikTok video. Returns a paginated list of comments. Use the `nextPageToken`
    field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokVideoCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokVideoCommentsResponse200 | TiktokVideoCommentsResponse400 | TiktokVideoCommentsResponse401 | TiktokVideoCommentsResponse402 | TiktokVideoCommentsResponse403 | TiktokVideoCommentsResponse404 | TiktokVideoCommentsResponse422 | TiktokVideoCommentsResponse429 | TiktokVideoCommentsResponse500 | TiktokVideoCommentsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokVideoCommentsBody,
) -> Response[
    TiktokVideoCommentsResponse200
    | TiktokVideoCommentsResponse400
    | TiktokVideoCommentsResponse401
    | TiktokVideoCommentsResponse402
    | TiktokVideoCommentsResponse403
    | TiktokVideoCommentsResponse404
    | TiktokVideoCommentsResponse422
    | TiktokVideoCommentsResponse429
    | TiktokVideoCommentsResponse500
    | TiktokVideoCommentsResponse503
]:
    """Fetch TikTok video comments

     Fetches comments for a TikTok video. Returns a paginated list of comments. Use the `nextPageToken`
    field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokVideoCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokVideoCommentsResponse200 | TiktokVideoCommentsResponse400 | TiktokVideoCommentsResponse401 | TiktokVideoCommentsResponse402 | TiktokVideoCommentsResponse403 | TiktokVideoCommentsResponse404 | TiktokVideoCommentsResponse422 | TiktokVideoCommentsResponse429 | TiktokVideoCommentsResponse500 | TiktokVideoCommentsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokVideoCommentsBody,
) -> (
    TiktokVideoCommentsResponse200
    | TiktokVideoCommentsResponse400
    | TiktokVideoCommentsResponse401
    | TiktokVideoCommentsResponse402
    | TiktokVideoCommentsResponse403
    | TiktokVideoCommentsResponse404
    | TiktokVideoCommentsResponse422
    | TiktokVideoCommentsResponse429
    | TiktokVideoCommentsResponse500
    | TiktokVideoCommentsResponse503
    | None
):
    """Fetch TikTok video comments

     Fetches comments for a TikTok video. Returns a paginated list of comments. Use the `nextPageToken`
    field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokVideoCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokVideoCommentsResponse200 | TiktokVideoCommentsResponse400 | TiktokVideoCommentsResponse401 | TiktokVideoCommentsResponse402 | TiktokVideoCommentsResponse403 | TiktokVideoCommentsResponse404 | TiktokVideoCommentsResponse422 | TiktokVideoCommentsResponse429 | TiktokVideoCommentsResponse500 | TiktokVideoCommentsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
