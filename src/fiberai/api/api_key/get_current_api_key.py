from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_current_api_key_body import GetCurrentApiKeyBody
from ...models.get_current_api_key_response_200 import GetCurrentApiKeyResponse200
from ...models.get_current_api_key_response_400 import GetCurrentApiKeyResponse400
from ...models.get_current_api_key_response_401 import GetCurrentApiKeyResponse401
from ...models.get_current_api_key_response_402 import GetCurrentApiKeyResponse402
from ...models.get_current_api_key_response_403 import GetCurrentApiKeyResponse403
from ...models.get_current_api_key_response_404 import GetCurrentApiKeyResponse404
from ...models.get_current_api_key_response_422 import GetCurrentApiKeyResponse422
from ...models.get_current_api_key_response_429 import GetCurrentApiKeyResponse429
from ...models.get_current_api_key_response_500 import GetCurrentApiKeyResponse500
from ...models.get_current_api_key_response_503 import GetCurrentApiKeyResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GetCurrentApiKeyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/api-keys/current",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetCurrentApiKeyResponse200
    | GetCurrentApiKeyResponse400
    | GetCurrentApiKeyResponse401
    | GetCurrentApiKeyResponse402
    | GetCurrentApiKeyResponse403
    | GetCurrentApiKeyResponse404
    | GetCurrentApiKeyResponse422
    | GetCurrentApiKeyResponse429
    | GetCurrentApiKeyResponse500
    | GetCurrentApiKeyResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetCurrentApiKeyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetCurrentApiKeyResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetCurrentApiKeyResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetCurrentApiKeyResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetCurrentApiKeyResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCurrentApiKeyResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetCurrentApiKeyResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetCurrentApiKeyResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetCurrentApiKeyResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetCurrentApiKeyResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetCurrentApiKeyResponse200
    | GetCurrentApiKeyResponse400
    | GetCurrentApiKeyResponse401
    | GetCurrentApiKeyResponse402
    | GetCurrentApiKeyResponse403
    | GetCurrentApiKeyResponse404
    | GetCurrentApiKeyResponse422
    | GetCurrentApiKeyResponse429
    | GetCurrentApiKeyResponse500
    | GetCurrentApiKeyResponse503
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
    body: GetCurrentApiKeyBody,
) -> Response[
    GetCurrentApiKeyResponse200
    | GetCurrentApiKeyResponse400
    | GetCurrentApiKeyResponse401
    | GetCurrentApiKeyResponse402
    | GetCurrentApiKeyResponse403
    | GetCurrentApiKeyResponse404
    | GetCurrentApiKeyResponse422
    | GetCurrentApiKeyResponse429
    | GetCurrentApiKeyResponse500
    | GetCurrentApiKeyResponse503
]:
    """Get API key

     Return details about an API key, including its name, prefix, expiration, and per-key credit usage.
    Acts on the key that authenticates this request unless target is OTHER.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (GetCurrentApiKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCurrentApiKeyResponse200 | GetCurrentApiKeyResponse400 | GetCurrentApiKeyResponse401 | GetCurrentApiKeyResponse402 | GetCurrentApiKeyResponse403 | GetCurrentApiKeyResponse404 | GetCurrentApiKeyResponse422 | GetCurrentApiKeyResponse429 | GetCurrentApiKeyResponse500 | GetCurrentApiKeyResponse503]
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
    body: GetCurrentApiKeyBody,
) -> (
    GetCurrentApiKeyResponse200
    | GetCurrentApiKeyResponse400
    | GetCurrentApiKeyResponse401
    | GetCurrentApiKeyResponse402
    | GetCurrentApiKeyResponse403
    | GetCurrentApiKeyResponse404
    | GetCurrentApiKeyResponse422
    | GetCurrentApiKeyResponse429
    | GetCurrentApiKeyResponse500
    | GetCurrentApiKeyResponse503
    | None
):
    """Get API key

     Return details about an API key, including its name, prefix, expiration, and per-key credit usage.
    Acts on the key that authenticates this request unless target is OTHER.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (GetCurrentApiKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCurrentApiKeyResponse200 | GetCurrentApiKeyResponse400 | GetCurrentApiKeyResponse401 | GetCurrentApiKeyResponse402 | GetCurrentApiKeyResponse403 | GetCurrentApiKeyResponse404 | GetCurrentApiKeyResponse422 | GetCurrentApiKeyResponse429 | GetCurrentApiKeyResponse500 | GetCurrentApiKeyResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetCurrentApiKeyBody,
) -> Response[
    GetCurrentApiKeyResponse200
    | GetCurrentApiKeyResponse400
    | GetCurrentApiKeyResponse401
    | GetCurrentApiKeyResponse402
    | GetCurrentApiKeyResponse403
    | GetCurrentApiKeyResponse404
    | GetCurrentApiKeyResponse422
    | GetCurrentApiKeyResponse429
    | GetCurrentApiKeyResponse500
    | GetCurrentApiKeyResponse503
]:
    """Get API key

     Return details about an API key, including its name, prefix, expiration, and per-key credit usage.
    Acts on the key that authenticates this request unless target is OTHER.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (GetCurrentApiKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCurrentApiKeyResponse200 | GetCurrentApiKeyResponse400 | GetCurrentApiKeyResponse401 | GetCurrentApiKeyResponse402 | GetCurrentApiKeyResponse403 | GetCurrentApiKeyResponse404 | GetCurrentApiKeyResponse422 | GetCurrentApiKeyResponse429 | GetCurrentApiKeyResponse500 | GetCurrentApiKeyResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetCurrentApiKeyBody,
) -> (
    GetCurrentApiKeyResponse200
    | GetCurrentApiKeyResponse400
    | GetCurrentApiKeyResponse401
    | GetCurrentApiKeyResponse402
    | GetCurrentApiKeyResponse403
    | GetCurrentApiKeyResponse404
    | GetCurrentApiKeyResponse422
    | GetCurrentApiKeyResponse429
    | GetCurrentApiKeyResponse500
    | GetCurrentApiKeyResponse503
    | None
):
    """Get API key

     Return details about an API key, including its name, prefix, expiration, and per-key credit usage.
    Acts on the key that authenticates this request unless target is OTHER.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (GetCurrentApiKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCurrentApiKeyResponse200 | GetCurrentApiKeyResponse400 | GetCurrentApiKeyResponse401 | GetCurrentApiKeyResponse402 | GetCurrentApiKeyResponse403 | GetCurrentApiKeyResponse404 | GetCurrentApiKeyResponse422 | GetCurrentApiKeyResponse429 | GetCurrentApiKeyResponse500 | GetCurrentApiKeyResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
