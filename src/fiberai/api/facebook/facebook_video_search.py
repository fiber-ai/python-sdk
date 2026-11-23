from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.facebook_video_search_body import FacebookVideoSearchBody
from ...models.facebook_video_search_response_200 import FacebookVideoSearchResponse200
from ...models.facebook_video_search_response_400 import FacebookVideoSearchResponse400
from ...models.facebook_video_search_response_401 import FacebookVideoSearchResponse401
from ...models.facebook_video_search_response_402 import FacebookVideoSearchResponse402
from ...models.facebook_video_search_response_403 import FacebookVideoSearchResponse403
from ...models.facebook_video_search_response_404 import FacebookVideoSearchResponse404
from ...models.facebook_video_search_response_422 import FacebookVideoSearchResponse422
from ...models.facebook_video_search_response_429 import FacebookVideoSearchResponse429
from ...models.facebook_video_search_response_500 import FacebookVideoSearchResponse500
from ...models.facebook_video_search_response_503 import FacebookVideoSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: FacebookVideoSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/facebook/search/videos",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FacebookVideoSearchResponse200
    | FacebookVideoSearchResponse400
    | FacebookVideoSearchResponse401
    | FacebookVideoSearchResponse402
    | FacebookVideoSearchResponse403
    | FacebookVideoSearchResponse404
    | FacebookVideoSearchResponse422
    | FacebookVideoSearchResponse429
    | FacebookVideoSearchResponse500
    | FacebookVideoSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = FacebookVideoSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FacebookVideoSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FacebookVideoSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = FacebookVideoSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = FacebookVideoSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FacebookVideoSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = FacebookVideoSearchResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = FacebookVideoSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FacebookVideoSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = FacebookVideoSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FacebookVideoSearchResponse200
    | FacebookVideoSearchResponse400
    | FacebookVideoSearchResponse401
    | FacebookVideoSearchResponse402
    | FacebookVideoSearchResponse403
    | FacebookVideoSearchResponse404
    | FacebookVideoSearchResponse422
    | FacebookVideoSearchResponse429
    | FacebookVideoSearchResponse500
    | FacebookVideoSearchResponse503
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
    body: FacebookVideoSearchBody,
) -> Response[
    FacebookVideoSearchResponse200
    | FacebookVideoSearchResponse400
    | FacebookVideoSearchResponse401
    | FacebookVideoSearchResponse402
    | FacebookVideoSearchResponse403
    | FacebookVideoSearchResponse404
    | FacebookVideoSearchResponse422
    | FacebookVideoSearchResponse429
    | FacebookVideoSearchResponse500
    | FacebookVideoSearchResponse503
]:
    """Search Facebook videos

     Searches public Facebook videos and Reels by keyword (text and photo posts are not included). Use
    the response's `nextPageToken` to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookVideoSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookVideoSearchResponse200 | FacebookVideoSearchResponse400 | FacebookVideoSearchResponse401 | FacebookVideoSearchResponse402 | FacebookVideoSearchResponse403 | FacebookVideoSearchResponse404 | FacebookVideoSearchResponse422 | FacebookVideoSearchResponse429 | FacebookVideoSearchResponse500 | FacebookVideoSearchResponse503]
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
    body: FacebookVideoSearchBody,
) -> (
    FacebookVideoSearchResponse200
    | FacebookVideoSearchResponse400
    | FacebookVideoSearchResponse401
    | FacebookVideoSearchResponse402
    | FacebookVideoSearchResponse403
    | FacebookVideoSearchResponse404
    | FacebookVideoSearchResponse422
    | FacebookVideoSearchResponse429
    | FacebookVideoSearchResponse500
    | FacebookVideoSearchResponse503
    | None
):
    """Search Facebook videos

     Searches public Facebook videos and Reels by keyword (text and photo posts are not included). Use
    the response's `nextPageToken` to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookVideoSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookVideoSearchResponse200 | FacebookVideoSearchResponse400 | FacebookVideoSearchResponse401 | FacebookVideoSearchResponse402 | FacebookVideoSearchResponse403 | FacebookVideoSearchResponse404 | FacebookVideoSearchResponse422 | FacebookVideoSearchResponse429 | FacebookVideoSearchResponse500 | FacebookVideoSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookVideoSearchBody,
) -> Response[
    FacebookVideoSearchResponse200
    | FacebookVideoSearchResponse400
    | FacebookVideoSearchResponse401
    | FacebookVideoSearchResponse402
    | FacebookVideoSearchResponse403
    | FacebookVideoSearchResponse404
    | FacebookVideoSearchResponse422
    | FacebookVideoSearchResponse429
    | FacebookVideoSearchResponse500
    | FacebookVideoSearchResponse503
]:
    """Search Facebook videos

     Searches public Facebook videos and Reels by keyword (text and photo posts are not included). Use
    the response's `nextPageToken` to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookVideoSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookVideoSearchResponse200 | FacebookVideoSearchResponse400 | FacebookVideoSearchResponse401 | FacebookVideoSearchResponse402 | FacebookVideoSearchResponse403 | FacebookVideoSearchResponse404 | FacebookVideoSearchResponse422 | FacebookVideoSearchResponse429 | FacebookVideoSearchResponse500 | FacebookVideoSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookVideoSearchBody,
) -> (
    FacebookVideoSearchResponse200
    | FacebookVideoSearchResponse400
    | FacebookVideoSearchResponse401
    | FacebookVideoSearchResponse402
    | FacebookVideoSearchResponse403
    | FacebookVideoSearchResponse404
    | FacebookVideoSearchResponse422
    | FacebookVideoSearchResponse429
    | FacebookVideoSearchResponse500
    | FacebookVideoSearchResponse503
    | None
):
    """Search Facebook videos

     Searches public Facebook videos and Reels by keyword (text and photo posts are not included). Use
    the response's `nextPageToken` to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookVideoSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookVideoSearchResponse200 | FacebookVideoSearchResponse400 | FacebookVideoSearchResponse401 | FacebookVideoSearchResponse402 | FacebookVideoSearchResponse403 | FacebookVideoSearchResponse404 | FacebookVideoSearchResponse422 | FacebookVideoSearchResponse429 | FacebookVideoSearchResponse500 | FacebookVideoSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
