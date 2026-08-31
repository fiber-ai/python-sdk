from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_hotel_property_types_response_200 import GetHotelPropertyTypesResponse200
from ...models.get_hotel_property_types_response_400 import GetHotelPropertyTypesResponse400
from ...models.get_hotel_property_types_response_401 import GetHotelPropertyTypesResponse401
from ...models.get_hotel_property_types_response_402 import GetHotelPropertyTypesResponse402
from ...models.get_hotel_property_types_response_403 import GetHotelPropertyTypesResponse403
from ...models.get_hotel_property_types_response_404 import GetHotelPropertyTypesResponse404
from ...models.get_hotel_property_types_response_422 import GetHotelPropertyTypesResponse422
from ...models.get_hotel_property_types_response_429 import GetHotelPropertyTypesResponse429
from ...models.get_hotel_property_types_response_500 import GetHotelPropertyTypesResponse500
from ...models.get_hotel_property_types_response_503 import GetHotelPropertyTypesResponse503
from ...types import UNSET, Response


def _get_kwargs(
    *,
    api_key: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["apiKey"] = api_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/enums/hotels/property-types",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetHotelPropertyTypesResponse200
    | GetHotelPropertyTypesResponse400
    | GetHotelPropertyTypesResponse401
    | GetHotelPropertyTypesResponse402
    | GetHotelPropertyTypesResponse403
    | GetHotelPropertyTypesResponse404
    | GetHotelPropertyTypesResponse422
    | GetHotelPropertyTypesResponse429
    | GetHotelPropertyTypesResponse500
    | GetHotelPropertyTypesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetHotelPropertyTypesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetHotelPropertyTypesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetHotelPropertyTypesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetHotelPropertyTypesResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetHotelPropertyTypesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetHotelPropertyTypesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetHotelPropertyTypesResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetHotelPropertyTypesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetHotelPropertyTypesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetHotelPropertyTypesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetHotelPropertyTypesResponse200
    | GetHotelPropertyTypesResponse400
    | GetHotelPropertyTypesResponse401
    | GetHotelPropertyTypesResponse402
    | GetHotelPropertyTypesResponse403
    | GetHotelPropertyTypesResponse404
    | GetHotelPropertyTypesResponse422
    | GetHotelPropertyTypesResponse429
    | GetHotelPropertyTypesResponse500
    | GetHotelPropertyTypesResponse503
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
    api_key: str,
) -> Response[
    GetHotelPropertyTypesResponse200
    | GetHotelPropertyTypesResponse400
    | GetHotelPropertyTypesResponse401
    | GetHotelPropertyTypesResponse402
    | GetHotelPropertyTypesResponse403
    | GetHotelPropertyTypesResponse404
    | GetHotelPropertyTypesResponse422
    | GetHotelPropertyTypesResponse429
    | GetHotelPropertyTypesResponse500
    | GetHotelPropertyTypesResponse503
]:
    """List hotel property type filters

     List supported hotel property type filter identifiers for use in `propertyTypes` on POST
    /v1/hotels/search.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetHotelPropertyTypesResponse200 | GetHotelPropertyTypesResponse400 | GetHotelPropertyTypesResponse401 | GetHotelPropertyTypesResponse402 | GetHotelPropertyTypesResponse403 | GetHotelPropertyTypesResponse404 | GetHotelPropertyTypesResponse422 | GetHotelPropertyTypesResponse429 | GetHotelPropertyTypesResponse500 | GetHotelPropertyTypesResponse503]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> (
    GetHotelPropertyTypesResponse200
    | GetHotelPropertyTypesResponse400
    | GetHotelPropertyTypesResponse401
    | GetHotelPropertyTypesResponse402
    | GetHotelPropertyTypesResponse403
    | GetHotelPropertyTypesResponse404
    | GetHotelPropertyTypesResponse422
    | GetHotelPropertyTypesResponse429
    | GetHotelPropertyTypesResponse500
    | GetHotelPropertyTypesResponse503
    | None
):
    """List hotel property type filters

     List supported hotel property type filter identifiers for use in `propertyTypes` on POST
    /v1/hotels/search.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetHotelPropertyTypesResponse200 | GetHotelPropertyTypesResponse400 | GetHotelPropertyTypesResponse401 | GetHotelPropertyTypesResponse402 | GetHotelPropertyTypesResponse403 | GetHotelPropertyTypesResponse404 | GetHotelPropertyTypesResponse422 | GetHotelPropertyTypesResponse429 | GetHotelPropertyTypesResponse500 | GetHotelPropertyTypesResponse503
    """

    return sync_detailed(
        client=client,
        api_key=api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> Response[
    GetHotelPropertyTypesResponse200
    | GetHotelPropertyTypesResponse400
    | GetHotelPropertyTypesResponse401
    | GetHotelPropertyTypesResponse402
    | GetHotelPropertyTypesResponse403
    | GetHotelPropertyTypesResponse404
    | GetHotelPropertyTypesResponse422
    | GetHotelPropertyTypesResponse429
    | GetHotelPropertyTypesResponse500
    | GetHotelPropertyTypesResponse503
]:
    """List hotel property type filters

     List supported hotel property type filter identifiers for use in `propertyTypes` on POST
    /v1/hotels/search.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetHotelPropertyTypesResponse200 | GetHotelPropertyTypesResponse400 | GetHotelPropertyTypesResponse401 | GetHotelPropertyTypesResponse402 | GetHotelPropertyTypesResponse403 | GetHotelPropertyTypesResponse404 | GetHotelPropertyTypesResponse422 | GetHotelPropertyTypesResponse429 | GetHotelPropertyTypesResponse500 | GetHotelPropertyTypesResponse503]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> (
    GetHotelPropertyTypesResponse200
    | GetHotelPropertyTypesResponse400
    | GetHotelPropertyTypesResponse401
    | GetHotelPropertyTypesResponse402
    | GetHotelPropertyTypesResponse403
    | GetHotelPropertyTypesResponse404
    | GetHotelPropertyTypesResponse422
    | GetHotelPropertyTypesResponse429
    | GetHotelPropertyTypesResponse500
    | GetHotelPropertyTypesResponse503
    | None
):
    """List hotel property type filters

     List supported hotel property type filter identifiers for use in `propertyTypes` on POST
    /v1/hotels/search.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetHotelPropertyTypesResponse200 | GetHotelPropertyTypesResponse400 | GetHotelPropertyTypesResponse401 | GetHotelPropertyTypesResponse402 | GetHotelPropertyTypesResponse403 | GetHotelPropertyTypesResponse404 | GetHotelPropertyTypesResponse422 | GetHotelPropertyTypesResponse429 | GetHotelPropertyTypesResponse500 | GetHotelPropertyTypesResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
        )
    ).parsed
