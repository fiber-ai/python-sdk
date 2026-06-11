from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tiktok_user_followers_body import TiktokUserFollowersBody
from ...models.tiktok_user_followers_response_200 import TiktokUserFollowersResponse200
from ...models.tiktok_user_followers_response_400 import TiktokUserFollowersResponse400
from ...models.tiktok_user_followers_response_401 import TiktokUserFollowersResponse401
from ...models.tiktok_user_followers_response_402 import TiktokUserFollowersResponse402
from ...models.tiktok_user_followers_response_403 import TiktokUserFollowersResponse403
from ...models.tiktok_user_followers_response_404 import TiktokUserFollowersResponse404
from ...models.tiktok_user_followers_response_429 import TiktokUserFollowersResponse429
from ...models.tiktok_user_followers_response_500 import TiktokUserFollowersResponse500
from ...models.tiktok_user_followers_response_503 import TiktokUserFollowersResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TiktokUserFollowersBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tiktok/user-followers",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TiktokUserFollowersResponse200
    | TiktokUserFollowersResponse400
    | TiktokUserFollowersResponse401
    | TiktokUserFollowersResponse402
    | TiktokUserFollowersResponse403
    | TiktokUserFollowersResponse404
    | TiktokUserFollowersResponse429
    | TiktokUserFollowersResponse500
    | TiktokUserFollowersResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TiktokUserFollowersResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TiktokUserFollowersResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TiktokUserFollowersResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TiktokUserFollowersResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TiktokUserFollowersResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TiktokUserFollowersResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TiktokUserFollowersResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TiktokUserFollowersResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TiktokUserFollowersResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TiktokUserFollowersResponse200
    | TiktokUserFollowersResponse400
    | TiktokUserFollowersResponse401
    | TiktokUserFollowersResponse402
    | TiktokUserFollowersResponse403
    | TiktokUserFollowersResponse404
    | TiktokUserFollowersResponse429
    | TiktokUserFollowersResponse500
    | TiktokUserFollowersResponse503
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
    body: TiktokUserFollowersBody,
) -> Response[
    TiktokUserFollowersResponse200
    | TiktokUserFollowersResponse400
    | TiktokUserFollowersResponse401
    | TiktokUserFollowersResponse402
    | TiktokUserFollowersResponse403
    | TiktokUserFollowersResponse404
    | TiktokUserFollowersResponse429
    | TiktokUserFollowersResponse500
    | TiktokUserFollowersResponse503
]:
    r"""Fetch TikTok user followers

     Fetches the followers of a TikTok user. Returns a paginated list. Use the `nextPageToken` field from
    the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokUserFollowersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokUserFollowersResponse200 | TiktokUserFollowersResponse400 | TiktokUserFollowersResponse401 | TiktokUserFollowersResponse402 | TiktokUserFollowersResponse403 | TiktokUserFollowersResponse404 | TiktokUserFollowersResponse429 | TiktokUserFollowersResponse500 | TiktokUserFollowersResponse503]
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
    body: TiktokUserFollowersBody,
) -> (
    TiktokUserFollowersResponse200
    | TiktokUserFollowersResponse400
    | TiktokUserFollowersResponse401
    | TiktokUserFollowersResponse402
    | TiktokUserFollowersResponse403
    | TiktokUserFollowersResponse404
    | TiktokUserFollowersResponse429
    | TiktokUserFollowersResponse500
    | TiktokUserFollowersResponse503
    | None
):
    r"""Fetch TikTok user followers

     Fetches the followers of a TikTok user. Returns a paginated list. Use the `nextPageToken` field from
    the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokUserFollowersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokUserFollowersResponse200 | TiktokUserFollowersResponse400 | TiktokUserFollowersResponse401 | TiktokUserFollowersResponse402 | TiktokUserFollowersResponse403 | TiktokUserFollowersResponse404 | TiktokUserFollowersResponse429 | TiktokUserFollowersResponse500 | TiktokUserFollowersResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokUserFollowersBody,
) -> Response[
    TiktokUserFollowersResponse200
    | TiktokUserFollowersResponse400
    | TiktokUserFollowersResponse401
    | TiktokUserFollowersResponse402
    | TiktokUserFollowersResponse403
    | TiktokUserFollowersResponse404
    | TiktokUserFollowersResponse429
    | TiktokUserFollowersResponse500
    | TiktokUserFollowersResponse503
]:
    r"""Fetch TikTok user followers

     Fetches the followers of a TikTok user. Returns a paginated list. Use the `nextPageToken` field from
    the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokUserFollowersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokUserFollowersResponse200 | TiktokUserFollowersResponse400 | TiktokUserFollowersResponse401 | TiktokUserFollowersResponse402 | TiktokUserFollowersResponse403 | TiktokUserFollowersResponse404 | TiktokUserFollowersResponse429 | TiktokUserFollowersResponse500 | TiktokUserFollowersResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokUserFollowersBody,
) -> (
    TiktokUserFollowersResponse200
    | TiktokUserFollowersResponse400
    | TiktokUserFollowersResponse401
    | TiktokUserFollowersResponse402
    | TiktokUserFollowersResponse403
    | TiktokUserFollowersResponse404
    | TiktokUserFollowersResponse429
    | TiktokUserFollowersResponse500
    | TiktokUserFollowersResponse503
    | None
):
    r"""Fetch TikTok user followers

     Fetches the followers of a TikTok user. Returns a paginated list. Use the `nextPageToken` field from
    the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokUserFollowersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokUserFollowersResponse200 | TiktokUserFollowersResponse400 | TiktokUserFollowersResponse401 | TiktokUserFollowersResponse402 | TiktokUserFollowersResponse403 | TiktokUserFollowersResponse404 | TiktokUserFollowersResponse429 | TiktokUserFollowersResponse500 | TiktokUserFollowersResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
