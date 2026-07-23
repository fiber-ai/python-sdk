from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rotate_webhook_endpoint_secret_body import RotateWebhookEndpointSecretBody
from ...models.rotate_webhook_endpoint_secret_response_200 import RotateWebhookEndpointSecretResponse200
from ...models.rotate_webhook_endpoint_secret_response_400 import RotateWebhookEndpointSecretResponse400
from ...models.rotate_webhook_endpoint_secret_response_401 import RotateWebhookEndpointSecretResponse401
from ...models.rotate_webhook_endpoint_secret_response_402 import RotateWebhookEndpointSecretResponse402
from ...models.rotate_webhook_endpoint_secret_response_403 import RotateWebhookEndpointSecretResponse403
from ...models.rotate_webhook_endpoint_secret_response_404 import RotateWebhookEndpointSecretResponse404
from ...models.rotate_webhook_endpoint_secret_response_422 import RotateWebhookEndpointSecretResponse422
from ...models.rotate_webhook_endpoint_secret_response_429 import RotateWebhookEndpointSecretResponse429
from ...models.rotate_webhook_endpoint_secret_response_500 import RotateWebhookEndpointSecretResponse500
from ...models.rotate_webhook_endpoint_secret_response_503 import RotateWebhookEndpointSecretResponse503
from ...types import Response


