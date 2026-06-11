from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.instagram_post_details_body import InstagramPostDetailsBody
from ...models.instagram_post_details_response_200 import InstagramPostDetailsResponse200
from ...models.instagram_post_details_response_400 import InstagramPostDetailsResponse400
from ...models.instagram_post_details_response_401 import InstagramPostDetailsResponse401
from ...models.instagram_post_details_response_402 import InstagramPostDetailsResponse402
from ...models.instagram_post_details_response_403 import InstagramPostDetailsResponse403
from ...models.instagram_post_details_response_404 import InstagramPostDetailsResponse404
from ...models.instagram_post_details_response_429 import InstagramPostDetailsResponse429
from ...models.instagram_post_details_response_500 import InstagramPostDetailsResponse500
from ...models.instagram_post_details_response_503 import InstagramPostDetailsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: InstagramPostDetailsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/instagram/post-details",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InstagramPostDetailsResponse200
    | InstagramPostDetailsResponse400
    | InstagramPostDetailsResponse401
    | InstagramPostDetailsResponse402
    | InstagramPostDetailsResponse403
    | InstagramPostDetailsResponse404
    | InstagramPostDetailsResponse429
    | InstagramPostDetailsResponse500
    | InstagramPostDetailsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = InstagramPostDetailsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InstagramPostDetailsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = InstagramPostDetailsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = InstagramPostDetailsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = InstagramPostDetailsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = InstagramPostDetailsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = InstagramPostDetailsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = InstagramPostDetailsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = InstagramPostDetailsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InstagramPostDetailsResponse200
    | InstagramPostDetailsResponse400
    | InstagramPostDetailsResponse401
    | InstagramPostDetailsResponse402
    | InstagramPostDetailsResponse403
    | InstagramPostDetailsResponse404
    | InstagramPostDetailsResponse429
    | InstagramPostDetailsResponse500
    | InstagramPostDetailsResponse503
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
    body: InstagramPostDetailsBody,
) -> Response[
    InstagramPostDetailsResponse200
    | InstagramPostDetailsResponse400
    | InstagramPostDetailsResponse401
    | InstagramPostDetailsResponse402
    | InstagramPostDetailsResponse403
    | InstagramPostDetailsResponse404
    | InstagramPostDetailsResponse429
    | InstagramPostDetailsResponse500
    | InstagramPostDetailsResponse503
]:
    r"""Fetch Instagram post details

     Fetches details for a single Instagram post including caption, like count, and media URL. Accepts a
    full post URL (e.g. 'https://www.instagram.com/p/DVoDVg5DkXM/') or a bare shortcode (e.g.
    'DVoDVg5DkXM').

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InstagramPostDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstagramPostDetailsResponse200 | InstagramPostDetailsResponse400 | InstagramPostDetailsResponse401 | InstagramPostDetailsResponse402 | InstagramPostDetailsResponse403 | InstagramPostDetailsResponse404 | InstagramPostDetailsResponse429 | InstagramPostDetailsResponse500 | InstagramPostDetailsResponse503]
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
    body: InstagramPostDetailsBody,
) -> (
    InstagramPostDetailsResponse200
    | InstagramPostDetailsResponse400
    | InstagramPostDetailsResponse401
    | InstagramPostDetailsResponse402
    | InstagramPostDetailsResponse403
    | InstagramPostDetailsResponse404
    | InstagramPostDetailsResponse429
    | InstagramPostDetailsResponse500
    | InstagramPostDetailsResponse503
    | None
):
    r"""Fetch Instagram post details

     Fetches details for a single Instagram post including caption, like count, and media URL. Accepts a
    full post URL (e.g. 'https://www.instagram.com/p/DVoDVg5DkXM/') or a bare shortcode (e.g.
    'DVoDVg5DkXM').

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InstagramPostDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstagramPostDetailsResponse200 | InstagramPostDetailsResponse400 | InstagramPostDetailsResponse401 | InstagramPostDetailsResponse402 | InstagramPostDetailsResponse403 | InstagramPostDetailsResponse404 | InstagramPostDetailsResponse429 | InstagramPostDetailsResponse500 | InstagramPostDetailsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InstagramPostDetailsBody,
) -> Response[
    InstagramPostDetailsResponse200
    | InstagramPostDetailsResponse400
    | InstagramPostDetailsResponse401
    | InstagramPostDetailsResponse402
    | InstagramPostDetailsResponse403
    | InstagramPostDetailsResponse404
    | InstagramPostDetailsResponse429
    | InstagramPostDetailsResponse500
    | InstagramPostDetailsResponse503
]:
    r"""Fetch Instagram post details

     Fetches details for a single Instagram post including caption, like count, and media URL. Accepts a
    full post URL (e.g. 'https://www.instagram.com/p/DVoDVg5DkXM/') or a bare shortcode (e.g.
    'DVoDVg5DkXM').

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InstagramPostDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstagramPostDetailsResponse200 | InstagramPostDetailsResponse400 | InstagramPostDetailsResponse401 | InstagramPostDetailsResponse402 | InstagramPostDetailsResponse403 | InstagramPostDetailsResponse404 | InstagramPostDetailsResponse429 | InstagramPostDetailsResponse500 | InstagramPostDetailsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: InstagramPostDetailsBody,
) -> (
    InstagramPostDetailsResponse200
    | InstagramPostDetailsResponse400
    | InstagramPostDetailsResponse401
    | InstagramPostDetailsResponse402
    | InstagramPostDetailsResponse403
    | InstagramPostDetailsResponse404
    | InstagramPostDetailsResponse429
    | InstagramPostDetailsResponse500
    | InstagramPostDetailsResponse503
    | None
):
    r"""Fetch Instagram post details

     Fetches details for a single Instagram post including caption, like count, and media URL. Accepts a
    full post URL (e.g. 'https://www.instagram.com/p/DVoDVg5DkXM/') or a bare shortcode (e.g.
    'DVoDVg5DkXM').

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InstagramPostDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstagramPostDetailsResponse200 | InstagramPostDetailsResponse400 | InstagramPostDetailsResponse401 | InstagramPostDetailsResponse402 | InstagramPostDetailsResponse403 | InstagramPostDetailsResponse404 | InstagramPostDetailsResponse429 | InstagramPostDetailsResponse500 | InstagramPostDetailsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
