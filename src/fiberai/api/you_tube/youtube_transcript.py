from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.youtube_transcript_body import YoutubeTranscriptBody
from ...models.youtube_transcript_response_200 import YoutubeTranscriptResponse200
from ...models.youtube_transcript_response_400 import YoutubeTranscriptResponse400
from ...models.youtube_transcript_response_401 import YoutubeTranscriptResponse401
from ...models.youtube_transcript_response_402 import YoutubeTranscriptResponse402
from ...models.youtube_transcript_response_403 import YoutubeTranscriptResponse403
from ...models.youtube_transcript_response_404 import YoutubeTranscriptResponse404
from ...models.youtube_transcript_response_422 import YoutubeTranscriptResponse422
from ...models.youtube_transcript_response_429 import YoutubeTranscriptResponse429
from ...models.youtube_transcript_response_500 import YoutubeTranscriptResponse500
from ...models.youtube_transcript_response_503 import YoutubeTranscriptResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: YoutubeTranscriptBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/youtube/transcript",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    YoutubeTranscriptResponse200
    | YoutubeTranscriptResponse400
    | YoutubeTranscriptResponse401
    | YoutubeTranscriptResponse402
    | YoutubeTranscriptResponse403
    | YoutubeTranscriptResponse404
    | YoutubeTranscriptResponse422
    | YoutubeTranscriptResponse429
    | YoutubeTranscriptResponse500
    | YoutubeTranscriptResponse503
    | None
):
    if response.status_code == 200:
        response_200 = YoutubeTranscriptResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = YoutubeTranscriptResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = YoutubeTranscriptResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = YoutubeTranscriptResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = YoutubeTranscriptResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = YoutubeTranscriptResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = YoutubeTranscriptResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = YoutubeTranscriptResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = YoutubeTranscriptResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = YoutubeTranscriptResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    YoutubeTranscriptResponse200
    | YoutubeTranscriptResponse400
    | YoutubeTranscriptResponse401
    | YoutubeTranscriptResponse402
    | YoutubeTranscriptResponse403
    | YoutubeTranscriptResponse404
    | YoutubeTranscriptResponse422
    | YoutubeTranscriptResponse429
    | YoutubeTranscriptResponse500
    | YoutubeTranscriptResponse503
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
    body: YoutubeTranscriptBody,
) -> Response[
    YoutubeTranscriptResponse200
    | YoutubeTranscriptResponse400
    | YoutubeTranscriptResponse401
    | YoutubeTranscriptResponse402
    | YoutubeTranscriptResponse403
    | YoutubeTranscriptResponse404
    | YoutubeTranscriptResponse422
    | YoutubeTranscriptResponse429
    | YoutubeTranscriptResponse500
    | YoutubeTranscriptResponse503
]:
    r"""Fetch YouTube video transcript

     Fetches the timestamped transcript for a YouTube video. Returns all transcript segments and the list
    of languages available. Provide a full YouTube URL or a bare 11-character video ID.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (YoutubeTranscriptBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[YoutubeTranscriptResponse200 | YoutubeTranscriptResponse400 | YoutubeTranscriptResponse401 | YoutubeTranscriptResponse402 | YoutubeTranscriptResponse403 | YoutubeTranscriptResponse404 | YoutubeTranscriptResponse422 | YoutubeTranscriptResponse429 | YoutubeTranscriptResponse500 | YoutubeTranscriptResponse503]
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
    body: YoutubeTranscriptBody,
) -> (
    YoutubeTranscriptResponse200
    | YoutubeTranscriptResponse400
    | YoutubeTranscriptResponse401
    | YoutubeTranscriptResponse402
    | YoutubeTranscriptResponse403
    | YoutubeTranscriptResponse404
    | YoutubeTranscriptResponse422
    | YoutubeTranscriptResponse429
    | YoutubeTranscriptResponse500
    | YoutubeTranscriptResponse503
    | None
):
    r"""Fetch YouTube video transcript

     Fetches the timestamped transcript for a YouTube video. Returns all transcript segments and the list
    of languages available. Provide a full YouTube URL or a bare 11-character video ID.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (YoutubeTranscriptBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        YoutubeTranscriptResponse200 | YoutubeTranscriptResponse400 | YoutubeTranscriptResponse401 | YoutubeTranscriptResponse402 | YoutubeTranscriptResponse403 | YoutubeTranscriptResponse404 | YoutubeTranscriptResponse422 | YoutubeTranscriptResponse429 | YoutubeTranscriptResponse500 | YoutubeTranscriptResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: YoutubeTranscriptBody,
) -> Response[
    YoutubeTranscriptResponse200
    | YoutubeTranscriptResponse400
    | YoutubeTranscriptResponse401
    | YoutubeTranscriptResponse402
    | YoutubeTranscriptResponse403
    | YoutubeTranscriptResponse404
    | YoutubeTranscriptResponse422
    | YoutubeTranscriptResponse429
    | YoutubeTranscriptResponse500
    | YoutubeTranscriptResponse503
]:
    r"""Fetch YouTube video transcript

     Fetches the timestamped transcript for a YouTube video. Returns all transcript segments and the list
    of languages available. Provide a full YouTube URL or a bare 11-character video ID.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (YoutubeTranscriptBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[YoutubeTranscriptResponse200 | YoutubeTranscriptResponse400 | YoutubeTranscriptResponse401 | YoutubeTranscriptResponse402 | YoutubeTranscriptResponse403 | YoutubeTranscriptResponse404 | YoutubeTranscriptResponse422 | YoutubeTranscriptResponse429 | YoutubeTranscriptResponse500 | YoutubeTranscriptResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: YoutubeTranscriptBody,
) -> (
    YoutubeTranscriptResponse200
    | YoutubeTranscriptResponse400
    | YoutubeTranscriptResponse401
    | YoutubeTranscriptResponse402
    | YoutubeTranscriptResponse403
    | YoutubeTranscriptResponse404
    | YoutubeTranscriptResponse422
    | YoutubeTranscriptResponse429
    | YoutubeTranscriptResponse500
    | YoutubeTranscriptResponse503
    | None
):
    r"""Fetch YouTube video transcript

     Fetches the timestamped transcript for a YouTube video. Returns all transcript segments and the list
    of languages available. Provide a full YouTube URL or a bare 11-character video ID.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (YoutubeTranscriptBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        YoutubeTranscriptResponse200 | YoutubeTranscriptResponse400 | YoutubeTranscriptResponse401 | YoutubeTranscriptResponse402 | YoutubeTranscriptResponse403 | YoutubeTranscriptResponse404 | YoutubeTranscriptResponse422 | YoutubeTranscriptResponse429 | YoutubeTranscriptResponse500 | YoutubeTranscriptResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
