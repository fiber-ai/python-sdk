from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.flight_deals_body import FlightDealsBody
from ...models.flight_deals_response_200 import FlightDealsResponse200
from ...models.flight_deals_response_400 import FlightDealsResponse400
from ...models.flight_deals_response_401 import FlightDealsResponse401
from ...models.flight_deals_response_402 import FlightDealsResponse402
from ...models.flight_deals_response_403 import FlightDealsResponse403
from ...models.flight_deals_response_404 import FlightDealsResponse404
from ...models.flight_deals_response_422 import FlightDealsResponse422
from ...models.flight_deals_response_429 import FlightDealsResponse429
from ...models.flight_deals_response_500 import FlightDealsResponse500
from ...models.flight_deals_response_503 import FlightDealsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: FlightDealsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/flights/deals",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FlightDealsResponse200
    | FlightDealsResponse400
    | FlightDealsResponse401
    | FlightDealsResponse402
    | FlightDealsResponse403
    | FlightDealsResponse404
    | FlightDealsResponse422
    | FlightDealsResponse429
    | FlightDealsResponse500
    | FlightDealsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = FlightDealsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FlightDealsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FlightDealsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = FlightDealsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = FlightDealsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FlightDealsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = FlightDealsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = FlightDealsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FlightDealsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = FlightDealsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FlightDealsResponse200
    | FlightDealsResponse400
    | FlightDealsResponse401
    | FlightDealsResponse402
    | FlightDealsResponse403
    | FlightDealsResponse404
    | FlightDealsResponse422
    | FlightDealsResponse429
    | FlightDealsResponse500
    | FlightDealsResponse503
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
    body: FlightDealsBody,
) -> Response[
    FlightDealsResponse200
    | FlightDealsResponse400
    | FlightDealsResponse401
    | FlightDealsResponse402
    | FlightDealsResponse403
    | FlightDealsResponse404
    | FlightDealsResponse422
    | FlightDealsResponse429
    | FlightDealsResponse500
    | FlightDealsResponse503
]:
    """Search flight deals

     Returns cheap round-trip flight deals from a given departure location, ranked by how much cheaper
    they are than usual. Dates and destinations are chosen per deal; use flight search when you already
    know the route and dates.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FlightDealsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlightDealsResponse200 | FlightDealsResponse400 | FlightDealsResponse401 | FlightDealsResponse402 | FlightDealsResponse403 | FlightDealsResponse404 | FlightDealsResponse422 | FlightDealsResponse429 | FlightDealsResponse500 | FlightDealsResponse503]
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
    body: FlightDealsBody,
) -> (
    FlightDealsResponse200
    | FlightDealsResponse400
    | FlightDealsResponse401
    | FlightDealsResponse402
    | FlightDealsResponse403
    | FlightDealsResponse404
    | FlightDealsResponse422
    | FlightDealsResponse429
    | FlightDealsResponse500
    | FlightDealsResponse503
    | None
):
    """Search flight deals

     Returns cheap round-trip flight deals from a given departure location, ranked by how much cheaper
    they are than usual. Dates and destinations are chosen per deal; use flight search when you already
    know the route and dates.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FlightDealsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlightDealsResponse200 | FlightDealsResponse400 | FlightDealsResponse401 | FlightDealsResponse402 | FlightDealsResponse403 | FlightDealsResponse404 | FlightDealsResponse422 | FlightDealsResponse429 | FlightDealsResponse500 | FlightDealsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FlightDealsBody,
) -> Response[
    FlightDealsResponse200
    | FlightDealsResponse400
    | FlightDealsResponse401
    | FlightDealsResponse402
    | FlightDealsResponse403
    | FlightDealsResponse404
    | FlightDealsResponse422
    | FlightDealsResponse429
    | FlightDealsResponse500
    | FlightDealsResponse503
]:
    """Search flight deals

     Returns cheap round-trip flight deals from a given departure location, ranked by how much cheaper
    they are than usual. Dates and destinations are chosen per deal; use flight search when you already
    know the route and dates.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FlightDealsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlightDealsResponse200 | FlightDealsResponse400 | FlightDealsResponse401 | FlightDealsResponse402 | FlightDealsResponse403 | FlightDealsResponse404 | FlightDealsResponse422 | FlightDealsResponse429 | FlightDealsResponse500 | FlightDealsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FlightDealsBody,
) -> (
    FlightDealsResponse200
    | FlightDealsResponse400
    | FlightDealsResponse401
    | FlightDealsResponse402
    | FlightDealsResponse403
    | FlightDealsResponse404
    | FlightDealsResponse422
    | FlightDealsResponse429
    | FlightDealsResponse500
    | FlightDealsResponse503
    | None
):
    """Search flight deals

     Returns cheap round-trip flight deals from a given departure location, ranked by how much cheaper
    they are than usual. Dates and destinations are chosen per deal; use flight search when you already
    know the route and dates.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FlightDealsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlightDealsResponse200 | FlightDealsResponse400 | FlightDealsResponse401 | FlightDealsResponse402 | FlightDealsResponse403 | FlightDealsResponse404 | FlightDealsResponse422 | FlightDealsResponse429 | FlightDealsResponse500 | FlightDealsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
