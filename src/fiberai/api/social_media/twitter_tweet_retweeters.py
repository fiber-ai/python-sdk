from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.twitter_tweet_retweeters_body import TwitterTweetRetweetersBody
from ...models.twitter_tweet_retweeters_response_200 import TwitterTweetRetweetersResponse200
from ...models.twitter_tweet_retweeters_response_400 import TwitterTweetRetweetersResponse400
from ...models.twitter_tweet_retweeters_response_401 import TwitterTweetRetweetersResponse401
from ...models.twitter_tweet_retweeters_response_402 import TwitterTweetRetweetersResponse402
from ...models.twitter_tweet_retweeters_response_403 import TwitterTweetRetweetersResponse403
from ...models.twitter_tweet_retweeters_response_404 import TwitterTweetRetweetersResponse404
from ...models.twitter_tweet_retweeters_response_429 import TwitterTweetRetweetersResponse429
from ...models.twitter_tweet_retweeters_response_500 import TwitterTweetRetweetersResponse500
from ...models.twitter_tweet_retweeters_response_503 import TwitterTweetRetweetersResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TwitterTweetRetweetersBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/twitter/tweet-retweeters",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TwitterTweetRetweetersResponse200
    | TwitterTweetRetweetersResponse400
    | TwitterTweetRetweetersResponse401
    | TwitterTweetRetweetersResponse402
    | TwitterTweetRetweetersResponse403
    | TwitterTweetRetweetersResponse404
    | TwitterTweetRetweetersResponse429
    | TwitterTweetRetweetersResponse500
    | TwitterTweetRetweetersResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TwitterTweetRetweetersResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TwitterTweetRetweetersResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TwitterTweetRetweetersResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TwitterTweetRetweetersResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TwitterTweetRetweetersResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TwitterTweetRetweetersResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TwitterTweetRetweetersResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TwitterTweetRetweetersResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TwitterTweetRetweetersResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TwitterTweetRetweetersResponse200
    | TwitterTweetRetweetersResponse400
    | TwitterTweetRetweetersResponse401
    | TwitterTweetRetweetersResponse402
    | TwitterTweetRetweetersResponse403
    | TwitterTweetRetweetersResponse404
    | TwitterTweetRetweetersResponse429
    | TwitterTweetRetweetersResponse500
    | TwitterTweetRetweetersResponse503
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
    body: TwitterTweetRetweetersBody,
) -> Response[
    TwitterTweetRetweetersResponse200
    | TwitterTweetRetweetersResponse400
    | TwitterTweetRetweetersResponse401
    | TwitterTweetRetweetersResponse402
    | TwitterTweetRetweetersResponse403
    | TwitterTweetRetweetersResponse404
    | TwitterTweetRetweetersResponse429
    | TwitterTweetRetweetersResponse500
    | TwitterTweetRetweetersResponse503
]:
    r"""Fetch Twitter/X tweet retweeters

     Fetches a page of users who retweeted a tweet. Use the `cursor` field from the response to retrieve
    subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterTweetRetweetersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwitterTweetRetweetersResponse200 | TwitterTweetRetweetersResponse400 | TwitterTweetRetweetersResponse401 | TwitterTweetRetweetersResponse402 | TwitterTweetRetweetersResponse403 | TwitterTweetRetweetersResponse404 | TwitterTweetRetweetersResponse429 | TwitterTweetRetweetersResponse500 | TwitterTweetRetweetersResponse503]
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
    body: TwitterTweetRetweetersBody,
) -> (
    TwitterTweetRetweetersResponse200
    | TwitterTweetRetweetersResponse400
    | TwitterTweetRetweetersResponse401
    | TwitterTweetRetweetersResponse402
    | TwitterTweetRetweetersResponse403
    | TwitterTweetRetweetersResponse404
    | TwitterTweetRetweetersResponse429
    | TwitterTweetRetweetersResponse500
    | TwitterTweetRetweetersResponse503
    | None
):
    r"""Fetch Twitter/X tweet retweeters

     Fetches a page of users who retweeted a tweet. Use the `cursor` field from the response to retrieve
    subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterTweetRetweetersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwitterTweetRetweetersResponse200 | TwitterTweetRetweetersResponse400 | TwitterTweetRetweetersResponse401 | TwitterTweetRetweetersResponse402 | TwitterTweetRetweetersResponse403 | TwitterTweetRetweetersResponse404 | TwitterTweetRetweetersResponse429 | TwitterTweetRetweetersResponse500 | TwitterTweetRetweetersResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TwitterTweetRetweetersBody,
) -> Response[
    TwitterTweetRetweetersResponse200
    | TwitterTweetRetweetersResponse400
    | TwitterTweetRetweetersResponse401
    | TwitterTweetRetweetersResponse402
    | TwitterTweetRetweetersResponse403
    | TwitterTweetRetweetersResponse404
    | TwitterTweetRetweetersResponse429
    | TwitterTweetRetweetersResponse500
    | TwitterTweetRetweetersResponse503
]:
    r"""Fetch Twitter/X tweet retweeters

     Fetches a page of users who retweeted a tweet. Use the `cursor` field from the response to retrieve
    subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterTweetRetweetersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwitterTweetRetweetersResponse200 | TwitterTweetRetweetersResponse400 | TwitterTweetRetweetersResponse401 | TwitterTweetRetweetersResponse402 | TwitterTweetRetweetersResponse403 | TwitterTweetRetweetersResponse404 | TwitterTweetRetweetersResponse429 | TwitterTweetRetweetersResponse500 | TwitterTweetRetweetersResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TwitterTweetRetweetersBody,
) -> (
    TwitterTweetRetweetersResponse200
    | TwitterTweetRetweetersResponse400
    | TwitterTweetRetweetersResponse401
    | TwitterTweetRetweetersResponse402
    | TwitterTweetRetweetersResponse403
    | TwitterTweetRetweetersResponse404
    | TwitterTweetRetweetersResponse429
    | TwitterTweetRetweetersResponse500
    | TwitterTweetRetweetersResponse503
    | None
):
    r"""Fetch Twitter/X tweet retweeters

     Fetches a page of users who retweeted a tweet. Use the `cursor` field from the response to retrieve
    subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterTweetRetweetersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwitterTweetRetweetersResponse200 | TwitterTweetRetweetersResponse400 | TwitterTweetRetweetersResponse401 | TwitterTweetRetweetersResponse402 | TwitterTweetRetweetersResponse403 | TwitterTweetRetweetersResponse404 | TwitterTweetRetweetersResponse429 | TwitterTweetRetweetersResponse500 | TwitterTweetRetweetersResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
