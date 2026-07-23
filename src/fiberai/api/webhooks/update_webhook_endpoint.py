from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_webhook_endpoint_body import UpdateWebhookEndpointBody
from ...models.update_webhook_endpoint_response_200 import UpdateWebhookEndpointResponse200
from ...models.update_webhook_endpoint_response_400 import UpdateWebhookEndpointResponse400
from ...models.update_webhook_endpoint_response_401 import UpdateWebhookEndpointResponse401
from ...models.update_webhook_endpoint_response_402 import UpdateWebhookEndpointResponse402
from ...models.update_webhook_endpoint_response_403 import UpdateWebhookEndpointResponse403
from ...models.update_webhook_endpoint_response_404 import UpdateWebhookEndpointResponse404
from ...models.update_webhook_endpoint_response_422 import UpdateWebhookEndpointResponse422
from ...models.update_webhook_endpoint_response_429 import UpdateWebhookEndpointResponse429
from ...models.update_webhook_endpoint_response_500 import UpdateWebhookEndpointResponse500
from ...models.update_webhook_endpoint_response_503 import UpdateWebhookEndpointResponse503
from ...types import Response


def _get_kwargs(
    endpoint_id: str,
    *,
    body: UpdateWebhookEndpointBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/webhooks/endpoints/{endpoint_id}".format(
            endpoint_id=quote(str(endpoint_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    UpdateWebhookEndpointResponse200
    | UpdateWebhookEndpointResponse400
    | UpdateWebhookEndpointResponse401
    | UpdateWebhookEndpointResponse402
    | UpdateWebhookEndpointResponse403
    | UpdateWebhookEndpointResponse404
    | UpdateWebhookEndpointResponse422
    | UpdateWebhookEndpointResponse429
    | UpdateWebhookEndpointResponse500
    | UpdateWebhookEndpointResponse503
    | None
):
    if response.status_code == 200:
        response_200 = UpdateWebhookEndpointResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateWebhookEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateWebhookEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = UpdateWebhookEndpointResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = UpdateWebhookEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateWebhookEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = UpdateWebhookEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = UpdateWebhookEndpointResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = UpdateWebhookEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = UpdateWebhookEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UpdateWebhookEndpointResponse200
    | UpdateWebhookEndpointResponse400
    | UpdateWebhookEndpointResponse401
    | UpdateWebhookEndpointResponse402
    | UpdateWebhookEndpointResponse403
    | UpdateWebhookEndpointResponse404
    | UpdateWebhookEndpointResponse422
    | UpdateWebhookEndpointResponse429
    | UpdateWebhookEndpointResponse500
    | UpdateWebhookEndpointResponse503
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
    body: UpdateWebhookEndpointBody,
) -> Response[
    UpdateWebhookEndpointResponse200
    | UpdateWebhookEndpointResponse400
    | UpdateWebhookEndpointResponse401
    | UpdateWebhookEndpointResponse402
    | UpdateWebhookEndpointResponse403
    | UpdateWebhookEndpointResponse404
    | UpdateWebhookEndpointResponse422
    | UpdateWebhookEndpointResponse429
    | UpdateWebhookEndpointResponse500
    | UpdateWebhookEndpointResponse503
]:
    r"""Update webhook endpoint

     Update a webhook endpoint. Change its URL, replace the event types it is subscribed to, update its
    description, or pause and resume delivery. Only the fields you provide are changed. Updating
    webhooks is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        endpoint_id (str):
        body (UpdateWebhookEndpointBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateWebhookEndpointResponse200 | UpdateWebhookEndpointResponse400 | UpdateWebhookEndpointResponse401 | UpdateWebhookEndpointResponse402 | UpdateWebhookEndpointResponse403 | UpdateWebhookEndpointResponse404 | UpdateWebhookEndpointResponse422 | UpdateWebhookEndpointResponse429 | UpdateWebhookEndpointResponse500 | UpdateWebhookEndpointResponse503]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateWebhookEndpointBody,
) -> (
    UpdateWebhookEndpointResponse200
    | UpdateWebhookEndpointResponse400
    | UpdateWebhookEndpointResponse401
    | UpdateWebhookEndpointResponse402
    | UpdateWebhookEndpointResponse403
    | UpdateWebhookEndpointResponse404
    | UpdateWebhookEndpointResponse422
    | UpdateWebhookEndpointResponse429
    | UpdateWebhookEndpointResponse500
    | UpdateWebhookEndpointResponse503
    | None
):
    r"""Update webhook endpoint

     Update a webhook endpoint. Change its URL, replace the event types it is subscribed to, update its
    description, or pause and resume delivery. Only the fields you provide are changed. Updating
    webhooks is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        endpoint_id (str):
        body (UpdateWebhookEndpointBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateWebhookEndpointResponse200 | UpdateWebhookEndpointResponse400 | UpdateWebhookEndpointResponse401 | UpdateWebhookEndpointResponse402 | UpdateWebhookEndpointResponse403 | UpdateWebhookEndpointResponse404 | UpdateWebhookEndpointResponse422 | UpdateWebhookEndpointResponse429 | UpdateWebhookEndpointResponse500 | UpdateWebhookEndpointResponse503
    """

    return sync_detailed(
        endpoint_id=endpoint_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateWebhookEndpointBody,
) -> Response[
    UpdateWebhookEndpointResponse200
    | UpdateWebhookEndpointResponse400
    | UpdateWebhookEndpointResponse401
    | UpdateWebhookEndpointResponse402
    | UpdateWebhookEndpointResponse403
    | UpdateWebhookEndpointResponse404
    | UpdateWebhookEndpointResponse422
    | UpdateWebhookEndpointResponse429
    | UpdateWebhookEndpointResponse500
    | UpdateWebhookEndpointResponse503
]:
    r"""Update webhook endpoint

     Update a webhook endpoint. Change its URL, replace the event types it is subscribed to, update its
    description, or pause and resume delivery. Only the fields you provide are changed. Updating
    webhooks is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        endpoint_id (str):
        body (UpdateWebhookEndpointBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateWebhookEndpointResponse200 | UpdateWebhookEndpointResponse400 | UpdateWebhookEndpointResponse401 | UpdateWebhookEndpointResponse402 | UpdateWebhookEndpointResponse403 | UpdateWebhookEndpointResponse404 | UpdateWebhookEndpointResponse422 | UpdateWebhookEndpointResponse429 | UpdateWebhookEndpointResponse500 | UpdateWebhookEndpointResponse503]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateWebhookEndpointBody,
) -> (
    UpdateWebhookEndpointResponse200
    | UpdateWebhookEndpointResponse400
    | UpdateWebhookEndpointResponse401
    | UpdateWebhookEndpointResponse402
    | UpdateWebhookEndpointResponse403
    | UpdateWebhookEndpointResponse404
    | UpdateWebhookEndpointResponse422
    | UpdateWebhookEndpointResponse429
    | UpdateWebhookEndpointResponse500
    | UpdateWebhookEndpointResponse503
    | None
):
    r"""Update webhook endpoint

     Update a webhook endpoint. Change its URL, replace the event types it is subscribed to, update its
    description, or pause and resume delivery. Only the fields you provide are changed. Updating
    webhooks is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        endpoint_id (str):
        body (UpdateWebhookEndpointBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateWebhookEndpointResponse200 | UpdateWebhookEndpointResponse400 | UpdateWebhookEndpointResponse401 | UpdateWebhookEndpointResponse402 | UpdateWebhookEndpointResponse403 | UpdateWebhookEndpointResponse404 | UpdateWebhookEndpointResponse422 | UpdateWebhookEndpointResponse429 | UpdateWebhookEndpointResponse500 | UpdateWebhookEndpointResponse503
    """

    return (
        await asyncio_detailed(
            endpoint_id=endpoint_id,
            client=client,
            body=body,
        )
    ).parsed
