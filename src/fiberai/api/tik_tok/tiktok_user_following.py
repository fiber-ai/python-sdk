from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tiktok_user_following_body import TiktokUserFollowingBody
from ...models.tiktok_user_following_response_200 import TiktokUserFollowingResponse200
from ...models.tiktok_user_following_response_400 import TiktokUserFollowingResponse400
from ...models.tiktok_user_following_response_401 import TiktokUserFollowingResponse401
from ...models.tiktok_user_following_response_402 import TiktokUserFollowingResponse402
from ...models.tiktok_user_following_response_403 import TiktokUserFollowingResponse403
from ...models.tiktok_user_following_response_404 import TiktokUserFollowingResponse404
from ...models.tiktok_user_following_response_422 import TiktokUserFollowingResponse422
from ...models.tiktok_user_following_response_429 import TiktokUserFollowingResponse429
from ...models.tiktok_user_following_response_500 import TiktokUserFollowingResponse500
from ...models.tiktok_user_following_response_503 import TiktokUserFollowingResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TiktokUserFollowingBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tiktok/user-following",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TiktokUserFollowingResponse200
    | TiktokUserFollowingResponse400
    | TiktokUserFollowingResponse401
    | TiktokUserFollowingResponse402
    | TiktokUserFollowingResponse403
    | TiktokUserFollowingResponse404
    | TiktokUserFollowingResponse422
    | TiktokUserFollowingResponse429
    | TiktokUserFollowingResponse500
    | TiktokUserFollowingResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TiktokUserFollowingResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TiktokUserFollowingResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TiktokUserFollowingResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TiktokUserFollowingResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TiktokUserFollowingResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TiktokUserFollowingResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = TiktokUserFollowingResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = TiktokUserFollowingResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TiktokUserFollowingResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TiktokUserFollowingResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TiktokUserFollowingResponse200
    | TiktokUserFollowingResponse400
    | TiktokUserFollowingResponse401
    | TiktokUserFollowingResponse402
    | TiktokUserFollowingResponse403
    | TiktokUserFollowingResponse404
    | TiktokUserFollowingResponse422
    | TiktokUserFollowingResponse429
    | TiktokUserFollowingResponse500
    | TiktokUserFollowingResponse503
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
    body: TiktokUserFollowingBody,
) -> Response[
    TiktokUserFollowingResponse200
    | TiktokUserFollowingResponse400
    | TiktokUserFollowingResponse401
    | TiktokUserFollowingResponse402
    | TiktokUserFollowingResponse403
    | TiktokUserFollowingResponse404
    | TiktokUserFollowingResponse422
    | TiktokUserFollowingResponse429
    | TiktokUserFollowingResponse500
    | TiktokUserFollowingResponse503
]:
    """Fetch TikTok user following

     Fetches the accounts that a TikTok user follows. Returns a paginated list. Use the `nextPageToken`
    field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokUserFollowingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokUserFollowingResponse200 | TiktokUserFollowingResponse400 | TiktokUserFollowingResponse401 | TiktokUserFollowingResponse402 | TiktokUserFollowingResponse403 | TiktokUserFollowingResponse404 | TiktokUserFollowingResponse422 | TiktokUserFollowingResponse429 | TiktokUserFollowingResponse500 | TiktokUserFollowingResponse503]
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
    body: TiktokUserFollowingBody,
) -> (
    TiktokUserFollowingResponse200
    | TiktokUserFollowingResponse400
    | TiktokUserFollowingResponse401
    | TiktokUserFollowingResponse402
    | TiktokUserFollowingResponse403
    | TiktokUserFollowingResponse404
    | TiktokUserFollowingResponse422
    | TiktokUserFollowingResponse429
    | TiktokUserFollowingResponse500
    | TiktokUserFollowingResponse503
    | None
):
    """Fetch TikTok user following

     Fetches the accounts that a TikTok user follows. Returns a paginated list. Use the `nextPageToken`
    field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokUserFollowingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokUserFollowingResponse200 | TiktokUserFollowingResponse400 | TiktokUserFollowingResponse401 | TiktokUserFollowingResponse402 | TiktokUserFollowingResponse403 | TiktokUserFollowingResponse404 | TiktokUserFollowingResponse422 | TiktokUserFollowingResponse429 | TiktokUserFollowingResponse500 | TiktokUserFollowingResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokUserFollowingBody,
) -> Response[
    TiktokUserFollowingResponse200
    | TiktokUserFollowingResponse400
    | TiktokUserFollowingResponse401
    | TiktokUserFollowingResponse402
    | TiktokUserFollowingResponse403
    | TiktokUserFollowingResponse404
    | TiktokUserFollowingResponse422
    | TiktokUserFollowingResponse429
    | TiktokUserFollowingResponse500
    | TiktokUserFollowingResponse503
]:
    """Fetch TikTok user following

     Fetches the accounts that a TikTok user follows. Returns a paginated list. Use the `nextPageToken`
    field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokUserFollowingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokUserFollowingResponse200 | TiktokUserFollowingResponse400 | TiktokUserFollowingResponse401 | TiktokUserFollowingResponse402 | TiktokUserFollowingResponse403 | TiktokUserFollowingResponse404 | TiktokUserFollowingResponse422 | TiktokUserFollowingResponse429 | TiktokUserFollowingResponse500 | TiktokUserFollowingResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokUserFollowingBody,
) -> (
    TiktokUserFollowingResponse200
    | TiktokUserFollowingResponse400
    | TiktokUserFollowingResponse401
    | TiktokUserFollowingResponse402
    | TiktokUserFollowingResponse403
    | TiktokUserFollowingResponse404
    | TiktokUserFollowingResponse422
    | TiktokUserFollowingResponse429
    | TiktokUserFollowingResponse500
    | TiktokUserFollowingResponse503
    | None
):
    """Fetch TikTok user following

     Fetches the accounts that a TikTok user follows. Returns a paginated list. Use the `nextPageToken`
    field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokUserFollowingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokUserFollowingResponse200 | TiktokUserFollowingResponse400 | TiktokUserFollowingResponse401 | TiktokUserFollowingResponse402 | TiktokUserFollowingResponse403 | TiktokUserFollowingResponse404 | TiktokUserFollowingResponse422 | TiktokUserFollowingResponse429 | TiktokUserFollowingResponse500 | TiktokUserFollowingResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
