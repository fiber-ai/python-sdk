from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.twitter_tweet_details_body import TwitterTweetDetailsBody
from ...models.twitter_tweet_details_response_200 import TwitterTweetDetailsResponse200
from ...models.twitter_tweet_details_response_400 import TwitterTweetDetailsResponse400
from ...models.twitter_tweet_details_response_401 import TwitterTweetDetailsResponse401
from ...models.twitter_tweet_details_response_402 import TwitterTweetDetailsResponse402
from ...models.twitter_tweet_details_response_403 import TwitterTweetDetailsResponse403
from ...models.twitter_tweet_details_response_404 import TwitterTweetDetailsResponse404
from ...models.twitter_tweet_details_response_429 import TwitterTweetDetailsResponse429
from ...models.twitter_tweet_details_response_500 import TwitterTweetDetailsResponse500
from ...models.twitter_tweet_details_response_503 import TwitterTweetDetailsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TwitterTweetDetailsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/twitter/tweet-details",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TwitterTweetDetailsResponse200
    | TwitterTweetDetailsResponse400
    | TwitterTweetDetailsResponse401
    | TwitterTweetDetailsResponse402
    | TwitterTweetDetailsResponse403
    | TwitterTweetDetailsResponse404
    | TwitterTweetDetailsResponse429
    | TwitterTweetDetailsResponse500
    | TwitterTweetDetailsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TwitterTweetDetailsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TwitterTweetDetailsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TwitterTweetDetailsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TwitterTweetDetailsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TwitterTweetDetailsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TwitterTweetDetailsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TwitterTweetDetailsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TwitterTweetDetailsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TwitterTweetDetailsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TwitterTweetDetailsResponse200
    | TwitterTweetDetailsResponse400
    | TwitterTweetDetailsResponse401
    | TwitterTweetDetailsResponse402
    | TwitterTweetDetailsResponse403
    | TwitterTweetDetailsResponse404
    | TwitterTweetDetailsResponse429
    | TwitterTweetDetailsResponse500
    | TwitterTweetDetailsResponse503
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
    body: TwitterTweetDetailsBody,
) -> Response[
    TwitterTweetDetailsResponse200
    | TwitterTweetDetailsResponse400
    | TwitterTweetDetailsResponse401
    | TwitterTweetDetailsResponse402
    | TwitterTweetDetailsResponse403
    | TwitterTweetDetailsResponse404
    | TwitterTweetDetailsResponse429
    | TwitterTweetDetailsResponse500
    | TwitterTweetDetailsResponse503
]:
    r"""Fetch Twitter/X tweet details

     Fetches details for a single tweet by its numeric ID. Returns full text, engagement metrics (likes,
    retweets, replies, views), and metadata.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterTweetDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwitterTweetDetailsResponse200 | TwitterTweetDetailsResponse400 | TwitterTweetDetailsResponse401 | TwitterTweetDetailsResponse402 | TwitterTweetDetailsResponse403 | TwitterTweetDetailsResponse404 | TwitterTweetDetailsResponse429 | TwitterTweetDetailsResponse500 | TwitterTweetDetailsResponse503]
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
    body: TwitterTweetDetailsBody,
) -> (
    TwitterTweetDetailsResponse200
    | TwitterTweetDetailsResponse400
    | TwitterTweetDetailsResponse401
    | TwitterTweetDetailsResponse402
    | TwitterTweetDetailsResponse403
    | TwitterTweetDetailsResponse404
    | TwitterTweetDetailsResponse429
    | TwitterTweetDetailsResponse500
    | TwitterTweetDetailsResponse503
    | None
):
    r"""Fetch Twitter/X tweet details

     Fetches details for a single tweet by its numeric ID. Returns full text, engagement metrics (likes,
    retweets, replies, views), and metadata.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterTweetDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwitterTweetDetailsResponse200 | TwitterTweetDetailsResponse400 | TwitterTweetDetailsResponse401 | TwitterTweetDetailsResponse402 | TwitterTweetDetailsResponse403 | TwitterTweetDetailsResponse404 | TwitterTweetDetailsResponse429 | TwitterTweetDetailsResponse500 | TwitterTweetDetailsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TwitterTweetDetailsBody,
) -> Response[
    TwitterTweetDetailsResponse200
    | TwitterTweetDetailsResponse400
    | TwitterTweetDetailsResponse401
    | TwitterTweetDetailsResponse402
    | TwitterTweetDetailsResponse403
    | TwitterTweetDetailsResponse404
    | TwitterTweetDetailsResponse429
    | TwitterTweetDetailsResponse500
    | TwitterTweetDetailsResponse503
]:
    r"""Fetch Twitter/X tweet details

     Fetches details for a single tweet by its numeric ID. Returns full text, engagement metrics (likes,
    retweets, replies, views), and metadata.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterTweetDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwitterTweetDetailsResponse200 | TwitterTweetDetailsResponse400 | TwitterTweetDetailsResponse401 | TwitterTweetDetailsResponse402 | TwitterTweetDetailsResponse403 | TwitterTweetDetailsResponse404 | TwitterTweetDetailsResponse429 | TwitterTweetDetailsResponse500 | TwitterTweetDetailsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TwitterTweetDetailsBody,
) -> (
    TwitterTweetDetailsResponse200
    | TwitterTweetDetailsResponse400
    | TwitterTweetDetailsResponse401
    | TwitterTweetDetailsResponse402
    | TwitterTweetDetailsResponse403
    | TwitterTweetDetailsResponse404
    | TwitterTweetDetailsResponse429
    | TwitterTweetDetailsResponse500
    | TwitterTweetDetailsResponse503
    | None
):
    r"""Fetch Twitter/X tweet details

     Fetches details for a single tweet by its numeric ID. Returns full text, engagement metrics (likes,
    retweets, replies, views), and metadata.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterTweetDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwitterTweetDetailsResponse200 | TwitterTweetDetailsResponse400 | TwitterTweetDetailsResponse401 | TwitterTweetDetailsResponse402 | TwitterTweetDetailsResponse403 | TwitterTweetDetailsResponse404 | TwitterTweetDetailsResponse429 | TwitterTweetDetailsResponse500 | TwitterTweetDetailsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
