from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_webhook_endpoint_body import CreateWebhookEndpointBody
from ...models.create_webhook_endpoint_response_200 import CreateWebhookEndpointResponse200
from ...models.create_webhook_endpoint_response_400 import CreateWebhookEndpointResponse400
from ...models.create_webhook_endpoint_response_401 import CreateWebhookEndpointResponse401
from ...models.create_webhook_endpoint_response_402 import CreateWebhookEndpointResponse402
from ...models.create_webhook_endpoint_response_403 import CreateWebhookEndpointResponse403
from ...models.create_webhook_endpoint_response_404 import CreateWebhookEndpointResponse404
from ...models.create_webhook_endpoint_response_422 import CreateWebhookEndpointResponse422
from ...models.create_webhook_endpoint_response_429 import CreateWebhookEndpointResponse429
from ...models.create_webhook_endpoint_response_500 import CreateWebhookEndpointResponse500
from ...models.create_webhook_endpoint_response_503 import CreateWebhookEndpointResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: CreateWebhookEndpointBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/webhooks/endpoints",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateWebhookEndpointResponse200
    | CreateWebhookEndpointResponse400
    | CreateWebhookEndpointResponse401
    | CreateWebhookEndpointResponse402
    | CreateWebhookEndpointResponse403
    | CreateWebhookEndpointResponse404
    | CreateWebhookEndpointResponse422
    | CreateWebhookEndpointResponse429
    | CreateWebhookEndpointResponse500
    | CreateWebhookEndpointResponse503
    | None
):
    if response.status_code == 200:
        response_200 = CreateWebhookEndpointResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateWebhookEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateWebhookEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = CreateWebhookEndpointResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = CreateWebhookEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateWebhookEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = CreateWebhookEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = CreateWebhookEndpointResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreateWebhookEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CreateWebhookEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateWebhookEndpointResponse200
    | CreateWebhookEndpointResponse400
    | CreateWebhookEndpointResponse401
    | CreateWebhookEndpointResponse402
    | CreateWebhookEndpointResponse403
    | CreateWebhookEndpointResponse404
    | CreateWebhookEndpointResponse422
    | CreateWebhookEndpointResponse429
    | CreateWebhookEndpointResponse500
    | CreateWebhookEndpointResponse503
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
    body: CreateWebhookEndpointBody,
) -> Response[
    CreateWebhookEndpointResponse200
    | CreateWebhookEndpointResponse400
    | CreateWebhookEndpointResponse401
    | CreateWebhookEndpointResponse402
    | CreateWebhookEndpointResponse403
    | CreateWebhookEndpointResponse404
    | CreateWebhookEndpointResponse422
    | CreateWebhookEndpointResponse429
    | CreateWebhookEndpointResponse500
    | CreateWebhookEndpointResponse503
]:
    r"""Create webhook endpoint

     Create a webhook endpoint that receives event payloads at the URL you provide. Returns the endpoint
    along with its signing secret — store the secret securely, as it is only shown here and when
    rotated. Setting up webhooks is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateWebhookEndpointBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWebhookEndpointResponse200 | CreateWebhookEndpointResponse400 | CreateWebhookEndpointResponse401 | CreateWebhookEndpointResponse402 | CreateWebhookEndpointResponse403 | CreateWebhookEndpointResponse404 | CreateWebhookEndpointResponse422 | CreateWebhookEndpointResponse429 | CreateWebhookEndpointResponse500 | CreateWebhookEndpointResponse503]
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
    body: CreateWebhookEndpointBody,
) -> (
    CreateWebhookEndpointResponse200
    | CreateWebhookEndpointResponse400
    | CreateWebhookEndpointResponse401
    | CreateWebhookEndpointResponse402
    | CreateWebhookEndpointResponse403
    | CreateWebhookEndpointResponse404
    | CreateWebhookEndpointResponse422
    | CreateWebhookEndpointResponse429
    | CreateWebhookEndpointResponse500
    | CreateWebhookEndpointResponse503
    | None
):
    r"""Create webhook endpoint

     Create a webhook endpoint that receives event payloads at the URL you provide. Returns the endpoint
    along with its signing secret — store the secret securely, as it is only shown here and when
    rotated. Setting up webhooks is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateWebhookEndpointBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWebhookEndpointResponse200 | CreateWebhookEndpointResponse400 | CreateWebhookEndpointResponse401 | CreateWebhookEndpointResponse402 | CreateWebhookEndpointResponse403 | CreateWebhookEndpointResponse404 | CreateWebhookEndpointResponse422 | CreateWebhookEndpointResponse429 | CreateWebhookEndpointResponse500 | CreateWebhookEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateWebhookEndpointBody,
) -> Response[
    CreateWebhookEndpointResponse200
    | CreateWebhookEndpointResponse400
    | CreateWebhookEndpointResponse401
    | CreateWebhookEndpointResponse402
    | CreateWebhookEndpointResponse403
    | CreateWebhookEndpointResponse404
    | CreateWebhookEndpointResponse422
    | CreateWebhookEndpointResponse429
    | CreateWebhookEndpointResponse500
    | CreateWebhookEndpointResponse503
]:
    r"""Create webhook endpoint

     Create a webhook endpoint that receives event payloads at the URL you provide. Returns the endpoint
    along with its signing secret — store the secret securely, as it is only shown here and when
    rotated. Setting up webhooks is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateWebhookEndpointBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWebhookEndpointResponse200 | CreateWebhookEndpointResponse400 | CreateWebhookEndpointResponse401 | CreateWebhookEndpointResponse402 | CreateWebhookEndpointResponse403 | CreateWebhookEndpointResponse404 | CreateWebhookEndpointResponse422 | CreateWebhookEndpointResponse429 | CreateWebhookEndpointResponse500 | CreateWebhookEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateWebhookEndpointBody,
) -> (
    CreateWebhookEndpointResponse200
    | CreateWebhookEndpointResponse400
    | CreateWebhookEndpointResponse401
    | CreateWebhookEndpointResponse402
    | CreateWebhookEndpointResponse403
    | CreateWebhookEndpointResponse404
    | CreateWebhookEndpointResponse422
    | CreateWebhookEndpointResponse429
    | CreateWebhookEndpointResponse500
    | CreateWebhookEndpointResponse503
    | None
):
    r"""Create webhook endpoint

     Create a webhook endpoint that receives event payloads at the URL you provide. Returns the endpoint
    along with its signing secret — store the secret securely, as it is only shown here and when
    rotated. Setting up webhooks is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateWebhookEndpointBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWebhookEndpointResponse200 | CreateWebhookEndpointResponse400 | CreateWebhookEndpointResponse401 | CreateWebhookEndpointResponse402 | CreateWebhookEndpointResponse403 | CreateWebhookEndpointResponse404 | CreateWebhookEndpointResponse422 | CreateWebhookEndpointResponse429 | CreateWebhookEndpointResponse500 | CreateWebhookEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
