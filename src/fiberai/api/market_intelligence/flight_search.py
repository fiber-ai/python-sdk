from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.flight_search_body import FlightSearchBody
from ...models.flight_search_response_200 import FlightSearchResponse200
from ...models.flight_search_response_400 import FlightSearchResponse400
from ...models.flight_search_response_401 import FlightSearchResponse401
from ...models.flight_search_response_402 import FlightSearchResponse402
from ...models.flight_search_response_403 import FlightSearchResponse403
from ...models.flight_search_response_404 import FlightSearchResponse404
from ...models.flight_search_response_422 import FlightSearchResponse422
from ...models.flight_search_response_429 import FlightSearchResponse429
from ...models.flight_search_response_500 import FlightSearchResponse500
from ...models.flight_search_response_503 import FlightSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: FlightSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/flights/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FlightSearchResponse200
    | FlightSearchResponse400
    | FlightSearchResponse401
    | FlightSearchResponse402
    | FlightSearchResponse403
    | FlightSearchResponse404
    | FlightSearchResponse422
    | FlightSearchResponse429
    | FlightSearchResponse500
    | FlightSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = FlightSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FlightSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FlightSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = FlightSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = FlightSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FlightSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = FlightSearchResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = FlightSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FlightSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = FlightSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FlightSearchResponse200
    | FlightSearchResponse400
    | FlightSearchResponse401
    | FlightSearchResponse402
    | FlightSearchResponse403
    | FlightSearchResponse404
    | FlightSearchResponse422
    | FlightSearchResponse429
    | FlightSearchResponse500
    | FlightSearchResponse503
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
    body: FlightSearchBody,
) -> Response[
    FlightSearchResponse200
    | FlightSearchResponse400
    | FlightSearchResponse401
    | FlightSearchResponse402
    | FlightSearchResponse403
    | FlightSearchResponse404
    | FlightSearchResponse422
    | FlightSearchResponse429
    | FlightSearchResponse500
    | FlightSearchResponse503
]:
    """Search flights

     Searches flight itineraries between cities of interest and returns trips, fares, timing, etc.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per search&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FlightSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlightSearchResponse200 | FlightSearchResponse400 | FlightSearchResponse401 | FlightSearchResponse402 | FlightSearchResponse403 | FlightSearchResponse404 | FlightSearchResponse422 | FlightSearchResponse429 | FlightSearchResponse500 | FlightSearchResponse503]
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
    body: FlightSearchBody,
) -> (
    FlightSearchResponse200
    | FlightSearchResponse400
    | FlightSearchResponse401
    | FlightSearchResponse402
    | FlightSearchResponse403
    | FlightSearchResponse404
    | FlightSearchResponse422
    | FlightSearchResponse429
    | FlightSearchResponse500
    | FlightSearchResponse503
    | None
):
    """Search flights

     Searches flight itineraries between cities of interest and returns trips, fares, timing, etc.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per search&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FlightSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlightSearchResponse200 | FlightSearchResponse400 | FlightSearchResponse401 | FlightSearchResponse402 | FlightSearchResponse403 | FlightSearchResponse404 | FlightSearchResponse422 | FlightSearchResponse429 | FlightSearchResponse500 | FlightSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FlightSearchBody,
) -> Response[
    FlightSearchResponse200
    | FlightSearchResponse400
    | FlightSearchResponse401
    | FlightSearchResponse402
    | FlightSearchResponse403
    | FlightSearchResponse404
    | FlightSearchResponse422
    | FlightSearchResponse429
    | FlightSearchResponse500
    | FlightSearchResponse503
]:
    """Search flights

     Searches flight itineraries between cities of interest and returns trips, fares, timing, etc.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per search&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FlightSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlightSearchResponse200 | FlightSearchResponse400 | FlightSearchResponse401 | FlightSearchResponse402 | FlightSearchResponse403 | FlightSearchResponse404 | FlightSearchResponse422 | FlightSearchResponse429 | FlightSearchResponse500 | FlightSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FlightSearchBody,
) -> (
    FlightSearchResponse200
    | FlightSearchResponse400
    | FlightSearchResponse401
    | FlightSearchResponse402
    | FlightSearchResponse403
    | FlightSearchResponse404
    | FlightSearchResponse422
    | FlightSearchResponse429
    | FlightSearchResponse500
    | FlightSearchResponse503
    | None
):
    """Search flights

     Searches flight itineraries between cities of interest and returns trips, fares, timing, etc.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per search&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FlightSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlightSearchResponse200 | FlightSearchResponse400 | FlightSearchResponse401 | FlightSearchResponse402 | FlightSearchResponse403 | FlightSearchResponse404 | FlightSearchResponse422 | FlightSearchResponse429 | FlightSearchResponse500 | FlightSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
