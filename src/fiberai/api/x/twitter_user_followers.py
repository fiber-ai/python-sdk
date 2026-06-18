from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.twitter_user_followers_body import TwitterUserFollowersBody
from ...models.twitter_user_followers_response_200 import TwitterUserFollowersResponse200
from ...models.twitter_user_followers_response_400 import TwitterUserFollowersResponse400
from ...models.twitter_user_followers_response_401 import TwitterUserFollowersResponse401
from ...models.twitter_user_followers_response_402 import TwitterUserFollowersResponse402
from ...models.twitter_user_followers_response_403 import TwitterUserFollowersResponse403
from ...models.twitter_user_followers_response_404 import TwitterUserFollowersResponse404
from ...models.twitter_user_followers_response_422 import TwitterUserFollowersResponse422
from ...models.twitter_user_followers_response_429 import TwitterUserFollowersResponse429
from ...models.twitter_user_followers_response_500 import TwitterUserFollowersResponse500
from ...models.twitter_user_followers_response_503 import TwitterUserFollowersResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TwitterUserFollowersBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/twitter/user-followers",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TwitterUserFollowersResponse200
    | TwitterUserFollowersResponse400
    | TwitterUserFollowersResponse401
    | TwitterUserFollowersResponse402
    | TwitterUserFollowersResponse403
    | TwitterUserFollowersResponse404
    | TwitterUserFollowersResponse422
    | TwitterUserFollowersResponse429
    | TwitterUserFollowersResponse500
    | TwitterUserFollowersResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TwitterUserFollowersResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TwitterUserFollowersResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TwitterUserFollowersResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TwitterUserFollowersResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TwitterUserFollowersResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TwitterUserFollowersResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = TwitterUserFollowersResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = TwitterUserFollowersResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TwitterUserFollowersResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TwitterUserFollowersResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TwitterUserFollowersResponse200
    | TwitterUserFollowersResponse400
    | TwitterUserFollowersResponse401
    | TwitterUserFollowersResponse402
    | TwitterUserFollowersResponse403
    | TwitterUserFollowersResponse404
    | TwitterUserFollowersResponse422
    | TwitterUserFollowersResponse429
    | TwitterUserFollowersResponse500
    | TwitterUserFollowersResponse503
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
    body: TwitterUserFollowersBody,
) -> Response[
    TwitterUserFollowersResponse200
    | TwitterUserFollowersResponse400
    | TwitterUserFollowersResponse401
    | TwitterUserFollowersResponse402
    | TwitterUserFollowersResponse403
    | TwitterUserFollowersResponse404
    | TwitterUserFollowersResponse422
    | TwitterUserFollowersResponse429
    | TwitterUserFollowersResponse500
    | TwitterUserFollowersResponse503
]:
    r"""Fetch Twitter/X user followers

     Fetches a page of followers for a Twitter/X user. Use the `cursor` field from the response to
    retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterUserFollowersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwitterUserFollowersResponse200 | TwitterUserFollowersResponse400 | TwitterUserFollowersResponse401 | TwitterUserFollowersResponse402 | TwitterUserFollowersResponse403 | TwitterUserFollowersResponse404 | TwitterUserFollowersResponse422 | TwitterUserFollowersResponse429 | TwitterUserFollowersResponse500 | TwitterUserFollowersResponse503]
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
    body: TwitterUserFollowersBody,
) -> (
    TwitterUserFollowersResponse200
    | TwitterUserFollowersResponse400
    | TwitterUserFollowersResponse401
    | TwitterUserFollowersResponse402
    | TwitterUserFollowersResponse403
    | TwitterUserFollowersResponse404
    | TwitterUserFollowersResponse422
    | TwitterUserFollowersResponse429
    | TwitterUserFollowersResponse500
    | TwitterUserFollowersResponse503
    | None
):
    r"""Fetch Twitter/X user followers

     Fetches a page of followers for a Twitter/X user. Use the `cursor` field from the response to
    retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterUserFollowersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwitterUserFollowersResponse200 | TwitterUserFollowersResponse400 | TwitterUserFollowersResponse401 | TwitterUserFollowersResponse402 | TwitterUserFollowersResponse403 | TwitterUserFollowersResponse404 | TwitterUserFollowersResponse422 | TwitterUserFollowersResponse429 | TwitterUserFollowersResponse500 | TwitterUserFollowersResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TwitterUserFollowersBody,
) -> Response[
    TwitterUserFollowersResponse200
    | TwitterUserFollowersResponse400
    | TwitterUserFollowersResponse401
    | TwitterUserFollowersResponse402
    | TwitterUserFollowersResponse403
    | TwitterUserFollowersResponse404
    | TwitterUserFollowersResponse422
    | TwitterUserFollowersResponse429
    | TwitterUserFollowersResponse500
    | TwitterUserFollowersResponse503
]:
    r"""Fetch Twitter/X user followers

     Fetches a page of followers for a Twitter/X user. Use the `cursor` field from the response to
    retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterUserFollowersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwitterUserFollowersResponse200 | TwitterUserFollowersResponse400 | TwitterUserFollowersResponse401 | TwitterUserFollowersResponse402 | TwitterUserFollowersResponse403 | TwitterUserFollowersResponse404 | TwitterUserFollowersResponse422 | TwitterUserFollowersResponse429 | TwitterUserFollowersResponse500 | TwitterUserFollowersResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TwitterUserFollowersBody,
) -> (
    TwitterUserFollowersResponse200
    | TwitterUserFollowersResponse400
    | TwitterUserFollowersResponse401
    | TwitterUserFollowersResponse402
    | TwitterUserFollowersResponse403
    | TwitterUserFollowersResponse404
    | TwitterUserFollowersResponse422
    | TwitterUserFollowersResponse429
    | TwitterUserFollowersResponse500
    | TwitterUserFollowersResponse503
    | None
):
    r"""Fetch Twitter/X user followers

     Fetches a page of followers for a Twitter/X user. Use the `cursor` field from the response to
    retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterUserFollowersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwitterUserFollowersResponse200 | TwitterUserFollowersResponse400 | TwitterUserFollowersResponse401 | TwitterUserFollowersResponse402 | TwitterUserFollowersResponse403 | TwitterUserFollowersResponse404 | TwitterUserFollowersResponse422 | TwitterUserFollowersResponse429 | TwitterUserFollowersResponse500 | TwitterUserFollowersResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
