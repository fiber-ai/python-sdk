from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_technologies_response_200 import GetTechnologiesResponse200
from ...models.get_technologies_response_400 import GetTechnologiesResponse400
from ...models.get_technologies_response_401 import GetTechnologiesResponse401
from ...models.get_technologies_response_402 import GetTechnologiesResponse402
from ...models.get_technologies_response_403 import GetTechnologiesResponse403
from ...models.get_technologies_response_404 import GetTechnologiesResponse404
from ...models.get_technologies_response_422 import GetTechnologiesResponse422
from ...models.get_technologies_response_429 import GetTechnologiesResponse429
from ...models.get_technologies_response_500 import GetTechnologiesResponse500
from ...models.get_technologies_response_503 import GetTechnologiesResponse503
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
        "url": "/v1/enums/technologies",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetTechnologiesResponse200
    | GetTechnologiesResponse400
    | GetTechnologiesResponse401
    | GetTechnologiesResponse402
    | GetTechnologiesResponse403
    | GetTechnologiesResponse404
    | GetTechnologiesResponse422
    | GetTechnologiesResponse429
    | GetTechnologiesResponse500
    | GetTechnologiesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetTechnologiesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetTechnologiesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetTechnologiesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetTechnologiesResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetTechnologiesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetTechnologiesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetTechnologiesResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetTechnologiesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetTechnologiesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetTechnologiesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetTechnologiesResponse200
    | GetTechnologiesResponse400
    | GetTechnologiesResponse401
    | GetTechnologiesResponse402
    | GetTechnologiesResponse403
    | GetTechnologiesResponse404
    | GetTechnologiesResponse422
    | GetTechnologiesResponse429
    | GetTechnologiesResponse500
    | GetTechnologiesResponse503
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
    GetTechnologiesResponse200
    | GetTechnologiesResponse400
    | GetTechnologiesResponse401
    | GetTechnologiesResponse402
    | GetTechnologiesResponse403
    | GetTechnologiesResponse404
    | GetTechnologiesResponse422
    | GetTechnologiesResponse429
    | GetTechnologiesResponse500
    | GetTechnologiesResponse503
]:
    """List technologies

     Get all searchable technologies and platforms with their synonyms. Useful for the technology search
    API.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTechnologiesResponse200 | GetTechnologiesResponse400 | GetTechnologiesResponse401 | GetTechnologiesResponse402 | GetTechnologiesResponse403 | GetTechnologiesResponse404 | GetTechnologiesResponse422 | GetTechnologiesResponse429 | GetTechnologiesResponse500 | GetTechnologiesResponse503]
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
    GetTechnologiesResponse200
    | GetTechnologiesResponse400
    | GetTechnologiesResponse401
    | GetTechnologiesResponse402
    | GetTechnologiesResponse403
    | GetTechnologiesResponse404
    | GetTechnologiesResponse422
    | GetTechnologiesResponse429
    | GetTechnologiesResponse500
    | GetTechnologiesResponse503
    | None
):
    """List technologies

     Get all searchable technologies and platforms with their synonyms. Useful for the technology search
    API.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTechnologiesResponse200 | GetTechnologiesResponse400 | GetTechnologiesResponse401 | GetTechnologiesResponse402 | GetTechnologiesResponse403 | GetTechnologiesResponse404 | GetTechnologiesResponse422 | GetTechnologiesResponse429 | GetTechnologiesResponse500 | GetTechnologiesResponse503
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
    GetTechnologiesResponse200
    | GetTechnologiesResponse400
    | GetTechnologiesResponse401
    | GetTechnologiesResponse402
    | GetTechnologiesResponse403
    | GetTechnologiesResponse404
    | GetTechnologiesResponse422
    | GetTechnologiesResponse429
    | GetTechnologiesResponse500
    | GetTechnologiesResponse503
]:
    """List technologies

     Get all searchable technologies and platforms with their synonyms. Useful for the technology search
    API.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTechnologiesResponse200 | GetTechnologiesResponse400 | GetTechnologiesResponse401 | GetTechnologiesResponse402 | GetTechnologiesResponse403 | GetTechnologiesResponse404 | GetTechnologiesResponse422 | GetTechnologiesResponse429 | GetTechnologiesResponse500 | GetTechnologiesResponse503]
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
    GetTechnologiesResponse200
    | GetTechnologiesResponse400
    | GetTechnologiesResponse401
    | GetTechnologiesResponse402
    | GetTechnologiesResponse403
    | GetTechnologiesResponse404
    | GetTechnologiesResponse422
    | GetTechnologiesResponse429
    | GetTechnologiesResponse500
    | GetTechnologiesResponse503
    | None
):
    """List technologies

     Get all searchable technologies and platforms with their synonyms. Useful for the technology search
    API.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTechnologiesResponse200 | GetTechnologiesResponse400 | GetTechnologiesResponse401 | GetTechnologiesResponse402 | GetTechnologiesResponse403 | GetTechnologiesResponse404 | GetTechnologiesResponse422 | GetTechnologiesResponse429 | GetTechnologiesResponse500 | GetTechnologiesResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
        )
    ).parsed
