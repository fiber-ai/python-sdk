from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.twitter_user_mentions_body import TwitterUserMentionsBody
from ...models.twitter_user_mentions_response_200 import TwitterUserMentionsResponse200
from ...models.twitter_user_mentions_response_400 import TwitterUserMentionsResponse400
from ...models.twitter_user_mentions_response_401 import TwitterUserMentionsResponse401
from ...models.twitter_user_mentions_response_402 import TwitterUserMentionsResponse402
from ...models.twitter_user_mentions_response_403 import TwitterUserMentionsResponse403
from ...models.twitter_user_mentions_response_404 import TwitterUserMentionsResponse404
from ...models.twitter_user_mentions_response_422 import TwitterUserMentionsResponse422
from ...models.twitter_user_mentions_response_429 import TwitterUserMentionsResponse429
from ...models.twitter_user_mentions_response_500 import TwitterUserMentionsResponse500
from ...models.twitter_user_mentions_response_503 import TwitterUserMentionsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TwitterUserMentionsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/twitter/user-mentions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TwitterUserMentionsResponse200
    | TwitterUserMentionsResponse400
    | TwitterUserMentionsResponse401
    | TwitterUserMentionsResponse402
    | TwitterUserMentionsResponse403
    | TwitterUserMentionsResponse404
    | TwitterUserMentionsResponse422
    | TwitterUserMentionsResponse429
    | TwitterUserMentionsResponse500
    | TwitterUserMentionsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TwitterUserMentionsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TwitterUserMentionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TwitterUserMentionsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TwitterUserMentionsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TwitterUserMentionsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TwitterUserMentionsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = TwitterUserMentionsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = TwitterUserMentionsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TwitterUserMentionsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TwitterUserMentionsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TwitterUserMentionsResponse200
    | TwitterUserMentionsResponse400
    | TwitterUserMentionsResponse401
    | TwitterUserMentionsResponse402
    | TwitterUserMentionsResponse403
    | TwitterUserMentionsResponse404
    | TwitterUserMentionsResponse422
    | TwitterUserMentionsResponse429
    | TwitterUserMentionsResponse500
    | TwitterUserMentionsResponse503
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
    body: TwitterUserMentionsBody,
) -> Response[
    TwitterUserMentionsResponse200
    | TwitterUserMentionsResponse400
    | TwitterUserMentionsResponse401
    | TwitterUserMentionsResponse402
    | TwitterUserMentionsResponse403
    | TwitterUserMentionsResponse404
    | TwitterUserMentionsResponse422
    | TwitterUserMentionsResponse429
    | TwitterUserMentionsResponse500
    | TwitterUserMentionsResponse503
]:
    r"""Fetch Twitter/X user mentions

     Fetches a page of tweets that mention a Twitter/X user. Use the `cursor` field from the response to
    retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterUserMentionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwitterUserMentionsResponse200 | TwitterUserMentionsResponse400 | TwitterUserMentionsResponse401 | TwitterUserMentionsResponse402 | TwitterUserMentionsResponse403 | TwitterUserMentionsResponse404 | TwitterUserMentionsResponse422 | TwitterUserMentionsResponse429 | TwitterUserMentionsResponse500 | TwitterUserMentionsResponse503]
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
    body: TwitterUserMentionsBody,
) -> (
    TwitterUserMentionsResponse200
    | TwitterUserMentionsResponse400
    | TwitterUserMentionsResponse401
    | TwitterUserMentionsResponse402
    | TwitterUserMentionsResponse403
    | TwitterUserMentionsResponse404
    | TwitterUserMentionsResponse422
    | TwitterUserMentionsResponse429
    | TwitterUserMentionsResponse500
    | TwitterUserMentionsResponse503
    | None
):
    r"""Fetch Twitter/X user mentions

     Fetches a page of tweets that mention a Twitter/X user. Use the `cursor` field from the response to
    retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterUserMentionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwitterUserMentionsResponse200 | TwitterUserMentionsResponse400 | TwitterUserMentionsResponse401 | TwitterUserMentionsResponse402 | TwitterUserMentionsResponse403 | TwitterUserMentionsResponse404 | TwitterUserMentionsResponse422 | TwitterUserMentionsResponse429 | TwitterUserMentionsResponse500 | TwitterUserMentionsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TwitterUserMentionsBody,
) -> Response[
    TwitterUserMentionsResponse200
    | TwitterUserMentionsResponse400
    | TwitterUserMentionsResponse401
    | TwitterUserMentionsResponse402
    | TwitterUserMentionsResponse403
    | TwitterUserMentionsResponse404
    | TwitterUserMentionsResponse422
    | TwitterUserMentionsResponse429
    | TwitterUserMentionsResponse500
    | TwitterUserMentionsResponse503
]:
    r"""Fetch Twitter/X user mentions

     Fetches a page of tweets that mention a Twitter/X user. Use the `cursor` field from the response to
    retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterUserMentionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwitterUserMentionsResponse200 | TwitterUserMentionsResponse400 | TwitterUserMentionsResponse401 | TwitterUserMentionsResponse402 | TwitterUserMentionsResponse403 | TwitterUserMentionsResponse404 | TwitterUserMentionsResponse422 | TwitterUserMentionsResponse429 | TwitterUserMentionsResponse500 | TwitterUserMentionsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TwitterUserMentionsBody,
) -> (
    TwitterUserMentionsResponse200
    | TwitterUserMentionsResponse400
    | TwitterUserMentionsResponse401
    | TwitterUserMentionsResponse402
    | TwitterUserMentionsResponse403
    | TwitterUserMentionsResponse404
    | TwitterUserMentionsResponse422
    | TwitterUserMentionsResponse429
    | TwitterUserMentionsResponse500
    | TwitterUserMentionsResponse503
    | None
):
    r"""Fetch Twitter/X user mentions

     Fetches a page of tweets that mention a Twitter/X user. Use the `cursor` field from the response to
    retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterUserMentionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwitterUserMentionsResponse200 | TwitterUserMentionsResponse400 | TwitterUserMentionsResponse401 | TwitterUserMentionsResponse402 | TwitterUserMentionsResponse403 | TwitterUserMentionsResponse404 | TwitterUserMentionsResponse422 | TwitterUserMentionsResponse429 | TwitterUserMentionsResponse500 | TwitterUserMentionsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
