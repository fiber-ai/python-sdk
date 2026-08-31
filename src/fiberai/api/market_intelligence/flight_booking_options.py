from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.flight_booking_options_body import FlightBookingOptionsBody
from ...models.flight_booking_options_response_200 import FlightBookingOptionsResponse200
from ...models.flight_booking_options_response_400 import FlightBookingOptionsResponse400
from ...models.flight_booking_options_response_401 import FlightBookingOptionsResponse401
from ...models.flight_booking_options_response_402 import FlightBookingOptionsResponse402
from ...models.flight_booking_options_response_403 import FlightBookingOptionsResponse403
from ...models.flight_booking_options_response_404 import FlightBookingOptionsResponse404
from ...models.flight_booking_options_response_422 import FlightBookingOptionsResponse422
from ...models.flight_booking_options_response_429 import FlightBookingOptionsResponse429
from ...models.flight_booking_options_response_500 import FlightBookingOptionsResponse500
from ...models.flight_booking_options_response_503 import FlightBookingOptionsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: FlightBookingOptionsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/flights/booking-options",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FlightBookingOptionsResponse200
    | FlightBookingOptionsResponse400
    | FlightBookingOptionsResponse401
    | FlightBookingOptionsResponse402
    | FlightBookingOptionsResponse403
    | FlightBookingOptionsResponse404
    | FlightBookingOptionsResponse422
    | FlightBookingOptionsResponse429
    | FlightBookingOptionsResponse500
    | FlightBookingOptionsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = FlightBookingOptionsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FlightBookingOptionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FlightBookingOptionsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = FlightBookingOptionsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = FlightBookingOptionsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FlightBookingOptionsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = FlightBookingOptionsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = FlightBookingOptionsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FlightBookingOptionsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = FlightBookingOptionsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FlightBookingOptionsResponse200
    | FlightBookingOptionsResponse400
    | FlightBookingOptionsResponse401
    | FlightBookingOptionsResponse402
    | FlightBookingOptionsResponse403
    | FlightBookingOptionsResponse404
    | FlightBookingOptionsResponse422
    | FlightBookingOptionsResponse429
    | FlightBookingOptionsResponse500
    | FlightBookingOptionsResponse503
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
    body: FlightBookingOptionsBody,
) -> Response[
    FlightBookingOptionsResponse200
    | FlightBookingOptionsResponse400
    | FlightBookingOptionsResponse401
    | FlightBookingOptionsResponse402
    | FlightBookingOptionsResponse403
    | FlightBookingOptionsResponse404
    | FlightBookingOptionsResponse422
    | FlightBookingOptionsResponse429
    | FlightBookingOptionsResponse500
    | FlightBookingOptionsResponse503
]:
    """Get flight booking options

     Retrieves booking options (providers, fares, booking links, and available cabin classes) for a
    single itinerary selected from a flight search. Pass the `bookingToken` returned on an itinerary
    from `POST /v1/flights/search` along with the same trip configuration.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per lookup&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FlightBookingOptionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlightBookingOptionsResponse200 | FlightBookingOptionsResponse400 | FlightBookingOptionsResponse401 | FlightBookingOptionsResponse402 | FlightBookingOptionsResponse403 | FlightBookingOptionsResponse404 | FlightBookingOptionsResponse422 | FlightBookingOptionsResponse429 | FlightBookingOptionsResponse500 | FlightBookingOptionsResponse503]
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
    body: FlightBookingOptionsBody,
) -> (
    FlightBookingOptionsResponse200
    | FlightBookingOptionsResponse400
    | FlightBookingOptionsResponse401
    | FlightBookingOptionsResponse402
    | FlightBookingOptionsResponse403
    | FlightBookingOptionsResponse404
    | FlightBookingOptionsResponse422
    | FlightBookingOptionsResponse429
    | FlightBookingOptionsResponse500
    | FlightBookingOptionsResponse503
    | None
):
    """Get flight booking options

     Retrieves booking options (providers, fares, booking links, and available cabin classes) for a
    single itinerary selected from a flight search. Pass the `bookingToken` returned on an itinerary
    from `POST /v1/flights/search` along with the same trip configuration.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per lookup&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FlightBookingOptionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlightBookingOptionsResponse200 | FlightBookingOptionsResponse400 | FlightBookingOptionsResponse401 | FlightBookingOptionsResponse402 | FlightBookingOptionsResponse403 | FlightBookingOptionsResponse404 | FlightBookingOptionsResponse422 | FlightBookingOptionsResponse429 | FlightBookingOptionsResponse500 | FlightBookingOptionsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FlightBookingOptionsBody,
) -> Response[
    FlightBookingOptionsResponse200
    | FlightBookingOptionsResponse400
    | FlightBookingOptionsResponse401
    | FlightBookingOptionsResponse402
    | FlightBookingOptionsResponse403
    | FlightBookingOptionsResponse404
    | FlightBookingOptionsResponse422
    | FlightBookingOptionsResponse429
    | FlightBookingOptionsResponse500
    | FlightBookingOptionsResponse503
]:
    """Get flight booking options

     Retrieves booking options (providers, fares, booking links, and available cabin classes) for a
    single itinerary selected from a flight search. Pass the `bookingToken` returned on an itinerary
    from `POST /v1/flights/search` along with the same trip configuration.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per lookup&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FlightBookingOptionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FlightBookingOptionsResponse200 | FlightBookingOptionsResponse400 | FlightBookingOptionsResponse401 | FlightBookingOptionsResponse402 | FlightBookingOptionsResponse403 | FlightBookingOptionsResponse404 | FlightBookingOptionsResponse422 | FlightBookingOptionsResponse429 | FlightBookingOptionsResponse500 | FlightBookingOptionsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FlightBookingOptionsBody,
) -> (
    FlightBookingOptionsResponse200
    | FlightBookingOptionsResponse400
    | FlightBookingOptionsResponse401
    | FlightBookingOptionsResponse402
    | FlightBookingOptionsResponse403
    | FlightBookingOptionsResponse404
    | FlightBookingOptionsResponse422
    | FlightBookingOptionsResponse429
    | FlightBookingOptionsResponse500
    | FlightBookingOptionsResponse503
    | None
):
    """Get flight booking options

     Retrieves booking options (providers, fares, booking links, and available cabin classes) for a
    single itinerary selected from a flight search. Pass the `bookingToken` returned on an itinerary
    from `POST /v1/flights/search` along with the same trip configuration.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per lookup&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FlightBookingOptionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FlightBookingOptionsResponse200 | FlightBookingOptionsResponse400 | FlightBookingOptionsResponse401 | FlightBookingOptionsResponse402 | FlightBookingOptionsResponse403 | FlightBookingOptionsResponse404 | FlightBookingOptionsResponse422 | FlightBookingOptionsResponse429 | FlightBookingOptionsResponse500 | FlightBookingOptionsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
