from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_subdivisions_response_200 import GetSubdivisionsResponse200
from ...models.get_subdivisions_response_400 import GetSubdivisionsResponse400
from ...models.get_subdivisions_response_401 import GetSubdivisionsResponse401
from ...models.get_subdivisions_response_402 import GetSubdivisionsResponse402
from ...models.get_subdivisions_response_403 import GetSubdivisionsResponse403
from ...models.get_subdivisions_response_404 import GetSubdivisionsResponse404
from ...models.get_subdivisions_response_429 import GetSubdivisionsResponse429
from ...models.get_subdivisions_response_500 import GetSubdivisionsResponse500
from ...models.get_subdivisions_response_503 import GetSubdivisionsResponse503
from ...types import UNSET, Response


def _get_kwargs(
    *,
    api_key: str,
    country_code: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["apiKey"] = api_key

    params["countryCode"] = country_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/enums/subdivisions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSubdivisionsResponse200
    | GetSubdivisionsResponse400
    | GetSubdivisionsResponse401
    | GetSubdivisionsResponse402
    | GetSubdivisionsResponse403
    | GetSubdivisionsResponse404
    | GetSubdivisionsResponse429
    | GetSubdivisionsResponse500
    | GetSubdivisionsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetSubdivisionsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetSubdivisionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetSubdivisionsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetSubdivisionsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetSubdivisionsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSubdivisionsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetSubdivisionsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetSubdivisionsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetSubdivisionsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSubdivisionsResponse200
    | GetSubdivisionsResponse400
    | GetSubdivisionsResponse401
    | GetSubdivisionsResponse402
    | GetSubdivisionsResponse403
    | GetSubdivisionsResponse404
    | GetSubdivisionsResponse429
    | GetSubdivisionsResponse500
    | GetSubdivisionsResponse503
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
    country_code: str,
) -> Response[
    GetSubdivisionsResponse200
    | GetSubdivisionsResponse400
    | GetSubdivisionsResponse401
    | GetSubdivisionsResponse402
    | GetSubdivisionsResponse403
    | GetSubdivisionsResponse404
    | GetSubdivisionsResponse429
    | GetSubdivisionsResponse500
    | GetSubdivisionsResponse503
]:
    r"""List subdivisions by country

     Get a list of subdivisions (states, provinces, Länder, etc.) for a given country, identified by ISO
    3166-1 alpha-2 or alpha-3 code.

    <span>⚡ <strong>Rate limit:</strong> 250 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):
        country_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSubdivisionsResponse200 | GetSubdivisionsResponse400 | GetSubdivisionsResponse401 | GetSubdivisionsResponse402 | GetSubdivisionsResponse403 | GetSubdivisionsResponse404 | GetSubdivisionsResponse429 | GetSubdivisionsResponse500 | GetSubdivisionsResponse503]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
        country_code=country_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    country_code: str,
) -> (
    GetSubdivisionsResponse200
    | GetSubdivisionsResponse400
    | GetSubdivisionsResponse401
    | GetSubdivisionsResponse402
    | GetSubdivisionsResponse403
    | GetSubdivisionsResponse404
    | GetSubdivisionsResponse429
    | GetSubdivisionsResponse500
    | GetSubdivisionsResponse503
    | None
):
    r"""List subdivisions by country

     Get a list of subdivisions (states, provinces, Länder, etc.) for a given country, identified by ISO
    3166-1 alpha-2 or alpha-3 code.

    <span>⚡ <strong>Rate limit:</strong> 250 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):
        country_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSubdivisionsResponse200 | GetSubdivisionsResponse400 | GetSubdivisionsResponse401 | GetSubdivisionsResponse402 | GetSubdivisionsResponse403 | GetSubdivisionsResponse404 | GetSubdivisionsResponse429 | GetSubdivisionsResponse500 | GetSubdivisionsResponse503
    """

    return sync_detailed(
        client=client,
        api_key=api_key,
        country_code=country_code,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    country_code: str,
) -> Response[
    GetSubdivisionsResponse200
    | GetSubdivisionsResponse400
    | GetSubdivisionsResponse401
    | GetSubdivisionsResponse402
    | GetSubdivisionsResponse403
    | GetSubdivisionsResponse404
    | GetSubdivisionsResponse429
    | GetSubdivisionsResponse500
    | GetSubdivisionsResponse503
]:
    r"""List subdivisions by country

     Get a list of subdivisions (states, provinces, Länder, etc.) for a given country, identified by ISO
    3166-1 alpha-2 or alpha-3 code.

    <span>⚡ <strong>Rate limit:</strong> 250 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):
        country_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSubdivisionsResponse200 | GetSubdivisionsResponse400 | GetSubdivisionsResponse401 | GetSubdivisionsResponse402 | GetSubdivisionsResponse403 | GetSubdivisionsResponse404 | GetSubdivisionsResponse429 | GetSubdivisionsResponse500 | GetSubdivisionsResponse503]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
        country_code=country_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    country_code: str,
) -> (
    GetSubdivisionsResponse200
    | GetSubdivisionsResponse400
    | GetSubdivisionsResponse401
    | GetSubdivisionsResponse402
    | GetSubdivisionsResponse403
    | GetSubdivisionsResponse404
    | GetSubdivisionsResponse429
    | GetSubdivisionsResponse500
    | GetSubdivisionsResponse503
    | None
):
    r"""List subdivisions by country

     Get a list of subdivisions (states, provinces, Länder, etc.) for a given country, identified by ISO
    3166-1 alpha-2 or alpha-3 code.

    <span>⚡ <strong>Rate limit:</strong> 250 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):
        country_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSubdivisionsResponse200 | GetSubdivisionsResponse400 | GetSubdivisionsResponse401 | GetSubdivisionsResponse402 | GetSubdivisionsResponse403 | GetSubdivisionsResponse404 | GetSubdivisionsResponse429 | GetSubdivisionsResponse500 | GetSubdivisionsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
            country_code=country_code,
        )
    ).parsed
