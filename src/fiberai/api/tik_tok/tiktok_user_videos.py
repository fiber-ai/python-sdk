from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tiktok_user_videos_body import TiktokUserVideosBody
from ...models.tiktok_user_videos_response_200 import TiktokUserVideosResponse200
from ...models.tiktok_user_videos_response_400 import TiktokUserVideosResponse400
from ...models.tiktok_user_videos_response_401 import TiktokUserVideosResponse401
from ...models.tiktok_user_videos_response_402 import TiktokUserVideosResponse402
from ...models.tiktok_user_videos_response_403 import TiktokUserVideosResponse403
from ...models.tiktok_user_videos_response_404 import TiktokUserVideosResponse404
from ...models.tiktok_user_videos_response_422 import TiktokUserVideosResponse422
from ...models.tiktok_user_videos_response_429 import TiktokUserVideosResponse429
from ...models.tiktok_user_videos_response_500 import TiktokUserVideosResponse500
from ...models.tiktok_user_videos_response_503 import TiktokUserVideosResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TiktokUserVideosBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tiktok/user-videos",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TiktokUserVideosResponse200
    | TiktokUserVideosResponse400
    | TiktokUserVideosResponse401
    | TiktokUserVideosResponse402
    | TiktokUserVideosResponse403
    | TiktokUserVideosResponse404
    | TiktokUserVideosResponse422
    | TiktokUserVideosResponse429
    | TiktokUserVideosResponse500
    | TiktokUserVideosResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TiktokUserVideosResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TiktokUserVideosResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TiktokUserVideosResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TiktokUserVideosResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TiktokUserVideosResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TiktokUserVideosResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = TiktokUserVideosResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = TiktokUserVideosResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TiktokUserVideosResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TiktokUserVideosResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TiktokUserVideosResponse200
    | TiktokUserVideosResponse400
    | TiktokUserVideosResponse401
    | TiktokUserVideosResponse402
    | TiktokUserVideosResponse403
    | TiktokUserVideosResponse404
    | TiktokUserVideosResponse422
    | TiktokUserVideosResponse429
    | TiktokUserVideosResponse500
    | TiktokUserVideosResponse503
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
    body: TiktokUserVideosBody,
) -> Response[
    TiktokUserVideosResponse200
    | TiktokUserVideosResponse400
    | TiktokUserVideosResponse401
    | TiktokUserVideosResponse402
    | TiktokUserVideosResponse403
    | TiktokUserVideosResponse404
    | TiktokUserVideosResponse422
    | TiktokUserVideosResponse429
    | TiktokUserVideosResponse500
    | TiktokUserVideosResponse503
]:
    """Fetch TikTok user videos

     Fetches the latest videos for a TikTok user. Returns a paginated list of videos with engagement
    metrics. Use the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokUserVideosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokUserVideosResponse200 | TiktokUserVideosResponse400 | TiktokUserVideosResponse401 | TiktokUserVideosResponse402 | TiktokUserVideosResponse403 | TiktokUserVideosResponse404 | TiktokUserVideosResponse422 | TiktokUserVideosResponse429 | TiktokUserVideosResponse500 | TiktokUserVideosResponse503]
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
    body: TiktokUserVideosBody,
) -> (
    TiktokUserVideosResponse200
    | TiktokUserVideosResponse400
    | TiktokUserVideosResponse401
    | TiktokUserVideosResponse402
    | TiktokUserVideosResponse403
    | TiktokUserVideosResponse404
    | TiktokUserVideosResponse422
    | TiktokUserVideosResponse429
    | TiktokUserVideosResponse500
    | TiktokUserVideosResponse503
    | None
):
    """Fetch TikTok user videos

     Fetches the latest videos for a TikTok user. Returns a paginated list of videos with engagement
    metrics. Use the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokUserVideosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokUserVideosResponse200 | TiktokUserVideosResponse400 | TiktokUserVideosResponse401 | TiktokUserVideosResponse402 | TiktokUserVideosResponse403 | TiktokUserVideosResponse404 | TiktokUserVideosResponse422 | TiktokUserVideosResponse429 | TiktokUserVideosResponse500 | TiktokUserVideosResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokUserVideosBody,
) -> Response[
    TiktokUserVideosResponse200
    | TiktokUserVideosResponse400
    | TiktokUserVideosResponse401
    | TiktokUserVideosResponse402
    | TiktokUserVideosResponse403
    | TiktokUserVideosResponse404
    | TiktokUserVideosResponse422
    | TiktokUserVideosResponse429
    | TiktokUserVideosResponse500
    | TiktokUserVideosResponse503
]:
    """Fetch TikTok user videos

     Fetches the latest videos for a TikTok user. Returns a paginated list of videos with engagement
    metrics. Use the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokUserVideosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokUserVideosResponse200 | TiktokUserVideosResponse400 | TiktokUserVideosResponse401 | TiktokUserVideosResponse402 | TiktokUserVideosResponse403 | TiktokUserVideosResponse404 | TiktokUserVideosResponse422 | TiktokUserVideosResponse429 | TiktokUserVideosResponse500 | TiktokUserVideosResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokUserVideosBody,
) -> (
    TiktokUserVideosResponse200
    | TiktokUserVideosResponse400
    | TiktokUserVideosResponse401
    | TiktokUserVideosResponse402
    | TiktokUserVideosResponse403
    | TiktokUserVideosResponse404
    | TiktokUserVideosResponse422
    | TiktokUserVideosResponse429
    | TiktokUserVideosResponse500
    | TiktokUserVideosResponse503
    | None
):
    """Fetch TikTok user videos

     Fetches the latest videos for a TikTok user. Returns a paginated list of videos with engagement
    metrics. Use the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokUserVideosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokUserVideosResponse200 | TiktokUserVideosResponse400 | TiktokUserVideosResponse401 | TiktokUserVideosResponse402 | TiktokUserVideosResponse403 | TiktokUserVideosResponse404 | TiktokUserVideosResponse422 | TiktokUserVideosResponse429 | TiktokUserVideosResponse500 | TiktokUserVideosResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
