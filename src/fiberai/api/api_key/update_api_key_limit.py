from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_api_key_limit_body import UpdateApiKeyLimitBody
from ...models.update_api_key_limit_response_200 import UpdateApiKeyLimitResponse200
from ...models.update_api_key_limit_response_400 import UpdateApiKeyLimitResponse400
from ...models.update_api_key_limit_response_401 import UpdateApiKeyLimitResponse401
from ...models.update_api_key_limit_response_402 import UpdateApiKeyLimitResponse402
from ...models.update_api_key_limit_response_403 import UpdateApiKeyLimitResponse403
from ...models.update_api_key_limit_response_404 import UpdateApiKeyLimitResponse404
from ...models.update_api_key_limit_response_422 import UpdateApiKeyLimitResponse422
from ...models.update_api_key_limit_response_429 import UpdateApiKeyLimitResponse429
from ...models.update_api_key_limit_response_500 import UpdateApiKeyLimitResponse500
from ...models.update_api_key_limit_response_503 import UpdateApiKeyLimitResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateApiKeyLimitBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/api-keys/limit",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    UpdateApiKeyLimitResponse200
    | UpdateApiKeyLimitResponse400
    | UpdateApiKeyLimitResponse401
    | UpdateApiKeyLimitResponse402
    | UpdateApiKeyLimitResponse403
    | UpdateApiKeyLimitResponse404
    | UpdateApiKeyLimitResponse422
    | UpdateApiKeyLimitResponse429
    | UpdateApiKeyLimitResponse500
    | UpdateApiKeyLimitResponse503
    | None
):
    if response.status_code == 200:
        response_200 = UpdateApiKeyLimitResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateApiKeyLimitResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateApiKeyLimitResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = UpdateApiKeyLimitResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = UpdateApiKeyLimitResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateApiKeyLimitResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = UpdateApiKeyLimitResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = UpdateApiKeyLimitResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = UpdateApiKeyLimitResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = UpdateApiKeyLimitResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UpdateApiKeyLimitResponse200
    | UpdateApiKeyLimitResponse400
    | UpdateApiKeyLimitResponse401
    | UpdateApiKeyLimitResponse402
    | UpdateApiKeyLimitResponse403
    | UpdateApiKeyLimitResponse404
    | UpdateApiKeyLimitResponse422
    | UpdateApiKeyLimitResponse429
    | UpdateApiKeyLimitResponse500
    | UpdateApiKeyLimitResponse503
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
    body: UpdateApiKeyLimitBody,
) -> Response[
    UpdateApiKeyLimitResponse200
    | UpdateApiKeyLimitResponse400
    | UpdateApiKeyLimitResponse401
    | UpdateApiKeyLimitResponse402
    | UpdateApiKeyLimitResponse403
    | UpdateApiKeyLimitResponse404
    | UpdateApiKeyLimitResponse422
    | UpdateApiKeyLimitResponse429
    | UpdateApiKeyLimitResponse500
    | UpdateApiKeyLimitResponse503
]:
    """Update API key credit limit

     Change the lifetime credit ceiling of an API key. Acts on the key that authenticates this request
    unless target is OTHER. Use set to pin an absolute limit, increase or decrease to adjust it by a
    number of credits, multiply or divide to scale it, or remove to make the key unlimited. Once a key's
    usage reaches its limit it can no longer authenticate until the limit is raised or removed.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (UpdateApiKeyLimitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateApiKeyLimitResponse200 | UpdateApiKeyLimitResponse400 | UpdateApiKeyLimitResponse401 | UpdateApiKeyLimitResponse402 | UpdateApiKeyLimitResponse403 | UpdateApiKeyLimitResponse404 | UpdateApiKeyLimitResponse422 | UpdateApiKeyLimitResponse429 | UpdateApiKeyLimitResponse500 | UpdateApiKeyLimitResponse503]
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
    body: UpdateApiKeyLimitBody,
) -> (
    UpdateApiKeyLimitResponse200
    | UpdateApiKeyLimitResponse400
    | UpdateApiKeyLimitResponse401
    | UpdateApiKeyLimitResponse402
    | UpdateApiKeyLimitResponse403
    | UpdateApiKeyLimitResponse404
    | UpdateApiKeyLimitResponse422
    | UpdateApiKeyLimitResponse429
    | UpdateApiKeyLimitResponse500
    | UpdateApiKeyLimitResponse503
    | None
):
    """Update API key credit limit

     Change the lifetime credit ceiling of an API key. Acts on the key that authenticates this request
    unless target is OTHER. Use set to pin an absolute limit, increase or decrease to adjust it by a
    number of credits, multiply or divide to scale it, or remove to make the key unlimited. Once a key's
    usage reaches its limit it can no longer authenticate until the limit is raised or removed.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (UpdateApiKeyLimitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateApiKeyLimitResponse200 | UpdateApiKeyLimitResponse400 | UpdateApiKeyLimitResponse401 | UpdateApiKeyLimitResponse402 | UpdateApiKeyLimitResponse403 | UpdateApiKeyLimitResponse404 | UpdateApiKeyLimitResponse422 | UpdateApiKeyLimitResponse429 | UpdateApiKeyLimitResponse500 | UpdateApiKeyLimitResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateApiKeyLimitBody,
) -> Response[
    UpdateApiKeyLimitResponse200
    | UpdateApiKeyLimitResponse400
    | UpdateApiKeyLimitResponse401
    | UpdateApiKeyLimitResponse402
    | UpdateApiKeyLimitResponse403
    | UpdateApiKeyLimitResponse404
    | UpdateApiKeyLimitResponse422
    | UpdateApiKeyLimitResponse429
    | UpdateApiKeyLimitResponse500
    | UpdateApiKeyLimitResponse503
]:
    """Update API key credit limit

     Change the lifetime credit ceiling of an API key. Acts on the key that authenticates this request
    unless target is OTHER. Use set to pin an absolute limit, increase or decrease to adjust it by a
    number of credits, multiply or divide to scale it, or remove to make the key unlimited. Once a key's
    usage reaches its limit it can no longer authenticate until the limit is raised or removed.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (UpdateApiKeyLimitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateApiKeyLimitResponse200 | UpdateApiKeyLimitResponse400 | UpdateApiKeyLimitResponse401 | UpdateApiKeyLimitResponse402 | UpdateApiKeyLimitResponse403 | UpdateApiKeyLimitResponse404 | UpdateApiKeyLimitResponse422 | UpdateApiKeyLimitResponse429 | UpdateApiKeyLimitResponse500 | UpdateApiKeyLimitResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateApiKeyLimitBody,
) -> (
    UpdateApiKeyLimitResponse200
    | UpdateApiKeyLimitResponse400
    | UpdateApiKeyLimitResponse401
    | UpdateApiKeyLimitResponse402
    | UpdateApiKeyLimitResponse403
    | UpdateApiKeyLimitResponse404
    | UpdateApiKeyLimitResponse422
    | UpdateApiKeyLimitResponse429
    | UpdateApiKeyLimitResponse500
    | UpdateApiKeyLimitResponse503
    | None
):
    """Update API key credit limit

     Change the lifetime credit ceiling of an API key. Acts on the key that authenticates this request
    unless target is OTHER. Use set to pin an absolute limit, increase or decrease to adjust it by a
    number of credits, multiply or divide to scale it, or remove to make the key unlimited. Once a key's
    usage reaches its limit it can no longer authenticate until the limit is raised or removed.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (UpdateApiKeyLimitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateApiKeyLimitResponse200 | UpdateApiKeyLimitResponse400 | UpdateApiKeyLimitResponse401 | UpdateApiKeyLimitResponse402 | UpdateApiKeyLimitResponse403 | UpdateApiKeyLimitResponse404 | UpdateApiKeyLimitResponse422 | UpdateApiKeyLimitResponse429 | UpdateApiKeyLimitResponse500 | UpdateApiKeyLimitResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
