from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reddit_post_comments_body import RedditPostCommentsBody
from ...models.reddit_post_comments_response_200 import RedditPostCommentsResponse200
from ...models.reddit_post_comments_response_400 import RedditPostCommentsResponse400
from ...models.reddit_post_comments_response_401 import RedditPostCommentsResponse401
from ...models.reddit_post_comments_response_402 import RedditPostCommentsResponse402
from ...models.reddit_post_comments_response_403 import RedditPostCommentsResponse403
from ...models.reddit_post_comments_response_404 import RedditPostCommentsResponse404
from ...models.reddit_post_comments_response_422 import RedditPostCommentsResponse422
from ...models.reddit_post_comments_response_429 import RedditPostCommentsResponse429
from ...models.reddit_post_comments_response_500 import RedditPostCommentsResponse500
from ...models.reddit_post_comments_response_503 import RedditPostCommentsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: RedditPostCommentsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/reddit/post/comments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RedditPostCommentsResponse200
    | RedditPostCommentsResponse400
    | RedditPostCommentsResponse401
    | RedditPostCommentsResponse402
    | RedditPostCommentsResponse403
    | RedditPostCommentsResponse404
    | RedditPostCommentsResponse422
    | RedditPostCommentsResponse429
    | RedditPostCommentsResponse500
    | RedditPostCommentsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = RedditPostCommentsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RedditPostCommentsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RedditPostCommentsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = RedditPostCommentsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = RedditPostCommentsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RedditPostCommentsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = RedditPostCommentsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = RedditPostCommentsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RedditPostCommentsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RedditPostCommentsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RedditPostCommentsResponse200
    | RedditPostCommentsResponse400
    | RedditPostCommentsResponse401
    | RedditPostCommentsResponse402
    | RedditPostCommentsResponse403
    | RedditPostCommentsResponse404
    | RedditPostCommentsResponse422
    | RedditPostCommentsResponse429
    | RedditPostCommentsResponse500
    | RedditPostCommentsResponse503
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
    body: RedditPostCommentsBody,
) -> Response[
    RedditPostCommentsResponse200
    | RedditPostCommentsResponse400
    | RedditPostCommentsResponse401
    | RedditPostCommentsResponse402
    | RedditPostCommentsResponse403
    | RedditPostCommentsResponse404
    | RedditPostCommentsResponse422
    | RedditPostCommentsResponse429
    | RedditPostCommentsResponse500
    | RedditPostCommentsResponse503
]:
    """Fetch post comments

     Fetch comments for a Reddit post by URL or `t3_<id>` identifier. Returns the parent post (when
    available) and a paginated, depth-first flat list of comments that includes nested replies. Each
    entry's `parentCommentId` is null for top-level comments or points at the parent comment for
    replies; group on `parentCommentId` to rebuild the thread tree. Use the `nextPageToken` field from
    the response to retrieve subsequent pages of top-level comments (their nested replies come along
    automatically).

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (RedditPostCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RedditPostCommentsResponse200 | RedditPostCommentsResponse400 | RedditPostCommentsResponse401 | RedditPostCommentsResponse402 | RedditPostCommentsResponse403 | RedditPostCommentsResponse404 | RedditPostCommentsResponse422 | RedditPostCommentsResponse429 | RedditPostCommentsResponse500 | RedditPostCommentsResponse503]
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
    body: RedditPostCommentsBody,
) -> (
    RedditPostCommentsResponse200
    | RedditPostCommentsResponse400
    | RedditPostCommentsResponse401
    | RedditPostCommentsResponse402
    | RedditPostCommentsResponse403
    | RedditPostCommentsResponse404
    | RedditPostCommentsResponse422
    | RedditPostCommentsResponse429
    | RedditPostCommentsResponse500
    | RedditPostCommentsResponse503
    | None
):
    """Fetch post comments

     Fetch comments for a Reddit post by URL or `t3_<id>` identifier. Returns the parent post (when
    available) and a paginated, depth-first flat list of comments that includes nested replies. Each
    entry's `parentCommentId` is null for top-level comments or points at the parent comment for
    replies; group on `parentCommentId` to rebuild the thread tree. Use the `nextPageToken` field from
    the response to retrieve subsequent pages of top-level comments (their nested replies come along
    automatically).

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (RedditPostCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RedditPostCommentsResponse200 | RedditPostCommentsResponse400 | RedditPostCommentsResponse401 | RedditPostCommentsResponse402 | RedditPostCommentsResponse403 | RedditPostCommentsResponse404 | RedditPostCommentsResponse422 | RedditPostCommentsResponse429 | RedditPostCommentsResponse500 | RedditPostCommentsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RedditPostCommentsBody,
) -> Response[
    RedditPostCommentsResponse200
    | RedditPostCommentsResponse400
    | RedditPostCommentsResponse401
    | RedditPostCommentsResponse402
    | RedditPostCommentsResponse403
    | RedditPostCommentsResponse404
    | RedditPostCommentsResponse422
    | RedditPostCommentsResponse429
    | RedditPostCommentsResponse500
    | RedditPostCommentsResponse503
]:
    """Fetch post comments

     Fetch comments for a Reddit post by URL or `t3_<id>` identifier. Returns the parent post (when
    available) and a paginated, depth-first flat list of comments that includes nested replies. Each
    entry's `parentCommentId` is null for top-level comments or points at the parent comment for
    replies; group on `parentCommentId` to rebuild the thread tree. Use the `nextPageToken` field from
    the response to retrieve subsequent pages of top-level comments (their nested replies come along
    automatically).

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (RedditPostCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RedditPostCommentsResponse200 | RedditPostCommentsResponse400 | RedditPostCommentsResponse401 | RedditPostCommentsResponse402 | RedditPostCommentsResponse403 | RedditPostCommentsResponse404 | RedditPostCommentsResponse422 | RedditPostCommentsResponse429 | RedditPostCommentsResponse500 | RedditPostCommentsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RedditPostCommentsBody,
) -> (
    RedditPostCommentsResponse200
    | RedditPostCommentsResponse400
    | RedditPostCommentsResponse401
    | RedditPostCommentsResponse402
    | RedditPostCommentsResponse403
    | RedditPostCommentsResponse404
    | RedditPostCommentsResponse422
    | RedditPostCommentsResponse429
    | RedditPostCommentsResponse500
    | RedditPostCommentsResponse503
    | None
):
    """Fetch post comments

     Fetch comments for a Reddit post by URL or `t3_<id>` identifier. Returns the parent post (when
    available) and a paginated, depth-first flat list of comments that includes nested replies. Each
    entry's `parentCommentId` is null for top-level comments or points at the parent comment for
    replies; group on `parentCommentId` to rebuild the thread tree. Use the `nextPageToken` field from
    the response to retrieve subsequent pages of top-level comments (their nested replies come along
    automatically).

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (RedditPostCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RedditPostCommentsResponse200 | RedditPostCommentsResponse400 | RedditPostCommentsResponse401 | RedditPostCommentsResponse402 | RedditPostCommentsResponse403 | RedditPostCommentsResponse404 | RedditPostCommentsResponse422 | RedditPostCommentsResponse429 | RedditPostCommentsResponse500 | RedditPostCommentsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
