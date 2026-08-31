from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tiktok_search_users_body import TiktokSearchUsersBody
from ...models.tiktok_search_users_response_200 import TiktokSearchUsersResponse200
from ...models.tiktok_search_users_response_400 import TiktokSearchUsersResponse400
from ...models.tiktok_search_users_response_401 import TiktokSearchUsersResponse401
from ...models.tiktok_search_users_response_402 import TiktokSearchUsersResponse402
from ...models.tiktok_search_users_response_403 import TiktokSearchUsersResponse403
from ...models.tiktok_search_users_response_404 import TiktokSearchUsersResponse404
from ...models.tiktok_search_users_response_422 import TiktokSearchUsersResponse422
from ...models.tiktok_search_users_response_429 import TiktokSearchUsersResponse429
from ...models.tiktok_search_users_response_500 import TiktokSearchUsersResponse500
from ...models.tiktok_search_users_response_503 import TiktokSearchUsersResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TiktokSearchUsersBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tiktok/search-users",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TiktokSearchUsersResponse200
    | TiktokSearchUsersResponse400
    | TiktokSearchUsersResponse401
    | TiktokSearchUsersResponse402
    | TiktokSearchUsersResponse403
    | TiktokSearchUsersResponse404
    | TiktokSearchUsersResponse422
    | TiktokSearchUsersResponse429
    | TiktokSearchUsersResponse500
    | TiktokSearchUsersResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TiktokSearchUsersResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TiktokSearchUsersResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TiktokSearchUsersResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TiktokSearchUsersResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TiktokSearchUsersResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TiktokSearchUsersResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = TiktokSearchUsersResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = TiktokSearchUsersResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TiktokSearchUsersResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TiktokSearchUsersResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TiktokSearchUsersResponse200
    | TiktokSearchUsersResponse400
    | TiktokSearchUsersResponse401
    | TiktokSearchUsersResponse402
    | TiktokSearchUsersResponse403
    | TiktokSearchUsersResponse404
    | TiktokSearchUsersResponse422
    | TiktokSearchUsersResponse429
    | TiktokSearchUsersResponse500
    | TiktokSearchUsersResponse503
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
    body: TiktokSearchUsersBody,
) -> Response[
    TiktokSearchUsersResponse200
    | TiktokSearchUsersResponse400
    | TiktokSearchUsersResponse401
    | TiktokSearchUsersResponse402
    | TiktokSearchUsersResponse403
    | TiktokSearchUsersResponse404
    | TiktokSearchUsersResponse422
    | TiktokSearchUsersResponse429
    | TiktokSearchUsersResponse500
    | TiktokSearchUsersResponse503
]:
    """Search TikTok users

     Searches for TikTok users by name or keyword. Returns a paginated list of matching accounts. Use the
    `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokSearchUsersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokSearchUsersResponse200 | TiktokSearchUsersResponse400 | TiktokSearchUsersResponse401 | TiktokSearchUsersResponse402 | TiktokSearchUsersResponse403 | TiktokSearchUsersResponse404 | TiktokSearchUsersResponse422 | TiktokSearchUsersResponse429 | TiktokSearchUsersResponse500 | TiktokSearchUsersResponse503]
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
    body: TiktokSearchUsersBody,
) -> (
    TiktokSearchUsersResponse200
    | TiktokSearchUsersResponse400
    | TiktokSearchUsersResponse401
    | TiktokSearchUsersResponse402
    | TiktokSearchUsersResponse403
    | TiktokSearchUsersResponse404
    | TiktokSearchUsersResponse422
    | TiktokSearchUsersResponse429
    | TiktokSearchUsersResponse500
    | TiktokSearchUsersResponse503
    | None
):
    """Search TikTok users

     Searches for TikTok users by name or keyword. Returns a paginated list of matching accounts. Use the
    `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokSearchUsersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokSearchUsersResponse200 | TiktokSearchUsersResponse400 | TiktokSearchUsersResponse401 | TiktokSearchUsersResponse402 | TiktokSearchUsersResponse403 | TiktokSearchUsersResponse404 | TiktokSearchUsersResponse422 | TiktokSearchUsersResponse429 | TiktokSearchUsersResponse500 | TiktokSearchUsersResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokSearchUsersBody,
) -> Response[
    TiktokSearchUsersResponse200
    | TiktokSearchUsersResponse400
    | TiktokSearchUsersResponse401
    | TiktokSearchUsersResponse402
    | TiktokSearchUsersResponse403
    | TiktokSearchUsersResponse404
    | TiktokSearchUsersResponse422
    | TiktokSearchUsersResponse429
    | TiktokSearchUsersResponse500
    | TiktokSearchUsersResponse503
]:
    """Search TikTok users

     Searches for TikTok users by name or keyword. Returns a paginated list of matching accounts. Use the
    `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokSearchUsersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokSearchUsersResponse200 | TiktokSearchUsersResponse400 | TiktokSearchUsersResponse401 | TiktokSearchUsersResponse402 | TiktokSearchUsersResponse403 | TiktokSearchUsersResponse404 | TiktokSearchUsersResponse422 | TiktokSearchUsersResponse429 | TiktokSearchUsersResponse500 | TiktokSearchUsersResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokSearchUsersBody,
) -> (
    TiktokSearchUsersResponse200
    | TiktokSearchUsersResponse400
    | TiktokSearchUsersResponse401
    | TiktokSearchUsersResponse402
    | TiktokSearchUsersResponse403
    | TiktokSearchUsersResponse404
    | TiktokSearchUsersResponse422
    | TiktokSearchUsersResponse429
    | TiktokSearchUsersResponse500
    | TiktokSearchUsersResponse503
    | None
):
    """Search TikTok users

     Searches for TikTok users by name or keyword. Returns a paginated list of matching accounts. Use the
    `nextPageToken` field from the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (TiktokSearchUsersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokSearchUsersResponse200 | TiktokSearchUsersResponse400 | TiktokSearchUsersResponse401 | TiktokSearchUsersResponse402 | TiktokSearchUsersResponse403 | TiktokSearchUsersResponse404 | TiktokSearchUsersResponse422 | TiktokSearchUsersResponse429 | TiktokSearchUsersResponse500 | TiktokSearchUsersResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
