from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fetch_real_estate_listings_body import FetchRealEstateListingsBody
from ...models.fetch_real_estate_listings_response_200 import FetchRealEstateListingsResponse200
from ...models.fetch_real_estate_listings_response_400 import FetchRealEstateListingsResponse400
from ...models.fetch_real_estate_listings_response_401 import FetchRealEstateListingsResponse401
from ...models.fetch_real_estate_listings_response_402 import FetchRealEstateListingsResponse402
from ...models.fetch_real_estate_listings_response_403 import FetchRealEstateListingsResponse403
from ...models.fetch_real_estate_listings_response_404 import FetchRealEstateListingsResponse404
from ...models.fetch_real_estate_listings_response_429 import FetchRealEstateListingsResponse429
from ...models.fetch_real_estate_listings_response_500 import FetchRealEstateListingsResponse500
from ...models.fetch_real_estate_listings_response_503 import FetchRealEstateListingsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: FetchRealEstateListingsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/real-estate/listings",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FetchRealEstateListingsResponse200
    | FetchRealEstateListingsResponse400
    | FetchRealEstateListingsResponse401
    | FetchRealEstateListingsResponse402
    | FetchRealEstateListingsResponse403
    | FetchRealEstateListingsResponse404
    | FetchRealEstateListingsResponse429
    | FetchRealEstateListingsResponse500
    | FetchRealEstateListingsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = FetchRealEstateListingsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FetchRealEstateListingsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FetchRealEstateListingsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = FetchRealEstateListingsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = FetchRealEstateListingsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FetchRealEstateListingsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = FetchRealEstateListingsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FetchRealEstateListingsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = FetchRealEstateListingsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FetchRealEstateListingsResponse200
    | FetchRealEstateListingsResponse400
    | FetchRealEstateListingsResponse401
    | FetchRealEstateListingsResponse402
    | FetchRealEstateListingsResponse403
    | FetchRealEstateListingsResponse404
    | FetchRealEstateListingsResponse429
    | FetchRealEstateListingsResponse500
    | FetchRealEstateListingsResponse503
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
    body: FetchRealEstateListingsBody,
) -> Response[
    FetchRealEstateListingsResponse200
    | FetchRealEstateListingsResponse400
    | FetchRealEstateListingsResponse401
    | FetchRealEstateListingsResponse402
    | FetchRealEstateListingsResponse403
    | FetchRealEstateListingsResponse404
    | FetchRealEstateListingsResponse429
    | FetchRealEstateListingsResponse500
    | FetchRealEstateListingsResponse503
]:
    r"""Fetch real estate listings

     Fetches real estate listings by location and optional filters such as listing status, price ranges,
    home types, and property features. Data is available for all 50 US states, D.C., Puerto Rico, and
    all 13 Canadian provinces and territories.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.\">ⓘ</span></span>

    Args:
        body (FetchRealEstateListingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FetchRealEstateListingsResponse200 | FetchRealEstateListingsResponse400 | FetchRealEstateListingsResponse401 | FetchRealEstateListingsResponse402 | FetchRealEstateListingsResponse403 | FetchRealEstateListingsResponse404 | FetchRealEstateListingsResponse429 | FetchRealEstateListingsResponse500 | FetchRealEstateListingsResponse503]
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
    body: FetchRealEstateListingsBody,
) -> (
    FetchRealEstateListingsResponse200
    | FetchRealEstateListingsResponse400
    | FetchRealEstateListingsResponse401
    | FetchRealEstateListingsResponse402
    | FetchRealEstateListingsResponse403
    | FetchRealEstateListingsResponse404
    | FetchRealEstateListingsResponse429
    | FetchRealEstateListingsResponse500
    | FetchRealEstateListingsResponse503
    | None
):
    r"""Fetch real estate listings

     Fetches real estate listings by location and optional filters such as listing status, price ranges,
    home types, and property features. Data is available for all 50 US states, D.C., Puerto Rico, and
    all 13 Canadian provinces and territories.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.\">ⓘ</span></span>

    Args:
        body (FetchRealEstateListingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FetchRealEstateListingsResponse200 | FetchRealEstateListingsResponse400 | FetchRealEstateListingsResponse401 | FetchRealEstateListingsResponse402 | FetchRealEstateListingsResponse403 | FetchRealEstateListingsResponse404 | FetchRealEstateListingsResponse429 | FetchRealEstateListingsResponse500 | FetchRealEstateListingsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FetchRealEstateListingsBody,
) -> Response[
    FetchRealEstateListingsResponse200
    | FetchRealEstateListingsResponse400
    | FetchRealEstateListingsResponse401
    | FetchRealEstateListingsResponse402
    | FetchRealEstateListingsResponse403
    | FetchRealEstateListingsResponse404
    | FetchRealEstateListingsResponse429
    | FetchRealEstateListingsResponse500
    | FetchRealEstateListingsResponse503
]:
    r"""Fetch real estate listings

     Fetches real estate listings by location and optional filters such as listing status, price ranges,
    home types, and property features. Data is available for all 50 US states, D.C., Puerto Rico, and
    all 13 Canadian provinces and territories.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.\">ⓘ</span></span>

    Args:
        body (FetchRealEstateListingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FetchRealEstateListingsResponse200 | FetchRealEstateListingsResponse400 | FetchRealEstateListingsResponse401 | FetchRealEstateListingsResponse402 | FetchRealEstateListingsResponse403 | FetchRealEstateListingsResponse404 | FetchRealEstateListingsResponse429 | FetchRealEstateListingsResponse500 | FetchRealEstateListingsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FetchRealEstateListingsBody,
) -> (
    FetchRealEstateListingsResponse200
    | FetchRealEstateListingsResponse400
    | FetchRealEstateListingsResponse401
    | FetchRealEstateListingsResponse402
    | FetchRealEstateListingsResponse403
    | FetchRealEstateListingsResponse404
    | FetchRealEstateListingsResponse429
    | FetchRealEstateListingsResponse500
    | FetchRealEstateListingsResponse503
    | None
):
    r"""Fetch real estate listings

     Fetches real estate listings by location and optional filters such as listing status, price ranges,
    home types, and property features. Data is available for all 50 US states, D.C., Puerto Rico, and
    all 13 Canadian provinces and territories.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.\">ⓘ</span></span>

    Args:
        body (FetchRealEstateListingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FetchRealEstateListingsResponse200 | FetchRealEstateListingsResponse400 | FetchRealEstateListingsResponse401 | FetchRealEstateListingsResponse402 | FetchRealEstateListingsResponse403 | FetchRealEstateListingsResponse404 | FetchRealEstateListingsResponse429 | FetchRealEstateListingsResponse500 | FetchRealEstateListingsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
