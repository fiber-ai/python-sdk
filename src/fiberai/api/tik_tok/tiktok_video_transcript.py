from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tiktok_video_transcript_body import TiktokVideoTranscriptBody
from ...models.tiktok_video_transcript_response_200 import TiktokVideoTranscriptResponse200
from ...models.tiktok_video_transcript_response_400 import TiktokVideoTranscriptResponse400
from ...models.tiktok_video_transcript_response_401 import TiktokVideoTranscriptResponse401
from ...models.tiktok_video_transcript_response_402 import TiktokVideoTranscriptResponse402
from ...models.tiktok_video_transcript_response_403 import TiktokVideoTranscriptResponse403
from ...models.tiktok_video_transcript_response_404 import TiktokVideoTranscriptResponse404
from ...models.tiktok_video_transcript_response_429 import TiktokVideoTranscriptResponse429
from ...models.tiktok_video_transcript_response_500 import TiktokVideoTranscriptResponse500
from ...models.tiktok_video_transcript_response_503 import TiktokVideoTranscriptResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TiktokVideoTranscriptBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tiktok/video-transcript",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TiktokVideoTranscriptResponse200
    | TiktokVideoTranscriptResponse400
    | TiktokVideoTranscriptResponse401
    | TiktokVideoTranscriptResponse402
    | TiktokVideoTranscriptResponse403
    | TiktokVideoTranscriptResponse404
    | TiktokVideoTranscriptResponse429
    | TiktokVideoTranscriptResponse500
    | TiktokVideoTranscriptResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TiktokVideoTranscriptResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TiktokVideoTranscriptResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TiktokVideoTranscriptResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TiktokVideoTranscriptResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TiktokVideoTranscriptResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TiktokVideoTranscriptResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TiktokVideoTranscriptResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TiktokVideoTranscriptResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TiktokVideoTranscriptResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TiktokVideoTranscriptResponse200
    | TiktokVideoTranscriptResponse400
    | TiktokVideoTranscriptResponse401
    | TiktokVideoTranscriptResponse402
    | TiktokVideoTranscriptResponse403
    | TiktokVideoTranscriptResponse404
    | TiktokVideoTranscriptResponse429
    | TiktokVideoTranscriptResponse500
    | TiktokVideoTranscriptResponse503
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
    body: TiktokVideoTranscriptBody,
) -> Response[
    TiktokVideoTranscriptResponse200
    | TiktokVideoTranscriptResponse400
    | TiktokVideoTranscriptResponse401
    | TiktokVideoTranscriptResponse402
    | TiktokVideoTranscriptResponse403
    | TiktokVideoTranscriptResponse404
    | TiktokVideoTranscriptResponse429
    | TiktokVideoTranscriptResponse500
    | TiktokVideoTranscriptResponse503
]:
    r"""Fetch TikTok video transcript

     Fetches the spoken word transcript for a TikTok video, broken into timed segments.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokVideoTranscriptBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokVideoTranscriptResponse200 | TiktokVideoTranscriptResponse400 | TiktokVideoTranscriptResponse401 | TiktokVideoTranscriptResponse402 | TiktokVideoTranscriptResponse403 | TiktokVideoTranscriptResponse404 | TiktokVideoTranscriptResponse429 | TiktokVideoTranscriptResponse500 | TiktokVideoTranscriptResponse503]
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
    body: TiktokVideoTranscriptBody,
) -> (
    TiktokVideoTranscriptResponse200
    | TiktokVideoTranscriptResponse400
    | TiktokVideoTranscriptResponse401
    | TiktokVideoTranscriptResponse402
    | TiktokVideoTranscriptResponse403
    | TiktokVideoTranscriptResponse404
    | TiktokVideoTranscriptResponse429
    | TiktokVideoTranscriptResponse500
    | TiktokVideoTranscriptResponse503
    | None
):
    r"""Fetch TikTok video transcript

     Fetches the spoken word transcript for a TikTok video, broken into timed segments.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokVideoTranscriptBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokVideoTranscriptResponse200 | TiktokVideoTranscriptResponse400 | TiktokVideoTranscriptResponse401 | TiktokVideoTranscriptResponse402 | TiktokVideoTranscriptResponse403 | TiktokVideoTranscriptResponse404 | TiktokVideoTranscriptResponse429 | TiktokVideoTranscriptResponse500 | TiktokVideoTranscriptResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokVideoTranscriptBody,
) -> Response[
    TiktokVideoTranscriptResponse200
    | TiktokVideoTranscriptResponse400
    | TiktokVideoTranscriptResponse401
    | TiktokVideoTranscriptResponse402
    | TiktokVideoTranscriptResponse403
    | TiktokVideoTranscriptResponse404
    | TiktokVideoTranscriptResponse429
    | TiktokVideoTranscriptResponse500
    | TiktokVideoTranscriptResponse503
]:
    r"""Fetch TikTok video transcript

     Fetches the spoken word transcript for a TikTok video, broken into timed segments.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokVideoTranscriptBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokVideoTranscriptResponse200 | TiktokVideoTranscriptResponse400 | TiktokVideoTranscriptResponse401 | TiktokVideoTranscriptResponse402 | TiktokVideoTranscriptResponse403 | TiktokVideoTranscriptResponse404 | TiktokVideoTranscriptResponse429 | TiktokVideoTranscriptResponse500 | TiktokVideoTranscriptResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokVideoTranscriptBody,
) -> (
    TiktokVideoTranscriptResponse200
    | TiktokVideoTranscriptResponse400
    | TiktokVideoTranscriptResponse401
    | TiktokVideoTranscriptResponse402
    | TiktokVideoTranscriptResponse403
    | TiktokVideoTranscriptResponse404
    | TiktokVideoTranscriptResponse429
    | TiktokVideoTranscriptResponse500
    | TiktokVideoTranscriptResponse503
    | None
):
    r"""Fetch TikTok video transcript

     Fetches the spoken word transcript for a TikTok video, broken into timed segments.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokVideoTranscriptBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokVideoTranscriptResponse200 | TiktokVideoTranscriptResponse400 | TiktokVideoTranscriptResponse401 | TiktokVideoTranscriptResponse402 | TiktokVideoTranscriptResponse403 | TiktokVideoTranscriptResponse404 | TiktokVideoTranscriptResponse429 | TiktokVideoTranscriptResponse500 | TiktokVideoTranscriptResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
