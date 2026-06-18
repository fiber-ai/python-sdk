from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.instagram_profile_body import InstagramProfileBody
from ...models.instagram_profile_response_200 import InstagramProfileResponse200
from ...models.instagram_profile_response_400 import InstagramProfileResponse400
from ...models.instagram_profile_response_401 import InstagramProfileResponse401
from ...models.instagram_profile_response_402 import InstagramProfileResponse402
from ...models.instagram_profile_response_403 import InstagramProfileResponse403
from ...models.instagram_profile_response_404 import InstagramProfileResponse404
from ...models.instagram_profile_response_422 import InstagramProfileResponse422
from ...models.instagram_profile_response_429 import InstagramProfileResponse429
from ...models.instagram_profile_response_500 import InstagramProfileResponse500
from ...models.instagram_profile_response_503 import InstagramProfileResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: InstagramProfileBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/instagram/profile",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InstagramProfileResponse200
    | InstagramProfileResponse400
    | InstagramProfileResponse401
    | InstagramProfileResponse402
    | InstagramProfileResponse403
    | InstagramProfileResponse404
    | InstagramProfileResponse422
    | InstagramProfileResponse429
    | InstagramProfileResponse500
    | InstagramProfileResponse503
    | None
):
    if response.status_code == 200:
        response_200 = InstagramProfileResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InstagramProfileResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = InstagramProfileResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = InstagramProfileResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = InstagramProfileResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = InstagramProfileResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = InstagramProfileResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = InstagramProfileResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = InstagramProfileResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = InstagramProfileResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InstagramProfileResponse200
    | InstagramProfileResponse400
    | InstagramProfileResponse401
    | InstagramProfileResponse402
    | InstagramProfileResponse403
    | InstagramProfileResponse404
    | InstagramProfileResponse422
    | InstagramProfileResponse429
    | InstagramProfileResponse500
    | InstagramProfileResponse503
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
    body: InstagramProfileBody,
) -> Response[
    InstagramProfileResponse200
    | InstagramProfileResponse400
    | InstagramProfileResponse401
    | InstagramProfileResponse402
    | InstagramProfileResponse403
    | InstagramProfileResponse404
    | InstagramProfileResponse422
    | InstagramProfileResponse429
    | InstagramProfileResponse500
    | InstagramProfileResponse503
]:
    r"""Fetch Instagram user profile

     Fetches profile information for an Instagram user including follower counts, bio, and account type.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InstagramProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstagramProfileResponse200 | InstagramProfileResponse400 | InstagramProfileResponse401 | InstagramProfileResponse402 | InstagramProfileResponse403 | InstagramProfileResponse404 | InstagramProfileResponse422 | InstagramProfileResponse429 | InstagramProfileResponse500 | InstagramProfileResponse503]
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
    body: InstagramProfileBody,
) -> (
    InstagramProfileResponse200
    | InstagramProfileResponse400
    | InstagramProfileResponse401
    | InstagramProfileResponse402
    | InstagramProfileResponse403
    | InstagramProfileResponse404
    | InstagramProfileResponse422
    | InstagramProfileResponse429
    | InstagramProfileResponse500
    | InstagramProfileResponse503
    | None
):
    r"""Fetch Instagram user profile

     Fetches profile information for an Instagram user including follower counts, bio, and account type.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InstagramProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstagramProfileResponse200 | InstagramProfileResponse400 | InstagramProfileResponse401 | InstagramProfileResponse402 | InstagramProfileResponse403 | InstagramProfileResponse404 | InstagramProfileResponse422 | InstagramProfileResponse429 | InstagramProfileResponse500 | InstagramProfileResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InstagramProfileBody,
) -> Response[
    InstagramProfileResponse200
    | InstagramProfileResponse400
    | InstagramProfileResponse401
    | InstagramProfileResponse402
    | InstagramProfileResponse403
    | InstagramProfileResponse404
    | InstagramProfileResponse422
    | InstagramProfileResponse429
    | InstagramProfileResponse500
    | InstagramProfileResponse503
]:
    r"""Fetch Instagram user profile

     Fetches profile information for an Instagram user including follower counts, bio, and account type.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InstagramProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstagramProfileResponse200 | InstagramProfileResponse400 | InstagramProfileResponse401 | InstagramProfileResponse402 | InstagramProfileResponse403 | InstagramProfileResponse404 | InstagramProfileResponse422 | InstagramProfileResponse429 | InstagramProfileResponse500 | InstagramProfileResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: InstagramProfileBody,
) -> (
    InstagramProfileResponse200
    | InstagramProfileResponse400
    | InstagramProfileResponse401
    | InstagramProfileResponse402
    | InstagramProfileResponse403
    | InstagramProfileResponse404
    | InstagramProfileResponse422
    | InstagramProfileResponse429
    | InstagramProfileResponse500
    | InstagramProfileResponse503
    | None
):
    r"""Fetch Instagram user profile

     Fetches profile information for an Instagram user including follower counts, bio, and account type.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InstagramProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstagramProfileResponse200 | InstagramProfileResponse400 | InstagramProfileResponse401 | InstagramProfileResponse402 | InstagramProfileResponse403 | InstagramProfileResponse404 | InstagramProfileResponse422 | InstagramProfileResponse429 | InstagramProfileResponse500 | InstagramProfileResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
