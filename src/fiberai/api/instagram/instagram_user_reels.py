from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.instagram_user_reels_body import InstagramUserReelsBody
from ...models.instagram_user_reels_response_200 import InstagramUserReelsResponse200
from ...models.instagram_user_reels_response_400 import InstagramUserReelsResponse400
from ...models.instagram_user_reels_response_401 import InstagramUserReelsResponse401
from ...models.instagram_user_reels_response_402 import InstagramUserReelsResponse402
from ...models.instagram_user_reels_response_403 import InstagramUserReelsResponse403
from ...models.instagram_user_reels_response_404 import InstagramUserReelsResponse404
from ...models.instagram_user_reels_response_429 import InstagramUserReelsResponse429
from ...models.instagram_user_reels_response_500 import InstagramUserReelsResponse500
from ...models.instagram_user_reels_response_503 import InstagramUserReelsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: InstagramUserReelsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/instagram/user-reels",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InstagramUserReelsResponse200
    | InstagramUserReelsResponse400
    | InstagramUserReelsResponse401
    | InstagramUserReelsResponse402
    | InstagramUserReelsResponse403
    | InstagramUserReelsResponse404
    | InstagramUserReelsResponse429
    | InstagramUserReelsResponse500
    | InstagramUserReelsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = InstagramUserReelsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InstagramUserReelsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = InstagramUserReelsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = InstagramUserReelsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = InstagramUserReelsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = InstagramUserReelsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = InstagramUserReelsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = InstagramUserReelsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = InstagramUserReelsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InstagramUserReelsResponse200
    | InstagramUserReelsResponse400
    | InstagramUserReelsResponse401
    | InstagramUserReelsResponse402
    | InstagramUserReelsResponse403
    | InstagramUserReelsResponse404
    | InstagramUserReelsResponse429
    | InstagramUserReelsResponse500
    | InstagramUserReelsResponse503
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
    body: InstagramUserReelsBody,
) -> Response[
    InstagramUserReelsResponse200
    | InstagramUserReelsResponse400
    | InstagramUserReelsResponse401
    | InstagramUserReelsResponse402
    | InstagramUserReelsResponse403
    | InstagramUserReelsResponse404
    | InstagramUserReelsResponse429
    | InstagramUserReelsResponse500
    | InstagramUserReelsResponse503
]:
    r"""Fetch Instagram user reels

     Fetches the latest reels for an Instagram user. Returns a paginated list of reels with engagement
    metrics. Use the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InstagramUserReelsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstagramUserReelsResponse200 | InstagramUserReelsResponse400 | InstagramUserReelsResponse401 | InstagramUserReelsResponse402 | InstagramUserReelsResponse403 | InstagramUserReelsResponse404 | InstagramUserReelsResponse429 | InstagramUserReelsResponse500 | InstagramUserReelsResponse503]
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
    body: InstagramUserReelsBody,
) -> (
    InstagramUserReelsResponse200
    | InstagramUserReelsResponse400
    | InstagramUserReelsResponse401
    | InstagramUserReelsResponse402
    | InstagramUserReelsResponse403
    | InstagramUserReelsResponse404
    | InstagramUserReelsResponse429
    | InstagramUserReelsResponse500
    | InstagramUserReelsResponse503
    | None
):
    r"""Fetch Instagram user reels

     Fetches the latest reels for an Instagram user. Returns a paginated list of reels with engagement
    metrics. Use the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InstagramUserReelsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstagramUserReelsResponse200 | InstagramUserReelsResponse400 | InstagramUserReelsResponse401 | InstagramUserReelsResponse402 | InstagramUserReelsResponse403 | InstagramUserReelsResponse404 | InstagramUserReelsResponse429 | InstagramUserReelsResponse500 | InstagramUserReelsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InstagramUserReelsBody,
) -> Response[
    InstagramUserReelsResponse200
    | InstagramUserReelsResponse400
    | InstagramUserReelsResponse401
    | InstagramUserReelsResponse402
    | InstagramUserReelsResponse403
    | InstagramUserReelsResponse404
    | InstagramUserReelsResponse429
    | InstagramUserReelsResponse500
    | InstagramUserReelsResponse503
]:
    r"""Fetch Instagram user reels

     Fetches the latest reels for an Instagram user. Returns a paginated list of reels with engagement
    metrics. Use the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InstagramUserReelsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstagramUserReelsResponse200 | InstagramUserReelsResponse400 | InstagramUserReelsResponse401 | InstagramUserReelsResponse402 | InstagramUserReelsResponse403 | InstagramUserReelsResponse404 | InstagramUserReelsResponse429 | InstagramUserReelsResponse500 | InstagramUserReelsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: InstagramUserReelsBody,
) -> (
    InstagramUserReelsResponse200
    | InstagramUserReelsResponse400
    | InstagramUserReelsResponse401
    | InstagramUserReelsResponse402
    | InstagramUserReelsResponse403
    | InstagramUserReelsResponse404
    | InstagramUserReelsResponse429
    | InstagramUserReelsResponse500
    | InstagramUserReelsResponse503
    | None
):
    r"""Fetch Instagram user reels

     Fetches the latest reels for an Instagram user. Returns a paginated list of reels with engagement
    metrics. Use the `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InstagramUserReelsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstagramUserReelsResponse200 | InstagramUserReelsResponse400 | InstagramUserReelsResponse401 | InstagramUserReelsResponse402 | InstagramUserReelsResponse403 | InstagramUserReelsResponse404 | InstagramUserReelsResponse429 | InstagramUserReelsResponse500 | InstagramUserReelsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
