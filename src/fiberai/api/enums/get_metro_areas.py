from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_metro_areas_response_200 import GetMetroAreasResponse200
from ...models.get_metro_areas_response_400 import GetMetroAreasResponse400
from ...models.get_metro_areas_response_401 import GetMetroAreasResponse401
from ...models.get_metro_areas_response_402 import GetMetroAreasResponse402
from ...models.get_metro_areas_response_403 import GetMetroAreasResponse403
from ...models.get_metro_areas_response_404 import GetMetroAreasResponse404
from ...models.get_metro_areas_response_422 import GetMetroAreasResponse422
from ...models.get_metro_areas_response_429 import GetMetroAreasResponse429
from ...models.get_metro_areas_response_500 import GetMetroAreasResponse500
from ...models.get_metro_areas_response_503 import GetMetroAreasResponse503
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
        "url": "/v1/enums/metro-areas",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetMetroAreasResponse200
    | GetMetroAreasResponse400
    | GetMetroAreasResponse401
    | GetMetroAreasResponse402
    | GetMetroAreasResponse403
    | GetMetroAreasResponse404
    | GetMetroAreasResponse422
    | GetMetroAreasResponse429
    | GetMetroAreasResponse500
    | GetMetroAreasResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetMetroAreasResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetMetroAreasResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetMetroAreasResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetMetroAreasResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetMetroAreasResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetMetroAreasResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetMetroAreasResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetMetroAreasResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetMetroAreasResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetMetroAreasResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetMetroAreasResponse200
    | GetMetroAreasResponse400
    | GetMetroAreasResponse401
    | GetMetroAreasResponse402
    | GetMetroAreasResponse403
    | GetMetroAreasResponse404
    | GetMetroAreasResponse422
    | GetMetroAreasResponse429
    | GetMetroAreasResponse500
    | GetMetroAreasResponse503
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
    GetMetroAreasResponse200
    | GetMetroAreasResponse400
    | GetMetroAreasResponse401
    | GetMetroAreasResponse402
    | GetMetroAreasResponse403
    | GetMetroAreasResponse404
    | GetMetroAreasResponse422
    | GetMetroAreasResponse429
    | GetMetroAreasResponse500
    | GetMetroAreasResponse503
]:
    """List preset metro areas

     List all preset metro area regions available for geographic filtering. Each region includes a slug
    (usable with the `preset-region` strategy in location-based search endpoints), geometry (center +
    radius for circles, vertices for polygons), major cities, and synonyms for fuzzy matching.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMetroAreasResponse200 | GetMetroAreasResponse400 | GetMetroAreasResponse401 | GetMetroAreasResponse402 | GetMetroAreasResponse403 | GetMetroAreasResponse404 | GetMetroAreasResponse422 | GetMetroAreasResponse429 | GetMetroAreasResponse500 | GetMetroAreasResponse503]
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
    GetMetroAreasResponse200
    | GetMetroAreasResponse400
    | GetMetroAreasResponse401
    | GetMetroAreasResponse402
    | GetMetroAreasResponse403
    | GetMetroAreasResponse404
    | GetMetroAreasResponse422
    | GetMetroAreasResponse429
    | GetMetroAreasResponse500
    | GetMetroAreasResponse503
    | None
):
    """List preset metro areas

     List all preset metro area regions available for geographic filtering. Each region includes a slug
    (usable with the `preset-region` strategy in location-based search endpoints), geometry (center +
    radius for circles, vertices for polygons), major cities, and synonyms for fuzzy matching.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMetroAreasResponse200 | GetMetroAreasResponse400 | GetMetroAreasResponse401 | GetMetroAreasResponse402 | GetMetroAreasResponse403 | GetMetroAreasResponse404 | GetMetroAreasResponse422 | GetMetroAreasResponse429 | GetMetroAreasResponse500 | GetMetroAreasResponse503
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
    GetMetroAreasResponse200
    | GetMetroAreasResponse400
    | GetMetroAreasResponse401
    | GetMetroAreasResponse402
    | GetMetroAreasResponse403
    | GetMetroAreasResponse404
    | GetMetroAreasResponse422
    | GetMetroAreasResponse429
    | GetMetroAreasResponse500
    | GetMetroAreasResponse503
]:
    """List preset metro areas

     List all preset metro area regions available for geographic filtering. Each region includes a slug
    (usable with the `preset-region` strategy in location-based search endpoints), geometry (center +
    radius for circles, vertices for polygons), major cities, and synonyms for fuzzy matching.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMetroAreasResponse200 | GetMetroAreasResponse400 | GetMetroAreasResponse401 | GetMetroAreasResponse402 | GetMetroAreasResponse403 | GetMetroAreasResponse404 | GetMetroAreasResponse422 | GetMetroAreasResponse429 | GetMetroAreasResponse500 | GetMetroAreasResponse503]
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
    GetMetroAreasResponse200
    | GetMetroAreasResponse400
    | GetMetroAreasResponse401
    | GetMetroAreasResponse402
    | GetMetroAreasResponse403
    | GetMetroAreasResponse404
    | GetMetroAreasResponse422
    | GetMetroAreasResponse429
    | GetMetroAreasResponse500
    | GetMetroAreasResponse503
    | None
):
    """List preset metro areas

     List all preset metro area regions available for geographic filtering. Each region includes a slug
    (usable with the `preset-region` strategy in location-based search endpoints), geometry (center +
    radius for circles, vertices for polygons), major cities, and synonyms for fuzzy matching.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMetroAreasResponse200 | GetMetroAreasResponse400 | GetMetroAreasResponse401 | GetMetroAreasResponse402 | GetMetroAreasResponse403 | GetMetroAreasResponse404 | GetMetroAreasResponse422 | GetMetroAreasResponse429 | GetMetroAreasResponse500 | GetMetroAreasResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
        )
    ).parsed
