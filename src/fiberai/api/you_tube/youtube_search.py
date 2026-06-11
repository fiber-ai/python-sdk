from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.youtube_search_body import YoutubeSearchBody
from ...models.youtube_search_response_200 import YoutubeSearchResponse200
from ...models.youtube_search_response_400 import YoutubeSearchResponse400
from ...models.youtube_search_response_401 import YoutubeSearchResponse401
from ...models.youtube_search_response_402 import YoutubeSearchResponse402
from ...models.youtube_search_response_403 import YoutubeSearchResponse403
from ...models.youtube_search_response_404 import YoutubeSearchResponse404
from ...models.youtube_search_response_429 import YoutubeSearchResponse429
from ...models.youtube_search_response_500 import YoutubeSearchResponse500
from ...models.youtube_search_response_503 import YoutubeSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: YoutubeSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/youtube/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    YoutubeSearchResponse200
    | YoutubeSearchResponse400
    | YoutubeSearchResponse401
    | YoutubeSearchResponse402
    | YoutubeSearchResponse403
    | YoutubeSearchResponse404
    | YoutubeSearchResponse429
    | YoutubeSearchResponse500
    | YoutubeSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = YoutubeSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = YoutubeSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = YoutubeSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = YoutubeSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = YoutubeSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = YoutubeSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = YoutubeSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = YoutubeSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = YoutubeSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    YoutubeSearchResponse200
    | YoutubeSearchResponse400
    | YoutubeSearchResponse401
    | YoutubeSearchResponse402
    | YoutubeSearchResponse403
    | YoutubeSearchResponse404
    | YoutubeSearchResponse429
    | YoutubeSearchResponse500
    | YoutubeSearchResponse503
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
    body: YoutubeSearchBody,
) -> Response[
    YoutubeSearchResponse200
    | YoutubeSearchResponse400
    | YoutubeSearchResponse401
    | YoutubeSearchResponse402
    | YoutubeSearchResponse403
    | YoutubeSearchResponse404
    | YoutubeSearchResponse429
    | YoutubeSearchResponse500
    | YoutubeSearchResponse503
]:
    r"""Search YouTube videos

     Searches YouTube for videos matching a query. Returns video titles, links, channel information, view
    counts, and durations.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (YoutubeSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[YoutubeSearchResponse200 | YoutubeSearchResponse400 | YoutubeSearchResponse401 | YoutubeSearchResponse402 | YoutubeSearchResponse403 | YoutubeSearchResponse404 | YoutubeSearchResponse429 | YoutubeSearchResponse500 | YoutubeSearchResponse503]
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
    body: YoutubeSearchBody,
) -> (
    YoutubeSearchResponse200
    | YoutubeSearchResponse400
    | YoutubeSearchResponse401
    | YoutubeSearchResponse402
    | YoutubeSearchResponse403
    | YoutubeSearchResponse404
    | YoutubeSearchResponse429
    | YoutubeSearchResponse500
    | YoutubeSearchResponse503
    | None
):
    r"""Search YouTube videos

     Searches YouTube for videos matching a query. Returns video titles, links, channel information, view
    counts, and durations.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (YoutubeSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        YoutubeSearchResponse200 | YoutubeSearchResponse400 | YoutubeSearchResponse401 | YoutubeSearchResponse402 | YoutubeSearchResponse403 | YoutubeSearchResponse404 | YoutubeSearchResponse429 | YoutubeSearchResponse500 | YoutubeSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: YoutubeSearchBody,
) -> Response[
    YoutubeSearchResponse200
    | YoutubeSearchResponse400
    | YoutubeSearchResponse401
    | YoutubeSearchResponse402
    | YoutubeSearchResponse403
    | YoutubeSearchResponse404
    | YoutubeSearchResponse429
    | YoutubeSearchResponse500
    | YoutubeSearchResponse503
]:
    r"""Search YouTube videos

     Searches YouTube for videos matching a query. Returns video titles, links, channel information, view
    counts, and durations.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (YoutubeSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[YoutubeSearchResponse200 | YoutubeSearchResponse400 | YoutubeSearchResponse401 | YoutubeSearchResponse402 | YoutubeSearchResponse403 | YoutubeSearchResponse404 | YoutubeSearchResponse429 | YoutubeSearchResponse500 | YoutubeSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: YoutubeSearchBody,
) -> (
    YoutubeSearchResponse200
    | YoutubeSearchResponse400
    | YoutubeSearchResponse401
    | YoutubeSearchResponse402
    | YoutubeSearchResponse403
    | YoutubeSearchResponse404
    | YoutubeSearchResponse429
    | YoutubeSearchResponse500
    | YoutubeSearchResponse503
    | None
):
    r"""Search YouTube videos

     Searches YouTube for videos matching a query. Returns video titles, links, channel information, view
    counts, and durations.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (YoutubeSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        YoutubeSearchResponse200 | YoutubeSearchResponse400 | YoutubeSearchResponse401 | YoutubeSearchResponse402 | YoutubeSearchResponse403 | YoutubeSearchResponse404 | YoutubeSearchResponse429 | YoutubeSearchResponse500 | YoutubeSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
