from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.facebook_group_posts_body import FacebookGroupPostsBody
from ...models.facebook_group_posts_response_200 import FacebookGroupPostsResponse200
from ...models.facebook_group_posts_response_400 import FacebookGroupPostsResponse400
from ...models.facebook_group_posts_response_401 import FacebookGroupPostsResponse401
from ...models.facebook_group_posts_response_402 import FacebookGroupPostsResponse402
from ...models.facebook_group_posts_response_403 import FacebookGroupPostsResponse403
from ...models.facebook_group_posts_response_404 import FacebookGroupPostsResponse404
from ...models.facebook_group_posts_response_422 import FacebookGroupPostsResponse422
from ...models.facebook_group_posts_response_429 import FacebookGroupPostsResponse429
from ...models.facebook_group_posts_response_500 import FacebookGroupPostsResponse500
from ...models.facebook_group_posts_response_503 import FacebookGroupPostsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: FacebookGroupPostsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/facebook/group/posts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FacebookGroupPostsResponse200
    | FacebookGroupPostsResponse400
    | FacebookGroupPostsResponse401
    | FacebookGroupPostsResponse402
    | FacebookGroupPostsResponse403
    | FacebookGroupPostsResponse404
    | FacebookGroupPostsResponse422
    | FacebookGroupPostsResponse429
    | FacebookGroupPostsResponse500
    | FacebookGroupPostsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = FacebookGroupPostsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FacebookGroupPostsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FacebookGroupPostsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = FacebookGroupPostsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = FacebookGroupPostsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FacebookGroupPostsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = FacebookGroupPostsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = FacebookGroupPostsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FacebookGroupPostsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = FacebookGroupPostsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FacebookGroupPostsResponse200
    | FacebookGroupPostsResponse400
    | FacebookGroupPostsResponse401
    | FacebookGroupPostsResponse402
    | FacebookGroupPostsResponse403
    | FacebookGroupPostsResponse404
    | FacebookGroupPostsResponse422
    | FacebookGroupPostsResponse429
    | FacebookGroupPostsResponse500
    | FacebookGroupPostsResponse503
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
    body: FacebookGroupPostsBody,
) -> Response[
    FacebookGroupPostsResponse200
    | FacebookGroupPostsResponse400
    | FacebookGroupPostsResponse401
    | FacebookGroupPostsResponse402
    | FacebookGroupPostsResponse403
    | FacebookGroupPostsResponse404
    | FacebookGroupPostsResponse422
    | FacebookGroupPostsResponse429
    | FacebookGroupPostsResponse500
    | FacebookGroupPostsResponse503
]:
    """Fetch Facebook group posts

     Fetches a page of posts from a public Facebook group. Returns a few posts per page; use the
    response's `nextPageToken` to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookGroupPostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookGroupPostsResponse200 | FacebookGroupPostsResponse400 | FacebookGroupPostsResponse401 | FacebookGroupPostsResponse402 | FacebookGroupPostsResponse403 | FacebookGroupPostsResponse404 | FacebookGroupPostsResponse422 | FacebookGroupPostsResponse429 | FacebookGroupPostsResponse500 | FacebookGroupPostsResponse503]
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
    body: FacebookGroupPostsBody,
) -> (
    FacebookGroupPostsResponse200
    | FacebookGroupPostsResponse400
    | FacebookGroupPostsResponse401
    | FacebookGroupPostsResponse402
    | FacebookGroupPostsResponse403
    | FacebookGroupPostsResponse404
    | FacebookGroupPostsResponse422
    | FacebookGroupPostsResponse429
    | FacebookGroupPostsResponse500
    | FacebookGroupPostsResponse503
    | None
):
    """Fetch Facebook group posts

     Fetches a page of posts from a public Facebook group. Returns a few posts per page; use the
    response's `nextPageToken` to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookGroupPostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookGroupPostsResponse200 | FacebookGroupPostsResponse400 | FacebookGroupPostsResponse401 | FacebookGroupPostsResponse402 | FacebookGroupPostsResponse403 | FacebookGroupPostsResponse404 | FacebookGroupPostsResponse422 | FacebookGroupPostsResponse429 | FacebookGroupPostsResponse500 | FacebookGroupPostsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookGroupPostsBody,
) -> Response[
    FacebookGroupPostsResponse200
    | FacebookGroupPostsResponse400
    | FacebookGroupPostsResponse401
    | FacebookGroupPostsResponse402
    | FacebookGroupPostsResponse403
    | FacebookGroupPostsResponse404
    | FacebookGroupPostsResponse422
    | FacebookGroupPostsResponse429
    | FacebookGroupPostsResponse500
    | FacebookGroupPostsResponse503
]:
    """Fetch Facebook group posts

     Fetches a page of posts from a public Facebook group. Returns a few posts per page; use the
    response's `nextPageToken` to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookGroupPostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookGroupPostsResponse200 | FacebookGroupPostsResponse400 | FacebookGroupPostsResponse401 | FacebookGroupPostsResponse402 | FacebookGroupPostsResponse403 | FacebookGroupPostsResponse404 | FacebookGroupPostsResponse422 | FacebookGroupPostsResponse429 | FacebookGroupPostsResponse500 | FacebookGroupPostsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookGroupPostsBody,
) -> (
    FacebookGroupPostsResponse200
    | FacebookGroupPostsResponse400
    | FacebookGroupPostsResponse401
    | FacebookGroupPostsResponse402
    | FacebookGroupPostsResponse403
    | FacebookGroupPostsResponse404
    | FacebookGroupPostsResponse422
    | FacebookGroupPostsResponse429
    | FacebookGroupPostsResponse500
    | FacebookGroupPostsResponse503
    | None
):
    """Fetch Facebook group posts

     Fetches a page of posts from a public Facebook group. Returns a few posts per page; use the
    response's `nextPageToken` to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookGroupPostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookGroupPostsResponse200 | FacebookGroupPostsResponse400 | FacebookGroupPostsResponse401 | FacebookGroupPostsResponse402 | FacebookGroupPostsResponse403 | FacebookGroupPostsResponse404 | FacebookGroupPostsResponse422 | FacebookGroupPostsResponse429 | FacebookGroupPostsResponse500 | FacebookGroupPostsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
