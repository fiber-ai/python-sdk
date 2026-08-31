from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reddit_subreddit_posts_body import RedditSubredditPostsBody
from ...models.reddit_subreddit_posts_response_200 import RedditSubredditPostsResponse200
from ...models.reddit_subreddit_posts_response_400 import RedditSubredditPostsResponse400
from ...models.reddit_subreddit_posts_response_401 import RedditSubredditPostsResponse401
from ...models.reddit_subreddit_posts_response_402 import RedditSubredditPostsResponse402
from ...models.reddit_subreddit_posts_response_403 import RedditSubredditPostsResponse403
from ...models.reddit_subreddit_posts_response_404 import RedditSubredditPostsResponse404
from ...models.reddit_subreddit_posts_response_422 import RedditSubredditPostsResponse422
from ...models.reddit_subreddit_posts_response_429 import RedditSubredditPostsResponse429
from ...models.reddit_subreddit_posts_response_500 import RedditSubredditPostsResponse500
from ...models.reddit_subreddit_posts_response_503 import RedditSubredditPostsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: RedditSubredditPostsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/reddit/subreddit/posts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RedditSubredditPostsResponse200
    | RedditSubredditPostsResponse400
    | RedditSubredditPostsResponse401
    | RedditSubredditPostsResponse402
    | RedditSubredditPostsResponse403
    | RedditSubredditPostsResponse404
    | RedditSubredditPostsResponse422
    | RedditSubredditPostsResponse429
    | RedditSubredditPostsResponse500
    | RedditSubredditPostsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = RedditSubredditPostsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RedditSubredditPostsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RedditSubredditPostsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = RedditSubredditPostsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = RedditSubredditPostsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RedditSubredditPostsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = RedditSubredditPostsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = RedditSubredditPostsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RedditSubredditPostsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RedditSubredditPostsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RedditSubredditPostsResponse200
    | RedditSubredditPostsResponse400
    | RedditSubredditPostsResponse401
    | RedditSubredditPostsResponse402
    | RedditSubredditPostsResponse403
    | RedditSubredditPostsResponse404
    | RedditSubredditPostsResponse422
    | RedditSubredditPostsResponse429
    | RedditSubredditPostsResponse500
    | RedditSubredditPostsResponse503
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
    body: RedditSubredditPostsBody,
) -> Response[
    RedditSubredditPostsResponse200
    | RedditSubredditPostsResponse400
    | RedditSubredditPostsResponse401
    | RedditSubredditPostsResponse402
    | RedditSubredditPostsResponse403
    | RedditSubredditPostsResponse404
    | RedditSubredditPostsResponse422
    | RedditSubredditPostsResponse429
    | RedditSubredditPostsResponse500
    | RedditSubredditPostsResponse503
]:
    """List subreddit posts

     List posts from a subreddit, optionally filtered by sort order and timeframe. Returns a paginated
    list of posts. Use the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (RedditSubredditPostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RedditSubredditPostsResponse200 | RedditSubredditPostsResponse400 | RedditSubredditPostsResponse401 | RedditSubredditPostsResponse402 | RedditSubredditPostsResponse403 | RedditSubredditPostsResponse404 | RedditSubredditPostsResponse422 | RedditSubredditPostsResponse429 | RedditSubredditPostsResponse500 | RedditSubredditPostsResponse503]
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
    body: RedditSubredditPostsBody,
) -> (
    RedditSubredditPostsResponse200
    | RedditSubredditPostsResponse400
    | RedditSubredditPostsResponse401
    | RedditSubredditPostsResponse402
    | RedditSubredditPostsResponse403
    | RedditSubredditPostsResponse404
    | RedditSubredditPostsResponse422
    | RedditSubredditPostsResponse429
    | RedditSubredditPostsResponse500
    | RedditSubredditPostsResponse503
    | None
):
    """List subreddit posts

     List posts from a subreddit, optionally filtered by sort order and timeframe. Returns a paginated
    list of posts. Use the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (RedditSubredditPostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RedditSubredditPostsResponse200 | RedditSubredditPostsResponse400 | RedditSubredditPostsResponse401 | RedditSubredditPostsResponse402 | RedditSubredditPostsResponse403 | RedditSubredditPostsResponse404 | RedditSubredditPostsResponse422 | RedditSubredditPostsResponse429 | RedditSubredditPostsResponse500 | RedditSubredditPostsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RedditSubredditPostsBody,
) -> Response[
    RedditSubredditPostsResponse200
    | RedditSubredditPostsResponse400
    | RedditSubredditPostsResponse401
    | RedditSubredditPostsResponse402
    | RedditSubredditPostsResponse403
    | RedditSubredditPostsResponse404
    | RedditSubredditPostsResponse422
    | RedditSubredditPostsResponse429
    | RedditSubredditPostsResponse500
    | RedditSubredditPostsResponse503
]:
    """List subreddit posts

     List posts from a subreddit, optionally filtered by sort order and timeframe. Returns a paginated
    list of posts. Use the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (RedditSubredditPostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RedditSubredditPostsResponse200 | RedditSubredditPostsResponse400 | RedditSubredditPostsResponse401 | RedditSubredditPostsResponse402 | RedditSubredditPostsResponse403 | RedditSubredditPostsResponse404 | RedditSubredditPostsResponse422 | RedditSubredditPostsResponse429 | RedditSubredditPostsResponse500 | RedditSubredditPostsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RedditSubredditPostsBody,
) -> (
    RedditSubredditPostsResponse200
    | RedditSubredditPostsResponse400
    | RedditSubredditPostsResponse401
    | RedditSubredditPostsResponse402
    | RedditSubredditPostsResponse403
    | RedditSubredditPostsResponse404
    | RedditSubredditPostsResponse422
    | RedditSubredditPostsResponse429
    | RedditSubredditPostsResponse500
    | RedditSubredditPostsResponse503
    | None
):
    """List subreddit posts

     List posts from a subreddit, optionally filtered by sort order and timeframe. Returns a paginated
    list of posts. Use the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (RedditSubredditPostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RedditSubredditPostsResponse200 | RedditSubredditPostsResponse400 | RedditSubredditPostsResponse401 | RedditSubredditPostsResponse402 | RedditSubredditPostsResponse403 | RedditSubredditPostsResponse404 | RedditSubredditPostsResponse422 | RedditSubredditPostsResponse429 | RedditSubredditPostsResponse500 | RedditSubredditPostsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
