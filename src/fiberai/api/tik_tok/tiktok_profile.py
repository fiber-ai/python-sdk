from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tiktok_profile_body import TiktokProfileBody
from ...models.tiktok_profile_response_200 import TiktokProfileResponse200
from ...models.tiktok_profile_response_400 import TiktokProfileResponse400
from ...models.tiktok_profile_response_401 import TiktokProfileResponse401
from ...models.tiktok_profile_response_402 import TiktokProfileResponse402
from ...models.tiktok_profile_response_403 import TiktokProfileResponse403
from ...models.tiktok_profile_response_404 import TiktokProfileResponse404
from ...models.tiktok_profile_response_422 import TiktokProfileResponse422
from ...models.tiktok_profile_response_429 import TiktokProfileResponse429
from ...models.tiktok_profile_response_500 import TiktokProfileResponse500
from ...models.tiktok_profile_response_503 import TiktokProfileResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TiktokProfileBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tiktok/profile",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TiktokProfileResponse200
    | TiktokProfileResponse400
    | TiktokProfileResponse401
    | TiktokProfileResponse402
    | TiktokProfileResponse403
    | TiktokProfileResponse404
    | TiktokProfileResponse422
    | TiktokProfileResponse429
    | TiktokProfileResponse500
    | TiktokProfileResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TiktokProfileResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TiktokProfileResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TiktokProfileResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TiktokProfileResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TiktokProfileResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TiktokProfileResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = TiktokProfileResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = TiktokProfileResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TiktokProfileResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TiktokProfileResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TiktokProfileResponse200
    | TiktokProfileResponse400
    | TiktokProfileResponse401
    | TiktokProfileResponse402
    | TiktokProfileResponse403
    | TiktokProfileResponse404
    | TiktokProfileResponse422
    | TiktokProfileResponse429
    | TiktokProfileResponse500
    | TiktokProfileResponse503
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
    body: TiktokProfileBody,
) -> Response[
    TiktokProfileResponse200
    | TiktokProfileResponse400
    | TiktokProfileResponse401
    | TiktokProfileResponse402
    | TiktokProfileResponse403
    | TiktokProfileResponse404
    | TiktokProfileResponse422
    | TiktokProfileResponse429
    | TiktokProfileResponse500
    | TiktokProfileResponse503
]:
    r"""Fetch TikTok user profile

     Fetches profile information for a TikTok user including follower counts, bio, and account type.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokProfileResponse200 | TiktokProfileResponse400 | TiktokProfileResponse401 | TiktokProfileResponse402 | TiktokProfileResponse403 | TiktokProfileResponse404 | TiktokProfileResponse422 | TiktokProfileResponse429 | TiktokProfileResponse500 | TiktokProfileResponse503]
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
    body: TiktokProfileBody,
) -> (
    TiktokProfileResponse200
    | TiktokProfileResponse400
    | TiktokProfileResponse401
    | TiktokProfileResponse402
    | TiktokProfileResponse403
    | TiktokProfileResponse404
    | TiktokProfileResponse422
    | TiktokProfileResponse429
    | TiktokProfileResponse500
    | TiktokProfileResponse503
    | None
):
    r"""Fetch TikTok user profile

     Fetches profile information for a TikTok user including follower counts, bio, and account type.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokProfileResponse200 | TiktokProfileResponse400 | TiktokProfileResponse401 | TiktokProfileResponse402 | TiktokProfileResponse403 | TiktokProfileResponse404 | TiktokProfileResponse422 | TiktokProfileResponse429 | TiktokProfileResponse500 | TiktokProfileResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokProfileBody,
) -> Response[
    TiktokProfileResponse200
    | TiktokProfileResponse400
    | TiktokProfileResponse401
    | TiktokProfileResponse402
    | TiktokProfileResponse403
    | TiktokProfileResponse404
    | TiktokProfileResponse422
    | TiktokProfileResponse429
    | TiktokProfileResponse500
    | TiktokProfileResponse503
]:
    r"""Fetch TikTok user profile

     Fetches profile information for a TikTok user including follower counts, bio, and account type.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokProfileResponse200 | TiktokProfileResponse400 | TiktokProfileResponse401 | TiktokProfileResponse402 | TiktokProfileResponse403 | TiktokProfileResponse404 | TiktokProfileResponse422 | TiktokProfileResponse429 | TiktokProfileResponse500 | TiktokProfileResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokProfileBody,
) -> (
    TiktokProfileResponse200
    | TiktokProfileResponse400
    | TiktokProfileResponse401
    | TiktokProfileResponse402
    | TiktokProfileResponse403
    | TiktokProfileResponse404
    | TiktokProfileResponse422
    | TiktokProfileResponse429
    | TiktokProfileResponse500
    | TiktokProfileResponse503
    | None
):
    r"""Fetch TikTok user profile

     Fetches profile information for a TikTok user including follower counts, bio, and account type.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokProfileResponse200 | TiktokProfileResponse400 | TiktokProfileResponse401 | TiktokProfileResponse402 | TiktokProfileResponse403 | TiktokProfileResponse404 | TiktokProfileResponse422 | TiktokProfileResponse429 | TiktokProfileResponse500 | TiktokProfileResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
