from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.twitter_user_tweets_body import TwitterUserTweetsBody
from ...models.twitter_user_tweets_response_200 import TwitterUserTweetsResponse200
from ...models.twitter_user_tweets_response_400 import TwitterUserTweetsResponse400
from ...models.twitter_user_tweets_response_401 import TwitterUserTweetsResponse401
from ...models.twitter_user_tweets_response_402 import TwitterUserTweetsResponse402
from ...models.twitter_user_tweets_response_403 import TwitterUserTweetsResponse403
from ...models.twitter_user_tweets_response_404 import TwitterUserTweetsResponse404
from ...models.twitter_user_tweets_response_429 import TwitterUserTweetsResponse429
from ...models.twitter_user_tweets_response_500 import TwitterUserTweetsResponse500
from ...models.twitter_user_tweets_response_503 import TwitterUserTweetsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TwitterUserTweetsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/twitter/user-tweets",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TwitterUserTweetsResponse200
    | TwitterUserTweetsResponse400
    | TwitterUserTweetsResponse401
    | TwitterUserTweetsResponse402
    | TwitterUserTweetsResponse403
    | TwitterUserTweetsResponse404
    | TwitterUserTweetsResponse429
    | TwitterUserTweetsResponse500
    | TwitterUserTweetsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TwitterUserTweetsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TwitterUserTweetsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TwitterUserTweetsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TwitterUserTweetsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TwitterUserTweetsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TwitterUserTweetsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TwitterUserTweetsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TwitterUserTweetsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TwitterUserTweetsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TwitterUserTweetsResponse200
    | TwitterUserTweetsResponse400
    | TwitterUserTweetsResponse401
    | TwitterUserTweetsResponse402
    | TwitterUserTweetsResponse403
    | TwitterUserTweetsResponse404
    | TwitterUserTweetsResponse429
    | TwitterUserTweetsResponse500
    | TwitterUserTweetsResponse503
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
    body: TwitterUserTweetsBody,
) -> Response[
    TwitterUserTweetsResponse200
    | TwitterUserTweetsResponse400
    | TwitterUserTweetsResponse401
    | TwitterUserTweetsResponse402
    | TwitterUserTweetsResponse403
    | TwitterUserTweetsResponse404
    | TwitterUserTweetsResponse429
    | TwitterUserTweetsResponse500
    | TwitterUserTweetsResponse503
]:
    r"""Fetch Twitter/X user tweets

     Fetches the latest tweets for a Twitter/X user. Returns a paginated list of tweets with engagement
    metrics. Use the `cursor` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterUserTweetsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwitterUserTweetsResponse200 | TwitterUserTweetsResponse400 | TwitterUserTweetsResponse401 | TwitterUserTweetsResponse402 | TwitterUserTweetsResponse403 | TwitterUserTweetsResponse404 | TwitterUserTweetsResponse429 | TwitterUserTweetsResponse500 | TwitterUserTweetsResponse503]
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
    body: TwitterUserTweetsBody,
) -> (
    TwitterUserTweetsResponse200
    | TwitterUserTweetsResponse400
    | TwitterUserTweetsResponse401
    | TwitterUserTweetsResponse402
    | TwitterUserTweetsResponse403
    | TwitterUserTweetsResponse404
    | TwitterUserTweetsResponse429
    | TwitterUserTweetsResponse500
    | TwitterUserTweetsResponse503
    | None
):
    r"""Fetch Twitter/X user tweets

     Fetches the latest tweets for a Twitter/X user. Returns a paginated list of tweets with engagement
    metrics. Use the `cursor` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterUserTweetsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwitterUserTweetsResponse200 | TwitterUserTweetsResponse400 | TwitterUserTweetsResponse401 | TwitterUserTweetsResponse402 | TwitterUserTweetsResponse403 | TwitterUserTweetsResponse404 | TwitterUserTweetsResponse429 | TwitterUserTweetsResponse500 | TwitterUserTweetsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TwitterUserTweetsBody,
) -> Response[
    TwitterUserTweetsResponse200
    | TwitterUserTweetsResponse400
    | TwitterUserTweetsResponse401
    | TwitterUserTweetsResponse402
    | TwitterUserTweetsResponse403
    | TwitterUserTweetsResponse404
    | TwitterUserTweetsResponse429
    | TwitterUserTweetsResponse500
    | TwitterUserTweetsResponse503
]:
    r"""Fetch Twitter/X user tweets

     Fetches the latest tweets for a Twitter/X user. Returns a paginated list of tweets with engagement
    metrics. Use the `cursor` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterUserTweetsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwitterUserTweetsResponse200 | TwitterUserTweetsResponse400 | TwitterUserTweetsResponse401 | TwitterUserTweetsResponse402 | TwitterUserTweetsResponse403 | TwitterUserTweetsResponse404 | TwitterUserTweetsResponse429 | TwitterUserTweetsResponse500 | TwitterUserTweetsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TwitterUserTweetsBody,
) -> (
    TwitterUserTweetsResponse200
    | TwitterUserTweetsResponse400
    | TwitterUserTweetsResponse401
    | TwitterUserTweetsResponse402
    | TwitterUserTweetsResponse403
    | TwitterUserTweetsResponse404
    | TwitterUserTweetsResponse429
    | TwitterUserTweetsResponse500
    | TwitterUserTweetsResponse503
    | None
):
    r"""Fetch Twitter/X user tweets

     Fetches the latest tweets for a Twitter/X user. Returns a paginated list of tweets with engagement
    metrics. Use the `cursor` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterUserTweetsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwitterUserTweetsResponse200 | TwitterUserTweetsResponse400 | TwitterUserTweetsResponse401 | TwitterUserTweetsResponse402 | TwitterUserTweetsResponse403 | TwitterUserTweetsResponse404 | TwitterUserTweetsResponse429 | TwitterUserTweetsResponse500 | TwitterUserTweetsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
