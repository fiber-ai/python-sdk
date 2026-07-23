from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_webhook_endpoint_response_200 import DeleteWebhookEndpointResponse200
from ...models.delete_webhook_endpoint_response_400 import DeleteWebhookEndpointResponse400
from ...models.delete_webhook_endpoint_response_401 import DeleteWebhookEndpointResponse401
from ...models.delete_webhook_endpoint_response_402 import DeleteWebhookEndpointResponse402
from ...models.delete_webhook_endpoint_response_403 import DeleteWebhookEndpointResponse403
from ...models.delete_webhook_endpoint_response_404 import DeleteWebhookEndpointResponse404
from ...models.delete_webhook_endpoint_response_422 import DeleteWebhookEndpointResponse422
from ...models.delete_webhook_endpoint_response_429 import DeleteWebhookEndpointResponse429
from ...models.delete_webhook_endpoint_response_500 import DeleteWebhookEndpointResponse500
from ...models.delete_webhook_endpoint_response_503 import DeleteWebhookEndpointResponse503
from ...types import UNSET, Response


def _get_kwargs(
    endpoint_id: str,
    *,
    api_key: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["apiKey"] = api_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/webhooks/endpoints/{endpoint_id}".format(
            endpoint_id=quote(str(endpoint_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteWebhookEndpointResponse200
    | DeleteWebhookEndpointResponse400
    | DeleteWebhookEndpointResponse401
    | DeleteWebhookEndpointResponse402
    | DeleteWebhookEndpointResponse403
    | DeleteWebhookEndpointResponse404
    | DeleteWebhookEndpointResponse422
    | DeleteWebhookEndpointResponse429
    | DeleteWebhookEndpointResponse500
    | DeleteWebhookEndpointResponse503
    | None
):
    if response.status_code == 200:
        response_200 = DeleteWebhookEndpointResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteWebhookEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteWebhookEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = DeleteWebhookEndpointResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = DeleteWebhookEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteWebhookEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = DeleteWebhookEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = DeleteWebhookEndpointResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = DeleteWebhookEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteWebhookEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteWebhookEndpointResponse200
    | DeleteWebhookEndpointResponse400
    | DeleteWebhookEndpointResponse401
    | DeleteWebhookEndpointResponse402
    | DeleteWebhookEndpointResponse403
    | DeleteWebhookEndpointResponse404
    | DeleteWebhookEndpointResponse422
    | DeleteWebhookEndpointResponse429
    | DeleteWebhookEndpointResponse500
    | DeleteWebhookEndpointResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> Response[
    DeleteWebhookEndpointResponse200
    | DeleteWebhookEndpointResponse400
    | DeleteWebhookEndpointResponse401
    | DeleteWebhookEndpointResponse402
    | DeleteWebhookEndpointResponse403
    | DeleteWebhookEndpointResponse404
    | DeleteWebhookEndpointResponse422
    | DeleteWebhookEndpointResponse429
    | DeleteWebhookEndpointResponse500
    | DeleteWebhookEndpointResponse503
]:
    r"""Delete webhook endpoint

     Delete a webhook endpoint. All future event deliveries to its URL stop immediately. Deleting
    webhooks is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        endpoint_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWebhookEndpointResponse200 | DeleteWebhookEndpointResponse400 | DeleteWebhookEndpointResponse401 | DeleteWebhookEndpointResponse402 | DeleteWebhookEndpointResponse403 | DeleteWebhookEndpointResponse404 | DeleteWebhookEndpointResponse422 | DeleteWebhookEndpointResponse429 | DeleteWebhookEndpointResponse500 | DeleteWebhookEndpointResponse503]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        api_key=api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> (
    DeleteWebhookEndpointResponse200
    | DeleteWebhookEndpointResponse400
    | DeleteWebhookEndpointResponse401
    | DeleteWebhookEndpointResponse402
    | DeleteWebhookEndpointResponse403
    | DeleteWebhookEndpointResponse404
    | DeleteWebhookEndpointResponse422
    | DeleteWebhookEndpointResponse429
    | DeleteWebhookEndpointResponse500
    | DeleteWebhookEndpointResponse503
    | None
):
    r"""Delete webhook endpoint

     Delete a webhook endpoint. All future event deliveries to its URL stop immediately. Deleting
    webhooks is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        endpoint_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWebhookEndpointResponse200 | DeleteWebhookEndpointResponse400 | DeleteWebhookEndpointResponse401 | DeleteWebhookEndpointResponse402 | DeleteWebhookEndpointResponse403 | DeleteWebhookEndpointResponse404 | DeleteWebhookEndpointResponse422 | DeleteWebhookEndpointResponse429 | DeleteWebhookEndpointResponse500 | DeleteWebhookEndpointResponse503
    """

    return sync_detailed(
        endpoint_id=endpoint_id,
        client=client,
        api_key=api_key,
    ).parsed


async def asyncio_detailed(
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> Response[
    DeleteWebhookEndpointResponse200
    | DeleteWebhookEndpointResponse400
    | DeleteWebhookEndpointResponse401
    | DeleteWebhookEndpointResponse402
    | DeleteWebhookEndpointResponse403
    | DeleteWebhookEndpointResponse404
    | DeleteWebhookEndpointResponse422
    | DeleteWebhookEndpointResponse429
    | DeleteWebhookEndpointResponse500
    | DeleteWebhookEndpointResponse503
]:
    r"""Delete webhook endpoint

     Delete a webhook endpoint. All future event deliveries to its URL stop immediately. Deleting
    webhooks is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        endpoint_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWebhookEndpointResponse200 | DeleteWebhookEndpointResponse400 | DeleteWebhookEndpointResponse401 | DeleteWebhookEndpointResponse402 | DeleteWebhookEndpointResponse403 | DeleteWebhookEndpointResponse404 | DeleteWebhookEndpointResponse422 | DeleteWebhookEndpointResponse429 | DeleteWebhookEndpointResponse500 | DeleteWebhookEndpointResponse503]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> (
    DeleteWebhookEndpointResponse200
    | DeleteWebhookEndpointResponse400
    | DeleteWebhookEndpointResponse401
    | DeleteWebhookEndpointResponse402
    | DeleteWebhookEndpointResponse403
    | DeleteWebhookEndpointResponse404
    | DeleteWebhookEndpointResponse422
    | DeleteWebhookEndpointResponse429
    | DeleteWebhookEndpointResponse500
    | DeleteWebhookEndpointResponse503
    | None
):
    r"""Delete webhook endpoint

     Delete a webhook endpoint. All future event deliveries to its URL stop immediately. Deleting
    webhooks is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        endpoint_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWebhookEndpointResponse200 | DeleteWebhookEndpointResponse400 | DeleteWebhookEndpointResponse401 | DeleteWebhookEndpointResponse402 | DeleteWebhookEndpointResponse403 | DeleteWebhookEndpointResponse404 | DeleteWebhookEndpointResponse422 | DeleteWebhookEndpointResponse429 | DeleteWebhookEndpointResponse500 | DeleteWebhookEndpointResponse503
    """

    return (
        await asyncio_detailed(
            endpoint_id=endpoint_id,
            client=client,
            api_key=api_key,
        )
    ).parsed