def _get_kwargs(
    endpoint_id: str,
    *,
    body: RotateWebhookEndpointSecretBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/webhooks/endpoints/{endpoint_id}/rotate-secret".format(
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
    RotateWebhookEndpointSecretResponse200
    | RotateWebhookEndpointSecretResponse400
    | RotateWebhookEndpointSecretResponse401
    | RotateWebhookEndpointSecretResponse402
    | RotateWebhookEndpointSecretResponse403
    | RotateWebhookEndpointSecretResponse404
    | RotateWebhookEndpointSecretResponse422
    | RotateWebhookEndpointSecretResponse429
    | RotateWebhookEndpointSecretResponse500
    | RotateWebhookEndpointSecretResponse503
    | None
):
    if response.status_code == 200:
        response_200 = RotateWebhookEndpointSecretResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RotateWebhookEndpointSecretResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RotateWebhookEndpointSecretResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = RotateWebhookEndpointSecretResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = RotateWebhookEndpointSecretResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RotateWebhookEndpointSecretResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = RotateWebhookEndpointSecretResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = RotateWebhookEndpointSecretResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RotateWebhookEndpointSecretResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RotateWebhookEndpointSecretResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RotateWebhookEndpointSecretResponse200
    | RotateWebhookEndpointSecretResponse400
    | RotateWebhookEndpointSecretResponse401
    | RotateWebhookEndpointSecretResponse402
    | RotateWebhookEndpointSecretResponse403
    | RotateWebhookEndpointSecretResponse404
    | RotateWebhookEndpointSecretResponse422
    | RotateWebhookEndpointSecretResponse429
    | RotateWebhookEndpointSecretResponse500
    | RotateWebhookEndpointSecretResponse503
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
    body: RotateWebhookEndpointSecretBody,
) -> Response[
    RotateWebhookEndpointSecretResponse200
    | RotateWebhookEndpointSecretResponse400
    | RotateWebhookEndpointSecretResponse401
    | RotateWebhookEndpointSecretResponse402
    | RotateWebhookEndpointSecretResponse403
    | RotateWebhookEndpointSecretResponse404
    | RotateWebhookEndpointSecretResponse422
    | RotateWebhookEndpointSecretResponse429
    | RotateWebhookEndpointSecretResponse500
    | RotateWebhookEndpointSecretResponse503
]:
    r"""Rotate webhook signing secret

     Rotate a webhook endpoint's signing secret and return the new value. The previous secret stays valid
    for a 24-hour grace period so in-flight deliveries keep verifying — roll the new secret out to your
    receiver within that window. Rotating secrets is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        endpoint_id (str):
        body (RotateWebhookEndpointSecretBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RotateWebhookEndpointSecretResponse200 | RotateWebhookEndpointSecretResponse400 | RotateWebhookEndpointSecretResponse401 | RotateWebhookEndpointSecretResponse402 | RotateWebhookEndpointSecretResponse403 | RotateWebhookEndpointSecretResponse404 | RotateWebhookEndpointSecretResponse422 | RotateWebhookEndpointSecretResponse429 | RotateWebhookEndpointSecretResponse500 | RotateWebhookEndpointSecretResponse503]
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
    body: RotateWebhookEndpointSecretBody,
) -> (
    RotateWebhookEndpointSecretResponse200
    | RotateWebhookEndpointSecretResponse400
    | RotateWebhookEndpointSecretResponse401
    | RotateWebhookEndpointSecretResponse402
    | RotateWebhookEndpointSecretResponse403
    | RotateWebhookEndpointSecretResponse404
    | RotateWebhookEndpointSecretResponse422
    | RotateWebhookEndpointSecretResponse429
    | RotateWebhookEndpointSecretResponse500
    | RotateWebhookEndpointSecretResponse503
    | None
):
    r"""Rotate webhook signing secret

     Rotate a webhook endpoint's signing secret and return the new value. The previous secret stays valid
    for a 24-hour grace period so in-flight deliveries keep verifying — roll the new secret out to your
    receiver within that window. Rotating secrets is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        endpoint_id (str):
        body (RotateWebhookEndpointSecretBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RotateWebhookEndpointSecretResponse200 | RotateWebhookEndpointSecretResponse400 | RotateWebhookEndpointSecretResponse401 | RotateWebhookEndpointSecretResponse402 | RotateWebhookEndpointSecretResponse403 | RotateWebhookEndpointSecretResponse404 | RotateWebhookEndpointSecretResponse422 | RotateWebhookEndpointSecretResponse429 | RotateWebhookEndpointSecretResponse500 | RotateWebhookEndpointSecretResponse503
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
    body: RotateWebhookEndpointSecretBody,
) -> Response[
    RotateWebhookEndpointSecretResponse200
    | RotateWebhookEndpointSecretResponse400
    | RotateWebhookEndpointSecretResponse401
    | RotateWebhookEndpointSecretResponse402
    | RotateWebhookEndpointSecretResponse403
    | RotateWebhookEndpointSecretResponse404
    | RotateWebhookEndpointSecretResponse422
    | RotateWebhookEndpointSecretResponse429
    | RotateWebhookEndpointSecretResponse500
    | RotateWebhookEndpointSecretResponse503
]:
    r"""Rotate webhook signing secret

     Rotate a webhook endpoint's signing secret and return the new value. The previous secret stays valid
    for a 24-hour grace period so in-flight deliveries keep verifying — roll the new secret out to your
    receiver within that window. Rotating secrets is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        endpoint_id (str):
        body (RotateWebhookEndpointSecretBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RotateWebhookEndpointSecretResponse200 | RotateWebhookEndpointSecretResponse400 | RotateWebhookEndpointSecretResponse401 | RotateWebhookEndpointSecretResponse402 | RotateWebhookEndpointSecretResponse403 | RotateWebhookEndpointSecretResponse404 | RotateWebhookEndpointSecretResponse422 | RotateWebhookEndpointSecretResponse429 | RotateWebhookEndpointSecretResponse500 | RotateWebhookEndpointSecretResponse503]
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
    body: RotateWebhookEndpointSecretBody,
) -> (
    RotateWebhookEndpointSecretResponse200
    | RotateWebhookEndpointSecretResponse400
    | RotateWebhookEndpointSecretResponse401
    | RotateWebhookEndpointSecretResponse402
    | RotateWebhookEndpointSecretResponse403
    | RotateWebhookEndpointSecretResponse404
    | RotateWebhookEndpointSecretResponse422
    | RotateWebhookEndpointSecretResponse429
    | RotateWebhookEndpointSecretResponse500
    | RotateWebhookEndpointSecretResponse503
    | None
):
    r"""Rotate webhook signing secret

     Rotate a webhook endpoint's signing secret and return the new value. The previous secret stays valid
    for a 24-hour grace period so in-flight deliveries keep verifying — roll the new secret out to your
    receiver within that window. Rotating secrets is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        endpoint_id (str):
        body (RotateWebhookEndpointSecretBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RotateWebhookEndpointSecretResponse200 | RotateWebhookEndpointSecretResponse400 | RotateWebhookEndpointSecretResponse401 | RotateWebhookEndpointSecretResponse402 | RotateWebhookEndpointSecretResponse403 | RotateWebhookEndpointSecretResponse404 | RotateWebhookEndpointSecretResponse422 | RotateWebhookEndpointSecretResponse429 | RotateWebhookEndpointSecretResponse500 | RotateWebhookEndpointSecretResponse503
    """

    return (
        await asyncio_detailed(
            endpoint_id=endpoint_id,
            client=client,
            body=body,
        )
    ).parsed
