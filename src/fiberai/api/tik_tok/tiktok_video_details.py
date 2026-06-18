from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tiktok_video_details_body import TiktokVideoDetailsBody
from ...models.tiktok_video_details_response_200 import TiktokVideoDetailsResponse200
from ...models.tiktok_video_details_response_400 import TiktokVideoDetailsResponse400
from ...models.tiktok_video_details_response_401 import TiktokVideoDetailsResponse401
from ...models.tiktok_video_details_response_402 import TiktokVideoDetailsResponse402
from ...models.tiktok_video_details_response_403 import TiktokVideoDetailsResponse403
from ...models.tiktok_video_details_response_404 import TiktokVideoDetailsResponse404
from ...models.tiktok_video_details_response_422 import TiktokVideoDetailsResponse422
from ...models.tiktok_video_details_response_429 import TiktokVideoDetailsResponse429
from ...models.tiktok_video_details_response_500 import TiktokVideoDetailsResponse500
from ...models.tiktok_video_details_response_503 import TiktokVideoDetailsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TiktokVideoDetailsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tiktok/video-details",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TiktokVideoDetailsResponse200
    | TiktokVideoDetailsResponse400
    | TiktokVideoDetailsResponse401
    | TiktokVideoDetailsResponse402
    | TiktokVideoDetailsResponse403
    | TiktokVideoDetailsResponse404
    | TiktokVideoDetailsResponse422
    | TiktokVideoDetailsResponse429
    | TiktokVideoDetailsResponse500
    | TiktokVideoDetailsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TiktokVideoDetailsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TiktokVideoDetailsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TiktokVideoDetailsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TiktokVideoDetailsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TiktokVideoDetailsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TiktokVideoDetailsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = TiktokVideoDetailsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = TiktokVideoDetailsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TiktokVideoDetailsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TiktokVideoDetailsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TiktokVideoDetailsResponse200
    | TiktokVideoDetailsResponse400
    | TiktokVideoDetailsResponse401
    | TiktokVideoDetailsResponse402
    | TiktokVideoDetailsResponse403
    | TiktokVideoDetailsResponse404
    | TiktokVideoDetailsResponse422
    | TiktokVideoDetailsResponse429
    | TiktokVideoDetailsResponse500
    | TiktokVideoDetailsResponse503
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
    body: TiktokVideoDetailsBody,
) -> Response[
    TiktokVideoDetailsResponse200
    | TiktokVideoDetailsResponse400
    | TiktokVideoDetailsResponse401
    | TiktokVideoDetailsResponse402
    | TiktokVideoDetailsResponse403
    | TiktokVideoDetailsResponse404
    | TiktokVideoDetailsResponse422
    | TiktokVideoDetailsResponse429
    | TiktokVideoDetailsResponse500
    | TiktokVideoDetailsResponse503
]:
    r"""Fetch TikTok video details

     Fetches detailed information about a TikTok video including engagement metrics and video metadata.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokVideoDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokVideoDetailsResponse200 | TiktokVideoDetailsResponse400 | TiktokVideoDetailsResponse401 | TiktokVideoDetailsResponse402 | TiktokVideoDetailsResponse403 | TiktokVideoDetailsResponse404 | TiktokVideoDetailsResponse422 | TiktokVideoDetailsResponse429 | TiktokVideoDetailsResponse500 | TiktokVideoDetailsResponse503]
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
    body: TiktokVideoDetailsBody,
) -> (
    TiktokVideoDetailsResponse200
    | TiktokVideoDetailsResponse400
    | TiktokVideoDetailsResponse401
    | TiktokVideoDetailsResponse402
    | TiktokVideoDetailsResponse403
    | TiktokVideoDetailsResponse404
    | TiktokVideoDetailsResponse422
    | TiktokVideoDetailsResponse429
    | TiktokVideoDetailsResponse500
    | TiktokVideoDetailsResponse503
    | None
):
    r"""Fetch TikTok video details

     Fetches detailed information about a TikTok video including engagement metrics and video metadata.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokVideoDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokVideoDetailsResponse200 | TiktokVideoDetailsResponse400 | TiktokVideoDetailsResponse401 | TiktokVideoDetailsResponse402 | TiktokVideoDetailsResponse403 | TiktokVideoDetailsResponse404 | TiktokVideoDetailsResponse422 | TiktokVideoDetailsResponse429 | TiktokVideoDetailsResponse500 | TiktokVideoDetailsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokVideoDetailsBody,
) -> Response[
    TiktokVideoDetailsResponse200
    | TiktokVideoDetailsResponse400
    | TiktokVideoDetailsResponse401
    | TiktokVideoDetailsResponse402
    | TiktokVideoDetailsResponse403
    | TiktokVideoDetailsResponse404
    | TiktokVideoDetailsResponse422
    | TiktokVideoDetailsResponse429
    | TiktokVideoDetailsResponse500
    | TiktokVideoDetailsResponse503
]:
    r"""Fetch TikTok video details

     Fetches detailed information about a TikTok video including engagement metrics and video metadata.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokVideoDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokVideoDetailsResponse200 | TiktokVideoDetailsResponse400 | TiktokVideoDetailsResponse401 | TiktokVideoDetailsResponse402 | TiktokVideoDetailsResponse403 | TiktokVideoDetailsResponse404 | TiktokVideoDetailsResponse422 | TiktokVideoDetailsResponse429 | TiktokVideoDetailsResponse500 | TiktokVideoDetailsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokVideoDetailsBody,
) -> (
    TiktokVideoDetailsResponse200
    | TiktokVideoDetailsResponse400
    | TiktokVideoDetailsResponse401
    | TiktokVideoDetailsResponse402
    | TiktokVideoDetailsResponse403
    | TiktokVideoDetailsResponse404
    | TiktokVideoDetailsResponse422
    | TiktokVideoDetailsResponse429
    | TiktokVideoDetailsResponse500
    | TiktokVideoDetailsResponse503
    | None
):
    r"""Fetch TikTok video details

     Fetches detailed information about a TikTok video including engagement metrics and video metadata.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokVideoDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokVideoDetailsResponse200 | TiktokVideoDetailsResponse400 | TiktokVideoDetailsResponse401 | TiktokVideoDetailsResponse402 | TiktokVideoDetailsResponse403 | TiktokVideoDetailsResponse404 | TiktokVideoDetailsResponse422 | TiktokVideoDetailsResponse429 | TiktokVideoDetailsResponse500 | TiktokVideoDetailsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
