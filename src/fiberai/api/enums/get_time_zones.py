from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_time_zones_response_200 import GetTimeZonesResponse200
from ...models.get_time_zones_response_400 import GetTimeZonesResponse400
from ...models.get_time_zones_response_401 import GetTimeZonesResponse401
from ...models.get_time_zones_response_402 import GetTimeZonesResponse402
from ...models.get_time_zones_response_403 import GetTimeZonesResponse403
from ...models.get_time_zones_response_404 import GetTimeZonesResponse404
from ...models.get_time_zones_response_429 import GetTimeZonesResponse429
from ...models.get_time_zones_response_500 import GetTimeZonesResponse500
from ...models.get_time_zones_response_503 import GetTimeZonesResponse503
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
        "url": "/v1/enums/time-zones",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetTimeZonesResponse200
    | GetTimeZonesResponse400
    | GetTimeZonesResponse401
    | GetTimeZonesResponse402
    | GetTimeZonesResponse403
    | GetTimeZonesResponse404
    | GetTimeZonesResponse429
    | GetTimeZonesResponse500
    | GetTimeZonesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetTimeZonesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetTimeZonesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetTimeZonesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetTimeZonesResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetTimeZonesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetTimeZonesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetTimeZonesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetTimeZonesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetTimeZonesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetTimeZonesResponse200
    | GetTimeZonesResponse400
    | GetTimeZonesResponse401
    | GetTimeZonesResponse402
    | GetTimeZonesResponse403
    | GetTimeZonesResponse404
    | GetTimeZonesResponse429
    | GetTimeZonesResponse500
    | GetTimeZonesResponse503
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
    GetTimeZonesResponse200
    | GetTimeZonesResponse400
    | GetTimeZonesResponse401
    | GetTimeZonesResponse402
    | GetTimeZonesResponse403
    | GetTimeZonesResponse404
    | GetTimeZonesResponse429
    | GetTimeZonesResponse500
    | GetTimeZonesResponse503
]:
    r"""List time zones

     Get a comprehensive list of all available timezones with geographic information, current time data,
    and UTC offset ranges. This is useful for passing time zones into our search filters.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTimeZonesResponse200 | GetTimeZonesResponse400 | GetTimeZonesResponse401 | GetTimeZonesResponse402 | GetTimeZonesResponse403 | GetTimeZonesResponse404 | GetTimeZonesResponse429 | GetTimeZonesResponse500 | GetTimeZonesResponse503]
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
    GetTimeZonesResponse200
    | GetTimeZonesResponse400
    | GetTimeZonesResponse401
    | GetTimeZonesResponse402
    | GetTimeZonesResponse403
    | GetTimeZonesResponse404
    | GetTimeZonesResponse429
    | GetTimeZonesResponse500
    | GetTimeZonesResponse503
    | None
):
    r"""List time zones

     Get a comprehensive list of all available timezones with geographic information, current time data,
    and UTC offset ranges. This is useful for passing time zones into our search filters.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTimeZonesResponse200 | GetTimeZonesResponse400 | GetTimeZonesResponse401 | GetTimeZonesResponse402 | GetTimeZonesResponse403 | GetTimeZonesResponse404 | GetTimeZonesResponse429 | GetTimeZonesResponse500 | GetTimeZonesResponse503
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
    GetTimeZonesResponse200
    | GetTimeZonesResponse400
    | GetTimeZonesResponse401
    | GetTimeZonesResponse402
    | GetTimeZonesResponse403
    | GetTimeZonesResponse404
    | GetTimeZonesResponse429
    | GetTimeZonesResponse500
    | GetTimeZonesResponse503
]:
    r"""List time zones

     Get a comprehensive list of all available timezones with geographic information, current time data,
    and UTC offset ranges. This is useful for passing time zones into our search filters.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTimeZonesResponse200 | GetTimeZonesResponse400 | GetTimeZonesResponse401 | GetTimeZonesResponse402 | GetTimeZonesResponse403 | GetTimeZonesResponse404 | GetTimeZonesResponse429 | GetTimeZonesResponse500 | GetTimeZonesResponse503]
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
    GetTimeZonesResponse200
    | GetTimeZonesResponse400
    | GetTimeZonesResponse401
    | GetTimeZonesResponse402
    | GetTimeZonesResponse403
    | GetTimeZonesResponse404
    | GetTimeZonesResponse429
    | GetTimeZonesResponse500
    | GetTimeZonesResponse503
    | None
):
    r"""List time zones

     Get a comprehensive list of all available timezones with geographic information, current time data,
    and UTC offset ranges. This is useful for passing time zones into our search filters.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTimeZonesResponse200 | GetTimeZonesResponse400 | GetTimeZonesResponse401 | GetTimeZonesResponse402 | GetTimeZonesResponse403 | GetTimeZonesResponse404 | GetTimeZonesResponse429 | GetTimeZonesResponse500 | GetTimeZonesResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
        )
    ).parsed
