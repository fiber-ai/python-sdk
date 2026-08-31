from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.instagram_post_comments_body import InstagramPostCommentsBody
from ...models.instagram_post_comments_response_200 import InstagramPostCommentsResponse200
from ...models.instagram_post_comments_response_400 import InstagramPostCommentsResponse400
from ...models.instagram_post_comments_response_401 import InstagramPostCommentsResponse401
from ...models.instagram_post_comments_response_402 import InstagramPostCommentsResponse402
from ...models.instagram_post_comments_response_403 import InstagramPostCommentsResponse403
from ...models.instagram_post_comments_response_404 import InstagramPostCommentsResponse404
from ...models.instagram_post_comments_response_422 import InstagramPostCommentsResponse422
from ...models.instagram_post_comments_response_429 import InstagramPostCommentsResponse429
from ...models.instagram_post_comments_response_500 import InstagramPostCommentsResponse500
from ...models.instagram_post_comments_response_503 import InstagramPostCommentsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: InstagramPostCommentsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/instagram/post-comments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InstagramPostCommentsResponse200
    | InstagramPostCommentsResponse400
    | InstagramPostCommentsResponse401
    | InstagramPostCommentsResponse402
    | InstagramPostCommentsResponse403
    | InstagramPostCommentsResponse404
    | InstagramPostCommentsResponse422
    | InstagramPostCommentsResponse429
    | InstagramPostCommentsResponse500
    | InstagramPostCommentsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = InstagramPostCommentsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InstagramPostCommentsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = InstagramPostCommentsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = InstagramPostCommentsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = InstagramPostCommentsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = InstagramPostCommentsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = InstagramPostCommentsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = InstagramPostCommentsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = InstagramPostCommentsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = InstagramPostCommentsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InstagramPostCommentsResponse200
    | InstagramPostCommentsResponse400
    | InstagramPostCommentsResponse401
    | InstagramPostCommentsResponse402
    | InstagramPostCommentsResponse403
    | InstagramPostCommentsResponse404
    | InstagramPostCommentsResponse422
    | InstagramPostCommentsResponse429
    | InstagramPostCommentsResponse500
    | InstagramPostCommentsResponse503
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
    body: InstagramPostCommentsBody,
) -> Response[
    InstagramPostCommentsResponse200
    | InstagramPostCommentsResponse400
    | InstagramPostCommentsResponse401
    | InstagramPostCommentsResponse402
    | InstagramPostCommentsResponse403
    | InstagramPostCommentsResponse404
    | InstagramPostCommentsResponse422
    | InstagramPostCommentsResponse429
    | InstagramPostCommentsResponse500
    | InstagramPostCommentsResponse503
]:
    """Fetch Instagram post comments

     Fetches comments for an Instagram post. Returns a paginated list. Use the `nextPageToken` field from
    the response to retrieve subsequent pages. Accepts a full post URL (e.g.
    'https://www.instagram.com/p/DVoDVg5DkXM/') or a bare shortcode (e.g. 'DVoDVg5DkXM').

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (InstagramPostCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstagramPostCommentsResponse200 | InstagramPostCommentsResponse400 | InstagramPostCommentsResponse401 | InstagramPostCommentsResponse402 | InstagramPostCommentsResponse403 | InstagramPostCommentsResponse404 | InstagramPostCommentsResponse422 | InstagramPostCommentsResponse429 | InstagramPostCommentsResponse500 | InstagramPostCommentsResponse503]
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
    body: InstagramPostCommentsBody,
) -> (
    InstagramPostCommentsResponse200
    | InstagramPostCommentsResponse400
    | InstagramPostCommentsResponse401
    | InstagramPostCommentsResponse402
    | InstagramPostCommentsResponse403
    | InstagramPostCommentsResponse404
    | InstagramPostCommentsResponse422
    | InstagramPostCommentsResponse429
    | InstagramPostCommentsResponse500
    | InstagramPostCommentsResponse503
    | None
):
    """Fetch Instagram post comments

     Fetches comments for an Instagram post. Returns a paginated list. Use the `nextPageToken` field from
    the response to retrieve subsequent pages. Accepts a full post URL (e.g.
    'https://www.instagram.com/p/DVoDVg5DkXM/') or a bare shortcode (e.g. 'DVoDVg5DkXM').

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (InstagramPostCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstagramPostCommentsResponse200 | InstagramPostCommentsResponse400 | InstagramPostCommentsResponse401 | InstagramPostCommentsResponse402 | InstagramPostCommentsResponse403 | InstagramPostCommentsResponse404 | InstagramPostCommentsResponse422 | InstagramPostCommentsResponse429 | InstagramPostCommentsResponse500 | InstagramPostCommentsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InstagramPostCommentsBody,
) -> Response[
    InstagramPostCommentsResponse200
    | InstagramPostCommentsResponse400
    | InstagramPostCommentsResponse401
    | InstagramPostCommentsResponse402
    | InstagramPostCommentsResponse403
    | InstagramPostCommentsResponse404
    | InstagramPostCommentsResponse422
    | InstagramPostCommentsResponse429
    | InstagramPostCommentsResponse500
    | InstagramPostCommentsResponse503
]:
    """Fetch Instagram post comments

     Fetches comments for an Instagram post. Returns a paginated list. Use the `nextPageToken` field from
    the response to retrieve subsequent pages. Accepts a full post URL (e.g.
    'https://www.instagram.com/p/DVoDVg5DkXM/') or a bare shortcode (e.g. 'DVoDVg5DkXM').

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (InstagramPostCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstagramPostCommentsResponse200 | InstagramPostCommentsResponse400 | InstagramPostCommentsResponse401 | InstagramPostCommentsResponse402 | InstagramPostCommentsResponse403 | InstagramPostCommentsResponse404 | InstagramPostCommentsResponse422 | InstagramPostCommentsResponse429 | InstagramPostCommentsResponse500 | InstagramPostCommentsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: InstagramPostCommentsBody,
) -> (
    InstagramPostCommentsResponse200
    | InstagramPostCommentsResponse400
    | InstagramPostCommentsResponse401
    | InstagramPostCommentsResponse402
    | InstagramPostCommentsResponse403
    | InstagramPostCommentsResponse404
    | InstagramPostCommentsResponse422
    | InstagramPostCommentsResponse429
    | InstagramPostCommentsResponse500
    | InstagramPostCommentsResponse503
    | None
):
    """Fetch Instagram post comments

     Fetches comments for an Instagram post. Returns a paginated list. Use the `nextPageToken` field from
    the response to retrieve subsequent pages. Accepts a full post URL (e.g.
    'https://www.instagram.com/p/DVoDVg5DkXM/') or a bare shortcode (e.g. 'DVoDVg5DkXM').

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (InstagramPostCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstagramPostCommentsResponse200 | InstagramPostCommentsResponse400 | InstagramPostCommentsResponse401 | InstagramPostCommentsResponse402 | InstagramPostCommentsResponse403 | InstagramPostCommentsResponse404 | InstagramPostCommentsResponse422 | InstagramPostCommentsResponse429 | InstagramPostCommentsResponse500 | InstagramPostCommentsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
