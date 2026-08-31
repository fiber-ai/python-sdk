from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tiktok_search_keyword_body import TiktokSearchKeywordBody
from ...models.tiktok_search_keyword_response_200 import TiktokSearchKeywordResponse200
from ...models.tiktok_search_keyword_response_400 import TiktokSearchKeywordResponse400
from ...models.tiktok_search_keyword_response_401 import TiktokSearchKeywordResponse401
from ...models.tiktok_search_keyword_response_402 import TiktokSearchKeywordResponse402
from ...models.tiktok_search_keyword_response_403 import TiktokSearchKeywordResponse403
from ...models.tiktok_search_keyword_response_404 import TiktokSearchKeywordResponse404
from ...models.tiktok_search_keyword_response_422 import TiktokSearchKeywordResponse422
from ...models.tiktok_search_keyword_response_429 import TiktokSearchKeywordResponse429
from ...models.tiktok_search_keyword_response_500 import TiktokSearchKeywordResponse500
from ...models.tiktok_search_keyword_response_503 import TiktokSearchKeywordResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TiktokSearchKeywordBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tiktok/search-keyword",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TiktokSearchKeywordResponse200
    | TiktokSearchKeywordResponse400
    | TiktokSearchKeywordResponse401
    | TiktokSearchKeywordResponse402
    | TiktokSearchKeywordResponse403
    | TiktokSearchKeywordResponse404
    | TiktokSearchKeywordResponse422
    | TiktokSearchKeywordResponse429
    | TiktokSearchKeywordResponse500
    | TiktokSearchKeywordResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TiktokSearchKeywordResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TiktokSearchKeywordResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TiktokSearchKeywordResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TiktokSearchKeywordResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TiktokSearchKeywordResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TiktokSearchKeywordResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = TiktokSearchKeywordResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = TiktokSearchKeywordResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TiktokSearchKeywordResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TiktokSearchKeywordResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TiktokSearchKeywordResponse200
    | TiktokSearchKeywordResponse400
    | TiktokSearchKeywordResponse401
    | TiktokSearchKeywordResponse402
    | TiktokSearchKeywordResponse403
    | TiktokSearchKeywordResponse404
    | TiktokSearchKeywordResponse422
    | TiktokSearchKeywordResponse429
    | TiktokSearchKeywordResponse500
    | TiktokSearchKeywordResponse503
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
    body: TiktokSearchKeywordBody,
) -> Response[
    TiktokSearchKeywordResponse200
    | TiktokSearchKeywordResponse400
    | TiktokSearchKeywordResponse401
    | TiktokSearchKeywordResponse402
    | TiktokSearchKeywordResponse403
    | TiktokSearchKeywordResponse404
    | TiktokSearchKeywordResponse422
    | TiktokSearchKeywordResponse429
    | TiktokSearchKeywordResponse500
    | TiktokSearchKeywordResponse503
]:
    """Search TikTok videos by keyword

     Searches for TikTok videos by keyword or phrase. Returns a paginated list of matching videos. Use
    the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokSearchKeywordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokSearchKeywordResponse200 | TiktokSearchKeywordResponse400 | TiktokSearchKeywordResponse401 | TiktokSearchKeywordResponse402 | TiktokSearchKeywordResponse403 | TiktokSearchKeywordResponse404 | TiktokSearchKeywordResponse422 | TiktokSearchKeywordResponse429 | TiktokSearchKeywordResponse500 | TiktokSearchKeywordResponse503]
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
    body: TiktokSearchKeywordBody,
) -> (
    TiktokSearchKeywordResponse200
    | TiktokSearchKeywordResponse400
    | TiktokSearchKeywordResponse401
    | TiktokSearchKeywordResponse402
    | TiktokSearchKeywordResponse403
    | TiktokSearchKeywordResponse404
    | TiktokSearchKeywordResponse422
    | TiktokSearchKeywordResponse429
    | TiktokSearchKeywordResponse500
    | TiktokSearchKeywordResponse503
    | None
):
    """Search TikTok videos by keyword

     Searches for TikTok videos by keyword or phrase. Returns a paginated list of matching videos. Use
    the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokSearchKeywordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokSearchKeywordResponse200 | TiktokSearchKeywordResponse400 | TiktokSearchKeywordResponse401 | TiktokSearchKeywordResponse402 | TiktokSearchKeywordResponse403 | TiktokSearchKeywordResponse404 | TiktokSearchKeywordResponse422 | TiktokSearchKeywordResponse429 | TiktokSearchKeywordResponse500 | TiktokSearchKeywordResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokSearchKeywordBody,
) -> Response[
    TiktokSearchKeywordResponse200
    | TiktokSearchKeywordResponse400
    | TiktokSearchKeywordResponse401
    | TiktokSearchKeywordResponse402
    | TiktokSearchKeywordResponse403
    | TiktokSearchKeywordResponse404
    | TiktokSearchKeywordResponse422
    | TiktokSearchKeywordResponse429
    | TiktokSearchKeywordResponse500
    | TiktokSearchKeywordResponse503
]:
    """Search TikTok videos by keyword

     Searches for TikTok videos by keyword or phrase. Returns a paginated list of matching videos. Use
    the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokSearchKeywordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokSearchKeywordResponse200 | TiktokSearchKeywordResponse400 | TiktokSearchKeywordResponse401 | TiktokSearchKeywordResponse402 | TiktokSearchKeywordResponse403 | TiktokSearchKeywordResponse404 | TiktokSearchKeywordResponse422 | TiktokSearchKeywordResponse429 | TiktokSearchKeywordResponse500 | TiktokSearchKeywordResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokSearchKeywordBody,
) -> (
    TiktokSearchKeywordResponse200
    | TiktokSearchKeywordResponse400
    | TiktokSearchKeywordResponse401
    | TiktokSearchKeywordResponse402
    | TiktokSearchKeywordResponse403
    | TiktokSearchKeywordResponse404
    | TiktokSearchKeywordResponse422
    | TiktokSearchKeywordResponse429
    | TiktokSearchKeywordResponse500
    | TiktokSearchKeywordResponse503
    | None
):
    """Search TikTok videos by keyword

     Searches for TikTok videos by keyword or phrase. Returns a paginated list of matching videos. Use
    the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokSearchKeywordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokSearchKeywordResponse200 | TiktokSearchKeywordResponse400 | TiktokSearchKeywordResponse401 | TiktokSearchKeywordResponse402 | TiktokSearchKeywordResponse403 | TiktokSearchKeywordResponse404 | TiktokSearchKeywordResponse422 | TiktokSearchKeywordResponse429 | TiktokSearchKeywordResponse500 | TiktokSearchKeywordResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
