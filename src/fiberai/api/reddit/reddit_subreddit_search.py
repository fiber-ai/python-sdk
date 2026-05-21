from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reddit_subreddit_search_body import RedditSubredditSearchBody
from ...models.reddit_subreddit_search_response_200 import RedditSubredditSearchResponse200
from ...models.reddit_subreddit_search_response_400 import RedditSubredditSearchResponse400
from ...models.reddit_subreddit_search_response_401 import RedditSubredditSearchResponse401
from ...models.reddit_subreddit_search_response_402 import RedditSubredditSearchResponse402
from ...models.reddit_subreddit_search_response_403 import RedditSubredditSearchResponse403
from ...models.reddit_subreddit_search_response_404 import RedditSubredditSearchResponse404
from ...models.reddit_subreddit_search_response_429 import RedditSubredditSearchResponse429
from ...models.reddit_subreddit_search_response_500 import RedditSubredditSearchResponse500
from ...models.reddit_subreddit_search_response_503 import RedditSubredditSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: RedditSubredditSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/reddit/subreddit/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RedditSubredditSearchResponse200
    | RedditSubredditSearchResponse400
    | RedditSubredditSearchResponse401
    | RedditSubredditSearchResponse402
    | RedditSubredditSearchResponse403
    | RedditSubredditSearchResponse404
    | RedditSubredditSearchResponse429
    | RedditSubredditSearchResponse500
    | RedditSubredditSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = RedditSubredditSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RedditSubredditSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RedditSubredditSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = RedditSubredditSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = RedditSubredditSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RedditSubredditSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = RedditSubredditSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RedditSubredditSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RedditSubredditSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RedditSubredditSearchResponse200
    | RedditSubredditSearchResponse400
    | RedditSubredditSearchResponse401
    | RedditSubredditSearchResponse402
    | RedditSubredditSearchResponse403
    | RedditSubredditSearchResponse404
    | RedditSubredditSearchResponse429
    | RedditSubredditSearchResponse500
    | RedditSubredditSearchResponse503
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
    body: RedditSubredditSearchBody,
) -> Response[
    RedditSubredditSearchResponse200
    | RedditSubredditSearchResponse400
    | RedditSubredditSearchResponse401
    | RedditSubredditSearchResponse402
    | RedditSubredditSearchResponse403
    | RedditSubredditSearchResponse404
    | RedditSubredditSearchResponse429
    | RedditSubredditSearchResponse500
    | RedditSubredditSearchResponse503
]:
    r"""Search within a subreddit

     Search posts within a subreddit by query, optionally filtered by sort order and timeframe. Returns a
    paginated list of posts. Use the `nextPageToken` field from the response to retrieve subsequent
    pages.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (RedditSubredditSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RedditSubredditSearchResponse200 | RedditSubredditSearchResponse400 | RedditSubredditSearchResponse401 | RedditSubredditSearchResponse402 | RedditSubredditSearchResponse403 | RedditSubredditSearchResponse404 | RedditSubredditSearchResponse429 | RedditSubredditSearchResponse500 | RedditSubredditSearchResponse503]
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
    body: RedditSubredditSearchBody,
) -> (
    RedditSubredditSearchResponse200
    | RedditSubredditSearchResponse400
    | RedditSubredditSearchResponse401
    | RedditSubredditSearchResponse402
    | RedditSubredditSearchResponse403
    | RedditSubredditSearchResponse404
    | RedditSubredditSearchResponse429
    | RedditSubredditSearchResponse500
    | RedditSubredditSearchResponse503
    | None
):
    r"""Search within a subreddit

     Search posts within a subreddit by query, optionally filtered by sort order and timeframe. Returns a
    paginated list of posts. Use the `nextPageToken` field from the response to retrieve subsequent
    pages.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (RedditSubredditSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RedditSubredditSearchResponse200 | RedditSubredditSearchResponse400 | RedditSubredditSearchResponse401 | RedditSubredditSearchResponse402 | RedditSubredditSearchResponse403 | RedditSubredditSearchResponse404 | RedditSubredditSearchResponse429 | RedditSubredditSearchResponse500 | RedditSubredditSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RedditSubredditSearchBody,
) -> Response[
    RedditSubredditSearchResponse200
    | RedditSubredditSearchResponse400
    | RedditSubredditSearchResponse401
    | RedditSubredditSearchResponse402
    | RedditSubredditSearchResponse403
    | RedditSubredditSearchResponse404
    | RedditSubredditSearchResponse429
    | RedditSubredditSearchResponse500
    | RedditSubredditSearchResponse503
]:
    r"""Search within a subreddit

     Search posts within a subreddit by query, optionally filtered by sort order and timeframe. Returns a
    paginated list of posts. Use the `nextPageToken` field from the response to retrieve subsequent
    pages.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (RedditSubredditSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RedditSubredditSearchResponse200 | RedditSubredditSearchResponse400 | RedditSubredditSearchResponse401 | RedditSubredditSearchResponse402 | RedditSubredditSearchResponse403 | RedditSubredditSearchResponse404 | RedditSubredditSearchResponse429 | RedditSubredditSearchResponse500 | RedditSubredditSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RedditSubredditSearchBody,
) -> (
    RedditSubredditSearchResponse200
    | RedditSubredditSearchResponse400
    | RedditSubredditSearchResponse401
    | RedditSubredditSearchResponse402
    | RedditSubredditSearchResponse403
    | RedditSubredditSearchResponse404
    | RedditSubredditSearchResponse429
    | RedditSubredditSearchResponse500
    | RedditSubredditSearchResponse503
    | None
):
    r"""Search within a subreddit

     Search posts within a subreddit by query, optionally filtered by sort order and timeframe. Returns a
    paginated list of posts. Use the `nextPageToken` field from the response to retrieve subsequent
    pages.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (RedditSubredditSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RedditSubredditSearchResponse200 | RedditSubredditSearchResponse400 | RedditSubredditSearchResponse401 | RedditSubredditSearchResponse402 | RedditSubredditSearchResponse403 | RedditSubredditSearchResponse404 | RedditSubredditSearchResponse429 | RedditSubredditSearchResponse500 | RedditSubredditSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
