from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.revoke_current_api_key_body import RevokeCurrentApiKeyBody
from ...models.revoke_current_api_key_response_200 import RevokeCurrentApiKeyResponse200
from ...models.revoke_current_api_key_response_400 import RevokeCurrentApiKeyResponse400
from ...models.revoke_current_api_key_response_401 import RevokeCurrentApiKeyResponse401
from ...models.revoke_current_api_key_response_402 import RevokeCurrentApiKeyResponse402
from ...models.revoke_current_api_key_response_403 import RevokeCurrentApiKeyResponse403
from ...models.revoke_current_api_key_response_404 import RevokeCurrentApiKeyResponse404
from ...models.revoke_current_api_key_response_422 import RevokeCurrentApiKeyResponse422
from ...models.revoke_current_api_key_response_429 import RevokeCurrentApiKeyResponse429
from ...models.revoke_current_api_key_response_500 import RevokeCurrentApiKeyResponse500
from ...models.revoke_current_api_key_response_503 import RevokeCurrentApiKeyResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: RevokeCurrentApiKeyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/api-keys/revoke",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RevokeCurrentApiKeyResponse200
    | RevokeCurrentApiKeyResponse400
    | RevokeCurrentApiKeyResponse401
    | RevokeCurrentApiKeyResponse402
    | RevokeCurrentApiKeyResponse403
    | RevokeCurrentApiKeyResponse404
    | RevokeCurrentApiKeyResponse422
    | RevokeCurrentApiKeyResponse429
    | RevokeCurrentApiKeyResponse500
    | RevokeCurrentApiKeyResponse503
    | None
):
    if response.status_code == 200:
        response_200 = RevokeCurrentApiKeyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RevokeCurrentApiKeyResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RevokeCurrentApiKeyResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = RevokeCurrentApiKeyResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = RevokeCurrentApiKeyResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RevokeCurrentApiKeyResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = RevokeCurrentApiKeyResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = RevokeCurrentApiKeyResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RevokeCurrentApiKeyResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RevokeCurrentApiKeyResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RevokeCurrentApiKeyResponse200
    | RevokeCurrentApiKeyResponse400
    | RevokeCurrentApiKeyResponse401
    | RevokeCurrentApiKeyResponse402
    | RevokeCurrentApiKeyResponse403
    | RevokeCurrentApiKeyResponse404
    | RevokeCurrentApiKeyResponse422
    | RevokeCurrentApiKeyResponse429
    | RevokeCurrentApiKeyResponse500
    | RevokeCurrentApiKeyResponse503
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
    body: RevokeCurrentApiKeyBody,
) -> Response[
    RevokeCurrentApiKeyResponse200
    | RevokeCurrentApiKeyResponse400
    | RevokeCurrentApiKeyResponse401
    | RevokeCurrentApiKeyResponse402
    | RevokeCurrentApiKeyResponse403
    | RevokeCurrentApiKeyResponse404
    | RevokeCurrentApiKeyResponse422
    | RevokeCurrentApiKeyResponse429
    | RevokeCurrentApiKeyResponse500
    | RevokeCurrentApiKeyResponse503
]:
    """Revoke API key

     Permanently revoke an API key. Acts on the key that authenticates this request unless target is
    OTHER. The key stops working immediately and cannot be restored. Create a replacement sandbox key
    via POST /v1/api-keys/create-sandbox, or a live key from the dashboard, before revoking a key that
    is still in use. First-time users: create your initial API key at https://app.fiber.ai or via POST
    /v1/account/send-otp + verify-otp. This endpoint manages keys once you have one.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (RevokeCurrentApiKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RevokeCurrentApiKeyResponse200 | RevokeCurrentApiKeyResponse400 | RevokeCurrentApiKeyResponse401 | RevokeCurrentApiKeyResponse402 | RevokeCurrentApiKeyResponse403 | RevokeCurrentApiKeyResponse404 | RevokeCurrentApiKeyResponse422 | RevokeCurrentApiKeyResponse429 | RevokeCurrentApiKeyResponse500 | RevokeCurrentApiKeyResponse503]
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
    body: RevokeCurrentApiKeyBody,
) -> (
    RevokeCurrentApiKeyResponse200
    | RevokeCurrentApiKeyResponse400
    | RevokeCurrentApiKeyResponse401
    | RevokeCurrentApiKeyResponse402
    | RevokeCurrentApiKeyResponse403
    | RevokeCurrentApiKeyResponse404
    | RevokeCurrentApiKeyResponse422
    | RevokeCurrentApiKeyResponse429
    | RevokeCurrentApiKeyResponse500
    | RevokeCurrentApiKeyResponse503
    | None
):
    """Revoke API key

     Permanently revoke an API key. Acts on the key that authenticates this request unless target is
    OTHER. The key stops working immediately and cannot be restored. Create a replacement sandbox key
    via POST /v1/api-keys/create-sandbox, or a live key from the dashboard, before revoking a key that
    is still in use. First-time users: create your initial API key at https://app.fiber.ai or via POST
    /v1/account/send-otp + verify-otp. This endpoint manages keys once you have one.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (RevokeCurrentApiKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RevokeCurrentApiKeyResponse200 | RevokeCurrentApiKeyResponse400 | RevokeCurrentApiKeyResponse401 | RevokeCurrentApiKeyResponse402 | RevokeCurrentApiKeyResponse403 | RevokeCurrentApiKeyResponse404 | RevokeCurrentApiKeyResponse422 | RevokeCurrentApiKeyResponse429 | RevokeCurrentApiKeyResponse500 | RevokeCurrentApiKeyResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RevokeCurrentApiKeyBody,
) -> Response[
    RevokeCurrentApiKeyResponse200
    | RevokeCurrentApiKeyResponse400
    | RevokeCurrentApiKeyResponse401
    | RevokeCurrentApiKeyResponse402
    | RevokeCurrentApiKeyResponse403
    | RevokeCurrentApiKeyResponse404
    | RevokeCurrentApiKeyResponse422
    | RevokeCurrentApiKeyResponse429
    | RevokeCurrentApiKeyResponse500
    | RevokeCurrentApiKeyResponse503
]:
    """Revoke API key

     Permanently revoke an API key. Acts on the key that authenticates this request unless target is
    OTHER. The key stops working immediately and cannot be restored. Create a replacement sandbox key
    via POST /v1/api-keys/create-sandbox, or a live key from the dashboard, before revoking a key that
    is still in use. First-time users: create your initial API key at https://app.fiber.ai or via POST
    /v1/account/send-otp + verify-otp. This endpoint manages keys once you have one.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (RevokeCurrentApiKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RevokeCurrentApiKeyResponse200 | RevokeCurrentApiKeyResponse400 | RevokeCurrentApiKeyResponse401 | RevokeCurrentApiKeyResponse402 | RevokeCurrentApiKeyResponse403 | RevokeCurrentApiKeyResponse404 | RevokeCurrentApiKeyResponse422 | RevokeCurrentApiKeyResponse429 | RevokeCurrentApiKeyResponse500 | RevokeCurrentApiKeyResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RevokeCurrentApiKeyBody,
) -> (
    RevokeCurrentApiKeyResponse200
    | RevokeCurrentApiKeyResponse400
    | RevokeCurrentApiKeyResponse401
    | RevokeCurrentApiKeyResponse402
    | RevokeCurrentApiKeyResponse403
    | RevokeCurrentApiKeyResponse404
    | RevokeCurrentApiKeyResponse422
    | RevokeCurrentApiKeyResponse429
    | RevokeCurrentApiKeyResponse500
    | RevokeCurrentApiKeyResponse503
    | None
):
    """Revoke API key

     Permanently revoke an API key. Acts on the key that authenticates this request unless target is
    OTHER. The key stops working immediately and cannot be restored. Create a replacement sandbox key
    via POST /v1/api-keys/create-sandbox, or a live key from the dashboard, before revoking a key that
    is still in use. First-time users: create your initial API key at https://app.fiber.ai or via POST
    /v1/account/send-otp + verify-otp. This endpoint manages keys once you have one.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (RevokeCurrentApiKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RevokeCurrentApiKeyResponse200 | RevokeCurrentApiKeyResponse400 | RevokeCurrentApiKeyResponse401 | RevokeCurrentApiKeyResponse402 | RevokeCurrentApiKeyResponse403 | RevokeCurrentApiKeyResponse404 | RevokeCurrentApiKeyResponse422 | RevokeCurrentApiKeyResponse429 | RevokeCurrentApiKeyResponse500 | RevokeCurrentApiKeyResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
