from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.booking_search_body import BookingSearchBody
from ...models.booking_search_response_200 import BookingSearchResponse200
from ...models.booking_search_response_400 import BookingSearchResponse400
from ...models.booking_search_response_401 import BookingSearchResponse401
from ...models.booking_search_response_402 import BookingSearchResponse402
from ...models.booking_search_response_403 import BookingSearchResponse403
from ...models.booking_search_response_404 import BookingSearchResponse404
from ...models.booking_search_response_422 import BookingSearchResponse422
from ...models.booking_search_response_429 import BookingSearchResponse429
from ...models.booking_search_response_500 import BookingSearchResponse500
from ...models.booking_search_response_503 import BookingSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: BookingSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/booking/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    BookingSearchResponse200
    | BookingSearchResponse400
    | BookingSearchResponse401
    | BookingSearchResponse402
    | BookingSearchResponse403
    | BookingSearchResponse404
    | BookingSearchResponse422
    | BookingSearchResponse429
    | BookingSearchResponse500
    | BookingSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = BookingSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = BookingSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = BookingSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = BookingSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = BookingSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = BookingSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = BookingSearchResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = BookingSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = BookingSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = BookingSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    BookingSearchResponse200
    | BookingSearchResponse400
    | BookingSearchResponse401
    | BookingSearchResponse402
    | BookingSearchResponse403
    | BookingSearchResponse404
    | BookingSearchResponse422
    | BookingSearchResponse429
    | BookingSearchResponse500
    | BookingSearchResponse503
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
    body: BookingSearchBody,
) -> Response[
    BookingSearchResponse200
    | BookingSearchResponse400
    | BookingSearchResponse401
    | BookingSearchResponse402
    | BookingSearchResponse403
    | BookingSearchResponse404
    | BookingSearchResponse422
    | BookingSearchResponse429
    | BookingSearchResponse500
    | BookingSearchResponse503
]:
    """Search Booking.com properties

     Searches Booking.com stays for a destination and returns matching properties with rates, ratings,
    and availability.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per search&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (BookingSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingSearchResponse200 | BookingSearchResponse400 | BookingSearchResponse401 | BookingSearchResponse402 | BookingSearchResponse403 | BookingSearchResponse404 | BookingSearchResponse422 | BookingSearchResponse429 | BookingSearchResponse500 | BookingSearchResponse503]
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
    body: BookingSearchBody,
) -> (
    BookingSearchResponse200
    | BookingSearchResponse400
    | BookingSearchResponse401
    | BookingSearchResponse402
    | BookingSearchResponse403
    | BookingSearchResponse404
    | BookingSearchResponse422
    | BookingSearchResponse429
    | BookingSearchResponse500
    | BookingSearchResponse503
    | None
):
    """Search Booking.com properties

     Searches Booking.com stays for a destination and returns matching properties with rates, ratings,
    and availability.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per search&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (BookingSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingSearchResponse200 | BookingSearchResponse400 | BookingSearchResponse401 | BookingSearchResponse402 | BookingSearchResponse403 | BookingSearchResponse404 | BookingSearchResponse422 | BookingSearchResponse429 | BookingSearchResponse500 | BookingSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BookingSearchBody,
) -> Response[
    BookingSearchResponse200
    | BookingSearchResponse400
    | BookingSearchResponse401
    | BookingSearchResponse402
    | BookingSearchResponse403
    | BookingSearchResponse404
    | BookingSearchResponse422
    | BookingSearchResponse429
    | BookingSearchResponse500
    | BookingSearchResponse503
]:
    """Search Booking.com properties

     Searches Booking.com stays for a destination and returns matching properties with rates, ratings,
    and availability.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per search&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (BookingSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingSearchResponse200 | BookingSearchResponse400 | BookingSearchResponse401 | BookingSearchResponse402 | BookingSearchResponse403 | BookingSearchResponse404 | BookingSearchResponse422 | BookingSearchResponse429 | BookingSearchResponse500 | BookingSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BookingSearchBody,
) -> (
    BookingSearchResponse200
    | BookingSearchResponse400
    | BookingSearchResponse401
    | BookingSearchResponse402
    | BookingSearchResponse403
    | BookingSearchResponse404
    | BookingSearchResponse422
    | BookingSearchResponse429
    | BookingSearchResponse500
    | BookingSearchResponse503
    | None
):
    """Search Booking.com properties

     Searches Booking.com stays for a destination and returns matching properties with rates, ratings,
    and availability.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per search&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (BookingSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingSearchResponse200 | BookingSearchResponse400 | BookingSearchResponse401 | BookingSearchResponse402 | BookingSearchResponse403 | BookingSearchResponse404 | BookingSearchResponse422 | BookingSearchResponse429 | BookingSearchResponse500 | BookingSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
