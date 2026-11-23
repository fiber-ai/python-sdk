from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.facebook_profile_posts_body import FacebookProfilePostsBody
from ...models.facebook_profile_posts_response_200 import FacebookProfilePostsResponse200
from ...models.facebook_profile_posts_response_400 import FacebookProfilePostsResponse400
from ...models.facebook_profile_posts_response_401 import FacebookProfilePostsResponse401
from ...models.facebook_profile_posts_response_402 import FacebookProfilePostsResponse402
from ...models.facebook_profile_posts_response_403 import FacebookProfilePostsResponse403
from ...models.facebook_profile_posts_response_404 import FacebookProfilePostsResponse404
from ...models.facebook_profile_posts_response_422 import FacebookProfilePostsResponse422
from ...models.facebook_profile_posts_response_429 import FacebookProfilePostsResponse429
from ...models.facebook_profile_posts_response_500 import FacebookProfilePostsResponse500
from ...models.facebook_profile_posts_response_503 import FacebookProfilePostsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: FacebookProfilePostsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/facebook/profile/posts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FacebookProfilePostsResponse200
    | FacebookProfilePostsResponse400
    | FacebookProfilePostsResponse401
    | FacebookProfilePostsResponse402
    | FacebookProfilePostsResponse403
    | FacebookProfilePostsResponse404
    | FacebookProfilePostsResponse422
    | FacebookProfilePostsResponse429
    | FacebookProfilePostsResponse500
    | FacebookProfilePostsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = FacebookProfilePostsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FacebookProfilePostsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FacebookProfilePostsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = FacebookProfilePostsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = FacebookProfilePostsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FacebookProfilePostsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = FacebookProfilePostsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = FacebookProfilePostsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FacebookProfilePostsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = FacebookProfilePostsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FacebookProfilePostsResponse200
    | FacebookProfilePostsResponse400
    | FacebookProfilePostsResponse401
    | FacebookProfilePostsResponse402
    | FacebookProfilePostsResponse403
    | FacebookProfilePostsResponse404
    | FacebookProfilePostsResponse422
    | FacebookProfilePostsResponse429
    | FacebookProfilePostsResponse500
    | FacebookProfilePostsResponse503
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
    body: FacebookProfilePostsBody,
) -> Response[
    FacebookProfilePostsResponse200
    | FacebookProfilePostsResponse400
    | FacebookProfilePostsResponse401
    | FacebookProfilePostsResponse402
    | FacebookProfilePostsResponse403
    | FacebookProfilePostsResponse404
    | FacebookProfilePostsResponse422
    | FacebookProfilePostsResponse429
    | FacebookProfilePostsResponse500
    | FacebookProfilePostsResponse503
]:
    """Fetch Facebook page posts

     Fetches a page of public posts from a Facebook page or profile, with link previews and video
    details. Returns a few posts per page; use the response's `nextPageToken` to retrieve subsequent
    pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookProfilePostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookProfilePostsResponse200 | FacebookProfilePostsResponse400 | FacebookProfilePostsResponse401 | FacebookProfilePostsResponse402 | FacebookProfilePostsResponse403 | FacebookProfilePostsResponse404 | FacebookProfilePostsResponse422 | FacebookProfilePostsResponse429 | FacebookProfilePostsResponse500 | FacebookProfilePostsResponse503]
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
    body: FacebookProfilePostsBody,
) -> (
    FacebookProfilePostsResponse200
    | FacebookProfilePostsResponse400
    | FacebookProfilePostsResponse401
    | FacebookProfilePostsResponse402
    | FacebookProfilePostsResponse403
    | FacebookProfilePostsResponse404
    | FacebookProfilePostsResponse422
    | FacebookProfilePostsResponse429
    | FacebookProfilePostsResponse500
    | FacebookProfilePostsResponse503
    | None
):
    """Fetch Facebook page posts

     Fetches a page of public posts from a Facebook page or profile, with link previews and video
    details. Returns a few posts per page; use the response's `nextPageToken` to retrieve subsequent
    pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookProfilePostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookProfilePostsResponse200 | FacebookProfilePostsResponse400 | FacebookProfilePostsResponse401 | FacebookProfilePostsResponse402 | FacebookProfilePostsResponse403 | FacebookProfilePostsResponse404 | FacebookProfilePostsResponse422 | FacebookProfilePostsResponse429 | FacebookProfilePostsResponse500 | FacebookProfilePostsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookProfilePostsBody,
) -> Response[
    FacebookProfilePostsResponse200
    | FacebookProfilePostsResponse400
    | FacebookProfilePostsResponse401
    | FacebookProfilePostsResponse402
    | FacebookProfilePostsResponse403
    | FacebookProfilePostsResponse404
    | FacebookProfilePostsResponse422
    | FacebookProfilePostsResponse429
    | FacebookProfilePostsResponse500
    | FacebookProfilePostsResponse503
]:
    """Fetch Facebook page posts

     Fetches a page of public posts from a Facebook page or profile, with link previews and video
    details. Returns a few posts per page; use the response's `nextPageToken` to retrieve subsequent
    pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookProfilePostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookProfilePostsResponse200 | FacebookProfilePostsResponse400 | FacebookProfilePostsResponse401 | FacebookProfilePostsResponse402 | FacebookProfilePostsResponse403 | FacebookProfilePostsResponse404 | FacebookProfilePostsResponse422 | FacebookProfilePostsResponse429 | FacebookProfilePostsResponse500 | FacebookProfilePostsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookProfilePostsBody,
) -> (
    FacebookProfilePostsResponse200
    | FacebookProfilePostsResponse400
    | FacebookProfilePostsResponse401
    | FacebookProfilePostsResponse402
    | FacebookProfilePostsResponse403
    | FacebookProfilePostsResponse404
    | FacebookProfilePostsResponse422
    | FacebookProfilePostsResponse429
    | FacebookProfilePostsResponse500
    | FacebookProfilePostsResponse503
    | None
):
    """Fetch Facebook page posts

     Fetches a page of public posts from a Facebook page or profile, with link previews and video
    details. Returns a few posts per page; use the response's `nextPageToken` to retrieve subsequent
    pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookProfilePostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookProfilePostsResponse200 | FacebookProfilePostsResponse400 | FacebookProfilePostsResponse401 | FacebookProfilePostsResponse402 | FacebookProfilePostsResponse403 | FacebookProfilePostsResponse404 | FacebookProfilePostsResponse422 | FacebookProfilePostsResponse429 | FacebookProfilePostsResponse500 | FacebookProfilePostsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
