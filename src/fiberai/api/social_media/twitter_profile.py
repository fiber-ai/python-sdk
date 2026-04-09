from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.twitter_profile_body import TwitterProfileBody
from ...models.twitter_profile_response_200 import TwitterProfileResponse200
from ...models.twitter_profile_response_400 import TwitterProfileResponse400
from ...models.twitter_profile_response_401 import TwitterProfileResponse401
from ...models.twitter_profile_response_402 import TwitterProfileResponse402
from ...models.twitter_profile_response_403 import TwitterProfileResponse403
from ...models.twitter_profile_response_404 import TwitterProfileResponse404
from ...models.twitter_profile_response_429 import TwitterProfileResponse429
from ...models.twitter_profile_response_500 import TwitterProfileResponse500
from ...models.twitter_profile_response_503 import TwitterProfileResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TwitterProfileBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/twitter/profile",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TwitterProfileResponse200
    | TwitterProfileResponse400
    | TwitterProfileResponse401
    | TwitterProfileResponse402
    | TwitterProfileResponse403
    | TwitterProfileResponse404
    | TwitterProfileResponse429
    | TwitterProfileResponse500
    | TwitterProfileResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TwitterProfileResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TwitterProfileResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TwitterProfileResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TwitterProfileResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TwitterProfileResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TwitterProfileResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TwitterProfileResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TwitterProfileResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TwitterProfileResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TwitterProfileResponse200
    | TwitterProfileResponse400
    | TwitterProfileResponse401
    | TwitterProfileResponse402
    | TwitterProfileResponse403
    | TwitterProfileResponse404
    | TwitterProfileResponse429
    | TwitterProfileResponse500
    | TwitterProfileResponse503
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
    body: TwitterProfileBody,
) -> Response[
    TwitterProfileResponse200
    | TwitterProfileResponse400
    | TwitterProfileResponse401
    | TwitterProfileResponse402
    | TwitterProfileResponse403
    | TwitterProfileResponse404
    | TwitterProfileResponse429
    | TwitterProfileResponse500
    | TwitterProfileResponse503
]:
    r"""Fetch Twitter/X user profile

     Fetches the public profile for a Twitter/X user by handle. Returns follower/following counts, bio,
    verification status, and account metadata.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwitterProfileResponse200 | TwitterProfileResponse400 | TwitterProfileResponse401 | TwitterProfileResponse402 | TwitterProfileResponse403 | TwitterProfileResponse404 | TwitterProfileResponse429 | TwitterProfileResponse500 | TwitterProfileResponse503]
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
    body: TwitterProfileBody,
) -> (
    TwitterProfileResponse200
    | TwitterProfileResponse400
    | TwitterProfileResponse401
    | TwitterProfileResponse402
    | TwitterProfileResponse403
    | TwitterProfileResponse404
    | TwitterProfileResponse429
    | TwitterProfileResponse500
    | TwitterProfileResponse503
    | None
):
    r"""Fetch Twitter/X user profile

     Fetches the public profile for a Twitter/X user by handle. Returns follower/following counts, bio,
    verification status, and account metadata.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwitterProfileResponse200 | TwitterProfileResponse400 | TwitterProfileResponse401 | TwitterProfileResponse402 | TwitterProfileResponse403 | TwitterProfileResponse404 | TwitterProfileResponse429 | TwitterProfileResponse500 | TwitterProfileResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TwitterProfileBody,
) -> Response[
    TwitterProfileResponse200
    | TwitterProfileResponse400
    | TwitterProfileResponse401
    | TwitterProfileResponse402
    | TwitterProfileResponse403
    | TwitterProfileResponse404
    | TwitterProfileResponse429
    | TwitterProfileResponse500
    | TwitterProfileResponse503
]:
    r"""Fetch Twitter/X user profile

     Fetches the public profile for a Twitter/X user by handle. Returns follower/following counts, bio,
    verification status, and account metadata.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwitterProfileResponse200 | TwitterProfileResponse400 | TwitterProfileResponse401 | TwitterProfileResponse402 | TwitterProfileResponse403 | TwitterProfileResponse404 | TwitterProfileResponse429 | TwitterProfileResponse500 | TwitterProfileResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TwitterProfileBody,
) -> (
    TwitterProfileResponse200
    | TwitterProfileResponse400
    | TwitterProfileResponse401
    | TwitterProfileResponse402
    | TwitterProfileResponse403
    | TwitterProfileResponse404
    | TwitterProfileResponse429
    | TwitterProfileResponse500
    | TwitterProfileResponse503
    | None
):
    r"""Fetch Twitter/X user profile

     Fetches the public profile for a Twitter/X user by handle. Returns follower/following counts, bio,
    verification status, and account metadata.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwitterProfileResponse200 | TwitterProfileResponse400 | TwitterProfileResponse401 | TwitterProfileResponse402 | TwitterProfileResponse403 | TwitterProfileResponse404 | TwitterProfileResponse429 | TwitterProfileResponse500 | TwitterProfileResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
