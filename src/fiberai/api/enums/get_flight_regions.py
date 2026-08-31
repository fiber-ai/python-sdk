from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_flight_regions_response_200 import GetFlightRegionsResponse200
from ...models.get_flight_regions_response_400 import GetFlightRegionsResponse400
from ...models.get_flight_regions_response_401 import GetFlightRegionsResponse401
from ...models.get_flight_regions_response_402 import GetFlightRegionsResponse402
from ...models.get_flight_regions_response_403 import GetFlightRegionsResponse403
from ...models.get_flight_regions_response_404 import GetFlightRegionsResponse404
from ...models.get_flight_regions_response_422 import GetFlightRegionsResponse422
from ...models.get_flight_regions_response_429 import GetFlightRegionsResponse429
from ...models.get_flight_regions_response_500 import GetFlightRegionsResponse500
from ...models.get_flight_regions_response_503 import GetFlightRegionsResponse503
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
        "url": "/v1/enums/flight-regions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetFlightRegionsResponse200
    | GetFlightRegionsResponse400
    | GetFlightRegionsResponse401
    | GetFlightRegionsResponse402
    | GetFlightRegionsResponse403
    | GetFlightRegionsResponse404
    | GetFlightRegionsResponse422
    | GetFlightRegionsResponse429
    | GetFlightRegionsResponse500
    | GetFlightRegionsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetFlightRegionsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetFlightRegionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetFlightRegionsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetFlightRegionsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetFlightRegionsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetFlightRegionsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetFlightRegionsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetFlightRegionsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetFlightRegionsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetFlightRegionsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetFlightRegionsResponse200
    | GetFlightRegionsResponse400
    | GetFlightRegionsResponse401
    | GetFlightRegionsResponse402
    | GetFlightRegionsResponse403
    | GetFlightRegionsResponse404
    | GetFlightRegionsResponse422
    | GetFlightRegionsResponse429
    | GetFlightRegionsResponse500
    | GetFlightRegionsResponse503
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
    GetFlightRegionsResponse200
    | GetFlightRegionsResponse400
    | GetFlightRegionsResponse401
    | GetFlightRegionsResponse402
    | GetFlightRegionsResponse403
    | GetFlightRegionsResponse404
    | GetFlightRegionsResponse422
    | GetFlightRegionsResponse429
    | GetFlightRegionsResponse500
    | GetFlightRegionsResponse503
]:
    """List flight region aliases

     List every supported `X-` flight region alias along with its metro name and the IATA airport codes
    it covers. Pass `apiCode` as `departureAirports` / `arrivalAirports` in `POST /v1/flights/search` to
    search across an entire metro area in one call.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFlightRegionsResponse200 | GetFlightRegionsResponse400 | GetFlightRegionsResponse401 | GetFlightRegionsResponse402 | GetFlightRegionsResponse403 | GetFlightRegionsResponse404 | GetFlightRegionsResponse422 | GetFlightRegionsResponse429 | GetFlightRegionsResponse500 | GetFlightRegionsResponse503]
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
    GetFlightRegionsResponse200
    | GetFlightRegionsResponse400
    | GetFlightRegionsResponse401
    | GetFlightRegionsResponse402
    | GetFlightRegionsResponse403
    | GetFlightRegionsResponse404
    | GetFlightRegionsResponse422
    | GetFlightRegionsResponse429
    | GetFlightRegionsResponse500
    | GetFlightRegionsResponse503
    | None
):
    """List flight region aliases

     List every supported `X-` flight region alias along with its metro name and the IATA airport codes
    it covers. Pass `apiCode` as `departureAirports` / `arrivalAirports` in `POST /v1/flights/search` to
    search across an entire metro area in one call.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFlightRegionsResponse200 | GetFlightRegionsResponse400 | GetFlightRegionsResponse401 | GetFlightRegionsResponse402 | GetFlightRegionsResponse403 | GetFlightRegionsResponse404 | GetFlightRegionsResponse422 | GetFlightRegionsResponse429 | GetFlightRegionsResponse500 | GetFlightRegionsResponse503
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
    GetFlightRegionsResponse200
    | GetFlightRegionsResponse400
    | GetFlightRegionsResponse401
    | GetFlightRegionsResponse402
    | GetFlightRegionsResponse403
    | GetFlightRegionsResponse404
    | GetFlightRegionsResponse422
    | GetFlightRegionsResponse429
    | GetFlightRegionsResponse500
    | GetFlightRegionsResponse503
]:
    """List flight region aliases

     List every supported `X-` flight region alias along with its metro name and the IATA airport codes
    it covers. Pass `apiCode` as `departureAirports` / `arrivalAirports` in `POST /v1/flights/search` to
    search across an entire metro area in one call.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFlightRegionsResponse200 | GetFlightRegionsResponse400 | GetFlightRegionsResponse401 | GetFlightRegionsResponse402 | GetFlightRegionsResponse403 | GetFlightRegionsResponse404 | GetFlightRegionsResponse422 | GetFlightRegionsResponse429 | GetFlightRegionsResponse500 | GetFlightRegionsResponse503]
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
    GetFlightRegionsResponse200
    | GetFlightRegionsResponse400
    | GetFlightRegionsResponse401
    | GetFlightRegionsResponse402
    | GetFlightRegionsResponse403
    | GetFlightRegionsResponse404
    | GetFlightRegionsResponse422
    | GetFlightRegionsResponse429
    | GetFlightRegionsResponse500
    | GetFlightRegionsResponse503
    | None
):
    """List flight region aliases

     List every supported `X-` flight region alias along with its metro name and the IATA airport codes
    it covers. Pass `apiCode` as `departureAirports` / `arrivalAirports` in `POST /v1/flights/search` to
    search across an entire metro area in one call.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFlightRegionsResponse200 | GetFlightRegionsResponse400 | GetFlightRegionsResponse401 | GetFlightRegionsResponse402 | GetFlightRegionsResponse403 | GetFlightRegionsResponse404 | GetFlightRegionsResponse422 | GetFlightRegionsResponse429 | GetFlightRegionsResponse500 | GetFlightRegionsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
        )
    ).parsed
