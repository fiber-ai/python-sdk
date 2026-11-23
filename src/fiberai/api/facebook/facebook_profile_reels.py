from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.facebook_profile_reels_body import FacebookProfileReelsBody
from ...models.facebook_profile_reels_response_200 import FacebookProfileReelsResponse200
from ...models.facebook_profile_reels_response_400 import FacebookProfileReelsResponse400
from ...models.facebook_profile_reels_response_401 import FacebookProfileReelsResponse401
from ...models.facebook_profile_reels_response_402 import FacebookProfileReelsResponse402
from ...models.facebook_profile_reels_response_403 import FacebookProfileReelsResponse403
from ...models.facebook_profile_reels_response_404 import FacebookProfileReelsResponse404
from ...models.facebook_profile_reels_response_422 import FacebookProfileReelsResponse422
from ...models.facebook_profile_reels_response_429 import FacebookProfileReelsResponse429
from ...models.facebook_profile_reels_response_500 import FacebookProfileReelsResponse500
from ...models.facebook_profile_reels_response_503 import FacebookProfileReelsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: FacebookProfileReelsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/facebook/profile/reels",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FacebookProfileReelsResponse200
    | FacebookProfileReelsResponse400
    | FacebookProfileReelsResponse401
    | FacebookProfileReelsResponse402
    | FacebookProfileReelsResponse403
    | FacebookProfileReelsResponse404
    | FacebookProfileReelsResponse422
    | FacebookProfileReelsResponse429
    | FacebookProfileReelsResponse500
    | FacebookProfileReelsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = FacebookProfileReelsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FacebookProfileReelsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FacebookProfileReelsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = FacebookProfileReelsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = FacebookProfileReelsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FacebookProfileReelsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = FacebookProfileReelsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = FacebookProfileReelsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FacebookProfileReelsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = FacebookProfileReelsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FacebookProfileReelsResponse200
    | FacebookProfileReelsResponse400
    | FacebookProfileReelsResponse401
    | FacebookProfileReelsResponse402
    | FacebookProfileReelsResponse403
    | FacebookProfileReelsResponse404
    | FacebookProfileReelsResponse422
    | FacebookProfileReelsResponse429
    | FacebookProfileReelsResponse500
    | FacebookProfileReelsResponse503
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
    body: FacebookProfileReelsBody,
) -> Response[
    FacebookProfileReelsResponse200
    | FacebookProfileReelsResponse400
    | FacebookProfileReelsResponse401
    | FacebookProfileReelsResponse402
    | FacebookProfileReelsResponse403
    | FacebookProfileReelsResponse404
    | FacebookProfileReelsResponse422
    | FacebookProfileReelsResponse429
    | FacebookProfileReelsResponse500
    | FacebookProfileReelsResponse503
]:
    """Fetch Facebook page Reels

     Fetches a page of Reels from a public Facebook page or profile. Use the response's `nextPageToken`
    to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookProfileReelsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookProfileReelsResponse200 | FacebookProfileReelsResponse400 | FacebookProfileReelsResponse401 | FacebookProfileReelsResponse402 | FacebookProfileReelsResponse403 | FacebookProfileReelsResponse404 | FacebookProfileReelsResponse422 | FacebookProfileReelsResponse429 | FacebookProfileReelsResponse500 | FacebookProfileReelsResponse503]
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
    body: FacebookProfileReelsBody,
) -> (
    FacebookProfileReelsResponse200
    | FacebookProfileReelsResponse400
    | FacebookProfileReelsResponse401
    | FacebookProfileReelsResponse402
    | FacebookProfileReelsResponse403
    | FacebookProfileReelsResponse404
    | FacebookProfileReelsResponse422
    | FacebookProfileReelsResponse429
    | FacebookProfileReelsResponse500
    | FacebookProfileReelsResponse503
    | None
):
    """Fetch Facebook page Reels

     Fetches a page of Reels from a public Facebook page or profile. Use the response's `nextPageToken`
    to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookProfileReelsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookProfileReelsResponse200 | FacebookProfileReelsResponse400 | FacebookProfileReelsResponse401 | FacebookProfileReelsResponse402 | FacebookProfileReelsResponse403 | FacebookProfileReelsResponse404 | FacebookProfileReelsResponse422 | FacebookProfileReelsResponse429 | FacebookProfileReelsResponse500 | FacebookProfileReelsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookProfileReelsBody,
) -> Response[
    FacebookProfileReelsResponse200
    | FacebookProfileReelsResponse400
    | FacebookProfileReelsResponse401
    | FacebookProfileReelsResponse402
    | FacebookProfileReelsResponse403
    | FacebookProfileReelsResponse404
    | FacebookProfileReelsResponse422
    | FacebookProfileReelsResponse429
    | FacebookProfileReelsResponse500
    | FacebookProfileReelsResponse503
]:
    """Fetch Facebook page Reels

     Fetches a page of Reels from a public Facebook page or profile. Use the response's `nextPageToken`
    to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookProfileReelsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookProfileReelsResponse200 | FacebookProfileReelsResponse400 | FacebookProfileReelsResponse401 | FacebookProfileReelsResponse402 | FacebookProfileReelsResponse403 | FacebookProfileReelsResponse404 | FacebookProfileReelsResponse422 | FacebookProfileReelsResponse429 | FacebookProfileReelsResponse500 | FacebookProfileReelsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookProfileReelsBody,
) -> (
    FacebookProfileReelsResponse200
    | FacebookProfileReelsResponse400
    | FacebookProfileReelsResponse401
    | FacebookProfileReelsResponse402
    | FacebookProfileReelsResponse403
    | FacebookProfileReelsResponse404
    | FacebookProfileReelsResponse422
    | FacebookProfileReelsResponse429
    | FacebookProfileReelsResponse500
    | FacebookProfileReelsResponse503
    | None
):
    """Fetch Facebook page Reels

     Fetches a page of Reels from a public Facebook page or profile. Use the response's `nextPageToken`
    to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookProfileReelsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookProfileReelsResponse200 | FacebookProfileReelsResponse400 | FacebookProfileReelsResponse401 | FacebookProfileReelsResponse402 | FacebookProfileReelsResponse403 | FacebookProfileReelsResponse404 | FacebookProfileReelsResponse422 | FacebookProfileReelsResponse429 | FacebookProfileReelsResponse500 | FacebookProfileReelsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
