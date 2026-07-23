from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hotel_property_body import HotelPropertyBody
from ...models.hotel_property_response_200 import HotelPropertyResponse200
from ...models.hotel_property_response_400 import HotelPropertyResponse400
from ...models.hotel_property_response_401 import HotelPropertyResponse401
from ...models.hotel_property_response_402 import HotelPropertyResponse402
from ...models.hotel_property_response_403 import HotelPropertyResponse403
from ...models.hotel_property_response_404 import HotelPropertyResponse404
from ...models.hotel_property_response_422 import HotelPropertyResponse422
from ...models.hotel_property_response_429 import HotelPropertyResponse429
from ...models.hotel_property_response_500 import HotelPropertyResponse500
from ...models.hotel_property_response_503 import HotelPropertyResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: HotelPropertyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/hotels/property",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HotelPropertyResponse200
    | HotelPropertyResponse400
    | HotelPropertyResponse401
    | HotelPropertyResponse402
    | HotelPropertyResponse403
    | HotelPropertyResponse404
    | HotelPropertyResponse422
    | HotelPropertyResponse429
    | HotelPropertyResponse500
    | HotelPropertyResponse503
    | None
):
    if response.status_code == 200:
        response_200 = HotelPropertyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = HotelPropertyResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = HotelPropertyResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = HotelPropertyResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = HotelPropertyResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = HotelPropertyResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = HotelPropertyResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = HotelPropertyResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = HotelPropertyResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = HotelPropertyResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    HotelPropertyResponse200
    | HotelPropertyResponse400
    | HotelPropertyResponse401
    | HotelPropertyResponse402
    | HotelPropertyResponse403
    | HotelPropertyResponse404
    | HotelPropertyResponse422
    | HotelPropertyResponse429
    | HotelPropertyResponse500
    | HotelPropertyResponse503
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
    body: HotelPropertyBody,
) -> Response[
    HotelPropertyResponse200
    | HotelPropertyResponse400
    | HotelPropertyResponse401
    | HotelPropertyResponse402
    | HotelPropertyResponse403
    | HotelPropertyResponse404
    | HotelPropertyResponse422
    | HotelPropertyResponse429
    | HotelPropertyResponse500
    | HotelPropertyResponse503
]:
    r"""Get hotel property details

     Retrieves full details for a single hotel or vacation rental, including amenities, images, and
    booking offers.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per property lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (HotelPropertyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HotelPropertyResponse200 | HotelPropertyResponse400 | HotelPropertyResponse401 | HotelPropertyResponse402 | HotelPropertyResponse403 | HotelPropertyResponse404 | HotelPropertyResponse422 | HotelPropertyResponse429 | HotelPropertyResponse500 | HotelPropertyResponse503]
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
    body: HotelPropertyBody,
) -> (
    HotelPropertyResponse200
    | HotelPropertyResponse400
    | HotelPropertyResponse401
    | HotelPropertyResponse402
    | HotelPropertyResponse403
    | HotelPropertyResponse404
    | HotelPropertyResponse422
    | HotelPropertyResponse429
    | HotelPropertyResponse500
    | HotelPropertyResponse503
    | None
):
    r"""Get hotel property details

     Retrieves full details for a single hotel or vacation rental, including amenities, images, and
    booking offers.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per property lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (HotelPropertyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HotelPropertyResponse200 | HotelPropertyResponse400 | HotelPropertyResponse401 | HotelPropertyResponse402 | HotelPropertyResponse403 | HotelPropertyResponse404 | HotelPropertyResponse422 | HotelPropertyResponse429 | HotelPropertyResponse500 | HotelPropertyResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: HotelPropertyBody,
) -> Response[
    HotelPropertyResponse200
    | HotelPropertyResponse400
    | HotelPropertyResponse401
    | HotelPropertyResponse402
    | HotelPropertyResponse403
    | HotelPropertyResponse404
    | HotelPropertyResponse422
    | HotelPropertyResponse429
    | HotelPropertyResponse500
    | HotelPropertyResponse503
]:
    r"""Get hotel property details

     Retrieves full details for a single hotel or vacation rental, including amenities, images, and
    booking offers.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per property lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (HotelPropertyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HotelPropertyResponse200 | HotelPropertyResponse400 | HotelPropertyResponse401 | HotelPropertyResponse402 | HotelPropertyResponse403 | HotelPropertyResponse404 | HotelPropertyResponse422 | HotelPropertyResponse429 | HotelPropertyResponse500 | HotelPropertyResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: HotelPropertyBody,
) -> (
    HotelPropertyResponse200
    | HotelPropertyResponse400
    | HotelPropertyResponse401
    | HotelPropertyResponse402
    | HotelPropertyResponse403
    | HotelPropertyResponse404
    | HotelPropertyResponse422
    | HotelPropertyResponse429
    | HotelPropertyResponse500
    | HotelPropertyResponse503
    | None
):
    r"""Get hotel property details

     Retrieves full details for a single hotel or vacation rental, including amenities, images, and
    booking offers.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per property lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (HotelPropertyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HotelPropertyResponse200 | HotelPropertyResponse400 | HotelPropertyResponse401 | HotelPropertyResponse402 | HotelPropertyResponse403 | HotelPropertyResponse404 | HotelPropertyResponse422 | HotelPropertyResponse429 | HotelPropertyResponse500 | HotelPropertyResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
