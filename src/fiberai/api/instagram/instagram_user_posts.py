from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.instagram_user_posts_body import InstagramUserPostsBody
from ...models.instagram_user_posts_response_200 import InstagramUserPostsResponse200
from ...models.instagram_user_posts_response_400 import InstagramUserPostsResponse400
from ...models.instagram_user_posts_response_401 import InstagramUserPostsResponse401
from ...models.instagram_user_posts_response_402 import InstagramUserPostsResponse402
from ...models.instagram_user_posts_response_403 import InstagramUserPostsResponse403
from ...models.instagram_user_posts_response_404 import InstagramUserPostsResponse404
from ...models.instagram_user_posts_response_429 import InstagramUserPostsResponse429
from ...models.instagram_user_posts_response_500 import InstagramUserPostsResponse500
from ...models.instagram_user_posts_response_503 import InstagramUserPostsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: InstagramUserPostsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/instagram/user-posts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InstagramUserPostsResponse200
    | InstagramUserPostsResponse400
    | InstagramUserPostsResponse401
    | InstagramUserPostsResponse402
    | InstagramUserPostsResponse403
    | InstagramUserPostsResponse404
    | InstagramUserPostsResponse429
    | InstagramUserPostsResponse500
    | InstagramUserPostsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = InstagramUserPostsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InstagramUserPostsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = InstagramUserPostsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = InstagramUserPostsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = InstagramUserPostsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = InstagramUserPostsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = InstagramUserPostsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = InstagramUserPostsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = InstagramUserPostsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InstagramUserPostsResponse200
    | InstagramUserPostsResponse400
    | InstagramUserPostsResponse401
    | InstagramUserPostsResponse402
    | InstagramUserPostsResponse403
    | InstagramUserPostsResponse404
    | InstagramUserPostsResponse429
    | InstagramUserPostsResponse500
    | InstagramUserPostsResponse503
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
    body: InstagramUserPostsBody,
) -> Response[
    InstagramUserPostsResponse200
    | InstagramUserPostsResponse400
    | InstagramUserPostsResponse401
    | InstagramUserPostsResponse402
    | InstagramUserPostsResponse403
    | InstagramUserPostsResponse404
    | InstagramUserPostsResponse429
    | InstagramUserPostsResponse500
    | InstagramUserPostsResponse503
]:
    r"""Fetch Instagram user posts

     Fetches the latest posts for an Instagram user. Returns a paginated list of posts with engagement
    metrics. Use the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InstagramUserPostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstagramUserPostsResponse200 | InstagramUserPostsResponse400 | InstagramUserPostsResponse401 | InstagramUserPostsResponse402 | InstagramUserPostsResponse403 | InstagramUserPostsResponse404 | InstagramUserPostsResponse429 | InstagramUserPostsResponse500 | InstagramUserPostsResponse503]
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
    body: InstagramUserPostsBody,
) -> (
    InstagramUserPostsResponse200
    | InstagramUserPostsResponse400
    | InstagramUserPostsResponse401
    | InstagramUserPostsResponse402
    | InstagramUserPostsResponse403
    | InstagramUserPostsResponse404
    | InstagramUserPostsResponse429
    | InstagramUserPostsResponse500
    | InstagramUserPostsResponse503
    | None
):
    r"""Fetch Instagram user posts

     Fetches the latest posts for an Instagram user. Returns a paginated list of posts with engagement
    metrics. Use the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InstagramUserPostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstagramUserPostsResponse200 | InstagramUserPostsResponse400 | InstagramUserPostsResponse401 | InstagramUserPostsResponse402 | InstagramUserPostsResponse403 | InstagramUserPostsResponse404 | InstagramUserPostsResponse429 | InstagramUserPostsResponse500 | InstagramUserPostsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InstagramUserPostsBody,
) -> Response[
    InstagramUserPostsResponse200
    | InstagramUserPostsResponse400
    | InstagramUserPostsResponse401
    | InstagramUserPostsResponse402
    | InstagramUserPostsResponse403
    | InstagramUserPostsResponse404
    | InstagramUserPostsResponse429
    | InstagramUserPostsResponse500
    | InstagramUserPostsResponse503
]:
    r"""Fetch Instagram user posts

     Fetches the latest posts for an Instagram user. Returns a paginated list of posts with engagement
    metrics. Use the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InstagramUserPostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstagramUserPostsResponse200 | InstagramUserPostsResponse400 | InstagramUserPostsResponse401 | InstagramUserPostsResponse402 | InstagramUserPostsResponse403 | InstagramUserPostsResponse404 | InstagramUserPostsResponse429 | InstagramUserPostsResponse500 | InstagramUserPostsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: InstagramUserPostsBody,
) -> (
    InstagramUserPostsResponse200
    | InstagramUserPostsResponse400
    | InstagramUserPostsResponse401
    | InstagramUserPostsResponse402
    | InstagramUserPostsResponse403
    | InstagramUserPostsResponse404
    | InstagramUserPostsResponse429
    | InstagramUserPostsResponse500
    | InstagramUserPostsResponse503
    | None
):
    r"""Fetch Instagram user posts

     Fetches the latest posts for an Instagram user. Returns a paginated list of posts with engagement
    metrics. Use the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InstagramUserPostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstagramUserPostsResponse200 | InstagramUserPostsResponse400 | InstagramUserPostsResponse401 | InstagramUserPostsResponse402 | InstagramUserPostsResponse403 | InstagramUserPostsResponse404 | InstagramUserPostsResponse429 | InstagramUserPostsResponse500 | InstagramUserPostsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
