from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reddit_search_body import RedditSearchBody
from ...models.reddit_search_response_200 import RedditSearchResponse200
from ...models.reddit_search_response_400 import RedditSearchResponse400
from ...models.reddit_search_response_401 import RedditSearchResponse401
from ...models.reddit_search_response_402 import RedditSearchResponse402
from ...models.reddit_search_response_403 import RedditSearchResponse403
from ...models.reddit_search_response_404 import RedditSearchResponse404
from ...models.reddit_search_response_422 import RedditSearchResponse422
from ...models.reddit_search_response_429 import RedditSearchResponse429
from ...models.reddit_search_response_500 import RedditSearchResponse500
from ...models.reddit_search_response_503 import RedditSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: RedditSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/reddit/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RedditSearchResponse200
    | RedditSearchResponse400
    | RedditSearchResponse401
    | RedditSearchResponse402
    | RedditSearchResponse403
    | RedditSearchResponse404
    | RedditSearchResponse422
    | RedditSearchResponse429
    | RedditSearchResponse500
    | RedditSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = RedditSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RedditSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RedditSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = RedditSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = RedditSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RedditSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = RedditSearchResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = RedditSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RedditSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RedditSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RedditSearchResponse200
    | RedditSearchResponse400
    | RedditSearchResponse401
    | RedditSearchResponse402
    | RedditSearchResponse403
    | RedditSearchResponse404
    | RedditSearchResponse422
    | RedditSearchResponse429
    | RedditSearchResponse500
    | RedditSearchResponse503
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
    body: RedditSearchBody,
) -> Response[
    RedditSearchResponse200
    | RedditSearchResponse400
    | RedditSearchResponse401
    | RedditSearchResponse402
    | RedditSearchResponse403
    | RedditSearchResponse404
    | RedditSearchResponse422
    | RedditSearchResponse429
    | RedditSearchResponse500
    | RedditSearchResponse503
]:
    r"""Search Reddit posts

     Search Reddit posts across all subreddits by query, optionally filtered by sort order and timeframe.
    Returns a paginated list of posts. Use the `nextPageToken` field from the response to retrieve
    subsequent pages. Queries with no matching posts return an empty list and are not charged credits.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (RedditSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RedditSearchResponse200 | RedditSearchResponse400 | RedditSearchResponse401 | RedditSearchResponse402 | RedditSearchResponse403 | RedditSearchResponse404 | RedditSearchResponse422 | RedditSearchResponse429 | RedditSearchResponse500 | RedditSearchResponse503]
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
    body: RedditSearchBody,
) -> (
    RedditSearchResponse200
    | RedditSearchResponse400
    | RedditSearchResponse401
    | RedditSearchResponse402
    | RedditSearchResponse403
    | RedditSearchResponse404
    | RedditSearchResponse422
    | RedditSearchResponse429
    | RedditSearchResponse500
    | RedditSearchResponse503
    | None
):
    r"""Search Reddit posts

     Search Reddit posts across all subreddits by query, optionally filtered by sort order and timeframe.
    Returns a paginated list of posts. Use the `nextPageToken` field from the response to retrieve
    subsequent pages. Queries with no matching posts return an empty list and are not charged credits.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (RedditSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RedditSearchResponse200 | RedditSearchResponse400 | RedditSearchResponse401 | RedditSearchResponse402 | RedditSearchResponse403 | RedditSearchResponse404 | RedditSearchResponse422 | RedditSearchResponse429 | RedditSearchResponse500 | RedditSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RedditSearchBody,
) -> Response[
    RedditSearchResponse200
    | RedditSearchResponse400
    | RedditSearchResponse401
    | RedditSearchResponse402
    | RedditSearchResponse403
    | RedditSearchResponse404
    | RedditSearchResponse422
    | RedditSearchResponse429
    | RedditSearchResponse500
    | RedditSearchResponse503
]:
    r"""Search Reddit posts

     Search Reddit posts across all subreddits by query, optionally filtered by sort order and timeframe.
    Returns a paginated list of posts. Use the `nextPageToken` field from the response to retrieve
    subsequent pages. Queries with no matching posts return an empty list and are not charged credits.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (RedditSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RedditSearchResponse200 | RedditSearchResponse400 | RedditSearchResponse401 | RedditSearchResponse402 | RedditSearchResponse403 | RedditSearchResponse404 | RedditSearchResponse422 | RedditSearchResponse429 | RedditSearchResponse500 | RedditSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RedditSearchBody,
) -> (
    RedditSearchResponse200
    | RedditSearchResponse400
    | RedditSearchResponse401
    | RedditSearchResponse402
    | RedditSearchResponse403
    | RedditSearchResponse404
    | RedditSearchResponse422
    | RedditSearchResponse429
    | RedditSearchResponse500
    | RedditSearchResponse503
    | None
):
    r"""Search Reddit posts

     Search Reddit posts across all subreddits by query, optionally filtered by sort order and timeframe.
    Returns a paginated list of posts. Use the `nextPageToken` field from the response to retrieve
    subsequent pages. Queries with no matching posts return an empty list and are not charged credits.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (RedditSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RedditSearchResponse200 | RedditSearchResponse400 | RedditSearchResponse401 | RedditSearchResponse402 | RedditSearchResponse403 | RedditSearchResponse404 | RedditSearchResponse422 | RedditSearchResponse429 | RedditSearchResponse500 | RedditSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
