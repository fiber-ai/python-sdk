from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.profile_posts_live_fetch_body import ProfilePostsLiveFetchBody
from ...models.profile_posts_live_fetch_response_200 import ProfilePostsLiveFetchResponse200
from ...models.profile_posts_live_fetch_response_400 import ProfilePostsLiveFetchResponse400
from ...models.profile_posts_live_fetch_response_401 import ProfilePostsLiveFetchResponse401
from ...models.profile_posts_live_fetch_response_402 import ProfilePostsLiveFetchResponse402
from ...models.profile_posts_live_fetch_response_403 import ProfilePostsLiveFetchResponse403
from ...models.profile_posts_live_fetch_response_404 import ProfilePostsLiveFetchResponse404
from ...models.profile_posts_live_fetch_response_429 import ProfilePostsLiveFetchResponse429
from ...models.profile_posts_live_fetch_response_500 import ProfilePostsLiveFetchResponse500
from ...models.profile_posts_live_fetch_response_503 import ProfilePostsLiveFetchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: ProfilePostsLiveFetchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/linkedin-live-fetch/profile-posts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ProfilePostsLiveFetchResponse200
    | ProfilePostsLiveFetchResponse400
    | ProfilePostsLiveFetchResponse401
    | ProfilePostsLiveFetchResponse402
    | ProfilePostsLiveFetchResponse403
    | ProfilePostsLiveFetchResponse404
    | ProfilePostsLiveFetchResponse429
    | ProfilePostsLiveFetchResponse500
    | ProfilePostsLiveFetchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ProfilePostsLiveFetchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProfilePostsLiveFetchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProfilePostsLiveFetchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ProfilePostsLiveFetchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ProfilePostsLiveFetchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ProfilePostsLiveFetchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ProfilePostsLiveFetchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ProfilePostsLiveFetchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ProfilePostsLiveFetchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ProfilePostsLiveFetchResponse200
    | ProfilePostsLiveFetchResponse400
    | ProfilePostsLiveFetchResponse401
    | ProfilePostsLiveFetchResponse402
    | ProfilePostsLiveFetchResponse403
    | ProfilePostsLiveFetchResponse404
    | ProfilePostsLiveFetchResponse429
    | ProfilePostsLiveFetchResponse500
    | ProfilePostsLiveFetchResponse503
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
    body: ProfilePostsLiveFetchBody,
) -> Response[
    ProfilePostsLiveFetchResponse200
    | ProfilePostsLiveFetchResponse400
    | ProfilePostsLiveFetchResponse401
    | ProfilePostsLiveFetchResponse402
    | ProfilePostsLiveFetchResponse403
    | ProfilePostsLiveFetchResponse404
    | ProfilePostsLiveFetchResponse429
    | ProfilePostsLiveFetchResponse500
    | ProfilePostsLiveFetchResponse503
]:
    r"""Fetch LinkedIn profile posts

     Fetches recent posts from a LinkedIn profile. Returns a paginated feed of posts with optional cursor
    for pagination. Each page returns up to 50 posts.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ProfilePostsLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfilePostsLiveFetchResponse200 | ProfilePostsLiveFetchResponse400 | ProfilePostsLiveFetchResponse401 | ProfilePostsLiveFetchResponse402 | ProfilePostsLiveFetchResponse403 | ProfilePostsLiveFetchResponse404 | ProfilePostsLiveFetchResponse429 | ProfilePostsLiveFetchResponse500 | ProfilePostsLiveFetchResponse503]
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
    body: ProfilePostsLiveFetchBody,
) -> (
    ProfilePostsLiveFetchResponse200
    | ProfilePostsLiveFetchResponse400
    | ProfilePostsLiveFetchResponse401
    | ProfilePostsLiveFetchResponse402
    | ProfilePostsLiveFetchResponse403
    | ProfilePostsLiveFetchResponse404
    | ProfilePostsLiveFetchResponse429
    | ProfilePostsLiveFetchResponse500
    | ProfilePostsLiveFetchResponse503
    | None
):
    r"""Fetch LinkedIn profile posts

     Fetches recent posts from a LinkedIn profile. Returns a paginated feed of posts with optional cursor
    for pagination. Each page returns up to 50 posts.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ProfilePostsLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfilePostsLiveFetchResponse200 | ProfilePostsLiveFetchResponse400 | ProfilePostsLiveFetchResponse401 | ProfilePostsLiveFetchResponse402 | ProfilePostsLiveFetchResponse403 | ProfilePostsLiveFetchResponse404 | ProfilePostsLiveFetchResponse429 | ProfilePostsLiveFetchResponse500 | ProfilePostsLiveFetchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ProfilePostsLiveFetchBody,
) -> Response[
    ProfilePostsLiveFetchResponse200
    | ProfilePostsLiveFetchResponse400
    | ProfilePostsLiveFetchResponse401
    | ProfilePostsLiveFetchResponse402
    | ProfilePostsLiveFetchResponse403
    | ProfilePostsLiveFetchResponse404
    | ProfilePostsLiveFetchResponse429
    | ProfilePostsLiveFetchResponse500
    | ProfilePostsLiveFetchResponse503
]:
    r"""Fetch LinkedIn profile posts

     Fetches recent posts from a LinkedIn profile. Returns a paginated feed of posts with optional cursor
    for pagination. Each page returns up to 50 posts.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ProfilePostsLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfilePostsLiveFetchResponse200 | ProfilePostsLiveFetchResponse400 | ProfilePostsLiveFetchResponse401 | ProfilePostsLiveFetchResponse402 | ProfilePostsLiveFetchResponse403 | ProfilePostsLiveFetchResponse404 | ProfilePostsLiveFetchResponse429 | ProfilePostsLiveFetchResponse500 | ProfilePostsLiveFetchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ProfilePostsLiveFetchBody,
) -> (
    ProfilePostsLiveFetchResponse200
    | ProfilePostsLiveFetchResponse400
    | ProfilePostsLiveFetchResponse401
    | ProfilePostsLiveFetchResponse402
    | ProfilePostsLiveFetchResponse403
    | ProfilePostsLiveFetchResponse404
    | ProfilePostsLiveFetchResponse429
    | ProfilePostsLiveFetchResponse500
    | ProfilePostsLiveFetchResponse503
    | None
):
    r"""Fetch LinkedIn profile posts

     Fetches recent posts from a LinkedIn profile. Returns a paginated feed of posts with optional cursor
    for pagination. Each page returns up to 50 posts.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ProfilePostsLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfilePostsLiveFetchResponse200 | ProfilePostsLiveFetchResponse400 | ProfilePostsLiveFetchResponse401 | ProfilePostsLiveFetchResponse402 | ProfilePostsLiveFetchResponse403 | ProfilePostsLiveFetchResponse404 | ProfilePostsLiveFetchResponse429 | ProfilePostsLiveFetchResponse500 | ProfilePostsLiveFetchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
