from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_api_keys_body import GetAllApiKeysBody
from ...models.get_all_api_keys_response_200 import GetAllApiKeysResponse200
from ...models.get_all_api_keys_response_400 import GetAllApiKeysResponse400
from ...models.get_all_api_keys_response_401 import GetAllApiKeysResponse401
from ...models.get_all_api_keys_response_402 import GetAllApiKeysResponse402
from ...models.get_all_api_keys_response_403 import GetAllApiKeysResponse403
from ...models.get_all_api_keys_response_404 import GetAllApiKeysResponse404
from ...models.get_all_api_keys_response_422 import GetAllApiKeysResponse422
from ...models.get_all_api_keys_response_429 import GetAllApiKeysResponse429
from ...models.get_all_api_keys_response_500 import GetAllApiKeysResponse500
from ...models.get_all_api_keys_response_503 import GetAllApiKeysResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GetAllApiKeysBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/api-keys",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAllApiKeysResponse200
    | GetAllApiKeysResponse400
    | GetAllApiKeysResponse401
    | GetAllApiKeysResponse402
    | GetAllApiKeysResponse403
    | GetAllApiKeysResponse404
    | GetAllApiKeysResponse422
    | GetAllApiKeysResponse429
    | GetAllApiKeysResponse500
    | GetAllApiKeysResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetAllApiKeysResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAllApiKeysResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetAllApiKeysResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetAllApiKeysResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetAllApiKeysResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAllApiKeysResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetAllApiKeysResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetAllApiKeysResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetAllApiKeysResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetAllApiKeysResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAllApiKeysResponse200
    | GetAllApiKeysResponse400
    | GetAllApiKeysResponse401
    | GetAllApiKeysResponse402
    | GetAllApiKeysResponse403
    | GetAllApiKeysResponse404
    | GetAllApiKeysResponse422
    | GetAllApiKeysResponse429
    | GetAllApiKeysResponse500
    | GetAllApiKeysResponse503
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
    body: GetAllApiKeysBody,
) -> Response[
    GetAllApiKeysResponse200
    | GetAllApiKeysResponse400
    | GetAllApiKeysResponse401
    | GetAllApiKeysResponse402
    | GetAllApiKeysResponse403
    | GetAllApiKeysResponse404
    | GetAllApiKeysResponse422
    | GetAllApiKeysResponse429
    | GetAllApiKeysResponse500
    | GetAllApiKeysResponse503
]:
    r"""List API keys

     List all API keys for your organization, including each key's name, prefix, expiration, and per-key
    credit usage. The secret value of a key is only shown once at creation and is never returned here.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetAllApiKeysBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllApiKeysResponse200 | GetAllApiKeysResponse400 | GetAllApiKeysResponse401 | GetAllApiKeysResponse402 | GetAllApiKeysResponse403 | GetAllApiKeysResponse404 | GetAllApiKeysResponse422 | GetAllApiKeysResponse429 | GetAllApiKeysResponse500 | GetAllApiKeysResponse503]
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
    body: GetAllApiKeysBody,
) -> (
    GetAllApiKeysResponse200
    | GetAllApiKeysResponse400
    | GetAllApiKeysResponse401
    | GetAllApiKeysResponse402
    | GetAllApiKeysResponse403
    | GetAllApiKeysResponse404
    | GetAllApiKeysResponse422
    | GetAllApiKeysResponse429
    | GetAllApiKeysResponse500
    | GetAllApiKeysResponse503
    | None
):
    r"""List API keys

     List all API keys for your organization, including each key's name, prefix, expiration, and per-key
    credit usage. The secret value of a key is only shown once at creation and is never returned here.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetAllApiKeysBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllApiKeysResponse200 | GetAllApiKeysResponse400 | GetAllApiKeysResponse401 | GetAllApiKeysResponse402 | GetAllApiKeysResponse403 | GetAllApiKeysResponse404 | GetAllApiKeysResponse422 | GetAllApiKeysResponse429 | GetAllApiKeysResponse500 | GetAllApiKeysResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetAllApiKeysBody,
) -> Response[
    GetAllApiKeysResponse200
    | GetAllApiKeysResponse400
    | GetAllApiKeysResponse401
    | GetAllApiKeysResponse402
    | GetAllApiKeysResponse403
    | GetAllApiKeysResponse404
    | GetAllApiKeysResponse422
    | GetAllApiKeysResponse429
    | GetAllApiKeysResponse500
    | GetAllApiKeysResponse503
]:
    r"""List API keys

     List all API keys for your organization, including each key's name, prefix, expiration, and per-key
    credit usage. The secret value of a key is only shown once at creation and is never returned here.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetAllApiKeysBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllApiKeysResponse200 | GetAllApiKeysResponse400 | GetAllApiKeysResponse401 | GetAllApiKeysResponse402 | GetAllApiKeysResponse403 | GetAllApiKeysResponse404 | GetAllApiKeysResponse422 | GetAllApiKeysResponse429 | GetAllApiKeysResponse500 | GetAllApiKeysResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetAllApiKeysBody,
) -> (
    GetAllApiKeysResponse200
    | GetAllApiKeysResponse400
    | GetAllApiKeysResponse401
    | GetAllApiKeysResponse402
    | GetAllApiKeysResponse403
    | GetAllApiKeysResponse404
    | GetAllApiKeysResponse422
    | GetAllApiKeysResponse429
    | GetAllApiKeysResponse500
    | GetAllApiKeysResponse503
    | None
):
    r"""List API keys

     List all API keys for your organization, including each key's name, prefix, expiration, and per-key
    credit usage. The secret value of a key is only shown once at creation and is never returned here.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetAllApiKeysBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllApiKeysResponse200 | GetAllApiKeysResponse400 | GetAllApiKeysResponse401 | GetAllApiKeysResponse402 | GetAllApiKeysResponse403 | GetAllApiKeysResponse404 | GetAllApiKeysResponse422 | GetAllApiKeysResponse429 | GetAllApiKeysResponse500 | GetAllApiKeysResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
