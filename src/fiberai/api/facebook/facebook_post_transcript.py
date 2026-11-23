from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.facebook_post_transcript_body import FacebookPostTranscriptBody
from ...models.facebook_post_transcript_response_200 import FacebookPostTranscriptResponse200
from ...models.facebook_post_transcript_response_400 import FacebookPostTranscriptResponse400
from ...models.facebook_post_transcript_response_401 import FacebookPostTranscriptResponse401
from ...models.facebook_post_transcript_response_402 import FacebookPostTranscriptResponse402
from ...models.facebook_post_transcript_response_403 import FacebookPostTranscriptResponse403
from ...models.facebook_post_transcript_response_404 import FacebookPostTranscriptResponse404
from ...models.facebook_post_transcript_response_422 import FacebookPostTranscriptResponse422
from ...models.facebook_post_transcript_response_429 import FacebookPostTranscriptResponse429
from ...models.facebook_post_transcript_response_500 import FacebookPostTranscriptResponse500
from ...models.facebook_post_transcript_response_503 import FacebookPostTranscriptResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: FacebookPostTranscriptBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/facebook/post/transcript",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FacebookPostTranscriptResponse200
    | FacebookPostTranscriptResponse400
    | FacebookPostTranscriptResponse401
    | FacebookPostTranscriptResponse402
    | FacebookPostTranscriptResponse403
    | FacebookPostTranscriptResponse404
    | FacebookPostTranscriptResponse422
    | FacebookPostTranscriptResponse429
    | FacebookPostTranscriptResponse500
    | FacebookPostTranscriptResponse503
    | None
):
    if response.status_code == 200:
        response_200 = FacebookPostTranscriptResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FacebookPostTranscriptResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FacebookPostTranscriptResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = FacebookPostTranscriptResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = FacebookPostTranscriptResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FacebookPostTranscriptResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = FacebookPostTranscriptResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = FacebookPostTranscriptResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FacebookPostTranscriptResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = FacebookPostTranscriptResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FacebookPostTranscriptResponse200
    | FacebookPostTranscriptResponse400
    | FacebookPostTranscriptResponse401
    | FacebookPostTranscriptResponse402
    | FacebookPostTranscriptResponse403
    | FacebookPostTranscriptResponse404
    | FacebookPostTranscriptResponse422
    | FacebookPostTranscriptResponse429
    | FacebookPostTranscriptResponse500
    | FacebookPostTranscriptResponse503
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
    body: FacebookPostTranscriptBody,
) -> Response[
    FacebookPostTranscriptResponse200
    | FacebookPostTranscriptResponse400
    | FacebookPostTranscriptResponse401
    | FacebookPostTranscriptResponse402
    | FacebookPostTranscriptResponse403
    | FacebookPostTranscriptResponse404
    | FacebookPostTranscriptResponse422
    | FacebookPostTranscriptResponse429
    | FacebookPostTranscriptResponse500
    | FacebookPostTranscriptResponse503
]:
    """Fetch Facebook video transcript

     Fetches the transcript of a public Facebook video or Reel. Videos longer than 2 minutes are not
    transcribed; those requests return 404 and are not charged.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookPostTranscriptBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookPostTranscriptResponse200 | FacebookPostTranscriptResponse400 | FacebookPostTranscriptResponse401 | FacebookPostTranscriptResponse402 | FacebookPostTranscriptResponse403 | FacebookPostTranscriptResponse404 | FacebookPostTranscriptResponse422 | FacebookPostTranscriptResponse429 | FacebookPostTranscriptResponse500 | FacebookPostTranscriptResponse503]
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
    body: FacebookPostTranscriptBody,
) -> (
    FacebookPostTranscriptResponse200
    | FacebookPostTranscriptResponse400
    | FacebookPostTranscriptResponse401
    | FacebookPostTranscriptResponse402
    | FacebookPostTranscriptResponse403
    | FacebookPostTranscriptResponse404
    | FacebookPostTranscriptResponse422
    | FacebookPostTranscriptResponse429
    | FacebookPostTranscriptResponse500
    | FacebookPostTranscriptResponse503
    | None
):
    """Fetch Facebook video transcript

     Fetches the transcript of a public Facebook video or Reel. Videos longer than 2 minutes are not
    transcribed; those requests return 404 and are not charged.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookPostTranscriptBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookPostTranscriptResponse200 | FacebookPostTranscriptResponse400 | FacebookPostTranscriptResponse401 | FacebookPostTranscriptResponse402 | FacebookPostTranscriptResponse403 | FacebookPostTranscriptResponse404 | FacebookPostTranscriptResponse422 | FacebookPostTranscriptResponse429 | FacebookPostTranscriptResponse500 | FacebookPostTranscriptResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookPostTranscriptBody,
) -> Response[
    FacebookPostTranscriptResponse200
    | FacebookPostTranscriptResponse400
    | FacebookPostTranscriptResponse401
    | FacebookPostTranscriptResponse402
    | FacebookPostTranscriptResponse403
    | FacebookPostTranscriptResponse404
    | FacebookPostTranscriptResponse422
    | FacebookPostTranscriptResponse429
    | FacebookPostTranscriptResponse500
    | FacebookPostTranscriptResponse503
]:
    """Fetch Facebook video transcript

     Fetches the transcript of a public Facebook video or Reel. Videos longer than 2 minutes are not
    transcribed; those requests return 404 and are not charged.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookPostTranscriptBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookPostTranscriptResponse200 | FacebookPostTranscriptResponse400 | FacebookPostTranscriptResponse401 | FacebookPostTranscriptResponse402 | FacebookPostTranscriptResponse403 | FacebookPostTranscriptResponse404 | FacebookPostTranscriptResponse422 | FacebookPostTranscriptResponse429 | FacebookPostTranscriptResponse500 | FacebookPostTranscriptResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookPostTranscriptBody,
) -> (
    FacebookPostTranscriptResponse200
    | FacebookPostTranscriptResponse400
    | FacebookPostTranscriptResponse401
    | FacebookPostTranscriptResponse402
    | FacebookPostTranscriptResponse403
    | FacebookPostTranscriptResponse404
    | FacebookPostTranscriptResponse422
    | FacebookPostTranscriptResponse429
    | FacebookPostTranscriptResponse500
    | FacebookPostTranscriptResponse503
    | None
):
    """Fetch Facebook video transcript

     Fetches the transcript of a public Facebook video or Reel. Videos longer than 2 minutes are not
    transcribed; those requests return 404 and are not charged.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookPostTranscriptBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookPostTranscriptResponse200 | FacebookPostTranscriptResponse400 | FacebookPostTranscriptResponse401 | FacebookPostTranscriptResponse402 | FacebookPostTranscriptResponse403 | FacebookPostTranscriptResponse404 | FacebookPostTranscriptResponse422 | FacebookPostTranscriptResponse429 | FacebookPostTranscriptResponse500 | FacebookPostTranscriptResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
