from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.twitter_tweet_replies_body import TwitterTweetRepliesBody
from ...models.twitter_tweet_replies_response_200 import TwitterTweetRepliesResponse200
from ...models.twitter_tweet_replies_response_400 import TwitterTweetRepliesResponse400
from ...models.twitter_tweet_replies_response_401 import TwitterTweetRepliesResponse401
from ...models.twitter_tweet_replies_response_402 import TwitterTweetRepliesResponse402
from ...models.twitter_tweet_replies_response_403 import TwitterTweetRepliesResponse403
from ...models.twitter_tweet_replies_response_404 import TwitterTweetRepliesResponse404
from ...models.twitter_tweet_replies_response_429 import TwitterTweetRepliesResponse429
from ...models.twitter_tweet_replies_response_500 import TwitterTweetRepliesResponse500
from ...models.twitter_tweet_replies_response_503 import TwitterTweetRepliesResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TwitterTweetRepliesBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/twitter/tweet-replies",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TwitterTweetRepliesResponse200
    | TwitterTweetRepliesResponse400
    | TwitterTweetRepliesResponse401
    | TwitterTweetRepliesResponse402
    | TwitterTweetRepliesResponse403
    | TwitterTweetRepliesResponse404
    | TwitterTweetRepliesResponse429
    | TwitterTweetRepliesResponse500
    | TwitterTweetRepliesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TwitterTweetRepliesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TwitterTweetRepliesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TwitterTweetRepliesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TwitterTweetRepliesResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TwitterTweetRepliesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TwitterTweetRepliesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TwitterTweetRepliesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TwitterTweetRepliesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TwitterTweetRepliesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TwitterTweetRepliesResponse200
    | TwitterTweetRepliesResponse400
    | TwitterTweetRepliesResponse401
    | TwitterTweetRepliesResponse402
    | TwitterTweetRepliesResponse403
    | TwitterTweetRepliesResponse404
    | TwitterTweetRepliesResponse429
    | TwitterTweetRepliesResponse500
    | TwitterTweetRepliesResponse503
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
    body: TwitterTweetRepliesBody,
) -> Response[
    TwitterTweetRepliesResponse200
    | TwitterTweetRepliesResponse400
    | TwitterTweetRepliesResponse401
    | TwitterTweetRepliesResponse402
    | TwitterTweetRepliesResponse403
    | TwitterTweetRepliesResponse404
    | TwitterTweetRepliesResponse429
    | TwitterTweetRepliesResponse500
    | TwitterTweetRepliesResponse503
]:
    r"""Fetch Twitter/X tweet replies

     Fetches a page of replies to a tweet. Use the `cursor` field from the response to retrieve
    subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterTweetRepliesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwitterTweetRepliesResponse200 | TwitterTweetRepliesResponse400 | TwitterTweetRepliesResponse401 | TwitterTweetRepliesResponse402 | TwitterTweetRepliesResponse403 | TwitterTweetRepliesResponse404 | TwitterTweetRepliesResponse429 | TwitterTweetRepliesResponse500 | TwitterTweetRepliesResponse503]
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
    body: TwitterTweetRepliesBody,
) -> (
    TwitterTweetRepliesResponse200
    | TwitterTweetRepliesResponse400
    | TwitterTweetRepliesResponse401
    | TwitterTweetRepliesResponse402
    | TwitterTweetRepliesResponse403
    | TwitterTweetRepliesResponse404
    | TwitterTweetRepliesResponse429
    | TwitterTweetRepliesResponse500
    | TwitterTweetRepliesResponse503
    | None
):
    r"""Fetch Twitter/X tweet replies

     Fetches a page of replies to a tweet. Use the `cursor` field from the response to retrieve
    subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterTweetRepliesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwitterTweetRepliesResponse200 | TwitterTweetRepliesResponse400 | TwitterTweetRepliesResponse401 | TwitterTweetRepliesResponse402 | TwitterTweetRepliesResponse403 | TwitterTweetRepliesResponse404 | TwitterTweetRepliesResponse429 | TwitterTweetRepliesResponse500 | TwitterTweetRepliesResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TwitterTweetRepliesBody,
) -> Response[
    TwitterTweetRepliesResponse200
    | TwitterTweetRepliesResponse400
    | TwitterTweetRepliesResponse401
    | TwitterTweetRepliesResponse402
    | TwitterTweetRepliesResponse403
    | TwitterTweetRepliesResponse404
    | TwitterTweetRepliesResponse429
    | TwitterTweetRepliesResponse500
    | TwitterTweetRepliesResponse503
]:
    r"""Fetch Twitter/X tweet replies

     Fetches a page of replies to a tweet. Use the `cursor` field from the response to retrieve
    subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterTweetRepliesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwitterTweetRepliesResponse200 | TwitterTweetRepliesResponse400 | TwitterTweetRepliesResponse401 | TwitterTweetRepliesResponse402 | TwitterTweetRepliesResponse403 | TwitterTweetRepliesResponse404 | TwitterTweetRepliesResponse429 | TwitterTweetRepliesResponse500 | TwitterTweetRepliesResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TwitterTweetRepliesBody,
) -> (
    TwitterTweetRepliesResponse200
    | TwitterTweetRepliesResponse400
    | TwitterTweetRepliesResponse401
    | TwitterTweetRepliesResponse402
    | TwitterTweetRepliesResponse403
    | TwitterTweetRepliesResponse404
    | TwitterTweetRepliesResponse429
    | TwitterTweetRepliesResponse500
    | TwitterTweetRepliesResponse503
    | None
):
    r"""Fetch Twitter/X tweet replies

     Fetches a page of replies to a tweet. Use the `cursor` field from the response to retrieve
    subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterTweetRepliesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwitterTweetRepliesResponse200 | TwitterTweetRepliesResponse400 | TwitterTweetRepliesResponse401 | TwitterTweetRepliesResponse402 | TwitterTweetRepliesResponse403 | TwitterTweetRepliesResponse404 | TwitterTweetRepliesResponse429 | TwitterTweetRepliesResponse500 | TwitterTweetRepliesResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
