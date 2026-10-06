from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.booking_property_body import BookingPropertyBody
from ...models.booking_property_response_200 import BookingPropertyResponse200
from ...models.booking_property_response_400 import BookingPropertyResponse400
from ...models.booking_property_response_401 import BookingPropertyResponse401
from ...models.booking_property_response_402 import BookingPropertyResponse402
from ...models.booking_property_response_403 import BookingPropertyResponse403
from ...models.booking_property_response_404 import BookingPropertyResponse404
from ...models.booking_property_response_422 import BookingPropertyResponse422
from ...models.booking_property_response_429 import BookingPropertyResponse429
from ...models.booking_property_response_500 import BookingPropertyResponse500
from ...models.booking_property_response_503 import BookingPropertyResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: BookingPropertyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/booking/property",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    BookingPropertyResponse200
    | BookingPropertyResponse400
    | BookingPropertyResponse401
    | BookingPropertyResponse402
    | BookingPropertyResponse403
    | BookingPropertyResponse404
    | BookingPropertyResponse422
    | BookingPropertyResponse429
    | BookingPropertyResponse500
    | BookingPropertyResponse503
    | None
):
    if response.status_code == 200:
        response_200 = BookingPropertyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = BookingPropertyResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = BookingPropertyResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = BookingPropertyResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = BookingPropertyResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = BookingPropertyResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = BookingPropertyResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = BookingPropertyResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = BookingPropertyResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = BookingPropertyResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    BookingPropertyResponse200
    | BookingPropertyResponse400
    | BookingPropertyResponse401
    | BookingPropertyResponse402
    | BookingPropertyResponse403
    | BookingPropertyResponse404
    | BookingPropertyResponse422
    | BookingPropertyResponse429
    | BookingPropertyResponse500
    | BookingPropertyResponse503
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
    body: BookingPropertyBody,
) -> Response[
    BookingPropertyResponse200
    | BookingPropertyResponse400
    | BookingPropertyResponse401
    | BookingPropertyResponse402
    | BookingPropertyResponse403
    | BookingPropertyResponse404
    | BookingPropertyResponse422
    | BookingPropertyResponse429
    | BookingPropertyResponse500
    | BookingPropertyResponse503
]:
    """Get Booking.com property details

     Retrieves full details for a single Booking.com property, including amenities, photos, scores, and
    house rules.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per property lookup&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (BookingPropertyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingPropertyResponse200 | BookingPropertyResponse400 | BookingPropertyResponse401 | BookingPropertyResponse402 | BookingPropertyResponse403 | BookingPropertyResponse404 | BookingPropertyResponse422 | BookingPropertyResponse429 | BookingPropertyResponse500 | BookingPropertyResponse503]
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
    body: BookingPropertyBody,
) -> (
    BookingPropertyResponse200
    | BookingPropertyResponse400
    | BookingPropertyResponse401
    | BookingPropertyResponse402
    | BookingPropertyResponse403
    | BookingPropertyResponse404
    | BookingPropertyResponse422
    | BookingPropertyResponse429
    | BookingPropertyResponse500
    | BookingPropertyResponse503
    | None
):
    """Get Booking.com property details

     Retrieves full details for a single Booking.com property, including amenities, photos, scores, and
    house rules.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per property lookup&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (BookingPropertyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingPropertyResponse200 | BookingPropertyResponse400 | BookingPropertyResponse401 | BookingPropertyResponse402 | BookingPropertyResponse403 | BookingPropertyResponse404 | BookingPropertyResponse422 | BookingPropertyResponse429 | BookingPropertyResponse500 | BookingPropertyResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BookingPropertyBody,
) -> Response[
    BookingPropertyResponse200
    | BookingPropertyResponse400
    | BookingPropertyResponse401
    | BookingPropertyResponse402
    | BookingPropertyResponse403
    | BookingPropertyResponse404
    | BookingPropertyResponse422
    | BookingPropertyResponse429
    | BookingPropertyResponse500
    | BookingPropertyResponse503
]:
    """Get Booking.com property details

     Retrieves full details for a single Booking.com property, including amenities, photos, scores, and
    house rules.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per property lookup&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (BookingPropertyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingPropertyResponse200 | BookingPropertyResponse400 | BookingPropertyResponse401 | BookingPropertyResponse402 | BookingPropertyResponse403 | BookingPropertyResponse404 | BookingPropertyResponse422 | BookingPropertyResponse429 | BookingPropertyResponse500 | BookingPropertyResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BookingPropertyBody,
) -> (
    BookingPropertyResponse200
    | BookingPropertyResponse400
    | BookingPropertyResponse401
    | BookingPropertyResponse402
    | BookingPropertyResponse403
    | BookingPropertyResponse404
    | BookingPropertyResponse422
    | BookingPropertyResponse429
    | BookingPropertyResponse500
    | BookingPropertyResponse503
    | None
):
    """Get Booking.com property details

     Retrieves full details for a single Booking.com property, including amenities, photos, scores, and
    house rules.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per property lookup&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (BookingPropertyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingPropertyResponse200 | BookingPropertyResponse400 | BookingPropertyResponse401 | BookingPropertyResponse402 | BookingPropertyResponse403 | BookingPropertyResponse404 | BookingPropertyResponse422 | BookingPropertyResponse429 | BookingPropertyResponse500 | BookingPropertyResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
