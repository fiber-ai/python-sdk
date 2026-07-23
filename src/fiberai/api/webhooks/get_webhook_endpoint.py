from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_webhook_endpoint_response_200 import GetWebhookEndpointResponse200
from ...models.get_webhook_endpoint_response_400 import GetWebhookEndpointResponse400
from ...models.get_webhook_endpoint_response_401 import GetWebhookEndpointResponse401
from ...models.get_webhook_endpoint_response_402 import GetWebhookEndpointResponse402
from ...models.get_webhook_endpoint_response_403 import GetWebhookEndpointResponse403
from ...models.get_webhook_endpoint_response_404 import GetWebhookEndpointResponse404
from ...models.get_webhook_endpoint_response_422 import GetWebhookEndpointResponse422
from ...models.get_webhook_endpoint_response_429 import GetWebhookEndpointResponse429
from ...models.get_webhook_endpoint_response_500 import GetWebhookEndpointResponse500
from ...models.get_webhook_endpoint_response_503 import GetWebhookEndpointResponse503
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
        "method": "get",
        "url": "/v1/webhooks/endpoints/{endpoint_id}".format(
            endpoint_id=quote(str(endpoint_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetWebhookEndpointResponse200
    | GetWebhookEndpointResponse400
    | GetWebhookEndpointResponse401
    | GetWebhookEndpointResponse402
    | GetWebhookEndpointResponse403
    | GetWebhookEndpointResponse404
    | GetWebhookEndpointResponse422
    | GetWebhookEndpointResponse429
    | GetWebhookEndpointResponse500
    | GetWebhookEndpointResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetWebhookEndpointResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetWebhookEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetWebhookEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetWebhookEndpointResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetWebhookEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetWebhookEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetWebhookEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetWebhookEndpointResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetWebhookEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetWebhookEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetWebhookEndpointResponse200
    | GetWebhookEndpointResponse400
    | GetWebhookEndpointResponse401
    | GetWebhookEndpointResponse402
    | GetWebhookEndpointResponse403
    | GetWebhookEndpointResponse404
    | GetWebhookEndpointResponse422
    | GetWebhookEndpointResponse429
    | GetWebhookEndpointResponse500
    | GetWebhookEndpointResponse503
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
    GetWebhookEndpointResponse200
    | GetWebhookEndpointResponse400
    | GetWebhookEndpointResponse401
    | GetWebhookEndpointResponse402
    | GetWebhookEndpointResponse403
    | GetWebhookEndpointResponse404
    | GetWebhookEndpointResponse422
    | GetWebhookEndpointResponse429
    | GetWebhookEndpointResponse500
    | GetWebhookEndpointResponse503
]:
    r"""Get webhook endpoint

     Return a single webhook endpoint's configuration: its delivery URL, the event types it is subscribed
    to, and whether delivery is currently paused. Reading webhook endpoints is free.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        endpoint_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWebhookEndpointResponse200 | GetWebhookEndpointResponse400 | GetWebhookEndpointResponse401 | GetWebhookEndpointResponse402 | GetWebhookEndpointResponse403 | GetWebhookEndpointResponse404 | GetWebhookEndpointResponse422 | GetWebhookEndpointResponse429 | GetWebhookEndpointResponse500 | GetWebhookEndpointResponse503]
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
    GetWebhookEndpointResponse200
    | GetWebhookEndpointResponse400
    | GetWebhookEndpointResponse401
    | GetWebhookEndpointResponse402
    | GetWebhookEndpointResponse403
    | GetWebhookEndpointResponse404
    | GetWebhookEndpointResponse422
    | GetWebhookEndpointResponse429
    | GetWebhookEndpointResponse500
    | GetWebhookEndpointResponse503
    | None
):
    r"""Get webhook endpoint

     Return a single webhook endpoint's configuration: its delivery URL, the event types it is subscribed
    to, and whether delivery is currently paused. Reading webhook endpoints is free.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        endpoint_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWebhookEndpointResponse200 | GetWebhookEndpointResponse400 | GetWebhookEndpointResponse401 | GetWebhookEndpointResponse402 | GetWebhookEndpointResponse403 | GetWebhookEndpointResponse404 | GetWebhookEndpointResponse422 | GetWebhookEndpointResponse429 | GetWebhookEndpointResponse500 | GetWebhookEndpointResponse503
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
    GetWebhookEndpointResponse200
    | GetWebhookEndpointResponse400
    | GetWebhookEndpointResponse401
    | GetWebhookEndpointResponse402
    | GetWebhookEndpointResponse403
    | GetWebhookEndpointResponse404
    | GetWebhookEndpointResponse422
    | GetWebhookEndpointResponse429
    | GetWebhookEndpointResponse500
    | GetWebhookEndpointResponse503
]:
    r"""Get webhook endpoint

     Return a single webhook endpoint's configuration: its delivery URL, the event types it is subscribed
    to, and whether delivery is currently paused. Reading webhook endpoints is free.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        endpoint_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWebhookEndpointResponse200 | GetWebhookEndpointResponse400 | GetWebhookEndpointResponse401 | GetWebhookEndpointResponse402 | GetWebhookEndpointResponse403 | GetWebhookEndpointResponse404 | GetWebhookEndpointResponse422 | GetWebhookEndpointResponse429 | GetWebhookEndpointResponse500 | GetWebhookEndpointResponse503]
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
    GetWebhookEndpointResponse200
    | GetWebhookEndpointResponse400
    | GetWebhookEndpointResponse401
    | GetWebhookEndpointResponse402
    | GetWebhookEndpointResponse403
    | GetWebhookEndpointResponse404
    | GetWebhookEndpointResponse422
    | GetWebhookEndpointResponse429
    | GetWebhookEndpointResponse500
    | GetWebhookEndpointResponse503
    | None
):
    r"""Get webhook endpoint

     Return a single webhook endpoint's configuration: its delivery URL, the event types it is subscribed
    to, and whether delivery is currently paused. Reading webhook endpoints is free.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        endpoint_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWebhookEndpointResponse200 | GetWebhookEndpointResponse400 | GetWebhookEndpointResponse401 | GetWebhookEndpointResponse402 | GetWebhookEndpointResponse403 | GetWebhookEndpointResponse404 | GetWebhookEndpointResponse422 | GetWebhookEndpointResponse429 | GetWebhookEndpointResponse500 | GetWebhookEndpointResponse503
    """

    return (
        await asyncio_detailed(
            endpoint_id=endpoint_id,
            client=client,
            api_key=api_key,
        )
    ).parsed
