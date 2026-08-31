from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_api_key_expiration_body import UpdateApiKeyExpirationBody
from ...models.update_api_key_expiration_response_200 import UpdateApiKeyExpirationResponse200
from ...models.update_api_key_expiration_response_400 import UpdateApiKeyExpirationResponse400
from ...models.update_api_key_expiration_response_401 import UpdateApiKeyExpirationResponse401
from ...models.update_api_key_expiration_response_402 import UpdateApiKeyExpirationResponse402
from ...models.update_api_key_expiration_response_403 import UpdateApiKeyExpirationResponse403
from ...models.update_api_key_expiration_response_404 import UpdateApiKeyExpirationResponse404
from ...models.update_api_key_expiration_response_422 import UpdateApiKeyExpirationResponse422
from ...models.update_api_key_expiration_response_429 import UpdateApiKeyExpirationResponse429
from ...models.update_api_key_expiration_response_500 import UpdateApiKeyExpirationResponse500
from ...models.update_api_key_expiration_response_503 import UpdateApiKeyExpirationResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateApiKeyExpirationBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/api-keys/expiration",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    UpdateApiKeyExpirationResponse200
    | UpdateApiKeyExpirationResponse400
    | UpdateApiKeyExpirationResponse401
    | UpdateApiKeyExpirationResponse402
    | UpdateApiKeyExpirationResponse403
    | UpdateApiKeyExpirationResponse404
    | UpdateApiKeyExpirationResponse422
    | UpdateApiKeyExpirationResponse429
    | UpdateApiKeyExpirationResponse500
    | UpdateApiKeyExpirationResponse503
    | None
):
    if response.status_code == 200:
        response_200 = UpdateApiKeyExpirationResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateApiKeyExpirationResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateApiKeyExpirationResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = UpdateApiKeyExpirationResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = UpdateApiKeyExpirationResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateApiKeyExpirationResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = UpdateApiKeyExpirationResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = UpdateApiKeyExpirationResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = UpdateApiKeyExpirationResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = UpdateApiKeyExpirationResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UpdateApiKeyExpirationResponse200
    | UpdateApiKeyExpirationResponse400
    | UpdateApiKeyExpirationResponse401
    | UpdateApiKeyExpirationResponse402
    | UpdateApiKeyExpirationResponse403
    | UpdateApiKeyExpirationResponse404
    | UpdateApiKeyExpirationResponse422
    | UpdateApiKeyExpirationResponse429
    | UpdateApiKeyExpirationResponse500
    | UpdateApiKeyExpirationResponse503
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
    body: UpdateApiKeyExpirationBody,
) -> Response[
    UpdateApiKeyExpirationResponse200
    | UpdateApiKeyExpirationResponse400
    | UpdateApiKeyExpirationResponse401
    | UpdateApiKeyExpirationResponse402
    | UpdateApiKeyExpirationResponse403
    | UpdateApiKeyExpirationResponse404
    | UpdateApiKeyExpirationResponse422
    | UpdateApiKeyExpirationResponse429
    | UpdateApiKeyExpirationResponse500
    | UpdateApiKeyExpirationResponse503
]:
    """Update API key expiration

     Change the expiration of an API key. Acts on the key that authenticates this request unless target
    is OTHER. Choose set to pin an absolute date, extend or prepone to move the date by a number of
    days, or remove to make the key never expire. Once a key expires it can no longer authenticate.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (UpdateApiKeyExpirationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateApiKeyExpirationResponse200 | UpdateApiKeyExpirationResponse400 | UpdateApiKeyExpirationResponse401 | UpdateApiKeyExpirationResponse402 | UpdateApiKeyExpirationResponse403 | UpdateApiKeyExpirationResponse404 | UpdateApiKeyExpirationResponse422 | UpdateApiKeyExpirationResponse429 | UpdateApiKeyExpirationResponse500 | UpdateApiKeyExpirationResponse503]
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
    body: UpdateApiKeyExpirationBody,
) -> (
    UpdateApiKeyExpirationResponse200
    | UpdateApiKeyExpirationResponse400
    | UpdateApiKeyExpirationResponse401
    | UpdateApiKeyExpirationResponse402
    | UpdateApiKeyExpirationResponse403
    | UpdateApiKeyExpirationResponse404
    | UpdateApiKeyExpirationResponse422
    | UpdateApiKeyExpirationResponse429
    | UpdateApiKeyExpirationResponse500
    | UpdateApiKeyExpirationResponse503
    | None
):
    """Update API key expiration

     Change the expiration of an API key. Acts on the key that authenticates this request unless target
    is OTHER. Choose set to pin an absolute date, extend or prepone to move the date by a number of
    days, or remove to make the key never expire. Once a key expires it can no longer authenticate.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (UpdateApiKeyExpirationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateApiKeyExpirationResponse200 | UpdateApiKeyExpirationResponse400 | UpdateApiKeyExpirationResponse401 | UpdateApiKeyExpirationResponse402 | UpdateApiKeyExpirationResponse403 | UpdateApiKeyExpirationResponse404 | UpdateApiKeyExpirationResponse422 | UpdateApiKeyExpirationResponse429 | UpdateApiKeyExpirationResponse500 | UpdateApiKeyExpirationResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateApiKeyExpirationBody,
) -> Response[
    UpdateApiKeyExpirationResponse200
    | UpdateApiKeyExpirationResponse400
    | UpdateApiKeyExpirationResponse401
    | UpdateApiKeyExpirationResponse402
    | UpdateApiKeyExpirationResponse403
    | UpdateApiKeyExpirationResponse404
    | UpdateApiKeyExpirationResponse422
    | UpdateApiKeyExpirationResponse429
    | UpdateApiKeyExpirationResponse500
    | UpdateApiKeyExpirationResponse503
]:
    """Update API key expiration

     Change the expiration of an API key. Acts on the key that authenticates this request unless target
    is OTHER. Choose set to pin an absolute date, extend or prepone to move the date by a number of
    days, or remove to make the key never expire. Once a key expires it can no longer authenticate.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (UpdateApiKeyExpirationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateApiKeyExpirationResponse200 | UpdateApiKeyExpirationResponse400 | UpdateApiKeyExpirationResponse401 | UpdateApiKeyExpirationResponse402 | UpdateApiKeyExpirationResponse403 | UpdateApiKeyExpirationResponse404 | UpdateApiKeyExpirationResponse422 | UpdateApiKeyExpirationResponse429 | UpdateApiKeyExpirationResponse500 | UpdateApiKeyExpirationResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateApiKeyExpirationBody,
) -> (
    UpdateApiKeyExpirationResponse200
    | UpdateApiKeyExpirationResponse400
    | UpdateApiKeyExpirationResponse401
    | UpdateApiKeyExpirationResponse402
    | UpdateApiKeyExpirationResponse403
    | UpdateApiKeyExpirationResponse404
    | UpdateApiKeyExpirationResponse422
    | UpdateApiKeyExpirationResponse429
    | UpdateApiKeyExpirationResponse500
    | UpdateApiKeyExpirationResponse503
    | None
):
    """Update API key expiration

     Change the expiration of an API key. Acts on the key that authenticates this request unless target
    is OTHER. Choose set to pin an absolute date, extend or prepone to move the date by a number of
    days, or remove to make the key never expire. Once a key expires it can no longer authenticate.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (UpdateApiKeyExpirationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateApiKeyExpirationResponse200 | UpdateApiKeyExpirationResponse400 | UpdateApiKeyExpirationResponse401 | UpdateApiKeyExpirationResponse402 | UpdateApiKeyExpirationResponse403 | UpdateApiKeyExpirationResponse404 | UpdateApiKeyExpirationResponse422 | UpdateApiKeyExpirationResponse429 | UpdateApiKeyExpirationResponse500 | UpdateApiKeyExpirationResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
